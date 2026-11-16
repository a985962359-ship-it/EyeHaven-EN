#!/usr/bin/env python3
"""Back-catalog wave 16: How E-H20…E-H24 → 12-page books. Owner sleeping; no questions."""
from __future__ import annotations

import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PREFIX_BOY = (
    "Children's picture book comic panel, soft warm friendly science lighting, landscape 4:3. "
    "Cute round-headed white robot Guangguang with green trim, warm glowing chest lamp, small star on head, honest smile. "
    "Blonde boy about 6 years old with freckles wearing a blue T-rex hoodie with white sleeve stripes. "
    "Two large empty white oval speech bubbles with space for short kids text, blank inside, no letters. "
    "Soft friendly how-it-works science, gentle pastel, not scary. No text logos, consistent character design. "
    "Simple readable background, big clear shapes, shallow depth, soft edges, no clutter. "
)
PREFIX_GIRL = (
    "Children's picture book comic panel, soft warm friendly science lighting, landscape 4:3. "
    "Cute round-headed white robot Guangguang with green trim, warm glowing chest lamp, small star on head, honest smile. "
    "Gentle girl about 6–7 with soft sweater and kind smile. "
    "Two large empty white oval speech bubbles with space for short kids text, blank inside, no letters. "
    "Soft friendly how-it-works science, gentle pastel, not scary. No text logos, consistent character design. "
    "Simple readable background, big clear shapes, shallow depth, soft edges, no clutter. "
)

