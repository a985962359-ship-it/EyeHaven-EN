#!/usr/bin/env python3
"""Record story IDs with VoiceDesign voices matched to who/what speaks.

Rules (2026-11-17 — docs/voice-match-art-casting.md):
  - No blind brand→boy→girl rotation.
  - Default: odd pages brand, even pages companion kid (boy|girl).
  - Optional per-page cast may include mom/dad/animal/sfx when text needs them.
  - Title always brand.

Usage:
  .../python scripts/record_vd_stories.py --only E-W01 E-W02
  .../python scripts/record_vd_stories.py --only E-B05 --companion girl
  .../python scripts/record_vd_stories.py --only E-A02   # uses vd_page_casting.json if present
"""
from __future__ import annotations

import argparse
import json
import shutil
import time
from datetime import datetime
from pathlib import Path

import lameenc
import numpy as np
import soundfile as sf
import torch
from qwen_tts import Qwen3TTSModel

REPO = Path(__file__).resolve().parents[1]
CATALOG = REPO / "EyeHaven" / "BedtimeContentCatalog.en.json"
BUNDLE = REPO / "EyeHaven" / "BedtimeAudioBundle"
MANIFEST = REPO / "EyeHaven" / "BedtimeAudioManifest.en.json"
CASTING_FILE = REPO / "scripts" / "vd_story_companions.json"
PAGE_CAST_FILE = REPO / "scripts" / "vd_page_casting.json"
MODEL = Path("/Users/song/qwen3-tts/models/Qwen3-TTS-12Hz-1.7B-VoiceDesign")
MEDIA = Path(
    "/Users/song/Library/Application Support/Cursor/AgentStores/"
    "cursor_agent_stores/bc-b474c295-0680-491b-a693-72941041732d/files/media/voicedesign-batch"
)

GAP_SEC = 0.28

# Locked: brand / boy / girl. Soft extras for pages that need other people or sounds.
INSTRUCT = {
    "brand": (
        "About 18 years old: young American male teen/young-adult children's storyteller. "
        "Youthful male voice just past puberty—warm, clear, friendly, bedtime-capable but young around 18. "
        "Not a little child, not a deep 30s uncle baritone, not feminine. "
        "Soft mid male pitch, slightly slow, calm and kind. No robot effects."
    ),
    "boy": (
        "Speak as a small schoolboy age ~5–7. High kid-boy pitch, lively playful little boy energy, soft and cute. "
        "Boyish male child—not feminine girl, not 18yo brand narrator, not teen. "
        "Big age contrast vs young adult male. Clear simple English. No robot."
    ),
    "girl": (
        "About 8 years old American girl. Soft gentle warm tender voice (温柔), cozy bedtime feel. "
        "Age clearly around 8—not a toddler, not a teen. Soft higher kid-girl pitch, calm and kind, "
        "cute but soft not sharp. Clear English, no baby lisp, no robot effects."
    ),
    "mom": (
        "Speak as a warm kind American mom about 30–35 reading to a child. Soft gentle female adult voice, "
        "caring and clear, bedtime-friendly. Not a little girl, not teen slang. Natural English. No robot."
    ),
    "dad": (
        "Speak as a warm kind American dad about 30–35. Friendly mid male adult voice, calm and clear, "
        "bedtime-friendly. Not a child, not deep scary baritone. Natural English. No robot."
    ),
    "animal": (
        "Playful children's storyteller doing a short cute animal sound or animal onomatopoeia in English "
        "(purr, meow, woof, chirp). Soft, funny, not scary, not realistic horror. Keep it brief and clear."
    ),
    "sfx": (
        "Playful children's storyteller performing a short sound-effect word for kids "
        "(pop, tap, boom, thump, splash). Soft cartoonish, not loud or scary. Clear and brief."
    ),
}


def default_page_voices(companion: str) -> list[str]:
    c = (companion or "boy").strip().lower()
    if c == "brand":
        return ["brand"] * 12
    kid = "girl" if c == "girl" else "boy"
    return ["brand" if i % 2 == 1 else kid for i in range(1, 13)]


def load_json_map(path: Path) -> dict:
    if not path.exists():
        return {}
    data = json.loads(path.read_text(encoding="utf-8"))
    return {k: v for k, v in data.items() if not str(k).startswith("_")}


