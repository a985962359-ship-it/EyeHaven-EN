#!/usr/bin/env python3
"""Back-catalog wave 18: Space E-S14…E-S21 → 12-page books. Owner sleeping; no questions."""
from __future__ import annotations

import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PREFIX_BOY = (
    "Children's picture book comic panel, soft warm friendly space-science lighting, landscape 4:3. "
    "Cute round-headed white robot Guangguang with green trim, warm glowing chest lamp, small star on head, honest smile. "
    "Blonde boy about 6 years old with freckles wearing a blue T-rex hoodie with white sleeve stripes. "
    "Two large empty white oval speech bubbles with space for short kids text, blank inside, no letters. "
    "Soft friendly space science, gentle pastel stars, not scary. No text logos, consistent character design. "
    "Simple readable background, big clear shapes, shallow depth, soft edges, no clutter. "
)
PREFIX_GIRL = (
    "Children's picture book comic panel, soft warm friendly space-science lighting, landscape 4:3. "
    "Cute round-headed white robot Guangguang with green trim, warm glowing chest lamp, small star on head, honest smile. "
    "Gentle girl about 6–7 with soft sweater and kind smile. "
    "Two large empty white oval speech bubbles with space for short kids text, blank inside, no letters. "
    "Soft friendly space science, gentle pastel stars, not scary. No text logos, consistent character design. "
    "Simple readable background, big clear shapes, shallow depth, soft edges, no clutter. "
)

