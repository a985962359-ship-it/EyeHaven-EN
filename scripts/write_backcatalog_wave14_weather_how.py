#!/usr/bin/env python3
"""Back-catalog wave 14: E-W23–W24 + How E-H06–H11 → 12-page books. Owner sleeping; no questions."""
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
    "E-W23": {
        "title": "Why Do Windows Fog on Cold Days?",
        "folder": "Weather",
        "tag": "Fog",
        "companion": "girl",
        "pages": [
            'Steamy glass on a cold day. "Fog inside?" asks Guangguang.',
            "Warm moist indoor air drifts toward the chilly window pane.",
            "When that air hits cold glass, it cools quickly.",
            "Cooler air cannot hold as much water vapor.",
            "Extra vapor becomes tiny droplets—fog on the glass.",
            "Wiping clears a peephole; a little fresh air helps too.",
            "Breath on a bathroom mirror makes the same kind of cloud.",
            "Outdoor frost is different—frozen crystals, not indoor steam fog.",
            "Cooking and showers add extra indoor moisture on cold days.",
            "Foggy windows are indoor clouds starting on cold glass.",
            "Open a crack with a grown-up if the room feels too steamy.",
            "Warm moist air, cold pane: window-fog science.",
        ],
        "bubbles": [
            ("Steamy glass!", "Fog inside?"),
            ("Warm moist", "air drifts."),
            ("Hits cold", "glass."),
            ("Cooler holds", "less vapor."),
            ("Droplets make", "fog."),
            ("Wipe or", "air out."),
            ("Like breath", "on mirror."),
            ("Frost is", "different."),
            ("Cooking adds", "moisture."),
            ("Indoor clouds", "on glass."),
            ("Crack window", "with help."),
            ("Window-fog", "science."),
        ],
        "scenes": [
            "WIDE soft cozy room foggy window; girl and robot one-third; empty speech bubbles",
            "MEDIUM warm air toward cold pane soft; characters one-third; empty speech bubbles",
            "CLOSE cold glass cooling air soft; characters half frame; empty speech bubbles",
            "DIAGRAM-SOFT vapor to droplets soft; tiny figures; empty speech bubbles",
            "CLOSE foggy pane droplets soft; girl points; robot; empty speech bubbles",
            "PLAYFUL wipe peephole soft; characters half frame; empty speech bubbles",
            "MEDIUM breath on mirror soft; characters half frame; empty speech bubbles",
            "DIAGRAM-SOFT frost vs fog soft; tiny figures; empty speech bubbles",
            "WIDE kitchen shower steam soft gentle; characters one-third; empty speech bubbles",
            "PLAYFUL indoor cloud idea soft; characters half frame; empty speech bubbles",
            "MEDIUM crack window with grown-up soft; girl and robot half frame; empty speech bubbles",
            "ENDING girl and robot soft smile; one-third; empty speech bubbles",
        ],
    },
    "E-W24": {
        "title": "Why Do Seasons Feel Different by the Ocean?",
        "folder": "Weather",
        "tag": "Coast",
        "companion": "girl",
        "pages": [
            'Coast feels milder than inland. "Why?" asks Guangguang.',
            "Oceans heat up slowly and cool down slowly.",
            "That big water buffer softens the air nearby.",
            "Coasts often have milder winters than deep inland places.",
            "Summers by the sea can stay cooler than far inland heat.",
            "Breezes carry the ocean’s temperature influence ashore.",
            "Same latitude can still feel different coast versus prairie.",
            "Pack layers for beach trips—wind can still bite.",
            "Foggy marine air is another coastal weather personality.",
            "Oceans are giant temperature shock absorbers for coastal weather.",
            "Compare a seaside day with an inland cousin’s weather report.",
            "Slow ocean buffer: coastal season science.",
        ],
        "bubbles": [
            ("Coast milder?", "Why?"),
            ("Oceans heat", "slowly."),
            ("Water buffers", "nearby air."),
            ("Milder winter", "by sea."),
            ("Cooler summer", "often."),
            ("Breezes carry", "influence."),
            ("Same latitude,", "different feel."),
            ("Pack layers;", "wind bites."),
            ("Marine fog", "personality."),
            ("Shock absorber", "ocean."),
            ("Compare coast", "inland."),
            ("Coastal season", "science."),
        ],
        "scenes": [
            "WIDE soft coast vs inland split; girl and robot one-third; empty speech bubbles",
            "DIAGRAM-SOFT ocean heat cool slow soft; tiny figures; empty speech bubbles",
            "MEDIUM water buffering air soft; characters one-third; empty speech bubbles",
            "WIDE mild winter coast soft; characters one-third; empty speech bubbles",
            "MEDIUM cooler summer shore soft; girl points; robot; empty speech bubbles",
            "PLAYFUL sea breeze ashore soft; characters half frame; empty speech bubbles",
            "WIDE map same latitude soft; characters one-third; empty speech bubbles",
            "CLOSE jacket layers beach soft; characters half frame; empty speech bubbles",
            "MEDIUM gentle marine fog soft; characters one-third; empty speech bubbles",
            "PLAYFUL shock absorber ocean soft; characters half frame; empty speech bubbles",
            "WIDE compare weather reports soft; girl and robot one-third; empty speech bubbles",
            "ENDING girl and robot soft smile; one-third; empty speech bubbles",
        ],
    },
    "E-H06": {
        "title": "Why Can We See Ourselves in Mirrors?",
        "folder": "How",
        "tag": "Mirror",
        "companion": "boy",
        "pages": [
            'Guangguang waves; the glass waves back. "How?"',
            "A mirror’s smooth surface reflects light in an orderly way.",
            "Light from your face bounces to your eyes as a clear image.",
            "Ordinary walls scatter light messily in many directions.",
            "Mirrors bounce light neatly like a tidy bounce house for photons.",
            "Left and right look swapped in the usual bathroom-mirror way.",
            "That swap is geometry with shine, not magic twin tricks.",
            "Curved mirrors can stretch or shrink what you see.",
            "Telescopes and cars use mirrors to send light where needed.",
            "Wipe gently—scratches scatter the neat bounce.",
            "Seeing yourself is light making a round trip.",
            "Orderly bounce: mirror science.",
        ],
        "bubbles": [
            ("Glass waves", "back!"),
            ("Smooth glass", "reflects."),
            ("Light bounces", "to eyes."),
            ("Walls scatter", "messily."),
            ("Mirrors bounce", "neatly."),
            ("Left right", "swap."),
            ("Geometry with", "shine."),
            ("Curves stretch", "views."),
            ("Cars use", "mirrors."),
            ("Wipe gentle,", "no scratch."),
            ("Light round", "trip."),
            ("Mirror", "science."),
        ],
        "scenes": [
            "WIDE soft bathroom mirror wave; boy and robot one-third; empty speech bubbles",
            "DIAGRAM-SOFT smooth mirror bounce soft; tiny figures; empty speech bubbles",
            "CLOSE face light to eyes soft; characters half frame; empty speech bubbles",
            "MEDIUM messy wall scatter soft; boy points; robot; empty speech bubbles",
            "PLAYFUL neat bounce soft; characters half frame; empty speech bubbles",
            "CLOSE left-right swap soft; characters half frame; empty speech bubbles",
            "PLAYFUL geometry shine soft; characters half frame; empty speech bubbles",
            "MEDIUM curved mirror fun soft; characters one-third; empty speech bubbles",
            "WIDE car side mirror soft; characters one-third; empty speech bubbles",
            "CLOSE gentle wipe soft; boy and robot half frame; empty speech bubbles",
            "DIAGRAM-SOFT light round trip soft; tiny figures; empty speech bubbles",
            "ENDING boy and robot thumbs-up soft; one-third; empty speech bubbles",
        ],
    },
    "E-H07": {
        "title": "What Makes a Plane Fly?",
        "folder": "How",
        "tag": "Plane",
        "companion": "boy",
        "pages": [
            'A plane lifts off. "How does it stay up?" asks Guangguang.',
            "Airplane wings are shaped to help create lift—an upward push.",
            "Engines move the plane forward so air flows fast over the wings.",
            "Fast airflow and wing shape work together for flight.",
            "Pilots and flaps adjust the wing for takeoff and landing.",
            "Birds flap and change shape; planes use engines and fixed wings.",
            "Same sky, different toolkits for staying aloft.",
            "Air traffic rules keep many planes sharing the sky safely.",
            "Watch takeoffs from a safe airport overlook with a grown-up.",
            "Lift is not magic—it is moving air doing a job.",
            "Forward speed plus wing shape equals a flying machine.",
            "Airflow and lift: plane science.",
        ],
        "bubbles": [
            ("Plane lifts!", "How?"),
            ("Wings help", "make lift."),
            ("Engines push", "forward."),
            ("Fast air", "over wings."),
            ("Flaps help", "takeoff."),
            ("Birds flap;", "planes engine."),
            ("Same sky,", "different tools."),
            ("Rules share", "the sky."),
            ("Watch with", "grown-up."),
            ("Lift is", "moving air."),
            ("Speed plus", "wing shape."),
            ("Plane", "science."),
        ],
        "scenes": [
            "WIDE soft runway takeoff; boy and robot one-third; empty speech bubbles",
            "DIAGRAM-SOFT wing lift soft; tiny figures; empty speech bubbles",
            "MEDIUM engines forward soft; characters one-third; empty speech bubbles",
            "CLOSE airflow over wing soft; boy points; robot; empty speech bubbles",
            "PLAYFUL flaps adjust soft; characters half frame; empty speech bubbles",
            "WIDE bird vs plane soft; characters one-third; empty speech bubbles",
            "MEDIUM shared sky soft; characters one-third; empty speech bubbles",
            "CLOSE air traffic soft cartoon; characters half frame; empty speech bubbles",
            "WIDE airport overlook soft; boy and robot one-third; empty speech bubbles",
            "DIAGRAM-SOFT lift not magic soft; tiny figures; empty speech bubbles",
            "PLAYFUL flying machine soft; characters half frame; empty speech bubbles",
            "ENDING boy and robot thumbs-up soft; one-third; empty speech bubbles",
        ],
    },
    "E-H08": {
        "title": "How Does a Simple Wheel Help?",
        "folder": "How",
        "tag": "Wheel",
        "companion": "boy",
        "pages": [
            'Guangguang rolls a toy car. "So smooth!"',
            "Wheels turn hard sliding into easier rolling motion.",
            "Rolling usually takes less effort than dragging a box.",
            "Axles hold wheels so carts and bikes can carry loads.",
            "Round shapes keep contact small and motion steady.",
            "Scooters, suitcases, and skateboards all borrow the idea.",
            "Without wheels, many heavy jobs would scrap and scrape.",
            "Oil and air in tires keep real wheels happier.",
            "A stuck pebble can turn a smooth roll into a bump—pick it safely.",
            "From ancient carts to cars, the round idea still moves the world.",
            "Try rolling versus dragging a book with a grown-up’s okay.",
            "Rolling beats dragging: wheel science.",
        ],
        "bubbles": [
            ("Toy car", "rolls!"),
            ("Sliding becomes", "rolling."),
            ("Rolling easier", "than drag."),
            ("Axles hold", "wheels."),
            ("Round keeps", "motion steady."),
            ("Scooters bags", "borrow it."),
            ("No wheels,", "more scrape."),
            ("Tires like", "care."),
            ("Pebble makes", "bumps."),
            ("Round idea", "moves world."),
            ("Try roll vs", "drag."),
            ("Wheel", "science."),
        ],
        "scenes": [
            "WIDE soft playroom toy car; boy and robot one-third; empty speech bubbles",
            "DIAGRAM-SOFT slide vs roll soft; tiny figures; empty speech bubbles",
            "MEDIUM drag box vs roll soft; characters one-third; empty speech bubbles",
            "CLOSE axle wheel soft; boy points; robot; empty speech bubbles",
            "PLAYFUL round roll soft; characters half frame; empty speech bubbles",
            "WIDE scooter suitcase soft; characters one-third; empty speech bubbles",
            "MEDIUM scrape without wheels soft; characters half frame; empty speech bubbles",
            "CLOSE tire care soft; characters half frame; empty speech bubbles",
            "PLAYFUL pebble bump soft; characters half frame; empty speech bubbles",
            "WIDE cart to car timeline soft; characters one-third; empty speech bubbles",
            "MEDIUM book roll vs drag soft; boy and robot half frame; empty speech bubbles",
            "ENDING boy and robot thumbs-up soft; one-third; empty speech bubbles",
        ],
    },
    "E-H09": {
        "title": "Why Do Boats Float?",
        "folder": "How",
        "tag": "Float",
        "companion": "girl",
        "pages": [
            'A toy boat sits high. "Heavy boats float—how?" asks Guangguang.',
            "Water pushes up on anything that pushes water aside.",
            "That upward push can equal the boat’s weight.",
            "A boat’s hollow shape spreads weight over enough water.",
            "A solid steel cube may sink; a steel hull shaped like a bowl can float.",
            "Holes that flood the hull spoil the floating trick.",
            "Life jackets help people stay up by adding floaty volume.",
            "Density and shape team up more than “being light” alone.",
            "Calm pools are safer places to test toy boats with a grown-up.",
            "Floating is a push-up contest between object and water.",
            "Respect deep water—float science still needs life rules.",
            "Shape, push, float: boat science.",
        ],
        "bubbles": [
            ("Heavy floats?", "How?"),
            ("Water pushes", "up."),
            ("Push can match", "weight."),
            ("Hollow shape", "spreads."),
            ("Cube sinks;", "hull floats."),
            ("Flood holes", "spoil it."),
            ("Jackets add", "float."),
            ("Shape beats", "only light."),
            ("Test toys", "safely."),
            ("Push-up with", "water."),
            ("Deep water", "needs rules."),
            ("Boat float", "science."),
        ],
        "scenes": [
            "WIDE soft pond toy boat; girl and robot one-third; empty speech bubbles",
            "DIAGRAM-SOFT water push up soft; tiny figures; empty speech bubbles",
            "MEDIUM push equals weight soft; characters one-third; empty speech bubbles",
            "CLOSE hollow hull soft; girl points; robot; empty speech bubbles",
            "PLAYFUL cube vs boat hull soft; characters half frame; empty speech bubbles",
            "CLOSE flooded hull soft gentle; characters half frame; empty speech bubbles",
            "MEDIUM life jacket soft; characters half frame; empty speech bubbles",
            "DIAGRAM-SOFT density shape soft; tiny figures; empty speech bubbles",
            "WIDE calm pool test soft; girl and robot one-third; empty speech bubbles",
            "PLAYFUL push-up contest soft; characters half frame; empty speech bubbles",
            "MEDIUM safety rules soft; characters half frame; empty speech bubbles",
            "ENDING girl and robot soft smile; one-third; empty speech bubbles",
        ],
    },
    "E-H10": {
        "title": "Why Do Rubber Bands Snap Back?",
        "folder": "How",
        "tag": "Rubber",
        "companion": "boy",
        "pages": [
            'Twang! "Why does it bounce back?" asks Guangguang.',
            "Rubber has long tangled molecules like stretchy noodles.",
            "Pulling straightens them and stores energy in the stretch.",
            "Let go and the molecules tug toward their relaxed shape.",
            "That springiness returns the band—until it finally breaks.",
            "Heat and old age can make rubber crackly and weak.",
            "Never aim rubber bands at faces or animals.",
            "Physics is cool; safety is cooler.",
            "Other elastic things—hair ties, some toys—use similar stretch ideas.",
            "Snap-back is molecular springs doing tiny yoga.",
            "Stretch gently for science demos with a grown-up watching.",
            "Store, return, rest: rubber-band science.",
        ],
        "bubbles": [
            ("Twang!", "Why back?"),
            ("Long stretchy", "molecules."),
            ("Pull stores", "energy."),
            ("Let go,", "they tug."),
            ("Returns until", "it breaks."),
            ("Old rubber", "weakens."),
            ("Never aim", "at faces."),
            ("Safety is", "cooler."),
            ("Other elastics", "similar."),
            ("Molecular", "yoga."),
            ("Demo with", "grown-up."),
            ("Rubber-band", "science."),
        ],
        "scenes": [
            "WIDE soft desk twang rubber band; boy and robot one-third; empty speech bubbles",
            "DIAGRAM-SOFT tangled molecules soft; tiny figures; empty speech bubbles",
            "CLOSE stretch store energy soft; boy points; robot; empty speech bubbles",
            "PLAYFUL snap back soft; characters half frame; empty speech bubbles",
            "MEDIUM band breaks gently soft; characters half frame; empty speech bubbles",
            "CLOSE old cracked rubber soft; characters half frame; empty speech bubbles",
            "CLOSE no aim faces soft X; robot shake; empty speech bubbles",
            "PLAYFUL safety first soft; characters half frame; empty speech bubbles",
            "WIDE hair tie toy elastic soft; characters one-third; empty speech bubbles",
            "DIAGRAM-SOFT molecular yoga soft; tiny figures; empty speech bubbles",
            "MEDIUM grown-up demo soft; boy and robot half frame; empty speech bubbles",
            "ENDING boy and robot thumbs-up soft; one-third; empty speech bubbles",
        ],
    },
    "E-H11": {
        "title": "Why Do Bike Gears Help Hills?",
        "folder": "How",
        "tag": "Gears",
        "companion": "boy",
        "pages": [
            'Pedal grind on a hill. "What do gears do?" asks Guangguang.',
            "Gears trade turning force and speed like a mechanical translator.",
            "A low gear makes pedaling easier uphill but you go slower.",
            "A high gear covers ground faster on flats with more effort per turn.",
            "The chain carries spin from pedals to the rear wheel.",
            "Clicking into the right gear matches your legs to the hill.",
            "Oil and clean care keep gear rides smooth.",
            "Walking the bike is okay if the hill still feels too hard.",
            "Helmets matter more than any fancy gear trick.",
            "Gears do not remove work—they reshape how hard each pedal feels.",
            "Practice shifting on a quiet path with a grown-up.",
            "Force and speed trade: bike-gear science.",
        ],
        "bubbles": [
            ("Hill grind!", "Gears?"),
            ("Trade force", "and speed."),
            ("Low gear", "easier up."),
            ("High gear", "faster flat."),
            ("Chain carries", "spin."),
            ("Match legs", "to hill."),
            ("Oil keeps", "smooth."),
            ("Walk bike", "if needed."),
            ("Helmet first", "always."),
            ("Reshape the", "work."),
            ("Practice with", "grown-up."),
            ("Bike-gear", "science."),
        ],
        "scenes": [
            "WIDE soft hill bike grind; boy and robot one-third; empty speech bubbles",
            "DIAGRAM-SOFT gear force speed soft; tiny figures; empty speech bubbles",
            "MEDIUM low gear uphill soft; characters one-third; empty speech bubbles",
            "MEDIUM high gear flat soft; boy points; robot; empty speech bubbles",
            "CLOSE chain spin soft; characters half frame; empty speech bubbles",
            "PLAYFUL shift click soft; characters half frame; empty speech bubbles",
            "CLOSE oil care soft; characters half frame; empty speech bubbles",
            "WIDE walk bike hill soft; characters one-third; empty speech bubbles",
            "CLOSE helmet first soft; boy and robot half frame; empty speech bubbles",
            "DIAGRAM-SOFT work reshaped soft; tiny figures; empty speech bubbles",
            "MEDIUM quiet path practice soft; characters one-third; empty speech bubbles",
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
    ref_dir = ROOT / ".comic_refs" / "w14_by_story"
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

    Path("/Users/song/qwen3-tts/comic_batch/comics_plan_en_backcatalog_w14.json").write_text(
        json.dumps(plan, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    Path("/Users/song/qwen3-tts/comic_batch/en_work/_raw_backcatalog_w14").mkdir(parents=True, exist_ok=True)
    Path("/Users/song/qwen3-tts/comic_batch/en_work/backcatalog_w14_prompts.json").write_text(
        json.dumps(prompts, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    bubbles_path = ROOT / "EyeHaven" / "ComicBubbleWords.en.json"
    bubbles = json.loads(bubbles_path.read_text(encoding="utf-8"))
    for sid, st in STORIES.items():
        bubbles[sid] = [{"i": i, "left": L, "right": R} for i, (L, R) in enumerate(st["bubbles"], 1)]
    bubbles_path.write_text(json.dumps(bubbles, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("wave14 done", len(STORIES), "prompts", len(prompts))


if __name__ == "__main__":
    main()
