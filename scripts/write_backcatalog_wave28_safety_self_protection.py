#!/usr/bin/env python3
"""Wave 28: Safety self-protection NEW books E-Z25…E-Z49 (25 titles).

Authoritative tips only (see docs/safety-content-authoritative-sources.md).
Fun theater tone; no scares; no fight-back advice. Appends catalog entries.
"""
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


def scenes_for(companion: str) -> list[str]:
    who = "boy" if companion == "boy" else "girl"
    return [
        f"WIDE soft friendly safety stage; {who} and robot one-third; empty speech bubbles",
        f"CLOSE curious almost-mistake soft; {who} points; robot; empty speech bubbles",
        f"MEDIUM oops pause soft; characters half frame; empty speech bubbles",
        f"PLAYFUL Guangguang asks soft; characters half frame; empty speech bubbles",
        f"WIDE learn tip one soft; characters one-third; empty speech bubbles",
        f"CLOSE learn tip two soft; characters half frame; empty speech bubbles",
        f"MEDIUM practice action soft; characters half frame; empty speech bubbles",
        f"PLAYFUL helper grown-up or buddy soft; characters half frame; empty speech bubbles",
        f"CLOSE chant practice soft; characters half frame; empty speech bubbles",
        f"DIAGRAM-SOFT safety idea soft; tiny figures; empty speech bubbles",
        f"MEDIUM victory pose soft; {who} and robot half frame; empty speech bubbles",
        f"ENDING {who} and robot soft smile; one-third; empty speech bubbles",
    ]


def book(title, tag, companion, pages, bubbles, source):
    assert len(pages) == 12 == len(bubbles)
    for i, p in enumerate(pages):
        assert len(p.split()) >= 4, (title, i + 1, p)
    return {
        "title": title,
        "folder": "Safety",
        "tag": tag,
        "companion": companion,
        "source": source,
        "pages": pages,
        "bubbles": bubbles,
        "scenes": scenes_for(companion),
    }


