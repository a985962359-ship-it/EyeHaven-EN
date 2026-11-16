#!/usr/bin/env python3
"""Back-catalog wave 27: Safety E-Z14…E-Z24 → 12-page books. Owner sleeping; no questions."""
from __future__ import annotations

import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PREFIX_BOY = (
    "Children's picture book comic panel, soft warm friendly safety lighting, landscape 4:3. "
    "Cute round-headed white robot Guangguang with green trim, warm glowing chest lamp, small star on head, honest smile. "
    "Blonde boy about 6 years old with freckles wearing a blue T-rex hoodie with white sleeve stripes. "
    "Two large empty white oval speech bubbles with space for short kids text, blank inside, no letters. "
    "Soft friendly kid safety, gentle pastel, not scary. No text logos, consistent character design. "
    "Simple readable background, big clear shapes, shallow depth, soft edges, no clutter. "
)
PREFIX_GIRL = (
    "Children's picture book comic panel, soft warm friendly safety lighting, landscape 4:3. "
    "Cute round-headed white robot Guangguang with green trim, warm glowing chest lamp, small star on head, honest smile. "
    "Gentle girl about 6–7 with soft sweater and kind smile. "
    "Two large empty white oval speech bubbles with space for short kids text, blank inside, no letters. "
    "Soft friendly kid safety, gentle pastel, not scary. No text logos, consistent character design. "
    "Simple readable background, big clear shapes, shallow depth, soft edges, no clutter. "
)

