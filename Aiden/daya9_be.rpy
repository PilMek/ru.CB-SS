label day9_aiden_be:
    $ location = location_rooftop
    show screen location
    show screen timeline
    show screen quick_menu
    $ quick_menu = True

    scene cga10 1 with fade
    play bgsound sfxloop_night loop

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
    voice audio.yoshi_vsa21b_line1
    yo "It's not your fault, Aiden... I know how big of a decision this is for you…"

    voice audio.yoshi_vsa21b_line2
    yo "But please let me help clear up your worries... and convince you why this opportunity is the best thing for you!"

    voice audio.yoshi_vsa21b_line3
    yo "And maybe for us…"

    show cga10 9 with Dissolve(0.25)
    voice audio.aiden_vsa21b_line1
    a "You don’t have to anymore… "

    voice audio.aiden_vsa21b_line2
    a "While I was alone, I was able to think about it... and I realized... you're right..."

    voice audio.aiden_vsa21b_line3
    a "I’m deliberately missing out on a life-changing opportunity that everyone knows is best for me…"

    voice audio.aiden_vsa21b_line4
    a "And to think that my reason for turning it down was just because I was so afraid to be away from you."

    show cga10 10 with Dissolve(0.25)
    voice audio.aiden_vsa21b_line5
    a "I… didn’t want to be alone again…"

    voice audio.yoshi_vsa21b_line4
    yo "Aiden…"

    show cga10 11 with Dissolve(0.25)
    voice audio.yoshi_vsa21_line14
    yo "When we got separated, I lost touch with you completely… "

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
    a "I went out there and got all sorts of jobs to make enough money for the both of us, and to afford Dad’s medication. "

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

    voice audio.aiden_vsa21b_line6
    a "We spent as much time together as we could, doing things we loved."

    show cga10 24 with Dissolve(0.25)
    voice audio.aiden_vsa21b_line7
    a "Up until his final moments…"

    show cga10 15 with Dissolve(0.25)
    voice audio.yoshi_vsa21b_line5
    yo "Aiden… I’m so sorry…"

    show cga10 16 with Dissolve(0.25)
    voice audio.aiden_vsa21b_line8
    a "It’s crazy to think that I was gonna walk away from the chance, just because I was too afraid to get out of my comfort zone…"

    voice audio.aiden_vsa21b_line9
    a "This was dad's dream, and he would've been so proud to see me fulfill it... So I can't take this huge opportunity for granted..."

    show cga10 25 with Dissolve(0.25)
    voice audio.aiden_vsa21b_line10
    a "I shouldn’t be so selfish… If I’m not going to do it for myself, I should at least do it for you and my dad since you’ve both supported me for so long."

    show cga10 15 with Dissolve(0.25)
    voice audio.yoshi_vsa21b_line6
    yo "But you’re doing this for yourself too, Aiden…"

    voice audio.yoshi_vsa21b_line7
    yo "You really deserve this because you’ve worked so hard all your life."

    show cga10 10 with Dissolve(0.25)
    voice audio.aiden_vsa21b_line11
    a "You’re right, Yoshi…"

    voice audio.aiden_vsa21b_line12
    a "I’ve always endured whatever life throws at me, and for some goddamn reason, I’m getting in my own way this time."

    voice audio.aiden_vsa21b_line13
    a "This isn’t the time to be doubting myself…! I need to believe in myself more!"

    show cga10 3 with Dissolve(0.25)
    voice audio.yoshi_vsa21b_line8
    yo "That’s the right way to think about it, Aiden!"

    voice audio.yoshi_vsa21b_line9
    yo "I’m glad you finally see now why all of us were guiding you in this direction!"

    voice audio.yoshi_vsa21b_line10
    yo "You’ll be the best chef out there, I’m sure! "

    voice audio.aiden_vsa21b_line14
    a "Th-Thanks, Yoshi…"

    show cga10 3 with Dissolve(0.25)
    voice audio.yoshi_vsa21b_line11
    yo "And don’t worry about being away! We can always keep in touch, send gifts, and maybe even meet up at a restaurant you’ll be working in!"

    voice audio.aiden_vsa21b_line15
    a "I’d really appreciate that, Yoshi… That’s all I’ll need…"

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

    jump day10_aiden_be
