label day4_goro:
    $ day = "79"
    $ time = timeline_timeday
    $ location = location_hotelroom
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    $ working = True
    $day3_goro = False

    scene bg_hotel_room1_day with fade
    play music old_familiar_home loop

    show yoshi2_sleep at center
    show yoshi2 sleepy5 at center
    with dissolve

    voice audio.yoshi_v_yawn1
    yo "*yawn*"

    show yoshi2_sleep at left2
    show yoshi2 sleepy5 at left2
    with move

    show goro_sleep at right2
    show goro talk3 at right2
    with dissolve

    voice audio.goro_v_ah1a
    g "Ah, you’re awake, Yoshinori."

    show yoshi2 sleepy6 at left2
    voice audio.yoshi_v_goodam1
    yo "Mnn… Good morning, Sir Goro."

    show goro relief2 at right2
    voice audio.goro_v_goodam1a2
    g "Good morning. I’m just having my coffee."

    show yoshi2 sleepy2 at left2
    voice audio.yoshi_v_sorry2b
    yo "I’m sorry I couldn’t stay up while we were drinking last night, sir…"

    hide goro_sleep
    hide goro relief2
    show goro2_sleep at right2
    show goro2 play2 at right2
    voice audio.goro_v_alright2a1
    g "Haha, it’s alright, getting you tipsy worked like a charm. You slept like a baby."

    show yoshi2 awkward4 at left2
    voice audio.yoshi_v_ah3
    yo "A-Ahh… That’s so embarrassing…"

    hide goro2_sleep
    hide goro2 play2
    show goro_sleep at right2
    show goro comp2 at right2
    voice audio.goro_v_heh1a
    g "We had such a long day yesterday though, so I’m not surprised you were that tired."
    g "I’m just glad we enjoyed our time together."

    hide yoshi2_sleep
    hide yoshi2 awkward4
    show yoshi_sleep at left2
    show yoshi comp2 at left2
    voice audio.yoshi_v_yessir1
    yo "Me too, sir."

    show goro explain3 at right2
    voice audio.goro_v_actually1a
    g "You know, it’s been quite some time since I was able to do something like this with someone special."

    show yoshi confused2 at left2
    voice audio.yoshi_v_really1
    yo "Really? I thought you and Yuri went on trips like this together."

    show goro laugh1 at right2
    voice audio.goro_v_laugh2b1
    g "Hahaha, I don’t mean it that way, Yoshinori! Yuri’s my daughter."
    g "What I meant is going out with a partner."

    hide yoshi_sleep
    hide yoshi confused2
    show yoshi2_sleep at left2
    show yoshi2_blush1 at left2
    show yoshi2 awkward2 at left2
    yo "..."

    show goro happy2 at right2
    voice audio.goro_v_but1a
    g "I used to take my dates on road trips, driving them to all sorts of new places. But that was long ago."

    show yoshi2 confused5 at left2
    voice audio.yoshi_v_oh2
    hide yoshi2_blush1
    yo "O-Oh, you mean way back when you were in the uh… biker gang?"

    hide goro_sleep
    hide goro happy2
    show goro2_sleep at right2
    show goro2 play3 at right2
    voice audio.goro_v_heh1a
    g "Heh, I bet it’s still hard for you to believe how someone like me could be in a group like that."

    $ working = False
    $ shuffle_menu()
    menu():
        g "Heh, I bet it’s still hard for you to believe how someone like me could be in a group like that.{fast}"
        "It seemed out of character.":
            $ working = True
            $ score_goro -= 1
            $ score_top += 1
            hide yoshi2_sleep
            hide yoshi2 confused5
            show yoshi_sleep at left2
            show yoshi think2 at left2
            voice audio.yoshi_v_actually1a
            yo "It really seems out of character, especially with the way you’ve always presented yourself to us, sir."
            yo "But then… That just makes me even more curious about what kind of person you were before I met you at Camp Buddy."
        "You were my role model.":
            $ working = True
            $ score_goro -= 1
            $ score_bot += 1
            hide yoshi2_sleep
            hide yoshi2 confused5
            show yoshi_sleep at left2
            show yoshi talk3 at left2
            voice audio.yoshi_v_sir1
            yo "You were my role model, sir. So it’s something I would’ve never expected."
            yo "But then… That just makes me even more curious about what kind of person you were before I met you at Camp Buddy."
        "It's not something to be ashamed of.":
            $ working = True
            $ score_goro += 2
            $ score_top += 1
            hide yoshi2_sleep
            hide yoshi2 confused5
            show yoshi_sleep at left2
            show yoshi comp3 at left2
            voice audio.yoshi_v_unsure1a
            yo "I really don’t think it’s something to be ashamed of… "
            yo "Instead, I can’t help but wonder what kind of person you were before I met you at Camp Buddy, sir."
        "It just makes me wonder.":
            $ working = True
            $ score_goro += 2
            $ score_bot += 1
            hide yoshi2_sleep
            hide yoshi2 confused5
            show yoshi_sleep at left2
            show yoshi bold2 at left2
            voice audio.yoshi_v_think2
            yo "It is hard to imagine, but that just makes me wonder what it was like even more!"
            yo "I can’t help but be curious about what kind of person you were before I met you at Camp Buddy, sir."

    show goro2 think2 at right2
    voice audio.goro_v_think1b1
    g "Hmmm… I guess I don’t mind telling you, if you really want to know…"

    show yoshi happy2 at left2
    voice audio.yoshi_v_yessir1
    yo "I-I do, sir!"

    show goro2 think6 at right2
    voice audio.goro_v_alright1c1
    g "Well… alright. But listen up, ’cause I’m only telling you once."

    show cg_fade at truecenter
    show fxg4 at fx_pos
    with dissolve

    voice audio.goro_vsg11_line1
    g "In my younger days, I was really into motorcycles and riding was my biggest hobby."

    voice audio.goro_vsg11_line2
    g "I’d always been outgoing and free-spirited at heart, so it only made sense to me at the time to gather people who had the same interests as me. So, I organized a biker’s club."

    voice audio.goro_vsg11_line3
    g "It’s a common misconception that groups like us were violent, good-for-nothing delinquents."

    voice audio.goro_vsg11_line4
    g "When in reality, at least in my case, it was all about the brotherhood."

    voice audio.goro_vsg11_line5
    g "While I can’t deny that we had our rivals and got into trouble with them often, we never went out of our way to cause harm or commit crimes."

    voice audio.goro_vsg11_line6
    g "If there was any silver lining, it was during that time that I learned most of the concepts and principles I carry today."

    voice audio.goro_vsg11_line7
    g "As a leader, I learned to handle people from all walks of life, resolve complex conflicts, and live in a culture where mutual respect was paramount."

    voice audio.yoshi_vsg11_line1
    yo "I can imagine it a lot better now…"

    voice audio.goro_vsg11_line8
    g "But it wasn’t always that serious either. Being teenagers, we had countless parties and all sorts of crazy ideas to entertain ourselves."

    voice audio.goro_vsg11_line9
    g "It was the wildest time of my life, where I lived in the moment and nothing else mattered as long as I was having fun."

    hide cg_fade
    hide fxg4
    with dissolve

    show goro2 norm3 at right2
    show yoshi shock2 at left2
    voice audio.yoshi_v_shock1b
    yo "I can’t believe I never knew anything even after all these years. These are some really crazy revelations, sir."

    show goro2 sigh2 at right2
    voice audio.goro_v_agree6a1
    g "I know, right? Honestly, I can’t think of any way that we contributed to society back then."
    g "Which is exactly why I’m not proud of it…"

    show yoshi happy1 at left2
    voice audio.yoshi_v_no1
    yo "No, sir… What I meant was, it’s more unbelievable to me how different you’ve become since then."

    show goro2 talk3 at right2
    voice audio.goro_v_think1a1
    g "The explanation for that is rather simple. "
    g "It was in my riding days that I met Vera and we had our child."

    show goro2 explain2 at right2
    voice audio.goro_v_so1a
    g "Having a family, I had to let go of my reckless ways in order to be a good husband, and especially a good father.  The rest is history."

    $ working = False
    $ shuffle_menu()
    menu():
        g "Having a family, I had to let go of my reckless ways in order to be a good husband, and especially a good father.  The rest is history.{fast}"
        "Do you miss those times?":
            $ working = True
            $ score_goro -= 1
            show yoshi confused2 at left2
            voice audio.yoshi_v_think3
            yo "Do you miss the times when you were in your biker group?"

            show goro2 talk1 at right2
            voice audio.goro_v_agree1a2
            g "I do, but I can’t imagine how badly my life would’ve turned out if I hadn’t grown out of it."
        "It was the right thing to do.":
            $ working = True
            show yoshi explain2 at left2
            voice audio.yoshi_v_sir1
            yo "It was the right thing to do, sir."

            show goro2 talk1 at right2
            voice audio.goro_v_agree1a2
            g "Yes, I can’t imagine how my life would be now if I had chosen differently."
        "It was worth it.":
            $ working = True
            $ score_goro += 1
            show yoshi comp2 at left2
            voice audio.yoshi_v_sir1
            yo "I think everything you did was worth it, sir."
            yo "If it weren’t for you choosing that life, Camp Buddy might never have been formed, and we wouldn’t have even met!"

            show goro2 comp2 at right2
            voice audio.goro_v_agree1a2
            g "Yes, I can’t imagine how my life would be now if I stayed the way I was."
        "You've come a long way.":
            $ working = True
            $ score_goro += 2
            show yoshi comp2 at left2
            voice audio.yoshi_v_sir1
            yo "You’ve come such a long way, sir."
            yo "If it weren’t for you choosing that life, Camp Buddy might never have been formed, and we wouldn’t have even met!"

            show goro2 comp2 at right2
            voice audio.goro_v_agree1a2
            g "Yes, I can’t imagine how my life would be now if I stayed the way I was."

    g "I just hope that you finding out about all of this won’t change the way you see me."

    show yoshi talk3 at left2
    voice audio.yoshi_v_disagree3
    yo "No way, sir! If anything, I think it’s really cool! In fact, I wish I could’ve seen it!"

    show goro2 play2 at right2
    voice audio.goro_v_heh1a
    g "Heh… If you did, you’d probably be twice as intimidated by me."

    show yoshi comp3 at left2
    voice audio.yoshi_v_actually1a
    yo "I-I’m not scared of you, sir...! I just really respect you!"

    show goro2 annoy2 at right2
    voice audio.goro_v_confused1a1
    g "You’re really insistent on keeping up that formal shtick around me, huh?"
    g "Then get your lazy ass up from that bed, scout. We’re on vacation and we’ve already spent half our day cooped up in this room."

    show yoshi awkward4 at left2
    voice audio.yoshi_v_shock4
    yo "G-Gah…! I’m sorry again for oversleeping!"

    hide goro2_sleep
    hide goro2 annoy2
    show goro_sleep at right2
    show goro angry3 at right2
    voice audio.goro_v_response1b1
    g "Go get dressed in five minutes and let’s have fun out there. Understood?"

    show yoshi awkward3 at left2
    voice audio.yoshi_v_yessir2
    yo "Yes, sir!"

    show goro laugh5 at right2
    voice audio.goro_v_laugh2b1
    g "Hahaha!"

    scene cg black with fade
    $renpy.choice_for_skipping()
    show screen minimap()
    $mm_talking = True
    $day4_goro_choice = False
    voice audio.goro_v_so1a
    g "So, Yoshinori. Where to today? "

    $ say_box = False
    $quick_menu = False
    $mm_talking = False
    $ renpy.pause (hard=True)


label day4_goro_lobby:
    $sq_yuri += 1
    $ say_box = True
    $quick_menu = True
    $mm_talking = True
    $ g4_lobby = True
    if g3_lobby == False:
        voice audio.yoshi_v_think4
        yo "How about we check out the lobby?"

        voice audio.goro_v_alright1a1
        g "There’s not much to see there, but I guess it’ll help kill some time.  "
    else:
        voice audio.yoshi_v_think4
        yo "How about we check out the lobby again, sir?"

        voice audio.goro_v_yoshi11a
        g "You know there’s nothing to see there, Yoshinori."

        voice audio.yoshi_v_well1
        yo "Well, maybe this time it’ll be different!"

        voice audio.goro_v_alright1a1
        g "*sigh* Alright."

    hide screen minimap
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

    if day4_goro_choice == False:
        $ location = location_hotellobby
        show screen location
        show screen timeline
        show screen quick_menu
        $quick_menu = True
        scene bg_hotel_lobby_day with fade
        play music buddy_oath_hotel loop
    else:
        $ location = location_hotellobby
        show screen location
        show screen timeline
        show screen quick_menu
        $quick_menu = True
        scene bg_hotel_lobby_sunset with fade
        play music buddy_oath_hotel loop

    show yuri_autumn at p5_1
    show yuri norm1 at p5_1
    show goro_autumn at p5_4
    show goro talk3 at p5_4
    show yoshi_autumn at p5_5
    show yoshi norm1 at p5_5
    voice audio.goro_v_ah1b
    g "Ah, it seems Yuri’s here as well."

    show yoshi confused2 at p5_5
    voice audio.yoshi_v_huh1
    yo "It looks like she’s on her laptop. Is she working?"

    show goro explain2 at p5_4
    voice audio.goro_v_think1a1
    g "I doubt it. But let’s see."

    show yuri_autumn at left
    show yuri norm1 at left
    show goro_autumn at center
    show goro confused2 at center
    show yoshi_autumn at right
    show yoshi norm1 at right
    with move

    voice audio.goro_v_yuridear3a
    g "Yuri-dear, what are you doing here all by yourself?"

    show yuri shock4 at left
    voice audio.yuri_v_shock1a1
    yu "Oh my gosh! You guys startled me!"

    hide goro_autumn
    hide goro confused2
    show goro2_autumn at center
    show goro2 annoy2 at center
    voice audio.goro_v_really4a
    g "Let me guess, you’re watching your ‘shows’ on that laptop, aren’t you? Don’t you think that’s something you should be doing in private…?"

    show yuri angry2 at left
    voice audio.yuri_v_rush1b1
    yu "Come on, Dad! I swear I’m not causing trouble! "
    yu "I already hung out in the café all day yesterday, so I wanted a change of scenery while I’m enjoying my BL~"

    hide yoshi_autumn
    hide yoshi norm1
    show yoshi2_autumn at right
    show yoshi2 comp6 at right
    voice audio.yoshi_v_unsure3a
    yo "I guess this is your idea of a vacation."

    show yuri relief2 at left
    voice audio.yuri_v_agree3a
    yu "Absolutely~! The last few months on the project haven’t really given me any time to consume my BL in peace!"

    show yoshi2 sigh4 at right
    voice audio.yoshi_v_response1a
    yo "That makes sense."

    show yuri_autumn at p4_1
    show yuri shock1 at p4_1
    show goro2_autumn at p4_2
    show goro2 norm1 at p4_2
    show yoshi2_autumn at p4_3
    show yoshi2 shock1 at p4_3
    with move

    show reimond_bellboy at p4_4
    show reimond confused2 at p4_4
    voice audio.reimond_v_greet1a1
    r "Excuse me, are you Mr. Nomoru?"

    hide goro2_autumn
    hide goro2 norm1
    show goro_autumn at p4_2
    show goro talk3 at p4_2
    voice audio.goro_v_agree2a1
    g "Ah, yes. Do you need anything?"

    show reimond_bellboy at p4_4
    show reimond talk1 at p4_4
    voice audio.reimond_v_apology3a1
    r "Please forgive me for interrupting your vacation time, but we need to confirm your staff list for the reservation."
    r "We thought we’d bring it your attention before we contacted Mr. Clermont."

    show goro talk4 at p4_2
    voice audio.goro_v_alright1a1
    g "Sure, I have everyone’s IDs on file. Would that suffice?"

    show reimond_bellboy at p4_4
    show reimond happy1 at p4_4
    voice audio.reimond_v_agree5a1
    r "Yes, sir! Kindly follow me this way to verify!"

    show goro talk1 at p4_2
    voice audio.goro_v_wait3a1
    g "I’ll be right back, you two."

    hide goro_autumn
    hide goro talk1
    hide reimond_bellboy
    hide reimond happy1
    with dissolve

    show yuri_autumn at left2
    show yuri sigh1 at left2
    show yoshi2_autumn at right2
    show yoshi2 norm3 at right2
    with move

    voice audio.yuri_v_sigh2a
    yu "*sigh* Even here Dad’s being chased by work. I really hope he’s had time to enjoy himself this vacation."

    hide yoshi2_autumn
    hide yoshi2 norm3
    show yoshi_autumn at right2
    show yoshi happy1 at right2
    voice audio.yoshi_v_comp5
    yo "Don’t worry, Yuri! I’ve been tagging along with him since yesterday, and I’m sure he’s having a lot of fun!"

    show yuri comp2 at left2
    voice audio.yuri_v_relief3a2
    yu "Whew! That’s a relief!"
    yu "I was worried he’d be stressing out about that commitment to Mr. Clermont to make up with Emilia, or other random stuff like that just now. "

    show yuri sigh3 at left2
    voice audio.yuri_v_but2a
    yu "He tends to take on all those burdens on his own just because he’s our leader."

    hide yoshi_autumn
    hide yoshi happy1
    show yoshi2_autumn at right2
    show yoshi2 think2 at right2
    voice audio.yoshi_v_yeah3
    yo "Yeah… I’m sure it’s difficult to be in Sir Goro’s place."

    show yuri talk2 at left2
    voice audio.yuri_v_conj6a
    yu "He’s always been like that, though. Not just as the camp president, but also as my dad."

    hide yoshi2_autumn
    hide yoshi2 think2
    show yoshi_autumn at right2
    show yoshi confused2 at right2
    voice audio.yoshi_v_unsure3b
    yo "I guess I have always wondered… What’s it like having Sir Goro as your father?"
    yo "I know from what I’ve seen, he’s protective of you, but at the same time lets you do the things you enjoy."

    show yuri happy1 at left2
    voice audio.yuri_v_yeah1a1
    yu "Yeah, pretty much! He always encouraged me to pursue my own interests no matter what they were!"
    yu "Honestly, that’s why I’ve always been closer to him than my mom."

    hide yoshi_autumn
    hide yoshi confused2
    show yoshi2_autumn at right2
    show yoshi2 worry2 at right2
    voice audio.yoshi_v_ah2
    yo "Ah…"

    show yuri think2 at left2
    voice audio.yuri_v_aww1a
    yu "Growing up, I never really got along with her…"
    yu "It always upset me to see Dad trying so hard to work things out with her, even though it was pointless. Mom was never on the same page as him."

    show yuri angry5 at left2
    voice audio.yuri_v_hmph1a
    yu "She was always away, leaving Dad and I, like we weren’t a family."

    show yoshi2 think3 at right2
    voice audio.yoshi_v_well3
    yo "I-I did get that idea from the few times I met her back when we were scouts. "
    yo "You were always bothered when we talked about your family..."

    show yuri sad4 at left2
    voice audio.yuri_v_actually4a
    yu "It was way worse before Camp Buddy too..."
    yu "I didn’t know any better back then, so I often lashed out whenever I saw them argue."

    show yuri irked2 at left2
    voice audio.yuri_v_annoyed2b
    yu "Knowing that Dad had to work twice as hard to raise me really made me resent my mom for constantly fighting with Dad."
    yu "It made me feel even more distant from her instead of wanting to build a relationship."

    show yoshi2 worry3 at right2
    voice audio.yoshi_v_isee2
    yo "I see…"

    show yuri comp2 at left2
    voice audio.yuri_v_but1a
    yu "But on the other hand, Dad always made time for me no matter how busy he was with work!"
    yu "I knew how much Dad wanted to give me a perfect family, so I’ve always had a soft spot for him."

    show yuri sigh3 at left2
    voice audio.yuri_v_sigh2a
    yu "That’s why even when he became so stern and shut-off the last few years, all I could do was try to be by his side."
    yu "Because I’ve seen firsthand how much Dad has gone through."

    show yoshi2 comp2 at right2
    voice audio.yoshi_v_yuri4
    yo "Yuri…"

    show yuri_autumn at left
    show yuri norm1 at left
    show yoshi2_autumn at center
    show yoshi2 shock1 at center
    with move

    show goro_autumn at right
    show goro talk3 at right
    with dissolve

    voice audio.goro_v_hey1a
    g "Hey, I’m back. It’s all fixed now. Did I miss anything?"

    show yuri happy2 at left
    voice audio.yuri_v_no1a1
    yu "Nope~! We were just chit-chatting!"
    yu "Now, shoo, I wanna focus on my BL and you boys should go out there and do something interesting!"

    hide goro_autumn
    hide goro talk3
    show goro2_autumn at right
    show goro2 play2 at right
    voice audio.goro_v_heh1a
    g "Heh. That’s what was I telling Yoshinori here."

    hide yoshi2_autumn
    hide yoshi2 shock1
    show yoshi_autumn at center
    show yoshi happy1 at center
    voice audio.yoshi_v_bye1b
    yo "Alright, Yuri! See you later!"

    show yuri laugh1 at left
    voice audio.yuri_v_tease2a
    yu "Have fun~"

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black with fade
    yo "{i}Hearing about Sir Goro’s past with his family gave me a new sense of respect for he and Yuri’s relationship…{/i}"

    if day4_goro_choice == False:
        $ day4_goro_choice = True
        $ renpy.pause (1.0, hard=True)
        yo "{i}After we left the lobby, we decided to check out somewhere else in the hotel.{/i}"

        scene cg black
        hide screen location
        hide screen timeline
        hide screen quick_menu
        $quick_menu = False
        with fade
        $ time_transition_day_to_sunset_winter()
        $ time = timeline_timesunset
        $ renpy.pause (2.0, hard=True)
        $ say_box = False
        $mm_talking = False
        $renpy.choice_for_skipping()
        show screen minimap()
        $ renpy.pause (hard=True)

    else:
        $ renpy.pause (1.0, hard=True)
        yo "{i}After we left the lobby, we decided to head back to our room for the night.{/i}"

        scene cg black
        hide screen location
        hide screen timeline
        hide screen quick_menu
        $quick_menu = False
        with fade
        $ time_transition_sunset_to_night_winter()
        $ renpy.pause (2.0, hard=True)
        jump day4_goro_after


