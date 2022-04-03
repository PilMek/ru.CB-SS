label day3_aiden_2:
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

    $ location = location_hotelclub
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene sxa2 1 with fade
    play bgsound sfxloop_nightclub loop
    play music on_the_edge loop
    voice audio.yoshi_vsxa2_line1
    yo "Mmppff!"
    yo "{i}(Before I could finish talking, Aiden suddenly climbed on top of me and placed his lips on mine.){/i}"

    show sxa2 2 with Dissolve(0.25)
    voice audio.aiden_vsxa2_line1
    a "Mmnnhh~! Mmmh~"
    yo "{i}(Aiden slammed his tongue into my mouth, wrapping it around mine and stealing my breath away…){/i}"
    yo "{i}(Even though he was almost naked, Aiden was incredibly warm from all the liquor we’d been drinking… I could feel the heat coming off of him, as he rubbed his crotch against my own.){/i}"

    show sxa2 3 with Dissolve(0.25)
    voice audio.yoshi_vsxa2_line2
    yo "Mmhh… Hmh…"
    yo "{i}(Aiden began to unbutton my shirt and pants while continuing to press his mouth against mine…){/i}"
    yo "{i}(Glancing down, I could see that he was already hard, his dick bulging in the tight jockstrap.){/i}"

    show sxa2 4 with Dissolve(0.25)
    voice audio.aiden_vsxa2_line2
    a "Fuck, Yoshi… I’m so horny right now… "

    voice audio.yoshi_vsxa2_line3
    yo "E-Everyone can see us from here, Aiden…"

    voice audio.aiden_vsxa2_line3
    a "I don’t give a damn, Yoshi… They can watch us for all I care…"

    voice audio.aiden_vsxa2_line4
    a "It just makes it more exciting, right…?"

    if aiden_deny == True:
        voice audio.aiden_vsxa2_line5a
        a "I’m gonna prove what you said to that bartender isn’t true!"
    else:
        voice audio.aiden_vsxa2_line5b
        a "After all, didn’t you say to that bartender a while ago that we’re together? This’ll show them~"

    yo "{i}(We’d been having such a crazy night so far that I didn’t realize Aiden took what I had said to the bartender to heart… ){/i}"
    yo "{i}(I guess even with all those years we’ve known and hung out with each other, we never even tapped into the idea of us having a label…){/i}"

    voice audio.aiden_vsxa2_line6
    a "What’s with that look?  Let’s just have fun tonight, Yoshi~"

    if score_top > score_bot:
        show sxa2 5a with Dissolve(0.25)
        voice audio.yoshi_vsxa2_line4a
        yo "Mmmm--!!"
        yo "{i}(Before I could think anything else, Aiden grasped my cheeks and pressed his lips onto mine again.){/i}"

    else:
        show sxa2 5b with Dissolve(0.25)
        voice audio.aiden_vsxa2_line7b
        a "Mmmm--!!"
        yo "{i}(I let my thoughts go and grabbed Aiden, pulling him forward into another kiss.){/i}"

    yo "{i}(I could taste the alcohol in his mouth, and I knew Aiden was too drunk and heated up to stop…){/i}"
    yo "{i}(As we continued to get carried away in the moment, I wanted to take charge and make the next move.){/i}"

    $ working = False
    $ shuffle_menu()
    menu():
        yo "{i}(As we continued to get carried away in the moment, I wanted to take charge and make the next move.){/i}{fast}"
        "Suck his lips.":
            $ working = True
            $ score_top -= 1
            $ score_bot += 1
            show sxa2 6a with Dissolve(0.25)
            voice audio.yoshi_vsxa2_line5a
            yo "Mmm…!"
            yo "{i}(I started to suck on Aiden’s lips, and he responded with the same…){/i}"

            show sxa2 7a with Dissolve(0.25)
            voice audio.aiden_vsxa2_line9a
            a "Hmmhh… Mmhh!"
            yo "{i}(Aiden began to grind his crotch against mine while I continued to pull on his lips… ){/i}"

            yo "{i}(My body began to move on its own, humping to match Aiden’s motions.){/i}"
            yo "{i}(I felt both of our dicks twitching strongly as we continued to frot together.){/i}"
        "Stick your tongue out.":
            $ working = True
            $ score_bot += 2
            show sxa2 6b with Dissolve(0.25)
            voice audio.yoshi_vsxa2_line5b
            yo "Haaahh…"
            yo "{i}(I stuck my tongue out, connecting with Aiden’s as we greedily licked each other…){/i}"

            show sxa2 7b with Dissolve(0.25)
            voice audio.aiden_vsxa2_line9b
            a "Haah… Ahhh…"
            yo "{i}(Aiden began to grind his crotch against mine while we continued to slide our tongues together….){/i}"

            yo "{i}(My body began to move on its own, humping to match Aiden’s motions.){/i}"
            yo "{i}(I felt both of our dicks twitching strongly as we continued to frot together.){/i}"
        "Bite his lips.":
            $ working = True
            $ score_top += 1
            $ score_bot -= 1
            show sxa2 6c with Dissolve(0.25)
            voice audio.aiden_vsxa2_line8c
            a "Khh…!!"
            yo "{i}(I gently bit down onto Aiden’s lips, feeling their firm but soft texture, along with his warm breath steaming out of his nose…){/i}"

            show sxa2 7c with Dissolve(0.25)
            yo "{i}(I started grinding my crotch against Aiden’s, while also biting down onto his lip a little harder than before…){/i}"

            voice audio.aiden_vsxa2_line9c
            a "Khh… Hnghh…!"

            yo "{i}(Aiden’s body began to move on its own, humping to match my motions.){/i}"
            yo "{i}(I felt both of our dicks twitching strongly as we continued to frot together.){/i}"
        "Push your tongue deeper.":
            $ working = True
            $ score_top += 2
            show sxa2 6d with Dissolve(0.25)
            voice audio.aiden_vsxa2_line8d
            a "Nnghk…!!"
            yo "{i}(I pushed my tongue deeper towards Aiden’s throat, and heard him gulp slightly, stopping himself from gagging…){/i}"

            show sxa2 7d with Dissolve(0.25)
            yo "{i}(I started grinding my crotch against Aiden’s, while shoving my tongue even further into him…){/i}"

            voice audio.aiden_vsxa2_line9d
            a "Mmhh…! Hmmhh..!!"

            yo "{i}(Aiden’s body began to move on its own, humping to match my motions.){/i}"
            yo "{i}(I felt both of our dicks twitching strongly as we continued to frot together.){/i}"

    $a3mini = False
    $ position = 0
    if score_bot == score_top:
        $ position = renpy.random.randint(1, 2)

    if score_bot > score_top or position == 1:
        show sxa2 8a with Dissolve(0.25)
        yo "{i}(Our gazes were locked passionately, even as drool slipped down our cheeks.){/i}"
        voice audio.aiden_vsxa2_line10a
        a "I want you so bad, Yoshi…"

        scene cg black with fade
        yo "{i}(Aiden climbed off of me, laying down across the couch giving me a complete view of his whole body.){/i}"

        hide screen location
        hide screen timeline
        hide screen quick_menu
        $ quick_menu = False
        $ say_box = False
        $ fp_stage = 'mga1_f'
        $ success_jumpto = 'day3_aiden_3t'
        $ failed_jumpto = 'day3_aiden_aftersx'
        jump fp

    elif score_top > score_bot or position == 2:
        show sxa2 8b with Dissolve(0.25)
        yo "{i}(Our gazes were locked passionately, even as drool slipped down our cheeks.){/i}"
        voice audio.yoshi_vsxa2_line6b
        yo "I can’t hold it anymore, Aiden… I want you…"

        scene cg black with fade
        yo "{i}(I grabbed Aiden and pulled him off of me, laying him down across the couch…){/i}"
        yo "{i}(He arched his back in response, giving me a complete view of his backside…){/i}"

        hide screen location
        hide screen timeline
        hide screen quick_menu
        $ quick_menu = False
        $ say_box = False
        $ fp_stage = 'mga1_b'
        $ success_jumpto = 'day3_aiden_3b'
        $ failed_jumpto = 'day3_aiden_aftersx'
        jump fp