STORIES = {
    "E-S14": {
        "title": "What Is the Milky Way?",
        "folder": "Space",
        "tag": "Galaxy",
        "companion": "girl",
        "pages": [
            'A milky band crosses the dark sky. "Our galaxy?" asks Guangguang.',
            "The Milky Way is the huge star city we live inside.",
            "It holds billions of stars plus gas and dust.",
            "Many of those stars form a flat spiral shape.",
            "From Earth we often see it edge-on as a pale river of light.",
            "Other galaxies shine far beyond our own star city.",
            "Telescopes are the ships that help us explore farther.",
            "Dark skies away from city glow show the band best.",
            "We are not outside looking in—we are riding inside it.",
            "The Milky Way is home, not a splash of spilled milk.",
            "Ask a grown-up for a dark-sky night when you can.",
            "Star city spiral: Milky Way science.",
        ],
        "bubbles": [
            ("Milky band!", "Our galaxy?"),
            ("Huge star", "city."),
            ("Billions of", "stars."),
            ("Flat spiral", "shape."),
            ("Pale river", "of light."),
            ("Other galaxies", "beyond."),
            ("Telescopes are", "ships."),
            ("Dark skies", "show best."),
            ("We ride", "inside."),
            ("Home, not", "spilled milk."),
            ("Ask for dark", "sky night."),
            ("Milky Way", "science."),
        ],
        "scenes": [
            "WIDE soft dark sky milky band; girl and robot one-third; empty speech bubbles",
            "DIAGRAM-SOFT star city soft; tiny figures; empty speech bubbles",
            "MEDIUM billions stars soft; characters one-third; empty speech bubbles",
            "CLOSE spiral galaxy soft; girl points; robot; empty speech bubbles",
            "WIDE pale river light soft; characters one-third; empty speech bubbles",
            "PLAYFUL other galaxies soft; characters half frame; empty speech bubbles",
            "MEDIUM telescope soft; characters half frame; empty speech bubbles",
            "WIDE dark countryside soft; characters one-third; empty speech bubbles",
            "DIAGRAM-SOFT inside galaxy soft; tiny figures; empty speech bubbles",
            "PLAYFUL not spilled milk soft; characters half frame; empty speech bubbles",
            "MEDIUM ask grown-up soft; girl and robot half frame; empty speech bubbles",
            "ENDING girl and robot soft smile; one-third; empty speech bubbles",
        ],
    },
    "E-S15": {
        "title": "Why Do Astronauts Float in Space?",
        "folder": "Space",
        "tag": "Float",
        "companion": "boy",
        "pages": [
            'Guangguang pretends to float. "Zero gravity?"',
            "In orbit, astronauts and their ship fall around Earth together.",
            "Everything falls at about the same rate.",
            "Because of that, people feel weightless inside the craft.",
            "It is like continuous freefall without hitting the ground.",
            "Gravity did not vanish—Earth still pulls.",
            "The fast sideways speed keeps the fall curved into orbit.",
            "Floating hair and water blobs are famous orbit sights.",
            "Exercise helps astronauts keep muscles strong up there.",
            "Weightless feeling is freefall teamwork, not magic off-switch.",
            "Jump gently on a trampoline with a grown-up and notice floaty moments.",
            "Fall together, feel float: orbit science.",
        ],
        "bubbles": [
            ("Pretend float!", "Zero-g?"),
            ("Ship and crew", "fall together."),
            ("Same rate", "fall."),
            ("Feel weightless", "inside."),
            ("Freefall without", "hitting."),
            ("Gravity still", "pulls."),
            ("Sideways speed", "makes orbit."),
            ("Floating hair", "blobs."),
            ("Exercise keeps", "strong."),
            ("Not a magic", "off-switch."),
            ("Trampoline floaty", "moments."),
            ("Orbit float", "science."),
        ],
        "scenes": [
            "WIDE soft pretend float room; boy and robot one-third; empty speech bubbles",
            "DIAGRAM-SOFT orbit freefall soft; tiny figures; empty speech bubbles",
            "MEDIUM same-rate fall soft; characters one-third; empty speech bubbles",
            "CLOSE weightless inside soft; boy points; robot; empty speech bubbles",
            "PLAYFUL freefall soft; characters half frame; empty speech bubbles",
            "DIAGRAM-SOFT Earth still pulls soft; tiny figures; empty speech bubbles",
            "WIDE curved orbit path soft; characters one-third; empty speech bubbles",
            "CLOSE floating hair water soft; characters half frame; empty speech bubbles",
            "MEDIUM astronaut exercise soft; characters half frame; empty speech bubbles",
            "PLAYFUL not magic switch soft; characters half frame; empty speech bubbles",
            "WIDE trampoline soft; boy and robot one-third; empty speech bubbles",
            "ENDING boy and robot thumbs-up soft; one-third; empty speech bubbles",
        ],
    },
    "E-S16": {
        "title": "What Is a Black Hole?",
        "folder": "Space",
        "tag": "Hole",
        "companion": "boy",
        "pages": [
            'A dark circle on a diagram. "Scary?" asks Guangguang gently.',
            "A black hole is a place where gravity is extremely strong.",
            "Inside a boundary called the event horizon, light cannot escape.",
            "Some form when very massive stars collapse at the end of life.",
            "They are not hungry monsters roaming to eat everything nearby.",
            "Far away, their pull is just gravity—like any massive object.",
            "Scientists study them with math, telescopes, and careful pictures.",
            "A famous image showed a glowing ring around one shadow.",
            "Curiosity is fine; nightmares are not required.",
            "Black holes are extreme gravity neighborhoods in space.",
            "Look at soft diagrams with a grown-up, not spooky movies only.",
            "Strong gravity, no escape light: black-hole science kindly.",
        ],
        "bubbles": [
            ("Dark circle!", "Scary?"),
            ("Gravity very", "strong."),
            ("Light can't", "escape."),
            ("Massive stars", "can collapse."),
            ("Not hungry", "monsters."),
            ("Far away,", "just gravity."),
            ("Science studies", "carefully."),
            ("Glowing ring", "picture."),
            ("Curiosity, not", "nightmares."),
            ("Extreme gravity", "neighborhood."),
            ("Soft diagrams", "with help."),
            ("Black-hole", "science."),
        ],
        "scenes": [
            "WIDE soft gentle diagram dark circle; boy and robot one-third; empty speech bubbles",
            "DIAGRAM-SOFT strong gravity soft not scary; tiny figures; empty speech bubbles",
            "CLOSE event horizon soft; characters half frame; empty speech bubbles",
            "MEDIUM star collapse soft gentle; boy points; robot; empty speech bubbles",
            "PLAYFUL not a monster soft; characters half frame; empty speech bubbles",
            "WIDE far-away gravity soft; characters one-third; empty speech bubbles",
            "MEDIUM telescope science soft; characters half frame; empty speech bubbles",
            "CLOSE glowing ring image soft; characters half frame; empty speech bubbles",
            "PLAYFUL calm curiosity soft; characters half frame; empty speech bubbles",
            "DIAGRAM-SOFT gravity neighborhood soft; tiny figures; empty speech bubbles",
            "MEDIUM grown-up diagram soft; boy and robot half frame; empty speech bubbles",
            "ENDING boy and robot gentle nod soft; one-third; empty speech bubbles",
        ],
    },
    "E-S17": {
        "title": "Why Is Venus So Hot?",
        "folder": "Space",
        "tag": "Venus",
        "companion": "girl",
        "pages": [
            'A bright morning “star.” "Hotter than Mercury?" asks Guangguang.',
            "Venus wears a thick blanket of carbon-dioxide air.",
            "That atmosphere traps heat like a runaway greenhouse.",
            "Surface temperatures climb oven-hot.",
            "Mercury is closer to the Sun, yet Venus can be hotter.",
            "The thick air, not just distance, drives the heat story.",
            "Clouds hide the surface from ordinary eyesight.",
            "Probes and telescopes study Venus from safer distances.",
            "Earth’s air is different—our greenhouse is milder with care.",
            "Venus heat is a thick-air trap more than a near-Sun prize.",
            "Compare a jacket greenhouse to a thin T-shirt with a grown-up.",
            "Thick air trap: Venus-hot science.",
        ],
        "bubbles": [
            ("Bright Venus!", "Hotter?"),
            ("Thick CO₂", "blanket."),
            ("Traps heat", "hard."),
            ("Oven-hot", "surface."),
            ("Closer Mercury", "can be cooler."),
            ("Air drives", "the heat."),
            ("Clouds hide", "surface."),
            ("Probes study", "safely."),
            ("Earth air", "differs."),
            ("Thick-air trap", "story."),
            ("Jacket vs", "T-shirt."),
            ("Venus-hot", "science."),
        ],
        "scenes": [
            "WIDE soft dawn bright Venus; girl and robot one-third; empty speech bubbles",
            "DIAGRAM-SOFT thick atmosphere soft; tiny figures; empty speech bubbles",
            "MEDIUM heat trap greenhouse soft; characters one-third; empty speech bubbles",
            "CLOSE oven-hot idea soft; girl points; robot; empty speech bubbles",
            "PLAYFUL Mercury vs Venus soft; characters half frame; empty speech bubbles",
            "DIAGRAM-SOFT air not only distance soft; tiny figures; empty speech bubbles",
            "WIDE cloudy Venus soft; characters one-third; empty speech bubbles",
            "MEDIUM probe telescope soft; characters half frame; empty speech bubbles",
            "CLOSE Earth milder air soft; characters half frame; empty speech bubbles",
            "PLAYFUL thick-air trap soft; characters half frame; empty speech bubbles",
            "MEDIUM jacket compare soft; girl and robot half frame; empty speech bubbles",
            "ENDING girl and robot soft smile; one-third; empty speech bubbles",
        ],
    },
    "E-S18": {
        "title": "What Are Saturn’s Rings Made Of?",
        "folder": "Space",
        "tag": "Rings",
        "companion": "girl",
        "pages": [
            'Sparkly rings around Saturn. "Ice?" asks Guangguang.',
            "Saturn’s rings are countless chunks of ice and rock.",
            "Some pieces are tiny; some are boulder-sized.",
            "They orbit in thin sheets like glittering traffic lanes.",
            "Moonlets and gravity sculpt gaps and waves in the rings.",
            "From far away the rings look solid and smooth.",
            "Up close they are a busy icy rubble highway.",
            "Spacecraft have flown near to photograph the details.",
            "Other giant planets have rings too, often fainter.",
            "Rings are icy rubble highways, not magic hoops.",
            "Spin a hula hoop gently and imagine many tiny moons inside.",
            "Ice, rock, orbit sheets: ring science.",
        ],
        "bubbles": [
            ("Sparkly rings!", "Ice?"),
            ("Ice and rock", "chunks."),
            ("Tiny to", "boulder."),
            ("Thin sheet", "lanes."),
            ("Gaps and", "waves."),
            ("Far away look", "solid."),
            ("Up close,", "rubble."),
            ("Crafts take", "photos."),
            ("Other giants", "have rings."),
            ("Not magic", "hoops."),
            ("Hula hoop", "imagine."),
            ("Ring", "science."),
        ],
        "scenes": [
            "WIDE soft Saturn sparkly rings; girl and robot one-third; empty speech bubbles",
            "DIAGRAM-SOFT ice rock chunks soft; tiny figures; empty speech bubbles",
            "CLOSE tiny and boulder soft; characters half frame; empty speech bubbles",
            "MEDIUM thin sheet lanes soft; girl points; robot; empty speech bubbles",
            "PLAYFUL gaps waves soft; characters half frame; empty speech bubbles",
            "WIDE far solid look soft; characters one-third; empty speech bubbles",
            "CLOSE icy rubble soft; characters half frame; empty speech bubbles",
            "MEDIUM spacecraft photo soft; characters half frame; empty speech bubbles",
            "WIDE other planet rings soft; characters one-third; empty speech bubbles",
            "PLAYFUL not magic hoops soft; characters half frame; empty speech bubbles",
            "MEDIUM hula hoop soft; girl and robot half frame; empty speech bubbles",
            "ENDING girl and robot soft smile; one-third; empty speech bubbles",
        ],
    },
    "E-S19": {
        "title": "Why Do We Have Seasons?",
        "folder": "Space",
        "tag": "Season",
        "companion": "boy",
        "pages": [
            'Summer sweat, winter coats. "Why seasons?" asks Guangguang.',
            "Earth’s axis is tilted as we travel around the Sun.",
            "For part of the year one hemisphere leans toward sunlight.",
            "That leaning side gets warmer months.",
            "The other hemisphere leans away and gets cooler months.",
            "Distance to the Sun changes a little, but tilt drives seasons.",
            "Near the equator, season changes can feel milder.",
            "Near the poles, summer light and winter dark get extreme.",
            "Calendars and festivals often celebrate these shifts.",
            "Seasons are a tilt dance, not Earth hopping closer then farther only.",
            "Shine a flashlight on a tilted globe with a grown-up.",
            "Tilted axis orbit: season science.",
        ],
        "bubbles": [
            ("Sweat or coat!", "Why seasons?"),
            ("Earth axis", "tilts."),
            ("One side leans", "toward Sun."),
            ("Leaning side", "warmer."),
            ("Other side", "cooler."),
            ("Tilt drives", "seasons."),
            ("Equator milder", "shifts."),
            ("Poles more", "extreme."),
            ("Festivals mark", "changes."),
            ("Tilt dance,", "not just distance."),
            ("Flashlight globe", "demo."),
            ("Season", "science."),
        ],
        "scenes": [
            "WIDE soft summer winter split; boy and robot one-third; empty speech bubbles",
            "DIAGRAM-SOFT tilted Earth soft; tiny figures; empty speech bubbles",
            "MEDIUM lean toward Sun soft; characters one-third; empty speech bubbles",
            "CLOSE warmer months soft; boy points; robot; empty speech bubbles",
            "MEDIUM lean away cool soft; characters half frame; empty speech bubbles",
            "DIAGRAM-SOFT tilt not only distance soft; tiny figures; empty speech bubbles",
            "WIDE equator mild soft; characters one-third; empty speech bubbles",
            "WIDE polar light dark soft; characters one-third; empty speech bubbles",
            "PLAYFUL festival soft; characters half frame; empty speech bubbles",
            "PLAYFUL tilt dance soft; characters half frame; empty speech bubbles",
            "MEDIUM flashlight globe soft; boy and robot half frame; empty speech bubbles",
            "ENDING boy and robot thumbs-up soft; one-third; empty speech bubbles",
        ],
    },
    "E-S20": {
        "title": "What Is the International Space Station?",
        "folder": "Space",
        "tag": "ISS",
        "companion": "boy",
        "pages": [
            'A metal butterfly in orbit. "ISS?" asks Guangguang.',
            "The International Space Station is a flying science lab.",
            "Astronauts from many countries live and work there.",
            "It circles Earth about once every ninety minutes.",
            "They study science in microgravity and test life in space.",
            "Cargo ships bring food, tools, and experiments.",
            "Solar panels gather sunlight to power the station.",
            "Crews exercise so bones and muscles stay healthier.",
            "Sometimes you can spot it as a bright moving dot at night.",
            "The ISS is a shared home lab above the clouds.",
            "Track a pass time online with a grown-up and wave hello.",
            "Orbit lab teamwork: ISS science.",
        ],
        "bubbles": [
            ("Metal butterfly!", "ISS?"),
            ("Flying science", "lab."),
            ("Many countries", "crew."),
            ("Circles every", "90 minutes."),
            ("Microgravity", "science."),
            ("Cargo brings", "supplies."),
            ("Solar panels", "power."),
            ("Exercise keeps", "strong."),
            ("Bright moving", "dot."),
            ("Shared home", "lab."),
            ("Track a pass", "together."),
            ("ISS", "science."),
        ],
        "scenes": [
            "WIDE soft ISS in orbit; boy and robot one-third; empty speech bubbles",
            "MEDIUM science lab modules soft; characters one-third; empty speech bubbles",
            "CLOSE international crew soft; boy points; robot; empty speech bubbles",
            "DIAGRAM-SOFT 90-minute orbit soft; tiny figures; empty speech bubbles",
            "PLAYFUL microgravity work soft; characters half frame; empty speech bubbles",
            "WIDE cargo ship dock soft; characters one-third; empty speech bubbles",
            "CLOSE solar panels soft; characters half frame; empty speech bubbles",
            "MEDIUM exercise soft; characters half frame; empty speech bubbles",
            "WIDE night sky bright dot soft; characters one-third; empty speech bubbles",
            "PLAYFUL shared home lab soft; characters half frame; empty speech bubbles",
            "MEDIUM track pass soft; boy and robot half frame; empty speech bubbles",
            "ENDING boy and robot thumbs-up soft; one-third; empty speech bubbles",
        ],
    },
    "E-S21": {
        "title": "Why Do Meteors Streak?",
        "folder": "Space",
        "tag": "Meteor",
        "companion": "girl",
        "pages": [
            'A quick scratch of light. "Shooting star?" asks Guangguang.',
            "A meteor is a space rock racing through Earth’s air.",
            "Friction heats it until it glows as a streak.",
            "Most meteors are tiny and burn up high above.",
            "If a piece survives and lands, it is called a meteorite.",
            "Meteor showers happen when Earth crosses dusty trails.",
            "Wishes are optional—the physics happens either way.",
            "Never confuse meteors with airplanes’ steady lights.",
            "Safe watching means eyes on the sky, feet on the ground.",
            "Meteor streaks are air-friction fireworks from tiny rocks.",
            "Lie on a blanket with a grown-up on a clear night.",
            "Glow, streak, maybe land: meteor science.",
        ],
        "bubbles": [
            ("Quick scratch!", "Shooting star?"),
            ("Space rock in", "air."),
            ("Friction makes", "glow."),
            ("Most burn up", "high."),
            ("Landed piece:", "meteorite."),
            ("Showers from", "dust trails."),
            ("Wish optional;", "physics sure."),
            ("Not airplane", "lights."),
            ("Eyes up, feet", "down."),
            ("Air-friction", "fireworks."),
            ("Blanket night", "watch."),
            ("Meteor", "science."),
        ],
        "scenes": [
            "WIDE soft night meteor streak; girl and robot one-third; empty speech bubbles",
            "DIAGRAM-SOFT rock entering air soft; tiny figures; empty speech bubbles",
            "CLOSE friction glow soft; characters half frame; empty speech bubbles",
            "MEDIUM burn up high soft; girl points; robot; empty speech bubbles",
            "PLAYFUL meteorite land soft; characters half frame; empty speech bubbles",
            "WIDE meteor shower soft; characters one-third; empty speech bubbles",
            "CLOSE wish optional soft; characters half frame; empty speech bubbles",
            "DIAGRAM-SOFT not airplane soft; tiny figures; empty speech bubbles",
            "MEDIUM safe watching soft; characters half frame; empty speech bubbles",
            "PLAYFUL air fireworks soft; characters half frame; empty speech bubbles",
            "WIDE blanket night soft; girl and robot one-third; empty speech bubbles",
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
    ref_dir = ROOT / ".comic_refs" / "w18_by_story"
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

    Path("/Users/song/qwen3-tts/comic_batch/comics_plan_en_backcatalog_w18.json").write_text(
        json.dumps(plan, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    Path("/Users/song/qwen3-tts/comic_batch/en_work/_raw_backcatalog_w18").mkdir(parents=True, exist_ok=True)
    Path("/Users/song/qwen3-tts/comic_batch/en_work/backcatalog_w18_prompts.json").write_text(
        json.dumps(prompts, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    bubbles_path = ROOT / "EyeHaven" / "ComicBubbleWords.en.json"
    bubbles = json.loads(bubbles_path.read_text(encoding="utf-8"))
    for sid, st in STORIES.items():
        bubbles[sid] = [{"i": i, "left": L, "right": R} for i, (L, R) in enumerate(st["bubbles"], 1)]
    bubbles_path.write_text(json.dumps(bubbles, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("wave18 done", len(STORIES), "prompts", len(prompts))


if __name__ == "__main__":
    main()
