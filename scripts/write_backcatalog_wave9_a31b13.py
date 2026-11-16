#!/usr/bin/env python3
"""Back-catalog wave 9: E-A31 E-A32 + Body E-B06…E-B13 → 12-page books. Owner sleeping; no questions."""
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
    "E-A31": {
        "title": "Why Do Hummingbirds Hover?",
        "folder": "Animals",
        "tag": "Hover",
        "companion": "girl",
        "pages": [
            'Wings blur. "How do they hang in the air?" Guangguang asks.',
            "Hummingbirds beat their wings in a special figure-eight path.",
            "That path makes lift on both the forward and back strokes.",
            "Most birds get lift mainly on the downstroke—hover needs both.",
            "Tiny strong muscles power hundreds of beats each second.",
            "Hovering lets them sip nectar while staying at the flower.",
            "They can also fly backward and sideways for careful sips.",
            "High-energy food from flowers fuels the busy wing work.",
            "Garden feeders help when placed clean and high enough.",
            "Watch softly—sudden moves can scare these tiny flyers.",
            "Never grab a hummingbird; eyes and quiet feet are enough.",
            "Figure-eight wings + fuel = floating flower visits.",
        ],
        "bubbles": [
            ("Wings blur!", "How hover?"),
            ("Figure-eight", "wing path."),
            ("Lift both", "strokes."),
            ("Other birds:", "mostly down."),
            ("Tiny muscles", "power beats."),
            ("Sip while", "staying."),
            ("Back and", "sideways too."),
            ("Nectar fuels", "wing work."),
            ("Clean feeder", "helps."),
            ("Watch soft—", "no scare."),
            ("Don't grab—", "just look."),
            ("Float sip", "science."),
        ],
        "scenes": [
            "WIDE soft garden hummingbird blur wings; girl and robot one-third; empty speech bubbles",
            "CLOSE wing figure-eight soft diagram; characters half frame; empty speech bubbles",
            "DIAGRAM-SOFT lift arrows both strokes; tiny figures; empty speech bubbles",
            "MEDIUM compare other bird flap soft; girl points; robot; empty speech bubbles",
            "CLOSE tiny strong chest muscles soft cartoon; characters half frame; empty speech bubbles",
            "ACTION hover at flower sipping soft; characters edge; empty speech bubbles",
            "PLAYFUL backward fly soft; characters half frame; empty speech bubbles",
            "MEDIUM nectar fuel soft flower; characters half frame; empty speech bubbles",
            "WIDE clean high feeder soft; characters one-third; empty speech bubbles",
            "CLOSE quiet watching soft; girl and robot half frame; empty speech bubbles",
            "CLOSE hands-off respect soft; robot nod; girl; half frame; empty speech bubbles",
            "ENDING girl and robot smile at soft hover; one-third; empty speech bubbles",
        ],
    },
    "E-A32": {
        "title": "Why Do Polar Bears Have White Fur?",
        "folder": "Animals",
        "tag": "Polar",
        "companion": "boy",
        "pages": [
            'White fur against snow. "Camouflage?" Max asks.',
            "Polar bear fur looks white, which helps them blend on ice.",
            "Each hair is mostly clear and hollow like a soft tube.",
            "Light scatters in the hollow hairs so we see white.",
            "Under the fur, skin is dark and helps hold warmth.",
            "Fat and fur coats keep heat in freezing winds.",
            "Big paws spread weight on snow like soft snowshoes.",
            "Hunting needs patience; white helps them stay less noticed.",
            "Climate and ice changes matter a lot for their homes.",
            "Learn and care—wild bears need distant respect always.",
            "Never approach a polar bear; watch films and museums instead.",
            "Hollow hairs, dark skin, thick coats: Arctic design.",
        ],
        "bubbles": [
            ("White fur!", "Camouflage?"),
            ("Blend on", "ice."),
            ("Hairs hollow", "clear tubes."),
            ("Light scatters", "looks white."),
            ("Dark skin", "holds warmth."),
            ("Fat fur", "coats."),
            ("Paws like", "snowshoes."),
            ("White helps", "hunt wait."),
            ("Ice homes", "matter."),
            ("Care from", "afar."),
            ("Don't approach—", "learn soft."),
            ("Arctic", "design."),
        ],
        "scenes": [
            "WIDE soft Arctic ice polar bear distant; boy and robot one-third; empty speech bubbles",
            "MEDIUM bear blend into snow soft; characters half frame; empty speech bubbles",
            "CLOSE hollow hair tube soft diagram; characters half frame; empty speech bubbles",
            "DIAGRAM-SOFT light scatter white look; tiny figures; empty speech bubbles",
            "CLOSE dark skin under fur soft cutaway; boy points; robot; empty speech bubbles",
            "WIDE windy ice thick coat soft; characters one-third; empty speech bubbles",
            "CLOSE big paw snowshoe soft; characters half frame; empty speech bubbles",
            "MEDIUM patient hunting distant soft not scary; characters edge; empty speech bubbles",
            "WIDE melting ice concern soft gentle; characters one-third; empty speech bubbles",
            "CLOSE respect distance soft; robot nod; boy; half frame; empty speech bubbles",
            "MEDIUM museum learning soft; boy and robot half frame; empty speech bubbles",
            "ENDING boy and robot wave from far soft; one-third; empty speech bubbles",
        ],
    },
    "E-B06": {
        "title": "Why Do We Wash Hands with Soap?",
        "folder": "Body",
        "tag": "Soap",
        "companion": "girl",
        "pages": [
            'Sink time! "Why soap, not only water?" asks Guangguang.',
            "Hands pick up tiny germs from doors, toys, and snacks.",
            "Water alone rinses some dirt but misses oily spots.",
            "Soap grabs oils and lifts germs so water can rinse them away.",
            "Bubbles help soap reach cracks around nails and fingers.",
            "Twenty seconds of scrubbing covers fronts, backs, and thumbs.",
            "Sing a short song while you scrub to mark the time.",
            "Rinse well, then dry—damp hands grab new germs faster.",
            "Wash before eating and after bathroom or pet play.",
            "Soap is a helper tool, not a scary chemical fight.",
            "Clean hands protect you and the people you hug.",
            "Soap + scrub + rinse + dry: tiny everyday science.",
        ],
        "bubbles": [
            ("Why soap?", "Not water?"),
            ("Hands pick", "up germs."),
            ("Water misses", "oily spots."),
            ("Soap lifts", "germs off."),
            ("Bubbles reach", "nail cracks."),
            ("Twenty seconds", "full scrub."),
            ("Sing while", "you scrub."),
            ("Rinse then", "dry."),
            ("Before eat,", "after potty."),
            ("Soap is a", "helper."),
            ("Protect you", "and hugs."),
            ("Soap scrub", "science."),
        ],
        "scenes": [
            "WIDE soft bathroom sink wash time; girl and robot one-third; empty speech bubbles",
            "CLOSE hands touching door toy soft; characters half frame; empty speech bubbles",
            "DIAGRAM-SOFT water vs soap oily spot; tiny figures; empty speech bubbles",
            "MEDIUM soap lifting germs soft cartoon friendly; girl points; robot; empty speech bubbles",
            "CLOSE bubbly fingers nails soft; characters half frame; empty speech bubbles",
            "ACTION twenty-second scrub soft; characters half frame; empty speech bubbles",
            "PLAYFUL singing scrub soft; girl and robot half frame; empty speech bubbles",
            "MEDIUM rinse and towel dry soft; characters half frame; empty speech bubbles",
            "WIDE before meal after pet soft montage; characters one-third; empty speech bubbles",
            "CLOSE friendly soap bottle helper soft; characters half frame; empty speech bubbles",
            "MEDIUM hug family soft clean hands; characters one-third; empty speech bubbles",
            "ENDING girl and robot thumbs-up clean hands; one-third; empty speech bubbles",
        ],
    },
    "E-B07": {
        "title": "Why Do Baby Teeth Fall Out?",
        "folder": "Body",
        "tag": "Teeth",
        "companion": "boy",
        "pages": [
            'A tooth wiggles. "Is it broken?" Guangguang worries.',
            "Baby teeth are starters that fit a smaller jaw.",
            "As you grow, adult teeth push up from underneath.",
            "Roots of baby teeth shrink so the tooth can loosen.",
            "Wiggling is often a sign the new tooth is ready.",
            "Losing teeth makes room for bigger chewing tools.",
            "Most kids lose teeth over several years, not all at once.",
            "Gentle brushing still matters for wiggly and new teeth.",
            "Do not yank hard—let the tooth leave when ready.",
            "If a tooth hurts a lot, ask a grown-up or dentist.",
            "A new smile grows one careful tooth at a time.",
            "Small starters make way for grown-up chewers.",
        ],
        "bubbles": [
            ("Tooth wiggle!", "Broken?"),
            ("Starter teeth", "for small jaws."),
            ("Adult teeth", "push up."),
            ("Roots shrink,", "tooth loosens."),
            ("Wiggle means", "almost ready."),
            ("Room for", "bigger teeth."),
            ("Over years,", "not all day."),
            ("Brush gentle", "always."),
            ("Don't yank—", "wait."),
            ("Hurt a lot?", "Tell grown-up."),
            ("New smile", "step by step."),
            ("Starters make", "way."),
        ],
        "scenes": [
            "WIDE soft mirror wiggle tooth; boy and robot one-third; empty speech bubbles",
            "DIAGRAM-SOFT small jaw baby teeth; tiny figures; empty speech bubbles",
            "CLOSE adult tooth rising soft under; characters half frame; empty speech bubbles",
            "MEDIUM root shrink soft diagram; boy points; robot; empty speech bubbles",
            "PLAYFUL gentle wiggle soft; characters half frame; empty speech bubbles",
            "WIDE bigger smile room soft; characters one-third; empty speech bubbles",
            "MEDIUM calendar years soft; characters half frame; empty speech bubbles",
            "CLOSE brushing wiggly tooth soft; boy and robot half frame; empty speech bubbles",
            "CLOSE no yank hands-off soft; robot shake; boy; empty speech bubbles",
            "MEDIUM tell grown-up soft; characters half frame; empty speech bubbles",
            "WIDE proud new gap smile soft; characters one-third; empty speech bubbles",
            "ENDING boy and robot cheer soft; one-third; empty speech bubbles",
        ],
    },
    "E-B08": {
        "title": "Why Do We Get Goosebumps?",
        "folder": "Body",
        "tag": "Bumps",
        "companion": "boy",
        "pages": [
            'Arms prickle. "Tiny bumps—why?" asks Guangguang.',
            "Goosebumps happen when tiny muscles at hair roots tighten.",
            "Cold can trigger the bumps to try to trap a little warmth.",
            "Long ago, fluffier fur would have puffed up more.",
            "People have thinner hair, so bumps look small now.",
            "Big feelings—awe, scare, music—can also flip the switch.",
            "Your body shares an old alert system with other animals.",
            "A sweater or warm hug often smooths cold bumps away.",
            "Scary movies can raise bumps even when you are safe.",
            "Bumps are a signal, not a sickness by themselves.",
            "Notice them, get cozy, and breathe if feelings feel big.",
            "Tiny muscles, old fur trick, modern soft reminders.",
        ],
        "bubbles": [
            ("Prickly arms!", "Why bumps?"),
            ("Tiny muscles", "tighten."),
            ("Cold tries", "trap warmth."),
            ("Old fur", "puffed more."),
            ("Our hair", "thinner now."),
            ("Feelings can", "flip switch."),
            ("Old alert", "system."),
            ("Sweater hug", "helps."),
            ("Safe scare", "still bumps."),
            ("Signal, not", "sickness."),
            ("Get cozy,", "breathe."),
            ("Old trick,", "soft now."),
        ],
        "scenes": [
            "WIDE soft chilly room arm bumps; boy and robot one-third; empty speech bubbles",
            "CLOSE hair root tiny muscle soft diagram; characters half frame; empty speech bubbles",
            "MEDIUM cold breeze soft; boy shivers; robot; empty speech bubbles",
            "DIAGRAM-SOFT fluffy animal fur puff soft; tiny figures; empty speech bubbles",
            "CLOSE human thin hair bumps soft; characters half frame; empty speech bubbles",
            "PLAYFUL music awe soft sparkles; characters half frame; empty speech bubbles",
            "WIDE animal alert soft friendly; characters one-third; empty speech bubbles",
            "MEDIUM sweater hug warm soft; boy and robot half frame; empty speech bubbles",
            "CLOSE movie couch safe bumps soft; characters half frame; empty speech bubbles",
            "DIAGRAM-SOFT signal not sickness; tiny figures; empty speech bubbles",
            "MEDIUM cozy breathe soft; characters half frame; empty speech bubbles",
            "ENDING boy and robot smile warm; one-third; empty speech bubbles",
        ],
    },
    "E-B09": {
        "title": "Why Do We Sneeze?",
        "folder": "Body",
        "tag": "Sneeze",
        "companion": "girl",
        "pages": [
            'Ah—choo! "Why sneeze?" Guangguang asks after a tissue.',
            "A sneeze is a fast blast that clears the nose path.",
            "Dust, pollen, or a tickle can wake sneeze sensors.",
            "Your body pushes air out to sweep the irritant away.",
            "Eyes may close for a blink during the big blast.",
            "Covering with a tissue or elbow keeps spray kinder.",
            "Some sneezes come with colds; some are just dust.",
            "Bright light makes a few people sneeze—a curious quirk.",
            "If sneezes keep coming, a grown-up can help check why.",
            "Hydration and clean air can calm a tickly nose.",
            "Sneezes are helpers, even when they interrupt stories.",
            "Sensors, blast, cover: nose cleanup in a flash.",
        ],
        "bubbles": [
            ("Ah-choo!", "Why sneeze?"),
            ("Fast blast", "clears nose."),
            ("Dust pollen", "tickle."),
            ("Air sweeps", "irritant."),
            ("Eyes blink", "in blast."),
            ("Tissue or", "elbow."),
            ("Cold or", "just dust."),
            ("Bright light", "quirk."),
            ("Many sneezes?", "Tell grown-up."),
            ("Clean air", "helps."),
            ("Sneezes are", "helpers."),
            ("Nose cleanup", "flash."),
        ],
        "scenes": [
            "WIDE soft living room tissue moment; girl and robot one-third; empty speech bubbles",
            "DIAGRAM-SOFT nose path clear blast; tiny figures; empty speech bubbles",
            "CLOSE dust pollen tickle soft; characters half frame; empty speech bubbles",
            "ACTION soft polite sneeze with tissue; girl; robot; empty speech bubbles",
            "CLOSE eyes blink soft; characters half frame; empty speech bubbles",
            "MEDIUM elbow cover soft; characters half frame; empty speech bubbles",
            "WIDE cold vs dusty room soft split; characters one-third; empty speech bubbles",
            "PLAYFUL sunny window sneeze quirk soft; characters half frame; empty speech bubbles",
            "MEDIUM tell grown-up soft; girl and robot half frame; empty speech bubbles",
            "CLOSE water and open window soft; characters half frame; empty speech bubbles",
            "WIDE story time interrupted giggle soft; characters one-third; empty speech bubbles",
            "ENDING girl and robot thumbs-up tissue; one-third; empty speech bubbles",
        ],
    },
    "E-B10": {
        "title": "Why Do I Have a Belly Button?",
        "folder": "Body",
        "tag": "Navel",
        "companion": "boy",
        "pages": [
            'Shirt up. "This button does nothing—why keep it?"',
            "Before birth, a cord brought food and oxygen to you.",
            "That cord connected to the place that is now your navel.",
            "After birth the cord is clamped and gently falls away.",
            "The healed spot becomes your belly button scar-soft mark.",
            "Innies and outies are both normal shapes of healing.",
            "The button is a reminder of how you grew, not a toy.",
            "Keep it clean like the rest of your skin in the bath.",
            "Doctors checked it when you were a tiny newborn.",
            "Every person who grew that way has a belly button story.",
            "It is quiet history written on your middle.",
            "Cord, heal, mark: your first delivery line.",
        ],
        "bubbles": [
            ("Belly button?", "Why keep?"),
            ("Cord brought", "food air."),
            ("Connected to", "this spot."),
            ("Cord falls", "away gently."),
            ("Healed soft", "mark."),
            ("Innie outie", "both ok."),
            ("Reminder,", "not a toy."),
            ("Keep clean", "in bath."),
            ("Doctors checked", "newborn."),
            ("Everyone has", "this story."),
            ("Quiet history", "middle."),
            ("Cord heal", "mark."),
        ],
        "scenes": [
            "WIDE soft kid showing belly button; boy and robot one-third; empty speech bubbles",
            "DIAGRAM-SOFT gentle cord to baby soft medical-friendly; tiny figures; empty speech bubbles",
            "CLOSE navel spot soft; characters half frame; empty speech bubbles",
            "MEDIUM cord clamp soft gentle hospital pastel; characters edge; empty speech bubbles",
            "CLOSE healed button soft; boy points; robot; empty speech bubbles",
            "PLAYFUL innie vs outie soft both happy; characters half frame; empty speech bubbles",
            "CLOSE not a toy hands soft; robot nod; empty speech bubbles",
            "MEDIUM bath clean soft; boy and robot half frame; empty speech bubbles",
            "WIDE newborn check soft pastel; characters one-third; empty speech bubbles",
            "MEDIUM friends all have buttons soft; characters one-third; empty speech bubbles",
            "CLOSE quiet proud middle soft; characters half frame; empty speech bubbles",
            "ENDING boy and robot smile soft; one-third; empty speech bubbles",
        ],
    },
    "E-B11": {
        "title": "Why Do We Have Skin?",
        "folder": "Body",
        "tag": "Skin",
        "companion": "girl",
        "pages": [
            '"Skin is just wrapping—right?" Guangguang taps softly.',
            "Skin is a living shield that keeps insides safely in.",
            "It blocks many germs and dirt from easy entry.",
            "Skin helps hold moisture so you do not dry out.",
            "Nerves in skin tell you hot, cold, soft, and ouch.",
            "Sweat glands help cool you when you run and play.",
            "Melanin pigment gives a range of beautiful skin tones.",
            "Cuts trigger a repair team of clotting and new cells.",
            "Gentle washing and lotion keep the shield comfortable.",
            "Sunscreen and shade protect skin on bright days.",
            "Your largest organ works quietly every minute.",
            "Shield, sense, cool, heal: skin does big jobs.",
        ],
        "bubbles": [
            ("Just wrapping?", "Nope."),
            ("Living shield", "keeps in."),
            ("Blocks germs", "and dirt."),
            ("Holds moisture", "in."),
            ("Nerves tell", "feelings."),
            ("Sweat helps", "cool."),
            ("Many beautiful", "tones."),
            ("Cuts start", "repair."),
            ("Wash lotion", "care."),
            ("Sun smart", "shade."),
            ("Biggest organ", "works."),
            ("Skin does", "big jobs."),
        ],
        "scenes": [
            "WIDE soft kid arm skin close friendly; girl and robot one-third; empty speech bubbles",
            "DIAGRAM-SOFT shield layer soft; tiny figures; empty speech bubbles",
            "CLOSE germs blocked soft cartoon; characters half frame; empty speech bubbles",
            "MEDIUM moisture soft glow; girl points; robot; empty speech bubbles",
            "CLOSE touch hot cold soft icons; characters half frame; empty speech bubbles",
            "ACTION running sweat cool soft; characters edge; empty speech bubbles",
            "WIDE diverse friends skin tones soft; characters one-third; empty speech bubbles",
            "MEDIUM bandage heal soft; characters half frame; empty speech bubbles",
            "CLOSE wash and lotion soft; girl and robot half frame; empty speech bubbles",
            "WIDE sunny park sunscreen soft; characters one-third; empty speech bubbles",
            "PLAYFUL organ crown soft joke; characters half frame; empty speech bubbles",
            "ENDING girl and robot gentle high-five; one-third; empty speech bubbles",
        ],
    },
    "E-B12": {
        "title": "Why Do Muscles Get Sore After Exercise?",
        "folder": "Body",
        "tag": "Sore",
        "companion": "boy",
        "pages": [
            'Stairs hurt tomorrow. "Did I break my legs?"',
            "Hard play makes tiny muscle fiber repairs begin.",
            "Soreness often peaks a day later as rebuilding starts.",
            "Your body reinforces muscles so next time feels easier.",
            "This delayed ache is common after new or big efforts.",
            "Gentle movement, water, and sleep help recovery.",
            "Stretching softly can feel nice but is not magic alone.",
            "Sharp sudden pain is different—tell a grown-up then.",
            "Rest days let the rebuild finish its quiet work.",
            "Stronger muscles are a gift from careful practice.",
            "Soreness means remodel, not that you failed.",
            "Work, tiny repair, stronger: workout science.",
        ],
        "bubbles": [
            ("Stairs hurt!", "Broken?"),
            ("Tiny fiber", "repairs."),
            ("Aches peak", "next day."),
            ("Rebuild makes", "stronger."),
            ("Common after", "big effort."),
            ("Water sleep", "help."),
            ("Soft stretch", "feels nice."),
            ("Sharp pain?", "Tell grown-up."),
            ("Rest days", "matter."),
            ("Practice gift:", "strength."),
            ("Remodel, not", "failure."),
            ("Work repair", "stronger."),
        ],
        "scenes": [
            "WIDE soft playground tired legs; boy and robot one-third; empty speech bubbles",
            "DIAGRAM-SOFT muscle fiber tiny repair; tiny figures; empty speech bubbles",
            "MEDIUM next-day calendar ache soft; characters half frame; empty speech bubbles",
            "PLAYFUL stronger arms soft glow; boy flex gentle; robot; empty speech bubbles",
            "WIDE new sport first time soft; characters one-third; empty speech bubbles",
            "CLOSE water bottle sleep soft; characters half frame; empty speech bubbles",
            "MEDIUM gentle stretch soft; boy and robot half frame; empty speech bubbles",
            "CLOSE sharp pain tell grown-up soft; characters half frame; empty speech bubbles",
            "WIDE rest day couch soft; characters one-third; empty speech bubbles",
            "ACTION careful practice soft; characters edge; empty speech bubbles",
            "MEDIUM thumbs-up remodel soft; characters half frame; empty speech bubbles",
            "ENDING boy and robot stretch-smile; one-third; empty speech bubbles",
        ],
    },
    "E-B13": {
        "title": "Why Do We Have Two Kidneys?",
        "folder": "Body",
        "tag": "Kidneys",
        "companion": "girl",
        "pages": [
            '"Two filters—why not one?" Guangguang peeks at a diagram.',
            "Kidneys clean blood and balance water and salts.",
            "They make urine to carry wastes out safely.",
            "Two kidneys give backup if one needs extra rest.",
            "Many people live well with one healthy kidney.",
            "Still, two give capacity for growth, play, and illness days.",
            "Blood flows in; cleaned blood flows back out.",
            "Drinking water helps kidneys do their quiet job.",
            "Foods and medicines also pass through kidney care.",
            "Protect them: helmets, seat belts, and grown-up guidance.",
            "You cannot see them, but they work every hour.",
            "Twin filters, backup plan, everyday clean-up crew.",
        ],
        "bubbles": [
            ("Two filters?", "Why?"),
            ("Clean blood,", "balance water."),
            ("Urine carries", "wastes out."),
            ("Backup if", "one rests."),
            ("One can work", "well too."),
            ("Two help", "busy days."),
            ("Blood in,", "clean out."),
            ("Water helps", "the job."),
            ("Food medicine", "pass through."),
            ("Protect with", "safety."),
            ("Quiet hourly", "work."),
            ("Twin cleanup", "crew."),
        ],
        "scenes": [
            "WIDE soft anatomy poster kid-friendly; girl and robot one-third; empty speech bubbles",
            "DIAGRAM-SOFT two kidney filters soft; tiny figures; empty speech bubbles",
            "CLOSE waste out path soft not gross; characters half frame; empty speech bubbles",
            "PLAYFUL backup twin idea soft; girl points; robot; empty speech bubbles",
            "MEDIUM one kidney ok soft; characters half frame; empty speech bubbles",
            "WIDE play run capacity soft; characters one-third; empty speech bubbles",
            "DIAGRAM-SOFT blood in clean out arrows; tiny figures; empty speech bubbles",
            "CLOSE water bottle help soft; girl and robot half frame; empty speech bubbles",
            "MEDIUM meal and medicine soft; characters half frame; empty speech bubbles",
            "CLOSE helmet seatbelt protect soft; characters half frame; empty speech bubbles",
            "WIDE clock quiet work soft; characters one-third; empty speech bubbles",
            "ENDING girl and robot salute soft filters; one-third; empty speech bubbles",
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
        assert len(st["pages"]) == 12 and len(st["bubbles"]) == 12 and len(st["scenes"]) == 12
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

    plan_path = Path("/Users/song/qwen3-tts/comic_batch/comics_plan_en_backcatalog_w9.json")
    plan_path.write_text(json.dumps(plan, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("wrote", plan_path)

    raw_dir = Path("/Users/song/qwen3-tts/comic_batch/en_work/_raw_backcatalog_w9")
    raw_dir.mkdir(parents=True, exist_ok=True)
    prompts_path = Path("/Users/song/qwen3-tts/comic_batch/en_work/backcatalog_w9_prompts.json")
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
