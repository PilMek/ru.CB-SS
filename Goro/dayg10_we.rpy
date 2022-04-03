label day10_goro_we:
    $ day = "84"
    $ time = timeline_timeday
    $ location = location_office
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    $ working = True

    scene bg_office_winter_day with fade
    play music brand_new_day_winter loop
    play bgsound sfxloop_birds loop

    show yuri_autumn at left2
    show yuri upset1 at left2
    show yoshi2_autumn at right2
    show yoshi2 upset1 at right2
    voice audio.william_v_sigh1
    w "That’s truly unfortunate… I’m sorry to hear that."

    show yoshi2 sad4 at right2
    voice audio.yoshi_v_sorry1a1
    yo "I hope you understand, Mr. Clermont, but there’s just some unexpected things that occurred yesterday…"
    yo "I will be taking over in Goro’s place for the time being…"

    voice audio.william_v_comp2a
    w "Please don’t worry about the offer anymore, and do what you have to for the project and camp!"

    hide yoshi2_autumn
    hide yoshi2 sad4
    show yoshi_autumn at right2
    show yoshi worry2 at right2
    voice audio.yoshi_v_gratitude2
    yo "I really appreciate your concern, Mr. Clermont. Thank you for understanding."

    voice audio.william_v_agree1a
    w "Of course! Let me know if there’s anything I can do to help."

    play sound sfx_phonebutton
    hide yoshi_autumn
    hide yoshi worry2
    show yoshi2_autumn at right2
    show yoshi2 sigh1 at right2
    voice audio.yoshi_v_relief1
    yo "Whew…"
    yo "I think we settled it in the best way possible, Yuri. "

    show yuri worry4 at left2
    voice audio.yuri_v_yeah1e1
    yu "Yeah… Thanks for handling it, Yoshi…"
    yu "I spoke with Dad over the phone this morning too… He doesn’t plan on coming back yet but he was apologizing for leaving everything behind."

    show yuri sigh3 at left2
    voice audio.yuri_v_sigh2a
    yu "I just reassured him that we can handle everything here at camp for now."

    show yoshi2 upset3 at right2
    voice audio.yoshi_v_sorry2a
    yo "I’m sorry, Yuri… I really tried hard to convince him… "
    yo "But it looks like I didn’t handle it in the best way… "

    show yuri worry5 at left2
    voice audio.yuri_v_comp2a1
    yu "It’s not your fault, Yoshi… There must’ve been something we all didn’t understand about him... "
    yu "Dad already did this once after you left the first term… Keeping everything to himself, and pushing everyone away…"

    show yoshi2 upset5 at right2
    voice audio.yoshi_v_unsure1b
    yo "Maybe I should try to reach out and help…"

    show yuri sad4 at left2
    voice audio.yuri_v_sad2a
    yu "Forcing things on him will just make things worse… So, I’m afraid there’s really not much we do…"

    show yoshi2 worry2 at right2
    voice audio.yoshi_v_unsure2a
    yo "Will he be okay…?"

    show yuri worry4 at left2
    voice audio.yuri_v_alright2a2
    yu "I’m still in contact with him at the very least, I’ll make sure he’s okay and try to change his mind."
    yu "But try not to worry about it and just focus on keeping the project going until the end."

    show yoshi2 sigh1 at right2
    voice audio.yoshi_v_sigh3a
    yo "You’re right… That’s the best thing we can do until he comes back."

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black with fade
    yo "{i}Yuri and I left the office and explained the situation to everyone... We were all upset about Goro's sudden departure, but none of us wanted to give up on the project.{/i}"
    yo "{i}Everyone worked hard for the next few months, and I did my best to lead in Goro's place.{/i}"
    yo "{i}Before long, the snow started to thaw, and the project was complete.{/i}"

    scene cg black
    hide screen location
    hide screen timeline
    hide screen quick_menu
    $quick_menu = False
    with fade
    $ time_transition_winter_to_spring()
    $ renpy.pause (2.0, hard=True)

    $ day = "221"
    $ season = season_spring
    $ location = location_site
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_site9_spring_day with fade
    play music brand_new_day loop
    play bgsound sfxloop_birds loop

    show emilia_autumn at p8_1
    show emilia norm3 at p8_1
    show yuri_autumn at p8_2
    show yuri norm3 at p8_2
    show aiden_autumn at p8_3
    show aiden norm3 at p8_3
    show yoshi_autumn at p8_4
    show yoshi talk1 at p8_4
    show william_autumn at p8_5
    show william norm1 at p8_5
    show darius_autumn at p8_7
    show darius norm3 at p8_7
    show lloyd_autumn at p8_6
    show lloyd norm3 at p8_6
    show jin_autumn at p8_8
    show jin_glasses at p8_8
    show jin norm3 at p8_8
    voice audio.yoshi_v_conj1a
    yo "Finally, after months of hard work, we’ve all reached the project completion we’ve been aiming for."
    yo "You’ve all worked extremely hard, and I want to express how thankful I am for all of your dedication and commitment!"

    show yoshi talk2 at p8_4
    voice audio.yoshi_v_thanks1
    yo "I’d also like to give a special thanks to Mr. Clermont, as without him we’d never have had this opportunity to grow."
    yo "Thank you again, sir, for everything you’ve done, and for being here with us today."

    show william comp4 at p8_5
    voice audio.william_v_comp1b
    w "It was my pleasure, Mr. Nagira."

    show yoshi worry2 at p8_4
    voice audio.yoshi_v_sigh3a
    yo "I know that for many of us, today is bittersweet without our leader, but I’m sure that no matter where he is, he’s proud of us."
    yo "We’ve all done our best to continue his dream, and one day, if he comes back, Camp Buddy will be here for him again."

    show yoshi talk1 at p8_4
    voice audio.yoshi_v_so1a
    yo "Now, let’s usher in a bright future, together!"

    play sound sfx_ribboncut
    show yoshi norm3 at p8_4
    yo "*cuts ribbon*"

    play sound sfx_applause
    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black with fade
    yo "{i}Even though we should’ve been celebrating with the ribbon-cutting, I couldn’t help but feel hollow inside…{/i}"
    yo "{i}This was everything Goro dreamed of… or so I thought.{/i}"
    yo "{i}I wish he could’ve been here today…{/i}"
    $ renpy.pause (2.0, hard=True)
    yo "{i}After the ceremony, everyone packed up, and it was time to say goodbye.{/i}"

    scene cg black
    hide screen location
    hide screen timeline
    hide screen quick_menu
    $quick_menu = False
    with fade
    $ renpy.pause (2.0, hard=True)

    $ location = location_entrance
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_entrance_past_day with fade
    play music ready_for_tomorrow loop
    play bgsound sfxloop_birds loop

    show darius_autumn at p7_2
    show darius norm3 at p7_2
    show lloyd_autumn at p7_1
    show lloyd worry1 at p7_1
    show jin_autumn at p7_3
    show jin_glasses at p7_3
    show jin worry1 at p7_3
    show emilia_autumn at p7_4
    show emilia norm3 at p7_4
    show yuri_autumn at p7_5
    show yuri sad1 at p7_5
    show aiden2_autumn at p7_7
    show aiden2 upset1 at p7_7
    show yoshi_autumn at p7_6
    show yoshi confused2 at p7_6
    voice audio.yoshi_v_alright1
    yo "I think that’s the last of it, right guys?"

    show darius talk1 at p7_2
    voice audio.darius_v_agree1a
    d "Yes."

    show lloyd sigh1 at p7_1
    voice audio.lloyd_v_sigh2a
    l "*sigh* It feels so wrong to leave now, especially without Sir Goro around…"

    show jin worry2 at p7_3
    voice audio.jin_v_yeah2a
    j "Y-Yeah… I kept hoping that he’d show up at the ceremony at least."

    show emilia confused3 at p7_4
    voice audio.emilia_v_yuri2
    e "You said you heard from him right, Yuri?"

    show yuri sigh1 at p7_5
    voice audio.yuri_v_sigh2a
    yu "I did text him letting him know about today… He said to congratulate everyone, but that he wouldn’t make it."

    show aiden2 sigh1 at p7_7
    voice audio.aiden_v_sigh2a
    a "*sigh* I guess he’s still not ready to come back, huh?"

    hide yoshi_autumn
    hide yoshi confused2
    show yoshi2_autumn at p7_6
    show yoshi2 upset1 at p7_6
    yo "..."

    show yuri worry3 at p7_5
    voice audio.yuri_v_comp1b1
    yu "D-Don’t worry, everyone! I’m sure he’ll be back someday!"
    yu "He just really needs some time to himself for now… Once he gets through with it, he’ll want to see all of us again."

    hide aiden2_autumn
    hide aiden2 sigh1
    show aiden_autumn at p7_7
    show aiden comp2 at p7_7
    voice audio.aiden_v_agree2b1
    a "Y-Yeah, you’re probably right, Yuri! He’ll probably have some crazy stories to tell, too!"

    show lloyd worry3 at p7_1
    voice audio.lloyd_v_aww1a1
    l "Awww, now I can’t wait to hear them! I hope it’s soon…"

    show darius explain2 at p7_2
    voice audio.darius_v_think1a1
    d "For now, we just have to be patient."

    play sound sfx_busdoor
    show jin talk3 at p7_3
    voice audio.jin_v_ah3a
    j "A-Ah, that must be our shuttle… I guess it’s time to leave…"

    show aiden comp5 at p7_7
    voice audio.aiden_v_bye1b
    a "See ya, guys! It’s been a pleasure working with everyone!"
    a "Camp Buddy will always be here for ya’ll!"

    show yuri pain6 at p7_5
    voice audio.yuri_v_ugh3a
    yu "Huhuhuhu… Be sure to keep in touch!"

    show darius happy2 at p7_2
    voice audio.darius_v_bye1b
    d "Goodbye now."

    hide darius_autumn
    hide darius happy2
    with dissolve

    show jin comp5 at p7_3
    voice audio.jin_v_bye1b1
    j "We’re just one message away…! "

    hide jin_autumn
    hide jin_glasses
    hide jin comp5
    with dissolve

    show lloyd comp2 at p7_1
    voice audio.lloyd_v_bye2a
    l "I’ll miss all of you guys!"

    hide lloyd_autumn
    hide lloyd comp2
    with dissolve

    play sound sfx_busengine
    show emilia_autumn at p4_1
    show emilia sad1 at p4_1
    show yuri_autumn at p4_2
    show yuri sad4 at p4_2
    show yoshi2_autumn at p4_3
    show yoshi2 upset1 at p4_3
    show aiden_autumn at p4_4
    show aiden sad1 at p4_4
    with move

    $ renpy.music.stop(channel='sound', fadeout = 2.0)
    voice audio.yuri_v_sigh2a
    yu "*sniff* This place just feels so empty now…"

    show emilia worry2 at p4_1
    voice audio.emilia_v_rush1b1
    e "Come on, let’s get you inside. We can watch a nice movie and get it off our minds."

    hide yuri_autumn
    hide yuri sad4
    hide emilia_autumn
    hide emilia worry2
    with dissolve

    show yoshi2_autumn at left2
    show yoshi2 sad2 at left2
    show aiden_autumn at right2
    show aiden worry1 at right2
    with move

    yo "..."

    hide aiden_autumn
    hide aiden worry1
    show aiden2_autumn at right2
    show aiden2 worry3 at right2
    voice audio.aiden_v_alright4a
    a "…You alright, Yoshi?"

    show yoshi2 sad4 at left2
    voice audio.yoshi_v_yeah3
    yo "Y-Yeah, I’ll be fine, Aiden."
    yo "You can go ahead, I’ll catch up."

    show aiden2 sad4 at right2
    voice audio.aiden_v_okay4a
    a "…Okay. Don’t stay out here too long."

    show yoshi2 sad1 at left2
    yo "..."

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black with fade
    yo "{i}As I stood there at the arches of Camp Buddy alone, I was left to wonder about the choices I’ve made…{/i}"
    yo "{i}Even though Goro and I thought we had gained so much throughout the seasons… In the end I felt like I lost everything…{/i}"
    yo "{i}My only hope now is that he’ll come back one day and see how I’ve kept the camp alive for him…{/i}"
    yo "{i}Until then, all the memories we shared together will keep replaying in my head, holding on to what’s left of the love I had for him…{/i}"

    scene cg black with fade
    hide screen location
    hide screen timeline
    hide screen quick_menu
    $ quick_menu = False
    $ renpy.pause (2.0, hard=True)

    scene bg_gameover with dissolve
    $ renpy.pause (5.0, hard=True)

    $persistent.routes_completed.append("goro")
    $renpy.save_persistent()

    #game over
