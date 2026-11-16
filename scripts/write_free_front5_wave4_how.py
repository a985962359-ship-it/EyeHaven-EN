#!/usr/bin/env python3
"""Free-front-5 wave 4: How shelf gaps E-H02…E-H05 → 12-page books.

E-H01 already remodeled. Background: kid-friendly-backgrounds.md +
character-background-scale.md. Audio: VoiceDesign matched to art companion
(see docs/voice-match-art-casting.md). EN UI only (no Chinese on screen).
One kid per book; free How gaps ~half girl: H02/H04 boy; H03/H05 girl.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PREFIX_BOY = (
    "Children's picture book comic panel, soft warm friendly lighting, landscape 4:3. "
    "Cute round-headed white robot Guangguang with green trim, warm glowing chest lamp, "
    "small star on head, honest smile. Blonde boy about 6 years old wearing a blue T-rex hoodie. "
    "Two large empty white oval speech bubbles with space for short kids text, blank inside, no letters. "
    "No scary imagery, no text logos, consistent character design. "
    "Simple readable background, big clear shapes, shallow depth, soft edges, no clutter. "
)

PREFIX_GIRL = (
    "Children's picture book comic panel, soft warm friendly lighting, landscape 4:3. "
    "Cute round-headed white robot Guangguang with green trim, warm glowing chest lamp, "
    "small star on head, honest smile. Gentle girl about 6–7 with soft sweater and kind smile. "
    "Two large empty white oval speech bubbles with space for short kids text, blank inside, no letters. "
    "No scary imagery, no text logos, consistent character design. "
    "Simple readable background, big clear shapes, shallow depth, soft edges, no clutter. "
)

STORIES = {
    "E-H02": {
        "title": "Why Does Ice Melt?",
        "folder": "How",
        "tag": "Ice",
        "companion": "boy",
        "pages": [
            'An ice cube drips. "Disappearing act!"',
            "Ice is water frozen into a solid shape.",
            "Heat gives tiny bits of water more energy.",
            "They slip free of the stiff ice pattern.",
            "Then ice becomes liquid water you can pour.",
            "Warm air can melt a cube on the table.",
            "Warm hands melt ice even faster.",
            "Sunlight adds heat on a bright day too.",
            "Melting is not vanishing into nothing.",
            "It is water changing form—solid to liquid.",
            "Freeze it again and water can become ice.",
            "Same water, different costume—cool science!",
        ],
        "bubbles": [
            ("Drip drip!", "Gone?"),
            ("Ice = water", "frozen solid."),
            ("Heat gives", "more energy."),
            ("Bits slip", "free."),
            ("Now it's", "liquid."),
            ("Warm air", "melts it."),
            ("Warm hands", "faster!"),
            ("Sunlight", "helps too."),
            ("Not gone—", "changing."),
            ("Solid →", "liquid."),
            ("Freeze again", "→ ice."),
            ("Same water,", "cool!"),
        ],
        "scenes": [
            "WIDE kitchen table; ice cube dripping; characters one-third frame watching; empty speech bubbles",
            "CLOSE shiny ice cube; robot points; boy curious; half frame clear faces; empty speech bubbles",
            "DIAGRAM-SOFT tiny warm sparkles entering ice; characters small corner; empty speech bubbles",
            "DIAGRAM-SOFT ice lattice loosening into drops; tiny figures; empty speech bubbles",
            "MEDIUM glass of water from melt; characters half frame; empty speech bubbles",
            "MEDIUM sunny window table melt; characters half frame; empty speech bubbles",
            "CLOSE boy hands gently near ice not squeezing hard; robot coaches; half frame; empty speech bubbles",
            "WIDE backyard sunbeam on ice tray; characters one-third; empty speech bubbles",
            "SPLIT: ice vs puddle same place; soft labels none; characters half frame; empty speech bubbles",
            "PLAYFUL costume change metaphor: ice hat to water splash cute; half frame; empty speech bubbles",
            "MEDIUM freezer tray making ice again; characters half frame; empty speech bubbles",
            "ENDING thumbs-up smile; characters one-third frame; empty speech bubbles",
        ],
    },
    "E-H03": {
        "title": "Why Do Soap Bubbles Float?",
        "folder": "How",
        "tag": "Bubble",
        "companion": "girl",
        "pages": [
            "A bubble drifts up, then pops!",
            "A bubble is a thin soap-water skin.",
            "Inside the skin is a pocket of air.",
            "Soap makes that skin stretchy and strong.",
            "Warm air inside can help it lift a bit.",
            "Gentle breezes can carry bubbles along.",
            "Gravity still pulls, so they do not fly forever.",
            "As the skin dries, it gets thinner.",
            "When it thins too much—pop!",
            "Bubbles teach thin films and air together.",
            "Sparkle colors dance on the soap skin.",
            "Blow softly, watch, then smile at the pop.",
        ],
        "bubbles": [
            ("Up… then", "pop!"),
            ("Thin soap", "water skin."),
            ("Air pocket", "inside."),
            ("Soap makes", "it stretchy."),
            ("Warm air", "lifts a bit."),
            ("Breezes", "carry them."),
            ("Gravity", "still pulls."),
            ("Skin dries", "thinner."),
            ("Too thin—", "pop!"),
            ("Films + air", "lesson."),
            ("Rainbow", "sparkle!"),
            ("Soft blow,", "smile."),
        ],
        "scenes": [
            "WIDE sunny yard; bubble rising; girl and robot one-third frame; empty speech bubbles",
            "CLOSE bubble wand with film; characters half frame; empty speech bubbles",
            "DIAGRAM-SOFT cutaway bubble air inside; tiny figures; empty speech bubbles",
            "MEDIUM stretchy film demo soft; characters half frame; empty speech bubbles",
            "CLOSE warm shimmer inside bubble; half frame faces; empty speech bubbles",
            "WIDE bubbles drifting on breeze; characters one-third; empty speech bubbles",
            "MEDIUM bubble slowly sinking feel; characters half frame; empty speech bubbles",
            "CLOSE drying thinner film soft; tiny sparkles; empty speech bubbles",
            "ACTION playful pop splash droplets soft; characters half frame; empty speech bubbles",
            "DIAGRAM-SOFT thin film + air icons kid-safe; tiny figures; empty speech bubbles",
            "CLOSE colorful soap sheen; girl amazed; robot smiles; half frame; empty speech bubbles",
            "ENDING both laughing after pop; one-third frame; empty speech bubbles",
        ],
    },
    "E-H04": {
        "title": "Why Do Balloons Float Up?",
        "folder": "How",
        "tag": "Balloon",
        "companion": "boy",
        "pages": [
            "A helium balloon tugs the string skyward.",
            "Helium is lighter than the air around us.",
            "A balloon full of helium weighs less.",
            "Less than the same-sized blob of regular air.",
            "Denser air pushes up, so the balloon rises.",
            "It is a bit like wood floating on water—but in air.",
            "Regular breath balloons usually fall down.",
            "Your breath is not lighter than outside air.",
            "Hold strings gently when you walk outside.",
            "Let balloons go only where it is safe.",
            "And only where grown-ups say it is allowed.",
            "Light gas, gentle hands, happy sky tug!",
        ],
        "bubbles": [
            ("String tugs", "up!"),
            ("Helium", "is lighter."),
            ("Balloon weighs", "less."),
            ("Less than", "same air."),
            ("Air pushes", "up."),
            ("Like float,", "but air."),
            ("Breath balloon", "falls."),
            ("Breath ≠", "lighter."),
            ("Hold string", "gently."),
            ("Only safe", "places."),
            ("Ask grown-ups", "first."),
            ("Light gas,", "yay!"),
        ],
        "scenes": [
            "WIDE park boy holding helium balloon string; robot beside; one-third frame; empty speech bubbles",
            "DIAGRAM-SOFT light helium dots vs heavier air; tiny figures; empty speech bubbles",
            "MEDIUM floating balloon cluster soft; characters half frame; empty speech bubbles",
            "SPLIT: helium up vs air blob; soft; characters half frame; empty speech bubbles",
            "CLOSE balloon rising tug; faces half frame; empty speech bubbles",
            "PLAYFUL wood-on-water metaphor puddle boat; tiny characters; empty speech bubbles",
            "MEDIUM breath balloon on floor; characters half frame shrug smile; empty speech bubbles",
            "CLOSE boy blowing regular balloon; robot explains; half frame; empty speech bubbles",
            "WIDE sidewalk walk holding string carefully; one-third; empty speech bubbles",
            "MEDIUM kind adult nearby nod; characters half frame; empty speech bubbles",
            "CLOSE safety reminder soft stop hand cute; half frame; empty speech bubbles",
            "ENDING happy balloon picnic; characters one-third; empty speech bubbles",
        ],
    },
    "E-H05": {
        "title": "Why Do Some Things Float?",
        "folder": "How",
        "tag": "Float",
        "companion": "girl",
        "pages": [
            "A leaf rides a puddle; a pebble sinks.",
            "Floating depends on density—how packed stuff is.",
            "Shape matters too, not only weight.",
            "If something pushes aside heavy water, it can float.",
            "The water it moves can weigh more than the object.",
            "Boats use hollow shapes to displace lots of water.",
            "That is why a big empty boat can float.",
            "Heavy metal can float as a boat shape.",
            "But the same metal as a tight ball may sink.",
            "Shape and density work as a team.",
            "Try a leaf, a pebble, and a toy boat.",
            "Watch who rides—and who takes a dive!",
        ],
        "bubbles": [
            ("Leaf rides!", "Pebble sinks."),
            ("Density =", "how packed."),
            ("Shape", "matters too."),
            ("Push water", "aside…"),
            ("…water can", "weigh more."),
            ("Hollow boats", "displace lots."),
            ("Empty boat", "can float."),
            ("Metal boat", "can float."),
            ("Metal ball", "may sink."),
            ("Shape +", "density."),
            ("Try leaf,", "pebble, boat."),
            ("Who rides?", "Who dives?"),
        ],
        "scenes": [
            "WIDE puddle leaf floating pebble sunk; girl and robot one-third watching; empty speech bubbles",
            "DIAGRAM-SOFT packed dots density idea; tiny figures; empty speech bubbles",
            "MEDIUM toy shapes compare; girl and robot half frame; empty speech bubbles",
            "DIAGRAM-SOFT object pushing water aside soft; tiny figures; empty speech bubbles",
            "CLOSE water line rising around boat; girl watches half frame; empty speech bubbles",
            "WIDE bathtub toy boat hollow; girl and robot one-third; empty speech bubbles",
            "MEDIUM big soft cartoon boat smile; girl and robot half frame; empty speech bubbles",
            "SPLIT metal boat vs metal ball in water; girl and robot half frame; empty speech bubbles",
            "CLOSE sinking ball bubbles soft; robot points; girl curious half frame; empty speech bubbles",
            "MEDIUM high-five density+shape team icons; girl and robot half frame; empty speech bubbles",
            "ACTION science tray leaf pebble boat; girl and robot half frame; empty speech bubbles",
            "ENDING splash laugh puddle play; girl and robot one-third frame; empty speech bubbles",
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
        print(f"{sid} TOTAL {sum(words)} words, mean {sum(words)/12:.1f}, companion={st['companion']}")


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
        data["updatedAt"] = "2026-11-17"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print("updated", path)

    plan = []
    prompts = []
    boy_ref = Path("/Users/song/qwen3-tts/comic_batch/en_boy_ref.png")
    girl_ref = Path("/Users/song/qwen3-tts/comic_batch/en_girl_ref.png")
    gg_ref = Path("/Users/song/qwen3-tts/comic_batch/guangguang_ref.png")
    # workspace copies if comic_batch refs fail for GenerateImage
    local_refs = ROOT / "scripts" / "comic_refs"
    local_refs.mkdir(parents=True, exist_ok=True)

    for sid, st in STORIES.items():
        prefix = PREFIX_GIRL if st["companion"] == "girl" else PREFIX_BOY
        kid = girl_ref if st["companion"] == "girl" else boy_ref
        refs = [str(p) for p in (gg_ref, kid) if p.exists()]
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
                    "description": prefix + "Scene: " + scene,
                    "refs": refs,
                }
            )
        plan.append({"id": sid, "title": st["title"], "companion": st["companion"], "panels": panels})

    plan_path = Path("/Users/song/qwen3-tts/comic_batch/comics_plan_en_free_front5_w4.json")
    plan_path.write_text(json.dumps(plan, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("wrote", plan_path)

    raw_dir = Path("/Users/song/qwen3-tts/comic_batch/en_work/_raw_free_front5_w4")
    raw_dir.mkdir(parents=True, exist_ok=True)
    prompts_path = Path("/Users/song/qwen3-tts/comic_batch/en_work/free_front5_w4_prompts.json")
    prompts_path.write_text(json.dumps(prompts, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("wrote", prompts_path, len(prompts))

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

    bubble_path = ROOT / "EyeHaven" / "ComicBubbleWords.en.json"
    bubbles = json.loads(bubble_path.read_text(encoding="utf-8")) if bubble_path.exists() else {}
    for sid, st in STORIES.items():
        bubbles[sid] = [
            {"i": i, "left": left, "right": right}
            for i, (left, right) in enumerate(st["bubbles"], 1)
        ]
    bubble_path.write_text(json.dumps(bubbles, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("updated", bubble_path, "stories", len(bubbles))


if __name__ == "__main__":
    main()
