#!/usr/bin/env python3
"""Record E-A01 + E-Y04 with locked VoiceDesign three voices. Does not change 0.6B pipeline."""
from __future__ import annotations

import json
import shutil
import time
from pathlib import Path

import lameenc
import numpy as np
import soundfile as sf
import torch
from qwen_tts import Qwen3TTSModel

REPO = Path("/Users/song/EyeHaven-EN")
CATALOG = REPO / "EyeHaven" / "BedtimeContentCatalog.en.json"
BUNDLE = REPO / "EyeHaven" / "BedtimeAudioBundle"
MODEL = Path("/Users/song/qwen3-tts/models/Qwen3-TTS-12Hz-1.7B-VoiceDesign")
MEDIA = Path(
    "/Users/song/Library/Application Support/Cursor/AgentStores/"
    "cursor_agent_stores/bc-b474c295-0680-491b-a693-72941041732d/files/media/voicedesign-two-stories"
)
MEDIA2 = Path(
    "/Users/song/Library/Application Support/Cursor/AgentStores/"
    "cursor_agent_stores/bc-6341924c-d627-5e70-8277-ff97645af6c8/files/media/voicedesign-two-stories"
)
DOC = Path(
    "/Users/song/Library/Application Support/Cursor/AgentStores/"
    "cursor_agent_stores/bc-b474c295-0680-491b-a693-72941041732d/files/docs/voicedesign-two-stories-casting.md"
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

# Page casting: each story uses all three voices (brand=光光, boy=Max, girl=Mia)
CASTING = {
    "E-A01": {
        # rotate evenly; p1 opening stays 光光
        "pages": [
            "brand",
            "boy",
            "girl",
            "brand",
            "boy",
            "girl",
            "brand",
            "boy",
            "girl",
            "brand",
            "boy",
            "girl",
        ],
        "title_voice": "brand",
        "notes": "Even rotate brand/boy/girl across 12 pages. Title by 光光.",
    },
    "E-Y04": {
        # p2 is Guangguang speaking → brand; still hit all three
        "pages": [
            "brand",  # POP
            "brand",  # Guangguang jumps / question
            "boy",
            "girl",
            "brand",
            "boy",
            "girl",
            "brand",
            "boy",
            "girl",
            "brand",
            "boy",
        ],
        "title_voice": "brand",
        "notes": "Pages 1–2 光光; then rotate boy/girl/brand so Max+Mia+光光 all appear. Title by 光光.",
    },
}


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


def main() -> int:
    stories = {s["id"]: s for s in json.loads(CATALOG.read_text(encoding="utf-8"))["stories"]}
    for d in (MEDIA, MEDIA2):
        d.mkdir(parents=True, exist_ok=True)
        (d / "segments").mkdir(exist_ok=True)
        (d / "backup-ryan").mkdir(exist_ok=True)

    # Backup current Ryan app audio once
    for sid in CASTING:
        for rel in (f"{sid}.mp3", f"Titles/{sid}.mp3"):
            src = BUNDLE / rel
            if src.exists():
                for d in (MEDIA, MEDIA2):
                    dst = d / "backup-ryan" / Path(rel).name.replace(sid, f"{sid}-{Path(rel).parent.name}" if "Titles" in rel else sid)
                    if "Titles" in rel:
                        dst = d / "backup-ryan" / f"{sid}-title.mp3"
                    else:
                        dst = d / "backup-ryan" / f"{sid}-body.mp3"
                    if not dst.exists():
                        shutil.copy2(src, dst)
                        print("backup", dst.name)

    print("loading VoiceDesign float16 mps", flush=True)
    t0 = time.time()
    model = Qwen3TTSModel.from_pretrained(
        str(MODEL),
        device_map="mps",
        dtype=torch.float16,
        attn_implementation="sdpa",
    )
    print(f"loaded {time.time()-t0:.1f}s", flush=True)

    casting_doc_rows: list[str] = []

    for sid, cast in CASTING.items():
        story = stories[sid]
        pages = [p.strip() for p in story["text"].split("\n\n") if p.strip()]
        assert len(pages) == 12, (sid, len(pages))
        assert len(cast["pages"]) == 12
        print(f"\n=== {sid} {story['title']} ===", flush=True)

        chunks: list[tuple[np.ndarray, int]] = []
        page_rows = []
        for i, (text, voice) in enumerate(zip(pages, cast["pages"]), 1):
            print(f"  p{i:02d} {voice}: {text[:56]}...", flush=True)
            wavs, sr = model.generate_voice_design(
                text=text,
                language="English",
                instruct=INSTRUCT[voice],
            )
            wav = np.asarray(wavs[0], dtype=np.float32)
            chunks.append((wav, int(sr)))
            for d in (MEDIA, MEDIA2):
                sf.write(str(d / "segments" / f"{sid}-p{i:02d}-{voice}.wav"), wav, int(sr))
            page_rows.append((i, voice, text, len(wav) / sr))
            if torch.backends.mps.is_available():
                torch.mps.empty_cache()

        body, sr = concat(chunks)
        # Title
        title_line = f"Please listen. {story['title']}"
        print(f"  title {cast['title_voice']}: {title_line}", flush=True)
        twavs, tsr = model.generate_voice_design(
            text=title_line,
            language="English",
            instruct=INSTRUCT[cast["title_voice"]],
        )
        title = np.asarray(twavs[0], dtype=np.float32)

        # Write App paths
        body_mp3 = BUNDLE / f"{sid}.mp3"
        title_mp3 = BUNDLE / "Titles" / f"{sid}.mp3"
        wav_to_mp3(body, sr, body_mp3)
        wav_to_mp3(title, int(tsr), title_mp3)

        # Write media copies (wav + mp3)
        for d in (MEDIA, MEDIA2):
            sf.write(str(d / f"{sid}-body.wav"), body, sr)
            sf.write(str(d / f"{sid}-title.wav"), title, int(tsr))
            shutil.copy2(body_mp3, d / f"{sid}-body.mp3")
            shutil.copy2(title_mp3, d / f"{sid}-title.mp3")

        print(f"  APP body {body_mp3} dur={len(body)/sr:.1f}s bytes={body_mp3.stat().st_size}", flush=True)
        print(f"  APP title {title_mp3} dur={len(title)/tsr:.1f}s", flush=True)

        casting_doc_rows.append((sid, story["title"], cast, page_rows, len(body) / sr, len(title) / tsr))

    # Document
    lines = [
        "# VoiceDesign 两篇三音色试录（E-A01 / E-Y04）",
        "",
        "> 日期：2026-11-16 · 模型：1.7B VoiceDesign float16 MPS  ",
        "> 锁定 instruct：见 [`voicedesign-locked-voices.md`](./voicedesign-locked-voices.md)  ",
        "> **未改** 0.6B 批录脚本；仅覆盖这两篇 App 音频（Ryan 原文件已备份到 media）。",
        "",
        "## 角色",
        "",
        "| 代号 | 角色 | 锁定 instruct 来源 |",
        "| --- | --- | --- |",
        "| brand / 光光 | 旁白 / 自述 | Brand 锁定 |",
        "| boy / Max | 男孩 | Boy take **b** 锁定 |",
        "| girl / Mia | 女孩 | Girl 锁定 |",
        "",
        "## 播放路径",
        "",
        "- App：`EyeHaven/BedtimeAudioBundle/<ID>.mp3` + `Titles/<ID>.mp3`",
        "- 试听包：`media/voicedesign-two-stories/`",
        "- Ryan 备份：`media/voicedesign-two-stories/backup-ryan/`",
        "",
    ]
    for sid, title, cast, page_rows, body_dur, title_dur in casting_doc_rows:
        counts = {"brand": 0, "boy": 0, "girl": 0}
        for _, v, _, _ in page_rows:
            counts[v] += 1
        lines += [
            f"## {sid} · {title}",
            "",
            f"- 标题声：`{cast['title_voice']}`（光光）· 约 {title_dur:.1f}s",
            f"- 正文：约 {body_dur:.1f}s · 页分配 brand={counts['brand']} boy={counts['boy']} girl={counts['girl']}",
            f"- 说明：{cast['notes']}",
            "",
            "| 页 | 声音 | 文案 | 段长约 |",
            "| ---: | --- | --- | ---: |",
        ]
        for i, voice, text, dur in page_rows:
            safe = text.replace("|", "\\|")
            lines.append(f"| {i} | {voice} | {safe} | {dur:.1f}s |")
        lines.append("")

    lines += [
        "## 怎么听",
        "",
        "1. 用 Xcode 打开 EyeHaven-EN，跑 App。",
        "2. 打开 Ages 3–10 → Animals → **Why Can Birds Fly?**；Why → **Why Does Popcorn Pop?**",
        "3. 点播放：先标题再正文；漫画 12 页随进度翻。",
        "4. 或直接听 `media/voicedesign-two-stories/*-body.mp3`。",
        "",
        "## 恢复 Ryan（如需要）",
        "",
        "```bash",
        "cp media/voicedesign-two-stories/backup-ryan/E-A01-body.mp3 EyeHaven/BedtimeAudioBundle/E-A01.mp3",
        "cp media/voicedesign-two-stories/backup-ryan/E-A01-title.mp3 EyeHaven/BedtimeAudioBundle/Titles/E-A01.mp3",
        "# 同上替换 E-Y04",
        "```",
        "",
    ]
    DOC.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("DOC", DOC, flush=True)
    print("DONE", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
