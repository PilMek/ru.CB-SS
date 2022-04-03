label day0_goro:
    e "If you want me to be even more honest, I believe the overall management is what troubles me the most."

    show emilia confused3 at right2
    voice audio.emilia_v_bossy4
    e "As you may have noticed from our meeting earlier, the issues I pointed out were all due to subpar leadership."
    e "Even though every department had its own shortcomings, when the ship sinks, the captain is to blame after all."

    show yoshi2 think2 at left2
    voice audio.yoshi_v_think1a
    yo "I don’t think there’s anything wrong with the way Sir Goro has been leading the project so far… Are you sure you’re just not looking too much into it?"

    show emilia disgust3 at right2
    voice audio.emilia_v_question2b
    e "Do you really want to wait until it becomes a problem? It’s better to deal with it now."
    e "Especially since we’re talking about something as serious as the one who holds this place together."

    show emilia angry2 at right2
    voice audio.emilia_v_hmph1a
    e "It’s about time this camp let go of its outdated ways and let the new generation take over."

    show yoshi2 worry1 at left2
    yo "..."

    show emilia eyeroll4 at right2
    voice audio.emilia_v_ugh1
    e "Eugh. Don’t give me that look, Yoshinori. It’s just business."

    show emilia sigh2 at right2
    voice audio.emilia_v_sigh1a
    e "Look, I know criticism isn’t easy to take in, but someone has to point these things out."
    e "You know me- I prefer to be straightforward, especially when it comes to work."

    show yoshi2 sad5 at left2
    voice audio.yoshi_v_response1c
    yo "I… understand."

    show emilia annoy2 at right2
    voice audio.emilia_v_worry5
    e "That doesn’t sound too enthusiastic. Did my comment about your role upset you?"

    show emilia tired2 at right2
    voice audio.emilia_v_ugh1
    e "You must be so tired of having no consistent responsibility for this project…"
    e "But don’t worry, I’m here to help!~ "

    show emilia bold2 at right2
    voice audio.emilia_v_so2a
    e "Starting tomorrow, you and I will be in charge of both technology and overall management."

    hide yoshi2_autumn
    hide yoshi2 sad5
    show yoshi_autumn at left2
    show yoshi awkward3 at left2
    voice audio.yoshi_v_what2
    yo "A-Are you saying we would take over Sir Goro’s position? We can’t do that!"

    show emilia confused5 at right2
    voice audio.emilia_v_no1
    e "No, no, we just need to work together and be Mr. Nomoru’s advisors – to ensure we provide more 'modern' insights about how this camp and project should be run."
    e "I’m sure you can agree that changes are inevitable. Refusing to adapt will eventually doom this camp."

    hide yoshi_autumn
    hide yoshi awkward3
    show yoshi2_autumn at left2
    show yoshi2 awkward1 at left2
    yo "..."

    show emilia talk3 at right2
    voice audio.emilia_v_conj2a
    e "Anyway, I’ll make sure that you know exactly what to do in both of these fields from now on."
    e "Since I’ll be staying here for the QA work, I thought I’d go out of my way to make sure you get a clearer perspective!"

    show emilia bold5 at right2
    voice audio.emilia_v_laugh1a
    e "There’s nobody better suited for the task, since it’s my job to oversee the entire project! We can take charge and lead together."

    show yoshi2 think1 at left2
    yo "..."

    show emilia play2 at right2
    voice audio.emilia_v_so3
    e "So? What do you say? Partners?"

    show yoshi2 explain2 at left2
    voice audio.yoshi_v_unsure1b
    yo "I… I’m not sure about this, Emilia… "

    show emilia irked2 at right2
    voice audio.emilia_v_annoyed1
    e "Why, that’s not the right answer!"
    e "You should be grateful; I’m offering to fix the exact issue you just mentioned."

    show emilia irked5 at right2
    voice audio.emilia_v_sarcastic4
    e "It baffles me why you’re having second thoughts about this. Help is literally being served to you on a silver—no, gold platter!"

    show yoshi2 worry2 at left2
    voice audio.yoshi_v_no4
    yo "I-It’s not that I don’t appreciate your offer, but I was trying to make a plan to resolve it myself…"

    show emilia disgust3 at right2
    voice audio.emilia_v_sarcastic1
    e "And that plan is…?"

    show yoshi2 sigh1 at left2
    voice audio.yoshi_v_well1
    yo "W-Well… I haven’t completely figured it out yet."
    yo "Can you at least give me a little time to think about what you’re proposing? It’s all very sudden, after all…"

    show emilia eyeroll6 at right2
    voice audio.emilia_v_response1a
    e "Fine. I’ll give you until tomorrow morning to decide."
    e "Let me emphasize this one last time, though, since you don't seem to be getting it."

    show emilia explain3 at right2
    voice audio.emilia_v_rush1c
    e "I’m a professional with exactly the experience you need, and I’m going out of my way to help you. The right choice is obvious."
    e "You need some guidance, and we can catch up! I don’t see any loss here."

    hide yoshi2_autumn
    hide yoshi2 sigh1
    hide yoshi talk1
    show yoshi_autumn at left2
    show yoshi talk1 at left2
    voice audio.yoshi_v_alright3
    yo "I’ll keep that in mind, Emilia…"

    show emilia evil2 at right2
    voice audio.emilia_v_amazed1a
    e "Excellent~! I expect nothing but great things from you, Yoshinori! It’s a pleasure to work with you again!"

    show emilia bold2 at right2
    voice audio.emilia_v_comp2a
    e "Everything will be alright now that I’m here!"
    e "Now, all this serious business has made me tired, not to mention all the walking around the camp to inspect!"

    show emilia bold6 at right2
    voice audio.emilia_v_bye2a
    e "I’ll take my leave for now and rest up! I still have to send an email report to Mr. Clermont, after all!"

    hide yoshi_autumn
    hide yoshi talk1
    show yoshi2_autumn at left2
    show yoshi2 talk3 at left2
    voice audio.yoshi_v_right4
    yo "R-Right. Goodnight, Emilia."

    show emilia happy4 at right2
    voice audio.emilia_v_bye1a
    e "Toodles~ "

    hide emilia_autumn2
    hide emilia happy4
    with dissolve

    $ renpy.pause (2.0, hard=True)
    show yoshi2 think1 at left2
    yo "..."

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
    $time_transition_sunset_to_night_fall()

    $ location = location_cabin
    $ time = timeline_timenight
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_quarters_autumn_night with fade
    play music ready_for_tomorrow loop
    play bgsound sfxloop_night loop

    play sound sfx_bagdrop
    show lloyd_autumn at p6_1
    show lloyd norm4 at p6_1
    show darius_autumn at p6_2
    show darius norm3 at p6_2
    show jin_autumn at p6_3
    show jin norm3 at p6_3
    show jin_glasses at p6_3
    show goro_autumn at p6_4
    show goro norm3 at p6_4
    show aiden_autumn at p6_5
    show aiden talk1 at p6_5
    show yoshi_autumn at p6_6
    show yoshi worry1 at p6_6
    a "Alright, Gramps! That should be all your stuff! "

    show goro talk1 at p6_4
    voice audio.goro_v_thanks1a1
    g "Thanks for helping me move in."

    show aiden comp3 at p6_5
    voice audio.aiden_v_alright3d
    a "Don’t mention it!"

    show jin worry2 at p6_3
    voice audio.jin_v_goro3b
    j "I hope it won’t be a hassle for you to stay here with us, Sir Goro…"

    show goro explain2 at p6_4
    voice audio.goro_v_response2a2
    g "It’s no problem. I don’t mind having some extra company."

    show aiden tease1 at p6_5
    voice audio.aiden_v_goro10a
    a "Haha, looks like you got demoted, huh Gramps?"

    show lloyd talk1 at p6_1
    voice audio.lloyd_v_aiden2c
    l "Careful what you say, Aiden. Sir Goro’s still in charge! You could get fired with one snap!"

    show aiden explain2 at p6_5
    voice audio.aiden_v_agree5b
    a "I know, I know, I’m just kidding around. Everyone hasn’t cracked a smile since that meeting."

    show jin sigh3 at p6_3
    voice audio.jin_v_emilia2c
    j "Looks like Ms. Emilia really said some upsetting things back there, huh?"

    hide goro_autumn
    hide goro explain2
    show goro2_autumn at p6_4
    show goro2 disappoint3 at p6_4
    voice audio.goro_v_think1a1
    g "The criticisms were rather trifling, but we don’t have much of a choice except to try and make do since Mr. Clermont placed her here."

    show aiden worry2 at p6_5
    voice audio.aiden_v_yeah1c3
    a "Yeah… And Yuri didn’t take it so well… I’ve never seen her lose her temper like that!"

    show lloyd happy1 at p6_1
    voice audio.lloyd_v_stars1a2
    l "On the upside, I think we’re all destined to connect better thanks to the divination I did earlier while you guys were in that meeting!"
    l "I interpreted my reading as “New Beginnings,” and that’s already true from the changes happening so far!"

    show jin confused2 at p6_3
    voice audio.jin_v_think2a1
    j "I still have no clue what you’re trying to say…"

    show darius happy1 at p6_2
    voice audio.darius_v_conj2a
    d "He means it’s good luck."

    show aiden happy1 at p6_5
    voice audio.aiden_v_yeah1a1
    a "Whatever mumbo jumbo Lloyd is saying, I agree! "
    a "Let’s look on the bright side, especially since we’ll be way busier starting tomorrow!"

    hide goro2_autumn
    hide goro2 disappoint3
    show goro_autumn at p6_4
    show goro talk1 at p6_4
    voice audio.goro_v_agree6a1
    g "That’s a very good mindset to have, Aiden."

    show lloyd tired1 at p6_1
    voice audio.lloyd_v_agree2a3
    l "Yeah, I bet the only time we’ll have to casually chat with each other will be at night after work, like this!"

    show aiden sleepy4 at p6_5
    voice audio.aiden_v_unsure1b
    a "I guess that’s my cue to hit the hay for now… "
    a "I have to get up earlier than usual and meal prep or we might get called out for being late again."

    show lloyd grin1 at p6_1
    voice audio.lloyd_v_laugh1a1
    l "See? ~ New beginnings! "

    show darius bored1 at p6_2
    voice audio.darius_v_lloyd4a
    d "That’s a generic phrase, Lloyd. "

    show lloyd pout2 at p6_1
    voice audio.lloyd_v_annoyed1a3
    l "Hmph, then tell me how it completely explains the coincidences! "

    show lloyd talk1 at p6_1
    voice audio.lloyd_v_conj2b1
    l "Anyway, we’ll be heading to sleep too!"

    show goro confused2 at p6_4
    voice audio.goro_v_unsure1a1
    g "Are you sure it’s alright for you to share a bed with Darius?"

    show darius tease2 at p6_2
    voice audio.darius_v_response1
    d "It’s fine. He won’t take up much space."

    show lloyd angry2 at p6_1
    voice audio.lloyd_v_greet2c1
    l "Hey! Not you too, Dar!"

    show jin talk2 at p6_3
    voice audio.jin_v_rush2a1
    j "You guys go ahead. I’m gonna take a shower since I’m just about to start my day."

    show aiden happy1 at p6_5
    voice audio.aiden_v_goodeve1a2
    a "Alright then! Good night, you guys~!"

    show darius relief2 at p6_2
    voice audio.darius_v_goodpm1
    d "Night."

    hide darius_autumn
    hide darius relief2
    hide lloyd_autumn
    hide lloyd angry2
    hide aiden_autumn
    hide aiden happy1
    hide jin_autumn
    hide jin talk2
    hide jin_glasses
    with dissolve

    show goro_autumn at left2
    show goro talk1 at left2
    show yoshi_autumn at right2
    show yoshi worry1 at right2
    with move

    hide goro_autumn
    hide goro talk1
    show goro2_autumn at left2
    show goro2 explain2 at left2
    voice audio.goro_v_so1a
    g "Now, do you mind telling me why you’re acting strangely again, Yoshinori?"
    g "Emilia didn’t say anything else back there to you, did she?"

    hide yoshi_autumn
    hide yoshi worry1
    show yoshi2_autumn at right2
    show yoshi2 sigh1 at right2
    voice audio.yoshi_v_well2
    yo "W-Well… She did, and it really gave me something to think about."

    hide goro2_autumn
    hide goro2 explain2
    show goro_autumn at left2
    show goro talk1 at left2
    voice audio.goro_v_think1a1
    g "If you’d like, I could reach out to Mr. Clermont and make some arrangements for a different inspector…"

    hide yoshi2_autumn
    hide yoshi2 sigh1
    show yoshi_autumn at right2
    show yoshi worry2 at right2
    voice audio.yoshi_v_oh2
    yo "O-Oh, no sir, please you don’t have to do that…"
    yo "Actually, for some reason, Emilia was trying to help clear up my role on this project."

    show goro talk3 at left2
    voice audio.goro_v_agree8a1
    g "That has been on your mind for the past week. "

    show yoshi explain2 at right2
    voice audio.yoshi_v_yessir4
    yo "Yes, sir… She actually offered to work directly with me, too. But I didn’t give her an answer just yet."
    yo "I think she genuinely wants to help me out, but that evaluation a while ago really seemed unnecessarily harsh."

    show goro upset4 at left2
    voice audio.goro_v_agree1a1
    g "Yes. She was rather strict and straightforward with her opinions. It kind of reminded me of how I was, and not in a good way."

    show goro sigh1 at left2
    voice audio.goro_v_sigh1a
    g "I don’t deny that I have flaws in my leadership… perhaps this project is a good opportunity for me to correct those."

    show yoshi talk1 at right2
    voice audio.yoshi_v_actually1a
    yo "That actually had me thinking, sir… If she had issues with the management, shouldn’t she have offered to work with you instead?"

    show goro think2 at left2
    voice audio.goro_v_well1a
    g "It seems Ms. Komarova is quite fond of you. She had a different tone when talking with you."
    g "I figured maybe since you two were past acquaintances, it had something to do with that."

    show yoshi think2 at right2
    voice audio.yoshi_v_yessir4
    yo "Yes, sir… I did notice that as well."
    yo "And that’s why I held back on her offer in the first place. "

    show goro happy1 at left2
    voice audio.goro_v_request4a1
    g "You should work with me instead then."
    g "Knowing what’s been going on in your mind since the start of this project, it only makes sense that I take you under my wing."

    show goro bold1 at left2
    voice audio.goro_v_heh1a
    g "With us working side by side, I can make sure to guide you every step of the way."

    show yoshi comp2 at right2
    voice audio.yoshi_v_sir1
    yo "I-I was thinking the same thing, sir…! After all, I realized I’m at my best when I’m working with you."

    show goro bold2 at left2
    voice audio.goro_v_agree4a2
    g "Exactly. "
    g "And more importantly, we can use this chance to further train you in the tasks and responsibilities of someone who will take over the camp one day."

    hide yoshi_autumn
    hide yoshi comp2
    show yoshi2_autumn at right2
    show yoshi2 comp6 at right2
    voice audio.yoshi_v_ah1
    yo "Ah… Well, I really don’t think I’m ready for that, sir…"

    hide goro_autumn
    hide goro bold2
    show goro2_autumn at left2
    show goro2 comp2 at left2
    voice audio.goro_v_comp4a
    g "You can learn as we go, I’m here to help after all."

    hide yoshi2_autumn
    hide yoshi2 comp6
    show yoshi_autumn at right2
    show yoshi comp2 at right2
    voice audio.yoshi_v_thanks1
    yo "Thank you so much for this opportunity, sir. It really cleared my mind about what my role in this project really is!"

    hide goro2_autumn
    hide goro2 comp2
    show goro_autumn at left2
    show goro laugh4 at left2
    voice audio.goro_v_response2a2
    g "It’s my pleasure."

    show goro talk1 at left2
    voice audio.goro_v_anyway2
    g "Anyways, I’ll let Ms. Komarova know as soon as possible that you will be declining her offer."

    show yoshi comp3 at right2
    voice audio.yoshi_v_comp1
    yo "I-It’s alright, sir! I can do it! I’m sure I can find a way to tell her as professionally as possible. What’s more important to me right now is the work we’ll do together."

    show goro play3 at left2
    voice audio.goro_v_laugh1b2
    g "Hehe…"

    show yoshi relief2 at right2
    voice audio.yoshi_v_gratitude1
    yo "I have to say, sir… I’m actually glad that you’re moving in here with us."

    show goro explain3 at left2
    voice audio.goro_v_well1a
    g "Well, either way, I did plan to move in here at some point to get closer with you guys…"
    g "That, or I was going to invite you to start staying over in my room to give the staff here more space."

    show yoshi talk3 at right2
    voice audio.yoshi_v_really2
    yo "A-Ah…! Really?"

    show goro happy1 at left2
    voice audio.goro_v_agree1a2
    g "Yes. But with how busy we’ve all been, I never had the chance."
    g "I guess Emilia’s stay here gave me a good push to actually do it."

    show yoshi happy2 at right2
    voice audio.yoshi_v_well1
    yo "Well, that’s a good way to look at it, sir!"

    show goro explain3 at left2
    voice audio.goro_v_response2a1
    g "All we have to do is to keep at it and stay true to the goals we have."

    show yoshi happy1 at right2
    voice audio.yoshi_v_yessir2
    yo "Yes, sir! I’ll do my best and stay by your side throughout the whole thing! "

    show goro happy2 at left2
    voice audio.goro_v_thanks1a1
    g "Thanks, Yoshinori. Let’s get some sleep, it’ll be a busy day tomorrow."

    show yoshi happy2 at right2
    voice audio.yoshi_v_goodpm3
    yo "Goodnight, sir!"

    show goro happy3 at left2
    voice audio.goro_v_goodpm3a1
    g "Good night, Yoshinori."

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
    $ time_transition_night_to_day_fall()
    $ renpy.pause (2.0, hard=True)
    $goro_route = True

    jump day1_goro