STORIES = {
    "E-Z14": {
        "title": "Hold a Grown-Up’s Hand",
        "folder": "Safety",
        "tag": "Hand",
        "companion": "girl",
        "pages": [
            'Busy sidewalk. "Hold a grown-up’s hand," says Mia.',
            "Hands keep you close when crowds move fast.",
            "Parking lots need hand-holding too.",
            "If you let go, freeze and call their name calmly.",
            "Meeting spots help if you get separated.",
            "Strollers and carts are not climbing gyms.",
            "Squeeze once means “I’m here.”",
            "Grown-ups watch cars; you watch the hand.",
            "Ask before wandering to a toy shelf.",
            "Together feet are safer feet.",
            "Practice the freeze-and-call plan together.",
            "Hand link: outing safety.",
        ],
        "bubbles": [
            ("Busy walk!", "Hold hand."),
            ("Hands keep", "you close."),
            ("Parking lots", "too."),
            ("Let go? Freeze,", "call name."),
            ("Meeting spots", "help."),
            ("No climbing", "carts."),
            ("Squeeze means", "I’m here."),
            ("Watch the", "hand."),
            ("Ask before", "wandering."),
            ("Together feet", "safer."),
            ("Practice plan", "together."),
            ("Outing", "safety."),
        ],
        "scenes": [
            "WIDE soft busy sidewalk hold hand; girl and robot one-third; empty speech bubbles",
            "CLOSE hands keep close soft; girl points; robot; empty speech bubbles",
            "MEDIUM parking lot soft; characters half frame; empty speech bubbles",
            "PLAYFUL freeze call soft; characters half frame; empty speech bubbles",
            "WIDE meeting spot soft; characters one-third; empty speech bubbles",
            "CLOSE no climb cart soft; characters half frame; empty speech bubbles",
            "MEDIUM squeeze I’m here soft; characters half frame; empty speech bubbles",
            "PLAYFUL watch hand soft; characters half frame; empty speech bubbles",
            "CLOSE ask before wander soft; characters half frame; empty speech bubbles",
            "DIAGRAM-SOFT together feet soft; tiny figures; empty speech bubbles",
            "MEDIUM practice plan soft; girl and robot half frame; empty speech bubbles",
            "ENDING girl and robot soft smile; one-third; empty speech bubbles",
        ],
    },
    "E-Z15": {
        "title": "Bike Helmet On",
        "folder": "Safety",
        "tag": "Helmet",
        "companion": "boy",
        "pages": [
            'Max clips a helmet. "Helmet on before wheels."',
            "Helmets protect your head if you tip.",
            "Straps snug under the chin—two fingers fit.",
            "Helmet sits level, not tipped back.",
            "Scooters and skateboards need helmets too.",
            "Crack in a helmet? Ask for a new one.",
            "Friends who wait while you buckle are kind.",
            "Bright helmets help drivers see you.",
            "Rules at parks often require helmets.",
            "Buckle first, then ride.",
            "Check the chin strap with a grown-up.",
            "Head guard: bike safety.",
        ],
        "bubbles": [
            ("Helmet clip!", "Before wheels."),
            ("Protects your", "head."),
            ("Snug chin", "strap."),
            ("Level, not", "tipped."),
            ("Scooters need", "helmets too."),
            ("Crack? Get", "new one."),
            ("Friends wait", "kindly."),
            ("Bright helps", "drivers see."),
            ("Park rules", "often."),
            ("Buckle first,", "then ride."),
            ("Check strap", "together."),
            ("Bike", "safety."),
        ],
        "scenes": [
            "WIDE soft driveway helmet bike; boy and robot one-third; empty speech bubbles",
            "DIAGRAM-SOFT protect head soft; tiny figures; empty speech bubbles",
            "CLOSE chin strap soft; boy points; robot; empty speech bubbles",
            "MEDIUM level helmet soft; characters half frame; empty speech bubbles",
            "PLAYFUL scooter helmet soft; characters half frame; empty speech bubbles",
            "WIDE crack ask new soft; characters one-third; empty speech bubbles",
            "CLOSE friends wait soft; characters half frame; empty speech bubbles",
            "MEDIUM bright helmet soft; characters half frame; empty speech bubbles",
            "PLAYFUL park rules soft; characters half frame; empty speech bubbles",
            "DIAGRAM-SOFT buckle first soft; tiny figures; empty speech bubbles",
            "MEDIUM check strap soft; boy and robot half frame; empty speech bubbles",
            "ENDING boy and robot soft smile; one-third; empty speech bubbles",
        ],
    },
    "E-Z16": {
        "title": "Stay Where a Grown-Up Can See",
        "folder": "Safety",
        "tag": "Sight",
        "companion": "girl",
        "pages": [
            'Playground edge. "Stay where a grown-up can see."',
            "If they can see you, they can help faster.",
            "Agree on a play zone before you run.",
            "Behind buildings and parking rows are out.",
            "Wave if you move to a new spot.",
            "Bathrooms: go with a grown-up plan.",
            "Hide-and-seek needs clear home-base rules.",
            "Evening darker? Stay even closer.",
            "Checking in is brave, not babyish.",
            "Being seen means staying safer.",
            "Pick a home-base tree together.",
            "In sight: play safety.",
        ],
        "bubbles": [
            ("Playground!", "Stay in sight."),
            ("Seen means", "faster help."),
            ("Agree on a", "play zone."),
            ("No parking", "rows."),
            ("Wave if you", "move."),
            ("Bathroom with", "a plan."),
            ("Hide-seek needs", "home base."),
            ("Darker? Stay", "closer."),
            ("Checking in is", "brave."),
            ("Seen =", "safer."),
            ("Pick home base", "together."),
            ("Play", "safety."),
        ],
        "scenes": [
            "WIDE soft playground in sight; girl and robot one-third; empty speech bubbles",
            "CLOSE seen faster help soft; girl points; robot; empty speech bubbles",
            "MEDIUM play zone soft; characters half frame; empty speech bubbles",
            "PLAYFUL no parking rows soft; characters half frame; empty speech bubbles",
            "WIDE wave new spot soft; characters one-third; empty speech bubbles",
            "CLOSE bathroom plan soft; characters half frame; empty speech bubbles",
            "MEDIUM home base soft; characters half frame; empty speech bubbles",
            "PLAYFUL darker closer soft; characters half frame; empty speech bubbles",
            "CLOSE checking in brave soft; characters half frame; empty speech bubbles",
            "DIAGRAM-SOFT seen safer soft; tiny figures; empty speech bubbles",
            "MEDIUM pick home base soft; girl and robot half frame; empty speech bubbles",
            "ENDING girl and robot soft smile; one-third; empty speech bubbles",
        ],
    },
    "E-Z17": {
        "title": "Strangers Are Not Instant Friends",
        "folder": "Safety",
        "tag": "Stranger",
        "companion": "boy",
        "pages": [
            'Park bench chat. "Strangers aren’t instant friends."',
            "Kind voices can still be people you don’t know.",
            "Never leave with someone your grown-up didn’t plan.",
            "Gifts or puppies are not reasons to go alone.",
            "Trusted adults wear agreed jobs or name tags sometimes.",
            "If unsure, find your grown-up first.",
            "Police helpers: you can ask to wait together.",
            "Your body belongs to you—space is okay.",
            "Code words with family can help check plans.",
            "Known plan > new invitation.",
            "Practice a polite “no, I need my grown-up.”",
            "People smart: stranger safety.",
        ],
        "bubbles": [
            ("Park chat!", "Not instant friends."),
            ("Kind ≠", "known."),
            ("Don’t leave", "unplanned."),
            ("Gifts aren’t", "tickets."),
            ("Trusted have", "plans."),
            ("Unsure? Find", "grown-up."),
            ("Wait with", "helpers."),
            ("Your body,", "your space."),
            ("Family code", "words."),
            ("Known plan", "wins."),
            ("Practice polite", "no."),
            ("People", "safety."),
        ],
        "scenes": [
            "WIDE soft park with grown-up nearby; boy and robot one-third; empty speech bubbles",
            "DIAGRAM-SOFT kind not known soft; tiny figures; empty speech bubbles",
            "CLOSE don’t leave unplanned soft; boy points; robot; empty speech bubbles",
            "MEDIUM gifts not tickets soft; characters half frame; empty speech bubbles",
            "PLAYFUL trusted plan soft; characters half frame; empty speech bubbles",
            "WIDE find grown-up soft; characters one-third; empty speech bubbles",
            "CLOSE wait helpers soft; characters half frame; empty speech bubbles",
            "MEDIUM body space soft; characters half frame; empty speech bubbles",
            "PLAYFUL code words soft; characters half frame; empty speech bubbles",
            "DIAGRAM-SOFT known plan soft; tiny figures; empty speech bubbles",
            "MEDIUM practice no soft; boy and robot half frame; empty speech bubbles",
            "ENDING boy and robot soft smile; one-third; empty speech bubbles",
        ],
    },
    "E-Z18": {
        "title": "Say No and Find a Trusted Adult",
        "folder": "Safety",
        "tag": "SayNo",
        "companion": "girl",
        "pages": [
            'Mia stands tall. "Say no and find a trusted adult."',
            "No is a complete sentence when you feel unsafe.",
            "Yell, move away, and look for a helper.",
            "Teachers, cashiers, and parents can be trusted adults.",
            "You don’t need to be polite to danger.",
            "Tell what happened even if it feels awkward.",
            "Friends support you by going with you to an adult.",
            "Secrets that scare you should not stay secret.",
            "Practice a loud clear “No!” at home.",
            "Voice + feet + trusted adult.",
            "Name three trusted adults together.",
            "Brave no: personal safety.",
        ],
        "bubbles": [
            ("Stand tall!", "Say no."),
            ("No is", "enough."),
            ("Yell move", "find help."),
            ("Trusted adults", "help."),
            ("Polite not for", "danger."),
            ("Tell what", "happened."),
            ("Friends go with", "you."),
            ("Scary secrets", "tell."),
            ("Practice loud", "No."),
            ("Voice feet", "adult."),
            ("Name three", "adults."),
            ("Personal", "safety."),
        ],
        "scenes": [
            "WIDE soft home practice stand tall; girl and robot one-third; empty speech bubbles",
            "CLOSE no is enough soft; girl points; robot; empty speech bubbles",
            "MEDIUM yell move help soft; characters half frame; empty speech bubbles",
            "PLAYFUL trusted adults soft; characters half frame; empty speech bubbles",
            "WIDE not polite danger soft; characters one-third; empty speech bubbles",
            "CLOSE tell happened soft; characters half frame; empty speech bubbles",
            "MEDIUM friends support soft; characters half frame; empty speech bubbles",
            "PLAYFUL scary secrets tell soft; characters half frame; empty speech bubbles",
            "CLOSE practice loud no soft; characters half frame; empty speech bubbles",
            "DIAGRAM-SOFT voice feet adult soft; tiny figures; empty speech bubbles",
            "MEDIUM name three soft; girl and robot half frame; empty speech bubbles",
            "ENDING girl and robot soft smile; one-third; empty speech bubbles",
        ],
    },
    "E-Z19": {
        "title": "Passwords Stay Private",
        "folder": "Safety",
        "tag": "Password",
        "companion": "boy",
        "pages": [
            'Tablet login. "Passwords stay private," says Max.',
            "A password is a secret key for your accounts.",
            "Share only with a parent who helps you set it.",
            "Friends at school don’t need your key.",
            "Don’t type passwords where strangers can watch.",
            "Grown-ups help pick strong, rememberable ideas.",
            "If someone asks for your password, tell a parent.",
            "Lock the screen when you walk away.",
            "Apps and games still need private keys.",
            "Private key = private.",
            "Practice locking the screen together.",
            "Key keep: password safety.",
        ],
        "bubbles": [
            ("Tablet login!", "Private."),
            ("Password is a", "secret key."),
            ("Share only with", "parent."),
            ("Friends don’t", "need it."),
            ("No watching", "while typing."),
            ("Grown-ups help", "choose."),
            ("Someone asks?", "Tell parent."),
            ("Lock screen", "when leave."),
            ("Games need", "private keys."),
            ("Private key", "stays private."),
            ("Practice lock", "together."),
            ("Password", "safety."),
        ],
        "scenes": [
            "WIDE soft couch tablet login; boy and robot one-third; empty speech bubbles",
            "DIAGRAM-SOFT secret key soft; tiny figures; empty speech bubbles",
            "CLOSE share with parent soft; boy points; robot; empty speech bubbles",
            "MEDIUM friends don’t need soft; characters half frame; empty speech bubbles",
            "PLAYFUL no watching type soft; characters half frame; empty speech bubbles",
            "WIDE grown-up choose soft; characters one-third; empty speech bubbles",
            "CLOSE tell parent soft; characters half frame; empty speech bubbles",
            "MEDIUM lock screen soft; characters half frame; empty speech bubbles",
            "PLAYFUL games private soft; characters half frame; empty speech bubbles",
            "DIAGRAM-SOFT private stays soft; tiny figures; empty speech bubbles",
            "MEDIUM practice lock soft; boy and robot half frame; empty speech bubbles",
            "ENDING boy and robot soft smile; one-third; empty speech bubbles",
        ],
    },
    "E-Z20": {
        "title": "Ask Before Clicking Links",
        "folder": "Safety",
        "tag": "Links",
        "companion": "girl",
        "pages": [
            'A bright button pops up. "Ask before clicking."',
            "Links can look fun but lead to unknown places.",
            "Pop-ups promising prizes need a grown-up check.",
            "Don’t download unless a parent says yes.",
            "If a message feels weird, show an adult.",
            "Friends’ accounts can be copied—still ask.",
            "Close the tab with help if you’re unsure.",
            "Safe sites are ones your family chooses.",
            "Curiosity plus a pause keeps you safer.",
            "Pause → ask → then maybe click.",
            "Practice showing a fake pop-up to a grown-up.",
            "Click pause: online safety.",
        ],
        "bubbles": [
            ("Bright button!", "Ask first."),
            ("Links can go", "unknown."),
            ("Prize pop-ups?", "Check adult."),
            ("Downloads need", "yes."),
            ("Weird message?", "Show adult."),
            ("Copied accounts", "still ask."),
            ("Unsure? Close", "with help."),
            ("Family chooses", "safe sites."),
            ("Curiosity plus", "pause."),
            ("Pause ask", "maybe click."),
            ("Show pop-up", "together."),
            ("Online", "safety."),
        ],
        "scenes": [
            "WIDE soft desk tablet pop-up; girl and robot one-third; empty speech bubbles",
            "DIAGRAM-SOFT unknown link soft; tiny figures; empty speech bubbles",
            "CLOSE prize pop-up soft; girl points; robot; empty speech bubbles",
            "MEDIUM download ask soft; characters half frame; empty speech bubbles",
            "PLAYFUL weird message soft; characters half frame; empty speech bubbles",
            "WIDE still ask soft; characters one-third; empty speech bubbles",
            "CLOSE close with help soft; characters half frame; empty speech bubbles",
            "MEDIUM family safe sites soft; characters half frame; empty speech bubbles",
            "PLAYFUL curiosity pause soft; characters half frame; empty speech bubbles",
            "DIAGRAM-SOFT pause ask click soft; tiny figures; empty speech bubbles",
            "MEDIUM show pop-up soft; girl and robot half frame; empty speech bubbles",
            "ENDING girl and robot soft smile; one-third; empty speech bubbles",
        ],
    },
    "E-Z21": {
        "title": "Wash Hands Before Eating",
        "folder": "Safety",
        "tag": "Hands",
        "companion": "boy",
        "pages": [
            'Sink time. "Wash hands before eating," sings Max.',
            "Soap and water lift invisible germ hitchhikers.",
            "Sing a short song while you scrub all sides.",
            "Rinse and dry with a clean towel or air.",
            "After bathroom and pets, wash again.",
            "Hand gel helps when sinks are far—ask first.",
            "Nails and thumbs need love too.",
            "Sharing snacks is nicer with clean hands.",
            "Cough into elbow, then wash when you can.",
            "Clean hands → ready plate.",
            "Time a twenty-second wash together.",
            "Soap pause: hand safety.",
        ],
        "bubbles": [
            ("Sink time!", "Wash first."),
            ("Soap lifts", "germs."),
            ("Sing while you", "scrub."),
            ("Rinse and", "dry."),
            ("After bathroom", "pets too."),
            ("Gel if sink", "far."),
            ("Nails thumbs", "too."),
            ("Clean hands,", "share snacks."),
            ("Elbow cough,", "then wash."),
            ("Clean hands,", "ready plate."),
            ("Twenty seconds", "together."),
            ("Hand", "safety."),
        ],
        "scenes": [
            "WIDE soft bathroom sink wash; boy and robot one-third; empty speech bubbles",
            "DIAGRAM-SOFT soap lifts germs soft; tiny figures; empty speech bubbles",
            "CLOSE scrub all sides soft; boy points; robot; empty speech bubbles",
            "MEDIUM rinse dry soft; characters half frame; empty speech bubbles",
            "PLAYFUL after pets soft; characters half frame; empty speech bubbles",
            "WIDE hand gel soft; characters one-third; empty speech bubbles",
            "CLOSE nails thumbs soft; characters half frame; empty speech bubbles",
            "MEDIUM share snacks soft; characters half frame; empty speech bubbles",
            "PLAYFUL elbow cough soft; characters half frame; empty speech bubbles",
            "DIAGRAM-SOFT clean ready plate soft; tiny figures; empty speech bubbles",
            "MEDIUM twenty seconds soft; boy and robot half frame; empty speech bubbles",
            "ENDING boy and robot soft smile; one-third; empty speech bubbles",
        ],
    },
    "E-Z22": {
        "title": "Swim Only With a Grown-Up",
        "folder": "Safety",
        "tag": "Swim",
        "companion": "girl",
        "pages": [
            'Pool edge. "Swim only with a grown-up."',
            "Water is fun and needs watching eyes.",
            "Floaties help but don’t replace a grown-up.",
            "No running on wet decks—slips hurt.",
            "Ask before going deeper than your chest.",
            "If tired, rest on the wall or steps.",
            "Buddy systems work with adult eyes too.",
            "Lakes and oceans have currents—stay close.",
            "Emergency whistle or shout brings help.",
            "Water + grown-up = swim yes.",
            "Agree on the shallow zone together.",
            "Pool rules: water safety.",
        ],
        "bubbles": [
            ("Pool edge!", "With grown-up."),
            ("Fun needs", "watching eyes."),
            ("Floaties ≠", "alone."),
            ("No running", "wet decks."),
            ("Ask before", "deeper."),
            ("Tired? Rest", "on wall."),
            ("Buddy plus", "adult eyes."),
            ("Currents: stay", "close."),
            ("Shout brings", "help."),
            ("Water + adult", "yes."),
            ("Agree shallow", "zone."),
            ("Water", "safety."),
        ],
        "scenes": [
            "WIDE soft pool edge grown-up; girl and robot one-third; empty speech bubbles",
            "CLOSE watching eyes soft; girl points; robot; empty speech bubbles",
            "MEDIUM floaties not alone soft; characters half frame; empty speech bubbles",
            "PLAYFUL no running deck soft; characters half frame; empty speech bubbles",
            "WIDE ask before deeper soft; characters one-third; empty speech bubbles",
            "CLOSE rest on wall soft; characters half frame; empty speech bubbles",
            "MEDIUM buddy adult soft; characters half frame; empty speech bubbles",
            "PLAYFUL lake stay close soft; characters half frame; empty speech bubbles",
            "CLOSE shout help soft; characters half frame; empty speech bubbles",
            "DIAGRAM-SOFT water adult yes soft; tiny figures; empty speech bubbles",
            "MEDIUM shallow zone soft; girl and robot half frame; empty speech bubbles",
            "ENDING girl and robot soft smile; one-third; empty speech bubbles",
        ],
    },
    "E-Z23": {
        "title": "Wear Sunscreen Outside",
        "folder": "Safety",
        "tag": "Sun",
        "companion": "boy",
        "pages": [
            'Sunny yard. "Wear sunscreen outside," says Max.',
            "Sun can pink skin even on cool breezy days.",
            "Grown-ups help rub cream on ears and nose.",
            "Hats and shade add extra kindness.",
            "Reapply after swimming or long play.",
            "Cloudy skies can still send strong light.",
            "Sunglasses help eyes on bright beaches.",
            "Dark clothes can add a little cover.",
            "If skin feels hot, seek shade and water.",
            "Cover + cream = sun care.",
            "Do a sunscreen checklist before going out.",
            "Sun smart: outdoor safety.",
        ],
        "bubbles": [
            ("Sunny yard!", "Sunscreen."),
            ("Can pink skin", "even cool."),
            ("Ears nose need", "cream."),
            ("Hats shade", "help."),
            ("Reapply after", "swim."),
            ("Clouds still", "bright."),
            ("Sunglasses for", "eyes."),
            ("Clothes add", "cover."),
            ("Hot skin? Shade", "water."),
            ("Cover plus", "cream."),
            ("Checklist before", "out."),
            ("Sun", "safety."),
        ],
        "scenes": [
            "WIDE soft sunny yard sunscreen; boy and robot one-third; empty speech bubbles",
            "DIAGRAM-SOFT sun pink skin soft; tiny figures; empty speech bubbles",
            "CLOSE ears nose cream soft; boy points; robot; empty speech bubbles",
            "MEDIUM hat shade soft; characters half frame; empty speech bubbles",
            "PLAYFUL reapply after swim soft; characters half frame; empty speech bubbles",
            "WIDE cloudy still bright soft; characters one-third; empty speech bubbles",
            "CLOSE sunglasses soft; characters half frame; empty speech bubbles",
            "MEDIUM clothes cover soft; characters half frame; empty speech bubbles",
            "PLAYFUL shade water soft; characters half frame; empty speech bubbles",
            "DIAGRAM-SOFT cover cream soft; tiny figures; empty speech bubbles",
            "MEDIUM checklist soft; boy and robot half frame; empty speech bubbles",
            "ENDING boy and robot soft smile; one-third; empty speech bubbles",
        ],
    },
    "E-Z24": {
        "title": "Tell an Adult If Something Hurts",
        "folder": "Safety",
        "tag": "Hurts",
        "companion": "girl",
        "pages": [
            'Mia holds a scraped knee. "Tell an adult if it hurts."',
            "Pain is a message your body sends.",
            "Small scrapes still deserve clean care.",
            "Big hurts or dizziness need fast grown-up help.",
            "You won’t get in trouble for telling the truth.",
            "Point to where it hurts with simple words.",
            "Ice packs and bandages are adult tools.",
            "Feelings can hurt too—say that out loud.",
            "Teachers and coaches count as adults who help.",
            "Early tell → faster comfort.",
            "Practice “My ___ hurts” sentences together.",
            "Speak up: body safety.",
        ],
        "bubbles": [
            ("Scraped knee!", "Tell adult."),
            ("Pain is a", "message."),
            ("Small scrapes", "need care."),
            ("Big hurts need", "fast help."),
            ("Truth is", "okay."),
            ("Point and use", "words."),
            ("Ice bandage", "adults."),
            ("Feelings can", "hurt too."),
            ("Teachers help", "also."),
            ("Early tell,", "faster care."),
            ("Practice sentences", "together."),
            ("Body", "safety."),
        ],
        "scenes": [
            "WIDE soft park scraped knee; girl and robot one-third; empty speech bubbles",
            "DIAGRAM-SOFT pain message soft; tiny figures; empty speech bubbles",
            "CLOSE small scrape care soft; girl points; robot; empty speech bubbles",
            "MEDIUM big hurt help soft; characters half frame; empty speech bubbles",
            "PLAYFUL truth okay soft; characters half frame; empty speech bubbles",
            "WIDE point words soft; characters one-third; empty speech bubbles",
            "CLOSE ice bandage soft; characters half frame; empty speech bubbles",
            "MEDIUM feelings hurt soft; characters half frame; empty speech bubbles",
            "PLAYFUL teacher help soft; characters half frame; empty speech bubbles",
            "DIAGRAM-SOFT early tell soft; tiny figures; empty speech bubbles",
            "MEDIUM practice sentences soft; girl and robot half frame; empty speech bubbles",
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
    ref_dir = ROOT / ".comic_refs" / "w27_by_story"
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

    Path("/Users/song/qwen3-tts/comic_batch/comics_plan_en_backcatalog_w27.json").write_text(
        json.dumps(plan, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    Path("/Users/song/qwen3-tts/comic_batch/en_work/_raw_backcatalog_w27").mkdir(parents=True, exist_ok=True)
    Path("/Users/song/qwen3-tts/comic_batch/en_work/backcatalog_w27_prompts.json").write_text(
        json.dumps(prompts, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    bubbles_path = ROOT / "EyeHaven" / "ComicBubbleWords.en.json"
    bubbles = json.loads(bubbles_path.read_text(encoding="utf-8"))
    for sid, st in STORIES.items():
        bubbles[sid] = [{"i": i, "left": L, "right": R} for i, (L, R) in enumerate(st["bubbles"], 1)]
    bubbles_path.write_text(json.dumps(bubbles, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("wave27 done", len(STORIES), "prompts", len(prompts))


if __name__ == "__main__":
    main()
