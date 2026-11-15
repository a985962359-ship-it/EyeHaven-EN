#!/usr/bin/env python3
"""Free-front-5 wave 1: Animals remaining E-A02…E-A05 → 12-page audible picture books.

Background rules: docs/kid-friendly-backgrounds.md (readable place, warm light,
knowledge object in scene, empty speech-bubble space).
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PREFIX = (
    "Children's picture book comic panel, soft warm friendly lighting, landscape 4:3. "
    "Cute round-headed white robot Guangguang with green trim, warm glowing chest lamp, "
    "small star on head, honest smile. Blonde boy about 6 years old wearing a blue T-rex hoodie. "
    "Exactly two empty white oval speech bubbles with blank white interiors and no letters inside. "
    "No scary imagery, no text logos, consistent character design. "
    "Simple readable background, big clear shapes, shallow depth, soft edges, no clutter. Scene: "
)

STORIES = {
    "E-A02": {
        "title": "Why Do Cats Purr?",
        "folder": "Animals",
        "tag": "Purr",
        "pages": [
            'A cat curls up. Rrr-rrr. Guangguang whispers, "Tiny motor?"',
            "Cats often purr when they feel safe and happy.",
            "Soft petting, resting, or snuggling can start the sound.",
            "Muscles near the voice box vibrate as the cat breathes.",
            "Air in, air out—tiny vibes make the purr.",
            "Some cats also purr when they need comfort.",
            "Nervous moments may bring a quiet, steady purr too.",
            'Purring does not mean "leave me alone."',
            "Soft ears and a soft body usually mean the cat likes it.",
            "Pet gently. Watch the whole cat, not only the sound.",
            "If the cat walks away, stop and give space.",
            "Kind hands, calm purrs—friends who listen carefully.",
        ],
        "bubbles": [
            ("Rrr-rrr!", "Tiny motor?"),
            ("Safe + happy", "purrs."),
            ("Pet. Rest.", "Snuggle."),
            ("Voice box", "vibrates."),
            ("Air in…", "purr out."),
            ("Need comfort?", "Purr too."),
            ("Nervous?", "Quiet purr."),
            ("Not leave me", "alone."),
            ("Soft ears,", "soft body."),
            ("Pet gently.", "Watch all."),
            ("Walks away?", "Give space."),
            ("Kind hands.", "Listen."),
        ],
        "scenes": [
            "Cozy sunny living room rug; fluffy orange cat curled purring; robot leans in curious; boy smiles; empty speech bubbles",
            "Same warm living room; cat eyes soft and happy; robot chest lamp glow; boy sits nearby; empty speech bubbles",
            "Boy gently pets cat on sofa; robot watches kindly; soft window light; empty speech bubbles",
            "Soft friendly close-up of cat throat area as gentle cartoon; robot points; boy curious; empty speech bubbles",
            "Simple soft diagram of breath arrows in and out near cat; robot and boy learn together; empty speech bubbles",
            "Cat tucked in blanket corner seeking comfort; robot offers calm presence; boy patient; empty speech bubbles",
            "Mild rainy window; cat quiet purr on cushion; boy and robot sit soft; empty speech bubbles",
            "Robot shakes head gently correcting myth; boy listens; cat still cozy; empty speech bubbles",
            "Cat with soft ears and loose body language; boy reads calm cues; robot nods; empty speech bubbles",
            "Boy pets slowly with open hand; robot coaches; bright kids room; empty speech bubbles",
            "Cat walks away to another room; boy stops petting respectfully; robot thumbs-up; empty speech bubbles",
            "Warm ending; boy and robot sit while cat purrs nearby; peaceful home; empty speech bubbles",
        ],
    },
    "E-A03": {
        "title": "Why Do Dogs Wag Their Tails?",
        "folder": "Animals",
        "tag": "Wag",
        "pages": [
            'A dog\'s tail goes swish-swish. "Always happy?" asks Guangguang.',
            "A wagging tail is a message, not just a yes.",
            "A loose, wide wag with a soft body often means friendly joy.",
            "A stiff, high wag can mean unsure or on alert.",
            "Look at ears, mouth, and how close the dog stands.",
            "The whole body tells the story of the wag.",
            "Friendly excitement looks bouncy and soft.",
            "Alert feelings look taller, tighter, and careful.",
            "Never rush a dog you do not know.",
            "Ask a grown-up before you say hello.",
            "Friendly wags are nice—calm hands are kinder.",
            "Read the dog. Then share a gentle hello.",
        ],
        "bubbles": [
            ("Swish-swish!", "Always happy?"),
            ("Tail =", "a message."),
            ("Loose wag,", "friendly joy."),
            ("Stiff high?", "Unsure."),
            ("Ears. Mouth.", "Distance."),
            ("Whole body", "tells it."),
            ("Bouncy soft", "hello!"),
            ("Tall tight", "careful."),
            ("Don't rush", "strange dogs."),
            ("Ask a", "grown-up."),
            ("Calm hands", "are kinder."),
            ("Read dog.", "Gentle hello."),
        ],
        "scenes": [
            "Sunny park grass; friendly golden dog wagging; robot curious; boy watching; empty speech bubbles",
            "Park path; robot points at wagging tail as message; boy thoughtful; empty speech bubbles",
            "Dog with loose wide wag and soft happy body; boy smiles; robot cheers; empty speech bubbles",
            "Same park; dog stiff high tail alert but not scary; boy steps back calmly; robot guides; empty speech bubbles",
            "Close friendly view of dog ears mouth stance; robot teaches; boy studies; empty speech bubbles",
            "Full-body dog pose storytelling; boy and robot compare cues; empty speech bubbles",
            "Playful soft bounce meet-and-greet; dog friendly; boy calm; empty speech bubbles",
            "Dog standing taller careful alert; boy gives space; robot nods; empty speech bubbles",
            "Boy pauses before approaching unknown dog; robot hand signal wait; empty speech bubbles",
            "Boy asks parent nearby; grown-up nods; dog waiting; empty speech bubbles",
            "Boy offers calm open hand; soft wag; robot approves; empty speech bubbles",
            "Warm ending park; gentle hello complete; dog soft wag; boy and robot smile; empty speech bubbles",
        ],
    },
    "E-A04": {
        "title": "How Do Fish Breathe Underwater?",
        "folder": "Animals",
        "tag": "Gills",
        "pages": [
            'Guangguang peeks at a fish tank. "No trip up for air?"',
            "Fish pull water in through their mouths.",
            "Then they push water out over their gills.",
            "Gills are thin layers that take oxygen from water.",
            "Oxygen moves into the fish's blood—quiet and steady.",
            "Gills work like tiny underwater lungs for water.",
            "Clean water helps fish breathe easily.",
            "If water has little oxygen, fish can struggle.",
            "People breathe air with lungs.",
            "Fish breathe oxygen dissolved in water.",
            "Different tools, but the same need: oxygen.",
            "Watch the tank. Thank the quiet gill work.",
        ],
        "bubbles": [
            ("No air trip?", "Hmm."),
            ("Water in", "mouth."),
            ("Out over", "gills."),
            ("Thin layers", "grab O2."),
            ("Into blood", "steady."),
            ("Underwater", "lungs!"),
            ("Clean water", "helps."),
            ("Low oxygen?", "Hard."),
            ("We use", "lungs."),
            ("Fish use", "water O2."),
            ("Same need:", "oxygen."),
            ("Quiet gills.", "Thanks."),
        ],
        "scenes": [
            "Bright kids room aquarium; colorful fish swimming; robot peeks glass; boy beside tank; empty speech bubbles",
            "Soft close view fish opening mouth underwater cartoon; robot points; boy watches; empty speech bubbles",
            "Gentle side view water flowing over gill covers; soft blue tank light; empty speech bubbles",
            "Friendly soft diagram of thin gill layers; robot teaches; boy curious; empty speech bubbles",
            "Simple oxygen dots moving into fish outline; cozy room; empty speech bubbles",
            "Playful metaphor tiny underwater lungs shape soft not medical; robot and boy smile; empty speech bubbles",
            "Clean sparkling tank water; happy fish; boy claps; robot glow; empty speech bubbles",
            "Slightly dull water caution gentle not scary; fish slower; robot concerned kindly; empty speech bubbles",
            "Boy takes a calm breath of air; robot contrasts; aquarium nearby; empty speech bubbles",
            "Split soft idea: air bubble vs water oxygen; robot explains; empty speech bubbles",
            "Robot and boy high-five same need oxygen; tank glow; empty speech bubbles",
            "Warm ending watching peaceful fish; night-soft room lamp; empty speech bubbles",
        ],
    },
    "E-A05": {
        "title": "Why Do Dogs Pant?",
        "folder": "Animals",
        "tag": "Pant",
        "pages": [
            'Warm day. A dog goes pant-pant. "Hot?" asks Guangguang.',
            "Dogs do not sweat much through skin like people.",
            "Panting moves air quickly over tongue and mouth.",
            "That airflow helps heat leave the body.",
            "After a run, panting is a dog's cooler.",
            "Sunny days can bring long, easy pant-pant too.",
            "Shade and water help a warm dog feel better.",
            "If panting is very hard and the dog seems weak, get help.",
            "Find shade, offer water, and tell a grown-up.",
            "Never leave a dog in a hot car.",
            "Rest and water help everyone cool down.",
            "Pant means cool-down—care keeps dogs safe.",
        ],
        "bubbles": [
            ("Pant-pant!", "Hot?"),
            ("Not much", "skin sweat."),
            ("Air over", "tongue."),
            ("Heat leaves", "body."),
            ("After a run,", "cooler!"),
            ("Sunny day", "pant too."),
            ("Shade + water", "help."),
            ("Hard pant?", "Get help."),
            ("Shade. Water.", "Grown-up."),
            ("Never hot", "car!"),
            ("Rest + water", "cool down."),
            ("Care keeps", "dogs safe."),
        ],
        "scenes": [
            "Sunny backyard grass; friendly dog panting tongue out; robot asks; boy with water bowl nearby; empty speech bubbles",
            "Soft compare: boy skin vs dog fur simple friendly; robot teaches; empty speech bubbles",
            "Close friendly dog mouth tongue airflow lines soft cartoon; boy watches; empty speech bubbles",
            "Heat wavy lines leaving dog gently; park path; empty speech bubbles",
            "Dog after short play run panting; boy jogs beside; robot cheers rest; empty speech bubbles",
            "Bright sunny lawn; dog pant-pant under sun hat shadow of tree starting; empty speech bubbles",
            "Dog drinks water in shade; boy pours bowl; robot approving; empty speech bubbles",
            "Dog looks tired weak soft concern not scary; boy calls; robot serious kind; empty speech bubbles",
            "Boy leads dog to tree shade with water; grown-up arrives; empty speech bubbles",
            "Hot car warning as gentle red-soft icon not horror; robot blocks kindly; boy understands; empty speech bubbles",
            "Family rest on blanket with dog cooled; water bowls; empty speech bubbles",
            "Warm ending sunset soft; dog calm; boy and robot smile; empty speech bubbles",
        ],
    },
}


def validate() -> None:
    for sid, st in STORIES.items():
        assert len(st["pages"]) == 12
        assert len(st["bubbles"]) == 12
        assert len(st["scenes"]) == 12
        words = []
        for i, page in enumerate(st["pages"], 1):
            w = len(page.split())
            words.append(w)
            if not (5 <= w <= 28):
                raise SystemExit(f"bad word count {sid} {i}: {w} — {page}")
        print(f"{sid} TOTAL {sum(words)} words, mean {sum(words)/12:.1f}")


def main() -> None:
    validate()
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
    prompts = []
    ref_candidates = [
        Path("/Users/song/qwen3-tts/comic_batch/en_work/_raw_pilot/c-E-A01-01.jpg"),
        Path(
            "/Users/song/Library/Application Support/Cursor/AgentStores/"
            "cursor_agent_stores/bc-6341924c-d627-5e70-8277-ff97645af6c8/files/comics/assets/c-E-A01-01.jpg"
        ),
        Path("/Users/song/EyeHaven-EN/.cursor/comic-refs/c-E-A01-01.jpg"),
        Path("/Users/song/qwen3-tts/comic_batch/guangguang_ref.png"),
    ]
    ref = next((str(p) for p in ref_candidates if p.exists()), ref_candidates[-1].as_posix())
    for sid, st in STORIES.items():
        panels = []
        for i, (scene, (left, right)) in enumerate(zip(st["scenes"], st["bubbles"]), 1):
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
                    "description": PREFIX + scene,
                    "ref": ref,
                }
            )
        plan.append({"id": sid, "title": st["title"], "companion": "boy", "panels": panels})

    plan_path = Path("/Users/song/qwen3-tts/comic_batch/comics_plan_en_free_front5_w1.json")
    plan_path.write_text(json.dumps(plan, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("wrote", plan_path)

    prompts_path = Path("/Users/song/qwen3-tts/comic_batch/en_work/free_front5_w1_prompts.json")
    prompts_path.parent.mkdir(parents=True, exist_ok=True)
    prompts_path.write_text(json.dumps(prompts, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("wrote", prompts_path, "count", len(prompts))

    # merge into tooling plan file used by finalize
    main_plan = Path("/Users/song/qwen3-tts/comic_batch/comics_plan_en_pilot12.json")
    if main_plan.exists():
        old = json.loads(main_plan.read_text(encoding="utf-8"))
        by_id = {ep["id"]: ep for ep in old}
        for ep in plan:
            by_id[ep["id"]] = ep
        main_plan.write_text(json.dumps(list(by_id.values()), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print("merged", main_plan, "episodes", len(by_id))

    for sid, st in STORIES.items():
        path = ROOT / "睡前有声稿" / "美国英文稿" / st["folder"] / f"{sid}.txt"
        path.parent.mkdir(parents=True, exist_ok=True)
        body = st["title"] + "\n\n" + "\n\n".join(st["pages"]) + "\n"
        path.write_text(body, encoding="utf-8")
        print("wrote", path)


if __name__ == "__main__":
    main()
