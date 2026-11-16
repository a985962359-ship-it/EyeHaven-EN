#!/usr/bin/env python3
"""Back-catalog wave 22: Why E-Y22…E-Y32 → 12-page books. Owner sleeping; no questions."""
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
    "E-Y22": {
        "title": "Why Do Leaves Fall in Autumn?",
        "folder": "Why",
        "tag": "Leaves",
        "companion": "girl",
        "pages": [
            'Orange leaves drift down. "Why fall now?" asks Guangguang.',
            "Trees sense shorter days and cooler air.",
            "They seal tiny doorways at each leaf stem.",
            "Chlorophyll fades; other colors shine through.",
            "Falling leaves help trees rest through winter.",
            "On the ground, leaves become soft soil food.",
            "Evergreens keep needles with special wax coats.",
            "Wind is a helper, not the only reason leaves drop.",
            "Raking can be a gentle outdoor chore with grown-ups.",
            "Autumn is a planned goodbye, not a broken tree.",
            "Catch one leaf and notice its stem scar.",
            "Seal, color, fall: leaf science.",
        ],
        "bubbles": [
            ("Leaves fall!", "Why now?"),
            ("Shorter days,", "cooler air."),
            ("Seal tiny", "stem doors."),
            ("Green fades;", "colors show."),
            ("Trees rest", "for winter."),
            ("Leaves feed", "the soil."),
            ("Evergreens keep", "needles."),
            ("Wind helps,", "not alone."),
            ("Rake gently", "together."),
            ("Planned", "goodbye."),
            ("Catch a leaf", "scar."),
            ("Leaf", "science."),
        ],
        "scenes": [
            "WIDE soft park orange leaves fall; girl and robot one-third; empty speech bubbles",
            "DIAGRAM-SOFT shorter cooler soft; tiny figures; empty speech bubbles",
            "CLOSE stem seal soft; girl points; robot; empty speech bubbles",
            "PLAYFUL colors shine soft; characters half frame; empty speech bubbles",
            "MEDIUM trees rest soft; characters half frame; empty speech bubbles",
            "WIDE leaves soil food soft; characters one-third; empty speech bubbles",
            "CLOSE evergreen needles soft; characters half frame; empty speech bubbles",
            "MEDIUM wind helper soft; characters half frame; empty speech bubbles",
            "PLAYFUL gentle rake soft; characters half frame; empty speech bubbles",
            "DIAGRAM-SOFT planned goodbye soft; tiny figures; empty speech bubbles",
            "MEDIUM catch leaf soft; girl and robot half frame; empty speech bubbles",
            "ENDING girl and robot soft smile; one-third; empty speech bubbles",
        ],
    },
    "E-Y23": {
        "title": "Why Does Pepper Make You Sneeze?",
        "folder": "Why",
        "tag": "Pepper",
        "companion": "boy",
        "pages": [
            'Pepper dust makes Max achoo. "Why sneeze?" asks Guangguang.',
            "Tiny pepper bits tickle sensors in your nose.",
            "Nerves send a fast message: clear this out!",
            "A sneeze blasts air to push the tickle away.",
            "Eyes may water a little from the same reflex path.",
            "Pepper is not germs—just a spicy dust alarm.",
            "Covering a sneeze keeps droplets kinder to friends.",
            "A tissue or elbow is a polite sneeze shield.",
            "Cooking with a grown-up? Keep pepper jars calm.",
            "Tickle → signal → blast: sneeze science.",
            "Smell gentle spices from a safe distance.",
            "Achoo alarm: nose science.",
        ],
        "bubbles": [
            ("Achoo!", "Why sneeze?"),
            ("Pepper tickles", "nose."),
            ("Nerves say", "clear out!"),
            ("Sneeze blasts", "air."),
            ("Eyes may", "water."),
            ("Not germs—", "dust alarm."),
            ("Cover sneeze", "kindly."),
            ("Tissue or", "elbow."),
            ("Calm pepper", "jars."),
            ("Tickle signal", "blast."),
            ("Smell from", "afar."),
            ("Nose", "science."),
        ],
        "scenes": [
            "WIDE soft kitchen pepper sneeze; boy and robot one-third; empty speech bubbles",
            "CLOSE pepper tickle nose soft; boy points; robot; empty speech bubbles",
            "DIAGRAM-SOFT nerve clear-out soft; tiny figures; empty speech bubbles",
            "PLAYFUL sneeze blast soft gentle; characters half frame; empty speech bubbles",
            "MEDIUM watery eyes soft; characters half frame; empty speech bubbles",
            "WIDE dust alarm not germs soft; characters one-third; empty speech bubbles",
            "CLOSE cover sneeze soft; characters half frame; empty speech bubbles",
            "MEDIUM tissue elbow soft; characters half frame; empty speech bubbles",
            "PLAYFUL calm pepper jar soft; characters half frame; empty speech bubbles",
            "DIAGRAM-SOFT tickle signal blast soft; tiny figures; empty speech bubbles",
            "MEDIUM smell afar soft; boy and robot half frame; empty speech bubbles",
            "ENDING boy and robot soft smile; one-third; empty speech bubbles",
        ],
    },
    "E-Y24": {
        "title": "Why Is Fire Hot?",
        "folder": "Why",
        "tag": "Fire",
        "companion": "girl",
        "pages": [
            'A candle glows. "Why is fire hot?" whispers Guangguang.',
            "Fire is a fast chemical dance with fuel and oxygen.",
            "That dance releases energy we feel as heat and see as light.",
            "Different fuels burn at different warmth levels.",
            "Grown-ups keep flames in safe places like candles or stoves.",
            "Never touch fire or play with matches—ask for help.",
            "Smoke means leftover bits floating away; step back.",
            "Firefighters train to cool and stop unsafe fires.",
            "Heat can cook food when adults control it carefully.",
            "Hot means energy pouring out of the reaction.",
            "Watch a candle only with a grown-up nearby.",
            "Fuel, air, heat: fire science—safely.",
        ],
        "bubbles": [
            ("Candle glow!", "Why hot?"),
            ("Fuel meets", "oxygen."),
            ("Energy = heat", "and light."),
            ("Fuels burn", "differently."),
            ("Grown-ups keep", "flames safe."),
            ("Never touch!", "Ask help."),
            ("Smoke? Step", "back."),
            ("Firefighters", "cool fires."),
            ("Adults cook", "with heat."),
            ("Hot = energy", "out."),
            ("Watch candle", "together."),
            ("Fire", "science."),
        ],
        "scenes": [
            "WIDE soft room safe candle glow; girl and robot one-third; empty speech bubbles",
            "DIAGRAM-SOFT fuel oxygen dance soft; tiny figures; empty speech bubbles",
            "CLOSE heat and light soft; girl points; robot; empty speech bubbles",
            "MEDIUM different fuels soft; characters half frame; empty speech bubbles",
            "WIDE safe stove candle soft; characters one-third; empty speech bubbles",
            "CLOSE never touch ask soft; characters half frame; empty speech bubbles",
            "PLAYFUL step back smoke soft; characters half frame; empty speech bubbles",
            "MEDIUM firefighter cool soft gentle; characters half frame; empty speech bubbles",
            "CLOSE cook with adult soft; characters half frame; empty speech bubbles",
            "DIAGRAM-SOFT energy out soft; tiny figures; empty speech bubbles",
            "MEDIUM watch candle soft; girl and robot half frame; empty speech bubbles",
            "ENDING girl and robot soft smile; one-third; empty speech bubbles",
        ],
    },
    "E-Y25": {
        "title": "Why Do We Get Brain Freeze From Cold Drinks?",
        "folder": "Why",
        "tag": "BrainFreeze",
        "companion": "boy",
        "pages": [
            'Icy slush makes Max wince. "Brain freeze!"',
            "Cold touches the roof of your mouth suddenly.",
            "Blood vessels there tighten, then open quickly.",
            "Nerves near your forehead feel the change as a sharp ache.",
            "It is not your brain turning into ice.",
            "Slow sips warm the mouth and calm the signal.",
            "Pressing your tongue to the roof can help gently.",
            "Warmth returns; the freeze usually fades fast.",
            "Treats are fun—just go a little slower.",
            "Cold shock → vessel dance → brief ouch.",
            "Share a slush with a grown-up at easy speed.",
            "Slush pause: cold-drink science.",
        ],
        "bubbles": [
            ("Ouch!", "Brain freeze!"),
            ("Cold hits", "mouth roof."),
            ("Vessels tighten", "then open."),
            ("Forehead nerves", "ache."),
            ("Brain not", "ice."),
            ("Slow sips", "help."),
            ("Tongue on roof", "helps."),
            ("Warmth returns", "fast."),
            ("Fun treats,", "go slow."),
            ("Cold shock", "ouch."),
            ("Share slush", "easy."),
            ("Cold-drink", "science."),
        ],
        "scenes": [
            "WIDE soft cafe icy slush wince; boy and robot one-third; empty speech bubbles",
            "CLOSE cold mouth roof soft; boy points; robot; empty speech bubbles",
            "DIAGRAM-SOFT vessels tighten open soft; tiny figures; empty speech bubbles",
            "MEDIUM forehead ache soft; characters half frame; empty speech bubbles",
            "PLAYFUL brain not ice soft; characters half frame; empty speech bubbles",
            "WIDE slow sips soft; characters one-third; empty speech bubbles",
            "CLOSE tongue on roof soft; characters half frame; empty speech bubbles",
            "MEDIUM warmth returns soft; characters half frame; empty speech bubbles",
            "PLAYFUL go slow treats soft; characters half frame; empty speech bubbles",
            "DIAGRAM-SOFT cold shock soft; tiny figures; empty speech bubbles",
            "MEDIUM share slush soft; boy and robot half frame; empty speech bubbles",
            "ENDING boy and robot soft smile; one-third; empty speech bubbles",
        ],
    },
    "E-Y26": {
        "title": "Why Do Cats Knead Soft Blankets?",
        "folder": "Why",
        "tag": "Knead",
        "companion": "girl",
        "pages": [
            'A cat presses paws on a blanket. "Why knead?" asks Mia.',
            "Kitten kneading helped milk flow from Mom.",
            "Grown cats keep the cozy habit when happy.",
            "Soft blankets feel like a safe nest spot.",
            "Kneading can release a little calming scent from paws.",
            "It is affection, not scratching to be mean.",
            "If claws prick, a soft pad or thick blanket helps.",
            "Different cats knead more or less—personalities differ.",
            "Pet gently when the cat invites you.",
            "Paw press = comfort memory.",
            "Watch your cat’s soft rhythm with a grown-up.",
            "Knead joy: cat science.",
        ],
        "bubbles": [
            ("Paw press!", "Why knead?"),
            ("Kittens helped", "milk flow."),
            ("Grown cats keep", "habit."),
            ("Blankets feel", "like nest."),
            ("Paws leave", "calm scent."),
            ("Affection,", "not mean."),
            ("Thick blanket", "helps."),
            ("Cats differ", "a lot."),
            ("Pet when", "invited."),
            ("Comfort", "memory."),
            ("Watch rhythm", "together."),
            ("Cat", "science."),
        ],
        "scenes": [
            "WIDE soft living room cat knead blanket; girl and robot one-third; empty speech bubbles",
            "DIAGRAM-SOFT kitten milk memory soft gentle; tiny figures; empty speech bubbles",
            "CLOSE grown cat happy knead soft; girl points; robot; empty speech bubbles",
            "MEDIUM nest blanket soft; characters half frame; empty speech bubbles",
            "PLAYFUL paw scent soft; characters half frame; empty speech bubbles",
            "WIDE affection not mean soft; characters one-third; empty speech bubbles",
            "CLOSE thick blanket soft; characters half frame; empty speech bubbles",
            "MEDIUM different cats soft; characters half frame; empty speech bubbles",
            "PLAYFUL pet invited soft; characters half frame; empty speech bubbles",
            "DIAGRAM-SOFT comfort memory soft; tiny figures; empty speech bubbles",
            "MEDIUM watch rhythm soft; girl and robot half frame; empty speech bubbles",
            "ENDING girl and robot soft smile; one-third; empty speech bubbles",
        ],
    },
    "E-Y27": {
        "title": "Why Does Metal Rust?",
        "folder": "Why",
        "tag": "Rust",
        "companion": "boy",
        "pages": [
            'An old bike shows orange flakes. "What is rust?"',
            "Iron in metal meets water and air oxygen.",
            "They slowly make a new crumbly orange material.",
            "Rust is a chemical change, not dirt you wipe once.",
            "Paint and oil can slow water from reaching metal.",
            "Stainless mixes help resist rust better.",
            "Wet bikes left outside rust faster.",
            "Gentle drying after rain is a kind habit.",
            "Ask a grown-up before scrubbing rusty tools.",
            "Iron + water + air = slow orange change.",
            "Wipe a wet bike chain together carefully.",
            "Rust watch: metal science.",
        ],
        "bubbles": [
            ("Orange flakes!", "What rust?"),
            ("Iron meets", "water air."),
            ("Makes crumbly", "orange."),
            ("Chemical change,", "not dirt."),
            ("Paint oil", "slow it."),
            ("Stainless", "resists."),
            ("Wet bikes rust", "faster."),
            ("Dry after", "rain."),
            ("Ask before", "scrub."),
            ("Iron water", "air."),
            ("Wipe chain", "together."),
            ("Metal", "science."),
        ],
        "scenes": [
            "WIDE soft garage rusty bike; boy and robot one-third; empty speech bubbles",
            "DIAGRAM-SOFT iron water air soft; tiny figures; empty speech bubbles",
            "CLOSE crumbly orange soft; boy points; robot; empty speech bubbles",
            "MEDIUM chemical not dirt soft; characters half frame; empty speech bubbles",
            "PLAYFUL paint oil protect soft; characters half frame; empty speech bubbles",
            "WIDE stainless resist soft; characters one-third; empty speech bubbles",
            "CLOSE wet bike outside soft; characters half frame; empty speech bubbles",
            "MEDIUM dry after rain soft; characters half frame; empty speech bubbles",
            "CLOSE ask before scrub soft; characters half frame; empty speech bubbles",
            "DIAGRAM-SOFT iron water air change soft; tiny figures; empty speech bubbles",
            "MEDIUM wipe chain soft; boy and robot half frame; empty speech bubbles",
            "ENDING boy and robot soft smile; one-third; empty speech bubbles",
        ],
    },
    "E-Y28": {
        "title": "Why Do We Have Different Blood Types?",
        "folder": "Why",
        "tag": "BloodType",
        "companion": "girl",
        "pages": [
            'Mia hears “blood type.” "Why different kinds?"',
            "Tiny markers on blood cells come in a few letter teams.",
            "A, B, AB, and O are common type names kids may hear.",
            "Your type is inherited from family patterns.",
            "Doctors match types carefully for transfusions.",
            "Having a type is normal—not a contest or rank.",
            "Only medical people should handle blood tests.",
            "Eating veggies and resting help your whole body.",
            "Curiosity is fine; needles belong to clinics.",
            "Markers differ; blood still carries life jobs.",
            "Ask a grown-up what your family knows gently.",
            "Type tags: body science.",
        ],
        "bubbles": [
            ("Blood type?", "Why kinds?"),
            ("Tiny markers", "on cells."),
            ("A B AB O", "names."),
            ("Inherited from", "family."),
            ("Doctors match", "carefully."),
            ("Normal—not a", "contest."),
            ("Only clinics", "test."),
            ("Veggies rest", "help."),
            ("Needles for", "clinics."),
            ("Markers differ;", "same jobs."),
            ("Ask family", "gently."),
            ("Body", "science."),
        ],
        "scenes": [
            "WIDE soft clinic waiting calm; girl and robot one-third; empty speech bubbles",
            "DIAGRAM-SOFT cell markers soft gentle; tiny figures; empty speech bubbles",
            "CLOSE letter type names soft; girl points; robot; empty speech bubbles",
            "MEDIUM family inherit soft; characters half frame; empty speech bubbles",
            "WIDE doctor match careful soft; characters one-third; empty speech bubbles",
            "PLAYFUL not a contest soft; characters half frame; empty speech bubbles",
            "CLOSE clinic only soft; characters half frame; empty speech bubbles",
            "MEDIUM veggies rest soft; characters half frame; empty speech bubbles",
            "DIAGRAM-SOFT clinics needles soft gentle; tiny figures; empty speech bubbles",
            "PLAYFUL same life jobs soft; characters half frame; empty speech bubbles",
            "MEDIUM ask family soft; girl and robot half frame; empty speech bubbles",
            "ENDING girl and robot soft smile; one-third; empty speech bubbles",
        ],
    },
    "E-Y29": {
        "title": "Why Do Stars Look Pointy in Drawings?",
        "folder": "Why",
        "tag": "StarPointy",
        "companion": "boy",
        "pages": [
            'Max draws a star with spikes. "Are stars pointy?"',
            "Real stars are giant glowing balls of gas.",
            "From Earth they look like tiny dots of light.",
            "Our eyes and air make sparkles that feel spiky.",
            "Artists draw points to show that sparkle feeling.",
            "Cameras can catch spikes from lens tricks too.",
            "Telescopes show rounder discs of bright stars.",
            "Constellation stick-figures are helpful maps, not wires.",
            "Night drawings can be science plus imagination.",
            "Pointy is a symbol for twinkle.",
            "Compare a drawing to a real sky with a grown-up.",
            "Twinkle art: star science.",
        ],
        "bubbles": [
            ("Pointy star!", "Real?"),
            ("Stars are", "gas balls."),
            ("From Earth:", "tiny dots."),
            ("Eyes and air", "sparkle."),
            ("Art shows", "sparkle."),
            ("Lenses make", "spikes too."),
            ("Telescopes see", "rounder."),
            ("Maps not", "wires."),
            ("Science plus", "imagination."),
            ("Pointy means", "twinkle."),
            ("Compare sky", "together."),
            ("Star", "science."),
        ],
        "scenes": [
            "WIDE soft desk draw pointy star; boy and robot one-third; empty speech bubbles",
            "DIAGRAM-SOFT gas ball star soft; tiny figures; empty speech bubbles",
            "CLOSE tiny sky dots soft; boy points; robot; empty speech bubbles",
            "PLAYFUL eye air sparkle soft; characters half frame; empty speech bubbles",
            "MEDIUM artist points soft; characters half frame; empty speech bubbles",
            "WIDE camera lens spikes soft; characters one-third; empty speech bubbles",
            "CLOSE telescope rounder soft; characters half frame; empty speech bubbles",
            "MEDIUM constellation map soft; characters half frame; empty speech bubbles",
            "PLAYFUL science imagination soft; characters half frame; empty speech bubbles",
            "DIAGRAM-SOFT pointy twinkle symbol soft; tiny figures; empty speech bubbles",
            "MEDIUM compare sky soft; boy and robot half frame; empty speech bubbles",
            "ENDING boy and robot soft smile; one-third; empty speech bubbles",
        ],
    },
    "E-Y30": {
        "title": "Why Do We Yawn When Others Yawn?",
        "folder": "Why",
        "tag": "Yawn",
        "companion": "girl",
        "pages": [
            'Mia yawns after Guangguang yawns. "Contagious?"',
            "Seeing or hearing a yawn can nudge your brain to copy.",
            "Scientists think it links to empathy and group sync.",
            "Your body may also need a stretch of jaw and air.",
            "Yawning can happen when you are tired or bored.",
            "Copying is not rude—it is a social echo.",
            "Animals yawn too; some species share the echo.",
            "A polite cover of the mouth is kind manners.",
            "Fresh air and sleep help real tiredness.",
            "Echo yawn = brain noticing friends.",
            "Try noticing who yawns first in a cozy room.",
            "Yawn echo: people science.",
        ],
        "bubbles": [
            ("I yawned too!", "Contagious?"),
            ("Brain wants", "to copy."),
            ("Empathy and", "group sync."),
            ("Jaw stretch", "and air."),
            ("Tired or", "bored."),
            ("Social echo,", "not rude."),
            ("Animals yawn", "too."),
            ("Cover mouth", "kindly."),
            ("Sleep fresh air", "help."),
            ("Noticing", "friends."),
            ("Who yawns", "first?"),
            ("People", "science."),
        ],
        "scenes": [
            "WIDE soft couch contagious yawn; girl and robot one-third; empty speech bubbles",
            "DIAGRAM-SOFT brain copy nudge soft; tiny figures; empty speech bubbles",
            "CLOSE empathy sync soft; girl points; robot; empty speech bubbles",
            "MEDIUM jaw stretch soft; characters half frame; empty speech bubbles",
            "PLAYFUL tired bored soft; characters half frame; empty speech bubbles",
            "WIDE social echo soft; characters one-third; empty speech bubbles",
            "CLOSE animals yawn soft; characters half frame; empty speech bubbles",
            "MEDIUM cover mouth soft; characters half frame; empty speech bubbles",
            "PLAYFUL sleep fresh air soft; characters half frame; empty speech bubbles",
            "DIAGRAM-SOFT noticing friends soft; tiny figures; empty speech bubbles",
            "MEDIUM who first soft; girl and robot half frame; empty speech bubbles",
            "ENDING girl and robot soft smile; one-third; empty speech bubbles",
        ],
    },
    "E-Y31": {
        "title": "Why Does Glue Stick?",
        "folder": "Why",
        "tag": "Glue",
        "companion": "boy",
        "pages": [
            'Glue holds paper. "How does sticky work?" asks Max.',
            "Wet glue flows into tiny bumps on surfaces.",
            "As it dries, it hardens and locks those bumps.",
            "Some glues make chemical bonds with the material.",
            "Different glues fit paper, wood, or fabric jobs.",
            "Too much glue can stay soft and fail.",
            "Clean, dry surfaces help glue grab better.",
            "Use school glue with a grown-up’s rules.",
            "Fingers sticky? Warm water and soap help.",
            "Flow, dry, lock: stick science.",
            "Make a tiny paper sandwich test together.",
            "Hold tight: glue science.",
        ],
        "bubbles": [
            ("Paper stuck!", "How sticky?"),
            ("Glue flows into", "bumps."),
            ("Dries and", "locks."),
            ("Some make", "bonds."),
            ("Right glue,", "right job."),
            ("Too much stays", "soft."),
            ("Clean dry", "helps."),
            ("Follow grown-up", "rules."),
            ("Soap washes", "fingers."),
            ("Flow dry", "lock."),
            ("Paper sandwich", "test."),
            ("Glue", "science."),
        ],
        "scenes": [
            "WIDE soft craft table glue paper; boy and robot one-third; empty speech bubbles",
            "DIAGRAM-SOFT glue into bumps soft; tiny figures; empty speech bubbles",
            "CLOSE dry lock soft; boy points; robot; empty speech bubbles",
            "MEDIUM chemical bonds soft; characters half frame; empty speech bubbles",
            "PLAYFUL different glue jobs soft; characters half frame; empty speech bubbles",
            "WIDE too much soft fail soft; characters one-third; empty speech bubbles",
            "CLOSE clean dry surface soft; characters half frame; empty speech bubbles",
            "MEDIUM grown-up rules soft; characters half frame; empty speech bubbles",
            "PLAYFUL wash sticky fingers soft; characters half frame; empty speech bubbles",
            "DIAGRAM-SOFT flow dry lock soft; tiny figures; empty speech bubbles",
            "MEDIUM paper sandwich soft; boy and robot half frame; empty speech bubbles",
            "ENDING boy and robot soft smile; one-third; empty speech bubbles",
        ],
    },
    "E-Y32": {
        "title": "Why Do We See Our Breath in Winter?",
        "folder": "Why",
        "tag": "Breath",
        "companion": "girl",
        "pages": [
            'Mia puffs a cloud outside. "Is that smoke?"',
            "Your breath carries warm water vapor from inside.",
            "Cold air cools that vapor into tiny droplets.",
            "The cloud is a mini fog of water, not fire smoke.",
            "Warmer rooms hide the cloud because air stays softer.",
            "On frosty days the contrast makes clouds pop.",
            "Animals make breath clouds too in winter.",
            "Scarves can catch moisture—keep them dry and cozy.",
            "Breath clouds vanish as droplets spread out.",
            "Warm wet air + cold = visible puff.",
            "Make gentle puffs with a grown-up outdoors.",
            "Winter puff: breath science.",
        ],
        "bubbles": [
            ("Cloud puff!", "Smoke?"),
            ("Warm vapor", "inside."),
            ("Cold makes", "droplets."),
            ("Mini fog,", "not smoke."),
            ("Warm rooms", "hide it."),
            ("Frosty days", "show more."),
            ("Animals puff", "too."),
            ("Scarves catch", "moisture."),
            ("Clouds fade", "away."),
            ("Warm plus cold", "puff."),
            ("Gentle puffs", "outside."),
            ("Breath", "science."),
        ],
        "scenes": [
            "WIDE soft winter outdoor breath cloud; girl and robot one-third; empty speech bubbles",
            "DIAGRAM-SOFT warm vapor soft; tiny figures; empty speech bubbles",
            "CLOSE cold droplets soft; girl points; robot; empty speech bubbles",
            "MEDIUM mini fog not smoke soft; characters half frame; empty speech bubbles",
            "PLAYFUL warm room hide soft; characters half frame; empty speech bubbles",
            "WIDE frosty contrast soft; characters one-third; empty speech bubbles",
            "CLOSE animals puff soft; characters half frame; empty speech bubbles",
            "MEDIUM scarf cozy soft; characters half frame; empty speech bubbles",
            "PLAYFUL cloud fades soft; characters half frame; empty speech bubbles",
            "DIAGRAM-SOFT warm cold puff soft; tiny figures; empty speech bubbles",
            "MEDIUM gentle puffs soft; girl and robot half frame; empty speech bubbles",
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
    ref_dir = ROOT / ".comic_refs" / "w22_by_story"
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

    Path("/Users/song/qwen3-tts/comic_batch/comics_plan_en_backcatalog_w22.json").write_text(
        json.dumps(plan, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    Path("/Users/song/qwen3-tts/comic_batch/en_work/_raw_backcatalog_w22").mkdir(parents=True, exist_ok=True)
    Path("/Users/song/qwen3-tts/comic_batch/en_work/backcatalog_w22_prompts.json").write_text(
        json.dumps(prompts, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    bubbles_path = ROOT / "EyeHaven" / "ComicBubbleWords.en.json"
    bubbles = json.loads(bubbles_path.read_text(encoding="utf-8"))
    for sid, st in STORIES.items():
        bubbles[sid] = [{"i": i, "left": L, "right": R} for i, (L, R) in enumerate(st["bubbles"], 1)]
    bubbles_path.write_text(json.dumps(bubbles, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("wave22 done", len(STORIES), "prompts", len(prompts))


if __name__ == "__main__":
    main()
