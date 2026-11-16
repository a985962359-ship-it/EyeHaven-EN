#!/usr/bin/env python3
"""Back-catalog wave 19: Space E-S22…E-S24 → 12-page books. Owner sleeping; no questions."""
from __future__ import annotations

import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PREFIX_BOY = (
    "Children's picture book comic panel, soft warm friendly space-science lighting, landscape 4:3. "
    "Cute round-headed white robot Guangguang with green trim, warm glowing chest lamp, small star on head, honest smile. "
    "Blonde boy about 6 years old with freckles wearing a blue T-rex hoodie with white sleeve stripes. "
    "Two large empty white oval speech bubbles with space for short kids text, blank inside, no letters. "
    "Soft friendly space science, gentle pastel stars, not scary. No text logos, consistent character design. "
    "Simple readable background, big clear shapes, shallow depth, soft edges, no clutter. "
)
PREFIX_GIRL = (
    "Children's picture book comic panel, soft warm friendly space-science lighting, landscape 4:3. "
    "Cute round-headed white robot Guangguang with green trim, warm glowing chest lamp, small star on head, honest smile. "
    "Gentle girl about 6–7 with soft sweater and kind smile. "
    "Two large empty white oval speech bubbles with space for short kids text, blank inside, no letters. "
    "Soft friendly space science, gentle pastel stars, not scary. No text logos, consistent character design. "
    "Simple readable background, big clear shapes, shallow depth, soft edges, no clutter. "
)