label day4_goro_club:
    $sq_aiden += 1
    $g4_club = True
    $quick_menu = True
    $mm_talking = True
    $say_box = True
    if g3_club == False:
        voice audio.yoshi_v_oh1
        yo "Oh, how about we head over to the bar, sir?"

        voice audio.goro_v_heh1a
        g "Heh, I was hoping you’d pick that. Let’s go."
    else:
        voice audio.yoshi_v_sir1
        yo "Want to go check out the club again, sir? "

        voice audio.goro_v_heh1a
        g "I wouldn’t say no to trying out some more drinks."

    hide screen minimap
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
    play music on_the_edge_club loop

    if day4_goro_choice == False:
        $ location = location_hotelclub
        show screen location
        show screen timeline
        show screen quick_menu
        $quick_menu = True
        scene bg_hotel_bar_day with fade
    else:
        $ location = location_hotelclub
        show screen location
        show screen timeline
        show screen quick_menu
        $quick_menu = True
        scene bg_hotel_bar_sunset with fade

    if g3_club == False:
        show yoshi_autumn at left2
        show yoshi shock2 at left2
        show goro_autumn at right2
        show goro shock1 at right2
        voice audio.yoshi_v_shock1b
        play music close_distance loop
        yo "Whoa… This place looks cozy!"

        show goro talk3 at right2
        voice audio.goro_v_think1a1
        g "I bet it’s completely different at night."

        show yoshi confused2 at left2
        voice audio.yoshi_v_think1a
        yo "It seems a lot more like a club than a casual pub…"

        show yoshi_autumn at p5_4
        show yoshi norm1 at p5_4
        show goro_autumn at p5_5
        show goro norm1 at p5_5
        with move

        show justin_bar at p5_1
        show justin_glasses at p5_1
        show justin talk2 at p5_1
        with dissolve

        voice audio.justin_v_greet2a1
        bt "Hey, dude. Wake up. We have guests coming."

        show goro talk4 at p5_5
        voice audio.goro_v_oh1a
        g "Ah, the bartender’s right over there. Let me just call him."

        show justin_bar at left
        show justin_glasses at left
        show justin norm1 at left
        show yoshi_autumn at center
        show yoshi norm1 at center
        show goro_autumn at right
        show goro talk1 at right
        with move

        voice audio.goro_v_goodam2a1
        g "Hello there, can we have the menu pl—"
    else:
        show yoshi_autumn at left2
        show yoshi happy1 at left2
        show goro_autumn at right2
        show goro norm1 at right2
        voice audio.yoshi_v_alright2
        yo "Alright, sir. What’ll we have this time?"

        show goro play3 at right2
        voice audio.goro_v_heh1a
        g "My turn to pick."

        show yoshi_autumn at p5_4
        show yoshi norm1 at p5_4
        show goro_autumn at p5_5
        show goro norm1 at p5_5
        with move

        show justin_bar at p5_1
        show justin_glasses at p5_1
        show justin talk2 at p5_1
        with dissolve

        voice audio.justin_v_greet2a1
        bt "Hey, dude. Wake up. We have guests coming."

        show goro talk4 at p5_5
        voice audio.goro_v_oh1a
        g "Ah, the bartender’s right over there. Let me just call him."

        show justin_bar at left
        show justin_glasses at left
        show justin norm1 at left
        show yoshi_autumn at center
        show yoshi norm1 at center
        show goro_autumn at right
        show goro talk1 at right
        with move

        voice audio.goro_v_goodam2a1
        g "Hello there, we’re back. We’d like to make an or—"

    show justin_bar at p4_2
    show justin_glasses at p4_2
    show justin comp1 at p4_2
    show yoshi_autumn at p4_3
    show yoshi shock1 at p4_3
    show goro_autumn at p4_4
    show goro shock3 at p4_4
    with move

    show aiden2_undie at p4_1
    show aiden2 hungry2 at p4_1
    with dissolve

    voice audio.goro_v_aiden10b
    g "AIDEN?! " with vpunch

    show justin comp3 at p4_2
    voice audio.justin_v_laugh5
    bt "A-Ahehe… Sorry about this! Our friend here had too much to drink last night!"

    if g3_club == False:
        hide goro_autumn
        hide goro shock3
        show goro2_autumn at p4_4
        show goro2 shy4 at p4_4
        voice audio.goro_v_shy1a
        g "He’s with us. We’ll take it from here."
    else:
        hide goro_autumn
        hide goro shock3
        show goro2_autumn at p4_4
        show goro2 shy4 at p4_4
        voice audio.goro_v_shy1a
        g "We’ll take it from here."

    show justin laugh1 at p4_2
    voice audio.justin_v_thankyou1a1
    bt "Thanks! Just call me for your orders!"

    hide justin_bar
    hide justin_glasses
    hide justin laugh1
    with dissolve

    show yoshi_autumn at left
    show yoshi worry2 at left
    show aiden2_undie at center
    show aiden2 hungry2 at center
    show goro2_autumn at right
    show goro2 annoy1 at right
    with move

    hide yoshi_autumn
    hide yoshi worry2
    show yoshi2_autumn at left
    show yoshi2 worry2 at left
    voice audio.yoshi_v_unsure2a
    yo "I-Is Aiden alright, sir?"

    show goro2 annoy2 at right
    voice audio.goro_v_yeah1c1
    g "Yeah, he’s just passed out."

    show yoshi2 sigh1 at left
    voice audio.yoshi_v_sigh3a
    yo "*sigh* Where are his clothes?"

    show goro2 angry2 at right
    voice audio.goro_v_aiden7a
    g "Boy, wake up."

    show aiden2 sleepy4 at center
    voice audio.aiden_v_confused2b3
    a "H-Huh…? Wha—? Where am I…?"

    show yoshi2 awkward3 at left
    voice audio.yoshi_v_aiden4
    yo "You’re at the club, Aiden. I think you spent the night here…"

    show aiden2 pain1 at center
    voice audio.aiden_v_hngh1b2
    a "Oh man… I might’ve partied too much… "
    a "This hangover’s intense, my head’s spinning."

    show goro2 disappoint3 at right
    voice audio.goro_v_here1a
    g "Here, cover yourself up."

    show goro2_autumn at center
    show goro2 disappoint3 at center
    with move

    hide goro2_autumn
    hide goro2 disappoint3
    hide aiden2_undie
    hide aiden2 pain1
    show goro2_autumn2 at center
    show goro2 disappoint1 at center
    show aiden2_undie3 at center
    show aiden2 pain1 at center
    with dissolve

    show goro2_autumn2 at right
    show goro2 disappoint1 at right
    with move

    voice audio.aiden_v_mmm1a1
    a "Mnn… Thanks, Gramps…"

    hide yoshi2_autumn
    hide yoshi2 awkward3
    show yoshi_autumn at left
    show yoshi awkward4 at left
    voice audio.yoshi_v_worry3b
    yo "What happened to you, Aiden?!"

    if g3_club == True:
        hide goro2_autumn2
        hide goro2 disappoint1
        show goro_autumn2 at right
        show goro confused3 at right
        voice audio.goro_v_worry3a1
        g "Yes. How did you end up in this situation?"

        show aiden2 think2 at center
        voice audio.aiden_v_well1c1
        a "Well… Last night, I came in to grab a drink, and the bartender convinced me I could join in with the other entertainers!"
        a "He offered me free drinks, so I thought, sure, why not!"
    else:
        hide goro2_autumn2
        hide goro2 disappoint1
        show goro_autumn2 at right
        show goro confused3 at right
        voice audio.goro_v_worry3a1
        g "Yes. The last we saw you, you were headed to serve a guest…"

    show aiden2 laugh2 at center
    voice audio.aiden_v_laugh2a1
    a "I spent most of the night hopping from client to client, and man were they thirsty! "
    a "So I gave them what they wanted and took my pants off! And then I got a ton of cash!"

    hide yoshi_autumn
    hide yoshi awkward4
    show yoshi2_autumn at left
    show yoshi2 sigh4 at left
    voice audio.yoshi_v_really6
    yo "A-Aiden… Was that really the best idea? "

    show aiden2 play2 at center
    voice audio.aiden_v_yeah2c1
    a "Oh yeah! I got a bunch of their numbers too, so if you guys ever wanna party with some rich dudes, hit me up~!"
    a "Hehe, maybe we can land a couple more sponsorships for the camp, Gramps~"

    hide goro_autumn2
    hide goro confused3
    show goro2_autumn2 at right
    show goro2 sigh4 at right
    voice audio.goro_v_sigh2a
    g "*sigh* I’m not interested in earning money that way, Aiden…"

    hide yoshi2_autumn
    hide yoshi2 sigh4
    show yoshi_autumn at left
    show yoshi confused2 at left
    voice audio.yoshi_v_but1
    yo "But what happened after that? How did you end up passed out naked here?"

    show aiden2 think2 at center
    voice audio.aiden_v_think1a1
    a "Hmmm… I’m not really sure! Last thing I remember, I was taking a break after finishing up with a client, and the rest is a blur!"
    a "Haha, I guess I got a little too drunk! The staff didn’t seem to mind though, they got a free view of my bod while I was napping~"

    hide goro2_autumn2
    hide goro2 sigh4
    show goro_autumn2 at right
    show goro annoy3 at right
    voice audio.goro_v_question1b1
    g "Seriously, Aiden. I can’t believe you haven’t grown out of this stripping habit of yours."

    show yoshi think3 at left
    voice audio.yoshi_v_yeah1
    yo "Yeah, it goes way back to our scout days."

    show aiden2 comp3 at center
    voice audio.aiden_v_laugh1b1
    a "Ahehe… What can I say…? Call it a quirk."

    hide goro_autumn2
    hide goro annoy3
    show goro2_autumn2 at right
    show goro2 disappoint2 at right
    voice audio.goro_v_ehem1a
    g "*ehem* That ‘quirk’ of yours has caused me trouble on multiple occasions, you know…"

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

    $ location = location_cabin
    $ day = "??"
    $ time = timeline_timeday
    $ season = season_summer
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_cabin_past_day with fade
    play music camping_time loop
    play bgsound sfxloop_birds loop

    play sound sfx_dooropen
    show ygoro_camp at center
    show ygoro happy2 at center
    voice audio.ygoro_v_goodam1a1
    g "Good morning, scouts! "

    show ygoro_camp at right2
    show ygoro norm1 at right2
    with move

    show yyoshi_sleep at left2
    show yyoshi sleepy5 at left2
    with dissolve

    voice audio.yyoshi_v_yawn1
    yo "*yawn* Good morning, Sir Goro. Is it time for an activity already?"

    show ygoro laugh3 at right2
    voice audio.ygoro_v_oh2
    g "Oh, not for another hour! I was just checking in to see how our new cabin resident’s doing!"

    show yyoshi talk3 at left2
    voice audio.yyoshi_v_sir2
    yo "Ah, Aiden’s still asleep, sir! We kinda stayed up late last night, a lot of our cabinmates wanted to get to know him more."
    yo "He was really happy you let him move in here with us! Thanks for granting our request, sir!"

    show ygoro comp2 at right2
    voice audio.ygoro_v_response2a1
    g "It’s no problem, it’s the least we could do. He’s been such a huge help to the camp, after all."

    show ygoro talk3 at right2
    voice audio.ygoro_v_conj7a
    g "Speaking of which, his father’s looking for him. I think they’re about to start kitchen duty."

    show yyoshi talk4 at left2
    voice audio.yyoshi_v_yeah2
    yo "Oh yeah! He told me to wake him up for that…!"

    show ygoro confused2 at right2
    voice audio.ygoro_v_so1b
    g "Where is he anyway? I don’t see him on any of the bunks."

    show yyoshi explain2 at left2
    voice audio.yyoshi_v_oh2
    yo "Oh, he’s in the corner bunk over there, sir!"

    show ygoro talk3 at right2
    voice audio.ygoro_v_alright1a
    g "Alright, I’ll go get him up."

    show ygoro_camp at p5_5
    show ygoro confused2 at p5_5
    with move

    voice audio.ygoro_v_aiden5
    g "Aiden? *taps the blanket*"

    show yyoshi comp6 at left2
    voice audio.yyoshi_v_laugh5
    yo "Ahehe… He did say he was a heavy sleeper…"
    a "..."

    show ygoro talk1 at p5_5
    voice audio.ygoro_v_aiden2
    g "Aiden, your dad’s looking for you."

    voice audio.yaiden_v_mmm1a1
    a "Mnnn…"

    show yyoshi happy1 at left2
    voice audio.yyoshi_v_confident2
    yo "Let me do it, sir!"

    show yyoshi_sleep at p5_5
    show yyoshi bold2 at p5_5
    show ygoro_camp at p5_4
    show ygoro shock1 at p5_4
    with move

    voice audio.yyoshi_v_aiden6
    yo "AIDEN, WAKE UP! *takes blanket off*"

    show cg_fade at truecenter
    show fxsq_aiden at fx_pos
    with dissolve

    play music here_they_come_fast loop
    voice audio.yyoshi_vsg12_line1
    yo "WAH!!"
    g "...!!"

    voice audio.aiden_vsa16_line1
    a "*snores*"

    voice audio.ygoro_vsg12_line1
    g "Did he go to sleep like this…?!"

    voice audio.yyoshi_vsg12_line2
    yo "He had his underwear on last night…!"

    voice audio.ygoro_vsg12_line2
    g "Quick, put the blanket on before anyone—"

    hide cg_fade
    hide fxsq_aiden
    with dissolve

    show ydarius_sleep at p5_1
    show ydarius norm4 at p5_1
    show ylloyd_sleep at p5_2
    show ylloyd sleepy2 at p5_2
    show ygoro_camp at p5_3
    show ygoro shock1 at p5_3
    show yyoshi_sleep at p5_4
    show yyoshi shock1 at p5_4
    show yaiden_naked3 at p5_5
    show yaiden sleepy4 at p5_5
    voice audio.ylloyd_v_yawn1a
    l "*yawn* You guys are so early—"

    show ylloyd shock1 at p5_2
    l "...!!"

    show ydarius tease2 at p5_1
    voice audio.ydarius_v_worry1a
    d "PP alert."

    show ygoro comic1 at p5_3
    voice audio.ygoro_v_yoshi8
    g "Yoshinori, quick, put his underwear back on…!"

    show yyoshi awkward3 at p5_4
    voice audio.yyoshi_v_shock2a
    yo "I-I’m on it, sir…!!"

    show yyoshi_sleep at p5_5
    show yyoshi awkward3 at p5_5
    with move

    hide yaiden_naked3
    hide yaiden sleepy4
    show yaiden_undie at p5_5
    show yaiden sleepy2 at p5_5
    with dissolve

    show yyoshi_sleep at p5_4
    show yyoshi awkward3 at p5_4
    with move

    voice audio.yaiden_v_confused1b
    a "H-Huh? What’s going on?"

    show yyoshi angry2 at p5_4
    voice audio.yyoshi_v_aiden6
    yo "A-Aiden! How did you end up naked again?!"

    show yaiden confused2 at p5_5
    voice audio.yaiden_v_what1a
    a "Wha? But my undies are on right now…"

    show yyoshi angry3 at p5_4
    voice audio.yyoshi_v_no2
    yo "I-I just did that!"

    show yaiden tease2 at p5_5
    voice audio.yaiden_v_yoshi13a
    a "Oho~ Yoshi, and in front of everyone else too!"

    show ygoro disappoint4 at p5_3
    voice audio.ygoro_v_sigh2a
    g "*sigh* Boy, didn’t you cause enough ruckus at the waterfall the other day?"

    show ylloyd disappoint2 at p5_2
    voice audio.ylloyd_v_groan2c1
    l "Somehow, I feel like we’re gonna be seeing a lot more of that."

    show ydarius tease3 at p5_1
    voice audio.ydarius_v_cringe1a
    d "Fanservice."

    show yaiden comp6 at p5_5
    voice audio.yaiden_v_laugh1b1
    a "Ahehe, sorry guys… I just get hot when I sleep…"

    show yyoshi sigh4 at p5_4
    voice audio.yyoshi_v_sigh2
    yo "Y-You could have taken off the blanket instead, you know…"

    show ygoro annoy2 at p5_3
    voice audio.ygoro_v_ehem1a
    g "*ehem* Regardless, Aiden, your dad was looking for you."

    show yaiden shock3 at p5_5
    voice audio.yaiden_v_shock2a4
    a "H-Huh?! Oh, crap! I’m late! I’ll head there right away!"

    hide yaiden_undie
    hide yaiden shock3
    with moveoutleft

    show yyoshi awkward4 at p5_4
    voice audio.yyoshi_v_awkward1
    yo "H-He just left in his underwear…"

    show ygoro disappoint2 at p5_3
    voice audio.ygoro_v_sigh2a
    g "*sigh* Let him be, Andre will handle it."
    g "Now come on, since you’re all up, get in your uniforms and let’s start an activity!"

    show ylloyd tired4 at p5_2
    voice audio.ylloyd_v_aww1a1
    l "Aww… But I wanted to sleep mooore…"

    show ydarius comp2 at p5_1
    voice audio.ydarius_v_comp3a1
    d "I’ll nap with you later."

    show yyoshi talk2 at p5_4
    voice audio.yyoshi_v_yessir2a
    yo "Yes, sir! We’ll get dressed right away!"

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

    if day4_goro_choice == False:
        $ day = "79"
        $ time = timeline_timeday
        $ season = season_winter
        $ location = location_hotelclub
        show screen location
        show screen timeline
        show screen quick_menu
        $quick_menu = True
        scene bg_hotel_bar_day with fade
    else:
        $ day = "79"
        $ time = timeline_timesunset
        $ season = season_winter
        $ location = location_hotelclub
        show screen location
        show screen timeline
        show screen quick_menu
        $quick_menu = True
        scene bg_hotel_bar_sunset with fade

    play music on_the_edge_club loop
    show yoshi_autumn at left
    show yoshi comp1 at left
    show aiden2_undie3 at center
    show aiden2 comp1 at center
    show goro_autumn2 at right
    show goro disappoint3 at right
    voice audio.goro_v_shy1a
    g "Ever since then, the same thing keeps happening, except in front of more and more people."

    show aiden2 comp3 at center
    voice audio.aiden_v_laugh1b1
    a "Ahehe, I’m surprised you didn’t kick me out then. Or even now."

    show goro bored1 at right
    voice audio.goro_v_hey1a
    g "Hey, it’s not my place to judge what you’re into. But I’m pretty sure the whole camp could get shut down if the wrong person saw…"

    show yoshi confused2 at left
    voice audio.yoshi_v_actually1a
    yo "Surprisingly, we haven’t gotten any complaints, at least before Emilia. "

    show goro disappoint2 at right
    voice audio.goro_v_conj7a
    g "On that note, let’s get you out of here before someone else walks in."

    show aiden2 worry2 at center
    voice audio.aiden_v_aww1b
    a "Awww… But I’m still groggy, Grampssss… Can we stay here a little longer?"

    hide goro_autumn2
    hide goro disappoint2
    show goro2_autumn2 at right
    show goro2 angry2 at right
    voice audio.goro_v_no1a1
    g "No."

    show goro2_autumn2 at right2
    show goro2 angry2 at right2
    with move

    hide goro2_autumn2
    hide goro2 angry2
    show goro_autumn2 at right2
    show goro annoy1 at right2
    show yoshi_blush1 at left
    show yoshi shock1 at left
    show aiden2 shock2 at center
    voice audio.aiden_v_shock5a
    a "W-WAH! You don’t have to carry me, Gramps!"

    show yoshi shock3 at left
    voice audio.yoshi_v_shock2b
    yo "Wha! Money’s falling out of your underwear! That’s where you put it?!"

    show goro talk1 at right2
    voice audio.goro_v_yoshi2a
    g "Yoshinori, look for his clothes then follow us to our room."

    show aiden2 pain3 at center
    voice audio.aiden_v_hngh1a2
    a "Ow, ow, Gramps! You’re crushing my balls…!"

    hide aiden2_undie3
    hide aiden2 pain3
    hide goro_autumn2
    hide goro talk1
    with moveoutright

    hide yoshi_blush1
    show yoshi shock2 at left
    voice audio.yoshi_v_wait3b
    yo "W-Wait, Aiden’s not dressed yet!"

    show yoshi_autumn at right
    show yoshi shock1 at right
    with move

    show justin_bar at left
    show justin_glasses at left
    show justin comp2 at left
    with dissolve

    voice audio.justin_v_hmm1a
    bt "I think these are what you’re looking for."

    show yoshi awkward3 at right
    voice audio.yoshi_v_yes8
    yo "Ah yes, that’s Aiden’s clothes! Thank you!"

    voice audio.yoshi_v_sorry2c
    yo "So sorry about all that! We’ll be on our way!"

    show justin tease2 at left
    voice audio.justin_v_laugh4
    bt "Hehe, throuples."

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black with fade
    yo "{i}Sir Goro and I brought Aiden back to our room and gave him some medicine to help with his hangover.{/i}"

    if day4_goro_choice == False:
        $ day4_goro_choice = True
        $ renpy.pause (1.0, hard=True)
        yo "{i}We left him to rest and headed out to check another area of the hotel.{/i}"
        scene cg black
        hide screen location
        hide screen timeline
        hide screen quick_menu
        $quick_menu = False
        with fade
        $ time_transition_day_to_sunset_winter()
        $ time = timeline_timesunset
        $ renpy.pause (2.0, hard=True)
        $say_box = False
        $mm_talking = False
        $renpy.choice_for_skipping()
        show screen minimap()
        $ renpy.pause (hard=True)

    else:
        $ renpy.pause (1.0, hard=True)
        yo "{i}He hung out with us until he felt better, and then left to go shower in his room.{/i}"

        scene cg black
        hide screen location
        hide screen timeline
        hide screen quick_menu
        $quick_menu = False
        with fade
        $ time_transition_sunset_to_night_winter()
        $ renpy.pause (2.0, hard=True)
        jump day4_goro_after


