#!/usr/bin/env python3
"""Record story IDs with locked VoiceDesign three voices (brand/boy/girl).

Default casting: rotate brand→boy→girl across 12 pages; title = brand.
Usage:
  /Users/song/qwen3-tts/.venv/bin/python scripts/record_vd_stories.py --only E-W01 E-W02
"""
from __future__ import annotations

import argparse
import json
import shutil
import time
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
MODEL = Path("/Users/song/qwen3-tts/models/Qwen3-TTS-12Hz-1.7B-VoiceDesign")
MEDIA = Path(
    "/Users/song/Library/Application Support/Cursor/AgentStores/"
    "cursor_agent_stores/bc-b474c295-0680-491b-a693-72941041732d/files/media/voicedesign-batch"
)

GAP_SEC = 0.28

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
}

ROTATE = ["brand", "boy", "girl"] * 4  # 12 pages


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
    # keep structure flexible
    entries = data.get("files") or data.get("stories") or data
    if isinstance(entries, dict):
        for i in ids:
            entries[i] = {"body": f"{i}.mp3", "title": f"Titles/{i}.mp3"}
    MANIFEST.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", nargs="+", required=True)
    args = ap.parse_args()

    stories = {s["id"]: s for s in json.loads(CATALOG.read_text(encoding="utf-8"))["stories"]}
    want = [sid for sid in args.only if sid in stories]
    if not want:
        print("no stories", flush=True)
        return 1
    if not MODEL.exists():
        print("missing model", MODEL, flush=True)
        return 1

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
        # backup existing once
        for label, rel in (("body", f"{sid}.mp3"), ("title", f"Titles/{sid}.mp3")):
            src = BUNDLE / rel
            if src.exists():
                dst = MEDIA / "backup" / f"{sid}-{label}.mp3"
                if not dst.exists():
                    shutil.copy2(src, dst)

        print(f"\n=== {sid} {story['title']} ===", flush=True)
        chunks: list[tuple[np.ndarray, int]] = []
        for i, (text, voice) in enumerate(zip(pages, ROTATE), 1):
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
