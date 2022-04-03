label day9_aiden_ge_pe:

    $ location = location_rooftop
    show screen location
    show screen timeline
    show screen quick_menu
    $ quick_menu = True

    scene cga10 1 with fade
    play bgsound sfxloop_windy loop

    a "..."
    $ renpy.pause (2.0, hard=True)

    show cga10 2 with Dissolve(0.25)
    voice audio.aiden_vsa21_line1
    a "Dad..."

    voice audio.aiden_vsa21_line2
    a "What should I do...?"

    show cg_fade at truecenter
    show fxa12 at fx_pos
    with Dissolve(0.25)

    voice audio.yoshi_vsa21_line1
    yo "A-Ah, there you are…!"

    voice audio.aiden_vsa21_line3
    a "…Yoshi?"

    voice audio.yoshi_vsa21_line2
    yo "I thought I’d find you here…!"

    voice audio.aiden_vsa21_line4
    a "Y-Yeah! I was just getting some air…!"

    voice audio.yoshi_vsa21_line3
    yo "Mind if I come up there?"

    voice audio.aiden_vsa21_line5
    a "S-Sure…"

    scene cg black
    hide screen location
    hide screen timeline
    hide screen quick_menu
    $quick_menu = False
    with fade
    $ renpy.pause (2.0, hard=True)

    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene cga10 3 with Dissolve(0.25)
    play music buddy_oath_aiden_sad loop

    voice audio.aiden_vsa21_line6
    a "A-Are you sure you wanna stay up here with me…? It’s pretty cold…"

    voice audio.yoshi_vsa21_line4
    yo "I’ll be alright, but what about you?"

    voice audio.aiden_vsa21_line7
    a "I’m fine. Today’s not as cold as yesterday."

    voice audio.yoshi_vsa21_line5
    yo "That’s good…"

    show cga10 4 with Dissolve(0.25)
    a "..."

    show cga10 5 with Dissolve(0.25)
    voice audio.yoshi_vsa21_line6
    yo "Hey, Aiden, I… "

    voice audio.yoshi_vsa21_line7
    yo "…I’m sorry about being so persistent earlier."

    voice audio.yoshi_vsa21_line8
    yo "I was so focused on trying to encourage you about the offer, even though I knew it was bothering you."

    show cga10 6 with Dissolve(0.25)
    voice audio.aiden_vsa21_line8
    a "I-It’s okay, Yoshi… I knew you and everyone else were only trying to help."

    voice audio.aiden_vsa21_line9
    a "I’m really sorry for the way I lashed out, too…"

    voice audio.aiden_vsa21_line10
    a "I didn’t mean to walk out on you like that, I just panicked ’cause I didn’t want to say anything worse…"

    show cga10 7 with Dissolve(0.25)
    voice audio.yoshi_vsa21_line9
    yo "It's not your fault, Aiden... I was being insensitive to your feelings, after all..."

    voice audio.aiden_vsa21_line11
    a "If I had only told you sooner that I wasn't gonna accept the offer, we wouldn't have argued..."

    voice audio.aiden_vsa21_line12
    a "Even though I felt strongly about my choice, I couldn’t admit to you that I was letting it go like that."

    voice audio.aiden_vsa21_line13
    a "Especially after seeing how excited you were for me. I didn’t want to let you down…"

    show cga10 8 with Dissolve(0.25)
    voice audio.yoshi_vsa21_line10
    yo "I understand…"

    voice audio.yoshi_vsa21_line11
    yo "But still, I was blinded by the opportunity, thinking it was best for you, regardless of the cost. "

    voice audio.yoshi_vsa21_line12
    yo "Now I realize that I wasn't even considering the reason you had for making that decision..."

    show cga10 9 with Dissolve(0.25)
    voice audio.aiden_vsa21_line14
    a "I know this is going to sound unreasonable, but…"

    voice audio.aiden_vsa21_line15
    a "As soon as I heard I’d be separated from you again, it just wasn’t worth it anymore."

    show cga10 10 with Dissolve(0.25)
    voice audio.aiden_vsa21_line16
    a "I… don’t want to be alone again…"

    show cga10 11 with Dissolve(0.25)
    voice audio.yoshi_vsa21_line13
    yo "I understand, Aiden… I was stupid to not have realized that…"

    voice audio.yoshi_vsa21_line14
    yo "When we got separated, I lost touch with you completely…"

    voice audio.yoshi_vsa21_line15
    yo "Being far away doesn’t excuse the fact that I didn’t put in the effort to try and reconnect…"

    voice audio.yoshi_vsa21_line16
    yo "I was wrapped up in my own goals, and just expected things to be the same when I came back."

    show cga10 12 with Dissolve(0.25)
    voice audio.aiden_vsa21_line17
    a "But I was the same, Yoshi… We had to go through our own lives, so I never blamed you for that…"

    voice audio.aiden_vsa21_line18
    a "In my head, I couldn’t reach out to you until I had something to show for myself."

    show cga10 13 with Dissolve(0.25)
    voice audio.yoshi_vsa21_line17
    yo "Even still… If I had only tried, then I would’ve known about what you had to go through…"

    voice audio.yoshi_vsa21_line18
    yo "It wasn’t even until today that I found out you and your dad had to leave Camp Buddy after the first term…"

    voice audio.aiden_vsa21_line19
    a "H-How did you know that?"

    voice audio.yoshi_vsa21_line19
    yo "From Sir Goro…"

    show cga10 14 with Dissolve(0.25)
    voice audio.yoshi_vsa21_line20
    yo "I-I understand why you kept that from me, though… "

    voice audio.yoshi_vsa21_line21
    yo "It was a difficult time for you, I can't even comprehend how much you both had to go through in the last few years..."

    show cga10 15 with Dissolve(0.25)
    a "..."

    voice audio.yoshi_vsa21_line22
    yo "I-I’m sorry… I knew you were trying your best to lock those memories away…"

    show cga10 16 with Dissolve(0.25)
    voice audio.aiden_vsa21_line20
    a "I didn’t think I could keep a secret like that forever either…"

    voice audio.aiden_vsa21_line21
    a "I’ll admit that times were tough back then…"

    voice audio.aiden_vsa21_line22
    a "As soon as we left Camp Buddy, Dad and I had to fend for ourselves again, and he kept trying to push himself to work despite being sick..."

    voice audio.aiden_vsa21_line23
    a "He worked twice as hard, wanting to make sure that we didn't end up in the life we had before."

    show cga10 17 with Dissolve(0.25)
    voice audio.aiden_vsa21_line24
    a "But it only made his health worse, and he still wasn't making enough to afford his medication..."

    voice audio.aiden_vsa21_line25
    a "Just like he'd given up on his dream before, he was going to give himself up for me, and I couldn't let that happen..."

    voice audio.aiden_vsa21_line26
    a "After everything I learned at Camp Buddy and the way you believed in me, I wanted to prove how capable I could be."

    show cga10 18 with Dissolve(0.25)
    voice audio.aiden_vsa21_line27
    a "So, I asked Dad to let me take over..."

    voice audio.aiden_vsa21_line28
    a "I went out there and got all sorts of jobs to make enough money for the both of us, and to afford Dad’s medication."

    voice audio.aiden_vsa21_line29
    a "I’d come back home from a long day of work and still find the time to take care of Dad, and he’d always try to show me that he was happy."

    show cga10 19 with Dissolve(0.25)
    voice audio.aiden_vsa21_line30
    a "He never forgot to tell me how proud he was of me… And I was too."

    show cga10 20 with Dissolve(0.25)
    voice audio.aiden_vsa21_line31
    a "As difficult as our life was, the struggles felt worth it…"

    voice audio.yoshi_vsa21_line23
    yo "That’s one thing that never changed about Mr. Andre…"

    show cga10 21 with Dissolve(0.25)
    voice audio.aiden_vsa21_line32
    a "Yeah, Dad’s always been my role model…"

    voice audio.aiden_vsa21_line33
    a "He always managed to turn something bad around, and found a reason to appreciate the littlest things, despite his illness."

    show cga10 22 with Dissolve(0.25)
    voice audio.aiden_vsa21_line34
    a "His condition was bound to get worse over time, so as the years went by, the smile on Dad’s face began to fade away…"

    hide screen location
    hide screen timeline
    hide screen quick_menu
    $ quick_menu = False
    scene cg white with Dissolve(2.0)
    $past_scene = True

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black
    hide screen location
    hide screen timeline
    hide screen quick_menu
    $ quick_menu = False
    with fade
    $ renpy.pause (2.0, hard=True)

    $ location = location_hospital
    $ day = "??"
    $ time = timeline_timeday
    $ season = season_summer
    show screen location
    show screen timeline
    show screen quick_menu
    $ quick_menu = True
    scene cga11 1 with fade
    play bgsound sfxloop_heartmonitor loop
    play music buddy_oath_aiden_sad loop

    voice audio.yaiden_vsa22_line1
    a "Hey, Dad! Sorry, I had to work overtime again…! And I got stuck in a traffic jam too!"

    voice audio.andre_vsa22_line1
    u "Ah, welcome back, son… "

    show cga11 2 with Dissolve(0.25)
    voice audio.yaiden_vsa22_line2
    a "Sheesh… I feel bad, it’s almost midnight and you haven’t eaten yet… "

    voice audio.yaiden_vsa22_line3
    a "Anyway, lemme just heat this up so you can take your meds and—"

    show cga11 3 with Dissolve(0.25)
    voice audio.andre_vsa22_line2
    u "Aiden, wait…"

    voice audio.yaiden_vsa22_line4
    a "What’s the matter, Dad? Not feeling great tonight?"

    voice audio.andre_vsa22_line3
    u "N-No, it’s not that…"

    show cga11 4 with Dissolve(0.25)
    voice audio.andre_vsa22_line4
    u "It’s just… I’ve been thinking…"

    voice audio.yaiden_vsa22_line5
    a "About what…?"

    voice audio.andre_vsa22_line5
    u "It’s been over five years… and I’m only getting worse…"

    show cga11 5 with Dissolve(0.25)
    voice audio.yaiden_vsa22_line6
    a "Y-You’ll get better, Dad! If we just keep doing the treatments, there’s a chance you’ll recover…!"

    $ renpy.music.stop(channel='music', fadeout = 2.0)
    voice audio.andre_vsa22_line6
    u "Aiden… The doctors have already told us there’s no cure, and I’ll always have to be hooked up like this…"

    voice audio.yaiden_vsa22_line7
    a "Wh-What are you trying to say, Dad…?"

    play music buddy_oath_aiden_tragic loop
    voice audio.andre_vsa22_line7
    u "Even though the pain’s been around for so long, it just… hurts."

    show cga11 6 with Dissolve(0.25)
    voice audio.andre_vsa22_line8
    u "It hurts to see you wasting your life on me like this with every passing day…"

    voice audio.andre_vsa22_line9
    u "You still have a future ahead of you, and I’m near the end of the road…"

    show cga11 7 with Dissolve(0.25)
    voice audio.yaiden_vsa22_line8
    a "Don’t say that, Dad! I’m your son, and I’m gonna take care of you no matter what…!!"

    voice audio.andre_vsa22_line10
    u "I know that, Aiden… but…"

    show cga11 8 with Dissolve(0.25)
    voice audio.andre_vsa22_line11
    u "I’m your father and I’m the one you’re supposed to rely on…"

    voice audio.andre_vsa22_line12
    u "Instead, I’m burdening you like this… because I couldn’t take care of my own health…"

    voice audio.yaiden_vsa22_line9
    a "Wh-What? Th-That’s not true, Dad! "

    voice audio.yaiden_vsa22_line10
    a "You wouldn’t have gotten sick if you didn’t work so hard to take care of me!"

    show cga11 9 with Dissolve(0.25)
    voice audio.andre_vsa22_line13
    u "But even with all that… I was never able to give you the life you deserved."

    voice audio.andre_vsa22_line14
    u "All we were doing was just surviving before we found Camp Buddy."

    show cga11 10 with Dissolve(0.25)
    voice audio.andre_vsa22_line15
    u "It was there that I saw you begin to have friends… dreams… and hope for the future…"

    voice audio.andre_vsa22_line16
    u "And yet, I dragged you away from it… because I didn’t want us to be so helpless, always relying on others…"

    show cga11 11 with Dissolve(0.25)
    voice audio.andre_vsa22_line17
    u "I really thought I could make it work, and give that kind of life to you myself, but here I am…"

    show cga11 12 with Dissolve(0.25)
    voice audio.andre_vsa22_line18
    u "It was selfish… and I truly regret it…"

    show cga11 13 with Dissolve(0.25)
    voice audio.andre_vsa22_line19
    u "I-I’m so sorry, Aiden… My son… "

    voice audio.yaiden_vsa22_line11
    a "Dad… It’s not your fault… "

    show cga11 14 with Dissolve(0.25)
    voice audio.yaiden_vsa22_line12
    a "And I’m still here…"

    voice audio.yaiden_vsa22_line13
    a "So, p-please… Don’t give up… "

    show cga11 15 with Dissolve(0.25)
    voice audio.andre_vsa22_line20
    u "I’m not giving up, Aiden…"

    voice audio.andre_vsa22_line21
    u "But I need you to understand… "

    show cga11 16 with Dissolve(0.25)
    voice audio.andre_vsa22_line22
    u "…That I have to let go."

    voice audio.yaiden_vsa22_line14
    a "Wh-What…?"

    show cga11 17 with Dissolve(0.25)
    voice audio.andre_vsa22_line23
    u "I want you to have your own life…"

    voice audio.andre_vsa22_line24
    u "To do the things you like…  be with people you love… and find what truly makes you happy…"

    show cga11 18 with Dissolve(0.25)
    voice audio.andre_vsa22_line25
    u "I’ll always be your father, and you’ll always be my son… So don’t be afraid…"

    show cga11 19 with Dissolve(0.25)
    voice audio.yaiden_vsa22_line15
    a "D-Dad… No… Please… Stop…."

    voice audio.andre_vsa22_line26
    u "I-I’m very… very tired, Aiden…"

    show cga11 20 with Dissolve(0.25)
    voice audio.andre_vsa22_line27
    u "Despite all of my shortcomings and the mistakes I’ve made… you were the best thing that ever happened to me…"

    voice audio.andre_vsa22_line28
    u "So please… grant me this last wish…"

    show cga11 21 with Dissolve(0.25)
    $ renpy.pause (1.0, hard=True)
    voice audio.andre_vsa22_line29
    u "Let’s go home… "

    show cga11 22 with Dissolve(0.25)
    voice audio.andre_vsa22_line30
    u "We’ll cook our favorite dish… Eat together like a family… Like we used to, Aiden…"

    show cga11 23 with Dissolve(0.25)
    voice audio.yaiden_vsa22_line16
    a "*cries*"

    hide screen location
    hide screen timeline
    hide screen quick_menu
    $ quick_menu = False
    scene cg white with Dissolve(4.0)
    $past_scene = False

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black
    hide screen location
    hide screen timeline
    hide screen quick_menu
    $ quick_menu = False
    with fade
    $ renpy.pause (2.0, hard=True)

    $ location = location_lake
    $ day = "83"
    $ time = timeline_timenight
    $ season = season_winter
    show screen location
    show screen timeline
    show screen quick_menu
    $ quick_menu = True

    scene cga10 23 with fade
    play music buddy_oath_aiden_sad
    play bgsound sfxloop_windy loop

    voice audio.aiden_vsa21_line35
    a "So, we did… and then Dad’s smile finally came back."

    voice audio.aiden_vsa21_line36
    a "We spent as much time together as we could, doing things we loved."

    show cga10 24 with Dissolve(0.25)
    voice audio.aiden_vsa21_line37
    a "Up until his final moments…"

    $ renpy.pause (2.0, hard=True)
    show cga10 25 with Dissolve(0.25)
    voice audio.aiden_vsa21_line38
    a "And when it finally happened… I thought I was going to be fine…"

    show cg_fade at truecenter
    show fxa13 at fx_pos
    with Dissolve(0.25)
    voice audio.aiden_vsa21_line39
    a "But I wasn’t."

    voice audio.aiden_vsa21_line40
    a "For a long time, I was in a really dark place, where everything felt meaningless…"

    voice audio.aiden_vsa21_line41
    a "I started hating myself for letting Dad go… And for being the reason he had to suffer his whole life…"

    voice audio.aiden_vsa21_line42
    a "The only thing I could think about was that everything happened because of how useless I was, and how I had no place in the world…"

    voice audio.aiden_vsa21_line43
    a "For a while, I did the exact thing my dad feared… I wasted away."

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.pause (3.0, hard=True)

    voice audio.aiden_vsa21_line44
    a "But then I remembered…"

    hide cg_fade
    hide fxa13
    show cga8 3
    with Dissolve(0.25)

    voice audio.aiden_vsa21_line45
    a "The promise we made to each other."
    play music buddy_oath_musicbox loop

    voice audio.aiden_vsa21_line46
    a "When I thought I had lost everything, it was the one thing that gave me hope."

    voice audio.aiden_vsa21_line47
    a "I promised you that I’d make something out of myself, and that was what Dad would’ve wanted for me too…"

    voice audio.aiden_vsa21_line48
    a "So I started picking myself back up."

    voice audio.aiden_vsa21_line49
    a "I decided that I’d do whatever it took to be the best version of myself by the time we met again."

    show cga10 26 with Dissolve(0.25)
    voice audio.aiden_vsa21_line50
    a "Now that I’m here and I have you, it’s everything I could have ever asked for…"

    voice audio.aiden_vsa21_line51
    a "And that’s why this time… I’m finally going to fight for what makes me truly happy."

    show cga10 27 with Dissolve(0.25)
    voice audio.aiden_vsa21_line52
    a "And that’s to be with you, Yoshi."

    voice audio.yoshi_vsa21_line24
    yo "Aiden…"

    voice audio.yoshi_vsa21_line25
    yo "I finally see now…"

    voice audio.yoshi_vsa21_line26
    yo "I hope you can forgive me for not understanding…"

    voice audio.yoshi_vsa21_line27
    yo "And for not being there when you needed me the most…"

    voice audio.yoshi_vsa21_line28
    yo "I can’t let myself focus on what I couldn’t do for you then…"

    show cga10 28 with Dissolve(0.25)
    voice audio.yoshi_vsa21_line29
    yo "You’re here now and there’s still so much I can do."

    voice audio.yoshi_vsa21_line30
    yo "I won’t ever risk letting us be apart again…"

    voice audio.yoshi_vsa21_line31
    yo "Because I want you to know, that your happiness is all I’ve ever wanted too."

    show cga10 29 with Dissolve(0.25)
    voice audio.yoshi_vsa21_line32
    yo "And this time around, I’ll make sure to protect your smile forever."

    show cga12 with Dissolve(0.25)
    yo "{i}(This is my new oath to you…){/i}"

    $ renpy.pause (1.0, hard=True)
    yo "{i}Under the shooting stars, our lips touched, with a newfound promise to each other that we’d always be together.{/i}"

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black
    hide screen location
    hide screen timeline
    hide screen quick_menu
    $ quick_menu = False
    with fade
    play sound sleeping_time
    $ time_transition_night_to_day_winter3()
    $ renpy.pause (2.0, hard=True)

    jump day10_aiden_gepe
