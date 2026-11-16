#!/usr/bin/env python3
"""Back-catalog wave 26: Safety E-Z06…E-Z13 → 12-page books. Owner sleeping; no questions."""
from __future__ import annotations

import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PREFIX_BOY = (
    "Children's picture book comic panel, soft warm friendly safety lighting, landscape 4:3. "
    "Cute round-headed white robot Guangguang with green trim, warm glowing chest lamp, small star on head, honest smile. "
    "Blonde boy about 6 years old with freckles wearing a blue T-rex hoodie with white sleeve stripes. "
    "Two large empty white oval speech bubbles with space for short kids text, blank inside, no letters. "
    "Soft friendly kid safety, gentle pastel, not scary. No text logos, consistent character design. "
    "Simple readable background, big clear shapes, shallow depth, soft edges, no clutter. "
)
PREFIX_GIRL = (
    "Children's picture book comic panel, soft warm friendly safety lighting, landscape 4:3. "
    "Cute round-headed white robot Guangguang with green trim, warm glowing chest lamp, small star on head, honest smile. "
    "Gentle girl about 6–7 with soft sweater and kind smile. "
    "Two large empty white oval speech bubbles with space for short kids text, blank inside, no letters. "
    "Soft friendly kid safety, gentle pastel, not scary. No text logos, consistent character design. "
    "Simple readable background, big clear shapes, shallow depth, soft edges, no clutter. "
)

