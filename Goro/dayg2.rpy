label day2_goro:
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
    show yoshi_autumn at p9_3
    show yoshi norm1 at p9_3
    show lloyd_autumn at p9_2
    show lloyd norm2 at p9_2
    show goro_autumn at p9_4
    show goro happy1 at p9_4
    show william_formal at p9_5
    show william norm1 at p9_5
    show aiden_autumn at p9_7
    show aiden norm1 at p9_7
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

    show goro happy3 at p9_4
    voice audio.goro_v_conj7a
    g "If you need any more details, you can find them in the report we’ve provided."

    show william comp4 at p9_5
    voice audio.william_v_impressed2a
    w "Excellent. But before we conclude this meeting, I have other concerns that I would like to discuss with everyone."

    show goro confused2 at p9_4
    voice audio.goro_v_oh3b
    g "What is it, Mr. Clermont?"

    show william explain2 at p9_5
    voice audio.william_v_well1b
    w "Well, throughout the previous months I received separate reports from our inspector."

    show darius shock4 at p9_1
    show lloyd confused2 at p9_2
    show aiden shock1 at p9_7
    show yoshi shock1 at p9_3
    show emilia play2 at p9_6
    show goro shock1 at p9_4
    show yuri annoy1 at p9_8
    show jin shock4 at p9_9
    w "I know that we’ve achieved our preliminary goals, but based on Ms. Komarova’s account, it seems that there were difficulties encountered along the way."

    hide goro_autumn
    hide goro shock1
    show goro2_autumn at p9_4
    show goro2 think5 at p9_4
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

    show yoshi angry2 at p9_3
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
    show goro_autumn at p9_4
    show goro explain2 at p9_4
    voice audio.goro_v_conj6a1
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

    show emilia angry5 at p9_6
    voice audio.emilia_v_conj3b1
    e "Moving forward, I suggest skipping these nonsense leisure activities and using your spare time to contribute to the project, considering we’re in crunch time."

    hide goro_autumn
    hide goro explain2
    show goro2_autumn at p9_4
    show goro2 disappoint3 at p9_4
    voice audio.goro_v_annoyed1a1
    g "It should be obvious that these routines are for health and wellness, not leisure. Which I’m sure you’ll agree is a requisite for labor-intensive jobs such as the ones Mr. Najjar and Mr. Sirius have."

    show goro2 angry2 at p9_4
    voice audio.goro_v_insult1a1
    g "Moreso, it’s entirely unreasonable to demand any person to commit themselves to business outside of work hours. That’s just straight up unethical."
    g "Regardless of our schedules and routines, we all adjusted to each other and finished the work according to all the deadlines."

    show yuri irked1 at p9_8
    voice audio.yuri_v_yeah1c1
    yu "Yeah! No one snooped around and called you out for your personal time!"

    show emilia annoy2 at p9_6
    voice audio.emilia_v_yuri7
    e "Which brings me to another issue: Ms. Nomoru’s attitude problem. She’s very hostile towards me, as you can see."

    show yuri rage1 at p9_8
    voice audio.yuri_v_what5a
    yu "Attitude problem?! Why I—"

    hide aiden_autumn
    hide aiden shock1
    show aiden2_autumn at p9_7
    show aiden2 worry5 at p9_7
    hide emilia_autumn
    hide emilia annoy2
    show emilia_autumn at p9_6
    show emilia annoy2 at p9_6
    voice audio.aiden_v_yuri6a
    a "*whispers* Yuri, calm down."

    hide aiden2_autumn
    hide aiden2 worry5
    show aiden_autumn at p9_7
    show aiden panic1 at p9_7
    hide emilia_autumn
    hide emilia annoy2
    show emilia_autumn at p9_6
    show emilia angry2 at p9_6
    voice audio.emilia_v_aiden6
    e "And you, Mr. Flynn! You continue to exhibit indecent and explicit behavior around the camp despite my previous warnings!"
    e "This leads to distractions that only causes more time lost on the project! "

    show goro2 confused3 at p9_4
    voice audio.goro_v_question1a1
    g "How exactly do you think that has any serious effect on our productivity?"
    g "And even so, the people working on this project aren’t machines – you can’t prohibit them from expressing themselves."

    show emilia angry6 at p9_6
    voice audio.emilia_v_celebrate1a
    e "And last but not least, Mr. Nagira."

    show yoshi panic1 at p9_3
    yo "...!"

    show emilia angry3 at p9_6
    voice audio.emilia_v_tsk1b
    e "You and Mr. Nomoru completely disregarded the plan I had laid out, repeatedly performing tasks out of your scope like headless chickens."

    hide yoshi_autumn
    hide yoshi panic1
    show yoshi2_autumn at p9_3
    show yoshi2 panic2 at p9_3
    hide lloyd_autumn
    hide lloyd annoy2
    show lloyd_autumn at p9_2
    show lloyd annoy2 at p9_2
    voice audio.yoshi_v_what3
    yo "What…?"

    show emilia rage4 at p9_6
    voice audio.emilia_v_angry1a
    e "You refused to follow the schedule I made to maximize efficiency only to blindly obey the whims of the camp president!"

    $ working = False
    $ shuffle_menu()
    menu():
        e "You refused to follow the schedule I made to maximize efficiency only to blindly obey the whims of the camp president!{fast}"
        "You're not the boss of me.":
            $ working = True
            $ score_goro += 1
            $ score_top += 1
            hide yoshi2_autumn
            hide yoshi2 panic2
            show yoshi_autumn at p9_3
            show yoshi angry2 at p9_3
            hide lloyd_autumn
            hide lloyd annoy2
            show lloyd_autumn at p9_2
            show lloyd annoy2 at p9_2
            voice audio.yoshi_v_disagree1b
            yo "I’m sorry, but you’re not in charge here, Sir Goro is."

            show emilia panic4 at p9_6
            e "...!"
        "That's not the case.":
            $ working = True
            $ score_goro += 1
            $ score_bot += 1
            hide yoshi2_autumn
            hide yoshi2 panic2
            show yoshi_autumn at p9_3
            show yoshi angry2 at p9_3
            hide lloyd_autumn
            hide lloyd annoy2
            show lloyd_autumn at p9_2
            show lloyd annoy2 at p9_2
            voice audio.yoshi_v_disagree1b
            yo "Th-That’s not what happened, Emilia! "
            yo "It’s only natural that unexpected things happen during a project, and Sir Goro and I dealt with them as they came up."
        "You're the one causing delays.":
            $ working = True
            $ score_goro += 2
            $ score_top += 1
            hide yoshi2_autumn
            hide yoshi2 panic2
            show yoshi_autumn at p9_3
            show yoshi angry2 at p9_3
            hide lloyd_autumn
            hide lloyd annoy2
            show lloyd_autumn at p9_2
            show lloyd annoy2 at p9_2
            voice audio.yoshi_v_disagree1b
            yo "I’m sorry, but if anyone has been causing delays here, it’s you."

            show emilia panic4 at p9_6
            e "...!"
        "Sir Goro knows what's best.":
            $ working = True
            $ score_goro += 2
            $ score_bot += 1
            hide yoshi2_autumn
            hide yoshi2 panic2
            show yoshi_autumn at p9_3
            show yoshi angry2 at p9_3
            hide lloyd_autumn
            hide lloyd annoy2
            show lloyd_autumn at p9_2
            show lloyd annoy2 at p9_2
            voice audio.yoshi_v_disagree1b
            yo "Sir Goro knows what’s best for the project, not you."
            yo "I trust his judgment when it comes to Camp Buddy, and I believe we worked as best as we could."

    show emilia rage5 at p9_6
    voice audio.emilia_v_disagree4b
    e "That doesn’t change the fact that you two have purposefully kept me out of the loop, all because you’re incapable of taking action without someone telling you what to do!"

    hide goro2_autumn
    hide goro2 disappoint3
    show goro_autumn at p9_4
    show goro rage1 at p9_4
    voice audio.goro_v_scold2a1
    g "You can keep ignoring every statement I make, Ms. Komarova, but I will not tolerate this any longer!" with vpunch

    show emilia scared2 at p9_6
    e "...!"

    hide goro_autumn
    hide goro rage1
    show goro2_autumn at p9_4
    show goro2 disappoint4 at p9_4
    voice audio.goro_v_shy1a
    g "These so-called ‘issues’ you’ve brought forward during this meeting have been completely irrelevant to the project, and quite frankly not worth Mr. Clermont’s, or any of our time."

    show emilia rage4 at p9_6
    voice audio.emilia_v_angry2
    e "What? How dare y—"

    hide goro2_autumn
    hide goro2 disappoint4
    show goro_autumn at p9_4
    show goro angry3 at p9_4
    voice audio.goro_v_scold3a
    g "I’m not done talking."
    g "Every single claim you’ve made, I’ve disproven with facts and rationally explained how ridiculous your arguments were."

    show goro disappoint2 at p9_4
    voice audio.goro_v_annoyed1a1
    g "If anything, all of these are personal issues which are a direct result of you refusing to get along with your fellow co-workers."

    show emilia angry2 at p9_6
    voice audio.emilia_v_bossy5a
    e "Personal?! I’m the only one who’s been professional here!"
    e "Shouldn’t you know better than anyone as the camp’s leader that business is no place for emotional attachment?!"

    show goro angry2 at p9_4
    voice audio.goro_v_no1a1
    g "No. A good leader treats everyone with sincerity and respect, especially those who make the project possible."
    g "I have a great deal of experience leading groups of people even before Camp Buddy, so don’t tell me how to do my job."

    show goro rage1 at p9_4
    voice audio.goro_v_insult1a2
    g "And how dare you call yourself a professional when all you’ve done is critique and never once lifted a finger to join in on the labor? "
    g "So tell me, Ms. Komarova. What ‘credentials’ give you the right to tell me how to run my own camp?"

    show emilia scared3 at p9_6
    voice audio.emilia_v_gasp1
    e "I… Well—"

    show william angry5 at p9_5
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

    show william serious2 at p9_5
    voice audio.william_v_well1b
    w "Well, Mr. Nomoru? It's your call."

    hide yoshi_autumn
    hide yoshi angry2
    show yoshi2_autumn at p9_3
    show yoshi2 sad1 at p9_3
    hide lloyd_autumn
    hide lloyd annoy2
    show lloyd_autumn at p9_2
    show lloyd panic1 at p9_2
    show darius panic1 at p9_1
    show aiden panic1 at p9_7
    show yuri angry1 at p9_8
    show jin panic1 at p9_9
    hide goro_autumn
    hide goro rage1
    show goro2_autumn at p9_4
    show goro2 think1 at p9_4
    g "..."

    show goro2 explain2 at p9_4
    voice audio.goro_v_sorry1a1
    g "I think we can all agree that this is just a simple misunderstanding that’s been blown out of proportion."
    g "Outside of these issues, Emilia has done her job to the best of her abilities."

    hide goro2_autumn
    hide goro2 explain2
    show goro_autumn at p9_4
    show goro talk1 at p9_4
    voice audio.goro_v_request5a1
    g "If you would allow us to fix the communication problems brought up, I’m sure we can still work this out."

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

    show goro confused2 at p9_4
    voice audio.goro_v_confused1a1
    g "Getaway…?"

    show william comp4 at p9_5
    voice audio.william_v_agree3a
    w "Yes, I’m sure it seems quite jarring coming off of the events here today, but I honestly wasn’t expecting such a back and forth."
    w "However, it was a part of today’s agenda."

    show william happy3 at p9_5
    voice audio.william_v_impressed1a
    w "To celebrate the completion of our initial objective, I thought it would be fitting to set up a celebratory trip! I’ve booked an exclusive hotel for everyone to stay at this weekend!"

    show goro shock2 at p9_4
    voice audio.goro_v_unsure1b1
    g "A-Are you sure, Mr. Clermont? Your sponsorship has already done so much for us, I’m not sure if we should accept—"

    show william comp4 at p9_5
    voice audio.william_v_well1a
    w "Well, I believe it’s important to unwind, especially after several months of hard work. "

    show yoshi2 awkward1 at p9_3
    w "Besides, I think it would be a great opportunity to teambuild and improve personal relationships, don’t you think? "

    show william happy3 at p9_5
    voice audio.william_v_please1a
    w "Please use this trip as a chance to further get to know one another so that you can properly empathize with each other once work resumes."

    show goro comp2 at p9_4
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

    show goro happy1 at p9_4
    voice audio.goro_v_thanks2a1
    g "Thank you again, Mr. Clermont. We’ll take our leave then."

    show emilia rage2 at p9_6
    voice audio.emilia_v_hmph1a
    e "Hmph!"

    hide emilia_autumn
    hide emilia rage2
    with dissolve

    hide yoshi2_autumn
    hide yoshi2 awkward1
    show yoshi_autumn at p9_3
    show yoshi awkward4 at p9_3
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
    show yoshi angry2 at right2
    voice audio.yoshi_vsa7_line1
    yo "Emilia, wait! Can we please talk?"

    show emilia angry3 at left2
    voice audio.emilia_vsa7_line1
    e "What?! "

    show yoshi angry3 at right2
    voice audio.yoshi_vsg8_line1
    yo "I just want to know why you’ve been acting this way for months now…!"

    play music heracleum_musicbox_a loop
    show emilia rage4 at left2
    voice audio.emilia_vsg8_line1
    e "Seriously?! After you kept your mouth shut and let everyone gang up on me back there, you still have the nerve to attack me like this?!"

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

    voice audio.emilia_vsg8_line2
    e "Everyone kept cowering behind that sorry excuse for a leader who just keeps abusing his power!"

    show yoshi rage1 at right2
    voice audio.yoshi_vsg8_line2
    yo "That’s not true, Emilia! Sir Goro was only trying to defend everyone from your criticisms!"

    voice audio.yoshi_vsg8_line3
    yo "Everything he said had a point, and he even acknowledged all your efforts in the end!"

    show emilia angry2 at left2
    voice audio.emilia_vsg8_line3
    e "Go ahead, keep licking his boots! That’s all you’ve ever done!"

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
    $ time_transition_sunset_to_night_fall()

    $ location = location_cabin
    $ time = timeline_timenight
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_quarters_autumn_night with fade
    play music ready_for_tomorrow loop
    play bgsound sfxloop_night loop

    show yoshi2_sleep at left2
    show yoshi2 sad1 at left2
    show goro2_sleep at right2
    show goro2 think2 at right2
    voice audio.goro_v_think1a1
    g "Hmm… I’m not surprised she said all that."

    show yoshi2 sad4 at left2
    voice audio.yoshi_v_sigh3a
    yo "I think I may have upset her even more than when we were with Mr. Clermont."

    hide goro2_sleep
    hide goro2 think2
    show goro_sleep at right2
    show goro angry2 at right2
    voice audio.goro_v_comp3a
    g "Don’t blame yourself for it, Yoshinori. Emilia’s actions are her own."

    show yoshi2 sad5 at left2
    voice audio.yoshi_v_but2
    yo "But still… Maybe if I had stood up in the meeting, things wouldn’t have escalated like that."

    hide goro_sleep
    hide goro angry2
    show goro2_sleep at right2
    show goro2 sigh1 at right2
    voice audio.goro_v_sigh1a
    g "*sigh* Now that I take responsibility for."
    g "With how Emilia has been acting, I knew something was bound to happen."

    show goro2 shy4 at right2
    voice audio.goro_v_shy1b
    g "Unfortunately, Mr. Clermont had to see it, which was quite embarrassing."
    g "And I’ll be honest, I already regret losing my temper back there. I said some pretty hurtful things."

    $ working = False
    $ shuffle_menu()
    menu():
        g "And I’ll be honest, I already regret losing my temper back there. I said some pretty hurtful things.{fast}"
        "She needs to learn a lesson.":
            $ working = True
            $ score_goro -= 2
            $ score_top += 1
            hide yoshi2_sleep
            hide yoshi2 sad5
            show yoshi_sleep at left2
            show yoshi angry2 at left2
            voice audio.yoshi_v_tsk1a
            yo "It’s about time someone said those things to her. She needs to learn a lesson."

            show goro2 angry2 at right2
            voice audio.goro_v_annoyed4a
            g "I don’t disagree, but what bothered me the most is how she kept digging into everyone, especially you…"
        "She deserved it.":
            $ working = True
            $ score_goro -= 2
            $ score_bot += 1
            hide yoshi2_sleep
            hide yoshi2 sad5
            show yoshi_sleep at left2
            show yoshi angry2 at left2
            voice audio.yoshi_v_tsk1a
            yo "It’s about time someone said those things to her. She deserved it."

            show goro2 angry2 at right2
            voice audio.goro_v_annoyed4a
            g "I don’t disagree, but what bothered me the most is how she kept digging into everyone, especially you…"
        "I would've done the same.":
            $ working = True
            $ score_goro += 2
            $ score_top += 1
            show yoshi2 worry2 at left2
            voice audio.yoshi_v_sir4
            yo "But I honestly would’ve done the same, sir…"

            show goro2 angry3 at right2
            voice audio.goro_v_annoyed4a
            g "I just couldn’t let her keep berating everyone, especially you, Yoshinori…"
        "You were only trying to protect us.":
            $ working = True
            $ score_goro += 2
            $ score_bot += 1
            show yoshi2 worry2 at left2
            voice audio.yoshi_v_sir4
            yo "But you were only trying to protect all of us, sir…"

            show goro2 angry3 at right2
            voice audio.goro_v_annoyed4a
            g "I just couldn’t let her keep berating everyone, especially you, Yoshinori…"

    g "I don’t care what her opinion of me is, but knowing how hard you’ve worked, I wasn’t going to stand by while she disrespected you like that."

    hide yoshi_sleep
    hide yoshi angry2
    show yoshi2_sleep at left2
    show yoshi2 sad5 at left2
    voice audio.yoshi_v_sirgoro4a
    yo "Sir Goro…"

    hide goro2_sleep
    hide goro2 angry2
    hide goro2 angry3
    show goro_sleep at right2
    show goro sigh4 at right2
    voice audio.goro_v_conj5a
    g "Still, I regret stooping down to her level and fighting with her about everything."
    g "If Mr. Clermont hadn’t stepped in, I wouldn’t have realized how uncomfortable you and everyone else were."

    show goro talk1 at right2
    voice audio.goro_v_so1a
    g "That’s when I knew I had to steer things in a different direction."

    show yoshi2 confused3 at left2
    voice audio.yoshi_v_huh3c
    yo "Is that why you let Emilia stay…? "

    show goro explain2 at right2
    voice audio.goro_v_think1a1
    g "Partly... I know most of you spent time with Emilia back when she was a scout. I stopped and thought of what you would’ve done in that scenario…"
    g "Emilia was only trying to prove a point from her perspective, and she must have reasons for the way she’s been acting."

    show goro comp2 at right2
    voice audio.goro_v_conj9a1
    g "And if there’s anything I’ve learned from you and the scouts, removing her would only cause resentment when we could still resolve things together."

    show yoshi2 think2 at left2
    voice audio.yoshi_v_isee2
    yo "I see…"

    show yoshi2 sigh1 at left2
    voice audio.yoshi_v_sigh3a
    yo "Maybe this wouldn’t have happened if I’d just worked with Emilia from the start… "

    show goro comp3 at right2
    voice audio.goro_v_dismiss2a
    g "Don’t say that, Yoshinori. I’m very grateful for the last few months we’ve worked together. I’d stand by that decision no matter what."
    g "I just need to ensure that Emilia doesn’t continue to bring out the worst in me."

    hide yoshi2_sleep
    hide yoshi2 sigh1
    show yoshi_sleep at left2
    show yoshi comp2 at left2
    voice audio.yoshi_v_unsure3c
    yo "Maybe this getaway Mr. Clermont offered us is the perfect way to get rid of the tension and loosen up some."

    show goro happy1 at right2
    voice audio.goro_v_agree4a1
    g "Exactly. I’m actually looking forward to what this vacation has in store for us."

    show goro_sleep at p6_1
    show goro happy1 at p6_1
    show yoshi_sleep at p6_2
    show yoshi comp5 at p6_2
    with move

    show darius_sleep at p6_4
    show darius norm3 at p6_4
    show lloyd_sleep at p6_3
    show lloyd pain4 at p6_3
    show aiden_sleep at p6_5
    show aiden norm1 at p6_5
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
    j "Th-Thanks for carrying mine though, Aiden…"

    show aiden laugh1 at p6_5
    voice audio.aiden_v_response1a
    a "No problem!"

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

    show aiden talk2 at p6_5
    voice audio.aiden_v_yeah1a4
    a "Yeah, but that was like a work trip! This time we won’t have any responsibilities… and that’s basically never happened before!"

    show goro happy2 at p6_1
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

    show aiden comp6 at p6_5
    voice audio.aiden_v_comp1a2
    a "Don’t worry Jin, I’m in the same boat as you! I’ve never been on a trip like this before."
    a "We’ll both be like headless chickens, haha!"

    show yuri_sleep at p9_9
    show yuri pain3 at p9_9
    with moveinright

    voice audio.yuri_v_groan1a
    yu "HNGHHHH…!!!"

    show aiden_sleep at p7_4
    show aiden comp6 at p7_4
    show lloyd_sleep at p7_2
    show lloyd happy1 at p7_2
    show darius_sleep at p7_3
    show darius think5 at p7_3
    show goro_sleep at p7_1
    show goro happy2 at p7_1
    show jin_sleep at p7_5
    show jin_glasses at p7_5
    show jin awkward3 at p7_5
    show yoshi_sleep at p7_6
    show yoshi shock3 at p7_6
    show yuri_sleep at p7_7
    show yuri pain3 at p7_7
    with move

    voice audio.yoshi_v_oh2
    yo "O-Oh…! Let me help you with that suitcase, Yuri!"

    show yuri pain6 at p7_7
    voice audio.yuri_v_groan1a
    yu "GAH!!" with vpunch

    show aiden shock3 at p7_4
    voice audio.aiden_v_shock1b1
    a "Whoa… What’s up with all the luggage, Yuri?"

    show yuri explain3 at p7_7
    voice audio.yuri_v_actually1a
    yu "This is for me and Dad! I always pack for him during trips like this or he’ll forget something!"

    hide goro_sleep
    hide goro happy2
    show goro2_sleep at p7_1
    show goro2 disappoint2 at p7_1
    hide lloyd_sleep
    hide lloyd happy1
    show lloyd_sleep at p7_2
    show lloyd happy1 at p7_2
    voice audio.goro_v_ehem1a
    g "*ehem* It’s not that I forget things, it’s more that I only bring what I need."

    show yuri tease2 at p7_7
    voice audio.yuri_v_yeah2b1
    yu "Oh yeah? Remember when we went to the beach last summer and you kept asking me for your razor?"
    yu "You were so cranky you didn’t get to shave that morning, especially before you got your coffee!"

    show goro2 sigh1 at p7_1
    voice audio.goro_v_sigh1a
    g "*sigh* Did you really have to share that with everyone, Yuri?"
    g "And besides, we don’t need to pack as many essential things. Usually hotels provide them, don’t they?"

    show yuri bold4 at p7_7
    voice audio.yuri_v_confident1b
    yu "Better to be safe than sorry!"

    show goro2 norm3 at p7_1
    show yoshi confused2 at p7_6
    voice audio.yoshi_v_think2
    yo "It makes me wonder what kind of hotel it is. Mr. Clermont didn’t really give us any details."

    hide aiden_sleep
    hide aiden shock3
    show aiden2_sleep at p7_4
    show aiden2 think5 at p7_4
    hide darius_sleep
    hide darius think5
    show darius_sleep at p7_3
    show darius think5 at p7_3
    hide lloyd_sleep
    hide lloyd happy1
    show lloyd_sleep at p7_2
    show lloyd happy1 at p7_2
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
    show aiden_sleep at p7_4
    show aiden tease1 at p7_4
    voice audio.aiden_v_oho1a
    a "Of course, Mr. ‘Sirius’!"

    show lloyd tease3 at p7_2
    voice audio.lloyd_v_greet2b1
    l "EYY!"

    show aiden wink2 at p7_4
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

    show lloyd pain1 at p7_2
    voice audio.lloyd_v_groan2a1
    l "Oof… Trust us, we know…"

    show jin worry2 at p7_5
    voice audio.jin_v_unsure2b3
    j "Is there even a chance of her getting along with us like Mr. Clermont asked?"

    show yuri rage2 at p7_7
    voice audio.yuri_v_conj2d1
    yu "It’s not even about getting along. She’s just a flat-out bitch! "

    show goro2 explain2 at p7_1
    voice audio.goro_v_scold1a1
    g "Now calm down, dear. This trip gives us a good chance to unwind after all the stress from work."

    show jin sad2 at p7_5
    voice audio.jin_v_sigh2a
    j "Honestly though, I thought she’d be a lot less aggressive in front of Mr. Clermont, but she didn’t even think twice about calling each of us out like that…"

    show lloyd annoy5 at p7_2
    voice audio.lloyd_v_annoyed1a3
    l "She’s so business-minded she couldn’t care less about our feelings! I bet that was the ugly side of a Capricorn talking!"
    l "But that explosive attitude sounds like something an Aries would do – they can be control freaks too."

    show darius annoy2 at p7_3
    voice audio.darius_v_ugh1
    d "She’s neither. She’s just mean. "

    show yuri angry6 at p7_7
    voice audio.yuri_v_annoyed1a
    yu "I’m already at my wits end with that girl. I don’t think we’ll ever be friends outside of work."

    show yoshi talk1 at p7_6
    voice audio.yoshi_v_but2
    yo "We don’t have to be friends with Emilia, but we don’t have to antagonize her either."
    yo "We just have to learn to not take her personal remarks seriously and focus on our jobs."

    show yuri rage3 at p7_7
    voice audio.yuri_v_annoyed2a
    yu "But if she crosses the line like that again, I’m not going to hold myself back anymore!"

    hide aiden_sleep
    hide aiden wink1
    show aiden2_sleep at p7_4
    show aiden2 sigh1 at p7_4
    hide darius_sleep
    hide darius annoy2 at p7_3
    show darius_sleep at p7_3
    show darius annoy2 at p7_3
    hide lloyd_sleep
    hide lloyd annoy5
    show lloyd_sleep at p7_2
    show lloyd annoy5 at p7_2
    voice audio.aiden_v_relief1a2
    a "I’m just relieved you said something back there, Gramps."

    show yuri bold2 at p7_7
    voice audio.yuri_v_yeah2a3
    yu "Oh yeah! That was so satisfying! In my head I was like “Yesss! Yesss! Get her, Dad!”"

    show lloyd bold2 at p7_2
    voice audio.lloyd_v_gratitude1a1
    l "Sir Goro really saved our butts!"

    hide goro2_sleep
    hide goro2 explain2
    show goro_sleep at p7_1
    show goro shock2 at p7_1
    hide lloyd_sleep
    hide lloyd bold2
    show lloyd_sleep at p7_2
    show lloyd bold2 at p7_2
    voice audio.goro_v_wait2c1
    g "W-Wait… You mean you all weren’t intimidated by me?"

    show lloyd_sleep at p7_2
    show lloyd talk2 at p7_2
    voice audio.lloyd_v_denial2a1
    l "No way! I’m glad you put Emilia in her place! "

    show darius_sleep at p7_3
    show darius comp5 at p7_3
    voice audio.darius_v_thanks1a1
    d "We appreciate it."

    show jin sigh1 at p7_5
    voice audio.jin_v_sigh2a
    j "You only really said what we were all thinking, sir…"

    show goro sigh1 at p7_1
    voice audio.goro_v_but2a
    g "But still, I’d rather you all hadn’t seen that."

    show lloyd confused2 at p7_2
    voice audio.lloyd_v_unsure1b1
    l "I guess that was first time you’ve raised your voice like that around us, sir."

    show darius think5 at p7_3
    voice audio.darius_v_agree2a
    d "Yeah. He never got angry, even when we were scouts."

    hide aiden2_sleep
    hide aiden2 sigh1
    show aiden_sleep at p7_4
    show aiden play3 at p7_4
    voice audio.aiden_v_laugh1a1
    a "Haha, you guys should’ve seen him over the last few years, then! He was the stiffest and scariest guy you’d ever met!"

    hide goro_sleep
    hide goro sigh1
    show goro2_sleep at p7_1
    show goro2 annoy2 at p7_1
    voice audio.goro_v_sigh1a
    g "*sigh* Did you really have to bring that up, Aiden?"

    show jin confused5 at p7_5
    voice audio.jin_v_really3a
    j "It’s so hard for me to imagine Sir Goro being strict... He's been cuddly and gentle with me ever since I first met him."
    j "But now I get it after seeing it up close and personal… I-It was kinda hot…"

    show yuri bold4 at p7_7
    voice audio.yuri_v_comp1a1
    yu "You guys should know that someone like Emilia won’t get away with causing trouble with Dad keeping his eye on her!"

    show yuri play2 at p7_7
    voice audio.yuri_v_laugh2b1
    yu "She’s lucky Dad’s way past his gangster days, or else she would’ve been taken down!"

    show yoshi confused2 at p7_6
    voice audio.yoshi_v_what4
    yo "I’m sorry, what…? "

    hide goro2_sleep
    hide goro2 annoy2
    show goro_sleep at p7_1
    show goro rage1 at p7_1
    hide lloyd_sleep
    hide lloyd confused2
    show lloyd_sleep at p7_2
    show lloyd confused2 at p7_2
    voice audio.goro_v_yuri8a
    g "Yuri! I told you never to bring that up!"

    show aiden panic3 at p7_4
    voice audio.aiden_v_wait1b1
    a "Wait! Don’t tell me you were a hitman or something back before Camp Buddy, Gramps?!"

    show lloyd scared1 at p7_2
    voice audio.lloyd_v_shock4a1
    l "Okay, now that’s actually scary."

    show darius tease2 at p7_3
    voice audio.darius_v_laugh1
    d "Thug life."

    hide goro_sleep
    hide goro rage1
    show goro2_sleep at p7_1
    show goro2 disappoint2 at p7_1
    hide lloyd_sleep
    hide lloyd scared1
    show lloyd_sleep at p7_2
    show lloyd scared1 at p7_2
    voice audio.goro_v_ehem1a
    g "*ehem* Don’t get carried away, all of you. I just happened to be mixed in with the wrong crowd during my younger years."

    show yuri tease2 at p7_7
    voice audio.yuri_v_actually1a
    yu "By wrong crowd, he means a biker gang~!"

    show yoshi shock3 at p7_6
    voice audio.yoshi_v_shock1a
    yo "A-A biker gang?! "

    show goro2 shy6 at p7_1
    voice audio.goro_v_no2c1
    g "I-It was more of a fraternity… it’s not as bad as you’re all imagining."

    show yoshi shock2 at p7_6
    voice audio.yoshi_v_really3
    yo "H-How have we never heard of any of this?"

    hide goro2_sleep
    hide goro2 shy6
    show goro_sleep at p7_1
    show goro shy4 at p7_1
    hide lloyd_sleep
    hide lloyd scared1
    show lloyd_sleep at p7_2
    show lloyd scared1 at p7_2
    voice audio.goro_v_well3a
    g "Well, it’s far in the past, way before Camp Buddy was around."
    g "There was never a reason to bring it up… And I don’t think it’s something to be proud of either… "

    show jin scheme2 at p7_5
    voice audio.jin_v_oh1c
    j "That explains all the leather…"

    show yuri excited2 at p7_7
    voice audio.yuri_v_response2a1
    yu "I know, right? But don’t let him downplay it – he was actually their leader, too!"

    show lloyd talk4 at p7_2
    voice audio.lloyd_v_amazed1b2
    l "Ooooohhh! So, that’s what he meant back at the meeting! "

    show aiden shock3 at p7_4
    voice audio.aiden_v_shock1b1
    a "Gramps was the number one tough guy in a group of tough guys! That’s crazy!"

    show darius bold2 at p7_3
    voice audio.darius_v_amazed3
    d "Top dog."

    hide yoshi_sleep
    hide yoshi shock3
    show yoshi2_sleep at p7_6
    show yoshi2 awkward4 at p7_6
    hide jin_sleep
    hide jin_glasses
    hide jin scheme2
    show jin_sleep at p7_5
    show jin_glasses at p7_5
    show jin scheme2 at p7_5
    voice audio.yoshi_v_shock1d
    yo "This is all so much to take in… "

    hide goro_sleep
    hide goro shy4
    show goro2_sleep at p7_1
    show goro2 explain2 at p7_1
    hide lloyd_sleep
    hide lloyd talk4
    show lloyd_sleep at p7_2
    show lloyd talk4 at p7_2
    voice audio.goro_v_no3a1
    g "I don’t talk about it for a reason. I can’t imagine the scouts would appreciate knowing their leader was once not a good example. "
    g "And like I said, I have long put that behind me."

    show yuri amazed3 at p7_7
    voice audio.yuri_v_goro1b
    yu "You shouldn’t be ashamed of it, Dad! All of us think it’s cool! Right, guys?"

    show goro2 sigh1 at p7_1
    voice audio.goro_v_sigh1a
    g "*sigh* Why are you insistent on this, Yuri-dear? You weren’t even born then."

    show yuri angry2 at p7_7
    voice audio.yuri_v_agree2a1
    yu "Exactly! You barely tell me anything about it! We all deserve to know!"

    show goro2 shy1 at p7_1
    show goro2_blush1 at p7_1
    voice audio.goro_v_no1a1
    g "No."

    show yuri pout2 at p7_7
    voice audio.yuri_v_rush1c2
    yu "Oh, come on, Dad!"

    show aiden tease2 at p7_4
    voice audio.aiden_v_laugh2b1
    a "Hahaha, let it go, Yuri! Gramps’ face is already red!"

    show lloyd explain3 at p7_2
    voice audio.lloyd_v_agree3a3
    l "Welp! If that’s all we’re getting, then I guess I’ll go ahead and do my night routines – we’ve spent enough time chit-chatting!"

    hide yoshi2_sleep
    hide yoshi2 awkward4
    show yoshi_sleep at p7_6
    show yoshi talk3 at p7_6
    voice audio.yoshi_v_oh2
    yo "Oh, right. I have to finish packing too. "

    hide goro2_sleep
    hide goro2_blush1
    hide goro2 shy1
    show goro_sleep at p7_1
    show goro talk3 at p7_1
    hide lloyd_sleep
    hide lloyd explain3
    show lloyd_sleep at p7_2
    show lloyd explain3 at p7_2
    voice audio.goro_v_rush1a1
    g "Let me help."

    show yuri pout4 at p7_7
    voice audio.yuri_v_hey3a
    yu "Heeeey! Don’t change the subject!"

    hide goro_sleep
    hide goro talk3
    show goro2_sleep at p7_1
    show goro2 angry3 at p7_1
    voice audio.goro_v_yuri8a
    g "Yuri, to your room. NOW."

    show yuri panic3 at p7_7
    voice audio.yuri_v_shock2a
    yu "Eek! Yes, Dad!"

    hide yuri_sleep
    hide yuri panic3
    with dissolve

    show aiden laugh3 at p7_4
    voice audio.aiden_v_amazed2b1
    a "Hahaha! Can’t believe that worked, Gramps!"

    show lloyd tease2 at p7_2
    voice audio.lloyd_v_laugh1a1
    l "Daddy mode on."

    hide jin_sleep
    hide jin_glasses
    hide jin scheme2
    show jin2_sleep at p7_5
    show jin2_glasses at p7_5
    show jin2 perv5 at p7_5
    voice audio.jin_v_fudan3a1
    j "I think I have a new kink…"

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
    show yoshi happy1 at left2
    show goro_sleep at right2
    show goro norm2 at right2
    voice audio.yoshi_v_alright2
    yo "There we go! I think I’m fully packed! "
    yo "Do you need any help checking your bags, Sir Goro?"

    show goro explain2 at right2
    voice audio.goro_v_dismiss3a
    g "No need – Yuri already handled it. She's so excited she couldn't even wait to start loading up all our stuff."

    hide yoshi_sleep
    hide yoshi happy1
    show yoshi2_sleep at left2
    show yoshi2 comp6 at left2
    voice audio.yoshi_v_laugh5a
    yo "Ahehe…"

    show goro happy2 at right2
    voice audio.goro_v_conj1a1
    g "Although I don’t blame her… I’m just as ready for a vacation where I don’t have to worry about any responsibilities."

    hide yoshi2_sleep
    hide yoshi2 comp6
    show yoshi_sleep at left2
    show yoshi happy2 at left2
    voice audio.yoshi_v_yessir1
    yo "Me too, sir. It'll be fun even if it's just for a few days, especially after how busy we've been!"

    show goro relief2 at right2
    voice audio.goro_v_relief1a
    g "I know we’ve been able to spend a great deal of time together working, but this is the perfect opportunity for us both to focus on enjoying each other’s company."
    g "Just pure quality time with each other."

    show yoshi comp2 at left2
    voice audio.yoshi_v_sirgoro12
    yo "Sir Goro…"

    play sound sfx_typing
    show yoshi confused2 at left2
    voice audio.yoshi_v_think1b
    yo "Wait… Do you hear that?"

    hide goro_sleep
    hide goro relief2
    show goro2_sleep at right2
    show goro2 confused3 at right2
    voice audio.goro_v_jin5a
    g "Jin? You’re not trying to work before the vacation, are you?"

    show yoshi_sleep at left
    show yoshi confused2 at left
    show goro2_sleep at center
    show goro2 confused3 at center
    with move

    show jin_sleep at right
    show jin_glasses at right
    show jin panic2 at right
    with dissolve

    voice audio.jin_v_ah4c
    j "A-Ah…! I’m sorry, was my keyboard too loud?"

    show jin talk4 at right
    voice audio.jin_v_oh3a
    j "A-And no, I’m not working either!"
    j "Although, I guess technically you could say that I’m working on something…"

    show jin happy1 at right
    voice audio.jin_v_yoshi4c
    j "It’s that side thing we started, Yoshi. I never had the time to get back to it since we’ve been so busy lately."

    show goro2 talk3 at center
    voice audio.goro_v_heh1a
    g "Ah… It sounds like you two have been having a secret affair, huh?"

    show jin daydream2 at right
    voice audio.jin_v_fudan1a2
    j "*cough* I wish."

    show yoshi talk3 at left
    voice audio.yoshi_v_right6
    yo "Ah, right! I didn’t get to tell you that Jin and I were working on this little website project, sir!"

    hide goro2_sleep
    hide goro2 talk3
    show goro_sleep at center
    show goro confused2 at center
    voice audio.goro_v_oh3a
    g "Oh? What’s it about?"

    show yoshi happy1 at left
    voice audio.yoshi_v_actually3a
    yo "We’re transcribing Yuri’s journal and restoring the photos for a blog! Jin’s doing most of the work though, since I’m notoriously bad with anything tech-related…"

    show goro happy1 at center
    voice audio.goro_v_agree8a1
    g "That sounds interesting."

    show yoshi happy2 at left
    voice audio.yoshi_v_oh1
    yo "Oh, if you’re not too tired, Sir Goro, why don’t we help Jin finish up tonight?"

    hide goro_sleep
    hide goro happy1
    show goro2_sleep at center
    show goro2 play3 at center
    voice audio.goro_v_alright1b1
    g "I don’t mind. The more hands, the better, right?"

    show jin fudan1 at right
    voice audio.jin_v_gulp1a
    j "*gulp*"

    show yoshi bold2 at left
    voice audio.yoshi_v_rush1
    yo "Come on! Let’s get on his bunk and work on tonight’s entry! "

    hide jin_sleep
    hide jin_glasses
    hide jin fudan1
    show jin2_sleep at right
    show jin2_glasses at right
    show jin2 fudan3 at right
    voice audio.jin_v_wah2b
    j "W-Wah! Is it finally happening?!"

    # JMG1
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
    $ minigame_id = 'jmG1'
    $ renpy.call(minigame_id)

