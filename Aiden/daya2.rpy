label day2_aiden:
    $ day = "77"
    $ season = season_winter
    $ time = timeline_timeday
    $ location = location_clermont
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    $ working = True

    scene bg_clermontoffice_day with fade
    play music heracleum_a loop
    show darius_autumn at p9_1
    show darius norm1 at p9_1
    show aiden_autumn at p9_3
    show aiden norm1 at p9_3
    show lloyd_autumn at p9_2
    show lloyd norm2 at p9_2
    show yoshi_autumn at p9_4
    show yoshi norm1 at p9_4
    show william_formal at p9_5
    show william norm1 at p9_5
    show goro_autumn at p9_7
    show goro happy1 at p9_7
    show emilia_autumn at p9_6
    show emilia norm3 at p9_6
    show yuri_autumn at p9_8
    show yuri norm1 at p9_8
    show jin_autumn at p9_9
    show jin_glasses at p9_9
    show jin norm1 at p9_9
    voice audio.goro_v_so1a
    g "…And that’s the progress of the project so far, Mr. Clermont.  I believe we’ve reached all targets on schedule."

    show william happy2 at p9_5
    voice audio.william_v_amazed2
    w "That’s great to hear! I’m glad to know everything’s still on track!"

    show goro happy3 at p9_7
    voice audio.goro_v_conj7a
    g "If you need any more details, you can find them in the report we’ve provided."

    show william comp4 at p9_5
    voice audio.william_v_impressed2a
    w "Excellent. But before we conclude this meeting, I have other concerns that I would like to discuss with everyone."

    show goro confused2 at p9_7
    voice audio.goro_v_oh3b
    g "What is it, Mr. Clermont?"

    show william explain2 at p9_5
    voice audio.william_v_well1b
    w "Well, throughout the previous months I received separate reports from our inspector."

    show darius shock4 at p9_1
    show lloyd confused2 at p9_2
    show aiden shock1 at p9_3
    show yoshi shock1 at p9_4
    show emilia evil2 at p9_6
    show goro shock1 at p9_7
    show yuri annoy1 at p9_8
    show jin shock4 at p9_9
    w "I know that we’ve achieved our preliminary goals, but based on Ms. Komarova’s account, it seems that there were difficulties encountered along the way."

    hide goro_autumn
    hide goro shock1
    show goro2_autumn at p9_7
    show goro2 think5 at p9_7
    voice audio.goro_v_sorry2a2
    g "I’m sorry, I don’t think we were informed about this…"

    show william think3 at p9_5
    voice audio.william_v_conj7
    w "Then this is the perfect moment to discuss these matters and ensure that we can move forward with the project positively."
    w "Ms. Komarova, if you may."

    show william norm3 at p9_5
    show emilia evil3 at p9_6
    voice audio.emilia_v_thanks2
    e "Thank you for bringing this up, Mr. Clermont. I believe these matters are of utmost importance."

    show emilia play2 at p9_6
    voice audio.emilia_v_conj3a
    e "As the standing representative for quality assurance, I wanted to discuss some specific departmental concerns that need to be corrected.  "

    show yuri irked2 at p9_8
    voice audio.yuri_v_ugh3a
    yu "Ugh… here we go again…"

    show yoshi angry2 at p9_4
    voice audio.yoshi_v_yuri9
    yo "Y-Yuri…!"

    show emilia angry5 at p9_6
    voice audio.emilia_v_jin3
    e "Let’s start off with Mr. Choi. I’ve found his reversed sleep schedule to be very unprofessional."
    e "He sleeps the whole day starting from 9:00 am until 6:00 pm which are the peak productivity hours. There was no way for me to reach him in-person to oversee his work."

    show jin panic2 at p9_9
    voice audio.jin_v_sorry1c3
    j "A-Ah… I admit that was very unprofessional of me… I apologize for causing trouble. "

    hide goro2_autumn
    hide goro2 think5
    show goro_autumn at p9_7
    show goro explain2 at p9_7
    hide emilia_autumn
    hide emilia angry5
    show emilia_autumn at p9_6
    show emilia angry5 at p9_6
    voice audio.goro_v_conj9a1
    g "If I may – I, too, was honestly concerned about this in the beginning, but despite Jin’s schedule being different from us, he had no problems communicating with the rest of the team."
    g "More importantly, he completed all his deadlines with time to spare. I would know, because I also watched over the progress of his department."

    show emilia eyeroll3 at p9_6
    voice audio.emilia_v_hmph1a
    e "Even so, it would’ve been optimal if he were accessible in the same time frame as everyone else. Not to mention that it’s a potential health concern. "

    show jin worry4 at p9_9
    voice audio.jin_v_comp2b2
    j "I-If it helps… I’ll promise to change my habits from now on…!"

    show emilia talk1 at p9_6
    voice audio.emilia_v_conj2a
    e "Moving on to the construction department, I have noticed inconsistencies with the time cards of Mr. Sirius and Mr. Najjar."
    e "From my observations, it was mostly due to the unnecessarily extensive morning routines they partake in."

    show lloyd annoy2 at p9_2
    voice audio.lloyd_v_question1e1
    l "W-What does that have to do with anything…?"

    show darius annoy2 at p9_1
    voice audio.darius_v_emilia5c
    d "She’s nitpicking at this point."

    show yuri annoy2 at p9_8
    voice audio.yuri_v_conj1a1
    yu "At the end of the day, it doesn’t matter. Some of us may have different schedules and routines, but we all adjusted to each other and finished the work according to all the deadlines."
    yu "We don’t snoop around and call you out for your personal schedules!"

    show emilia annoy2 at p9_6
    voice audio.emilia_v_yuri7
    e "Which brings me to another issue: Ms. Nomoru’s attitude problem. She’s very hostile towards me, as you can see."

    show yuri rage1 at p9_8
    voice audio.yuri_v_what5a
    yu "Attitude problem?! Why I—"

    hide goro_autumn
    hide goro explain2
    show goro2_autumn at p9_7
    show goro2 disappoint3 at p9_7
    voice audio.goro_v_scold1a1
    g "Yuri, calm down."

    show yuri pout4 at p9_8
    voice audio.yuri_v_hmph1a
    yu "Hmph!"

    show emilia disgust1 at p9_6
    voice audio.emilia_v_aiden6
    e "And last but not least, I have a strange issue with Mr. Flynn. According to my investigations, he was still exhibiting indecent behavior around camp."
    e "Even though I pointed it out at the beginning, it seems that he refused to listen to initial warnings and there were still instances of such displays."

    show william confused2 at p9_5
    voice audio.william_v_think4
    w "Hmm? This wasn’t included in your reports. Please elaborate."

    show yoshi explain2 at p9_4
    voice audio.yoshi_v_william2
    yo "It’s nothing serious, Mr. Clermont. She’s talking about the times where we needed to wear less clothing to cool off from the work. You know how men are."

    show emilia disgust5 at p9_6
    voice audio.emilia_v_annoyed1
    e "With the weather getting colder, surely a habit like that is unnecessary. I just thought it was important to point out. "
    e "Although, I have to give props where they’re due. If it weren’t for Mr. Nagira being in charge of overseeing Mr. Flynn’s department, things could’ve been worse."

    hide aiden_autumn
    hide aiden shock1
    show aiden2_autumn2 at p9_3
    show aiden2 scared2 at p9_3
    show emilia annoy3 at p9_6
    voice audio.emilia_v_sarcastic3b
    e "Not to mention, if one of the staff is handling JUST the maintenance, wouldn’t it make more sense that the scoutmaster title for Mr. Flynn be revoked and changed back to a ‘helper’?"

    $working = False
    $shuffle_menu()
    menu():
        e "Not to mention, if one of the staff is handling JUST the maintenance, wouldn’t it make more sense that the scoutmaster title for Mr. Flynn be revoked and changed back to a ‘helper’?{fast}"
        "Just maintenance?":
            $working = True
            $score_aiden += 1
            $score_bot += 1
            show yoshi rage1 at p9_4
            voice audio.yoshi_v_what4
            yo "Just… maintenance? "
            yo "Excuse me, but maintenance is not an easy job at all."
        "You don't know what you're saying.":
            $working = True
            $score_aiden += 1
            $score_top += 1
            show yoshi rage1 at p9_4
            voice audio.yoshi_v_disagree2
            yo "You don’t know what you’re talking about."
            yo "You don’t see how hard he works to keep the camp running. "
        "Aiden does more than you think.":
            $working = True
            $score_aiden += 2
            $score_bot += 1
            show yoshi rage1 at p9_4
            voice audio.yoshi_v_disagree2
            yo "Aiden does a lot more than you think."
            yo "He’s really stepped up to the scoutmaster role these last few months, and that’s not even counting all the other work he does that you don’t even see. "
        "This camp wouldn't even function without Aiden.":
            $working = True
            $score_aiden += 2
            $score_top += 1
            show yoshi rage1 at p9_4
            voice audio.yoshi_v_what4
            yo "What are you talking about? This camp wouldn’t function without Aiden."
            yo "You don’t have any right to question his role considering how much he does for Camp Buddy, especially these last few months."

    show yoshi angry2 at p9_4
    voice audio.yoshi_v_conj3b
    yo "Aiden had to wake up the earliest to prepare meals and other essential needs for more than thirty people. Including yourself."
    yo "He also took care of the sanitation of facilities and occasional repairs on top of that, which he always handled without fail."

    show yoshi angry3 at p9_4
    voice audio.yoshi_v_conj5b
    yo "Now imagine that during a summer term with all the scouts too. And he still manages to participate in physical and wellness activities at the same time."

    show aiden2 worry2 at p9_3
    voice audio.aiden_v_yoshi4a
    a "Yoshi…"

    show yoshi angry5 at p9_4
    voice audio.yoshi_v_please1b
    yo "I request that you’d be more empathetic to everyone here as your co-workers."

    show emilia explain2 at p9_6
    voice audio.emilia_v_worry1
    e "I’m only telling things as they are. I can’t let an opportunity to point out legitimate flaws pass."

    show yoshi annoy4 at p9_4
    voice audio.yoshi_v_well1
    yo "I just think that everything you’ve brought up so far hasn’t been relevant to the project but are rather personal issues you have with us. "
    yo "You can’t expect me to stand by and not defend everyone, especially if you’re being unreasonable."

    show yoshi angry5 at p9_4
    voice audio.yoshi_v_rush4
    yo "If you’re the professional you say you are, then surely you can tell the difference between what you’ve said and what matters."

    show emilia panic3 at p9_6
    voice audio.emilia_v_agree1c1
    e "O-Of course I can! My only intent was—"

    show william serious2 at p9_5
    voice audio.william_v_angry1a
    w "I’ve heard enough."
    w "I think we can all agree that each department has had its own communication issues that can be improved upon."

    show william serious3 at p9_5
    voice audio.william_v_conj3a
    w "However, Ms. Komarova. It’s apparent to me that you’ve been failing to empathize with your co-workers, and it has led to high levels of tension in the project."
    w "May I remind you that as the inspector and as a representative of Clermont Inc., that while your job is to critique and point out flaws, you should do so in a more supportive manner."

    show william explain2 at p9_5
    voice audio.william_v_emilia1a
    w "As you’ve noted many times, the deadline is tight, and motivation is a key factor to ensuring completion."
    w "I am disappointed to be explaining all of this, as I thought a former alumnus would’ve understood these aspects better."

    show emilia panic6 at p9_6
    voice audio.emilia_v_wait1c
    e "Mr. Clermont, please allow me to explain—"

    show william angry6 at p9_5
    voice audio.william_v_dismiss1
    w "You’ve already explained plenty. Frankly, I am even considering that it may be in everyone’s best interest to reassign your position."

    show emilia panic4 at p9_6
    e "...!!"

    show yoshi talk1 at p9_4
    voice audio.yoshi_v_sir1
    yo "If I may, sir…"

    show emilia irked1 at p9_6
    show yoshi explain2 at p9_4
    voice audio.yoshi_v_emilia2
    yo "Outside of these issues, Emilia has done her job to the best of her abilities."
    yo "If you would allow us to fix the communication problems brought up, I’m sure we can still work this out."

    show william explain2 at p9_5
    voice audio.william_v_agree2a
    w "Very well. I’m glad that you’re willing to resolve this amongst yourselves."

    show emilia eyeroll5 at p9_6
    e "..."

    show william talk1 at p9_5
    voice audio.william_v_anyway1
    w "Regardless, knowing that everything is on track, it’s clear to me that you all have done an excellent job with the project so far."

    show william think3 at p9_5
    voice audio.william_v_conj5
    w "Moving forward, I’m sure everyone here is well aware that we will be pausing this coming winter season."
    w "We’re going to wait for the weather to pass to avoid any dangerous conditions that could harm the workers. "

    show william talk1 at p9_5
    voice audio.william_v_think1
    w "Originally, we planned to jump straight into administrative tasks and other integrations that could be done indoors."
    w "But, after reviewing the project’s progress over the last two months, I’ve decided that it’s in everyone’s best interest to take a few days off and let loose with a well-deserved break."

    show william happy3 at p9_5
    voice audio.william_v_laugh1
    w "With that being said, I took it upon myself to arrange a little getaway for the entire team!"

    hide goro2_autumn
    hide goro2 disappoint3
    show goro_autumn at p9_7
    show goro confused2 at p9_7
    voice audio.goro_v_confused1a1
    g "Getaway…?"

    show william comp2 at p9_5
    voice audio.william_v_impressed1a
    w "I've been so impressed with how hard you've all worked, so I thought it would be fitting to set up a celebratory trip! I booked an exclusive hotel for everyone to stay at this weekend!"

    show goro shock2 at p9_7
    voice audio.goro_v_unsure1b1
    g "A-Are you sure, Mr. Clermont? Your sponsorship has already done so much for us, I’m not sure if we should accept—"

    show william comp4 at p9_5
    voice audio.william_v_well1a
    w "Well, I believe it’s important to unwind, especially after several months of hard work. "

    show emilia annoy1 at p9_6
    show yoshi awkward1 at p9_4
    w "Besides, I think it would be a great opportunity to teambuild and improve personal relationships, don’t you think? "

    show william happy3 at p9_5
    voice audio.william_v_please1a
    w "Please use this trip as a chance to further get to know one another so that you can properly empathize with each other once work resumes."

    show goro comp2 at p9_7
    voice audio.goro_v_agree3b1
    g "Of course, sir... If that’s the case, we’ll do our best to meet your expectations."
    g "Thank you very much for your generosity."

    show william laugh1 at p9_5
    voice audio.william_v_amazed1
    w "Great! With that being said, I can schedule a shuttle to pick everyone up as early as tomorrow from Camp Buddy!"
    w "You have the entire night to prepare and pack up for your wonderful vacation!"

    show william happy2 at p9_5
    voice audio.william_v_bye2a
    w "If there are no more questions, then this meeting is adjourned."

    show goro happy1 at p9_7
    voice audio.goro_v_thanks2a1
    g "Thank you again, Mr. Clermont. We’ll take our leave then."

    show emilia rage2 at p9_6
    voice audio.emilia_v_hmph1a
    e "Hmph!"

    hide emilia_autumn
    hide emilia rage2
    with dissolve

    show yoshi awkward4 at p9_4
    voice audio.yoshi_v_ah1
    yo "Ah…! Please excuse me!"

    hide yoshi_autumn
    hide yoshi awkward4
    with dissolve

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black
    hide screen location
    hide screen timeline
    hide screen quick_menu
    $quick_menu = False
    with fade
    $ renpy.pause (2.0, hard=True)

    $ location = location_clermont
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_clermontlobby_day with fade

    show emilia_autumn at left2
    show emilia angry1 at left2
    show yoshi_autumn at right2
    show yoshi awkward4 at right2
    voice audio.yoshi_vsa7_line1
    yo "Emilia, wait! Can we please talk?"

    show emilia angry3 at left2
    voice audio.emilia_vsa7_line1
    e "What?! "

    show yoshi angry3 at right2
    voice audio.yoshi_vsa7_line2
    yo "What’s your problem?! You’ve been acting this way for months now!"

    play music heracleum_a loop
    show emilia rage4 at left2
    voice audio.emilia_vsa7_line2
    e "Seriously?! After everyone tore into me back there, you still have the nerve to attack me like this?!"

    show yoshi angry2 at right2
    voice audio.yoshi_vsa7_line3
    yo "I’m just trying to understand you!"

    show emilia rage6 at left2
    voice audio.emilia_vsa7_line3
    e "Understand me?! I tried to get back in touch with you from the start, and you never once reciprocated! "

    voice audio.emilia_vsa7_line4
    e "Here I was trying my hardest to help you and this stupid camp, but you didn’t think twice about humiliating me in front of everyone!"

    show yoshi rage1 at right2
    voice audio.yoshi_vsa7_line4
    yo "That’s not true, Emilia! I was only trying to reason with you! "

    voice audio.yoshi_vsa7_line5
    yo "We both know how hard everyone worked to reach our goals, but you still pointed out so many unnecessary things!"

    show yoshi angry3 at right2
    voice audio.yoshi_vsa7_line6
    yo "Can’t you just admit that you’re making a problem when there isn’t one?!"

    show emilia rage4 at left2
    voice audio.emilia_vsa7_line5
    e "I’m just doing my job! It’s not my fault that none of you can accept how wrong you all are! "

    show yoshi angry2 at right2
    voice audio.yoshi_vsa7_line7
    yo "You can’t expect me to just stand there while you berate everyone, especially Aiden!"

    voice audio.yoshi_vsa7_line8
    yo "Don’t think I haven’t noticed how much you’ve been belittling him since you first got here!"

    show yoshi angry6 at right2
    voice audio.yoshi_vsa7_line9
    yo "He’s taken it all in stride, and even been nice to you the entire time, but you still won’t let up!"

    show emilia rage5 at left2
    voice audio.emilia_vsa7_line6
    e "Aiden again?! All you ever talk about is him!"

    voice audio.emilia_vsa7_line7
    e "You know what, I’m done with you, Yoshinori. "

    show emilia upset5 at left2
    voice audio.emilia_vsa7_line8
    e "And I thought you were my friend..."

    voice audio.emilia_vsa7_line9
    e "You’ve changed."

    hide emilia_autumn
    hide emilia upset5
    with dissolve

    show yoshi sad1 at right2
    yo "..."

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black with fade
    yo "{i}After all this time, I guess the tension and stress of dealing with Emilia finally exploded out of me…{/i}"
    yo "{i}I do feel bad that I upset her as much as I did, but I couldn’t keep doing nothing.{/i}"
    yo "{i}It’s a good thing Mr. Clermont was so generous to offer us a trip to bond together… Maybe we can help resolve our issues there.{/i}"
    yo "{i}And after all those months of hard work, I think everyone could use a break.{/i}"

    $ renpy.pause (1.0, hard=True)
    yo "{i}Eventually we drove back to Camp Buddy and all began to pack for the trip.{/i}"

    scene cg black
    hide screen location
    hide screen timeline
    hide screen quick_menu
    $quick_menu = False
    with fade
    $ renpy.pause (2.0, hard=True)
    $ time_transition_sunset_to_night_winter()

    $ location = location_cabin
    $ time = timeline_timenight
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_quarters_autumn_night with fade
    play music ready_for_tomorrow loop
    play bgsound sfxloop_night loop

    show aiden2_sleep at left2
    show aiden2 worry5 at left2
    show yoshi2_sleep at right2
    show yoshi2 upset1 at right2
    voice audio.aiden_v_shock2b1
    a "Yikes… She really said all that?"

    show yoshi2 sad4 at right2
    voice audio.yoshi_v_yeah3
    yo "Yeah… I think I may have upset her even more than when we were with Mr. Clermont."

    show aiden2 sad4 at left2
    voice audio.aiden_v_unsure2a
    a "I dunno, Yoshi… Maybe you hanging out with me so much is starting to cause a problem. "
    a "Don’t you think it’d be easier for you to let me handle my work on my own?"

    hide yoshi2_sleep
    hide yoshi2 sad4
    show yoshi_sleep at right2
    show yoshi talk1 at right2
    voice audio.yoshi_v_no4
    yo "We don’t have to do that, Aiden. "
    yo "After working with you these past few months, I really got to see just how much stuff you have on your plate."

    show yoshi comp2 at right2
    voice audio.yoshi_v_please1c
    yo "It’s really not something one person can do. So please let me help you."

    show aiden2 upset5 at left2
    voice audio.aiden_v_confused1c1
    a "Ehh… If you’re sure…"

    show yoshi comp5 at right2
    voice audio.yoshi_v_comp4
    yo "Yeah! Don’t sweat it, Aiden!"

    show aiden2_sleep at p6_1
    show aiden2 upset5 at p6_1
    show yoshi_sleep at p6_2
    show yoshi comp5 at p6_2
    with move


    show darius_sleep at p6_4
    show darius norm3 at p6_4
    show lloyd_sleep at p6_3
    show lloyd pain4 at p6_3
    show goro_sleep at p6_5
    show goro norm1 at p6_5
    show jin_sleep at p6_6
    show jin_glasses at p6_6
    show jin norm4 at p6_6
    with dissolve

    voice audio.lloyd_v_shock4a2
    l "Gah! These suitcases sure are heavy!"

    show darius sigh5 at p6_4
    voice audio.darius_v_conj2a
    d "I told you to let me carry them for you…"

    show jin comp3 at p6_6
    voice audio.jin_v_thanks1c2
    j "Th-Thanks for carrying mine though, Sir Goro…"

    show goro happy1 at p6_5
    voice audio.goro_v_response2a1
    g "No problem."

    show yoshi shock2 at p6_2
    voice audio.yoshi_v_shock1a
    yo "Whoa… You guys are already packed? "

    show lloyd amazed3 at p6_3
    voice audio.lloyd_v_agree4a1
    l "Heck yeah! You guys don’t even know how excited I am for this trip! It’s been so long since I went on a vacation!"

    show darius think5 at p6_4
    voice audio.darius_v_conj1a1
    d "The last time was at a beach."

    show yoshi talk3 at p6_2
    voice audio.yoshi_v_oh1
    yo "Oh, we actually went to a beach too with the scouts not too long ago!"

    hide aiden2_sleep
    hide aiden2 upset5
    show aiden_sleep at p6_1
    show aiden talk2 at p6_1
    voice audio.aiden_v_yeah1a4
    a "Yeah, but that was like a work trip! This time we won’t have any responsibilities… and that’s basically never happened before!"

    show goro happy2 at p6_5
    voice audio.goro_v_agree4a2
    g "That’s exactly why I agreed to Mr. Clermont’s offer. We couldn’t pass up the chance to bond like this."

    show jin confuseddn2 at p6_6
    voice audio.jin_v_conj1c3
    j "I-I’ll be honest, the only outdoor vacation I’ve ever been on was at this camp…"

    show lloyd happy1 at p6_3
    voice audio.lloyd_v_conj1a3
    l "We’re booked at a hotel, though, so I’m sure it’ll be like a staycation at least. You’ll be comfortable with that, right? "

    show jin awkward3 at p6_6
    voice audio.jin_v_yeah2a
    j "Y-Yeah, I guess…"

    show aiden comp6 at p6_1
    voice audio.aiden_v_comp1a2
    a "Don’t worry Jin, I’m in the same boat as you! I’ve never been on a trip like this before."
    a "We’ll both be like headless chickens, haha!"

    show yuri_autumn at p9_9
    show yuri pain3 at p9_9
    with moveinright

    voice audio.yuri_v_groan1a
    yu "HNGHHHH…!!!"

    show aiden_sleep at p7_1
    show aiden comp6 at p7_1
    show lloyd_sleep at p7_2
    show lloyd happy1 at p7_2
    show darius_sleep at p7_3
    show darius think5 at p7_3
    show goro_sleep at p7_4
    show goro happy2 at p7_4
    show jin_sleep at p7_5
    show jin_glasses at p7_5
    show jin awkward3 at p7_5
    show yoshi_sleep at p7_6
    show yoshi shock3 at p7_6
    show yuri_autumn at p7_7
    show yuri pain3 at p7_7
    with move

    voice audio.yoshi_v_oh2
    yo "O-Oh…! Let me help you with that suitcase, Yuri!"

    show yuri pain6 at p7_7
    voice audio.yuri_v_groan1a
    yu "GAH!!" with vpunch

    show aiden shock3 at p7_1
    voice audio.aiden_v_shock1b1
    a "Whoa… What’s up with all the luggage, Yuri?"

    show yuri explain3 at p7_7
    voice audio.yuri_v_actually1a
    yu "This is for me and Dad! I always pack for him during trips like this or he’ll forget something!"

    hide goro_sleep
    hide goro happy2
    show goro2_sleep at p7_4
    show goro2 disappoint2 at p7_4
    voice audio.goro_v_ehem1a
    g "*ehem* It’s not that I forget things, it’s more that I only bring what I need."

    show yuri tease2 at p7_7
    voice audio.yuri_v_yeah2b1
    yu "Oh yeah? Remember when we went to the beach last summer and you kept asking me for your razor?"
    yu "You were so cranky you didn’t get to shave that morning, especially before you got your coffee!"

    show goro2 sigh1 at p7_4
    voice audio.goro_v_sigh1a
    g "*sigh* Did you really have to share that with everyone, Yuri?"
    g "And besides, we don’t need to pack as many essential things. Usually hotels provide them, don’t they?"

    show yuri bold4 at p7_7
    voice audio.yuri_v_confident1b
    yu "Better to be safe than sorry!"

    show yoshi think2 at p7_6
    voice audio.yoshi_v_think2
    yo "It makes me wonder what kind of hotel it is. Mr. Clermont didn’t really give us any details."

    hide aiden_sleep
    hide aiden shock3
    show aiden2_sleep at p7_1
    show aiden2 think5 at p7_1
    voice audio.aiden_v_think1a1
    a "Yeah. What are we supposed to pack even?"

    show yuri happy1 at p7_7
    voice audio.yuri_v_well1a
    yu "Well, I’d make sure and pack some cold weather clothes! It’s getting a lot chillier lately and winter’s coming really soon!"

    show jin think3 at p7_5
    voice audio.jin_v_laugh1a
    j "I just hope there’s a wi-fi connection there… that’s all I need to survive."

    show lloyd tease2 at p7_2
    voice audio.lloyd_v_jin4a
    l "Where’s your sense of camaraderie, Jin? There’s no better connection than the connection through real life experiences with your friends, am I right? "

    show darius disgust4 at p7_3
    voice audio.darius_v_cringe1a
    d "Cringe."

    show lloyd talk1 at p7_2
    voice audio.lloyd_v_greet2a2
    l "Hey, I’m being serious!"

    hide aiden2_sleep
    hide aiden2 think5
    show aiden_sleep at p7_1
    show aiden tease1 at p7_1
    voice audio.aiden_v_oho1a
    a "Of course, Mr. ‘Sirius’!"

    show lloyd tease3 at p7_2
    voice audio.lloyd_v_greet2b1
    l "EYY!"

    show aiden wink2 at p7_1
    voice audio.aiden_v_hey1a2
    a "EYYY!!"

    show darius bored1 at p7_3
    d "*facepalms*"

    show jin comp2 at p7_5
    voice audio.jin_v_comp2a1
    j "I guess I’m just not used to having friends to hang out with… But I promise I’ll try not to spend the whole trip on my phone or computer!"

    show yuri angry1 at p7_7
    voice audio.yuri_v_ugh2a
    yu "I’m just glad I don’t have to hear Emilia boss us around for at least a couple of days."
    yu "You guys have no idea how much just her voice has been irritating me for the last few months!"

    show goro2 bored1 at p7_4
    voice audio.goro_v_annoyed1a1
    g "Trust us, dear. We know."
    g "But can you at least try to get along with her like Mr. Clermont asked?"

    show yuri rage2 at p7_7
    voice audio.yuri_v_conj2d1
    yu "It’s not even about getting along. She’s just a flat-out bitch! "

    show yoshi explain2 at p7_6
    voice audio.yoshi_v_comp7
    yo "Now calm down, Yuri. Like Mr. Clermont said, this trip might be a good chance for us to unwind after all the stress from work."

    hide aiden_sleep
    hide aiden wink2
    show aiden2_sleep at p7_1
    show aiden2 sigh1 at p7_1
    voice audio.aiden_v_relief1a2
    a "I’m just relieved you said something back there, Yoshi."

    show yoshi worry2 at p7_6
    voice audio.yoshi_v_aiden4
    yo "Aiden…"

    show yuri bold2 at p7_7
    voice audio.yuri_v_yeah2a3
    yu "Oh yeah! That was so satisfying! In my head I was like “Yesss! Yesss! Get her, Yoshi!”"

    show jin sad2 at p7_5
    voice audio.jin_v_sigh2a
    j "Ms. Emilia is so scary… I thought she’d be a lot less aggressive in front of Mr. Clermont, but she didn’t even think twice about calling each of us out like that…"

    show lloyd annoy5 at p7_2
    voice audio.lloyd_v_annoyed1a3
    l "She’s so business-minded she couldn’t care less about our feelings! I bet that was the ugly side of a Capricorn talking!"
    l "But that explosive attitude sounds like something an Aries would do – they can be control freaks too."

    show darius annoy2 at p7_3
    voice audio.darius_v_ugh1
    d "She’s neither. She’s just mean. "

    show goro2 disappoint3 at p7_4
    voice audio.goro_v_conj9b2
    g "I was honestly about to say something, but I’m glad Yoshinori stepped in before I did. If I had, I would’ve been much more blunt with her."

    hide yoshi_sleep
    hide yoshi worry2
    show yoshi2_sleep at p7_6
    show yoshi2 sad4 at p7_6
    hide jin_sleep
    hide jin_glasses
    hide jin sad2
    show jin_sleep at p7_5
    show jin_glasses at p7_5
    show jin sad2 at p7_5
    voice audio.yoshi_v_actually2a
    yo "I-I was actually thinking about it on our way home… As embarrassing as it was to argue with Emilia in front of Mr. Clermont, I had to do it because…"
    $working = False
    $shuffle_menu()
    menu():
        yo "I-I was actually thinking about it on our way home… As embarrassing as it was to argue with Emilia in front of Mr. Clermont, I had to do it because…{fast}"
        "It wasn't a productive conversation.":
            $working = True
            $score_bot += 1
            show yoshi2 angry5 at p7_6
            voice audio.yoshi_v_sigh3a
            yo "It wasn’t a productive conversation anymore."

            show yuri angry2 at p7_7
            voice audio.yuri_v_response2b1
            yu "Ugh! I know right?! "
        "She was trying to discredit everyone.":
            $working = True
            $score_top += 1
            hide yoshi2_sleep
            hide yoshi2 sad4
            show yoshi_sleep at p7_6
            show yoshi angry5 at p7_6
            voice audio.yoshi_v_sigh3a
            yo "She was trying to discredit all of us after our hard work."

            show yuri angry2 at p7_7
            voice audio.yuri_v_response2b1
            yu "Ugh! I know right?! "
        "She was saying hurtful things.":
            $working = True
            $score_aiden += 2
            $score_bot += 1
            hide yoshi2_sleep
            hide yoshi2 sad4
            show yoshi_sleep at p7_6
            show yoshi angry5 at p7_6
            voice audio.yoshi_v_sigh3a
            yo "She was saying so many hurtful things, especially about Aiden."

            show aiden2 worry2 at p7_1
            voice audio.aiden_v_yoshi4a
            a "Yoshi…"

            show yuri angry2 at p7_7
            voice audio.yuri_v_response2b1
            yu "Ugh! I know right?! I didn’t mind when she was talking shit about me! But why did she have to pick on Aiden for some reason?!"

            hide aiden2_sleep
            hide aiden2 worry2
            show aiden_sleep at p7_1
            show aiden comp2 at p7_1
            voice audio.aiden_v_comp1a2
            a "Don’t worry about me, you guys…! I swear I’m fine!"
        "She was so disrespectful.":
            $working = True
            $score_aiden += 2
            $score_top += 1
            hide yoshi2_sleep
            hide yoshi2 sad4
            show yoshi_sleep at p7_6
            show yoshi angry5 at p7_6
            voice audio.yoshi_v_sigh3a
            yo "She was being so disrespectful, especially to Aiden."

            show aiden2 worry2 at p7_1
            voice audio.aiden_v_yoshi4a
            a "Yoshi…"

            show yuri angry2 at p7_7
            voice audio.yuri_v_response2b1
            yu "Ugh! I know right?! I didn’t mind when she was talking shit about me! But why did she have to pick on Aiden for some reason?!"

            hide aiden2_sleep
            hide aiden2 worry2
            show aiden_sleep at p7_1
            show aiden comp2 at p7_1
            voice audio.aiden_v_comp1a2
            a "Don’t worry about me, you guys…! I swear I’m fine!"

    show yuri angry6 at p7_7
    voice audio.yuri_v_annoyed1a
    yu "I’m already at my wits end with that girl. I don’t think we’ll ever be friends outside of work."

    hide yoshi2_sleep
    hide yoshi2 angry5
    show yoshi_sleep at p7_6
    show yoshi talk1 at p7_6
    voice audio.yoshi_v_but2
    yo "We don’t have to be friends with Emilia, but we don’t have to antagonize her either."
    yo "We just have to learn to not take her personal remarks seriously and focus on our jobs."

    show yuri rage3 at p7_7
    voice audio.yuri_v_annoyed2a
    yu "But if she crosses the line like that again, I’m not going to hold myself back anymore!"

    show lloyd sigh5 at p7_2
    voice audio.lloyd_v_sigh1d
    l "All this negative energy is exactly why we need to go on a vacation detox."

    show darius laugh3 at p7_3
    voice audio.darius_v_laugh2a
    d "Vacay."

    hide goro2_sleep
    hide goro2 disappoint3
    show goro_sleep at p7_4
    show goro talk1 at p7_4
    hide jin_sleep
    hide jin_glasses
    hide jin sad2
    show jin_sleep at p7_5
    show jin_glasses at p7_5
    show jin sad2 at p7_5
    voice audio.goro_v_agree4a2
    g "Exactly. This is our chance to spend time with each other and loosen up."

    hide aiden2_sleep
    hide aiden2
    show aiden_sleep at p7_1
    show aiden tease1 at p7_1
    voice audio.aiden_v_oho1a
    a "I like where this is going~"

    hide yoshi_sleep
    hide yoshi talk1
    show yoshi2_sleep at p7_6
    show yoshi2 sigh4 at p7_6
    hide jin_sleep
    hide jin_glasses
    hide jin sad2
    show jin_sleep at p7_5
    show jin_glasses at p7_5
    show jin sad2 at p7_5
    voice audio.yoshi_v_sigh3a
    yo "Not again with the ‘loose’ jokes, Aiden… Let’s just pack."

    hide jin_sleep
    hide jin sad2
    hide jin_glasses
    show jin2_sleep at p7_5
    show jin2 scheme2 at p7_5
    voice audio.jin_v_gulp1a
    j "Did you just say ‘fuck’?"

    show yoshi2 annoy2 at p7_6
    voice audio.yoshi_v_really6
    yo "Now you guys are just stretching it."

    show aiden bold2 at p7_1
    voice audio.aiden_v_laugh1b2
    a "STRETCH?!"

    show goro sigh1 at p7_4
    voice audio.goro_v_sigh1a
    g "*sigh*"

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black
    hide screen location
    hide screen timeline
    hide screen quick_menu
    $quick_menu = False
    with fade
    play sound sfx_bagdrop
    $ renpy.pause (2.0, hard=True)

    $ location = location_cabin
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_quarters_autumn_night with fade
    play music ready_for_tomorrow loop
    play bgsound sfxloop_night loop

    show yoshi_sleep at left2
    show yoshi norm1 at left2
    show aiden_sleep at right2
    show aiden norm2 at right2
    voice audio.yoshi_v_alright2
    yo "And there we go! That should be all our stuff, Aiden!"

    show aiden happy1 at right2
    voice audio.aiden_v_thanks1a1
    a "Thanks for helping me pack, Yoshi! "

    show yoshi happy2 at left2
    voice audio.yoshi_v_response3a
    yo "No problem!"

    show aiden excited1 at right2
    voice audio.aiden_v_excited1a
    a "I know this is gonna sound silly, but I can’t wait to sleep! The faster I go to bed, the sooner the trip starts!"

    show yoshi bold2 at left2
    voice audio.yoshi_v_laugh1
    yo "I get it! I’m just as excited as you are!"

    show aiden excited3 at right2
    voice audio.aiden_v_relief1a1
    a "I mean… I can’t help it! After being so busy for the last two months, we finally get some time to relax!"
    a "I know we’ve been spending a lot more time together lately, but this time around it’s a hundred percent quality time! No doing laundry or washing dishes, hahaha!"

    show yoshi excited1 at left2
    voice audio.yoshi_v_yeah2
    yo "Yeah! Let’s make sure we have a great time on this vacation!"

    play sound sfx_typing
    show yoshi confused2 at left2
    voice audio.yoshi_v_think1b
    yo "Hm? Is that…?"

    show aiden play2 at right2
    voice audio.aiden_v_jin3a
    a "No use trying to hide under that blanket, Jin. We can hear you on your computer~!"

    show yoshi_sleep at left
    show yoshi confused2 at left
    show aiden_sleep at center
    show aiden play2 at center
    with move

    show jin_sleep at right
    show jin_glasses at right
    show jin panic2 at right
    with dissolve

    voice audio.jin_v_ah4c
    j "A-Ah…! I’m sorry, was my keyboard too loud?"

    show aiden tease2 at center
    voice audio.aiden_v_no2a1
    a "Nah~ What porn are you watching? Mind sharing?"

    hide yoshi_sleep
    hide yoshi confused2
    show yoshi2_sleep at left
    show yoshi2 sigh4 at left
    voice audio.yoshi_v_sigh3a
    yo "*sigh* You know he’s working, Aiden…"

    show jin talk4 at right
    voice audio.jin_v_oh3a
    j "O-Oh…! I’m not working either!"
    j "Although, I guess technically you could say that I’m working on something…"

    show jin happy1 at right
    voice audio.jin_v_yoshi4c
    j "It’s that side thing we started, Yoshi. I never had the time to get back to it since we’ve been so busy lately."

    show aiden pout4 at center
    voice audio.aiden_v_hey1e2
    a "Heeey…! You didn’t tell me Jin here was your side-ho, Yoshi! You guys could’ve invited me for that kind of fun!"

    hide yoshi2_sleep
    hide yoshi2 sigh4
    show yoshi_sleep at left
    show yoshi panic4 at left
    voice audio.yoshi_v_wait2b
    yo "Wait, what…? No, Aiden!"

    show jin daydream2 at right
    voice audio.jin_v_fudan1a2
    j "*cough* I wish it was. "

    show yoshi talk3 at left
    voice audio.yoshi_v_actually1a
    yo "Jin and I have this little website project where we’re transcribing Yuri’s journal and restoring the photos for a blog! "

    hide aiden_sleep
    hide aiden pout4
    show aiden2_sleep at center
    show aiden2 confused2 at center
    voice audio.aiden_v_confused2a2
    a "You lost me at website…"

    hide yoshi_sleep
    hide yoshi talk3
    show yoshi2_sleep at left
    show yoshi2 comp6 at left
    voice audio.yoshi_v_laugh6
    yo "Ahehe… I didn’t really understand all the tech stuff at first either, but Jin here has been teaching me a lot!"

    hide yoshi2_sleep
    hide yoshi2 comp6
    show yoshi_sleep at left
    show yoshi happy2 at left
    voice audio.yoshi_v_oh1
    yo "Oh, if you’re not too tired, Aiden, why don’t we help Jin finish up tonight?"

    hide aiden2_sleep
    hide aiden2 confused2
    show aiden_sleep at center
    show aiden play2 at center
    voice audio.aiden_v_oho1a
    a "Oho~ Don’t mind if I do~"

    show jin fudan1 at right
    voice audio.jin_v_gulp1a
    j "*gulp*"

    show yoshi bold2 at left
    voice audio.yoshi_v_rush1
    yo "Come on! Let’s get on his bunk and work on tonight’s entry! "

    hide jin_sleep
    hide jin fudan1
    hide jin_glasses
    show jin2_sleep at right
    show jin2 fudan3 at right
    show jin2_glasses at right
    voice audio.jin_v_wah2b
    j "W-Wah! Is it finally happening?!"

    # JMA1
    $renpy.choice_for_skipping()
    scene cg white
    $ quick_menu = False
    $ say_box = False
    hide screen location
    hide screen timeline
    hide screen quick_menu
    with Dissolve(2.0)
    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    $ global minigame_id
    $ minigame_id = 'jmA1'
    $ renpy.call(minigame_id, 'night')

