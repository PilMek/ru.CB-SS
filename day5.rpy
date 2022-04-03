label day5:
    $ day = "05"
    $ time = timeline_timeday
    $ location = location_cabin
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    $ working = True
    $ d5_goro = False
    $ d5_aiden = False

    scene bg_quarters_autumn_day with fade
    play music brand_new_day loop
    play bgsound sfxloop_birds loop

    show yoshi2_sleep at center
    show yoshi2 sleepy5 at center
    voice audio.yoshi_v_yawn1
    yo "*yawn*"

    show yoshi2 awkward4 at center
    voice audio.yoshi_v_huh2
    yo "H-Huh? Everyone’s left already…? Again?"

    show yoshi2 sigh1 at center
    voice audio.yoshi_v_sigh3a
    yo "*sigh* Just when I thought I’d be the first one up since everyone went to bed much later than I did."
    yo "I’m starting to feel like everyone’s really got their own thing to work on… while I just oversee everything but don’t actually get involved much…"

    hide yoshi2_sleep
    hide yoshi2 sigh1
    show yoshi_sleep at center
    show yoshi awkward3 at center
    voice audio.yoshi_v_ah1
    yo "Ah, I shouldn’t be thinking this way…! I’ll just focus on finding where I can help out today.  "

    $working = False
    $shuffle_menu()
    menu():
        yo "Ah, I shouldn’t be thinking this way…! I’ll just focus on finding where I can help out today.{fast}"
        "Ask about today's tasks.":
            $working = True
            $score_goro += 1
            $score_bot += 1
            show yoshi think2 at center
            voice audio.yoshi_v_actually1a
            yo "Actually… Maybe Sir Goro has something specific for me."
            yo "I better get dressed and head to his office."
            $d5_goro = True
            jump day5_g
        "Report to the office.":
            $working = True
            $score_goro += 1
            $score_top += 1
            show yoshi talk1 at center
            voice audio.yoshi_v_conj6a
            yo "But before that, I have to make sure to report to the office first."
            yo "Sir Goro will want to know how yesterday went."
            $d5_goro = True
            jump day5_g
        "Help out with chores.":
            $working = True
            $score_aiden += 1
            $score_bot += 1
            show yoshi think2 at center
            voice audio.yoshi_v_think1a
            yo "Maybe I should go and see if I can help Aiden with his tasks."
            yo "I better get dressed and find him. He should be at the kitchen right now."
            $d5_aiden = True
            jump day5_a
        "Assist with meal prep.":
            $working = True
            $score_top += 1
            show yoshi talk1 at center
            voice audio.yoshi_v_oh2
            yo "Oh, Aiden needs some help again in the kitchen."
            yo "I better get dressed and head there."
            $d5_aiden = True
            jump day5_a