STORIES = {
    "E-S22": {
        "title": "What Is a Light-Year?",
        "folder": "Space",
        "tag": "Lightyr",
        "companion": "boy",
        "pages": [
            'Guangguang draws a ruler across stars. "Light-year?"',
            "A light-year measures distance, not birthday time.",
            "It is how far light travels in one whole year.",
            "That stretch is about 9.5 trillion kilometers.",
            "Stars are so far that ordinary miles feel tiny and silly.",
            "Saying “four light-years away” packs a huge trip into short words.",
            "Light is the fastest messenger we know in empty space.",
            "When you see a star, its light may be years old already.",
            "Telescopes collect that old light like bottles of travel stories.",
            "Light-years turn huge space into numbers we can say out loud.",
            "Imagine a beam racing while Earth orbits once—then smile at the size.",
            "Distance stick of light: light-year science.",
        ],
        "bubbles": [
            ("Star ruler!", "Light-year?"),
            ("Measures distance,", "not time."),
            ("How far light", "goes in a year."),
            ("About 9.5", "trillion km."),
            ("Miles feel", "too tiny."),
            ("Short words,", "huge trip."),
            ("Light is a", "fast messenger."),
            ("Starlight can", "be years old."),
            ("Telescopes catch", "old light."),
            ("Huge space,", "sayable numbers."),
            ("Beam races one", "Earth year."),
            ("Light-year", "science."),
        ],
        "scenes": [
            "WIDE soft night star ruler; boy and robot one-third; empty speech bubbles",
            "DIAGRAM-SOFT distance not time soft; tiny figures; empty speech bubbles",
            "MEDIUM light travel one year soft; characters one-third; empty speech bubbles",
            "CLOSE huge number soft; boy points; robot; empty speech bubbles",
            "PLAYFUL tiny miles soft; characters half frame; empty speech bubbles",
            "WIDE short words huge trip soft; characters one-third; empty speech bubbles",
            "DIAGRAM-SOFT fast light soft; tiny figures; empty speech bubbles",
            "CLOSE old starlight soft; characters half frame; empty speech bubbles",
            "MEDIUM telescope soft; characters half frame; empty speech bubbles",
            "PLAYFUL sayable numbers soft; characters half frame; empty speech bubbles",
            "WIDE Earth orbit beam soft; boy and robot one-third; empty speech bubbles",
            "ENDING boy and robot thumbs-up soft; one-third; empty speech bubbles",
        ],
    },
    "E-S23": {
        "title": "Why Does the Sun Rise in the East?",
        "folder": "Space",
        "tag": "Sunrise",
        "companion": "girl",
        "pages": [
            'Morning gold. "Always east?" asks Guangguang.',
            "Earth spins from west toward east.",
            "From the ground, the Sun seems to climb in the east.",
            "Later it seems to set toward the west.",
            "The Sun is not racing around us each day—we are turning.",
            "That spin paints sunrise and sunset on the sky.",
            "Poles and seasons can tweak the Sun’s path a bit.",
            "Compasses still help hikers keep directions straight.",
            "Noon is when the Sun is highest for your place.",
            "Sunrise direction is Earth’s spin written in light.",
            "Watch a morning with a grown-up and point east together.",
            "West-to-east spin: sunrise science.",
        ],
        "bubbles": [
            ("Morning gold!", "Always east?"),
            ("Earth spins", "west to east."),
            ("Sun climbs", "in the east."),
            ("Sets toward", "the west."),
            ("We turn;", "Sun seems to move."),
            ("Spin paints", "sunrise."),
            ("Poles seasons", "tweak path."),
            ("Compass helps", "hikers."),
            ("Noon is", "highest Sun."),
            ("Spin written", "in light."),
            ("Point east", "together."),
            ("Sunrise", "science."),
        ],
        "scenes": [
            "WIDE soft morning gold sunrise; girl and robot one-third; empty speech bubbles",
            "DIAGRAM-SOFT Earth spin west to east soft; tiny figures; empty speech bubbles",
            "MEDIUM sun climb east soft; characters one-third; empty speech bubbles",
            "WIDE sunset west soft; girl points; robot; empty speech bubbles",
            "PLAYFUL we turn soft; characters half frame; empty speech bubbles",
            "DIAGRAM-SOFT spin paints sky soft; tiny figures; empty speech bubbles",
            "MEDIUM pole path tweak soft; characters half frame; empty speech bubbles",
            "CLOSE compass soft; characters half frame; empty speech bubbles",
            "WIDE noon high sun soft; characters one-third; empty speech bubbles",
            "PLAYFUL spin in light soft; characters half frame; empty speech bubbles",
            "MEDIUM point east soft; girl and robot half frame; empty speech bubbles",
            "ENDING girl and robot soft smile; one-third; empty speech bubbles",
        ],
    },
    "E-S24": {
        "title": "What Are Constellations?",
        "folder": "Space",
        "tag": "Constel",
        "companion": "girl",
        "pages": [
            'Dot-to-dot bears and hunters. "Real groups?" asks Guangguang.',
            "Constellations are patterns people imagined in the stars.",
            "We connect dots as seen from Earth into sky pictures.",
            "Stars in one pattern may not be neighbors in real space.",
            "They can just line up from our viewpoint.",
            "Different cultures drew different sky stories.",
            "Astronomers still use the names as handy sky maps.",
            "Learning a few patterns helps you find your way at night.",
            "Apps and grown-ups can point out the bright landmarks.",
            "Constellations are storytelling overlays on distant suns.",
            "Trace one simple shape on paper after looking up together.",
            "Sky stories on real stars: constellation science.",
        ],
        "bubbles": [
            ("Dot-to-dot!", "Real groups?"),
            ("Patterns people", "imagined."),
            ("Connect dots", "from Earth."),
            ("May not be", "neighbors."),
            ("Lined up from", "our view."),
            ("Cultures drew", "different stories."),
            ("Names help", "sky maps."),
            ("Patterns help", "night finding."),
            ("Grown-ups point", "landmarks."),
            ("Story overlays", "on suns."),
            ("Trace a shape", "on paper."),
            ("Constellation", "science."),
        ],
        "scenes": [
            "WIDE soft night constellation dots; girl and robot one-third; empty speech bubbles",
            "MEDIUM imagined patterns soft; characters one-third; empty speech bubbles",
            "CLOSE connect-the-dots soft; girl points; robot; empty speech bubbles",
            "DIAGRAM-SOFT not real neighbors soft; tiny figures; empty speech bubbles",
            "PLAYFUL viewpoint lineup soft; characters half frame; empty speech bubbles",
            "WIDE culture sky stories soft; characters one-third; empty speech bubbles",
            "MEDIUM sky map names soft; characters half frame; empty speech bubbles",
            "CLOSE night finding soft; characters half frame; empty speech bubbles",
            "MEDIUM grown-up point soft; characters half frame; empty speech bubbles",
            "PLAYFUL story overlay soft; characters half frame; empty speech bubbles",
            "WIDE paper trace soft; girl and robot one-third; empty speech bubbles",
            "ENDING girl and robot soft smile; one-third; empty speech bubbles",
        ],
    },
}