STORIES = {
    'E-Z25': book(
        'Who’s at the Door?',
        'Door',
        'boy',
        [
        'Knock knock! Max leans toward the door. "Who’s there?"',
        'Guangguang whispers, "Doors need a grown-up plan."',
        'Max almost twists the lock—then freezes with a giggle.',
        '"Who answers the door?" Guangguang asks softly.',
        'If you are home with a grown-up, call them first.',
        'Do not open for someone your grown-up did not expect.',
        'A peephole check is a grown-up job too.',
        'On the phone, do not say you are home alone.',
        'Practice: knock, call grown-up, wait together.',
        'Curious ears are fine; unlocking alone is not.',
        'Max grins. "I shout for help before I open!"',
        'Door rule: call a grown-up first.'
        ],
        [
        ('Knock knock!', 'Who’s there?'),
        ('Doors need', 'grown-up plan.'),
        ('Almost unlocked—', 'freeze!'),
        ('Who answers', 'the door?'),
        ('Call grown-up', 'first.'),
        ('Don’t open if', 'unexpected.'),
        ('Peephole is', 'grown-up job.'),
        ('Don’t say you’re', 'home alone.'),
        ('Knock, call,', 'wait.'),
        ('Listen okay;', 'unlock alone? No.'),
        ('I shout before', 'I open!'),
        ('Door rule:', 'call first.')
        ],
        'AAP HealthyChildren Home Alone',
    ),
    'E-Z26': book(
        'Windows Are Not Playgrounds',
        'Window',
        'girl',
        [
        'Mia climbs a chair near the window. "I can see farther!"',
        'Guangguang says, "Windows are for looking—not climbing."',
        'Screens keep bugs out; they are not strong walls.',
        'Furniture near windows can turn into accidental ladders.',
        'Open windows need grown-up stops or watchful eyes.',
        'Balconies and high decks are grown-up zones too.',
        'Step back; keep both feet on the floor.',
        'Ask a grown-up before moving chairs to the glass.',
        'Looking out is fun when your body stays safe.',
        'Window tip: feet down, grown-up nearby.',
        'Mia hops down. "I look with my eyes, not my climbing!"',
        'Windows: look, don’t climb.'
        ],
        [
        ('See farther!', 'Climb chair?'),
        ('Windows are for', 'looking.'),
        ('Screens aren’t', 'strong walls.'),
        ('Chairs can be', 'ladders.'),
        ('Stops need', 'grown-ups.'),
        ('Balconies are', 'grown-up zones.'),
        ('Feet on floor,', 'step back.'),
        ('Ask before moving', 'chairs.'),
        ('Look out,', 'stay safe.'),
        ('Feet down,', 'grown-up near.'),
        ('Eyes look—', 'I don’t climb!'),
        ('Windows: look,', 'don’t climb.')
        ],
        'Safe Kids Falls Prevention',
    ),
    'E-Z27': book(
        'Outlets Are Not Toys',
        'Outlet',
        'boy',
        [
        'Max spots a wall outlet. "Tiny holes look curious!"',
        'Guangguang says, "Hot, hot—not for play."',
        'Outlets and plugs are grown-up tools.',
        'Fingers and toys never go into the holes.',
        'Covers help, but telling a grown-up is smart too.',
        'If a cord looks chewed or broken, call a grown-up.',
        'Take three big steps away from hot things.',
        'Unplugging big appliances is a grown-up job.',
        'Curiosity can ask questions without touching.',
        'Outlet chant: look, don’t poke, tell a grown-up.',
        'Max backs up. "I ask instead of poking!"',
        'Outlets: grown-up zone only.'
        ],
        [
        ('Tiny holes!', 'Curious?'),
        ('Hot hot—', 'not for play.'),
        ('Plugs are', 'grown-up tools.'),
        ('No fingers in', 'holes.'),
        ('Covers help;', 'tell grown-up.'),
        ('Broken cord?', 'Call help.'),
        ('Three steps', 'away.'),
        ('Unplugging is', 'grown-up work.'),
        ('Ask questions,', 'don’t touch.'),
        ('Look, don’t poke,', 'tell.'),
        ('I ask—', 'no poking!'),
        ('Outlet:', 'grown-up zone.')
        ],
        'USFA Sesame Street Fire Safety Family Guide',
    ),
    'E-Z28': book(
        'Home Alone Starter Rules',
        'HomeAlone',
        'girl',
        [
        'Mia waves as Mom leaves for a short errand. "I’ve got this!"',
        'Guangguang smiles. "Short alone time needs a practice plan."',
        'First, know which grown-up nearby can come fast.',
        'Call or text when you get home if that is your rule.',
        'Do not invite friends over unless a grown-up said yes.',
        'If the phone rings, take a message—don’t say you’re alone.',
        'Post emergency numbers where you can see them.',
        'Know where flashlights live if lights blink off.',
        'Practice the plan once with your grown-up before real alone time.',
        'Brave means prepared, not secret-keeping.',
        'Mia nods. "I know my helper list!"',
        'Home-alone: plan, call, no surprise guests.'
        ],
        [
        ('Short errand!', 'I’ve got this!'),
        ('Alone time needs', 'a plan.'),
        ('Know a nearby', 'helper.'),
        ('Call when you', 'get home.'),
        ('No guests unless', 'grown-up yes.'),
        ('Don’t say you’re', 'alone.'),
        ('Post emergency', 'numbers.'),
        ('Flashlights ready', 'if dark.'),
        ('Practice plan', 'first.'),
        ('Prepared,', 'not secret.'),
        ('I know my', 'helper list!'),
        ('Plan, call,', 'no surprise guests.')
        ],
        'AAP HealthyChildren Home Alone',
    ),
    'E-Z29': book(
        'Pets Need Soft Hands',
        'Pets',
        'girl',
        [
        'Mia reaches toward a dog bowl. "Just a friendly pet?"',
        'Guangguang says, "Soft hands start with asking."',
        'Ask the owner or a grown-up before you touch.',
        'Do not bother a dog that is eating or sleeping.',
        'If a dog looks scared or angry, give space.',
        'Strange dogs are not instant friends—even cute ones.',
        'Never run or scream if a dog startles you.',
        'If you fall, curl small and cover your head.',
        'Young kids need a grown-up watching pet time.',
        'Kind petting is calm, slow, and invited.',
        'Mia asks first. "Soft hands win!"',
        'Pets: ask, soft hands, give space.'
        ],
        [
        ('Friendly pet?', 'Reach bowl?'),
        ('Soft hands start', 'with asking.'),
        ('Ask owner or', 'grown-up.'),
        ('Don’t bother eating', 'or sleeping.'),
        ('Scared dog?', 'Give space.'),
        ('Strange dogs aren’t', 'instant friends.'),
        ('Don’t run or', 'scream.'),
        ('Fall? Curl and', 'cover head.'),
        ('Grown-up watches', 'pet time.'),
        ('Calm slow', 'petting.'),
        ('I ask first!', 'Soft hands.'),
        ('Ask, soft hands,', 'space.')
        ],
        'CDC Healthy Pets Dogs',
    ),
    'E-Z30': book(
        'Hot Drinks Can Splash',
        'HotDrink',
        'boy',
        [
        'Max tugs a mug near the table edge. "I just want a sip peek!"',
        'Guangguang says, "Hot drinks can splash faster than you think."',
        'Keep cups away from the edge where sleeves catch.',
        'Two hands on a warm cup feel steadier than one.',
        'Grown-ups pour; kids can wait for the cool-down word.',
        'If something spills hot, call a grown-up—don’t wipe alone.',
        'Steam means still hot even when it looks quiet.',
        'Sitting while sipping beats walking with a full mug.',
        'Ask before you carry anyone else’s hot cup.',
        'Hot-drink chant: edge back, two hands, ask.',
        'Max slides the mug inward. "Edge back—I got it!"',
        'Hot drinks: careful hands win.'
        ],
        [
        ('Sip peek!', 'Tug mug?'),
        ('Hot drinks can', 'splash.'),
        ('Keep cups from', 'the edge.'),
        ('Two hands feel', 'steadier.'),
        ('Grown-ups pour;', 'kids wait.'),
        ('Hot spill? Call', 'grown-up.'),
        ('Steam means', 'still hot.'),
        ('Sit to sip,', 'don’t walk.'),
        ('Ask before carrying', 'hot cups.'),
        ('Edge back, two', 'hands, ask.'),
        ('Edge back—', 'I got it!'),
        ('Hot drinks:', 'careful hands.')
        ],
        'Safe Kids burn prevention / home safety',
    ),
    'E-Z31': book(
        'Bus Line Superpower',
        'Bus',
        'boy',
        [
        'Max bounces in the bus line. "First seat race!"',
        'Guangguang says, "Bus lines have a quiet superpower."',
        'Wait on the sidewalk until the bus fully stops.',
        'Climb on, sit down, and face forward.',
        'Hands and head stay inside the window space.',
        'Aisle walking waits until the bus is stopped.',
        'Listen to the driver—the grown-up captain.',
        'Backpacks stay where they won’t trip friends.',
        'Crossing in front of a bus needs extra looking.',
        'Bus chant: wait, sit, hands in, listen.',
        'Max sits tall. "I’m a seat superhero!"',
        'Bus line: wait, sit, stay inside.'
        ],
        [
        ('First seat', 'race!'),
        ('Bus lines have', 'superpower.'),
        ('Wait until bus', 'stops.'),
        ('Sit down, face', 'forward.'),
        ('Hands and head', 'stay in.'),
        ('Aisle waits for', 'full stop.'),
        ('Driver is the', 'captain.'),
        ('Backpacks won’t', 'trip friends.'),
        ('Cross with extra', 'looking.'),
        ('Wait, sit, hands', 'in, listen.'),
        ('I’m a seat', 'superhero!'),
        ('Bus: wait, sit,', 'stay inside.')
        ],
        'NHTSA / school bus rider safety norms',
    ),
    'E-Z32': book(
        'Recess Buddy Check',
        'Recess',
        'boy',
        [
        'The bell rings. Max zooms alone to the far fence.',
        'Guangguang calls, "Recess is better with a buddy check!"',
        'Before you play, pick a friend you can still see.',
        'Stay where a teacher or aide can see you too.',
        'Far quiet corners can hide problems—and helpers.',
        'If plans change, tell your buddy where you’ll be.',
        'Most mean moments happen when grown-ups aren’t near.',
        'A buddy can walk with you to ask for help.',
        'Whistle or line-up means everyone regroups fast.',
        'Buddy chant: see me, see you, see a grown-up.',
        'Max waves to a friend. "Buddy check—let’s play!"',
        'Recess: buddy up where grown-ups see.'
        ],
        [
        ('Far fence!', 'Zoom alone?'),
        ('Recess needs', 'buddy check.'),
        ('Pick a friend', 'you can see.'),
        ('Stay where teachers', 'see too.'),
        ('Far corners hide', 'helpers.'),
        ('Tell buddy if', 'plans change.'),
        ('Mean moments like', 'no grown-ups.'),
        ('Buddy walks to', 'ask help.'),
        ('Line-up means', 'regroup.'),
        ('See me, see you,', 'see grown-up.'),
        ('Buddy check—', 'let’s play!'),
        ('Recess: buddy up,', 'be seen.')
        ],
        'StopBullying.gov stay near adults and other kids',
    ),
    'E-Z33': book(
        'Bathroom Privacy Power',
        'Bathroom',
        'girl',
        [
        'Mia pauses at the bathroom door. "Knock first?"',
        'Guangguang nods. "Privacy power starts with respect."',
        'Knock, wait, and give people space.',
        'Your body belongs to you—awkward feelings matter.',
        'If anything feels wrong, leave right away.',
        'You do not need a long polite speech to leave.',
        'Find a teacher or other trusted adult fast.',
        'A friend can walk with you to tell.',
        'Secrets that scare you should not stay secret.',
        'Privacy chant: knock, space, leave, tell.',
        'Mia practices. "I can leave and tell!"',
        'Bathroom: respect, leave, tell a grown-up.'
        ],
        [
        ('Knock first?', 'Pause.'),
        ('Privacy power', 'starts here.'),
        ('Knock, wait,', 'give space.'),
        ('Your body is', 'yours.'),
        ('Feels wrong?', 'Leave now.'),
        ('No long polite', 'speech needed.'),
        ('Find a teacher', 'fast.'),
        ('Friend can walk', 'with you.'),
        ('Scary secrets', 'don’t stay.'),
        ('Knock, space,', 'leave, tell.'),
        ('I can leave', 'and tell!'),
        ('Respect, leave,', 'tell grown-up.')
        ],
        'StopBullying / personal safety say no find adult',
    ),
    'E-Z34': book(
        'Lost in the Hall? Find a Teacher',
        'Hall',
        'boy',
        [
        'Max turns a corner and the class is gone. "Uh-oh."',
        'Guangguang says, "Lost in the hall has a simple fix."',
        'Stop walking farther into empty hallways.',
        'Look for a teacher, office, or hallway helper.',
        'Do not leave the building with someone you don’t know.',
        'Office adults can help you find your class.',
        'If a stranger offers a shortcut, you can say no.',
        'Stay in bright busy spots while you wait for help.',
        'Your full name helps grown-ups call the right room.',
        'Hall chant: stop, find a teacher, stay put.',
        'Max finds the office. "I asked for help!"',
        'Lost in school: find a teacher fast.'
        ],
        [
        ('Class is gone!', 'Uh-oh.'),
        ('Hall lost has', 'a fix.'),
        ('Stop walking', 'farther.'),
        ('Find teacher or', 'office.'),
        ('Don’t leave with', 'strangers.'),
        ('Office helps find', 'your class.'),
        ('Shortcut offer?', 'You can say no.'),
        ('Stay in busy', 'bright spots.'),
        ('Full name helps', 'grown-ups.'),
        ('Stop, find teacher,', 'stay put.'),
        ('I asked for', 'help!'),
        ('Lost at school:', 'find teacher.')
        ],
        'NCMEC find staff / school trusted adult',
    ),
    'E-Z35': book(
        '“Just Kidding” That Doesn’t Feel Okay',
        'Teasing',
        'girl',
        [
        'A joke lands wrong. Mia forces a tiny smile.',
        'Guangguang says, "If it doesn’t feel okay, it matters."',
        'You can say stop in a calm clear voice.',
        'Walking away is brave when talking feels unsafe.',
        'Laughing along is not required.',
        'Tell a trusted teacher or grown-up what happened.',
        'It is not snitching—it is asking for help.',
        'A friend can go with you when you tell.',
        'You did not cause someone else’s mean choice.',
        'Teasing chant: stop, walk, tell a grown-up.',
        'Mia practices. "Stop. That didn’t feel okay."',
        'Just kidding? Your feelings still count.'
        ],
        [
        ('Forced smile…', 'ouch.'),
        ('If it feels bad,', 'it matters.'),
        ('Say stop calm', 'and clear.'),
        ('Walking away can', 'be brave.'),
        ('You don’t have to', 'laugh along.'),
        ('Tell a trusted', 'grown-up.'),
        ('Help-seeking isn’t', 'snitching.'),
        ('A friend can go', 'with you.'),
        ('Their mean choice', 'isn’t your fault.'),
        ('Stop, walk,', 'tell.'),
        ('Stop. That didn’t', 'feel okay.'),
        ('Feelings still', 'count.')
        ],
        'StopBullying.gov What Kids Can Do',
    ),
    'E-Z36': book(
        'Food Sharing Needs a Yes',
        'Food',
        'girl',
        [
        'A friend offers a snack swap. Mia almost trades.',
        'Guangguang says, "Food sharing needs a yes first."',
        'Some bodies react badly to hidden ingredients.',
        'Your grown-up’s lunch rules matter even at school.',
        'Ask before you trade, taste, or share.',
        'If labels are confusing, ask a teacher or nurse.',
        'No is a kind answer when food rules say no.',
        'Friends can still play without swapping bites.',
        'Allergies are not picky—they are safety.',
        'Food chant: ask, check, then yes or no.',
        'Mia smiles. "Ask first—then we both stay safe!"',
        'Food sharing: ask before you trade.'
        ],
        [
        ('Snack swap?', 'Almost.'),
        ('Sharing needs a', 'yes first.'),
        ('Hidden ingredients', 'can hurt.'),
        ('Lunch rules still', 'matter.'),
        ('Ask before you', 'trade.'),
        ('Confused label?', 'Ask teacher.'),
        ('No can be kind', 'and safe.'),
        ('Play without', 'swapping bites.'),
        ('Allergies equal', 'safety.'),
        ('Ask, check,', 'yes or no.'),
        ('Ask first—', 'stay safe!'),
        ('Food: ask before', 'you trade.')
        ],
        'AAP food allergy / caregiver rules',
    ),
    'E-Z37': book(
        'Fire Drill Is a Game We Practice',
        'FireDrill',
        'boy',
        [
        'The alarm beeps. Max wants to hide under a desk.',
        'Guangguang says, "Fire drills are practice games that keep us ready."',
        'Stop what you are doing and listen for directions.',
        'Walk quickly and quietly—no racing chaos.',
        'Do not hide in closets or bathrooms.',
        'Leave stuff behind; grown-ups and firefighters handle pets and toys.',
        'Know your class meeting place outside.',
        'If you are alone in the hall, follow other students out and tell a teacher.',
        'Stay outside until a grown-up says it is safe.',
        'Drill chant: listen, walk, meet, stay out.',
        'Max lines up. "I’m a drill champion!"',
        'Fire drill: practice calm exits.'
        ],
        [
        ('Alarm! Hide?', 'Desk?'),
        ('Drills are practice', 'games.'),
        ('Stop and listen', 'for directions.'),
        ('Walk quick and', 'quiet.'),
        ('Don’t hide in', 'closets.'),
        ('Leave stuff;', 'get out.'),
        ('Know the outside', 'meeting place.'),
        ('Alone? Follow kids,', 'tell teacher.'),
        ('Stay out until', 'safe word.'),
        ('Listen, walk, meet,', 'stay out.'),
        ('I’m a drill', 'champion!'),
        ('Drill: practice', 'calm exits.')
        ],
        'Safe Kids Fire + USFA/NFPA drill guidance',
    ),
    'E-Z38': book(
        'Ask the Teacher When Stuck',
        'Ask',
        'girl',
        [
        'Mia stares at a hard problem. Her pencil freezes.',
        'Guangguang whispers, "Stuck is a signal—not a fail."',
        'Teachers expect questions; that is their job.',
        'Raise a quiet hand or wait for a fair turn.',
        'You can ask after class if the room feels loud.',
        'Friends can cheer you on to ask—not give shame.',
        'Needing help means you are learning bravely.',
        'Write your question so it is ready to say.',
        'Grown-ups would rather hear stuck than watch silent tears.',
        'Ask chant: pause, hand up, say I need help.',
        'Mia raises her hand. "I need a hint, please!"',
        'Stuck? Ask the teacher—brave and smart.'
        ],
        [
        ('Hard problem…', 'pencil freezes.'),
        ('Stuck is a signal,', 'not a fail.'),
        ('Teachers expect', 'questions.'),
        ('Raise a quiet', 'hand.'),
        ('Ask after class if', 'needed.'),
        ('Friends cheer—', 'no shame.'),
        ('Needing help is', 'brave learning.'),
        ('Write the question', 'first.'),
        ('Grown-ups prefer', 'honest stuck.'),
        ('Pause, hand up,', 'ask help.'),
        ('I need a hint,', 'please!'),
        ('Stuck? Ask—', 'brave and smart.')
        ],
        'school help-seeking / trusted adult path',
    ),
    'E-Z39': book(
        'Buddy Up Against Mean Stuff',
        'Bullying',
        'boy',
        [
        'Mean words land. Max’s shoulders scramble up.',
        'Guangguang says, "Mean stuff has a kid-safe plan."',
        'If it is safe, say stop in a calm clear voice.',
        'If talking feels unsafe, walk away and stay away.',
        'Do not fight back—that can make hurt bigger.',
        'Tell a teacher or trusted adult what happened.',
        'Telling is help-seeking, not tattling for fun.',
        'Stay near adults and other kids when you can.',
        'A buddy can walk with you to report together.',
        'Bullying chant: stop, walk, tell, buddy up.',
        'Max finds a teacher with a friend. "We need help."',
        'Mean stuff: stop, walk, tell a grown-up.'
        ],
        [
        ('Mean words…', 'shoulders up.'),
        ('Mean stuff has', 'a plan.'),
        ('Say stop calm', 'and clear.'),
        ('Unsafe to talk?', 'Walk away.'),
        ('Don’t fight back—', 'hurt grows.'),
        ('Tell a trusted', 'adult.'),
        ('Help-seeking isn’t', 'tattling.'),
        ('Stay near adults', 'and kids.'),
        ('Buddy walks to', 'report.'),
        ('Stop, walk, tell,', 'buddy up.'),
        ('We need help', 'together.'),
        ('Stop, walk,', 'tell grown-up.')
        ],
        'StopBullying.gov + AACAP Bullying',
    ),
    'E-Z40': book(
        'Scissors Points Down',
        'Scissors',
        'girl',
        [
        'Mia carries classroom scissors tip-up like a sword.',
        'Guangguang yelps softly, "Points down when we walk!"',
        'Scissors are tools, not pretend swords.',
        'Walk slowly with tips pointed toward the floor.',
        'Pass scissors handle-first to a friend.',
        'Cut only what the teacher said to cut.',
        'Closed scissors rest flat when you are done.',
        'Running with scissors is a hard no.',
        'If you drop them, let them fall—don’t grab the blades.',
        'Scissors chant: tips down, walk slow, handle first.',
        'Mia flips the tips down. "Tool mode on!"',
        'Scissors: tips down, walk slow.'
        ],
        [
        ('Tips up like', 'a sword?'),
        ('Points down when', 'we walk!'),
        ('Tools, not', 'swords.'),
        ('Tips toward the', 'floor.'),
        ('Pass handle-first', 'to friends.'),
        ('Cut only what', 'teacher said.'),
        ('Closed scissors', 'rest flat.'),
        ('No running with', 'scissors.'),
        ('Drop? Don’t grab', 'blades.'),
        ('Tips down, walk,', 'handle first.'),
        ('Tool mode', 'on!'),
        ('Tips down,', 'walk slow.')
        ],
        'classroom tool safety norms',
    ),
    'E-Z41': book(
        'If You Get Separated',
        'Separated',
        'boy',
        [
        'In a busy store, Max turns—and his grown-up is gone.',
        'Guangguang says, "Separated has a calm kid plan."',
        'Stop in a bright spot instead of racing farther away.',
        'Find a worker with a name tag or store uniform.',
        'Say your full name in a clear voice.',
        'If they ask, share your grown-up’s phone number.',
        'You can share your home address with that helper too.',
        'Do not leave the store with a stranger who offers a ride.',
        'Stay with the helper until your grown-up arrives.',
        'Separated chant: stop, find staff, say name.',
        'Max finds a cashier. "I’m Max. Please help me find my dad."',
        'Separated: stop, find staff, use your info.'
        ],
        [
        ('Grown-up gone!', 'Busy store.'),
        ('Separated has a', 'calm plan.'),
        ('Stop in a bright', 'spot.'),
        ('Find uniform or', 'name tag.'),
        ('Say your full', 'name.'),
        ('Share grown-up’s', 'phone if asked.'),
        ('Address for the', 'helper too.'),
        ('No stranger', 'rides.'),
        ('Stay until your', 'grown-up comes.'),
        ('Stop, find staff,', 'say name.'),
        ('I’m Max—please', 'help find Dad.'),
        ('Stop, staff,', 'use your info.')
        ],
        'NCMEC store staff + AAP name/address/phone',
    ),
    'E-Z42': book(
        'Strange Dogs: Soft Freeze',
        'Dogs',
        'boy',
        [
        'A loose dog trots near. Max wants to run.',
        'Guangguang says, "Soft freeze beats a scary chase."',
        'Do not run, scream, or wave wild arms.',
        'Stand still like a tree, side-facing if you can.',
        'Do not reach to pet a dog you do not know.',
        'Call a grown-up with a steady voice.',
        'If you fall, curl up and cover your head.',
        'Give eating or sleeping dogs plenty of space.',
        'Even friendly-looking dogs can get startled.',
        'Dog chant: freeze, no pet, call grown-up.',
        'Max freezes, then calls, "Dad—dog help!"',
        'Strange dogs: freeze, don’t chase, get help.'
        ],
        [
        ('Loose dog!', 'Want to run.'),
        ('Soft freeze beats', 'a chase.'),
        ('Don’t run or', 'scream.'),
        ('Stand still like', 'a tree.'),
        ('Don’t pet dogs', 'you don’t know.'),
        ('Call a grown-up', 'steadily.'),
        ('Fall? Curl and', 'cover.'),
        ('Space for eating', 'dogs.'),
        ('Cute can still', 'startle.'),
        ('Freeze, no pet,', 'call.'),
        ('Dad—dog', 'help!'),
        ('Freeze, don’t chase,', 'get help.')
        ],
        'CDC Healthy Pets Dogs',
    ),
    'E-Z43': book(
        'Thunder Means Inside Time',
        'Thunder',
        'girl',
        [
        'A rumble rolls. Mia wants to finish the playground climb.',
        'Guangguang says, "When thunder roars, go indoors."',
        'Hearing thunder means lightning can already be near.',
        'Head inside a sturdy building or a hard-top car.',
        'Do not shelter under a lone tall tree.',
        'Leave open fields, peaks, and water edges.',
        'Picnic sheds and dugouts are not enough.',
        'Wait indoors a good while after the last thunder.',
        'Tell a grown-up as soon as you hear the rumble.',
        'Thunder chant: hear it, head in, wait.',
        'Mia jogs inside. "Thunder—inside time!"',
        'Thunder: go indoors, stay safe.'
        ],
        [
        ('Rumble!', 'One more climb?'),
        ('Thunder roars,', 'go indoors.'),
        ('Thunder means', 'lightning near.'),
        ('Sturdy building or', 'hard-top car.'),
        ('Not under a lone', 'tall tree.'),
        ('Leave fields and', 'water edges.'),
        ('Sheds aren’t', 'enough.'),
        ('Wait after last', 'thunder.'),
        ('Tell a grown-up', 'fast.'),
        ('Hear it, head in,', 'wait.'),
        ('Thunder—inside', 'time!'),
        ('Thunder: go', 'indoors.')
        ],
        'CDC Lightning Safety',
    ),
    'E-Z44': book(
        'Playground Check First',
        'Playground',
        'boy',
        [
        'Max sprints toward wet metal slides after rain.',
        'Guangguang says, "Playground check first—then fun."',
        'Look for broken parts, sharp edges, or deep puddles.',
        'Wet equipment can be extra slippery.',
        'Tell a grown-up about anything that looks wrong.',
        'Take turns so nobody gets bumped mid-air.',
        'Shoes on for climbing when that is the rule.',
        'If a swing chain looks twisted or worn, skip it.',
        'Safe play means eyes open before speed.',
        'Playground chant: look, tell, then play.',
        'Max points to a puddle. "Check first—then we go!"',
        'Playground: check, tell, then play.'
        ],
        [
        ('Wet slides!', 'Sprint?'),
        ('Check first—', 'then fun.'),
        ('Look for broken', 'parts.'),
        ('Wet means extra', 'slippery.'),
        ('Tell a grown-up', 'what’s wrong.'),
        ('Take turns,', 'no mid-air bumps.'),
        ('Shoes on for', 'climbing.'),
        ('Worn chain?', 'Skip it.'),
        ('Eyes open before', 'speed.'),
        ('Look, tell,', 'then play.'),
        ('Check first—', 'then we go!'),
        ('Check, tell,', 'then play.')
        ],
        'CPSC playground safety guidance',
    ),
    'E-Z45': book(
        'Water’s Edge Pause',
        'WaterEdge',
        'girl',
        [
        'Mia dashes toward the lake edge to toss a pebble.',
        'Guangguang says, "Water’s edge needs a pause."',
        'Stop one step before the shore or pool rim.',
        'A grown-up should watch closely—no phone fog.',
        'Drowning can be quiet; that is why eyes stay on kids.',
        'Life jackets help in boats and some natural water.',
        'Do not rely on float toys as safety gear.',
        'Ask before you step closer than the pause line.',
        'Buddy systems still need a watching grown-up.',
        'Edge chant: pause, grown-up eyes, then maybe closer.',
        'Mia stops short. "Pause at the edge!"',
        'Water’s edge: pause for a watching grown-up.'
        ],
        [
        ('Lake edge!', 'Toss pebble?'),
        ('Water’s edge needs', 'a pause.'),
        ('Stop one step', 'before.'),
        ('Grown-up watches—', 'no phone fog.'),
        ('Drowning can be', 'quiet.'),
        ('Life jackets help', 'on water.'),
        ('Float toys aren’t', 'safety gear.'),
        ('Ask before stepping', 'closer.'),
        ('Buddies still need', 'grown-up eyes.'),
        ('Pause, grown-up eyes,', 'then closer.'),
        ('Pause at the', 'edge!'),
        ('Edge: pause for', 'grown-up eyes.')
        ],
        'CDC Drowning Prevention',
    ),
    'E-Z46': book(
        'Night Walk Glow Rules',
        'NightWalk',
        'boy',
        [
        'Evening stroll. Max blends into dark clothes.',
        'Guangguang says, "Night walks need glow rules."',
        'Wear bright or reflective bits so drivers see you.',
        'Carry a light or walk near street lamps.',
        'Use sidewalks; cross at corners with looking.',
        'Devices down when you cross—eyes up.',
        'Hold a grown-up’s hand on busy night streets.',
        'Light colors help even without fancy gear.',
        'If a street feels too dark, choose a brighter path.',
        'Glow chant: bright, light, look, hold on.',
        'Max clips a reflector. "Glow mode on!"',
        'Night walk: be seen, stay with a grown-up.'
        ],
        [
        ('Dark clothes…', 'blend in.'),
        ('Night walks need', 'glow rules.'),
        ('Bright bits help', 'drivers see.'),
        ('Light or street', 'lamps.'),
        ('Sidewalks and', 'corner looking.'),
        ('Devices down,', 'eyes up.'),
        ('Hold hands on', 'busy nights.'),
        ('Light colors help', 'too.'),
        ('Too dark? Pick', 'brighter path.'),
        ('Bright, light, look,', 'hold on.'),
        ('Glow mode', 'on!'),
        ('Night: be seen,', 'stay with grown-up.')
        ],
        'Safe Kids pedestrian visibility',
    ),
    'E-Z47': book(
        'Park Restroom Plan',
        'ParkRestroom',
        'girl',
        [
        'Park path. Mia needs the restroom alone.',
        'Guangguang says, "Park restrooms need a tiny plan."',
        'Tell your grown-up before you go.',
        'A grown-up can wait just outside when that is the rule.',
        'Buddy up with a friend if your grown-up agrees.',
        'Do not tell strangers you are by yourself.',
        'If someone makes you uneasy, leave and find your grown-up.',
        'Choose busy, lit restrooms when you can.',
        'Your grown-up should know which building you entered.',
        'Restroom chant: tell, buddy or wait, come right back.',
        'Mia waves. "I’ll be quick—Mom’s outside!"',
        'Park restroom: tell, plan, come back.'
        ],
        [
        ('Restroom alone?', 'Park path.'),
        ('Needs a tiny', 'plan.'),
        ('Tell your grown-up', 'first.'),
        ('Grown-up can wait', 'outside.'),
        ('Buddy up if', 'allowed.'),
        ('Don’t say you’re', 'alone.'),
        ('Uneasy? Leave and', 'find grown-up.'),
        ('Busy lit rooms', 'are better.'),
        ('Grown-up knows', 'which building.'),
        ('Tell, buddy or wait,', 'come back.'),
        ('I’ll be quick—', 'Mom’s outside!'),
        ('Tell, plan,', 'come back.')
        ],
        'personal safety trusted adult / buddy',
    ),
    'E-Z48': book(
        'Trail Stick Together',
        'Trail',
        'boy',
        [
        'On a trail, Max zooms ahead around a bend.',
        'Guangguang puffs, "Trails work when we stick together!"',
        'Keep the group where you can see the leader.',
        'Agree on a simple call-back word or whistle.',
        'If you can’t see your people, stop and shout the word.',
        'Do not invent a secret shortcut alone.',
        'Grown-ups set the pace for steep or muddy bits.',
        'Water bottles and rests happen as a team.',
        'Buddy pairs help count everyone at each stop.',
        'Trail chant: see the group, call back, no solo shortcuts.',
        'Max waits at the bend. "Stick together—I’m here!"',
        'Trail: stay where your people can see you.'
        ],
        [
        ('Zoom ahead!', 'Around bend.'),
        ('Trails need stick', 'together.'),
        ('See the leader', 'always.'),
        ('Agree on a call-back', 'word.'),
        ('Can’t see them?', 'Stop and call.'),
        ('No solo secret', 'shortcuts.'),
        ('Grown-ups set', 'the pace.'),
        ('Rests happen as', 'a team.'),
        ('Buddy pairs help', 'count.'),
        ('See group, call back,', 'no shortcuts.'),
        ('Stick together—', 'I’m here!'),
        ('Trail: stay where', 'people see you.')
        ],
        'outdoor supervision / buddy system',
    ),
    'E-Z49': book(
        'My Address & Grown-Up’s Number',
        'AddressPhone',
        'girl',
        [
        'Mia practices words on a fridge card. "Street… number…"',
        'Guangguang cheers, "Knowing your info is a superpower!"',
        'Learn your full name the clear way.',
        'Learn your home address like a little song.',
        'Learn a grown-up’s phone number you can recite.',
        'Share that info with police, teachers, or store helpers who are helping you.',
        'Do not announce your address to random strangers for fun.',
        'Practice at home until it feels easy—not scary.',
        'A pocket card can help while you are still learning.',
        'Info chant: name, address, phone—for trusted helpers.',
        'Mia recites proudly. "I know my safety words!"',
        'Name, address, phone: ready for trusted helpers.'
        ],
        [
        ('Street… number…', 'practice.'),
        ('Knowing info is', 'a superpower!'),
        ('Full name,', 'clear way.'),
        ('Address like a', 'little song.'),
        ('Grown-up phone', 'you can say.'),
        ('Share with trusted', 'helpers.'),
        ('Don’t announce to', 'random strangers.'),
        ('Practice at home', 'until easy.'),
        ('Pocket card can', 'help.'),
        ('Name, address, phone', 'for helpers.'),
        ('I know my', 'safety words!'),
        ('Ready for trusted', 'helpers.')
        ],
        'AAP Home Alone name/address/when to share',
    ),
}


