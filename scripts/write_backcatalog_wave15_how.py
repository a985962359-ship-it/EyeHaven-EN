#!/usr/bin/env python3
"""Back-catalog wave 15: How E-H12…E-H19 → 12-page books. Owner sleeping; no questions."""
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
    "E-H12": {
        "title": "Why Do Speakers Make Sound?",
        "folder": "How",
        "tag": "Speaker",
        "companion": "girl",
        "pages": [
            'Music shakes the air. "How?" asks Guangguang.',
            "A speaker cone moves back and forth very quickly.",
            "That motion pushes air into waves your ears hear as sound.",
            "Electricity and magnets drive the cone following the music signal.",
            "Bigger waves can mean louder sounds; smaller waves can mean softer ones.",
            "Different speeds of shaking help make high and low notes.",
            "Phones, TVs, and concert stacks all use versions of this idea.",
            "Too-loud volume can hurt ears—ask a grown-up to keep it gentle.",
            "Covering a speaker muffles the air waves and softens the song.",
            "Sound is shaking air that reaches your eardrums.",
            "Dance a little when the cone makes the room hum kindly.",
            "Cone, magnet, air waves: speaker science.",
        ],
        "bubbles": [
            ("Music shakes", "air!"),
            ("Cone moves", "fast."),
            ("Pushes air", "waves."),
            ("Magnet follows", "signal."),
            ("Bigger wave,", "louder."),
            ("Speed makes", "high low."),
            ("Phones TVs", "same idea."),
            ("Keep volume", "gentle."),
            ("Cover muffles", "waves."),
            ("Sound reaches", "ears."),
            ("Dance to kind", "hum."),
            ("Speaker", "science."),
        ],
        "scenes": [
            "WIDE soft living room speaker music; girl and robot one-third; empty speech bubbles",
            "CLOSE speaker cone motion soft; characters half frame; empty speech bubbles",
            "DIAGRAM-SOFT air waves to ear soft; tiny figures; empty speech bubbles",
            "MEDIUM magnet coil drive soft; girl points; robot; empty speech bubbles",
            "PLAYFUL loud soft waves soft; characters half frame; empty speech bubbles",
            "DIAGRAM-SOFT high low notes soft; tiny figures; empty speech bubbles",
            "WIDE phone TV speakers soft; characters one-third; empty speech bubbles",
            "CLOSE gentle volume soft; characters half frame; empty speech bubbles",
            "MEDIUM cover muffles soft; characters half frame; empty speech bubbles",
            "CLOSE eardrum idea soft; characters half frame; empty speech bubbles",
            "WIDE gentle dance soft; girl and robot one-third; empty speech bubbles",
            "ENDING girl and robot soft smile; one-third; empty speech bubbles",
        ],
    },
    "E-H13": {
        "title": "Why Do Fridges Stay Cold Inside?",
        "folder": "How",
        "tag": "Fridge",
        "companion": "boy",
        "pages": [
            'Cold lettuce, warm kitchen. "How?" asks Guangguang.',
            "A fridge does not make a bag of coldness—it moves heat out.",
            "A special fluid cycles through pipes, picking up indoor heat.",
            "The warm heat is dumped to coils on the back or bottom.",
            "Inside stays cooler while the kitchen gets a little of that heat.",
            "The door seal keeps warm room air from rushing back in.",
            "Opening the door a long time invites warmth to sneak inside.",
            "Dusty coils work harder—grown-ups sometimes wipe them carefully.",
            "Freezers are colder cousins using a similar heat-moving trick.",
            "Food stays fresher when heat is pumped away on purpose.",
            "Feel the warm coils with a grown-up’s okay—science you can touch.",
            "Move heat out: fridge science.",
        ],
        "bubbles": [
            ("Cold inside!", "How?"),
            ("Moves heat", "out."),
            ("Fluid picks", "up heat."),
            ("Coils dump", "warmth."),
            ("Kitchen gets", "a little."),
            ("Seal keeps", "warm out."),
            ("Long open", "lets warmth."),
            ("Clean coils", "help."),
            ("Freezer is", "colder kin."),
            ("Food stays", "fresher."),
            ("Feel coils", "with help."),
            ("Fridge", "science."),
        ],
        "scenes": [
            "WIDE soft kitchen open fridge; boy and robot one-third; empty speech bubbles",
            "DIAGRAM-SOFT heat moving out soft; tiny figures; empty speech bubbles",
            "MEDIUM fluid pipes cycle soft; characters one-third; empty speech bubbles",
            "CLOSE back coils warm soft; boy points; robot; empty speech bubbles",
            "PLAYFUL kitchen warm bit soft; characters half frame; empty speech bubbles",
            "CLOSE door seal soft; characters half frame; empty speech bubbles",
            "MEDIUM long open door soft; characters half frame; empty speech bubbles",
            "CLOSE dusty coils wipe soft; characters half frame; empty speech bubbles",
            "WIDE freezer cousin soft; characters one-third; empty speech bubbles",
            "MEDIUM fresh food soft; characters one-third; empty speech bubbles",
            "CLOSE touch coils with grown-up soft; boy and robot half frame; empty speech bubbles",
            "ENDING boy and robot thumbs-up soft; one-third; empty speech bubbles",
        ],
    },
    "E-H14": {
        "title": "Why Do Straws Make Drinking Easier?",
        "folder": "How",
        "tag": "Straw",
        "companion": "girl",
        "pages": [
            'Slurp! "Is it a vacuum magic?" asks Guangguang.',
            "When you suck, you lower air pressure inside the straw.",
            "Higher outside air pressure pushes the drink up toward your mouth.",
            "You are not lifting the juice with pure willpower alone.",
            "Air is a quiet helper shoving the liquid up the tube.",
            "Pinch the straw and the push path gets blocked.",
            "Very tall straws fight gravity more—sips get harder.",
            "Reusable straws work the same physics with less trash.",
            "Don’t share straws when someone is sick—germs hitch rides.",
            "Pressure difference is the real straw superpower.",
            "Try a short sip experiment with a grown-up watching.",
            "Lower inside, push up: straw science.",
        ],
        "bubbles": [
            ("Slurp!", "Vacuum magic?"),
            ("Suck lowers", "pressure."),
            ("Outside air", "pushes up."),
            ("Not only", "willpower."),
            ("Air helps", "shove."),
            ("Pinch blocks", "the path."),
            ("Tall straw", "harder."),
            ("Reusable same", "physics."),
            ("Don't share", "if sick."),
            ("Pressure is", "superpower."),
            ("Try with", "grown-up."),
            ("Straw", "science."),
        ],
        "scenes": [
            "WIDE soft kitchen table juice straw; girl and robot one-third; empty speech bubbles",
            "DIAGRAM-SOFT low pressure in straw soft; tiny figures; empty speech bubbles",
            "MEDIUM outside air push up soft; characters one-third; empty speech bubbles",
            "PLAYFUL not willpower alone soft; girl points; robot; empty speech bubbles",
            "CLOSE air shove liquid soft; characters half frame; empty speech bubbles",
            "CLOSE pinch straw soft; characters half frame; empty speech bubbles",
            "MEDIUM tall straw hard soft; characters half frame; empty speech bubbles",
            "WIDE reusable straw soft; characters one-third; empty speech bubbles",
            "CLOSE no share sick soft; robot nod; empty speech bubbles",
            "DIAGRAM-SOFT pressure difference soft; tiny figures; empty speech bubbles",
            "MEDIUM sip experiment soft; girl and robot half frame; empty speech bubbles",
            "ENDING girl and robot soft smile; one-third; empty speech bubbles",
        ],
    },
    "E-H15": {
        "title": "Why Do Flashlights Need Batteries?",
        "folder": "How",
        "tag": "Flash",
        "companion": "boy",
        "pages": [
            'Click—a beam! "Why batteries?" asks Guangguang.',
            "Batteries store chemical energy ready to become electricity.",
            "That current can heat a filament or power bright LEDs.",
            "Without a power source, the bulb stays dark.",
            "The switch completes the circuit so electricity can flow.",
            "Dead batteries mean the chemical store is used up.",
            "Rechargeable packs can refill; others get recycled with help.",
            "Never put batteries in mouths—they are not snacks.",
            "A flashlight is a tiny portable power-and-light team.",
            "Camping and power outages make that team feel heroic.",
            "Check the + and − ends so the current knows its path.",
            "Chemical store to light: flashlight science.",
        ],
        "bubbles": [
            ("Click beam!", "Why batteries?"),
            ("Store chemical", "energy."),
            ("Current powers", "LEDs."),
            ("No power,", "stays dark."),
            ("Switch closes", "circuit."),
            ("Dead means", "used up."),
            ("Recharge or", "recycle."),
            ("Not for", "mouths."),
            ("Portable light", "team."),
            ("Hero in", "outages."),
            ("Check plus", "minus."),
            ("Flashlight", "science."),
        ],
        "scenes": [
            "WIDE soft dark room flashlight beam; boy and robot one-third; empty speech bubbles",
            "DIAGRAM-SOFT battery chemical store soft; tiny figures; empty speech bubbles",
            "CLOSE LED light soft; characters half frame; empty speech bubbles",
            "MEDIUM dark bulb no battery soft; boy points; robot; empty speech bubbles",
            "CLOSE switch circuit soft; characters half frame; empty speech bubbles",
            "PLAYFUL dead battery soft; characters half frame; empty speech bubbles",
            "MEDIUM recharge recycle soft; characters one-third; empty speech bubbles",
            "CLOSE no mouth batteries soft X; robot shake; empty speech bubbles",
            "WIDE portable team soft; characters one-third; empty speech bubbles",
            "MEDIUM camping outage soft; characters one-third; empty speech bubbles",
            "CLOSE plus minus ends soft; boy and robot half frame; empty speech bubbles",
            "ENDING boy and robot thumbs-up soft; one-third; empty speech bubbles",
        ],
    },
    "E-H16": {
        "title": "Why Do Bridges Have Triangles?",
        "folder": "How",
        "tag": "Bridge",
        "companion": "boy",
        "pages": [
            'Steel triangles rise. "Why that shape?" asks Guangguang.',
            "Triangles are strong and stable under pushes and pulls.",
            "Push a triangle’s corner and the sides share the force.",
            "A floppy square can squash into a slant more easily.",
            "Bridge builders lace triangles into trusses for strength.",
            "Cars and trains send weight that triangles help carry.",
            "Wood craft sticks can make tiny triangle bridges for demos.",
            "Circles and arches are strong too—in different jobs.",
            "Look for triangles next time you cross with a grown-up.",
            "Shape is a silent tool as important as the steel itself.",
            "Engineers choose geometry so people and cargo stay safe.",
            "Stable three sides: bridge-triangle science.",
        ],
        "bubbles": [
            ("Triangles!", "Why?"),
            ("Strong under", "pushes."),
            ("Sides share", "force."),
            ("Squares can", "squash."),
            ("Trusses lace", "triangles."),
            ("Carry car", "weight."),
            ("Stick demos", "work."),
            ("Arches strong", "too."),
            ("Spot them", "on walks."),
            ("Shape is a", "tool."),
            ("Geometry keeps", "safe."),
            ("Triangle", "science."),
        ],
        "scenes": [
            "WIDE soft steel bridge triangles; boy and robot one-third; empty speech bubbles",
            "DIAGRAM-SOFT strong triangle soft; tiny figures; empty speech bubbles",
            "CLOSE force shared sides soft; boy points; robot; empty speech bubbles",
            "PLAYFUL floppy square squash soft; characters half frame; empty speech bubbles",
            "MEDIUM truss lace soft; characters one-third; empty speech bubbles",
            "WIDE cars on bridge soft; characters one-third; empty speech bubbles",
            "CLOSE craft stick triangle soft; characters half frame; empty speech bubbles",
            "DIAGRAM-SOFT arch vs triangle soft; tiny figures; empty speech bubbles",
            "MEDIUM walk spot triangles soft; boy and robot half frame; empty speech bubbles",
            "PLAYFUL shape as tool soft; characters half frame; empty speech bubbles",
            "WIDE safe bridge crossing soft; characters one-third; empty speech bubbles",
            "ENDING boy and robot thumbs-up soft; one-third; empty speech bubbles",
        ],
    },
    "E-H17": {
        "title": "Why Do Matches Light When Scratched?",
        "folder": "How",
        "tag": "Match",
        "companion": "boy",
        "pages": [
            'Scratch—flame. Grown-up only. "How?" whispers Guangguang.',
            "Friction heat starts a chemical reaction in the match head.",
            "Special chemicals catch fire more easily than plain wood.",
            "Safety matches need the special strip on the box to light.",
            "Strike-anywhere matches are still not toys for kids.",
            "Fire needs fuel, heat, and air—scratch supplies the heat spark.",
            "Never play with matches; ask a grown-up for any demo.",
            "Blow gently or use water to put out practice flames safely.",
            "Lighters and stoves follow related heat-and-fuel ideas.",
            "Respect fire: it cooks food and also can hurt.",
            "Science explains the scratch; rules keep fingers safe.",
            "Friction, chemistry, care: match science.",
        ],
        "bubbles": [
            ("Scratch flame!", "Grown-up only."),
            ("Friction starts", "reaction."),
            ("Chemicals catch", "easier."),
            ("Safety strip", "needed."),
            ("Not toys", "for kids."),
            ("Fuel heat", "air."),
            ("Never play", "alone."),
            ("Put out", "safely."),
            ("Stoves similar", "ideas."),
            ("Respect fire", "always."),
            ("Rules keep", "safe."),
            ("Match", "science."),
        ],
        "scenes": [
            "WIDE soft grown-up demo match distant safe; boy and robot one-third; empty speech bubbles",
            "DIAGRAM-SOFT friction heat soft; tiny figures; empty speech bubbles",
            "CLOSE match head chemicals soft not scary; characters half frame; empty speech bubbles",
            "MEDIUM safety strip box soft; boy points; robot; empty speech bubbles",
            "CLOSE not a toy soft X; robot shake; empty speech bubbles",
            "DIAGRAM-SOFT fuel heat air soft; tiny figures; empty speech bubbles",
            "MEDIUM ask grown-up soft; characters half frame; empty speech bubbles",
            "CLOSE water put out soft; characters half frame; empty speech bubbles",
            "WIDE stove lighter soft distant; characters one-third; empty speech bubbles",
            "PLAYFUL respect fire soft; characters half frame; empty speech bubbles",
            "MEDIUM rules poster soft; boy and robot half frame; empty speech bubbles",
            "ENDING boy and robot serious-kind nod soft; one-third; empty speech bubbles",
        ],
    },
    "E-H18": {
        "title": "Why Do Sunglasses Help?",
        "folder": "How",
        "tag": "Shades",
        "companion": "girl",
        "pages": [
            'Bright glare. Dark lenses. "Just fashion?" asks Guangguang.',
            "Good sunglasses cut harsh light that makes eyes squint.",
            "Many also block invisible ultraviolet rays that stress eyes over time.",
            "Polarized lenses tame bounce glare from water and roads.",
            "Fashion frames are fun; protection labels matter more.",
            "Hats and shade help too on blazing days.",
            "Never stare at the Sun even with glasses—look away.",
            "Kids’ eyes deserve gentle light as much as grown-ups’ do.",
            "Store glasses in a case so scratches don’t scatter light.",
            "Comfortable seeing helps you play longer outdoors.",
            "Ask a grown-up for UV-protecting pair when shopping.",
            "Cut glare, block UV: sunglass science.",
        ],
        "bubbles": [
            ("Bright glare!", "Just fashion?"),
            ("Cut harsh", "light."),
            ("Block UV", "rays."),
            ("Polarized tames", "bounce."),
            ("Labels beat", "only looks."),
            ("Hats help", "too."),
            ("Never stare", "at Sun."),
            ("Kids' eyes", "matter."),
            ("Case stops", "scratches."),
            ("Play longer", "outdoors."),
            ("Ask grown-up", "for UV."),
            ("Sunglass", "science."),
        ],
        "scenes": [
            "WIDE soft sunny park glare; girl and robot one-third; empty speech bubbles",
            "CLOSE sunglasses cut light soft; characters half frame; empty speech bubbles",
            "DIAGRAM-SOFT UV block soft; tiny figures; empty speech bubbles",
            "MEDIUM polarized water glare soft; girl points; robot; empty speech bubbles",
            "PLAYFUL fashion vs label soft; characters half frame; empty speech bubbles",
            "WIDE hat shade soft; characters one-third; empty speech bubbles",
            "CLOSE never stare Sun soft X; robot shake; empty speech bubbles",
            "MEDIUM kids eyes care soft; characters half frame; empty speech bubbles",
            "CLOSE glasses case soft; characters half frame; empty speech bubbles",
            "WIDE outdoor play soft; girl and robot one-third; empty speech bubbles",
            "MEDIUM shop with grown-up soft; characters half frame; empty speech bubbles",
            "ENDING girl and robot soft smile shades; one-third; empty speech bubbles",
        ],
    },
    "E-H19": {
        "title": "Why Do Clocks Tick?",
        "folder": "How",
        "tag": "Tick",
        "companion": "boy",
        "pages": [
            'Tick-tock. "Why the sound?" asks Guangguang.',
            "Many clocks move gears in tiny careful steps.",
            "Escapement parts catch and release, making the tick.",
            "Each tick marks a small slice of time marching forward.",
            "Quartz clocks use a vibrating crystal for steady timing.",
            "Their tick can be a speaker click copying that rhythm.",
            "Silent digital clocks hide the steps behind a screen.",
            "Pendulum clocks swing a weight to keep the pace.",
            "Timekeepers help schools, trains, and bedtimes stay fair.",
            "Listen to a wind-up clock with a grown-up—gentle science music.",
            "The sound is machinery counting, not a tiny insect.",
            "Catch, release, count: clock-tick science.",
        ],
        "bubbles": [
            ("Tick-tock!", "Why sound?"),
            ("Gears move", "in steps."),
            ("Catch release", "makes tick."),
            ("Tiny slices", "of time."),
            ("Quartz crystal", "vibrates."),
            ("Speaker can", "click too."),
            ("Digital hides", "the steps."),
            ("Pendulum keeps", "pace."),
            ("Helps fair", "schedules."),
            ("Listen with", "grown-up."),
            ("Machinery", "counting."),
            ("Clock-tick", "science."),
        ],
        "scenes": [
            "WIDE soft bedroom clock tick; boy and robot one-third; empty speech bubbles",
            "DIAGRAM-SOFT gear steps soft; tiny figures; empty speech bubbles",
            "CLOSE escapement catch release soft; characters half frame; empty speech bubbles",
            "MEDIUM time slices soft; boy points; robot; empty speech bubbles",
            "DIAGRAM-SOFT quartz crystal soft; tiny figures; empty speech bubbles",
            "CLOSE speaker click soft; characters half frame; empty speech bubbles",
            "PLAYFUL silent digital soft; characters half frame; empty speech bubbles",
            "MEDIUM pendulum swing soft; characters one-third; empty speech bubbles",
            "WIDE school train bedtime soft; characters one-third; empty speech bubbles",
            "CLOSE listen wind-up soft; boy and robot half frame; empty speech bubbles",
            "PLAYFUL not an insect soft; characters half frame; empty speech bubbles",
            "ENDING boy and robot thumbs-up soft; one-third; empty speech bubbles",
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
    ref_dir = ROOT / ".comic_refs" / "w15_by_story"
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

    Path("/Users/song/qwen3-tts/comic_batch/comics_plan_en_backcatalog_w15.json").write_text(
        json.dumps(plan, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    Path("/Users/song/qwen3-tts/comic_batch/en_work/_raw_backcatalog_w15").mkdir(parents=True, exist_ok=True)
    Path("/Users/song/qwen3-tts/comic_batch/en_work/backcatalog_w15_prompts.json").write_text(
        json.dumps(prompts, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    bubbles_path = ROOT / "EyeHaven" / "ComicBubbleWords.en.json"
    bubbles = json.loads(bubbles_path.read_text(encoding="utf-8"))
    for sid, st in STORIES.items():
        bubbles[sid] = [{"i": i, "left": L, "right": R} for i, (L, R) in enumerate(st["bubbles"], 1)]
    bubbles_path.write_text(json.dumps(bubbles, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("wave15 done", len(STORIES), "prompts", len(prompts))


if __name__ == "__main__":
    main()