label day5_a:
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
    scene bg_messhall_autumn_day with fade
    play music buddy_oath_casual loop

    show yoshi_autumn at center
    show yoshi confused1 at center
    voice audio.yoshi_v_think1a
    yo "Looks like everyone’s having their breakfast. I still can’t get used to seeing this place so lively outside of the summer. "

    show yoshi_autumn at right2
    show yoshi talk1 at right2
    with move

    show jin_autumn at left2
    show jin_glasses at left2
    show jin dizzy1 at left2
    show jin_nosebleed at left2
    with moveinleft

    voice audio.yoshi_v_oh2
    yo "Oh…! Good morning, Jin!"
    yo "I was wondering where you—"

    show yoshi shock2 at right2
    voice audio.yoshi_v_shock1a
    yo "Whoa! Y-Your nose is bleeding! " with vpunch

    hide jin_autumn
    hide jin dizzy1
    hide jin_glasses
    hide jin_nosebleed
    show jin2_autumn at left2
    show jin2 fudan3 at left2
    show jin2_glasses at left2
    show jin2_nosebleed at left2
    voice audio.jin_v_fudan3b2
    j "It’s hot as hell inside that kitchen, I tell you! I don’t know if I can handle the heat any longer…!!"

    show yoshi panic4 at right2
    voice audio.yoshi_v_comp8b
    yo "Oh my goodness, you might be having a heatstroke! Let’s get some cotton to stop the bleeding… or better yet, you should take a cold shower!"

    show jin2 perv5 at left2
    voice audio.jin_v_hngh4a
    j "I don’t think even a shower could cool me down after what I just saw!"

    hide yoshi_autumn
    hide yoshi panic4
    show yoshi2_autumn at right2
    show yoshi2 confused2 at right2
    voice audio.yoshi_v_what4
    yo "Wh-What…? "

    show jin2 daydream2 at left2
    voice audio.jin_v_laugh6c
    j "I came here for a snack, but I got a whole cake instead! "
    j "If you’ll excuse me, I need to savor this meal the heavens blessed me with!"

    hide jin2_autumn
    hide jin2 daydream2
    hide jin2_glasses
    hide jin2_nosebleed
    with moveoutright

    hide yoshi2_autumn
    hide yoshi2 confused2
    show yoshi_autumn at right2
    show yoshi panic3 at right2
    voice audio.yoshi_v_wait3b
    yo "W-Wait, Jin…!!"

    hide yoshi_autumn
    hide yoshi panic3
    show yoshi2_autumn at right2
    show yoshi2 sigh4 at right2
    voice audio.yoshi_v_sigh3a
    yo "*sigh* I think I know exactly what he saw in there…"
    yo "Guess I’ll go see for myself."

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
    scene cga3 1 with fade
    play music opposites_attract loop
    play bgsound sfxloop_stirfry loop

    yo "{i}(It looks like Aiden is busy as usual…){/i}"
    yo "{i}(I don’t know how he’s always so energetic even while doing most of the strenuous chores around the camp.){/i}"
    yo "{i}(But I have to admit, though, it’s really nice to see him in his element.){/i}"
    yo "{i}(No wonder he makes such great food. He always cooks with so much passion){/i}"
    yo "{i}(…and never with any clothes on.){/i}"

    voice audio.yoshi_vsg2_line9
    yo "*gulp*"

    show cga3 2 with Dissolve(0.25)
    yo "{i}(His sweat is dripping into the crevices of his muscles, all the way down to his exposed butt…){/i}"
    yo "{i}(Not only that, but the  wind from the fan is lifting his apron up, showing a bit of his—){/i}"

    show cga3 3 with Dissolve(0.25)
    voice audio.aiden_vsa2_line1
    a "Oh! Hey there, Yoshi! "

    voice audio.aiden_vsa2_line2
    a "How long have you been standing there? I didn’t notice you come in at all!"

    voice audio.yoshi_vsa2_line8
    yo "A-Ah, I—"

    show cga3 4 with Dissolve(0.25)
    voice audio.aiden_vsa2_line3
    a "Huh? What’s with that look? And is that drool I see on your face?"

    $working = False
    $shuffle_menu()
    menu():
        a "Huh? What’s with that look? And is that drool I see on your face?{fast}"
        "You’re covered in sweat… ":
            $working = True
            $score_bot += 1
            voice audio.yoshi_vsa2_line9a
            yo "N-No, I’m fine, but you’re covered in sweat…"

            show cga3 5 with Dissolve(0.25)
            voice audio.aiden_vsa2_line4a
            a "Hehe, I wouldn’t mind you covering me in something else~"

            voice audio.aiden_vsa2_line5a
            a "Plus, I think you’d enjoy working up a sweat too, if you know what I mean~"
        "What’s for breakfast?":
            $working = True
            $score_top += 1
            voice audio.yoshi_vsa2_line9b
            yo "I-I was just wondering what we’re having for breakfast."

            show cga3 5 with Dissolve(0.25)
            voice audio.aiden_vsa2_line4b
            a "Well, you can have \“these buns”\ for any meal you want~"

            voice audio.aiden_vsa2_line5b
            a "Come and have a taste~! Grab ’em while they're hot!"
        "I’m just feeling really thirsty…":
            $working = True
            $score_aiden += 1
            $score_bot += 1
            voice audio.yoshi_vsa2_line9c
            yo "I-I’m just feeling really thirsty…"

            show cga3 5 with Dissolve(0.25)
            voice audio.aiden_vsa2_line4c
            a "Oho~ You came all the way here just to tell me that?"

            voice audio.aiden_vsa2_line5c
            a "Well, I can make my special juice to help quench that “thirst” of yours~"
        "It’s really hot in here!":
            $working = True
            $score_aiden += 1
            $score_top += 1
            voice audio.yoshi_vsa2_line9d
            yo "I-I’m just sweating…! It’s really hot in here."

            voice audio.yoshi_vsa2_line10d
            yo "Is there anything I can do to help you cool down…?"

            show cga3 5 with Dissolve(0.25)
            voice audio.aiden_vsa2_line4d
            a "Hehe, I’d rather you turn up the “heat”, if you know what I mean~ "

    voice audio.yoshi_vsa2_line11
    yo "Th-That’s not what I meant, Aiden…!"

    show cga3 6 with Dissolve(0.25)
    voice audio.aiden_vsa2_line6
    a "Hahaha! I’m just messing with you, Yoshi!"

    show cga3 7 with Dissolve(0.25)
    voice audio.aiden_vsa2_line7
    a "By the way, look – my kitchen finally has a fan! It’s funny how I never thought to add one in here before."

    voice audio.yoshi_vsa2_line12
    yo "A-Ah yeah, I noticed…! We should really improve the vents in here, huh?"

    voice audio.yoshi_vsa2_line13
    yo "Even during the colder months, you still have to put up with a hot kitchen. "

    voice audio.aiden_vsa2_line8
    a "Well, it’s a good thing we have Jin around now! He actually stopped by to drop this fan off a little while ago."

    voice audio.yoshi_vsa2_line14
    yo "*sigh* No wonder he was so flustered… "

    voice audio.yoshi_vsa2_line15
    yo "Did you warn him that you… uhh… do “this” to cool down?"

    show cga3 4 with Dissolve(0.25)
    voice audio.aiden_vsa2_line9
    a "Is this about the apron again? You guys should make that a part of the camp briefing already! "

    voice audio.yoshi_vsa2_line16
    yo "His nose was bleeding, Aiden."

    voice audio.aiden_vsa2_line10
    a "Huh… I probably hugged him too tight when I was thanking him for the fan. No wonder he left all of a sudden."

    voice audio.yoshi_vsa2_line17
    yo "*sigh* Have you considered that it’s because you were butt-naked? "

    voice audio.aiden_vsa2_line11
    a "Come on, he’ll get used to it! Besides, everyone else seems to really like it so far!"

    voice audio.yoshi_vsa2_line18
    yo "E-Everyone, else…?"

    show cga3 8 with Dissolve(0.25)
    voice audio.aiden_vsa2_line12
    a "Yep! The workers always cheer and holler at me whenever I bring them their meals!"

    voice audio.yoshi_vsa2_line19
    yo "*sigh* I just really hope it’s the food they’re excited for."

    show cga3 9 with Dissolve(0.25)
    voice audio.aiden_vsa2_line13
    a "Hehe, don’t pretend you don’t like it too – your face earlier said it all~"

    voice audio.yoshi_vsa2_line20
    yo "A-Aiden! "

    show cga3 10 with Dissolve(0.25)
    voice audio.aiden_vsa2_line14
    a "Hahaha! I’m just teasing you! "

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    play music go_with_the_flow loop
    scene bg_kitchen_autumn_day with fade
    show yoshi_autumn at left2
    show yoshi talk1 at left2
    show aiden_apron at right2
    show aiden norm1 at right2 #Double check
    voice audio.yoshi_v_anyway2
    yo "Anyway, Aiden, I actually came here to ask if you needed any help with the kitchen work or any of your other tasks."

    show aiden happy2 at right2
    voice audio.aiden_v_oh2b
    a "Oh, not this time around. I’m making sure I finish all my prep work in the evenings now, especially after how much we crammed the other day."

    voice audio.yoshi_v_oh2
    yo "O-Oh, I see."

    hide aiden_apron
    hide aiden happy2
    show aiden2_apron at right2
    show aiden2 confused2 at right2
    voice audio.aiden_v_confused1a2
    a "Eh? Are you free today or something? "

    show yoshi explain2 at left2
    voice audio.yoshi_v_well1
    yo "Well, I only need to oversee every aspect of this week’s checklist…"
    yo "It’s pretty vague, but I’m trying my best to ask around and see if there’s anything I can help with."

    hide aiden2_apron
    hide aiden2 confused2
    show aiden_apron at right2
    show aiden comp2 at right2
    voice audio.aiden_v_aww3a
    a "Aww, and I’m the first one you thought of? That’s really sweet, Yoshi~!"
    a "Well, if you really want to spend your day with me, why don’t you help me out with my other chores? I just finished up here, anyways."

    show yoshi talk3 at left2
    voice audio.yoshi_v_sure2
    yo "Oh, sure! What’s next on your task list?"

    show aiden talk3 at right2
    voice audio.aiden_v_think1a1
    a "I was planning to head over to the obstacle course and clean the place up."

    show yoshi talk1 at left2
    voice audio.yoshi_v_right3
    yo "Oh right, that’s a good idea. I don’t think that was on my checklist – good thing you thought of it."
    yo "Should we head over there now?"

    show aiden happy2 at right2
    voice audio.aiden_v_agree3a2
    a "Let me just serve this last batch I cooked up before we go out!"

    hide yoshi_autumn
    hide yoshi talk1
    show yoshi2_autumn at left2
    show yoshi2 comp3 at left2
    voice audio.yoshi_v_uh1a
    yo "You’re not going out there naked again, are you…?"

    show aiden tease1 at right2
    voice audio.aiden_v_laugh1b2
    a "Hehehe… Why? Is it for your eyes only~?"

    hide yoshi2_autumn
    hide yoshi2 comp3
    show yoshi_autumn at left2
    show yoshi shock3 at left2
    show yoshi_blush2 at left2
    voice audio.yoshi_v_ah5
    yo "A-Ah…!"

    show aiden tease2 at right2
    voice audio.aiden_v_oho2a
    a "Ohoho~ Since when did you get so possessive, Yoshi? I like it~"

    hide yoshi_autumn
    hide yoshi shock3
    hide yoshi_blush2
    show yoshi2_autumn at left2
    show yoshi2 sigh4 at left2
    voice audio.yoshi_v_sigh3a
    yo "*sigh*"

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

    $ location = location_obstacle
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_obstacle_autumn_day_dirty with fade
    play music sunset_stroll loop
    play bgsound sfxloop_birds loop

    show yoshi_autumn at right2
    show yoshi shock2 at right2
    show aiden_work at left2
    show aiden norm1 at left2
    voice audio.yoshi_v_shock1a
    yo "Whoa, you weren’t kidding when you said this place needed a cleanup…"

    show aiden laugh1 at left2
    voice audio.aiden_v_yeah1a3
    a "Yeah, wait till you see the pool… It’s filthy!"

    show yoshi think2 at right2
    voice audio.yoshi_v_unsure3a
    yo "I guess the autumn season made it worse too… Everything’s covered in leaves."

    show aiden explain1 at left2
    voice audio.aiden_v_well1a3
    a "Well, it’s been quite a while since we closed down, and nobody’s used it since the scouts, right?"

    show yoshi worry2 at right2
    voice audio.yoshi_v_really1
    yo "And you were planning to clean this all by yourself? There’s no way you could’ve finished it in a day…!"

    show aiden comp2 at left2
    voice audio.aiden_v_glad1a
    a "It’s a good thing you came to the rescue, huh? Haha!"

    hide yoshi_autumn
    hide yoshi worry2
    show yoshi2_autumn at right2
    show yoshi2 sigh4 at right2
    voice audio.yoshi_v_sigh3a
    yo "*sigh* I guess I have to check on you more often, or else you’ll keep doing these difficult chores on your own. "

    show aiden comp6 at left2
    voice audio.aiden_v_no2a1
    a "Nah, don’t worry about me like that! I’m used to it! Besides, you have way more important stuff to do!"

    show yoshi2 shy5 at right2
    voice audio.yoshi_v_what1
    yo "Like what? Just stand around and watch everyone else all day?"

    show aiden laugh3 at left2
    voice audio.aiden_v_laugh2a1
    a "Hahaha! I guess it doesn’t sound bad at all when you put it that way!"

    hide yoshi2_autumn
    hide yoshi2 shy5
    show yoshi_autumn at right2
    show yoshi talk1 at right2
    voice audio.yoshi_v_anyway1a
    yo "Anyway, looks like we have a lot to clean, huh? We better start now so we’ll finish before sundown."

    show aiden happy1 at left2
    voice audio.aiden_v_alright1a2
    a "Alright, then let’s start with the pool right away!"

    show aiden_work at center
    show aiden shock3 at center
    with move

    show yoshi shock2 at right2
    voice audio.yoshi_v_comp8b
    yo "Be careful, Aiden. It’s—"

    hide aiden_work
    hide aiden shock3
    with moveoutbottom

    play sound sfx_bodydrop
    voice audio.aiden_v_shock1c2
    a "Wh-Whoa!"

    show yoshi_autumn at center
    show yoshi panic4 at center
    with move

    voice audio.yoshi_v_aiden6
    yo "A-Aiden!!" with vpunch

    show cg fade at truecenter
    show fxa2 1 at fx_pos
    with dissolve

    voice audio.yoshi_vsa4_line1
    yo "Are you alright?!"

    voice audio.aiden_vsa4_line1
    a "Yeah… I just slipped on my way down."

    voice audio.aiden_vsa4_line2
    a "Though I kinda landed on my elbow – it’s a good thing the leaves broke my fall."
    yo "{i}(I can’t help but remember how Aiden was back in the days…){/i}"

    show fxa2 2 at fx_pos with Dissolve(1.5)
    yo "{i}(I’m not sure if it’s because he gets overly excited whenever we hang out, but he’s always been extremely clumsy.){/i}"
    yo "{i}(I hope it’s not a bad thing, but I find that so endearing about him.){/i}"

    show fxa2 3 at fx_pos with dissolve
    voice audio.yoshi_vsa4_line2
    yo "Here, let me help you up."

    show fxa2 4 at fx_pos with dissolve
    voice audio.aiden_vsa4_line3
    a "Thanks, Yoshi."

    voice audio.yoshi_vsa4_line3
    yo "I’ll grab my first aid kit, and we’ll patch up that bruise!"

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

    $ location = location_obstacle
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene cga4 1 with fade
    play bgsound sfxloop_birds loop
    play music go_with_the_flow_slow loop

    voice audio.yoshi_vsa5_line1
    yo "Watch out for the moss around the pool in this time of year. It gets really slippery when it’s damp. "

    show cga4 2 with Dissolve(0.25)
    voice audio.aiden_vsa5_line1
    a "Yeah, sorry about that… I wasn’t careful at all, Yoshi."

    voice audio.yoshi_vsa5_line2
    yo "Haha, you were clumsy, especially back in the days. You’d always show up with lots of bandages."

    voice audio.aiden_vsa5_line2
    a "Ahehe… At least it’s not as bad as before, right?"

    voice audio.yoshi_vsa5_line3
    yo "You say that, but you slipped several times just this past summer."

    voice audio.aiden_vsa5_line3
    a "Hehe, like that time I spilled hot soup all over your pants~"

    voice audio.yoshi_vsa5_line4
    yo "Thankfully, I caught you that time, so you didn’t get scraped up."

    show cga4 3 with Dissolve(0.25)
    voice audio.yoshi_vsa5_line5
    yo "Anyway, you’re all patched up! "

    voice audio.aiden_vsa5_line4
    a "Thanks, Yoshi! You’re the best!"

    show cga4 4 with Dissolve(0.25)
    voice audio.aiden_vsa5_line5
    a "I gotta say though… it feels really weird to have you take care of me like this. "

    $working = False
    $shuffle_menu()
    menu():
        a "I gotta say though… it feels really weird to have you take care of me like this.{fast}"
        "I should watch over you more often.":
            $working = True
            $score_aiden -= 1
            $score_top += 1
            show cga4 5ab with Dissolve(0.25)
            voice audio.yoshi_vsa5_line6a
            yo "Seriously, I should watch over you more often. "

            show cga4 6a with Dissolve(0.25)
            voice audio.aiden_vsa5_line6a
            a "Oho, if you’ll be paying attention to me, then maybe I’ll have more “accidental” slip-ups~"

            voice audio.yoshi_vsa5_line7a
            yo "Don’t be silly, Aiden. You could’ve gotten seriously hurt."

            show cga4 7a with Dissolve(0.25)
            voice audio.aiden_vsa5_line7a
            a "Come on, Yoshi. You know I’m kidding."

            voice audio.yoshi_vsa5_line9ab
            yo "What I’m trying to say is that you’ve always been doing things on your own while also watching out for all of us."
        "It's not a bad thing.":
            $working = True
            $score_aiden -= 1
            $score_bot += 1
            show cga4 5ab with Dissolve(0.25)
            voice audio.yoshi_vsa5_line6b
            yo "It’s not a bad thing, Aiden."

            voice audio.yoshi_vsa5_line7b
            yo "Besides, you always try to hide it from me whenever something like this happens."

            show cga4 6b with Dissolve(0.25)
            voice audio.aiden_vsa5_line6b
            a "Well… I just don’t wanna be a burden to you, you know?"

            voice audio.yoshi_vsa5_line8b
            yo "I never thought of you like that though."

            voice audio.yoshi_vsa5_line9ab
            yo "What I’m trying to say is that you’ve always been doing things on your own while also watching out for all of us."
        "It's the least I could do.":
            $working = True
            $score_aiden += 1
            $score_bot += 1
            show cga4 5c with Dissolve(0.25)
            voice audio.yoshi_vsa5_line6c
            yo "It’s the least I could do, Aiden."

            voice audio.yoshi_vsa5_line7c
            yo "I don’t really get many chances to help you out like this."

            show cga4 6c with Dissolve(0.25)
            voice audio.aiden_vsa5_line6c
            a "Aww, Yoshi~ It’s alright, you know I can handle myself, no problem."

            voice audio.yoshi_vsa5_line8c
            yo "That’s true, but you still deserve to be taken care of every once in a while."

            show cga4 7cd with Dissolve(0.25)
            voice audio.yoshi_vsa5_line9cd
            yo "You’ve always been the one watching out for all of us."
        "Get used to it.":
            $working = True
            $score_aiden += 1
            $score_top += 1
            show cga4 5d with Dissolve(0.25)
            voice audio.yoshi_vsa5_line6d
            yo "You better get used to it, Aiden."

            voice audio.yoshi_vsa5_line7d
            yo "Now that I’m less busy this season, I’ll definitely be sticking around you more often."

            show cga4 6d with Dissolve(0.25)
            voice audio.aiden_vsa5_line6d
            a "Yeah, it’ll be just like old times! We used to spend so much time together."

            voice audio.yoshi_vsa5_line8d
            yo "Haha, I had to keep an eye on you and make sure you’re not just working all day long."

            show cga4 7cd with Dissolve(0.25)
            voice audio.yoshi_vsa5_line9cd
            yo "You’ve always been the one watching out for all of us."

    show cga4 8 with Dissolve(0.25)
    voice audio.yoshi_vsa5_line10
    yo "I know you try your best to be reliable, so much so that you’re willing to work on anything, whether it’s part of your job or not…"

    voice audio.aiden_vsa5_line8
    a "Well… I do all those things because it makes me happy to help everyone out, but it’s also what I’ve always been used to growing up."

    voice audio.aiden_vsa5_line9
    a "I’ve never really had the luxury to pick or choose my own path, so I’ve gotten used to a simple life."

    show cga4 9 with Dissolve(0.25)
    voice audio.aiden_vsa5_line10
    a "…And I guess I’ve just gotten used to handling things on my own."

    voice audio.aiden_vsa5_line11
    a "Especially after everything that happened with dad… "

    voice audio.yoshi_vsa5_line11
    yo "Ah… I understand… I wasn’t there for you then..."

    voice audio.aiden_vsa5_line12
    a "Well, we had to go our different paths after the first term. That’s just the way it worked out."

    show cga4 10 with Dissolve(0.25)
    voice audio.aiden_vsa5_line13
    a "But you know me! I’m a go-with-the-flow kinda guy, and I try to make do with whatever’s on my plate."

    show cga4 11 with Dissolve(0.25)
    voice audio.yoshi_vsa5_line12
    yo "That’s something I really admire about you, Aiden. I wish I were as optimistic as you."

    voice audio.aiden_vsa5_line14
    a "But you are though! Heck, you’re the one who helped me become like this!"

    voice audio.aiden_vsa5_line15
    a "Why do you think you’re different now? Are you overthinking again?"

    show cga4 12 with Dissolve(0.25)
    voice audio.yoshi_vsa5_line13
    yo "Well, I’ve had a really negative mindset about my role here at Camp Buddy for a while now…"

    voice audio.aiden_vsa5_line16
    a "You mean with the entire expansion project thingy?"

    show cga4 13 with Dissolve(0.25)
    voice audio.yoshi_vsa5_line14
    yo "Yeah… I keep waking up every day ready to work, but I don’t have any specific jobs other than just overseeing things…"

    voice audio.yoshi_vsa5_line15
    yo "Meanwhile, everyone else has their own exciting tasks that contribute to the project directly."

    voice audio.yoshi_vsa5_line16
    yo "You take care of the camp maintenance, Yuri handles the builders, and Sir Goro has the most important job of dealing with things behind the scenes."

    voice audio.yoshi_vsa5_line17
    yo "And all the new jobs that come up are being taken care of by the specialists."

    voice audio.yoshi_vsa5_line18
    yo "Everyone besides me has been doing such a good job lately… "

    voice audio.yoshi_vsa5_line19
    yo "I just can’t help but feel… irrelevant."

    show cga4 14 with Dissolve(0.25)
    voice audio.aiden_vsa5_line17
    a "What?! I can’t believe I’m hearing all of this from you! "

    voice audio.yoshi_vsa5_line20
    yo "I-I know it’s sounds stupid… I’m honestly embarrassed telling you all of this…"

    voice audio.aiden_vsa5_line18
    a "Come on, Yoshi! You’re like the foundation that keeps us all together here, you know!"

    show cga4 15 with Dissolve(0.25)
    voice audio.aiden_vsa5_line19
    a "I’m sure without you, Camp Buddy wouldn’t be nearly as successful, and the rest of us wouldn’t be so passionate about it!"

    voice audio.aiden_vsa5_line20
    a "Heck, you held this place together when it’s about to fall apart for years now, and look what happened!"

    voice audio.aiden_vsa5_line21
    a "We’re setting up for the best year ever, and so much of that is thanks to you!"

    show cga4 16 with Dissolve(0.25)
    voice audio.yoshi_vsa5_line21
    yo "I really appreciate you saying all that, Aiden. I’m really flattered you see me like that."

    voice audio.yoshi_vsa5_line22
    yo "I guess I’m just not used to the new environment yet… Camp Buddy is undergoing a huge change after all."

    show cga4 17 with Dissolve(0.25)
    voice audio.aiden_vsa5_line22
    a "You know, sometimes you just gotta learn to go with the flow and see where it takes you!"

    voice audio.aiden_vsa5_line23
    a "You’re already doing everything you can, so try and look at things on the brighter side. "

    voice audio.aiden_vsa5_line24
    a "Trust me, you’ll be a lot happier that way! "

    show cga4 18 with Dissolve(0.25)
    voice audio.yoshi_vsa5_line23
    yo "You’re right, Aiden… It really helps me to see things from your perspective."

    voice audio.yoshi_vsa5_line24
    yo "Thanks for cheering me up!"

    show cga4 19 with Dissolve(0.25)
    voice audio.aiden_vsa5_line25
    a "It’s what I do best, Yoshi!"

    voice audio.aiden_vsa5_line26
    a "Now come on, the best way to get you out of a slump is to get your muscles pumping! Let’s get to cleaning!"

    voice audio.yoshi_vsa5_line25
    yo "Haha, alright!"

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black with fade
    yo "{i}Talking with Aiden like that was really good for both of us… I think we both needed to get some things off our chest.{/i}"

    $ renpy.pause (1.0, hard=True)
    yo "{i}After our talk, we spent the rest of the day cleaning up the obstacle course.{/i}"
    yo "{i}It was hard work, but we managed to finish it all just before sunset.{/i}"

    scene cg black
    hide screen location
    hide screen timeline
    hide screen quick_menu
    $quick_menu = False
    with fade
    $ renpy.pause (2.0, hard=True)
    $ time_transition_day_to_sunset_fall()

    $ location = location_obstacle
    $ time = timeline_timesunset
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_obstacle_autumn_sunset with fade
    play music sunset_stroll loop

    show yoshi_autumn4 at left2
    show yoshi norm1 at left2
    show aiden2_work2 at right2
    show aiden2 tired5 at right2
    voice audio.aiden_v_relief1a1
    a "*phew* Everything’s squeaky clean now!"

    show yoshi comp5 at left2
    voice audio.yoshi_v_response6b
    yo "I’m glad I was able to help. This would’ve been impossible to do by yourself."

    hide aiden2_work2
    hide aiden2 tired5
    show aiden_work2 at right2
    show aiden comp5 at right2
    voice audio.aiden_v_laugh2a1
    a "Hahaha! You did save me a ton of time!"

    show yoshi comp3 at left2
    voice audio.yoshi_v_hey2
    yo "Hey, Aiden."

    show aiden talk3 at right2
    voice audio.aiden_v_yeah1e1
    a "Yeah?"

    show yoshi comp1 at left2
    voice audio.yoshi_v_thanks1
    yo "Thank you."

    hide aiden_work2
    hide aiden talk3
    show aiden2_work2 at right2
    show aiden2 confused2 at right2
    voice audio.aiden_v_confused1a2
    a "Eh, for what? Cleaning the pool?"

    hide yoshi_autumn4
    hide yoshi comp1
    show yoshi2_autumn4 at left2
    show yoshi2 comp6 at left2
    voice audio.yoshi_v_no4
    yo "N-No, I meant for the advice you gave me earlier."
    yo "It made me see things differently and be content with what I have today."

    hide aiden2_work2
    hide aiden2 confused2
    show aiden_work2 at right2
    show aiden comp3 at right2
    voice audio.aiden_v_laugh3b
    a "Psh…! You’re cheesy as always, Yoshi!"

    show yoshi2 shy5 at left2
    voice audio.yoshi_v_hey3
    yo "H-Hey, I’m just really grateful of what I learned from you…!"

    show aiden relief2 at right2
    voice audio.aiden_v_actually1a
    a "I learn a lot of things from you too. You just don’t realize it!"
    a "Sometimes, I wish I could do all the leadership stuff that you can do! Totally fits the scoutmaster title."
    a "We just have different strengths, and together we make the perfect balance!"

    show aiden wink2 at right2
    voice audio.aiden_v_encourage2b
    a "Remember, we’ve got each other’s backs! Through thick and thin! "

    show yoshi2 play2 at left2
    voice audio.yoshi_v_laugh6
    yo "Hehe, and you said I was the one who’s getting cheesy!"

    show aiden pout4 at right2
    voice audio.aiden_v_shutup2a
    a "Oh, shut up! I blame you – your dorkiness is rubbing off on me. "
    a "But hey, I had fun too. Thanks for working with me today."

    hide yoshi2_autumn4
    hide yoshi2 play2
    show yoshi_autumn4 at left2
    show yoshi_blush at left2
    show yoshi comp2 at left2
    voice audio.yoshi_v_response6a
    yo "You’re welcome, Aiden. "

    show aiden happy1 at right2
    voice audio.aiden_v_anyway2a
    a "Anyways, we’re pretty grimy… Why don’t we head back to our cabin and get washed up?"

    show yoshi happy1 at left2
    voice audio.yoshi_v_right3
    yo "Right!"

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
    $ time_transition_sunset_to_night_fall()

    $ location = location_cabin
    $ time = timeline_timenight
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_quarters_autumn_night with fade
    play music ready_for_tomorrow loop
    play bgsound sfxloop_night loop

    show yoshi_autumn4 at left2
    show yoshi norm1 at left2
    show aiden2_work2 at right2
    show aiden2 sleepy4 at right2
    voice audio.aiden_v_sheesh1a
    a "Sheesh, we totally reek from all that pool sludge!"

    show yoshi relief2 at left2
    voice audio.yoshi_v_relief1
    yo "A good, hot shower would be nice right now… It’s getting chillier each day!"

    hide aiden2_work2
    hide aiden2 sleepy4
    show aiden_work2 at right2
    show aiden tease1 at right2
    voice audio.aiden_v_laugh1a1
    a "Hehe, I can wash your back if you want~ Or maybe you want me to go lower than that~"

    show yoshi awkward4 at left2
    voice audio.yoshi_v_aiden6
    yo "A-Aiden…!"

    show yoshi_autumn4 at p5_1
    show yoshi awkward4 at p5_1
    show aiden_work2 at p5_2
    show aiden tease1 at p5_2
    with move

    show lloyd_work at p5_3
    show lloyd tired6 at p5_3
    show darius_work at p5_4
    show darius norm3 at p5_4
    show goro_work at p5_5
    show goro norm3 at p5_5
    with dissolve

    voice audio.lloyd_v_tired1b2
    l "*huff* *huff*"

    show aiden shock3 at p5_2
    voice audio.aiden_v_shock1d1
    a "Whoa, you guys look beat! What have you been doing today? "

    show lloyd talk3 at p5_3
    voice audio.lloyd_v_conj4a1
    l "We started clearing out the site today! Had to chop lots of wood and move stuff around."

    show darius talk2 at p5_4
    voice audio.darius_v_goro2
    d "Sir Goro helped us too."

    show goro talk2 at p5_5
    voice audio.goro_v_think1a1
    g "We were a little behind schedule on the site clearing, so I decided to lend an extra hand."
    g "I needed to stretch my muscles too… Working in the office all day made me stagnant."

    show yoshi shock2 at p5_1
    voice audio.yoshi_v_amazed1d
    yo "Oh wow! I didn’t think you’d do that kind of job, sir…!"

    show lloyd laugh2 at p5_3
    voice audio.lloyd_v_laugh1a1
    l "Haha, you should’ve seen him with the axe! Those trees toppled down with just a couple swings!"

    show darius bold3 at p5_4
    voice audio.darius_v_amazed3
    d "Dope."

    show goro confused2 at p5_5
    voice audio.goro_v_worry3a1
    g "What about you two? You’re all covered in muck."

    show yoshi explain2 at p5_1
    voice audio.yoshi_v_well1
    yo "We spent the day cleaning the obstacle course, and the pool was especially dirty."

    show aiden_work2 at p6_2
    show aiden shock3 at p6_2
    show yoshi_autumn4 at p6_3
    show yoshi shock2 at p6_3
    show goro_work at p6_4
    show goro confused2 at p6_4
    show lloyd_work at p6_5
    show lloyd laugh2 at p6_5
    show darius_work at p6_6
    show darius bold3 at p6_6
    with move

    jump day5_after

