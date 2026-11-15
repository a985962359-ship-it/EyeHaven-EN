#!/usr/bin/env python3
"""Free-front-5 wave 2: Weather E-W01…E-W05 → 12-page audible picture books.

Background: kid-friendly-backgrounds.md. Audio later via VoiceDesign locked voices.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PREFIX = (
    "Children's picture book comic panel, soft warm friendly lighting, landscape 4:3. "
    "Cute round-headed white robot Guangguang with green trim, warm glowing chest lamp, "
    "small star on head, honest smile. Blonde boy about 6 years old wearing a blue T-rex hoodie. "
    "Exactly two empty white oval speech bubbles with blank white interiors and no letters inside. "
    "No scary imagery, no text logos, consistent character design. "
    "Simple readable background, big clear shapes, shallow depth, soft edges, no clutter. Scene: "
)

STORIES = {
    "E-W01": {
        "title": "Why Is the Sky Blue?",
        "folder": "Weather",
        "tag": "Sky",
        "pages": [
            "Guangguang looks up. Blue forever!",
            "Sunlight holds many colors mixed together.",
            "Air molecules scatter blue light the most.",
            "Red light scatters less on its way.",
            "Looking away from the Sun, more blue reaches our eyes.",
            "That is why daytime sky looks blue.",
            "Near the Sun, light can look brighter white-gold.",
            "Space looks black—there is almost no air there.",
            "Without air, light does not scatter the same way.",
            "Earth's air paints our blue ceiling.",
            "Same sunlight, special sky paint.",
            "Next sunny day, thank the tiny air helpers.",
        ],
        "bubbles": [
            ("Blue forever!", "Wow."),
            ("Many colors", "in sunlight."),
            ("Blue scatters", "most."),
            ("Red scatters", "less."),
            ("More blue", "to our eyes."),
            ("Daytime sky", "looks blue."),
            ("Near Sun:", "bright gold."),
            ("Space is", "black."),
            ("No air,", "no scatter."),
            ("Air paints", "blue ceiling."),
            ("Same sun,", "sky paint."),
            ("Thank tiny", "air helpers."),
        ],
        "scenes": [
            "Sunny park looking up at clear blue sky; robot and boy gaze upward; empty speech bubbles",
            "Soft prism/sunbeam showing many colors; robot points; boy curious; empty speech bubbles",
            "Friendly soft dots of air scattering blue rays; park grass; empty speech bubbles",
            "Red rays traveling straighter soft diagram; robot teaches; empty speech bubbles",
            "Boy looking away from sun toward blue sky; robot beside; empty speech bubbles",
            "Wide blue daytime sky over green lawn; both smile; empty speech bubbles",
            "Bright white-gold near sun edge soft not blinding; boy squints gently; empty speech bubbles",
            "Gentle night space view black with stars; robot and boy at window; empty speech bubbles",
            "Contrast: Earth with air glow vs space dark; soft teaching; empty speech bubbles",
            "Earth globe soft cartoon with blue air shell; empty speech bubbles",
            "Robot chest lamp glow under blue sky; boy thumbs up; empty speech bubbles",
            "Warm ending picnic under blue sky; empty speech bubbles",
        ],
    },
    "E-W02": {
        "title": "Why Is the Sunset Red?",
        "folder": "Weather",
        "tag": "Sunset",
        "pages": [
            "Evening turns peach and red.",
            "At sunset, sunlight travels through more air.",
            "Blue light scatters out of the long path.",
            "Reds and oranges travel farther to your eyes.",
            "Dust and clouds can deepen the colors.",
            "Same Sun—longer path, warmer colors.",
            "Morning sunrise can wear similar warm coats.",
            "City haze may make reds look extra deep.",
            "Clean air still makes soft peach evenings.",
            "Sunsets are physics wearing a pretty coat.",
            "Watch safely—never stare hard at the Sun.",
            "Wave goodnight to the warm sky.",
        ],
        "bubbles": [
            ("Peach and red!", "Pretty."),
            ("Longer path", "through air."),
            ("Blue scatters", "away."),
            ("Red travels", "farther."),
            ("Dust deepens", "color."),
            ("Same Sun,", "warmer."),
            ("Sunrise too", "can glow."),
            ("Haze makes", "deeper red."),
            ("Clean air,", "soft peach."),
            ("Physics in", "pretty coat."),
            ("Don't stare", "at Sun."),
            ("Goodnight,", "warm sky."),
        ],
        "scenes": [
            "Hillside evening peach-red sunset; robot and boy watch; empty speech bubbles",
            "Soft long sun rays through thick air layers; empty speech bubbles",
            "Blue light scattering out of path diagram soft; empty speech bubbles",
            "Warm red-orange light reaching boy eyes; empty speech bubbles",
            "Soft dusty clouds deepening sunset; empty speech bubbles",
            "Same sun lower on horizon warmer colors; empty speech bubbles",
            "Gentle sunrise peach sky morning; empty speech bubbles",
            "City skyline soft haze deep red evening; not scary; empty speech bubbles",
            "Clean countryside soft peach sunset; empty speech bubbles",
            "Robot presents pretty physics coat metaphor playful; empty speech bubbles",
            "Boy looks beside sunset not staring into sun; robot guides; empty speech bubbles",
            "Warm ending waving goodnight under red sky; empty speech bubbles",
        ],
    },
    "E-W03": {
        "title": "Why Does It Rain?",
        "folder": "Weather",
        "tag": "Rain",
        "pages": [
            "Drops tap the window. Tap tap!",
            "Warm air lifts invisible water vapor up.",
            "High up, the air cools.",
            "Tiny droplets gather into clouds.",
            "Droplets grow heavier and heavier.",
            "Gravity pulls them down as rain.",
            "Rain waters plants and thirsty soil.",
            "Rain helps fill rivers and lakes.",
            "Too much rain can make puddle floods.",
            "Too little rain makes dry, thirsty days.",
            "Weather is Earth's water on the move.",
            "Listen—rain is the sky sharing a drink.",
        ],
        "bubbles": [
            ("Tap tap!", "Rain."),
            ("Warm air", "lifts vapor."),
            ("High up,", "air cools."),
            ("Tiny drops", "make clouds."),
            ("Drops grow", "heavier."),
            ("Gravity =", "rain down."),
            ("Waters plants", "and soil."),
            ("Fills rivers", "and lakes."),
            ("Too much?", "Big puddles."),
            ("Too little?", "Thirsty."),
            ("Water on", "the move."),
            ("Sky shares", "a drink."),
        ],
        "scenes": [
            "Cozy window rainy day; drops on glass; robot and boy watch; empty speech bubbles",
            "Warm ground steam vapor rising soft cartoon; empty speech bubbles",
            "Cool high sky layer soft blues; empty speech bubbles",
            "Fluffy cloud forming from tiny droplets; empty speech bubbles",
            "Cloud droplets growing bigger; empty speech bubbles",
            "Rain falling to ground park; empty speech bubbles",
            "Green plants drinking rain; boy smiles; empty speech bubbles",
            "River filling after rain soft landscape; empty speech bubbles",
            "Big puddles gentle not scary flood; boots splash; empty speech bubbles",
            "Dry cracked soil thirsty soft concern; empty speech bubbles",
            "Water cycle soft loop arrows; robot teaches; empty speech bubbles",
            "Warm ending listening to rain with cocoa; empty speech bubbles",
        ],
    },
    "E-W04": {
        "title": "Why Does Thunder Follow Lightning?",
        "folder": "Weather",
        "tag": "Thunder",
        "pages": [
            "Flash first… then comes the boom.",
            "Lightning is a giant spark in the sky.",
            "The spark heats air incredibly fast.",
            "Hot air expands in a sudden shock.",
            "That shock is the sound we call thunder.",
            "Light races much faster than sound.",
            "So we see the flash before we hear the rumble.",
            "Counting seconds after a flash can hint distance.",
            "But the safe rule is simpler.",
            "If you hear thunder, head indoors.",
            "Go with a grown-up. Stay cozy and dry.",
            "Storm science and storm safety stay together.",
        ],
        "bubbles": [
            ("Flash first,", "then boom."),
            ("Giant spark", "in sky."),
            ("Heats air", "so fast."),
            ("Air expands", "shock!"),
            ("Shock =", "thunder."),
            ("Light faster", "than sound."),
            ("See first,", "hear later."),
            ("Count seconds", "for distance."),
            ("Safer rule", "is simple."),
            ("Hear thunder?", "Go inside."),
            ("With grown-up.", "Stay dry."),
            ("Science +", "safety."),
        ],
        "scenes": [
            "Soft stormy window; gentle flash then sound waves; not scary; empty speech bubbles",
            "Friendly cartoon lightning spark in cloud; soft colors; empty speech bubbles",
            "Air heating lines around spark soft diagram; empty speech bubbles",
            "Expanding air shock rings soft; empty speech bubbles",
            "Boy hears boom; robot explains calmly; empty speech bubbles",
            "Race metaphor: light beam beats sound wave; empty speech bubbles",
            "Flash then delayed rumble timeline soft; empty speech bubbles",
            "Boy counts on fingers after flash; empty speech bubbles",
            "Robot holds simple safe rule sign soft; empty speech bubbles",
            "Boy and robot hurry indoors kindly; empty speech bubbles",
            "Cozy indoor with grown-up; rain outside; empty speech bubbles",
            "Warm ending safe indoors; storm science smile; empty speech bubbles",
        ],
    },
    "E-W05": {
        "title": "Why Does It Snow?",
        "folder": "Weather",
        "tag": "Snow",
        "pages": [
            "Soft flakes fall. Quiet white!",
            "When clouds are cold enough, water can freeze.",
            "Ice crystals begin to grow.",
            "Crystals stick together into flakes.",
            "Flakes drift down if the air stays cold.",
            "If air is too warm, flakes may melt to rain.",
            "Every flake grows with a pattern.",
            "No two flake journeys are identical.",
            "Snow is winter's quiet rain of crystals.",
            "Snow can blanket soil and sleep seeds.",
            "Boots, hats, and gentle play keep toes warm.",
            "Catch one flake—then smile at winter science.",
        ],
        "bubbles": [
            ("Soft flakes!", "Quiet white."),
            ("Cold clouds", "freeze water."),
            ("Ice crystals", "grow."),
            ("Crystals stick", "into flakes."),
            ("Cold air", "lets them fall."),
            ("Too warm?", "Melts to rain."),
            ("Each flake", "has pattern."),
            ("No two", "same journey."),
            ("Quiet rain", "of crystals."),
            ("Blankets soil,", "sleeps seeds."),
            ("Warm boots", "and hats."),
            ("Catch one.", "Smile."),
        ],
        "scenes": [
            "Gentle snowfall park; robot and boy catch flakes; empty speech bubbles",
            "Cold cloud with freeze sparkles soft; empty speech bubbles",
            "Close friendly ice crystal growing; empty speech bubbles",
            "Crystals joining into flake; empty speech bubbles",
            "Flakes drifting down cold air; empty speech bubbles",
            "Warm air melting flake into drop soft; empty speech bubbles",
            "Pretty unique flake patterns display; empty speech bubbles",
            "Two different flake journeys side by side; empty speech bubbles",
            "Quiet winter field crystal rain feel; empty speech bubbles",
            "Snow blanket over garden soil; empty speech bubbles",
            "Boy in hat and boots; robot cozy; empty speech bubbles",
            "Warm ending catching flake on mitten; empty speech bubbles",
        ],
    },
}


def validate() -> None:
    for sid, st in STORIES.items():
        assert len(st["pages"]) == 12 and len(st["bubbles"]) == 12 and len(st["scenes"]) == 12
        words = []
        for i, page in enumerate(st["pages"], 1):
            w = len(page.split())
            words.append(w)
            if not (5 <= w <= 28):
                raise SystemExit(f"bad word count {sid} {i}: {w} — {page}")
        print(f"{sid} TOTAL {sum(words)} words, mean {sum(words)/12:.1f}")


def main() -> None:
    validate()
    text_map = {sid: "\n\n".join(st["pages"]) for sid, st in STORIES.items()}
    for rel in (
        "EyeHaven/BedtimeContentCatalog.en.json",
        "EyeHaven/BedtimeContentCatalog.json",
    ):
        path = ROOT / rel
        data = json.loads(path.read_text(encoding="utf-8"))
        for story in data["stories"]:
            if story["id"] in text_map:
                story["text"] = text_map[story["id"]]
        data["updatedAt"] = "2026-11-16"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print("updated", path)

    plan = []
    prompts = []
    ref_candidates = [
        Path("/Users/song/qwen3-tts/comic_batch/en_work/_raw_pilot/c-E-A01-01.jpg"),
        Path("/Users/song/qwen3-tts/comic_batch/guangguang_ref.png"),
    ]
    ref = next(str(p) for p in ref_candidates if p.exists())
    for sid, st in STORIES.items():
        panels = []
        for i, (scene, (left, right)) in enumerate(zip(st["scenes"], st["bubbles"]), 1):
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
            prompts.append(
                {
                    "id": sid,
                    "i": i,
                    "filename": f"c-{sid}-{i:02d}.jpg",
                    "description": PREFIX + scene,
                    "ref": ref,
                }
            )
        plan.append({"id": sid, "title": st["title"], "companion": "boy", "panels": panels})

    plan_path = Path("/Users/song/qwen3-tts/comic_batch/comics_plan_en_free_front5_w2.json")
    plan_path.write_text(json.dumps(plan, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("wrote", plan_path)

    prompts_path = Path("/Users/song/qwen3-tts/comic_batch/en_work/free_front5_w2_prompts.json")
    prompts_path.parent.mkdir(parents=True, exist_ok=True)
    prompts_path.write_text(json.dumps(prompts, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("wrote", prompts_path, len(prompts))

    # merge into pilot plan for finalize tooling
    main_plan = Path("/Users/song/qwen3-tts/comic_batch/comics_plan_en_pilot12.json")
    if main_plan.exists():
        old = json.loads(main_plan.read_text(encoding="utf-8"))
        by_id = {ep["id"]: ep for ep in old}
        for ep in plan:
            by_id[ep["id"]] = ep
        main_plan.write_text(json.dumps(list(by_id.values()), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    for sid, st in STORIES.items():
        path = ROOT / "睡前有声稿" / "美国英文稿" / st["folder"] / f"{sid}.txt"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(st["title"] + "\n\n" + "\n\n".join(st["pages"]) + "\n", encoding="utf-8")
        print("wrote", path)


if __name__ == "__main__":
    main()
