#!/usr/bin/env python3
"""Caption blank EN pilot panels and install into EyeHaven BedtimeComics."""
from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, "/Users/song/qwen3-tts/comic_batch")
from stable_caption import fill_bubbles  # noqa: E402

PLAN = Path("/Users/song/qwen3-tts/comic_batch/comics_plan_en_pilot12.json")
PLAN_B2 = Path("/Users/song/qwen3-tts/comic_batch/comics_plan_en_pilot12_b2.json")
PLAN_FREE_W1 = Path("/Users/song/qwen3-tts/comic_batch/comics_plan_en_free_front5_w1.json")
PLAN_FREE_W2 = Path("/Users/song/qwen3-tts/comic_batch/comics_plan_en_free_front5_w2.json")
PLAN_FREE_W3 = Path("/Users/song/qwen3-tts/comic_batch/comics_plan_en_free_front5_w3.json")
PLAN_FREE_W4 = Path("/Users/song/qwen3-tts/comic_batch/comics_plan_en_free_front5_w4.json")
PLAN_FREE_W5 = Path("/Users/song/qwen3-tts/comic_batch/comics_plan_en_free_front5_w5.json")
PLAN_BACK_W6 = Path("/Users/song/qwen3-tts/comic_batch/comics_plan_en_backcatalog_w6.json")
PLAN_BACK_W7 = Path("/Users/song/qwen3-tts/comic_batch/comics_plan_en_backcatalog_w7.json")
PLAN_BACK_W8 = Path("/Users/song/qwen3-tts/comic_batch/comics_plan_en_backcatalog_w8.json")
PLAN_BACK_W9 = Path("/Users/song/qwen3-tts/comic_batch/comics_plan_en_backcatalog_w9.json")
PLAN_BACK_W10 = Path("/Users/song/qwen3-tts/comic_batch/comics_plan_en_backcatalog_w10.json")
PLAN_BACK_W11 = Path("/Users/song/qwen3-tts/comic_batch/comics_plan_en_backcatalog_w11.json")
PLAN_BACK_W12 = Path("/Users/song/qwen3-tts/comic_batch/comics_plan_en_backcatalog_w12.json")
PLAN_BACK_W13 = Path("/Users/song/qwen3-tts/comic_batch/comics_plan_en_backcatalog_w13.json")
PLAN_BACK_W14 = Path("/Users/song/qwen3-tts/comic_batch/comics_plan_en_backcatalog_w14.json")
PLAN_BACK_W15 = Path("/Users/song/qwen3-tts/comic_batch/comics_plan_en_backcatalog_w15.json")
PLAN_BACK_W16 = Path("/Users/song/qwen3-tts/comic_batch/comics_plan_en_backcatalog_w16.json")
PLAN_BACK_W17 = Path("/Users/song/qwen3-tts/comic_batch/comics_plan_en_backcatalog_w17.json")
PLAN_BACK_W18 = Path("/Users/song/qwen3-tts/comic_batch/comics_plan_en_backcatalog_w18.json")
PLAN_BACK_W19 = Path("/Users/song/qwen3-tts/comic_batch/comics_plan_en_backcatalog_w19.json")
PLAN_BACK_W20 = Path("/Users/song/qwen3-tts/comic_batch/comics_plan_en_backcatalog_w20.json")
PLAN_BACK_W21 = Path("/Users/song/qwen3-tts/comic_batch/comics_plan_en_backcatalog_w21.json")
PLAN_BACK_W22 = Path("/Users/song/qwen3-tts/comic_batch/comics_plan_en_backcatalog_w22.json")
ASSETS = Path(
    "/Users/song/Library/Application Support/Cursor/AgentStores/"
    "cursor_agent_stores/bc-6341924c-d627-5e70-8277-ff97645af6c8/files/artifacts/assets"
)
# Parent store artifacts (coordinator) also hold generated panels sometimes
ASSETS_PARENT = Path(
    "/Users/song/Library/Application Support/Cursor/AgentStores/"
    "cursor_agent_stores/bc-b474c295-0680-491b-a693-72941041732d/files/artifacts/assets"
)
RAW = Path("/Users/song/qwen3-tts/comic_batch/en_work/_raw_pilot")
RAW_FREE_W1 = Path("/Users/song/qwen3-tts/comic_batch/en_work/_raw_free_front5_w1")
RAW_FREE_W2 = Path("/Users/song/qwen3-tts/comic_batch/en_work/_raw_free_front5_w2")
RAW_FREE_W3 = Path("/Users/song/qwen3-tts/comic_batch/en_work/_raw_free_front5_w3")
RAW_FREE_W4 = Path("/Users/song/qwen3-tts/comic_batch/en_work/_raw_free_front5_w4")
RAW_FREE_W5 = Path("/Users/song/qwen3-tts/comic_batch/en_work/_raw_free_front5_w5")
RAW_BACK_W6 = Path("/Users/song/qwen3-tts/comic_batch/en_work/_raw_backcatalog_w6")
RAW_BACK_W7 = Path("/Users/song/qwen3-tts/comic_batch/en_work/_raw_backcatalog_w7")
RAW_BACK_W8 = Path("/Users/song/qwen3-tts/comic_batch/en_work/_raw_backcatalog_w8")
RAW_BACK_W9 = Path("/Users/song/qwen3-tts/comic_batch/en_work/_raw_backcatalog_w9")
RAW_BACK_W10 = Path("/Users/song/qwen3-tts/comic_batch/en_work/_raw_backcatalog_w10")
RAW_BACK_W11 = Path("/Users/song/qwen3-tts/comic_batch/en_work/_raw_backcatalog_w11")
RAW_BACK_W12 = Path("/Users/song/qwen3-tts/comic_batch/en_work/_raw_backcatalog_w12")
RAW_BACK_W13 = Path("/Users/song/qwen3-tts/comic_batch/en_work/_raw_backcatalog_w13")
RAW_BACK_W14 = Path("/Users/song/qwen3-tts/comic_batch/en_work/_raw_backcatalog_w14")
RAW_BACK_W15 = Path("/Users/song/qwen3-tts/comic_batch/en_work/_raw_backcatalog_w15")
RAW_BACK_W16 = Path("/Users/song/qwen3-tts/comic_batch/en_work/_raw_backcatalog_w16")
RAW_BACK_W17 = Path("/Users/song/qwen3-tts/comic_batch/en_work/_raw_backcatalog_w17")
RAW_BACK_W18 = Path("/Users/song/qwen3-tts/comic_batch/en_work/_raw_backcatalog_w18")
RAW_BACK_W19 = Path("/Users/song/qwen3-tts/comic_batch/en_work/_raw_backcatalog_w19")
RAW_BACK_W20 = Path("/Users/song/qwen3-tts/comic_batch/en_work/_raw_backcatalog_w20")
RAW_BACK_W21 = Path("/Users/song/qwen3-tts/comic_batch/en_work/_raw_backcatalog_w21")
RAW_BACK_W22 = Path("/Users/song/qwen3-tts/comic_batch/en_work/_raw_backcatalog_w22")
WORK = Path("/Users/song/qwen3-tts/comic_batch/en_work")
APP = ROOT / "EyeHaven" / "BedtimeComics"
# Prefer English-friendly rounded font for bubble text
import stable_caption as sc