label day4_goro_spa:
    $g4_spa = True
    $quick_menu = True
    $mm_talking = True
    $say_box = True
    voice audio.yoshi_v_think4
    yo "How about we take a dip in the bathhouse again, sir?"

    voice audio.goro_v_rush1a1
    g "Hehe, you read my mind. Let’s go."

    hide screen minimap
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

    if day4_goro_choice == False:
        $ location = location_hotelspa
        show screen location
        show screen timeline
        show screen quick_menu
        $quick_menu = True
        scene bg_hotel_spa_day with fade
        play music close_distance loop
        play bgsound sfxloop_waterflow loop
    else:
        $ location = location_hotelspa
        show screen location
        show screen timeline
        show screen quick_menu
        $quick_menu = True
        scene bg_hotel_spa_sunset with fade
        play music close_distance loop
        play bgsound sfxloop_waterflow loop

    show goro2_towel at right2
    show goro2 tease2 at right2
    show yoshi_towel at left2
    show yoshi awkward1 at left2
    voice audio.goro_v_laugh1b1
    g "Hehe, you better behave this time around, Yoshinori. The bath’s a lot more crowded than yesterday."

    hide yoshi_towel
    hide yoshi awkward1
    show yoshi2_towel at left2
    show yoshi2 awkward3 at left2
    voice audio.yoshi_v_sir4
    yo "A-As long as you don’t sneakily try to seduce me, sir…"

    voice audio.lloyd_v_groan2a3
    l "Ughhh! I can barely walk!!"

    hide yoshi2_towel
    hide yoshi2 awkward3
    show yoshi_towel at left2
    show yoshi confused2 at left2
    voice audio.yoshi_v_huh2
    yo "Huh? That voice sounds familiar. "

    show goro2_towel at p6_2
    show goro2 norm1 at p6_2
    show yoshi_towel at p6_1
    show yoshi confused2 at p6_1
    with move

    show darius_towel at p6_6
    show darius play1 at p6_6
    show lloyd_towel at p6_5
    show lloyd pout4 at p6_5
    with dissolve

    voice audio.lloyd_v_darius6c
    l "This wouldn’t have happened if you weren’t so rough last night, you know?"

    show darius comp2 at p6_6
    voice audio.darius_v_comp3a
    d "I’ll carry you."

    show lloyd angry2 at p6_5
    voice audio.lloyd_v_question1e4
    l "Wh-What? No! Everyone’s gonna look at us again!"

    show yoshi happy1 at p6_1
    voice audio.yoshi_v_guys2
    yo "Hey, guys! Over here!"

    show darius happy2 at p6_6
    voice audio.darius_v_shock1c1
    d "Oh. Yoshi. Sir Goro."

    show darius_towel at p4_4
    show darius happy2 at p4_4
    show lloyd_towel at p4_3
    show lloyd angry2 at p4_3
    show goro2_towel at p4_2
    show goro2 happy2 at p4_2
    show yoshi_towel at p4_1
    show yoshi happy2 at p4_1
    with move

    hide goro2_towel
    hide goro2 happy2
    show goro_towel at p4_2
    show goro happy2 at p4_2
    voice audio.goro_v_goodam2a2
    g "It’s nice seeing you two here, Lloyd, Darius."

    show lloyd happy2 at p4_3
    voice audio.lloyd_v_greet1b2
    l "Hiiii~! I’m so excited we get to check out the spa today! We didn’t get to yesterday, and I totally would’ve regretted not coming here!"
    l "Isn’t this place cool?!"

    show darius tease2 at p4_4
    voice audio.darius_v_conj1a2
    d "More like hot."

    show lloyd annoy2 at p4_3
    voice audio.lloyd_v_angry1a2
    l "Shush, Dar."

    show yoshi laugh2 at p4_1
    voice audio.yoshi_v_unsure3a
    yo "I guess today is treat-yourself day, huh?"

    show lloyd happy2 at p4_3
    voice audio.lloyd_v_agree2b2
    l "Yeah! I heard aromatherapy is really good to reduce stress and boost energy levels~ So we came here for a soak!"

    show darius play2 at p4_4
    voice audio.darius_v_conj2a
    d "Hot water is good for muscle pain."

    show goro happy3 at p4_2
    voice audio.goro_v_rush2a1
    g "Why don’t you guys join us then? There’s plenty of room beside me and Yoshinori here in the tub!"

    show lloyd_towel at center
    show lloyd happy2 at center
    with move

    show lloyd_towel at p4_3
    show lloyd pain5 at p4_3
    voice audio.lloyd_v_shock4c1
    l "GAHHH! HOT! HOT! HOT! " with vpunch
    l "How are you guys withstanding this heat?! "

    show darius relief2 at p4_4
    voice audio.darius_v_excited1a1
    d "It’s nice."

    show lloyd rage3 at p4_3
    voice audio.lloyd_v_disagree1b2
    l "TOTALLY NOT! It feels like I’m being boiled alive!!"

    show goro laugh1 at p4_2
    voice audio.goro_v_comp2a2
    g "Haha! Don’t worry, you’ll get used to it if you stay in longer."

    show lloyd pain1 at p4_3
    voice audio.lloyd_v_groan1b1
    l "Hnghh… This boiling water doesn’t really help. I just can’t get comfy in this bath, no matter how I sit!"

    show yoshi talk3 at p4_1
    voice audio.yoshi_v_oh1
    yo "Oh, what’s the matter, Lloyd? Are you hurt somewhere?"

    show lloyd tired1 at p4_3
    voice audio.lloyd_v_unsure1b1
    l "Sort of… I’ve been limping all day thanks to Dar over here! This guy doesn’t know how to take it easy!"

    show darius tired2 at p4_4
    voice audio.darius_v_agree2a
    d "I’m pretty sore too."

    show goro play2 at p4_2
    voice audio.goro_v_heh1a
    g "Did you two have a group ‘workout’ yesterday?"

    show lloyd talk1 at p4_3
    voice audio.lloyd_v_agree2a3
    l "Yeah! We tried so many positions. It’s been a while since we got to sweat together like that."

    show yoshi shock2 at p4_1
    voice audio.yoshi_v_what3
    yo "H-How are you all talking so casually about this…?"

    show lloyd confused2 at p4_3
    voice audio.lloyd_v_confused1a3
    l "Huh? We’re talking about our exercise sesh yesterday! I was doing yoga and he was lifting!"

    show darius tease4 at p4_4
    voice audio.darius_v_naughty1a
    d "Naughty Yoshi."

    show yoshi awkward5 at p4_1
    voice audio.yoshi_v_shock4
    yo "A-Ack…! "

    hide goro_towel
    hide goro play2
    show goro2_towel at p4_2
    show goro2 tease3 at p4_2
    voice audio.goro_v_yoshi15a
    g "Yeah, Yoshinori. Get your mind out of the gutter."

    show lloyd laugh2 at p4_3
    voice audio.lloyd_v_laugh1a1
    l "Haha, being in a giant pool like this feels kinda nostalgic though – it’s been a long time since we’ve been swimming together!"

    show darius confused2 at p4_4
    voice audio.darius_v_question1a
    d "You and I just went to the beach last summer, though."

    show lloyd happy2 at p4_3
    voice audio.lloyd_v_agree2a1
    l "Yeah, but I meant as a group! We used to go on short trips to the beach when we were scouts~"
    l "Honestly, it’s kinda nicer in here though – I don’t have to worry about the sun as much!"

    show yoshi talk3 at p4_1
    voice audio.yoshi_v_yeah1
    yo "Oh yeah, I forgot that you get sunburnt really easily, don’t you?"

    show darius tease2 at p4_4
    voice audio.darius_v_laugh1
    d "He has sensitive skin."

    show goro2 think6 at p4_2
    voice audio.goro_v_think1a1
    g "Hmm, if I recall, you had a fairly severe case of it on one our trips too…"

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

    $ location = location_beach
    $ day = "??"
    $ time = timeline_timeday
    $ season = season_summer
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_beach_summer_day with fade
    play music coastal_groove loop

    show ydarius_swim at p4_1
    show ydarius norm2 at p4_1
    show yyoshi_swim at p4_2
    show yyoshi relief2 at p4_2
    show ygoro_swim at p4_3
    show ygoro norm2 at p4_3
    show yaiden_swim at p4_4
    show yaiden norm1 at p4_4
    voice audio.yyoshi_v_relief1
    yo "Whew! That swim was so refreshing!"

    show ygoro laugh2 at p4_3
    voice audio.ygoro_v_laugh1a
    g "Haha, I agree. Thank goodness the water’s cool, we needed an escape from the heat."

    show ydarius happy2 at p4_1
    voice audio.ydarius_v_agree5b
    d "Summer’s here."

    show yaiden amazed2 at p4_4
    voice audio.yaiden_v_amazed3b
    a "Wahh… I feel so lucky I finally got to swim on a real beach. "

    show yyoshi comp2 at p4_2
    voice audio.yyoshi_v_yessir2a
    yo "Yeah, sir! Thanks for taking us here for the field trip!"

    show ygoro happy3 at p4_3
    voice audio.ygoro_v_glad1a
    g "Haha, I knew you boys would like it."

    show yyoshi confused3 at p4_2
    voice audio.yyoshi_v_wait5
    yo "Hold on…  I just realized… Aren’t we missing someone?"

    show ydarius confused2 at p4_1
    voice audio.ydarius_v_agree2a1
    d "Yeah. Where’s Lloyd?"

    show ydarius_swim at p5_2
    show ydarius shock1 at p5_2
    show yyoshi_swim at p5_3
    show yyoshi shock1 at p5_3
    show ygoro_swim at p5_4
    show ygoro shock1 at p5_4
    show yaiden_swim at p5_5
    show yaiden shock1 at p5_5
    with move

    show ylloyd_swim2 at p5_1
    show ylloyd sigh5 at p5_1
    with dissolve

    hide yyoshi_swim
    hide yyoshi shock1
    show yyoshi_swim at p5_3
    show yyoshi shock1 at p5_3
    voice audio.ylloyd_v_ah1c1
    l "Aaaaaa…."

    show yyoshi shock3 at p5_3
    voice audio.yyoshi_v_shock2a
    yo "Wah! What happened to you, Lloyd?!"

    show ygoro shock2 at p5_4
    voice audio.ygoro_v_shock1a
    g "Th-That’s a really bad sunburn!"

    show ylloyd pain1 at p5_1
    voice audio.ylloyd_v_groan1c1
    l "Hnghh… I chilled out on the hammock and forgot to put sunscreen on… I didn’t realize the sun was directly on me when I fell asleep."

    show yaiden pain1 at p5_5
    voice audio.yaiden_v_shock2b1
    a "Yikes… That looks like it hurts!"

    show ylloyd scared3 at p5_1
    voice audio.ylloyd_v_sad1a1
    l "Huhuhu… It does… What do I doooo, guys?"

    show ygoro talk1 at p5_4
    voice audio.ygoro_v_rush2d1
    g "First off, let’s get you out of the sun right away."
    g "Yoshinori, get the aloe cream from the first aid kit. Darius, set up a beach mat and an umbrella. Aiden, fetch him some water."

    show yaiden talk6 at p5_5
    show yyoshi talk1 at p5_3
    voice audio.yaiden_v_yessir1a1
    yoa "Yes, sir!"

    hide yyoshi_swim
    hide yyoshi talk1
    hide yaiden_swim
    hide yaiden talk6
    with dissolve

    show ydarius_swim at p5_4
    show ydarius worry2 at p5_4
    show ylloyd_swim2 at p5_3
    show ylloyd pain1 at p5_3
    show ygoro_swim at p5_2
    show ygoro worry1 at p5_2
    with move

    voice audio.ydarius_v_lloyd4a
    d "Lay down here, Lloyd."

    show ylloyd pain3 at p5_3
    voice audio.ylloyd_v_shock4a1
    l "Ow, ow, ow, it hurts when I move."

    show ygoro confused3 at p5_2
    voice audio.ygoro_v_think2a1
    g "It looks like a bad burn, but only on your front side.  Applying cream should do the trick."

    show yaiden_swim at p5_5
    show yaiden talk3 at p5_5
    with dissolve

    voice audio.yaiden_v_lloyd1a
    a "Here, Lloyd! Drink up!"

    show ylloyd pain1 at p5_3
    l "*glug* *glug*"

    show yyoshi_swim at p5_1
    show yyoshi talk3 at p5_1
    with dissolve

    voice audio.yyoshi_v_here1
    yo "Here’s the cream, sir!"

    show ygoro explain2 at p5_2
    voice audio.ygoro_v_alright1a
    g "Alright, this is going to sting a little. I’ll start applying it to your face."

    show ydarius tease2 at p5_4
    voice audio.ydarius_v_agree5d
    d "I’ll do his legs."

    show yaiden excited3 at p5_5
    voice audio.yaiden_v_excited6a
    a "Ooh, ooh, I wanna help too!"

    show yyoshi angry2 at p5_1
    voice audio.yyoshi_v_okay2
    yo "Okay, let’s start creaming! "

    show cg_fade at truecenter
    show fxsq_lloyd 1 at fx_pos with dissolve

    play sound sfx_lotion
    voice audio.ylloyd_vsg13_line1
    l "Wah, careful! Don’t get it in my eye!"

    show fxsq_lloyd 2 at fx_pos with Dissolve(0.25)
    voice audio.yyoshi_vsg13_line1
    yo "Uhh... We might’ve squirted too much."

    voice audio.ylloyd_vsg13_line2
    l "Nnn….Stickyyy…"

    voice audio.ydarius_vsg13_line1
    d "Let’s get rubbing."

    show fxsq_lloyd 3 at fx_pos with Dissolve(0.25)
    voice audio.ylloyd_vsg13_line3
    l "Ow, ow! That stings!"

    voice audio.yaiden_vsg13_line1
    a "Oof, don’t move too much, Lloyd!"

    voice audio.ygoro_vsg13_line1
    g "Don’t worry it’ll feel better soon."

    show fxsq_lloyd 4 at fx_pos with Dissolve(0.25)
    voice audio.ylloyd_vsg13_line4
    l "Waaahhh… That feels nice and cool…"

    voice audio.ygoro_vsg13_line2
    g "See? Just relax and enjoy it."

    voice audio.ydarius_vsg13_line2
    d "Your skin is so soft, Lloyd."

    voice audio.yyoshi_vsg13_line2
    yo "Y-Yeah, I was gonna say…"

    voice audio.yaiden_vsg13_line2
    a "Hehe~ Smooth and silky!"

    show fxsq_lloyd 5 at fx_pos with Dissolve(0.25)
    voice audio.ylloyd_vsg13_line5
    l "Hey, hey! Don’t squeeze too much, it tickles…!!"

    hide cg_fade
    hide fxsq_lloyd 5
    with dissolve

    hide ylloyd_swim2
    hide ylloyd pain1
    show yaiden_swim at p6_6
    show yaiden shock1 at p6_6
    show ydarius_swim at p6_5
    show ydarius shock1 at p6_5
    show ylloyd_swim3 at p6_4
    show ylloyd relief1 at p6_4
    show ygoro_swim at p6_3
    show ygoro shock1 at p6_3
    show yyoshi_swim at p6_2
    show yyoshi shock1 at p6_2

    show yyuri_swim at p6_1
    show yyuri fangirl2 at p6_1
    voice audio.yyuri_v_kyaa1
    yu "KYAAAAAAA!!!" with vpunch
    yu "What are you all doing to poor Lloyd?! A fivesome out in the open?!"

    show ylloyd relief3 at p6_4
    voice audio.ylloyd_v_relief2a1
    l "Hehh… More please…"

    show yyoshi shock3 at p6_2
    voice audio.yyoshi_v_shock4
    yo "G-Gah, YURI! This is not what it looks like!"

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

    if day4_goro_choice == True:
        $ day = "79"
        $ time = timeline_timeday
        $ season = season_winter
        $ location = location_hotelspa
        show screen location
        show screen timeline
        show screen quick_menu
        $quick_menu = True
        scene bg_hotel_spa_sunset with fade
        play music close_distance loop
        play bgsound sfxloop_waterflow loop
    else:
        $ location = location_hotelspa
        $ day = "79"
        $ time = timeline_timesunset
        $ season = season_winter
        show screen location
        show screen timeline
        show screen quick_menu
        $quick_menu = True
        scene bg_hotel_spa_day with fade
        play music close_distance loop
        play bgsound sfxloop_waterflow loop

    show darius_towel at p4_4
    show darius tease1 at p4_4
    show lloyd_towel at p4_3
    show lloyd scared3 at p4_3
    show goro2_towel at p4_2
    show goro2 shy1 at p4_2
    show yoshi2_towel at p4_1
    show yoshi2 comp1 at p4_1
    voice audio.lloyd_v_groan1c2
    l "Oh my god, I had forgotten about that… That was so criiiinge!!!"

    show darius tease2 at p4_4
    voice audio.darius_v_naughty1a
    d "You were enjoying it."

    show lloyd sigh4 at p4_3
    voice audio.lloyd_v_darius6a
    l "Darrrrr…"

    show goro2 sigh4 at p4_2
    voice audio.goro_v_sigh2a
    g "*sigh* I had so much to explain to Yuri after that…"

    show yoshi2 comp3 at p4_1
    voice audio.yoshi_v_well1
    yo "Well, at least here in the spa you don’t have to worry about getting burnt again, Lloyd!"

    show lloyd happy1 at p4_3
    voice audio.lloyd_v_agree2b1
    l "Yeah, exactly!"

    show darius tease4 at p4_4
    voice audio.darius_v_conj1b1
    d "Although if you want to get creamed again, that’s still an option."

    show lloyd shock3 at p4_3
    show lloyd_blush2 at p4_3
    voice audio.lloyd_v_darius10a
    l "DAR!"

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black with fade
    yo "{i}Sir Goro and I stayed a little longer to chat with Lloyd and Darius, while we all relaxed in the hot bath.{/i}"

    if day4_goro_choice == False:
        $ day4_goro_choice = True
        $ renpy.pause (1.0, hard=True)
        yo "{i}Eventually, we decided to get out and explore another area of the hotel!{/i}"
        scene cg black
        hide screen location
        hide screen timeline
        hide screen quick_menu
        $quick_menu = False
        with fade
        $ time_transition_day_to_sunset_winter()
        $ time = timeline_timesunset
        $ renpy.pause (2.0, hard=True)
        $say_box = False
        $mm_talking = False
        $renpy.choice_for_skipping()
        show screen minimap()
        $ renpy.pause (hard=True)

    else:
        $ renpy.pause (1.0, hard=True)
        yo "{i}Eventually, we decided to head back to our room for the night.{/i}"

        scene cg black
        hide screen location
        hide screen timeline
        hide screen quick_menu
        $quick_menu = False
        with fade
        $ time_transition_sunset_to_night_winter()
        $ renpy.pause (2.0, hard=True)
        jump day4_goro_after