label day2_aiden_postmg:

    hide screen location
    hide screen timeline
    hide screen quick_menu
    $quick_menu = False
    scene cg white with Dissolve(2.0)
    $past_scene = True

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black
    hide screen location
    hide screen timeline
    hide screen quick_menu
    $quick_menu = False
    with fade
    $ renpy.pause (2.0, hard=True)

    $ location = location_tent
    $ day = "??"
    $ time = timeline_timesunset
    $ season = season_summer
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_tent_past_sunset with fade
    play music go_with_the_flow_slow loop
    play bgsound sfxloop_forest loop

    show yaiden_casual at left2
    show yaiden norm1 at left2
    show yyoshi_camp at right2
    show yyoshi relief4 at right2
    voice audio.yyoshi_v_relief1
    yo "Whew! Finally, it’s done!"
    yo "Thanks for helping me set up the tent, Aiden! Couldn’t have done it without you!"

    show yaiden comp6 at left2
    voice audio.yaiden_v_welcome1a
    a "You’re welcome, Yoshi!"
    a "Hehe, you guys sure had a long day today, huh?"

    show yyoshi tired4 at right2
    voice audio.yyoshi_v_sigh2
    yo "Yeaaahhh… I thought my legs were gonna break off from that ten-mile hike!"
    yo "Not to mention we had that foraging activity! All I could gather were mushrooms and herbs… And that’s supposed to be our dinner too…"

    show yaiden bold2 at left2
    voice audio.yaiden_v_comp1a1
    a "Don’t worry, Yoshi! We brought meat!"
    a "I’m sure Dad can make something really tasty out of what you guys gathered!"

    show yaiden grin1 at left2
    voice audio.yaiden_v_well1a1
    a "He’s gonna let me help cook today too, so it’s gonna be extra special!"

    show yyoshi amazed1 at right2
    voice audio.yyoshi_v_amazed1a
    yo "Wow!! I can’t wait! I can always count on you and your dad to cook up something good!"
    yo "I gotta say though, you guys were pretty busy yourselves today too."

    show yyoshi worry2 at right2
    voice audio.yyoshi_v_sad4
    yo "You had to hike, and then prepare everyone’s meals on top of that…"

    show yaiden comp2 at left2
    voice audio.yaiden_v_alright3a
    a "It’s alright! It’s my job to help after all!"

    show yyoshi worry5 at right2
    voice audio.yyoshi_v_sad5
    yo "Now I feel bad that I get to do all these activities while all you do is work…"
    yo "I gotta ask the scoutmasters to let you join for the next one!"

    show yaiden awkward2 at left2
    voice audio.yaiden_v_confused1c1
    a "Ehhh… You don’t have to do that, Yoshi! "

    show yyoshi bold2 at right2
    voice audio.yyoshi_v_comp4
    yo "Don’t worry, I can just sneak you in!"

    show yaiden sigh1 at left2
    voice audio.yaiden_v_sigh1a
    a "*sigh* Yoshi… You’ve already done so much for me."
    a "I’m already happy enough getting to spend time with you, you know?"

    show yyoshi comp2 at right2
    voice audio.yyoshi_v_aww2
    yo "Aww, that’s so sweet, Aiden! This is why you’re my best friend!"

    show yaiden comp3 at left2
    voice audio.yaiden_v_laugh1b1
    a "Hehe."

    show yyoshi_camp at right3
    show yyoshi relief4 at right3
    with move

    play sound sfx_clotheschanging
    voice audio.yyoshi_v_relief2
    yo "Fwah! It feels so nice to rest my legs after all that walking!"

    $ renpy.pause (1.0, hard=True)
    show yyoshi comp2 at right3
    voice audio.yyoshi_v_awkward1
    yo "Aren’t you gonna lie down? You must be pretty tired too!"

    show yaiden think2 at left2
    voice audio.yaiden_v_yeah1c1
    a "Yeah, I guess I kinda am."

    show yyoshi comp5 at right3
    voice audio.yyoshi_v_here1
    yo "Here, there’s plenty of space for both of us!"

    show yaiden_casual at left3
    show yaiden relief2 at left3
    with move

    voice audio.yaiden_v_relief1a1
    a "Whew… You’re right.  Now that I’m laying down, I can’t feel my legs anymore, haha!"

    show yyoshi happy2 at right3
    voice audio.yyoshi_v_idea1
    yo "Oh, I just got an idea! You should move into our cabin from now on!"

    show yaiden worry2 at left3
    voice audio.yaiden_v_what4a
    a "Y-You mean sleep together with you and all the scouts? I don’t think I’m allowed to…"

    show yyoshi laugh2 at right3
    voice audio.yyoshi_v_laugh2a
    yo "It doesn’t say anywhere in the camp rules that you can’t! So, you have no excuses, hahaha!"

    show yaiden explain2 at left3
    voice audio.yaiden_v_well1c1
    a "Well… I’d really like that. I know Dad wouldn’t mind."

    show yyoshi play2 at right3
    voice audio.yyoshi_v_confident1
    yo "Consider it done then! Yuri and I can arrange that with the president! *wink*"

    show yaiden comp3 at left3
    voice audio.yaiden_v_sheesh2a
    a "Sheesh… I dunno what to say, Yoshi."

    show yyoshi play3 at right3
    voice audio.yyoshi_v_laugh1
    yo "Say, yes?"

    show yaiden comp6 at left3
    voice audio.yaiden_v_alright1b
    a "Hehe, alright, you got me."

    show yyoshi grin1 at right3
    voice audio.yyoshi_v_alright5
    yo "Score! I just got the best roommate!"

    show yaiden_casual at center
    show yaiden comp6 at center
    with move

    show cg fade at truecenter
    show fxma1 1 at fx_pos
    with dissolve

    voice audio.yaiden_vsa73_line1
    a "Thanks, Yoshi… "

    voice audio.yyoshi_vsa73_line1
    yo "Hehe, don’t say thanks yet until you’re fully moved in."

    voice audio.yaiden_vsa73_line2
    a "Alright…"

    show fxma1 2 at fx_pos with dissolve
    $ renpy.pause (2.0, hard=True)

    show fxma1 3 at fx_pos with dissolve
    voice audio.yyoshi_vsa73_line2
    yo "*yawn* Now I’m feeling kinda sleepy…"

    voice audio.yaiden_vsa73_line3
    a "This is nice…"

    show fxma1 4 at fx_pos with dissolve
    yo "..."

    $ renpy.pause (2.0, hard=True)
    show fxma1 5 at fx_pos with vpunch
    voice audio.yyuri_v_kyaa1
    yu "KYAAAAA!!!!"

    hide fxma1 5
    hide cg fade
    play music here_they_come loop
    show yyuri_camp at p5_2
    show yyuri angry2 at p5_2
    show yaiden_casual at p5_4
    show yaiden shock1 at p5_4
    show yyoshi_camp at p5_5
    show yyoshi shock1 at p5_5
    show yyoshi_blush1 at p5_5
    voice audio.yyuri_v_idea3b1
    yu "So that’s where you two were!" with vpunch

    show yyoshi shock2 at p5_5
    voice audio.yyoshi_v_yuri9a
    yo "Gosh, Yuri...! You scared me!"

    show yyuri drool3 at p5_2
    voice audio.yyuri_v_fujo4b
    yu "AM I SEEING WHAT I THINK I’M SEEING?!"
    yu "Two boys cuddling in a tent, zero feet apart ’cause they’re very much gay~"

    show yaiden confused2 at p5_4
    voice audio.yaiden_v_confused1a1
    a "Eh? What’s going on?"

    show yyoshi sigh1 at p5_5
    voice audio.yyoshi_v_sigh2
    yo "*sigh* It’s just another one of Yuri’s episodes…"

    show yyuri jizz1 at p5_2
    voice audio.yyuri_v_shock1a3
    yu "OH NO! Did I interrupt a very intimate love-making session?!"

    show yyoshi awkward4 at p5_5
    voice audio.yyoshi_v_wait3
    yo "W-Wait…! L-Love-making?!"

    show yyuri jizz4 at p5_2
    voice audio.yyuri_v_fujo1b1
    yu "With Yoshi’s arms lovingly entwined around Aiden’s slim yet chiseled body, they share each other’s heat…"
    yu "Passionately, Yoshi makes a tender thrust, grinding their bodies ever so softly~"

    show yyoshi panic4 at p5_5
    voice audio.yyoshi_v_yuri9b
    yo "Y-Yuri…!!"

    show yaiden laugh1 at p5_4
    voice audio.yaiden_v_laugh2a1
    a "Hahaha! "

    show andre_camp at p5_1
    show andre talk3 at p5_1
    with dissolve

    voice audio.andre_v_aiden1b
    u "Aiden, it’s time to make di—"

    show yyoshi scared3 at p5_5
    voice audio.yyoshi_v_shock2a
    yo "WAH! Mr. Andre, it’s not what you think…!!"

    show yyuri fangirl2 at p5_2
    voice audio.yyuri_v_fujo5a
    yu "The shocking turn of events reveals the forbidden affair!"

    show andre confused2 at p5_1
    voice audio.andre_v_eh1b
    u "Eh? I’m not sure I understand…"

    show yaiden_casual at p5_2
    show yaiden talk1 at p5_2
    show yyuri_camp at p5_3
    show yyuri fangirl2 at p5_3
    with move

    voice audio.yaiden_v_dad3a
    a "Oh, hey Dad! It’s probably time to cook dinner, right?"

    show andre happy1 at p5_1
    voice audio.andre_v_agree3b1
    u "Yep! Now if you both don’t mind, I’ll be taking my little chef to work!"

    show yaiden happy1 at p5_2
    voice audio.yaiden_v_bye1a
    a "Seeya later, you two!"

    hide andre_camp
    hide andre happy1
    hide yaiden_casual
    hide yaiden happy1
    with dissolve

    show yyuri drool5 at p5_3
    voice audio.yyuri_v_fujo1b2
    yu "Alas… The threads of fate have snapped, and only time will tell if destiny shall bring them back together again…"

    show yyoshi sigh1 at p5_5
    voice audio.yyoshi_v_yuri6
    yo "*sigh* Yuri…"

    hide screen location
    hide screen timeline
    hide screen quick_menu
    $quick_menu = False
    scene cg white with Dissolve(2.0)
    $past_scene = False

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black
    hide screen location
    hide screen timeline
    hide screen quick_menu
    $quick_menu = False
    with fade
    $ renpy.pause (2.0, hard=True)