EN_FONT = "/System/Library/Fonts/Supplemental/Arial Rounded Bold.ttf"
if Path(EN_FONT).exists():
    sc.FONT = EN_FONT


def find_asset(story_id: str, i: int) -> Path | None:
    stem = f"c-{story_id}-{i:02d}"
    bases = [
        RAW_BACK_W22,
        RAW_BACK_W21,
        RAW_BACK_W20,
        RAW_BACK_W19,
        RAW_BACK_W18,
        RAW_BACK_W17,
        RAW_BACK_W16,
        RAW_BACK_W15,
        RAW_BACK_W14,
        RAW_BACK_W13,
        RAW_BACK_W12,
        RAW_BACK_W11,
        RAW_BACK_W10,
        RAW_BACK_W9,
        RAW_BACK_W8,
        RAW_BACK_W7,
        RAW_BACK_W6,
        RAW_FREE_W5,
        RAW_FREE_W4,
        RAW_FREE_W3,
        RAW_FREE_W2,
        RAW_FREE_W1,
        RAW,
        ASSETS,
        ASSETS_PARENT,
    ]
    for base in bases:
        if not base.exists():
            continue
        for ext in (".jpg", ".png", ".jpeg"):
            p = base / f"{stem}{ext}"
            if p.exists():
                return p
    for base in bases:
        if not base.exists():
            continue
        for p in base.rglob(f"{stem}.*"):
            if p.suffix.lower() in {".jpg", ".png", ".jpeg"}:
                return p
    return None