label day5_g:
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
    scene bg_office_autumn_day with fade
    play music go_with_the_flow loop
    play bgsound sfxloop_birds loop

    show yoshi_autumn at center
    show yoshi talk1 at center
    voice audio.yoshi_v_goodam1
    yo "Good morning, s—"

    hide yoshi_autumn
    hide yoshi talk1
    show yoshi2_autumn at center
    show yoshi2 confused1 at center
    voice audio.yoshi_v_think1a
    yo "Hmm… Is Sir Goro not here? I wonder if he’s out again today."

    play sound sfx_doorcreak
    show yoshi2 confused3 at center
    voice audio.yoshi_v_oh4
    yo "Oh? I think he’s still in his quarters…!"
    yo "I should go and check."

    show yoshi2_autumn at p5_1
    show yoshi2 confused3 at p5_1
    with move

    $ renpy.music.stop(channel='music', fadeout = 2.0)
    $ location = location_gororoom
    play sound sfx_dooropen
    scene cgg3 1 with fade
    voice audio.goro_vsg2_line1
    g "*snores*"
    yo "!!!"
    yo "{i}(I didn’t think Sir Goro would still be asleep… He’s usually the first one up){/i}"
    yo "{i}(I can’t blame him for sleeping in… He must be exhausted from his errands yesterday…){/i}"
    yo "{i}(Seeing him resting peacefully like this is kind of relieving though…){/i}"
    yo "{i}(He’s usually either slumped over paperwork on his desk or out all day handling important matters for the camp…){/i}"
    yo "..."

    play music opposites_attract loop
    yo "{i}(I just realized… Sir Goro’s almost naked right in front of me…){/i}"
    yo "{i}(I’ve never really paid close attention before to how built and muscular he is… ){/i}"
    yo "{i}(He’s kept himself perfectly fit throughout the years despite his busy schedule.){/i}"
    yo "{i}(Not only that, but it seems like he’s been grooming himself, from the clean trim of his beard, the hairs on his chest, and all the way down to his—){/i}"

    voice audio.yoshi_vsg2_line9
    yo "*gulp*"
    yo "{i}(I-Is this really all Sir Goro wears when he sleeps?){/i}"
    yo "{i}(He’s normally so conservative, so I didn’t expect something this revealing from someone like him… ){/i}"
    yo "{i}(That underwear is barely containing what’s packing in there… ){/i}"

    show cgg3 2 with Dissolve(0.25)
    voice audio.goro_vsg2_line2
    g "Mmmhh…"

    voice audio.yoshi_vsg2_line13
    yo "A-Ah, Sir Goro…!"

    show cgg3 3 with Dissolve(0.25)
    voice audio.goro_vsg2_line3
    g "W… Wh-Wha… Yoshinori?"

    $working = False
    $shuffle_menu()
    menu():
        g "W… Wh-Wha… Yoshinori?{fast}"
        "It’s time for breakfast!":
            $score_bot += 1
            $working = True
            voice audio.yoshi_vsg2_line14a
            yo "It’s time for sausage, sir!"

            show cgg3 4 with Dissolve(0.25)
            voice audio.goro_vsg2_line4a
            g "H-Huh…?"

            voice audio.yoshi_vsg2_line15a
            yo "I-I mean, i-it’s time for breakfast, sir…! "
            yo "{i}(Oh, crap! Why did I let that slip off my tongue?!){/i}"

            voice audio.goro_vsg2_line5a
            g "I thought I heard something else… I’m still sort of groggy…"
        "Reporting for duty!":
            $score_top += 1
            $working = True
            voice audio.yoshi_vsg2_line14b
            yo "R-Reporting for daddy— I mean, DUTY…!!"
            yo "{i}(Oh, crap! Why did I let that slip off my tongue?!){/i}"

            show cgg3 4 with Dissolve(0.25)
            voice audio.goro_vsg2_line4b
            g "For a second there, I thought I heard…"
        "Good morning, sir!":
            $working = True
            $score_goro += 1
            $score_bot += 1
            voice audio.yoshi_vsg2_line14c
            yo "Wood morning, sir!"

            show cgg3 4 with Dissolve(0.25)
            voice audio.goro_vsg2_line4c
            g "Wait, what…?"

            voice audio.yoshi_vsg2_line15c
            yo "GAH! I-I mean, good morning, sir! "
            yo "{i}(Oh, crap! Why did I let that slip off my tongue?!){/i}"
        "I'm ready, sir!":
            $working = True
            $score_goro += 1
            $score_top += 1
            voice audio.yoshi_vsg2_line14d
            yo "I’m ready for you, sir!"

            show cgg3 4 with Dissolve(0.25)
            voice audio.goro_vsg2_line4c
            g "Wait, what…?"

            voice audio.yoshi_vsg2_line15d
            yo "GAH! I-I mean, I’m ready for your orders, sir!"
            yo "{i}(Oh, crap! Why did I let that slip off my tongue?!){/i}"

    show cgg3 5 with Dissolve(0.25)
    voice audio.goro_vsg2_line6
    g "*ehem* Anyway, I didn’t think you, of all people, would come into my room."

    voice audio.yoshi_vsg2_line16
    yo "I-I apologize for walking into your private space, sir…!"

    show cgg3 6 with Dissolve(0.25)
    voice audio.goro_vsg2_line7
    g "It’s alright, Yoshinori. There’s no need for privacy, especially with you. We’ve gone hand in hand over the years."

    voice audio.yoshi_vsg2_line17
    yo "W-Well, I mean… it’s probably out of my bounds to see you in the raw, sir…!"

    show cgg3 7 with Dissolve(0.25)
    voice audio.goro_vsg2_line8
    g "I don’t think there’s anything wrong with it, Yoshinori. Or… is there?"

    voice audio.yoshi_vsg2_line18
    yo "N-Not at all, sir! In fact, I think you look bulked up, sir!"

    show cgg3 8 with Dissolve(0.25)
    voice audio.goro_vsg2_line9
    g "You say that with your eyes down my—"

    voice audio.yoshi_vsg2_line19
    yo "AH! I was talking about your body, sir…!! I-It’s been a while since I’ve last seen you like this…"

    show cgg3 9 with Dissolve(0.25)
    voice audio.goro_vsg2_line10
    g "Hahaha!! Don’t get too flustered, Yoshinori! "

    show cgg3 6 with Dissolve(0.25)
    voice audio.goro_vsg2_line11
    g "Like I said a few days ago, I’m just trying to ease up around you more often. "

    voice audio.yoshi_vsg2_line20
    yo "R-Right, sir…"

    show cgg3 7 with Dissolve(0.25)
    voice audio.goro_vsg2_line12
    g "What time is it anyway? I must’ve overslept…"

    voice audio.yoshi_vsg2_line21
    yo "I-It’s nine in the morning, sir…!"

    show cgg3 10 with Dissolve(0.25)
    voice audio.goro_vsg2_line13
    g "Ugh, I see… Let me get up then."

    $ renpy.music.stop(channel='music', fadeout = 2.0)
    play music old_familiar_home loop
    scene bg_gororoom_autumn_day with fade

    show yoshi2_autumn at left2
    show yoshi2 awkward1 at left2
    show goro_undie at right2
    show goro tired2 at right2
    voice audio.goro_v_thanks2a1
    g "Thank you again for waking me up… It seems that my body clock isn’t properly tuned today."

    show yoshi2 awkward3 at left2
    voice audio.yoshi_v_comp2
    yo "I-It’s alright, Sir Goro! Honestly, I didn’t expect to wake you when I first came in here!"

    show goro talk3 at right2
    voice audio.goro_v_well1b
    g "Well, it’s a good thing you did, or else I wouldn’t have been able to work on my checklist today."

    hide yoshi2_autumn
    hide yoshi2 awkward3
    show yoshi_autumn at left2
    show yoshi talk1 at left2
    voice audio.yoshi_v_ah1
    yo "Ah… About that, sir…! That was the reason I was looking for you!"
    yo "I was wondering if there was anything I could do to assist you with your tasks."

    hide goro_undie
    hide goro talk3
    show goro2_undie at right2
    show goro2 think6 at right2
    voice audio.goro_v_think1a1
    g "Hmm… Actually, I was planning to oversee the construction today."
    g "Based on the report Yuri gave me last night, it looks like they are a day behind on the site clearing."

    hide goro2_undie
    hide goro2 think6
    show goro_undie at right2
    show goro disappoint2 at right2
    voice audio.goro_v_sigh1a
    g "I’ve been swamped with management tasks and missing out on what’s actually going on in each department."
    g "I want to check and see how things are going for myself and see if there’s anything I can do to help."

    show goro happy1 at right2
    voice audio.goro_v_rush3b1
    g "Why don’t you come along with me?"

    show yoshi happy1 at left2
    voice audio.yoshi_v_sure2
    yo "Oh, sure! I’d be happy to help, sir!"

    show goro happy2 at right2
    voice audio.goro_v_amazed2a1
    g "Great, then I should probably get dressed. "

    show goro tease5 at right2
    voice audio.goro_v_heh1a
    g "Unless… you’re not finished with the view?  "

    show yoshi panic5 at left2
    voice audio.yoshi_v_ah4
    yo "A-Ah…! I-I’ll just wait for you outside, sir…!"

    show goro talk3 at right2
    voice audio.goro_v_wait2a2
    g "Wait, Yoshinori, I’m just—"

    show yoshi_autumn at p5_1
    show yoshi panic3 at p5_1
    with move

    voice audio.yoshi_v_sorry4c1
    yo "I-I’m sorry again for invading your privacy, sir…!!"

    hide yoshi_autumn
    hide yoshi panic3
    with moveoutleft

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black
    hide screen location
    hide screen timeline
    hide screen quick_menu
    $quick_menu = False
    with fade
    play sound sfx_clotheschanging
    $ renpy.pause (2.0, hard=True)

    $ location = location_site
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_site2_autumn_day with fade
    play music buddy_oath_casual loop
    play bgsound sfxloop_birds loop

    show darius_work at p5_1
    show darius norm3 at p5_1
    show darius_goggles1 at p5_1
    show lloyd_work at p5_2
    show lloyd norm2 at p5_2
    show yuri_autumn2 at p5_3
    show yuri happy2 at p5_3
    show goro_autumn2 at p5_4
    show goro norm1 at p5_4
    show yoshi_autumn at p5_5
    show yoshi norm1 at p5_5
    voice audio.yuri_v_greet3a
    yu "Oh! Hi, Dad and Yoshi! "

    show goro happy1 at p5_4
    voice audio.goro_v_goodam1a2
    g "Good morning, Yuri. Did you gather everyone for our work? I was hoping we could get back on schedule today."

    show yuri talk3 at p5_3
    voice audio.yuri_v_agree1a1
    yu "Ah, yes! Yesterday, we were able to survey the land and mark the trees we’ll need to cut down."

    show yuri worry2 at p5_3
    voice audio.yuri_v_sad2a
    yu "I don’t think that we’ll be able to finish all the chopping today, unfortunately…"
    yu "Even though we have a big team, there’s just a ton of trees and clutter to get rid of."

    show goro think2 at p5_4
    voice audio.goro_v_think1a1
    g "Hmm, I see… "
    g "Lloyd, do you have an estimate for when you think we can finish the site clearing phase?"

    show lloyd talk1 at p5_2
    voice audio.lloyd_v_conj6a2
    l "With the current workforce, we should be done in around two to three days."

    show goro talk1 at p5_4
    voice audio.goro_v_so1a
    g "I have to file a report to Mr. Clermont by the end of the week, so that means we have to finish the weekly checklist before then."

    show lloyd sad4 at p5_2
    voice audio.lloyd_v_sorry2a1
    l "That’s partly my fault, sir. I didn’t foresee that the expansion site would have this much vegetation. I should’ve conducted the survey earlier."

    show goro comp2 at p5_4
    voice audio.goro_v_alright2a2
    g "Please, it’s no one’s fault. I’m sure Mr. Clermont will understand if there are minor adjustments to our schedule."
    g "Besides, I think we can cut down the work too by reducing the amount of trees we’ll take down."

    show goro bold2 at p5_4
    voice audio.goro_v_conj2a1
    g "I believe that if we conserve some of them, they’ll complement the structures we’re building here."

    show lloyd excited1 at p5_2
    voice audio.lloyd_v_praise1b
    l "That’s an excellent idea, sir! I can easily adjust the site development plan to retain some of the trees and incorporate the camp’s aesthetics!"

    # show yuri_folder at p5_3
    show yuri bold2 at p5_3
    voice audio.yuri_v_praise1b
    yu "Good thinking, Dad~!"

    show lloyd bold2 at p5_2
    voice audio.lloyd_v_agree3a3
    l "On top of that, we’ll make sure to work overtime today to speed things up a bit!"

    show goro play2 at p5_4
    voice audio.goro_v_well1a
    g "Well, maybe I could help out as well? I was planning to be more hands-on today anyway.  "

    show lloyd bold3 at p5_2
    voice audio.lloyd_v_encourage1b
    l "You don’t need to, sir! You can leave it to me and Yuri to supervise everyone!"

    show darius confused2 at p5_1
    voice audio.darius_v_lloyd1
    d "He meant with chopping trees, Lloyd."

    show lloyd shock3 at p5_2
    voice audio.lloyd_v_question1b2
    l "Wh-What?! Sir Goro… the camp president… is gonna chop wood with us???"

    show yoshi happy1 at p5_5
    voice audio.yoshi_v_yes1
    yo "Yes, and I’m here to volunteer too! This wouldn’t be a new thing to us anyway! Sir Goro, Aiden and I have a rotation for chopping firewood!"

    show yuri play2 at p5_3
    voice audio.yuri_v_laugh1a1
    yu "Hihi, how did you guys think my dad got so buff? He’s always been a fan of working out~"

    show goro bold2 at p5_4
    voice audio.goro_v_heh1a
    g "I’ve spent too much time behind a desk recently, and I’m eager to stretch my muscles."

    show lloyd shock2 at p5_2
    voice audio.lloyd_v_amazed1a1
    l "Wow, now it all makes sense that you’ve always been so fit, sir… This camp really struck gold with its leader…"

    show darius bold2 at p5_1
    voice audio.darius_v_agree2a
    d "Brains and brawn."

    show goro happy3 at p5_4
    voice audio.goro_v_anyway2
    g "Anyway, we should make the most of the daylight. Let me just gear up, and we’ll start working."

    show darius bold2 at p5_1
    show lloyd talk2 at p5_2
    show yuri bold2 at p5_3
    show yoshi bold2 at p5_5
    all "Yes, sir!"

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
    scene bg_site2_autumn_day with fade
    play music old_familiar_home loop
    play bgsound sfxloop_birds loop

    show yoshi_autumn at left2
    show yoshi norm1 at left2
    show goro_work at right2
    show goro happy1 at right2
    voice audio.goro_v_alright1a1
    g "Alright, I’m ready."

    show yoshi happy2 at left2
    voice audio.yoshi_v_laugh1
    yo "It’s been a while since I’ve seen you chop wood, sir."

    show goro sigh1 at right2
    voice audio.goro_v_sigh1a
    g "I have to admit, I might be a little rusty now from doing nothing but paperwork for weeks."

    show yoshi comp3 at left2
    voice audio.yoshi_v_encourage1
    yo "I’m sure you’re still in perfect shape, sir!"

    show goro tease2 at right2
    voice audio.goro_v_heh1a
    g "Heh, how about we make it a challenge and see who chops down the most today?"

    show yoshi_sweat at left2
    show yoshi comp6 at left2
    voice audio.yoshi_v_laugh6
    yo "Ahehe… I-I don’t think I’ll be able to keep up with you, sir."

    hide goro_work
    hide goro tease2
    show goro2_work at right2
    show goro2 play2 at right2
    voice audio.goro_v_rush2a1
    g "Where’s your competitive spirit, Yoshinori? You didn’t build those arms for nothing, right?"

    show yoshi awkward4 at left2
    voice audio.yoshi_v_ah3
    yo "A-Ah, well…"

    show goro2 annoy1 at right2
    voice audio.goro_v_hmph1a
    g "Hmph. Or is it because you think I won’t stand a chance just because you’re younger?"

    show yoshi shock2 at left2
    voice audio.yoshi_v_no5
    yo "N-No, not at all, sir! That’s not what I was thinking!"

    hide goro2_work
    hide goro2 annoy1
    show goro_work at right2
    show goro bold2 at right2
    voice audio.goro_v_taunt1a
    g "Then grab an axe and show me what you got~!"

    show yoshi norm4 at left2
    show cg fade at truecenter
    show fxg2 1 at fx_pos
    with dissolve

    play sound sfx_woodchop
    voice audio.goro_vsg5_line1
    g "GAH!"

    play sound sfx_woodchop
    voice audio.goro_vsg5_line2
    g "ARGH!!" with vpunch

    play sound sfx_treecrash
    yo "{i}(With just a few powerful swings, Sir Goro was able to topple down his first tree.){/i}" with vpunch
    yo "{i}(It’s crazy what those arms can do…){/i}"

    play sound sfx_woodchop
    voice audio.goro_vsg5_line2
    g "ARGH!!" with vpunch

    show fxg2 2 at fx_pos with dissolve
    voice audio.goro_vsg5_line3
    g "Heh! Are you keeping up, Yoshinori?!"

    voice audio.yoshi_vsg5_line1
    yo "I-I’m working on it, s-sir…!"

    voice audio.goro_vsg5_line4
    g "Come on, the wood’s not even hard at all! Put some more force into it!"

    voice audio.yoshi_vsg5_line2
    yo "Yes, sir!"

    play sound sfx_woodchop
    voice audio.yoshi_vsg5_line3
    yo "HNGH!" with vpunch

    play sound sfx_woodchop
    voice audio.yoshi_vsg5_line4
    yo "TIMBER!!" with vpunch

    play sound sfx_treecrash
    voice audio.goro_vsg5_line5
    g "Hahahaha! Not bad, Yoshinori!" with vpunch

    play bgsound2 sfxloop_woodchop

    yo "{i}(Everyone’s starting to watch Sir Goro as he fells each tree… I don’t blame them – I can’t help but look too.){/i}"
    yo "{i}(It reminds me of when I watched him do this every morning…){/i}"

    show fxg2 3 at fx_pos with Dissolve(1.5)
    yo "{i}(Sir Goro has always loved to keep himself in shape no matter what the task.){/i}"
    yo "{i}(Even after all these years, he’s had that same display of strength that really made me look up to him even more.){/i}"
    yo "{i}(In fact, he’s the reason I started working out in the first place.){/i}"

    show fxg2 4 at fx_pos with dissolve
    voice audio.goro_vsg5_line6
    g "What’s the matter, Yoshinori? Running out of breath already?"

    voice audio.yoshi_vsg5_line5
    yo "A-Ah, a little, sir…!"

    voice audio.goro_vsg5_line7
    g "Hahaha, let’s take a break for a while, then!"

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
    play bgsound sfxloop_birds loop
    play music old_familiar_home_slow loop
    scene cgg4 1 with fade
    voice audio.yoshi_vsg6_line1
    yo "*huff* *huff*"

    voice audio.goro_vsg6_line1
    g "I'm surprised, Yoshinori. You're not usually winded so easily. "

    show cgg4 2 with Dissolve(0.25)
    voice audio.goro_vsg6_line2
    g "Haha, what happened to the scout who never ran out of energy back then?"

    show cgg4 3 with Dissolve(0.25)
    voice audio.yoshi_vsg6_line2
    yo "Ah, hehe… I've always had trouble keeping up with you, sir. "

    voice audio.yoshi_vsg6_line3
    yo "I mean… you’re the toughest guy I’ve ever known."

    voice audio.goro_vsg6_line3
    g "Heh, I'm not sure about all that. I'm just glad I was able to get out here and actually be involved today."

    show cgg4 4 with Dissolve(0.25)
    voice audio.yoshi_vsg6_line4
    yo "That's actually something I really admire about you, sir!"

    voice audio.yoshi_vsg6_line5
    yo "You were able to jump in today and provide solutions right away, and you didn't hesitate to get involved either."

    show cgg4 5 with Dissolve(0.25)
    voice audio.yoshi_vsg6_line6
    yo "I wish I had that same kind of confidence and ability to take charge when needed."

    voice audio.goro_vsg6_line4
    g "Huh? What makes you think you don't, Yoshinori? "

    voice audio.goro_vsg6_line5
    g "Are you having the same doubts you talked about a few days ago?"

    show cgg4 6 with Dissolve(0.25)
    voice audio.yoshi_vsg6_line7
    yo "Well, it’s not that big of a deal… But yes, I’ve never been able to fully shake off my negative mindset about my role here at Camp Buddy…"

    voice audio.goro_vsg6_line6
    g "You’re talking about your role for this expansion project, right?"

    show cgg4 7 with Dissolve(0.25)
    voice audio.yoshi_vsa5_line14
    yo "Yeah… I keep waking up every day ready to work, but I don’t have any specific jobs other than just overseeing things…"

    voice audio.yoshi_vsa5_line15
    yo "Meanwhile, everyone else has their own exciting tasks that contribute to the project directly."

    voice audio.yoshi_vsa5_line16
    yo "You take care of the camp maintenance, Yuri handles the builders, and Sir Goro has the most important job of dealing with things behind the scenes."

    voice audio.yoshi_vsa5_line17
    yo "And all the new jobs that come up are being taken care of by the specialists."

    voice audio.yoshi_vsa5_line18
    yo "Everyone besides me has been doing such a good job lately… "

    show cgg4 8 with Dissolve(0.25)
    voice audio.yoshi_vsa5_line19
    yo "I just can’t help but feel… irrelevant."

    show cgg4 9 with Dissolve(0.25)
    voice audio.goro_vsg6_line7
    g "Yoshinori… "

    voice audio.yoshi_vsg6_line9
    yo "I-I know it’s sounds stupid… I’m honestly embarrassed telling you all of this, sir…"

    voice audio.goro_vsg6_line8
    g "No, it’s alright… "

    voice audio.goro_vsg6_line9
    g "It’s perfectly normal to feel a little out of place with the current state of the camp."

    show cgg4 10 with Dissolve(0.25)
    voice audio.goro_vsg6_line10
    g "But remember – you’re a scoutmaster. Your job is to take care of the scouts and engage with them."

    voice audio.goro_vsg6_line11
    g "And because it’s the off-season, that role naturally feels empty to you right now."

    voice audio.goro_vsg6_line12
    g "So, give it some time, and let yourself adjust. It’s been less than a week since the expansion project kicked off after all."

    show cgg4 11 with Dissolve(0.25)
    voice audio.yoshi_vsg6_line10
    yo "Th-Thank you, sir… I really appreciate your advice."

    show cgg4 12 with Dissolve(0.25)
    voice audio.goro_vsg6_line13
    g "Well, I’m glad you still trust me enough to tell me your doubts and concerns."

    voice audio.goro_vsg6_line14
    g "It’s been a long time since we got to talk like this, and it really brought me back to the days when I was there to guide you as your scoutmaster."

    show cgg4 13 with Dissolve(0.25)
    voice audio.goro_vsg6_line15
    g "Although, you were always the one who listened when I had problems with my family.  "

    voice audio.yoshi_vsg6_line11
    yo "Ah… I really didn’t mind, sir. In fact, I was more than happy to be someone you could talk to."

    voice audio.goro_vsg6_line16
    g "You really did help me get through some tough times, and I owe you a lot for that."

    show cgg4 14 with Dissolve(0.25)
    voice audio.goro_vsg6_line17
    g "And yet, I became so distant over the years that I couldn’t even return the favor."

    $working = False
    $shuffle_menu()
    menu():
        g "Yet I’ve become so distant over the years that I couldn’t even return the favor.{fast}"
        "It couldn't be helped.":
            $working = True
            $score_goro -= 1
            $score_top += 1
            voice audio.yoshi_vsg6_line12a
            yo "It couldn’t be helped, sir… There’s nothing we can do to change what’s already happened…"
        "It's all in the past.":
            $working = True
            $score_goro -= 1
            $score_bot += 1
            voice audio.yoshi_vsg6_line12b
            yo "It doesn’t matter now, sir, ’cause it’s all in the past…"
        "I don’t hold anything against you.":
            $working = True
            $score_goro += 1
            $score_top += 1
            voice audio.yoshi_vsg6_line12c
            yo "I don’t hold anything against you, sir…"
        "You were going through a lot.":
            $working = True
            $score_goro += 1
            $score_bot += 1
            voice audio.yoshi_vsg6_line12d
            yo "But I understand that you were going through a lot of things I didn’t know about, sir…"

    voice audio.yoshi_vsg6_line13
    yo "Since I left after the first term, you had to manage everything on your own… I can only imagine how much more difficult it was to be in your shoes."

    show cgg4 15 with Dissolve(0.25)
    voice audio.goro_vsg6_line18
    g "Well… I do believe everything happens for a reason."

    voice audio.goro_vsg6_line19
    g "And all we can do is control how we respond to those events and try our best no matter the circumstances."

    show cgg4 16 with Dissolve(0.25)
    voice audio.yoshi_vsg6_line14
    yo "Haha, that kinda reminds me of the Buddy Law, sir."

    show cgg4 17 with Dissolve(0.25)
    voice audio.goro_vsg6_line20
    g "*ehem* I didn’t mean to sound so sentimental."

    voice audio.yoshi_vsg6_line15
    yo "Well, I feel a lot more motivated now! Thank you, Sir Goro."

    show cgg4 18 with Dissolve(0.25)
    voice audio.goro_vsg6_line21
    g "Good. Now channel that motivation into that axe, and let’s get back to chopping."

    voice audio.yoshi_vsg6_line16
    yo "Yes, sir!"

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black with fade
    yo "{i}(I’m really glad Sir Goro and I had our talk… It really made me feel better to know that we understand each other....){/i}"

    $ renpy.pause (1.0, hard=True)
    yo "{i}(After our talk, we spent the rest of the day chopping up more trees.){/i}"
    yo "{i}(It was hard work, but we managed to finish it all just before sunset.){/i}"

    scene cg black
    hide screen location
    hide screen timeline
    hide screen quick_menu
    $quick_menu = False
    with fade
    $ renpy.pause (2.0, hard=True)
    $ time_transition_day_to_sunset_fall()

    $ location = location_site
    $ time = timeline_timesunset
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_site2_autumn_sunset with fade
    play music sunset_stroll loop

    show yoshi2_autumn at left2
    show yoshi2 tired4 at left2
    show goro_work at right2
    show goro norm1 at right2
    voice audio.yoshi_v_pant1
    yo "*huff* *huff* That might be the most trees I’ve chopped down in my life…"

    show goro happy1 at right2
    voice audio.goro_v_amazed1a1
    g "Looks like we don’t have to worry about firewood for the winter. I even think these might last us till next year."
    g "I have to say, you’re not too shabby after all, Yoshinori. You managed to keep up with me."

    hide yoshi2_autumn
    hide yoshi2 tired4
    show yoshi_autumn at left2
    show yoshi bold2 at left2
    voice audio.yoshi_v_sir2
    yo "No way, sir… I only took down about half as many as you did. I didn’t stand a chance of winning that challenge, haha."

    show goro play3 at right2
    voice audio.goro_v_heh1a
    g "Heh, you tried. It was a good workout though, wasn’t it?"

    show yoshi comp6 at left2
    voice audio.yoshi_v_ah1
    yo "Ah, hehe… You don’t look like you’re tired at all, sir."

    show goro tired2 at right2
    voice audio.goro_v_relief1a
    g "Don’t get me wrong, I have my limits too. I could really use a massage tonight."

    show yoshi talk1 at left2
    voice audio.yoshi_v_oh1
    yo "Oh, I can give you one if you—"

    show yoshi_autumn at p5_4
    show yoshi talk1 at p5_4
    show goro_work at p5_5
    show goro tired2 at p5_5
    with move

    show lloyd_work at p5_1
    show lloyd norm2 at p5_1
    show darius_work at p5_2
    show darius norm1 at p5_2
    show darius_goggles2 at p5_2
    show yuri_autumn2 at p5_3
    show yuri amazed1 at p5_3
    with dissolve

    voice audio.yuri_v_amazed2a
    yu "Wow! Everything’s cleared over here! Good job, you two!"

    show goro happy3 at p5_5
    voice audio.goro_v_ah2a
    g "Ah, looks like you all have cleared up over there as well. Great work."

    show lloyd sigh5 at p5_1
    voice audio.lloyd_v_agree2b1
    l "Yeah, Dar was chopping trees down like crazy! I wish I could’ve helped as much as you guys though."

    show darius comp2 at p5_2
    voice audio.darius_v_comp3a
    d "You helped carry the wood. "

    show yoshi happy1 at p5_4
    voice audio.yoshi_v_praise1
    yo "Yeah, everyone really worked hard today!  The place looks a lot bigger without all the vegetation."

    show yoshi talk3 at p5_4
    voice audio.yoshi_v_amazed1a
    yo "Looking at it all cleared like this makes me realize how much larger Camp Buddy’s property is."

    show lloyd happy1 at p5_1
    voice audio.lloyd_v_agree2a1
    l "Yeah, this is probably one of the biggest sites I’ve ever worked on! I’m really excited to start ground-breaking soon!"

    show yuri happy1 at p5_3
    voice audio.yuri_v_agree4b1
    yu "We should be back on schedule now, right?"

    show lloyd explain4 at p5_1
    voice audio.lloyd_v_think3b3
    l "I’d say we’re at about 80\% completion of the original target! You guys can leave the rest for us tomorrow, and we’ll finish it before sunset!"

    show goro happy3 at p5_5
    voice audio.goro_v_praise1a
    g "Excellent. And since it’s already sundown, I believe we can all call it a day. "
    g "Great job, everyone!"

    show yuri laugh1 at p5_3
    voice audio.yuri_v_laugh1a1
    yu "Hihi~ Now, if you boys don’t mind, I have to wash up~ I got dirty from trying to carry stuff around too~"

    show goro think3 at p5_5
    voice audio.goro_v_alright1a1
    g "If that’s the case, then I’ll have to shower elsewhere."

    show yoshi happy2 at p5_4
    voice audio.yoshi_v_sir1
    yo "You can use the ones in our quarters, sir! We have several cubicles there!"

    show yuri tease2 at p5_3
    voice audio.yuri_v_sus2a
    yu "Ooh~? I smell something fishy~"

    show lloyd scared3 at p5_1
    voice audio.lloyd_v_groan1a3
    l "Hngh! No way! I don’t have body odor, just so you know!"

    show darius play2 at p5_2
    voice audio.darius_v_amazed2
    d "Even your sweat smells good."

    show yoshi talk3 at p5_4
    voice audio.yoshi_v_anyway3a
    yo "A-Anyway, should we all go now before it gets chilly out here?"

    show yuri tease4 at p5_3
    voice audio.yuri_v_tease2a
    yu "Hihihi~ Have funnn~~"

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
    $ time_transition_sunset_to_night_fall()

    $ location = location_cabin
    $ time = timeline_timenight
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_quarters_autumn_night with fade
    play music ready_for_tomorrow loop
    play bgsound sfxloop_night loop

    show aiden_work2 at p5_1
    show aiden happy1 at p5_1
    show yoshi_autumn at p5_2
    show yoshi norm1 at p5_2
    show goro_work at p5_3
    show goro norm1 at p5_3
    show lloyd_work at p5_4
    show lloyd norm4 at p5_4
    show darius_work at p5_5
    show darius norm3 at p5_5
    voice audio.aiden_v_guys2b
    a "Hey, guys!"

    show yoshi shock3 at p5_2
    voice audio.yoshi_v_aiden6
    yo "A-Aiden! What happened to you? You’re a mess!"

    show lloyd pain3 at p5_4
    voice audio.lloyd_v_groan2b3
    l "Eugh… And you reek too… Did you fall in the dumpster or something?"

    show aiden comp5 at p5_1
    voice audio.aiden_v_oops1a
    a "Whoops, sorry! I cleaned the pool today, and I guess a lot of sludge got onto me!"
    a "You guys are ones to talk! You’re all covered in dirt!"

    show lloyd talk2 at p5_4
    voice audio.lloyd_v_conj4a1
    l "We started clearing out the site today! Had to chop lots of wood and move stuff around."

    show darius talk1 at p5_5
    voice audio.darius_v_goro2
    d "Sir Goro helped us too."

    show goro talk2 at p5_3
    voice audio.goro_v_think1a1
    g "We were a little behind schedule on the site clearing, so I decided to lend an extra hand."

    show aiden shock3 at p5_1
    voice audio.aiden_v_goro3a
    a "Whoa! Good thing you didn’t hurt your back, Gramps!"

    hide yoshi_autumn
    hide yoshi shock3
    show yoshi2_autumn at p5_2
    show yoshi2 shy5 at p5_2
    voice audio.yoshi_v_actually1b
    yo "He actually chopped down the most out of everyone, Aiden…"

    show aiden excited1 at p5_1
    voice audio.aiden_v_amazed1b1
    a "Awesooome! Didn’t know you still had it in you, Gramps! Hahaha!"

    show goro sigh1 at p5_3
    voice audio.goro_v_sigh1a
    g "*sigh*"

    show aiden_work2 at p6_2
    show aiden shock3 at p6_2
    show yoshi2_autumn at p6_3
    show yoshi2 shy5 at p6_3
    show goro_work at p6_4
    show goro sigh1 at p6_4
    show darius_work at p6_6
    show darius talk1 at p6_6
    show lloyd_work at p6_5
    show lloyd talk2 at p6_5
    with move

    jump day5_after

