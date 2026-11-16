#!/usr/bin/env python3
"""Back-catalog wave 25: Earth E-E22…E-E24 → 12-page books. Owner sleeping; no questions."""
from __future__ import annotations

import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PREFIX_BOY = (
    "Children's picture book comic panel, soft warm friendly earth-science lighting, landscape 4:3. "
    "Cute round-headed white robot Guangguang with green trim, warm glowing chest lamp, small star on head, honest smile. "
    "Blonde boy about 6 years old with freckles wearing a blue T-rex hoodie with white sleeve stripes. "
    "Two large empty white oval speech bubbles with space for short kids text, blank inside, no letters. "
    "Soft friendly earth science, gentle pastel, not scary. No text logos, consistent character design. "
    "Simple readable background, big clear shapes, shallow depth, soft edges, no clutter. "
)
PREFIX_GIRL = (
    "Children's picture book comic panel, soft warm friendly earth-science lighting, landscape 4:3. "
    "Cute round-headed white robot Guangguang with green trim, warm glowing chest lamp, small star on head, honest smile. "
    "Gentle girl about 6–7 with soft sweater and kind smile. "
    "Two large empty white oval speech bubbles with space for short kids text, blank inside, no letters. "
    "Soft friendly earth science, gentle pastel, not scary. No text logos, consistent character design. "
    "Simple readable background, big clear shapes, shallow depth, soft edges, no clutter. "
)