label day2_goro_postmg:
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

    $ location = location_forest
    $ day = "??"
    $ time = timeline_timeday
    $ season = season_summer
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_forest_past_day with fade
    play music camping_time loop
    play bgsound sfxloop_forest loop

    show ydarius_camp at left
    show ydarius confused1 at left
    show yyoshi_camp at center
    show yyoshi talk1 at center
    show ylloyd_camp at right
    show ylloyd confused1 at right
    voice audio.yyoshi_v_alright2
    yo "One… two… three…"

    play sound sfx_woodchop
    show yyoshi pain3 at center
    voice audio.yyoshi_v_shock2a
    yo "GAH!" with vpunch

    show yyoshi pain1 at center
    voice audio.yyoshi_v_groan1a
    yo "Hngh! It didn’t budge!"

    show yyoshi sigh1 at center
    voice audio.yyoshi_v_aww1
    yo "Oh man… How can I make a campfire if I can’t even split wood?"

    show ylloyd confused3 at right
    voice audio.ylloyd_v_sus1a1
    l "I dunno, Yoshi… Shouldn’t you be doing something else for today’s badge activity?"
    l "I mean… This looks really dangerous. You’ve missed and sent that axe flying about three times now. "

    show ydarius think2 at left
    voice audio.ydarius_v_worry1a
    d "You’ll lose both of your legs before you get a badge."

    show yyoshi happy1 at center
    voice audio.yyoshi_v_well1
    yo "Well, it’s not just for the badge! I saw Sir Goro chopping trees over there, and I thought I could help!"
    yo "Also, I thought it was super cool! His really huge muscles can take down trees like they’re nothing! "

    show ylloyd tease2 at right
    voice audio.ylloyd_v_shock1a1
    l "Oh… So that’s what this is about."

    show yyoshi confused2 at center
    voice audio.yyoshi_v_huh1
    yo "Huh?"

    show ydarius play2 at left
    voice audio.ydarius_v_laugh1a
    d "You’ve got a crush on the camp president."

    show yyoshi_blush1 at center
    show yyoshi panic3 at center
    voice audio.yyoshi_v_what6
    yo "Wh-What?!" with vpunch

    show ygoro_camp2 at p9_9
    show ygoro talk3 at p9_9
    with dissolve

    voice audio.ygoro_v_greet3a1
    g "Ah, there you boys, are! I’ve been looking for—"

    show ygoro shock1 at p9_9
    g "...!"

    show ydarius_camp at p4_1
    show ydarius shock1 at p4_1
    show ylloyd_camp at p4_2
    show ylloyd shock1 at p4_2
    show yyoshi_camp at p4_3
    show yyoshi shock1 at p4_3
    hide yyoshi_blush1
    show ygoro_camp2 at p4_4
    show ygoro angry3 at p4_4
    with move

    voice audio.ygoro_v_yoshi9
    g "Yoshinori! Where did you get this axe from?!"

    show yyoshi shy3 at p4_3
    voice audio.yyoshi_v_awkward1
    yo "Umm... the shed???"

    show ylloyd worry2 at p4_2
    voice audio.ylloyd_v_shock2b1
    l "Uh-oh…"

    show ygoro sigh1 at p4_4
    voice audio.ygoro_v_sigh2a
    g "*sigh* You’re trying to split wood, are you? "

    show yyoshi sad4 at p4_3
    voice audio.yyoshi_v_yessir3a
    yo "Y-Yes, sir…"

    show ygoro angry2 at p4_4
    voice audio.ygoro_v_request3a1
    g "Look, I know you want to help around the camp, Yoshinori. But this is not a job for a scout."
    g "Also, shouldn’t you all be with the other scouts for the badge activity?"

    show yyoshi worry2 at p4_3
    voice audio.yyoshi_v_sorry2b
    yo "I’m sorry, sir. I also thought a woodcutting badge would be cool…"

    show ygoro comp1 at p4_4
    g "..."

    show ygoro explain1 at p4_4
    voice audio.ygoro_v_well1
    g "Well, you’re not holding the axe the right way. Here, let me show you."

    show ygoro_camp2 at p4_3
    show ygoro talk1 at p4_3
    show yyoshi_camp at p4_4
    show yyoshi shock1 at p4_4
    with move

    voice audio.ygoro_v_see5a
    g "You need to have a stable base, preferably a stump, larger than the rounds you’re going to be splitting on top of it. "
    g "Not only will that give you a good, flat surface to work with, but your axe will also have a place to dig into."

    show ygoro explain2 at p4_3
    voice audio.ygoro_v_conj2a1
    g "You’re going to break your blade if you keep splitting wood directly on the ground."

    show yyoshi talk4 at p4_4
    voice audio.yyoshi_v_oh3
    yo "Oh… "

    show ygoro talk3 at p4_3
    voice audio.ygoro_v_alright1a
    g "Clear a spot around you… Spread your legs… Hold your axe like this…"
    g "Raise your arms overhead, extending them high with a straight body…"

    play sound sfx_woodchop
    show ygoro bold2 at p4_3
    voice audio.ygoro_v_heh3c
    g "…then SWING!" with vpunch

    show yyoshi shock2 at p4_4
    voice audio.yyoshi_v_shock1b
    yo "Whoaaa! "

    show ylloyd excited4 at p4_2
    voice audio.ylloyd_v_amazed3a1
    l "Holy wood boulevard!"

    show ydarius excited6 at p4_1
    d "*claps*"

    show yyoshi excited1 at p4_4
    voice audio.yyoshi_v_amazed1a
    yo "That was so freaking awesome, Sir Goro! "

    show ygoro play2 at p4_3
    voice audio.ygoro_v_well1
    g "Well, want me to teach you?"

    show yyoshi amazed2 at p4_4
    voice audio.yyoshi_v_agree1b
    yo "Do I ever!!"

    show ygoro happy2 at p4_3
    voice audio.ygoro_v_here1a
    g "Come here then."

    show cg_fade at truecenter
    show fxmgg1 1 at fx_pos
    with dissolve

    play music here_they_come loop
    voice audio.ygoro_vsg9_line1
    g "First, plan where you’re going to aim by looking for cracks so you can align yourself with them as your target."

    voice audio.ygoro_vsg9_line2
    g "Avoid knots and twisted grains – instead aim your blow near the edge of the round but not at the very center."

    voice audio.yyoshi_vsg9_line1
    yo "Ohhh… So that’s why no matter how hard I was hitting it, it wouldn’t split."

    show fxmgg1 2 at fx_pos with Dissolve(0.25)
    voice audio.ygoro_vsg9_line3
    g "Splitting wood is not just about strength, you need good technique and posture too."

    voice audio.ygoro_vsg9_line4
    g "You should stand with your feet shoulder-width apart, so that you won’t hit your leg after a swing."

    show fxmgg1 3 at fx_pos with Dissolve(0.25)
    voice audio.ygoro_vsg9_line5
    g "Then hold your axe near your waist – one hand on the base of the handle, palm facing toward you and the other hand at the neck, palm facing away, thumb next to the axe head."

    voice audio.ygoro_vsg9_line6
    g "During your upswing, extend your body like I showed you earlier, raising your toes up a little, while sliding your other hand down to the handle to gain momentum."

    voice audio.ygoro_vsg9_line7
    g "When you deliver a forceful downswing, concentrate your vision on your target, all the way down to the base."

    voice audio.ygoro_vsg9_line8
    g "Bend into a squat, adding the weight of your body to the force of impact.  "

    show fxmgg1 4 at fx_pos with Dissolve(0.25)
    voice audio.ylloyd_vsg9_line1
    l "Yo-shi-no-ri cutting down a tree."

    voice audio.ydarius_vsg9_line1
    d "Face-as-red-as a strawberry."

    voice audio.yyoshi_vsg9_line2
    yo "C-Cut it out, you guys…!"

    voice audio.ygoro_vsg9_line9
    g "Now… Give it a try."

    hide cg_fade
    hide fxmgg1 4
    with dissolve

    show ygoro_camp2 at p4_4
    show ygoro norm3 at p4_4
    show yyoshi_camp at p4_3
    show yyoshi sigh1 at p4_3
    with move

    voice audio.yyoshi_v_relief1
    yo "Whew... Okay… "

    show yyoshi norm3 at p4_3
    show ygoro talk1 at p4_4
    voice audio.ygoro_v_alright1a
    g "On my count. One… Two…"
    g "SWING!"

    play sound sfx_woodchop
    show yyoshi shock3 at p4_3
    voice audio.yyoshi_v_shock2a
    yo "WAH! I did it!" with vpunch

    show ygoro play3 at p4_4
    voice audio.ygoro_v_see5a
    g "See? It’s pretty easy."

    show ylloyd amazed3 at p4_2
    voice audio.ylloyd_v_amazed1b1
    l "Wow, I wanna try too!"

    show ydarius tease2 at p4_1
    voice audio.ydarius_v_think3a
    d "Do you want me to hug you also?"

    show yyoshi bold2 at p4_3
    voice audio.yyoshi_v_really2
    yo "Does this mean you’ll let me split wood now too, Sir Goro?!"

    show ygoro explain3 at p4_4
    voice audio.ygoro_v_okay2a
    g "Sure, but only when I’m supervising."

    show yyoshi excited1 at p4_3
    voice audio.yyoshi_v_yes2
    yo "YES! YES! Thank you! Thank you!"

    show ygoro talk1 at p4_4
    voice audio.ygoro_v_response1b1
    g "Six in the morning sharp, you'll come with me, and we'll chop wood together."

    show yyoshi amazed1 at p4_3
    voice audio.yyoshi_v_yessir2a
    yo "Yes, sir!"

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

