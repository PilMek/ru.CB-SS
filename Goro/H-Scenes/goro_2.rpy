label day3_goro_2:
    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black
    hide screen location
    hide screen timeline
    hide screen quick_menu
    $quick_menu = False
    with fade
    $ renpy.pause (1.0, hard=True)

    $ location = location_hotelsauna
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene sxg2 1 with fade
    play music on_the_edge loop

    voice audio.yoshi_vsxg2_line1
    yo "Mmppff!"
    yo "{i}(Before I could say anything, Sir Goro suddenly grabbed me by the neck and placed his lips on mine.){/i}"

    show sxg2 2 with Dissolve(0.25)
    voice audio.goro_vsxg2_line1
    g "Mmnnhh…. Mmhhmmm…"
    yo "{i}(He pushed his tongue into my mouth, wrapping it around mine and stealing my breath away…){/i}"
    yo "{i}(Our bodies were burning up from the heat of the room, our sweat running down our faces and mixing into our kiss.){/i}"

    show sxg2 3 with Dissolve(0.25)
    voice audio.yoshi_vsxg2_line2
    yo "Mmhh… Hmh…"
    yo "{i}(Sir Goro slipped down my towel, grabbing onto my already hardened dick… ){/i}"
    yo "{i}(Glancing down, I could see that he was just as stiff, his dick bulging so massively underneath that tiny, wet towel.){/i}"

    show sxg2 4 with Dissolve(0.25)
    yo "{i}(I couldn’t help but reach towards it. Sir Goro’s cock was hard as a rock and its entire girth barely fit in my grasp.){/i}"

    voice audio.goro_vsxg2_line2
    g "H-Heh… Hehehe…"

    voice audio.yoshi_vsxg2_line3
    yo "Haaa... Sir Goro…"

    show sxg2 5 with Dissolve(0.25)
    voice audio.goro_vsxg2_line3
    g "This is what you wanted all along, isn’t it Yoshinori…?"

    if deny_goro == True:
        voice audio.goro_vsxg2_line4a
        g "Fooling around with your boss, you say? I know you want more…"
    else:
        voice audio.goro_vsxg2_line4b
        g "Not even denying to that masseur what you really think of me…"
    yo "{i}(I was so distracted earlier that I didn’t realize Sir Goro noticed how I answered the masseur’s question…){/i}"
    yo "{i}(I guess even after all the years I’ve looked up to him, I couldn’t admit to myself how I’ve always had a thing for him…){/i}"

    voice audio.goro_vsxg2_line5
    g "Don’t give me that helpless look… I’m all yours, Yoshinori…"

    if score_top > score_bot:
        show sxg2 6a with Dissolve(0.25)
        voice audio.goro_vsxg2_line6b
        g "Mmmhh…"
        yo "{i}(I let my thoughts go and grabbed onto Sir Goro tighter, pushing my lips back onto his.){/i}"
    else:
        show sxg2 6a with Dissolve(0.25)
        voice audio.yoshi_vsxg2_line4a
        yo "Mmmm--!!"
        yo "{i}(Before I could think anymore, Sir Goro held onto me tighter and pressed his lips onto mine again.){/i}"

    yo "{i}(I could feel his beard tickling my chin, and his firm chest push against my arm…){/i}"
    yo "{i}(As we continued to get carried away in the moment, I couldn’t control myself anymore and made the next move.){/i}"

    $working = False
    $shuffle_menu()
    menu():
        yo "{i}(As we continued to get carried away in the moment, I couldn’t control myself anymore and made the next move.){/i}{fast}"
        "Suck his lips.":
            show sxg2 7a with Dissolve(0.25)
            $working = True
            $score_top -= 1
            $score_bot += 1
            voice audio.yoshi_vsxg2_line5a
            yo "Mmm~!"
            yo "{i}(I started to suck on Sir Goro’s lips, and he responded with the same…){/i}"

            voice audio.goro_vsxg2_line7a
            g "Hmmhh… Mmhh!"
            yo "{i}(Sir Goro began to jerk my dick faster while I continued to pull on his lips…){/i}"
            yo "{i}(My body began to move on its own, thrusting to match Sir Goro’s hand.){/i}"
        "Stick your tongue out.":
            show sxg2 7b with Dissolve(0.25)
            $working = True
            $score_bot += 2
            voice audio.yoshi_vsxg2_line5b
            yo "Haaahh~!"
            yo "{i}(I stuck my tongue out, connecting with Sir Goro’s as we greedily licked each other…){/i}"

            voice audio.goro_vsxg2_line7b
            g "Haah… Ahhh…"
            yo "{i}(Sir Goro began to jerk my dick faster while we continued to slide our tongues together….){/i}"
            yo "{i}(My body began to move on its own, thrusting to match Sir Goro’s hand.){/i}"
        "Bite his lips.":
            show sxg2 7c with Dissolve(0.25)
            $working = True
            $score_top += 1
            $score_bot -= 1
            voice audio.goro_vsxg2_line7c
            g "Khhh…"
            yo "{i}(I gently bit down onto Sir Goro’s lips, feeling their firm but soft texture, along with his warm breath steaming out of his nose…){/i}"
            yo "{i}(It didn’t take long for Sir Goro to take over, and bite my lips back){/i}"

            voice audio.goro_vsxg2_line8c
            g "Khh… Hnghh…!"
            yo "{i}(Sir Goro’s hips began to thrust, matching the motions of my hand.){/i}"
        "Push your tongue deeper.":
            show sxg2 7d with Dissolve(0.25)
            $working = True
            $score_top += 2
            voice audio.goro_vsxg2_line7d
            g "Mmgkk…!"
            yo "{i}(I pushed my tongue deeper into Sir Goro’s mouth, and heard him startle slightly. ){/i}"
            yo "{i}(It didn’t take long for Sir Goro to take over, and push his tongue deeper than I did.){/i}"

            voice audio.goro_vsxg2_line8d
            g "Mmhh…! Hmmhh..!!"
            yo "{i}(Sir Goro’s hips began to thrust, matching the motions of my hand.){/i}"

    yo "{i}(I felt both of our dicks reacting strongly as we continued.){/i}"

    $ position = 0
    if score_bot == score_top:
        $ position = renpy.random.randint(1, 2)

    if score_bot > score_top or position == 1:
        show sxg2 8 with Dissolve(0.25)
        yo "{i}(Our gazes were locked passionately, even as drool slipped down our cheeks.){/i}"

        voice audio.goro_vsxg2_line9a
        g "I want you, Yoshinori…"

        scene cg black with fade
        yo "{i}(Sir Goro released his grasp, laying down across the wood and giving me a complete view of his entire body…){/i}"

        hide screen location
        hide screen timeline
        hide screen quick_menu
        $ quick_menu = False
        $ say_box = False
        $ fp_stage = 'mgg1_f'
        $ success_jumpto = 'day3_goro_3d'
        $ failed_jumpto = 'day3_goro_aftersx'
        jump fp

    elif score_top > score_bot or position == 2:
        show sxg2 8 with Dissolve(0.25)
        yo "{i}(Our gazes were locked passionately, even as drool slipped down our cheeks.){/i}"

        voice audio.yoshi_vsxg2_line6b
        yo "I want you so badly, Sir Goro…"

        scene cg black with fade
        yo "{i}(Sir Goro released his grasp, laying down on his side across the wood, letting me worship his body…){/i}"

        hide screen location
        hide screen timeline
        hide screen quick_menu
        $ quick_menu = False
        $ say_box = False
        $ fp_stage = 'mgg1_b'
        $ success_jumpto = 'day3_goro_3s'
        $ failed_jumpto = 'day3_goro_aftersx'
        jump fp