label day4_goro_cafe:
    $sq_emilia += 1
    $g4_cafe = True
    $quick_menu = True
    $mm_talking = True
    $say_box = True
    voice audio.yoshi_v_think4
    yo "We could grab something to eat over at the café!"

    if a3_cafe == True:
        voice audio.goro_v_alright1b1
        g "Sure, I’m curious what the menu is like there."
    else:
        voice audio.goro_v_alright1b1
        g "Sure. We can grab a light snack."

    hide screen minimap
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

    if day4_goro_choice == False:
        $ location = location_hotelcafe
        show screen location
        show screen timeline
        show screen quick_menu
        $quick_menu = True
        scene bg_hotel_cafe_day with fade
        play music close_distance loop
    else:
        $ location = location_hotelcafe
        show screen location
        show screen timeline
        show screen quick_menu
        $quick_menu = True
        scene bg_hotel_cafe_sunset with fade
        play music close_distance loop

    show goro_autumn at left2
    show goro norm1 at left2
    show yoshi_autumn at right2
    show yoshi shock2 at right2
    voice audio.yoshi_v_amazed1a
    yo "Wow, look at all these fancy-sounding drinks and desserts! They all look delicious, sir!"

    show goro happy2 at left2
    voice audio.goro_v_yeah1a1
    g "Yeah. I’ll get us some and we can chill here for a while. Everything we order is paid for anyway."

    show yoshi laugh1 at right2
    voice audio.yoshi_v_laugh1
    yo "We should enjoy that while it lasts! Haha!"

    show goro confused2 at left2
    voice audio.goro_v_unsure3a1
    g "Looking at the menu, I might order some exotic black coffee. Maybe you could pick a snack we can share?"

    $ working = False
    $ shuffle_menu()
    menu():
        g "Looking at the menu, I might order some exotic black coffee. Maybe you could pick a snack we can share?{fast}"
        "Hotdog sandwich.":
            $ working = True
            $ score_bot += 1
            show yoshi confused2 at right2
            voice audio.yoshi_v_think4
            yo "How about a hotdog sandwich, sir?"

            hide goro_autumn
            hide goro confused2
            show goro2_autumn at left2
            show goro2 play2 at left2
            voice audio.goro_v_heh1a
            g "Oh, I’d love it if you sandwiched my hotdog."
        "Bread Roll.":
            $ working = True
            $ score_top += 1
            show yoshi confused2 at right2
            voice audio.yoshi_v_think4
            yo "Bread rolls look good."

            hide goro_autumn
            hide goro confused2
            show goro2_autumn at left2
            show goro2 play2 at left2
            voice audio.goro_v_heh1a
            g "Bread rolls, you say? *lifts shirt up a little*"
        "Baguette.":
            $ working = True
            $ score_bot += 2
            show yoshi confused2 at right2
            voice audio.yoshi_v_think4
            yo "How about that whole wheat baguette, sir?"

            hide goro_autumn
            hide goro confused2
            show goro2_autumn at left2
            show goro2 play2 at left2
            voice audio.goro_v_heh1a
            g "Oh, I’ll show you a whole meat baguette."
        "Cream-Filled Donut.":
            $ working = True
            $ score_top += 2
            show yoshi confused2 at right2
            voice audio.yoshi_v_think4
            yo "How about some cream-filled donut holes!"

            hide goro_autumn
            hide goro confused2
            show goro2_autumn at left2
            show goro2 play2 at left2
            voice audio.goro_v_heh1a
            g "Oh, I’ll cream fill your donut hole."

    show yoshi awkward3 at right2
    voice audio.yoshi_v_sir3
    yo "S-Sir!"

    hide goro2_autumn
    hide goro2 play2
    show goro_autumn at left2
    show goro laugh1 at left2
    voice audio.goro_v_laugh2a
    g "Hahaha! Come on, you asked for that one!"
    g "You know what? I could get used to this."

    show yoshi angry2 at right2
    voice audio.yoshi_v_no2
    yo "I won’t…!"

    show goro happy2 at left2
    voice audio.goro_v_anyway1
    g "Anyway, I’ll go place our order. Go and find us a table."

    hide yoshi_autumn
    hide yoshi angry2
    show yoshi2_autumn at right2
    show yoshi2 sigh4 at right2
    voice audio.yoshi_v_sigh3a
    yo "*sigh* Okay, sir…"

    hide goro_autumn
    hide goro happy2
    with dissolve

    show yoshi2_autumn at center
    show yoshi2 sigh4 at center
    with move

    $ renpy.music.stop(channel='music', fadeout = 2.0)
    hide yoshi2_autumn
    hide yoshi2 sigh4
    show yoshi_autumn at center
    show yoshi think2 at center
    voice audio.yoshi_v_alright1
    yo "Alright, maybe somewhere in the back…"

    show yoshi_autumn at p5_5
    show yoshi shock1 at p5_5
    with move

    show reimond_waiter at p5_1
    show reimond sad1 at p5_1
    show emilia_autumn at p5_2
    show emilia angry2 at p5_2
    with dissolve

    play music heracleum_a loop
    voice audio.emilia_v_angry2
    e "I can’t believe you served me something raw! Touch this meat and tell me that’s not just taken straight out of the fridge!"

    show reimond confused2 at p5_1
    voice audio.reimond_v_maam1b
    r "You ordered prosciutto, ma’am… And it’s from our cold cuts menu…"

    show emilia rage4 at p5_2
    voice audio.emilia_v_question4b
    e "I-I knew that! But I’m not trying to get salmonella on my vacation, is that too hard to understand?!"

    show reimond sad2 at p5_1
    voice audio.reimond_v_apology1a1
    r "U-Um… No, I’m sorry. Maybe you would prefer some bacon or ham instead?"

    show emilia disgust2 at p5_2
    voice audio.emilia_v_request4a
    e "I didn’t come here to eat something that common! Now, cook this meat up before I sue this entire place!"

    show reimond sad6 at p5_1
    voice audio.reimond_v_agree6c1
    r "S-Sure… Right away, ma’am."

    hide reimond_waiter
    hide reimond sad6
    with dissolve

    show emilia sigh1 at p5_2
    voice audio.emilia_v_sigh1a
    e "*sigh* Can’t even have a good time around here…"

    show emilia shock3 at p5_2
    e "...!"

    show emilia irked2 at p5_2
    voice audio.emilia_v_so3
    e "Are you just going to stand over there and pretend I didn’t see you?"

    hide yoshi_autumn
    hide yoshi shock1
    show yoshi2_autumn at p5_5
    show yoshi2 awkward3 at p5_5
    voice audio.yoshi_v_ah4
    yo "A-Ah…!"

    show emilia_autumn at left2
    show emilia irked2 at left2
    show yoshi2_autumn at right2
    show yoshi2 talk3 at right2
    with move

    voice audio.yoshi_v_actually1a
    yo "Sir Goro and I are actually here to grab a meal. I just happened to notice you were having a problem with the staff again."

    show emilia eyeroll4 at left2
    voice audio.emilia_v_hmph1a
    e "Hmph! If you assumed I needed you or anyone’s help then you’re sorely mistaken."

    show yoshi2 awkward3 at right2
    voice audio.yoshi_v_well1
    yo "Well… It’s hard to think otherwise seeing you stressed out like this even though we’re on vacation."
    yo "In fact, I haven’t seen you hang out with anyone since we got here… Maybe you should try to join us and use this chance to get to know everyone!"

    show emilia angry2 at left2
    voice audio.emilia_v_angry1b
    e "You have the nerve to tell me that? Don’t tell me how I should spend my time!"

    show yoshi2 panic2 at right2
    voice audio.yoshi_v_no4
    yo "N-No, Emilia. I was only trying to—"

    show emilia sigh1 at left2
    voice audio.emilia_v_tsun4
    e "None of you invited me anyway, so why should I bother squeezing myself into a group who doesn’t give a damn in the first place?"
    e "I’d rather be alone than spend my precious time pretending to be friends with people like you."

    show yoshi2 angry3 at right2
    voice audio.yoshi_v_emilia4
    yo "*sigh* Emilia… "

    show emilia irked2 at left2
    voice audio.emilia_v_what2
    e "What?!"

    hide yoshi2_autumn
    hide yoshi2 panic2
    show yoshi_autumn at right2
    show yoshi worry2 at right2
    voice audio.yoshi_v_unsure1b
    yo "I just don’t understand… What are you getting out of this?"
    yo "You’re pushing everyone away and letting all of us think that you hate us…"

    show emilia angry5 at left2
    voice audio.emilia_v_scoff1
    e "Who are we kidding here, Yoshinori? I hate all of you, and you all hate me. There’s no secret there."

    show yoshi sad4 at right2
    voice audio.yoshi_v_but2
    yo "Even if I tell you that’s not true, you wouldn’t believe me anyway."
    yo "But I at least thought you’d feel a little ‘at-home’ with all of these fancy things around."

    show emilia explain2 at left2
    voice audio.emilia_v_well2
    e "It’s nowhere close to what I’m used to. "
    e "You know I have high standards, considering I get way better food, service and atmosphere at home than at this mediocre hotel!"

    show emilia talk1 at left2
    voice audio.emilia_v_conj6
    e "But don’t get me wrong, this is far more bearable than having to stay in that raggedy camp."

    show yoshi confused2 at right2
    voice audio.yoshi_v_why1
    yo "It really doesn’t make sense to me why you even chose to come back and work with us if you hate it so much…"

    show emilia rage4 at left2
    voice audio.emilia_v_angry4b
    e "GRAH! Why are you suddenly probing me about all of this?! As if I needed one more person to keep scrutinizing everything I do!"
    e "This is exactly why I wanted to be alone in the first place!"

    show yoshi awkward4 at right2
    voice audio.yoshi_v_no4
    yo "N-No, Emilia wait—"

    hide emilia_autumn
    hide emilia rage4
    with dissolve

    hide yoshi_autumn
    hide yoshi awkward4
    show yoshi2_autumn at right2
    show yoshi2 sigh1 at right2
    voice audio.yoshi_v_sigh3a
    yo "Not again…"

    show goro_autumn at left2
    show goro disappoint2 at left2
    with dissolve

    voice audio.goro_v_annoyed4a
    g "That was hard to watch…"

    show yoshi2 worry2 at right2
    voice audio.yoshi_v_ah4
    yo "A-Ah…! I didn’t realize you were there, sir…"

    show goro confused2 at left2
    voice audio.goro_v_worry3a1
    g "I just arrived. What happened?"

    show yoshi2 worry3 at right2
    voice audio.yoshi_v_think1a
    yo "It looks like there’s no chance any of us can get along with her. She’s made up her mind that we’re all out to get her."

    show goro disappoint3 at left2
    voice audio.goro_v_conj10a1
    g "Sadly, she’s always been like that…"
    g "Even when she was a scout, all she ever did was complain and push people away…"

    show yoshi2 sad4 at right2
    voice audio.yoshi_v_well1
    yo "I don’t think that was her intent… She’s had a lot of problems she had to deal with even back then."

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
    $quick_menu = False
    hide screen quick_menu
    with fade
    $ renpy.pause (2.0, hard=True)

    $ location = location_shed
    $ day = "??"
    $ time = timeline_timeday
    $ season = season_summer
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_outshed_past_day with fade
    play bgsound sfxloop_birds loop

    show yyoshi_camp at center
    show yyoshi pain1 at center
    voice audio.yyoshi_v_groan1b
    yo "Hnghh... This wagon really needs some oil…"
    yo "I should’ve dragged Aiden with me, he’d know what to do to fix this!"

    voice audio.yemilia_v_dismiss1
    mys_e "I demand you come here and pick me up from this place once and for all!"

    show yyoshi confused2 at center
    voice audio.yyoshi_v_huh1
    yo "H-Huh…?"

    show cg fade at truecenter
    show fxsq_emilia 1 at fx_pos
    with dissolve

    play music heracleum_musicbox_a loop
    voice audio.yemilia_vsa12_line1
    e "Everything here is primitive and disgusting! And the commoners here make me sick!"

    voice audio.yemilia_vsa12_line2
    e "Surely there was a better option than this trashy camp! At the very least you could’ve let me stay at home alone!"

    voice audio.yemilia_vsa12_line3
    e "I can’t stand being here for another minute! Why did you even send me here?!"

    show fxsq_emilia 2 at fx_pos with Dissolve(0.25)
    e "..."

    show fxsq_emilia 3 at fx_pos with Dissolve(0.25)
    voice audio.yemilia_vsa12_line4
    e "I-I know that you’re out of the country! Shouldn’t I have gone with you?!"

    voice audio.yemilia_vsa12_line5
    e "You’re always leaving me behind! And all you and Dad ever do is scold me when you’re around!"

    voice audio.yemilia_vsa12_line6
    e "It’s like you don’t even care about me! You’re the worst—"

    show fxsq_emilia 4 at fx_pos with Dissolve(0.25)
    e "...!"

    show fxsq_emilia 5 at fx_pos with Dissolve(0.25)
    voice audio.yemilia_vsa12_line7
    e "Did you really send me here just to punish me?! "

    voice audio.yemilia_vsa12_line8
    e "I-I don’t need strangers giving me useless life lessons!"

    show fxsq_emilia 4 at fx_pos with Dissolve(0.25)
    e "...!!"

    show fxsq_emilia 3 at fx_pos with Dissolve(0.25)
    voice audio.yemilia_vsa12_line9
    e "Wh-What…?! N-No! You can’t do that!!"

    voice audio.yemilia_vsa12_line10
    e "Mom, please!! Don’t leave me here!"

    voice audio.yemilia_vsa12_line11
    e "I—"

    play sound sfx_phonebutton
    hide cg fade
    hide fxsq_emilia 3
    with dissolve

    show yemilia_camp at p5_1
    show yemilia rage4 at p5_1
    with dissolve

    voice audio.yemilia_v_angry4a
    e "GRAHHH!!!" with vpunch
    e "*throws phone on the ground*"

    show yemilia rage6 at p5_1
    voice audio.yemilia_v_angry9
    e "Stupid camp! Stupid parents! Stupid everything!!"

    show yyoshi_camp at right2
    show yyoshi worry2 at right2
    show yemilia_camp at left2
    show yemilia rage6 at left2
    with move

    voice audio.yyoshi_v_emilia5
    yo "A-Are you alright, Emilia?"

    show yemilia panic2 at left2
    e "...!"

    show yemilia angry3 at left2
    voice audio.yemilia_v_gasp1
    e "How long have you been standing there?! Were you spying on me?!"

    show yyoshi worry5 at right2
    voice audio.yyoshi_v_no3
    yo "N-No, I was just passing by and I heard you screaming on the phone…"

    show yemilia angry2 at left2
    voice audio.yemilia_v_angry1a
    e "It’s none of your business! And don’t you dare tell anyone what you’ve heard!"

    show yyoshi sad4 at right2
    voice audio.yyoshi_v_awkward1
    yo "Y-Your phone, though… It’s broken… I can ask a scoutmaster to fix it."

    show yemilia rage4 at left2
    voice audio.yemilia_v_angry2a
    e "You’re just gonna use that to get me in trouble, aren’t you?!"

    show yyoshi panic2 at right2
    voice audio.yyoshi_v_disagree2
    yo "N-No, that’s not—"

    show yemilia rage6 at left2
    voice audio.yemilia_v_annoyed2b2
    e "Shut up! Just leave me alone like everyone else!!!"

    hide yemilia_camp
    hide yemilia rage6
    with dissolve

    show yyoshi sad1 at right2
    yo "..."

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

    if day4_goro_choice == True:
        $ day = "79"
        $ time = timeline_timeday
        $ season = season_winter
        $ location = location_hotelcafe
        show screen location
        show screen timeline
        show screen quick_menu
        $quick_menu = True
        scene bg_hotel_cafe_sunset with fade
        play music heracleum_musicbox_a loop
    else:
        $ location = location_hotelcafe
        $ day = "79"
        $ time = timeline_timesunset
        $ season = season_winter
        show screen location
        show screen timeline
        show screen quick_menu
        $quick_menu = True
        scene bg_hotel_cafe_day with fade
        play music heracleum_musicbox_a loop

    show goro_autumn at left2
    show goro sigh1 at left2
    show yoshi2_autumn at right2
    show yoshi2 upset1 at right2
    voice audio.goro_v_sigh2a
    g "Sadly, what you overheard was true. "
    g "I only met her parents once when they enrolled her in the camp. And let’s just say they made a… lasting impression."

    show goro angry2 at left2
    voice audio.goro_v_annoyed4a
    g "They talked about their own daughter as if it was a nuisance to deal with her."
    g "As a parent myself, I couldn’t understand that at all. "

    show yoshi2 worry2 at right2
    voice audio.yoshi_v_response1c
    yo "None of us know the whole story but I can understand a little why she acts like that…"

    show goro worry2 at left2
    voice audio.goro_v_yoshi4
    g "You were always so nice to her. But then, you’re always nice to everyone."

    show yoshi2 sad5 at right2
    voice audio.yoshi_v_well1
    yo "Well... We never know what’s going on behind the scenes in people’s lives, so it’s best to give them the benefit of the doubt…"

    hide goro_autumn
    hide goro worry2
    show goro2_autumn at left2
    show goro2 sigh2 at left2
    voice audio.goro_v_conj4a
    g "Still, it’s unfortunate she never grew out of her past attitude."

    show yoshi2 sigh1 at right2
    voice audio.yoshi_v_right10
    yo "I agree…"

    hide goro2_autumn
    hide goro2 sigh2
    show goro_autumn at left2
    show goro talk1 at left2
    voice audio.goro_v_anyway1
    g "Anyway, try not to get too bothered by it. Let’s sit down and enjoy our snacks."

    hide yoshi2_autumn
    hide yoshi2 sigh1
    show yoshi_autumn at right2
    show yoshi sad4 at right2
    voice audio.yoshi_v_sure3
    yo "Alright, Sir Goro. Thanks."

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black with fade
    yo "{i}Somehow, whenever Emilia and I interact, it always ends up so tense… I wish there was a way to reach her like I could back then.{/i}"
    yo "{i}But I can only do so much, and she’s not willing to meet me halfway…{/i}"
    yo "{i}Thankfully, Sir Goro was there to get my mind off of her.{/i}"
    $ renpy.pause (1.0, hard=True)

    if day4_goro_choice == False:
        $ day4_goro_choice = True
        yo "{i}We stayed a little longer, enjoying our snacks with the beautiful view.{/i}"
        $ renpy.pause (1.0, hard=True)
        yo "{i}Eventually, we decided to get out and explore another area of the hotel! {/i}"
        scene cg black
        hide screen location
        hide screen timeline
        hide screen quick_menu
        $quick_menu = False
        with fade
        $ time_transition_day_to_sunset_winter()
        $ time = timeline_timesunset
        $ renpy.pause (2.0, hard=True)
        $say_box = False
        $mm_talking = False
        $renpy.choice_for_skipping()
        show screen minimap()
        $ renpy.pause (hard=True)

    else:
        yo "{i}We stayed a little longer, relaxing and enjoying the afternoon.{/i}"
        $ renpy.pause (1.0, hard=True)
        yo "{i}Eventually, we decided to head back to our room for the night.{/i}"

        scene cg black
        hide screen location
        hide screen timeline
        hide screen quick_menu
        $quick_menu = False
        with fade
        $ time_transition_sunset_to_night_winter()
        $ renpy.pause (2.0, hard=True)
        jump day4_goro_after

label day4_goro_room:
    $sq_jin += 1
    $say_box = True
    $quick_menu = True
    $mm_talking = True
    $g4_room = True
    if g4_room == True:
        voice audio.yoshi_v_think4
        yo "Why don’t we go and check on Jin? "

        voice audio.goro_v_yeah1a1
        g "Yeah. He might need some encouragement getting out of his room."
    else:
        voice audio.yoshi_v_think4
        yo "Maybe we should check on what the others are doing?"

        voice audio.goro_v_alright1a1
        g "I don’t mind. Maybe they’re up to something interesting."

    hide screen minimap
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

    if day4_goro_choice == False:
        $ location = location_hotelroom
        show screen location
        show screen timeline
        show screen quick_menu
        $quick_menu = True
        scene bg_hotel_room2_day with fade
        play music here_they_come loop
    else:
        $ location = location_hotelroom
        show screen location
        show screen timeline
        show screen quick_menu
        $quick_menu = True
        scene bg_hotel_room2_sunset with fade
        play music here_they_come loop

    play sound sfx_doorknock
    show jin_sleep at center
    show jin_glasses at center
    show jin talk2 at center
    $ renpy.pause (1.0, hard=True)
    voice audio.jin_v_oh3a
    j "O-Oh, coming! Give me just a moment!"

    show jin_sleep at p5_5
    show jin_glasses at p5_5
    show jin talk2 at p5_5
    with move

    play sound sfx_dooropen
    show jin_sleep at left
    show jin_glasses at left
    show jin talk2 at left
    with move

    show yoshi_autumn at center
    show yoshi norm1 at center
    show goro_autumn at right
    show goro norm1 at right
    with dissolve

    if g3_room == True:
        show jin happy1 at left
        voice audio.jin_v_greet1b3
        j "Ah! Hello, you two!"

        show yoshi talk1 at center
        voice audio.yoshi_v_jin1
        yo "Hello, Jin! We were coming to see if you’d gotten out into the hotel yet."

        hide goro_autumn
        hide goro norm1
        show goro2_autumn at right
        show goro2 talk2 at right
        voice audio.goro_v_annoyed2b1
        g "Guess the answer is no."

        show jin awkward3 at left
        voice audio.jin_v_conj1c1
        j "A-Actually, I did try and tag along with Lloyd and Darius to the bathhouse earlier…!"

        hide goro2_autumn
        hide goro2 talk2
        show goro_autumn at right
        show goro play2 at right
        voice audio.goro_v_heh1a
        g "That sounds like something you’d be more interested in."

        show jin sigh1 at left
        voice audio.jin_v_yeah2c
        j "I-I thought so too, but it definitely got too hot and heavy in there for me to handle…"

        show yoshi comp3 at center
        voice audio.yoshi_v_aww1
        yo "Aww, Jin! You know you’re supposed to wait a while to adjust before pulling out."

        hide goro_autumn
        hide goro play2
        show goro2_autumn at right
        show goro2 relief2 at right
        voice audio.goro_v_agree1a2
        g "Yes, Jin. You’re supposed to take it slow – if you go too fast, it can be painful."

        show jin shy3 at left
        voice audio.jin_v_gulp1a
        j "*gulp*"

        show yoshi explain2 at center
        voice audio.yoshi_v_ehem1b
        yo "*ehem* Anyway, are you alright in here by yourself? "
    else:
        show yoshi talk1 at center
        voice audio.yoshi_v_jin1
        yo "Hey there, Jin! "

        show jin happy1 at left
        voice audio.jin_v_greet1b3
        j "A-Ah, hey guys, please come in!"

        show yoshi talk3 at center
        voice audio.yoshi_v_greet2a1
        yo "I hope we didn’t bother you!"

        show jin comp3 at left
        voice audio.jin_v_denial2b1
        j "N-Not at all! I was just resting!"

        hide goro_autumn
        hide goro norm1
        show goro2_autumn at right
        show goro2 confused2 at right
        voice audio.goro_v_really4a
        g "Have you been in here since yesterday? "

        show jin comp6 at left
        voice audio.jin_v_yessir3a
        j "Y-Yes, sir. Guilty as charged."

        show goro2 explain2 at right
        voice audio.goro_v_annoyed2b1
        g "Today’s the last day of vacation, are you not planning to go explore around the hotel at all?"

        show jin shy3 at left
        voice audio.jin_v_no2a
        j "No, sir…"

        show yoshi confused2 at center
        voice audio.yoshi_v_unsure2a
        yo "Are you alright in here by yourself? "

    show jin talk2 at left
    voice audio.jin_v_yes4b
    j "O-Oh, yes, I’m totally fine! This place is a little out of my element, anyway…"

    hide goro2_autumn
    hide goro2 explain2
    hide goro2 relief2
    show goro_autumn at right
    show goro talk3 at right
    voice audio.goro_v_well1a
    g "Well, I hope you don’t mind if we hang out here with you then."

    show jin talk4 at left
    voice audio.jin_v_no1b
    j "O-Oh no, sir…! I wouldn’t want you guys to miss out on all the fun stuff around the hotel! "

    show yoshi comp2 at center
    voice audio.yoshi_v_comp2
    yo "It’s fine! We needed to rest a little anyways!"

    show goro confused3 at right
    voice audio.goro_v_jin5a
    g "What do you usually do for fun though, Jin?"

    show jin daydream2 at left
    voice audio.jin_v_laugh2c
    j "I-It depends… I have several definitions of fun..."

    show yoshi explain2 at center
    voice audio.yoshi_v_well3
    yo "W-Well, I remember that you enjoy the same stuff as Yuri. But is there something else that maybe… you know? We could do together?"

    show jin fudan1 at left
    voice audio.jin_v_gulp1a
    j "*gulp*"

    hide goro_autumn
    hide goro confused3
    show goro2_autumn at right
    show goro2 play3 at right
    voice audio.goro_v_laugh2b1
    g "Hehe… Careful with your phrasing, Yoshinori. You’re giving Jin a different idea."

    hide yoshi_autumn
    hide yoshi explain2
    show yoshi2_autumn at center
    show yoshi2 shock2 at center
    voice audio.yoshi_v_what3
    yo "Wh-Wha?"

    show goro2 tease2 at right
    voice audio.goro_v_sorry2a1
    g "Sorry about Yoshinori here, I don’t think he’s fully gotten his mind off of a certain ‘event’ yesterday."

    show jin perv2 at left
    voice audio.jin_v_fudan1a2
    j "Oh my…"

    hide yoshi2_autumn
    hide yoshi2 shock2
    show yoshi_autumn at center
    show yoshi awkward3 at center
    voice audio.yoshi_v_think4
    yo "H-How about we do something with your computer, Jin?! You use that for fun too, right?"

    show jin scheme4 at left
    voice audio.jin_v_yes1c
    j "Yes, I read my BL there."

    show yoshi tired4 at center
    voice audio.yoshi_v_sigh3a
    yo "Okay, I give up…"

    show jin thinkdn2 at left
    voice audio.jin_v_conj2c1
    j "W-Well, I also play games and watch anime on it, if that’s the answer you’re looking for…"

    show yoshi comp3 at center
    voice audio.yoshi_v_yeah4
    yo "Y-Yeah! Why don’t we do that?"

    show jin talk5 at left
    voice audio.jin_v_conj1b1
    j "Oh! Actually, we could continue with that journal project maybe? I had a lot of fun last time we did it together!"

    hide goro2_autumn
    hide goro2 tease2
    show goro_autumn at right
    show goro happy2 at right
    voice audio.goro_v_alright1a1
    g "Sure. I don’t mind telling you another story."

    # JMG2
    $renpy.choice_for_skipping()
    scene cg white with Dissolve(2.0)
    $ quick_menu = False
    $ say_box = False
    hide screen location
    hide screen timeline
    hide screen quick_menu
    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    $ global minigame_id
    $ minigame_id = 'jmG2'
    if day4_goro_choice == False:
        $ renpy.call(minigame_id, 'day')
    else:
        $ renpy.call(minigame_id, 'sunset')

label day4_goro_postmg:

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

    $ location = location_office
    $ day = "??"
    $ time = timeline_timeday
    $ season = season_summer
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_office_past_day with fade
    play music where_am_i loop

    show ygoro_camp at left2
    show ygoro awkward1 at left2
    show vera_casual at right2
    show vera talk1 at right2
    voice audio.vera_vsg142_line1
    v "I’m off.  I’ll be back next week."

    show ygoro awkward2 at left2
    voice audio.ygoro_vsg142_line1
    g "You’re heading out again?"

    show vera annoy2 at right2
    voice audio.vera_vsg142_line2
    v "There’s nothing for me to do here. You can’t expect me to sit around here and watch you play house with a bunch of scouts."

    show ygoro annoy2 at left2
    voice audio.ygoro_vsg142_line2
    g "But today is…"

    show ygoro disappoint1 at left2
    voice audio.ygoro_vsg142_line3
    g "Tch…"

    show vera annoy3 at right2
    voice audio.vera_vsg142_line3
    v "What? Why are you giving me that face?"

    show ygoro angry3 at left2
    voice audio.ygoro_vsg142_line4
    g "I don’t understand why you hate making time for us."

    show vera annoy2 at right2
    voice audio.vera_vsg142_line4
    v "Am I not here right now? I stayed here all day yesterday, and what did you and Yuri have me do? Nothing!"

    voice audio.vera_vsg142_line5
    v "And you have the nerve to say that I don’t make time?!"

    show vera angry2 at right2
    voice audio.vera_vsg142_line6
    v "And you’re one to talk, ever since you built this stupid camp!"

    voice audio.vera_vsg142_line7
    v "You quit your job and put all your savings into this without me knowing, and now you expect me to play along and act as if everything is perfect?!"

    show ygoro rage1 at left2
    voice audio.ygoro_vsg142_line5
    g "You know I did this for Yuri! I did it for us!"

    show vera rage4 at right2
    voice audio.vera_vsg142_line8
    v "Oh, don’t give me that bullshit! Why can’t you admit that the real reason you’re doing this is only for yourself?!"

    show ygoro panic2 at left2
    voice audio.ygoro_vsg142_line6
    g "Wh-What…?"

    show vera angry6 at right2
    voice audio.vera_vsg142_line9
    v "You’re obsessed with reliving your younger days and being the boss."

    voice audio.vera_vsg142_line10
    v "Why can’t I go out and do what I want then?!"

    show vera rage4 at right2
    voice audio.vera_vsg142_line11
    v "You’ve already taken so much of my youth away from me! You knew I never wanted any of this!"

    voice audio.vera_vsg142_line12
    v "I agreed to keep that child, but you know I never wanted to be a mother, and I should never have agreed to be your wife!"

    show ygoro angry4 at left2
    voice audio.ygoro_vsg142_line7
    g "But we did it, Vera! We’re married! We made our vows!"

    show vera rage6 at right2
    voice audio.vera_vsg142_line13
    v "Screw that! I did my part!! Our daughter’s old enough, what else do you want from me?!"

    voice audio.vera_vsg142_line14
    v "You’ve gotta know at this point that we’re just dragging this out. "

    show vera rage5 at right2
    voice audio.vera_vsg142_line15
    v "Eighteen. YEARS. We’re both sick of it!"

    show ygoro awkward5 at left2
    g "..."

    show vera eyeroll5 at right2
    voice audio.vera_vsg142_line16
    v "Tsk."

    hide vera_casual
    hide vera eyeroll5
    with dissolve

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    show ygoro angry4 at left2
    voice audio.ygoro_vsg142_line8
    g "Vera, wait—!"

    play sound sfx_doorslam
    show ygoro disappoint3 at left2
    voice audio.ygoro_vsg142_line9
    g "Ah, shit…"

    $ renpy.pause (1.0, hard=True)
    play music old_familiar_home_slow loop
    play sound sfx_doorknock
    $ renpy.pause (1.0, hard=True)
    show ygoro disappoint2 at left2
    voice audio.ygoro_v_ehem1a
    g "*ehem* Come in!"

    show yyoshi_camp at right2
    show yyoshi worry2 at right2
    with dissolve

    voice audio.yyoshi_v_awkward1
    yo "Umm… Sir Goro?"

    show ygoro talk3 at left2
    voice audio.ygoro_v_shock1a
    g "Ah, Yoshinori! What brings you here?"

    show yyoshi upset6 at right2
    voice audio.yyoshi_v_well3
    yo "W-Well… I was waiting by the door until Ms. Vera walked out… "
    yo "Are you okay…?"

    show ygoro sigh1 at left2
    voice audio.ygoro_v_sorry2a
    g "Ah, I’m sorry you had to hear that. But yes, I’m quite alright."

    show yyoshi worry4 at right2
    voice audio.yyoshi_v_but2a
    yo "I-I know it’s not my place, sir, but… if you need someone to talk to, I’m always here!"
    yo "I might have no experience as a camp leader, father, or a husband, but… I’ll try my best to listen and understand!"

    show ygoro comp2 at left2
    voice audio.ygoro_v_laugh1a
    g "H-Hehe… You’re as innocent as ever, Yoshinori, but you always mean well."
    g "Either way, I appreciate your offer. I won’t forget it."

    show yyoshi comp2 at right2
    voice audio.yyoshi_v_confident2
    yo "We’re your family too, sir!"

    show ygoro comp6 at left2
    voice audio.ygoro_v_heh1a
    g "Heh… Never imagined I’d be hearing all this from a scout… But you’re right."

    show yyoshi shock3 at right2
    voice audio.yyoshi_v_really3
    yo "Wah, really?!"

    show ygoro happy2 at left2
    voice audio.ygoro_v_agree1a2
    g "Yes, really. Who knew we’d get along so well, right?"

    show yyoshi happy2 at right2
    voice audio.yyoshi_v_yessir2a
    yo "Yes, sir!"

    show ygoro confused2 at left2
    voice audio.ygoro_v_anyway1
    g "Anyway, did you need anything from me?"

    show yyoshi bold2 at right2
    voice audio.yyoshi_v_awkward1
    yo "Umm… Yes! I need you to come to the mess hall with me, sir!"

    show ygoro confused3 at left2
    voice audio.ygoro_v_what1a
    g "What for?"

    show yyoshi bold5 at right2
    voice audio.yyoshi_v_confident4
    yo "You’ll see!"

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

    $ location = location_messhall
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_messhall_past_day_celebration with fade

    show andre_camp at p7_1
    show andre norm1 at p7_1
    show yaiden_casual at p7_2
    show yaiden norm1 at p7_2
    show ygoro_camp at p7_4
    show ygoro explain2 at p7_4
    show yyoshi_camp at p7_3
    show yyoshi norm1 at p7_3
    show yyuri_camp at p7_5
    show yyuri excited1 at p7_5
    show ylloyd_camp at p7_6
    show ylloyd norm1 at p7_6
    show ydarius_camp at p7_7
    show ydarius norm1 at p7_7
    voice audio.ygoro_v_unsure1b1
    g "Do I really have to close my eyes?"

    show yyoshi bold2 at p7_3
    voice audio.yyoshi_v_alright2
    yo "You can open them now, sir!"

    show cg_fade at truecenter
    show mgg2 1 at fx_pos
    with dissolve

    play sound sfx_partypopper
    play music buddy_oath_hotel loop
    voice audio.all_vsg14_line1
    all "HAPPY BIRTHDAY!"

    voice audio.yyuri_vsg14_line1
    yu "To the bestest dad and scoutmaster ever! "

    voice audio.yyuri_vsg14_line2
    yu "You didn’t think I’d forget, did you Dad?! It’s been so hard pretending all morning!"

    voice audio.yyuri_vsg14_line3
    yu "It was Yoshinori’s idea to throw you a party, though!"

    voice audio.yyoshi_vsg14_line1
    yo "Oh, but everyone worked hard on the decorations! And of course, Mr. Andre and Aiden cooked all the food!"

    voice audio.andre_vsg14_line1
    u "We cooked all your favorites, sir."

    voice audio.ylloyd_vsg14_line1
    l "We weren’t sure how old you were, so we just had each scout stick a candle in there!"

    voice audio.ydarius_vsg14_line1
    d "He’s only thirty-eight."

    show mgg2 2 with Dissolve(0.25)
    voice audio.ygoro_vsg14_line1
    g "Thank you, everyone."

    voice audio.yyoshi_vsg14_line2
    yo "No, thank you, sir! If you didn’t build Camp Buddy, we wouldn’t have the greatest summer ever! "

    voice audio.yyuri_vsg14_line4
    yu "Awwww~ You made Dad cry, Yoshi!"

    voice audio.ygoro_vsg14_line2
    g "N-No, some confetti just got in my eye…!"

    voice audio.yaiden_vsg14_line1
    a "Hurry up, blow the candles off your fire-cake already!"

    hide screen location
    hide screen timeline
    hide screen quick_menu
    $quick_menu = False
    scene cg white with Dissolve(2.0)
    $past_scene = False