STORIES = {
    "E-E22": {
        "title": "Why Do Trees Help the Air?",
        "folder": "Earth",
        "tag": "TreeAir",
        "companion": "boy",
        "pages": [
            'Max breathes under a tree. "How do trees help air?"',
            "Leaves take in carbon dioxide from the air.",
            "Using sunlight, they make food for the tree.",
            "They release oxygen that animals and people breathe.",
            "Shade from trees can cool hot sidewalks.",
            "Roots and leaves also catch dust gently.",
            "Forests are big air helpers for the whole planet.",
            "Planting and caring for trees is Earth kindness.",
            "Never carve bark—trees need their skin.",
            "Take in CO2, give out oxygen: leaf work.",
            "Water a young tree with a grown-up.",
            "Fresh breath: tree-air science.",
        ],
        "bubbles": [
            ("Under tree!", "Help air?"),
            ("Leaves take", "CO2."),
            ("Sunlight makes", "food."),
            ("Release oxygen", "we breathe."),
            ("Shade cools", "sidewalks."),
            ("Catch dust", "gently."),
            ("Forests help", "planet."),
            ("Care for trees", "kindly."),
            ("Don’t carve", "bark."),
            ("CO2 in,", "oxygen out."),
            ("Water a tree", "together."),
            ("Tree-air", "science."),
        ],
        "scenes": [
            "WIDE soft park under tree breathe; boy and robot one-third; empty speech bubbles",
            "DIAGRAM-SOFT leaves take CO2 soft; tiny figures; empty speech bubbles",
            "CLOSE sunlight leaf food soft; boy points; robot; empty speech bubbles",
            "MEDIUM oxygen release soft; characters half frame; empty speech bubbles",
            "PLAYFUL shade cool soft; characters half frame; empty speech bubbles",
            "WIDE catch dust soft; characters one-third; empty speech bubbles",
            "CLOSE forest helpers soft; characters half frame; empty speech bubbles",
            "MEDIUM care trees soft; characters half frame; empty speech bubbles",
            "CLOSE no carve bark soft; characters half frame; empty speech bubbles",
            "DIAGRAM-SOFT CO2 oxygen soft; tiny figures; empty speech bubbles",
            "MEDIUM water young tree soft; boy and robot half frame; empty speech bubbles",
            "ENDING boy and robot soft smile; one-third; empty speech bubbles",
        ],
    },
    "E-E23": {
        "title": "What Is Groundwater?",
        "folder": "Earth",
        "tag": "Groundwater",
        "companion": "girl",
        "pages": [
            'Mia wonders about a well. "What’s groundwater?"',
            "Rain soaks down through soil and rock cracks.",
            "Water collects in underground spaces like a sponge.",
            "That hidden water is called groundwater.",
            "Wells and springs can bring it up carefully.",
            "It moves slowly—much slower than a river.",
            "Clean soil helps keep groundwater healthier.",
            "Don’t dump chemicals outside—ask grown-ups.",
            "Many towns drink groundwater every day.",
            "Rain down → store below → use wisely.",
            "Look at a simple well diagram together.",
            "Hidden water: groundwater science.",
        ],
        "bubbles": [
            ("A well!", "Groundwater?"),
            ("Rain soaks", "down."),
            ("Stores like a", "sponge."),
            ("Hidden water", "below."),
            ("Wells springs", "bring it up."),
            ("Moves very", "slowly."),
            ("Clean soil", "helps."),
            ("No dumping", "chemicals."),
            ("Towns drink", "it."),
            ("Rain store", "use."),
            ("Well diagram", "together."),
            ("Groundwater", "science."),
        ],
        "scenes": [
            "WIDE soft countryside well; girl and robot one-third; empty speech bubbles",
            "DIAGRAM-SOFT rain soak down soft; tiny figures; empty speech bubbles",
            "CLOSE sponge store soft; girl points; robot; empty speech bubbles",
            "MEDIUM hidden water soft; characters half frame; empty speech bubbles",
            "PLAYFUL well spring soft; characters half frame; empty speech bubbles",
            "WIDE slow move soft; characters one-third; empty speech bubbles",
            "CLOSE clean soil soft; characters half frame; empty speech bubbles",
            "MEDIUM no dump chemicals soft; characters half frame; empty speech bubbles",
            "PLAYFUL town drinks soft; characters half frame; empty speech bubbles",
            "DIAGRAM-SOFT rain store use soft; tiny figures; empty speech bubbles",
            "MEDIUM well diagram soft; girl and robot half frame; empty speech bubbles",
            "ENDING girl and robot soft smile; one-third; empty speech bubbles",
        ],
    },
    "E-E24": {
        "title": "Why Do We Need National Parks?",
        "folder": "Earth",
        "tag": "Parks",
        "companion": "boy",
        "pages": [
            'A park map with a bear icon. "Why national parks?"',
            "Parks protect wild places for animals and plants.",
            "People can visit to learn, hike, and wonder.",
            "Rules keep trails, nests, and water safer.",
            "Rangers teach and help when visitors need care.",
            "Parks save stories of rocks, trees, and history.",
            "Leave no trash—pack out what you pack in.",
            "Stay on paths so tiny homes stay uncrushed.",
            "Photos are better souvenirs than taking rocks.",
            "Protect + share = park promise.",
            "Plan a park day with a grown-up someday.",
            "Wild classroom: park science.",
        ],
        "bubbles": [
            ("Park map!", "Why parks?"),
            ("Protect wild", "homes."),
            ("Visit learn", "hike."),
            ("Rules keep", "safe."),
            ("Rangers help", "teach."),
            ("Save rock tree", "stories."),
            ("Pack out", "trash."),
            ("Stay on", "paths."),
            ("Photos not", "taking rocks."),
            ("Protect and", "share."),
            ("Plan a day", "together."),
            ("Park", "science."),
        ],
        "scenes": [
            "WIDE soft national park trail entrance; boy and robot one-third; empty speech bubbles",
            "DIAGRAM-SOFT protect wild homes soft; tiny figures; empty speech bubbles",
            "CLOSE visit learn hike soft; boy points; robot; empty speech bubbles",
            "MEDIUM rules safer soft; characters half frame; empty speech bubbles",
            "PLAYFUL ranger teach soft; characters half frame; empty speech bubbles",
            "WIDE rock tree stories soft; characters one-third; empty speech bubbles",
            "CLOSE pack out trash soft; characters half frame; empty speech bubbles",
            "MEDIUM stay on paths soft; characters half frame; empty speech bubbles",
            "PLAYFUL photo souvenir soft; characters half frame; empty speech bubbles",
            "DIAGRAM-SOFT protect share soft; tiny figures; empty speech bubbles",
            "MEDIUM plan park day soft; boy and robot half frame; empty speech bubbles",
            "ENDING boy and robot soft smile; one-third; empty speech bubbles",
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
                story["title"] = STORIES[story["id"]]["title"]
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
    ref_dir = ROOT / ".comic_refs" / "w25_by_story"
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

    Path("/Users/song/qwen3-tts/comic_batch/comics_plan_en_backcatalog_w25.json").write_text(
        json.dumps(plan, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    Path("/Users/song/qwen3-tts/comic_batch/en_work/_raw_backcatalog_w25").mkdir(parents=True, exist_ok=True)
    Path("/Users/song/qwen3-tts/comic_batch/en_work/backcatalog_w25_prompts.json").write_text(
        json.dumps(prompts, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    bubbles_path = ROOT / "EyeHaven" / "ComicBubbleWords.en.json"
    bubbles = json.loads(bubbles_path.read_text(encoding="utf-8"))
    for sid, st in STORIES.items():
        bubbles[sid] = [{"i": i, "left": L, "right": R} for i, (L, R) in enumerate(st["bubbles"], 1)]
    bubbles_path.write_text(json.dumps(bubbles, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("wave25 done", len(STORIES), "prompts", len(prompts))


if __name__ == "__main__":
    main()
