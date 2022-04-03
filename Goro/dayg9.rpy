label day9_goro:
    $ day = "83"
    $ time = timeline_timeday
    $ location = location_cabin
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    $ working = True

    scene bg_gororoom_winter_day with fade
    play music ready_for_tomorrow_winter loop
    play bgsound sfxloop_birds loop

    show yoshi2_naked at center
    show yoshi2 pain1 at center
    voice audio.yoshi_v_groan1a
    yo "Nnghh…"

    show yoshi2 pain3 at center
    voice audio.yoshi_v_swear2
    yo "Damn, my whole body hurts… We got too wild last night…"
    yo "And it looks like Goro cleaned up after me, too… "

    show yoshi2 confused2 at center
    voice audio.yoshi_v_wait7
    yo "Hold on a second…"

    $crack_sx = False
    if crack_sx == True:
        yo "Where’s Goro and Aiden…?"

        show yoshi2 worry2 at center
        voice audio.yoshi_v_oops1
        yo "Goodness… I think I woke up way too late…"
        yo "Maybe they already headed to work…?"
    else:
        yo "Where’s Goro?"

        show yoshi2 worry2 at center
        voice audio.yoshi_v_oops1
        yo "Goodness… I think I woke up way too late…"
        yo "Maybe he started working in the office…?"

    show yoshi2 sigh4 at center
    voice audio.yoshi_v_sigh3a
    yo "*sigh* I knew it was a bad idea to drink yesterday…"
    yo "He must’ve tried waking me but I was too hungover to notice. "
    yo "All this booze is way out of character for me… I’ve been getting loose and careless since Goro’s been spoiling me."

    hide yoshi2_naked
    hide yoshi2 sigh4
    show yoshi_naked at center
    show yoshi shock2 at center
    voice audio.yoshi_v_wait3a
    yo "Wait… Maybe this is a test of my punctuality…? "

    show yoshi shock3 at center
    voice audio.yoshi_v_shock4
    yo "G-Gah! I better suit up and report in…!"

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

    $ location = location_office
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_office_winter_day with fade
    play music brand_new_day_winter loop
    show yoshi_winter at center
    show yoshi shock2 at center
    voice audio.yoshi_v_sorry2c
    yo "S-Sorry, I’m late! I was—"

    hide yoshi_winter
    hide yoshi shock2
    show yoshi2_winter at center
    show yoshi2 confused2 at center
    voice audio.yoshi_v_huh3a
    yo "H-Huh…? He’s not here either?"
    yo "He must be outside then. Today’s the day we resume work, after all."

    play sound sfx_doorknock
    show yoshi2_winter at left2
    show yoshi2 confused2 at left2
    with move

    show yuri_winter at right2
    show yuri shock3 at right2
    with dissolve

    voice audio.yuri_v_yoshi9a
    yu "Ah, Yoshi!"

    hide yoshi2_winter
    hide yoshi2 confused2
    show yoshi_winter at left2
    show yoshi talk1 at left2
    voice audio.yoshi_v_goodam1
    yo "Good morning, Yuri!"

    show yuri shock4 at right2
    voice audio.yuri_v_worry1a
    yu "Where’s Dad?! The workers just arrived! "

    hide yoshi_winter
    hide yoshi talk1
    show yoshi2_winter at left2
    show yoshi2 confused3 at left2
    voice audio.yoshi_v_huh1
    yo "Huh…? I thought he was outside already."

    show yuri shock5 at right2
    voice audio.yuri_v_wait1a1
    yu "Wait, he isn’t here? I thought he’d be with you!"

    show yoshi2 worry2 at left2
    voice audio.yoshi_v_no1
    yo "Unfortunately, not…"

    show yuri sigh3 at right2
    voice audio.yuri_v_sigh1a
    yu "*sigh* I didn’t receive any instructions from him… He usually takes care of this stuff."

    hide yoshi2_winter
    hide yoshi2 worry2
    show yoshi_winter at left2
    show yoshi confused2 at left2
    voice audio.yoshi_v_unsure2a
    yo "Did you check if he’s in the mess hall? Maybe he’s having his coffee."

    show yuri worry2 at right2
    voice audio.yuri_v_no1a2
    yu "No, I was there cleaning up with Aiden and Emilia earlier. He told me he last saw Dad in here…"

    hide yoshi_winter
    hide yoshi confused2
    show yoshi2_winter at left2
    show yoshi2 think5 at left2
    voice audio.yoshi_v_think1a
    yo "Hmm… He must not be at camp then…"

    show yuri confused2 at right2
    voice audio.yuri_v_unsure5a
    yu "I tried calling him and his phone was just ringing… Maybe he’s in a meeting?"

    show yoshi2 confused5 at left2
    voice audio.yoshi_v_uh1a
    yo "I don’t remember there being an appointment on his schedule."

    show yuri think3 at right2
    voice audio.yuri_v_sus2a
    yu "That’s weird… Where could Dad be? And how are we gonna handle everything today?"

    $ working = False
    $ shuffle_menu()
    menu():
        yu "That’s weird… Where could Dad be? And how are we gonna handle everything today?{fast}"
        "Only Goro knows what to do.":
            $ working = True
            $ score_goro -= 1
            $ score_top += 1
            show yoshi2 worry2 at left2
            voice audio.yoshi_v_unsure1a
            yo "I’m not sure… And he’s the only one who knows how to lead the project…"
            yo "We have to wait for him to get back before doing anything."

            show yuri worry3 at right2
            voice audio.yuri_v_unsure1a2
            yu "I don’t think that’s gonna work… We need to address the workers before they can start."
            yu "Maybe you can do it, Yoshi?"

            hide yoshi2_winter
            hide yoshi2 worry2
            show yoshi_winter at left2
            show yoshi talk3 at left2
            voice audio.yoshi_v_alright2
            yo "A-Alright, I’ll handle it until Goro gets back."
        "We should wait for Goro.":
            $ working = True
            $ score_goro -= 1
            $ score_bot += 1
            show yoshi2 worry2 at left2
            voice audio.yoshi_v_unsure1a
            yo "I’m not sure… Maybe we should wait for him before doing anything?"

            show yuri worry3 at right2
            voice audio.yuri_v_unsure1a2
            yu "I don’t think that’s gonna work… We need to address the workers before they can start."
            yu "Maybe you can do it, Yoshi?"

            hide yoshi2_winter
            hide yoshi2 worry2
            show yoshi_winter at left2
            show yoshi talk3 at left2
            voice audio.yoshi_v_alright2
            yo "A-Alright, I’ll handle it until Goro gets back."
        "I'll take over for now.":
            $ working = True
            $ score_goro += 1
            $ score_top += 1
            hide yoshi2_winter
            hide yoshi2 confused5
            show yoshi_winter at left2
            show yoshi talk1 at left2
            voice audio.yoshi_v_unsure1a
            yo "I’m not sure, but it’s probably important, so we’ll just have to handle it for now."
            yo "I’ll take over and brief everyone."
        "Goro's counting on us.":
            $ working = True
            $ score_goro += 1
            $ score_bot += 1
            hide yoshi2_winter
            hide yoshi2 confused5
            show yoshi_winter at left2
            show yoshi talk1 at left2
            voice audio.yoshi_v_unsure1a
            yo "I’m not sure, but Goro trusts us to handle things while he’s away."
            yo "Whatever he’s doing is probably important, so I’ll cover for him and brief everyone."

    show yuri comp2 at right2
    voice audio.yuri_v_thanks1a
    yu "Thanks, Yoshi! you’re a lifesaver! The workers should be waiting at the site with Lloyd and Darius!"

    show yoshi talk2 at left2
    voice audio.yoshi_v_bye1a
    yo "Got it! I’ll head there right away!"

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

    $ location = location_site
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_site7_winter_day with fade
    play music sunset_stroll_winter loop
    show yoshi_winter2 at center
    show yoshi talk1 at center
    voice audio.yoshi_v_so1a
    yo "—and that should cover the rest of the project timeline."
    yo "If you need any further clarifications on your tasks or schedules, please refer to Architect Sirius and Foreman Najjar for more details! "

    show yoshi talk2 at center
    voice audio.yoshi_v_bye6a
    yo "Dismissed!"
    all "Yes, sir!"

    show yoshi_winter2 at p5_3
    show yoshi talk3 at p5_3
    with move

    show yoichi_winter at p5_1
    show yoichi normal1 at p5_1
    show taiga_winter at p5_2
    show taiga normal1 at p5_2
    show lloyd_work2 at p5_4
    show lloyd norm1 at p5_4
    show darius_workw at p5_5
    show darius norm1 at p5_5
    show darius_goggles2 at p5_5
    with dissolve

    voice audio.yoshi_v_guys1
    yo "Ah, hey guys. Sorry about the slight delay. "
    yo "We couldn’t find Sir Goro this morning. He must’ve had to attend something urgent."

    show lloyd talk2 at p5_4
    voice audio.lloyd_v_agree2a1
    l "Yeah, and he had the updated schedule, so we couldn’t start."

    show darius happy2 at p5_5
    voice audio.darius_v_amazed1
    d "Good thing you have it with you, Yoshi."

    show yoshi happy2 at p5_3
    voice audio.yoshi_v_yeah2
    yo "Oh, yeah. I know where to find the agenda documents, so I figured I’d take over."
    yo "What brings you two scouts here, anyways?"

    show taiga talking2 at p5_2
    voice audio.taiga2_v_conjunction3a
    t "Well, we’re planning to help with the work."

    show darius relief2 at p5_5
    voice audio.darius_v_laugh1
    d "Taiga’s quite an aspiring carpenter."

    show yoichi angry1 at p5_1
    voice audio.yoichi_v_greet1d1
    yi "Hey! I didn’t sign up for this! You said we’re gonna blow some snow!"

    show taiga annoyed4 at p5_2
    voice audio.taiga_v_dummy1
    t "There’s barely any left, you dummy."

    show lloyd talk4 at p5_4
    voice audio.lloyd_v_conj2b2
    l "A-Anyway, Yoshi! We need to talk to you about something…!"

    show yoshi talk3 at p5_3
    voice audio.yoshi_v_ah1
    yo "Ah, what is it?"

    show lloyd worry2 at p5_4
    voice audio.lloyd_v_conj1b1
    l "Well, we’ve stumbled on a little problem… The storm from before destroyed some of the raw materials that weren’t properly stored…"

    hide yoshi_winter2
    hide yoshi talk3
    show yoshi2_winter2 at p5_3
    show yoshi2 worry2 at p5_3
    voice audio.yoshi_v_oops2
    yo "Oh no…"

    show lloyd sad4 at p5_4
    voice audio.lloyd_v_think3b1
    l "We have enough to last for a little while still, but it looks like we need to order more to cover what we lost."

    show darius talk2 at p5_5
    voice audio.darius_v_conj1a1
    d "We already had spare materials in case of something like this to be safe, but most of that was used on the repairs yesterday."

    show yoshi2 think2 at p5_3
    voice audio.yoshi_v_isee1
    yo "A-Ah, I see."

    show lloyd sigh5 at p5_4
    voice audio.lloyd_v_sorry1a1
    l "Sorry for causing you trouble first thing in the morning, Yoshi…"

    hide yoshi2_winter2
    hide yoshi2 think2
    show yoshi_winter2 at p5_3
    show yoshi comp2 at p5_3
    voice audio.yoshi_v_comp1
    yo "It’s alright, it can’t be helped. I assume we need a budget approval to order these?"

    show lloyd talk3 at p5_4
    voice audio.lloyd_v_agree2a2
    l "Y-Yes! We prepared this billing estimate for all the materials!"

    show darius talk1 at p5_5
    voice audio.darius_v_conj2b
    d "We just need a review and signature from Sir Goro and we’ll take care of the rest."

    show lloyd worry3 at p5_4
    voice audio.lloyd_v_aww1a1
    l "But since he’s not here right now, we can’t really proceed…"

    show yoshi bold2 at p5_3
    voice audio.yoshi_v_well1
    yo "Well, I can sign them for now! I’ll just run it by him as soon as he gets back!"

    show lloyd bold2 at p5_4
    voice audio.lloyd_v_praise3a
    l "Oh, that’d be great if you can!"

    show yoshi play3 at p5_3
    voice audio.yoshi_v_confident1
    yo "I know it’s not the standard policy, but sometimes we gotta bend the rules a little, don’t we?"

    show darius play2 at p5_5
    voice audio.darius_v_laugh2a
    d "Hehe… Now you sound like a real contractor…"

    show yoichi playful1 at p5_1
    voice audio.yoichi_v_confused1a1
    yi "Who’s this guy and what did you do to the old, boring sheriff?"

    show lloyd_work2 at p5_3
    show lloyd talk2 at p5_3
    with move

    show lloyd_work2 at p5_4
    show lloyd talk2 at p5_4
    with move

    voice audio.lloyd_v_gratitude3a
    l "Here’s the list!"

    show yoshi talk3 at p5_3
    voice audio.yoshi_v_think1a
    yo "Everything seems to be in order… And I don’t think we even need to ask Mr. Clermont for more funding, either. "

    show darius confused2 at p5_5
    voice audio.darius_v_shock1c1
    d "Oh? "

    show yoshi happy1 at p5_3
    voice audio.yoshi_v_alright1
    yo "We already allocated funds for situations like this. We’ll just use them!"

    show yoshi_winter2 at p5_4
    show yoshi bold2 at p5_4
    with move

    show yoshi_winter2 at p5_3
    show yoshi bold2 at p5_3
    with move

    voice audio.yoshi_v_lloyd3
    yo "Here you go, Lloyd. Signed and approved."

    show lloyd excited1 at p5_4
    voice audio.lloyd_v_amazed1a1
    l "Wow, thanks~!"
    l "I gotta say, Yoshi. You’ve gotten really good at this over the last few months."

    show darius happy2 at p5_5
    voice audio.darius_v_agree1a
    d "Yes. Every day, you’re becoming more and more like a leader."

    $ working = False
    $ shuffle_menu()
    menu():
        d "Yes. Every day, you’re becoming more and more like a leader.{fast}"
        "I have no choice but to step in.":
            $ working = True
            $ score_goro -= 2
            show yoshi explain2 at p5_3
            voice audio.yoshi_v_well2
            yo "Well, Goro is counting on me to run this place one day."
            yo "I have no choice but to step in."
        "I’m following Goro’s footsteps.":
            $ working = True
            $ score_goro -= 1
            show yoshi explain2 at p5_3
            voice audio.yoshi_v_laugh1
            yo "Haha, I’m just doing what Goro would. "
            yo "I’ve got to meet his expectations if I’m going to run this place one day."
        "I don’t want to take all the credit.":
            $ working = True
            $ score_goro += 1
            hide yoshi_winter2
            hide yoshi bold2
            show yoshi2_winter2 at p5_3
            show yoshi2 comp6 at p5_3
            voice audio.yoshi_v_laugh6
            yo "Ahehe, I can’t take all the credit, though. "
            yo "Goro’s the one who taught me how to handle this kind of stuff."
        "I’m only applying what I learned.":
            $ working = True
            $ score_goro += 2
            hide yoshi_winter2
            hide yoshi bold2
            show yoshi2_winter2 at p5_3
            show yoshi2 comp6 at p5_3
            voice audio.yoshi_v_laugh6
            yo "Ahehe, I learned from the best, and I’m only applying it."
            yo "Goro’s the one who taught me how to handle this kind of stuff."
    hide yoshi2_winter2
    hide yoshi2 comp6
    show yoshi_winter2 at p5_3
    show yoshi comp2 at p5_3
    voice audio.yoshi_v_conj4a
    yo "After working with him throughout the project, I’ve been trying to absorb all that knowledge and think like him too."

    show yoichi pout1 at p5_1
    voice audio.yoichi_v_hmph1a
    yi "Hmph, took you long enough! Spending all that time with the old geezer is finally paying off."
    yi "You actually sounded tough when you were doing all that serious talk a while ago – it’s way different from your lame, dorky-ass self!"

    show taiga playful2 at p5_2
    voice audio.taiga2_v_teasing1a
    t "So, you’re saying Yoshi is… cool?"

    show yoichi angry3 at p5_1
    voice audio.yoichi_v_insult1a
    yi "Don’t put words in my mouth, Dynamite! "

    hide yoshi_winter2
    hide yoshi comp2
    show yoshi2_winter2 at p5_3
    show yoshi2 shock2 at p5_3
    voice audio.yoshi_v_really3
    yo "Wh-What…? Really? "

    voice audio.yoshi_v_wait1
    yo "Wait… do you need anything from me, Yoichi?"

    show yoichi angry1 at p5_1
    voice audio.yoichi_v_disagree1b1
    yi "No! I’m just saying...! Don’t make such a big deal outta it! "

    hide yoshi2_winter2
    hide yoshi2 shock2
    show yoshi_winter2 at p5_3
    show yoshi comp2 at p5_3
    voice audio.yoshi_v_aww1
    yo "Aww~ I appreciate it, Yoichi."

    show yoichi annoyed4 at p5_1
    voice audio.yoichi_v_goro6a
    yi "It’s not ALL good though, you just went from dad to grandpa energy.  "

    hide yoshi_winter2
    hide yoshi comp2
    show yoshi2_winter2 at p5_3
    show yoshi2 sigh4 at p5_3
    voice audio.yoshi_v_sigh3a
    yo "*sigh* And I thought I was finally getting a compliment from you, Yoichi…"

    show lloyd talk3 at p5_4
    voice audio.lloyd_v_conj2a1
    l "Anyway, I guess we got all that we need for now! I’ll call the suppliers and they should be able to deliver by sundown!"

    hide yoshi2_winter2
    hide yoshi2 sigh4
    show yoshi_winter2 at p5_3
    show yoshi talk3 at p5_3
    voice audio.yoshi_v_confident3
    yo "If anything comes up again, don’t hesitate to ask me, alright? "

    show lloyd bold2 at p5_4
    voice audio.lloyd_v_agree3a1
    l "Aye, aye! Captain!"

    show darius happy2 at p5_5
    voice audio.darius_v_rush2
    d "Come with me, scouts. Let’s get crafting."

    show taiga excited1 at p5_2
    voice audio.taiga2_v_excited2a
    t "Sweet! I’m ready for some woodworking!"

    show yoichi angry3 at p5_1
    voice audio.yoichi_v_disagree1a3
    yi "Not me! I’m into a different kind of woodworking! Later, dorks!"

    hide yoichi_winter
    hide yoichi angry3
    with dissolve

    show taiga angry2 at p5_2
    voice audio.taiga2_v_hey1h
    t "Hey, get back here!"

    show darius comp5 at p5_5
    voice audio.darius_v_comp3a
    d "Let him be, Taiga. He’ll come back."

    show lloyd sigh4 at p5_4
    voice audio.lloyd_v_think1a2
    l "But it might be best if he doesn’t…"

    hide taiga_winter
    hide taiga angry2
    hide darius_workw
    hide darius_goggles2
    hide darius comp5
    hide lloyd_work2
    hide lloyd sigh4
    with dissolve

    show yoshi talk2 at p5_3
    voice audio.yoshi_v_alright1
    yo "Alright, that takes care of this department. I might as well check on the others."

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

    $ location = location_kitchen
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_kitchen_winter_day with fade
    play music go_with_the_flow loop
    play bgsound sfxloop_kitchen loop

    show aiden_apron at left2
    show aiden confused2 at left2
    show emilia_winter4 at right2
    show emilia scared1 at right2
    voice audio.aiden_v_emilia5a
    a "Emilia, where’s the lamb sauce?! "

    show emilia angry2 at right2
    voice audio.emilia_v_wait1a1
    e "I’m coming, I’m coming! What do you think this is? Hell’s kitchen?!"

    show emilia_winter4 at right
    show emilia angry2 at right
    show aiden_apron at center
    show aiden happy1 at center
    with move

    show yoshi_winter at left
    show yoshi norm1 at left
    with dissolve

    voice audio.aiden_v_hey2a1
    a "Hey there, Yoshi! "

    show yoshi confused2 at left
    voice audio.yoshi_v_emilia6
    yo "Oh hello, Aiden! And… Emilia…?"

    show emilia annoy2 at right
    voice audio.emilia_v_what2
    e "What’s with that look, Yoshi?"

    show yoshi comp3 at left
    voice audio.yoshi_v_laugh6
    yo "A-Ahehe… I’m just not used to seeing you working in the kitchen."

    show aiden play3 at center
    voice audio.aiden_v_agree4a
    a "I know, right? She suddenly came in and offered to help with today’s lunch service!"

    show emilia explain5 at right
    voice audio.emilia_v_well1
    e "Well, I already finished making all the beds in the workers’ cabins, and the laundry’s already running, so I might as well make myself useful."

    hide aiden_apron
    hide aiden play3
    show aiden2_apron at center
    show aiden2 comp6 at center
    voice audio.aiden_v_aww2a
    a "Hehe~ Isn’t she sweet? This is much better than you were playing the villain!"

    show emilia shy5 at right
    voice audio.emilia_v_tsun2a
    e "Don’t get the wrong idea. I thought it’d be nice to learn how to cook, and since you needed help, it was mutually beneficial."

    hide yoshi_winter
    hide yoshi comp3
    show yoshi2_winter at left
    show yoshi2 confused5 at left
    voice audio.yoshi_v_really1
    yo "Really? You seem more of a food critic than a chef to me..."

    show emilia eyeroll4 at right
    voice audio.emilia_v_hmph1a
    e "Hmph! I’m way past being a rich snob!"

    hide aiden2_apron
    hide aiden2 comp6
    show aiden_apron at center
    show aiden tease1 at center
    voice audio.aiden_v_yeah2b1
    a "Hahaha! You sure?"

    show emilia talk3 at right
    voice audio.emilia_v_conj2a
    e "Anyway, it’s something that I wish my parents had taught me. Or anyone for that matter."
    e "For most of my life I lived with maids doing everything for me, and I didn’t have the chance to learn anything useful."

    show emilia sigh1 at right
    voice audio.emilia_v_so1
    e "So, when I got cut off from that lifestyle, I realized I don’t really know anything at all."
    e "I had the chance to learn some of that when I was here as a scout, but I didn’t realize how important it was."

    hide yoshi2_winter
    hide yoshi2 confused2
    show yoshi_winter at left
    show yoshi happy1 at left
    voice audio.yoshi_v_encourage3
    yo "Well, as long as you have the drive, it’s never too late to learn! "

    show aiden bold2 at center
    voice audio.aiden_v_praise1a
    a "Yeah, and you’re doing great! You’ve taken a lot of work off my plate with all the stirring and washing!"

    show emilia disgust5 at right
    voice audio.emilia_v_ugh1
    e "Eugh, I didn’t know I was going to get this gross and sweaty from all of this though… Why did I wear white?!"

    show aiden bold5 at center
    voice audio.aiden_v_confident2a
    a "I told you it was gonna be hot in here! Just do like me!"

    show emilia angry2 at right
    voice audio.emilia_v_disgust1
    e "You men are so disgusting! No way I’m undressing in a work space! EVER!"

    hide yoshi_winter
    hide yoshi happy1
    show yoshi2_winter at left
    show yoshi2 comp3 at left
    voice audio.yoshi_v_laugh6
    yo "Okay, now that sounds like the Emilia we know…"

    show emilia angry3 at right
    voice audio.emilia_v_question4a
    e "Hey! How else was I supposed to react to that?! "

    show aiden happy2 at center
    voice audio.aiden_v_anyway1a
    a "Anyway~ What brings you here, Yoshi? Food’s not ready for another hour or two!"

    hide yoshi2_winter
    hide yoshi2 comp3
    show yoshi_winter at left
    show yoshi talk3 at left
    voice audio.yoshi_v_ah1
    yo "Ah, I was just doing the rounds to see if everything’s going well."
    yo "Also, I figured kitchen work would be pretty hectic, since there’s plenty of workers to feed again. So, I came by to help!"

    show aiden talk2 at center
    voice audio.aiden_v_yeah1a1
    a "Yeah, totally! We could use some more hands around here!"

    show emilia talk2 at right
    voice audio.emilia_v_oh2b
    e "Here, you can chop these veggies that Aiden needed. I can’t leave my station since this stew needs to be stirred constantly."

    show aiden_apron at left
    show aiden norm1 at left
    show yoshi_winter at center
    show yoshi norm1 at center
    with move

    show emilia confused2 at right
    voice audio.emilia_v_conj2a
    e "Anyway, I heard that Sir Goro has gone missing today? Is that true?"

    hide yoshi_winter
    hide yoshi norm1
    show yoshi2_winter at center
    show yoshi2 awkward4 at center
    voice audio.yoshi_v_yeah3
    yo "Ah, yeah… He wasn’t in the office when I woke up."

    hide aiden_apron
    hide aiden norm1
    show aiden2_apron at left
    show aiden2 confused5 at left
    voice audio.aiden_v_agree2e1
    a "Oh right! That’s why you had to do the announcement thingy a while ago…"

    show yoshi2 sigh4 at center
    voice audio.yoshi_v_conj4a
    yo "I’ll be honest, I was winging the whole thing. I just repeated the same stuff Goro said during the previous meetings."

    show emilia happy2 at right
    voice audio.emilia_v_amazed1a
    e "Either way, you handled the situation quite well if I do say so myself. I didn’t see you have any problems taking charge. "

    hide aiden2_apron
    hide aiden2 confused5
    show aiden_apron at left
    show aiden wink2 at left
    voice audio.aiden_v_confused1a2
    a "Might as well call Yoshi ‘Mr. Future President’, eh?"

    show yoshi2 awkward3 at center
    voice audio.yoshi_v_well3
    yo "Ah, well… I’m only taking over while he’s gone… "

    show emilia think2 at right
    voice audio.emilia_v_think1
    e "It is pretty strange for him to be absent like that without any warning."

    hide yoshi2_winter
    hide yoshi2 awkward3
    show yoshi_winter at center
    show yoshi explain2 at center
    voice audio.yoshi_v_think1a
    yo "He probably had to take care of something else more important."

    show emilia confused3 at right
    voice audio.emilia_v_disagree4a
    e "That doesn’t add up. What else is more important than Camp Buddy to him?"

    show aiden excited3 at left
    voice audio.aiden_v_oh1b
    a "Oh! Maybe it’s kinda like a test to see if Yoshi can handle being in charge for the day?"
    a "Kinda like a secret initiation!"

    show emilia annoy2 at right
    voice audio.emilia_v_disagree3a
    e "I doubt someone like him would do something silly like that…"

    show aiden relief2 at left
    voice audio.aiden_v_but1a2
    a "Yeah, but he’s told Yoshi a ton of times before that he’ll make him head of the camp once he retires!"

    show emilia confused2 at right
    voice audio.emilia_v_yoshi3
    e "You think you have what it takes, Yoshi?"

    $ working = False
    $ shuffle_menu()
    menu():
        e "You think you have what it takes, Yoshi?{fast}"
        "I have to prove myself first.":
            $ working = True
            $ score_goro -= 1
            show yoshi talk1 at center
            voice audio.yoshi_v_no1
            yo "I have to prove myself to him first. "
            yo "Only Goro would know when it’s time."
        "I'm not sure if I even want that.":
            $ working = True
            show yoshi sigh1 at center
            voice audio.yoshi_v_conj4a
            yo "Honestly, I’m not sure that I even want that…"
            yo "Goro has so much responsibility, and taking it on myself is intimidating..."
        "I'd rather Goro stick around.":
            $ working = True
            $ score_goro += 1
            show yoshi comp2 at center
            voice audio.yoshi_v_conj4a
            yo "Honestly, I’d rather Goro stick around and work together."
            yo "He handles so much and does it all so well. I’m content to keep assisting him for now."
        "I would rather us lead together.":
            $ working = True
            $ score_goro += 2
            show yoshi comp2 at center
            voice audio.yoshi_v_conj4a
            yo "Honestly, I’d rather stay by his side than take over."
            yo "If we work together, then we can share the burden and grow as partners."

    show emilia angry2 at right
    voice audio.emilia_v_surprised1a
    e "My goodness, Yoshinori! That’s not a very ambitious mindset!"
    e "You underestimate yourself far too much – you have the skills and charisma needed to lead the entire camp if you wanted to."

    hide aiden_apron
    hide aiden relief2
    show aiden2_apron at left
    show aiden2 tease2 at left
    voice audio.aiden_v_laugh1b2
    a "Hehe, just look at Emilia, she almost got away with being our manager~  "

    show emilia angry5 at right
    voice audio.emilia_v_request1a
    e "*ehem* My point is, Sir Goro isn’t going to be here forever – at some point, he’s going to want to take it easy."
    e "After all, it’s been what…? A decade since this place started? You’re going to have to step up eventually!"

    hide yoshi_winter
    hide yoshi comp2
    hide yoshi talk1
    hide yoshi sigh1
    show yoshi2_winter at center
    show yoshi2 think1 at center
    voice audio.yoshi_v_think1b
    yo "Hmmm…"

    show aiden2 comp3 at left
    voice audio.aiden_v_comp3a
    a "Chill, Emilia. I’m sure there’s plenty of time for Yoshi to think about all that!"

    show emilia worry2 at right
    voice audio.emilia_v_agree1b1
    e "R-Right. I wasn’t trying to be overbearing. I just thought you should know, Sir Goro ought to be proud to one day leave this place to you."

    show yoshi2 comp2 at center
    voice audio.yoshi_v_thanks6
    yo "Th-Thanks, Emilia…"

    hide aiden2_apron
    hide aiden2 comp3
    show aiden_apron at left
    show aiden talk1 at left
    voice audio.aiden_v_anyway1a
    a "Anyway! I think we’re done with the chopping! That should be all the prep work we need help with, all that’s left is the actual cooking!"
    a "You can get back to doing your management stuff while Gramps is gone, Yoshi! Thanks for the help!"

    hide yoshi2_winter
    hide yoshi2 comp2
    show yoshi_winter at center
    show yoshi happy1 at center
    voice audio.yoshi_v_okay2
    yo "Okay, then! There’s just one last department I have to check!"
    yo "I’ll be at the office if you guys need me, alright?"

    show aiden happy1 at left
    voice audio.aiden_v_bye1a
    a "Gotcha! See ya, Yoshi!"

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

    $ location = location_office
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_office_winter_day with fade
    play music old_familiar_home loop

    play sound sfx_doorknock
    $ renpy.pause (1.0, hard=True)
    show jin_autumn at left2
    show jin_glasses at left2
    show jin norm1 at left2
    show yuri_autumn at right2
    show yuri talk2 at right2
    voice audio.yuri_v_rush1a1
    yu "Come in~!"

    play sound sfx_dooropen
    show jin_autumn at left
    show jin_glasses at left
    show jin norm1 at left
    show yuri_autumn at center
    show yuri norm1 at center
    with move

    show yoshi_winter at right
    show yoshi happy2 at right
    with dissolve

    voice audio.yoshi_v_hey1
    yo "Hey there, Yuri, Jin!"

    show yuri talk3 at center
    voice audio.yuri_v_greet2a
    yu "Hi, Yoshi! For a second, I thought Dad had come back."

    show jin awkward4 at left
    voice audio.jin_v_think2a1
    j "Umm… I hope you don’t mind us using Sir Goro’s computer here, Yoshi…"

    show yoshi talk1 at right
    voice audio.yoshi_v_disagree3
    yo "Not at all! What are you up to?"

    show jin talk2 at left
    voice audio.jin_v_conj2a1
    j "Well, this morning, the workers and I set up cameras around the camp based on Yuri’s recommendations."
    j "Now we’re just connecting them all to the network and making sure they’re working properly."

    show yoshi amazed1 at right
    voice audio.yoshi_v_amazed1c
    yo "Oh, wow! I can’t believe we have security cameras now!"

    hide yuri_autumn
    hide yuri talk3
    show yuri2_autumn at center
    show yuri2 fangirl2 at center
    voice audio.yuri_v_response2a1
    yu "Finally, right?! Now, nothing can escape my eyes! "

    hide yoshi_winter
    hide yoshi amazed1
    show yoshi2_winter at right
    show yoshi2 awkward4 at right
    voice audio.yoshi_v_yuri6
    yo "Th-That’s kinda creepy, Yuri…"

    hide yuri2_autumn
    hide yuri2 fangirl2
    show yuri_autumn at center
    show yuri angry2 at center
    voice audio.yuri_v_what2a
    yu "What?! I meant bullying, Yoshi! What were you even thinking?!"

    hide yoshi2_winter
    hide yoshi2 awkward4
    show yoshi_winter at right
    show yoshi angry5 at right
    voice audio.yoshi_v_ehem1a
    yo "*ehem* Anyway, are they working, Jin?"

    show jin happy2 at left
    voice audio.jin_v_yes5a
    j "Yep! We have ten connected so far, mostly around the perimeter and activity areas."
    j "For example… we have one in the mess hall… the campgrounds… entrance… and here at the office!"

    show yoshi shock2 at right
    voice audio.yoshi_v_oh2
    yo "Oh yeah! I can see us on the monitor!"

    show jin talk3 at left
    voice audio.jin_v_conj3a1
    j "We made it where only admins can access the footage, and only you and Sir Goro have those accounts for now. "
    j "It’s password protected too, so you don’t have to worry about anyone else sneaking a peek!"

    show jin awkward6 at left
    voice audio.jin_v_oh4a
    j "Oh, and the password is CUMBODY69…."

    show yuri excited2 at center
    voice audio.yuri_v_laugh1a1
    yu "Like it? I came up with it myself!"

    show yoshi irked3 at right
    voice audio.yoshi_v_sigh3a
    yo "O-Obviously…"

    show jin comp3 at left
    voice audio.jin_v_laugh3a
    j "You can always change it later…!"

    show yoshi happy1 at right
    voice audio.yoshi_v_alright2
    yo "Alright! Good job, you two! That’s a huge task off your to-do list!"

    show jin happy2 at left
    voice audio.jin_v_thanks1a1
    j "Thank you! There’s gonna be another batch of cameras to install in the spring when they finish the expansion site."
    j "But for the rest of the winter, it’ll most likely be web design work for me!"

    show yoshi happy2 at right
    voice audio.yoshi_v_yeah2
    yo "Yeah. That sounds perfect!"

    show yuri talk2 at center
    voice audio.yuri_v_oh1a
    yu "Oh, I almost forgot to ask… How are the other departments doing?"

    show yoshi explain4 at right
    voice audio.yoshi_v_comp5
    yo "Everything’s going smoothly! I did a quick patrol around the camp too just to be sure!"

    show yuri worry2 at center
    voice audio.yuri_v_think1a1
    yu "Still no sign of Dad?"

    hide yoshi_winter
    hide yoshi explain4
    show yoshi2_winter at right
    show yoshi2 worry2 at right
    voice audio.yoshi_v_no1
    yo "No, unfortunately. But luckily, I’ve been able to handle everything so far!"

    show yuri sigh3 at center
    voice audio.yuri_v_sorry1c1
    yu "*sigh* I’m sorry Dad suddenly went missing. I thought he was way past his habit of doing things on his own without telling anyone."
    yu "And I’m shocked he picked an important day like this of all days…"

    hide yoshi2_winter
    hide yoshi2 worry2
    show yoshi_winter at right
    show yoshi comp2 at right
    voice audio.yoshi_v_comp1
    yo "It’s alright. I’m sure he had a good reason! We’ll keep everything in place until he comes back."

    show yuri worry4 at center
    voice audio.yuri_v_unsure3a
    yu "I guess…"

    show yoshi talk1 at right
    voice audio.yoshi_v_conj2a
    yo "Speaking of which, I’ll get some admin work done too!"
    yo "There must be a new wave of e-mails we need to respond to! Do you mind if I use the computer, Jin?"

    show jin talk2 at left
    voice audio.jin_v_agree1c1
    j "S-Sure…! Here you go. "

    show jin_autumn at right
    show jin_glasses at right
    show jin confuseddn2 at right
    show yoshi_winter at left
    show yoshi norm3 at left
    with move

    voice audio.jin_v_conj4a1
    j "By the way, I forgot to mention, but this might be relevant… Mr. Clermont called me a while ago…"

    show yuri confused3 at center
    voice audio.yuri_v_william4a
    yu "Mr. Clermont…? That’s odd."

    show jin awkward4 at right
    voice audio.jin_v_yeah2a
    j "Y-Yeah, it freaked me out a little… I thought I might’ve been in trouble or something…"

    show yuri confused4 at center
    voice audio.yuri_v_worry1a
    yu "What did he tell you? Did he need anything?"

    show jin explain3 at right
    voice audio.jin_v_conj2b1
    j "Well… He was actually looking for Sir Goro. He said that he couldn’t contact him this morning…"

    show yoshi shock1 at left
    show yuri shock2 at center
    voice audio.yuri_v_what3a
    yu "What…? Even Mr. Clermont can’t reach him? "

    show jin worry2 at right
    voice audio.jin_v_worry2a
    j "Do you guys think there’s something wrong…?"

    show yuri worry4 at center
    voice audio.yuri_v_worry3a
    yu "He wasn’t answering my calls this morning either… I’m starting to get worried…"
    yu "Did Mr. Clermont say anything else to you…? "

    show jin confused3 at right
    voice audio.jin_v_conj2c1
    j "W-Well… He kept mentioning an email Sir Goro sent him this morning… I couldn’t really follow since I didn’t know the full story."

    show yuri talk2 at center
    voice audio.yuri_v_yoshi5b
    yu "Yoshi! You’re in the emails now, right? Can you check that out for us?  "

    show yoshi panic1 at left
    yo "..."

    show yuri confused3 at center
    voice audio.yuri_v_yoshi7
    yu "Yoshi, are you listening?!"

    show yoshi_winter at center
    show yoshi panic1 at center
    show yuri_autumn at left
    show yuri irked1 at left
    with move

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    voice audio.yuri_v_hey5b
    yu "H-Hey! "

    hide yoshi_winter
    hide yoshi panic1
    show yoshi2_winter at center
    show yoshi2 awkward4 at center
    voice audio.yoshi_v_ah4
    yo "A-Ah! S-Sorry, Yuri… I…"

    show yuri shock2 at left
    voice audio.yuri_v_worry1a
    yu "What happened…? You look like you’ve seen a ghost..."

    show yoshi2 worry2 at center
    voice audio.yoshi_v_sigh3a
    yo "I just got caught off guard by what I read…"

    show yuri confused2 at left
    voice audio.yuri_v_what3a
    yu "What is it?"

    show yoshi2 sigh1 at center
    voice audio.yoshi_v_well1
    yo "W-Well… It’s about the offer Mr. Clermont gave Goro yesterday. He wants to reopen the other branches of Camp Buddy…"

    hide yuri_autumn
    hide yuri confused2
    show yuri2_autumn at left
    show yuri2 excited3 at left
    voice audio.yuri_v_omg1a
    yu "What?! Reopen?! OMG!"

    show jin shock3 at right
    voice audio.jin_v_amazed2a
    j "That’s big news! This is probably what Mr. Clermont was talking about on our call…"

    show yuri2 amazed3 at left
    voice audio.yuri_v_excited1a
    yu "How come Dad didn’t tell us about it?! This is like the biggest offer we’ve ever received! "
    yu "Even bigger than the sponsorship!"

    show yoshi2 awkward3 at center
    voice audio.yoshi_v_actually2a
    yo "A-Actually… He told me yesterday after Mr. Clermont left…  "

    hide yuri2_autumn
    hide yuri2 amazed3
    show yuri_autumn at left
    show yuri irked1 at left
    voice audio.yuri_v_hmph1a
    yu "Oh, so you knew about this! You two are being secretive now, huh?!"

    show yoshi2 shock2 at center
    voice audio.yoshi_v_no4
    yo "N-No, Yuri! That’s all I know… and that he didn’t give an answer right away."
    yo "But seeing this… I don’t understand why Goro left out something so important…"

    show yuri confused2 at left
    voice audio.yuri_v_confused3a1
    yu "What do you mean?"

    show yoshi2 think2 at center
    voice audio.yoshi_v_but2
    yo "With the offer, everything here at this branch would remain the same and Goro would still be the leader, but…"
    yo "For the new branch, Mr. Clermont wants me… to be the president."

    hide yuri_autumn
    hide yuri confused2
    show yuri2_autumn at left
    show yuri2 fangirl1 at left
    voice audio.yuri_v_kyaa1a
    yu "Oh my god, Yoshi!!! I’m sooo happy for you! Isn’t this your dream?!"

    show jin shock2 at right
    voice audio.jin_v_shock1a
    j "Wow… Mr. Clermont is really going all out on Camp Buddy…"

    show yoshi2 worry2 at center
    voice audio.yoshi_v_disagree4a
    yo "N-Not to rain on everyone’s parade, but… "
    yo "Apparently, Goro already sent a reply this morning…"

    show yoshi2 sad4 at center
    voice audio.yoshi_v_sigh3a
    yo "He turned down the offer."

    play music where_am_i loop
    hide yuri2_autumn
    hide yuri2 fangirl1
    show yuri_autumn at left
    show yuri shock5 at left
    voice audio.yuri_v_what5a
    yu "WHAT?!  " with vpunch

    show jin worry4 at right
    voice audio.jin_v_confused2b1
    j "H-Huh?! B-But, why?!"

    show yoshi2 sad5 at center
    voice audio.yoshi_v_unsure1b
    yo "I… I’m just as shocked as you guys…"

    show yuri panic2 at left
    voice audio.yuri_v_angry4a1
    yu "No, no, no… You can’t be serious! Why would he turn down something we’ve all been working so hard for?!"

    show yoshi2 worry2 at center
    voice audio.yoshi_v_think1b
    yo "I don’t understand either… I thought he’d at least ask my opinion about it…"
    yo "Especially since I thought I was doing so much better working alongside him…"

    show jin sad5 at right
    voice audio.jin_v_confused3b1
    j "Th-This really doesn’t make sense… I always thought Sir Goro wanted the camp to grow…"

    show yuri angry2 at left
    voice audio.yuri_v_angry6a
    yu "What was he thinking..? There’s literally nothing to lose here…!"
    yu "This is like… a life-changing opportunity, not only for the camp, but for you, Yoshi! "

    $ working = False
    $ shuffle_menu()
    menu():
        yu "This is like… a life-changing opportunity, not only for the camp, but for you, Yoshi!{fast}"
        "Maybe he thinks I’m not ready…":
            $ working = True
            $ score_goro -= 2
            show yoshi2 sigh1 at center
            voice audio.yoshi_v_sad1
            yo "Maybe he thinks I’m not ready for it…"

            show yuri angry2 at left
            voice audio.yuri_v_what5a
            yu "What?! But everyone knows you’re the best candidate for the job…!"

            voice audio.yuri_v_sus2a
            yu "Something’s not adding up here… I think the only way to know is to ask Dad directly…"
        "He knows what’s best for the camp.":
            $ working = True
            $ score_goro -= 1
            show yoshi2 sigh1 at center
            voice audio.yoshi_v_sad1
            yo "Maybe this is for the best…"

            show yuri angry2 at left
            voice audio.yuri_v_what5a
            yu "What?! But everyone knows you’re the best candidate for the job…!"

            voice audio.yuri_v_sus2a
            yu "Something’s not adding up here… I think the only way to know is to ask Dad directly…"
        "There's no way to know.":
            $ working = True
            $ score_goro += 1
            show yoshi2 sigh1 at center
            voice audio.yoshi_v_sigh3a
            yo "There’s no way to know unless we ask Goro himself…"

            show yuri think2 at left
            voice audio.yuri_v_sus2a
            yu "Y-Yeah… Something’s not adding up here…"
        "There must be a reason.":
            $ working = True
            $ score_goro += 2
            show yoshi2 sigh1 at center
            voice audio.yoshi_v_sigh3a
            yo "There must be a reason he made this decision…"
            yo "The only way we’ll know is if we ask Goro directly… "

            show yuri think2 at left
            voice audio.yuri_v_sus2a
            yu "Y-Yeah… Something’s not adding up here…"

    play sound sfx_doorknock
    show yuri_autumn at p4_1
    show yuri shock1 at p4_1
    show jin_autumn at p4_3
    show jin_glasses at p4_3
    show jin shock1 at p4_3
    show yoshi2_winter at p4_2
    show yoshi2 shock1 at p4_2
    with move

    show lloyd_work2 at p5_5
    show lloyd talk4 at p5_5
    with dissolve

    voice audio.lloyd_v_sorry1a2
    l "Sorry for barging in, but the materials just arrived, Yoshi!"

    hide yoshi2_winter
    hide yoshi2 sigh1
    show yoshi_winter at p4_2
    show yoshi talk3 at p4_2
    voice audio.yoshi_v_ah2
    yo "Ah, right…! "
    yo "We can take care of this later, guys. Let me know if Goro calls back."

    show yuri worry2 at p4_1
    voice audio.yuri_v_alright1b1
    yu "Alright, Yoshi…"

    show yoshi talk1 at p4_2
    voice audio.yoshi_v_rush5
    yo "Let’s go, Lloyd."

    hide yoshi_winter
    hide yoshi talk1
    hide lloyd_work2
    hide lloyd talk4
    with dissolve

    show yuri sad4 at p4_1
    show jin worry1 at p4_3
    voice audio.yuri_v_goro6a
    yu "Dad…"

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black
    hide screen location
    hide screen timeline
    hide screen quick_menu
    $quick_menu = False
    with fade
    $ time_transition_day_to_sunset_winter2()
    $ renpy.pause (2.0, hard=True)

    $ location = location_entrance
    $ time = timeline_timesunset
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_entrance_winter_sunset with fade
    play bgsound sfxloop_windy loop

    show darius_workw2 at left
    show darius talk4 at left
    show lloyd_work2 at center
    show lloyd norm4 at center
    show yoshi_winter2 at right
    show yoshi norm3 at right
    voice audio.darius_v_amazed2
    d "I think that’s the last sack. We can take it from here."

    show lloyd comp2 at center
    voice audio.lloyd_v_gratitude1b1
    l "Thanks again for helping us take care of the deliveries today, Yoshi!"

    show yoshi talk1 at right
    voice audio.yoshi_v_response3a
    yo "No problem."

    show lloyd bold2 at center
    voice audio.lloyd_v_encourage1a
    l "We’ll head back to the site and put these in temporary storage while there’s still daylight!"

    show yoshi explain2 at right
    voice audio.yoshi_v_sure3
    yo "Sure thing, Lloyd."

    show darius confused2 at left
    voice audio.darius_v_confused1b
    d "Are you alright, Yoshi? You seem uneasy."

    hide yoshi_winter2
    hide yoshi explain2
    show yoshi2_winter2 at right
    show yoshi2 worry2 at right
    voice audio.yoshi_v_ah3
    yo "A-Ah…! I’m fine!"

    show darius comp2 at left
    voice audio.darius_v_comp2
    d "Give yourself a break, Yoshi. You’ve been handling everything all day."

    show yoshi2 sad4 at right
    voice audio.yoshi_v_thanks6
    yo "Th-Thanks. You guys can go ahead, I’ll catch up."

    show lloyd confused2 at center
    voice audio.lloyd_v_think2a1
    l "Umm… Alright…!"

    show darius talk1 at left
    voice audio.darius_v_bye1a
    d "See you inside, Yoshi. "

    hide darius_workw2
    hide darius talk1
    hide lloyd_work2
    hide lloyd confused2
    with dissolve

    show yoshi2_winter2 at center
    show yoshi2 sad1 at center
    with move

    yo "..."

    show yoshi2 upset1 at center
    yo "{i}(Looking up at Camp Buddy’s arch... We’ve really come a long way since that first term…){/i}"
    yo "{i}(It’s been my dream to work here and see the camp grow. And I always believed Goro thought the same.){/i}"

    show yoshi2 sad2 at center
    yo "{i}(I can think of a lot of reasons why he might turn down an opportunity like this but… what’s he thinking?){/i}"
    yo "{i}(I really need to know…){/i}"

    play sound sfx_harleyarriveshutoff
    show yoshi2 confused2 at center
    voice audio.yoshi_v_what3
    yo "Wh-What’s that sound…?"

    stop sound
    show yoshi2_winter2 at right2
    show yoshi2 shock1 at right2
    with move

    hide yoshi2_winter2
    hide yoshi2 confused2
    show yoshi_winter2 at right2
    show yoshi shock1 at right2
    yo "...!!"

    show goro_biker at left2
    show goro play1 at left2
    play music brand_new_day_winter loop
    show cg_fade at truecenter
    show fxg11 1 at fx_pos
    with dissolve

    voice audio.yoshi_vsg21_line1
    yo "G-Goro?! "

    voice audio.goro_vsg21_line1
    g "I’m back, Yoshinori. Were you waiting for me?"

    voice audio.yoshi_vsg21_line2
    yo "Y-Yeah…! I’ve been looking for you all day."

    show fxg11 2 at fx_pos with Dissolve(0.25)
    voice audio.goro_vsg21_line2
    g "I know I left without telling anyone, but I wanted to surprise you."

    voice audio.yoshi_vsg21_line3
    yo "We couldn’t contact you, and we were all getting worried..."

    voice audio.goro_vsg21_line3
    g "Ah, sorry about that. I couldn’t answer my phone while I was driving."

    voice audio.yoshi_vsg21_line4
    yo "Wh-Where have you been?"

    show fxg11 3 at fx_pos with Dissolve(0.25)
    voice audio.goro_vsg21_line4
    g "Well, I got caught up with a lot of things… but mostly, I got this bad boy back from my friend. "

    voice audio.goro_vsg21_line5
    g "It’s been well-maintained even after all these years, but I still had it outfitted and tuned up to be ready for tonight."

    voice audio.goro_vsg21_line6
    g "Pretty slick, huh?"
    yo "..."

    show fxg11 1 at fx_pos with Dissolve(0.25)
    voice audio.goro_vsg21_line7
    g "Well, what are you waiting for? Let’s ride!"

    $ working = False
    $ shuffle_menu()
    menu():
        g "Well, what are you waiting for? Let’s ride!{fast}"
        "What about the camp?":
            $ working = True
            $ score_goro -= 2
            voice audio.yoshi_vsg21_line5a
            yo "Wh-What about the camp…?"

            voice audio.goro_vsg21_line8a
            g "Don’t worry about it. I already texted Yuri that we’re headed out."
        "We're going out?":
            $ working = True
            $ score_goro -= 1
            voice audio.yoshi_vsg21_line5b
            yo "W-We’re going out…?"

            voice audio.goro_vsg21_line9bcd
            g "Don’t worry about the camp, I already texted Yuri that we’re headed out."
        "What's going on?":
            $ working = True
            $ score_goro += 1
            voice audio.yoshi_vsg21_line5c
            yo "What’s going on? This is all too sudden…"

            voice audio.goro_vsg21_line8c
            g "You’ll find out."
            yo "..."

            voice audio.goro_vsg21_line9bcd
            g "Don’t worry about the camp, I already texted Yuri that we’re headed out."
        "Where are you taking me?":
            $ working = True
            $ score_goro += 2
            voice audio.yoshi_vsg21_line5d
            yo "Wh-Where are you taking me?"

            voice audio.goro_vsg21_line8d
            g "I don’t want to spoil it. Just come with me."
            yo "..."

            voice audio.goro_vsg21_line9bcd
            g "Don’t worry about the camp, I already texted Yuri that we’re headed out."

    voice audio.yoshi_vsg21_line6
    yo "Ah…"

    hide cg_fade
    hide fxg11 1
    with dissolve

    show goro play2 at left2
    show yoshi shock1 at right2
    voice audio.goro_v_here1a
    g "Here, wear this."
    g "*throws jacket to Yoshinori*"

    show yoshi awkward3 at right2
    voice audio.yoshi_v_alright2
    yo "A-Alright…!"

    show goro bold2 at left2
    voice audio.goro_v_rush1a1
    g "Let’s go."

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black with fade
    yo "{i}I was so caught off guard by Goro’s sudden appearance, I didn’t even have time to ask him about the offer…{/i}"
    yo "{i}He was acting strangely, but he didn’t seem upset… I wonder where he’s taking me…{/i}"

    scene cg black
    hide screen location
    hide screen timeline
    hide screen quick_menu
    $quick_menu = False
    with fade
    play sound sfx_harleystart
    $ renpy.pause (4.0, hard=True)

    $ location = location_forest
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene cgg10 1 with fade
    play music old_familiar_home loop
    play bgsound sfx_harleydriving loop

    voice audio.goro_vsg22_line1
    g "You holdin’ up ok back there, Yoshinori?"

    voice audio.yoshi_vsg22_line1
    yo "Y-Yeah…!"

    voice audio.goro_vsg22_line2
    g "How’s the ride so far? Hope you’re enjoying it~!"

    voice audio.yoshi_vsg22_line2
    yo "I-It’s thrilling…! But I’m kinda scared that we’ll crash at the speed we’re going…! "

    voice audio.goro_vsg22_line3
    g "This isn’t fast at all, hahaha! And trust me, I rode through way worse than this back in my day! I’ve still got the skills to handle it!"

    voice audio.yoshi_vsg22_line3
    yo "B-But the roads can get icy too…!"

    voice audio.goro_vsg22_line4
    g "It’s not as cold today, so don’t worry ‘cause I fitted this bad boy out with some winter tires, so we’re covered!"

    show cgg10 2 with Dissolve(0.25)
    voice audio.yoshi_vsg22_line4
    yo "I didn’t know you were such a daredevil, Goro…! We didn’t even put helmets on! We might not make it back home alive at this rate…!"

    voice audio.goro_vsg22_line5
    g "Hahaha! It’s not really that far of a ride, we should be fine!"

    voice audio.yoshi_vsg22_line5
    yo "You still haven’t told me where we’re going."

    voice audio.goro_vsg22_line6
    g "Just wait, and you’ll see!"

    voice audio.yoshi_vsg22_line6
    yo "*sigh* Okay…"

    show cgg10 3 with Dissolve(0.25)
    yo "{i}(I’ve never seen Goro this excited before… He seems to be really happy that we’re riding together.){/i}"
    yo "{i}(It makes me feel guilty that I can’t get what I found out earlier off my mind…){/i}"

    show cgg10 4 with Dissolve(0.25)
    voice audio.goro_vsg22_line7
    g "So, how did things go back at camp while I was gone?"

    voice audio.yoshi_vsg22_line7
    yo "W-Well, the workers came back so it got quite busy…"

    show cgg10 5 with Dissolve(0.25)
    voice audio.goro_vsg22_line8
    g "Ah, shit… I completely forgot that was today."

    $ working = False
    $ shuffle_menu()
    menu():
        g "Ah, shit… I completely forgot that was today.{fast}"
        "I could’ve used your help.":
            $ working = True
            $ score_goro -= 2
            show cgg10 6a with Dissolve(0.25)
            voice audio.yoshi_vsg22_line8a
            yo "I managed to get things moving, but… I could’ve really used your help."

            voice audio.goro_vsg22_line9a
            g "Ah, I’m sorry about that… and for going out without telling you."

            show cgg10 7 with Dissolve(0.25)
            voice audio.goro_vsg22_line11
            g "I didn’t mean to neglect work today. I just had something really important to take care of."

            voice audio.yoshi_vsg22_line9
            yo "I-I see…"
        "That’s not like you at all.":
            $ working = True
            $ score_goro -= 1
            show cgg10 6a with Dissolve(0.25)
            voice audio.yoshi_vsg22_line8b
            yo "Th-That’s not like you at all, Goro…"

            voice audio.goro_vsg22_line9b
            g "Ah… I know. I’m sorry for going out without telling you."

            show cgg10 7 with Dissolve(0.25)
            voice audio.goro_vsg22_line11
            g "I didn’t mean to neglect work today. I just had something really important to take care of."

            voice audio.yoshi_vsg22_line9
            yo "I-I see…"
        "I took care of it.":
            $ working = True
            $ score_goro += 1
            show cgg10 6b with Dissolve(0.25)
            voice audio.yoshi_vsg22_line8c
            yo "D-Don’t worry…! I took care of it. "

            voice audio.goro_vsg22_line9c
            g "Ah, that’s good to know."

            show cgg10 7 with Dissolve(0.25)
            voice audio.goro_vsg22_line10cd
            g "I’m really sorry for going out without telling you. "

            voice audio.goro_vsg22_line11
            g "I didn’t mean to neglect work today. I just had something really important to take care of."

            voice audio.yoshi_vsg22_line9
            yo "I-I see…"
        "Everything’s under control.":
            $ working = True
            $ score_goro += 2
            show cgg10 6b with Dissolve(0.25)
            voice audio.yoshi_vsg22_line8d
            yo "I had everything under control, though…! Everyone got back to work pretty smoothly."

            voice audio.goro_vsg22_line9d
            g "Ah, I’m glad you took care of things."

            show cgg10 7 with Dissolve(0.25)
            voice audio.goro_vsg22_line10cd
            g "I’m really sorry for going out without telling you. "

            voice audio.goro_vsg22_line11
            g "I didn’t mean to neglect work today. I just had something really important to take care of."

            voice audio.yoshi_vsg22_line9
            yo "I-I see…"

    show cgg10 8 with Dissolve(0.25)
    voice audio.goro_vsg22_line12
    g "You did a great job, Yoshinori. You’ve always been an amazing leader, and I’m really proud of you."
    yo "{i}(Hearing Goro acknowledge me like that made me even more confused… I don’t know why he’d say that after what he told Mr. Clermont…){/i}"

    show cgg10 9 with Dissolve(0.25)
    voice audio.goro_vsg22_line13
    g "Ah, we’re going into the woods soon so it’s gonna be a little rocky! "

    voice audio.goro_vsg22_line14
    g "Hold tight, Yoshinori!"

    voice audio.yoshi_vsg22_line10
    yo "A-Alright…!"

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    play sound sfx_harleydepart
    scene cg black
    hide screen location
    hide screen timeline
    hide screen quick_menu
    $quick_menu = False
    with fade
    $ renpy.pause (2.0, hard=True)

    $ location = location_waterfall
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_waterfall_winter_sunset2 with fade
    play music old_familiar_home_slow loop

    show yoshi2_biker at left2
    show yoshi2 sad2 at left2
    show goro_biker at right2
    show goro confused3 at right2
    voice audio.goro_v_alright3a
    g "You alright, Yoshinori?"

    show yoshi2 sad4 at left2
    voice audio.yoshi_v_yeah3
    yo "Y-Yeah… just a little nauseous from the bumpy ride. I didn’t think you were serious about driving on a snowy dirt path."

    show goro talk3 at right2
    voice audio.goro_v_sorry2a1
    g "Sorry I had to take that detour. It’s the only route available to reach this place by motorcycle."

    hide yoshi2_biker
    hide yoshi2 sad4
    show yoshi_biker at left2
    show yoshi confused2 at left2
    voice audio.yoshi_v_wait4
    yo "Wait a minute… This is…"

    hide goro_biker
    hide goro talk3
    show goro2_biker at right2
    show goro2 play2 at right2
    voice audio.goro_v_heh1a
    g "Buddy Falls. I figured I’d show you how beautiful it is during the winter…"
    g "The surface of the pool is frozen, but the falls themselves are still flowing so calmly."

    show yoshi shock2 at left2
    voice audio.yoshi_v_yeah1
    yo "Yeah, it’s so pretty… In all my years at camp, I’ve never seen it like this."
    yo "We only ever camp here on special occasions, after all…  "

    hide goro2_biker
    hide goro2 play2
    show goro_biker at right2
    show goro relief2 at right2
    voice audio.goro_v_agree1a1
    g "Yes. But we’re not camping here tonight. I brought you here for something else…"

    hide yoshi_biker
    hide yoshi shock2
    show yoshi2_biker at left2
    show yoshi2 awkward4 at left2
    voice audio.yoshi_v_what3
    yo "Wh-What is it…?"

    show goro happy2 at right2
    voice audio.goro_v_rush3a1
    g "Come with me, it’s almost time."

    show yoshi2 confused5 at left2
    voice audio.yoshi_v_huh3a
    yo "Wh-Where to?"

    show goro comp3 at right2
    voice audio.goro_v_rush2a1
    g "Take my hand. It’s best if I just show you."

    show yoshi2_biker at center
    show yoshi2 worry1 at center
    with move

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    play sound sfx_snowtrek
    scene cg black with fade
    yo "{i}Taking Goro’s hand, we hiked our way to the top of the falls as the sun continued to set.{/i}"

    scene cg black
    hide screen location
    hide screen timeline
    hide screen quick_menu
    $quick_menu = False
    with fade

    if score_goro <= 0:
        $ time_transition_sunset_to_night_winter2()
        $ renpy.pause (2.0, hard=True)
    elif score_goro > 0 and score_goro <=24:
        $ time_transition_sunset_to_night_winter2()
        $ renpy.pause (2.0, hard=True)
    elif score_goro > 24 and score_goro <= 49:
        $ time_transition_sunset_to_night_winter2()
        $ renpy.pause (2.0, hard=True)
    elif score_goro >49:
        $ time_transition_sunset_to_night_winter3()
        $ renpy.pause (2.0, hard=True)

    $ location = location_waterfall
    $ time = timeline_timenight
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_waterfall_winter_night_top with fade
    play bgsound sfxloop_windy loop

    show yoshi_biker at left2
    show yoshi shock2 at left2
    show goro_biker at right2
    show goro comp1 at right2
    voice audio.yoshi_vsg23_line1
    yo "W-Wow…!!"

    hide goro_biker
    hide goro comp1
    show goro2_biker at right2
    show goro2 play3 at right2
    voice audio.goro_vsg23_line1
    g "Heh… Amazing isn’t it…? "

    show yoshi shock5 at left2
    voice audio.yoshi_vsg23_line2
    yo "Y-Yeah… I’ve never seen it this beautiful before!"

    hide goro2_biker
    hide goro2 play3
    show goro_biker at right2
    show goro relief2 at right2
    voice audio.goro_vsg23_line2
    g "We’re lucky we caught the aurora in time… It’s pretty rare to spot it so clearly like this…"

    hide yoshi_biker
    hide yoshi shock5
    show yoshi2_biker at left2
    show yoshi2 awkward3 at left2
    voice audio.yoshi_vsg23_line3
    yo "Is this what you wanted to show me…?"

    hide goro_biker
    hide goro relief2
    show goro2_biker at right2
    show goro2 comp3 at right2
    voice audio.goro_vsg23_line3
    g "Yes. But more than that, this place is very special to me."

    voice audio.goro_vsg23_line4
    g "This is exactly where we made our promise way back then... at the end of the very first term."

    show yoshi2 upset6 at left2
    voice audio.yoshi_vsg23_line4
    yo "I… I remember…"

    hide goro2_biker
    hide goro2 comp3
    show goro_biker at right2
    show goro comp5 at right2
    voice audio.goro_vsg23_line5
    g "My life has completely changed since then… It marked a new beginning for me…"

    show yoshi2 confused5 at left2
    show goro happy2 at right2
    voice audio.goro_vsg23_line6
    g "You set out to become a scoutmaster, and I couldn’t have been happier to have someone else share my dream for Camp Buddy."

    show yoshi2 sad3 at left2
    voice audio.goro_vsg23_line7
    g "You gave me hope when I thought everything was failing in my life… A second chance at happiness… "

    show yoshi2 upset4 at left2
    yo "..."

    $ renpy.pause (1.0, hard=True)
    show goro worry2 at right2
    voice audio.goro_vsg23_line8
    g "Wh-What’s the matter, Yoshinori…?"

    show yoshi2 upset6 at left2
    voice audio.yoshi_vsg23_line5
    yo "I-I’m just so confused, Goro…"

    show goro worry3 at right2
    voice audio.goro_vsg23_line9
    g "About what…?"

    show yoshi2 upset3 at left2
    voice audio.yoshi_vsg23_line6
    yo "While you were gone today, I found out that you turned down the offer for Camp Buddy…"

    play music buddy_oath_goro_sad loop
    show goro shock1 at right2
    g "...!"

    show yoshi2 sigh3 at left2
    voice audio.yoshi_vsg23_line7
    yo "I just thought that… you would at least talk to me about it first… "

    show goro sad2 at right2
    voice audio.goro_vsg23_line10
    g "I-I’m sorry, Yoshinori… I was planning on telling you all along…"

    $ working = False
    $ shuffle_menu()
    menu():
        g "I-I’m sorry, Yoshinori… I was planning on telling you all along…{fast}"
        "I thought you believed in me…":
            $ working = True
            $ score_goro -= 2
            show yoshi2 worry2 at left2
            voice audio.yoshi_vsg23_line8a
            yo "I thought you believed in me, Goro…"

            voice audio.yoshi_vsg23_line9a
            yo "All this time, you’ve been telling me how much I’ve grown as a scoutmaster and a future leader."

            show yoshi2 sad4 at left2
            voice audio.yoshi_vsg23_line10a
            yo "To think that you turned down the biggest opportunity we’ve ever had without me knowing…"

            voice audio.yoshi_vsg23_line11a
            yo "It really feels like you don’t think I’m cut out for it at all…"
        "I thought you could rely on me…":
            $ working = True
            $ score_goro -= 1
            show yoshi2 worry2 at left2
            voice audio.yoshi_vsg23_line8b
            yo "I thought you could rely on me, Goro…"

            voice audio.yoshi_vsg23_line9b
            yo "All this time, we opened up to each other and did everything together… "

            show yoshi2 sad4 at left2
            voice audio.yoshi_vsg23_line10b
            yo "To think that you turned down the biggest opportunity we’ve ever had without me knowing…"

            voice audio.yoshi_vsg23_line11b
            yo "It really feels like you don’t trust me at all…"
        "I need to understand why…":
            $ working = True
            $ score_goro += 1
            show yoshi2 worry2 at left2
            voice audio.yoshi_vsg23_line8cd
            yo "This is the biggest opportunity we’ve ever had, and I thought it was your dream…"

            voice audio.yoshi_vsg23_line9cd
            yo "I really thought I knew you well enough by now, but I can’t figure this out…"

            show yoshi2 sad4 at left2
            voice audio.yoshi_vsg23_line10c
            yo "I just need to understand why, Goro… "
        "We’re in this together…":
            $ working = True
            $ score_goro += 2
            show yoshi2 worry2 at left2
            voice audio.yoshi_vsg23_line8cd
            yo "This is the biggest opportunity we’ve ever had, and I thought it was your dream…"

            voice audio.yoshi_vsg23_line9cd
            yo "I really thought I knew you well enough by now, but I can’t figure this out…"

            show yoshi2 sad4 at left2
            voice audio.yoshi_vsg23_line10d
            yo "I’ve always believed that we’re in this together, Goro… We’re partners, aren’t we?"

    show goro worry1 at right2
    g "..."

    show goro sigh1 at right2
    voice audio.goro_vsg23_line11
    g "I apologize, Yoshinori…"

    show goro worry2 at right2
    voice audio.goro_vsg23_line12
    g "I understand why you’re upset, and you have every right to be."

    voice audio.goro_vsg23_line13
    g "It was wrong of me to make such a huge decision on my own…"

    if score_goro <= 0:
        jump day9_goro_we
    elif score_goro > 0 and score_goro <=24:
        jump day9_goro_be
    elif score_goro > 24 and score_goro <= 49:
        jump day9_goro_gepe
    elif score_goro >49:
        jump day9_goro_gepe
