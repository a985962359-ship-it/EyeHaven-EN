#!/usr/bin/env python3
"""Back-catalog wave 6: Animals E-A06…E-A13 → 12-page books.

Owner sleeping: continue without asking. Casting = content-fit + even neutrals.
Classic empty-bubble lettering later. EN only. Do not touch RestSession.
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

STORIES = {'E-A06': {'title': 'Why Do Bees Make Honey?',
           'folder': 'Animals',
           'tag': 'Honey',
           'companion': 'girl',
           'pages': ['A bee visits a flower. "Snack time?" asks Guangguang.',
                     'Bees collect sweet nectar from blossoms.',
                     'They carry it home to the hive in tiny belly tanks.',
                     'In the hive, bees pass nectar and fan their wings.',
                     'Fanning dries water out until nectar turns thick.',
                     'That thick golden food is honey for the colony.',
                     'Honey helps bees through cold or flower-scarce days.',
                     'While bees work, pollen sticks to their fuzzy bodies.',
                     'Pollen rides to other flowers and helps make seeds.',
                     'Honey is bee food first—people treat it carefully.',
                     'Watch bees from a safe distance with a grown-up.',
                     'Busy bees, sweet honey, and flowers that need friends.'],
           'bubbles': [('Flower visit!', 'Snack time?'),
                       ('Sweet nectar', 'from blooms.'),
                       ('Belly tanks', 'carry home.'),
                       ('Pass + fan', 'in the hive.'),
                       ('Water dries;', 'nectar thick.'),
                       ('Golden honey', 'for bees.'),
                       ('Food for', 'cold days.'),
                       ('Fuzzy bodies', 'catch pollen.'),
                       ('Pollen helps', 'make seeds.'),
                       ('Bee food first;', 'share kindly.'),
                       ('Watch safe', 'with grown-ups.'),
                       ('Busy bees.', 'Flower friends.')],
           'scenes': ['WIDE sunny garden flowers; girl and robot one-third; soft bee near bloom; '
                      'empty speech bubbles',
                      'CLOSE flower with soft bee sipping nectar cartoon; characters half frame; '
                      'empty speech bubbles',
                      'MEDIUM bee flying to hive soft; girl points; robot glow; half frame; empty '
                      'speech bubbles',
                      'INSIDE soft hive cartoon hexagons; tiny bee helpers; characters small edge; '
                      'empty speech bubbles',
                      'DIAGRAM-SOFT wing fanning drying nectar; tiny figures; empty speech bubbles',
                      'CLOSE honey jar soft glow not sticky mess; characters half frame; empty '
                      'speech bubbles',
                      'WIDE winter-soft hive outside snow light; characters one-third; empty '
                      'speech bubbles',
                      'CLOSE fuzzy bee with pollen dots soft; girl curious; robot; half frame; '
                      'empty speech bubbles',
                      'SPLIT flower to seed soft diagram; characters half frame; empty speech '
                      'bubbles',
                      'MEDIUM kitchen table honey taste carefully with grown-up hint; characters '
                      'half frame; empty speech bubbles',
                      'WIDE garden path watching bees from afar; girl and robot one-third; empty '
                      'speech bubbles',
                      'ENDING girl and robot smile by flowers; soft bee nearby; one-third; empty '
                      'speech bubbles']},
 'E-A07': {'title': 'Why Are Some Animals Striped?',
           'folder': 'Animals',
           'tag': 'Stripes',
           'companion': 'boy',
           'pages': ['A zebra picture makes Guangguang tilt. "Fashion?"',
                     'Stripes can be more than decoration.',
                     'For a tiger in tall grass, stripes break up its shape.',
                     'Prey may not notice the outline as quickly.',
                     'For zebras in a group, many stripes can blur together.',
                     'A hunter may struggle to pick just one zebra.',
                     'Patterns match the places animals live and hide.',
                     'Spots, stripes, and colors can be survival tools.',
                     'Not every striped animal uses stripes the same way.',
                     'Science keeps learning from photos, tracks, and studies.',
                     'Next time you see stripes, ask: help or just pretty?',
                     'Patterns can be beautiful and useful at once.'],
           'bubbles': [('Zebra pic!', 'Fashion?'),
                       ('Stripes do', 'more.'),
                       ('Tall grass', 'hides shape.'),
                       ('Outline hard', 'to see.'),
                       ('Herd blur', 'of stripes.'),
                       ('Hard to pick', 'just one.'),
                       ('Patterns fit', 'homes.'),
                       ('Colors can', 'help survive.'),
                       ('Not always', 'same job.'),
                       ('Science keeps', 'learning.'),
                       ('Help or', 'pretty?'),
                       ('Beautiful +', 'useful.')],
           'scenes': ['MEDIUM desk zebra photo book; boy and robot half frame; empty speech '
                      'bubbles',
                      'WIDE soft savanna; stripe icons floating soft; characters one-third; empty '
                      'speech bubbles',
                      'THROUGH tall green grass tiger soft not scary; characters small; empty '
                      'speech bubbles',
                      'CLOSE outline broken by stripes diagram soft; characters half frame; empty '
                      'speech bubbles',
                      'WIDE zebra herd soft cartoon; boy and robot one-third; empty speech bubbles',
                      'DIAGRAM-SOFT hunter confuse soft dots; tiny figures; empty speech bubbles',
                      'SPLIT forest spots vs grass stripes soft; characters half frame; empty '
                      'speech bubbles',
                      'MEDIUM nature tools icons soft; boy nods; robot; half frame; empty speech '
                      'bubbles',
                      'CLOSE different striped animals soft collage; characters edge; empty speech '
                      'bubbles',
                      'PLAYFUL science notebook and binoculars soft; boy and robot half frame; '
                      'empty speech bubbles',
                      'WIDE boy points at stripe poster; robot glow; one-third; empty speech '
                      'bubbles',
                      'ENDING boy and robot smile at zebra art; peaceful; one-third; empty speech '
                      'bubbles']},
 'E-A08': {'title': 'Why Did Dinosaurs Get So Big?',
           'folder': 'Animals',
           'tag': 'DinoSize',
           'companion': 'boy',
           'pages': ['Guangguang holds a tiny toy T. rex. "School-bus big!"',
                     'Long ago, Earth had different plants and climates.',
                     'Some dinosaurs grew huge over many generations.',
                     'Big bodies can help reach high leaves for food.',
                     'Size can also help with defense in a wild world.',
                     'Growing big needs lots of food and time.',
                     'Not every dinosaur was a giant.',
                     'Many were chicken-sized or about dog-sized.',
                     'Fossils show bones, teeth, and footprints.',
                     'Scientists guess size and diet from those clues.',
                     'Movies exaggerate; fossils keep us honest.',
                     'Big or small, dinosaurs were real animals once.'],
           'bubbles': [('Tiny toy!', 'School-bus big?'),
                       ('Old Earth,', 'different world.'),
                       ('Grew huge', 'over time.'),
                       ('High leaves', 'for giants.'),
                       ('Size can', 'help defend.'),
                       ('Big needs', 'lots of food.'),
                       ('Not all', 'were giants.'),
                       ('Some small', 'like chickens.'),
                       ('Bones teeth', 'footprints.'),
                       ('Clues tell', 'size + diet.'),
                       ('Movies big;', 'fossils true.'),
                       ('Real animals', 'long ago.')],
           'scenes': ['MEDIUM playroom toy dinosaur; boy and robot half frame; empty speech '
                      'bubbles',
                      'WIDE soft prehistoric landscape kid-safe greens; characters one-third; '
                      'empty speech bubbles',
                      'DIAGRAM-SOFT growth across generations soft; tiny figures; empty speech '
                      'bubbles',
                      'CLOSE tall plant leaves soft; long-neck silhouette friendly; characters '
                      'edge; empty speech bubbles',
                      'PLAYFUL big vs small dino soft compare; boy points; robot; half frame; '
                      'empty speech bubbles',
                      'MEDIUM food pile cartoon soft; hungry giant gentle; characters half frame; '
                      'empty speech bubbles',
                      'SPLIT giant vs tiny dinosaur soft; characters half frame; empty speech '
                      'bubbles',
                      'CLOSE chicken-size dino soft cute; boy smiles; robot; half frame; empty '
                      'speech bubbles',
                      'WIDE fossil dig soft sand; bones outline; characters one-third; empty '
                      'speech bubbles',
                      'MEDIUM scientists with measuring tape soft; boy watches; robot; half frame; '
                      'empty speech bubbles',
                      'SPLIT movie screen exaggerate vs fossil case soft; characters half frame; '
                      'empty speech bubbles',
                      'ENDING museum hall soft; boy and robot admire fossils; one-third; empty '
                      'speech bubbles']},
 'E-A09': {'title': 'What Did T. rex Eat?',
           'folder': 'Animals',
           'tag': 'Trex',
           'companion': 'boy',
           'pages': ['Guangguang shows long pointed teeth. "Salad?"',
                     'Tyrannosaurus rex had strong jaws and sharp teeth.',
                     'Those tools fit meat better than leafy salads.',
                     'It may have hunted living animals.',
                     'It may also have eaten animals already dead.',
                     'Big meat-eaters can do both kinds of feeding.',
                     'Tooth shape is a helpful clue.',
                     'Flat grinders often mean plant foods.',
                     'Sharp slicers often mean meat foods.',
                     'We learn from fossils, not movies alone.',
                     'T. rex was a powerful biter of its time.',
                     'Teeth tell stories if we look carefully.'],
           'bubbles': [('Pointy teeth!', 'Salad?'),
                       ('Strong jaws,', 'sharp teeth.'),
                       ('Built for', 'meat foods.'),
                       ('Maybe hunted', 'live prey.'),
                       ('Maybe ate', 'already dead.'),
                       ('Both can', 'be true.'),
                       ('Tooth shape', 'is a clue.'),
                       ('Flat grinders', 'plants.'),
                       ('Sharp slicers', 'meat.'),
                       ('Fossils teach', 'better.'),
                       ('Powerful bite', 'long ago.'),
                       ('Teeth tell', 'stories.')],
           'scenes': ['MEDIUM fossil tooth display soft not scary; boy and robot half frame; empty '
                      'speech bubbles',
                      'CLOSE strong jaw fossil soft cartoon; characters half frame; empty speech '
                      'bubbles',
                      'DIAGRAM-SOFT meat icon vs salad myth soft; tiny figures; empty speech '
                      'bubbles',
                      'WIDE soft prehistoric plain kid-safe; distant gentle trex silhouette; '
                      'characters one-third; empty speech bubbles',
                      'MEDIUM scavenger birds soft compare idea; boy thinks; robot; half frame; '
                      'empty speech bubbles',
                      'SPLIT hunt vs scavenge soft icons; characters half frame; empty speech '
                      'bubbles',
                      'CLOSE plant-grinder tooth vs sharp tooth soft; characters half frame; empty '
                      'speech bubbles',
                      'PLAYFUL leaf pile ignored soft joke; boy laughs; robot; half frame; empty '
                      'speech bubbles',
                      'MEDIUM meat-slicer tooth soft science; characters half frame; empty speech '
                      'bubbles',
                      'WIDE museum fossil case; boy and robot one-third; empty speech bubbles',
                      'CLOSE powerful bite diagram soft arrows; characters half frame; empty '
                      'speech bubbles',
                      'ENDING boy and robot nod at tooth clue poster; one-third; empty speech '
                      'bubbles']},
 'E-A10': {'title': 'Why Do Whales Spout Water?',
           'folder': 'Animals',
           'tag': 'Spout',
           'companion': 'girl',
           'pages': ['A whale blows a misty fountain. "Water fountain?"',
                     'Whales are mammals with lungs, not gills.',
                     'They must breathe air at the surface.',
                     'A blowhole sits on top of the head.',
                     'Warm breath whooshes out when the whale surfaces.',
                     'Cool air can turn that breath into mist.',
                     'The spout looks like water, but it is mostly breath cloud.',
                     'Then the whale breathes in and can dive again.',
                     'Different whales make different spout shapes.',
                     'Watch from a safe boat with grown-ups.',
                     'Kind watching keeps ocean friends safer.',
                     'Lungs, blowholes, and misty hellos at sea.'],
           'bubbles': [('Misty spout!', 'Fountain?'),
                       ('Mammals with', 'lungs.'),
                       ('Need air', 'up top.'),
                       ('Blowhole on', 'the head.'),
                       ('Warm breath', 'whooshes out.'),
                       ('Cool air makes', 'mist.'),
                       ('Mostly breath', 'cloud.'),
                       ('Breathe in,', 'then dive.'),
                       ('Spout shapes', 'differ.'),
                       ('Safe boat', 'with grown-ups.'),
                       ('Kind watching', 'helps.'),
                       ('Misty hellos', 'at sea.')],
           'scenes': ['WIDE soft ocean whale spout mist; girl and robot on safe boat one-third; '
                      'empty speech bubbles',
                      'DIAGRAM-SOFT lungs vs fish gills soft; tiny figures; empty speech bubbles',
                      'MEDIUM whale surfacing soft; characters half frame; empty speech bubbles',
                      'CLOSE blowhole soft cartoon; characters half frame; empty speech bubbles',
                      'ACTION breath whoosh mist soft; girl points; robot; half frame; empty '
                      'speech bubbles',
                      'SPLIT warm breath + cool air = mist soft; characters half frame; empty '
                      'speech bubbles',
                      'PLAYFUL not a mouth spray myth soft; robot shakes head kindly; girl nods; '
                      'half frame; empty speech bubbles',
                      'WIDE whale diving soft arc; characters one-third; empty speech bubbles',
                      'MEDIUM different spout shape icons soft; characters half frame; empty '
                      'speech bubbles',
                      'WIDE family boat with grown-up; girl and robot one-third; empty speech '
                      'bubbles',
                      'CLOSE kind binoculars watching soft; characters half frame; empty speech '
                      'bubbles',
                      'ENDING girl and robot wave at distant spout; peaceful sea; one-third; empty '
                      'speech bubbles']},
 'E-A11': {'title': 'Why Do Sharks Have So Many Teeth?',
           'folder': 'Animals',
           'tag': 'Teeth',
           'companion': 'boy',
           'pages': ['Guangguang counts cartoon shark teeth. "A hundred?"',
                     'Sharks grow many teeth in rows.',
                     'When a front tooth wears out, another can move up.',
                     'That keeps a working set for slippery food.',
                     'Lots of teeth means replaceable tools.',
                     'It does not mean a shark is "mean."',
                     'Different sharks eat different meals.',
                     'Some chase fish; some filter tiny plankton.',
                     'Healthy oceans help sharks and other sea life.',
                     'Respect wild sharks from a safe distance.',
                     'Teeth are tools that get replaced over time.',
                     'Ocean neighbors need clean, living seas.'],
           'bubbles': [('Count teeth!', 'A hundred?'),
                       ('Many teeth', 'in rows.'),
                       ('New tooth', 'moves up.'),
                       ('Working set', 'stays ready.'),
                       ('Replaceable', 'tools.'),
                       ('Not mean—', 'just tools.'),
                       ('Sharks eat', 'different meals.'),
                       ('Fish or', 'plankton.'),
                       ('Healthy seas', 'help all.'),
                       ('Watch safe', 'from afar.'),
                       ('Teeth get', 'replaced.'),
                       ('Clean oceans', 'matter.')],
           'scenes': ['MEDIUM soft cartoon shark smile not scary; boy and robot half frame; empty '
                      'speech bubbles',
                      'DIAGRAM-SOFT tooth rows conveyor soft; tiny figures; empty speech bubbles',
                      'CLOSE worn tooth replaced soft; characters half frame; empty speech bubbles',
                      'PLAYFUL slippery fish cartoon soft; shark gentle; characters edge; empty '
                      'speech bubbles',
                      'MEDIUM toolbox metaphor soft teeth tools; boy nods; robot; half frame; '
                      'empty speech bubbles',
                      'WIDE friendly ocean class poster soft; characters one-third; empty speech '
                      'bubbles',
                      'SPLIT chase fish vs plankton cruise soft; characters half frame; empty '
                      'speech bubbles',
                      'CLOSE plankton sparkles soft; gentle shark; characters half frame; empty '
                      'speech bubbles',
                      'WIDE healthy reef soft colors; boy and robot one-third; empty speech '
                      'bubbles',
                      'MEDIUM shore watching with grown-up soft; characters half frame; empty '
                      'speech bubbles',
                      'DIAGRAM-SOFT tooth replacement timeline; tiny figures; empty speech bubbles',
                      'ENDING boy and robot thumbs-up ocean care poster; one-third; empty speech '
                      'bubbles']},
 'E-A12': {'title': 'Why Do Camels Have Humps?',
           'folder': 'Animals',
           'tag': 'Humps',
           'companion': 'boy',
           'pages': ['A camel hump looks like a backpack. "Water tank?"',
                     'A camel’s hump stores fat, not a jug of water.',
                     'Fat is energy when food is hard to find.',
                     'Deserts can be hot, dry, and scarce of snacks.',
                     'Camels also save water with clever bodies.',
                     'They handle heat and thirst better than many animals.',
                     'People once guessed humps were water bottles.',
                     'Science says: energy packs for the journey.',
                     'One-hump and two-hump camels both use fat stores.',
                     'After a hard trip, a soft hump can look leaner.',
                     'Food and rest help the energy pack refill.',
                     'Desert travelers with built-in snack backpacks.'],
           'bubbles': [('Backpack hump!', 'Water tank?'),
                       ('Fat store,', 'not water.'),
                       ('Energy when', 'food scarce.'),
                       ('Deserts are', 'tough.'),
                       ('Bodies save', 'water too.'),
                       ('Handle heat', 'and thirst.'),
                       ('Old guess:', 'water bottle.'),
                       ('Science: energy', 'packs.'),
                       ('One hump or', 'two.'),
                       ('Hard trip,', 'leaner hump.'),
                       ('Food + rest', 'refill.'),
                       ('Desert snack', 'backpacks.')],
           'scenes': ['WIDE soft desert dune; camel; boy and robot one-third; empty speech bubbles',
                      'DIAGRAM-SOFT hump fat not water myth soft; tiny figures; empty speech '
                      'bubbles',
                      'CLOSE hump energy icon soft; characters half frame; empty speech bubbles',
                      'MEDIUM scarce plants desert soft; camel walks; characters half frame; empty '
                      'speech bubbles',
                      'PLAYFUL water bottle myth crossed soft; robot shakes head; boy; half frame; '
                      'empty speech bubbles',
                      'WIDE sunny desert trail soft; characters one-third; empty speech bubbles',
                      'MEDIUM science book correction soft; boy reads; robot; half frame; empty '
                      'speech bubbles',
                      'SPLIT one-hump vs two-hump soft; characters half frame; empty speech '
                      'bubbles',
                      'CLOSE leaner hump after journey soft; characters half frame; empty speech '
                      'bubbles',
                      'MEDIUM resting camel eating soft; boy smiles; robot; half frame; empty '
                      'speech bubbles',
                      'WIDE oasis stop soft; characters one-third; empty speech bubbles',
                      'ENDING boy and robot wave to camel; warm desert light; one-third; empty '
                      'speech bubbles']},
 'E-A13': {'title': 'Why Do Owls Stay Up at Night?',
           'folder': 'Animals',
           'tag': 'Owls',
           'companion': 'girl',
           'pages': ['An owl’s eyes look round and ready. "Night shift?"',
                     'Many owls hunt when nights are busy with small animals.',
                     'Mice and other snacks often move after dark.',
                     'Soft feathers help owls fly with quiet wings.',
                     'Big eyes gather dim moonlight and starlight.',
                     'Keen ears help find tiny rustling sounds.',
                     'Night tools fit night hunting.',
                     'Not every owl is strictly a night-only bird.',
                     'Some hunt at dawn or dusk too.',
                     'A hoot in the dark can mean a quiet flyer nearby.',
                     'Listen softly; give wild owls space.',
                     'Night-shift neighbors with silent wings.'],
           'bubbles': [('Round eyes!', 'Night shift?'),
                       ('Busy nights', 'for hunting.'),
                       ('Small animals', 'move then.'),
                       ('Quiet soft', 'feathers.'),
                       ('Big eyes', 'gather light.'),
                       ('Ears find', 'tiny sounds.'),
                       ('Night tools', 'fit night.'),
                       ('Not always', 'only night.'),
                       ('Dawn or dusk', 'too.'),
                       ('A hoot means', 'nearby.'),
                       ('Listen soft;', 'give space.'),
                       ('Silent wing', 'neighbors.')],
           'scenes': ['WIDE soft twilight tree; owl perch; girl and robot one-third; empty speech '
                      'bubbles',
                      'MEDIUM moonlit meadow soft; tiny mouse hint gentle; characters half frame; '
                      'empty speech bubbles',
                      'CLOSE quiet wing feathers soft; characters half frame; empty speech bubbles',
                      'DIAGRAM-SOFT big eyes gather light; tiny figures; empty speech bubbles',
                      'CLOSE ear tufts listening soft; girl curious; robot; half frame; empty '
                      'speech bubbles',
                      'PLAYFUL night toolkit icons soft; characters half frame; empty speech '
                      'bubbles',
                      'SPLIT night owl vs dusk owl soft; characters half frame; empty speech '
                      'bubbles',
                      'WIDE dawn soft sky with owl; characters one-third; empty speech bubbles',
                      'MEDIUM kids window hearing distant hoot soft; characters half frame; empty '
                      'speech bubbles',
                      'WIDE forest edge giving space soft; girl and robot one-third; empty speech '
                      'bubbles',
                      'CLOSE silent flight silhouette soft not scary; characters edge; empty '
                      'speech bubbles',
                      'ENDING girl and robot smile under stars; owl soft on branch; one-third; '
                      'empty speech bubbles']}}


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
    print("updated", companions_path)

    plan = []
    prompts = []
    girl_ref = Path("/Users/song/qwen3-tts/comic_batch/en_girl_ref.png")
    boy_ref = Path("/Users/song/qwen3-tts/comic_batch/en_boy_ref.png")
    gg_ref = Path("/Users/song/qwen3-tts/comic_batch/guangguang_ref.png")
    for sid, st in STORIES.items():
        g = st["companion"]
        prefix = PREFIX_GIRL if g == "girl" else PREFIX_BOY
        kid = girl_ref if g == "girl" else boy_ref
        refs = [str(p) for p in (gg_ref, kid) if p.exists()]
        panels = []
        for i, (scene, (left, right)) in enumerate(zip(st["scenes"], st["bubbles"]), 1):
            panels.append({
                "i": i,
                "scene": scene,
                "left": left,
                "right": right,
                "tag": f"{st['tag']} {i}/12",
                "narration": st["pages"][i - 1],
            })
            prompts.append({
                "id": sid,
                "i": i,
                "filename": f"c-{sid}-{i:02d}.jpg",
                "description": prefix + "Scene: " + scene,
                "refs": refs,
                "companion": g,
            })
        plan.append({"id": sid, "title": st["title"], "companion": g, "panels": panels})
        path = ROOT / "睡前有声稿" / "美国英文稿" / st["folder"] / f"{sid}.txt"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(st["title"] + "\n\n" + "\n\n".join(st["pages"]) + "\n", encoding="utf-8")
        print("wrote", path)

    plan_path = Path("/Users/song/qwen3-tts/comic_batch/comics_plan_en_backcatalog_w6.json")
    plan_path.write_text(json.dumps(plan, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("wrote", plan_path)

    raw_dir = Path("/Users/song/qwen3-tts/comic_batch/en_work/_raw_backcatalog_w6")
    raw_dir.mkdir(parents=True, exist_ok=True)
    prompts_path = Path("/Users/song/qwen3-tts/comic_batch/en_work/backcatalog_w6_prompts.json")
    prompts_path.write_text(json.dumps(prompts, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("wrote", prompts_path, "count", len(prompts))

    bubbles_path = ROOT / "EyeHaven" / "ComicBubbleWords.en.json"
    bubbles = json.loads(bubbles_path.read_text(encoding="utf-8"))
    for sid, st in STORIES.items():
        bubbles[sid] = [{"i": i, "left": L, "right": R} for i, (L, R) in enumerate(st["bubbles"], 1)]
    bubbles_path.write_text(json.dumps(bubbles, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("updated", bubbles_path)


if __name__ == "__main__":
    main()
