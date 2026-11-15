#!/usr/bin/env python3
"""英文睡前稿批量配音：阿里千问本机 Ryan/Aiden/Serena。

光光=Ryan，男孩 Max=Aiden，女孩 Mia=Serena。
安全剧场按 Guangguang:/Max:/Mia: 分行；其余整篇 Ryan 旁白。
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

import lameenc
import numpy as np
import soundfile as sf
import torch
from qwen_tts import Qwen3TTSModel

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent.parent
CATALOG = REPO / "EyeHaven" / "BedtimeContentCatalog.en.json"
MODEL = Path("/Users/song/qwen3-tts/models/Qwen3-TTS-12Hz-0.6B-CustomVoice")
OUT = ROOT / "_音频"
BUNDLE = REPO / "EyeHaven" / "BedtimeAudioBundle"
MANIFEST = REPO / "EyeHaven" / "BedtimeAudioManifest.en.json"
PROGRESS = OUT / "_qwen_progress.jsonl"

CAST = {
    "Guangguang": "Ryan",
    "narrator": "Ryan",
    "Max": "Aiden",
    "Mia": "Serena",
}
INSTRUCT = {
    "Ryan": "Speak gently and clearly, like a friendly storyteller for children. No robot effects.",
    "Aiden": "Speak like a curious playful boy, clear and natural.",
    "Serena": "Speak like a warm gentle girl, clear and natural.",
}
GAP_SEC = 0.28
SPEAKER_RE = re.compile(
    r"^(Guangguang|Max|Mia)\s*:\s*(.*)$",
    re.IGNORECASE | re.DOTALL,
)


def load_stories() -> list[dict]:
    data = json.loads(CATALOG.read_text(encoding="utf-8"))
    stories: list[dict] = []

    def walk(o):
        if isinstance(o, dict):
            if str(o.get("id", "")).startswith("E-") and "text" in o:
                stories.append(o)
            for v in o.values():
                walk(v)
        elif isinstance(o, list):
            for v in o:
                walk(v)

    walk(data)
    stories.sort(key=lambda s: s["id"])
    return stories


def split_safety(text: str) -> list[tuple[str, str]]:
    """Return list of (role, line). role in narrator|Guangguang|Max|Mia."""
    parts: list[tuple[str, str]] = []
    buf_narr: list[str] = []
    for raw in text.splitlines():
        line = raw.strip()
        if not line:
            continue
        m = SPEAKER_RE.match(line)
        if m:
            if buf_narr:
                parts.append(("narrator", " ".join(buf_narr).strip()))
                buf_narr = []
            role = m.group(1).capitalize()
            if role.lower() == "guangguang":
                role = "Guangguang"
            elif role.lower() == "max":
                role = "Max"
            elif role.lower() == "mia":
                role = "Mia"
            parts.append((role, m.group(2).strip()))
        else:
            buf_narr.append(line)
    if buf_narr:
        parts.append(("narrator", " ".join(buf_narr).strip()))
    return [(r, t) for r, t in parts if t]


def wav_to_mp3(wav: np.ndarray, sr: int, path: Path, bitrate: int = 96) -> None:
    if wav.ndim > 1:
        wav = wav.mean(axis=1)
    pcm = np.clip(wav, -1.0, 1.0)
    pcm_i16 = (pcm * 32767.0).astype(np.int16)
    enc = lameenc.Encoder()
    enc.set_bit_rate(bitrate)
    enc.set_in_sample_rate(sr)
    enc.set_channels(1)
    enc.set_quality(2)
    mp3 = enc.encode(pcm_i16.tobytes())
    mp3 += enc.flush()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(mp3)


def concat(chunks: list[tuple[np.ndarray, int]], gap: float = GAP_SEC) -> tuple[np.ndarray, int]:
    if not chunks:
        raise ValueError("empty audio")
    sr = chunks[0][1]
    out: list[np.ndarray] = []
    silence = np.zeros(int(sr * gap), dtype=np.float32)
    for i, (w, s) in enumerate(chunks):
        if s != sr:
            raise ValueError(f"sample rate mismatch {s} vs {sr}")
        if w.ndim > 1:
            w = w.mean(axis=1)
        out.append(w.astype(np.float32))
        if i < len(chunks) - 1:
            out.append(silence)
    return np.concatenate(out), sr


class Synth:
    def __init__(self) -> None:
        device = "mps" if torch.backends.mps.is_available() else "cpu"
        print(f"device={device}", flush=True)
        self.model = Qwen3TTSModel.from_pretrained(
            str(MODEL),
            device_map=device,
            dtype=torch.float32,
            attn_implementation="sdpa",
        )
        self.cache: dict[tuple[str, str], tuple[np.ndarray, int]] = {}

    def say(self, speaker: str, text: str) -> tuple[np.ndarray, int]:
        text = re.sub(r"\s+", " ", text).strip()
        if not text:
            raise ValueError("empty text")
        key = (speaker, text)
        if key in self.cache:
            return self.cache[key]
        instruct = INSTRUCT.get(speaker, "")
        last_err: Exception | None = None
        for attempt in range(3):
            try:
                wavs, sr = self.model.generate_custom_voice(
                    text=text,
                    language="English",
                    speaker=speaker,
                    instruct=instruct,
                )
                wav = np.asarray(wavs[0], dtype=np.float32)
                if not np.isfinite(wav).all() or wav.size == 0:
                    raise RuntimeError("non-finite or empty wav")
                self.cache[key] = (wav, int(sr))
                return self.cache[key]
            except Exception as e:
                last_err = e
                print(f"  retry {attempt+1}/3 {speaker}: {e}", flush=True)
                if torch.backends.mps.is_available():
                    torch.mps.empty_cache()
        assert last_err is not None
        raise last_err

    def clear_cache(self) -> None:
        self.cache.clear()
        if torch.backends.mps.is_available():
            torch.mps.empty_cache()


def split_chunks(text: str, max_chars: int = 180) -> list[str]:
    paras = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    if not paras:
        paras = [text.strip()]
    out: list[str] = []
    for p in paras:
        p = re.sub(r"\s+", " ", p).strip()
        if len(p) <= max_chars:
            out.append(p)
            continue
        parts = re.split(r"(?<=[.!?])\s+", p)
        buf = ""
        for part in parts:
            if not part:
                continue
            if buf and len(buf) + 1 + len(part) > max_chars:
                out.append(buf)
                buf = part
            else:
                buf = f"{buf} {part}".strip() if buf else part
        if buf:
            out.append(buf)
    return [c for c in out if c]


def render_body(synth: Synth, story: dict) -> tuple[np.ndarray, int]:
    sid = story["id"]
    text = story["text"].strip()
    if sid.startswith("E-Z"):
        chunks = []
        for role, line in split_safety(text):
            spk = CAST[role]
            print(f"  {role}->{spk}: {line[:60]}", flush=True)
            chunks.append(synth.say(spk, line))
        return concat(chunks)
    parts = split_chunks(text)
    print(f"  narrator->Ryan chunks={len(parts)} chars={len(text)}", flush=True)
    audio = [synth.say("Ryan", p) for p in parts]
    return concat(audio) if len(audio) > 1 else audio[0]


def render_title(synth: Synth, story: dict) -> tuple[np.ndarray, int]:
    title = story.get("title", "").strip()
    line = f"Please listen. {title}" if title else "Please listen."
    return synth.say("Ryan", line)


def update_manifest(ids: list[str]) -> None:
    if MANIFEST.exists():
        man = json.loads(MANIFEST.read_text(encoding="utf-8"))
    else:
        man = {
            "version": 1,
            "basePath": "bedtime-audio-en",
            "bodies": [],
            "titles": [],
            "notes": "English-only audio manifest. Do not mix with Chinese bedtime-audio.",
        }
    for key in ("bodies", "titles"):
        cur = [x for x in man.get(key, []) if str(x).startswith("E-")]
        for i in ids:
            if str(i).startswith("E-") and i not in cur:
                cur.append(i)
        man[key] = sorted(set(cur))
    man["basePath"] = "bedtime-audio-en"
    MANIFEST.write_text(json.dumps(man, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def log_line(obj: dict) -> None:
    PROGRESS.parent.mkdir(parents=True, exist_ok=True)
    with PROGRESS.open("a", encoding="utf-8") as f:
        f.write(json.dumps(obj, ensure_ascii=False) + "\n")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", nargs="*", help="only these story ids")
    ap.add_argument("--only-file", help="text file with one story id per line")
    ap.add_argument("--skip-existing", action="store_true")
    ap.add_argument("--no-bundle", action="store_true")
    ap.add_argument("--no-titles", action="store_true")
    args = ap.parse_args()

    stories = load_stories()
    want = set(args.only or [])
    if args.only_file:
        want |= {ln.strip() for ln in Path(args.only_file).read_text().splitlines() if ln.strip()}
    if want:
        stories = [s for s in stories if s["id"] in want]
    if not stories:
        print("no stories", file=sys.stderr)
        return 1
    if not MODEL.exists():
        print(f"missing model {MODEL}", file=sys.stderr)
        return 1

    synth = Synth()
    done_ids: list[str] = []
    for i, story in enumerate(stories, 1):
        sid = story["id"]
        body_path = OUT / f"{sid}.mp3"
        title_path = OUT / "Titles" / f"{sid}.mp3"
        bundle_body = BUNDLE / f"{sid}.mp3"
        bundle_title = BUNDLE / "Titles" / f"{sid}.mp3"
        have_out = body_path.exists() and (args.no_titles or title_path.exists())
        have_bundle = bundle_body.exists() and (args.no_titles or bundle_title.exists())
        if args.skip_existing and (have_out or have_bundle):
            if have_bundle and not have_out:
                body_path.write_bytes(bundle_body.read_bytes())
                if not args.no_titles and bundle_title.exists():
                    title_path.parent.mkdir(parents=True, exist_ok=True)
                    title_path.write_bytes(bundle_title.read_bytes())
            elif have_out and not args.no_bundle and not have_bundle:
                bundle_body.write_bytes(body_path.read_bytes())
                if not args.no_titles and title_path.exists():
                    bundle_title.parent.mkdir(parents=True, exist_ok=True)
                    bundle_title.write_bytes(title_path.read_bytes())
            print(f"[{i}/{len(stories)}] skip {sid}", flush=True)
            done_ids.append(sid)
            continue
        print(f"[{i}/{len(stories)}] {sid} {story.get('title','')}", flush=True)
        try:
            wav, sr = render_body(synth, story)
            wav_to_mp3(wav, sr, body_path)
            if not args.no_titles:
                tw, tsr = render_title(synth, story)
                wav_to_mp3(tw, tsr, title_path)
            if not args.no_bundle:
                (BUNDLE / f"{sid}.mp3").write_bytes(body_path.read_bytes())
                if not args.no_titles:
                    (BUNDLE / "Titles" / f"{sid}.mp3").write_bytes(title_path.read_bytes())
            log_line({"id": sid, "ok": True, "bytes": body_path.stat().st_size})
            done_ids.append(sid)
            update_manifest([sid])
            print(f"  saved {body_path.name} {body_path.stat().st_size}", flush=True)
            if len(done_ids) % 5 == 0:
                synth.clear_cache()
                print("  cache cleared", flush=True)
        except Exception as e:
            log_line({"id": sid, "ok": False, "error": str(e)})
            print(f"  FAIL {sid}: {e}", flush=True)
            synth.clear_cache()
            continue

    update_manifest(done_ids)
    print(f"DONE {len(done_ids)} stories; manifest updated", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