def resolve_voices(sid: str, companion: str, page_casts: dict) -> list[str]:
    raw = page_casts.get(sid)
    if isinstance(raw, list) and len(raw) == 12:
        voices = [str(v).lower() for v in raw]
        for v in voices:
            if v not in INSTRUCT:
                raise SystemExit(f"{sid}: unknown voice {v!r}; allowed {sorted(INSTRUCT)}")
        return voices
    return default_page_voices(companion)


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
    sr = chunks[0][1]
    out: list[np.ndarray] = []
    silence = np.zeros(int(sr * gap), dtype=np.float32)
    for i, (w, s) in enumerate(chunks):
        if s != sr:
            raise ValueError("sr mismatch")
        if w.ndim > 1:
            w = w.mean(axis=1)
        out.append(w.astype(np.float32))
        if i < len(chunks) - 1:
            out.append(silence)
    return np.concatenate(out), sr


def update_manifest(ids: list[str]) -> None:
    if not MANIFEST.exists():
        return
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    entries = data.get("files") or data.get("stories") or data
    if isinstance(entries, dict):
        for i in ids:
            entries[i] = {"body": f"{i}.mp3", "title": f"Titles/{i}.mp3"}
    MANIFEST.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def backup_existing(sid: str) -> None:
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    bak_dir = MEDIA / "backup" / stamp
    bak_dir.mkdir(parents=True, exist_ok=True)
    for label, rel in (("body", f"{sid}.mp3"), ("title", f"Titles/{sid}.mp3")):
        src = BUNDLE / rel
        if src.exists():
            shutil.copy2(src, bak_dir / f"{sid}-{label}.mp3")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", nargs="+", required=True)
    ap.add_argument(
        "--companion",
        choices=("boy", "girl", "brand"),
        default=None,
        help="Override companion for all --only ids (else vd_story_companions.json, else boy)",
    )
    args = ap.parse_args()

    stories = {s["id"]: s for s in json.loads(CATALOG.read_text(encoding="utf-8"))["stories"]}
    want = [sid for sid in args.only if sid in stories]
    if not want:
        print("no stories", flush=True)
        return 1
    if not MODEL.exists():
        print("missing model", MODEL, flush=True)
        return 1

    casting = {k: str(v).lower() for k, v in load_json_map(CASTING_FILE).items()}
    page_casts = load_json_map(PAGE_CAST_FILE)
    MEDIA.mkdir(parents=True, exist_ok=True)
    (MEDIA / "segments").mkdir(exist_ok=True)
    (MEDIA / "backup").mkdir(exist_ok=True)

    print("loading VoiceDesign float16 mps", flush=True)
    t0 = time.time()
    model = Qwen3TTSModel.from_pretrained(
        str(MODEL),
        device_map="mps",
        dtype=torch.float16,
        attn_implementation="sdpa",
    )
    print(f"loaded {time.time()-t0:.1f}s", flush=True)

    done: list[str] = []
    for sid in want:
        story = stories[sid]
        pages = [p.strip() for p in story["text"].split("\n\n") if p.strip()]
        if len(pages) != 12:
            print(f"SKIP {sid}: need 12 pages, got {len(pages)}", flush=True)
            continue

        companion = args.companion or casting.get(sid, "boy")
        voices = resolve_voices(sid, companion, page_casts)
        print(f"\n=== {sid} {story['title']} companion={companion} voices={voices} ===", flush=True)
        backup_existing(sid)

        chunks: list[tuple[np.ndarray, int]] = []
        for i, (text, voice) in enumerate(zip(pages, voices), 1):
            print(f"  p{i:02d} {voice}: {text[:64]}", flush=True)
            wavs, sr = model.generate_voice_design(
                text=text,
                language="English",
                instruct=INSTRUCT[voice],
            )
            wav = np.asarray(wavs[0], dtype=np.float32)
            chunks.append((wav, int(sr)))
            sf.write(str(MEDIA / "segments" / f"{sid}-p{i:02d}-{voice}.wav"), wav, int(sr))
            if torch.backends.mps.is_available():
                torch.mps.empty_cache()

        body, sr = concat(chunks)
        title_line = f"Please listen. {story['title']}"
        print(f"  title brand: {title_line}", flush=True)
        twavs, tsr = model.generate_voice_design(
            text=title_line,
            language="English",
            instruct=INSTRUCT["brand"],
        )
        title = np.asarray(twavs[0], dtype=np.float32)

        body_mp3 = BUNDLE / f"{sid}.mp3"
        title_mp3 = BUNDLE / "Titles" / f"{sid}.mp3"
        wav_to_mp3(body, sr, body_mp3)
        wav_to_mp3(title, int(tsr), title_mp3)
        shutil.copy2(body_mp3, MEDIA / f"{sid}-body.mp3")
        shutil.copy2(title_mp3, MEDIA / f"{sid}-title.mp3")
        print(f"  saved body {len(body)/sr:.1f}s title {len(title)/tsr:.1f}s", flush=True)
        done.append(sid)
        update_manifest([sid])

    print("DONE", done, flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
