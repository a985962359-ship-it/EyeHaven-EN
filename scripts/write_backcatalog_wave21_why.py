#!/usr/bin/env python3
"""Back-catalog wave 21: Why E-Y14…E-Y21 → 12-page books. Owner sleeping; no questions."""
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
    "Soft friendly why-science, gentle pastel, not scary. No text logos, consistent character design. "
    "Simple readable background, big clear shapes, shallow depth, soft edges, no clutter. "
)
PREFIX_GIRL = (
    "Children's picture book comic panel, soft warm friendly science lighting, landscape 4:3. "
    "Cute round-headed white robot Guangguang with green trim, warm glowing chest lamp, small star on head, honest smile. "
    "Gentle girl about 6–7 with soft sweater and kind smile. "
    "Two large empty white oval speech bubbles with space for short kids text, blank inside, no letters. "
    "Soft friendly why-science, gentle pastel, not scary. No text logos, consistent character design. "
    "Simple readable background, big clear shapes, shallow depth, soft edges, no clutter. "
)

STORIES = {
    "E-Y14": {
        "title": "Why Is Honey Sticky?",
        "folder": "Why",
        "tag": "Honey",
        "companion": "girl",
        "pages": [
            'Honey clings to Guangguang’s spoon. "Why so sticky?"',
            "Honey is mostly sugars dissolved in a tiny bit of water.",
            "Those sugar chains grab onto each other and onto the spoon.",
            "Thick liquids flow slowly; scientists call that viscosity.",
            "Bees remove a lot of water so honey stays thick and lasting.",
            "Warmth makes honey runnier; cool makes it cling more.",
            "A little honey on toast can drip in slow golden ribbons.",
            "Sticky is useful: it stays put for bees and for snacks.",
            "Wash sticky fingers with warm water—sugar loves water.",
            "Stickiness is sugar chemistry holding hands.",
            "Taste a tiny drop with a grown-up and feel the cling.",
            "Golden cling: honey science.",
        ],
        "bubbles": [
            ("Spoon sticky!", "Why cling?"),
            ("Sugars in", "little water."),
            ("Chains grab", "the spoon."),
            ("Thick = slow", "flow."),
            ("Bees dry it", "thick."),
            ("Warm runs;", "cool clings."),
            ("Slow golden", "ribbons."),
            ("Sticky helps", "stay put."),
            ("Warm water", "washes sugar."),
            ("Sugars hold", "hands."),
            ("Tiny taste", "together."),
            ("Honey", "science."),
        ],
        "scenes": [
            "WIDE soft kitchen honey spoon cling; girl and robot one-third; empty speech bubbles",
            "DIAGRAM-SOFT sugars tiny water soft; tiny figures; empty speech bubbles",
            "CLOSE sugar chains grab soft; girl points; robot; empty speech bubbles",
            "MEDIUM thick slow flow soft; characters half frame; empty speech bubbles",
            "PLAYFUL bees dry honey soft; characters half frame; empty speech bubbles",
            "CLOSE warm vs cool honey soft; characters half frame; empty speech bubbles",
            "WIDE toast golden ribbons soft; characters one-third; empty speech bubbles",
            "MEDIUM sticky useful soft; characters half frame; empty speech bubbles",
            "CLOSE wash warm water soft; characters half frame; empty speech bubbles",
            "DIAGRAM-SOFT sugars hold hands soft; tiny figures; empty speech bubbles",
            "MEDIUM tiny taste soft; girl and robot half frame; empty speech bubbles",
            "ENDING girl and robot soft smile; one-third; empty speech bubbles",
        ],
    },
    "E-Y15": {
        "title": "Why Do We Dream?",
        "folder": "Why",
        "tag": "Dream",
        "companion": "boy",
        "pages": [
            'Max wakes from a funny dream. "Guangguang, why do we dream?"',
            "While you sleep, your brain stays busy sorting the day.",
            "Dreams can mix memories, feelings, and little made-up scenes.",
            "Some dreams feel like practice for feelings or ideas.",
            "REM sleep is a stage when dreams often get vivid.",
            "Not every dream has a secret code—many are brain play.",
            "Scary dreams can fade if you tell a grown-up and breathe.",
            "Good sleep habits help the brain’s night cleanup.",
            "Dreams do not predict the future like a crystal ball.",
            "Night stories are your brain’s soft rehearsal room.",
            "Keep a tiny dream notebook if you like remembering.",
            "Sleep, sort, dream: brain night science.",
        ],
        "bubbles": [
            ("Funny dream!", "Why dream?"),
            ("Brain sorts", "the day."),
            ("Memories mix", "with scenes."),
            ("Practice for", "feelings."),
            ("REM sleep", "vivid."),
            ("Not always", "a code."),
            ("Scary? Tell", "grown-up."),
            ("Good sleep", "helps."),
            ("Not a crystal", "ball."),
            ("Soft rehearsal", "room."),
            ("Tiny dream", "notebook."),
            ("Brain night", "science."),
        ],
        "scenes": [
            "WIDE soft bedroom wake dream; boy and robot one-third; empty speech bubbles",
            "DIAGRAM-SOFT brain sorting soft; tiny figures; empty speech bubbles",
            "PLAYFUL memory mix scenes soft; characters half frame; empty speech bubbles",
            "MEDIUM feelings practice soft; boy points; robot; empty speech bubbles",
            "CLOSE REM sleep soft; characters half frame; empty speech bubbles",
            "WIDE brain play soft; characters one-third; empty speech bubbles",
            "CLOSE tell grown-up breathe soft; characters half frame; empty speech bubbles",
            "MEDIUM good sleep habits soft; characters half frame; empty speech bubbles",
            "DIAGRAM-SOFT not crystal ball soft; tiny figures; empty speech bubbles",
            "PLAYFUL rehearsal room soft; characters half frame; empty speech bubbles",
            "MEDIUM dream notebook soft; boy and robot half frame; empty speech bubbles",
            "ENDING boy and robot soft smile; one-third; empty speech bubbles",
        ],
    },
    "E-Y16": {
        "title": "Why Does the Moon Change Shape?",
        "folder": "Why",
        "tag": "MoonPhase",
        "companion": "girl",
        "pages": [
            'The moon looks skinny tonight. "Did it shrink?" asks Guangguang.',
            "The moon is still round; we only see lit parts change.",
            "Sunlight hits half the moon like a lamp on a ball.",
            "As the moon orbits Earth, our view of the lit half shifts.",
            "New moon hides the lit face from us; full moon shows it.",
            "Crescents and halves are just different viewing angles.",
            "The moon does not make its own bright light—it reflects.",
            "Phases repeat in a gentle monthly cycle.",
            "Clouds can hide the moon, but the phase still continues.",
            "Changing shape is changing shadow-and-light view.",
            "Watch the sky a week and notice the slow shift.",
            "Orbit, light, phase: moon science.",
        ],
        "bubbles": [
            ("Skinny moon?", "Did it shrink?"),
            ("Still round!", "Lit parts change."),
            ("Sun lights", "half."),
            ("Orbit shifts", "our view."),
            ("New hides;", "full shows."),
            ("Crescents are", "angles."),
            ("Moon reflects", "sunlight."),
            ("Monthly", "cycle."),
            ("Clouds hide;", "phase goes."),
            ("Light and", "shadow view."),
            ("Watch a week", "shift."),
            ("Moon", "science."),
        ],
        "scenes": [
            "WIDE soft night skinny moon; girl and robot one-third; empty speech bubbles",
            "DIAGRAM-SOFT round moon lit parts soft; tiny figures; empty speech bubbles",
            "CLOSE sun lamp on ball soft; girl points; robot; empty speech bubbles",
            "MEDIUM orbit view shift soft; characters half frame; empty speech bubbles",
            "PLAYFUL new vs full soft; characters half frame; empty speech bubbles",
            "WIDE crescent half angles soft; characters one-third; empty speech bubbles",
            "CLOSE moon reflects soft; characters half frame; empty speech bubbles",
            "DIAGRAM-SOFT monthly cycle soft; tiny figures; empty speech bubbles",
            "MEDIUM clouds hide soft; characters half frame; empty speech bubbles",
            "PLAYFUL light shadow view soft; characters half frame; empty speech bubbles",
            "MEDIUM watch week soft; girl and robot half frame; empty speech bubbles",
            "ENDING girl and robot soft smile; one-third; empty speech bubbles",
        ],
    },
    "E-Y17": {
        "title": "Why Do Apples Turn Brown After Cutting?",
        "folder": "Why",
        "tag": "Apple",
        "companion": "boy",
        "pages": [
            'A cut apple turns brown. "Is it spoiled already?" asks Max.',
            "Cutting lets air meet the apple’s inside chemicals.",
            "An enzyme starts a browning reaction with oxygen.",
            "Brown is a color change, not always a danger sign.",
            "Lemon juice or chill can slow the browning.",
            "Whole uncut apples stay protected by their peel.",
            "Browning apples can still taste fine for a while.",
            "If it smells weird or feels slimy, ask a grown-up.",
            "Cooks use browning tricks in pies and snacks.",
            "Cut + air + enzyme = freckle chemistry.",
            "Try lemon on half a slice with a grown-up.",
            "Apple freckles: cut-fruit science.",
        ],
        "bubbles": [
            ("Brown already?", "Spoiled?"),
            ("Air meets", "inside."),
            ("Enzyme plus", "oxygen."),
            ("Color change,", "not always bad."),
            ("Lemon or chill", "slows it."),
            ("Peel protects", "whole apple."),
            ("Can still", "taste fine."),
            ("Weird smell?", "Ask grown-up."),
            ("Cooks use", "browning."),
            ("Cut air", "enzyme."),
            ("Try lemon", "half."),
            ("Apple", "science."),
        ],
        "scenes": [
            "WIDE soft kitchen cut apple brown; boy and robot one-third; empty speech bubbles",
            "DIAGRAM-SOFT air meets inside soft; tiny figures; empty speech bubbles",
            "CLOSE enzyme oxygen soft; boy points; robot; empty speech bubbles",
            "MEDIUM color not always bad soft; characters half frame; empty speech bubbles",
            "PLAYFUL lemon chill soft; characters half frame; empty speech bubbles",
            "CLOSE whole peel protect soft; characters half frame; empty speech bubbles",
            "WIDE still tasty soft; characters one-third; empty speech bubbles",
            "CLOSE ask grown-up soft; characters half frame; empty speech bubbles",
            "MEDIUM cooks browning soft; characters half frame; empty speech bubbles",
            "DIAGRAM-SOFT cut air enzyme soft; tiny figures; empty speech bubbles",
            "MEDIUM lemon half soft; boy and robot half frame; empty speech bubbles",
            "ENDING boy and robot soft smile; one-third; empty speech bubbles",
        ],
    },
    "E-Y18": {
        "title": "Why Do We Need Two Eyes?",
        "folder": "Why",
        "tag": "TwoEyes",
        "companion": "girl",
        "pages": [
            'Mia covers one eye. "Why two eyes, Guangguang?"',
            "Each eye sees a slightly different picture.",
            "Your brain blends both views into one smart scene.",
            "Two views help you judge near and far—depth.",
            "Catching a ball or pouring juice uses depth cues.",
            "One eye still sees a lot; two eyes add 3D help.",
            "Animals use eyes in different places for their lives.",
            "Glasses and checkups keep both eyes working kindly.",
            "Closing one eye makes stacking blocks trickier.",
            "Two cameras, one brain movie.",
            "Try the cover-one-eye game with a grown-up.",
            "Depth duo: eye science.",
        ],
        "bubbles": [
            ("Cover one!", "Why two?"),
            ("Each eye", "differs a bit."),
            ("Brain blends", "views."),
            ("Helps judge", "near far."),
            ("Balls and juice", "need depth."),
            ("One sees a lot;", "two add 3D."),
            ("Animals place", "eyes differently."),
            ("Checkups keep", "eyes kind."),
            ("One eye makes", "blocks hard."),
            ("Two cameras,", "one movie."),
            ("Cover-eye", "game."),
            ("Eye", "science."),
        ],
        "scenes": [
            "WIDE soft room cover one eye; girl and robot one-third; empty speech bubbles",
            "DIAGRAM-SOFT two slightly different views soft; tiny figures; empty speech bubbles",
            "CLOSE brain blends soft; girl points; robot; empty speech bubbles",
            "MEDIUM near far depth soft; characters half frame; empty speech bubbles",
            "PLAYFUL catch ball pour juice soft; characters half frame; empty speech bubbles",
            "WIDE one vs two soft; characters one-third; empty speech bubbles",
            "CLOSE animal eye places soft; characters half frame; empty speech bubbles",
            "MEDIUM checkup glasses soft; characters half frame; empty speech bubbles",
            "PLAYFUL stacking blocks soft; characters half frame; empty speech bubbles",
            "DIAGRAM-SOFT two cameras movie soft; tiny figures; empty speech bubbles",
            "MEDIUM cover-eye game soft; girl and robot half frame; empty speech bubbles",
            "ENDING girl and robot soft smile; one-third; empty speech bubbles",
        ],
    },
    "E-Y19": {
        "title": "Why Does Salt Melt Ice on Sidewalks?",
        "folder": "Why",
        "tag": "SaltIce",
        "companion": "boy",
        "pages": [
            'Salt on icy steps. "How does salt melt ice?" asks Max.',
            "Ice likes a certain freezing temperature.",
            "Salt mixes with the thin water film on ice.",
            "That mix freezes at a lower temperature than plain water.",
            "So ice can melt even when air is still chilly.",
            "Workers sprinkle salt to make walkways safer.",
            "Too much salt can bother plants—use carefully.",
            "Sand can add grip without melting as much.",
            "Warm sun and salt often team up on sidewalks.",
            "Lower freeze point = melt help.",
            "Watch salt work on a tiny ice cube with a grown-up.",
            "Sidewalk thaw: salt science.",
        ],
        "bubbles": [
            ("Salt on ice!", "How melts?"),
            ("Ice likes a", "freeze point."),
            ("Salt mixes", "thin water."),
            ("Mix freezes", "lower."),
            ("Melts in", "chilly air."),
            ("Safer", "walkways."),
            ("Too much salt?", "Careful."),
            ("Sand adds", "grip."),
            ("Sun and salt", "team up."),
            ("Lower freeze", "helps melt."),
            ("Tiny ice cube", "test."),
            ("Salt", "science."),
        ],
        "scenes": [
            "WIDE soft icy steps salt; boy and robot one-third; empty speech bubbles",
            "DIAGRAM-SOFT freeze point soft; tiny figures; empty speech bubbles",
            "CLOSE salt thin water film soft; boy points; robot; empty speech bubbles",
            "MEDIUM lower freeze soft; characters half frame; empty speech bubbles",
            "PLAYFUL melt chilly air soft; characters half frame; empty speech bubbles",
            "WIDE safer walkway soft; characters one-third; empty speech bubbles",
            "CLOSE careful plants soft; characters half frame; empty speech bubbles",
            "MEDIUM sand grip soft; characters half frame; empty speech bubbles",
            "PLAYFUL sun salt team soft; characters half frame; empty speech bubbles",
            "DIAGRAM-SOFT lower freeze melt soft; tiny figures; empty speech bubbles",
            "MEDIUM ice cube test soft; boy and robot half frame; empty speech bubbles",
            "ENDING boy and robot soft smile; one-third; empty speech bubbles",
        ],
    },
    "E-Y20": {
        "title": "Why Do We Have Belly Buttons?",
        "folder": "Why",
        "tag": "BellyButton",
        "companion": "girl",
        "pages": [
            'Mia peeks at her belly button. "Why is this here?"',
            "Before birth, a cord brought food and oxygen from Mom.",
            "That cord connected at the place that becomes your navel.",
            "After birth, the cord is gently clamped and falls away.",
            "The soft mark left behind is your belly button.",
            "Innies and outies are just different healing shapes.",
            "Everyone who grew with a cord has a navel story.",
            "Keep it clean like the rest of your tummy skin.",
            "It is a tiny scar of how you were fed early on.",
            "Your first delivery door—closed for good.",
            "Ask a grown-up about baby photos of the cord stump.",
            "Navel note: body beginning science.",
        ],
        "bubbles": [
            ("Belly button!", "Why here?"),
            ("Cord brought", "food oxygen."),
            ("Connected at", "navel place."),
            ("Cord falls", "away."),
            ("Mark left is", "button."),
            ("Innie or outie", "healing."),
            ("Everyone has", "navel story."),
            ("Keep tummy", "clean."),
            ("Tiny scar of", "early feeding."),
            ("Delivery door", "closed."),
            ("Baby photos", "ask."),
            ("Body", "science."),
        ],
        "scenes": [
            "WIDE soft bathroom peek belly button; girl and robot one-third; empty speech bubbles",
            "DIAGRAM-SOFT cord food oxygen soft gentle; tiny figures; empty speech bubbles",
            "CLOSE navel place soft; girl points; robot; empty speech bubbles",
            "MEDIUM cord falls away soft; characters half frame; empty speech bubbles",
            "PLAYFUL belly button mark soft; characters half frame; empty speech bubbles",
            "WIDE innie outie soft; characters one-third; empty speech bubbles",
            "CLOSE everyone navel soft; characters half frame; empty speech bubbles",
            "MEDIUM clean tummy soft; characters half frame; empty speech bubbles",
            "DIAGRAM-SOFT tiny scar story soft; tiny figures; empty speech bubbles",
            "PLAYFUL door closed soft; characters half frame; empty speech bubbles",
            "MEDIUM baby photos soft; girl and robot half frame; empty speech bubbles",
            "ENDING girl and robot soft smile; one-third; empty speech bubbles",
        ],
    },
    "E-Y21": {
        "title": "Why Do Balloons Stick to Hair After Rubbing?",
        "folder": "Why",
        "tag": "Balloon",
        "companion": "boy",
        "pages": [
            'A rubbed balloon sticks to Max’s hair. "Magic?" laughs Guangguang.',
            "Rubbing moves tiny charges between balloon and hair.",
            "Opposite charges attract—so hair and balloon cling.",
            "Scientists call this static electricity.",
            "Dry air makes static tricks show up more often.",
            "The balloon can also stick lightly to a wall.",
            "Touching metal can quietly share charges away.",
            "Static is not lightning, but both involve charge.",
            "Hair standing up is charges pushing alike apart.",
            "Rub, charge, cling: soft electric play.",
            "Try the balloon-on-wall test with a grown-up.",
            "Static cling: balloon science.",
        ],
        "bubbles": [
            ("Sticky hair!", "Magic?"),
            ("Rub moves", "tiny charges."),
            ("Opposites", "attract."),
            ("Called static", "electricity."),
            ("Dry air helps", "tricks."),
            ("Sticks to", "wall too."),
            ("Metal shares", "charges away."),
            ("Not lightning,", "same family."),
            ("Alike charges", "push apart."),
            ("Rub charge", "cling."),
            ("Wall test", "together."),
            ("Balloon", "science."),
        ],
        "scenes": [
            "WIDE soft room balloon sticks hair; boy and robot one-third; empty speech bubbles",
            "DIAGRAM-SOFT charges move soft; tiny figures; empty speech bubbles",
            "CLOSE opposites attract soft; boy points; robot; empty speech bubbles",
            "MEDIUM static electricity soft; characters half frame; empty speech bubbles",
            "PLAYFUL dry air tricks soft; characters half frame; empty speech bubbles",
            "WIDE balloon on wall soft; characters one-third; empty speech bubbles",
            "CLOSE touch metal soft; characters half frame; empty speech bubbles",
            "DIAGRAM-SOFT charge family soft; tiny figures; empty speech bubbles",
            "PLAYFUL hair stand up soft; characters half frame; empty speech bubbles",
            "MEDIUM rub charge cling soft; characters half frame; empty speech bubbles",
            "MEDIUM wall test soft; boy and robot half frame; empty speech bubbles",
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
    ref_dir = ROOT / ".comic_refs" / "w21_by_story"
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

    Path("/Users/song/qwen3-tts/comic_batch/comics_plan_en_backcatalog_w21.json").write_text(
        json.dumps(plan, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    Path("/Users/song/qwen3-tts/comic_batch/en_work/_raw_backcatalog_w21").mkdir(parents=True, exist_ok=True)
    Path("/Users/song/qwen3-tts/comic_batch/en_work/backcatalog_w21_prompts.json").write_text(
        json.dumps(prompts, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    bubbles_path = ROOT / "EyeHaven" / "ComicBubbleWords.en.json"
    bubbles = json.loads(bubbles_path.read_text(encoding="utf-8"))
    for sid, st in STORIES.items():
        bubbles[sid] = [{"i": i, "left": L, "right": R} for i, (L, R) in enumerate(st["bubbles"], 1)]
    bubbles_path.write_text(json.dumps(bubbles, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("wave21 done", len(STORIES), "prompts", len(prompts))


if __name__ == "__main__":
    main()