def main() -> None:
    text_map = {sid: "\n\n".join(st["pages"]) for sid, st in STORIES.items()}
    for rel in ["EyeHaven/BedtimeContentCatalog.en.json", "EyeHaven/BedtimeContentCatalog.json"]:
        path = ROOT / rel
        data = json.loads(path.read_text(encoding="utf-8"))
        by_id = {s["id"]: s for s in data["stories"]}
        for sid, st in STORIES.items():
            body = {
                "id": sid,
                "age": "child",
                "shelf": "safety",
                "title": st["title"],
                "text": text_map[sid],
                "group": None,
            }
            if sid in by_id:
                by_id[sid]["title"] = st["title"]
                by_id[sid]["text"] = text_map[sid]
            else:
                data["stories"].append(body)
        data["updatedAt"] = "2026-11-18"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print("updated", path, "stories", len(data["stories"]))

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
    ref_dir = ROOT / ".comic_refs" / "w28_by_story"
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
            panels.append(
                {
                    "i": i,
                    "scene": scene,
                    "left": left,
                    "right": right,
                    "tag": f"{st['tag']} {i}/12",
                    "narration": st["pages"][i - 1],
                    "source": st["source"],
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
        plan.append({"id": sid, "title": st["title"], "companion": g, "source": st["source"], "panels": panels})
        path = ROOT / "睡前有声稿" / "美国英文稿" / st["folder"] / f"{sid}.txt"
        path.parent.mkdir(parents=True, exist_ok=True)
        note = f"# source: {st['source']}\n"
        path.write_text(note + st["title"] + "\n\n" + "\n\n".join(st["pages"]) + "\n", encoding="utf-8")
        print("wrote", path)
        story_dir = ref_dir / sid
        story_dir.mkdir(parents=True, exist_ok=True)
        (ref_dir / f"{sid}_prompts.json").write_text(
            json.dumps(story_prompts, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
        for ref in (gg_ref, kid):
            if ref.exists():
                shutil.copy2(ref, story_dir / ref.name)

    batch = Path("/Users/song/qwen3-tts/comic_batch")
    batch.mkdir(parents=True, exist_ok=True)
    (batch / "comics_plan_en_backcatalog_w28.json").write_text(
        json.dumps(plan, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    (batch / "en_work" / "_raw_backcatalog_w28").mkdir(parents=True, exist_ok=True)
    (batch / "en_work" / "backcatalog_w28_prompts.json").write_text(
        json.dumps(prompts, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    bubbles_path = ROOT / "EyeHaven" / "ComicBubbleWords.en.json"
    bubbles = json.loads(bubbles_path.read_text(encoding="utf-8"))
    for sid, st in STORIES.items():
        bubbles[sid] = [{"i": i, "left": L, "right": R} for i, (L, R) in enumerate(st["bubbles"], 1)]
    bubbles_path.write_text(json.dumps(bubbles, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    sources_note = ROOT / "scripts" / "wave28_safety_sources.json"
    sources_note.write_text(
        json.dumps({sid: st["source"] for sid, st in STORIES.items()}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print("wave28 done", len(STORIES), "prompts", len(prompts))


if __name__ == "__main__":
    main()
