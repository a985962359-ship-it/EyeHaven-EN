#!/usr/bin/env python3
"""Write 12-page pilot scripts for E-A01, E-A14, E-Y04 into catalogs + comic plan."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

STORIES = {
    "E-A01": {
        "title": "Why Can Birds Fly?",
        "pages": [
            'Guangguang lifts a tiny paper bird. "Why can real birds fly?"',
            "Birds have light, hollow bones—less weight to lift.",
            "Strong chest muscles pull the wings hard.",
            "Feathers catch the air like soft sails.",
            "A flap pushes air down, and the bird goes up.",
            "Gliding rides moving air under the curved wing.",
            "People are heavier and have no wing feathers.",
            "Airplanes borrow the same idea with big wings.",
            "Watch how a wing curves when a bird turns.",
            "Push, then coast. Push, then coast again.",
            "Birds aren't magic—they're built for the sky.",
            "Next time you see a bird, count one careful flap.",
        ],
        "bubbles": [
            ("Why can birds fly?", "Paper ones can't!"),
            ("Hollow bones!", "Less to lift."),
            ("Strong chest.", "Wings pull hard."),
            ("Soft feathers", "catch the air."),
            ("Push air down—", "bird goes up!"),
            ("Curved wing", "rides the wind."),
            ("We're heavier.", "No wing feathers."),
            ("Planes borrow", "the same idea."),
            ("See the curve?", "Watch a turn."),
            ("Push, then coast.", "Again!"),
            ("Not magic—", "built for sky."),
            ("Count one flap.", "Smile."),
        ],
        "scenes": [
            "Sunny classroom; robot holds tiny paper bird; blonde boy in blue T-rex hoodie leans in curious; chalkboard and window behind",
            "Soft close-up diagram feel: bird silhouette with glowing light hollow bones, robot points, boy looks amazed",
            "Bird on a branch flexing strong chest; robot and boy watching from below in a park",
            "Close wing feathers catching breeze like soft sails; robot and boy reach toward floating feather",
            "Bird mid-flap pushing air down with motion lines; robot and boy cheer upward",
            "Bird gliding on curved wing over soft clouds; robot and boy watch from hill",
            "Boy stands arms out trying to fly beside robot; both look heavy vs tiny bird above",
            "Toy airplane with big wings on desk; robot points from plane to bird outside window; boy smiles",
            "Bird banking a turn, wing curve clear; robot and boy track it with pointing fingers",
            "Bird flap then coast rhythm across blue sky; robot and boy clap gently",
            "Bird soaring proudly; robot and boy stand side by side nodding",
            "Boy and robot outdoors count one careful flap of a nearby bird; warm sunset smile",
        ],
    },
    "E-A14": {
        "title": "Why Do Butterflies Start as Caterpillars?",
        "pages": [
            'Guangguang peeks at a chrysalis. "Costume change?"',
            "A butterfly's life starts as a tiny egg.",
            "The egg hatches into a hungry caterpillar.",
            "The caterpillar eats leaves and grows fast.",
            "Then it makes a chrysalis—or soft pupa shell.",
            "Inside the shell, the body quietly rebuilds.",
            "Wings form. Legs change. A new shape waits.",
            "At last, a butterfly climbs out carefully.",
            "It waits for soft wings to dry and stiffen.",
            "This big change is called metamorphosis.",
            "Caterpillars and butterflies need different plants.",
            "A garden with the right leaves helps them thrive.",
        ],
        "bubbles": [
            ("Costume change?", "What's inside?"),
            ("Life starts", "as a tiny egg."),
            ("Hello, caterpillar!", "So hungry."),
            ("Eat and grow.", "Faster!"),
            ("Chrysalis time.", "Soft shell."),
            ("Quiet rebuild", "inside."),
            ("Wings forming...", "New shape!"),
            ("Climb out", "carefully."),
            ("Wings drying.", "Almost ready."),
            ("Metamorphosis!", "Big change."),
            ("Different plants", "for each stage."),
            ("Right leaves", "help them thrive."),
        ],
        "scenes": [
            "Lush garden; robot peeks at green chrysalis; blonde boy in blue T-rex hoodie leans close curious",
            "Tiny egg on a green leaf close-up; robot and boy observe gently",
            "Bright green caterpillar hatching on leaf; robot waves; boy delighted",
            "Caterpillar munching leaf; robot and boy watch it grow bigger",
            "Caterpillar wrapping into chrysalis on stem; robot and boy whisper",
            "Semi-transparent chrysalis with soft glow of change inside; robot and boy wait patiently",
            "Inside silhouette of forming wings and legs; dreamy soft light; robot and boy amazed",
            "Butterfly carefully climbing from open chrysalis; robot and boy hold still",
            "Butterfly resting with soft wet wings spreading; robot and boy smile",
            "Garden path; robot points to cycle egg-caterpillar-chrysalis-butterfly as soft nature props; boy nods",
            "Caterpillar on milkweed leaf and butterfly on flower nearby; robot and boy compare",
            "Sunny garden with host plants; butterfly flies; robot and boy wave goodbye happily",
        ],
    },
    "E-Y04": {
        "title": "Why Does Popcorn Pop?",
        "pages": [
            "A quiet kernel sits still. Then—POP!",
            'Guangguang jumps. "Why does popcorn pop?"',
            "Inside each hard kernel is a little water.",
            "Heat turns that tiny water into steam.",
            "Steam needs more room than liquid water.",
            "Pressure builds inside the tough shell.",
            "Suddenly the hard shell bursts wide open.",
            "The soft inside flips out fluffy and white.",
            "That's the loud pop you hear and see.",
            "If a kernel is too dry, it may not pop.",
            "Heat and a sip of water work as a team.",
            "Not exploding candy—just a steamy seed surprise.",
        ],
        "bubbles": [
            ("Quiet kernel...", "Then POP!"),
            ("Why does it pop?", "Whoa!"),
            ("Little water", "inside!"),
            ("Heat makes", "steam."),
            ("Steam needs", "more room."),
            ("Pressure builds...", "Hold on!"),
            ("Shell bursts!", "Wide open!"),
            ("Fluffy white", "inside out."),
            ("That's the pop!", "I heard it."),
            ("Too dry?", "Won't pop."),
            ("Heat + water", "teamwork."),
            ("Steamy seed", "surprise!"),
        ],
        "scenes": [
            "Cozy kitchen; single yellow kernel on counter; soft suspense before pop; robot and blonde boy in blue T-rex hoodie watch",
            "Pan on stove popping; robot jumps in surprise; boy says whoa with wide eyes",
            "Cutaway of hard kernel showing tiny water droplet inside; robot points; boy leans in",
            "Kernel over warm flame; water becoming steam swirls; robot and boy watch carefully",
            "Steam expanding inside kernel diagram-style soft art; robot and boy curious",
            "Kernel shell straining under pressure; robot and boy tense excited faces",
            "Kernel bursting open mid-air with pop burst lines; robot and boy cheer",
            "Fluffy white popcorn flipping out of shell; robot catches a piece gently; boy laughs",
            "Bowl of popcorn; robot and boy listening to pops with happy faces",
            "Sad dry kernel that will not pop beside fluffy ones; robot and boy learn gently",
            "Stove heat and tiny water droplet icons as teamwork; robot and boy high-five",
            "Big bowl of popcorn; robot and boy share snack; warm kitchen happy ending",
        ],
    },
}

TAGS = {"E-A01": "Birds", "E-A14": "Butterfly", "E-Y04": "Popcorn"}
FOLDERS = {"E-A01": "Animals", "E-A14": "Animals", "E-Y04": "Why"}


def main() -> None:
    for sid, st in STORIES.items():
        print("===", sid, st["title"])
        words = []
        for i, page in enumerate(st["pages"], 1):
            w = len(page.split())
            words.append(w)
            if not (6 <= w <= 25):
                raise SystemExit(f"bad word count {sid} {i}: {w} — {page}")
            # target band ~8–18; 6–7 ok for punchy beats
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
        data["updatedAt"] = "2026-11-15"
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

    plan_path = Path("/Users/song/qwen3-tts/comic_batch/comics_plan_en_pilot12.json")
    plan_path.write_text(json.dumps(plan, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("wrote", plan_path)

    for sid, folder in FOLDERS.items():
        path = ROOT / "睡前有声稿" / "美国英文稿" / folder / f"{sid}.txt"
        path.parent.mkdir(parents=True, exist_ok=True)
        body = STORIES[sid]["title"] + "\n\n" + "\n\n".join(STORIES[sid]["pages"]) + "\n"
        path.write_text(body, encoding="utf-8")
        print("wrote", path)


if __name__ == "__main__":
    main()
