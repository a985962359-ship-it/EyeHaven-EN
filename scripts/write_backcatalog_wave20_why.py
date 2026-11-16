#!/usr/bin/env python3
"""Back-catalog wave 20: Why E-Y06…E-Y13 → 12-page books. Owner sleeping; no questions."""
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
    "E-Y06": {
        "title": "Why Do Bananas Turn Brown?",
        "folder": "Why",
        "tag": "Banana",
        "companion": "girl",
        "pages": [
            'A yellow banana gets freckles, then brown. "Why?" asks Guangguang.',
            "Bananas keep changing after they are picked.",
            "A natural signal tells them it is time to ripen.",
            "Soft enzymes break down the firm parts inside.",
            "The peel’s yellow color slowly gives way to brown spots.",
            "Sweeter soft fruit is easier for animals—and kids—to enjoy.",
            "Cooler storage slows the browning; warm kitchens speed it up.",
            "Brown freckles can mean ripe and ready, not always “bad.”",
            "If it smells off or is mushy-weird, ask a grown-up before eating.",
            "Browning is ripening chemistry wearing freckles.",
            "Make banana bread with a grown-up when spots arrive.",
            "Ripen, soften, freckle: banana science.",
        ],
        "bubbles": [
            ("Yellow freckles!", "Why brown?"),
            ("Keeps changing", "after picking."),
            ("Signal says", "ripen."),
            ("Enzymes soften", "inside."),
            ("Yellow turns", "to spots."),
            ("Sweeter soft", "fruit."),
            ("Cool slows;", "warm speeds."),
            ("Spots can mean", "ready."),
            ("Weird smell?", "Ask grown-up."),
            ("Ripening", "chemistry."),
            ("Banana bread", "time."),
            ("Banana", "science."),
        ],
        "scenes": [
            "WIDE soft kitchen banana freckles; girl and robot one-third; empty speech bubbles",
            "MEDIUM banana after picking soft; characters one-third; empty speech bubbles",
            "DIAGRAM-SOFT ripen signal soft; tiny figures; empty speech bubbles",
            "CLOSE enzymes soften soft; girl points; robot; empty speech bubbles",
            "PLAYFUL yellow to brown soft; characters half frame; empty speech bubbles",
            "MEDIUM sweet soft fruit soft; characters half frame; empty speech bubbles",
            "CLOSE cool vs warm storage soft; characters half frame; empty speech bubbles",
            "WIDE ripe ready banana soft; characters one-third; empty speech bubbles",
            "CLOSE ask grown-up soft; characters half frame; empty speech bubbles",
            "PLAYFUL chemistry freckles soft; characters half frame; empty speech bubbles",
            "MEDIUM banana bread soft; girl and robot half frame; empty speech bubbles",
            "ENDING girl and robot soft smile; one-third; empty speech bubbles",
        ],
    },
    "E-Y07": {
        "title": "Why Does Metal Feel Colder Than Wood?",
        "folder": "Why",
        "tag": "Metal",
        "companion": "boy",
        "pages": [
            'Guangguang touches a metal spoon and a wooden spoon. "Metal feels colder—same room?"',
            "Often both spoons are nearly the same temperature in the room.",
            "Metal moves heat away from your fingers quickly.",
            "That fast heat steal makes metal feel colder to the touch.",
            "Wood holds heat closer and moves it more slowly.",
            "So wood can feel warmer even when the thermometer agrees.",
            "Tile floors and metal doorknobs play the same trick.",
            "Your skin is a heat detective, not always a temperature label.",
            "Scientists call the quick heat-moving ability conductivity.",
            "Feeling cold can mean heat leaving you fast.",
            "Touch both spoons with a grown-up and compare the surprise.",
            "Heat flows fast in metal: touch science.",
        ],
        "bubbles": [
            ("Metal colder?", "Same room?"),
            ("Temps nearly", "the same."),
            ("Metal steals", "heat fast."),
            ("Fast steal", "feels cold."),
            ("Wood moves", "heat slow."),
            ("Wood can feel", "warmer."),
            ("Tiles knobs", "same trick."),
            ("Skin detects", "heat flow."),
            ("Called", "conductivity."),
            ("Cold = heat", "leaving fast."),
            ("Compare spoons", "together."),
            ("Touch", "science."),
        ],
        "scenes": [
            "WIDE soft kitchen two spoons; boy and robot one-third; empty speech bubbles",
            "DIAGRAM-SOFT same room temp soft; tiny figures; empty speech bubbles",
            "CLOSE metal steals heat soft; characters half frame; empty speech bubbles",
            "MEDIUM feels colder soft; boy points; robot; empty speech bubbles",
            "CLOSE wood slow heat soft; characters half frame; empty speech bubbles",
            "PLAYFUL wood warmer feel soft; characters half frame; empty speech bubbles",
            "WIDE tile doorknob soft; characters one-third; empty speech bubbles",
            "DIAGRAM-SOFT skin heat detective soft; tiny figures; empty speech bubbles",
            "CLOSE conductivity idea soft; characters half frame; empty speech bubbles",
            "PLAYFUL heat leaving soft; characters half frame; empty speech bubbles",
            "MEDIUM compare spoons soft; boy and robot half frame; empty speech bubbles",
            "ENDING boy and robot thumbs-up soft; one-third; empty speech bubbles",
        ],
    },
    "E-Y08": {
        "title": "Why Do We Hiccup?",
        "folder": "Why",
        "tag": "Hiccup",
        "companion": "boy",
        "pages": [
            'Hic—! Guangguang blinks. "Why do we hiccup?"',
            "A hiccup is a sudden squeeze of the diaphragm under your lungs.",
            "Air pops in quickly when that muscle jumps.",
            "Your voice box makes a tiny “hic” sound.",
            "Spicy food, giggles, or gulping air can wake the hiccups.",
            "Most hiccup spells stop on their own after a little while.",
            "Slow breaths and a calm sip of water often help.",
            "Hiccups are annoying, not usually a big danger.",
            "If they last a very long time, tell a grown-up.",
            "A hiccup is a surprise squeeze concert in your chest.",
            "Giggle about it—then breathe soft like a sleepy kitten.",
            "Diaphragm jump: hiccup science.",
        ],
        "bubbles": [
            ("Hic!", "Why?"),
            ("Diaphragm", "squeezes."),
            ("Air pops", "in."),
            ("Voice box", "says hic."),
            ("Spice giggles", "gulps."),
            ("Often stop", "alone."),
            ("Slow breath,", "sip water."),
            ("Annoying, not", "usually danger."),
            ("Lasts long?", "Tell grown-up."),
            ("Surprise squeeze", "concert."),
            ("Breathe soft", "after."),
            ("Hiccup", "science."),
        ],
        "scenes": [
            "WIDE soft living room hiccup; boy and robot one-third; empty speech bubbles",
            "DIAGRAM-SOFT diaphragm soft; tiny figures; empty speech bubbles",
            "CLOSE air pop soft; characters half frame; empty speech bubbles",
            "MEDIUM hic sound soft; boy points; robot; empty speech bubbles",
            "PLAYFUL spicy giggle gulp soft; characters half frame; empty speech bubbles",
            "WIDE wait it out soft; characters one-third; empty speech bubbles",
            "CLOSE water sip soft; characters half frame; empty speech bubbles",
            "PLAYFUL annoying not danger soft; characters half frame; empty speech bubbles",
            "MEDIUM tell grown-up soft; characters half frame; empty speech bubbles",
            "DIAGRAM-SOFT squeeze concert soft; tiny figures; empty speech bubbles",
            "MEDIUM calm breathe soft; boy and robot half frame; empty speech bubbles",
            "ENDING boy and robot thumbs-up soft; one-third; empty speech bubbles",
        ],
    },
    "E-Y09": {
        "title": "Why Do We Have Five Fingers?",
        "folder": "Why",
        "tag": "Fingers",
        "companion": "girl",
        "pages": [
            'Guangguang counts fingers. "Why five?"',
            "Humans usually grow five digits on each hand.",
            "That layout helps us grip, pinch, and use tools.",
            "Thumbs that can touch other fingers make fine work easier.",
            "Fossils show distant relatives also had a five-digit pattern.",
            "Not every animal matches our count—horses and birds differ.",
            "Five is common for us, not a magic perfect number for all life.",
            "Hands learn skills with practice: writing, tying, catching.",
            "Keep fingers safe from doors and sharp tools with care.",
            "Five fingers are a handy toolkit grown on your palms.",
            "Trace your hand and label each helper finger with a grown-up.",
            "Grip, pinch, tool use: five-finger science.",
        ],
        "bubbles": [
            ("Count five!", "Why?"),
            ("Usually five", "digits."),
            ("Helps grip", "and pinch."),
            ("Thumbs do", "fine work."),
            ("Fossils show", "five too."),
            ("Animals differ", "in count."),
            ("Not magic for", "all life."),
            ("Practice builds", "skills."),
            ("Keep fingers", "safe."),
            ("Handy palm", "toolkit."),
            ("Trace and", "label."),
            ("Five-finger", "science."),
        ],
        "scenes": [
            "WIDE soft counting fingers; girl and robot one-third; empty speech bubbles",
            "CLOSE five digits soft; characters half frame; empty speech bubbles",
            "MEDIUM grip pinch soft; girl points; robot; empty speech bubbles",
            "CLOSE thumb touch soft; characters half frame; empty speech bubbles",
            "DIAGRAM-SOFT fossil five soft; tiny figures; empty speech bubbles",
            "PLAYFUL other animals soft; characters half frame; empty speech bubbles",
            "WIDE not magic number soft; characters one-third; empty speech bubbles",
            "MEDIUM practice skills soft; characters half frame; empty speech bubbles",
            "CLOSE finger safety soft; characters half frame; empty speech bubbles",
            "PLAYFUL toolkit hands soft; characters half frame; empty speech bubbles",
            "MEDIUM trace hand soft; girl and robot half frame; empty speech bubbles",
            "ENDING girl and robot soft smile; one-third; empty speech bubbles",
        ],
    },
    "E-Y10": {
        "title": "Why Does Bread Get Moldy?",
        "folder": "Why",
        "tag": "Mold",
        "companion": "boy",
        "pages": [
            'Green fuzz on bread. "Ew—why?" asks Guangguang.',
            "Mold is a tiny living fungus, not magic dirt.",
            "Spores float in air and can land on food.",
            "They grow when bread is moist and not too cold.",
            "Bread is a cozy buffet of starch for them.",
            "Cool, dry, sealed storage slows the fuzzy party.",
            "Seeing mold means skip that slice—don’t just scrape.",
            "Ask a grown-up before tossing or saving nearby pieces.",
            "Some cheeses use friendly molds on purpose; sandwich bread usually does not.",
            "Moldy bread is fungus having a picnic.",
            "Check the bag date and keep the loaf closed tight.",
            "Spores, moisture, buffet: mold science.",
        ],
        "bubbles": [
            ("Green fuzz!", "Why?"),
            ("Tiny living", "fungus."),
            ("Spores float", "and land."),
            ("Moist bread", "helps grow."),
            ("Starch buffet", "for mold."),
            ("Cool dry seal", "slows it."),
            ("See mold,", "skip slice."),
            ("Ask grown-up", "what to do."),
            ("Cheese differs", "from sandwich."),
            ("Fungus picnic", "on bread."),
            ("Close the bag", "tight."),
            ("Mold", "science."),
        ],
        "scenes": [
            "WIDE soft kitchen moldy bread gentle not gross; boy and robot one-third; empty speech bubbles",
            "DIAGRAM-SOFT tiny fungus soft; tiny figures; empty speech bubbles",
            "CLOSE spores landing soft; characters half frame; empty speech bubbles",
            "MEDIUM moist warm soft; boy points; robot; empty speech bubbles",
            "PLAYFUL starch buffet soft; characters half frame; empty speech bubbles",
            "CLOSE sealed bag cool soft; characters half frame; empty speech bubbles",
            "MEDIUM skip the slice soft; characters half frame; empty speech bubbles",
            "CLOSE ask grown-up soft; characters half frame; empty speech bubbles",
            "WIDE cheese vs bread soft; characters one-third; empty speech bubbles",
            "PLAYFUL fungus picnic soft; characters half frame; empty speech bubbles",
            "MEDIUM close bag soft; boy and robot half frame; empty speech bubbles",
            "ENDING boy and robot thumbs-up soft; one-third; empty speech bubbles",
        ],
    },
    "E-Y11": {
        "title": "Why Do We Have Eyebrows?",
        "folder": "Why",
        "tag": "Brows",
        "companion": "girl",
        "pages": [
            'Guangguang draws brows on a face. "What for?"',
            "Eyebrows help keep sweat and rain from running into your eyes.",
            "They act like tiny umbrellas above your gaze.",
            "Brows also show feelings—surprise, worry, joy.",
            "Friends can read your face partly by watching them move.",
            "Without brows, expressions can look flatter.",
            "Hair there grows in a special shape on the brow bone.",
            "Gently patting sweat away still helps on hot days.",
            "Never shave experiments without a grown-up’s okay.",
            "Eyebrows are rain guards and feeling flags together.",
            "Make silly brow faces in a mirror and laugh.",
            "Shield plus signal: eyebrow science.",
        ],
        "bubbles": [
            ("Draw brows!", "What for?"),
            ("Keep sweat", "from eyes."),
            ("Tiny umbrellas", "above."),
            ("Show feelings", "too."),
            ("Friends read", "your face."),
            ("Flat without", "brows."),
            ("Special shape", "on bone."),
            ("Pat sweat on", "hot days."),
            ("No shave games", "alone."),
            ("Rain guards +", "feeling flags."),
            ("Silly faces", "in mirror."),
            ("Eyebrow", "science."),
        ],
        "scenes": [
            "WIDE soft drawing brows; girl and robot one-third; empty speech bubbles",
            "CLOSE sweat rain shield soft; characters half frame; empty speech bubbles",
            "PLAYFUL tiny umbrellas soft; characters half frame; empty speech bubbles",
            "MEDIUM surprise worry joy soft; girl points; robot; empty speech bubbles",
            "WIDE friends read face soft; characters one-third; empty speech bubbles",
            "DIAGRAM-SOFT flatter without soft; tiny figures; empty speech bubbles",
            "CLOSE brow bone shape soft; characters half frame; empty speech bubbles",
            "MEDIUM hot day pat soft; characters half frame; empty speech bubbles",
            "CLOSE ask grown-up soft; characters half frame; empty speech bubbles",
            "PLAYFUL rain guard flags soft; characters half frame; empty speech bubbles",
            "WIDE mirror silly faces soft; girl and robot one-third; empty speech bubbles",
            "ENDING girl and robot soft smile; one-third; empty speech bubbles",
        ],
    },
    "E-Y12": {
        "title": "Why Does Ice Cream Melt?",
        "folder": "Why",
        "tag": "Melt",
        "companion": "boy",
        "pages": [
            'A scoop sags. "Why so fast?" Max wails.',
            "Ice cream is frozen water, fat, and sugar mixed with air.",
            "Warm air and your tongue add heat to the scoop.",
            "Heat makes ice crystals turn back into liquid.",
            "That is why the scoop collapses into a sweet puddle.",
            "Shade and a cold bowl slow the melt; sun speeds it up.",
            "Licking fast is a race against soft physics.",
            "Dropped scoops on hot sidewalks melt even quicker.",
            "Freezers keep crystals solid until snack time.",
            "Melting is heat winning a gentle tug-of-war with ice.",
            "Eat outside with a grown-up’s napkin plan ready.",
            "Heat vs ice crystals: melt science.",
        ],
        "bubbles": [
            ("Scoop sags!", "So fast?"),
            ("Frozen mix", "with air."),
            ("Warm air adds", "heat."),
            ("Ice turns to", "liquid."),
            ("Scoop becomes", "puddle."),
            ("Shade slows;", "sun speeds."),
            ("Licking is a", "race."),
            ("Hot sidewalk", "faster."),
            ("Freezer keeps", "solid."),
            ("Heat wins the", "tug."),
            ("Napkin plan", "ready."),
            ("Melt", "science."),
        ],
        "scenes": [
            "WIDE soft sagging ice cream; boy and robot one-third; empty speech bubbles",
            "DIAGRAM-SOFT ice fat sugar air soft; tiny figures; empty speech bubbles",
            "CLOSE warm air tongue soft; characters half frame; empty speech bubbles",
            "MEDIUM crystals to liquid soft; boy points; robot; empty speech bubbles",
            "PLAYFUL sweet puddle soft; characters half frame; empty speech bubbles",
            "WIDE shade vs sun soft; characters one-third; empty speech bubbles",
            "CLOSE licking race soft; characters half frame; empty speech bubbles",
            "MEDIUM sidewalk melt soft; characters half frame; empty speech bubbles",
            "CLOSE freezer soft; characters half frame; empty speech bubbles",
            "DIAGRAM-SOFT heat tug soft; tiny figures; empty speech bubbles",
            "MEDIUM napkin plan soft; boy and robot half frame; empty speech bubbles",
            "ENDING boy and robot thumbs-up soft; one-third; empty speech bubbles",
        ],
    },
    "E-Y13": {
        "title": "Why Do We Get Hiccups After Soda?",
        "folder": "Why",
        "tag": "Fizz",
        "companion": "girl",
        "pages": [
            'Fizz! Hic! "Why now?" asks Guangguang.',
            "Bubbly drinks can tickle your stomach.",
            "They can also bother the diaphragm under your lungs.",
            "A sudden squeeze makes that tiny “hic.”",
            "Cold fizz and fast gulps make hiccups more likely.",
            "Slow sips give your body a calmer chance.",
            "Most soda hiccups fade after a short wait.",
            "A quiet breath and a water sip may help settle things.",
            "You did nothing “wrong”—bubbles just woke a reflex.",
            "Fizz plus diaphragm equals a surprise hic concert.",
            "Pause between gulps when drinks are very bubbly.",
            "Bubbles tickle, then hic: soda-hiccup science.",
        ],
        "bubbles": [
            ("Fizz! Hic!", "Why now?"),
            ("Bubbles tickle", "stomach."),
            ("Can bother", "diaphragm."),
            ("Squeeze makes", "hic."),
            ("Fast cold gulps", "more likely."),
            ("Slow sips", "calmer."),
            ("Usually fade", "soon."),
            ("Breath and", "water help."),
            ("Not your", "fault."),
            ("Fizz surprise", "concert."),
            ("Pause between", "gulps."),
            ("Soda-hiccup", "science."),
        ],
        "scenes": [
            "WIDE soft soda fizz hiccup; girl and robot one-third; empty speech bubbles",
            "MEDIUM bubbles tickle soft; characters one-third; empty speech bubbles",
            "DIAGRAM-SOFT diaphragm soft; tiny figures; empty speech bubbles",
            "CLOSE hic squeeze soft; girl points; robot; empty speech bubbles",
            "PLAYFUL fast gulp soft; characters half frame; empty speech bubbles",
            "CLOSE slow sip soft; characters half frame; empty speech bubbles",
            "WIDE wait fade soft; characters one-third; empty speech bubbles",
            "MEDIUM water help soft; characters half frame; empty speech bubbles",
            "PLAYFUL not your fault soft; characters half frame; empty speech bubbles",
            "DIAGRAM-SOFT fizz concert soft; tiny figures; empty speech bubbles",
            "MEDIUM pause gulps soft; girl and robot half frame; empty speech bubbles",
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
    ref_dir = ROOT / ".comic_refs" / "w20_by_story"
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

    Path("/Users/song/qwen3-tts/comic_batch/comics_plan_en_backcatalog_w20.json").write_text(
        json.dumps(plan, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    Path("/Users/song/qwen3-tts/comic_batch/en_work/_raw_backcatalog_w20").mkdir(parents=True, exist_ok=True)
    Path("/Users/song/qwen3-tts/comic_batch/en_work/backcatalog_w20_prompts.json").write_text(
        json.dumps(prompts, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    bubbles_path = ROOT / "EyeHaven" / "ComicBubbleWords.en.json"
    bubbles = json.loads(bubbles_path.read_text(encoding="utf-8"))
    for sid, st in STORIES.items():
        bubbles[sid] = [{"i": i, "left": L, "right": R} for i, (L, R) in enumerate(st["bubbles"], 1)]
    bubbles_path.write_text(json.dumps(bubbles, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("wave20 done", len(STORIES), "prompts", len(prompts))


if __name__ == "__main__":
    main()
