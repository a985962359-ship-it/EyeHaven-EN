#!/usr/bin/env python3
"""Rewrite E-W01…E-W05 panel scenes for stronger page-to-page visual variety.

Keeps narration + bubbles. Updates comics plans + prompts for regen.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PREFIX = (
    "Children's picture book comic panel, soft warm friendly lighting, landscape 4:3. "
    "Cute round-headed white robot Guangguang with green trim, warm glowing chest lamp, "
    "small star on head, honest smile when visible. Blonde boy about 6 in blue T-rex hoodie when visible. "
    "Exactly two empty white oval speech bubbles with blank white interiors and no letters inside. "
    "No scary imagery, no text logos. Simple readable background, big clear shapes, soft edges, no clutter. "
    "IMPORTANT: unique camera angle for this page; do NOT reuse a side-by-side park medium shot. Scene: "
)

# Each page: forced distinct shot type + place + knowledge object
SCENES = {
    "E-W01": [
        "WIDE low-angle looking straight up into huge clear blue sky; tiny robot and boy silhouettes at very bottom edge looking up; empty speech bubbles high",
        "CLOSE-UP soft prism splitting a sunbeam into rainbow bands on a wooden floor; robot finger points to blue band; boy kneels; empty speech bubbles",
        "DIAGRAM-SOFT: many tiny air dots bouncing blue light rays sideways; characters small in corner watching; empty speech bubbles",
        "SPLIT panel feel: left red ray going straight, right blue rays bouncing; no park pose; empty speech bubbles",
        "OVER-SHOULDER from boy looking away from sun toward deep blue sky; robot peeks from side; empty speech bubbles",
        "BIRD-EYE of green lawn with long blue sky filling 70% frame; characters lying on backs pointing up; empty speech bubbles",
        "CLOSE sky near sun edge soft white-gold glow (not painful); boy squints at edge of frame; robot shade-hand; empty speech bubbles",
        "THROUGH bedroom window at night: black starry sky outside; robot and boy at windowsill inside warm room; empty speech bubbles",
        "SOFT cutaway: Earth with glowing blue air shell vs black space beyond; robot holds toy globe; empty speech bubbles",
        "MACRO-ish soft cartoon of blue air shell hugging Earth globe on table; boy amazed; empty speech bubbles",
        "MEDIUM indoor science corner with sky poster; robot chest lamp glow; boy thumbs-up; NOT outdoor park; empty speech bubbles",
        "WARM ENDING picnic blanket, sky big above, characters reclining not standing side-by-side; empty speech bubbles",
    ],
    "E-W02": [
        "WIDE hillside silhouette against peach-red sunset sky filling most of frame; tiny robot+boy watching; empty speech bubbles",
        "DIAGRAM-SOFT: long orange sun rays traveling through thick layered air; characters tiny; empty speech bubbles",
        "CLOSE diagram: blue sparkles scattering out of a light path; robot points; empty speech bubbles",
        "CLOSE-UP boy's face lit warm red-orange; robot beside with soft glow; background bokeh sunset; empty speech bubbles",
        "WIDE dusty clouds catching deep red light; characters small on ridge; empty speech bubbles",
        "LOW horizon sun, long warm path of light across grass; robot and boy walk toward light not facing camera side-by-side; empty speech bubbles",
        "MORNING reverse: soft peach sunrise opposite mood; empty speech bubbles",
        "CITY rooftop evening deep red haze; skyline soft; characters at railing looking out; empty speech bubbles",
        "COUNTRYSIDE peach sunset over fields; wagon or fence detail; characters sitting on fence; empty speech bubbles",
        "PLAYFUL metaphor: robot drapes a shiny red-orange 'pretty coat' on a sun cutout; indoor craft table; empty speech bubbles",
        "SAFETY: boy looks beside sunset (not into sun); robot guides chin turn; hillside; empty speech bubbles",
        "ENDING: characters waving goodnight; big red sky; different poses from page 1; empty speech bubbles",
    ],
    "E-W03": [
        "THROUGH rainy window CLOSE glass with big drops; robot and boy reflections soft inside; empty speech bubbles",
        "GROUND-LEVEL: warm steam/vapor rising from sunny puddle; macro grass; characters distant; empty speech bubbles",
        "HIGH ABOVE clouds cool blue layer; airplane-tiny sense of height; empty speech bubbles",
        "INSIDE fluffy cloud cross-section: tiny droplets gathering; soft; empty speech bubbles",
        "CLOSE droplets merging bigger inside cloud; empty speech bubbles",
        "WIDE rain shafts hitting park path with splash rings; characters under umbrella walking; empty speech bubbles",
        "GARDEN CLOSE plants leaves with rain beads; boy crouches; robot measures with stick; empty speech bubbles",
        "RIVER rising after rain, bridge midground; characters on bridge looking down; empty speech bubbles",
        "BOOTS SPLASH big puddle foreground; low camera; joyful; empty speech bubbles",
        "DRY cracked earth thirsty contrast; soft concern; empty speech bubbles",
        "WATER-CYCLE loop arrows soft mural on classroom wall; characters point at mural; empty speech bubbles",
        "COZY ENDING couch cocoa; rain on window; indoor lamp; empty speech bubbles",
    ],
    "E-W04": [
        "WINDOW storm: gentle flash illuminates room; soft sound-wave rings outside; not scary; empty speech bubbles",
        "CLOUD CLOSE friendly cartoon lightning spark (rounded, soft yellow); empty speech bubbles",
        "DIAGRAM air heating lines around spark; empty speech bubbles",
        "EXPANDING shock rings in air like soft ripples; empty speech bubbles",
        "BOY covers ears playfully hearing boom; robot calm coach indoors; empty speech bubbles",
        "RACE metaphor track: yellow light beam finishes before blue sound wave; playful stadium soft; empty speech bubbles",
        "TIMELINE strip: flash icon then pause then boom icon; characters point at strip; empty speech bubbles",
        "BOY counts fingers after flash; porch; empty speech bubbles",
        "ROBOT holds soft round sign 'If thunder → inside'; empty speech bubbles",
        "ACTION: hurrying indoors through door; rain behind; empty speech bubbles",
        "INDOOR with grown-up; warm lamp; storm window; empty speech bubbles",
        "ENDING safe living room smiles; storm science book open; empty speech bubbles",
    ],
    "E-W05": [
        "WIDE snowfall night street lamps soft; characters catch flakes tongues out playful; empty speech bubbles",
        "INSIDE cold cloud: water droplets turning to ice sparkles; empty speech bubbles",
        "MACRO ice crystal growing like soft star; empty speech bubbles",
        "TWO crystals sticking into a flake; empty speech bubbles",
        "FLAKES drifting past camera in cold blue air; characters blurred behind; empty speech bubbles",
        "WARM pocket of air melting flake into drop mid-fall; empty speech bubbles",
        "DISPLAY board of different pretty flake patterns; museum-kid room; empty speech bubbles",
        "SPLIT: two flake journeys different paths side by side; empty speech bubbles",
        "QUIET winter field, flakes as crystal rain; distant tree line; empty speech bubbles",
        "SNOW blanket covering garden soil close; seeds sleeping soft icons; empty speech bubbles",
        "COSTUME change: boy hat+boots+mittens; robot scarf; porch; empty speech bubbles",
        "ENDING mitten close-up catching one flake; faces soft behind; empty speech bubbles",
    ],
}


def main() -> None:
    plan_path = Path("/Users/song/qwen3-tts/comic_batch/comics_plan_en_free_front5_w2.json")
    plan = json.loads(plan_path.read_text(encoding="utf-8"))
    prompts = []
    ref = "/Users/song/qwen3-tts/comic_batch/en_work/_raw_pilot/c-E-A01-01.jpg"
    for ep in plan:
        sid = ep["id"]
        if sid not in SCENES:
            continue
        assert len(SCENES[sid]) == 12
        for panel, scene in zip(ep["panels"], SCENES[sid]):
            panel["scene"] = scene
            prompts.append(
                {
                    "id": sid,
                    "i": panel["i"],
                    "filename": f"c-{sid}-{panel['i']:02d}.jpg",
                    "description": PREFIX + scene,
                    "ref": ref,
                }
            )
    plan_path.write_text(json.dumps(plan, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("updated", plan_path)

    # merge into main plan
    main_plan = Path("/Users/song/qwen3-tts/comic_batch/comics_plan_en_pilot12.json")
    if main_plan.exists():
        old = json.loads(main_plan.read_text(encoding="utf-8"))
        by = {e["id"]: e for e in old}
        for ep in plan:
            by[ep["id"]] = ep
        main_plan.write_text(json.dumps(list(by.values()), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    prompts_path = Path("/Users/song/qwen3-tts/comic_batch/en_work/free_front5_w2_prompts_varied.json")
    prompts_path.write_text(json.dumps(prompts, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("wrote", prompts_path, len(prompts))

    # also patch write_free_front5_wave2.py scenes in a sidecar for future
    sidecar = ROOT / "scripts" / "weather_scenes_varied.json"
    sidecar.write_text(json.dumps(SCENES, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("wrote", sidecar)


if __name__ == "__main__":
    main()