label day4_goro_postfb:

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black
    hide screen location
    hide screen timeline
    hide screen quick_menu
    $quick_menu = False
    with fade
    play music here_they_come loop
    $ renpy.pause (2.0, hard=True)

    if day4_goro_choice == False:
        $ day = "79"
        $ time = timeline_timeday
        $ season = season_winter
        $ location = location_hotelroom
        show screen location
        show screen timeline
        show screen quick_menu
        $quick_menu = True
        scene bg_hotel_room2_day with fade
    else:
        $ location = location_hotelroom
        $ day = "79"
        $ time = timeline_timesunset
        $ season = season_winter
        show screen location
        show screen timeline
        show screen quick_menu
        $quick_menu = True
        scene bg_hotel_room2_sunset with fade

    show jin_sleep at left
    show jin_glasses at left
    show jin comp2 at left
    show yoshi_autumn at center
    show yoshi comp1 at center
    show goro_autumn at right
    show goro comp1 at right
    voice audio.jin_v_aww2a1
    j "Aww… It’s so sweet everyone threw you a party, Sir Goro!"

    show goro comp2 at right
    voice audio.goro_v_thanks2b1
    g "The credit goes to Yoshinori. He was quite the thoughtful scout, you know."

    hide yoshi_autumn
    hide yoshi comp1
    show yoshi2_autumn at center
    show yoshi2 comp5 at center
    voice audio.yoshi_v_laugh6
    yo "Ahehe… It’s really nothing, sir.."

    show jin talk2 at left
    voice audio.jin_v_conj4a1
    j "A-Anyway, I really appreciate you guys’ company, and for helping me out with the blog project…"

    hide yoshi2_autumn
    hide yoshi2 comp5
    show yoshi_autumn at center
    show yoshi talk3 at center
    voice audio.yoshi_v_unsure2a
    yo "Are you sure you don’t want to come with us and tour the hotel some?"

    show jin comp3 at left
    voice audio.jin_v_comp1b1
    j "No thanks, I think I’ll keep working on this for a little while longer!"

    show goro talk1 at right
    voice audio.goro_v_well1a
    g "Well, if that’s the case, we’ll be on our way, Jin."
    g "As long as you’re enjoying this vacation, then that’s what matters."

    show jin comp6 at left
    voice audio.jin_v_thanks1c1
    j "Th-Thank you, sir!"

    hide goro_autumn
    hide goro talk1
    show goro2_autumn at right
    show goro2 play2 at right
    voice audio.goro_v_but1a
    g "But one of these days, you’re going to come with us and we’re going to party. And that’s an order!"

    show jin comp5 at left
    voice audio.jin_v_yessir2a
    j "Yes, sir…!"

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black with fade

    if day4_goro_choice == False:
        $ day4_goro_choice = True
        yo "{i}Eventually, we decided to get out and explore another area of the hotel!{/i}"
        scene cg black
        hide screen location
        hide screen timeline
        hide screen quick_menu
        $quick_menu = False
        with fade
        $ time_transition_day_to_sunset_winter()
        $ time = timeline_timesunset
        $ renpy.pause (2.0, hard=True)
        $say_box = False
        $mm_talking = False
        $renpy.choice_for_skipping()
        show screen minimap()
        $ renpy.pause (hard=True)

    else:
        yo "{i}Eventually, we decided to head back to our room for the night.{/i}"
        scene cg black
        hide screen location
        hide screen timeline
        hide screen quick_menu
        $quick_menu = False
        with fade
        $ time_transition_sunset_to_night_winter()
        $ renpy.pause (2.0, hard=True)
        jump day4_goro_after