label dayg2_postfb:
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
    show goro_sleep at right2
    show goro norm1 at right2
    voice audio.yoshi_v_alright2
    yo "Alright, this entry is done, but I can’t believe it’s already past midnight! "
    yo "We didn’t even notice how long we were working on this. I can see how you struggle with the concept of time, Jin! "

    hide goro_sleep
    hide goro norm1
    show goro2_sleep at right2
    show goro2 play3 at right2
    voice audio.goro_v_heh1a
    g "Heh, it doesn’t look like he struggled tonight."

    voice audio.jin_v_hngh1a
    j "*snores*"

    hide yoshi_sleep
    hide yoshi happy1
    show yoshi2_sleep at left2
    show yoshi2 comp3 at left2
    voice audio.yoshi_v_laugh5a
    yo "Ahehe… This is the first time I’ve seen him asleep at night."
    yo "Let me just tuck him in, then let’s get off his bunk."

    hide goro2_sleep
    hide goro2 play3
    show goro_sleep at right2
    show goro laugh3 at right2
    voice audio.goro_v_laugh1a1
    g "Haha, you’re acting like a scoutmaster even now, Yoshinori."

    show yoshi2 comp6 at left2
    voice audio.yoshi_v_really2
    yo "A-Ah, am I? I guess Jin could be a camper…"

    show goro talk3 at right2
    voice audio.goro_v_agree7a
    g "True. But regardless, we should get some rest too."
    g "We have a long day of travel ahead of us tomorrow!"

    hide yoshi2_sleep
    hide yoshi2 comp6
    show yoshi_sleep at left2
    show yoshi happy1 at left2
    voice audio.yoshi_v_goodpm3
    yo "Right! Goodnight, sir!"

    show goro happy2 at right2
    voice audio.goro_v_goodpm3a1
    g "Goodnight, Yoshinori."

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
    $ time_transition_night_to_day_fallwinter()
    $ renpy.pause (2.0, hard=True)
    jump day3_goro
