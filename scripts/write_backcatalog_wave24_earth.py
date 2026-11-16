#!/usr/bin/env python3
"""Back-catalog wave 24: Earth E-E14…E-E21 → 12-page books. Owner sleeping; no questions."""
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
    "E-E14": {
        "title": "Why Do Glaciers Move?",
        "folder": "Earth",
        "tag": "Glacier",
        "companion": "boy",
        "pages": [
            'A slow river of ice. "Do glaciers really move?" asks Max.',
            "Glaciers are thick ice that flows very slowly downhill.",
            "Their own weight makes ice slide and deform a little.",
            "Meltwater at the bottom can help ice slip.",
            "They scrape rock and carry stones like a bulldozer.",
            "When ice melts back, it leaves valleys and lakes.",
            "Climate warmth can speed melting at the edges.",
            "Scientists measure glacier speed with careful tools.",
            "Visit icy places only with trained grown-ups.",
            "Heavy ice + slope = slow motion.",
            "Watch a short glacier video with a grown-up.",
            "Ice river: glacier science.",
        ],
        "bubbles": [
            ("Ice river!", "It moves?"),
            ("Thick ice flows", "slowly."),
            ("Weight makes", "ice slide."),
            ("Meltwater helps", "slip."),
            ("Scrapes rock,", "carries stones."),
            ("Leaves valleys", "lakes."),
            ("Warmth speeds", "melt."),
            ("Scientists", "measure."),
            ("Go with trained", "adults."),
            ("Heavy ice", "slow motion."),
            ("Watch video", "together."),
            ("Glacier", "science."),
        ],
        "scenes": [
            "WIDE soft icy glacier valley; boy and robot one-third; empty speech bubbles",
            "DIAGRAM-SOFT thick ice flow soft; tiny figures; empty speech bubbles",
            "CLOSE weight slide soft; boy points; robot; empty speech bubbles",
            "MEDIUM meltwater slip soft; characters half frame; empty speech bubbles",
            "PLAYFUL scrape stones soft; characters half frame; empty speech bubbles",
            "WIDE valleys lakes soft; characters one-third; empty speech bubbles",
            "CLOSE warmth melt soft; characters half frame; empty speech bubbles",
            "MEDIUM scientists measure soft; characters half frame; empty speech bubbles",
            "CLOSE trained adults soft; characters half frame; empty speech bubbles",
            "DIAGRAM-SOFT heavy ice motion soft; tiny figures; empty speech bubbles",
            "MEDIUM watch video soft; boy and robot half frame; empty speech bubbles",
            "ENDING boy and robot soft smile; one-third; empty speech bubbles",
        ],
    },
    "E-E15": {
        "title": "What Is the Water Cycle?",
        "folder": "Earth",
        "tag": "WaterCycle",
        "companion": "girl",
        "pages": [
            'Puddles disappear. "Where does water go?" asks Mia.',
            "Sun warms water into invisible vapor—evaporation.",
            "Vapor rises, cools, and makes cloud droplets.",
            "Clouds can release rain or snow—precipitation.",
            "Water runs into rivers, lakes, and oceans again.",
            "Some soaks into soil as groundwater.",
            "Plants drink and breathe out vapor too.",
            "The same water travels this loop again and again.",
            "We share Earth’s water—use it kindly.",
            "Evaporate, cloud, fall, flow: a cycle.",
            "Trace the loop on a simple drawing together.",
            "Water journey: cycle science.",
        ],
        "bubbles": [
            ("Puddle gone!", "Where water?"),
            ("Sun makes", "vapor."),
            ("Vapor cools", "to clouds."),
            ("Rain or snow", "falls."),
            ("Flows to lakes", "oceans."),
            ("Some becomes", "groundwater."),
            ("Plants breathe", "vapor too."),
            ("Same water", "loops."),
            ("Use water", "kindly."),
            ("Evaporate cloud", "fall."),
            ("Draw the loop", "together."),
            ("Cycle", "science."),
        ],
        "scenes": [
            "WIDE soft puddle drying sun; girl and robot one-third; empty speech bubbles",
            "DIAGRAM-SOFT evaporation soft; tiny figures; empty speech bubbles",
            "CLOSE cloud droplets soft; girl points; robot; empty speech bubbles",
            "MEDIUM rain snow soft; characters half frame; empty speech bubbles",
            "PLAYFUL rivers lakes soft; characters half frame; empty speech bubbles",
            "WIDE groundwater soft; characters one-third; empty speech bubbles",
            "CLOSE plants vapor soft; characters half frame; empty speech bubbles",
            "MEDIUM water loops soft; characters half frame; empty speech bubbles",
            "PLAYFUL use kindly soft; characters half frame; empty speech bubbles",
            "DIAGRAM-SOFT full cycle soft; tiny figures; empty speech bubbles",
            "MEDIUM draw loop soft; girl and robot half frame; empty speech bubbles",
            "ENDING girl and robot soft smile; one-third; empty speech bubbles",
        ],
    },
    "E-E16": {
        "title": "Why Do Some Rocks Sparkle?",
        "folder": "Earth",
        "tag": "Sparkle",
        "companion": "boy",
        "pages": [
            'A rock twinkles in sun. "Why sparkle?" asks Max.',
            "Some rocks hold shiny mineral crystals.",
            "Flat crystal faces bounce light like tiny mirrors.",
            "Mica flakes can glitter in granite.",
            "Quartz and other minerals can flash too.",
            "Sparkle is light play, not always a gem treasure.",
            "Never taste rocks; wash hands after collecting.",
            "Ask before taking stones from parks.",
            "A hand lens helps you see crystal shapes.",
            "Minerals + light = twinkle.",
            "Compare a dull rock and a shiny one together.",
            "Twinkle stone: mineral science.",
        ],
        "bubbles": [
            ("Twinkle rock!", "Why?"),
            ("Shiny mineral", "crystals."),
            ("Faces bounce", "light."),
            ("Mica can", "glitter."),
            ("Quartz can", "flash."),
            ("Light play,", "not always gem."),
            ("No tasting;", "wash hands."),
            ("Ask before", "taking."),
            ("Hand lens", "helps."),
            ("Minerals plus", "light."),
            ("Compare rocks", "together."),
            ("Mineral", "science."),
        ],
        "scenes": [
            "WIDE soft outdoor sparkling rock; boy and robot one-third; empty speech bubbles",
            "DIAGRAM-SOFT mineral crystals soft; tiny figures; empty speech bubbles",
            "CLOSE crystal faces light soft; boy points; robot; empty speech bubbles",
            "MEDIUM mica granite soft; characters half frame; empty speech bubbles",
            "PLAYFUL quartz flash soft; characters half frame; empty speech bubbles",
            "WIDE not always gem soft; characters one-third; empty speech bubbles",
            "CLOSE wash hands soft; characters half frame; empty speech bubbles",
            "MEDIUM ask parks soft; characters half frame; empty speech bubbles",
            "PLAYFUL hand lens soft; characters half frame; empty speech bubbles",
            "DIAGRAM-SOFT minerals light soft; tiny figures; empty speech bubbles",
            "MEDIUM compare rocks soft; boy and robot half frame; empty speech bubbles",
            "ENDING boy and robot soft smile; one-third; empty speech bubbles",
        ],
    },
    "E-E17": {
        "title": "What Is an Island?",
        "folder": "Earth",
        "tag": "Island",
        "companion": "girl",
        "pages": [
            'Water all around a land patch. "What’s an island?"',
            "An island is land completely surrounded by water.",
            "Some rise from volcanoes under the sea.",
            "Others are tips of underwater mountains.",
            "River islands form where channels split.",
            "People, plants, and animals can live on islands.",
            "Bridges or boats connect many islands to shore.",
            "Tides can change the wet edges each day.",
            "Protect island shores—they are delicate homes.",
            "Land + water all around = island.",
            "Find an island on a map with a grown-up.",
            "Surrounded land: island science.",
        ],
        "bubbles": [
            ("Land in water!", "Island?"),
            ("Land surrounded", "by water."),
            ("Some from", "volcanoes."),
            ("Tips of undersea", "mountains."),
            ("River channels", "make some."),
            ("Life can live", "there."),
            ("Boats bridges", "connect."),
            ("Tides change", "edges."),
            ("Protect shore", "homes."),
            ("Land plus", "water around."),
            ("Find on map", "together."),
            ("Island", "science."),
        ],
        "scenes": [
            "WIDE soft island in blue water; girl and robot one-third; empty speech bubbles",
            "DIAGRAM-SOFT surrounded by water soft; tiny figures; empty speech bubbles",
            "CLOSE volcano island soft gentle; girl points; robot; empty speech bubbles",
            "MEDIUM undersea mountain tip soft; characters half frame; empty speech bubbles",
            "PLAYFUL river island soft; characters half frame; empty speech bubbles",
            "WIDE life on island soft; characters one-third; empty speech bubbles",
            "CLOSE boat bridge soft; characters half frame; empty speech bubbles",
            "MEDIUM tides edges soft; characters half frame; empty speech bubbles",
            "PLAYFUL protect shores soft; characters half frame; empty speech bubbles",
            "DIAGRAM-SOFT land water around soft; tiny figures; empty speech bubbles",
            "MEDIUM map find soft; girl and robot half frame; empty speech bubbles",
            "ENDING girl and robot soft smile; one-third; empty speech bubbles",
        ],
    },
    "E-E18": {
        "title": "Why Do Earthquakes Happen?",
        "folder": "Earth",
        "tag": "Quake",
        "companion": "boy",
        "pages": [
            'The floor wiggles in a drill. "Why quakes?" asks Max.',
            "Earth’s plates push, pull, and slide past each other.",
            "Stress builds until rock slips along a fault.",
            "That sudden slip sends shaking waves.",
            "Most quakes are small; some feel stronger.",
            "Buildings can be made to sway more safely.",
            "Drop, cover, and hold on in a practice drill.",
            "Grown-ups make family safety plans.",
            "Aftershocks are smaller follow-up shakes.",
            "Plate slip → shake waves.",
            "Practice a calm drill with a grown-up.",
            "Shake sense: earthquake science.",
        ],
        "bubbles": [
            ("Floor wiggle!", "Why quakes?"),
            ("Plates push pull", "slide."),
            ("Stress slips on", "a fault."),
            ("Slip sends", "shake waves."),
            ("Many small;", "some stronger."),
            ("Safer buildings", "sway."),
            ("Drop cover", "hold on."),
            ("Family safety", "plans."),
            ("Aftershocks", "follow."),
            ("Plate slip", "waves."),
            ("Practice drill", "together."),
            ("Quake", "science."),
        ],
        "scenes": [
            "WIDE soft home drill calm; boy and robot one-third; empty speech bubbles",
            "DIAGRAM-SOFT plates push soft; tiny figures; empty speech bubbles",
            "CLOSE fault slip soft gentle; boy points; robot; empty speech bubbles",
            "MEDIUM shake waves soft; characters half frame; empty speech bubbles",
            "PLAYFUL small vs stronger soft; characters half frame; empty speech bubbles",
            "WIDE safer building soft; characters one-third; empty speech bubbles",
            "CLOSE drop cover hold soft; characters half frame; empty speech bubbles",
            "MEDIUM family plan soft; characters half frame; empty speech bubbles",
            "PLAYFUL aftershocks soft; characters half frame; empty speech bubbles",
            "DIAGRAM-SOFT plate slip waves soft; tiny figures; empty speech bubbles",
            "MEDIUM practice drill soft; boy and robot half frame; empty speech bubbles",
            "ENDING boy and robot soft smile; one-third; empty speech bubbles",
        ],
    },
    "E-E19": {
        "title": "What Are Minerals?",
        "folder": "Earth",
        "tag": "Minerals",
        "companion": "girl",
        "pages": [
            'Shiny salt and a pebble. "What are minerals?"',
            "Minerals are natural solid bits with set recipes.",
            "They grow as crystals with ordered insides.",
            "Rocks are often mixtures of several minerals.",
            "Salt, quartz, and gold are mineral examples.",
            "We use minerals in phones, bikes, and buildings.",
            "Hardness and color help scientists tell them apart.",
            "Collecting is fine where rules allow—ask first.",
            "Wash hands after handling outdoor finds.",
            "Recipe + crystal = mineral.",
            "Sort three pebbles by sparkle with a grown-up.",
            "Building blocks: mineral science.",
        ],
        "bubbles": [
            ("Salt pebble!", "Minerals?"),
            ("Natural solids", "with recipes."),
            ("Crystals ordered", "inside."),
            ("Rocks mix", "minerals."),
            ("Salt quartz", "gold."),
            ("Used in phones", "bikes."),
            ("Hardness color", "clues."),
            ("Ask before", "collecting."),
            ("Wash hands", "after."),
            ("Recipe plus", "crystal."),
            ("Sort pebbles", "together."),
            ("Mineral", "science."),
        ],
        "scenes": [
            "WIDE soft table salt pebble; girl and robot one-third; empty speech bubbles",
            "DIAGRAM-SOFT mineral recipe soft; tiny figures; empty speech bubbles",
            "CLOSE crystal ordered soft; girl points; robot; empty speech bubbles",
            "MEDIUM rock mix soft; characters half frame; empty speech bubbles",
            "PLAYFUL salt quartz gold soft; characters half frame; empty speech bubbles",
            "WIDE phones bikes soft; characters one-third; empty speech bubbles",
            "CLOSE hardness color soft; characters half frame; empty speech bubbles",
            "MEDIUM ask collect soft; characters half frame; empty speech bubbles",
            "PLAYFUL wash hands soft; characters half frame; empty speech bubbles",
            "DIAGRAM-SOFT recipe crystal soft; tiny figures; empty speech bubbles",
            "MEDIUM sort pebbles soft; girl and robot half frame; empty speech bubbles",
            "ENDING girl and robot soft smile; one-third; empty speech bubbles",
        ],
    },
    "E-E20": {
        "title": "Why Do Beaches Have Sand?",
        "folder": "Earth",
        "tag": "Sand",
        "companion": "boy",
        "pages": [
            'Toes in warm sand. "Where does sand come from?"',
            "Waves and weather break rocks into tiny grains.",
            "Rivers carry grains toward the sea.",
            "Shells and coral can become soft pale sand too.",
            "Wind and water sort grains into beaches.",
            "Different rocks make different sand colors.",
            "Dunes can form when wind piles dry sand.",
            "Leave shells where parks ask you to.",
            "Rinse sandy feet before going indoors.",
            "Break, carry, sort: beach sand.",
            "Look at sand grains with a magnifier together.",
            "Tiny rocks: sand science.",
        ],
        "bubbles": [
            ("Warm sand!", "From where?"),
            ("Waves break", "rocks."),
            ("Rivers carry", "grains."),
            ("Shells can make", "pale sand."),
            ("Wind water", "sort beaches."),
            ("Colors from", "rocks."),
            ("Wind piles", "dunes."),
            ("Leave shells", "if asked."),
            ("Rinse sandy", "feet."),
            ("Break carry", "sort."),
            ("Magnify grains", "together."),
            ("Sand", "science."),
        ],
        "scenes": [
            "WIDE soft sunny beach toes sand; boy and robot one-third; empty speech bubbles",
            "DIAGRAM-SOFT waves break rocks soft; tiny figures; empty speech bubbles",
            "CLOSE river carry grains soft; boy points; robot; empty speech bubbles",
            "MEDIUM shells pale sand soft; characters half frame; empty speech bubbles",
            "PLAYFUL wind water sort soft; characters half frame; empty speech bubbles",
            "WIDE sand colors soft; characters one-third; empty speech bubbles",
            "CLOSE dunes wind soft; characters half frame; empty speech bubbles",
            "MEDIUM leave shells soft; characters half frame; empty speech bubbles",
            "PLAYFUL rinse feet soft; characters half frame; empty speech bubbles",
            "DIAGRAM-SOFT break carry sort soft; tiny figures; empty speech bubbles",
            "MEDIUM magnify grains soft; boy and robot half frame; empty speech bubbles",
            "ENDING boy and robot soft smile; one-third; empty speech bubbles",
        ],
    },
    "E-E21": {
        "title": "What Is Compost?",
        "folder": "Earth",
        "tag": "Compost",
        "companion": "girl",
        "pages": [
            'A bin of leaves and peels. "What is compost?"',
            "Compost is food scraps and yard bits broken down.",
            "Tiny helpers—bugs, fungi, microbes—do the work.",
            "Air and a little moisture keep the helpers happy.",
            "Over time scraps become dark crumbly soil food.",
            "Fruit peels yes; meat and oily scraps often no.",
            "Finished compost feeds gardens gently.",
            "Less kitchen trash goes to the landfill.",
            "Wash hands after helping with the bin.",
            "Scraps + helpers = garden gold.",
            "Add a banana peel with a grown-up’s bin rules.",
            "Kitchen to garden: compost science.",
        ],
        "bubbles": [
            ("Leaves peels!", "Compost?"),
            ("Scraps break", "down."),
            ("Bugs fungi", "microbes."),
            ("Air moisture", "help."),
            ("Becomes soil", "food."),
            ("Peels yes;", "meat often no."),
            ("Feeds gardens", "gently."),
            ("Less landfill", "trash."),
            ("Wash hands", "after."),
            ("Scraps helpers", "gold."),
            ("Add peel", "together."),
            ("Compost", "science."),
        ],
        "scenes": [
            "WIDE soft yard compost bin; girl and robot one-third; empty speech bubbles",
            "DIAGRAM-SOFT scraps break down soft; tiny figures; empty speech bubbles",
            "CLOSE bugs fungi soft gentle; girl points; robot; empty speech bubbles",
            "MEDIUM air moisture soft; characters half frame; empty speech bubbles",
            "PLAYFUL dark crumbly soft; characters half frame; empty speech bubbles",
            "WIDE peels yes meat no soft; characters one-third; empty speech bubbles",
            "CLOSE feed garden soft; characters half frame; empty speech bubbles",
            "MEDIUM less landfill soft; characters half frame; empty speech bubbles",
            "PLAYFUL wash hands soft; characters half frame; empty speech bubbles",
            "DIAGRAM-SOFT scraps helpers gold soft; tiny figures; empty speech bubbles",
            "MEDIUM add peel soft; girl and robot half frame; empty speech bubbles",
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
    ref_dir = ROOT / ".comic_refs" / "w24_by_story"
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

    Path("/Users/song/qwen3-tts/comic_batch/comics_plan_en_backcatalog_w24.json").write_text(
        json.dumps(plan, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    Path("/Users/song/qwen3-tts/comic_batch/en_work/_raw_backcatalog_w24").mkdir(parents=True, exist_ok=True)
    Path("/Users/song/qwen3-tts/comic_batch/en_work/backcatalog_w24_prompts.json").write_text(
        json.dumps(prompts, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    bubbles_path = ROOT / "EyeHaven" / "ComicBubbleWords.en.json"
    bubbles = json.loads(bubbles_path.read_text(encoding="utf-8"))
    for sid, st in STORIES.items():
        bubbles[sid] = [{"i": i, "left": L, "right": R} for i, (L, R) in enumerate(st["bubbles"], 1)]
    bubbles_path.write_text(json.dumps(bubbles, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("wave24 done", len(STORIES), "prompts", len(prompts))


if __name__ == "__main__":
    main()
