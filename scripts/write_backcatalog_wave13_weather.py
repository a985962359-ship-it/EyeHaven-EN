#!/usr/bin/env python3
"""Back-catalog wave 13: Weather Why E-W15…E-W22 → 12-page books. Owner sleeping; no questions."""
from __future__ import annotations

import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PREFIX_BOY = (
    "Children's picture book comic panel, soft warm friendly weather-science lighting, landscape 4:3. "
    "Cute round-headed white robot Guangguang with green trim, warm glowing chest lamp, small star on head, honest smile. "
    "Blonde boy about 6 years old with freckles wearing a blue T-rex hoodie with white sleeve stripes. "
    "Two large empty white oval speech bubbles with space for short kids text, blank inside, no letters. "
    "Soft friendly weather science, gentle pastel sky, not scary. No text logos, consistent character design. "
    "Simple readable background, big clear shapes, shallow depth, soft edges, no clutter. "
)
PREFIX_GIRL = (
    "Children's picture book comic panel, soft warm friendly weather-science lighting, landscape 4:3. "
    "Cute round-headed white robot Guangguang with green trim, warm glowing chest lamp, small star on head, honest smile. "
    "Gentle girl about 6–7 with soft sweater and kind smile. "
    "Two large empty white oval speech bubbles with space for short kids text, blank inside, no letters. "
    "Soft friendly weather science, gentle pastel sky, not scary. No text logos, consistent character design. "
    "Simple readable background, big clear shapes, shallow depth, soft edges, no clutter. "
)