label day4_goro_after:
    $ time = timeline_timenight
    $say_box = True
    $ location = location_hotelroom
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_hotel_room1_night with fade
    play music close_distance loop

    show yoshi_sleep at right2
    show yoshi relief2 at right2
    show goro_sleep at left2
    show goro norm2 at left2
    voice audio.yoshi_v_relief1
    yo "Phew, today was jam-packed again!"

    show goro laugh2 at left2
    voice audio.goro_v_laugh1a1
    g "Haha, true. But we somehow finished touring around even earlier than yesterday, so there’s still a few hours left before bed."

    show yoshi comp2 at right2
    voice audio.yoshi_v_yeah1
    yo "Yeah, although I’m not sure how much more I’m up for, haha!"

    show goro confused2 at left2
    voice audio.goro_v_conj6a1
    g "By the way, I know I’ve been pretty clear about how much I’ve enjoyed the trip so far, but how about you?"

    show yoshi bold2 at right2
    voice audio.yoshi_v_amazed3
    yo "I’m enjoying it just as much, sir! I never would’ve thought I’d be able to experience all this luxury in my life."

    show goro happy3 at left2
    voice audio.goro_v_agree5a1
    g "Haha, I could say the same. We get to live like millionaires for a few days. "

    hide yoshi_sleep
    hide yoshi bold2
    show yoshi2_sleep at right2
    show yoshi2 awkward4 at right2
    voice audio.yoshi_v_conj4a
    yo "Yeah… I had to look up how much it cost to book this place, and honestly it’s nowhere near what I can afford. "

    show goro explain2 at left2
    voice audio.goro_v_actually1a
    g "I was worried you might not enjoy it here as much because of that, knowing how you prefer simpler things. "
    g "But I’m glad that didn’t end up being the case."

    hide yoshi2_sleep
    hide yoshi2 awkward4
    show yoshi_sleep at right2
    show yoshi comp2 at right2
    voice audio.yoshi_v_well1
    yo "Well, it was only because I was with you, sir!"

    hide goro_sleep
    hide goro explain2
    show goro2_sleep at left2
    show goro2 comp3 at left2
    voice audio.goro_v_laugh2b1
    g "Hehe."
    g "It’s a shame we’re going to be checking out tomorrow."

    show yoshi shock2 at right2
    voice audio.yoshi_v_oh4
    yo "Oh, already?! Time’s moved so fast the past few days…"

    hide goro2_sleep
    hide goro2 comp3
    show goro_sleep at left2
    show goro happy2 at left2
    voice audio.goro_v_well1a
    g "Well, we can always go out again someday when we finish the project."
    g "Spending this vacation with you gave me some ideas of what we can do in the future. "

    show goro confused2 at left2
    voice audio.goro_v_but1a
    g "But I want to know, what is a perfect vacation to you?"

    $ working = False
    $ shuffle_menu()
    menu():
        g "But I want to know, what is a perfect vacation to you?{fast}"
        "Staycation.":
            $ working = True
            $ score_goro -= 1
            $ score_bot += 1
            show yoshi happy1 at right2
            voice audio.yoshi_v_sir1
            yo "I’m fine staying at Camp Buddy, sir! No need to go anywhere fancy!"

            show goro explain2 at left2
            voice audio.goro_v_well1a
            g "Well, it doesn’t have to be fancy. I’d really like to take you somewhere new!"
        "Hotel.":
            $ working = True
            $ score_goro -= 1
            $ score_top += 1
            show yoshi happy1 at right2
            voice audio.yoshi_v_sir1
            yo "Take me back here, sir!"

            g "Heh, you really like fancy living, huh?"

            show goro confused2 at left2
            voice audio.goro_v_alright1a1
            g "Sure, I’ll bring you back, but don’t you want to try something new?"
        "Roadtrip.":
            $ working = True
            $ score_goro += 1
            $ score_top += 1
            show yoshi happy1 at right2
            voice audio.yoshi_v_excited1
            yo "I think it’d be fun to drive around somewhere just exploring!"

            show goro play3 at left2
            voice audio.goro_v_laugh2b1
            g "Hehe, you know I’m into that."

            show yoshi laugh1 at right2
            voice audio.yoshi_v_yeah1
            yo "Yeah, we could even camp out, no need for fancy hotels!"
        "Travel.":
            $ working = True
            $ score_goro += 2
            $ score_bot += 1
            show yoshi happy1 at right2
            voice audio.yoshi_v_excited1
            yo "It’d be really exciting to travel the world with you, sir!"

            show goro happy3 at left2
            voice audio.goro_v_agree7a
            g "I agree. There’s so much out there to see."

            hide yoshi_sleep
            hide yoshi happy1
            show yoshi2_sleep at right2
            show yoshi2 comp6 at right2
            voice audio.yoshi_v_conj2a
            yo "I probably need to save a lot of money for that though."

    g "You don’t need to worry about the money. I’ll handle everything."

    hide yoshi_sleep
    hide yoshi laugh1
    hide yoshi happy1
    show yoshi2_sleep at right2
    show yoshi2 comp3 at right2
    voice audio.yoshi_v_comp3
    yo "Y-You don’t have to do that, sir."

    show goro comp2 at left2
    voice audio.goro_v_alright2c1
    g "I want to. The moments and memories are priceless."

    play sound sfx_doorknock
    $ renpy.pause (1.0, hard=True)
    show goro confused2 at left2
    voice audio.goro_v_oh3a
    g "Oh?"

    show goro_sleep at p5_1
    show goro confused1 at p5_1
    with move

    show yoshi2_sleep at p4_4
    show yoshi2 norm1 at p4_4
    show goro_sleep at p4_3
    show goro norm1 at p4_3
    with move

    show yuri_autumn at p4_2
    show yuri happy1 at p4_2
    show aiden_autumn at p4_1
    show aiden norm1 at p4_1
    with dissolve

    voice audio.yuri_v_hey2c
    yu "Hi Dad~!  "

    show aiden play2 at p4_1
    voice audio.aiden_v_perv1
    a "Hehe, hope we’re not interrupting anything spicy~"

    show goro talk3 at p4_3
    voice audio.goro_v_no2a1
    g "Not at all. What brings you two here? "

    hide yoshi2_sleep
    hide yoshi2 norm1
    show yoshi_sleep at p4_4
    show yoshi confused2 at p4_4
    voice audio.yoshi_v_wait4
    yo "Wait… What’s with all the luggage?"

    show yuri talk5 at p4_2
    voice audio.yuri_v_oh3a
    yu "Oh, the receptionist told us that we have a scheduled formal dinner tonight down at the restaurant."

    show yoshi awkward4 at p4_4
    voice audio.yoshi_v_amazed1c
    yo "Wow, and here I thought this trip couldn’t get any fancier."

    hide aiden_autumn
    hide aiden play2
    show aiden2_autumn at p4_1
    show aiden2 comp3 at p4_1
    voice audio.aiden_v_agree4a
    a "You’re telling me! Who knew they’d throw a fancy dinner at us to top off the trip?!"

    show yuri happy1 at p4_2
    voice audio.yuri_v_yeah1a1
    yu "Yeah, it was another surprise arrangement by Mr. Clermont."

    show yoshi shock2 at p4_4
    voice audio.yoshi_v_wait3b
    yo "W-Wait, did you say formal dinner, Yuri? I don’t think any of us packed appropriate clothing for something like this…"

    show yuri explain3 at p4_2
    voice audio.yuri_v_well1b
    yu "Well… Mr. Clermont expected that, so he made provisions for us."

    show yuri_autumn at center
    show yuri norm1 at center
    with move

    play sound sfx_clothesslam
    show yuri_autumn at p4_2
    show yuri talk1 at p4_2
    with move

    voice audio.yuri_v_here1a
    yu "Here, guys. The hotel staff delivered the invitations and something for each of us to wear! "

    hide goro_sleep
    hide goro talk3
    show goro2_sleep at p4_3
    show goro2 confused5 at p4_3
    voice audio.goro_v_isee3a
    g "Now it makes sense why Mr. Clermont was asking for our measurements a few weeks ago… "
    g "I guess he was collecting them to get these clothes made for us."

    show aiden2 worry2 at p4_1
    voice audio.aiden_v_sheesh2a
    a "Man, talk about being extra… am I right?"

    show yuri excited2 at p4_2
    voice audio.yuri_v_unsure1c1
    yu "I don’t know about you guys, but I won’t be saying no to a fancy dinner night~!  "

    hide yuri_autumn
    hide yuri excited2
    show yuri2_autumn at p4_2
    show yuri2 excited2 at p4_2
    voice audio.yuri_v_excited1b
    yu "I’ve always wanted to experience a top tier five-star dinner! I wonder if there’s gonna be some entertainment like a gala or a ball!"
    yu "Couples dancing to the music, sharing a glass of wine, and all the fancy food they can eat!"

    show yuri2 relief4 at p4_2
    voice audio.yuri_v_fujo1b1
    yu "So romantic~! "

    show goro2 bored1 at p4_3
    voice audio.goro_v_yuri7a
    g "Yuri… It’s fine dining. I don’t think there’s going to be any dancing involved."

    hide yuri2_autumn
    hide yuri2 relief4
    show yuri_autumn at p4_2
    show yuri excited2 at p4_2
    voice audio.yuri_v_laugh1a1
    yu "I’m still excited either way!"

    show yoshi confused3 at p4_4
    voice audio.yoshi_v_think1a
    yo "This invitation says our reservation is an hour from now."

    hide goro2_sleep
    hide goro2 bored1
    show goro_sleep at p4_3
    show goro talk3 at p4_3
    voice audio.goro_v_rush1c1
    g "Then we better start dressing up now, or we’ll be late."

    show yuri happy2 at p4_2
    voice audio.yuri_v_well1a
    yu "Well, you guys go ahead! Aiden and I have to go bring everyone their suits!"

    hide aiden2_autumn
    hide aiden2 worry2
    show aiden_autumn at p4_1
    show aiden happy1 at p4_1
    voice audio.aiden_v_alright1a1
    a "Let’s all just meet at the resto!"

    show goro talk4 at p4_3
    voice audio.goro_v_response2a1
    g "Sure thing."

    show yuri laugh1 at p4_2
    voice audio.yuri_v_bye2a
    yu "See you guys soon! Can’t wait to see your formal looks~!"

    hide yuri_autumn
    hide yuri laugh1
    hide aiden_autumn
    hide aiden happy1
    with dissolve

    show yoshi_sleep at right2
    show yoshi norm1 at right2
    show goro_sleep at left2
    show goro happy2 at left2
    with move

    voice audio.goro_v_yoshi2b
    g "I’ve always wanted to take you out on a dinner like this, Yoshinori."

    hide yoshi_sleep
    hide yoshi norm1
    show yoshi2_sleep at right2
    show yoshi2 comp6 at right2
    voice audio.yoshi_v_laugh6
    yo "Ahehe… I haven’t experienced anything like it before, so I’m counting on you to lead the way, sir."

    show goro laugh3 at left2
    voice audio.goro_v_amazed2b1
    g "What a perfect way to end our trip. I’m sure we’ll have an amazing night."

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

    $ location = location_restaurant
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_hotel_restaraunt_night with fade
    play bgsound sfxloop_crowd loop
    play music buddy_oath_hotel loop

    show yoshi_formal at left2
    show yoshi shock1 at left2
    show goro_formal at right2
    show goro shock2 at right2
    voice audio.goro_v_amazed1a1
    g "I should’ve expected this considering the rest of the hotel, but this place is just as extravagant…"

    show yoshi shock2 at left2
    voice audio.yoshi_v_amazed1a
    yo "Everywhere you look there’s gold and crystals… they’re almost blinding me."

    show goro happy1 at right2
    voice audio.goro_v_heh1a
    g "Luckily we had our suits provided for us. We blend right in."

    show yoshi comp6 at left2
    voice audio.yoshi_v_yeah1
    yo "Yeah… Even if I’d known about this, I doubt anything in my wardrobe would be fitting for tonight!"

    show goro play3 at right2
    voice audio.goro_v_well1a
    g "Well, you have been wearing suits lately thanks to all those meetings we attended together, but this is different. "
    g "You look dashing… and really handsome, I should say."

    show yoshi comp2 at left2
    voice audio.yoshi_v_thanks2
    yo "Ah… Thank you, sir. You look good as well…!"
    yo "A-And you smell very nice too…"

    show goro play5 at right2
    voice audio.goro_v_laugh2b1
    g "Hehe, I figured I’d wear my special cologne for this occasion."
    g "You’re not the only one paying attention, though. I see you’re wearing that brooch I gave you again."

    show yoshi bold2 at left2
    voice audio.yoshi_v_yessir1
    yo "Yes, sir. I thought it would match the style. It’s been a long time since I wore something this nice."
    yo "Business suits are one thing, but the last time I was in full formal wear was my prom."

    show goro relief2 at right2
    voice audio.goro_v_oh1a
    g "Oh, those days are so far behind me. You’re not making me feel any younger."

    show yoshi laugh2 at left2
    voice audio.yoshi_v_but1
    yo "But we do look good together, sir! Hahaha!"

    show goro play2 at right2
    voice audio.goro_v_heh3a
    g "Now we’re just buttering each other up. "

    show yoshi_formal at p4_1
    show yoshi norm1 at p4_1
    show goro_formal at p4_2
    show goro norm1 at p4_2
    with move

    show aiden_formal at p4_3
    show aiden norm1 at p4_3
    show yuri_formal at p4_4
    show yuri excited3 at p4_4
    with dissolve

    voice audio.yuri_v_greet2a
    yu "Hiii guuuys~!"
    yu "Oh wooow, don’t you two look classy?"

    show aiden play2 at p4_3
    voice audio.aiden_v_laugh1a2
    a "Yeaaah, it really ‘suits’ you guys well! Get it? Suit?"

    show yoshi amazed1 at p4_1
    voice audio.yoshi_v_hey1
    yo "Hey there, Yuri and Aiden! You both look amazing too!"

    show goro happy3 at p4_2
    voice audio.goro_v_yuridear1b
    g "Yes, you look beautiful, dear… You were still little the last time I saw you in a dress."

    show yuri comp4 at p4_4
    voice audio.yuri_v_thanks1a
    yu "Thanks, Dad! I do feel expensive and elegant, which is very unusual!"

    show goro play2 at p4_2
    voice audio.goro_v_aiden9b
    g "You’re looking dapper in that suit too, Aiden. I didn’t think formal would fit you so well."

    show aiden confused2 at p4_3
    voice audio.aiden_v_really1b
    a "Eh? Really?"

    show yoshi confused2 at p4_1
    voice audio.yoshi_v_actually1a
    yo "This might be the first time I’ve seen you this covered up, though."

    show aiden sigh4 at p4_3
    voice audio.aiden_v_agree4b
    a "I know, right Yoshi?! This suit and tie are so tight I feel like I can’t breathe!"

    show goro confused3 at p4_2
    voice audio.goro_v_oh3a
    g "Don’t you like the attire, Aiden?"

    show aiden comp2 at p4_3
    voice audio.aiden_v_comeon1a2
    a "Haha, come on, you guys know me – I’d rather be in loose clothes or nothing at all!"
    a "This is way out of my usual comfort zone, but hey! If you guys think I look cool, then I’m fine with it! Plus, it’s not like I have to wear this forever."

    show yuri angry6 at p4_4
    voice audio.yuri_v_ugh3a
    yu "Ugh… Don’t get me started on how much these high heels hurt my feet! "

    show aiden laugh2 at p4_3
    voice audio.aiden_v_laugh2b1
    a "Hahaha! I can imagine!"

    show aiden_formal at p6_3
    show aiden norm1 at p6_3
    show yoshi_formal at p6_1
    show yoshi norm1 at p6_1
    show yuri_formal at p6_4
    show yuri norm1 at p6_4
    show goro_formal at p6_2
    show goro norm1 at p6_2
    with move

    show lloyd_formal at p6_5
    show lloyd talk2 at p6_5
    show darius_formal at p6_6
    show darius norm1 at p6_6
    with dissolve

    voice audio.lloyd_v_shock1a3
    l "Oh! There they are! "
    l "Looks like we’re late for the party, huh?"

    show yoshi happy2 at p6_1
    voice audio.yoshi_v_disagree4a
    yo "Not really! We just got here too!"

    show yuri confused2 at p6_4
    voice audio.yuri_v_lloyd5a
    yu "Lloyd… Um… Didn’t we give you a suit?"

    show lloyd worry2 at p6_5
    voice audio.lloyd_v_conj1c1
    l "W-Well… About that…"

    show darius play2 at p6_6
    voice audio.darius_v_conj2a
    d "It didn’t fit him."

    show lloyd panic2 at p6_5
    voice audio.lloyd_v_darius8c
    l "D-Dar! "

    show aiden laugh1 at p6_3
    voice audio.aiden_v_laugh2a1
    a "Haha! Why, is it like kid-size or something?"

    show lloyd shy2 at p6_5
    voice audio.lloyd_v_conj1c1
    l "W-Well, not really… It’s actually the opposite… "

    show goro confused2 at p6_2
    voice audio.goro_v_confused1a1
    g "It didn’t fit…? I could’ve sworn I’ve gotten your measurements before, right…?"

    show lloyd shy6 at p6_5
    voice audio.lloyd_v_conj4c1
    l "Hehe… you did… but… It’s a funny story really, you guys don’t have to—"

    show darius bored2 at p6_6
    voice audio.darius_v_laugh1
    d "He lied to oversell his size."
    d "Now everything is too long and baggy for him."

    show lloyd tired5 at p6_5
    voice audio.lloyd_v_darius6a
    l "Dar… you didn’t have to put it so bluntly…"

    show aiden think2 at p6_3
    voice audio.aiden_v_actually3a
    a "To be fair, I just thought they were for camp records too when we got asked…"

    show lloyd angry2 at p6_5
    voice audio.lloyd_v_groan2a2
    l "Right?! I thought it was for like a physical checkup or something!"

    show goro talk3 at p6_2
    voice audio.goro_v_actually1a
    g "I didn’t know the reason Mr. Clermont asked for our measurements too, but I didn’t question it."

    show yoshi comp3 at p6_1
    voice audio.yoshi_v_well1
    yo "Well, it’s a good thing you had something semi-formal… You still look nice nonetheless! "

    show lloyd sigh4 at p6_5
    voice audio.lloyd_v_agree2a1
    l "Yeah, luckily Darius’ attire came with these suspenders he didn’t need since he’s wearing a closed suit."
    l "But still…"

    show lloyd sigh1 at p6_5
    voice audio.lloyd_v_sigh2a
    l "*sigh* I look like a dork compared to you guys…"

    show darius comp5 at p6_6
    voice audio.darius_v_cute1
    d "I like your bowtie. It’s cute."

    show goro happy2 at p6_2
    voice audio.goro_v_oh1a
    g "Oh. Maybe this will help out."

    show goro_formal at p6_5
    show goro happy2 at p6_5
    with move

    hide lloyd_formal
    hide lloyd sigh1
    show lloyd_formal2 at p6_5
    show lloyd sigh1 at p6_5
    with dissolve

    show goro_formal at p6_2
    show goro bold2 at p6_2
    with move

    voice audio.goro_v_comp2a1
    g "I have a brooch that’s perfect for the occasion. It’s not much, but it’ll help a little bit."

    show lloyd amazed3 at p6_5
    voice audio.lloyd_v_amazed1a4
    l "Oh wow! Thank you, Sir Goro! "

    show yuri comp2 at p6_4
    voice audio.yuri_v_aww3a
    yu "Aww, look at that~! It kinda looks like a dad sending his son off to prom~"

    show darius laugh3 at p6_6
    voice audio.darius_v_amazed2
    d "It looks good on you, Lloyd."

    show lloyd think2 at p6_5
    voice audio.lloyd_v_unsure1a2
    l "I guess it is better… But I still look like your secretary or something, Dar…"

    show aiden happy3 at p6_3
    voice audio.aiden_v_yeah1a1
    a "Yeah, Darius looks like he’s a mob boss or something! "

    show goro play3 at p6_2
    voice audio.goro_v_heh1a
    g "He does look rather imposing… But in a good way…"

    show yoshi comp2 at p6_1
    voice audio.yoshi_v_unsure1b
    yo "Maybe if you wipe that blank look and smile more you’d be less intimidating?"

    show darius annoy2 at p6_6
    voice audio.darius_v_no1a
    d "No."

    show lloyd happy2 at p6_5
    voice audio.lloyd_v_agree2b1
    l "Try it, Dar! We wanna see! "

    show darius grin3 at p6_6
    d "..."

    show aiden comp2 at p6_3
    voice audio.aiden_v_oh4a
    a "Oh… Well… I guess we can work on that one…"

    show yuri bold2 at p6_4
    voice audio.yuri_v_praise5a
    yu "There’s nothing wrong with Darius’ expressions! Honestly, his blank face is a lot more mysterious and attractive to some people!"

    show darius happy1 at p6_6
    voice audio.darius_v_conj1a1
    d "I kind of like looking scary. "
    d "Maybe people will think twice before making fun of Lloyd’s bowtie."

    show lloyd sigh5 at p6_5
    voice audio.lloyd_v_darius8a
    l "You’re the one who made fun of it back in the room, Dar."

    show darius laugh3 at p6_6
    voice audio.darius_v_laugh2a
    d "Hehe."

    show yoshi think2 at p6_1
    voice audio.yoshi_v_anyway2
    yo "By the way, aren’t we missing someone from your group…?"

    show yoshi_formal at p7_1
    show yoshi norm1 at p7_1
    show goro_formal at p7_2
    show goro play3 at p7_2
    show aiden_formal at p7_3
    show aiden comp2 at p7_3
    show yuri_formal at p7_4
    show yuri bold2 at p7_4
    show lloyd_formal2 at p7_5
    show lloyd sigh5 at p7_5
    show darius_formal at p7_6
    show darius norm1 at p7_6
    with move

    show jin_formal at p7_7
    show jin awkward4 at p7_7
    with dissolve

    voice audio.jin_v_sorry1a2
    j "W-Wahh… I’m here! Sorry I’m late, guys…!"

    show aiden shock2 at p7_3
    voice audio.aiden_v_shock1d1
    a "Whoa! Jin you look so… different! "

    show yuri amazed3 at p7_4
    voice audio.yyuri_v_kyaa1
    yu "Kyaaa!! Look at you! You look like a pop idol!"
    yu "Who knew that cutie Jin can look as handsome as this?"

    show goro play2 at p7_2
    voice audio.goro_v_laugh2a
    g "Jin already has a good-looking face to begin with. This just shows his full potential."

    show jin laugh3 at p7_7
    voice audio.jin_v_laugh3a
    j "Hehehe… I really don’t groom myself at all… But thanks, you guys."

    show lloyd talk1 at p7_5
    voice audio.lloyd_v_jin2b
    l "It’s about time you joined the party, Jin! When we left you were still in the shower!"
    l "We were actually worried for a bit! You looked like you didn’t wanna come!"

    show jin scared2 at p7_7
    voice audio.jin_v_sorry1d1
    j "S-Sorry… I take a long time to get ready… Especially for a special occasion…"
    j "It’s rare that I attend events like this, and even rarer with a group of friends…"

    show yuri comp2 at p7_4
    voice audio.yuri_v_jin5b
    yu "Aww, are you still feeling nervous, Jin?"

    show jin comp3 at p7_7
    voice audio.jin_v_conj1c1
    j "A little bit, I only came because all of you were here."

    show yoshi comp2 at p7_1
    voice audio.yoshi_v_comp5
    yo "Don’t worry, Jin. I’m sure all of us will have a good time tonight!"

    show jin comp2 at p7_7
    voice audio.jin_v_yeah2a
    j "Yeah… I’d like to be less of a shut-in. Especially when it comes to spending time with you guys."
    j "This is the perfect chance for me to—"

    show yoshi_formal at p8_1
    show yoshi shock1 at p8_1
    show goro_formal at p8_2
    show goro shock1 at p8_2
    show aiden_formal at p8_3
    show aiden shock1 at p8_3
    show yuri_formal at p8_4
    show yuri comp2 at p8_4
    show lloyd_formal2 at p8_5
    show lloyd shock1 at p8_5
    show darius_formal at p8_6
    show darius shock4 at p8_6
    show jin_formal at p8_7
    show jin shock1 at p8_7
    show emilia_formal at p8_8
    show emilia bold3 at p8_8
    with vpunch

    voice audio.emilia_v_laugh1a
    e "MAKE WAY! MAKE WAY! The queen of the night has arrived! "

    show yuri annoy2 at p8_4
    voice audio.yuri_v_ugh3a
    yu "Ugh…"

    show emilia_formal at p8_2
    show emilia bold3 at p8_2
    show goro_formal at p8_3
    show goro flat1 at p8_3
    show aiden_formal at p8_4
    show aiden awkward1 at p8_4
    show yuri_formal at p8_5
    show yuri pout2 at p8_5
    show lloyd_formal2 at p8_6
    show lloyd awkward2 at p8_6
    show darius_formal at p8_7
    show darius disgust1 at p8_7
    show jin_formal at p8_8
    show jin shy3 at p8_8
    with move

    all "..."

    show emilia annoy5 at p8_2
    voice audio.emilia_v_well2
    e "Well?! Not even one compliment? I didn’t put on a lovely dress just to be ignored!"

    show yoshi awkward3 at p8_1
    voice audio.yoshi_v_uh1a
    yo "Y-You look stunning, Emilia…"

    show emilia bold5 at p8_2
    voice audio.emilia_v_laugh3b
    e "*chuckles* I know~"
    e "I was pleasantly surprised to find out Mr. Clermont arranged a fine dining experience for us tonight! Truly such a treat~!"

    show emilia bold2 at p8_2
    voice audio.emilia_v_sigh2b
    e "It’s been a hot minute since my last one! But better late than never!"

    show yuri confused2 at p8_5
    voice audio.yuri_v_wait1a1
    yu "Wait… that’s not the dress we gave you."

    show emilia play2 at p8_2
    voice audio.emilia_v_bossy5a
    e "Why of course I brought my own attire!"
    e "Dress to impress, after all! I wouldn’t be caught dead wearing a free tacky dress, unlike someone~"

    show yuri angry3 at p8_5
    voice audio.yuri_v_request3a
    yu "Listen here, you—"

    show yoshi confused2 at p8_1
    voice audio.yoshi_v_think3
    yo "Would you like me to call for the staff to take your feathers and purse? Just so you’d be more comfortable before our meal."

    show emilia play5 at p8_2
    voice audio.emilia_v_thanks1b
    e "No, thank you! Like they say, beauty is pain~"
    e "The gown? Cucci! The feather? Verse-ace! The shoes? Louis Butt-on! The jewelry? Stiffany & Ho!"

    show emilia laugh1 at p8_2
    voice audio.emilia_v_amazed1a
    e "All custom made for me!"

    show yuri annoy4 at p8_5
    voice audio.yyuri_v_hmph1a
    yu "For the small price of two kidneys I bet."

    show yoshi irked1 at p8_1
    voice audio.yoshi_v_yuri4
    yo "Hush, Yuri…!"

    show emilia evil2 at p8_2
    voice audio.emilia_v_laugh3a
    e "Teehee~ It’s no surprise anyone would be jealous. I mean… who wouldn’t be over someone like me?"
    e "Now! Where are we supposed to sit? Shouldn’t we be getting served right about now?"

    show emilia rage4 at p8_2
    voice audio.emilia_v_waiter1
    e "WAITER!"

    show yoshi_formal at p9_2
    show yoshi shock1 at p9_2
    show emilia_formal at p9_3
    show emilia irked5 at p9_3
    show goro_formal at p9_4
    show goro annoy1 at p9_4
    show aiden_formal at p9_5
    show aiden shock1 at p9_5
    show yuri_formal at p9_6
    show yuri annoy1 at p9_6
    show lloyd_formal2 at p9_7
    show lloyd awkward2 at p9_7
    show darius_formal at p9_8
    show darius disgust1 at p9_8
    show jin_formal at p9_9
    show jin shy3 at p9_9
    with move

    show reimond_waiter at p9_1
    show reimond shock1 at p9_1
    with dissolve

    voice audio.emilia_v_request4a
    e "You! Aren’t you gonna show us our table?! Don’t you know that we’re VIP guests here?!"

    show reimond sad2 at p9_1
    voice audio.reimond_v_ah1a
    r "A-Ah… I was just waiting for you to gather up your party, madam…"

    show emilia irked2 at p9_3
    voice audio.emilia_v_hmph1a
    e "That should’ve been obvious upon my arrival! Now, show me to the best seat in here!"

    show reimond talk2 at p9_1
    voice audio.reimond_v_rush1a1
    r "Reservations for Clermont Inc., yes? Right this way, everyone."

    show jin_formal at p9_2
    show jin shy3 at p9_2
    show yuri_formal at p9_3
    show yuri annoy4 at p9_3
    show goro_formal at p9_4
    show goro talk2 at p9_4
    show yoshi_formal at p9_5
    show yoshi irked1 at p9_5
    show aiden_formal at p9_6
    show aiden shock1 at p9_6
    show emilia_formal at p9_7
    show emilia irked5 at p9_7
    show darius_formal at p9_8
    show darius disgust1 at p9_8
    show lloyd_formal2 at p9_9
    show lloyd awkward2 at p9_9
    with move

    show reimond explain2 at p9_1
    voice audio.reimond_v_ehem1a
    r "*ehem*"

    show reimond happy1 at p9_1
    voice audio.reimond_v_goodpm2a2
    r "Good evening, ladies and gentlemen! Welcome to The Glory Whole! My name is Reimond, and I will be taking care of you for the evening!"
    r "Please make yourselves comfortable while I get everyone a menu. "

    hide reimond_waiter
    hide reimond happy1
    with dissolve

    show jin_formal at p8_1
    show jin shy3 at p8_1
    show yuri_formal at p8_2
    show yuri excited3 at p8_2
    show goro_formal at p8_3
    show goro talk2 at p8_3
    show yoshi_formal at p8_4
    show yoshi irked1 at p8_4
    show aiden_formal at p8_5
    show aiden shock1 at p8_5
    show emilia_formal at p8_6
    show emilia irked5 at p8_6
    show darius_formal at p8_7
    show darius disgust1 at p8_7
    show lloyd_formal2 at p8_8
    show lloyd awkward2 at p8_8
    with move

    voice audio.yuri_v_omg1a
    yu "OMG, OMG, OMG, it’s finally happening~!!"

    show aiden confused3 at p8_5
    voice audio.aiden_v_think1a2
    a "I wonder what kind of food we’ll have here? Probably nothing I could ever make back at camp!"

    show lloyd excited3 at p8_8
    voice audio.lloyd_v_unsure1a1
    l "Maybe it’ll be something like you see on Food TV Shows!"

    show darius explain3 at p8_7
    voice audio.darius_v_confused1a
    d "Like Masterbaste Chef?"

    show yoshi excited1 at p8_4
    voice audio.yoshi_v_excited1
    yo "Either way I think it’s gonna be quite the experience! "

    show jin shock2 at p8_1
    voice audio.jin_v_whoa3a
    j "Th-They weren’t kidding when they said we’re going to be treated like royalty here…We have all these staff doing everything for us."

    show aiden awkward2 at p8_5
    voice audio.aiden_v_yeah1c1
    a "Yeah, I’m not used to it either. It’s usually me who does stuff like that."

    show yoshi confused2 at p8_4
    voice audio.yoshi_v_right1
    yo "I’m guessing this is going to be a first for most of us, right?"

    show emilia bold5 at p8_6
    voice audio.emilia_v_disagree2a1
    e "Kindly exclude me from that list. I’m very much used to this kind of setting."
    e "I’ve taken special lessons on fine dining etiquette from a young age, after all~"

    show yuri angry3 at p8_2
    voice audio.yuri_v_no2a1
    yu "You’re not the only one who’s tried this before. Right, Dad?"

    show goro explain2 at p8_3
    voice audio.goro_v_no2a1
    g "Well, not as frequently, dear. And it was usually for business appointments and not leisure dining like this."
    g "Although, it’s not unusual to feel intimidated by etiquette rules at first."

    show lloyd confused2 at p8_8
    voice audio.lloyd_v_conj1a3
    l "Well… most of them are common sense, but yeah, some rules are a little more nuanced, the fancier the place is."

    show darius confused2 at p8_7
    voice audio.darius_v_comp3a
    d "It’s not that hard, just don’t make a mess."

    show aiden confused2 at p8_5
    voice audio.aiden_v_confused1c1
    a "Ehh… Easy for you guys to say, I’ve been trying to figure out why there’s a big-ass napkin on my plate. Should I tuck it into my shirt or something?"

    show goro talk2 at p8_3
    voice audio.goro_v_no1a1
    g "No, Aiden. Just gently unfold it without shaking it out and place it on your lap."

    show aiden excited3 at p8_5
    voice audio.aiden_v_oho1a
    a "Oooh~ I felt fancy doing that~!"

    show emilia bold2 at p8_6
    voice audio.emilia_v_conj1b
    e "You should know there’s a secret language of the napkin that comes in handy when you need to excuse yourself from the table~"
    e "Leaving it on your chair will signal to the waiter that you’re not done with your meal, while leaving it neatly on the left-hand side of your plate will inform the waiter to clear your plate!"

    show aiden confused3 at p8_5
    voice audio.aiden_v_confused2a2
    a "The what goes to the what now…?"

    show goro comp2 at p8_3
    voice audio.goro_v_response3a1
    g "It’s fine, Aiden. I’ll teach you later."

    show jin worry4 at p8_1
    voice audio.jin_v_think2b1
    j "U-Umm… What about these extra spoons and forks? Will I get kicked out if I use the wrong one?"

    show emilia bold6 at p8_6
    voice audio.emilia_v_bossy4
    e "Since it sounds like everyone’s not that willing to learn, you can all just watch what I’m doing and follow~"

    show goro explain3 at p8_3
    voice audio.goro_v_actually1a
    g "Actually, there’s a simple trick to know which ones to use."
    g "Always start with the utensil farthest away from your plate, working your way towards the dinner plate as the courses progress."

    show jin think2 at p8_1
    voice audio.jin_v_agree3a1
    j "Ah, I see. I didn’t know it was that easy…"

    show yoshi happy2 at p8_4
    voice audio.yoshi_v_thanks4
    yo "Thanks for explaining, sir!"

    show emilia play2 at p8_6
    voice audio.emilia_v_sarcastic2b1
    e "Those are just the mere basics, though~ There are a lot more to consider especially once the meal has been served!"

    show emilia explain5 at p8_6
    voice audio.emilia_v_conj3a
    e "For example, did you know you’re not supposed to blow on your food to cool it off?  You’re supposed to wait at least a minute to let it cool down!"
    e "Pacing your eating is just as essential too! Smaller bites are encouraged even if it takes longer!"

    show emilia angry2 at p8_6
    voice audio.emilia_v_bossy1a
    e "And it’s very important to taste everything on your plate, even if you’re unsure you’ll like it!"
    e "Oh, and don’t forget noisy chewing and lip-smacking. That’s just disgustingly barbaric."

    show yuri annoy2 at p8_2
    voice audio.yuri_v_annoyed4a
    yu "Um. No one asked."

    show yoshi irked1 at p8_4
    voice audio.yoshi_v_yuri6
    yo "Y-Yuri…"

    show aiden scared2 at p8_5
    voice audio.aiden_v_hngh1b4
    a "Hngh… I feel like it’s starting to get complicated, though."

    show goro talk3 at p8_3
    voice audio.goro_v_response3a2
    g "It’s really not, Aiden. You just need to slow down and make less noise than usual. All of us can do that."
    g "And if there’s anything some of you aren’t sure of, you can always ask me."

    show goro happy2 at p8_3
    voice audio.goro_v_confident1a
    g "Otherwise, just follow my lead and everything will go smoothly."

    show emilia awkward2 at p8_6
    voice audio.emilia_v_what3a
    e "But that’s what I was sayi—"

    show jin_formal at p9_2
    show jin norm1 at p9_2
    show yuri_formal at p9_3
    show yuri norm1 at p9_3
    show goro_formal at p9_4
    show goro norm1 at p9_4
    show yoshi_formal at p9_5
    show yoshi norm1 at p9_5
    show aiden_formal at p9_6
    show aiden norm1 at p9_6
    show emilia_formal at p9_7
    show emilia annoy1 at p9_7
    show darius_formal at p9_8
    show darius norm1 at p9_8
    show lloyd_formal2 at p9_9
    show lloyd norm1 at p9_9
    with move

    show reimond_waiter at p9_1
    show reimond happy1 at p9_1
    with dissolve

    voice audio.reimond_v_here1b
    r "Sorry for the wait, here are your menus!"
    r "For tonight, we will be serving a three-course meal that includes an appetizer, a main, and a dessert!"

    show reimond happy3 at p9_1
    voice audio.reimond_v_request1a1
    r "Take a look at our menu to see what we have for each course! Feel free to let us know if you have any specific requests and we’ll gladly prepare them for you!"
    r "Meanwhile, please help yourselves to some freshly prepared complimentary snacks and beverages while the party decides on—"

    show emilia evil2 at p9_7
    voice audio.emilia_v_disagree2a2
    e "Why, there’s no need for that~ I’ve had plenty of experience with fine dining establishments, and I know exactly what I want!"
    e "For an appetizer, I’ll have the smoked salmon crostini with herbed mayo— Actually, hold the mayo, and use pesto instead~"

    show emilia play4 at p9_7
    voice audio.emilia_v_think1
    e "For the main course, give me the petit beef wellington, obviously it had better be made with filet mignon and hand-kneaded puff pastry."
    e "Medium RARE, oh, and don’t overdo it. Trust me, I’ll know."

    show emilia bold3 at p9_7
    voice audio.emilia_v_comp1a
    e "Lastly, for dessert… I’ll keep it simple. I’ll have a vanilla crème brulee topped with fresh blueberries and a dash of raspberry coulis. "

    show reimond explain3 at p9_1
    voice audio.reimond_v_greatchoice1b1
    r "Very fine choice, madam. I’ll make sure everything is carefully prepared to your liking."
    r "Does everyone else have their order ready as well?"

    show goro talk3 at p9_4
    voice audio.goro_v_no1a1
    g "Ah, not yet. Can you give us a little bit more time to browse the menu?"

    show reimond talk1 at p9_1
    voice audio.reimond_v_agree4b
    r "Of course! Take your time!"

    show emilia evil6 at p9_7
    voice audio.emilia_v_laugh3b
    e "First timers, am I right? "

    show lloyd confused2 at p9_9
    voice audio.lloyd_v_geez1a2
    l "Gee… Everything in this menu sounds like gibberish to me… even with all the descriptions, I can’t tell how it’ll taste…"

    show jin confuseddn3 at p9_2
    voice audio.jin_v_think2a3
    j "Honestly I can’t even pronounce some of this… Like this booyah…boys?"

    show emilia play3 at p9_7
    voice audio.emilia_v_worry3a
    e "That’s bouillabaisse my dear, it’s a good thing I’m here. If anyone needs help with the menu, I don’t mind educating you~"

    show yuri pout4 at p9_3
    voice audio.yuri_v_hmph1a
    yu "*whispers* As if anyone wants to hear you talk more… "

    show goro think2 at p9_4
    voice audio.goro_v_think1a1
    g "Hmm… If you all want, I can help suggest dishes for each of you that might be to your liking. "
    g "I do pay attention to what you often eat during mealtimes, after all."

    show aiden laugh2 at p9_6
    voice audio.aiden_v_amazed1a1
    a "Ooh, I don’t mind that! I can barely read any of these anyways, hahaha!"

    show goro talk1 at p9_4
    voice audio.goro_v_aiden2a
    g "For you, Aiden, I’ll get you some porkchops and gravy. With mashed potatoes of course."

    show aiden amazed1 at p9_6
    voice audio.aiden_v_amazed2b1
    a "Wow, Gramps!  I’m impressed! You do know what I like!"

    show reimond talk2 at p9_1
    voice audio.reimond_v_agree5a1
    r "Noted, sir!"

    show lloyd bold2 at p9_9
    voice audio.lloyd_v_shock1b1
    l "I’d like something fresh! What about foie gras? That sounds greeny!"

    show darius confused4 at p9_8
    voice audio.darius_v_think2b1
    d "I think you read that as grass…"

    show goro shy6 at p9_4
    voice audio.goro_v_lloyd1c1
    g "Well, Lloyd… That’s duck liver."

    show lloyd pain2 at p9_9
    voice audio.lloyd_v_disgust1b3
    l "Blech! No thanks, then!"

    show goro comp2 at p9_4
    voice audio.goro_v_well1a
    g "Well, you can have some fish if you want something lighter. Here, how about I narrow it down for you."

    show lloyd amazed3 at p9_9
    voice audio.lloyd_v_shock1b1
    l "Ooh, the seafood options all sounds so faaancy! I guess I’ll just order the longest-spelled one! "

    show goro confused3 at p9_4
    voice audio.goro_v_darius1c
    g "For you, Darius. Perhaps korma?"

    show darius happy4 at p9_8
    voice audio.darius_v_agree1a
    d "Yes. Curry is life."

    show yuri play2 at p9_3
    voice audio.yuri_v_goro1b
    yu "Ooh! Dad, should I get coq au vin? That sounds juicy~"

    show jin play2 at p9_2
    voice audio.jin_v_laugh8a
    j "P-Pfftt… coq…"

    show goro happy2 at p9_4
    voice audio.goro_v_response4a1
    g "Sure, Yuri. That should be good enough. I think you and Hyunjin will like it in fact."
    g "For me, I’ll pick the T-bone steak, medium rare with a nice tall glass of red wine."

    show goro happy3 at p9_4
    voice audio.goro_v_actually1a
    g "Actually, please make that two. "
    g "You should try this, Yoshinori. I’m sure you’ll love it."

    show yoshi happy1 at p9_5
    voice audio.yoshi_v_gratitude1
    yo "You read my mind sir, I was just going to order whatever you did, hahaha!"

    show goro explain3 at p9_4
    voice audio.goro_v_think2a1
    g "For the appetizers and dessert, we’ll take the chef’s recommendations."

    show emilia confused2 at p9_7
    voice audio.emilia_v_request1b2
    e "Pardon my intrusion, but I can’t help but overhear some of your selections… Allow me to offer some valuable advice."
    e "For the main, the superior choice is obviously the slow roasted pork belly~ Flavorful and hearty."

    show yuri annoy4 at p9_3
    voice audio.yuri_v_response2a3
    yu "Sounds more like a heart attack."

    show yoshi annoy2 at p9_5
    voice audio.yoshi_v_yuri7
    yo "Yuri, ssh..!"

    show emilia bold3 at p9_7
    voice audio.emilia_v_lloyd3
    e "Mr. Sirius, if you prefer seafood with a higher price point, then the choice for you is lobster bisque! Black truffle dal for Mr. Najjar. And saffron chicken paella for everyone else~"
    e "As for the appetizers—"

    show goro annoy2 at p9_4
    voice audio.goro_v_no1a1
    g "Thanks, but no thanks. We’re good with our orders. "

    show reimond happy3 at p9_1
    voice audio.reimond_v_greatchoice1a1
    r "Excellent choices, sirs and madams. I will relay these to the chef!"
    r "Please excuse me."

    hide reimond_waiter
    hide reimond happy3
    with dissolve

    show jin_formal at p8_1
    show jin shy1 at p8_1
    show yuri_formal at p8_2
    show yuri annoy1 at p8_2
    show goro_formal at p8_3
    show goro annoy1 at p8_3
    show yoshi_formal at p8_4
    show yoshi awkward1 at p8_4
    show aiden_formal at p8_5
    show aiden awkward1 at p8_5
    show emilia_formal at p8_6
    show emilia angry3 at p8_6
    show darius_formal at p8_7
    show darius disgust1 at p8_7
    show lloyd_formal2 at p8_8
    show lloyd awkward1 at p8_8
    with move

    voice audio.emilia_v_surprised2a1
    e "Goodness gracious, I can’t believe all of you wasted your opportunity to order something more sophisticated."
    e "Instead, you all let just one person decide everything. And he didn’t even choose appetizers and desserts!"

    show yuri confused4 at p8_2
    voice audio.yuri_v_confused2b1
    yu "Huh? What’s wrong with that? And why do you care?"
    yu "And aren’t we all ordering from the same menu? With that logic, anything we order would be “SoPhIsTicAtEd”."

    show emilia angry5 at p8_6
    voice audio.emilia_v_question4a
    e "Excuse me, there’s no need to be so rude. I’ve just been trying to share my knowledge ever since we sat down."
    e "Because quite frankly, you all looked like you could use some guidance."

    show goro disappoint2 at p8_3
    voice audio.goro_v_dismiss3a
    g "No need to get so worked up about our orders, Emilia. It’s part of the experience."

    show yuri angry2 at p8_2
    voice audio.yuri_v_yeah1c4
    yu "Yeah, and we can handle ourselves, no problem. Dad’s got us covered."

    show emilia angry3 at p8_6
    voice audio.emilia_v_disagree3b
    e "That’s not the issue here, the problem is that none of my suggestions are even considered, while everyone just agrees to whatever Mr. Nomoru says."

    show yoshi confused2 at p8_4
    voice audio.yoshi_v_comp7
    yo "Calm down, Emilia. There’s nothing to get upset about."

    show emilia rage4 at p8_6
    voice audio.emilia_v_bossy5a
    e "I’m only trying to prove my point. Do I look upset to you?"

    show yuri rage1 at p8_2
    voice audio.yuri_v_ugh2a
    yu "Oh my god… Can’t we have this dinner without you trying to argue?"

    show emilia rage1 at p8_6
    voice audio.emilia_v_what3a
    e "Argue? I was trying to help. You’re all twisting the narrative on me."

    show jin_formal at p9_2
    show jin norm3 at p9_2
    show yuri_formal at p9_3
    show yuri annoy1 at p9_3
    show goro_formal at p9_4
    show goro annoy1 at p9_4
    show yoshi_formal at p9_5
    show yoshi awkward1 at p9_5
    show aiden_formal at p9_6
    show aiden awkward1 at p9_6
    show emilia_formal at p9_7
    show emilia annoy1 at p9_7
    show darius_formal at p9_8
    show darius norm3 at p9_8
    show lloyd_formal2 at p9_9
    show lloyd norm3 at p9_9
    with move

    show reimond_waiter at p9_1
    show reimond happy1 at p9_1
    with dissolve

    voice audio.reimond_v_comingup1a
    r "Serving the first course! "

    show emilia angry2 at p9_7
    voice audio.emilia_v_celebrate1c
    e "A-About time…!"

    show reimond laugh2 at p9_1
    voice audio.reimond_v_callme1b
    r "Please enjoy! And call me if you need anything!"

    hide reimond_waiter
    hide reimond laugh2
    with dissolve

    show jin_formal at p8_1
    show jin shy1 at p8_1
    show yuri_formal at p8_2
    show yuri annoy1 at p8_2
    show goro_formal at p8_3
    show goro annoy1 at p8_3
    show yoshi_formal at p8_4
    show yoshi awkward1 at p8_4
    show aiden_formal at p8_5
    show aiden excited3 at p8_5
    show emilia_formal at p8_6
    show emilia angry3 at p8_6
    show darius_formal at p8_7
    show darius disgust1 at p8_7
    show lloyd_formal2 at p8_8
    show lloyd awkward1 at p8_8
    with move

    voice audio.aiden_v_excited2b
    a "Oooh~ This looks good! What’s it called?"

    show goro confused2 at p8_3
    voice audio.goro_v_think1a1
    g "I think that’s ratatouille."

    show lloyd shock3 at p8_8
    voice audio.lloyd_v_question1b1
    l "RAT?! Didn’t know rich-person food is that exotic?!"

    show darius bored5 at p8_7
    voice audio.darius_v_no1a
    d "No, it’s not, Lloyd. It’s vegetables."

    show yuri laugh1 at p8_2
    voice audio.yuri_v_laugh1a1
    yu "Hihi~ The serving’s so cute and tiny!"

    show jin thinkdn2 at p8_1
    voice audio.jin_v_think1a1
    j "It looks like rainbow pepperoni.."

    show yoshi awkward3 at p8_4
    voice audio.yoshi_v_uh1b
    yo "T-The portions are kinda small, aren’t they…?"

    show emilia rage4 at p8_6
    voice audio.emilia_v_annoyed2
    e "Simpletons! These are just the appetizers! They’re supposed to be small!"

    show lloyd hungry1 at p8_8
    voice audio.lloyd_v_shock1a1
    l "Oh, well I’m done eating it. That just made me hungrier."

    show emilia angry5 at p8_6
    voice audio.emilia_v_hmph1a
    e "That’s the point! It’s meant to stimulate your senses, to build up your appetite for the main course! "
    e "And you’re not supposed to shove it down your throat and swallow it like a pill! You’re ruining the experience!"

    show emilia annoy3 at p8_6
    voice audio.emilia_v_request2b
    e "Look at how it’s done! I sliced mine into four equal parts, making sure each part has every ingredient, allowing me to savor each bite!"
    e "If only everyone had listened to my recommendations, then you wouldn’t have missed out~"

    show darius confused2 at p8_7
    voice audio.darius_v_confused1b
    d "The appetizers were good. I don’t see the problem here."

    show jin confused5 at p8_1
    voice audio.jin_v_conj1c3
    j "A-And we weren’t complaining either… We were just commenting on it…"

    show goro disappoint2 at p8_3
    voice audio.goro_v_response3a1
    g "Just let it go, everyone."

    show emilia angry1 at p8_6
    e "..."

    show jin_formal at p9_2
    show jin norm3 at p9_2
    show yuri_formal at p9_3
    show yuri norm3 at p9_3
    show goro_formal at p9_4
    show goro norm3 at p9_4
    show yoshi_formal at p9_5
    show yoshi norm3 at p9_5
    show aiden_formal at p9_6
    show aiden norm3 at p9_6
    show emilia_formal at p9_7
    show emilia annoy1 at p9_7
    show darius_formal at p9_8
    show darius norm3 at p9_8
    show lloyd_formal2 at p9_9
    show lloyd norm3 at p9_9
    with move

    show reimond_waiter at p9_1
    show reimond happy1 at p9_1
    with dissolve

    $ renpy.music.stop(channel='music', fadeout = 3.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 3.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 3.0)
    voice audio.reimond_v_request1d1
    r "I hope everyone enjoyed their appetizers, as the main course is ready! Please enjoy!"

    hide reimond_waiter
    hide reimond
    with dissolve

    show jin_formal at p8_1
    show jin norm1 at p8_1
    show yuri_formal at p8_2
    show yuri norm1 at p8_2
    show goro_formal at p8_3
    show goro norm1 at p8_3
    show yoshi_formal at p8_4
    show yoshi norm1 at p8_4
    show aiden_formal at p8_5
    show aiden norm1 at p8_5
    show emilia_formal at p8_6
    show emilia annoy1 at p8_6
    show darius_formal at p8_7
    show darius norm1 at p8_7
    show lloyd_formal2 at p8_8
    show lloyd norm1 at p8_8
    with move

    play music heracleum_a loop
    show cg fade2 at truecenter
    show fx5g 1 at fx_pos
    with dissolve
    voice audio.lloyd_vsa13_line1
    l "Now we’re talking! My mouth is watering from just looking at it!"

    voice audio.yuri_vsa13_line1
    yu "KYAA~! Talk about the plating and presentation!"

    voice audio.jin_vsa13_line1
    j "I wish I’d brought my camera to take a picture of this…"

    voice audio.goro_vsa13_line1
    g "Well let’s see if it tastes as good as it looks."

    voice audio.yoshi_vsg15_line1
    yo "Mmm… It’s delicious! Your orders for us were perfect, sir!"

    voice audio.darius_vsa13_line1
    d "Melts in my mouth."

    voice audio.aiden_v_mmm1a1 #aiden_vsg15_line1 #jey
    a "Mm-mm! This is way better than anything I can make!"

    show fx5g 2 at fx_pos with Dissolve(0.25)
    voice audio.emilia_vsg15_line1
    e "My goodness, did we not just have a conversation about table manners? Stop talking when your mouth is full."

    voice audio.yuri_vsg15_line1
    yu "Wow. What is wrong with you?"

    voice audio.yoshi_vsg15_line2
    yo "Emilia, can we please just enjoy our dinner?"

    voice audio.emilia_vsg15_line2
    e "How am I supposed to with all of you talking over each other like you’ve never seen food on a plate before?"

    show fx5g 3 at fx_pos with Dissolve(0.25)
    voice audio.goro_vsg15_line1
    g "Why are you so absorbed in what everyone else is doing? "

    voice audio.goro_vsg15_line2
    g "All those classes you had for fine dining etiquette, and you can’t even practice what you preach."

    voice audio.emilia_vsg15_line3
    e "Excuse me, I’m doing exactly as I should. Unlike some of you who can’t even keep their elbows off the table."

    voice audio.goro_vsg15_line3
    g "I’m talking about your attitude and tone. Tell me that’s not being disruptive."

    show fx5g 4 at fx_pos with Dissolve(0.25)
    voice audio.emilia_vsg15_line4
    e "What…?"

    voice audio.goro_vsg15_line4
    g "We’re here to have a good time and that’s what we’re gonna do. "

    voice audio.goro_vsg15_line5
    g "We’re already doing you a favor by trying to deflect each of your attempts to spoil this amazing night for us."

    voice audio.emilia_vsg15_line5
    e "I’m the one spoiling the mood?! Preposterous!"

    show fx5g 5 at fx_pos with Dissolve(0.25)
    voice audio.yoshi_vsg15_line3
    yo "Emilia, keep it down… The other tables are looking at us…"

    voice audio.yuri_vsg15_line2
    yu "Yeah, don’t be such a pain in the ass."

    voice audio.emilia_vsg15_line6
    e "I’ve only been trying to participate the conversation and you all shut me down at every chance."

    voice audio.goro_vsg15_line6
    g "You had nothing nice to say. What did you expect?"

    show fx5g 6 at fx_pos with Dissolve(0.25)
    voice audio.emilia_vsg15_line7
    e "Am I not allowed to have an opinion? How come when I’m the one talking all of you always assume that I have ill intentions?"

    voice audio.yuri_vsg15_line3
    yu "How else are we supposed to take it when everything you say is condescending?!"

    voice audio.emilia_vsg15_line8
    e "You know what? There’s no point explaining myself to people who won’t even bother to listen! "

    show fx5g 7 at fx_pos with Dissolve(0.25)
    voice audio.goro_vsg15_line7
    g "Then leave."

    voice audio.emilia_vsg15_line9
    e "W-What…?"

    voice audio.goro_vsg15_line8
    g "Did you not hear what I said?"

    show fx5g 8 at fx_pos with Dissolve(0.25)
    voice audio.goro_vsg15_line9
    g "Leave!"

    show fx5g 9 at fx_pos with Dissolve(0.25)
    voice audio.emilia_vsg15_line10
    e "What gives you the right to kick me out?"

    voice audio.emilia_vsg15_line11
    e "First of all, we’re not at camp, and second of all, even if we were, you’re in no position to boss me around!  "

    voice audio.emilia_vsg15_line12
    e "This is exactly your problem. Just because you have some title, you think you can abuse your power and dictate for everyone what they can and can’t do!"

    voice audio.emilia_vsg15_line13
    e "It’s one thing when it’s work-related, but it’s entirely another when you force everyone into a situation where they’re not even allowed to think for themselves!"

    show fx5g 10 at fx_pos with Dissolve(0.25)
    voice audio.yoshi_vsg15_line4
    yo "It’s not like that, Emilia. We’re not just following Sir Goro because he’s our leader."

    voice audio.yoshi_vsg15_line5
    yo "We’re looking to him for his opinion because he has the skill and experience."

    voice audio.emilia_vsg15_line14
    e "So, you’re saying that I don’t?"

    voice audio.yoshi_vsg15_line6
    yo "Enough, Emilia… We don’t have to talk about this… Not right now."

    show fx5a 7 at fx_pos with Dissolve(0.25)
    voice audio.emilia_vsa13_line7
    e "No, no. Let’s talk about it, since she’s questioning my abilities."

    voice audio.emilia_vsa13_line8
    e "I think I’ve proven how skilled I am over the last few months with actual results."

    voice audio.emilia_vsa13_line9
    e "Without me, your whole project wouldn’t have gotten this far, and we wouldn’t be sitting here enjoying this lovely dinner."

    hide fx5g 10
    show fx5a 8 at fx_pos with Dissolve(0.25)
    voice audio.lloyd_vsa13_line3
    l "I didn’t see you lift a finger to help any of the departments the entire time…"

    voice audio.darius_vsa13_line3
    d "You’re just micro-managing."

    show fx5a 9 at fx_pos with Dissolve(0.25)
    voice audio.emilia_vsa13_line10
    e "I cannot believe what I’m hearing! You’re all just trying to discredit me, just like you did in that meeting!"

    voice audio.emilia_vsa13_line11
    e "If anything, all of you just can’t accept honest criticism!"

    show fx5a 10 at fx_pos with Dissolve(0.25)
    voice audio.yoshi_vsa13_line3
    yo "Emilia, stop!"

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    $ renpy.pause (2.0, hard=True)
    hide cg fade2
    hide fx5a 10
    with dissolve

    play music heracleum_b loop
    show jin worry1 at p8_1
    show yuri annoy1 at p8_2
    show goro angry1 at p8_3
    show yoshi angry1 at p8_4
    show aiden scared3 at p8_5
    show emilia rage4 at p8_6
    show darius worry1 at p8_7
    show lloyd awkward2 at p8_8
    voice audio.emilia_vsa13_line12
    e "It’s awfully convenient for all of you to point at me for your own shortcomings, isn’t it?"

    voice audio.emilia_vsg15_line15
    e "Why has nobody pointed out that we have an outdated leader who built this franchise up, then ran it into the ground?!"

    show emilia angry6 at p8_6
    voice audio.emilia_vsg15_line16
    e "It’s no secret that the reason the other branches of Camp Buddy closed down was because of his mismanagement! "

    voice audio.emilia_vsg15_line17
    e "And yet we’re supposed to believe that following the same leadership would make a difference?"

    show emilia angry3 at p8_6
    voice audio.emilia_vsg15_line18
    e "It’s pretty telling how incompetent the one in charge really is when the only thing that saved the camp from disgrace... was the scouts."

    show yuri rage4 at p8_2
    voice audio.yuri_vsg15_line4
    yu "You have no idea what you’re talking about! You weren’t even here for any of that! So, just shut the hell up!"

    show emilia rage4 at p8_6
    voice audio.emilia_vsg15_line19
    e "That’s another thing!  The only reason you have the nerve to constantly insult me is because your father lets you get away with all of it!"

    voice audio.emilia_vsg15_line20
    e "I can’t believe this blatant bias went on for years!  Your confrontational behavior and all your frivolous whims in and out of the camp just shows how hopelessly unprofessional you are! "

    show goro rage1 at p8_3
    voice audio.goro_vsg15_line10
    g "How dare you talk to her like that?!" with vpunch

    show yoshi angry2 at p8_4
    voice audio.yoshi_vsg15_line7
    yo "S-Sir Goro, don’t let her get to you…!"

    show emilia eyeroll6 at p8_6
    voice audio.emilia_vsg15_line21
    e "Hmph! Speaking of which, Yoshinori… you’re the prime example of someone who has been corrupted for so many years. "

    voice audio.emilia_vsg15_line22
    e "You continue to let yourself be held down and waste your potential, keeping yourself and the camp from a better future."

    show emilia angry2 at p8_6
    voice audio.emilia_vsg15_line23
    e "In fact, you all wouldn’t even need a sponsorship if it wasn’t for how badly you handled last year’s scandal and ruined the camp’s reputation!"

    voice audio.emilia_vsg15_line24
    e "You should’ve known better than to be so passive and ingratiating – always crawling back to someone you look up to, all because you lack the spine to make your own choices!"

    play sound sfx_thud
    show goro rage3 at p8_3
    voice audio.goro_vsg15_line11
    g "SHUT YOUR FUCKING MOUTH!"

    voice audio.goro_vsg15_line12
    g "I don’t give a damn about what you think of me, but I’m not going to let you attack my daughter and Yoshinori like this!"

    show goro angry4 at p8_3
    voice audio.goro_vsg15_line13
    g "Your repulsive attitude is the only problem here!"

    voice audio.goro_vsg15_line14
    g "It has been nothing but absolute stress and displeasure to deal with you, and quite frankly you’ve long overstayed your welcome!"

    show goro disappoint4 at p8_3
    voice audio.goro_vsg15_line15
    g "Consider yourself finished. I don’t want you at this dinner, at Camp Buddy, or in my sight ever again."

    show emilia eyeroll3 at p8_6
    voice audio.emilia_vsg15_line25
    e "Why am I not surprised that your solution to everything is to just cut it off?"

    voice audio.emilia_vsg15_line26
    e "You’re doing it to me, you did it to your scouts and staff, and you did it with your wife."

    show emilia disgust3 at p8_6
    voice audio.emilia_vsg15_line27
    e "I bet when you eventually don’t get your way with Yoshinori, you’ll cut him off just the same. "

    voice audio.emilia_vsg15_line28
    e "This is why nobody stays in your life. Except maybe for your daughter, because you know what? She doesn’t really have much of a choice."

    show emilia angry2 at p8_6
    voice audio.emilia_vsg15_line29
    e "Do the right thing for once, and keep everyone else out of your midlife crisis!"

    show goro angry3 at p8_3
    voice audio.goro_vsg15_line16
    g "Disrespect me all you want, but it’s not going to change how hopelessly rotten you are inside and out!"

    voice audio.goro_vsg15_line17
    g "Take a good look at yourself and ask if there’s a single person in the world who's ever wanted you."

    show goro annoy4 at p8_3
    voice audio.goro_vsg15_line18
    g "Not me. Not anyone at Camp Buddy. Not even your own parents! "

    show emilia rage6 at p8_6
    voice audio.emilia_vsg15_line30
    e "*gasp* Take that back!"

    play sound sfx_winespill
    show emilia rage3 at p8_6
    hide goro_formal
    hide goro annoy4
    show goro_formal2 at p8_3
    show goro rage1 at p8_3
    hide yuri_formal
    hide yuri rage4
    show yuri_formal at p8_2
    show yuri rage4 at p8_2
    e "*throws wine at Goro*" with vpunch

    play sound sfx_thud
    show goro rage4 at p8_3
    voice audio.goro_vsg15_line19
    g "GRRRR!!! I’VE HAD IT WITH YOU! " with vpunch

    show goro_formal2 at p8_4
    show goro rage4 at p8_4
    show yoshi_formal at p8_3
    show yoshi panic5 at p8_3
    with move

    yo "...!"

    show cg_fade at truecenter
    show fxg5 at fx_pos
    voice audio.goro_vsg16_line1
    g "GRAAHHH!!!" with vpunch

    voice audio.yoshi_vsg16_line1
    yo "Sir Goro, no!!"

    voice audio.aiden_vsg16_line1
    a "H-Hey! C-Calm down…!"

    voice audio.jin_vsg16_line1
    j "W-Wahh!!"

    voice audio.lloyd_vsg16_line1
    l "Oh shit… oh shit…"

    voice audio.yuri_vsg16_line1
    yu "Dad! She’s not worth it!!"

    voice audio.emilia_vsg16_line1
    e "Go on! I dare you!"

    voice audio.darius_vsg16_line1
    d "Emilia, stop it already!"

    voice audio.yoshi_vsg16_line2
    yo "Sir Goro, ENOUGH!"

    $ renpy.music.stop(channel='music', fadeout = 2.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 2.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 2.0)
    hide cg_fade
    hide fxg5
    with dissolve

    show jin panic3 at p8_1
    show yuri panic2 at p8_2
    show yoshi panic1 at p8_3
    show goro rage2 at p8_4
    show aiden scared3 at p8_5
    show emilia rage1 at p8_6
    show darius panic5 at p8_7
    show lloyd panic3 at p8_8
    voice audio.goro_v_angry1a1
    g "Grrr… Grr… *heavy breathing*"

    $ working = False
    $ shuffle_menu()
    menu():
        g "Grrr… Grr… *heavy breathing*{fast}"
        "What were you thinking?":
            $ working = True
            $ score_goro -=2
            $ score_top += 1
            show yoshi panic4 at p8_3
            voice audio.yoshi_v_sirgoro4b
            yo "What were you thinking, sir?!"
        "You're better than this.":
            $ working = True
            $ score_goro -=2
            $ score_bot += 1
            show yoshi sad4 at p8_3
            voice audio.yoshi_v_sirgoro4b
            yo "Sir… You’re better than this…"
        "Take a deep breath.":
            $ working = True
            $ score_goro +=2
            $ score_top += 1
            show yoshi sad4 at p8_3
            voice audio.yoshi_v_sirgoro4b
            yo "That’s right, sir… Just take a deep breath…"
        "...":
            $ working = True
            $ score_goro +=2
            $ score_bot += 1
            show yoshi sad3 at p8_3
            yo "{i}(All I could do was look into Sir Goro’s eyes to help him calm down.){/i}"

    show goro disappoint1 at p8_4
    g "..."

    show jin panic1 at p8_1
    show yuri panic1 at p8_2
    show yoshi sad1 at p8_3
    show aiden scared1 at p8_5
    show emilia angry1 at p8_6
    show lloyd panic1 at p8_8
    show darius panic1 at p8_7
    all "..."

    show yoshi worry1 at p8_3
    yo "{i}(The silence is deafening… All eyes in the room are on us...){/i}"
    yo "{i}(I don’t know what would’ve happened if we didn’t stop him…){/i}"

    show goro panic1 at p8_4
    g "..."

    show yoshi sad1 at p8_3
    yo "{i}(Sir Goro’s starting to calm down now… and he’s looking at each of us, and his eyes are filled with regret. ){/i}"

    show jin sad1 at p8_1
    show yuri sad1 at p8_2
    show aiden sad1 at p8_5
    show emilia evil1 at p8_6
    show darius sad1 at p8_7
    show lloyd sad1 at p8_8
    all "..."

    show goro sad3 at p8_4
    voice audio.goro_v_i1a
    g "I…"

    show goro upset5 at p8_4
    voice audio.goro_v_sorry2c1
    g "I’m sorry…"

    hide goro_formal2
    hide goro upset5
    with dissolve

    show yoshi panic2 at p8_3
    voice audio.yoshi_v_sirgoro1
    yo "Sir Goro…!"

    hide yoshi_formal
    hide yoshi panic2
    with dissolve

    show jin_formal at p6_1
    show jin worry1 at p6_1
    show yuri_formal at p6_2
    show yuri annoy1 at p6_2
    show aiden_formal at p6_3
    show aiden worry1 at p6_3
    show emilia_formal at p6_4
    show emilia angry5 at p6_4
    show darius_formal at p6_5
    show darius worry1 at p6_5
    show lloyd_formal2 at p6_6
    show lloyd worry1 at p6_6
    with move

    play music heracleum_musicbox_a loop
    voice audio.emilia_v_hmph1a
    e "Hmph… And so, we see his true colors."

    show yuri angry3 at p6_2
    voice audio.yuri_v_emilia8a
    yu "What are you getting out of this, Emilia?!"

    show emilia rage4 at p6_4
    voice audio.emilia_v_what3a
    e "What? I’m the one who was verbally assaulted here!"
    e "Maybe all of you shouldn’t have been so rude, then none of this would’ve happened!"

    show yuri rage1 at p6_2
    voice audio.yuri_v_what5a
    yu "ALL OF US?! You’re the only one who’s been rude this whole time!!" with vpunch
    yu "You’re rotten to the core just like you were back then!"

    show yuri rage4 at p6_2
    voice audio.yuri_v_angry1a1
    yu "Step off that putrid high horse and get away from Camp Buddy already!"
    yu "You don’t belong with us, and you never will!"

    show emilia rage6 at p6_4
    voice audio.emilia_v_response1c
    e "Fine! I never wanted to be here anyway!"

    hide emilia_formal
    hide emilia rage6
    with dissolve

    show jin_formal at p6_2
    show jin worry1 at p6_2
    show yuri_formal at p6_3
    show yuri angry1 at p6_3
    show aiden_formal at p6_4
    show aiden worry1 at p6_4
    with move

    show reimond_waiter at p6_1
    show reimond confused2 at p6_1
    with dissolve

    voice audio.reimond_v_worry2a
    r "Is everything alright here? I heard a commotion…"

    show aiden talk5 at p6_4
    voice audio.aiden_v_alright3a
    a "No, yeah, we’re good…! Just a little squabble, is all…!"

    show lloyd worry3 at p6_6
    voice audio.lloyd_v_ah1c1
    l "Oh my god… Everyone’s still looking…"

    show jin sad2 at p6_2
    voice audio.jin_v_worry2b
    j "I hope Sir Goro’s okay, though…"

    show darius disappoint2 at p6_5
    voice audio.darius_v_rush2
    d "Let’s call it a night and get back to our rooms, everyone."

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

    $ location = location_hotelroom
    show screen location
    show screen timeline
    show screen quick_menu
    scene bg_hotel_room1_night_lightsout with fade

    play sound sfx_cardbeep
    $ renpy.pause (1.0, hard=True)
    $quick_menu = True
    play sound sfx_dooropen
    show yoshi_formal at center
    show yoshi worry4 at center
    with dissolve

    voice audio.yoshi_vsg17_line1
    yo "Sir Goro?? Are you in here?"

    show yoshi worry2 at center
    voice audio.yoshi_vsg17_line2
    yo "Sir Goro?"

    show yoshi panic1 at center
    yo "...!"

    show cg_fade at truecenter
    show fxg6 at fx_pos
    with dissolve

    voice audio.yoshi_vsg17_line3
    yo "I-I’ve been looking for you, sir… I couldn’t find you around the hotel…"
    g "..."

    voice audio.yoshi_vsg17_line4
    yo "S-Sir Goro? Are you alright…? "

    voice audio.goro_vsg17_line1
    g "I… I’m fine."
    yo "{i}(Even with his answer, I know he’s not…){/i}"
    yo "{i}(With a bottle in his hand and his head held down in this dark, unlit, room... I can’t begin to imagine the shame Sir Goro’s feeling right now…){/i}"

    voice audio.goro_vsg17_line2
    g "Go back to everyone, Yoshinori… "

    $ working = False
    $ shuffle_menu()
    menu():
        g "Go back to everyone, Yoshinori… {fast}"
        "I won't go without you.":
            $ working = True
            $ score_goro -= 1
            $ score_bot += 1
            voice audio.yoshi_vsg17_line5a
            yo "I won’t go without you, sir…"
        "There's no point.":
            $ working = True
            $ score_goro -= 1
            $ score_top += 1
            voice audio.yoshi_vsg17_line5b
            yo "There’s no point, sir… I’m sure everyone’s already left…"
        "I'm staying here.":
            $ working = True
            $ score_goro += 1
            $ score_bot += 1
            voice audio.yoshi_vsg17_line5c
            yo "I’m staying here with you, sir…"
        "But you're not okay.":
            $ working = True
            $ score_goro += 1
            $ score_top += 1
            voice audio.yoshi_vsg17_line5d
            yo "But… you’re not okay, sir."
    voice audio.goro_vsg17_line3
    g "Khh…"

    voice audio.yoshi_vsg17_line6
    yo "You don’t have to be alone, sir… I’m here."

    voice audio.yoshi_vsg17_line7
    yo "You can talk to me… I-I’ll listen..."

    scene cgg5 1 with fade
    play music buddy_oath_goro_sad loop
    g "..."
    yo "{i}(Even after all the years I’ve known Sir Goro, this is the first time he’s allowed me to see him like this…){/i}"
    yo "{i}(Holding him, I knew he was trembling with frustration over what happened…){/i}"

    voice audio.goro_vsg17_line4
    g "I’m so sorry, Yoshinori…"

    voice audio.goro_vsg17_line5
    g "I hate that you all had to see me like that… "

    voice audio.goro_vsg17_line6
    g "I’m so ashamed of how I acted in front of everyone else… in front of you…"

    show cgg5 2 with Dissolve(0.25)
    voice audio.yoshi_vsg17_line8
    yo "Sir Goro…"

    voice audio.goro_vsg17_line7
    g "I was trying my best to control my anger… But in the end, I couldn’t…"

    voice audio.yoshi_vsg17_line9
    yo "But I understand why you lost your patience, sir… All of us were feeling the same way…"

    voice audio.yoshi_vsg17_line10
    yo "What Emilia did back there was completely uncalled for… and you were only trying to stand up for all of us, just like you have before…"

    show cgg5 3 with Dissolve(0.25)
    voice audio.goro_vsg17_line8
    g "Still… It’s not an excuse to let myself fall into a fit of rage like that… "

    voice audio.goro_vsg17_line9
    g "Knowing who I was up against, I should’ve been the bigger person…"

    voice audio.goro_vsg17_line10
    g "You all look to me to make the right decisions, but instead I chose to let my anger get the best of me… "

    voice audio.goro_vsg17_line11
    g "My actions only proved what Emilia said…"

    show cgg5 4 with Dissolve(0.25)
    voice audio.yoshi_vsg17_line11
    yo "But none of what she said was true, sir. She was just desperate to defend herself like always, and can never admit when she’s wrong."

    voice audio.goro_vsg17_line12
    g "Regardless, my behavior was unacceptable, especially for someone who carries the name of the camp on their shoulders."

    voice audio.goro_vsg17_line13
    g "We’re here representing both Camp Buddy and Mr. Clermont’s reputation… And this incident might have just cost us our sponsorship…"

    voice audio.yoshi_vsg17_line12
    yo "I… didn’t realize that, sir."

    voice audio.goro_vsg17_line14
    g "Everything that we’ve worked so hard for… there’s a possibility that it’ll be lost thanks to what I’ve done…"

    show cgg5 5 with Dissolve(0.25)
    voice audio.goro_vsg17_line15
    g "I really screwed up big time…!"

    voice audio.yoshi_vsg17_line13
    yo "I-I’m sure there’s a way for us to fix this, sir."

    voice audio.yoshi_vsg17_line14
    yo "What happened tonight was something none of us meant for, after all."

    voice audio.yoshi_vsg17_line15
    yo "I’m sure Mr. Clermont will understand if we explain…"

    voice audio.goro_vsg17_line16
    g "But that’s just it, Yoshinori… We’ve already been given more than enough chances to make things right for the camp…"

    show cgg5 6 with Dissolve(0.25)
    voice audio.goro_vsg17_line17
    g "What if this was the final straw…?"
    yo "..."
    yo "{i}(Seeing Sir Goro look so defeated, I wasn’t sure if there was anything I could do to comfort him. But I have to try.){/i}"

    show cgg5 7 with Dissolve(0.25)
    voice audio.yoshi_vsg17_line16
    yo "Sir Goro… I know things aren’t going the way you planned…"

    voice audio.yoshi_vsg17_line17
    yo "You’ve gone through so much worse in the past and pulled through every single one… "

    voice audio.yoshi_vsg17_line18
    yo "I know what’s hurting you right now is something else much deeper…"
    g "..."

    voice audio.yoshi_vsg17_line19
    yo "So please… tell me what it is…"

    $ renpy.pause (2.0, hard=True)
    show cgg5 8 with Dissolve(0.25)
    voice audio.goro_vsg17_line18
    g "What hurts the most is the realization… that I never had a chance at redemption."

    voice audio.yoshi_vsg17_line20
    yo "R-Redemption…?"

    voice audio.goro_vsg17_line19
    g "I’ve been trying so hard to work on myself since this season began…"

    show cgg5 9 with Dissolve(0.25)
    voice audio.goro_vsg17_line20
    g "It took me so long to start making up for all the mistakes I’ve made in the past, and I really believed that it wasn’t too late to change."

    voice audio.goro_vsg17_line21
    g "I had hoped to redeem myself not only with the scouts, but also with all of you, who’ve been with me and the camp through thick and thin…"

    voice audio.goro_vsg17_line22
    g "Trying to be more cheerful and softspoken, I really thought I was doing better…"

    show cgg5 10 with Dissolve(0.25)
    voice audio.goro_vsg17_line23
    g "And yet… it only took one moment to undo it all."

    show cgg5 11 with Dissolve(0.25)
    voice audio.goro_vsg17_line24
    g "When I saw the look on everyone’s faces back there… even my own daughter…"

    voice audio.goro_vsg17_line25
    g "All I felt was disappointment in myself…"

    voice audio.goro_vsg17_line26
    g "It made me realize that I haven’t changed at all… I’m still that bitter old man with anger issues…"

    $ working = False
    $ shuffle_menu()
    menu():
        g "It made me realize that I haven’t changed at all… I’m still that bitter old man with anger issues…{fast}"
        "But we've all changed.":
            $ working = True
            $ score_goro -= 2
            show cgg5 12ab with Dissolve(0.25)
            voice audio.yoshi_vsg17_line21a
            yo "But all of us have changed, sir, including you!"

            voice audio.yoshi_vsg17_line22a
            yo "And everyone else knows that things are different now and won’t let this one incident define you!"
        "You're not who you used to be.":
            $ working = True
            $ score_goro -= 1
            show cgg5 12ab with Dissolve(0.25)
            voice audio.yoshi_vsg17_line21b
            yo "But you’re not who you used to be, sir."

            voice audio.yoshi_vsg17_line22b
            yo "You’ve changed for the better, and nobody will let this one incident define you."
        "I didn't think of you any less.":
            $ working = True
            $ score_goro += 1
            show cgg5 12cd with Dissolve(0.25)
            voice audio.yoshi_vsg17_line21c
            yo "I don’t think of you that way, sir… "

            voice audio.yoshi_vsg17_line22cd
            yo "In fact, I’ve never thought any less of you."

            voice audio.yoshi_vsg17_line22a
            yo "And everyone else knows that things are different now and won’t let this one incident define you!"
        "I still look up to you the same.":
            $ working = True
            $ score_goro += 2
            show cgg5 12cd with Dissolve(0.25)
            voice audio.yoshi_vsg17_line21d
            yo "I still look up to you, just like I did back then, sir…"

            voice audio.yoshi_vsg17_line22cd
            yo "In fact, I’ve never thought any less of you."

            voice audio.yoshi_vsg17_line22a
            yo "And everyone else knows that things are different now and won’t let this one incident define you!"

    show cgg5 13 with Dissolve(0.25)
    voice audio.goro_vsg17_line27
    g "But that’s the thing… All I wanted was to return to the person I once was…"

    voice audio.yoshi_vsg17_line23
    yo "But you don’t have to go back to that, sir! I never expected you to stay the same, especially after everything you’ve been through…"

    show cgg5 14 with Dissolve(0.25)
    voice audio.yoshi_vsg17_line24
    yo "You built a home for all of us, somewhere we could always return to, no matter what happened. "

    voice audio.yoshi_vsg17_line25
    yo "None of the amazing experiences and memories would’ve been possible if it weren’t for you."

    voice audio.yoshi_vsg17_line26
    yo "And we wouldn’t have come this far if you hadn’t selflessly given yourself up for all of us…"

    show cgg5 15 with Dissolve(0.25)
    voice audio.yoshi_vsg17_line27
    yo "That’s something that I will forever admire about you… "

    voice audio.yoshi_vsg17_line28
    yo "Your strength and resilience when facing even the toughest situations… Always giving your best unconditionally for the people you care for."

    voice audio.yoshi_vsg17_line29
    yo "But you don’t have to keep bearing everything alone anymore… Everyone at Camp Buddy is here for you…"

    voice audio.yoshi_vsg17_line30
    yo "…and I’m here for you! "

    show cgg5 16 with Dissolve(0.25)
    voice audio.yoshi_vsg17_line31
    yo "We’re partners, aren’t we?"
    g "...!"

    $ renpy.pause (2.0, hard=True)
    show cgg5 17 with Dissolve(0.25)
    voice audio.goro_vsg17_line28
    g "No matter how hard I fall, you’re always there for me…"

    voice audio.goro_vsg17_line29
    g "I’ve always known how much I don’t deserve you… "

    voice audio.goro_vsg17_line30
    g "But… I need you to know…"

    voice audio.goro_vsg17_line31
    g "That the only reason I keep fighting and looking towards the future…"

    $ renpy.music.stop(channel='music', fadeout = 2.0)
    scene cgg6 1 with Dissolve(2.0)
    voice audio.goro_vsg17_line32
    play music buddy_oath_musicbox loop
    g "…is all because of you."

    show cgg6 2 with Dissolve(0.25)
    voice audio.goro_vsg17_line33
    g "I can’t fight this feeling anymore…"

    voice audio.goro_vsg17_line34
    g "From the moment I met you, I knew you were special."

    voice audio.goro_vsg17_line35
    g "And when I was at my worst, you still saw the best in me."

    voice audio.goro_vsg17_line36
    g "You gave me hope for the future and a chance at true happiness…"

    show cgg6 3 with Dissolve(0.25)
    voice audio.goro_vsg17_line37
    g "I love you, Yoshinori."

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

    $ location = location_waterfall
    $ day = "??"
    $ time = timeline_timenight
    $ season = season_summer
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_waterfall_past_night_top with fade
    play bgsound sfxloop_windy loop

    show ygoro_camp at center
    show ygoro upset1 at center
    g "..."

    show ygoro_camp at right
    show ygoro upset1 at right
    with move

    show yyoshi_camp at left
    show yyoshi talk3 at left
    with dissolve

    voice audio.yyoshi_vsg18_line1
    yo "There you are, Sir Goro! "

    show ygoro sad3 at right
    voice audio.ygoro_vsg18_line1
    g "Ah… Yoshinori…"

    show yyoshi worry2 at left
    voice audio.yyoshi_vsg18_line2
    yo "Everyone else has settled into their tents for the night, but…"

    voice audio.yyoshi_vsg18_line3
    yo "…Yuri told me you came up here to answer a call?  "

    show ygoro sigh1 at right
    voice audio.ygoro_vsg18_line2
    g "I see…"

    show yyoshi worry3 at left
    voice audio.yyoshi_vsg18_line4
    yo "I-Is everything alright, sir…?"

    show ygoro upset1 at right
    g "..."

    show yyoshi_camp at center
    show yyoshi sad3 at center
    with move

    voice audio.yyoshi_vsg18_line5
    yo "I hope you don’t mind if I stay here with you…"

    show ygoro sad2 at right
    voice audio.ygoro_vsg18_line3
    g "Yoshinori…"

    scene cgg7 1 with fade
    play music old_familiar_home_slow loop
    voice audio.ygoro_vsg18_line4
    g "It’s over…"

    voice audio.yyoshi_vsg18_line6
    yo "What is…?"

    voice audio.ygoro_vsg18_line5
    g "My wife… We’re over… for good this time."

    show cgg7 2 with Dissolve(0.25)
    yo "...!"

    voice audio.ygoro_vsg18_line6
    g "While we were on this trip… I found out that my wife has been… seeing someone else."

    voice audio.ygoro_vsg18_line7
    g "Everything made sense about why she’s never around for me and Yuri…"

    show cgg7 3 with Dissolve(0.25)
    voice audio.yyoshi_vsg18_line7
    yo "I-I’m so sorry, sir…"

    voice audio.ygoro_vsg18_line8
    g "To be honest, I think I’ve always known, deep in my heart, and just kept denying it…"

    voice audio.ygoro_vsg18_line9
    g "I was going to forgive her… and try to work things out so we could still be a family… but I shouldn’t force her anymore."

    voice audio.ygoro_vsg18_line10
    g "It’s about time I let go…"

    show cgg7 4 with Dissolve(0.25)
    yo "..."

    voice audio.ygoro_vsg18_line11
    g "I had it coming… For all the mistakes I’ve made in the past."

    voice audio.ygoro_vsg18_line12
    g "Having a family at a young age, I kept pushing for the idea of a perfect one. "

    voice audio.ygoro_vsg18_line13
    g "I tried to change my ways, and only wanted to be a good husband and father. I did everything in my power to keep us together."

    voice audio.ygoro_vsg18_line14
    g "But in the end, it only hurt me… my wife… and my daughter in the process… And none of us were truly happy…"

    voice audio.yyoshi_vsg18_line8
    yo "Sir Goro…"

    show cgg7 5 with Dissolve(0.25)
    voice audio.ygoro_vsg18_line15
    g "I ruined my family… I was never going to be good enough… Everything was a mistake."

    show cgg7 6 with Dissolve(0.25)
    voice audio.yyoshi_vsg18_line9
    yo "Th-That’s not true, sir! What about Yuri? "

    voice audio.yyoshi_vsg18_line10
    yo "And what about Camp Buddy?!"

    voice audio.yyoshi_vsg18_line11
    yo "You’ve given me, Yuri, and everyone else here a place to belong that we never had before!"

    show cgg7 7 with Dissolve(0.25)
    voice audio.yyoshi_vsg18_line12
    yo "I know we’ve only been together for the summer, but it’s the best one I’ve ever had!"

    voice audio.yyoshi_vsg18_line13
    yo "Here I’ve finally been able to make new friends, unforgettable memories, and most importantly… meet you!"

    show cgg7 8 with Dissolve(0.25)
    voice audio.yyoshi_vsg18_line14
    yo "And for that, I’m forever grateful!"
    g "..."

    voice audio.yyoshi_vsg18_line15
    yo "Not everything is lost, sir…! We’re all a part of your family now, too!"

    $ renpy.pause (2.0, hard=True)
    show cgg7 9 with Dissolve(0.25)
    voice audio.ygoro_vsg18_line16
    g "You’re right… I still have Camp Buddy… Yuri… and you."

    $ renpy.pause (2.0, hard=True)
    show cgg7 10 with Dissolve(0.25)
    voice audio.ygoro_vsg18_line17
    g "*sigh*"

    voice audio.ygoro_vsg18_line18
    g "This isn’t really the best look for your scoutmaster, especially on our last camping trip together."

    voice audio.ygoro_vsg18_line19
    g "And I can’t believe I said all that to a scout."

    show cgg7 11 with Dissolve(0.25)
    voice audio.yyoshi_vsg18_line16
    yo "Well, I’m not just your scout, sir! I’m your friend too!"
    g "..."

    show cgg7 12 with Dissolve(0.25)
    voice audio.ygoro_vsg18_line20
    g "I have to admit… I’ve never had anyone to say all these things to."

    voice audio.ygoro_vsg18_line21
    g "Being a father and a leader, I felt like I had to stay strong and not show any weakness."

    show cgg7 13 with Dissolve(0.25)
    voice audio.yyoshi_vsg18_line17
    yo "I’ve seen how hard you work not only for the camp, but for your family too… All while keeping a smile on your face!"

    voice audio.yyoshi_vsg18_line18
    yo "That’s why you’re my biggest inspiration, sir!"

    voice audio.yyoshi_vsg18_line19
    yo "Someday, I’m going to be a scoutmaster like you! A person that everyone can count on!"

    voice audio.yyoshi_vsg18_line20
    yo "Then maybe you won’t have to do everything on your own, sir!"

    voice audio.ygoro_vsg18_line22
    g "Yoshinori…"

    show cgg7 14 with Dissolve(0.25)
    voice audio.yyoshi_vsg18_line21
    yo "I know that’s a long time from now, but… when it happens, you can count on me to stay with you here!"

    voice audio.ygoro_vsg18_line23
    g "If that’s the case, then I’ll support you while you reach for your dream."

    voice audio.ygoro_vsg18_line24
    g "I’ll keep this camp alive and make it bigger than you ever imagined it could be."

    voice audio.ygoro_vsg18_line25
    g "Until then, I’ll be right here waiting."

    voice audio.yyoshi_vsg18_line22
    yo "We have to make a promise!"

    show cgg8 1 with Dissolve(0.25)
    voice audio.yyoshi_vsg18_line23
    yo "One day, I’ll be right back here, and we’ll be together again!"

    voice audio.ygoro_vsg18_line26
    g "No matter what happens, we’ll stay strong and keep doing our best until that day comes."

    show cgg8 2 with Dissolve(0.25)
    voice audio.yyoshi_vsg18_line24
    yo "Partners?"

    voice audio.ygoro_vsg18_line27
    g "Partners."

    hide screen location
    hide screen timeline
    hide screen quick_menu
    $quick_menu = False
    scene cg white with Dissolve(2.0)

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black
    $past_scene = False
    hide screen location
    hide screen timeline
    hide screen quick_menu
    $quick_menu = False
    with fade
    play sound sleeping_time
    $ time_transition_night_to_day_winter()
    $ renpy.pause (2.0, hard=True)
    jump day5_goro