STORIES = {
    "E-H20": {
        "title": "Why Do Microwaves Heat Food Fast?",
        "folder": "How",
        "tag": "Micro",
        "companion": "boy",
        "pages": [
            'Beep. Steam rises. "How so quick?" asks Guangguang.',
            "Microwave ovens make special waves inside a metal box.",
            "Those waves jostle water molecules in the food.",
            "Jostling molecules make heat from the inside, not only the outside.",
            "A regular oven mostly warms from the outside in, which can take longer.",
            "Metal and some containers are unsafe—follow the manual with a grown-up.",
            "Stirring helps heat spread more evenly through the food.",
            "Hot spots can burn tongues, so wait and test carefully.",
            "Covers can reduce splatters while waves still reach the meal.",
            "Microwaves are water-molecule dance floors in a careful metal box.",
            "Never run empty tricks—ask a grown-up before any experiment.",
            "Waves jostle water: microwave science.",
        ],
        "bubbles": [
            ("Beep steam!", "So quick?"),
            ("Waves inside", "metal box."),
            ("Jostle water", "molecules."),
            ("Heat from", "inside too."),
            ("Ovens warm", "outside in."),
            ("Follow manual", "with help."),
            ("Stir for", "even heat."),
            ("Hot spots", "can burn."),
            ("Covers cut", "splatters."),
            ("Molecule dance", "floor."),
            ("Ask grown-up", "first."),
            ("Microwave", "science."),
        ],
        "scenes": [
            "WIDE soft kitchen microwave beep; boy and robot one-third; empty speech bubbles",
            "DIAGRAM-SOFT waves in metal box soft; tiny figures; empty speech bubbles",
            "CLOSE water molecules jostle soft; characters half frame; empty speech bubbles",
            "MEDIUM heat inside food soft; boy points; robot; empty speech bubbles",
            "PLAYFUL oven vs microwave soft; characters half frame; empty speech bubbles",
            "CLOSE manual with grown-up soft; characters half frame; empty speech bubbles",
            "MEDIUM stir food soft; characters half frame; empty speech bubbles",
            "CLOSE careful taste test soft; characters half frame; empty speech bubbles",
            "WIDE covered dish soft; characters one-third; empty speech bubbles",
            "PLAYFUL molecule dance soft; characters half frame; empty speech bubbles",
            "MEDIUM ask grown-up soft; boy and robot half frame; empty speech bubbles",
            "ENDING boy and robot thumbs-up soft; one-third; empty speech bubbles",
        ],
    },
    "E-H21": {
        "title": "Why Do Parachutes Slow Falls?",
        "folder": "How",
        "tag": "Chute",
        "companion": "boy",
        "pages": [
            'A silk umbrella blooms. "Why safer?" asks Guangguang.',
            "A parachute catches a lot of air as it opens.",
            "That big catch makes a drag force pushing upward against the fall.",
            "More area means more air resistance, so the descent slows.",
            "Free fall without a chute is much faster and not a game.",
            "Skydiving needs serious training—kids watch, not jump.",
            "Toy parachutes can show the idea safely indoors with a grown-up.",
            "Lines and canopy shape help the chute stay steady.",
            "Emergency chutes on some planes are carefully packed tools.",
            "Parachutes buy time by hugging a lot of air.",
            "Respect height rules on playgrounds and balconies always.",
            "Catch air, slow down: parachute science.",
        ],
        "bubbles": [
            ("Umbrella blooms!", "Safer?"),
            ("Catches lots", "of air."),
            ("Drag pushes", "up."),
            ("More area,", "slower fall."),
            ("Free fall", "not a game."),
            ("Training for", "real jumps."),
            ("Toy demos", "indoors."),
            ("Lines keep", "steady."),
            ("Packed tools", "ready."),
            ("Hugging air", "buys time."),
            ("Respect height", "rules."),
            ("Parachute", "science."),
        ],
        "scenes": [
            "WIDE soft sky parachute bloom gentle; boy and robot one-third; empty speech bubbles",
            "DIAGRAM-SOFT chute catching air soft; tiny figures; empty speech bubbles",
            "MEDIUM drag force up soft; characters one-third; empty speech bubbles",
            "CLOSE big canopy area soft; boy points; robot; empty speech bubbles",
            "PLAYFUL free fall vs chute soft; characters half frame; empty speech bubbles",
            "MEDIUM watch not jump soft; characters half frame; empty speech bubbles",
            "WIDE indoor toy chute soft; boy and robot one-third; empty speech bubbles",
            "CLOSE lines canopy soft; characters half frame; empty speech bubbles",
            "DIAGRAM-SOFT packed chute soft; tiny figures; empty speech bubbles",
            "PLAYFUL hugging air soft; characters half frame; empty speech bubbles",
            "MEDIUM height safety soft; characters half frame; empty speech bubbles",
            "ENDING boy and robot thumbs-up soft; one-third; empty speech bubbles",
        ],
    },
    "E-H22": {
        "title": "Why Do Locks Need Keys?",
        "folder": "How",
        "tag": "Lock",
        "companion": "girl",
        "pages": [
            'Click. The door opens. "How?" asks Guangguang.',
            "A key’s jagged edge lifts tiny pins inside the lock.",
            "When pins reach the matching height, the cylinder can turn.",
            "Wrong keys leave pins blocking so the lock stays shut.",
            "It is a tiny three-dimensional puzzle made of metal.",
            "Digital locks use codes or cards instead of teeth.",
            "Keep spare keys in a safe place with a grown-up’s plan.",
            "Never hide house keys under the mat for strangers to find.",
            "Oil and gentle care keep old locks from sticking.",
            "Keys are portable answers to a pin puzzle in metal.",
            "Ask before borrowing keys—they open more than toys.",
            "Pins, teeth, turn: lock-and-key science.",
        ],
        "bubbles": [
            ("Click open!", "How?"),
            ("Key lifts", "pins."),
            ("Matching height", "turns."),
            ("Wrong key", "blocks."),
            ("Tiny metal", "puzzle."),
            ("Codes replace", "teeth."),
            ("Spare keys", "stay safe."),
            ("No mat", "hiding."),
            ("Gentle care", "helps."),
            ("Portable puzzle", "answer."),
            ("Ask before", "borrow."),
            ("Lock-key", "science."),
        ],
        "scenes": [
            "WIDE soft front door key click; girl and robot one-third; empty speech bubbles",
            "DIAGRAM-SOFT key lifting pins soft; tiny figures; empty speech bubbles",
            "CLOSE matching pin height soft; characters half frame; empty speech bubbles",
            "MEDIUM wrong key blocked soft; girl points; robot; empty speech bubbles",
            "PLAYFUL 3D puzzle idea soft; characters half frame; empty speech bubbles",
            "WIDE digital keypad soft; characters one-third; empty speech bubbles",
            "CLOSE spare key safe soft; characters half frame; empty speech bubbles",
            "CLOSE no mat hide soft X; robot shake; empty speech bubbles",
            "MEDIUM oil care soft; characters half frame; empty speech bubbles",
            "DIAGRAM-SOFT portable answer soft; tiny figures; empty speech bubbles",
            "MEDIUM ask before borrow soft; girl and robot half frame; empty speech bubbles",
            "ENDING girl and robot soft smile; one-third; empty speech bubbles",
        ],
    },
    "E-H23": {
        "title": "Why Do Fans Cool Us If They Don’t Make Cold Air?",
        "folder": "How",
        "tag": "Fan",
        "companion": "boy",
        "pages": [
            'Whirr. "The air isn’t icy—why cooler?" asks Guangguang.',
            "Fans move air across your skin in a steady breeze.",
            "Moving air helps sweat evaporate faster.",
            "When sweat evaporates, it carries heat away from your body.",
            "The room air temperature may stay about the same.",
            "You feel cooler because heat leaves your skin quicker.",
            "In a sealed empty room with no people, a fan mostly just stirs air.",
            "Open windows can help move humid air out on sticky days.",
            "Keep fingers away from spinning blades—covers matter.",
            "Fan “cool” is evaporating-sweat express, not fridge wind.",
            "Sip water too; fans help comfort, not magic freeze.",
            "Breeze, evaporate, cool: fan science.",
        ],
        "bubbles": [
            ("Whirr!", "Why cooler?"),
            ("Moves air", "on skin."),
            ("Sweat dries", "faster."),
            ("Heat leaves", "with vapor."),
            ("Room temp", "similar."),
            ("You feel", "cooler."),
            ("Empty room,", "just stirs."),
            ("Windows help", "sticky days."),
            ("Fingers off", "blades."),
            ("Not fridge", "wind."),
            ("Sip water", "too."),
            ("Fan", "science."),
        ],
        "scenes": [
            "WIDE soft room fan breeze; boy and robot one-third; empty speech bubbles",
            "MEDIUM air across skin soft; characters one-third; empty speech bubbles",
            "DIAGRAM-SOFT sweat evaporate soft; tiny figures; empty speech bubbles",
            "CLOSE heat leaving soft; boy points; robot; empty speech bubbles",
            "PLAYFUL thermometer same soft; characters half frame; empty speech bubbles",
            "MEDIUM smile cooler soft; characters half frame; empty speech bubbles",
            "WIDE empty room fan soft; characters one-third; empty speech bubbles",
            "MEDIUM open window soft; characters one-third; empty speech bubbles",
            "CLOSE blade cover safe soft; characters half frame; empty speech bubbles",
            "PLAYFUL not fridge soft; characters half frame; empty speech bubbles",
            "CLOSE water sip soft; boy and robot half frame; empty speech bubbles",
            "ENDING boy and robot thumbs-up soft; one-third; empty speech bubbles",
        ],
    },
    "E-H24": {
        "title": "Why Do Velcro Stick and Peel?",
        "folder": "How",
        "tag": "Velcro",
        "companion": "girl",
        "pages": [
            'Rrrrip! "How does it stick and peel?" asks Guangguang.',
            "Velcro pairs tiny hooks with tiny loops.",
            "Pressing lets hooks catch the loops and hold on.",
            "Peeling unhooks them with that famous ripping sound.",
            "The idea was inspired by burrs stuck on clothes after a walk.",
            "Nature’s hitchhikers taught a useful fastening trick.",
            "Dirt fills loops and weakens the grip over time.",
            "A brush or gentle clean helps fuzzy sides work again.",
            "Shoes, bags, and jackets often use hook-and-loop strips.",
            "Velcro is miniature grappling hooks taught by burrs.",
            "Press firm, peel slow—and laugh at the rrrrip.",
            "Hooks meet loops: Velcro science.",
        ],
        "bubbles": [
            ("Rrrrip!", "How stick?"),
            ("Hooks meet", "loops."),
            ("Press to", "catch."),
            ("Peel makes", "the sound."),
            ("Burrs gave", "the idea."),
            ("Nature taught", "fastening."),
            ("Dirt weakens", "grip."),
            ("Clean fuzzy", "sides."),
            ("Shoes bags", "use it."),
            ("Tiny grappling", "hooks."),
            ("Press firm,", "peel slow."),
            ("Velcro", "science."),
        ],
        "scenes": [
            "WIDE soft jacket velcro rip; girl and robot one-third; empty speech bubbles",
            "DIAGRAM-SOFT hooks and loops soft; tiny figures; empty speech bubbles",
            "CLOSE press catch soft; characters half frame; empty speech bubbles",
            "PLAYFUL peel sound soft; girl points; robot; empty speech bubbles",
            "MEDIUM burrs on clothes soft; characters one-third; empty speech bubbles",
            "WIDE nature walk idea soft; characters one-third; empty speech bubbles",
            "CLOSE dirty loops soft; characters half frame; empty speech bubbles",
            "MEDIUM brush clean soft; characters half frame; empty speech bubbles",
            "WIDE shoes bags jackets soft; characters one-third; empty speech bubbles",
            "PLAYFUL grappling hooks soft; characters half frame; empty speech bubbles",
            "CLOSE press peel laugh soft; girl and robot half frame; empty speech bubbles",
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
    ref_dir = ROOT / ".comic_refs" / "w16_by_story"
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

    Path("/Users/song/qwen3-tts/comic_batch/comics_plan_en_backcatalog_w16.json").write_text(
        json.dumps(plan, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    Path("/Users/song/qwen3-tts/comic_batch/en_work/_raw_backcatalog_w16").mkdir(parents=True, exist_ok=True)
    Path("/Users/song/qwen3-tts/comic_batch/en_work/backcatalog_w16_prompts.json").write_text(
        json.dumps(prompts, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    bubbles_path = ROOT / "EyeHaven" / "ComicBubbleWords.en.json"
    bubbles = json.loads(bubbles_path.read_text(encoding="utf-8"))
    for sid, st in STORIES.items():
        bubbles[sid] = [{"i": i, "left": L, "right": R} for i, (L, R) in enumerate(st["bubbles"], 1)]
    bubbles_path.write_text(json.dumps(bubbles, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("wave16 done", len(STORIES), "prompts", len(prompts))


if __name__ == "__main__":
    main()
