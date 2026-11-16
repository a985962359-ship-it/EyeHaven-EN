#!/usr/bin/env python3
"""Back-catalog wave 8: Animals E-A23…E-A30 → 12-page books. Owner sleeping; no questions."""
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

STORIES = {
    "E-A23": {
        "title": "Why Do Bats Sleep Upside Down?",
        "folder": "Animals",
        "tag": "Bats",
        "companion": "boy",
        "pages": [
            'Guangguang hangs a sock by its toes. "Bats sleep upside down—why?"',
            "Bat feet lock around a perch so hanging takes little energy.",
            "Their legs and hips are built for dangling, not long walking.",
            "From a hang, a bat can drop and open wings into flight fast.",
            "Taking off from the ground is harder for many bat bodies.",
            "Caves, trees, and quiet roofs make safe upside-down bedrooms.",
            "Hanging high keeps bats away from many ground hunters.",
            "They rest by day and wake to hunt insects in soft night air.",
            "Echolocation clicks help some bats find food in the dark.",
            "Bats are helpers: many eat mosquitoes and other pests.",
            "Watch bats from a calm distance—never poke roosts.",
            "Toes lock, drop, and fly: a clever upside-down bedtime.",
        ],
        "bubbles": [
            ("Upside down?", "Why hang?"),
            ("Feet lock", "easy rest."),
            ("Built to", "dangle."),
            ("Drop then", "open wings."),
            ("Ground takeoff", "is hard."),
            ("Quiet roosts", "are beds."),
            ("High hang,", "safer."),
            ("Day rest,", "night hunt."),
            ("Clicks find", "food."),
            ("Bat helpers", "eat pests."),
            ("Watch soft—", "don't poke."),
            ("Lock, drop,", "fly."),
        ],
        "scenes": [
            "WIDE soft cave mouth sock puppet hang joke; boy and robot one-third; empty speech bubbles",
            "CLOSE soft bat feet lock on branch; characters half frame; empty speech bubbles",
            "MEDIUM hanging bat silhouette soft friendly; boy points; robot; half frame; empty speech bubbles",
            "ACTION soft bat dropping into gentle flight; characters edge; empty speech bubbles",
            "DIAGRAM-SOFT ground vs hang takeoff arrows; tiny figures; empty speech bubbles",
            "WIDE quiet roost under roof soft dusk; characters one-third; empty speech bubbles",
            "MEDIUM high perch safe above ground soft; boy and robot half frame; empty speech bubbles",
            "PLAYFUL night insects soft glow; bat helper distant; empty speech bubbles",
            "CLOSE soft echolocation wave dots; characters half frame; empty speech bubbles",
            "WIDE garden dusk bat helpers soft; characters one-third; empty speech bubbles",
            "CLOSE hands-off respect roost soft; robot nod; boy; half frame; empty speech bubbles",
            "ENDING boy and robot smile at hanging soft bat shape; one-third; empty speech bubbles",
        ],
    },
    "E-A24": {
        "title": "Why Do Zebras Have Stripes?",
        "folder": "Animals",
        "tag": "Zebras",
        "companion": "girl",
        "pages": [
            'Black and white flash by. "Why stripes?" asks Guangguang.',
            "Scientists study several helpful stripe ideas together.",
            "Stripes may confuse biting flies that chase solid shapes.",
            "Moving stripes can make it harder for flies to land.",
            "In a herd, stripes may blur who begins and who ends.",
            "That blur can make a hunter pause for a moment.",
            "Stripes also help zebras recognize family patterns.",
            "Each zebra's stripe map is a little different.",
            "Open grasslands are bright—patterns matter in motion.",
            "Zebras still need space, water, and calm watching.",
            "Never chase wild zebras; learn from books and zoos too.",
            "Stripes: fly tips, herd blur, and family ID—science keeps asking.",
        ],
        "bubbles": [
            ("Flash stripes!", "Why?"),
            ("Many helpful", "ideas."),
            ("Confuse", "biting flies."),
            ("Harder to", "land."),
            ("Herd blur", "edges."),
            ("Hunter may", "pause."),
            ("Family stripe", "maps."),
            ("Each pattern", "unique."),
            ("Grassland", "motion."),
            ("Space water", "calm."),
            ("Don't chase—", "learn soft."),
            ("Stripes still", "puzzle."),
        ],
        "scenes": [
            "WIDE soft savannah zebra herd stripes; girl and robot one-third; empty speech bubbles",
            "CLOSE stripe pattern soft detail; characters half frame; empty speech bubbles",
            "MEDIUM soft flies near solid vs stripe shapes; tiny diagram; empty speech bubbles",
            "ACTION zebra walk motion soft; girl points; robot; half frame; empty speech bubbles",
            "WIDE herd blur soft edges; characters one-third; empty speech bubbles",
            "PLAYFUL hunter pause soft distant silhouette not scary; empty speech bubbles",
            "CLOSE two zebra faces soft different stripes; characters half frame; empty speech bubbles",
            "DIAGRAM-SOFT unique stripe maps; tiny figures; empty speech bubbles",
            "WIDE bright grassland soft sun; characters one-third; empty speech bubbles",
            "MEDIUM calm watching with space soft; girl and robot half frame; empty speech bubbles",
            "CLOSE hands-off respect soft; robot nod; girl; half frame; empty speech bubbles",
            "ENDING girl and robot wave to soft zebra herd; one-third; empty speech bubbles",
        ],
    },
    "E-A25": {
        "title": "Why Do Kangaroos Hop?",
        "folder": "Animals",
        "tag": "Roos",
        "companion": "boy",
        "pages": [
            'Guangguang bounce-bounces. "Why hop?"',
            "Kangaroos have strong back legs and long springy feet.",
            "Hopping stores and returns energy like a soft pogo.",
            "Tendons stretch and snap back to help the next jump.",
            "At travel speed, hopping can save energy on open land.",
            "A heavy tail helps balance like a friendly third leg.",
            "Front paws are free for soft touches and little tasks.",
            "Joeys ride in a pouch while moms hop carefully.",
            "Different kangaroo sizes hop in their own ways.",
            "Give wild hoppers wide space—no chasing for fun.",
            "Watch with a grown-up and cheer from far away.",
            "Strong legs, spring tendons, balanced tail: hop science.",
        ],
        "bubbles": [
            ("Bounce!", "Why hop?"),
            ("Strong legs,", "big feet."),
            ("Energy like", "a pogo."),
            ("Tendons snap", "back."),
            ("Saves energy", "traveling."),
            ("Tail helps", "balance."),
            ("Paws free", "for tasks."),
            ("Joey rides", "in pouch."),
            ("Sizes hop", "differently."),
            ("Wide space—", "no chase."),
            ("Cheer from", "afar."),
            ("Legs spring", "tail."),
        ],
        "scenes": [
            "WIDE soft outback kangaroo hop; boy and robot one-third; empty speech bubbles",
            "CLOSE strong back legs soft; characters half frame; empty speech bubbles",
            "DIAGRAM-SOFT pogo energy arrows; tiny figures; empty speech bubbles",
            "ACTION soft hop mid-air; boy cheers; robot; half frame; empty speech bubbles",
            "MEDIUM travel hop path soft; characters one-third; empty speech bubbles",
            "CLOSE balancing tail soft; characters half frame; empty speech bubbles",
            "PLAYFUL front paws soft gesture; boy and robot half frame; empty speech bubbles",
            "MEDIUM mom with soft joey pouch; characters edge; empty speech bubbles",
            "WIDE different size hoppers soft; characters one-third; empty speech bubbles",
            "CLOSE hands-off wide space soft; robot nod; boy; half frame; empty speech bubbles",
            "MEDIUM watching with grown-up soft; boy and robot half frame; empty speech bubbles",
            "ENDING boy and robot hop-smile softly; one-third; empty speech bubbles",
        ],
    },
    "E-A26": {
        "title": "Why Do Dolphins Click and Whistle?",
        "folder": "Animals",
        "tag": "Dolphins",
        "companion": "girl",
        "pages": [
            'Clicks echo in Guangguang\'s pretend ocean. "Why so noisy?"',
            "Dolphins use sound to talk with friends nearby.",
            "Whistles can be like names that help them find each other.",
            "Clicks bounce off fish and return as soft echo maps.",
            "That echo sense is called echolocation—seeing with sound.",
            "Murky water is less of a problem when ears lead the way.",
            "Pods stay close by chatting across short distances.",
            "Playful leaps and spins often come with happy sounds.",
            "Listening quietly teaches more than chasing boats.",
            "Wild dolphins need calm seas and respectful space.",
            "Learn from aquariums and nature shows with a grown-up.",
            "Click, whistle, listen: ocean friends speak in sound.",
        ],
        "bubbles": [
            ("Clicks?", "Why noisy?"),
            ("Sound talks", "to friends."),
            ("Whistles like", "names."),
            ("Clicks bounce", "echo maps."),
            ("See with", "sound."),
            ("Murky water?", "Ears lead."),
            ("Pods chat", "nearby."),
            ("Play leaps,", "happy sounds."),
            ("Listen soft,", "don't chase."),
            ("Calm seas,", "space."),
            ("Learn with", "grown-ups."),
            ("Ocean friends", "speak."),
        ],
        "scenes": [
            "WIDE soft blue ocean dolphin leap; girl and robot one-third; empty speech bubbles",
            "MEDIUM two dolphins facing soft chat; characters half frame; empty speech bubbles",
            "CLOSE whistle name soft sound waves; characters half frame; empty speech bubbles",
            "DIAGRAM-SOFT click echo to fish arrows; tiny figures; empty speech bubbles",
            "PLAYFUL echolocation soft glow dots; girl points; robot; empty speech bubbles",
            "WIDE murky water soft clearer with sound idea; characters one-third; empty speech bubbles",
            "MEDIUM dolphin pod together soft; characters one-third; empty speech bubbles",
            "ACTION playful spin leap soft; characters edge; empty speech bubbles",
            "CLOSE quiet listening on boat soft; girl and robot half frame; empty speech bubbles",
            "WIDE calm sea respectful distance soft; characters one-third; empty speech bubbles",
            "MEDIUM learning with grown-up soft; girl and robot half frame; empty speech bubbles",
            "ENDING girl and robot wave to soft dolphin; one-third; empty speech bubbles",
        ],
    },
    "E-A27": {
        "title": "Why Do Fireflies Glow?",
        "folder": "Animals",
        "tag": "Glow",
        "companion": "girl",
        "pages": [
            'Tiny lights blink in the grass. "Why glow?"',
            "Fireflies make light with a gentle chemical reaction.",
            "The glow is cold light—little heat, lots of soft shine.",
            "Different blink patterns help fireflies find partners.",
            "Some patterns say hello; others say this spot is mine.",
            "Larvae may glow too as they grow toward flashy nights.",
            "Warm evenings after rain often bring more blinks.",
            "City lights can hide the tiny messages—dark helps.",
            "Cupping a firefly briefly then letting it go is kind.",
            "Never spray chemicals where soft blinkers live.",
            "Sit still and count flashes like a night science game.",
            "Chemistry, patterns, and patience: backyard star bugs.",
        ],
        "bubbles": [
            ("Tiny lights!", "Why glow?"),
            ("Chemical soft", "reaction."),
            ("Cold light,", "little heat."),
            ("Blink codes", "find friends."),
            ("Hello or", "my spot."),
            ("Larvae may", "glow too."),
            ("Warm damp", "evenings."),
            ("Dark helps", "messages."),
            ("Cup gently,", "let go."),
            ("No spray", "near them."),
            ("Count flashes", "science."),
            ("Backyard", "star bugs."),
        ],
        "scenes": [
            "WIDE soft dusk lawn firefly blinks; girl and robot one-third; empty speech bubbles",
            "CLOSE soft firefly glow abdomen; characters half frame; empty speech bubbles",
            "DIAGRAM-SOFT cold light vs hot bulb; tiny figures; empty speech bubbles",
            "MEDIUM blink pattern soft Morse-like dots; girl points; robot; empty speech bubbles",
            "PLAYFUL two fireflies signal soft; characters half frame; empty speech bubbles",
            "CLOSE soft larva glow friendly; characters half frame; empty speech bubbles",
            "WIDE warm evening after rain soft; characters one-third; empty speech bubbles",
            "MEDIUM city glow vs dark yard soft contrast; characters one-third; empty speech bubbles",
            "CLOSE gentle cupped hands release soft; girl and robot half frame; empty speech bubbles",
            "CLOSE no spray bottle soft X idea; robot shake; girl; half frame; empty speech bubbles",
            "WIDE sitting still counting flashes soft; characters one-third; empty speech bubbles",
            "ENDING girl and robot smile under soft blink sky; one-third; empty speech bubbles",
        ],
    },
    "E-A28": {
        "title": "Why Do Crabs Walk Sideways?",
        "folder": "Animals",
        "tag": "Crabs",
        "companion": "boy",
        "pages": [
            'A crab skitters left. "Why sideways?" Guangguang laughs.',
            "Many crab leg joints swing best in a side-to-side path.",
            "Side steps fit their wide flat bodies on sand and rock.",
            "Quick sideways dashes help them slip into tiny shelters.",
            "Some crabs can walk forward a little, but side is smoother.",
            "Claws up front are busy—legs behind do the travel work.",
            "Tide pools are busy cities of sideways traffic.",
            "Watch footprints in wet sand: little side-dash tracks.",
            "Give crabs room; pinching claws are for crab business.",
            "Never yank a crab from a rock hole—it needs that home.",
            "Tide pool rules: look, learn, leave creatures in place.",
            "Sideways isn't silly—it's joint design on the move.",
        ],
        "bubbles": [
            ("Sideways?", "Why?"),
            ("Joints swing", "sideways."),
            ("Wide body,", "side steps."),
            ("Dash into", "shelters."),
            ("Forward ok,", "side smoother."),
            ("Claws busy,", "legs travel."),
            ("Tide pool", "traffic."),
            ("Sand tracks", "side-dash."),
            ("Give room—", "claws work."),
            ("Don't yank", "homes."),
            ("Look learn", "leave."),
            ("Sideways =", "design."),
        ],
        "scenes": [
            "WIDE soft beach crab skitter; boy and robot one-third; empty speech bubbles",
            "CLOSE crab leg joints soft diagram; characters half frame; empty speech bubbles",
            "MEDIUM wide crab body side step soft; boy points; robot; empty speech bubbles",
            "ACTION crab dash into rock shelter soft; characters edge; empty speech bubbles",
            "DIAGRAM-SOFT forward vs side arrows; tiny figures; empty speech bubbles",
            "CLOSE claws up front soft not scary; characters half frame; empty speech bubbles",
            "WIDE tide pool busy soft; characters one-third; empty speech bubbles",
            "CLOSE wet sand side-dash tracks soft; boy and robot half frame; empty speech bubbles",
            "MEDIUM give space soft; robot arm out; boy; half frame; empty speech bubbles",
            "CLOSE rock hole home soft; hands-off; empty speech bubbles",
            "WIDE tide pool look-learn-leave soft; characters one-third; empty speech bubbles",
            "ENDING boy and robot side-step giggle soft; one-third; empty speech bubbles",
        ],
    },
    "E-A29": {
        "title": "Why Do Beavers Build Dams?",
        "folder": "Animals",
        "tag": "Beavers",
        "companion": "boy",
        "pages": [
            'Splash! Sticks pile up. "Why build dams?"',
            "Beavers cut trees and pack mud to slow a stream.",
            "The pond behind a dam makes a safer deep home zone.",
            "Deep water hides the entrance to their lodge.",
            "Stored branches underwater are winter snack shelves.",
            "Dam ponds also help other animals find wet habitat.",
            "Engineers with orange teeth reshaping the creek.",
            "Listen for soft slap warnings on the water surface.",
            "Leave beaver work alone—removing dams can harm homes.",
            "Watch from a trail with a grown-up and binoculars.",
            "Nature's builders teach patience and planning.",
            "Stick, mud, pond, lodge: beaver town planning.",
        ],
        "bubbles": [
            ("Stick pile!", "Why dams?"),
            ("Trees mud", "slow stream."),
            ("Pond makes", "safe home."),
            ("Deep water", "hides door."),
            ("Underwater", "snack shelf."),
            ("Other animals", "benefit."),
            ("Orange-tooth", "engineers."),
            ("Slap warns", "softly."),
            ("Leave dams", "alone."),
            ("Watch with", "grown-ups."),
            ("Builders teach", "plans."),
            ("Beaver town", "planning."),
        ],
        "scenes": [
            "WIDE soft creek beaver dam sticks; boy and robot one-third; empty speech bubbles",
            "MEDIUM beaver packing mud soft friendly; characters half frame; empty speech bubbles",
            "WIDE pond behind dam soft; characters one-third; empty speech bubbles",
            "CUTAWAY soft lodge underwater door; characters edge; empty speech bubbles",
            "CLOSE underwater branch snack shelf soft; characters half frame; empty speech bubbles",
            "WIDE birds frogs share pond soft; characters one-third; empty speech bubbles",
            "CLOSE friendly beaver teeth soft not scary; boy points; robot; empty speech bubbles",
            "ACTION soft tail slap on water; characters edge; empty speech bubbles",
            "CLOSE hands-off dam respect soft; robot nod; boy; half frame; empty speech bubbles",
            "MEDIUM trail watching with grown-up soft; boy and robot half frame; empty speech bubbles",
            "PLAYFUL blueprint sticks soft icons; characters half frame; empty speech bubbles",
            "ENDING boy and robot thumbs-up at soft dam; one-third; empty speech bubbles",
        ],
    },
    "E-A30": {
        "title": "Why Do Snakes Stick Out Their Tongues?",
        "folder": "Animals",
        "tag": "Tongues",
        "companion": "girl",
        "pages": [
            'A tongue flicks softly. "Why?" asks Guangguang kindly.',
            "Snakes smell with their tongues—not to be rude.",
            "Tiny scent bits stick to the tongue tip.",
            "The tongue carries smells to a special nose-inside sensor.",
            "That sensor helps map where prey or paths might be.",
            "Flicking gathers fresh air samples again and again.",
            "A forked tip can compare left and right scent clues.",
            "Snakes are shy neighbors; most want quiet space.",
            "Never grab or tease a snake—call a grown-up if worried.",
            "Learn safe local snakes from park rangers and books.",
            "Curiosity is good; touching wild snakes is not.",
            "Flick, sense, map: tongues that smell the world.",
        ],
        "bubbles": [
            ("Tongue flick?", "Why?"),
            ("Smelling,", "not rude."),
            ("Scent bits", "stick."),
            ("Sensor reads", "smells."),
            ("Maps prey", "and paths."),
            ("Flick again", "for samples."),
            ("Fork compares", "left right."),
            ("Shy neighbors", "need space."),
            ("Don't grab—", "tell grown-up."),
            ("Learn from", "rangers."),
            ("Curious ok,", "no touch."),
            ("Tongues that", "smell."),
        ],
        "scenes": [
            "WIDE soft sunny path friendly snake distant; girl and robot one-third; empty speech bubbles",
            "CLOSE soft tongue flick not scary; characters half frame; empty speech bubbles",
            "DIAGRAM-SOFT scent bits on tongue tip; tiny figures; empty speech bubbles",
            "MEDIUM soft sensor idea inside head diagram; girl points; robot; empty speech bubbles",
            "PLAYFUL scent map dots soft; characters half frame; empty speech bubbles",
            "ACTION gentle repeated flick soft; characters edge; empty speech bubbles",
            "CLOSE forked tongue soft compare L/R; characters half frame; empty speech bubbles",
            "WIDE give wide space soft; characters one-third; empty speech bubbles",
            "MEDIUM tell grown-up soft; girl and robot half frame; empty speech bubbles",
            "CLOSE park ranger book soft learning; characters half frame; empty speech bubbles",
            "CLOSE hands-off respect soft; robot nod; girl; half frame; empty speech bubbles",
            "ENDING girl and robot calm smile; soft snake silhouette far; one-third; empty speech bubbles",
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
            prompts.append(
                {
                    "id": sid,
                    "i": i,
                    "filename": f"c-{sid}-{i:02d}.jpg",
                    "description": prefix + "Scene: " + scene,
                    "refs": refs,
                    "companion": g,
                }
            )
        plan.append({"id": sid, "title": st["title"], "companion": g, "panels": panels})
        path = ROOT / "睡前有声稿" / "美国英文稿" / st["folder"] / f"{sid}.txt"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(st["title"] + "\n\n" + "\n\n".join(st["pages"]) + "\n", encoding="utf-8")
        print("wrote", path)

    plan_path = Path("/Users/song/qwen3-tts/comic_batch/comics_plan_en_backcatalog_w8.json")
    plan_path.write_text(json.dumps(plan, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("wrote", plan_path)

    raw_dir = Path("/Users/song/qwen3-tts/comic_batch/en_work/_raw_backcatalog_w8")
    raw_dir.mkdir(parents=True, exist_ok=True)
    prompts_path = Path("/Users/song/qwen3-tts/comic_batch/en_work/backcatalog_w8_prompts.json")
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