label day5_after:

    show jin_sleep at p6_1
    show jin sleepy4 at p6_1
    show jin_glasses at p6_1
    with dissolve

    voice audio.jin_v_yawn1a
    j "Hnnn… Good morning, guys…"

    hide lloyd_work
    hide lloyd talk2
    show lloyd_work at p6_5
    show lloyd shock6 at p6_5
    voice audio.lloyd_v_question1a2
    l "What? It’s, like, eight in the evening! You’re way off!"

    show jin worry4 at p6_1
    voice audio.jin_v_sorry1b2
    j "Ahh… I’m sorry, I must’ve overslept a little… Did I miss anything? "

    show lloyd annoy2 at p6_5
    voice audio.lloyd_v_wait1a2
    l "Wait a minute! You were sleeping all day while all of us were working our asses off?! "

    show jin panic2 at p6_1
    voice audio.jin_v_shock2b
    j "Ack…! I-It’s not what you think! I wasn’t slacking off…!"

    show aiden talk2 at p6_2
    voice audio.aiden_v_jin3a
    a "Jin’s telling the truth though. He was up all night yesterday working on his laptop, and he was still awake when I got up this morning to make breakfast."

    hide yoshi2_autumn
    hide yoshi2 shy5
    hide yoshi worry5
    show yoshi_autumn at p6_3
    show yoshi worry5 at p6_3
    voice audio.yoshi_v_wait2a
    yo "Wait… Does that mean you haven’t slept since you got here, Jin?!"

    show jin thinkdn2 at p6_1
    voice audio.jin_v_conj2b3
    j "Well, I have now… But yeah, I didn’t really sleep the night before either…"

    show lloyd pain1 at p6_5
    voice audio.lloyd_v_shock2b3
    l "Yikes… I don’t know how you do that. I don’t function well without my eight hours of REM sleep!"

    show darius think5 at p6_6
    voice audio.darius_v_agree1a
    d "He’s a night owl."

    show jin talk3 at p6_1
    voice audio.jin_v_response1b2
    j "Yeah… That’s right! I’m more focused and productive during the night!"

    show goro confused2 at p6_4
    voice audio.goro_v_unsure3a2
    g "I suppose you work better during those hours, but isn’t that a little… unhealthy?"

    show yoshi confused2 at p6_3
    voice audio.yoshi_v_yeah1
    yo "Yeah, I agree… Do you have trouble sleeping, Jin?"

    show jin comp3 at p6_1
    voice audio.jin_v_comp8b1
    j "I-I’m fine…! Please don’t worry about me."

    show lloyd think2 at p6_5
    voice audio.lloyd_v_shock1b1
    l "Have you tried sipping a nice, warm cup of chamomile tea before bed? It’s a natural and organic treatment for insomnia! "
    l "Darius usually has trouble sleeping sometimes as well, and it works wonders for him."

    show darius relief2 at p6_6
    voice audio.darius_v_laugh1
    d "I like tea."

    show lloyd laugh1 at p6_5
    voice audio.lloyd_v_laugh1a1
    l "If that can knock this big guy out, that should solve your insomnia problems!"

    show jin awkward3 at p6_1
    voice audio.jin_v_confused2b1
    j "But… I don’t have insomnia."

    show aiden comp3 at p6_2
    voice audio.aiden_v_comeon1b1
    a "Give him a break, guys. His brain is just more active at night. There’s nothing more to it~"

    show goro talk1 at p6_4
    voice audio.goro_v_agree6a2
    g "That’s right. Besides, Jin’s tasks do not need to follow a strict daily schedule. As long as he gets the job done, then there’s no problem."

    show lloyd think5 at p6_5
    voice audio.lloyd_v_unsure1a2
    l "I guess if he does it all the time then his body must have already developed its own circadian rhythm."

    show yoshi think2 at p6_3
    voice audio.yoshi_v_huh5
    yo "You really don’t want to let this go, huh, Lloyd?"

    show darius laugh3 at p6_6
    voice audio.darius_v_laugh2a
    d "Haha."

    show jin confused2 at p6_1
    voice audio.jin_v_worry2a
    j "F-Forgive me for asking, but… I’ve been wondering why everyone’s covered in dirt… Did something happen out there while I was asleep?"

    show yoshi talk1 at p6_3
    voice audio.yoshi_v_oh1
    yo "Oh, we all just worked on physical tasks today! We should probably get washed up now though, huh?"

    show lloyd tired5 at p6_5
    voice audio.lloyd_v_groan2a2
    l "Ugh! I’ve been wanting to do that since we got back here! This dirty, sticky sweat is really bad for my skin!"

    show jin talk4 at p6_1
    voice audio.jin_v_oh1a
    j "Oh, you guys are gonna take a shower?"

    show yoshi talk3 at p6_3
    voice audio.yoshi_v_yeah2
    yo "Yeah! Are you planning on using the bathroom, Jin?"

    show jin awkward6 at p6_1
    voice audio.jin_v_conj2c1
    j "W-Well, I was about to… I really haven’t got the chance to shower ever since I got here…"
    j "But you guys can go ahead! I can be at the back of the queue!"

    show aiden play2 at p6_2
    voice audio.aiden_v_confused2a2
    a "Back of the queue? The bathroom’s big enough for all of us."
    a "To save time, water, and heating, here at Camp Buddy, we shower TOGETHER!"

    hide jin_sleep
    hide jin awkward6
    hide jin_glasses
    show jin2_sleep at p6_1
    show jin2 fudan3 at p6_1
    show jin2_glasses at p6_1
    voice audio.jin_v_what4b
    j "FDJASKLFSAFLK! What?! T-TOGETHER?!"
    with vpunch

    show lloyd talk3 at p6_5
    voice audio.lloyd_v_agree4b2
    l "Oh yeah, we used to do that all the time when we were scouts too!"

    show darius tease2 at p6_6
    voice audio.darius_v_think3a
    d "Do you need me to wash your back again?"

    show lloyd angry2 at p6_5
    voice audio.lloyd_v_greet2c2
    l "H-Hey! My arms are long enough now to reach!"

    show jin2 fudan2 at p6_1
    voice audio.jin_v_wait5b
    j "W-Wait… I-I’ve never really taken a shower with someone else, but—"

    show aiden tease2 at p6_2
    voice audio.aiden_v_no1a1
    a "No buts! Oh wait… Actually, there’ll be a lot of butts."

    show goro talk3 at p6_4
    voice audio.goro_v_heh1a
    g "We’re all men here. There’s nothing to be embarrassed about."

    show yoshi comp6 at p6_3
    voice audio.yoshi_v_rush1
    yo "Now, now, guys. If Jin isn’t comfortable with it, maybe we shouldn’t—"

    show jin2 scheme2 at p6_1
    voice audio.jin_v_gulp1a
    j "Well, if you all insist… I… guess I could join…"

    show aiden bold2 at p6_2
    voice audio.aiden_v_alright1a1
    a "Alright! What are we waiting for, then?! Let’s go!"

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black
    hide screen location
    hide screen timeline
    hide screen quick_menu
    $quick_menu = False
    with fade
    play sound sfx_clotheschanging
    $ renpy.pause (2.0, hard=True)

    $ location = location_bathroom
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene cg5 1 with fade
    play music opposites_attract loop
    play bgsound sfxloop_night loop

    voice audio.aiden_vs6_line1
    a "Phew! You guys don’t know how ready I am to get out of these clothes! "

    voice audio.goro_vs6_line1
    g "My shirt’s drenched in sweat as well… I hope it won’t stain much…"

    show cg5 2 with Dissolve(0.25)
    voice audio.aiden_vs6_line2
    a "Wait a minute, Gramps. Why are you here with us anyways? You have your own shower, right? "

    voice audio.goro_vs6_line2
    g "Yuri’s already using it, and knowing her, it’ll be at least an hour before she’s finished."

    show cg5 3 with Dissolve(0.25)
    voice audio.yoshi_vs6_line1
    yo "It’s nice that you get to join us this time around, sir! We rarely get the chance to do something like this together."

    voice audio.goro_vs6_line3
    g "Well, maybe I should join you guys more often, then."

    voice audio.aiden_vs6_line3
    a "Yeaaaahhh, Yoshi and I shower together all the time! You’ve been missing out on the fun stuff, Gramps!"

    show cg5 4 with Dissolve(0.25)
    voice audio.jin_vs6_line1
    j "*gulp* "

    voice audio.lloyd_vs6_line1
    l "W-Wait a minute… Why is Jin just standing there in the corner?"

    voice audio.darius_vs6_line1
    d "Come join us."

    voice audio.yoshi_vs6_line2
    yo "Oh, I forgot Jin has the same… interests as Yuri. Maybe he’s a little… overwhelmed?"

    voice audio.goro_vs6_line4
    g "Uhh… Don’t tell me he’s also—"

    voice audio.aiden_vs6_line4
    a "Oh, why didn’t you say so?!"

    show cg5 5 with Dissolve(0.25)
    voice audio.aiden_vs6_line5
    a "Hey, Jin! You’re getting front-row seats for the beefcake show! Check out these muscles!"

    voice audio.jin_vs6_line2
    j "S-S-So m-many n-naked… men…"

    voice audio.lloyd_vs6_line2
    l "Dude, you’re naked too."

    voice audio.jin_vs6_line3
    j "Am I dead? Did I die in my apartment alone from all the MSG in the instant noodles I ate and caffeine from all the coffee I drank?"

    voice audio.darius_vs6_line2
    d "Earth to Jin. Are you there? "

    voice audio.jin_vs6_line4
    j "Am I in heaven? Was I sent here because of my good deeds translating those BL doujins for free…?"

    voice audio.goro_vs6_line5
    g "Wow… You weren’t kidding… He really is like Yuri…"

    voice audio.yoshi_vs6_line3
    yo "Snap out of it, Jin!"

    scene bg_bathroom_autumn_night with fade
    play music here_they_come loop
    show darius_naked at p6_1
    show darius norm4 at p6_1
    show lloyd_naked at p6_2
    show lloyd norm4 at p6_2
    show goro_naked at p6_3
    show goro norm3 at p6_3
    show yoshi_naked at p6_4
    show yoshi norm3 at p6_4
    show aiden_naked at p6_5
    show aiden tease1 at p6_5
    show jin2_naked at p6_6
    show jin2_blush2 at p6_6
    show jin2 perv2 at p6_6
    voice audio.aiden_v_idea1a2
    a "Now that everyone’s naked, let’s check out everyone’s bod, shall we? I wanna know who Jin thinks is the best~"

    hide yoshi_naked
    hide yoshi norm3
    show yoshi2_naked at p6_4
    show yoshi2 sigh4 at p6_4
    voice audio.yoshi_v_sigh3a
    yo "*sigh* I’m not sure this is a good idea, Aiden…"

    show aiden bold2 at p6_5
    voice audio.aiden_v_response3b
    a "I’ll go first!"

    show aiden excited2 at p6_5
    voice audio.aiden_v_flex1a
    a "Flex these guns~"
    a "I used to have a twiggy body just like you, Jin!"

    show aiden tease1 at p6_5
    voice audio.aiden_v_perv1
    a "If you wanna be buff like me, I can give you a “huge tip,” if you know what I mean~"

    show jin2 dizzy4 at p6_6
    voice audio.jin_v_hngh5c
    j "HNGHHHH!!! "

    show lloyd sigh5 at p6_2
    voice audio.lloyd_v_geez1a3
    l "Geez… He’s really doing that in front of all of us…"

    show yoshi2 sigh1 at p6_4
    voice audio.yoshi_v_aiden13
    yo "Aiden does this all the time, even if it’s just the two of us…"

    show aiden_naked at p6_4
    show aiden play2 at p6_4
    show yoshi2_naked at p6_5
    show yoshi2 sigh1 at p6_5
    with move

    show goro annoy1 at p6_3
    voice audio.aiden_v_yoshi3a
    a "Speaking of which, do I even need to check you out, Yoshi? I know every “inch” of you already!"

    hide yoshi2_naked
    hide yoshi2 sigh1
    show yoshi_naked at p6_5
    show yoshi awkward3 at p6_5
    voice audio.yoshi_v_wait3a
    yo "A-Aiden, don’t give them the wrong idea…!"

    show aiden wink2 at p6_4
    voice audio.aiden_v_actually1a
    a "He used to be a skinny twink too, you know? "
    a "So just let us know if you wanna get jacked, Jin! We’ll team up and work you out~ *wink*"

    hide yoshi_naked
    hide yoshi awkward3
    show yoshi2_naked at p6_5
    show yoshi2 sigh4 at p6_5
    voice audio.yoshi_v_sigh3a
    yo "*sigh*"

    show aiden happy1 at p6_4
    voice audio.aiden_v_alright1a3
    a "Moving on!"

    show aiden_naked at p6_3
    show aiden wink2 at p6_3
    show goro_naked at p6_4
    show goro annoy1 at p6_4
    show yoshi2_naked at p6_5
    show yoshi2 sigh4 at p6_5
    show jin2_naked at p6_6
    show jin2_blush2 at p6_6
    show jin2 dizzy4 at p6_6
    with move

    hide aiden_naked
    hide aiden wink2
    show aiden2_naked at p6_3
    show aiden2 confused4 at p6_3
    a "..."

    show aiden2_naked at p6_2
    show aiden2 confused4 at p6_2
    show lloyd_naked at p6_3
    show lloyd rage1 at p6_3
    with move

    hide aiden2_naked
    hide aiden2 confused4
    show aiden_naked at p6_2
    show aiden happy3 at p6_2
    voice audio.aiden_v_darius1a
    a "Darius, my man! The one who’s had the most “growth” out of all of us~"

    hide lloyd_naked
    hide lloyd rage3
    show lloyd_naked at p6_3
    show lloyd rage3 at p6_3
    voice audio.lloyd_v_greet2d4
    l "H-HEY!!! WHY DID YOU SKIP ME?!!"
    with vpunch

    show aiden comp5 at p6_2
    voice audio.aiden_v_oops1a
    a "Whoops, didn’t see you there, Lloyd~!"
    a "You’re fine. You’re pretty chiseled, even if you’re cut a little short."

    show lloyd pout1 at p6_3
    voice audio.lloyd_v_annoyed1b5
    l "I just look short because Dar is with me all the time, and everyone keeps comparing us!"

    show darius play2 at p6_1
    voice audio.darius_v_lloyd7a
    d "I like Lloyd’s height the best."

    show lloyd sigh5 at p6_3
    voice audio.lloyd_v_sad1a1
    l "Huhuhu, Dar… Don’t say that out of pity…"

    show darius tease2 at p6_1
    voice audio.darius_v_denial2a2
    d "I’m not. You’re perfect for head pats."

    show aiden tease2 at p6_2
    voice audio.aiden_v_laugh2a1
    a "More like you’ll be patting Lloyd with your other “head” at that height~! Hahaha!"

    hide yoshi2_naked
    hide yoshi2 sigh4
    show yoshi_naked at p6_5
    show yoshi annoy3 at p6_5
    voice audio.yoshi_v_rush3
    yo "Come on, Aiden… It’s not all about size."

    show aiden tease1 at p6_2
    voice audio.aiden_v_agree2a1
    a "Riiiight…"

    show lloyd angry2 at p6_3
    voice audio.lloyd_v_ignored1c1
    l "YOSHI’S RIGHT, YOU KNOW?! Don’t you agree, Jin?"

    show jin2 perv5  at p6_6
    voice audio.jin_v_laugh2c
    j "I do like it big…"

    show lloyd shock6 at p6_3
    voice audio.lloyd_v_question1d4
    l "Whaaat?! We’re part of the skinny squad, so you’re supposed to be on my side!"

    show goro explain2 at p6_4
    voice audio.goro_v_rush2a2
    g "Come on, all of you. Every body type is good as long as you’re healthy."

    show aiden_naked at p6_3
    show aiden play2 at p6_3
    show lloyd_naked at p6_2
    show lloyd shock6 at p6_2
    with move

    voice audio.aiden_v_whistle1a
    a "Says the guy who has the biggest “everything” out of everyone here!"
    a "With arms that can choke you to death, man boobs, cheese-grater abs, and watermelon-crushing thighs, what more can you ask for?!"

    show goro shy2 at p6_4
    voice audio.goro_v_ah2b
    g "Gah! "

    show aiden play6 at p6_3
    voice audio.aiden_v_goro3a
    a "Don’t even get me started about that third leg – even when it’s unerect, it says a lot about you, Gramps!"

    show yoshi panic4 at p6_5
    voice audio.yoshi_v_aiden6
    yo "A-Aiden…!!"

    show goro awkward5 at p6_4
    voice audio.goro_v_annoyed3d2
    g "S-Stop staring at it, all of you…! "
    g "Having this isn’t always a good thing either, you know…! Sometimes it’s impossible to keep it hidden away when you have any unexpected—"

    show jin2 dizzy6 at p6_6
    voice audio.jin_v_bye2b2
    j "GAAAHHH!! I CAN’T TAKE IT ANYMORE! PLEASE EXCUSE ME!!" with vpunch

    hide jin2_naked
    hide jin2 dizzy6
    with dissolve

    show darius_naked at p5_1
    show darius play2 at p5_1
    show lloyd_naked at p5_2
    show lloyd shock6 at p5_2
    show aiden_naked at p5_3
    show aiden laugh3 at p5_3
    show goro_naked at p5_4
    show goro awkward5 at p5_4
    show yoshi_naked at p5_5
    show yoshi panic4 at p5_5
    with move

    voice audio.aiden_v_laugh2a1
    a "Hahaha! Look what you just did, Gramps! You scared him with your anaconda!"

    show goro sigh1 at p5_4
    voice audio.goro_v_sigh1a
    g "*sigh* "

    show aiden happy3 at p5_3
    voice audio.aiden_v_well1b1
    a "Well, now that our judge has left the scene, you have to do it, Yoshi!"

    show yoshi confused2 at p5_5
    voice audio.yoshi_v_what4
    yo "Wh-Wha… Do what?"

    show aiden tease2 at p5_3
    voice audio.aiden_v_rush1a1
    a "Isn’t it obvious already? We’re gonna have a “not-so-small” contest on who’s got the best D!"

    show darius bored5 at p5_1
    voice audio.darius_v_shock1b
    d "Oh… We’re doing that now."

    show lloyd pout4 at p5_2
    voice audio.lloyd_v_annoyed1b3
    l "Hmph! I’m not taking part in this!"

    show darius play5 at p5_1
    voice audio.darius_v_lloyd7b
    d "Don’t be shy, Lloyd. "

    show lloyd annoy2 at p5_2
    voice audio.lloyd_v_angry1b3
    l "Easy for you to say with that meat cannon of yours."
    l "Life has just been so unfair to me… Despite my accumulation of good karma, I’m still full of “short”-comings."

    show darius tease4 at p5_1
    voice audio.darius_v_laugh1
    d "You just need to make it “alive”."

    show lloyd scared3 at p5_2
    voice audio.lloyd_v_disgust1b2
    l "WAH! I am NOT giving myself a boner in front of my co-workers!!"

    hide yoshi_naked
    hide yoshi confused2
    show yoshi2_naked at p5_5
    show yoshi2 sigh4 at p5_5
    voice audio.yoshi_v_sigh3a
    yo "*sigh* This is starting to get inappropriate."

    show aiden annoy2 at p5_3
    voice audio.aiden_v_comeon2a
    a "Oh, stop acting so innocent, all of you! None of us are virgins here, right?!"

    hide yoshi2_naked
    hide yoshi2 sigh4
    show yoshi_naked at p5_5
    show yoshi angry3 at p5_5
    voice audio.yoshi_v_what4
    yo "Wh-What the hell, Aiden?!"

    hide goro_naked
    hide goro sigh1
    show goro2_naked at p5_4
    show goro2 think4 at p5_4
    voice audio.goro_v_think1a1
    g "I have a daughter."

    show lloyd worry1 at p5_2
    voice audio.lloyd_v_gulp1c
    l "*gulp*"

    show aiden laugh4 at p5_3
    voice audio.aiden_v_laugh2a1
    a "Hahaha!"

    hide yoshi_naked
    hide yoshi angry3
    show yoshi2_naked at p5_5
    show yoshi2 sigh1 at p5_5
    voice audio.yoshi_v_sigh3a
    yo "*sigh* I should’ve thought twice before letting everyone share a bathroom with you, Aiden…"

    show aiden play3 at p5_3
    voice audio.aiden_v_so2
    a "So, tell us, Yoshi! What makes the best dick in your humble opinion~?"

    $working = False
    $shuffle_menu()
    menu():
        a "So, tell us, Yoshi! What makes the best dick in your humble opinion~?{fast}"
        "Skill.":
            $working = True
            $score_aiden += 1
            $score_bot += 1
            show yoshi2 awkward3 at p5_5
            voice audio.yoshi_v_really6
            yo "Do I really have to answer this, Aiden?!"

            show aiden pout1 at p5_3
            voice audio.aiden_v_comeon1a1
            a "Come on! Don’t be lame, Yoshi!"

            hide yoshi2_naked
            hide yoshi2 awkward3
            show yoshi_naked at p5_5
            show yoshi angry2 at p5_5
            voice audio.yoshi_v_agree2b1
            yo "Fine! It’s HOW YOU USE IT!"

            show aiden bold2 at p5_3
            voice audio.aiden_v_amazed1b1
            a "Sounds like I win~"

            show goro2 angry2 at p5_4
            voice audio.goro_v_what3a
            g "What?! How can you even prove that?!"

            show aiden tease2 at p5_3
            voice audio.aiden_v_unsure3a
            a "I don’t know~ Why don’t you ask Yoshi?"

            hide goro2_naked
            hide goro2 angry2
            show goro_naked at p5_4
            show goro rage2 at p5_4
            voice audio.goro_v_angry1a1
            g "GRRR!!!"

            show aiden tease1 at p5_3
            voice audio.aiden_v_laugh1a1
            a "I heard monster cocks need a lot of blood pumping into them to keep up, so maybe that’s why~"

            show goro disappoint5 at p5_4
            voice audio.goro_v_annoyed1b2
            g "Tch! I’ll have you know this cock lives up to its size! So don’t test me, or else you’ll get a taste of it yourself!"

            show aiden rage1 at p5_3
            voice audio.aiden_v_yeah2b1
            a "Oh yeah? I’d like to see you try!"

            show lloyd sigh5 at p5_2
            voice audio.lloyd_v_rush1c3
            l "Come on, Dar. Let’s hit the showers before we get caught up in any more of this."

            show darius laugh4 at p5_1
            voice audio.darius_v_laugh2a
            d "Haha."

            hide lloyd_naked
            hide lloyd sigh5
            hide darius_naked
            hide darius laugh4
            with dissolve

            show aiden_naked at left
            show aiden rage1 at left
            show goro_naked at center
            show goro disappoint5 at center
            show yoshi_naked at right
            show yoshi angry2 at right
            with move
        "Shape.":
            $working = True
            $score_aiden += 1
            $score_top +=1
            show yoshi2 awkward3 at p5_5
            voice audio.yoshi_v_really6
            yo "Do I really have to answer this, Aiden?!"

            show aiden pout1 at p5_3
            voice audio.aiden_v_comeon1a1
            a "Come on! Don’t be lame, Yoshi!"

            hide yoshi2_naked
            hide yoshi2 awkward3
            show yoshi_naked at p5_5
            show yoshi angry2 at p5_5
            voice audio.yoshi_v_agree2b1
            yo "Fine! It’s HOW IT LOOKS!"

            show aiden bold2 at p5_3
            voice audio.aiden_v_amazed1b1
            a "Sounds like I win~"

            show goro2 angry2 at p5_4
            voice audio.goro_v_what3a
            g "What?! How?!"

            show aiden tease2 at p5_3
            voice audio.aiden_v_unsure3a
            a "I don’t know~ Why don’t you ask Yoshi?"

            hide goro2_naked
            hide goro2 angry2
            show goro_naked at p5_4
            show goro rage2 at p5_4
            voice audio.goro_v_angry1a1
            g "GRRR!!!"

            show aiden tease1 at p5_3
            voice audio.aiden_v_laugh1a1
            a "Not my fault you have a monster cock, Gramps~!"

            show goro disappoint5 at p5_4
            voice audio.goro_v_annoyed1b2
            g "Tch! I’ll have you know this cock lives up to its size! So don’t test me, or else you’ll get a taste of it yourself!"

            show aiden rage1 at p5_3
            voice audio.aiden_v_yeah2b1
            a "Oh yeah? I’d like to see you try!"

            show lloyd sigh5 at p5_2
            voice audio.lloyd_v_rush1c3
            l "Come on, Dar. Let’s hit the showers before we get caught up in any more of this."

            show darius laugh4 at p5_1
            voice audio.darius_v_laugh2a
            d "Haha."

            hide lloyd_naked
            hide lloyd sigh5
            hide darius_naked
            hide darius laugh4
            with dissolve

            show aiden_naked at left
            show aiden rage1 at left
            show goro_naked at center
            show goro disappoint5 at center
            show yoshi_naked at right
            show yoshi angry2 at right
            with move
        "Girth.":
            $working = True
            $score_goro += 1
            $score_top +=1
            show yoshi2 awkward3 at p5_5
            voice audio.yoshi_v_really6
            yo "Do I really have to answer this, Aiden?!"

            show aiden pout1 at p5_3
            voice audio.aiden_v_comeon1a1
            a "Come on! Don’t be lame, Yoshi!"

            hide yoshi2_naked
            hide yoshi2
            show yoshi_naked at p5_5
            show yoshi angry2 at p5_5
            voice audio.yoshi_v_agree2b1
            yo "Fine! It’s GIRTH!"

            show goro2 tease5 at p5_4
            voice audio.goro_v_heh1a
            g "Heh, I win."

            hide aiden_naked
            hide aiden pout1
            show aiden2_naked at p5_3
            show aiden2 annoy3 at p5_3
            voice audio.aiden_v_hey1c1
            a "Hey, mine’s pretty thick too!"

            show goro2 tease2 at p5_4
            voice audio.goro_v_taunt2a
            g "Size matters. Deal with it, chump."

            hide aiden2_naked
            hide aiden2 annoy3
            show aiden_naked at p5_3
            show aiden angry2 at p5_3
            voice audio.aiden_v_goro8b
            a "Yoshi didn’t say that it has to be as thick as an arm, you old man!"

            hide goro2_naked
            hide goro2 tease2
            show goro_naked at p5_4
            show goro tease3 at p5_4
            voice audio.goro_v_heh3b
            g "Hah! Running out of comebacks, I see. Not my fault that you didn’t grow enough, kiddo!"

            show aiden pout4 at p5_3
            voice audio.aiden_v_yeah2b1
            a "Once you see mine all grown up, I’ll drop that jaw of yours!"

            show goro rage1 at p5_4
            voice audio.goro_v_insult2b1
            g "Try me!"

            show lloyd sigh5 at p5_2
            voice audio.lloyd_v_rush1c3
            l "Come on, Dar. Let’s hit the showers before we get caught up in any more of this."

            show darius laugh4 at p5_1
            voice audio.darius_v_laugh2a
            d "Haha."

            hide lloyd_naked
            hide lloyd sigh5
            hide darius_naked
            hide darius laugh4
            with dissolve

            show aiden_naked at left
            show aiden pout4 at left
            show goro_naked at center
            show goro rage1 at center
            show yoshi_naked at right
            show yoshi angry2 at right
            with move

        "Length.":
            $working = True
            $score_goro += 1
            $score_bot += 1
            show yoshi2 awkward3 at p5_5
            voice audio.yoshi_v_really6
            yo "Do I really have to answer this, Aiden?!"

            show aiden pout1 at p5_3
            voice audio.aiden_v_comeon1a1
            a "Come on! Don’t be lame, Yoshi!"

            hide yoshi2_naked
            hide yoshi2 awkward3
            show yoshi_naked at p5_5
            show yoshi angry2 at p5_5
            voice audio.yoshi_v_agree2b1
            yo "Fine! It’s LENGTH!"

            show goro2 tease5 at p5_4
            voice audio.goro_v_heh1a
            g "Heh, I win."

            hide aiden_naked
            hide aiden pout1
            show aiden2_naked at p5_3
            show aiden2 annoy3 at p5_3
            voice audio.aiden_v_hey1c1
            a "Hey, mine’s pretty long too!"

            show goro2 tease2 at p5_4
            voice audio.goro_v_taunt2a
            g "Size matters. Deal with it, chump."

            hide aiden2_naked
            hide aiden2 annoy3
            show aiden_naked at p5_3
            show aiden angry2 at p5_3
            voice audio.aiden_v_goro8b
            a "Yoshi didn’t say that it has to be as long as a pole, you old man!"

            hide goro2_naked
            hide goro2 tease2
            show goro_naked at p5_4
            show goro tease3 at p5_4
            voice audio.goro_v_heh3b
            g "Hah! Running out of comebacks, I see. Not my fault that you didn’t grow enough, kiddo!"

            show aiden pout4 at p5_3
            voice audio.aiden_v_yeah2b1
            a "Once you see mine all grown up, I’ll drop that jaw of yours!"

            show goro rage1 at p5_4
            voice audio.goro_v_insult2b1
            g "Try me!"

            show lloyd sigh5 at p5_2
            voice audio.lloyd_v_rush1c3
            l "Come on, Dar. Let’s hit the showers before we get caught up in any more of this."

            show darius laugh4 at p5_1
            voice audio.darius_v_laugh2a
            d "Haha."

            hide lloyd_naked
            hide lloyd sigh5
            hide darius_naked
            hide darius laugh4
            with dissolve

            show aiden_naked at left
            show aiden pout4 at left
            show goro_naked at center
            show goro rage1 at center
            show yoshi_naked at right
            show yoshi angry2 at right
            with move

    hide yoshi_naked
    hide yoshi angry2
    show yoshi2_naked at right
    show yoshi2 sigh4 at right
    voice audio.yoshi_v_comp7
    yo "Everyone else went ahead, you two… Calm down already."

    show aiden awkward3 at left
    voice audio.aiden_v_oops1a
    a "Whoops, I got too carried away!"

    show goro sigh3 at center
    voice audio.goro_v_sigh1a
    g "*sigh* That was embarrassing for our guests…"

    show yoshi2 shy1 at right
    voice audio.yoshi_v_guys4
    yo "L-Let’s just get washed up, you guys…"

    show aiden confused2 at left
    voice audio.aiden_v_think1a1
    a "There’s only two cubicles left though… Even with Darius and Lloyd sharing one…"

    hide yoshi2_naked
    hide yoshi2 shy1
    show yoshi_naked at right
    show yoshi confused3 at right
    voice audio.yoshi_v_think1a
    yo "It looks like two of us have to share one as well…"

    if d5_goro == True:
        show goro_naked at p5_4
        show goro talk1 at p5_4
        with move

        voice audio.goro_v_rush3b1
        g "You’re coming with me then, Yoshinori."

        show yoshi shock3 at right
        voice audio.yoshi_v_shock2a
        yo "W-Wah…! Sir Goro, wait—"

        show goro_naked at right
        show goro talk1 at right
        with move

        hide goro_naked
        hide goro talk1
        hide yoshi_naked
        hide yoshi shock2
        with dissolve

        show aiden rage6 at left
        voice audio.aiden_v_hey1c1
        a "HEY!"

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

        $ location = location_bathroom
        show screen location
        show screen timeline
        show screen quick_menu
        $quick_menu = True

        jump day5_goro_1

    elif d5_aiden == True:
        show aiden_naked at p5_4
        show aiden excited3 at p5_4
        with move
        voice audio.aiden_v_yoshi3a
        a "Dibs on Yoshi~!"

        show yoshi shock2 at right
        voice audio.yoshi_v_shock2a
        yo "W-Wah…! Aiden, wait—"

        show aiden_naked at right
        show aiden excited2 at right
        with move

        hide aiden_naked
        hide aiden excited2
        hide yoshi_naked
        hide yoshi shock2
        with dissolve

        show goro rage1 at center
        voice audio.goro_v_hey4a
        g "H-Hey…!!"

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

        $ location = location_bathroom
        show screen location
        show screen timeline
        show screen quick_menu
        $quick_menu = True

        jump day5_aiden_1