label daya2_postfb:
    $ location = location_cabin
    $ day = "77"
    $ time = timeline_timenight
    $ season = season_winter
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_quarters_autumn_night with fade
    play bgsound sfxloop_night loop

    show yoshi_sleep at left2
    show yoshi happy1 at left2
    show aiden_sleep at right2
    show aiden norm1 at right2
    voice audio.yoshi_v_alright2
    yo "Alright, this entry is done, but I can’t believe it’s already past midnight! "
    yo "We didn’t even notice how long we were working on this. I can see how you struggle with the concept of time, Jin! "

    show aiden laugh1 at right2
    voice audio.aiden_v_laugh2a1
    a "Look who you’re talking to."

    voice audio.jin_v_yawn1a
    j "*snores*"

    hide yoshi_sleep
    hide yoshi happy1
    show yoshi2_sleep at left2
    show yoshi2 comp6 at left2
    voice audio.yoshi_v_laugh6
    yo "Ahehe… This is the first time I’ve seen him asleep at night."
    yo "Let me just tuck him in, then let’s get off his bunk."

    show aiden comp2 at right2
    voice audio.aiden_v_aww3a
    a "Aww, isn’t that cute? You sound just like my dad right now, Yoshi~!"

    hide yoshi2_sleep
    hide yoshi2 comp6
    show yoshi_sleep at left2
    show yoshi annoy3 at left2
    voice audio.yoshi_v_ehem1b
    yo "You better not start calling me Gramps too."

    show aiden laugh3 at right2
    voice audio.aiden_v_laugh2a1
    a "Hahaha!"

    show yoshi happy2 at left2
    voice audio.yoshi_v_well1
    yo "Everybody else is already asleep, should we join them?"

    show aiden happy1 at right2
    voice audio.aiden_v_agree1a1
    a "Yup!"

    show yoshi relief2 at left2
    voice audio.yoshi_v_goodpm4
    yo "Good night, Aiden!"

    show aiden relief2 at right2
    voice audio.aiden_v_goodeve1a2
    a "Good night, Yoshi~"

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black
    hide screen location
    hide screen timeline
    hide screen quick_menu
    $quick_menu = False
    with fade
    play sound sleeping_time
    $ time_transition_night_to_day_winter()
    $ renpy.pause (2.0, hard=True)
    jump day3_aiden
