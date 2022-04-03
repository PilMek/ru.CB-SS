label day9_aiden_we:
    $ day = "83"
    $ time = timeline_timenight
    $ location = location_lake
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    $ working = True
    scene bg_lake_winter_night with fade
    play bgsound sfxloop_windy loop

    show aiden2_winter at center
    show aiden2 upset1 at center
    a "..."

    show aiden2 sigh1 at center
    voice audio.aiden_vsa21_line1
    a "Dad..."

    show aiden2 worry5 at center
    voice audio.aiden_vsa21_line2
    a "What should I do…?"

    show aiden2_winter at left2
    show aiden2 worry5 at left2
    with move

    show yoshi_winter at right2
    show yoshi panic2 at right2
    voice audio.yoshi_vsa21_line1
    yo "A-Ah, there you are…!"

    show aiden2 panic4 at left2
    voice audio.aiden_vsa21_line3
    a "…Yoshi?"

    hide yoshi_winter
    hide yoshi panic2
    show yoshi2_winter at right2
    show yoshi2 sad4 at right2
    voice audio.yoshi_vsa21_line2
    yo "I thought I’d find you here…!"

    hide aiden2_winter
    hide aiden2 panic4
    show aiden_winter at left2
    show aiden upset6 at left2
    voice audio.aiden_vsa21_line4
    a "Y-Yeah! I was just getting some air…!"

    hide aiden_winter
    hide aiden upset6
    show aiden2_winter at left2
    show aiden2 worry2 at left2
    voice audio.aiden_vsa21c_line1
    a "A-Are you sure you wanna stay out here with me…? It’s pretty cold…"

    show yoshi2_winter at right2
    show yoshi2 worry3 at right2
    voice audio.yoshi_vsa21_line4
    yo "I’ll be alright, but what about you?"

    show aiden2 explain2 at left2
    voice audio.aiden_vsa21_line7
    a "I’m fine. Today’s not as cold as yesterday."

    show yoshi2 upset6 at right2
    voice audio.yoshi_vsa21_line5
    yo "That’s good…"

    show aiden2 sad5 at left2
    a "..."

    show yoshi2 upset3 at right2
    voice audio.yoshi_vsa21_line6
    yo "Hey, Aiden, I… "

    voice audio.yoshi_vsa21_line7
    yo "…I’m sorry about being so persistent earlier."

    show yoshi2 sigh3 at right2
    voice audio.yoshi_vsa21_line8
    yo "I was so focused on trying to encourage you about the offer, even though I knew it was bothering you."

    show aiden2 sigh1 at left2
    voice audio.aiden_vsa21_line8
    a "I-It’s okay, Yoshi… I knew you and everyone else were only trying to help."

    voice audio.aiden_vsa21_line9
    a "I’m really sorry for the way I lashed out, too…"

    show aiden2 sad4 at left2
    voice audio.aiden_vsa21_line10
    a "I didn’t mean to walk out on you like that, I just panicked ’cause I didn’t want to say anything worse…"

    show yoshi2 sad4 at right2
    voice audio.yoshi_vsa21b_line1
    yo "It's not your fault, Aiden... I know how big of a decision this is for you…"

    show yoshi2 worry2 at right2
    voice audio.yoshi_vsa21b_line2
    yo "But please let me help clear up your worries... and convince you why this opportunity is the best thing for you!"

    voice audio.yoshi_vsa21b_line3
    yo "And maybe for us…"

    show aiden2 upset6 at left2
    voice audio.aiden_vsa21b_line1
    a "You don’t have to anymore… "

    voice audio.aiden_vsa21b_line2
    a "While I was alone, I was able to think about it... and I realized... you're right..."

    show aiden2 sigh3 at left2
    voice audio.aiden_vsa21b_line3
    a "I’m deliberately missing out on a life changing opportunity that everyone knows is best for me…"

    voice audio.aiden_vsa21b_line4
    a "And to think that my reason for turning it down was just because I was so afraid to be away from you."

    show aiden2 worry5 at left2
    voice audio.aiden_vsa21b_line8
    a "It’s crazy to think that I was gonna walk away from the chance, just because I was too afraid to get out of my comfort zone…"

    voice audio.aiden_vsa21c_line2
    a "This was what Dad would’ve wanted for me… So I can't take this huge opportunity for granted..."

    show aiden2 angry5 at left2
    voice audio.aiden_vsa21b_line10
    a "I shouldn’t be so selfish… If I’m not going to do it for myself, I should at least do it for you and my dad since you’ve both supported me for so long."

    hide yoshi2_winter
    hide yoshi2 worry2
    show yoshi_winter at right2
    show yoshi worry3 at right2
    voice audio.yoshi_vsa21b_line6
    yo "But you’re doing this for yourself too, Aiden…"

    voice audio.yoshi_vsa21b_line7
    yo "You really deserve this because you’ve worked so hard all your life."

    show aiden2 sigh1 at left2
    voice audio.aiden_vsa21b_line11
    a "You’re right, Yoshi…"

    voice audio.aiden_vsa21b_line12
    a "I’ve always endured whatever life throws at me, and for some goddamn reason, I’m getting in my own way this time."

    show aiden2 angry2 at left2
    voice audio.aiden_vsa21b_line13
    a "This isn’t the time to be doubting myself…! I need to believe in myself more!"

    show yoshi comp2 at right2
    voice audio.yoshi_vsa21b_line8
    yo "That’s the right way to think about it, Aiden!"

    voice audio.yoshi_vsa21b_line9
    yo "I’m glad you finally see now why all of us were guiding you in this direction!"

    show yoshi comp5 at right2
    voice audio.yoshi_vsa21b_line10
    yo "You’ll be the best chef out there, I’m sure!"

    show aiden2 comp3 at left2
    voice audio.aiden_vsa21b_line14
    a "Th-Thanks, Yoshi…"

    show yoshi bold2 at right2
    voice audio.yoshi_vsa21b_line11
    yo "And don’t worry about being away! We can always keep in touch, send gifts, and maybe even meet up at the restaurant you’ll be working in!"

    show aiden2 sigh1 at left2
    voice audio.aiden_vsa21b_line15
    a "I’d really appreciate that, Yoshi… That’s all I’ll need…"

    show yoshi comp2 at right2
    voice audio.yoshi_vsa21b_line12
    yo "Of course! All of us here at Camp Buddy will be there for you!"

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black with fade
    yo "{i}Thankfully, I was able to help Aiden clear up his doubts and steer him towards the right path.{/i}"
    yo "{i}I'm going to make sure to support him any way that I can, so that he doesn't have to hesitate anymore!{/i}"

    scene cg black
    hide screen location
    hide screen timeline
    hide screen quick_menu
    $quick_menu = False
    with fade
    play sound sleeping_time
    $ time_transition_night_to_day_winter2()
    $ renpy.pause (2.0, hard=True)

    jump day10_aiden_we