STORIES = {
    "E-Z06": {
        "title": "Outdoor Light Helps Eyes",
        "folder": "Safety",
        "tag": "Outdoor",
        "companion": "girl",
        "pages": [
            'Mia steps into soft daylight. "Outdoor light helps eyes?"',
            "Natural light is gentler than staring at one bright screen.",
            "Looking far across a park gives eye muscles a stretch.",
            "A short outdoor break can rest tired near-focus eyes.",
            "Sunglasses help on very bright days—ask a grown-up.",
            "Shade trees and hats can soften strong sun.",
            "Play catch or walk—moving eyes feel happier.",
            "Indoor lamps still help when days are short.",
            "Balance screen time with outdoor looks.",
            "Far light + blinks = kinder eyes.",
            "Take a ten-minute outdoor peek with a grown-up.",
            "Daylight pause: eye-care science.",
        ],
        "bubbles": [
            ("Daylight!", "Helps eyes?"),
            ("Softer than", "one screen."),
            ("Looking far", "stretches."),
            ("Short break", "rests eyes."),
            ("Sunglasses if", "very bright."),
            ("Shade and hats", "help."),
            ("Play and walk", "happy eyes."),
            ("Lamps help", "short days."),
            ("Balance screens", "outdoors."),
            ("Far light", "kinder."),
            ("Ten-minute peek", "together."),
            ("Eye-care", "science."),
        ],
        "scenes": [
            "WIDE soft park daylight step out; girl and robot one-third; empty speech bubbles",
            "DIAGRAM-SOFT natural vs screen soft; tiny figures; empty speech bubbles",
            "CLOSE look far park soft; girl points; robot; empty speech bubbles",
            "MEDIUM outdoor break soft; characters half frame; empty speech bubbles",
            "PLAYFUL sunglasses grown-up soft; characters half frame; empty speech bubbles",
            "WIDE shade hat soft; characters one-third; empty speech bubbles",
            "CLOSE play catch soft; characters half frame; empty speech bubbles",
            "MEDIUM indoor lamp soft; characters half frame; empty speech bubbles",
            "PLAYFUL balance screens soft; characters half frame; empty speech bubbles",
            "DIAGRAM-SOFT far light blinks soft; tiny figures; empty speech bubbles",
            "MEDIUM ten-minute peek soft; girl and robot half frame; empty speech bubbles",
            "ENDING girl and robot soft smile; one-third; empty speech bubbles",
        ],
    },
    "E-Z07": {
        "title": "Hot Stove, Cool Hands",
        "folder": "Safety",
        "tag": "Stove",
        "companion": "boy",
        "pages": [
            'A stove glows. "Hot stove—cool hands," says Guangguang.',
            "Burners and pots can stay hot after cooking.",
            "Keep a safe step-back space from the stove.",
            "Only grown-ups turn knobs and move hot pans.",
            "Handles should point inward so sleeves don’t catch.",
            "If something spills hot, call a grown-up—don’t wipe alone.",
            "Oven mitts are for helpers who know how.",
            "Curious sniffing from afar is safer than touching.",
            "A kitchen timer reminds everyone to check safely.",
            "Hot means grown-up zone.",
            "Practice pointing to the stove’s safe line together.",
            "Cool hands: kitchen safety.",
        ],
        "bubbles": [
            ("Stove hot!", "Cool hands."),
            ("Pots stay hot", "after."),
            ("Step back", "space."),
            ("Grown-ups turn", "knobs."),
            ("Handles point", "in."),
            ("Hot spill? Call", "grown-up."),
            ("Mitts for", "helpers."),
            ("Sniff afar,", "don’t touch."),
            ("Timer helps", "check."),
            ("Hot = grown-up", "zone."),
            ("Point safe line", "together."),
            ("Kitchen", "safety."),
        ],
        "scenes": [
            "WIDE soft kitchen stove glow safe; boy and robot one-third; empty speech bubbles",
            "CLOSE pots stay hot soft; boy points; robot; empty speech bubbles",
            "MEDIUM step-back space soft; characters half frame; empty speech bubbles",
            "PLAYFUL grown-up knobs soft; characters half frame; empty speech bubbles",
            "WIDE handles inward soft; characters one-third; empty speech bubbles",
            "CLOSE call grown-up spill soft; characters half frame; empty speech bubbles",
            "MEDIUM oven mitts soft; characters half frame; empty speech bubbles",
            "PLAYFUL sniff afar soft; characters half frame; empty speech bubbles",
            "CLOSE timer check soft; characters half frame; empty speech bubbles",
            "DIAGRAM-SOFT grown-up zone soft; tiny figures; empty speech bubbles",
            "MEDIUM point safe line soft; boy and robot half frame; empty speech bubbles",
            "ENDING boy and robot soft smile; one-third; empty speech bubbles",
        ],
    },
    "E-Z08": {
        "title": "Knives Are for Grown-Ups",
        "folder": "Safety",
        "tag": "Knives",
        "companion": "girl",
        "pages": [
            'Mia sees a cutting board. "Knives are for grown-ups."',
            "Sharp edges cut food—and can cut skin.",
            "Kids can wash fruit or tear lettuce instead.",
            "Ask before touching any tool in the drawer.",
            "Grown-ups keep knives pointed down and away.",
            "Plastic kid cutters are different—still ask first.",
            "If a knife falls, step back; don’t catch it.",
            "A safe helper job: carry plates with two hands.",
            "Praise careful hands more than fast hands.",
            "Sharp = grown-up tool.",
            "Choose a no-knife helper task together.",
            "Careful kitchen: tool safety.",
        ],
        "bubbles": [
            ("Cutting board!", "Grown-ups."),
            ("Sharp cuts food", "and skin."),
            ("Wash fruit,", "tear lettuce."),
            ("Ask before", "tools."),
            ("Point knives", "down."),
            ("Kid cutters?", "Still ask."),
            ("Falls? Step", "back."),
            ("Carry plates", "two hands."),
            ("Careful beats", "fast."),
            ("Sharp = grown-up", "tool."),
            ("Pick helper task", "together."),
            ("Tool", "safety."),
        ],
        "scenes": [
            "WIDE soft kitchen cutting board; girl and robot one-third; empty speech bubbles",
            "DIAGRAM-SOFT sharp edge soft gentle; tiny figures; empty speech bubbles",
            "CLOSE wash fruit soft; girl points; robot; empty speech bubbles",
            "MEDIUM ask before tools soft; characters half frame; empty speech bubbles",
            "PLAYFUL knife point down soft; characters half frame; empty speech bubbles",
            "WIDE ask kid cutter soft; characters one-third; empty speech bubbles",
            "CLOSE step back fall soft; characters half frame; empty speech bubbles",
            "MEDIUM carry plates soft; characters half frame; empty speech bubbles",
            "PLAYFUL careful hands soft; characters half frame; empty speech bubbles",
            "DIAGRAM-SOFT grown-up tool soft; tiny figures; empty speech bubbles",
            "MEDIUM helper task soft; girl and robot half frame; empty speech bubbles",
            "ENDING girl and robot soft smile; one-third; empty speech bubbles",
        ],
    },
    "E-Z09": {
        "title": "Medicine Is Not Candy",
        "folder": "Safety",
        "tag": "Medicine",
        "companion": "boy",
        "pages": [
            'Colorful pills in a bottle. "Not candy," warns Guangguang.',
            "Medicine can look sweet but is measured for bodies.",
            "Only a grown-up or nurse gives the right dose.",
            "Never share medicine with friends.",
            "Closed cabinets keep bottles out of little hands.",
            "If you find a pill on the floor, tell an adult.",
            "Vitamins also need grown-up rules.",
            "Stickers and cartoons on bottles don’t mean treats.",
            "Feeling sick? Describe it; don’t self-dose.",
            "Medicine = grown-up job.",
            "Practice “tell an adult” with a pretend bottle.",
            "Not candy: medicine safety.",
        ],
        "bubbles": [
            ("Pretty pills!", "Not candy."),
            ("Measured for", "bodies."),
            ("Grown-up gives", "dose."),
            ("Never share", "medicine."),
            ("Closed cabinets", "safe."),
            ("Floor pill? Tell", "adult."),
            ("Vitamins need", "rules too."),
            ("Cartoons ≠", "treats."),
            ("Sick? Describe,", "don’t dose."),
            ("Medicine =", "grown-up job."),
            ("Practice tell", "adult."),
            ("Medicine", "safety."),
        ],
        "scenes": [
            "WIDE soft bathroom cabinet closed; boy and robot one-third; empty speech bubbles",
            "DIAGRAM-SOFT measured dose soft; tiny figures; empty speech bubbles",
            "CLOSE grown-up gives soft; boy points; robot; empty speech bubbles",
            "MEDIUM never share soft; characters half frame; empty speech bubbles",
            "PLAYFUL closed cabinet soft; characters half frame; empty speech bubbles",
            "WIDE tell adult floor pill soft; characters one-third; empty speech bubbles",
            "CLOSE vitamins rules soft; characters half frame; empty speech bubbles",
            "MEDIUM cartoons not treats soft; characters half frame; empty speech bubbles",
            "PLAYFUL describe sick soft; characters half frame; empty speech bubbles",
            "DIAGRAM-SOFT grown-up job soft; tiny figures; empty speech bubbles",
            "MEDIUM practice tell soft; boy and robot half frame; empty speech bubbles",
            "ENDING boy and robot soft smile; one-third; empty speech bubbles",
        ],
    },
    "E-Z10": {
        "title": "Don’t Climb on Furniture",
        "folder": "Safety",
        "tag": "Climb",
        "companion": "girl",
        "pages": [
            'Mia eyes a bookshelf. "Don’t climb furniture."',
            "Shelves and dressers can tip if pulled.",
            "Climbing chairs to reach high things can slip.",
            "Ask a grown-up to get the high toy.",
            "Anchored furniture is safer—grown-ups check straps.",
            "Sofas are for sitting, not launching.",
            "Build forts on the floor with pillows instead.",
            "If something wobbles, step away and call help.",
            "Proud feet stay on the floor or playgrounds.",
            "High reach = ask, don’t climb.",
            "Practice asking for the high shelf together.",
            "Steady home: furniture safety.",
        ],
        "bubbles": [
            ("Bookshelf!", "Don’t climb."),
            ("Shelves can", "tip."),
            ("Chairs can", "slip."),
            ("Ask for high", "toys."),
            ("Anchors keep", "safer."),
            ("Sofas for", "sitting."),
            ("Floor forts", "instead."),
            ("Wobble? Step", "away."),
            ("Feet on floor", "or parks."),
            ("High? Ask,", "don’t climb."),
            ("Practice ask", "together."),
            ("Furniture", "safety."),
        ],
        "scenes": [
            "WIDE soft living room bookshelf; girl and robot one-third; empty speech bubbles",
            "DIAGRAM-SOFT tip risk soft gentle; tiny figures; empty speech bubbles",
            "CLOSE chair slip soft; girl points; robot; empty speech bubbles",
            "MEDIUM ask high toy soft; characters half frame; empty speech bubbles",
            "PLAYFUL anchored furniture soft; characters half frame; empty speech bubbles",
            "WIDE sofa sitting soft; characters one-third; empty speech bubbles",
            "CLOSE floor fort pillows soft; characters half frame; empty speech bubbles",
            "MEDIUM wobble step away soft; characters half frame; empty speech bubbles",
            "PLAYFUL feet on floor soft; characters half frame; empty speech bubbles",
            "DIAGRAM-SOFT ask don’t climb soft; tiny figures; empty speech bubbles",
            "MEDIUM practice ask soft; girl and robot half frame; empty speech bubbles",
            "ENDING girl and robot soft smile; one-third; empty speech bubbles",
        ],
    },
    "E-Z11": {
        "title": "Smoke Alarm Means Go Outside",
        "folder": "Safety",
        "tag": "Alarm",
        "companion": "boy",
        "pages": [
            'Beep-beep practice. "Smoke alarm means go outside."',
            "The loud sound is a helper, not a monster.",
            "Leave toys; walk quickly to the meeting place.",
            "Stay low if air feels smoky—grown-ups lead.",
            "Never hide; firefighters look for you outside.",
            "Feel doors with a grown-up before opening.",
            "Call emergency numbers only with an adult plan.",
            "Practice drills make real days calmer.",
            "Batteries in alarms are grown-up check jobs.",
            "Hear beep → go out → stay together.",
            "Walk the family exit path once together.",
            "Alarm helper: fire drill safety.",
        ],
        "bubbles": [
            ("Beep beep!", "Go outside."),
            ("Loud helper,", "not monster."),
            ("Leave toys;", "meeting place."),
            ("Stay low if", "smoky."),
            ("Don’t hide;", "go out."),
            ("Feel doors with", "grown-up."),
            ("Adults call", "help."),
            ("Drills make", "calm."),
            ("Battery checks", "grown-ups."),
            ("Beep → out →", "together."),
            ("Walk exit path", "once."),
            ("Fire-drill", "safety."),
        ],
        "scenes": [
            "WIDE soft home smoke alarm practice; boy and robot one-third; empty speech bubbles",
            "CLOSE loud helper soft; boy points; robot; empty speech bubbles",
            "MEDIUM meeting place soft; characters half frame; empty speech bubbles",
            "PLAYFUL stay low soft gentle; characters half frame; empty speech bubbles",
            "WIDE outside not hide soft; characters one-third; empty speech bubbles",
            "CLOSE feel door soft; characters half frame; empty speech bubbles",
            "MEDIUM adult call soft; characters half frame; empty speech bubbles",
            "PLAYFUL calm drill soft; characters half frame; empty speech bubbles",
            "CLOSE battery grown-up soft; characters half frame; empty speech bubbles",
            "DIAGRAM-SOFT beep out together soft; tiny figures; empty speech bubbles",
            "MEDIUM walk exit soft; boy and robot half frame; empty speech bubbles",
            "ENDING boy and robot soft smile; one-third; empty speech bubbles",
        ],
    },
    "E-Z12": {
        "title": "Stop, Look, Listen at Crossings",
        "folder": "Safety",
        "tag": "Crossing",
        "companion": "girl",
        "pages": [
            'Curb edge. "Stop, look, listen," says Mia.',
            "Stop at the edge before wheels or feet go.",
            "Look left, right, then left again for cars.",
            "Listen for engines, bells, and horns.",
            "Cross with a grown-up on busy streets.",
            "Make eye contact with drivers when you can.",
            "Phones wait—eyes on the road first.",
            "Rain and dark need extra careful looking.",
            "Bike riders follow the same stop-look-listen.",
            "Pause → eyes → ears → then go.",
            "Practice at a quiet corner with a grown-up.",
            "Street smart: crossing safety.",
        ],
        "bubbles": [
            ("Curb edge!", "Stop look listen."),
            ("Stop before", "going."),
            ("Left right", "left."),
            ("Listen for", "cars."),
            ("Busy? Cross with", "grown-up."),
            ("Eye contact", "drivers."),
            ("Phones wait;", "eyes first."),
            ("Rain dark:", "extra care."),
            ("Bikes same", "rule."),
            ("Pause eyes", "ears go."),
            ("Practice corner", "together."),
            ("Crossing", "safety."),
        ],
        "scenes": [
            "WIDE soft quiet street curb; girl and robot one-third; empty speech bubbles",
            "CLOSE stop at edge soft; girl points; robot; empty speech bubbles",
            "MEDIUM look left right soft; characters half frame; empty speech bubbles",
            "PLAYFUL listen engines soft; characters half frame; empty speech bubbles",
            "WIDE cross with grown-up soft; characters one-third; empty speech bubbles",
            "CLOSE eye contact soft; characters half frame; empty speech bubbles",
            "MEDIUM phones wait soft; characters half frame; empty speech bubbles",
            "PLAYFUL rain dark care soft; characters half frame; empty speech bubbles",
            "CLOSE bike same rule soft; characters half frame; empty speech bubbles",
            "DIAGRAM-SOFT pause eyes ears soft; tiny figures; empty speech bubbles",
            "MEDIUM practice corner soft; girl and robot half frame; empty speech bubbles",
            "ENDING girl and robot soft smile; one-third; empty speech bubbles",
        ],
    },
    "E-Z13": {
        "title": "Wait for the Green Light",
        "folder": "Safety",
        "tag": "GreenLight",
        "companion": "boy",
        "pages": [
            'Traffic light. "Wait for green," says Max.',
            "Red means stop; green means check then go.",
            "Yellow means get ready to stop—don’t rush.",
            "Walk signals show a person or a hand.",
            "Even on green, look both ways once more.",
            "Turning cars may still move—stay alert.",
            "Hold a grown-up’s hand at big lights.",
            "Never dart between parked cars.",
            "Patience keeps toes safer than hurry.",
            "Light color is a shared street language.",
            "Watch one full light cycle together.",
            "Green means go carefully: light safety.",
        ],
        "bubbles": [
            ("Traffic light!", "Wait green."),
            ("Red stop;", "green check."),
            ("Yellow: ready", "to stop."),
            ("Walk signal", "helps."),
            ("Green still look", "both ways."),
            ("Watch turning", "cars."),
            ("Hold hand at", "big lights."),
            ("No darting", "between cars."),
            ("Patience beats", "hurry."),
            ("Colors are", "street talk."),
            ("Watch one cycle", "together."),
            ("Light", "safety."),
        ],
        "scenes": [
            "WIDE soft city crosswalk light; boy and robot one-third; empty speech bubbles",
            "DIAGRAM-SOFT red green soft; tiny figures; empty speech bubbles",
            "CLOSE yellow ready soft; boy points; robot; empty speech bubbles",
            "MEDIUM walk signal soft; characters half frame; empty speech bubbles",
            "PLAYFUL look both ways soft; characters half frame; empty speech bubbles",
            "WIDE turning cars soft; characters one-third; empty speech bubbles",
            "CLOSE hold hand soft; characters half frame; empty speech bubbles",
            "MEDIUM no dart soft; characters half frame; empty speech bubbles",
            "PLAYFUL patience soft; characters half frame; empty speech bubbles",
            "DIAGRAM-SOFT street language soft; tiny figures; empty speech bubbles",
            "MEDIUM watch cycle soft; boy and robot half frame; empty speech bubbles",
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
    ref_dir = ROOT / ".comic_refs" / "w26_by_story"
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

    Path("/Users/song/qwen3-tts/comic_batch/comics_plan_en_backcatalog_w26.json").write_text(
        json.dumps(plan, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    Path("/Users/song/qwen3-tts/comic_batch/en_work/_raw_backcatalog_w26").mkdir(parents=True, exist_ok=True)
    Path("/Users/song/qwen3-tts/comic_batch/en_work/backcatalog_w26_prompts.json").write_text(
        json.dumps(prompts, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    bubbles_path = ROOT / "EyeHaven" / "ComicBubbleWords.en.json"
    bubbles = json.loads(bubbles_path.read_text(encoding="utf-8"))
    for sid, st in STORIES.items():
        bubbles[sid] = [{"i": i, "left": L, "right": R} for i, (L, R) in enumerate(st["bubbles"], 1)]
    bubbles_path.write_text(json.dumps(bubbles, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("wave26 done", len(STORIES), "prompts", len(prompts))


if __name__ == "__main__":
    main()