def load_plan(story_id: str | None = None) -> list:
    plans: list = []
    for path in (
        PLAN,
        PLAN_B2,
        PLAN_FREE_W1,
        PLAN_FREE_W2,
        PLAN_FREE_W3,
        PLAN_FREE_W4,
        PLAN_FREE_W5,
        PLAN_BACK_W6,
        PLAN_BACK_W7,
        PLAN_BACK_W8,
        PLAN_BACK_W9,
        PLAN_BACK_W10,
        PLAN_BACK_W11,
        PLAN_BACK_W12,
        PLAN_BACK_W13,
        PLAN_BACK_W14,
        PLAN_BACK_W15,
        PLAN_BACK_W16,
        PLAN_BACK_W17,
        PLAN_BACK_W18,
        PLAN_BACK_W19,
        PLAN_BACK_W20,
        PLAN_BACK_W21,
        PLAN_BACK_W22,
    ):
        if path.exists():
            plans.extend(json.loads(path.read_text(encoding="utf-8")))
    # de-dupe by id keeping last (b2 overrides)
    by_id = {}
    for ep in plans:
        by_id[ep["id"]] = ep
    eps = list(by_id.values())
    if story_id:
        eps = [ep for ep in eps if ep["id"] == story_id]
    return eps


def process(story_id: str | None = None) -> None:
    for ep in load_plan(story_id):
        sid = ep["id"]
        work = WORK / f"{sid}-12"
        work.mkdir(parents=True, exist_ok=True)
        app_dir = APP / sid
        # backup old 3-panel set once
        bak = WORK / f"{sid}-old3"
        if not bak.exists() and app_dir.exists():
            bak.mkdir(parents=True, exist_ok=True)
            for p in sorted(app_dir.glob("*.jpg")):
                shutil.copy2(p, bak / p.name)
        ok = 0
        for panel in ep["panels"]:
            i = panel["i"]
            src = find_asset(sid, i)
            if not src:
                print("MISSING", sid, i)
                continue
            blank = work / f"{i:02d}-blank.jpg"
            Image.open(src).convert("RGB").save(blank, quality=92)
            captioned = work / f"{i:02d}-captioned.jpg"
            title = panel.get("tag") or f"{i:02d}"
            success = fill_bubbles(
                blank,
                captioned,
                panel["left"],
                panel["right"],
                title,
                allow_fallback=False,
            )
            if not success:
                print("CAPTION_FAIL", sid, i, "— retry with fallback bubbles")
                success = fill_bubbles(
                    blank,
                    captioned,
                    panel["left"],
                    panel["right"],
                    title,
                    allow_fallback=True,
                )
            if not success:
                print("FAIL", sid, i)
                continue
            app_dir.mkdir(parents=True, exist_ok=True)
            dest = app_dir / f"{i:02d}.jpg"
            # normalize to ~1152x864 like existing comics
            im = Image.open(captioned).convert("RGB")
            im = im.resize((1152, 864), Image.Resampling.LANCZOS)
            im.save(dest, quality=90)
            ok += 1
            print("ok", sid, i, dest)
        # remove leftover old panels beyond new count
        if ok:
            for p in app_dir.glob("*.jpg"):
                try:
                    n = int(p.stem)
                except ValueError:
                    continue
                if n > ok:
                    p.unlink()
                    print("removed leftover", p)
        print(f"{sid} installed {ok}/12")


if __name__ == "__main__":
    only = sys.argv[1] if len(sys.argv) > 1 else None
    process(only)
