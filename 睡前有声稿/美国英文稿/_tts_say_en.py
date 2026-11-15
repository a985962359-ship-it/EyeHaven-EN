#!/usr/bin/env python3
"""Fallback English TTS via macOS `say` (Samantha) → mp3 into Bundle.

Used when Qwen MPS hangs. Keep voice English-only.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
from pathlib import Path

import lameenc
import numpy as np
import soundfile as sf

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent.parent
CATALOG = REPO / "EyeHaven" / "BedtimeContentCatalog.json"
OUT = ROOT / "_音频"
BUNDLE = REPO / "EyeHaven" / "BedtimeAudioBundle"
MANIFEST = REPO / "EyeHaven" / "BedtimeAudioManifest.json"

VOICE = {
    "Guangguang": "Samantha",
    "Max": "Junior",
    "Mia": "Kathy",
    "Ryan": "Samantha",
}
RATE = "170"


def load_stories() -> list[dict]:
    data = json.loads(CATALOG.read_text(encoding="utf-8"))
    stories = data.get("stories", data) if isinstance(data, dict) else data
    return [s for s in stories if str(s.get("id", "")).startswith("E-")]


def split_safety(text: str) -> list[tuple[str, str]]:
    lines = []
    for raw in text.splitlines():
        line = raw.strip()
        if not line:
            continue
        m = re.match(r"^(Guangguang|Max|Mia)\s*:\s*(.*)$", line)
        if m:
            lines.append((m.group(1), m.group(2).strip()))
        else:
            lines.append(("Guangguang", line))
    return lines


def say_to_wav(text: str, voice: str, path: Path) -> None:
    text = re.sub(r"\s+", " ", text).strip()
    if not text:
        raise ValueError("empty text")
    aiff = path.with_suffix(".aiff")
    subprocess.run(
        ["say", "-v", voice, "-r", RATE, "-o", str(aiff), text],
        check=True,
        timeout=120,
    )
    wav, sr = sf.read(str(aiff), dtype="float32")
    if wav.ndim > 1:
        wav = wav.mean(axis=1)
    sf.write(str(path), wav.astype(np.float32), sr)
    aiff.unlink(missing_ok=True)


def wav_to_mp3(wav_path: Path, mp3_path: Path, bitrate: int = 96) -> None:
    wav, sr = sf.read(str(wav_path), dtype="float32")
    if wav.ndim > 1:
        wav = wav.mean(axis=1)
    pcm = (np.clip(wav, -1, 1) * 32767.0).astype(np.int16)
    enc = lameenc.Encoder()
    enc.set_bit_rate(bitrate)
    enc.set_in_sample_rate(int(sr))
    enc.set_channels(1)
    enc.set_quality(2)
    mp3 = enc.encode(pcm.tobytes()) + enc.flush()
    mp3_path.parent.mkdir(parents=True, exist_ok=True)
    mp3_path.write_bytes(mp3)


def concat_wavs(paths: list[Path], out: Path, gap_sec: float = 0.35) -> None:
    chunks = []
    sr0 = None
    for p in paths:
        w, sr = sf.read(str(p), dtype="float32")
        if w.ndim > 1:
            w = w.mean(axis=1)
        if sr0 is None:
            sr0 = sr
        elif sr != sr0:
            raise ValueError("sr mismatch")
        chunks.append(w.astype(np.float32))
        chunks.append(np.zeros(int(sr0 * gap_sec), dtype=np.float32))
    if chunks:
        chunks.pop()  # trailing gap
    sf.write(str(out), np.concatenate(chunks), int(sr0 or 22050))


def render_body(story: dict, tmp: Path) -> Path:
    sid = story["id"]
    text = story["text"].strip()
    out = tmp / f"{sid}_body.wav"
    if sid.startswith("E-Z"):
        parts = []
        for i, (role, line) in enumerate(split_safety(text)):
            p = tmp / f"{sid}_{i}.wav"
            say_to_wav(line, VOICE.get(role, "Samantha"), p)
            parts.append(p)
        concat_wavs(parts, out)
    else:
        paras = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
        if not paras:
            paras = [text]
        if len(paras) == 1 and len(paras[0]) <= 500:
            say_to_wav(paras[0], VOICE["Ryan"], out)
        else:
            parts = []
            for i, para in enumerate(paras):
                p = tmp / f"{sid}_p{i}.wav"
                say_to_wav(para, VOICE["Ryan"], p)
                parts.append(p)
            concat_wavs(parts, out)
    return out


def render_title(story: dict, tmp: Path) -> Path:
    title = story.get("title", "").strip()
    line = f"Please listen. {title}" if title else "Please listen."
    out = tmp / f"{story['id']}_title.wav"
    say_to_wav(line, VOICE["Ryan"], out)
    return out


def update_manifest(ids: list[str]) -> None:
    if MANIFEST.exists():
        man = json.loads(MANIFEST.read_text(encoding="utf-8"))
    else:
        man = {
            "version": 1,
            "basePath": "bedtime-audio-en",
            "bodies": [],
            "titles": [],
            "notes": "English-only audio manifest.",
        }
    for key in ("bodies", "titles"):
        cur = [x for x in man.get(key, []) if str(x).startswith("E-")]
        for i in ids:
            if str(i).startswith("E-") and i not in cur:
                cur.append(i)
        man[key] = sorted(set(cur))
    man["basePath"] = "bedtime-audio-en"
    MANIFEST.write_text(json.dumps(man, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--only-file")
    ap.add_argument("--skip-existing", action="store_true")
    args = ap.parse_args()

    stories = load_stories()
    if args.only_file:
        want = {ln.strip() for ln in Path(args.only_file).read_text().splitlines() if ln.strip()}
        stories = [s for s in stories if s["id"] in want]

    done: list[str] = []
    tmp = OUT / "_say_tmp"
    tmp.mkdir(parents=True, exist_ok=True)
    for i, story in enumerate(stories, 1):
        sid = story["id"]
        body_mp3 = OUT / f"{sid}.mp3"
        title_mp3 = OUT / "Titles" / f"{sid}.mp3"
        bundle_body = BUNDLE / f"{sid}.mp3"
        bundle_title = BUNDLE / "Titles" / f"{sid}.mp3"
        if args.skip_existing and bundle_body.exists() and bundle_title.exists():
            print(f"[{i}/{len(stories)}] skip {sid}", flush=True)
            done.append(sid)
            continue
        print(f"[{i}/{len(stories)}] {sid} {story.get('title','')}", flush=True)
        try:
            body_wav = render_body(story, tmp)
            wav_to_mp3(body_wav, body_mp3)
            title_wav = render_title(story, tmp)
            wav_to_mp3(title_wav, title_mp3)
            bundle_body.write_bytes(body_mp3.read_bytes())
            bundle_title.parent.mkdir(parents=True, exist_ok=True)
            bundle_title.write_bytes(title_mp3.read_bytes())
            update_manifest([sid])
            done.append(sid)
            print(f"  saved {sid}.mp3 {body_mp3.stat().st_size}", flush=True)
            # Keep tmp small.
            for p in tmp.glob(f"{sid}*"):
                p.unlink(missing_ok=True)
        except Exception as e:
            print(f"  FAIL {sid}: {e}", flush=True)
            continue
    update_manifest(done)
    print(f"DONE {len(done)}/{len(stories)}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