def main() -> None:
    text_map = {sid: "\n\n".join(st["pages"]) for sid, st in STORIES.items()}
    for rel in ["EyeHaven/BedtimeContentCatalog.en.json", "EyeHaven/BedtimeContentCatalog.json"]:
        path = ROOT / rel
        data = json.loads(path.read_text(encoding="utf-8"))
        for story in data["stories"]:
            if story["id"] in text_map:
                story["text"] = text_map[story["id"]]
        data["updatedAt"] = "2026-11-17"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print("updated", path)

    companions_path = ROOT / "scripts" / "vd_story_companions.json"
    companions = json.loads(companions_path.read_text(encoding="utf-8"))
    for sid, st in STORIES.items():
        companions[sid] = st["companion"]
    companions_path.write_text(json.dumps(companions, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    plan: list = []
    prompts: list = []
    girl_ref = ROOT / ".comic_refs" / "en_girl_ref.png"
    boy_ref = ROOT / ".comic_refs" / "en_boy_ref.png"
    gg_ref = ROOT / ".comic_refs" / "guangguang_ref.png"
    ref_dir = ROOT / ".comic_refs" / "w19_by_story"
    ref_dir.mkdir(parents=True, exist_ok=True)

    for sid, st in STORIES.items():
        assert len(st["pages"]) == 12 == len(st["bubbles"]) == len(st["scenes"])
        g = st["companion"]
        prefix = PREFIX_GIRL if g == "girl" else PREFIX_BOY
        kid = girl_ref if g == "girl" else boy_ref
        refs = [str(p) for p in (gg_ref, kid) if p.exists()]
        panels = []
        story_prompts = []
        for i, (scene, (left, right)) in enumerate(zip(st["scenes"], st["bubbles"]), 1):
            assert len(st["pages"][i - 1].split()) >= 4
            panels.append(
                {
                    "i": i,
                    "scene": scene,
                    "left": left,
                    "right": right,
                    "tag": f"{st['tag']} {i}/12",
                    "narration": st["pages"][i - 1],
                }
            )
            item = {
                "id": sid,
                "i": i,
                "filename": f"c-{sid}-{i:02d}.jpg",
                "description": prefix + "Scene: " + scene,
                "refs": refs,
                "companion": g,
            }
            prompts.append(item)
            story_prompts.append(item)
        plan.append({"id": sid, "title": st["title"], "companion": g, "panels": panels})
        path = ROOT / "睡前有声稿" / "美国英文稿" / st["folder"] / f"{sid}.txt"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(st["title"] + "\n\n" + "\n\n".join(st["pages"]) + "\n", encoding="utf-8")
        print("wrote", path)
        story_dir = ref_dir / sid
        story_dir.mkdir(parents=True, exist_ok=True)
        (ref_dir / f"{sid}_prompts.json").write_text(
            json.dumps(story_prompts, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
        for ref in (gg_ref, kid):
            if ref.exists():
                shutil.copy2(ref, story_dir / ref.name)

    Path("/Users/song/qwen3-tts/comic_batch/comics_plan_en_backcatalog_w19.json").write_text(
        json.dumps(plan, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    Path("/Users/song/qwen3-tts/comic_batch/en_work/_raw_backcatalog_w19").mkdir(parents=True, exist_ok=True)
    Path("/Users/song/qwen3-tts/comic_batch/en_work/backcatalog_w19_prompts.json").write_text(
        json.dumps(prompts, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    bubbles_path = ROOT / "EyeHaven" / "ComicBubbleWords.en.json"
    bubbles = json.loads(bubbles_path.read_text(encoding="utf-8"))
    for sid, st in STORIES.items():
        bubbles[sid] = [{"i": i, "left": L, "right": R} for i, (L, R) in enumerate(st["bubbles"], 1)]
    bubbles_path.write_text(json.dumps(bubbles, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("wave19 done", len(STORIES), "prompts", len(prompts))


if __name__ == "__main__":
    main()
