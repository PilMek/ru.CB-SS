label day9_goro_gepe:
    hide yoshi2_biker
    hide yoshi2 sad4
    show yoshi_biker at left2
    show yoshi worry2 at left2
    voice audio.yoshi_vsg24_line1
    yo "What was the reason then…?"

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    scene cgg11 1 with fade
    play music buddy_oath_goro_sad loop
    play bgsound sfxloop_windy loop
    voice audio.goro_vsg24_line1
    g "I… I’m already content…"

    voice audio.goro_vsg24_line2
    g "To me, Camp Buddy is already perfect the way it is…"

    voice audio.goro_vsg24_line3
    g "To start, we’ve received so many amazing chances already and regained what we nearly lost the previous term…"

    voice audio.goro_vsg24_line4
    g "Now we’ve made it even bigger in such a short period of time… and to receive yet another opportunity was just so unexpected... "

    show cgg11 2 with Dissolve(0.25)
    voice audio.goro_vsg24_line5
    g "And honestly…. It’s something I don’t aspire for anymore…"

    voice audio.yoshi_vsg24_line2
    yo "Wh-What do you mean…?"

    show cgg11 3 with Dissolve(0.25)
    voice audio.goro_vsg24_line6
    g "Don’t get me wrong… I love Camp Buddy with all my heart. It’s my lifelong dream that I had the honor of sharing with everyone, especially you…"

    voice audio.goro_vsg24_line7
    g "But… I’ve been holding on to this place for so long, believing it’s the only thing that makes all of us happy…"

    voice audio.goro_vsg24_line8
    g "Now, after getting the chance to be closer with you, I started to see things differently…"

    show cgg11 4 with Dissolve(0.25)
    voice audio.yoshi_vsg24_line3
    yo "B-But… I don’t understand… This is what we’ve all been working for."

    voice audio.yoshi_vsg24_line4
    yo "It’s just all too sudden… after everything we’ve been through…"

    voice audio.yoshi_vsg24_line5
    yo "What changed…?"

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    show cgg11 5 with Dissolve(0.25)
    $ renpy.pause (1.0, hard=True)
    g "..."

    show cgg11 6 with Dissolve(0.25)
    voice audio.goro_vsg24_line9
    g "I’m afraid."

    voice audio.yoshi_vsg24_line6
    yo "O-Of what…?"

    voice audio.goro_vsg24_line10
    g "I’m afraid of the past repeating itself…"

    show cgg11 7 with Dissolve(0.25)
    voice audio.goro_vsg24_line11
    g "I’m afraid that I’d lose someone I love again…"

    play music buddy_oath_goro_tragic loop
    yo "...!"

    show cgg11 8 with Dissolve(0.25)
    voice audio.goro_vsg24_line12
    g "When I was dealing with all the problems with my ex-wife, I didn’t feel the full extent of the pain because you were there to distract me…"

    voice audio.goro_vsg24_line13
    g "Then you left to pursue your dream to become a scoutmaster, and the effects of my divorce finally hit me."

    show cgg11 9 with Dissolve(0.25)
    voice audio.goro_vsg24_line14
    g "All of a sudden there was a hole in my heart…"
    yo "..."

    show cgg8 3 with Dissolve(0.25)
    voice audio.goro_vsg24_line15
    g "All that was left in me was the promise that we made to each other, so I did everything in my power to make Camp Buddy the best it could be…"

    voice audio.goro_vsg24_line16
    g "I owe that place so much for allowing me to become a better version of myself, to bond with my daughter, and most importantly… to have met you."

    hide cgg11 9
    show cgg11 10 with Dissolve(0.25)
    voice audio.goro_vsg24_line17
    g "In my mind, I was going to make it big and successful by the time you came back… thinking it would make you, my daughter, and myself happy."

    voice audio.goro_vsg24_line18
    g "I put all my blood, sweat, and tears into it… expanding over and over with blind ambition, until it grew into something I could barely handle…"

    show cg_fade at truecenter
    show fxg12 at fx_pos
    with dissolve

    voice audio.goro_vsg24_line19
    g "What I didn’t realize was that I was doing it to cover the pain inside…"

    voice audio.goro_vsg24_line20
    g "I never knew how truly lonely I was… "

    voice audio.goro_vsg24_line21
    g "I tried numbing myself from any emotion, convinced that I had to stay strong and tough, always…"

    voice audio.goro_vsg24_line22
    g "I even pushed my own daughter away, assigning her to a different place, and shutting down any attempts she made to reach me…"

    voice audio.goro_vsg24_line23
    g "I let no one see my weakness, and it started a vicious cycle where I grew more and more bitter each day for letting you go…"

    voice audio.goro_vsg24_line24
    g "The dream we had lost all its spirit, turning the camp into a soulless business, and I completely lost touch of what it was supposed to be…"

    hide cg_fade
    hide fxg12
    show cgg11 11
    with Dissolve(1.0)
    voice audio.yoshi_vsg24_line7
    yo "I… didn’t know you had to go through all that, Goro…"

    voice audio.goro_vsg24_line25
    g "Even when we were reunited, it took me so long to break the walls I had built up… "

    show cgg11 12 with Dissolve(0.25)
    voice audio.goro_vsg24_line26
    g "But with time… you slowly mended my broken heart… "

    voice audio.goro_vsg24_line27
    g "And now, we’ve grown into something I could only wish for…"

    voice audio.goro_vsg24_line28
    g "I don’t want to risk letting you go again… because everything I want is already here..."

    show cgg11 13 with Dissolve(0.25)
    voice audio.yoshi_vsg24_line8
    yo "You’re right… We’ve already reached our dream… We’re together again and leading the camp side by side."

    voice audio.goro_vsg24_line29
    g "I was hoping you would feel the same way once you heard my reason… but I still should’ve told you."

    voice audio.yoshi_vsg24_line9
    yo "I think I understand now… You don’t deserve to suffer like that again, just because we aren’t satisfied with what we have…"

    show cgg11 14 with Dissolve(0.25)
    voice audio.goro_vsg24_line30
    g "I’m very grateful for all the amazing things that happened and the lessons I’ve learned along the way, but I’m more than satisfied with what we’ve achieved…"

    voice audio.goro_vsg24_line31
    g "It’s not that I’m giving up on our dream, but that I’m ready to move on to a different chapter… "

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    show cgg11 15 with Dissolve(0.25)
    voice audio.goro_vsg24_line32
    g "And that chapter is with you, Yoshinori…"

    voice audio.goro_vsg24_line33
    g "For once in my life, the path is clear and I know what I want for the future…"

    voice audio.yoshi_vsg24_line10
    yo "Wh-What is it…?"

    show cgg11 16 with Dissolve(0.25)
    voice audio.goro_vsg24_line34
    g "Not only have you taught me how to love again, but you also showed me what it’s like to be truly loved…"

    voice audio.goro_vsg24_line35
    g "I know this might be sudden... But I’ve been preparing for this moment for a long time, and only today did I have the courage to do anything…"

    voice audio.goro_vsg24_line36
    g "I’ve had these feelings for so long… And I’m ready for them to be set in stone..."

    voice audio.goro_vsg24_line37
    g "Yoshinori…"

    show cg_fade at truecenter
    show fxg13 at fx_pos
    with dissolve

    play music buddy_oath_musicbox loop
    voice audio.goro_vsg24_line38
    g "I want to live the rest of my life with you… To be partners in heart and soul…"
    yo "...!!"

    voice audio.goro_vsg24_line39
    g "Will you be forever by my side…?"

    voice audio.yoshi_vsg24_line11
    yo "Yes…! "

    scene cgg12 1 with Dissolve(1.0)
    yo "{i}(As I accepted Goro’s proposal, I was overwhelmed with emotion…){/i}"
    yo "{i}(I never thought this moment would come…){/i}"
    yo "{i}(For as long as I’ve known him, Goro has always sacrificed for the sake of others and let go of his own happiness…){/i}"
    yo "{i}(Now, he’s finally pursuing something for himself… And to know that I’m what truly makes him happy, I couldn’t ask for anything more.){/i}"

    scene cgg12 2 with Dissolve(0.5)
    voice audio.goro_vsg24_line40
    g "I love you, Yoshinori…"

    voice audio.yoshi_vsg24_line12
    yo "I love you too…"

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
    $ time_transition_night_to_day_winter3()
    $ renpy.pause (2.0, hard=True)
    jump day10_goro_gepe