STORIES = {
    "E-W15": {
        "title": "Why Do Puddles Disappear?",
        "folder": "Weather",
        "tag": "Puddle",
        "companion": "boy",
        "pages": [
            'Morning puddle, noon dry. "Where did it go?" asks Guangguang.',
            "Sun and warm air give water energy to turn into invisible vapor.",
            "That jump from liquid to vapor is called evaporation.",
            "Wind brushes the surface and whisks vapor away faster.",
            "The puddle did not fall into another dimension—it joined the air.",
            "Bigger puddles hold more water, so they last longer.",
            "Shade and cool air slow the drying, so some spots stay wet.",
            "Tiny leftover rings of dirt show where the edge used to be.",
            "The same water may later make a cloud, then rain again.",
            "So disappearing puddles are slow-motion steam without a teapot whistle.",
            "Watch one puddle with a grown-up after rain—science in the sidewalk.",
            "Sun, air, wind: puddle vanishing science.",
        ],
        "bubbles": [
            ("Puddle gone!", "Where?"),
            ("Sun warms", "the water."),
            ("Liquid turns", "to vapor."),
            ("Wind whisks", "it away."),
            ("Joined the", "air."),
            ("Bigger lasts", "longer."),
            ("Shade slows", "drying."),
            ("Dirt rings", "mark edges."),
            ("May rain", "again later."),
            ("Slow steam,", "no whistle."),
            ("Watch with", "grown-up."),
            ("Puddle vanish", "science."),
        ],
        "scenes": [
            "WIDE soft sidewalk morning puddle; boy and robot one-third; empty speech bubbles",
            "MEDIUM sun warming puddle soft; characters one-third; empty speech bubbles",
            "DIAGRAM-SOFT liquid to vapor soft cartoon; tiny figures; empty speech bubbles",
            "PLAYFUL wind brushing puddle soft; characters half frame; empty speech bubbles",
            "WIDE vapor joining air soft; boy points; robot; empty speech bubbles",
            "MEDIUM big vs small puddle soft; characters one-third; empty speech bubbles",
            "CLOSE shade cool puddle soft; characters half frame; empty speech bubbles",
            "CLOSE dirt ring leftover soft; characters half frame; empty speech bubbles",
            "WIDE cloud then rain cycle soft; characters one-third; empty speech bubbles",
            "PLAYFUL teapot joke soft no whistle; characters half frame; empty speech bubbles",
            "MEDIUM boy and robot watch puddle soft; half frame; empty speech bubbles",
            "ENDING boy and robot thumbs-up soft; one-third; empty speech bubbles",
        ],
    },
    "E-W16": {
        "title": "What Is Humidity?",
        "folder": "Weather",
        "tag": "Humidity",
        "companion": "girl",
        "pages": [
            'Sticky air hugs everyone. "What is humidity?" asks Guangguang.',
            "Humidity measures how much water vapor the air is holding.",
            "High humidity means lots of invisible water already in the air.",
            "Then sweat evaporates slowly, so skin feels muggy and clingy.",
            "Low humidity means drier air that can chap lips and static hair.",
            "Weather apps often show a humidity percent for the day.",
            "A fan helps by moving moist still air across your skin.",
            "Bathrooms fog up fast because warm water adds vapor indoors.",
            "Plants and wet clothes also release water into room air.",
            "Feeling sticky is not a failure—it is vapor chemistry on you.",
            "Dress light, sip water, and rest in shade when air is heavy.",
            "Invisible water load: humidity science.",
        ],
        "bubbles": [
            ("Sticky air!", "Humidity?"),
            ("Vapor the", "air holds."),
            ("High means", "lots of water."),
            ("Sweat dries", "slowly."),
            ("Low air", "feels dry."),
            ("Apps show", "percent."),
            ("Fan moves", "moist air."),
            ("Bath steam", "adds vapor."),
            ("Plants add", "water too."),
            ("Sticky is", "chemistry."),
            ("Light clothes,", "sip water."),
            ("Humidity", "science."),
        ],
        "scenes": [
            "WIDE soft muggy porch; girl and robot one-third; empty speech bubbles",
            "DIAGRAM-SOFT vapor dots in air soft; tiny figures; empty speech bubbles",
            "MEDIUM high humidity cling soft; characters one-third; empty speech bubbles",
            "CLOSE sweaty skin muggy soft not gross; characters half frame; empty speech bubbles",
            "PLAYFUL static hair dry day soft; characters half frame; empty speech bubbles",
            "CLOSE weather app humidity soft; girl points; robot; empty speech bubbles",
            "MEDIUM fan breeze soft; characters half frame; empty speech bubbles",
            "WIDE steamy bathroom soft gentle; characters one-third; empty speech bubbles",
            "MEDIUM plants wet laundry soft; characters one-third; empty speech bubbles",
            "PLAYFUL vapor chemistry hug soft; characters half frame; empty speech bubbles",
            "WIDE shade rest water soft; girl and robot one-third; empty speech bubbles",
            "ENDING girl and robot soft smile; one-third; empty speech bubbles",
        ],
    },
    "E-W17": {
        "title": "Why Do Weather Maps Use Colors?",
        "folder": "Weather",
        "tag": "Map",
        "companion": "boy",
        "pages": [
            'A blob of green and red. "What does that mean?" asks Guangguang.',
            "Weather maps paint data so your eyes grasp patterns fast.",
            "Colors can show rain strength, temperature bands, or radar echoes.",
            "On many rain maps, green is lighter rain and yellow or red means heavier.",
            "Every map has a key—read it like a legend for the colors.",
            "Forecasts guess tomorrow; your window confirms today.",
            "Dress for the color story: coat for cold blues, rain gear for wet greens.",
            "Satellites and radars feed the colorful pictures scientists draw.",
            "Colors are shortcuts, not magic paint that makes weather.",
            "Ask a grown-up to decode a map before a big trip.",
            "Busy numbers become a picture kids can scan in seconds.",
            "Color shortcuts for sky data: map science.",
        ],
        "bubbles": [
            ("Green red", "blob?"),
            ("Colors show", "patterns."),
            ("Rain heat", "or radar."),
            ("Green light,", "red heavy."),
            ("Read the", "map key."),
            ("Forecast vs", "window."),
            ("Dress for", "colors."),
            ("Radar feeds", "pictures."),
            ("Not magic", "paint."),
            ("Ask grown-up", "to decode."),
            ("Numbers become", "pictures."),
            ("Map color", "science."),
        ],
        "scenes": [
            "WIDE soft living room weather map on tablet; boy and robot one-third; empty speech bubbles",
            "MEDIUM colorful weather map soft; characters one-third; empty speech bubbles",
            "DIAGRAM-SOFT rain temp radar icons soft; tiny figures; empty speech bubbles",
            "CLOSE green to red rain key soft; boy points; robot; empty speech bubbles",
            "CLOSE map legend key soft; characters half frame; empty speech bubbles",
            "PLAYFUL window vs forecast soft; characters half frame; empty speech bubbles",
            "WIDE coat and rain gear soft; characters one-third; empty speech bubbles",
            "MEDIUM satellite radar soft cartoon; characters edge; empty speech bubbles",
            "PLAYFUL not magic paint soft; characters half frame; empty speech bubbles",
            "MEDIUM ask grown-up soft; boy and robot half frame; empty speech bubbles",
            "WIDE kids scanning map soft; characters one-third; empty speech bubbles",
            "ENDING boy and robot thumbs-up soft; one-third; empty speech bubbles",
        ],
    },
    "E-W18": {
        "title": "Why Does Dew Form on Grass?",
        "folder": "Weather",
        "tag": "Dew",
        "companion": "girl",
        "pages": [
            'Morning sparkles on grass. "Did it rain overnight?" asks Guangguang.',
            "Clear nights let the ground cool after the sun goes away.",
            "Air near the blades can cool until it cannot hold all its vapor.",
            "Extra vapor becomes tiny droplets—dew—on leaves and grass.",
            "Dew is condensation jewelry, not always rain from clouds.",
            "Shoes get wet on purpose when you walk the sparkling lawn.",
            "As the day warms, dew evaporates back into the air.",
            "Frost is related but frozen—ice crystals instead of liquid beads.",
            "Garden spiders’ webs look jeweled when dew clings to silk.",
            "Farmers once watched dew as a clue about cool clear nights.",
            "Step gently and notice how cold grass can make water appear.",
            "Cool ground, clingy vapor: dew science.",
        ],
        "bubbles": [
            ("Sparkles!", "Overnight rain?"),
            ("Ground cools", "at night."),
            ("Air near grass", "gets cold."),
            ("Vapor becomes", "droplets."),
            ("Dew, not", "always rain."),
            ("Shoes get", "wet."),
            ("Day warms,", "dew goes."),
            ("Frost is", "frozen kin."),
            ("Webs look", "jeweled."),
            ("Cool nights", "clue."),
            ("Notice cold", "grass water."),
            ("Dew science", "sparkle."),
        ],
        "scenes": [
            "WIDE soft dawn lawn sparkles; girl and robot one-third; empty speech bubbles",
            "MEDIUM clear night cooling ground soft; characters one-third; empty speech bubbles",
            "DIAGRAM-SOFT cool air near blades soft; tiny figures; empty speech bubbles",
            "CLOSE dew droplets on grass soft; girl points; robot; empty speech bubbles",
            "PLAYFUL dew vs rain cloud soft; characters half frame; empty speech bubbles",
            "CLOSE wet shoes on lawn soft; characters half frame; empty speech bubbles",
            "WIDE sun warming dew away soft; characters one-third; empty speech bubbles",
            "DIAGRAM-SOFT frost crystals soft gentle; tiny figures; empty speech bubbles",
            "CLOSE spider web dew jewels soft friendly; characters half frame; empty speech bubbles",
            "MEDIUM farm dawn soft; characters one-third; empty speech bubbles",
            "WIDE girl and robot step gently soft; one-third; empty speech bubbles",
            "ENDING girl and robot soft smile; one-third; empty speech bubbles",
        ],
    },
    "E-W19": {
        "title": "What Causes a Drought?",
        "folder": "Weather",
        "tag": "Drought",
        "companion": "boy",
        "pages": [
            'Cracked earth under a bright sky. "Why so little rain?" asks Guangguang.',
            "A drought is a long stretch with less water than plants and people need.",
            "Stubborn weather patterns can park dry air over a region for weeks.",
            "Rivers, soil, and reservoirs slowly shrink when rain stays away.",
            "People’s water use also matters when supplies run thin.",
            "Conservation—short showers, fixing leaks—helps communities cope.",
            "Lawns can wait; drinking water and farms matter more.",
            "Follow local water rules posted by grown-ups and cities.",
            "Drought is a water budget gone thin for too long.",
            "Scientists watch rainfall totals and soil moisture for warnings.",
            "Hope returns when storms finally refill the land’s savings.",
            "Thin water budget: drought science kindly.",
        ],
        "bubbles": [
            ("Cracked earth!", "No rain?"),
            ("Long stretch", "too dry."),
            ("Dry air", "parks here."),
            ("Rivers and", "soil shrink."),
            ("Use matters", "too."),
            ("Conserve and", "fix leaks."),
            ("Lawns wait;", "drink first."),
            ("Follow water", "rules."),
            ("Budget gone", "thin."),
            ("Scientists", "watch totals."),
            ("Storms refill", "savings."),
            ("Drought science", "kindly."),
        ],
        "scenes": [
            "WIDE soft dry field cracked earth gentle not scary; boy and robot one-third; empty speech bubbles",
            "DIAGRAM-SOFT drought calendar dry soft; tiny figures; empty speech bubbles",
            "MEDIUM parked dry air soft; characters one-third; empty speech bubbles",
            "WIDE shrinking river reservoir soft; characters one-third; empty speech bubbles",
            "CLOSE faucet use soft; boy points; robot; empty speech bubbles",
            "PLAYFUL short shower fix leak soft; characters half frame; empty speech bubbles",
            "MEDIUM brown lawn vs drinking glass soft; characters half frame; empty speech bubbles",
            "CLOSE water rules sign soft; characters half frame; empty speech bubbles",
            "DIAGRAM-SOFT thin water budget soft; tiny figures; empty speech bubbles",
            "MEDIUM scientist chart soft; characters half frame; empty speech bubbles",
            "WIDE hopeful rain clouds soft; boy and robot one-third; empty speech bubbles",
            "ENDING boy and robot gentle nod soft; one-third; empty speech bubbles",
        ],
    },
    "E-W20": {
        "title": "Why Do Weather Balloons Go Up?",
        "folder": "Weather",
        "tag": "Balloon",
        "companion": "boy",
        "pages": [
            'A giant balloon lifts a little box. "Why send it up?" asks Guangguang.',
            "Weather balloons carry sensors through layers of sky.",
            "As they rise, gadgets measure temperature, humidity, and pressure.",
            "Radios send those numbers down so forecasts can improve.",
            "High up the balloon stretches and finally bursts safely by design.",
            "A parachute helps the instrument package float back down.",
            "They are science messengers, not party balloons for cake.",
            "Twice a day in many places, teams launch them for global data.",
            "Planes and models use that sky notebook to steer safer flights.",
            "Watch a launch with a grown-up if a weather station invites kids.",
            "Each flight is a flying notebook for the atmosphere’s layers.",
            "Rise, measure, radio home: balloon science.",
        ],
        "bubbles": [
            ("Big balloon!", "Why up?"),
            ("Carries sky", "sensors."),
            ("Measures temp", "and more."),
            ("Radios send", "numbers down."),
            ("Bursts high", "on purpose."),
            ("Parachute", "brings box."),
            ("Science, not", "party."),
            ("Teams launch", "often."),
            ("Helps planes", "and models."),
            ("Watch with", "grown-up."),
            ("Flying sky", "notebook."),
            ("Balloon", "science."),
        ],
        "scenes": [
            "WIDE soft launch field giant weather balloon; boy and robot one-third; empty speech bubbles",
            "MEDIUM sensors under balloon soft; characters one-third; empty speech bubbles",
            "DIAGRAM-SOFT rising through sky layers soft; tiny figures; empty speech bubbles",
            "CLOSE radio waves down soft; boy points; robot; empty speech bubbles",
            "PLAYFUL balloon stretch high soft; characters edge; empty speech bubbles",
            "MEDIUM parachute float down soft; characters half frame; empty speech bubbles",
            "PLAYFUL party balloon vs science soft; characters half frame; empty speech bubbles",
            "WIDE team launch morning soft; characters one-third; empty speech bubbles",
            "MEDIUM plane and forecast soft; characters one-third; empty speech bubbles",
            "CLOSE kids watching launch soft; boy and robot half frame; empty speech bubbles",
            "WIDE flying notebook idea soft; characters one-third; empty speech bubbles",
            "ENDING boy and robot thumbs-up soft; one-third; empty speech bubbles",
        ],
    },
    "E-W21": {
        "title": "Why Is Snow Quiet?",
        "folder": "Weather",
        "tag": "Snow",
        "companion": "girl",
        "pages": [
            'Soft footsteps hush the street. "Why so quiet?" asks Guangguang.',
            "Fresh snow is packed with tiny air pockets between flakes.",
            "Those pockets soak up sound waves like gentle acoustic foam.",
            "City noise sounds muffled after a thick new blizzard.",
            "When snow melts or packs hard, the hush fades away.",
            "Ice alone is louder under boots than fluffy powder.",
            "Enjoy the quiet walk—then shovel with a grown-up’s plan.",
            "Animals leave soft tracks that barely crackle in deep powder.",
            "Wind can still whistle above, even when ground snow muffles.",
            "Quiet snow is physics you can feel in your ears.",
            "Bundle up, listen closely, and thank the fluffy blanket.",
            "Air pockets hush the world: snow quiet science.",
        ],
        "bubbles": [
            ("Soft hush!", "Why quiet?"),
            ("Air pockets", "in snow."),
            ("Pockets soak", "sound."),
            ("Cities sound", "muffled."),
            ("Hard pack", "hush fades."),
            ("Ice louder", "than powder."),
            ("Shovel with", "grown-up."),
            ("Soft animal", "tracks."),
            ("Wind may", "still whistle."),
            ("Quiet is", "physics."),
            ("Listen to", "the blanket."),
            ("Snow quiet", "science."),
        ],
        "scenes": [
            "WIDE soft snowy street hush; girl and robot one-third; empty speech bubbles",
            "DIAGRAM-SOFT snowflake air pockets soft; tiny figures; empty speech bubbles",
            "CLOSE sound waves soaking soft; characters half frame; empty speech bubbles",
            "MEDIUM muffled city after snow soft; characters one-third; empty speech bubbles",
            "PLAYFUL packed snow vs fluff soft; characters half frame; empty speech bubbles",
            "CLOSE boots on ice vs powder soft; girl points; robot; empty speech bubbles",
            "WIDE shovel with grown-up soft; characters one-third; empty speech bubbles",
            "MEDIUM animal tracks soft; characters half frame; empty speech bubbles",
            "WIDE wind above quiet ground soft; characters one-third; empty speech bubbles",
            "PLAYFUL ear listening soft; characters half frame; empty speech bubbles",
            "MEDIUM bundled walk soft; girl and robot half frame; empty speech bubbles",
            "ENDING girl and robot soft smile; one-third; empty speech bubbles",
        ],
    },
    "E-W22": {
        "title": "What Is the Jet Stream?",
        "folder": "Weather",
        "tag": "Jet",
        "companion": "boy",
        "pages": [
            'A fast ribbon on the forecast map. "Jet stream?" asks Guangguang.',
            "Jet streams are swift rivers of wind high up in the sky.",
            "They steer weather systems like invisible sky freeways.",
            "Planes sometimes ride a jet stream to save time on long trips.",
            "The ribbon wiggles and shifts as seasons change.",
            "Cold and warm air meeting helps build these fast currents.",
            "They are not airplane-only highways—storms ride them too.",
            "Forecasters watch the jet stream to guess where rain may go.",
            "You cannot see it from the ground, but maps sketch its path.",
            "High and fast, it still follows physics, not magic rails.",
            "Next flight delay or early arrival may thank that wind river.",
            "Sky freeway for storms and jets: jet-stream science.",
        ],
        "bubbles": [
            ("Fast ribbon!", "Jet stream?"),
            ("Swift wind", "rivers high."),
            ("Steer weather", "systems."),
            ("Planes ride", "to save time."),
            ("Ribbon wiggles", "by season."),
            ("Cold meets", "warm air."),
            ("Storms ride", "too."),
            ("Forecasts", "watch it."),
            ("Maps sketch", "the path."),
            ("Physics, not", "magic."),
            ("Flights feel", "the river."),
            ("Jet-stream", "science."),
        ],
        "scenes": [
            "WIDE soft forecast map ribbon; boy and robot one-third; empty speech bubbles",
            "DIAGRAM-SOFT high wind river soft; tiny figures; empty speech bubbles",
            "MEDIUM weather systems steered soft; characters one-third; empty speech bubbles",
            "PLAYFUL plane riding wind soft; characters edge; empty speech bubbles",
            "WIDE wiggly seasonal ribbon soft; characters one-third; empty speech bubbles",
            "DIAGRAM-SOFT cold warm meeting soft; tiny figures; empty speech bubbles",
            "MEDIUM storm and plane both soft; boy points; robot; empty speech bubbles",
            "CLOSE forecaster map soft; characters half frame; empty speech bubbles",
            "WIDE ground view clear sky soft; characters one-third; empty speech bubbles",
            "PLAYFUL not magic rails soft; characters half frame; empty speech bubbles",
            "MEDIUM airport soft; boy and robot half frame; empty speech bubbles",
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
    ref_dir = ROOT / ".comic_refs" / "w13_by_story"
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

    Path("/Users/song/qwen3-tts/comic_batch/comics_plan_en_backcatalog_w13.json").write_text(
        json.dumps(plan, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    raw = Path("/Users/song/qwen3-tts/comic_batch/en_work/_raw_backcatalog_w13")
    raw.mkdir(parents=True, exist_ok=True)
    Path("/Users/song/qwen3-tts/comic_batch/en_work/backcatalog_w13_prompts.json").write_text(
        json.dumps(prompts, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    bubbles_path = ROOT / "EyeHaven" / "ComicBubbleWords.en.json"
    bubbles = json.loads(bubbles_path.read_text(encoding="utf-8"))
    for sid, st in STORIES.items():
        bubbles[sid] = [{"i": i, "left": L, "right": R} for i, (L, R) in enumerate(st["bubbles"], 1)]
    bubbles_path.write_text(json.dumps(bubbles, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("wave13 done", len(STORIES), "prompts", len(prompts))


if __name__ == "__main__":
    main()
