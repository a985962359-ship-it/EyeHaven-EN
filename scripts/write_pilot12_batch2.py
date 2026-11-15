#!/usr/bin/env python3
"""Write 12-page pilot scripts for E-B03, E-S01, E-H01, E-W06, E-Z01."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

STORIES = {
    "E-B03": {
        "title": "Why Do We Blink?",
        "pages": [
            "Guangguang tries not to blink. Impossible!",
            "Your eyelids close and open—blink, blink.",
            "Each blink spreads tears like a tiny wipe.",
            "Tears wash away dust so eyes stay clear.",
            "Moist eyes feel soft and comfortable.",
            "Most blinks happen without you thinking.",
            "Screens can make us blink less often.",
            "Fewer blinks mean eyes feel dry and tired.",
            "Soft, slow blinks help the surface shine.",
            "Look far away for a gentle eye break.",
            "Your eyelids are tiny windshield wipers.",
            "Blink kindly—then your eyes say thank you.",
        ],
        "bubbles": [
            ("Don't blink!", "Impossible!"),
            ("Close… open.", "Blink blink!"),
            ("Tiny wipe", "of tears."),
            ("Wash dust.", "Stay clear."),
            ("Moist eyes", "feel soft."),
            ("No thinking.", "Just blink."),
            ("Screens…", "blink less."),
            ("Dry eyes?", "Tired!"),
            ("Soft blinks", "help shine."),
            ("Look far.", "Eye break."),
            ("Windshield", "wipers!"),
            ("Blink kindly.", "Thank you."),
        ],
        "scenes": [
            "Bright kids room; round white robot with green trim and chest lamp tries not to blink funny face; blonde boy in blue T-rex hoodie giggles; two empty white speech bubbles with space for text",
            "Close friendly view of blinking eyelids as soft cartoon; robot points gently; boy mirrors a blink; empty speech bubbles",
            "Diagram-soft tears spreading across eye surface like a wipe; robot and boy watch curious; empty speech bubbles",
            "Tiny dust speck washed away by tear sheen; robot and boy relieved smiles; empty speech bubbles",
            "Boy's eyes look comfy and bright; robot gives thumbs up; cozy indoor light; empty speech bubbles",
            "Boy reading casually while automatic blinks happen; robot nods; empty speech bubbles",
            "Boy on tablet; blink count low; robot taps shoulder kindly; empty speech bubbles",
            "Boy rubs dry tired eyes gently; robot offers water bottle concern; empty speech bubbles",
            "Boy practices soft slow blinks; robot coaches calmly; empty speech bubbles",
            "Boy and robot look out window to far trees; soft daylight; empty speech bubbles",
            "Playful metaphor: eyelids as tiny windshield wipers on a toy car face; robot and boy laugh; empty speech bubbles",
            "Warm ending; boy blinks kindly; robot chest lamp glows; both smile; empty speech bubbles",
        ],
    },
    "E-S01": {
        "title": "Why Does the Moon Follow Us?",
        "pages": [
            "On a car ride, the Moon seems to tag along.",
            'Guangguang asks, "Is the Moon chasing us?"',
            "Nearby trees zoom past the window fast.",
            "The Moon is very, very far away.",
            "Far things seem to move slowly beside you.",
            "So the Moon looks like a friendly follower.",
            "It isn't jogging after the car at all.",
            "The Moon orbits Earth on its own path.",
            "Distance and perspective play this cozy trick.",
            "Many towns see the same bright Moon tonight.",
            "Not a chase—just space looking close.",
            "Wave hello. The Moon keeps its quiet watch.",
        ],
        "bubbles": [
            ("Moon tags along!", "Wow."),
            ("Is it chasing", "us?"),
            ("Trees zoom!", "So fast."),
            ("Moon is", "far away."),
            ("Far things", "move slow."),
            ("Friendly", "follower!"),
            ("Not jogging!", "Nope."),
            ("Own path", "around Earth."),
            ("Cozy trick", "of distance."),
            ("Same Moon", "many towns."),
            ("Not a chase.", "Just space."),
            ("Wave hello!", "Quiet watch."),
        ],
        "scenes": [
            "Night car ride; big soft Moon outside window; round white green-trim robot and blonde boy in blue T-rex hoodie looking out; empty speech bubbles",
            "Robot asks with curious face; boy points at Moon; car interior cozy; empty speech bubbles",
            "Blurred trees rushing past window; Moon hangs steady; robot and boy notice contrast; empty speech bubbles",
            "Wide night sky showing distant Moon; Earth curve soft; robot and boy small in car; empty speech bubbles",
            "Side-by-side idea: near fence zooms, far Moon drifts slow; robot explains; boy nods; empty speech bubbles",
            "Friendly Moon seems to follow the car down the road; warm moonlight; empty speech bubbles",
            "Silly joke panel: Moon not wearing jogging shoes; robot and boy laugh; empty speech bubbles",
            "Simple orbit diagram Moon circling Earth; soft kids science art; robot and boy watch; empty speech bubbles",
            "Perspective trick shown with near lamp post vs far Moon; empty speech bubbles",
            "Two towns under same Moon; robot and boy wave from car; empty speech bubbles",
            "Calm night; Moon close-looking but peaceful; robot and boy relaxed; empty speech bubbles",
            "Boy and robot wave hello to Moon; quiet starry ending; empty speech bubbles",
        ],
    },
    "E-H01": {
        "title": "Why Do Shadows Follow Us?",
        "pages": [
            "Guangguang spins. The shadow spins too!",
            "A shadow appears when something blocks light.",
            "Light hits you; a dark shape falls behind.",
            "Move left—the blocked spot moves left.",
            "That's why the shadow seems to follow.",
            "Move the lamp, and shadows stretch or shrink.",
            "At noon the Sun is high; shadows stay short.",
            "Later, long shadows walk across the ground.",
            "Soft light makes fuzzy edges; hard light looks sharp.",
            "Shadows are light's quiet footprints.",
            "No feet of their own—just blocked brightness.",
            "Dance once. Your shadow dances with you.",
        ],
        "bubbles": [
            ("I spin!", "Shadow too!"),
            ("Block light.", "Shadow!"),
            ("Light hits.", "Dark behind."),
            ("Move left—", "shadow left."),
            ("Seems to", "follow me!"),
            ("Move lamp.", "Stretch!"),
            ("Noon sun.", "Short shadow."),
            ("Later…", "long shadow."),
            ("Fuzzy or", "sharp edges."),
            ("Quiet", "footprints."),
            ("No own feet.", "Just light."),
            ("Dance!", "Shadow dance!"),
        ],
        "scenes": [
            "Sunny room; round white green-trim robot spins; matching shadow on floor; blonde boy in blue T-rex hoodie laughs; empty speech bubbles",
            "Lamp light blocked by robot making clear shadow; boy points; empty speech bubbles",
            "Light beam hits boy; dark shape on wall behind; robot explains; empty speech bubbles",
            "Boy steps left; shadow slides left with him; robot follows; empty speech bubbles",
            "Boy walks; shadow tags along on sidewalk; playful; empty speech bubbles",
            "Hand moves desk lamp; shadows stretch and shrink; robot and boy experiment; empty speech bubbles",
            "Outdoor noon; short stubby shadows under high sun; robot and boy; empty speech bubbles",
            "Golden hour; long shadows across park path; robot and boy stroll; empty speech bubbles",
            "Split soft cloudy light fuzzy shadow vs hard lamp sharp shadow; empty speech bubbles",
            "Shadows as quiet footprint shapes on ground; gentle metaphor art; empty speech bubbles",
            "Boy looks at shadow feet; robot shakes head kindly no own feet; empty speech bubbles",
            "Boy and robot dance; shadows dance with them; joyful ending; empty speech bubbles",
        ],
    },
    "E-W06": {
        "title": "Why Do Rainbows Appear?",
        "pages": [
            "After a shower, colors arc across the sky.",
            'Guangguang points. "Where did that bow come from?"',
            "Sunlight slips into tiny raindrops.",
            "Inside each drop, light bends and reflects.",
            "Different colors bend by different amounts.",
            "Red, orange, yellow—then green to violet.",
            "You need sun behind you and drops ahead.",
            "The bow isn't a road you can walk on.",
            "It's light's geometry painted in water.",
            "Move a little; the rainbow seems to move too.",
            "Same sunshine, same drops—new place to stand.",
            "After rain, look opposite the Sun and smile.",
        ],
        "bubbles": [
            ("Colors arc!", "After rain."),
            ("Where from?", "That bow!"),
            ("Sunlight in", "raindrops."),
            ("Bend and", "reflect."),
            ("Colors bend", "differently."),
            ("Red to", "violet!"),
            ("Sun behind.", "Drops ahead."),
            ("Not a road!", "Can't walk."),
            ("Light math", "in water."),
            ("I move—", "bow moves."),
            ("New spot.", "Same light."),
            ("Look opposite", "the Sun!"),
        ],
        "scenes": [
            "Post-rain landscape; bright rainbow arc; round white green-trim robot and blonde boy in blue T-rex hoodie marvel; empty speech bubbles",
            "Robot points up at rainbow; boy wonders; wet grass sparkle; empty speech bubbles",
            "Sun rays entering cute oversized raindrop; soft science picture book; robot and boy watch; empty speech bubbles",
            "Inside raindrop light bouncing; gentle refraction glow; empty speech bubbles",
            "Spectrum splitting inside drop; simple colorful diagram feel; empty speech bubbles",
            "Full rainbow bands red to violet labeled softly in scene without hard text clutter; characters smile; empty speech bubbles",
            "Boy stands with sun behind him; raindrops ahead; robot positions him correctly; empty speech bubbles",
            "Boy tries to walk toward rainbow that stays away; funny gentle lesson; empty speech bubbles",
            "Geometry of light in water painted as soft art; robot and boy thoughtful; empty speech bubbles",
            "Boy steps aside; rainbow appears to shift; robot nods; empty speech bubbles",
            "Same sun and drops; boy stands in new spot; still sees bow; empty speech bubbles",
            "Ending: boy and robot look opposite the Sun after rain and smile; empty speech bubbles",
        ],
    },
    "E-Z01": {
        "title": "Eyes Get Tired—Time to Rest",
        "pages": [
            "Please listen. Guangguang Safety Theater. Eyes Get Tired—Time to Rest.",
            "Guangguang: Max, you're staring at that screen like a statue.",
            "Max: One more minute! Just one!",
            "Guangguang: One minute often turns into eleven.",
            "Guangguang: Sore eyes and fewer blinks? That's the alarm.",
            "Max: How do I turn the alarm off?",
            "Guangguang: Stop. Look far away. Soft blink.",
            "Guangguang: Stand up and walk a little bit.",
            "Max: So after this episode I stop?",
            "Guangguang: After this episode—you stop. Say it.",
            "Max: I stop. Then I pass Safety Theater!",
            "Guangguang: Eye care isn't winning or losing—it's care. Rest now.",
        ],
        "bubbles": [
            ("Safety Theater", "Eyes rest."),
            ("Screen statue!", "Blink, Max."),
            ("One more", "minute!"),
            ("One → eleven.", "Uh-oh."),
            ("Sore eyes?", "Alarm!"),
            ("Turn alarm", "off how?"),
            ("Stop. Look far.", "Soft blink."),
            ("Stand up.", "Walk a bit."),
            ("After this,", "I stop?"),
            ("You stop.", "Say it."),
            ("I stop!", "I pass!"),
            ("It's care.", "Rest now."),
        ],
        "scenes": [
            "Soft stage-like kids room intro; round white green-trim robot presents Safety Theater; blonde boy Max in blue T-rex hoodie ready; empty speech bubbles",
            "Max frozen staring at tablet like statue; robot taps shoulder; empty speech bubbles",
            "Max pleading one more minute; robot patient; empty speech bubbles",
            "Clock jumping from 1 to 11 minutes comic style; Max surprised; robot knowing look; empty speech bubbles",
            "Max with sore eyes fewer blinks; red soft alarm icon gentle not scary; robot points; empty speech bubbles",
            "Max asks how to turn alarm off; robot kind coach pose; empty speech bubbles",
            "Max looks far out window and soft-blinks; robot coaches; empty speech bubbles",
            "Max stands and takes a short walk with robot; living room; empty speech bubbles",
            "Max checks after episode; tablet closing; robot nods; empty speech bubbles",
            "Robot firm but kind: you stop, say it; Max listening; empty speech bubbles",
            "Max declares I stop and passes Safety Theater proudly; robot cheers; empty speech bubbles",
            "Warm ending rest; tablet away; robot chest lamp glow; Max relaxed smile; empty speech bubbles",
        ],
    },
}

TAGS = {
    "E-B03": "Blink",
    "E-S01": "Moon",
    "E-H01": "Shadow",
    "E-W06": "Rainbow",
    "E-Z01": "Rest",
}
FOLDERS = {
    "E-B03": "Body",
    "E-S01": "Space",
    "E-H01": "How",
    "E-W06": "Weather",
    "E-Z01": "Safety",
}


def main() -> None:
    for sid, st in STORIES.items():
        print("===", sid, st["title"])
        words = []
        for i, page in enumerate(st["pages"], 1):
            # strip speaker label for word-count band on dialogue pages
            body = page
            if ": " in page and page.split(":", 1)[0] in {"Guangguang", "Max", "Mia"}:
                body = page.split(":", 1)[1].strip()
            w = len(body.split())
            words.append(w)
            if not (5 <= w <= 28):
                raise SystemExit(f"bad word count {sid} {i}: {w} — {page}")
            print(f"  {i:02d} ({w}w) {page}")
        print(f"  TOTAL {sum(words)} words, mean {sum(words)/len(words):.1f}")

    text_map = {sid: "\n\n".join(st["pages"]) for sid, st in STORIES.items()}
    for rel in (
        "EyeHaven/BedtimeContentCatalog.en.json",
        "EyeHaven/BedtimeContentCatalog.json",
    ):
        path = ROOT / rel
        data = json.loads(path.read_text(encoding="utf-8"))
        for story in data["stories"]:
            if story["id"] in text_map:
                story["text"] = text_map[story["id"]]
        data["updatedAt"] = "2026-11-16"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print("updated", path)

    plan = []
    for sid, st in STORIES.items():
        panels = []
        for i, (scene, (left, right)) in enumerate(zip(st["scenes"], st["bubbles"]), 1):
            panels.append(
                {
                    "i": i,
                    "scene": scene,
                    "left": left,
                    "right": right,
                    "tag": f"{TAGS[sid]} {i}/12",
                    "narration": st["pages"][i - 1],
                }
            )
        plan.append(
            {
                "id": sid,
                "title": st["title"],
                "companion": "boy",
                "panels": panels,
            }
        )

    plan_path = Path("/Users/song/qwen3-tts/comic_batch/comics_plan_en_pilot12_b2.json")
    plan_path.write_text(json.dumps(plan, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("wrote", plan_path)

    # also merge into main pilot plan for tooling that expects one file
    main_plan_path = Path("/Users/song/qwen3-tts/comic_batch/comics_plan_en_pilot12.json")
    if main_plan_path.exists():
        old = json.loads(main_plan_path.read_text(encoding="utf-8"))
        by_id = {ep["id"]: ep for ep in old}
        for ep in plan:
            by_id[ep["id"]] = ep
        merged = list(by_id.values())
        main_plan_path.write_text(json.dumps(merged, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print("merged", main_plan_path, "episodes", len(merged))

    for sid, folder in FOLDERS.items():
        path = ROOT / "睡前有声稿" / "美国英文稿" / folder / f"{sid}.txt"
        path.parent.mkdir(parents=True, exist_ok=True)
        body = STORIES[sid]["title"] + "\n\n" + "\n\n".join(STORIES[sid]["pages"]) + "\n"
        path.write_text(body, encoding="utf-8")
        print("wrote", path)


if __name__ == "__main__":
    main()
