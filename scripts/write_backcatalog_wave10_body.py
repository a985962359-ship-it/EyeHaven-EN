#!/usr/bin/env python3
"""Back-catalog wave 10: Body E-B14…E-B21 → 12-page books. Owner sleeping; no questions."""
from __future__ import annotations
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
PREFIX_BOY = "Children's picture book comic panel, soft warm friendly lighting, landscape 4:3. Cute round-headed white robot Guangguang with green trim, warm glowing chest lamp, small star on head, honest smile. Blonde boy about 6 years old wearing a blue T-rex hoodie. Two large empty white oval speech bubbles with space for short kids text, blank inside, no letters. No scary imagery, no text logos, consistent character design. Simple readable background, big clear shapes, shallow depth, soft edges, no clutter. "
PREFIX_GIRL = "Children's picture book comic panel, soft warm friendly lighting, landscape 4:3. Cute round-headed white robot Guangguang with green trim, warm glowing chest lamp, small star on head, honest smile. Gentle girl about 6–7 with soft sweater and kind smile. Two large empty white oval speech bubbles with space for short kids text, blank inside, no letters. No scary imagery, no text logos, consistent character design. Simple readable background, big clear shapes, shallow depth, soft edges, no clutter. "
STORIES = {
 'E-B14': {
  "title": 'Why Does My Stomach Growl?', "folder": 'Body', "tag": 'Growl', "companion": 'boy',
  "pages": ['Rumble! "Is a monster in there?" Guangguang asks.', 'Your stomach and intestines mix food with soft squeezes.', 'When empty, gas and juices slosh and make growly sounds.', 'Hunger hormones tell your brain it may be meal time.', 'Growls can also happen while digesting a big snack.', 'Drinking water and waiting a bit often settles the noise.', 'A balanced meal gives steady fuel instead of big crashes.', "Everyone's tummy talks sometimes—it is not a failure.", 'If pain comes with growls, tell a grown-up.', 'Rest and calm breathing help when the rumble feels loud.', 'Your body is a busy kitchen, not a scary cave.', 'Mix, slosh, signal: tummy soundtrack science.'],
  "bubbles": [('Rumble!', 'Monster?'), ('Soft squeezes', 'mix food.'), ('Empty slosh', 'makes noise.'), ('Hunger tells', 'the brain.'), ('Big snack', 'can rumble.'), ('Water helps', 'settle.'), ('Steady meals', 'fuel well.'), ('Tummies talk', 'sometimes.'), ('Pain too?', 'Tell grown-up.'), ('Breathe calm', 'if loud.'), ('Busy kitchen,', 'not scary.'), ('Tummy soundtrack', 'science.')],
  "scenes": ['WIDE soft living room tummy rumble joke; boy and robot one-third; empty speech bubbles', 'DIAGRAM-SOFT stomach intestine squeezes; tiny figures; empty speech bubbles', 'CLOSE empty tummy slosh soft cartoon; characters half frame; empty speech bubbles', 'MEDIUM hunger signal to brain soft; boy points; robot; empty speech bubbles', 'PLAYFUL snack digest rumble soft; characters half frame; empty speech bubbles', 'CLOSE water bottle settle soft; characters half frame; empty speech bubbles', 'WIDE balanced plate soft; characters one-third; empty speech bubbles', 'MEDIUM friends all rumble giggle soft; characters one-third; empty speech bubbles', 'CLOSE tell grown-up soft; characters half frame; empty speech bubbles', 'MEDIUM calm breathe soft; boy and robot half frame; empty speech bubbles', 'PLAYFUL kitchen tummy idea soft; characters half frame; empty speech bubbles', 'ENDING boy and robot thumbs-up soft; one-third; empty speech bubbles'],
 },
 'E-B15': {
  "title": 'Why Do We Get Chickenpox Only Once Usually?', "folder": 'Body', "tag": 'Pox', "companion": 'girl',
  "pages": ['Itchy dots! "Will it come back forever?" asks Guangguang.', 'Chickenpox is usually caused by a virus called varicella.', "Your immune system learns the virus's face during illness.", 'Memory cells keep that lesson ready for later.', 'If the virus visits again, defenses often stop a full round.', 'That is why most people get the classic rash only once.', 'Vaccines teach the same lesson more gently beforehand.', 'Some viruses hide and can return as different itchy shingles later in life.', 'For kids, rest, soft clothes, and grown-up care help.', 'Do not scratch hard—nails can open skin to other germs.', 'Never share lotion guesses; ask a grown-up or doctor.', 'Learn once, remember long: immune school for pox.'],
  "bubbles": [('Itchy dots!', 'Forever?'), ('Virus called', 'varicella.'), ('Immune learns', 'its face.'), ('Memory cells', 'keep lesson.'), ('Later visits', 'get stopped.'), ('Usually once', 'classic rash.'), ('Vaccines teach', 'gently.'), ('Sometimes later', 'shingles.'), ('Rest soft', 'care.'), ("Don't scratch", 'hard.'), ('Ask grown-up', 'or doctor.'), ('Immune school', 'lesson.')],
  "scenes": ['WIDE soft cozy bed itchy dots soft not gross; girl and robot one-third; empty speech bubbles', 'DIAGRAM-SOFT tiny virus friendly cartoon; tiny figures; empty speech bubbles', 'MEDIUM immune cells learn soft; girl points; robot; empty speech bubbles', 'CLOSE memory cell soft glow; characters half frame; empty speech bubbles', 'PLAYFUL shield blocks second visit soft; characters half frame; empty speech bubbles', 'WIDE once usually idea soft; characters one-third; empty speech bubbles', 'MEDIUM vaccine gentle lesson soft; characters half frame; empty speech bubbles', 'DIAGRAM-SOFT later shingles note soft gentle; tiny figures; empty speech bubbles', 'MEDIUM rest soft clothes soft; girl and robot half frame; empty speech bubbles', 'CLOSE hands-off no hard scratch soft; robot nod; empty speech bubbles', 'MEDIUM ask grown-up soft; characters half frame; empty speech bubbles', 'ENDING girl and robot gentle high-five; one-third; empty speech bubbles'],
 },
 'E-B16': {
  "title": 'Why Do Babies Have Soft Spots on Their Heads?', "folder": 'Body', "tag": 'Softspot', "companion": 'girl',
  "pages": ['A soft spot! "Is the head unfinished?" Guangguang whispers.', 'Babies have soft spots called fontanelles between skull bones.', 'Flexible gaps help the head pass through birth more safely.', 'They also leave room for a fast-growing baby brain.', 'Bones slowly meet and harden as months pass.', 'Gentle touch is fine; rough pressing is not a game.', 'Doctors check soft spots during well-baby visits.', 'Helmets and car seats protect growing heads on the go.', 'Soft spots usually close on their own with time.', 'If a spot looks very sunken or bulging with worry signs, tell a grown-up.', 'Every baby skull has a careful building plan.', 'Gaps for birth and growth: soft-spot science.'],
  "bubbles": [('Soft spot!', 'Unfinished?'), ('Fontanelles', 'between bones.'), ('Help during', 'birth.'), ('Room for', 'growing brain.'), ('Bones meet', 'over time.'), ('Gentle touch,', 'no press game.'), ('Doctors check', 'visits.'), ('Helmets seats', 'protect.'), ('Close on', 'their own.'), ('Worry signs?', 'Tell grown-up.'), ('Building plan', 'for skull.'), ('Soft-spot', 'science.')],
  "scenes": ['WIDE soft baby with parent pastel; girl and robot one-third; empty speech bubbles', 'DIAGRAM-SOFT skull soft gaps; tiny figures; empty speech bubbles', 'MEDIUM birth path soft gentle medical; characters edge; empty speech bubbles', 'CLOSE growing brain room soft; girl points; robot; empty speech bubbles', 'PLAYFUL bones meeting over months soft; characters half frame; empty speech bubbles', 'CLOSE gentle touch soft; characters half frame; empty speech bubbles', 'MEDIUM doctor check soft; characters half frame; empty speech bubbles', 'WIDE car seat helmet soft; characters one-third; empty speech bubbles', 'DIAGRAM-SOFT closing over time; tiny figures; empty speech bubbles', 'CLOSE tell grown-up soft; characters half frame; empty speech bubbles', 'WIDE proud baby plan soft; characters one-third; empty speech bubbles', 'ENDING girl and robot soft smile; one-third; empty speech bubbles'],
 },
 'E-B17': {
  "title": 'Why Do We Need Saliva?', "folder": 'Body', "tag": 'Spit', "companion": 'boy',
  "pages": ['"Spit is gross—why make it?" Guangguang holds a napkin.', 'Saliva is mostly water with helpful helpers mixed in.', 'It moistens food so chewing and swallowing feel easier.', 'Enzymes in spit begin breaking some starches early.', 'Saliva washes teeth and helps keep the mouth less dry.', 'It also carries taste bits to your tongue sensors.', 'A dry mouth makes talking and eating harder.', 'Drinking water supports healthy spit production.', 'Brushing still matters—spit is a helper, not a toothbrush.', 'Spitting at people is unkind; use a sink if needed.', 'Your mouth makes a quiet river of useful liquid.', 'Moisten, start digest, wash, taste: saliva jobs.'],
  "bubbles": [('Spit gross?', 'Why make?'), ('Water with', 'helpers.'), ('Moistens food', 'to swallow.'), ('Enzymes start', 'starch work.'), ('Helps wash', 'teeth.'), ('Carries taste', 'bits.'), ('Dry mouth', 'is harder.'), ('Water supports', 'spit.'), ('Brush still', 'matters.'), ("Don't spit", 'at people.'), ('Quiet useful', 'river.'), ('Saliva does', 'jobs.')],
  "scenes": ['WIDE soft kitchen napkin moment; boy and robot one-third; empty speech bubbles', 'DIAGRAM-SOFT saliva helpers soft; tiny figures; empty speech bubbles', 'MEDIUM chewing moist food soft; characters half frame; empty speech bubbles', 'CLOSE enzyme starch soft cartoon; boy points; robot; empty speech bubbles', 'CLOSE teeth wash soft; characters half frame; empty speech bubbles', 'PLAYFUL taste buds soft; characters half frame; empty speech bubbles', 'MEDIUM dry mouth hard talk soft; characters half frame; empty speech bubbles', 'CLOSE water glass soft; boy and robot half frame; empty speech bubbles', 'MEDIUM brush teeth soft; characters half frame; empty speech bubbles', 'CLOSE kind manners soft; robot nod; empty speech bubbles', 'WIDE smile soft; characters one-third; empty speech bubbles', 'ENDING boy and robot thumbs-up; one-third; empty speech bubbles'],
 },
 'E-B18': {
  "title": 'Why Does My Heart Beat Faster When I Run?', "folder": 'Body', "tag": 'Heart', "companion": 'boy',
  "pages": ['After a race, thump-thump! "Why so fast?"', 'Muscles need more oxygen and fuel during hard play.', 'Your heart pumps blood that carries those supplies.', 'Faster beats push more blood each minute.', 'Lungs work harder too, so breath may get quicker.', 'When you rest, the beat slows toward normal again.', 'A strong heart likes regular movement and sleep.', 'Warm up and cool down help the change feel smoother.', 'If chest pain or dizziness happens, stop and tell a grown-up.', 'Feeling your pulse on a wrist can be a calm science check.', 'Fast beat is your body answering the run.', 'Demand up, pump up, then settle: heart pacing.'],
  "bubbles": [('Thump fast!', 'Why?'), ('Muscles need', 'more fuel.'), ('Heart pumps', 'the supply.'), ('Faster beats,', 'more blood.'), ('Breath gets', 'quicker too.'), ('Rest slows', 'it down.'), ('Move sleep', 'help heart.'), ('Warm cool', 'smoother.'), ('Pain dizzy?', 'Tell grown-up.'), ('Feel pulse', 'science.'), ('Body answers', 'the run.'), ('Pump then', 'settle.')],
  "scenes": ['WIDE soft playground after race; boy and robot one-third; empty speech bubbles', 'DIAGRAM-SOFT muscles need oxygen; tiny figures; empty speech bubbles', 'CLOSE heart pump soft friendly; characters half frame; empty speech bubbles', 'ACTION running faster beat soft; characters edge; empty speech bubbles', 'MEDIUM breathing harder soft; boy; robot; empty speech bubbles', 'WIDE rest slow down soft; characters one-third; empty speech bubbles', 'PLAYFUL sleep and play icons soft; characters half frame; empty speech bubbles', 'MEDIUM warm-up stretch soft; boy and robot half frame; empty speech bubbles', 'CLOSE tell grown-up soft; characters half frame; empty speech bubbles', 'CLOSE pulse on wrist soft; characters half frame; empty speech bubbles', 'WIDE proud run soft; characters one-third; empty speech bubbles', 'ENDING boy and robot high-five; one-third; empty speech bubbles'],
 },
 'E-B19': {
  "title": 'Why Do We Have Earwax?', "folder": 'Body', "tag": 'Wax', "companion": 'girl',
  "pages": ['"Sticky ear stuff—yuck. Why?" Guangguang peeks carefully.', 'Earwax is a natural cleaner and protector for the ear canal.', 'It traps dust and tiny bits before they go deeper.', 'It also helps keep the canal from getting too dry.', 'Old wax usually works its way out on its own.', 'Cotton swabs can push wax farther in—skip the dig.', 'A grown-up or doctor can help if hearing feels blocked.', 'Never pour random liquids into ears for fun.', 'Ears do important listening work every day.', 'Gentle outer cleaning of the ear flap is enough at home.', 'Wax is a tiny bodyguard, not dirt to dig out.', 'Trap, protect, migrate out: earwax jobs.'],
  "bubbles": [('Sticky wax?', 'Why?'), ('Cleans and', 'protects.'), ('Traps dust', 'bits.'), ('Keeps canal', 'less dry.'), ('Old wax', 'moves out.'), ('No swab', 'digging.'), ('Blocked?', 'Ask grown-up.'), ('No random', 'liquids.'), ('Ears do', 'listening.'), ('Clean outer', 'flap only.'), ('Tiny bodyguard', 'wax.'), ('Earwax does', 'jobs.')],
  "scenes": ['WIDE soft bathroom curious look; girl and robot one-third; empty speech bubbles', 'DIAGRAM-SOFT ear canal wax soft; tiny figures; empty speech bubbles', 'CLOSE dust trapped soft; characters half frame; empty speech bubbles', 'MEDIUM moisture protect soft; girl points; robot; empty speech bubbles', 'PLAYFUL wax migrating out soft; characters half frame; empty speech bubbles', 'CLOSE no cotton swab soft X; robot shake; empty speech bubbles', 'MEDIUM tell grown-up soft; characters half frame; empty speech bubbles', 'CLOSE no pouring liquids soft; characters half frame; empty speech bubbles', 'WIDE listening music soft; characters one-third; empty speech bubbles', 'CLOSE wipe outer ear soft; girl and robot half frame; empty speech bubbles', 'PLAYFUL bodyguard wax soft; characters half frame; empty speech bubbles', 'ENDING girl and robot soft smile; one-third; empty speech bubbles'],
 },
 'E-B20': {
  "title": 'Why Do Fingernails Grow?', "folder": 'Body', "tag": 'Nails', "companion": 'boy',
  "pages": ['Clip time! "Why do nails keep coming back?"', 'Nails grow from a root area under the skin at the base.', 'New cells push older cells forward into the hard plate.', 'The hard part is mostly keratin, a tough protein.', 'Nails protect fingertips and help tiny pick-up jobs.', 'Growth is slow and steady for most kids.', 'Biting nails can hurt the skin around them.', 'Keep nails clean and trimmed with grown-up help.', 'A balanced diet supports many growing body parts, including nails.', 'If a nail looks painful or infected, tell a grown-up.', 'Nails are tools and shields that quietly renew.', 'Root push, keratin plate, protect: nail science.'],
  "bubbles": [('Nails return!', 'Why?'), ('Grow from', 'root base.'), ('New cells', 'push forward.'), ('Keratin makes', 'hard plate.'), ('Protect tips,', 'help pick.'), ('Slow steady', 'growth.'), ("Don't bite", 'nails.'), ('Trim clean', 'with help.'), ('Food helps', 'growing.'), ('Pain infect?', 'Tell grown-up.'), ('Tools that', 'renew.'), ('Nail science', 'push.')],
  "scenes": ['WIDE soft bathroom nail clip; boy and robot one-third; empty speech bubbles', 'DIAGRAM-SOFT nail root soft; tiny figures; empty speech bubbles', 'CLOSE cells pushing plate soft; characters half frame; empty speech bubbles', 'MEDIUM keratin hard plate soft; boy points; robot; empty speech bubbles', 'PLAYFUL fingertip protect pick soft; characters half frame; empty speech bubbles', 'WIDE calendar slow growth soft; characters one-third; empty speech bubbles', 'CLOSE no biting soft; robot shake; empty speech bubbles', 'MEDIUM trim with grown-up soft; boy and robot half frame; empty speech bubbles', 'WIDE healthy plate soft; characters one-third; empty speech bubbles', 'CLOSE tell grown-up soft; characters half frame; empty speech bubbles', 'PLAYFUL shield tool icons soft; characters half frame; empty speech bubbles', 'ENDING boy and robot thumbs-up; one-third; empty speech bubbles'],
 },
 'E-B21': {
  "title": 'Why Do We Get Allergies?', "folder": 'Body', "tag": 'Allergy', "companion": 'girl',
  "pages": ['Achoo near cats! "Why does my body overreact?"', 'An allergy is when the immune system treats a harmless thing as a threat.', 'Pollen, some foods, or pet dander can be triggers for some people.', 'The body releases chemicals that cause itch, sneeze, or swell.', 'Not everyone reacts to the same triggers.', 'Avoiding known triggers and plans from doctors help a lot.', 'Allergy is different from a cold germ infection.', 'If breathing gets hard, get grown-up help right away.', 'Labels on food matter when allergies are serious.', 'You did nothing wrong—bodies just have different alarm settings.', 'Learn your triggers and keep calm helpers nearby.', 'False alarm, real feelings: allergy science kindly.'],
  "bubbles": [('Achoo cats!', 'Overreact?'), ('Immune treats', 'harmless threat.'), ('Pollen food', 'dander.'), ('Chemicals cause', 'itch sneeze.'), ('Triggers differ', 'by person.'), ('Avoid plus', 'doctor plan.'), ('Not the same', 'as cold.'), ('Hard breath?', 'Get help.'), ('Read food', 'labels.'), ('Not your', 'fault.'), ('Know triggers,', 'stay calm.'), ('Allergy science', 'kindly.')],
  "scenes": ['WIDE soft park sneeze near cat distant; girl and robot one-third; empty speech bubbles', 'DIAGRAM-SOFT immune false alarm soft; tiny figures; empty speech bubbles', 'MEDIUM pollen food pet icons soft; girl points; robot; empty speech bubbles', 'CLOSE itch sneeze soft not gross; characters half frame; empty speech bubbles', 'PLAYFUL different kids different triggers soft; characters one-third; empty speech bubbles', 'MEDIUM doctor plan soft; characters half frame; empty speech bubbles', 'DIAGRAM-SOFT allergy vs cold soft; tiny figures; empty speech bubbles', 'CLOSE hard breath get help soft; characters half frame; empty speech bubbles', 'CLOSE food label soft; girl and robot half frame; empty speech bubbles', 'MEDIUM kind reassure soft; characters half frame; empty speech bubbles', 'WIDE calm helpers soft; characters one-third; empty speech bubbles', 'ENDING girl and robot gentle hug pose soft; one-third; empty speech bubbles'],
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
    plan=[]; prompts=[]
    girl_ref = Path("/Users/song/qwen3-tts/comic_batch/en_girl_ref.png")
    boy_ref = Path("/Users/song/qwen3-tts/comic_batch/en_boy_ref.png")
    gg_ref = Path("/Users/song/qwen3-tts/comic_batch/guangguang_ref.png")
    for sid, st in STORIES.items():
        assert len(st["pages"])==12==len(st["bubbles"])==len(st["scenes"])
        g=st["companion"]; prefix=PREFIX_GIRL if g=="girl" else PREFIX_BOY
        kid=girl_ref if g=="girl" else boy_ref
        refs=[str(p) for p in (gg_ref,kid) if p.exists()]
        panels=[]
        for i,(scene,(left,right)) in enumerate(zip(st["scenes"], st["bubbles"]),1):
            assert len(st["pages"][i-1].split())>=4
            panels.append({"i":i,"scene":scene,"left":left,"right":right,"tag":f"{st['tag']} {i}/12","narration":st["pages"][i-1]})
            prompts.append({"id":sid,"i":i,"filename":f"c-{sid}-{i:02d}.jpg","description":prefix+"Scene: "+scene,"refs":refs,"companion":g})
        plan.append({"id":sid,"title":st["title"],"companion":g,"panels":panels})
        path=ROOT/"睡前有声稿"/"美国英文稿"/st["folder"]/f"{sid}.txt"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(st["title"]+"\n\n"+"\n\n".join(st["pages"])+"\n", encoding="utf-8")
        print("wrote", path)
    Path("/Users/song/qwen3-tts/comic_batch/comics_plan_en_backcatalog_w10.json").write_text(json.dumps(plan, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    Path("/Users/song/qwen3-tts/comic_batch/en_work/_raw_backcatalog_w10").mkdir(parents=True, exist_ok=True)
    Path("/Users/song/qwen3-tts/comic_batch/en_work/backcatalog_w10_prompts.json").write_text(json.dumps(prompts, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    bubbles_path=ROOT/"EyeHaven"/"ComicBubbleWords.en.json"
    bubbles=json.loads(bubbles_path.read_text(encoding="utf-8"))
    for sid, st in STORIES.items():
        bubbles[sid]=[{"i":i,"left":L,"right":R} for i,(L,R) in enumerate(st["bubbles"],1)]
    bubbles_path.write_text(json.dumps(bubbles, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    print("wave10 done", len(STORIES))

if __name__ == "__main__":
    main()
