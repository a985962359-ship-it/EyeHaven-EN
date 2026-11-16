#!/usr/bin/env python3
"""Back-catalog wave 7: Animals E-A15…E-A22 → 12-page books. Owner sleeping; no questions."""
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
STORIES = {'E-A15': {'title': 'Why Do Ants Walk in a Line?',
           'folder': 'Animals',
           'tag': 'Ants',
           'companion': 'girl',
           'pages': ['Ants march in a neat line. "Parade?" asks Guangguang.',
                     'Ants leave scent trails for nest-mates to follow.',
                     'A good food find gets shared by the path they mark.',
                     'Other ants smell the trail and join the job.',
                     'Lines help many tiny workers move food efficiently.',
                     'Teamwork matters more than any one ant alone.',
                     'If a trail goes cold, ants may search new routes.',
                     'Their nest is a busy underground city of rooms.',
                     'Watch ants outdoors from a gentle distance.',
                     'Do not poke nests—ants need calm space to work.',
                     'Little insects show big cooperation every day.',
                     'Follow the scent road: science in tiny steps.'],
           'bubbles': [('Neat line!', 'Parade?'),
                       ('Scent trails', 'guide friends.'),
                       ('Food find', 'gets shared.'),
                       ('Smell path,', 'join in.'),
                       ('Lines move', 'food fast.'),
                       ('Teamwork >', 'one ant.'),
                       ('Cold trail?', 'New search.'),
                       ('Busy nest', 'city.'),
                       ('Watch soft', 'from afar.'),
                       ("Don't poke", 'nests.'),
                       ('Tiny bugs,', 'big teams.'),
                       ('Scent road', 'science.')],
           'scenes': ['WIDE sidewalk ants soft line; girl and robot one-third; empty speech '
                      'bubbles',
                      'CLOSE scent trail dots soft diagram; characters half frame; empty speech '
                      'bubbles',
                      'MEDIUM crumb food find soft; ants; characters half frame; empty speech '
                      'bubbles',
                      'ACTION more ants joining line soft; girl points; robot; half frame; empty '
                      'speech bubbles',
                      'DIAGRAM-SOFT efficient line arrows; tiny figures; empty speech bubbles',
                      'PLAYFUL teamwork icons soft; characters half frame; empty speech bubbles',
                      'WIDE ants exploring new path soft; characters one-third; empty speech '
                      'bubbles',
                      'CUTAWAY soft underground nest rooms; characters edge; empty speech bubbles',
                      'MEDIUM garden watching gently; girl and robot half frame; empty speech '
                      'bubbles',
                      'CLOSE hands-off respect soft; robot nod; girl; half frame; empty speech '
                      'bubbles',
                      'WIDE ant line to nest soft; characters one-third; empty speech bubbles',
                      'ENDING girl and robot smile at tiny march; one-third; empty speech '
                      'bubbles']},
 'E-A16': {'title': 'Why Do Sea Turtles Come Ashore?',
           'folder': 'Animals',
           'tag': 'Turtles',
           'companion': 'girl',
           'pages': ['A turtle crawls onto sand. "Beach day?"',
                     'Many sea turtles lay eggs on sandy beaches.',
                     'They grew in the ocean but need land for nests.',
                     'A mother digs a soft pit above the tide line.',
                     'She lays eggs, covers them, then returns to sea.',
                     'Warm sand helps the eggs develop over time.',
                     'Hatchlings later race toward the bright ocean.',
                     'Lights and trash on beaches can confuse them.',
                     'Kind people keep nesting beaches dark and clean.',
                     'Never pick up wild hatchlings without experts.',
                     'Ocean homes, sandy nurseries, careful humans.',
                     'Sand, eggs, and a long swim ahead.'],
           'bubbles': [('On sand!', 'Beach day?'),
                       ('Eggs need', 'sandy nests.'),
                       ('Ocean life,', 'land nests.'),
                       ('Dig a pit', 'above tide.'),
                       ('Lay, cover,', 'back to sea.'),
                       ('Warm sand', 'helps eggs.'),
                       ('Hatchlings', 'race ocean.'),
                       ('Lights/trash', 'confuse.'),
                       ('Dark clean', 'beaches.'),
                       ('Leave wild', 'babies.'),
                       ('Ocean + sand', 'care.'),
                       ('Long swim', 'ahead.')],
           'scenes': ['WIDE moonlit beach turtle soft; girl and robot one-third; empty speech '
                      'bubbles',
                      'MEDIUM nesting sand soft; characters half frame; empty speech bubbles',
                      'DIAGRAM-SOFT ocean vs beach nest soft; tiny figures; empty speech bubbles',
                      'CLOSE digging nest soft cartoon; characters half frame; empty speech '
                      'bubbles',
                      'MEDIUM covering eggs soft; turtle to sea; characters half frame; empty '
                      'speech bubbles',
                      'CLOSE warm sand eggs soft; characters half frame; empty speech bubbles',
                      'WIDE hatchlings toward water soft; characters one-third; empty speech '
                      'bubbles',
                      'PLAYFUL beach trash crossed out soft; robot shakes head; girl; half frame; '
                      'empty speech bubbles',
                      'MEDIUM dark beach helpers soft grown-up; characters half frame; empty '
                      'speech bubbles',
                      'CLOSE hands-off hatchling soft; characters half frame; empty speech bubbles',
                      'WIDE sunrise sea soft; girl and robot one-third; empty speech bubbles',
                      'ENDING girl and robot wave to ocean; peaceful; one-third; empty speech '
                      'bubbles']},
 'E-A17': {'title': 'Why Do Frogs Jump So Far?',
           'folder': 'Animals',
           'tag': 'Frogs',
           'companion': 'boy',
           'pages': ['A frog leaps. Boing! "Super legs?"',
                     'Frog back legs are long and strong.',
                     'Muscles store a springy push for takeoff.',
                     'Webbed feet help landings and swimming too.',
                     'Jumping helps frogs catch food and escape danger.',
                     'Not every hop is the same length.',
                     'Some frogs climb; some swim more than they leap.',
                     'Look at the whole frog, not only the jump.',
                     'Wet skin needs moist places to stay healthy.',
                     'Ponds and clean water help frog neighbors.',
                     'Strong legs, soft landings, careful habitats.',
                     'Boing science: push, fly, splash.'],
           'bubbles': [('Boing leap!', 'Super legs?'),
                       ('Long strong', 'back legs.'),
                       ('Springy push', 'takeoff.'),
                       ('Webbed feet', 'help too.'),
                       ('Catch food,', 'escape.'),
                       ('Hops vary', 'in length.'),
                       ('Some climb', 'or swim.'),
                       ('Whole frog', 'matters.'),
                       ('Moist skin', 'needs damp.'),
                       ('Clean ponds', 'help.'),
                       ('Strong legs,', 'soft homes.'),
                       ('Push, fly,', 'splash.')],
           'scenes': ['WIDE pond edge frog leap soft; boy and robot one-third; empty speech '
                      'bubbles',
                      'CLOSE strong back legs soft; characters half frame; empty speech bubbles',
                      'DIAGRAM-SOFT spring push arrows soft; tiny figures; empty speech bubbles',
                      'MEDIUM webbed feet soft water; characters half frame; empty speech bubbles',
                      'ACTION frog catching bug soft cute; characters edge; empty speech bubbles',
                      'SPLIT short hop vs long hop soft; characters half frame; empty speech '
                      'bubbles',
                      'MEDIUM tree frog climb soft; boy points; robot; half frame; empty speech '
                      'bubbles',
                      'WIDE whole frog pose soft; characters one-third; empty speech bubbles',
                      'CLOSE moist skin dew soft; characters half frame; empty speech bubbles',
                      'WIDE clean pond habitat soft; boy and robot one-third; empty speech bubbles',
                      'PLAYFUL splash landing soft; characters half frame; empty speech bubbles',
                      'ENDING boy and robot cheer a gentle hop; one-third; empty speech bubbles']},
 'E-A18': {'title': 'Why Do Octopuses Have Eight Arms?',
           'folder': 'Animals',
           'tag': 'Octopus',
           'companion': 'boy',
           'pages': ['An octopus waves many arms. "Why eight?"',
                     'Eight arms help grab, taste, and explore.',
                     'Suckers can hold rocks, food, and tools.',
                     'Arms let an octopus open shells cleverly.',
                     'They also help crawl across the seafloor.',
                     'An octopus can squeeze through small gaps.',
                     'Soft bodies plus many arms make great explorers.',
                     'Ink and color changes help them stay safe.',
                     'Ocean rocks and reefs are favorite hideouts.',
                     'Watch gently in aquariums with grown-ups.',
                     'Eight helpers for a curious ocean mind.',
                     'Grab, taste, hide, explore.'],
           'bubbles': [('Many arms!', 'Why eight?'),
                       ('Grab taste', 'explore.'),
                       ('Suckers hold', 'stuff.'),
                       ('Open shells', 'cleverly.'),
                       ('Crawl the', 'seafloor.'),
                       ('Squeeze small', 'gaps.'),
                       ('Soft body', 'explorer.'),
                       ('Ink + color', 'safety.'),
                       ('Rocks reefs', 'homes.'),
                       ('Aquarium with', 'grown-ups.'),
                       ('Eight helper', 'arms.'),
                       ('Grab, hide,', 'explore.')],
           'scenes': ['WIDE soft reef octopus; boy and robot one-third; empty speech bubbles',
                      'CLOSE arm suckers soft; characters half frame; empty speech bubbles',
                      'MEDIUM octopus holding shell soft; characters half frame; empty speech '
                      'bubbles',
                      'PLAYFUL opening clam soft cartoon; boy amazed; robot; half frame; empty '
                      'speech bubbles',
                      'WIDE seafloor crawl soft; characters one-third; empty speech bubbles',
                      'DIAGRAM-SOFT squeeze through gap soft; tiny figures; empty speech bubbles',
                      'MEDIUM color-change camouflage soft; characters half frame; empty speech '
                      'bubbles',
                      'CLOSE ink puff soft not scary; characters half frame; empty speech bubbles',
                      'WIDE rocky hideout soft; characters one-third; empty speech bubbles',
                      'MEDIUM aquarium visit soft grown-up; boy and robot half frame; empty speech '
                      'bubbles',
                      'PLAYFUL eight arm count soft; characters half frame; empty speech bubbles',
                      'ENDING boy and robot wave to octopus; peaceful reef; one-third; empty '
                      'speech bubbles']},
 'E-A19': {'title': 'Why Do Penguins Huddle Together?',
           'folder': 'Animals',
           'tag': 'Penguins',
           'companion': 'girl',
           'pages': ['Penguins pack into a fluffy crowd. "Group hug?"',
                     'Cold winds steal heat from lonely birds.',
                     'A huddle shares warmth across many bodies.',
                     'Penguins take turns at the chilly outer edge.',
                     'Friends in the middle get a warmer break.',
                     'Huddles help eggs and chicks stay safer too.',
                     'Teamwork is survival on icy shores.',
                     'Not every penguin species huddles the same way.',
                     'Watching from afar keeps wild birds calm.',
                     'Warmth, turns, and togetherness matter here.',
                     'Cold places reward good neighbors.',
                     'Fluffy science: share the heat.'],
           'bubbles': [('Fluffy crowd!', 'Group hug?'),
                       ('Cold winds', 'steal heat.'),
                       ('Huddle shares', 'warmth.'),
                       ('Turns on the', 'cold edge.'),
                       ('Middle gets', 'warmer.'),
                       ('Eggs chicks', 'safer.'),
                       ('Teamwork =', 'survival.'),
                       ('Species differ', 'a bit.'),
                       ('Watch from', 'afar.'),
                       ('Warmth +', 'turns.'),
                       ('Good neighbors', 'help.'),
                       ('Share the', 'heat.')],
           'scenes': ['WIDE icy shore penguin huddle soft; girl and robot one-third; empty speech '
                      'bubbles',
                      'DIAGRAM-SOFT heat arrows in huddle; tiny figures; empty speech bubbles',
                      'MEDIUM dense fluffy huddle soft; characters half frame; empty speech '
                      'bubbles',
                      'CLOSE outer edge penguin soft; characters half frame; empty speech bubbles',
                      'ACTION penguins rotating turns soft; girl points; robot; half frame; empty '
                      'speech bubbles',
                      'MEDIUM chick in huddle soft; characters half frame; empty speech bubbles',
                      'WIDE blizzard soft background; huddle; characters one-third; empty speech '
                      'bubbles',
                      'SPLIT different penguin kinds soft; characters half frame; empty speech '
                      'bubbles',
                      'WIDE far viewers with binoculars soft; characters one-third; empty speech '
                      'bubbles',
                      'PLAYFUL warm heart icons soft; characters half frame; empty speech bubbles',
                      'MEDIUM teamwork poster soft; girl and robot half frame; empty speech '
                      'bubbles',
                      'ENDING girl and robot smile at huddle; peaceful ice; one-third; empty '
                      'speech bubbles']},
 'E-A20': {'title': 'Why Do Elephants Have Trunks?',
           'folder': 'Animals',
           'tag': 'Trunks',
           'companion': 'boy',
           'pages': ['An elephant trunk swings. "Super nose?"',
                     'A trunk is a nose and a helper hand together.',
                     'Elephants smell, breathe, and drink with it.',
                     'They can grab leaves and lift light objects.',
                     'Trunks spray water for cool baths.',
                     'Soft tip fingers help careful picking.',
                     'Babies practice trunk skills as they grow.',
                     'Herds use trunks in gentle hellos too.',
                     'Never tease wild elephants—give wide space.',
                     'Respect big animals with quiet watching.',
                     'Nose plus hand equals trunk power.',
                     'Smell, sip, spray, say hello.'],
           'bubbles': [('Swing trunk!', 'Super nose?'),
                       ('Nose + hand', 'together.'),
                       ('Smell breathe', 'drink.'),
                       ('Grab leaves,', 'lift light.'),
                       ('Spray cool', 'water baths.'),
                       ('Soft tip', 'picks gently.'),
                       ('Babies practice', 'skills.'),
                       ('Gentle herd', 'hellos.'),
                       ('Wide space', 'for wild.'),
                       ('Quiet watching', 'respect.'),
                       ('Trunk power', 'tools.'),
                       ('Smell sip', 'hello.')],
           'scenes': ['WIDE savanna elephant soft; boy and robot one-third; empty speech bubbles',
                      'CLOSE trunk tip soft; characters half frame; empty speech bubbles',
                      'MEDIUM drinking with trunk soft; characters half frame; empty speech '
                      'bubbles',
                      'ACTION grabbing leaves soft; boy amazed; robot; half frame; empty speech '
                      'bubbles',
                      'PLAYFUL water spray bath soft; characters half frame; empty speech bubbles',
                      'CLOSE delicate tip fingers soft; characters half frame; empty speech '
                      'bubbles',
                      'MEDIUM baby elephant learning soft; characters half frame; empty speech '
                      'bubbles',
                      'WIDE herd trunk hello soft; characters one-third; empty speech bubbles',
                      'DIAGRAM-SOFT give space distance soft; tiny figures; empty speech bubbles',
                      'MEDIUM calm watching with grown-up soft; boy and robot half frame; empty '
                      'speech bubbles',
                      'PLAYFUL trunk toolbox icons soft; characters half frame; empty speech '
                      'bubbles',
                      'ENDING boy and robot wave kindly from afar; one-third; empty speech '
                      'bubbles']},
 'E-A21': {'title': 'Why Do Giraffes Have Long Necks?',
           'folder': 'Animals',
           'tag': 'Giraffes',
           'companion': 'boy',
           'pages': ['A giraffe stretches high. "Why so tall?"',
                     'Long necks help reach leaves other animals miss.',
                     'Tall browsing can mean extra food options.',
                     'Necks also help giraffes watch for danger far away.',
                     'Strong hearts pump blood up that long path.',
                     'Special valves help blood flow carefully.',
                     'Calves grow into their height over time.',
                     'Not every tall animal uses height the same way.',
                     'Savanna trees and giraffes fit together.',
                     'Watch quietly; wild giraffes need calm space.',
                     'High snacks, far views, careful bodies.',
                     'Tall science under the sun.'],
           'bubbles': [('So tall!', 'Why?'),
                       ('Reach high', 'leaves.'),
                       ('Extra food', 'options.'),
                       ('See danger', 'far.'),
                       ('Strong heart', 'pumps up.'),
                       ('Valves help', 'blood flow.'),
                       ('Calves grow', 'taller.'),
                       ('Tall uses', 'differ.'),
                       ('Trees +', 'giraffes.'),
                       ('Watch calm', 'quietly.'),
                       ('High snacks,', 'far views.'),
                       ('Tall science', 'sun.')],
           'scenes': ['WIDE savanna giraffe soft; boy and robot one-third; empty speech bubbles',
                      'CLOSE high leaves browsing soft; characters half frame; empty speech '
                      'bubbles',
                      'MEDIUM giraffe among shorter animals soft; characters half frame; empty '
                      'speech bubbles',
                      'WIDE lookout tall neck soft; characters one-third; empty speech bubbles',
                      'DIAGRAM-SOFT heart to head blood path soft; tiny figures; empty speech '
                      'bubbles',
                      'CLOSE valve icons soft science; characters half frame; empty speech bubbles',
                      'MEDIUM calf beside adult soft; boy smiles; robot; half frame; empty speech '
                      'bubbles',
                      'SPLIT giraffe vs other browsers soft; characters half frame; empty speech '
                      'bubbles',
                      'WIDE acacia trees soft; characters one-third; empty speech bubbles',
                      'MEDIUM far viewing soft; characters half frame; empty speech bubbles',
                      'PLAYFUL height ruler soft cartoon; characters half frame; empty speech '
                      'bubbles',
                      'ENDING boy and robot gaze up at giraffe; warm light; one-third; empty '
                      'speech bubbles']},
 'E-A22': {'title': 'Why Do Spiders Spin Webs?',
           'folder': 'Animals',
           'tag': 'Webs',
           'companion': 'girl',
           'pages': ['A shiny web sparkles. "Art project?"',
                     'Many spiders spin silk from their bodies.',
                     'Webs can catch flying insects for food.',
                     'Different web shapes fit different hunting styles.',
                     'Silk is strong for its thin size.',
                     'Spiders may rebuild webs when weather tears them.',
                     'Not every spider waits on a big orb web.',
                     'Some hunt by chasing or hiding instead.',
                     'Most spiders are helpful neighbors for gardens.',
                     'Give them space; watch without touching webs.',
                     'Silk threads, patient hunters, tiny engineers.',
                     'Sparkle science between leaves.'],
           'bubbles': [('Shiny web!', 'Art project?'),
                       ('Silk from', 'their bodies.'),
                       ('Catch flying', 'insects.'),
                       ('Shapes fit', 'hunting.'),
                       ('Thin but', 'strong.'),
                       ('Rebuild after', 'tears.'),
                       ('Not all use', 'orb webs.'),
                       ('Some chase', 'or hide.'),
                       ('Garden helpers', 'often.'),
                       ('Watch, don’t', 'touch.'),
                       ('Tiny silk', 'engineers.'),
                       ('Sparkle', 'science.')],
           'scenes': ['WIDE garden web dew soft; girl and robot one-third; empty speech bubbles',
                      'CLOSE spinnerets silk soft cartoon; characters half frame; empty speech '
                      'bubbles',
                      'MEDIUM insect in web soft not scary; characters half frame; empty speech '
                      'bubbles',
                      'SPLIT orb vs other web shapes soft; characters half frame; empty speech '
                      'bubbles',
                      'DIAGRAM-SOFT strong thin silk; tiny figures; empty speech bubbles',
                      'ACTION rebuilding web soft; girl watches; robot; half frame; empty speech '
                      'bubbles',
                      'MEDIUM hunting spider no big web soft; characters half frame; empty speech '
                      'bubbles',
                      'WIDE garden veggies soft healthy; characters one-third; empty speech '
                      'bubbles',
                      'CLOSE hands-off respect soft; characters half frame; empty speech bubbles',
                      'PLAYFUL tiny engineer hardhat soft cute; characters half frame; empty '
                      'speech bubbles',
                      'WIDE morning dew sparkle soft; girl and robot one-third; empty speech '
                      'bubbles',
                      'ENDING girl and robot admire web sparkle; peaceful; one-third; empty speech '
                      'bubbles']}}

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

    plan_path = Path("/Users/song/qwen3-tts/comic_batch/comics_plan_en_backcatalog_w7.json")
    plan_path.write_text(json.dumps(plan, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("wrote", plan_path)

    raw_dir = Path("/Users/song/qwen3-tts/comic_batch/en_work/_raw_backcatalog_w7")
    raw_dir.mkdir(parents=True, exist_ok=True)
    prompts_path = Path("/Users/song/qwen3-tts/comic_batch/en_work/backcatalog_w7_prompts.json")
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
