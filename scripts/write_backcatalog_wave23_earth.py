#!/usr/bin/env python3
"""Back-catalog wave 23: Earth E-E06…E-E13 → 12-page books. Owner sleeping; no questions."""
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
    "E-E06": {
        "title": "Why Do Trees Need Roots?",
        "folder": "Earth",
        "tag": "Roots",
        "companion": "boy",
        "pages": [
            'Max tugs a tiny weed. "Why do trees need roots?"',
            "Roots drink water and minerals from the soil.",
            "They also anchor the tree so wind does not tip it.",
            "Tiny root hairs increase the drinking surface.",
            "Some roots store food for lean seasons.",
            "Fungi can partner with roots to share nutrients.",
            "Deep roots reach moisture; wide roots grab soil.",
            "Cutting big roots can hurt a living tree—ask grown-ups.",
            "Fallen leaves feed the soil that feeds roots.",
            "Roots are the tree’s quiet underground helpers.",
            "Gently feel soil near a tree with a grown-up.",
            "Drink, hold, store: root science.",
        ],
        "bubbles": [
            ("Weed tug!", "Need roots?"),
            ("Roots drink", "from soil."),
            ("They anchor", "in wind."),
            ("Tiny hairs", "help drink."),
            ("Some store", "food."),
            ("Fungi can", "partner."),
            ("Deep and wide", "roots."),
            ("Ask before", "cutting."),
            ("Leaves feed", "soil."),
            ("Quiet underground", "helpers."),
            ("Feel soil", "gently."),
            ("Root", "science."),
        ],
        "scenes": [
            "WIDE soft park tree roots idea; boy and robot one-third; empty speech bubbles",
            "DIAGRAM-SOFT roots drink soil soft; tiny figures; empty speech bubbles",
            "CLOSE roots anchor soft; boy points; robot; empty speech bubbles",
            "MEDIUM root hairs soft; characters half frame; empty speech bubbles",
            "PLAYFUL store food soft; characters half frame; empty speech bubbles",
            "WIDE fungi partner soft; characters one-third; empty speech bubbles",
            "CLOSE deep wide roots soft; characters half frame; empty speech bubbles",
            "MEDIUM ask grown-up soft; characters half frame; empty speech bubbles",
            "PLAYFUL leaves feed soil soft; characters half frame; empty speech bubbles",
            "DIAGRAM-SOFT underground helpers soft; tiny figures; empty speech bubbles",
            "MEDIUM feel soil soft; boy and robot half frame; empty speech bubbles",
            "ENDING boy and robot soft smile; one-third; empty speech bubbles",
        ],
    },
    "E-E07": {
        "title": "Why Do We Recycle?",
        "folder": "Earth",
        "tag": "Recycle",
        "companion": "girl",
        "pages": [
            'Bins labeled paper and plastic. "Why recycle?" asks Mia.',
            "Recycling gives used materials a new job.",
            "It can save energy compared with making everything new.",
            "Less trash in landfills means more room for Earth care.",
            "Clean, dry recyclables help workers sort safely.",
            "Not every item belongs in the blue bin—check labels.",
            "Reuse first: jars, bags, and boxes can live again.",
            "Reduce means buying less waste when you can.",
            "Recycling is teamwork: home, school, and city.",
            "Old stuff → new stuff with less waste.",
            "Sort a small pile with a grown-up tonight.",
            "Reduce, reuse, recycle: Earth care science.",
        ],
        "bubbles": [
            ("Two bins!", "Why recycle?"),
            ("Used stuff gets", "new jobs."),
            ("Can save", "energy."),
            ("Less landfill", "trash."),
            ("Clean dry", "helps."),
            ("Check labels", "first."),
            ("Reuse jars", "bags."),
            ("Reduce waste", "too."),
            ("Teamwork", "everywhere."),
            ("Old to new", "less waste."),
            ("Sort a pile", "together."),
            ("Earth care", "science."),
        ],
        "scenes": [
            "WIDE soft kitchen recycle bins; girl and robot one-third; empty speech bubbles",
            "DIAGRAM-SOFT materials new jobs soft; tiny figures; empty speech bubbles",
            "CLOSE save energy soft; girl points; robot; empty speech bubbles",
            "MEDIUM less landfill soft; characters half frame; empty speech bubbles",
            "PLAYFUL clean dry sort soft; characters half frame; empty speech bubbles",
            "WIDE check labels soft; characters one-third; empty speech bubbles",
            "CLOSE reuse jars soft; characters half frame; empty speech bubbles",
            "MEDIUM reduce waste soft; characters half frame; empty speech bubbles",
            "PLAYFUL teamwork soft; characters half frame; empty speech bubbles",
            "DIAGRAM-SOFT old to new soft; tiny figures; empty speech bubbles",
            "MEDIUM sort pile soft; girl and robot half frame; empty speech bubbles",
            "ENDING girl and robot soft smile; one-third; empty speech bubbles",
        ],
    },
    "E-E08": {
        "title": "Why Do Mountains Form?",
        "folder": "Earth",
        "tag": "Mountains",
        "companion": "boy",
        "pages": [
            'Tall peaks on a map. "How do mountains grow?" asks Max.',
            "Earth’s crust is broken into giant moving plates.",
            "When plates push together, rock can fold upward.",
            "Some mountains rise where magma lifts the land.",
            "Others form when blocks of crust tilt and lift.",
            "Rain and ice slowly carve sharp shapes later.",
            "Mountains can take millions of quiet years.",
            "Hiking trails show layers of old rock stories.",
            "Respect steep places—go with grown-ups.",
            "Push, lift, carve: mountain making.",
            "Trace mountain ridges on a soft map together.",
            "High ground: mountain science.",
        ],
        "bubbles": [
            ("Tall peaks!", "How grow?"),
            ("Crust has", "moving plates."),
            ("Plates push;", "rock folds up."),
            ("Magma can", "lift land."),
            ("Blocks tilt", "and lift."),
            ("Rain ice", "carve."),
            ("Takes quiet", "years."),
            ("Trails show", "rock layers."),
            ("Hike with", "grown-ups."),
            ("Push lift", "carve."),
            ("Trace ridges", "together."),
            ("Mountain", "science."),
        ],
        "scenes": [
            "WIDE soft map tall peaks; boy and robot one-third; empty speech bubbles",
            "DIAGRAM-SOFT moving plates soft; tiny figures; empty speech bubbles",
            "CLOSE plates fold up soft; boy points; robot; empty speech bubbles",
            "MEDIUM magma lift soft gentle; characters half frame; empty speech bubbles",
            "PLAYFUL crust blocks tilt soft; characters half frame; empty speech bubbles",
            "WIDE rain ice carve soft; characters one-third; empty speech bubbles",
            "CLOSE millions years soft; characters half frame; empty speech bubbles",
            "MEDIUM trail rock layers soft; characters half frame; empty speech bubbles",
            "CLOSE hike grown-ups soft; characters half frame; empty speech bubbles",
            "DIAGRAM-SOFT push lift carve soft; tiny figures; empty speech bubbles",
            "MEDIUM trace ridges soft; boy and robot half frame; empty speech bubbles",
            "ENDING boy and robot soft smile; one-third; empty speech bubbles",
        ],
    },
    "E-E09": {
        "title": "What Are Fossils?",
        "folder": "Earth",
        "tag": "Fossils",
        "companion": "girl",
        "pages": [
            'A stone leaf print. "Is this a fossil?" asks Mia.',
            "Fossils are traces of ancient life kept in rock.",
            "Bones, shells, footprints, and leaf prints can fossilize.",
            "Mud or sand can bury remains before they vanish.",
            "Minerals slowly replace soft parts over long time.",
            "Fossils teach us who lived before our cities.",
            "Not every cool rock is a fossil—museums help tell.",
            "Never dig protected sites; look with grown-ups.",
            "Drawings and photos record finds kindly.",
            "Old life stories locked in stone.",
            "Visit a fossil exhibit or book with a grown-up.",
            "Stone stories: fossil science.",
        ],
        "bubbles": [
            ("Stone leaf!", "A fossil?"),
            ("Traces of", "ancient life."),
            ("Bones shells", "footprints."),
            ("Mud can bury", "remains."),
            ("Minerals replace", "slowly."),
            ("Teach who lived", "before."),
            ("Museums help", "tell."),
            ("No protected", "digs."),
            ("Draw finds", "kindly."),
            ("Life stories", "in stone."),
            ("Visit exhibit", "together."),
            ("Fossil", "science."),
        ],
        "scenes": [
            "WIDE soft museum stone leaf; girl and robot one-third; empty speech bubbles",
            "DIAGRAM-SOFT ancient life traces soft; tiny figures; empty speech bubbles",
            "CLOSE bones shells prints soft; girl points; robot; empty speech bubbles",
            "MEDIUM mud bury soft; characters half frame; empty speech bubbles",
            "PLAYFUL minerals replace soft; characters half frame; empty speech bubbles",
            "WIDE teach past life soft; characters one-third; empty speech bubbles",
            "CLOSE museum tell soft; characters half frame; empty speech bubbles",
            "MEDIUM no protected dig soft; characters half frame; empty speech bubbles",
            "PLAYFUL draw finds soft; characters half frame; empty speech bubbles",
            "DIAGRAM-SOFT stories in stone soft; tiny figures; empty speech bubbles",
            "MEDIUM visit exhibit soft; girl and robot half frame; empty speech bubbles",
            "ENDING girl and robot soft smile; one-third; empty speech bubbles",
        ],
    },
    "E-E10": {
        "title": "Why Do Rivers Curve?",
        "folder": "Earth",
        "tag": "Rivers",
        "companion": "boy",
        "pages": [
            'A winding blue line on the map. "Why curves?"',
            "Water flows downhill, finding easier paths.",
            "Faster water digs the outer bend a little more.",
            "Slower water drops sand on the inner bend.",
            "Over time, dig and drop make bigger loops.",
            "Curves are called meanders by scientists.",
            "Floods can reshape bends after big rains.",
            "Stay back from steep muddy banks—safety first.",
            "Bridges and boats respect the river’s path.",
            "Flow, dig, drop: river curves.",
            "Trace a river’s loops on a map together.",
            "Winding water: river science.",
        ],
        "bubbles": [
            ("Winding river!", "Why curves?"),
            ("Water seeks", "easy paths."),
            ("Outer bend", "digs more."),
            ("Inner bend", "gets sand."),
            ("Loops grow", "over time."),
            ("Called", "meanders."),
            ("Floods reshape", "bends."),
            ("Stay back from", "banks."),
            ("Boats respect", "the path."),
            ("Flow dig", "drop."),
            ("Trace loops", "together."),
            ("River", "science."),
        ],
        "scenes": [
            "WIDE soft map winding river; boy and robot one-third; empty speech bubbles",
            "DIAGRAM-SOFT downhill flow soft; tiny figures; empty speech bubbles",
            "CLOSE outer bend dig soft; boy points; robot; empty speech bubbles",
            "MEDIUM inner sand drop soft; characters half frame; empty speech bubbles",
            "PLAYFUL bigger loops soft; characters half frame; empty speech bubbles",
            "WIDE meanders word soft; characters one-third; empty speech bubbles",
            "CLOSE floods reshape soft gentle; characters half frame; empty speech bubbles",
            "MEDIUM stay back banks soft; characters half frame; empty speech bubbles",
            "PLAYFUL boat bridge soft; characters half frame; empty speech bubbles",
            "DIAGRAM-SOFT flow dig drop soft; tiny figures; empty speech bubbles",
            "MEDIUM trace loops soft; boy and robot half frame; empty speech bubbles",
            "ENDING boy and robot soft smile; one-third; empty speech bubbles",
        ],
    },
    "E-E11": {
        "title": "What Is Soil Made Of?",
        "folder": "Earth",
        "tag": "Soil",
        "companion": "girl",
        "pages": [
            'Mia digs a little garden hole. "What is soil?"',
            "Soil mixes broken rock, air, water, and living bits.",
            "Tiny creatures and roots keep soil lively.",
            "Dead leaves and bugs become soft dark humus.",
            "Sandy soil drains fast; clay holds water longer.",
            "Healthy soil grows food and flowers.",
            "Compacting soil with heavy steps can hurt roots.",
            "Mulch and compost feed soil gently.",
            "Wash hands after digging—garden manners.",
            "Rock + life + water = growing ground.",
            "Feel sand vs clay with a grown-up.",
            "Dirt treasure: soil science.",
        ],
        "bubbles": [
            ("Garden dig!", "What soil?"),
            ("Rock air water", "living bits."),
            ("Creatures keep", "it lively."),
            ("Leaves become", "humus."),
            ("Sand drains;", "clay holds."),
            ("Healthy soil", "grows food."),
            ("Heavy steps", "hurt roots."),
            ("Mulch compost", "feed."),
            ("Wash hands", "after."),
            ("Rock life", "water."),
            ("Feel sand clay", "together."),
            ("Soil", "science."),
        ],
        "scenes": [
            "WIDE soft garden dig soil; girl and robot one-third; empty speech bubbles",
            "DIAGRAM-SOFT soil mix soft; tiny figures; empty speech bubbles",
            "CLOSE creatures roots soft; girl points; robot; empty speech bubbles",
            "MEDIUM humus leaves soft; characters half frame; empty speech bubbles",
            "PLAYFUL sand vs clay soft; characters half frame; empty speech bubbles",
            "WIDE grow food flowers soft; characters one-third; empty speech bubbles",
            "CLOSE compact soil soft; characters half frame; empty speech bubbles",
            "MEDIUM mulch compost soft; characters half frame; empty speech bubbles",
            "PLAYFUL wash hands soft; characters half frame; empty speech bubbles",
            "DIAGRAM-SOFT rock life water soft; tiny figures; empty speech bubbles",
            "MEDIUM feel sand clay soft; girl and robot half frame; empty speech bubbles",
            "ENDING girl and robot soft smile; one-third; empty speech bubbles",
        ],
    },
    "E-E12": {
        "title": "Why Do We Have Day and Night?",
        "folder": "Earth",
        "tag": "DayNight",
        "companion": "boy",
        "pages": [
            'Sun up, then dark. "Why day and night?" asks Max.',
            "Earth spins like a gentle top once a day.",
            "The side facing the Sun gets daylight.",
            "The side turned away rests in night shadow.",
            "Sunrise and sunset are the turning edges.",
            "We do not feel the spin because everything spins with us.",
            "A globe and lamp can show the light half.",
            "Clocks help us meet the day together.",
            "Sleep fits the dark side’s quiet time.",
            "Spin → light half → dark half.",
            "Try a lamp-globe demo with a grown-up.",
            "Day night spin: Earth science.",
        ],
        "bubbles": [
            ("Sun then dark!", "Why?"),
            ("Earth spins", "once a day."),
            ("Facing Sun =", "daylight."),
            ("Turned away =", "night."),
            ("Sunrise sunset", "edges."),
            ("We spin", "too."),
            ("Globe lamp", "shows it."),
            ("Clocks help", "meet day."),
            ("Sleep fits", "night."),
            ("Spin light", "dark."),
            ("Lamp demo", "together."),
            ("Day-night", "science."),
        ],
        "scenes": [
            "WIDE soft window day to night; boy and robot one-third; empty speech bubbles",
            "DIAGRAM-SOFT Earth spin soft; tiny figures; empty speech bubbles",
            "CLOSE day side sun soft; boy points; robot; empty speech bubbles",
            "MEDIUM night shadow soft; characters half frame; empty speech bubbles",
            "PLAYFUL sunrise sunset soft; characters half frame; empty speech bubbles",
            "WIDE we spin too soft; characters one-third; empty speech bubbles",
            "CLOSE globe lamp soft; characters half frame; empty speech bubbles",
            "MEDIUM clocks day soft; characters half frame; empty speech bubbles",
            "PLAYFUL sleep night soft; characters half frame; empty speech bubbles",
            "DIAGRAM-SOFT spin light dark soft; tiny figures; empty speech bubbles",
            "MEDIUM lamp demo soft; boy and robot half frame; empty speech bubbles",
            "ENDING boy and robot soft smile; one-third; empty speech bubbles",
        ],
    },
    "E-E13": {
        "title": "What Causes Caves?",
        "folder": "Earth",
        "tag": "Caves",
        "companion": "girl",
        "pages": [
            'A dark cozy cave picture. "How do caves form?"',
            "Some caves grow where water slowly dissolves rock.",
            "Limestone is a rock that water can nibble for ages.",
            "Cracks widen into tunnels and rooms.",
            "Dripping water can build stone icicles over time.",
            "Lava tubes are caves left by cooled lava rivers.",
            "Sea caves form where waves carve cliffs.",
            "Only explore caves with trained grown-ups.",
            "Lights, helmets, and buddies keep visits safe.",
            "Water + time + rock = cave rooms.",
            "Look at cave photos in a book together.",
            "Underground rooms: cave science.",
        ],
        "bubbles": [
            ("Cave picture!", "How form?"),
            ("Water dissolves", "rock slowly."),
            ("Limestone gets", "nibbled."),
            ("Cracks become", "rooms."),
            ("Drips build", "stone icicles."),
            ("Lava tubes", "too."),
            ("Waves carve", "sea caves."),
            ("Explore with", "trained adults."),
            ("Helmet light", "buddy."),
            ("Water time", "rock."),
            ("Cave photos", "together."),
            ("Cave", "science."),
        ],
        "scenes": [
            "WIDE soft cave entrance picture; girl and robot one-third; empty speech bubbles",
            "DIAGRAM-SOFT water dissolve rock soft; tiny figures; empty speech bubbles",
            "CLOSE limestone nibble soft; girl points; robot; empty speech bubbles",
            "MEDIUM cracks to rooms soft; characters half frame; empty speech bubbles",
            "PLAYFUL stone icicles soft; characters half frame; empty speech bubbles",
            "WIDE lava tube soft gentle; characters one-third; empty speech bubbles",
            "CLOSE sea cave waves soft; characters half frame; empty speech bubbles",
            "MEDIUM trained adults soft; characters half frame; empty speech bubbles",
            "PLAYFUL helmet light buddy soft; characters half frame; empty speech bubbles",
            "DIAGRAM-SOFT water time rock soft; tiny figures; empty speech bubbles",
            "MEDIUM cave photos soft; girl and robot half frame; empty speech bubbles",
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
    ref_dir = ROOT / ".comic_refs" / "w23_by_story"
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

    Path("/Users/song/qwen3-tts/comic_batch/comics_plan_en_backcatalog_w23.json").write_text(
        json.dumps(plan, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    Path("/Users/song/qwen3-tts/comic_batch/en_work/_raw_backcatalog_w23").mkdir(parents=True, exist_ok=True)
    Path("/Users/song/qwen3-tts/comic_batch/en_work/backcatalog_w23_prompts.json").write_text(
        json.dumps(prompts, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    bubbles_path = ROOT / "EyeHaven" / "ComicBubbleWords.en.json"
    bubbles = json.loads(bubbles_path.read_text(encoding="utf-8"))
    for sid, st in STORIES.items():
        bubbles[sid] = [{"i": i, "left": L, "right": R} for i, (L, R) in enumerate(st["bubbles"], 1)]
    bubbles_path.write_text(json.dumps(bubbles, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("wave23 done", len(STORIES), "prompts", len(prompts))


if __name__ == "__main__":
    main()
