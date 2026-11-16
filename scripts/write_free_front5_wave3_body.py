#!/usr/bin/env python3
"""Free-front-5 wave 3: Body shelf gaps E-B01, E-B02, E-B04, E-B05 → 12-page books.

E-B03 already remodeled. Background: kid-friendly-backgrounds.md +
character-background-scale.md. Audio: VoiceDesign locked voices.
Boy:girl ≈ 7:3 → B01/B02/B04 boy; B05 girl.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PREFIX_BOY = (
    "Children's picture book comic panel, soft warm friendly lighting, landscape 4:3. "
    "Cute round-headed white robot Guangguang with green trim, warm glowing chest lamp, "
    "small star on head, honest smile. Blonde boy about 6 years old wearing a blue T-rex hoodie. "
    "Exactly two empty white oval speech bubbles with blank white interiors and no letters inside. "
    "No scary imagery, no text logos, consistent character design. "
    "Simple readable background, big clear shapes, shallow depth, soft edges, no clutter. "
)

PREFIX_GIRL = (
    "Children's picture book comic panel, soft warm friendly lighting, landscape 4:3. "
    "Cute round-headed white robot Guangguang with green trim, warm glowing chest lamp, "
    "small star on head, honest smile. Gentle girl about 6–7 with soft sweater and kind smile. "
    "Exactly two empty white oval speech bubbles with blank white interiors and no letters inside. "
    "No scary imagery, no text logos, consistent character design. "
    "Simple readable background, big clear shapes, shallow depth, soft edges, no clutter. "
)

STORIES = {
    "E-B01": {
        "title": "Why Do We Need Sleep?",
        "folder": "My Body",
        "tag": "Sleep",
        "companion": "boy",
        "pages": [
            'Guangguang yawns wide. "Nap attack!"',
            "Sleep lets your body and brain recover.",
            "While you rest, your brain sorts memories.",
            "Your body repairs tiny wear and grows.",
            "Kids need plenty of sleep—growing is busy work.",
            "Dim lights tell your brain night is near.",
            "Quiet stories help the body slow down.",
            "Bright screens late can keep you too alert.",
            "A calm bedtime is like a soft off-switch.",
            "Sleep is not wasted time—it is nightly repair.",
            "Rest well, then wake ready to play and learn.",
            "Goodnight, little repair crew inside you.",
        ],
        "bubbles": [
            ("Nap attack!", "Yaaawn."),
            ("Body + brain", "recover."),
            ("Brain sorts", "memories."),
            ("Body repairs", "and grows."),
            ("Kids need", "lots of sleep."),
            ("Dim lights", "say night."),
            ("Quiet stories", "slow down."),
            ("Late screens", "keep you up."),
            ("Calm bedtime", "off-switch."),
            ("Not wasted—", "night repair."),
            ("Rest well,", "wake ready."),
            ("Goodnight,", "repair crew."),
        ],
        "scenes": [
            "WIDE cozy bedroom evening; full-body about one-third frame: robot and boy yawn on bed; empty speech bubbles top",
            "MEDIUM characters about half frame height clear faces; soft blanket fort; robot explains rest; empty speech bubbles",
            "DIAGRAM-SOFT tiny glowing memory stars sorting in a gentle brain cloud; characters small corner; empty speech bubbles",
            "CLOSE soft cartoon growth marks on a measuring wall; boy stretches; robot smiles; characters half frame; empty speech bubbles",
            "MEDIUM kid bedroom calendar with moon stickers; characters half frame talking; empty speech bubbles",
            "CLOSE lamp dimming warm; boy reaches switch; robot nods; faces clear half frame; empty speech bubbles",
            "MEDIUM parent silhouette far back reading; boy and robot listen on bed half frame; empty speech bubbles",
            "SPLIT: bright tablet glow vs soft book light; boy turns tablet away; robot coaches; half frame; empty speech bubbles",
            "WIDE quiet room moon at window; characters reclining one-third frame; empty speech bubbles",
            "DIAGRAM-SOFT soft wrench and heart icons as nightly repair metaphor kid-safe; tiny figures; empty speech bubbles",
            "MEDIUM morning sunbeam; boy stretches awake; robot cheers; half frame clear faces; empty speech bubbles",
            "ENDING snug under blanket; characters one-third frame waving goodnight; empty speech bubbles",
        ],
    },
    "E-B02": {
        "title": "Why Do We Yawn?",
        "folder": "My Body",
        "tag": "Yawn",
        "companion": "boy",
        "pages": [
            "A big yawn spreads. Contagious!",
            "Scientists still study why we yawn.",
            "It may help cool a warm busy brain.",
            "A yawn can wake you a little bit.",
            "It can also signal rest time to friends.",
            "Seeing a yawn often makes you yawn too.",
            "Humans copy soft signals—we are social.",
            "Yawning does not always mean you are bored.",
            "Sometimes your body wants a quick reset.",
            "Stretch, breathe, and follow a night yawn to bed.",
            "Day yawns can mean you need a short break.",
            "Smile—your body just asked for a tiny reset.",
        ],
        "bubbles": [
            ("Big yawn!", "Contagious!"),
            ("Still studying", "why."),
            ("Cool the", "busy brain?"),
            ("Wake you", "a little."),
            ("Signal rest", "to friends."),
            ("See a yawn,", "yawn too."),
            ("We copy", "soft signals."),
            ("Not always", "bored."),
            ("Body wants", "a reset."),
            ("Stretch. Breathe.", "Then bed."),
            ("Day yawn:", "short break."),
            ("Tiny reset!", "Smile."),
        ],
        "scenes": [
            "WIDE living room sofa; full-body one-third: boy mid-yawn, robot mirrors yawn playfully; empty speech bubbles",
            "MEDIUM science corner poster of a soft brain; characters half frame pointing; empty speech bubbles",
            "DIAGRAM-SOFT cool blue breeze around a cartoon head; tiny characters; empty speech bubbles",
            "CLOSE boy face after yawn eyes brighter; robot nearby half frame; empty speech bubbles",
            "MEDIUM two kids far soft; boy and robot wave rest gesture half frame; empty speech bubbles",
            "OVER-SHOULDER watching another yawn; contagious sparkles soft; characters half frame; empty speech bubbles",
            "MEDIUM playground bench social chat; characters half frame smiling; empty speech bubbles",
            "CLOSE not-bored: boy curious with book; robot shrugs kindly; half frame; empty speech bubbles",
            "MEDIUM stretch arms big; robot coaches breathe-in; half frame; empty speech bubbles",
            "WIDE hallway to bedroom night light; characters walking one-third frame; empty speech bubbles",
            "MEDIUM daytime window stretch break; characters half frame; empty speech bubbles",
            "ENDING both smile after yawn; cozy one-third frame; empty speech bubbles",
        ],
    },
    "E-B04": {
        "title": "Why Does My Heart Beat?",
        "folder": "My Body",
        "tag": "Heart",
        "companion": "boy",
        "pages": [
            'Hand on chest: thump-thump. "A drum?"',
            "Your heart is a strong muscle pump.",
            "It pushes blood through soft tube paths.",
            "Those paths are called blood vessels.",
            "Blood carries oxygen and food to you.",
            "Then blood returns to refill oxygen from lungs.",
            "Exercise makes the heart beat faster.",
            "Your body asks for more delivery right then.",
            "Rest slows the beat to a calm rhythm.",
            "A steady heartbeat is your delivery system.",
            "Feel your pulse—gentle drum for life.",
            "Thank your heart for every quiet thump.",
        ],
        "bubbles": [
            ("Thump-thump!", "A drum?"),
            ("Strong muscle", "pump."),
            ("Pushes blood", "through tubes."),
            ("Blood vessels", "are paths."),
            ("Oxygen + food", "ride along."),
            ("Lungs refill", "oxygen."),
            ("Exercise:", "faster beat."),
            ("More delivery", "right then."),
            ("Rest slows", "the rhythm."),
            ("Steady beat =", "delivery."),
            ("Feel pulse:", "life drum."),
            ("Thank you,", "heart."),
        ],
        "scenes": [
            "MEDIUM boy hand on chest; robot listens with smile; characters half frame clear faces; bedroom; empty speech bubbles",
            "DIAGRAM-SOFT friendly heart pump icon kid-safe not medical gore; tiny figures corner; empty speech bubbles",
            "SOFT tubes like garden hoses carrying sparkles; characters small; empty speech bubbles",
            "MAP-SOFT simple body outline with gentle vessel lines; robot points; boy watches half frame; empty speech bubbles",
            "CLOSE lunch apple and soft oxygen bubbles metaphor; characters half frame; empty speech bubbles",
            "SPLIT lungs refill then heart send; soft arrows; tiny characters; empty speech bubbles",
            "WIDE park running; characters one-third frame jogging; empty speech bubbles",
            "MEDIUM after run; boy breathing; robot counts beats playfully half frame; empty speech bubbles",
            "COZY couch rest; calm faces half frame; empty speech bubbles",
            "DIAGRAM-SOFT delivery truck metaphor tiny heart driver cute; empty speech bubbles",
            "CLOSE fingers on wrist feeling pulse; robot coaching; half frame; empty speech bubbles",
            "ENDING warm hug-self gesture; characters one-third frame grateful; empty speech bubbles",
        ],
    },
    "E-B05": {
        "title": "Why Do I Get a Fever?",
        "folder": "My Body",
        "tag": "Fever",
        "companion": "girl",
        "pages": [
            'Cheeks feel warm. "Broken thermostat?"',
            "A fever often means your body is fighting germs.",
            "A little higher heat can help defenses work.",
            "Your immune team works hard when you feel hot.",
            "Fevers can have other causes too.",
            "Grown-ups decide what care you need.",
            "Rest helps your body use its energy wisely.",
            "Sips of water or warm drinks help a lot.",
            "Medicine is only from a trusted adult.",
            "Never grab pills by yourself.",
            "Fever is a signal, not a game.",
            "Ask for help, rest, and feel the care.",
        ],
        "bubbles": [
            ("Warm cheeks!", "Thermostat?"),
            ("Fighting germs", "sometimes."),
            ("Little heat", "helps defenses."),
            ("Immune team", "works hard."),
            ("Other causes", "possible."),
            ("Grown-ups", "decide care."),
            ("Rest helps", "your body."),
            ("Sip water,", "warm drinks."),
            ("Medicine from", "trusted adult."),
            ("Never grab", "pills alone."),
            ("Fever = signal,", "not a game."),
            ("Ask. Rest.", "Feel care."),
        ],
        "scenes": [
            "MEDIUM girl on couch warm cheeks; robot gentle concern; characters half frame; living room; empty speech bubbles",
            "DIAGRAM-SOFT cute shield vs tiny soft germ shapes kid-safe not scary; small figures; empty speech bubbles",
            "SOFT thermometer with mild warm glow not alarming; characters half frame; empty speech bubbles",
            "PLAYFUL immune team as tiny star helpers; girl watches; robot coaches; half frame; empty speech bubbles",
            "MEDIUM kind mom nearby with care bag; girl and robot half frame; empty speech bubbles",
            "CLOSE grown-up hand on forehead check; soft trust; characters half frame; empty speech bubbles",
            "WIDE rest nest pillows; characters one-third frame resting; empty speech bubbles",
            "CLOSE water cup and honey-warm mug; girl sips; robot nods; half frame; empty speech bubbles",
            "MEDIUM adult offers medicine cup carefully; girl waits; robot reminds; half frame; empty speech bubbles",
            "SPLIT: locked medicine cabinet vs asking adult; clear safety; tiny figures; empty speech bubbles",
            "MEDIUM soft warning sign heart-safe; characters half frame serious kind; empty speech bubbles",
            "ENDING cozy blanket; mom far soft; girl and robot one-third frame peaceful; empty speech bubbles",
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
    a01 = Path("/Users/song/EyeHaven-EN/EyeHaven/BedtimeComics/E-A01/01.jpg")

    for sid, st in STORIES.items():
        prefix = PREFIX_GIRL if st["companion"] == "girl" else PREFIX_BOY
        ref = str(girl_ref if st["companion"] == "girl" and girl_ref.exists() else boy_ref if boy_ref.exists() else a01)
        refs = [str(p) for p in (gg_ref, Path(ref)) if p.exists()]
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
        plan.append(
            {
                "id": sid,
                "title": st["title"],
                "companion": st["companion"],
                "panels": panels,
            }
        )

    plan_path = Path("/Users/song/qwen3-tts/comic_batch/comics_plan_en_free_front5_w3.json")
    plan_path.write_text(json.dumps(plan, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("wrote", plan_path)

    raw_dir = Path("/Users/song/qwen3-tts/comic_batch/en_work/_raw_free_front5_w3")
    raw_dir.mkdir(parents=True, exist_ok=True)
    prompts_path = Path("/Users/song/qwen3-tts/comic_batch/en_work/free_front5_w3_prompts.json")
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

    # merge bubbles into App JSON for corner speakers
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
