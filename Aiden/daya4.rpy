label day4_aiden:
    $ day = "79"
    $ time = timeline_timeday
    $ location = location_hotelroom
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    $ working = True
    $day3_aiden = False

    scene bg_hotel_room1_day with fade
    play music go_with_the_flow_slow loop

    show aiden2_undie at center
    show aiden2 pain1 at center
    voice audio.aiden_v_hngh1b2
    a "Hngh… I feel like my head is gonna split in half… "

    show aiden2_undie at right2
    show aiden2 pain1 at right2
    with move

    show yoshi_sleep at left2
    show yoshi shock2 at left2
    with dissolve

    voice audio.yoshi_v_oh1
    yo "Oh, Aiden! You’re up!"

    show aiden2 pain3 at right2
    voice audio.aiden_v_shock5a
    a "G-Gah! Not so loud, Yoshi…"

    hide yoshi_sleep
    hide yoshi shock2
    show yoshi2_sleep at left2
    show yoshi2 shy5 at left2
    voice audio.yoshi_v_uh1a
    yo "That wasn’t loud at all…"

    show aiden2 upset6 at right2
    voice audio.aiden_v_hngh1b4
    a "Ugh… I’m sorry… I don’t feel so good…"

    hide yoshi2_sleep
    hide yoshi2 shy5
    show yoshi_sleep at left2
    show yoshi comp2 at left2
    voice audio.yoshi_v_confident2
    yo "Here, I ordered some warm soup and got you some aspirin."

    show aiden2 comp3 at right2
    voice audio.aiden_v_thanks1c2
    a "Thanks…"

    hide yoshi_sleep
    hide yoshi comp2
    show yoshi2_sleep at left2
    show yoshi2 comp5 at left2
    voice audio.yoshi_v_huh1
    yo "Looks like you have quite the hangover, huh? You really didn’t hold back on those drinks…"

    show aiden2 comp6 at right2
    voice audio.aiden_v_yeah1g1
    a "Y-Yeah… And from all the stuff laying around, it looks like you’ve been taking care of me, huh…?"

    show yoshi2 awkward4 at left2
    voice audio.yoshi_v_oh2
    yo "O-Oh, you mean the empty bucket…? Well… You did puke around two times last night…"

    show aiden2 pain1 at right2
    voice audio.aiden_v_swear3b
    a "Oh crap, I don’t even remember doing that… Sorry, Yoshi…"

    hide yoshi2_sleep
    hide yoshi2 awkward4
    show yoshi_sleep at left2
    show yoshi laugh2 at left2
    voice audio.yoshi_v_comp2
    yo "Haha! It’s alright, Aiden! You’ve cleaned up after my messes plenty of times before!"
    yo "I’m usually the one who gets drunk first after all…"

    show yoshi comp3 at left2
    voice audio.yoshi_v_laugh1
    yo "When I saw you chugging those drinks last night, I decided to slow down to make sure we both didn’t get wasted, haha!"

    show aiden2 upset5 at right2
    voice audio.aiden_v_yeah1c1
    a "Yeah… Good call."

    show aiden2 sigh4 at right2
    voice audio.aiden_v_think1b
    a "I… can’t even remember exactly how things went down yesterday… "

    show yoshi shock2 at left2
    voice audio.yoshi_v_wait3b
    yo "W-Wait, really? You don’t remember anything at all? "

    show aiden2 confused5 at right2
    voice audio.aiden_v_confused1c1
    a "Eh… Just a little… Everything’s kind of a blur… "

    $ working = False
    $ shuffle_menu()
    menu():
        a "Eh… Just a little… Everything’s kind of a blur… {fast}"
        "You were a drunken mess":
            $ score_aiden -= 2
            $ working = True
            hide yoshi_sleep
            hide yoshi shock2
            show yoshi2_sleep at left2
            show yoshi2 think2 at left2
            voice audio.yoshi_v_well3
            yo "You were so drunk you started acting crazy in the club…"

            show aiden2 awkward5 at right2
            voice audio.aiden_v_oops2a
            a "Uh-oh, don’t tell me I turned into a puking machine?!"

            show yoshi2 worry2 at left2
            voice audio.yoshi_v_no5
            yo "N-No! I-I mean… I don’t know if what you did was worse, but…"
            yo "You kinda stripped in front of everyone there…"

            hide aiden2_undie
            hide aiden2 awkward5
            show aiden_undie at right2
            show aiden shock2 at right2
            voice audio.aiden_v_what4a
            a "Oh my god, I did what?!"

            show yoshi2 sigh4 at left2
            voice audio.yoshi_v_sigh3a
            yo "It got even wilder when you took your pants off… People mistook you as one of the strippers…"
        "You made a scene.":
            $ working = True
            $ score_aiden -= 1
            hide yoshi_sleep
            hide yoshi shock2
            show yoshi2_sleep at left2
            show yoshi2 think2 at left2
            voice audio.yoshi_v_well3
            yo "Well… You kinda made a scene when you stripped in front of everyone at the club… "

            hide aiden2_undie
            hide aiden2 confused5
            show aiden_undie at right2
            show aiden shock2 at right2
            voice audio.aiden_v_what4a
            a "Oh my god, I did what?!"

            show yoshi2 sigh4 at left2
            voice audio.yoshi_v_sigh3a
            yo "It got even wilder when you took your pants off… People mistook you as one of the strippers…"
        "You passed out." if a3mini == False:          # need to test this, not sure it'll work
            $ working = True
            hide yoshi_sleep
            hide yoshi shock2
            show yoshi2_sleep at left2
            show yoshi2 think2 at left2
            voice audio.yoshi_v_well3
            yo "For starters, you kinda passed out on me… "
            yo "I had no idea how I was gonna bring you back to our room, especially since you were fully naked…"

            hide aiden2_undie
            hide aiden2 confused5
            show aiden_undie at right2
            show aiden tease1 at right2
            voice audio.aiden_v_oho1a
            a "Fully naked? Oho~ I knew you couldn’t resist me, Yoshi."

            show yoshi2 shy5 at left2
            voice audio.yoshi_v_no4
            yo "N-No Aiden. You stripped yourself… in front of everyone at the club."

            show aiden shock2 at right2
            voice audio.aiden_v_what4a
            a "Oh my god, I did what?!"

            show yoshi2 awkward4 at left2
            voice audio.yoshi_v_oops2
            yo "Everything got wilder when you took your pants off… People mistook you as one of the strippers…"

            hide aiden_undie
            hide aiden shock2
            show aiden2_undie at right2
            show aiden2 tease4 at right2
            voice audio.aiden_v_laugh1b2
            a "Hehe, was I at least good at it?"

            show yoshi2 sigh4 at left2
            voice audio.yoshi_v_sigh3a
            yo "*sigh* I should’ve expected you’d ask that…"
        "We almost had sex..." if a3mini == False:          # need to test this, not sure it'll work
            $ working = True
            $ score_aiden += 1
            hide yoshi_sleep
            hide yoshi shock2
            show yoshi2_sleep at left2
            show yoshi2 think2 at left2
            voice audio.yoshi_v_well3
            yo "W-Well… How do I put this…?"
            yo "We… almost had sex… in the club…"

            hide aiden2_undie
            hide aiden2 confused5
            show aiden_undie at right2
            show aiden shock2 at right2
            voice audio.aiden_v_shock1a1
            a "WHOA! Did we really?!"

            show yoshi2 shy5 at left2
            voice audio.yoshi_v_uh1a
            yo "W-Well… I kinda had to stop myself in the middle before I got too carried away."
            yo "The booth we were in wasn’t very private and I was worried someone would catch us…"

            show yoshi2 sigh4 at left2
            voice audio.yoshi_v_but2
            yo "But I guess I don’t know if that’s any worse than having the entire club watch your strip show…"

            show aiden shock2 at right2
            voice audio.aiden_v_what4a
            a "Oh my god, I did what?!"

            show yoshi2 awkward4 at left2
            voice audio.yoshi_v_oops2
            yo "Everything got wilder when you took your pants off… People mistook you as one of the strippers…"

            hide aiden_undie
            hide aiden shock2
            show aiden2_undie at right2
            show aiden2 tease4 at right2
            voice audio.aiden_v_laugh1b2
            a "Hehe, was I at least good at it?"

            show yoshi2 sigh4 at left2
            voice audio.yoshi_v_sigh3a
            yo "*sigh* I should’ve expected you’d ask that…"
        "Even the part when..." if a3mini == True:
            $ working = True
            $ score_aiden += 2
            $ score_bot += 1
            hide yoshi_sleep
            hide yoshi shock2
            show yoshi2_sleep at left2
            show yoshi2 shy5 at left2
            voice audio.yoshi_v_uh1a
            yo "Even the part when we… did ‘it’?"

            hide aiden2_undie
            hide aiden2 confused5
            show aiden_undie at right2
            show aiden shock2 at right2
            voice audio.aiden_v_shock1a1
            a "WHOA! We had sex?! "

            show yoshi2 comp6 at left2
            voice audio.yoshi_v_yeah4
            yo "Y-Yeah…"

            show aiden laugh1 at right2
            voice audio.aiden_v_laugh2a1
            a "No wonder my butt was so sore when I woke up! I thought I was just having a wet dream, hahaha!"

            show yoshi2 shy5 at left2
            voice audio.yoshi_v_aiden5
            yo "I-It was very real, Aiden…"

            show aiden excited1 at right2
            voice audio.aiden_v_swear2a2
            a "Damn! I scored one with you and I barely even remember, hahaha!"

            show yoshi2 sigh4 at left2
            voice audio.yoshi_v_confused1a
            yo "Well, let’s just hope nobody saw us."
            yo "Although I’m pretty sure everyone got a clear view of your half-naked body when I was dragging you out…"

            hide aiden_undie
            hide aiden excited1
            show aiden2_undie at right2
            show aiden2 confused2 at right2
            voice audio.aiden_v_confused1a2
            a "Eh? How did that happen?"

            show yoshi2 confused5 at left2
            voice audio.yoshi_v_really1
            yo "You really don’t remember? You stripped in front of everyone at the club!"

            hide aiden2_undie
            hide aiden2 confused2
            show aiden_undie at right2
            show aiden shock2 at right2
            voice audio.aiden_v_what4a
            a "Oh my god, I did what?!"

            show yoshi2 awkward4 at left2
            voice audio.yoshi_v_oops2
            yo "Everything got wilder when you took your pants off… People mistook you as one of the strippers…"

            show aiden excited3 at right2
            voice audio.aiden_v_amazed2b1
            a "HOLY CRAP! That’s awesome!"

            show yoshi2 sigh4 at left2
            voice audio.yoshi_v_sigh3a
            yo "*sigh* I knew you’d say something like that…"

            show aiden tease2 at right2
            voice audio.aiden_v_laugh1b2
            a "Hehe, did they like the show?"

            show yoshi2 shy6 at left2
            voice audio.yoshi_v_yeah4
            yo "They sure did…"
        "We did it in public..." if a3mini == True:
            $ score_aiden += 2
            $ score_top += 2
            $ working = True
            hide yoshi_sleep
            hide yoshi shock2
            show yoshi2_sleep at left2
            show yoshi2 shy5 at left2
            voice audio.yoshi_v_well3
            yo "Well, Aiden… We kinda did ‘it’… in public…"

            hide aiden2_undie
            hide aiden2 confused5
            show aiden_undie at right2
            show aiden shock2 at right2
            voice audio.aiden_v_shock1a1
            a "WHOA! We had sex?! Like in front of a crowd?! "

            show yoshi2 panic4 at left2
            voice audio.yoshi_v_no5
            yo "N-No…! I mean, we were in a booth, and things just kind of happened…"
            yo "Even though no one could hear us with the loud music playing, we weren’t really hidden, so I’m pretty sure someone saw us…"

            show aiden laugh1 at right2
            voice audio.aiden_v_laugh2a1
            a "Huh, no wonder my butt was pretty sore when I woke up! I thought I was just having a wet dream, hahaha!"

            show yoshi2 shy5 at left2
            voice audio.yoshi_v_aiden5
            yo "I-It was very real, Aiden…"

            show aiden excited1 at right2
            voice audio.aiden_v_swear2a2
            a "Damn! I scored one with you and I barely even remember, hahaha!"

            show yoshi2 sigh4 at left2
            voice audio.yoshi_v_confused1a
            yo "Well, let’s just hope nobody saw us."
            yo "Although I’m pretty sure everyone got a clear view of your half-naked body when I was dragging you out…"

            hide aiden_undie
            hide aiden excited1
            show aiden2_undie at right2
            show aiden2 confused2 at right2
            voice audio.aiden_v_confused1a2
            a "Eh? How did that happen?"

            show yoshi2 confused5 at left2
            voice audio.yoshi_v_really1
            yo "You really don’t remember? You stripped in front of everyone at the club!"

            hide aiden2_undie
            hide aiden2 confused2
            show aiden_undie at right2
            show aiden shock2 at right2
            voice audio.aiden_v_what4a
            a "Oh my god, I did what?!"

            show yoshi2 awkward4 at left2
            voice audio.yoshi_v_oops2
            yo "Everything got wilder when you took your pants off… People mistook you as one of the strippers…"

            show aiden excited3 at right2
            voice audio.aiden_v_amazed2b1
            a "HOLY CRAP! That’s awesome!"

            show yoshi2 sigh4 at left2
            voice audio.yoshi_v_sigh3a
            yo "*sigh* I knew you’d say something like that…"

            show aiden tease2 at right2
            voice audio.aiden_v_laugh1b2
            a "Hehe, did they like the show?"

            show yoshi2 shy6 at left2
            voice audio.yoshi_v_yeah4
            yo "They sure did…"

    hide aiden2_undie
    hide aiden2 tease4
    show aiden_undie at right2
    show aiden laugh3 at right2
    voice audio.aiden_v_laugh2a1
    a "Hahaha! Your reaction always cracks me up, even after all this time."

    show yoshi2_sleep at left2
    show yoshi2 comp3 at left2
    voice audio.yoshi_v_really6
    yo "Even though I’m used to it, you still manage to catch me off guard every time..."

    show aiden tease2 at right2
    voice audio.aiden_v_well1b2
    a "Nothing will beat the first time I stripped in front of you, though!"

    show yoshi2 think2 at left2
    voice audio.yoshi_v_actually1b
    yo "It was more than just me who saw you naked, Aiden… Remember?"

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
    with fade
    $quick_menu = False
    $ renpy.pause (2.0, hard=True)

    $ location = location_fields
    $ day = "??"
    $ time = timeline_timeday
    $ season = season_summer
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_fields_past_day with fade
    play music camping_time loop
    play bgsound sfxloop_windy loop

    show ygoro_camp at p5_1
    show ygoro happy3 at p5_1
    show yyuri_camp at p5_2
    show yyuri norm1 at p5_2
    show yyoshi_camp at p5_3
    show yyoshi norm1 at p5_3
    show yaiden_casual at p5_4
    show yaiden norm1 at p5_4
    show andre_camp at p5_5
    show andre norm1 at p5_5
    voice audio.ygoro_v_alright1a
    g "Alright, that was a good hike! Everyone knows the drill now, right? "
    g "Let’s set up the camp! I’ll check around and see if anyone needs my help!"

    show ygoro bold5 at p5_1
    voice audio.ygoro_v_dismiss2a
    g "Dismissed!"

    hide ygoro_camp
    hide ygoro bold5
    with dissolve

    show andre talk1 at p5_5
    voice audio.andre_v_aiden1b
    u "Aiden, start the fire, I’ll go and prepare lunch."

    show yaiden talk2 at p5_4
    voice audio.yaiden_v_yessir1a1
    a "Yes, Dad!"

    hide andre_camp
    hide andre talk1
    with dissolve

    show yyuri_camp at left
    show yyuri sigh3 at left
    show yyoshi_camp at center
    show yyoshi norm1 at center
    show yaiden_casual at right
    show yaiden talk2 at right
    with move

    voice audio.yyuri_v_ugh1a
    yu "Ugh… Why the heck did Dad pick the only spot with no shade for us to camp in?!"

    show yyoshi talk3 at center
    voice audio.yyoshi_v_well1
    yo "Well, the handbook did say that one of the best spots for camping is in a nice, flat grassy area! "

    show yyuri pout1 at left
    voice audio.yyuri_v_hmph1a
    yu "Hmph! Did the handbook know it was gonna be this hot today?"

    show yyoshi comp2 at center
    voice audio.yyoshi_v_anyway1a
    yo "Why don’t we set up the tents to get some shade then?"

    show yyuri sigh1 at left
    voice audio.yyuri_v_agree5a2
    yu "Fine… Let me grab our stuff…"

    hide yyuri_camp
    hide yyuri sigh1
    with dissolve

    show yaiden_casual at right2
    show yaiden tired4 at right2
    show yyoshi_camp at left2
    show yyoshi comp2 at left2
    with move

    show yaiden tired4 at right2
    voice audio.yaiden_v_well1a1
    a "Yuri’s kinda right, though… I’m already sweating bullets out here."
    a "Starting a fire is the last thing I wanna do… I wish we could at least cool down first…"

    show yyoshi excited1 at left2
    voice audio.yyoshi_v_idea1
    yo "Oh, I have an idea, Aiden! "
    yo "I know a place not too far from here where we could chill! "

    show yaiden shock2 at right2
    voice audio.yaiden_v_really1a
    a "Whoa, really? "

    show yyoshi laugh2 at left2
    voice audio.yyoshi_v_yeah2
    yo "Yeah! I kinda memorized this place when I got my navigation badge!"

    show yaiden worry2 at right2
    voice audio.yaiden_v_think3a
    a "A-Are you sure we should leave the group, though? Won’t we get in trouble?"

    show yyoshi comp5 at left2
    voice audio.yyoshi_v_comp2
    yo "It’s okay! The place is really close by and isolated, and plus everyone will be busy setting up!"
    yo "They won’t even notice we’re gone, and we can come back as soon as we’ve cooled down!"

    show yaiden comp5 at right2
    voice audio.yaiden_v_alright1a
    a "Well… sure, I won’t say no to that! Take me, take me!"

    show yyoshi play2 at left2
    voice audio.yyoshi_v_ssh1a
    yo "Alright! But shhh… don’t act suspicious and follow me!"

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black
    hide screen location
    hide screen timeline
    hide screen quick_menu
    with fade
    $quick_menu = False
    $ renpy.pause (2.0, hard=True)

    $ location = location_waterfall
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_waterfall_past_day with fade
    play music go_with_the_flow loop
    play bgsound sfxloop_waterfall loop

    show yaiden_casual at left2
    show yaiden excited3 at left2
    show yyoshi_camp at right2
    show yyoshi bold2 at right2
    voice audio.yyoshi_v_tada1
    yo "Tada!"

    show yaiden excited1 at left2
    voice audio.yaiden_v_amazed2b2
    a "WOOOWWW!! "

    show yyoshi bold5 at right2
    voice audio.yyoshi_v_greet3a
    yo "Welcome to Buddy Falls, Aiden! Isn’t this place amazing?"

    show yaiden amazed1 at left2
    voice audio.yaiden_v_hey1c
    a "Why didn’t we come here to begin with?! With this heat, this would’ve been the perfect camping spot!"

    show yyoshi happy2 at right2
    voice audio.yyoshi_v_laugh1
    yo "Well, Sir Goro actually brought us here not too long ago! It’s partly why I still know the way here, haha!"

    show yaiden grin1 at left2
    voice audio.yaiden_v_praise1a
    a "This is just what I need to beat the heat!"

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    hide yaiden_casual
    hide yaiden grin1
    show yaiden_naked at left2
    show yaiden amazed1 at left2

    play music here_they_come_fast loop
    show cg fade at truecenter
    show fxa4 at fx_pos
    with vpunch

    voice audio.yyoshi_vsa8_line1
    yo "WAHHHH!!! A-Aiden!!! "

    voice audio.yaiden_vsa8_line1
    a "Ehhh? What?"

    voice audio.yyoshi_vsa8_line2
    yo "Y-You’re… NAKED! "

    voice audio.yaiden_vsa8_line2
    a "Yup! Hahaha!"

    voice audio.yyoshi_vsa8_line3
    yo "W-We’re outdoors! What if someone sees you?!"

    voice audio.yaiden_vsa8_line3
    a "Then I’ll show them how to make a good splash!"

    voice audio.yaiden_vsa8_line4
    a "COWA-GANGBANG!"

    play sound sfx_splash
    hide cg fade
    hide fxa4
    with flash

    hide yaiden_naked
    hide yaiden amazed1
    show yaiden_naked2 at left2
    show yaiden play1 at left2
    hide yyoshi_camp
    hide yyoshi bold5
    show yyoshi_camp2 at right2
    show yyoshi angry2 at right2
    voice audio.yyoshi_v_aiden6
    yo "A-Aiden! You got me all wet!"

    show yaiden tease1 at left2
    voice audio.yaiden_v_ohno1a
    a "Oh no~ I guess you gonna have to strip too!"

    show yyoshi scared3 at right2
    voice audio.yyoshi_v_shock2b
    yo "W-Wah! Why would I do that?! "

    show yaiden tease4 at left2
    voice audio.yaiden_v_confused1a3
    a "You’re not gonna swim with clothes on, are you? Isn’t that why you brought me here in the first place?"

    show yyoshi worry2 at right2
    voice audio.yyoshi_v_ah3
    yo "I just thought we would dip our feet in, or wash our faces…"

    show yaiden relief2 at left2
    voice audio.yaiden_v_comeon1a1
    a "We wouldn’t have cooled off that way! I already feel so much better, so you should jump in too!"

    show yyoshi shy1 at right2
    yo "..."

    show yaiden tease2 at left2
    voice audio.yaiden_v_laugh1c1
    a "Hehe, are you staring at my thing?"

    show yyoshi awkward4 at right2
    voice audio.yyoshi_v_what4
    yo "Wh-What?! I-I am not—"

    show yaiden tease5 at left2
    voice audio.yaiden_v_yeah2b1
    a "Your pants say otherwise."

    show yyoshi angry2 at right2
    voice audio.yyoshi_v_hey1
    yo "Y-You were distracting me!"

    show yaiden bold2 at left2
    voice audio.yaiden_v_rush1b1
    a "Well, don’t just stand there, join me! The water’s fine!"

    show yyoshi angry3 at right2
    voice audio.yyoshi_v_agree2b1
    yo "Fine! But I’m not getting naked!"

    hide yyoshi_camp2
    hide yyoshi angry3
    show yyoshi_undie at right2
    show yyoshi angry2 at right2
    with dissolve

    show yyoshi_undie at center
    show yyoshi angry2 at center
    with move

    hide yyoshi_undie
    hide yyoshi angry2
    show yyoshi_undie2 at center
    show yyoshi relief2 at center
    with dissolve

    voice audio.yyoshi_v_relief1
    yo "Ahhh..."

    show yyoshi_undie2 at left2
    show yyoshi relief2 at left2
    show yaiden_naked2 at right2
    show yaiden relief2 at right2
    with move

    voice audio.yaiden_v_see1a
    a "See? Isn’t that nice?"

    show yyoshi relief5 at left2
    voice audio.yyoshi_v_yeah3
    yo "Y-Yeah… It’s so refreshing… "

    show yyoshi relief4 at left2
    voice audio.yyoshi_v_relief2
    yo "Wheww… On a hot day like this, I could float here all day!"

    show yaiden laugh2 at right2
    voice audio.yaiden_v_see2a
    a "Hehe, I told you!"

    show yyoshi_undie2 at p5_4
    show yyoshi shock1 at p5_4
    show yaiden_naked2 at p5_5
    show yaiden shock1 at p5_5
    with move

    show ylloyd_camp at p5_1
    show ylloyd angry2 at p5_1
    show ydarius_camp at p5_2
    show ydarius norm4 at p5_2
    with dissolve

    voice audio.ylloyd_v_excited2b
    l "A-ha! Found you two!"

    show yyoshi scared3 at p5_4
    voice audio.yyoshi_v_shock2a
    yo "WAHHH!!!" with vpunch
    yo "H-How did you guys find us?!"

    show ylloyd explain1 at p5_1
    voice audio.ylloyd_v_sus2a2
    l "We saw you both acting sus and we followed to see what you two were up to!"
    l "And boy was I right! Everyone’s melting from the heat, so I knew you must’ve been going to some super-secret hideout!"

    show ydarius bold2 at p5_2
    voice audio.ydarius_v_excited2c
    d "I want to swim."

    show yyoshi panic4 at p5_4
    voice audio.yyoshi_v_oops1
    yo "Oh no… With four of us missing, I’m sure Sir Goro will notice…!"

    hide ydarius_camp
    hide ydarius bold2
    show ydarius_undie at p5_2
    show ydarius relief2 at p5_2
    with dissolve

    voice audio.ydarius_v_conj2a2
    d "I’m going in."

    show yyoshi panic3 at p5_4
    voice audio.yyoshi_v_wait3
    yo "W-Wait! Let’s go back to camp or else we’ll all get in trouble!"

    show ylloyd play2 at p5_1
    voice audio.ylloyd_v_laugh1b
    l "Hehe, this is your idea so it’s all on you~! "

    hide ylloyd_camp
    hide ylloyd play2
    show ylloyd_undie at p5_1
    show ylloyd play2 at p5_1
    with dissolve

    show ylloyd_undie at p5_3
    show ylloyd laugh6 at p5_3
    with move

    play sound sfx_splash
    voice audio.ylloyd_v_celebarate1a3
    l "CANNONBALL!" with flash

    show ydarius_undie at p4_1
    show ydarius relief2 at p4_1
    show ylloyd_undie at p4_2
    show ylloyd laugh6 at p4_2
    show yyoshi_undie2 at p4_3
    show yyoshi panic3 at p4_3
    show yaiden_naked2 at p4_4
    show yaiden at p4_4
    with move

    hide ydarius_undie
    hide ydarius relief2
    hide ylloyd_undie
    hide ylloyd laugh6

    show ydarius_undie2 at p4_1
    show ydarius relief2 at p4_1
    show ylloyd_undie2 at p4_2
    show ylloyd laugh6 at p4_2
    voice audio.ylloyd_v_relief3d
    l "FWAH! That hits the spot!"

    show yyoshi sigh1 at p4_3
    voice audio.yyoshi_v_sigh2
    yo "*sigh* You could at least be quiet, you know…"

    show yaiden laugh1 at p4_4
    voice audio.yaiden_v_yoshi3a
    a "Haha, come on, Yoshi! Let loose and try to have fun! "

    show ydarius tease2 at p4_1
    voice audio.ydarius_v_question2a1
    d "Is that why your dick is out?"

    show ylloyd shock3 at p4_2
    voice audio.ylloyd_v_denial3a1
    l "No way! You’re actually naked down there!? DAMN, you got guts!"

    show yaiden bold2 at p4_4
    voice audio.yaiden_v_yeah1a1
    a "Yeah! You guys should try it too! The water feels really good down there!"

    show yyoshi scared3 at p4_3
    voice audio.yyoshi_v_aiden6
    yo "Aiden…!!"

    show yaiden comp5 at p4_4
    voice audio.yaiden_v_comp2a
    a "It’s fine, Yoshi! It’s just us here, anyways!"

    show ylloyd confused3 at p4_2
    voice audio.ylloyd_v_agree2a3
    l "Yeah! Besides, haven’t you guys seen each other naked in the showers already? "

    show yyoshi shy4 at p4_3
    voice audio.yyoshi_v_no4
    yo "N-No, not really… This is the first time."

    show yaiden pout2 at p4_4
    voice audio.yaiden_v_comeon1b1
    a "Yeah, so it’s not fair I’m the only one!"

    show yaiden_naked2 at p4_3
    show yaiden pout2 at p4_3
    with move

    hide yyoshi_undie2
    hide yyoshi shy4
    show yyoshi_naked2 at p4_3
    show yyoshi panic5 at p4_3
    with dissolve

    show yaiden_naked2 at p4_4
    show yaiden excited1 at p4_4
    with move

    voice audio.yaiden_v_here1a
    a "There! That’s much better!"

    show yyoshi scared3 at p4_3
    voice audio.yyoshi_v_aiden6
    yo "A-AIDEN!! WHAT THE HELL?!" with vpunch

    show yaiden excited3 at p4_4
    voice audio.yaiden_v_amazed2c1
    a "Wow! You have a nice one too, Yoshi!"

    show yyoshi scared2 at p4_3
    voice audio.yyoshi_v_stop1
    yo "S-Stop staring at it!"

    show ylloyd blep5 at p4_2
    voice audio.ylloyd_v_geez1a1
    l "Geez… Get a room, you two."

    show ydarius tease3 at p4_1
    voice audio.ydarius_v_tease2b
    d "Ding dong. "

    show yyoshi awkward4 at p4_3
    voice audio.yyoshi_v_rush7a
    yo "N-Now we really have to get out of here, before anyone—"

    show ydarius shock1 at p4_1
    show ylloyd panic1 at p4_2
    show yyoshi scared1 at p4_3
    show yaiden panic1 at p4_4
    voice audio.ygoro_v_greet3b1
    mys "THERE YOU ARE!!!" with vpunch

    show ydarius_undie2 at p7_4
    show ydarius shock1 at p7_4
    show ylloyd_undie2 at p7_5
    show ylloyd panic1 at p7_5
    show yyoshi_naked2 at p7_6
    show yyoshi scared1 at p7_6
    show yaiden_naked2 at p7_7
    show yaiden at p7_7
    with move

    show andre_camp at p7_1
    show andre shock1 at p7_1
    show ygoro_camp at p7_3
    show ygoro angry1 at p7_3
    show yyuri_camp at p7_2
    show yyuri fangirl3 at p7_2
    with dissolve

    voice audio.yyuri_v_shock2a
    yu "*gasp*"

    show ygoro angry4 at p7_3
    voice audio.ygoro_v_question1a1
    g "Is this where you boys have been?! I was looking all over the campsite for you!"

    show andre angry2 at p7_1
    voice audio.andre_v_aiden4b
    u "Aiden! W-Why are you butt naked?!"

    show yyuri fangirl2 at p7_2
    voice audio.yyuri_v_kyaa1
    yu "Kyaaaa!!!! Why isn’t everybody?! That’s the bigger question! "
    yu "My eyes have been blessed on this day! Just when I thought today couldn’t get any hotter! "

    show andre_camp at p8_2
    show andre angry2 at p8_2
    show yyuri_camp at p8_3
    show yyuri fangirl2 at p8_3
    show ygoro_camp at p8_4
    show ygoro angry4 at p8_4
    show ydarius_undie2 at p8_5
    show ydarius shock1 at p8_5
    show ylloyd_undie2 at p8_6
    show ylloyd panic1 at p8_6
    show yyoshi_naked2 at p8_7
    show yyoshi scared1 at p8_7
    show yaiden_naked2 at p8_8
    show yaiden at p8_8
    with move

    show yemilia_camp at p8_1
    show yemilia confused2 at p8_1
    with dissolve

    voice audio.yemilia_v_oh4
    e "I heard screaming did someone— oh…"

    show yemilia annoy2 at p8_1
    voice audio.yemilia_v_ugh1
    e "Ew."

    show andre angry3 at p8_2
    voice audio.andre_v_angry1b
    u "A-Aiden, put something on this instant! "

    show yaiden panic4 at p8_8
    voice audio.yaiden_v_dad6a
    a "D-Dad?!"

    show ygoro panic2 at p8_4
    voice audio.ygoro_v_wait3b1
    g "Oh no, the other campers are coming in…"

    play sound sfx_splash
    all "Wooo!! River party!!!" with vpunch

    show ygoro rage1 at p8_4
    voice audio.ygoro_v_scold1c1
    g "E-Everyone, settle down!!"

    show andre_camp at p8_3
    show andre angry3 at p8_3
    show yyuri_camp at p8_2
    show yyuri fangirl2 at p8_2
    with move

    voice audio.andre_v_sorry2a
    u "This must be Aiden’s idea, I-I’m so sorry about this, sir!! I-I’ll get this under control…!"

    show andre_camp at p8_3
    show andre angry3 at p8_3
    show yaiden_naked2 at p8_4
    show yaiden panic4 at p8_4
    show ygoro_camp at p8_5
    show ygoro rage1 at p8_5
    show ydarius_undie2 at p8_6
    show ydarius shock1 at p8_6
    show ylloyd_undie2 at p8_7
    show ylloyd panic1 at p8_7
    show yyoshi_naked2 at p8_8
    show yyoshi scared1 at p8_8
    with move

    hide yaiden_naked2
    hide yaiden panic4
    show yaiden_naked2 at p8_4
    show yaiden panic4 at p8_4
    voice audio.yaiden_v_ah1b
    a "Ah, Dad… I uhh…"

    $working = False
    $shuffle_menu()
    menu():
        a "Ah, Dad… I uhh…{fast}"
        "Aiden was hot.":
            $working = True
            $score_aiden -= 2
            show ygoro_camp at p8_6
            show ygoro rage1 at p8_6
            show ydarius_undie2 at p8_7
            show ydarius shock1 at p8_7
            show ylloyd_undie2 at p8_8
            show ylloyd panic1 at p8_8
            show yyoshi_naked2 at p8_5
            show yyoshi awkward4 at p8_5
            with move

            hide yyoshi_naked2
            hide yyoshi awkward4
            show yyoshi_naked2 at p8_5
            show yyoshi awkward4 at p8_5
            voice audio.yyoshi_v_awkward1
            yo "A-Aiden was so hot, I needed to help him…!"

            show ygoro annoy3 at p8_6
            voice audio.ygoro_v_doubt2a1
            g "You’re telling me, you two snuck up here to—"
        "We got lost.":
            $working = True
            $score_aiden -= 1
            show ygoro_camp at p8_6
            show ygoro rage1 at p8_6
            show ydarius_undie2 at p8_7
            show ydarius shock1 at p8_7
            show ylloyd_undie2 at p8_8
            show ylloyd panic1 at p8_8
            show yyoshi_naked2 at p8_5
            show yyoshi awkward4 at p8_5
            with move

            hide yyoshi_naked2
            hide yyoshi awkward4
            show yyoshi_naked2 at p8_5
            show yyoshi awkward4 at p8_5
            voice audio.yyoshi_v_well1
            yo "W-Well, we kinda got lost…"

            show ygoro annoy3 at p8_6
            voice audio.ygoro_v_unsure1b1
            g "Apparently you lost your clothes too?"
        "It's not Aiden's fault.":
            $working = True
            $score_aiden += 1
            show ygoro_camp at p8_6
            show ygoro rage1 at p8_6
            show ydarius_undie2 at p8_7
            show ydarius shock1 at p8_7
            show ylloyd_undie2 at p8_8
            show ylloyd panic1 at p8_8
            show yyoshi_naked2 at p8_5
            show yyoshi awkward4 at p8_5
            with move

            hide yyoshi_naked2
            hide yyoshi awkward4
            show yyoshi_naked2 at p8_5
            show yyoshi awkward4 at p8_5
            voice audio.yyoshi_v_sad1
            yo "I-It’s not Aiden’s fault, sir!"

            show ygoro annoy3 at p8_6
            voice audio.ygoro_v_doubt2a1
            g "Don’t tell me you’re the one who’s responsible for this?"
        "It was my idea.":
            $working = True
            $score_aiden += 2
            show ygoro_camp at p8_6
            show ygoro rage1 at p8_6
            show ydarius_undie2 at p8_7
            show ydarius shock1 at p8_7
            show ylloyd_undie2 at p8_8
            show ylloyd panic1 at p8_8
            show yyoshi_naked2 at p8_5
            show yyoshi awkward4 at p8_5
            with move

            hide yyoshi_naked2
            hide yyoshi awkward4
            show yyoshi_naked2 at p8_5
            show yyoshi awkward4 at p8_5
            voice audio.yyoshi_v_sad1
            yo "I-It was my idea, sir! "

            show ygoro annoy3 at p8_6
            voice audio.ygoro_v_question1a2
            g "Seriously?! What’s gotten into you, Yoshinori?!"

    show yyuri fangirl1 at p8_2
    voice audio.yyuri_v_kyaa1
    yu "KYAAAAA!!! Yoshi’s naked too?!"

    show yyoshi scared1 at p8_5
    voice audio.yyoshi_v_shock2a
    yo "W-WAH!"

    show yemilia angry5 at p8_1
    voice audio.yemilia_v_scoff1b
    e "How scandalous… I’m not taking any part in this."

    hide yemilia_camp
    hide yemilia angry5
    with dissolve

    show ygoro sigh1 at p8_6
    voice audio.ygoro_v_sigh2a
    g "*sigh* It’s too late, everyone’s already splashing about…"
    g "Let’s just watch over them and make sure everyone stays safe."

    show yyuri drool1 at p8_2
    voice audio.yyuri_v_fujo5b
    yu "It’s time to take some pictures!!! "

    play sound sfx_camerashot
    show ygoro comic1 at p8_6
    voice audio.ygoro_v_yuri8
    g "Y-YURI!! STOP THAT!!" with flash

    show ygoro_camp at p8_4
    show ygoro comic1 at p8_4
    show ydarius_undie2 at p8_5
    show ydarius shock1 at p8_5
    show ylloyd_undie2 at p8_6
    show ylloyd panic1 at p8_6
    show yyoshi_naked2 at p8_7
    show yyoshi panic4 at p8_7
    show yaiden_naked2 at p8_8
    show yaiden panic4 at p8_8
    with move

    voice audio.yyoshi_v_aiden6
    yo "GAH! Aiden, let’s get back in the water! We can’t let her—"

    hide yyoshi_naked2
    hide yyoshi panic4
    hide yaiden_naked2
    hide yaiden panic4
    with moveoutright

    play sound sfx_camerashot
    show yyuri fangirl2 at p8_2
    voice audio.yyuri_v_fujo6a
    yu "GEHEHEHEHEHE!!" with flash

    show andre angry2 at p8_3
    voice audio.andre_v_aiden4a
    u "A-Aiden, get back here…!!"

    hide andre_camp
    hide andre
    with moveoutright

    show ygoro sigh1 at p8_4
    voice audio.ygoro_v_sigh2a
    g "*sigh* This is gonna be a long day…"

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

    $ location = location_hotelroom
    $ day = "79"
    $ time = timeline_timeday
    $ season = season_winter
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_hotel_room1_day with fade
    play music go_with_the_flow_slow loop

    show yoshi2_sleep at left2
    show yoshi2 sigh4 at left2
    show aiden_undie at right2
    show aiden tease2 at right2
    voice audio.yoshi_v_sigh3a
    yo "And ever since then, you’ve always stripped to cool down, even at camp…"

    show aiden laugh1 at right2
    voice audio.aiden_v_laugh1b2
    a "Hehe, what can I say? You liked it, so I leaned into it!"
    a "Besides, I don’t think it ever got us in any serious trouble!"

    show yoshi2 sleepy2 at left2
    voice audio.yoshi_v_well1
    yo "Well, you did manage to flash an entire club last night, you know… "

    show aiden tease1 at right2
    voice audio.aiden_v_psh1a
    a "Psh, there were already strippers in there! Everyone was already expecting to see some dick, I just added an extra one!"

    show yoshi2 annoy3 at left2
    voice audio.yoshi_v_but3
    yo "At Camp Buddy we let it slide, but not here in the city! What if someone had recorded you?"

    show aiden excited1 at right2
    voice audio.aiden_v_laugh2a1
    a "Then I’ll be a star!"

    show yoshi2 angry5 at left2
    voice audio.yoshi_v_huh1
    yo "You’re really not bothered by it at all, huh?"

    show aiden relief2 at right2
    voice audio.aiden_v_hey1a3
    a "Hey, if you got the goods, why not show ‘em off? "

    $working = False
    $shuffle_menu()
    menu():
        a "Hey, if you got the goods, why not show ‘em off? {fast}"
        "I guess...":
            $working = True
            $score_bot += 1
            show yoshi2 sigh4 at left2
            voice audio.yoshi_v_unsure3c
            yo "I guess that makes sense…"
        "That makes sense.":
            $working = True
            $score_top += 1
            show yoshi2 sigh4 at left2
            voice audio.yoshi_v_unsure3c
            yo "I guess that makes sense…"
        "You're so confident.":
            $working = True
            $score_aiden += 1
            $score_bot +=1
            hide yoshi2_sleep
            hide yoshi2 angry5
            show yoshi_sleep at left2
            show yoshi comp6 at left2
            voice audio.yoshi_v_huh1
            yo "You really are confident, aren’t you?"

            show aiden bold2 at right2
            voice audio.aiden_v_well1b2
            a "Well, I worked hard to look like this, after all! Hahaha!"
        "I'd rather not share.":
            $working = True
            $score_aiden += 1
            $score_top += 1
            hide yoshi2_sleep
            hide yoshi2 angry5
            show yoshi_sleep at left2
            show yoshi annoy2 at left2
            voice audio.yoshi_v_well1
            yo "I’d rather not share you with strangers."

            show aiden play3 at right2
            voice audio.aiden_v_oho2a
            a "Ohoho~ I like a clingy Yoshi!"

    show aiden happy1 at right2
    voice audio.aiden_v_anyway1a
    a "Anyway, that’s enough worrying about me! Why don’t we go check out some more stuff around the hotel?"

    hide yoshi2_sleep
    hide yoshi2 sigh4
    show yoshi_sleep at left2
    show yoshi worry2 at left2
    voice audio.yoshi_v_unsure2a
    yo "Are you sure? You’re still hungover…"

    show aiden bold5 at right2
    voice audio.aiden_v_no2a1
    a "Nah, the soup and the meds fixed me right up!"
    a "Besides, we’re going back to camp tomorrow, right? You don’t wanna spend our last day stuck in our room, do you?"

    show yoshi comp2 at left2
    voice audio.yoshi_v_well1
    yo "Well, as long as you’re okay!"

    show aiden bold2 at right2
    voice audio.aiden_v_agree1b1
    a "Yup! "

    $day4_aiden_choice = False
    $mm_talking = True
    $renpy.choice_for_skipping()
    show screen minimap()
    voice audio.aiden_v_so2
    a "So, what do we wanna check out this time? "

    voice audio.yoshi_v_think1a
    yo "Let’s see…"

    $mm_talking = False
    $quick_menu = False
    $ say_box = False
    $ renpy.pause (hard=True)

label day4_aiden_lobby:
    $sq_yuri += 1
    $quick_menu = True
    $a4_lobby = True
    $mm_talking = True
    $say_box = True
    if a3_lobby == False:
        voice audio.yoshi_v_think4
        yo "How about we check out the lobby?"

        voice audio.aiden_v_unsure1b
        a "I guess that’ll kill some time. Sure, why not!  "
    else:
        voice audio.yoshi_v_think4
        yo "How about we check out the lobby again?"

        voice audio.aiden_v_yoshi4a
        a "You know there’s nothing to see there, Yoshi…"

        voice audio.yoshi_v_well1
        yo "Well, maybe this time it’ll be different!"

        voice audio.aiden_v_sigh1a
        a "*sigh* Alright."

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

    if day4_aiden_choice == False:
        $ location = location_hotellobby
        show screen location
        show screen timeline
        show screen quick_menu
        $quick_menu = True
        scene bg_hotel_lobby_day with fade
        play music here_they_come loop
    else:
        $ location = location_hotellobby
        show screen location
        show screen timeline
        show screen quick_menu
        $quick_menu = True
        scene bg_hotel_lobby_sunset with fade
        play music here_they_come loop

    show aiden_autumn at p6_1
    show aiden norm1 at p6_1
    show yoshi_autumn at p6_2
    show yoshi norm1 at p6_2
    show yuri_autumn at p6_5
    show yuri norm1 at p6_5
    show jin_autumn at p6_6
    show jin_glasses at p6_6
    show jin norm1 at p6_6

    if a4_room == True:
        show aiden talk2 at p6_1
        voice audio.aiden_v_oh1a
        a "Oh, isn’t that Jin over there?"

        show yoshi talk2 at p6_2
        voice audio.yoshi_v_rush6
        yo "Looks like Yuri’s with him too. Let’s go see what they’re up to!"

        show aiden_autumn at p4_1
        show aiden norm1 at p4_1
        show yoshi_autumn at p4_2
        show yoshi happy1 at p4_2
        show yuri_autumn at p4_3
        show yuri norm1 at p4_3
        show jin_autumn at p4_4
        show jin_glasses at p4_4
        show jin norm1 at p4_4
        with move

        voice audio.yoshi_v_hey1
        yo "Hey there, you two! "

        show yuri happy1 at p4_3
        voice audio.yuri_v_oh1b
        yu "Oh! Yoshi, Aiden! "

        show aiden play2 at p4_1
        voice audio.aiden_v_laugh1b2
        a "Hehe, looks like you finally decided to get out of your room and hang around, huh Jin?"

        show jin laugh3 at p4_4
        voice audio.jin_v_laugh3a
        j "A-Ahehe… Actually, Yuri knocked on my room and dragged me out here…"

        show yoshi talk1 at p4_2
        voice audio.yoshi_v_so1a
        yo "So, what are you both up to?"
    else:
        show aiden talk2 at p6_1
        voice audio.aiden_v_oh1a
        a "Oh, isn’t that Jin over there?"

        show yoshi talk2 at p6_2
        voice audio.yoshi_v_rush6
        yo "Looks like Yuri’s with him too. Let’s see what they’re up to!"

        show aiden_autumn at p4_1
        show aiden happy1 at p4_1
        show yoshi_autumn at p4_2
        show yoshi talk2 at p4_2
        show yuri_autumn at p4_3
        show yuri norm1 at p4_3
        show jin_autumn at p4_4
        show jin_glasses at p4_4
        show jin norm1 at p4_4
        with move

        voice audio.aiden_v_hey2a2
        a "Hey there, you two! Whatcha doin’?"

        show yuri happy1 at p4_3
        voice audio.yuri_v_oh1b
        yu "Oh! Yoshi, Aiden! "

    show yuri relief2 at p4_3
    voice audio.yuri_v_well1a
    yu "We wanted to find a nice place to chill, and the seats here are super comfy! Plus, check out the ambience!"

    show jin think5 at p4_4
    voice audio.jin_v_conj1c3
    j "The Wi-Fi signal’s the strongest here, too…"

    show yoshi annoy3 at p4_2
    voice audio.yoshi_v_unsure3a
    yo "Let me guess, you two are watching BL on that laptop, aren’t you? Don’t you think that’s something you should be doing in private…?"

    show yuri angry3 at p4_3
    voice audio.yuri_v_yoshi9a
    yu "Come on, Yoshi! Just because Jin and I are avid fans of the genre doesn’t mean that’s all we think about!"

    show aiden tease1 at p4_1
    voice audio.aiden_v_think1a1
    a "Somehow I doubt that…"

    show yoshi confused2 at p4_2
    voice audio.yoshi_v_well1
    yo "What are you doing then?"

    show yuri think4 at p4_3
    voice audio.yuri_v_well2c
    yu "Well… It’s kinda confidential…"

    show aiden bold5 at p4_1
    voice audio.aiden_v_agree1a2
    a "Yup, she’s watching porn, alright."

    show yuri angry3 at p4_3
    voice audio.yuri_v_hey3d
    yu "Hey! We’re really not!"

    show yoshi annoy4 at p4_2
    voice audio.yoshi_v_think1a
    yo "Why are you acting so suspicious, then? You two are up to something, aren’t you?"

    show jin awkward3 at p4_4
    voice audio.jin_v_conj2c1
    j "W-Well… We were actually looking up Ms. Emilia’s profile online…"

    show yoshi confused3 at p4_2
    voice audio.yoshi_v_emilia5
    yo "Emilia…?"

    show yuri rage1 at p4_3
    voice audio.yuri_v_jin8a
    yu "J-Jin! That was supposed to be our secret!"

    show jin shock2 at p4_4
    voice audio.jin_v_sorry1b1
    j "A-Ah! I-I’m sorry! Is it too late to say we’re watching BL?"

    show yuri sigh3 at p4_3
    voice audio.yuri_v_sigh2a
    yu "*sigh* I guess we’ve been caught red-handed, then…"

    show aiden confused2 at p4_1
    voice audio.aiden_v_wait2b2
    a "Hold on, Yuri. Aren’t you the one who dislikes her the most? Why are you looking her up???"

    show aiden panic3 at p4_1
    voice audio.aiden_v_shock4a
    a "*gasp* Don’t tell me you’re secretly into her?!"

    show yuri rage4 at p4_3
    voice audio.yuri_v_what5a
    yu "WHAAAAAAT?! NO WAY, AIDEN! TOTALLY THE OPPOSITE!"

    show yoshi angry5 at p4_2
    voice audio.yoshi_v_tsk1a
    yo "*tsk* *tsk* You know you shouldn’t be sticking your nose into other people’s business, Yuri."

    show jin talk3 at p4_4
    voice audio.jin_v_comp2b1
    j "D-Don’t worry… It’s actually her public profile we’re looking at… So, we’re not invading her privacy at all…"

    show yuri angry3 at p4_3
    voice audio.yuri_v_yeah1a2
    yu "Yeah, what Jin said! This is why we didn’t want to show you, ’cause I knew you’d jump to conclusions!"

    hide aiden_autumn
    hide aiden panic3
    show aiden2_autumn at p4_1
    show aiden2 confused6 at p4_1
    voice audio.aiden_v_but1a1
    a "But why though?"

    show yuri angry6 at p4_3
    voice audio.yuri_v_conj3a
    yu "Like I’ve been telling you guys, I’ve had a really bad feeling about her from the start!"
    yu "It’s like the old saying, ‘know your enemy!’ "

    hide yoshi_autumn
    hide yoshi angry5
    show yoshi2_autumn at p4_2
    show yoshi2 sigh4 at p4_2
    voice audio.yoshi_v_sigh3a
    yo "*sigh* Yuri… Emilia’s not our enemy, she’s our co-worker."

    show yuri rage3 at p4_3
    voice audio.yuri_v_sigh2a
    yu "I’m only trying to see if she’s been trash-talking any of us online! Just to make sure she’s really on our side!"

    show yoshi2 annoy3 at p4_2
    voice audio.yoshi_v_so1a
    yo "So, you decided to stalk her…?"

    show yuri angry2 at p4_3
    voice audio.yuri_v_rush1d1
    yu "Come on, Yoshi! Don’t look at it that way! Looking up people online is super normal, you know!"

    hide yoshi2_autumn
    hide yoshi2 annoy3
    show yoshi_autumn at p4_2
    show yoshi angry2 at p4_2
    voice audio.yoshi_v_but1
    yo "But you’re doing it to find something she did wrong… And you’re dragging Jin into this too…"

    show yuri pout1 at p4_3
    voice audio.yyuri_v_hmph1a
    yu "Hmph! You don’t get it, Yoshi! She’s bossy and mean at work, and she has the nerve to throw shade at me every chance she gets!"
    yu "When I ran into her yesterday, she tried to call me cheap and tacky!"

    show yoshi shock2 at p4_2
    voice audio.yoshi_v_really1
    yo "She said that to you…?"

    show yuri angry6 at p4_3
    voice audio.yuri_v_ugh2a
    yu "She might as well have, saying that my taste in fashion hasn’t changed after all these years!"
    yu "Just because I don’t wear designer brands like her doesn’t make that true, you know?!"

    show yuri annoy5 at p4_3
    voice audio.yuri_v_annoyed1a
    yu "Like I get it! You’re rich! Stop shoving it in my face!"

    show yoshi explain2 at p4_2
    voice audio.yoshi_v_yuri4
    yo "You know that’s how she’s always been, Yuri… Who knows? Maybe she’s just trying to start a conversation with you."

    show yuri irked2 at p4_3
    voice audio.yuri_v_annoyed4a
    yu "If ‘starting a conversation’ means being a rude and condescending bitch, then no thanks!"
    yu "Not knowing how to socialize doesn’t give her a pass to be a bitch!"

    show aiden2 sigh5 at p4_1
    voice audio.aiden_v_sheesh1a
    a "Sheesh, Yuri… Even after all these years, you still hate her this much?"

    show yuri pout4 at p4_3
    voice audio.yyuri_v_hmph1a
    yu "Hmph! Why shouldn’t I? She and I never got along in the first place!"

    show jin think4 at p4_4
    voice audio.jin_v_think2a1
    j "I’m really curious as to why… Maybe you two just got off on the wrong foot?"

    show yuri serious2 at p4_3
    voice audio.yuri_v_jin2c
    yu "Don’t get me wrong, Jin. I tried to be friends with her, and I gave her lots of chances back then!"
    yu "But it never worked because we were never on the same wavelength!"

    show yuri annoy2 at p4_3
    voice audio.yuri_v_annoyed2a
    yu "She used to act as if I was her rival or something when I was just minding my own business!"
    yu "We even fought when no one could see us…"

    show jin shock2 at p4_4
    voice audio.jin_v_whoa3a
    j "Whoa… like an actual physical fight?"

    hide yoshi_autumn
    hide yoshi explain2
    show yoshi2_autumn at p4_2
    show yoshi2 sigh4 at p4_2
    voice audio.yoshi_v_sigh3a
    yo "*sigh* I remember that… One time it got really bad and they got caught by Sir Goro…"

    show yuri rage2 at p4_3
    voice audio.yuri_v_ugh2a
    yu "And it was about something so pointless, too! Ugh, I’ll never forget that one either…"

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

    $ location = location_campsite
    $ day = "??"
    $ time = timeline_timeday
    $ season = season_summer
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_campgrounds_past_day with fade
    play music heracleum_a loop

    show yemilia_camp at left3
    show yemilia angry1 at left3
    show yyuri_camp at right3
    show yyuri rage1 at right3
    voice audio.yyuri_v_emilia8a
    yu "Give it back, Emilia! That’s not yours!"

    show yemilia angry2 at left3
    voice audio.yemilia_v_angry6
    e "Gadgets aren’t allowed at camp! How come that rule doesn’t apply to you?!"

    show yemilia angry5 at left3
    voice audio.yemilia_v_sarcastic2a
    e "Oh, I KNOW! It’s because you’re the owner’s daughter! Talk about rampant nepotism! This camp is absolutely ridiculous!!!"

    show yyuri angry3 at right3
    voice audio.yyuri_v_what5a
    yu "What does that have to do with my camera, Emilia?! I’m not doing any harm, and it’s not distracting anyone! "

    show yemilia rage6 at left3
    voice audio.yemilia_v_angry6
    e "It’s not just about this stupid camera! You get away with EVERYTHING!"
    e "You get to skip activities whenever you want, bring your books on camping trips, and they even let you stay with everyone in the boys’ cabins!!"

    show yemilia rage5 at left3
    voice audio.yemilia_v_sarcastic4b
    e "If you can get your demands fulfilled on a whim, then why can’t I as well?!"
    e "I don’t want this ugly uniform, I want my own designer wardrobe! "

    show yemilia rage4 at left3
    voice audio.yemilia_v_angry7a
    e "I’m sick and tired of being fed commoner’s grub every meal! I want my personal chef!"
    e "And last but not the least, I don’t want to share a room with girls who keep gossiping about me just because they’re jealous! "

    show yemilia rage6 at left3
    voice audio.yemilia_v_angry8
    e "Is that too much to ask?!" with vpunch

    show yyuri angry3 at right3
    voice audio.yyuri_v_angry3a
    yu "You’re being such a SPOILED BRAT! Just give me my camera back!!"

    show yemilia angry3 at left3
    voice audio.yemilia_v_dismiss1
    e "Not until you tell your dad to give me everything I just said!"

    show yyuri rage3 at right3
    voice audio.yyuri_v_no1c1
    yu "Go ask him yourself! I’m not your servant!"

    show yemilia annoy2 at left3
    voice audio.yemilia_v_disagree1
    e "It’s not my fault that you look like one!"

    show yyuri rage1 at right3
    voice audio.yyuri_v_emilia10b
    yu "I can’t stand you! You’re so whiney and entitled! Why are you even at this camp?!"
    yu "Shouldn’t pompous, rich snobs like you be rotting in your mansion all alone?!"

    show yyuri bleh3 at right3
    voice audio.yyuri_v_hmph2a
    yu "Your parents probably don’t even have the time for you, that’s why you have such a nasty attitude!"

    show yemilia rage4 at left3
    voice audio.yemilia_v_angry5a
    e "Sh-Shut up! My parents love me! They buy me EVERYTHING I ask for!"

    show yyuri rage4 at right3
    voice audio.yyuri_v_angry6a
    yu "Apparently, they forgot to buy you a GOOD PERSONALITY, too!"
    yu "Just accept the fact that you’re stuck here because they don’t wanna deal with a spoiled brat like you!"

    show yemilia panic3 at left3
    voice audio.yemilia_v_i1
    e "I—"

    show yyuri angry6 at right3
    voice audio.yyuri_v_annoyed2c
    yu "They threw you away, crossing their fingers that you’d change, and learn how to get along with other people."

    voice audio.yyuri_v_emilia12a
    yu "But too bad nobody wants to be friends with you because you’re such a BITCH!!!"

    show yemilia rage6 at left3
    voice audio.yemilia_v_what3b
    e "I’m a WHAT?! Take that back!!!"

    show yyuri rage4 at right3
    voice audio.yyuri_v_angry6a
    yu "Did I stutter? I said, You’re. A. BITCH."

    show yemilia rage4 at left3
    voice audio.yemilia_v_angry2a
    e "EURGH! How dare you?!"

    play sound sfx_cameracrash
    e "*throws Yuri’s camera on the ground*" with vpunch

    show yyuri panic3 at right3
    voice audio.yyuri_v_shock2a
    yu "M-My camera…!!"

    play sound sfx_cameracrash
    e "*tramples the camera*" with vpunch

    show yemilia rage5 at left3
    voice audio.yemilia_v_rage1a
    e "Nobody calls me a bitch!!! Take that!!" with vpunch

    show yyuri scared2 at right3
    voice audio.yyuri_v_angry5a
    yu "Stop!! You’re breaking it!!!" with vpunch

    show yemilia tease2 at left3
    voice audio.yemilia_v_laugh4
    e "Just ask daddy for a new one~! Oh wait, you’re too poor to afford another!"

    show yyuri rage4 at right3
    voice audio.yyuri_v_angry3a
    yu "GRRR!!!"

    show yyuri_camp at center
    show yyuri rage4 at center
    with move

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    play music heracleum_b loop
    show cg fade at truecenter
    show fxsq_catfight at fx_pos
    with dissolve

    voice audio.yyuri_vsa9_line1
    yu "Do you have any idea how much that camera means to me?! My dad gave it to me for my birthday!!!"

    voice audio.yemilia_vsa9_line1
    e "Owww!! You’re ruining my hair!!! I spent all morning styling this!!"

    voice audio.yyuri_vsa9_line2
    yu "No one cares about your freaking hair! You ugly, conceited-ass bitch!!"

    voice audio.yemilia_vsa9_line2
    e "I told you, stop calling me a bitch!!! "

    voice audio.yyuri_vsa9_line3
    yu "That’s what you are! "
    all "Fight! Fight! Fight!"

    hide cg fade
    hide fxsq_catfight
    with dissolve

    show yemilia_camp at p5_4
    show yemilia angry1 at p5_4
    show yyuri_camp at p5_5
    show yyuri rage4 at p5_5
    with move

    show ygoro_camp at p5_1
    show ygoro angry4 at p5_1
    show yyoshi_camp at p5_2
    show yyoshi panic1 at p5_2
    with dissolve

    voice audio.ygoro_v_worry1b
    g "Wh-What’s going on here?! "

    show yemilia_camp at p5_3
    show yemilia angry1 at p5_3
    show ygoro_camp at p5_4
    show ygoro rage1 at p5_4
    with move

    hide yemilia_camp
    hide yemilia angry1
    show yemilia_camp at p5_3
    show yemilia angry1 at p5_3
    voice audio.ygoro_v_yuri8
    g "YURI! "

    show yyoshi_camp at p5_2
    show yyoshi angry2 at p5_2
    voice audio.yyoshi_v_stop1
    yo "Yuri, that’s enough! Let her go!"

    show yemilia_camp at p4_1
    show yemilia cry1 at p4_1
    show yyoshi_camp at p4_2
    show yyoshi angry2 at p4_2
    show yyuri_camp at p4_3
    show yyuri rage4 at p4_3
    show ygoro_camp at p4_4
    show ygoro rage1 at p4_4
    with move

    voice audio.yemilia_v_sob1
    e "*sobs* Look what she did to my hair! Thanks for saving me from this bully, Yoshi! "
    e "She… just… attacked me out of nowhere! "

    show yyuri rage1 at p4_3
    voice audio.yyuri_v_what5a
    yu "What?! Nowhere?! You threw my camera on the ground, you lying bitch!!"

    show ygoro rage3 at p4_4
    voice audio.ygoro_v_yuri9
    g "Yuri! Language! " with vpunch

    show yyuri angry3 at p4_3
    voice audio.yyuri_v_but3a
    yu "I’m telling the truth! She really—"

    show yemilia cry2 at p4_1
    voice audio.yemilia_v_no2
    e "She’s the one who pulled my hair first! I was just defending myself!"

    show ygoro angry3 at p4_4
    voice audio.ygoro_v_insult1a
    g "Yuri! You should know that violence is never the answer!!"

    show yyuri rage4 at p4_3
    voice audio.yyuri_v_goro9c
    yu "B-But, Dad!!"

    show yemilia angry3 at p4_1
    voice audio.yemilia_v_bossy6
    e "She should be punished for this! You can’t let this slide just because she’s your daughter!!"

    show ygoro disappoint3 at p4_4
    voice audio.ygoro_v_scold2b1
    g "Time out, you two!!"

    show ygoro angry3 at p4_4
    voice audio.ygoro_v_yuri8
    g "Yuri, in my office!"

    show yyuri worry5 at p4_3
    voice audio.yyuri_v_i2a
    yu "I—"

    show ygoro rage3 at p4_4
    voice audio.ygoro_v_rush4
    g "NOW!" with vpunch

    show yyuri rage3 at p4_3
    voice audio.yyuri_v_ugh2a
    yu "UGH!!!"

    hide yyuri_camp
    hide yyuri rage3
    with dissolve

    show ygoro angry2 at p4_4
    voice audio.ygoro_v_emilia10
    g "Ms. Komarova, we’ll discuss this matter later. Yoshinori, please take her to the infirmary and check for any injuries."

    show yemilia tease1 at p4_1
    show yyoshi awkward4 at p4_2
    voice audio.yyoshi_v_yessir3a
    yo "Y-Yes, sir…!"

    show ygoro angry4 at p4_4
    voice audio.ygoro_v_scold2a1
    g "As for the rest of you! Go back to your cabins! There’s nothing to see here!"

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

    if day4_aiden_choice == False:
        $ day = "79"
        $ time = timeline_timeday
        $ season = season_winter
        $ location = location_hotellobby
        show screen location
        show screen timeline
        show screen quick_menu
        $quick_menu = True
        scene bg_hotel_lobby_day with fade
    else:
        $ day = "79"
        $ time = timeline_timesunset
        $ season = season_winter
        $ location = location_hotellobby
        show screen location
        show screen timeline
        show screen quick_menu
        $quick_menu = True
        scene bg_hotel_lobby_sunset with fade
    play music here_they_come loop

    show aiden_autumn at p4_1
    show aiden worry1 at p4_1
    show yoshi_autumn at p4_2
    show yoshi norm3 at p4_2
    show yuri_autumn at p4_3
    show yuri annoy1 at p4_3
    show jin_autumn at p4_4
    show jin_glasses at p4_4
    show jin scared1 at p4_4
    voice audio.jin_v_relief1a1
    j "Whew… That sounds… really intense…"

    hide aiden_autumn
    hide aiden worry1
    show aiden2_autumn at p4_1
    show aiden2 comp6 at p4_1
    voice audio.aiden_v_laugh1b1
    a "Ahehe, kinda feel like I missed out on that show… "

    show yuri bold1 at p4_3
    voice audio.yuri_v_laugh1a1
    yu "I’m a lot stronger than I look~ She never tried to get anywhere near me after that incident."

    hide yoshi_autumn
    hide yoshi norm3
    show yoshi2_autumn at p4_2
    show yoshi2 sigh4 at p4_2
    voice audio.yoshi_v_sigh3a
    yo "*sigh* I know it’s hard to believe but Yuri was quite the troublemaker back then."

    show yuri pout1 at p4_3
    voice audio.yuri_v_hey3c
    yu "Heeeeeyyy! Don’t just slander me like that in front of Jin!"

    show jin shock5 at p4_4
    voice audio.jin_v_shock1a
    j "Oh wow… I was sure you were a model scout like Yoshi…"

    show yuri bold2 at p4_3
    voice audio.yuri_v_annoyed3a
    yu "Not when someone like Emilia tests me! That time should’ve taught her a lesson not to mess with my stuff!"

    hide aiden2_autumn
    hide aiden2 comp6
    show aiden_autumn at p4_1
    show aiden tease1 at p4_1
    voice audio.aiden_v_so2
    a "So, when’s the rematch? She’s been getting on your nerves again, so…"

    show yoshi2 annoy2 at p4_2
    voice audio.yoshi_v_aiden4
    yo "Aiden… Don’t encourage her… "

    show yuri pout4 at p4_3
    voice audio.yyuri_v_hmph1a
    yu "Hmph! We’re already professionals, I’m not going to be childish and spiteful like her!"

    show jin talk2 at p4_4
    voice audio.jin_v_oh2a
    j "Oh! I just found her Instaglam!"

    show yuri shock4 at p4_3
    voice audio.yyuri_v_shock2a
    yu "WHERE?! Lemme see!"

    show yuri_autumn at p5_4
    show yuri shock4 at p5_4
    with move

    show aiden sigh1 at p4_1
    voice audio.aiden_v_sheesh1a
    a "So much for being professionals…"

    show yuri rage1 at p5_4
    voice audio.yuri_v_ugh2a
    yu "Ugh! Elitist as always! Posting pictures of designer stuff and random things in the hotel!"

    show jin thinkdn2 at p4_4
    voice audio.jin_v_think1a1
    j "It looks like she hasn’t posted anything before this too. Let me see if she linked her Fakebook and Twatter here too… "

    show yuri bold2 at p5_4
    voice audio.yuri_v_yeah1b1
    yu "Haha, yeah! Do that!"

    show yoshi2 sigh4 at p4_2
    voice audio.yoshi_v_sigh3a
    yo "*sigh* Maybe it’s best to leave them to their business."

    show aiden talk3 at p4_1
    voice audio.aiden_v_yeah1b2
    a "Yeah, they look like they’re having harmless fun, anyways."

    hide yoshi2_autumn
    hide yoshi2 sigh4
    show yoshi_autumn at p4_2
    show yoshi talk1 at p4_2
    voice audio.yoshi_v_alright1
    yo "Alright, let’s go somewhere else!"

    if day4_aiden_choice == False:
        $ day4_aiden_choice = True
        $ renpy.music.stop(channel='music', fadeout = 1.0)
        $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
        $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
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
        $ renpy.music.stop(channel='music', fadeout = 1.0)
        $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
        $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
        scene cg black with fade

        yo "{i}Eventually, we decided to head back to our room for the night.{/i}"

        scene cg black
        hide screen location
        hide screen timeline
        hide screen quick_menu
        $quick_menu = False
        with fade
        $ time_transition_sunset_to_night_winter()
        $ renpy.pause (2.0, hard=True)
        jump day4_aiden_after

label day4_aiden_club:
    $sq_goro += 1
    $quick_menu = True
    $say_box = True
    $mm_talking = True
    $a4_club = True
    voice audio.yoshi_v_think4
    yo "Wanna go check out the club again? I’m curious what’s there during the day."

    voice audio.aiden_v_shock1e2
    a "Whoa, whoa, whoa, you’re not planning to get me drunk again, are you?"

    voice audio.yoshi_v_comp6
    yo "Haha, don’t worry! We’ll just go there to chill this time."

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

    if day4_aiden_choice == False:
        $ location = location_hotelclub
        show screen location
        show screen timeline
        show screen quick_menu
        $quick_menu = True
        scene bg_hotel_bar_day with fade
        play music old_familiar_home loop
    else:
        $ location = location_hotelclub
        show screen location
        show screen timeline
        show screen quick_menu
        $quick_menu = True
        scene bg_hotel_bar_sunset with fade
        play music old_familiar_home loop

    show goro_autumn at left
    show goro happy3 at left
    show yoshi_autumn at center
    show yoshi norm1 at center
    show aiden_autumn at right
    show aiden norm1 at right
    voice audio.goro_v_ah2a
    g "Ah! I thought you two might end up here at some point today."
    g "Here, come sit with me."

    show aiden play2 at right
    voice audio.aiden_v_laugh1b2
    a "Hehe, doin’ some good ol’ day drinking, Gramps?"

    show goro laugh2 at left
    voice audio.goro_v_laugh2a
    g "Haha! I thought it might be a nice way to warm me up. The weather’s gotten much colder over the last few days.  "
    g "Besides, I was so relaxed at the spa that I lost track of time and then ended up spending the whole day there yesterday."

    show yoshi happy1 at center
    voice audio.yoshi_v_actually1a
    yo "We actually checked this place out last night… It was much livelier then!"
    yo "There were a lot more people, loud music, and... uh… entertainers."

    show goro happy2 at left
    voice audio.goro_v_isee1a
    g "That makes sense. High-end bars like these tend to have nightlife activities."
    g "I personally prefer a cozier and calmer ambience when I’m having my drinks."

    show aiden happy1 at right
    voice audio.aiden_v_yeah1a1
    a "Yeah, I can barely recognize this place compared to how crazy it was here last night!"
    a "I gotta say, I had tons of fun with that whole ‘clubbing’ thing last night! I could get used to it! "

    hide yoshi_autumn
    hide yoshi norm1
    show yoshi2_autumn at center
    show yoshi2 comp3 at center
    voice audio.yoshi_v_yeah1
    yo "Yeah, you did. A lot more than you were supposed to…"

    show goro play2 at left
    voice audio.goro_v_well1a
    g "Well, Aiden does strike me as someone who’d enjoy a place like this. Maybe not as much for you, Yoshinori."

    hide yoshi2_autumn
    hide yoshi2 comp3
    show yoshi_autumn at center
    show yoshi comp5 at center
    voice audio.yoshi_v_sigh3a
    yo "I was trying to moderate our drinks, but I still lost count in the end…"

    show aiden comp5 at right
    voice audio.aiden_v_relief1a1
    a "Yeah, I was super wasted! "
    a "Those cocktails really hit the spot! I can’t remember how many I had!  "

    show goro happy1 at left
    voice audio.goro_v_oh3b
    g "What did you guys have?"

    if drink == 1 or drink == 2:
        hide yoshi_autumn
        hide yoshi comp5
        show yoshi2_autumn at center
        show yoshi2 think5 at center
        voice audio.yoshi_v_think1a
        yo "I don’t actually remember… The bartender mixed something up for us, I forgot to ask what it was called."

        show aiden laugh1 at right
        voice audio.aiden_v_laugh2a1
        a "Hahaha, Yoshi and I looked like headless chickens, not knowing what to order!"

        hide yoshi2_autumn
        hide yoshi2 think5
        show yoshi_autumn at center
        show yoshi comp2 at center
        voice audio.yoshi_v_sirgoro2
        yo "You usually order stuff for us whenever we have a drink out, Sir Goro. "
        yo "But then again, we always just get beer."

        show goro tease5 at left
        voice audio.goro_v_heh1a
        g "Well, it’s a good thing the bartender here knows their job. Especially if you guys managed to get drunk, hehe."

        show aiden play3 at right
        voice audio.aiden_v_hey1e2
        a "Hey! Speak for yourself, Gramps! Look at you with all these empty glasses lying around."
    if drink == 3:
        show yoshi think2 at center
        voice audio.yoshi_v_think1a
        yo "I remember Aiden and I getting some ‘blow job’ shots."

        show aiden tease1 at right
        voice audio.aiden_v_laugh1c1
        a "Hehehe~ Spilling the beans in front of Gramps, Yoshi?"

        hide yoshi_autumn
        hide yoshi think2
        show yoshi2_autumn at center
        show yoshi2 sigh4 at center
        voice audio.yoshi_v_sigh3a
        yo "*sigh* I knew you were gonna react to that."

        show goro bold5 at left
        voice audio.goro_v_agree3a1
        g "Ah, yes, of course. Very fitting for youngsters like you."
        g "Either way, I’m glad you two had a great time last night. The bartender here’s really good at their job."

        hide yoshi2_autumn
        hide yoshi2 sigh4
        show yoshi_autumn at center
        show yoshi comp2 at center
        voice audio.yoshi_v_sir1
        yo "You do seem like you’ve been drinking for a while with all these empty glasses lying around, sir."
    if drink == 4:
        show aiden bold2 at right
        voice audio.aiden_v_oh1a
        a "Oh, I remember! Yoshi and I had ‘Sex on the Beach!’"

        hide yoshi_autumn
        hide yoshi comp2
        show yoshi2_autumn at center
        show yoshi2 shy5 at center
        voice audio.yoshi_v_ehem1b
        yo "*ehem* The way you phrased that…"

        show goro bold5 at left
        voice audio.goro_v_agree3a1
        g "Ah, yes, of course. Very fitting for youngsters like you."
        g "Either way, I’m glad you two had a great time last night. The bartender here’s really good at their job."

        hide yoshi2_autumn
        hide yoshi2 shy5
        show yoshi_autumn at center
        show yoshi comp2 at center
        voice audio.yoshi_v_sir1
        yo "You do seem like you’ve been drinking for a while with all these empty glasses lying around, sir."

    show goro happy2 at left
    voice audio.goro_v_laugh2a
    g "Well, I thought I’d take advantage of this rare opportunity and try out some options I’ve never had before."
    g "But even after all this, I still prefer a vintage scotch on the rocks."

    show aiden awkward2 at right
    voice audio.aiden_v_shock1d2
    a "Whoa, careful, Gramps. You don’t wanna get so drunk that you’ll strip down and scare everyone with your monster dong."

    hide goro_autumn
    hide goro happy2
    show goro2_autumn at left
    show goro2 play3 at left
    voice audio.goro_v_heh1a
    g "Heh! I’m not like you, kiddo. With all my experience, I have a pretty high tolerance."

    show aiden think2 at right
    voice audio.aiden_v_mmm2a1
    a "Except for that one time!"
    a "If Yoshi’s a sappy drunk, and I’m a wild drunk, then you’re a mopey drunk, Gramps!"

    show goro2 shy2 at left
    voice audio.goro_v_what1
    g "What? I don’t remember you seeing that."

    hide yoshi_autumn
    hide yoshi comp2
    show yoshi2_autumn at center
    show yoshi2 shy6 at center
    voice audio.yoshi_v_sir4
    yo "S-Sir, I think he’s talking about a different time…"

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

    $ location = location_campsite
    $ day = "??"
    $ time = timeline_timenight
    $ season = season_summer
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_campgrounds_past_night_lightsout with fade
    play music ready_for_tomorrow loop
    play bgsound sfxloop_night loop

    show yyoshi_sleep at center
    show yyoshi explain1 at center
    yo "..."

    show yyoshi_sleep at right2
    show yyoshi explain1 at right2
    with move

    show yaiden_sleep at left2
    show yaiden confused2 at left2
    with dissolve

    voice audio.yaiden_v_yoshi7a
    a "Yoshi?"

    show yyoshi talk3 at right2
    voice audio.yyoshi_v_aiden2
    yo "Hey, Aiden."

    show yaiden think2 at left2
    voice audio.yaiden_v_think1a
    a "Can’t sleep?"

    show yyoshi explain2 at right2
    voice audio.yyoshi_v_yeah3
    yo "Yeah… I’m just stretching a bit and watching the stars before bed."

    show yaiden_sleep at p5_1
    show yaiden awkward2 at p5_1
    show yyoshi_sleep at p5_2
    show yyoshi explain2 at p5_2
    with move

    show yyuri_sleep at p5_5
    show yyuri annoy1 at p5_5
    with dissolve

    voice audio.yaiden_v_oh3
    a "O-Oh hey, is that… Yuri?"

    show yyoshi confused2 at p5_2
    voice audio.yyoshi_v_huh1
    yo "Huh? What is she doing over there?"

    show yaiden_sleep at left
    show yaiden awkward2 at left
    show yyoshi_sleep at center
    show yyoshi talk3 at center
    show yyuri_sleep at right
    show yyuri annoy1 at right
    with move

    voice audio.yyoshi_v_yuri2
    yo "Hey, Yuri!"

    show yyuri shock5 at right
    voice audio.yyuri_v_shock3b
    yu "GAH!!" with vpunch

    show yyuri sigh3 at right
    voice audio.yyuri_v_guys3a
    yu "You guys startled me!"

    show yyoshi confused3 at center
    voice audio.yyoshi_v_huh1
    yo "What are you doing up so late?"

    show yyuri angry2 at right
    voice audio.yyuri_v_angry2a1
    yu "I should be asking you that! You’re the one who always makes us go to sleep on time!"

    show yyuri excited2 at right
    voice audio.yyuri_v_idea3b1
    yu "ha! You two must’ve been trying to sneak away for some midnight action, huh?!"

    show yyoshi awkward4 at center
    voice audio.yyoshi_v_no3
    yo "N-No, Yuri. Aiden just happened to catch me out here while I was getting some fresh air."

    show yyoshi angry2 at center
    voice audio.yyoshi_v_hey1
    yo "But you still didn’t answer my question! Why are you out here?"
    yo "And why do you have a bag of stuff? "

    show yaiden shock3 at left
    voice audio.yaiden_v_shock4a
    a "*gasp* Are you running away from home?!"

    show yyuri explain2 at right
    voice audio.yyuri_v_aiden2c
    yu "Don’t be silly, Aiden. It’s nothing like that! I’m just getting away from Dad for a little while."

    show yaiden confused3 at left
    voice audio.yaiden_v_confused1e
    a "Eh? Why? Did you guys have a fight?"

    show yyuri sigh3 at right
    voice audio.yyuri_v_conj2b1
    yu "N-Not really. It’s just… He’s been drinking a lot more lately and tonight he’s hit the jackpot."
    yu "I really hate seeing him whenever he’s drunk like this."

    show yyoshi worry2 at center
    voice audio.yyoshi_v_unsure2a
    yo "Is it really okay to leave him alone like that, though? Should we check on him to be sure?"

    show yyuri annoy2 at right
    voice audio.yyuri_v_ugh1a
    yu "Trust me, you don’t wanna see it. He acts like a completely different person!"
    yu "He’s all weird and cringey, nothing like what you guys see when he’s at work as our scoutmaster!"

    show yaiden bold2 at left
    voice audio.yaiden_v_excited1a
    a "Oh boy! We gotta see this, Yoshi!"

    show yyoshi shy5 at center
    voice audio.yyoshi_v_praise1
    yo "G-Good idea, Aiden! Maybe Sir Goro needs help or something…!"

    show yyuri pout1 at right
    voice audio.yyuri_v_hmph1a
    yu "Hmph, that excuse is as fake as it gets, Yoshi. You just wanna see too."

    show yyoshi comp6 at center
    voice audio.yyoshi_v_promise1
    yo "I promise, just a quick peek…!"

    show yyuri angry5 at right
    voice audio.yyuri_v_well1a
    yu "If you guys want to see him so bad, you can from the window. But don’t say I didn’t warn you!"

    show yaiden excited3 at left
    voice audio.yaiden_v_excited4a
    a "First!"

    show yyoshi_sleep at p5_2
    show yyoshi shock1 at p5_2
    show yyuri_sleep at p5_1
    show yyuri shock1 at p5_1
    show yaiden_sleep at p5_4
    show yaiden excited3 at p5_4
    with move

    show yyoshi shock2 at p5_2
    voice audio.yyoshi_v_wait3
    yo "H-Hey! Wait for me!"

    show yyoshi_sleep at p5_5
    show yyoshi shock2 at p5_5
    with move

    show yyuri_sleep at p5_3
    show yyuri sigh1 at p5_3
    with move

    voice audio.yyuri_v_sigh1a
    yu "*sigh*"

    show yaiden talk6 at p5_4
    voice audio.yaiden_v_excited5a
    a "There he is!"

    show yyuri angry2 at p5_3
    voice audio.yyuri_v_annoyed4c
    yu "Ssh! Keep it down!"

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    show yyoshi at p5_5
    voice audio.yyoshi_v_oh2
    yo "O-Oh! Sir Goro’s saying something…!"

    show cg fade at truecenter
    show fxsq_goro 1 at fx_pos
    with dissolve

    play music here_they_come loop
    voice audio.ygoro_vsa10_line1
    g "Ahhh… It’s just you and me, now…"

    voice audio.ygoro_vsa10_line2
    g "You’re the only one who listens to all my problems, you know?"

    voice audio.yaiden_vsa10_line1
    a "Is he… talking to that bottle…?"

    voice audio.yyoshi_vsa10_line1
    yo "It looks like it…"

    show fxsq_goro 2 at fx_pos with Dissolve(0.25)
    voice audio.ygoro_vsa10_line3
    g "I know I’m not the same guy I used to be, but I’m really trying my best… for us…"

    voice audio.ygoro_vsa10_line4
    g "We’ve come so far after all these years… Please don’t ever leave us…"

    voice audio.ygoro_vsa10_line5
    g "You won’t leave me right…? Right?"

    voice audio.ygoro_vsa10_line6
    g "Please answer me… The silence is deafening… Hello???"

    voice audio.yaiden_vsa10_line2
    a "Pfft…! Is this for real?!"

    #voice audio.yyoshi_vsa10_line2
    yo "A-Aiden, ssh…!!"

    show fxsq_goro 3 at fx_pos with Dissolve(0.25)
    voice audio.ygoro_vsa10_line7
    g "W-What’s that…? You’re saying yes…?"

    voice audio.ygoro_vsa10_line8
    g "I knew you’d change your mind…! Now come here and give me a kiss!"

    voice audio.ygoro_vsa10_line9
    g "*gulp* *gulp* *gulp*"

    voice audio.yyuri_vsa10_line1
    yu "Ugh… This is so embarrassing…"

    voice audio.ygoro_vsa10_line10
    g "Ahhh… I love you bottle… I love you too, couch… "

    show fxsq_goro 1 at fx_pos with Dissolve(0.25)
    voice audio.ygoro_vsa10_line11
    g "*burp*"

    show fxsq_goro 4 at fx_pos with Dissolve(0.25)
    g "..."

    voice audio.yaiden_vsa10_line3
    a "Oh crap! He just died!"

    hide cg fade
    hide fxsq_goro 4
    with dissolve

    show yyoshi panic3 at p5_5
    voice audio.yyoshi_v_shock2a
    yo "WAH! Should we call an ambulance or something?!"

    show yaiden laugh3 at p5_4
    voice audio.yaiden_v_laugh2c1
    a "HAHAHAHA!!! Calm down, Yoshi! He just passed out!"

    show yyoshi angry3 at p5_5
    voice audio.yyoshi_v_aiden6
    yo "Th-This isn’t something to laugh about, Aiden…!!"

    show yaiden laugh4 at p5_4
    voice audio.yaiden_v_laugh2c2
    a "HAHAHA! How can I not?! Did you see how he made out with that bottle?!"

    show yyoshi panic4 at p5_5
    voice audio.yyoshi_v_yuri9a
    yo "Y-Yuri, how are you so calm about this?!"

    show yyuri sigh1 at p5_3
    voice audio.yyuri_v_sigh2a
    yu "*sigh* Dad’s fine, Yoshi. It happens all the time."

    show yaiden tease2 at p5_4
    voice audio.yaiden_v_really3a
    a "Even the part when he started straddling the pillow? HAHAHA! "

    show yyuri tease2 at p5_3
    voice audio.yyuri_v_yeah1b1
    yu "Yup! There’s also that one gross time he was sobbing about giving me a little brother to fix the problems."
    yu "Can’t unsee the stuff he tried to do to my poor stuffed panda…"

    show yyoshi play5 at p5_5
    voice audio.yyoshi_v_laugh6
    yo "P-Pfftt…!!"

    show yaiden laugh3 at p5_4
    voice audio.yaiden_v_laugh2c2
    a "Oh my god! HAHAHAHA! You should’ve taken pictures!"

    show yyuri tease4 at p5_3
    voice audio.yyuri_v_laugh2a1
    yu "Hehe, I definitely have! I can show you guys tomorrow!"

    show yaiden excited3 at p5_4
    voice audio.yaiden_v_excited6a
    a "Ooh, ooh, I wanna see!"

    show yyoshi awkward4 at p5_5
    voice audio.yyoshi_v_noway1
    yo "Y-You guys can’t do that!"

    show yyuri play2 at p5_3
    voice audio.yyuri_v_rush1c1
    yu "Oh, come on, Yoshi. I know you want to see them too~"
    yu "Besides, I’m gonna show them to Dad someday to make him stop drinking!"

    show yyoshi worry5 at p5_5
    voice audio.yyoshi_v_sorry6a
    yo "Does Sir Goro drink this much usually…?"

    show yyuri angry2 at p5_3
    voice audio.yyuri_v_annoyed5a
    yu "Only when he has problems! That’s why I hate it so much!"
    yu "He never opens up to me unless he’s drunk. And when he’s this drunk, he becomes a total crybaby and can’t even hold a real conversation."

    show yyoshi worry2 at p5_5
    voice audio.yyoshi_v_but2a
    yo "But the stuff he was saying… It sounded like it’s a big deal."

    show yaiden play2 at p5_4
    voice audio.yaiden_v_yoshi1a
    a "Yoshi, he’s talking to furniture."

    show yyuri tease2 at p5_3
    voice audio.yyuri_v_laugh2a1
    yu "Don’t forget humping."

    show yaiden laugh4 at p5_4
    voice audio.yaiden_v_laugh2c1
    a "HAHAHA!"

    show yyoshi sigh1 at p5_5
    voice audio.yyoshi_v_rush4a
    yo "Come on, you two… "

    show yyuri irked2 at p5_3
    voice audio.yyuri_v_confident3a
    yu "I told you, he’s gonna be fine, Yoshi. He’ll be back to normal tomorrow morning like nothing happened."
    yu "I don’t know how, but as soon as he gears up in his camp uniform, he’s enthusiastic and happy all of a sudden."

    show yaiden tease2 at p5_4
    voice audio.yaiden_v_laugh3a
    a "Hahaha, totally the opposite of the snot-covered face we just saw!"

    show yyoshi sigh4 at p5_5
    voice audio.yyoshi_v_sigh2
    yo "*sigh* He’s still our scoutmaster, Aiden."

    show yyuri talk1 at p5_3
    voice audio.yyuri_v_anyway1a
    yu "Anyway, can I bunk with you guys for the night? Usually this goes on for hours and I can’t sleep with all the groaning and sobbing."

    show yyoshi worry2 at p5_5
    voice audio.yyoshi_v_agree2b1
    yo "It’s fine, but… Are you sure we can leave your dad like that?"

    show yyuri irked2 at p5_3
    voice audio.yyuri_v_yeah1h2
    yu "Yeah, yeah, it’s fine! How many times do I have to tell you?"
    yu "Now, I’ll go take that top bunk!"

    hide yyuri_sleep
    hide yyuri irked2
    with moveoutleft

    show yyoshi shock2 at p5_5
    voice audio.yyoshi_v_hey1
    yo "H-Hey, that’s my spot…!"

    voice audio.yyuri_v_laugh2b1
    yu "Go share a bed with Aiden! Hihihi~"

    show yyoshi sigh1 at p5_5
    voice audio.yyoshi_v_sigh2
    yo "*sigh*"

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

    if day4_aiden_choice == False:
        $ day = "79"
        $ time = timeline_timeday
        $ season = season_winter
        $ location = location_hotelclub
        show screen location
        show screen timeline
        show screen quick_menu
        $quick_menu = True
        scene bg_hotel_bar_day with fade
        play music old_familiar_home loop
    else:
        $ location = location_hotelclub
        $ day = "79"
        $ time = timeline_timenight
        $ season = season_winter
        show screen location
        show screen timeline
        show screen quick_menu
        $quick_menu = True
        scene bg_hotel_bar_sunset with fade
        play music old_familiar_home loop

    show goro2_autumn at left
    show goro2 disappoint5 at left
    show yoshi2_autumn at center
    show yoshi2 comp1 at center
    show aiden_autumn at right
    show aiden play1 at right
    voice audio.goro_v_swear1a
    g "Damn it… I can’t believe you two saw me like that…"

    show yoshi2 sigh4 at center
    voice audio.yoshi_v_aiden4
    yo "That was supposed to be a secret, Aiden…"

    show goro2 shy6 at left
    voice audio.goro_v_sigh1a
    g "Over all these years, I thought I kept up the reliable and responsible scoutmaster image, but you both witnessed such an embarrassing moment… "

    show aiden bold5 at right
    voice audio.aiden_v_agree1b1
    a "Yup, Gramps~! That’s why no matter how tough you act around us, we know you’re a softie~!"

    hide goro2_autumn
    hide goro2 shy6
    show goro_autumn at left
    show goro comic1 at left
    voice audio.goro_v_what3a
    g "S-SOFTIE?! "

    show aiden tease2 at right
    voice audio.aiden_v_laugh1b2
    a "You better take it easy with those shots, alright? Don’t want you turning into a crying mess so early in the morning!"

    hide goro_autumn
    hide goro comic1
    show goro2_autumn at left
    show goro2 play3 at left
    voice audio.goro_v_really3b
    g "Oh? Says the boy who can’t keep his clothes on when he’s drunk?"

    hide yoshi2_autumn
    hide yoshi2 sigh4
    show yoshi_autumn at center
    show yoshi comp3 at center
    voice audio.yoshi_v_comp7
    yo "Now, now, you two…"

    show aiden bold2 at right
    voice audio.aiden_v_comeon1a2
    a "Let’s put it to the test then – whoever drinks the most shots wins!"

    show yoshi shock2 at center
    voice audio.yoshi_v_wait7
    yo "H-Hold on, Aiden! You’re still hungover, I thought we weren’t gonna—"

    hide goro2_autumn
    hide goro2 comic3
    show goro_autumn at left
    show goro irked3 at left
    voice audio.goro_v_insult2a1
    g "You’re on, kiddo! If you lose, you’re running down the lobby naked!"

    show yoshi shock6 at center
    voice audio.yoshi_v_shock4
    yo "A-Ack! Don’t get carried away, sir…! We’re all gonna get kicked out if Aiden—"

    show aiden excited1 at right
    voice audio.aiden_v_oho2a
    a "DEAL!  Ohohoho, put your ugly-crying face on, ’cause I’m the obvious winner when it comes to booze, Gramps!"
    a "*takes a shot*"

    play sound sfx_shotglass
    show aiden drunk6 at right
    voice audio.aiden_v_drink1a
    a "AHH!"
    g "*takes a shot*"

    play sound sfx_shotglass
    hide goro_autumn
    hide goro irked3
    show goro2_autumn at left
    show goro2 tease6 at left
    voice audio.goro_v_heh1a
    g "Heh! I didn’t even feel a thing!"

    hide yoshi_autumn
    hide yoshi shock6
    show yoshi2_autumn at center
    show yoshi2 sigh4 at center
    voice audio.yoshi_v_sigh3a
    yo "This is gonna be a long day…"

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black with fade
    yo "{i}Sir Goro and Aiden had gotten really fired up for their sudden drinking competition…{/i}"

    if day4_aiden_choice == False:
        $day4_aiden_choice = True
        yo "{i}After they’d had a few drinks, I stepped in and stopped them from getting totally wasted before it was even evening.{/i}"
        yo "{i}They both grudgingly agreed to stop but promised to settle it when we got back to camp.  {/i}"

        $ renpy.pause (1.0, hard=True)
        yo "{i}Eventually, we decided to get out and explore another area of the hotel.{/i}"
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
        yo "{i}After they’d had a few drinks, I stepped in and stopped them from getting totally wasted before dark.{/i}"
        yo "{i}They both grudgingly agreed to stop but promised to settle it when we got back to camp.  {/i}"

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
        jump day4_aiden_after

label day4_aiden_spa:
    $quick_menu = True
    $say_box = True
    $mm_talking = True
    $a4_spa = True
    if a3_spa == False:
        voice audio.yoshi_v_think4
        yo "Maybe it’d be nice to relax a little bit, so how about we try the spa?"
    else:
        voice audio.yoshi_v_think4
        yo "How about we take a dip at the bathhouse again?"

    voice audio.aiden_v_praise3b
    a "Ooh, good idea! That’ll help me with my hangover!"

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

    if day4_aiden_choice == False:
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

    show aiden_towel at right2
    show aiden relief2 at right2
    show yoshi_towel at left2
    show yoshi relief3 at left2
    voice audio.aiden_v_relief2a
    a "Fwahhh… This is great! I can already feel my headache melting away!"

    show yoshi relief5 at left2
    voice audio.yoshi_v_relief1
    yo "The water is so nice and warm… Perfect for how cold it’s been getting lately…"

    voice audio.lloyd_v_groan2a3
    l "Ughhh! I can barely walk!!"

    show yoshi confused2 at left2
    voice audio.yoshi_v_huh1
    yo "Huh? That voice sounds familiar. "

    show aiden_towel at p5_2
    show aiden relief2 at p5_2
    show yoshi_towel at p5_1
    show yoshi confused2 at p5_1
    with move

    show darius_towel at p5_5
    show darius play1 at p5_5
    show lloyd_towel at p5_4
    show lloyd pout4 at p5_4
    with dissolve

    voice audio.lloyd_v_darius6c
    l "This wouldn’t have happened if you weren’t so rough last night, you know?"

    show darius comp2 at p5_5
    voice audio.darius_v_comp3a
    d "I’ll carry you."

    show lloyd angry2 at p5_4
    voice audio.lloyd_v_question1e4
    l "Wh-What? No! Everyone’s gonna look at us again!"

    show aiden happy1 at p5_2
    voice audio.aiden_v_guys2a
    a "Hey, guys! Over here!"

    show darius happy2 at p5_5
    voice audio.darius_v_shock1c1
    d "Oh. Aiden. Yoshi."

    show darius_towel at p4_4
    show darius happy2 at p4_4
    show lloyd_towel at p4_3
    show lloyd angry2 at p4_3
    show aiden_towel at p4_2
    show aiden happy1 at p4_2
    show yoshi_towel at p4_1
    show yoshi happy2 at p4_1
    with move

    voice audio.yoshi_v_greet11
    yo "It’s nice seeing you two here, Lloyd, Darius."

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

    show aiden happy2 at p4_2
    voice audio.aiden_v_comeon1a2
    a "Why don’t you guys join us then? There’s plenty of room beside me and Yoshi here in the tub!"

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

    show aiden laugh1 at p4_2
    voice audio.aiden_v_comp1a2
    a "Haha! Don’t worry, you’ll get used to it if you stay in longer~!"

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

    show aiden play2 at p4_2
    voice audio.aiden_v_oho1a
    a "Oho~ Did you guys have a group ‘workout’ yesterday~?"

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

    show aiden laugh3 at p4_2
    voice audio.aiden_v_laugh2a1
    a "Hahaha! That’s what you get for sticking around me too much, Yoshi~"

    show lloyd sigh5 at p4_3
    voice audio.lloyd_v_sigh2a
    l "Your stripping habits are starting to rub off on Dar, you know? He walked in here without a towel…"

    show darius bored5 at p4_4
    voice audio.darius_v_sarcastic1a
    d "It’s a bath. There’s no point."

    show lloyd pout4 at p4_3
    voice audio.lloyd_v_annoyed1a3
    l "Easy for you to say with that meatstick of yours to flaunt around!"

    show yoshi awkward3 at p4_1
    voice audio.yoshi_v_lloyd8
    yo "L-Lloyd! Don’t talk so loudly! People are staring…!"

    show lloyd think5 at p4_3
    voice audio.lloyd_v_think1a1
    l "Ehh… They already were. I mean… who wouldn’t look at his junk?!"
    #l "If you guys thought he was big before, you should see it now!"

    show aiden happy2 at p4_2
    voice audio.aiden_v_yeah2a1
    a "Oh yeah, I remember the first time I saw it! Do you guys remember that?"

    show darius talk1 at p4_4
    voice audio.darius_v_agree4
    d "I do."

    hide yoshi_towel
    hide yoshi awkward3
    show yoshi2_towel at p4_1
    show yoshi2 awkward4 at p4_1
    voice audio.yoshi_v_really6
    yo "Aiden, is this really the best topic?"

    show lloyd explain3 at p4_3
    voice audio.lloyd_v_conj4a3
    l "It was actually the first time we showered together!"

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

    $ day = "??"
    $ time = timeline_timeday
    $ season = season_summer
    $ location = location_bathroom
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_bathroom_past_day with fade
    play music here_they_come loop

    show yaiden_casual at center
    #jey
    show yaiden relief2 at center
    voice audio.yaiden_v_relief1a3
    a "Whew… I think that fixes this one. "
    a "I wonder if Dad’s done with the other bathrooms too."

    show yaiden_casual at p5_1
    show yaiden relief2 at p5_1
    with move

    show yyoshi_camp at p5_3
    show yyoshi think5 at p5_3
    show ylloyd_camp at p5_4
    show ylloyd annoy1 at p5_4
    show ydarius_camp at p5_5
    show ydarius norm3 at p5_5
    with dissolve

    voice audio.yyoshi_v_think1a
    yo "How about we try this one? Maybe it works over here!"

    show ylloyd angry5 at p5_4
    voice audio.ylloyd_v_groan2a1
    l "Ugh, I hope so! I really need a shower!"

    show ydarius tired2 at p5_5
    voice audio.ydarius_v_agree3a
    d "Same."

    show yyoshi talk3 at p5_3
    voice audio.yyoshi_v_oh2
    yo "Oh! Aiden’s here, you guys!"

    show yaiden_casual at p4_1
    #jey
    show yaiden relief2 at p4_1
    show yyoshi_camp at p4_2
    show yyoshi confused2 at p4_2
    show ylloyd_camp at p4_3
    show ylloyd angry5 at p4_3
    show ydarius_camp at p4_4
    show ydarius tired2 at p4_4
    with move

    voice audio.yyoshi_v_worry3a
    yo "What are you doing in here, Aiden?"

    show yaiden happy1 at p4_1
    voice audio.yaiden_v_guys2a
    a "Oh, hey guys! I was just doing some repairs. Dad let me help him today!"

    show yyoshi amazed1 at p4_2
    voice audio.yyoshi_v_amazed1a
    yo "Wow, I didn’t know you were good with plumbing too!"

    show yaiden comp6 at p4_1
    voice audio.yaiden_v_laugh1b1
    a "Ehehe, it’s really not that complicated… I do this kind of stuff when I’m alone back at home!"
    a "You guys sure got dirty from that gardening activity though!"

    show yyoshi explain2 at p4_2
    voice audio.yyoshi_v_yeah3
    yo "Yeah… And the showers in our cabin aren’t working so we’re looking for a place to wash off."

    show yaiden bold2 at p4_1
    voice audio.yaiden_v_well1a1
    a "Well you’re in luck, ’cause I just finished fixing up the water in here!"

    show ylloyd excited3 at p4_3
    voice audio.ylloyd_v_celebarate2a1
    l "Finally! We can take a shower!! "
    l "I thought we’d be stuck in these sticky clothes for the rest of the day!"

    show yaiden think2 at p4_1
    voice audio.yaiden_v_think1a
    a "Guess I could use a shower too. I do feel kinda gross after digging around in those pipes."

    show yyoshi happy2 at p4_2
    voice audio.yyoshi_v_aiden2
    yo "You should join us then, Aiden! "

    show yaiden excited3 at p4_1
    voice audio.yaiden_v_amazed3b
    a "Wah! I’d love to! I’ve never had a group shower before!"

    show ylloyd bold2 at p4_3
    voice audio.ylloyd_v_rush2a
    l "Let’s go, the quicker I’m clean, the better!"

    show yaiden_casual at p6_1
    #jey
    show yaiden excited3 at p6_1
    show yyoshi_camp at p6_2
    show yyoshi happy2 at p6_2
    show ylloyd_camp at p6_3
    show ylloyd bold3 at p6_3
    with move

    show ydarius awkward1 at p4_4
    d "..."

    show ylloyd confused3 at p6_3
    voice audio.ylloyd_v_darius4b
    l "Hmm? What’s wrong, Dar? Aren’t you coming?"

    show ydarius think2 at p4_4
    voice audio.ydarius_v_think1b1
    d "There aren’t any booths."

    show yyoshi talk3 at p6_2
    voice audio.yyoshi_v_yeah3
    yo "Oh yeah, I noticed that too. These unused cabins don’t have them. "

    show yaiden tease1 at p6_1
    voice audio.yaiden_v_laugh1c1
    a "Hehe~ Nowhere to hide in here."

    show ydarius talk2 at p4_4
    voice audio.ydarius_v_response1b
    d "I’ll just shower later then."

    show yaiden_casual at p4_1
    #jey
    show yaiden tease1 at p4_1
    show yyoshi_camp at p4_2
    show yyoshi talk3 at p4_2
    show ylloyd_camp at p4_3
    show ylloyd think2 at p4_3
    with move

    voice audio.ylloyd_v_confused1a1
    l "Eh? Why would you do that? You know we have an indoor activity next!"

    show ydarius think5 at p4_4
    voice audio.ydarius_v_conj2b2
    d "Well…"

    show ylloyd confused2 at p4_3
    voice audio.ylloyd_v_wait1b1
    l "You’re not embarrassed, are you? "

    show ydarius worry1 at p4_4
    d "..."

    show yyoshi confused2 at p4_2
    voice audio.yyoshi_v_darius5
    yo "Is this your first time taking a group shower too, Darius?"

    show ydarius worry2 at p4_4
    voice audio.ydarius_v_agree2c
    d "Yeah."

    show yaiden bold2 at p4_1
    voice audio.yaiden_v_darius3a
    a "Don’t be shy, Darius! We all have dicks too!"

    show ydarius sad3 at p4_4
    voice audio.ydarius_v_think2a2
    d "But mine’s… Uhh…"

    show yaiden bold5 at p4_1
    voice audio.yaiden_v_laugh2c1
    a "A dong’s a dong, no matter what it looks like, hahaha!"

    show yyoshi annoy3 at p4_2
    voice audio.yyoshi_v_aiden4
    yo "Aiden…"

    show ydarius explain2 at p4_4
    voice audio.ydarius_v_unsure2a
    d "I guess…"
    d "Promise not to laugh."

    show ylloyd shock6 at p4_3
    voice audio.ylloyd_v_confused1d1
    l "Huhhh? Why would we? You don’t have like three dicks and one ball down there, do you?"

    show ydarius bored1 at p4_4
    voice audio.ydarius_v_no1a2
    d "No."

    show yaiden bold3 at p4_1
    voice audio.yaiden_v_here1a
    a "If you’re so shy then here, I’ll show you mine first!"

    play sound sfx_clotheschanging
    hide yaiden_casual
    #jey
    hide yaiden bold3
    show yaiden_naked at p4_1
    show yaiden bold1 at p4_1
    with dissolve

    show yyoshi sigh4 at p4_2
    voice audio.yyoshi_v_sigh2
    yo "You really are quick to strip, aren’t you?"

    show yaiden bold2 at p4_1
    voice audio.yaiden_v_yoshi3a
    a "Your turn, Yoshi!"

    show yaiden_naked at p4_2
    show yaiden bold1 at p4_2
    with move

    play sound sfx_clotheschanging
    hide yyoshi_camp
    hide yyoshi sigh4
    show yyoshi_naked at p4_2
    show yyoshi angry2 at p4_2
    with dissolve

    show yaiden_naked at p4_1
    show yaiden bold1 at p4_1
    with move

    voice audio.yyoshi_v_aiden6
    yo "A-Aiden! I could’ve done it myself!"

    show yaiden tease2 at p4_1
    voice audio.yaiden_v_laugh1a1
    a "Haha, I know, but this is more fun!"

    show ylloyd sigh5 at p4_3
    voice audio.ylloyd_v_sigh2a
    l "*sigh* You two are weird, sometimes."

    play sound sfx_clotheschanging
    hide ylloyd_camp
    hide ylloyd sigh5
    show ylloyd_naked at p4_3
    show ylloyd bold2 at p4_3
    voice audio.ylloyd_v_darius3c
    l "See, Dar? There’s no need to be shy!"

    show ydarius awkward1 at p4_4
    d "..."

    show ydarius sigh1 at p4_4
    voice audio.ydarius_v_agree5c
    d "Well… Alright"
    d "Remember your promises."

    show ylloyd bold5 at p4_3
    voice audio.ylloyd_v_agree5a
    l "Of course!"

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    play sound sfx_clotheschanging
    hide ydarius_camp
    hide ydarius sigh1
    show ydarius_naked at p4_4
    show ydarius sigh1 at p4_4
    with dissolve

    $ renpy.pause (2.0, hard=True)

    show cg fade at truecenter
    show fxsq_darius 1 at fx_pos
    with dissolve

    play music here_they_come_fast loop
    voice audio.yaiden_vsa11_line1
    a "WHOA!"

    voice audio.yyoshi_vsa11_line1
    yo "I-Is that real…?"

    voice audio.ylloyd_vsa11_line1
    l "No way…"

    show fxsq_darius 2 at fx_pos with Dissolve(0.25)
    voice audio.ydarius_vsa11_line1
    d "I knew it… You guys think it’s—"

    voice audio.yaiden_vsa11_line2
    a "It’s the biggest dick I’ve ever seen!! Who knew you were packing this much, dude?! " with vpunch

    voice audio.ylloyd_vsa11_line2
    l "Why did you never tell me about this, Dar?! I should’ve been the first one to know!"

    voice audio.ydarius_vsa11_line2
    d "Seeing others, I thought I was a freak."

    voice audio.ylloyd_vsa11_line3
    l "FREAKING HUGE, you mean! You’re so lucky!!"

    voice audio.yyoshi_vsa11_line2
    yo "Yeah… Yours could be bigger than all of ours combined…"

    voice audio.ydarius_vsa11_line3
    d "You guys don’t think it’s weird?"

    voice audio.ylloyd_vsa11_line4
    l "Uh, no way, it’s awesome! You’re gonna make someone very happy one day, Dar!"

    voice audio.yaiden_vsa11_line3
    a "Or break them in half – in a good way~"

    hide cg fade
    hide fxsq_darius 2
    with dissolve

    show yyoshi laugh2 at p4_2
    voice audio.yyoshi_v_laugh1
    yo "Haha, there was nothing to worry about after all, Darius."

    show ydarius comp2 at p4_4
    voice audio.ydarius_v_agree2a1
    d "You’re right. "

    show yaiden happy2 at p4_1
    voice audio.yaiden_v_so1
    a "Does that mean you’re good to wash up with us now?"

    show ylloyd_naked at p5_4
    show ylloyd amazed1 at p5_4
    with move

    voice audio.ylloyd_v_excited3b
    l "Ooh, ooh, dibs on you, Dar! I’ll give you a good scrubbing!"

    show yaiden tease1 at p4_1
    voice audio.yaiden_v_darius3a
    a "Hehe, watch out Darius! He might go grabbing for your polearm."

    show ydarius play2 at p4_4
    voice audio.ydarius_v_laugh1a
    d "I wouldn’t mind."

    show ylloyd talk2 at p5_4
    voice audio.ylloyd_v_greet2c1
    l "H-Hey! A good wash means being squeaky clean from head to toe, y-you know!"

    show yaiden_naked at p5_2
    show yaiden tease4 at p5_2
    with move

    voice audio.yaiden_v_see1a
    a "Hear that, Yoshi? "

    show yyoshi awkward4 at p4_2
    voice audio.yyoshi_v_hey3
    yo "H-Hey…! If you touch me like that, I might—"

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
    if day4_aiden_choice == True:
        $ location = location_hotelspa
        $ day = "79"
        $ time = timeline_timeday
        $ season = season_winter
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

    show darius_towel at p4_1
    show darius play1 at p4_1
    show lloyd_towel at p4_2
    show lloyd norm2 at p4_2
    show aiden_towel at p4_3
    show aiden play1 at p4_3
    show yoshi_towel at p4_4
    show yoshi sigh4 at p4_4
    voice audio.yoshi_v_sigh3a
    yo "*sigh* We spent so long in the showers and we totally missed the next activity…"

    show lloyd talk2 at p4_2
    voice audio.lloyd_v_aiden2c
    l "I blame Aiden! He’s the one who started it!"

    show aiden tease2 at p4_3
    voice audio.aiden_v_lloyd7a
    a "Hehe, don’t act like you didn’t have a lot of fun, Lloyd. You basically arm wrestled Darius’ dick!"

    show darius tease2 at p4_1
    voice audio.darius_v_agree2a
    d "He did."

    show lloyd angry2 at p4_2
    voice audio.lloyd_v_greet2c2
    l "H-Hey! You’re supposed to be inside— I mean on my side, Dar!"

    show yoshi comp3 at p4_4
    voice audio.yoshi_v_but1
    yo "But seriously, I can’t believe you used to be embarrassed about it, Darius."

    show darius laugh3 at p4_1
    voice audio.darius_v_laugh1
    d "It was silly."

    show aiden play3 at p4_3
    voice audio.aiden_v_agree4b
    a "Now you don’t even care if the strangers here ogle your package~"

    show lloyd pout1 at p4_2
    voice audio.lloyd_v_annoyed1b3
    l "Hmph, he’s not theirs to ogle! "
    l "Anyways, I’ve been sitting for so long my butt cheeks are getting cramped."

    show darius play2 at p4_1
    voice audio.darius_v_lloyd7a
    d "I can loosen them up again. "

    show lloyd happy1 at p4_2
    voice audio.lloyd_v_agree2b3
    l "Yeah! Come on Dar, let’s go get a room and you can give me that deep massage you promised!"

    show darius bold5 at p4_1
    voice audio.darius_v_rush1
    d "Alright."
    d "Don’t be surprised if you need a wheelchair after."

    show lloyd laugh1 at p4_2
    voice audio.lloyd_v_bye1a
    l "We’ll go ahead, you guys!"

    show aiden laugh1 at p4_3
    voice audio.aiden_v_bye1a
    a "Haha, see you guys later! Yoshi and I are gonna keep chilling here for now."

    show yoshi happy2 at p4_4
    voice audio.yoshi_v_bye1a
    yo "Bye, guys!"

    show darius happy2 at p4_1
    voice audio.darius_v_bye1a
    d "Bye."

    hide lloyd_towel
    hide lloyd laugh1
    hide darius_towel
    hide darius happy2
    with dissolve

    show aiden_towel at left2
    show aiden laugh1 at left2
    show yoshi_towel at right2
    show yoshi talk1 at right2
    with move

    voice audio.yoshi_v_okay1
    yo "Okay, now you can’t tell me they’re not planning to have sex from how they both said that."

    show aiden tease1 at left2
    voice audio.aiden_v_perv1
    a "Hahaha! Guess my prophecy about Darius splitting someone in half will come true."

    hide yoshi_towel
    hide yoshi talk1
    show yoshi2_towel at right2
    show yoshi2 sigh1 at right2
    voice audio.yoshi_v_sigh3a
    yo "*sigh* Aiden…"

    show aiden laugh3 at left2
    voice audio.aiden_v_laugh2a1
    a "Hahaha!"

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black with fade

    if day4_aiden_choice == False:
        $day4_aiden_choice = True
        yo "{i}Aiden and I stayed a little longer, relaxing and recovering from last night.{/i}"

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
        $ say_box = False
        $mm_talking = False
        $renpy.choice_for_skipping()
        show screen minimap()
        $ renpy.pause (hard=True)

    else:
        yo "{i}Aiden and I stayed a little longer, relaxing and enjoying the afternoon.{/i}"

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
        jump day4_aiden_after

label day4_aiden_cafe:
    $sq_emilia += 1
    $quick_menu = True
    $say_box = True
    $mm_talking = True
    $a4_cafe = True
    voice audio.yoshi_v_think4
    yo "We could grab something to eat over at the café!"

    if a3_cafe == True:
        voice audio.aiden_v_agree3a1
        a "Sure thing! I’m curious what the food there is like, anyway!"
    else:
        voice audio.aiden_v_agree3a1
        a "Sure thing! I’m feeling pretty hungry too!"

    hide screen minimap
    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black
    hide screen location
    hide screen timeline
    hide screen quick_menu
    with fade
    $quick_menu = False
    $ renpy.pause (2.0, hard=True)

    if day4_aiden_choice == False:
        $ location = location_hotelcafe
        show screen location
        show screen timeline
        show screen quick_menu
        $quick_menu = True
        scene bg_hotel_cafe_day with fade
        play music heracleum_a loop
    else:
        $ location = location_hotelcafe
        show screen location
        show screen timeline
        show screen quick_menu
        $quick_menu = True
        scene bg_hotel_cafe_sunset with fade
        play music heracleum_a loop

    show reimond_waiter at p6_1
    show reimond sad1 at p6_1
    show emilia_autumn at p6_2
    show emilia annoy1 at p6_2
    show aiden2_autumn at p6_6
    show aiden2 scared2 at p6_6
    show yoshi_autumn at p6_5
    show yoshi norm3 at p6_5
    voice audio.aiden_v_shock2b2
    a "Yikes, Emilia is here… "

    if a4_lobby == True:
        a "Guess we know why Yuri didn’t hang out here, huh?"
        a "Looks like she’s harassing that waiter too…"
    else:
        a "And it looks like she’s harassing that waiter…"

    show emilia angry2 at p6_2
    voice audio.emilia_v_angry2
    e "I can’t believe you served me something raw! Touch this meat and tell me that’s not just taken straight out of the fridge!"

    show reimond confused2 at p6_1
    voice audio.reimond_v_maam1b
    r "You ordered prosciutto, ma’am… And it’s from our cold cuts menu…"

    show emilia rage4 at p6_2
    voice audio.emilia_v_question4b
    e "I-I knew that! But I’m not trying to get salmonella on my vacation, is that too hard to understand?!"

    show reimond sad2 at p6_1
    voice audio.reimond_v_apology1a1
    r "U-Um… No, I’m sorry. Maybe you would prefer some bacon or ham instead?"

    show emilia disgust2 at p6_2
    voice audio.emilia_v_request4a
    e "I didn’t come here to eat something that common! Now, cook this meat up before I sue this entire place!"

    show reimond sad6 at p6_1
    voice audio.reimond_v_agree6c1
    r "S-Sure… Right away, ma’am."

    hide reimond_waiter
    hide reimond sad6
    with dissolve

    show emilia sigh1 at p6_2
    voice audio.emilia_v_sigh1a
    e "*sigh* Can’t even have a good time around here…"

    show emilia shock3 at p6_2
    e "...!"

    hide aiden2_autumn
    hide aiden2 scared2
    show aiden_autumn at p6_6
    show aiden panic4 at p6_6
    voice audio.aiden_v_swear3b
    a "Oh crap! She saw us…!"
    a "I’ll go order something and get a table for us! Distract her for me, Yoshi!"

    hide aiden_autumn
    hide aiden panic4
    with dissolve

    show yoshi shock2 at p6_5
    voice audio.yoshi_v_wait3a
    yo "A-Aiden, wait…!"

    show emilia irked2 at p6_2
    voice audio.emilia_v_so3
    e "Are you just going to stand over there and pretend I didn’t see you?"

    hide yoshi_autumn
    hide yoshi shock2
    show yoshi2_autumn at p6_5
    show yoshi2 awkward3 at p6_5
    voice audio.yoshi_v_ah4
    yo "A-Ah…!"

    show emilia_autumn at left2
    show emilia irked2 at left2
    show yoshi2_autumn at right2
    show yoshi2 talk3 at right2
    with move

    voice audio.yoshi_v_actually1a
    yo "Aiden and I are actually here to grab a meal. We just happened to notice you were having a problem with the staff again."

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

    show aiden2_autumn at p5_5
    show aiden2 awkward5 at p5_5
    with dissolve

    voice audio.aiden_v_hey1e2
    a "Is the coast clear?"

    show yoshi2_autumn at left2
    show yoshi2 sigh1 at left2
    show aiden2_autumn at right2
    show aiden2 worry2 at right2
    with move

    voice audio.aiden_v_sheesh1a
    a "Sheesh, Yoshi… That was messy…"

    show yoshi2 worry2 at left2
    voice audio.yoshi_v_think1a
    yo "It looks like there’s no chance any of us can get along with her. She’s made up her mind that we’re all out to get her."

    show aiden2 sad4 at right2
    voice audio.aiden_v_comeon1a2
    a "You know she’s always been like that…"
    a "Even when you guys were scouts, all she ever did was complain and push people away…"

    show yoshi2 sad4 at left2
    voice audio.yoshi_v_well1
    yo "I don’t think that was her intent… She had a lot of problems to deal with, even back then."

    show aiden2 confused5 at right2
    voice audio.aiden_v_actually2a
    a "Really? If I was as rich as her, I’d have nothing to whine about!"

    show yoshi2 upset6 at left2
    voice audio.yoshi_v_actually2a
    yo "It’s a lot more complicated than that…"

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

    show yemilia_camp at p5_5
    show yemilia rage4 at p5_5
    with dissolve

    voice audio.yemilia_v_angry4a
    e "GRAHHH!!!" with vpunch
    e "*throws phone on the ground*"

    show yemilia rage6 at p5_5
    voice audio.yemilia_v_angry9
    e "Stupid camp! Stupid parents! Stupid everything!!"

    show yyoshi_camp at left2
    show yyoshi worry2 at left2
    show yemilia_camp at right2
    show yemilia rage6 at right2
    with move

    voice audio.yyoshi_v_emilia5
    yo "A-Are you alright, Emilia?"

    show yemilia panic2 at right2
    e "...!"

    show yemilia angry3 at right2
    voice audio.yemilia_v_gasp1
    e "How long have you been standing there?! Were you spying on me?!"

    show yyoshi worry5 at left2
    voice audio.yyoshi_v_no3
    yo "N-No, I was just passing by and I heard you screaming on the phone…"

    show yemilia angry2 at right2
    voice audio.yemilia_v_angry1a
    e "It’s none of your business! And don’t you dare tell anyone what you’ve heard!"

    show yyoshi sad4 at left2
    voice audio.yyoshi_v_awkward1
    yo "Y-Your phone, though… It’s broken… I can ask a scoutmaster to fix it."

    show yemilia rage4 at right2
    voice audio.yemilia_v_angry2a
    e "You’re just gonna use that to get me in trouble, aren’t you?!"

    show yyoshi panic2 at left2
    voice audio.yyoshi_v_disagree2
    yo "N-No, that’s not—"

    show yemilia rage6 at right2
    voice audio.yemilia_v_annoyed2b2
    e "Shut up! Just leave me alone like everyone else!!!"

    hide yemilia_camp
    hide yemilia rage6
    with dissolve

    show yyoshi sad1 at left2
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

    if day4_aiden_choice == True:
        $ day = "79"
        $ time = timeline_timesunset
        $ season = season_winter
        $ location = location_hotelcafe
        show screen location
        show screen timeline
        show screen quick_menu
        $quick_menu = True
        scene bg_hotel_cafe_sunset with fade
        play music buddy_oath_hotel loop
    else:
        $ location = location_hotelcafe
        $ day = "79"
        $ time = timeline_timeday
        $ season = season_winter
        show screen location
        show screen timeline
        show screen quick_menu
        $quick_menu = True
        scene bg_hotel_cafe_day with fade
        play music buddy_oath_hotel loop

    show yoshi2_autumn at left2
    show yoshi2 upset1 at left2
    show aiden2_autumn at right2
    show aiden2 worry5 at right2
    voice audio.aiden_v_shock2b1
    a "Yikes… It sounds like her parents are even worse than her…"

    show yoshi2 sad4 at left2
    voice audio.yoshi_v_so2
    yo "I never got the full the story but, it helps me understand why she acts like that…"

    show aiden2 think2 at right2
    voice audio.aiden_v_sigh1a
    a "No wonder you were always so nice to her. But then, you’re always nice to everyone."

    show yoshi2 sad5 at left2
    voice audio.yoshi_v_well1
    yo "Well.. You never know what’s going on behind the scenes in people’s lives, so it’s best to give them the benefit of the doubt…"

    show aiden2 angry2 at right2
    voice audio.aiden_v_but1a1
    a "Still, doesn’t give her an excuse for that attitude. "

    show yoshi2 sigh1 at left2
    voice audio.yoshi_v_right10
    yo "I agree…"

    hide aiden2_autumn
    hide aiden2 angry2
    show aiden_autumn at right2
    show aiden comp3 at right2
    voice audio.aiden_v_anyway2b
    a "Anyways, I got us both some snacks… Let’s eat and forget about all that drama."

    hide yoshi2_autumn
    hide yoshi2 sigh1
    show yoshi_autumn at left2
    show yoshi sad4 at left2
    voice audio.yoshi_v_sure3
    yo "Sure, Aiden. Thanks."

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black with fade
    yo "{i}Somehow, whenever Emilia and I interact, it always ends up so tense… I wish there was a way to reach her like I could back then.{/i}"
    yo "{i}But I can only do so much, and she’s not willing to meet me halfway…{/i}"
    yo "{i}Thankfully, Aiden was there to get my mind off of her.{/i}"
    $ renpy.pause (1.0, hard=True)
    if day4_aiden_choice == False:
        $ day4_aiden_choice = True
        yo "{i}Aiden and I stayed a little longer, relaxing and recovering from last night.{/i}"
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
        yo "{i}Aiden and I stayed a little longer, relaxing and enjoying the afternoon.{/i}"
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
        jump day4_aiden_after

label day4_aiden_room:
    $sq_jin += 1
    $quick_menu = True
    $say_box = True
    $mm_talking = True
    $a4_room = True
    if a4_lobby == True:
        voice audio.yoshi_v_think4
        yo "Why don’t we head over to the other rooms and see what they’re doing?"

        voice audio.aiden_v_agree3a1
        a "Sure! Let’s just hope we don’t interrupt something, hehe~"
    else:
        voice audio.yoshi_v_think4
        yo "Why don’t we go and check on Jin? He might need some encouragement getting out of his room."

        voice audio.aiden_v_agree3a1
        a "Sure! Let’s head over there."

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

    if day4_aiden_choice == False:
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
    show jin_autumn at center
    show jin_glasses at center
    show jin talk2 at center
    $ renpy.pause (1.0, hard=True)
    voice audio.jin_v_oh3a
    j "O-Oh, coming! Give me just a moment!"

    show jin_autumn at p5_5
    show jin_glasses at p5_5
    show jin talk2 at p5_5
    with move

    play sound sfx_dooropen
    show jin_autumn at left
    show jin_glasses at left
    show jin talk2 at left
    with move

    show yoshi_autumn at center
    show yoshi norm1 at center
    show aiden_autumn at right
    show aiden norm1 at right
    with dissolve

    if a4_lobby == True:
        show jin happy1 at left
        voice audio.jin_v_greet1b3
        j "Ah! Hello again, you two!"

        show yoshi confused2 at center
        voice audio.yoshi_v_jin5
        yo "Jin? What are you doing back in the room already?"

        show aiden play2 at right
        voice audio.aiden_v_yeah1a1
        a "Yeah, weren’t you enjoying a snoopfest with Yuri?"

        show jin awkward3 at left
        voice audio.jin_v_conj2c1
        j "W-Well, we were trying to, but Sir Goro actually found us shortly after you guys left."
        j "Yuri didn’t want us to get scolded, so she made me run with the laptop before he noticed…"

        hide yoshi_autumn
        hide yoshi confused2
        show yoshi2_autumn at center
        show yoshi2 sigh1 at center
        voice audio.yoshi_v_sigh3a
        yo "*sigh* You make it sound like it was a whole criminal operation or something…"

        show aiden laugh1 at right
        voice audio.aiden_v_laugh2a1
        a "Haha, can’t blame Jin though! He was probably ready to get back to the room anyway~"

        show jin shy2 at left
        voice audio.jin_v_sigh1a
        j "I-I was starting to feel a little too exposed out there…"
    else:
        show jin happy1 at left
        voice audio.jin_v_greet1b3
        j "Ah! Hello, you two!"

        show yoshi talk1 at center
        voice audio.yoshi_v_jin1
        yo "Hello, Jin! We were coming to see if you’d gotten out into the hotel yet."

        show aiden play2 at right
        voice audio.aiden_v_no1a2
        a "Guess the answer is no."

        show jin awkward3 at left
        voice audio.jin_v_conj1c1
        j "A-Actually, I did try and tag along with Lloyd and Darius to the bathhouse earlier…!"

        show aiden tease2 at right
        voice audio.aiden_v_oho2a
        a "Ohoho, now that sounds like something you’d be more interested in~"

        show jin sigh1 at left
        voice audio.jin_v_yeah2c
        j "I-I thought so too, but it definitely got too hot and heavy in there for me to handle…"

        show yoshi comp3 at center
        voice audio.yoshi_v_aww1
        yo "Aww, Jin! You know you’re supposed to wait a while to adjust before pulling out."

        show aiden wink2 at right
        voice audio.aiden_v_laugh1b2
        a "Hehe, yeah Jin, you’re supposed to take it slow – if you go too fast, it can be painful~"

        show jin shy3 at left
        voice audio.jin_v_gulp1a
        j "*gulp*"

    hide yoshi2_autumn
    hide yoshi2 sigh1
    show yoshi_autumn at center
    show yoshi explain2 at center
    voice audio.yoshi_v_ehem1b
    yo "*ehem* Anyway, are you alright in here by yourself? "

    show jin talk2 at left
    voice audio.jin_v_yes4b
    j "O-Oh, yes, I’m totally fine! This place is a little out of my element, anyway…"

    show yoshi confused2 at center
    voice audio.yoshi_v_huh1
    yo "Huh? What do you mean?"

    if a3_room == True:
        show aiden talk2 at right
        voice audio.aiden_v_oh1a
        a "Oh! I think I get it."
        a "Jin here is like me, he prefers the outdoors! A place this fancy can feel too stuffy for our liking."

        show aiden happy1 at right
        voice audio.aiden_v_agree2e2
        a "Isn’t that right, Jin?"
    else:
        show jin worry2 at left
        voice audio.jin_v_conj2b1
        j "I-It’s just… a place like this has a little too much hustle and bustle for someone like me…"

        show yoshi talk3 at center
        voice audio.yoshi_v_but1
        yo "I can understand that, but you won’t know what you’re missing unless you give it a chance!"

        show aiden talk3 at right
        voice audio.aiden_v_yoshi11a
        a "Give him a break, Yoshi! Maybe Jin is more like me, and prefers the outdoors~"
        a "Right, Jin?"

    show jin think2 at left
    voice audio.jin_v_yeah2a
    j "W-Well… Yeah, kind of like Camp Buddy."

    show aiden happy3 at right
    voice audio.aiden_v_yeah2a2
    a "Haha, you shoulda been with us last term, when we went to the beach with the scouts!"
    a "I bet that’s way more up your alley!"

    hide jin_autumn
    hide jin think2
    hide jin_glasses
    show jin2_autumn at left
    show jin2 fudan3 at left
    show jin2_glasses at left
    voice audio.jin_v_gasp2a
    j "*gasp* A beach episode?!"

    show aiden bold2 at right
    voice audio.aiden_v_agree1a2
    a "Yup! Just sun, sand, and all the beach bods you can imagine!"

    show jin2 fudan5 at left
    voice audio.jin_v_hngh1b
    j "Hngh…!!"

    hide yoshi_autumn
    hide yoshi talk3
    hide yoshi confused3
    show yoshi2_autumn at center
    show yoshi2 sigh4 at center
    voice audio.yoshi_v_sigh3a
    yo "*sigh* Don’t get him worked up, Aiden…"

    show aiden tease2 at right
    voice audio.aiden_v_what2b
    a "What? It’s true! I had on the tiniest white swimsuit too, Jin~ "

    show jin2 excited2 at left
    voice audio.jin_v_rush1c1
    j "Y-You have to tell me all the details, right now!"

    show aiden excited3 at right
    voice audio.aiden_v_yeah2a1
    a "Oh yeah! You can add that to that blog you’ve been working on!"
    a "It’ll be a special section about the spiciest moments with a certain someone~"

    show aiden wink3 at right
    a "*winks at Yoshinori*"

    hide yoshi2_autumn
    hide yoshi2 sigh4
    show yoshi_autumn at center
    show yoshi awkward3 at center
    voice audio.yoshi_v_aiden6
    yo "A-Aiden! I don’t think that’s appropriate for—"

    show jin2 scheme4 at left
    voice audio.jin_v_yes6c
    j "YES, IT IS! I INSIST!"
    j "LET ME GRAB MY LAPTOP RIGHT NOW!"

    show aiden tease1 at right
    voice audio.aiden_v_alright1b2
    a "Alright~!"

    hide yoshi_autumn
    hide yoshi awkward3
    show yoshi2_autumn at center
    show yoshi2 sigh4 at center
    voice audio.yoshi_v_really6
    yo "*sigh* Are we really doing this…?"

    # JMA3
    $renpy.choice_for_skipping()
    scene cg white
    $ quick_menu = False
    $ say_box = False
    hide screen location
    hide screen timeline
    hide screen quick_menu
    with Dissolve(2.0)
    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    $ global minigame_id
    $ minigame_id = 'jmA3'
    if day4_aiden_choice == False:
        $ renpy.call(minigame_id, 'day')
    else:
        $ renpy.call(minigame_id, 'sunset')

label day4_aiden_postmg:
    hide screen location
    hide screen timeline
    hide screen quick_menu
    $quick_menu = False
    scene cg white with Dissolve(2.0)

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
    play bgsound sfxloop_seagulls loop
    play bgsound2 sfxloop_wavesday loop
    play music beachside_day loop

    show yoshi2_swim at center
    show yoshi2 sigh1 at center
    voice audio.yoshi_v_relief1
    yo "Phew… I finally got a chance to get changed too."

    hide yoshi2_swim
    hide yoshi2 sigh1
    show yoshi_swim at center
    show yoshi talk1 at center
    voice audio.yoshi_v_alright1
    yo "Now that we have the tents set up, I should start getting the first activity ready!"
    yo "Let’s see—"

    show yoshi_swim at p5_4
    show yoshi talk1 at p5_4
    with move

    show aiden_swim at p5_5
    show aiden talk4 at p5_5
    with dissolve

    voice audio.aiden_v_oh1a
    a "Oh! There you are, Yoshi!"

    show yoshi_swim at left2
    show yoshi shock3 at left2
    show aiden_swim at right2
    show aiden talk4 at right2
    with move

    voice audio.yoshi_v_aiden6
    yo "A-Aiden! What the heck are you wearing?!"

    show aiden happy1 at right2
    voice audio.aiden_v_laugh1b2
    a "You like it? Yuri got me this suit just for the occasion!"
    a "She said it contrasts with my skin tone nicely~"

    hide yoshi_swim
    hide yoshi shock3
    show yoshi2_swim at left2
    show yoshi2 awkward3 at left2
    voice audio.yoshi_v_but3
    yo "But it’s… barely covering anything…"

    show aiden play2 at right2
    voice audio.aiden_v_hey1b2
    a "Hey, you’re talking to the guy who walks around the camp naked."
    a "This is teeeechnically more than usual!"

    show yoshi2 sigh4 at left2
    voice audio.yoshi_v_sigh3a
    yo "*sigh* That’s true, but your apron at least covers your crotch completely…"
    yo "With this, it’s… well…"

    show aiden tease1 at right2
    voice audio.aiden_v_oho2a
    a "Ohoho~ Can’t help but stare at my junk, Yoshi? "

    hide yoshi2_swim
    hide yoshi2 sigh4
    show yoshi_swim at left2
    show yoshi explain2 at left2
    voice audio.yoshi_v_ehem1b
    yo "*ehem* W-Well, in any case, I should really start preparing the next activity."

    hide aiden_swim
    hide aiden tease1
    show aiden2_swim at right2
    show aiden2 worry2 at right2
    voice audio.aiden_v_what1b
    a "What? We just got here! "
    a "We’re on vacation, and we just had the sportsfest too! Loosen up a little!"

    show yoshi explain1 at left2
    voice audio.yoshi_v_unsure3c
    yo "I-I’m not sure—"

    hide aiden2_swim
    hide aiden2 worry2
    show aiden_swim at right2
    show aiden excited1 at right2
    voice audio.aiden_v_comeon1a1
    a "I’m sure for you! Come on, let’s go swim!"

    show aiden_swim at center
    show aiden excited1 at center
    with move

    show yoshi shock2 at left2
    voice audio.yoshi_v_wait3a
    yo "A-Aiden, wait—"

    hide yoshi_swim
    hide yoshi shock2
    hide aiden_swim
    hide aiden excited1
    with moveoutright

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
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_beach3_summer_day with fade
    play bgsound sfxloop_seagulls loop
    play bgsound2 sfxloop_wavesday loop
    play music beachside_day loop

    show yoshi_swim at p5_1
    show yoshi norm1 at p5_1
    show aiden_swim2 at p5_5
    show aiden relief2 at p5_5
    voice audio.aiden_v_relief1a1
    a "Whew, the water feels great!"
    a "Get in here, Yoshi! Come swim!  "

    show yoshi laugh1 at p5_1
    voice audio.yoshi_v_laugh1
    yo "Haha, you’re just as energetic as ever, Aiden."
    yo "You’ve hardly changed from when we were younger."

    show aiden play2 at p5_5
    voice audio.aiden_v_laugh1b2
    a "And you still ramble about cheesy stuff like there’s no tomorrow!"

    show aiden_swim2 at p5_3
    show aiden happy1 at p5_3
    with move

    voice audio.aiden_v_comeon1a1
    a "Quit stalling and take a d—"

    show yoshi shock3 at p5_1
    voice audio.yoshi_v_shock4
    yo "G-G-GREAT WHITE SHANK!" with vpunch

    show aiden shock6 at p5_3
    voice audio.aiden_v_shock5a
    a "S-Shark?! WHERE?!"

    show aiden_swim2 at p5_2
    show aiden shock6 at p5_2
    with move

    show yoshi_swim at left2
    show yoshi shock6 at left2
    show aiden_swim2 at right2
    show aiden shock6 at right2
    with move

    voice audio.yoshi_v_no5
    yo "N-No, Aiden! Y-Your suit! Cover your crotch up, before anyone else sees!"

    hide aiden_swim2
    hide aiden shock6
    show aiden2_swim2 at right2
    show aiden2 pout2 at right2
    voice audio.aiden_v_sheesh1a
    a "Sheesh, Yoshi, I almost had a heart attack!"

    show yoshi angry3 at left2
    voice audio.yoshi_v_what4
    yo "I should be the one saying that! Look at yourself, you might as well be naked!"

    hide aiden2_swim2
    hide aiden2 pout2
    show aiden_swim2 at right2
    show aiden tease1 at right2
    voice audio.aiden_v_perv1
    a "That can be arranged, if you want~"

    hide yoshi_swim
    hide yoshi angry3
    show yoshi2_swim at left2
    show yoshi2 shy5 at left2
    voice audio.yoshi_v_gulp1a
    yo "*gulp* Don’t be silly, Aiden. You know we can’t do stuff like that here, at least not when there could be scouts around."

    show aiden tease2 at right2
    voice audio.aiden_v_yeah2b2
    a "Oh yeah? I think the bulge in your pants disagrees~"

    hide yoshi2_swim
    hide yoshi2 shy5
    show yoshi_swim at left2
    show yoshi awkward4 at left2
    voice audio.yoshi_v_what4
    yo "W-What…?! I’m not—"

    show aiden_swim2 at center
    show aiden wink3 at center
    with move

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    voice audio.aiden_v_yoshi14a
    a "Oh I dunno, Yoshi~ I’m not convinced ’til I get a closer look!"

    jump day4_aiden_ma1

label day4_aiden_aftermasx:
    hide screen location
    hide screen timeline
    hide screen quick_menu
    $quick_menu = False
    scene cg white with Dissolve(2.0)

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

label day4_aiden_postfb:
    if day4_aiden_choice == False:
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
        $ day = "79"
        $ time = timeline_timesunset
        $ season = season_winter
        $ location = location_hotelroom
        show screen location
        show screen timeline
        show screen quick_menu
        $quick_menu = True
        scene bg_hotel_room2_sunset with fade

    play music here_they_come loop
    show jin2_autumn2 at left
    show jin2 dizzy2 at left
    show jin2_blush2 at left
    show jin2_nosebleed at left
    show jin2_glasses at left
    show yoshi_autumn at center
    show yoshi think1 at center
    show aiden_autumn at right
    show aiden norm1 at right
    voice audio.jin_v_fudan4a1
    j "B-Beach… W-White foam…"

    hide yoshi_autumn
    hide yoshi think1
    show yoshi2_autumn at center
    show yoshi2 think2 at center
    voice audio.yoshi_v_actually1a
    yo "You know, it was probably a good thing we were in the water, or there would’ve been no way to clean up that mess."
    yo "*sigh* And I remember my thing feeling numb for the rest of the day after that too."

    show aiden laugh1 at right
    voice audio.aiden_v_laugh2a1
    a "I gotta admit, I felt so full after I couldn’t eat a single bite of lunch or dinner, hahaha!"

    show jin2 dizzy3 at left
    voice audio.jin_v_fudan2c
    j "Cream… Pie…"

    show yoshi2 sigh4 at center
    voice audio.yoshi_v_sigh3a
    yo "It was a miracle nobody found us, or else it would’ve been a disaster."
    yo "I can’t even imagine what would’ve happened if Sir Goro and the scouts caught us… Or worse, Yuri…"

    show aiden tease2 at right
    voice audio.aiden_v_jin8a
    a "So, Jin~ How was that for a spicy story~?"

    show jin2 dizzy1 at left
    j "..."

    hide yoshi2_autumn
    hide yoshi2 sigh4
    show yoshi_autumn at center
    show yoshi confused2 at center
    voice audio.yoshi_v_uh1a
    yo "Uhh… We might’ve overloaded him again, Aiden…"

    show aiden tease1 at right
    voice audio.aiden_v_think2a
    a "Oh something’s overloaded for sure. Just look at his pants~"

    show yoshi shock2 at center
    voice audio.yoshi_v_shock4
    yo "Gah! J-Jin!"

    show jin2 dizzy5 at left
    voice audio.jin_v_bye2b2
    j "I have to go… to the toilet… "

    hide jin2_autumn2
    hide jin2 dizzy5
    hide jin2_nosebleed
    hide jin2_blush2
    hide jin2_glasses
    with dissolve

    show yoshi_autumn at left2
    show yoshi shock2 at left2
    show aiden_autumn at right2
    show aiden laugh3 at right2
    with move

    voice audio.aiden_v_laugh2a1
    a "Hahaha! Guess we really worked him up~"

    hide yoshi_autumn
    hide yoshi shock2
    show yoshi2_autumn at left2
    show yoshi2 sigh1 at left2
    voice audio.yoshi_v_sigh3a
    yo "*sigh* And it looks like he didn’t even write anything down on his laptop."

    hide yoshi2_autumn
    hide yoshi2 sigh1
    show yoshi_autumn at left2
    show yoshi talk2 at left2
    voice audio.yoshi_v_anyway1a
    yo "Although, that might be for the best… We shouldn’t publish anything like that on the blog."
    yo "Let’s just fill out a story about the activities while Jin, uhh… takes care of his business."

    show aiden bold2 at right2
    voice audio.aiden_v_oh1a
    a "Oh, you mean like the time we slept naked together later that same night?"

    voice audio.jin_v_hngh5c
    j "HNGHGHGHGGHH!" with vpunch

    hide yoshi_autumn
    hide yoshi sigh1
    show yoshi2_autumn at left2
    show yoshi2 sigh4 at left2
    voice audio.yoshi_v_sigh3a
    yo "*sigh*"

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black with fade
    yo "{i}We spent the next while typing out some of the fun events we’d done at the beach on Jin’s laptop.{/i}"
    yo "{i}After he calmed down, Jin joined us and helped get the next entry ready.{/i}"
    $ renpy.pause (1.0, hard=True)

    if day4_aiden_choice == False:
        $ day4_aiden_choice = True
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
        jump day4_aiden_after

label day4_aiden_after:
    $ time = timeline_timenight
    $say_box = True
    $ location = location_hotelroom
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_hotel_room1_night with fade
    play music close_distance loop

    show yoshi_sleep at left2
    show yoshi norm1 at left2
    show aiden_sleep at right2
    show aiden tired4 at right2
    voice audio.aiden_v_relief1a1
    a "Whew… it’s really getting chillier, huh?"

    hide yoshi_sleep
    hide yoshi norm1
    show yoshi2_sleep at left2
    show yoshi2 comp3 at left2
    voice audio.yoshi_v_well3
    yo "W-Well, you’re barely wearing anything, Aiden…"

    show aiden relief2 at right2
    voice audio.aiden_v_hngh1b2
    a "Can’t help it! I wanna feel these premium sheets rub against my skin!"

    show yoshi2 sigh1 at left2
    voice audio.yoshi_v_sigh3a
    yo "*sigh* You’ll take any excuse to get your clothes off, I guess…"

    show aiden talk4 at right2
    voice audio.aiden_v_question1a
    a "But seriously, have you noticed that it’s been snowing nonstop the whole time we’ve been here?"

    hide yoshi2_sleep
    hide yoshi2 sigh1
    show yoshi_sleep at left2
    show yoshi talk1 at left2
    voice audio.yoshi_v_oh1
    yo "Oh yeah, I saw. It looks like it’s not stopping anytime soon either."

    show aiden happy2 at right2
    voice audio.aiden_v_relief2a
    a "Feels good to have a warm and cozy room, without all the troubles of setting up a fireplace! Hahaha!"
    a "Don’t get me wrong, I’d pick our cozy cabins over a thousand-dollar room like this any day! "

    show yoshi comp2 at left2
    voice audio.yoshi_v_well1
    yo "Well, I’m just glad you’re starting to enjoy your time here, Aiden."

    show aiden comp2 at right2
    voice audio.aiden_v_well1b2
    a "I wouldn’t if it weren’t for you."
    a "But I’m still a little on edge by how lavish everything is. Makes me really miss our simple life back at camp."

    show yoshi comp5 at left2
    voice audio.yoshi_v_right9
    yo "I get you. It’s only been two days, and I have to admit I’m feeling kind of homesick too. "

    show aiden relief4 at right2
    voice audio.aiden_v_actually1b
    a "Good thing we don’t have any plans for tonight, I’d rather just stay in our room and wait for this trip to end!"

    play sound sfx_doorknock
    $ renpy.pause (1.0, hard=True)
    show yoshi talk3 at left2
    voice audio.yoshi_v_oh4
    yo "Oh? Who could that be?"

    show yoshi_sleep at p5_1
    show yoshi talk3 at p5_1
    with move

    play sound sfx_dooropen
    show yoshi_sleep at p4_3
    show yoshi talk3 at p4_3
    show aiden_sleep at p4_4
    show aiden relief4 at p4_4
    with move

    show goro_autumn at p4_1
    show goro norm1 at p4_1
    show yuri_autumn at p4_2
    show yuri happy2 at p4_2
    with dissolve

    voice audio.yuri_v_greet2a
    yu "Hi, guys~!"

    show aiden happy1 at p4_4
    voice audio.aiden_v_hey2a1
    a "Hey, Yuri~ Hey, Gramps!"

    show yuri tease2 at p4_2
    voice audio.yuri_v_oh1b
    yu "Oh? Are we interrupting something here~?"

    show yoshi happy2 at p4_3
    voice audio.yoshi_v_disagree3
    yo "Not at all!"

    show yuri tease4 at p4_2
    voice audio.yuri_v_unsure4a
    yu "Are you suuuure? ’Cause Aiden’s rolling on the bed half-naked~"

    show yoshi sigh1 at p4_3
    voice audio.yoshi_v_yuri6
    yo "That’s nothing new, Yuri. He’s actually wearing more than usual."

    show goro play3 at p4_1
    voice audio.goro_v_well1a
    g "You know how men are, dear."

    show aiden bold2 at p4_4
    voice audio.aiden_v_greet1c
    a "Hehe, what made you guys drop by? Need anything? "

    show goro talk1 at p4_1
    voice audio.goro_v_ah1a
    g "Ah, we were informed that we have a scheduled formal dinner tonight down at the restaurant."

    hide aiden_sleep
    hide aiden bold2
    show aiden2_sleep at p4_4
    show aiden2 shy2 at p4_4
    voice audio.aiden_v_whistle1a
    a "*whistles* Fancy…"

    show yoshi awkward4 at p4_3
    voice audio.yoshi_v_amazed1c
    yo "And I thought we were done getting spoiled…"

    show yuri happy1 at p4_2
    voice audio.yuri_v_yeah1a1
    yu "Yeah, it was another surprise arrangement by Mr. Clermont."

    show aiden2 awkward5 at p4_4
    voice audio.aiden_v_sheesh1a
    a "Sheesh... He really has that much money to blow on peeps like us? You sure the guy just doesn’t have a crush on you, Gramps?"

    hide goro_autumn
    hide goro talk1
    show goro2_autumn at p4_1
    show goro2 shy2 at p4_1
    voice audio.goro_v_what2
    g "Wh-What…? Where did that even come from?!"
    g "Just so you all know. This is simply part of the VIP-Class package he got for us."

    show yoshi worry5 at p4_3
    voice audio.yoshi_v_wait3a
    yo "W-Wait, did you say formal dinner, sir? I don’t think any of us packed appropriate clothing for something like this…"

    hide goro2_autumn
    hide goro2 shy2
    show goro_autumn at p4_1
    show goro explain2 at p4_1
    voice audio.goro_v_actually1a
    g "Well… Mr. Clermont expected that, so he made provisions for us."

    show goro_autumn at p6_3
    show goro explain2 at p6_3
    with move

    show goro_autumn at p4_1
    show goro explain2 at p4_1
    with move

    play sound sfx_clothesslam
    g "Here. The hotel staff delivered us sets of formalwear to choose from."

    show goro think3 at p4_1
    voice audio.goro_v_think1a1
    g "He asked me for everyone’s uniform measurements a few weeks ago, so he got all of our sizes."

    show yoshi shock2 at p4_3
    voice audio.yoshi_v_shock1b
    yo "Whoa… Mr. Clermont’s really gone overboard with this…"

    show goro shy4 at p4_1
    voice audio.goro_v_yeah1b1
    g "I know. As much as we’re all overwhelmed by his generosity, it would be best to just appreciate it."

    show yuri excited2 at p4_2
    voice audio.yuri_v_yeah1b1
    yu "I don’t know about you guys, but I won’t be saying no to a fancy dinner night~!  "
    yu "Why don’t you start trying these suits on to see what matches your style~?"

    show aiden2 confused5 at p4_4
    voice audio.aiden_v_unsure2a
    a "E-Eh… I don’t know if any of this would look right on me…"

    show yuri play2 at p4_2
    voice audio.yuri_v_here1a
    yu "Anything would look good on hunks like you two, for sure~! Here, try this one, Aiden~!"

    hide goro_autumn
    hide goro shy4
    show goro2_autumn at p4_1
    show goro2 bored1 at p4_1
    voice audio.goro_v_annoyed1a1
    g "They’re grown men. You don’t have to dress them like dolls. "

    show yuri worry4 at p4_2
    voice audio.yuri_v_aww1a
    yu "Aww…"

    hide goro2_autumn
    hide goro2 bored1
    show goro_autumn at p4_1
    show goro talk1 at p4_1
    voice audio.goro_v_anyway2
    g "Anyway, we still have to inform the others and bring them their suits."
    g "Our reservation is in thirty minutes. Let’s all meet there."

    show yoshi happy1 at p4_3
    voice audio.yoshi_v_yessir1
    yo "Yes, sir. We’ll get dressed immediately."

    show yuri laugh1 at p4_2
    voice audio.yuri_v_bye2a
    yu "See you guys soon! Can’t wait to see your formal looks~!"

    hide yuri_autumn
    hide yuri laugh1
    hide goro_autumn
    hide goro talk1
    with dissolve

    show yoshi_sleep at left2
    show yoshi happy1 at left2
    show aiden2_sleep at right2
    show aiden2 sigh4 at right2
    with move

    voice audio.aiden_v_relief1a1
    a "Whew… Just when I thought tonight’s gonna be chill…"

    show yoshi excited1 at left2
    voice audio.yoshi_v_excited1
    yo "We’ll get to eat great food though! Aren’t you excited about that?"
    yo "You never know, maybe you’ll get some ideas for a new camp menu!"

    show aiden2 upset5 at right2
    voice audio.aiden_v_think1a1
    a "They’re probably using expensive ingredients, though… I’m much more used to making homey food with cheap stuff…"
    a "And do I really have to dress up like an aristocrat?"

    show yoshi play2 at left2
    voice audio.yoshi_v_laugh3
    yo "Hehe, you never know, the look might fit you~"

    show aiden2 sigh5 at right2
    voice audio.aiden_v_unsure2a
    a "Oh, I dunno… Something about this whole thing is making me low-key anxious…"

    show aiden2 worry5 at right2
    voice audio.aiden_v_hngh1b2
    a "Ughhh… Do we really have to go, Yoshi??"

    $ working = False
    $ shuffle_menu()
    menu():
        a "Ughhh… Do we really have to go, Yoshi??{fast}"
        "We can't just turn it down.":
            $ working = True
            $ score_aiden -= 2
            $ score_top += 1
            show yoshi worry2 at left2
            voice audio.yoshi_v_well1
            yo "It’d be really rude to turn down Mr. Clermont’s generous offer."

            show aiden2 sigh4 at right2
            voice audio.aiden_v_sigh1a
            a "*sigh* You’re right..."

            hide aiden2_sleep
            hide aiden2 sigh4
            hide aiden2 think5
            hide aiden2 comp3
            show aiden_sleep at right2
            show aiden awkward3 at right2
            voice audio.aiden_v_but1a2
            a "You gotta help me with this tie, though. I know how to tie a knot twenty different ways, but I have no clue what to do with this thing."

            show yoshi_sleep at center
            show yoshi play3 at center
            with move

            voice audio.yoshi_v_confident2
            yo "Hehe, here let me do it for you."
        "Everyone else is going.":
            $ working = True
            $ score_aiden -= 1
            $ score_bot += 1
            hide yoshi_sleep
            hide yoshi play2
            show yoshi2_sleep at left2
            show yoshi2 comp6 at left2
            voice audio.yoshi_v_laugh6
            yo "Ahehe… We have to. Everyone’s gonna look for us if we don’t show up."

            show aiden2 sigh4 at right2
            voice audio.aiden_v_sigh1a
            a "*sigh* Alright."

            hide aiden2_sleep
            hide aiden2 sigh4
            hide aiden2 think5
            hide aiden2 comp3
            show aiden_sleep at right2
            show aiden awkward3 at right2
            voice audio.aiden_v_but1a2
            a "You gotta help me with this tie, though. I know how to tie a knot twenty different ways, but I have no clue what to do with this thing."

            show yoshi2_sleep at center
            show yoshi2 play3 at center
            with move

            hide yoshi2_sleep
            hide yoshi2 play3
            show yoshi_sleep at center
            show yoshi play3 at center
            voice audio.yoshi_v_confident2
            yo "Hehe, here let me do it for you."
        "It's a chance to spend time with everyone.":
            $ working = True
            $ score_aiden += 1
            $ score_bot += 1
            show yoshi bold2 at left2
            voice audio.yoshi_v_comp5
            yo "Think of it as a chance to have a nice dinner with everyone!"
            yo "And this time, you don’t have to do any work!"

            show aiden2 think5 at right2
            voice audio.aiden_v_well1a1
            a "Well, if you put it that way…"

            hide aiden2_sleep
            hide aiden2 sigh4
            hide aiden2 think5
            hide aiden2 comp3
            show aiden_sleep at right2
            show aiden awkward3 at right2
            voice audio.aiden_v_but1a2
            a "You gotta help me with this tie, though. I know how to tie a knot twenty different ways, but I have no clue what to do with this thing."

            show yoshi_sleep at center
            show yoshi play3 at center
            with move

            voice audio.yoshi_v_confident2
            yo "Hehe, here let me do it for you."
        "There's nothing to worry about.":
            $ working = True
            $ score_aiden += 2
            $ score_top += 1
            show yoshi comp2 at left2
            voice audio.yoshi_v_comp5
            yo "There’s nothing to worry about, Aiden. "
            yo "Think of it as a fancy date for the two of us!"

            show aiden2 comp3 at right2
            voice audio.aiden_v_laugh1b2
            a "Hehe, if you put it that way…"

            hide aiden2_sleep
            hide aiden2 sigh4
            hide aiden2 think5
            hide aiden2 comp3
            show aiden_sleep at right2
            show aiden awkward3 at right2
            voice audio.aiden_v_but1a2
            a "You gotta help me with this tie, though. I know how to tie a knot twenty different ways, but I have no clue what to do with this thing."

            show yoshi_sleep at center
            show yoshi play3 at center
            with move

            voice audio.yoshi_v_confident2
            yo "Hehe, here let me do it for you."

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

    show yoshi_formal at center
    show yoshi happy1 at center
    voice audio.yoshi_v_rush2
    yo "Over here, Aiden! Come check the place out!"

    show aiden_formal at p5_1
    show aiden awkward2 at p5_1
    with dissolve

    voice audio.aiden_v_yeah1g2
    a "Y-Yeah, I’m coming—"

    show aiden_formal at left2
    show aiden awkward2 at left2
    show yoshi_formal at right2
    show yoshi awkward4 at right2
    with move

    voice audio.yoshi_v_amazed1a
    yo "I should’ve expected this considering the rest of the hotel, but this place is incredible…"

    show aiden awkward3 at left2
    voice audio.aiden_v_whistle1a
    a "No kidding…"
    a "Everywhere you look there’s gold and crystals, it’s almost blinding me. You sure this is a restaurant?"

    show yoshi_formal at right2
    show yoshi confused2 at right2
    voice audio.yoshi_v_think1a
    yo "This is where Yuri told us to go… But I don’t see anyone else yet."

    show aiden upset5 at left2
    voice audio.aiden_v_unsure4a
    a "Being in a place like this is kinda freaking me out, it’s almost suffocating."
    a "That or this necktie is choking me to death!"

    show yoshi_formal at center
    show yoshi talk3 at center
    with move

    show yoshi_formal at center
    show yoshi talk3 at center
    voice audio.yoshi_v_oh1
    yo "Oh, let me loosen that for you."

    show aiden sigh5 at left2
    voice audio.aiden_v_sigh1a
    a "*sigh* This suit isn’t helping either. It’s hugging my body way too tight."
    a "And what’s up with these shoes? I can’t even walk properly in them."

    show yoshi comp3 at center
    voice audio.yoshi_v_comp7
    yo "Relax, Aiden. This is what formal wear is supposed to feel like."
    yo "But don’t worry, you look really handsome in it."

    show aiden comp3 at left2
    voice audio.aiden_v_thanks1c2
    a "Ahehe… Thanks, Yoshi. It suits you way better though."

    show yoshi happy1 at center
    voice audio.yoshi_v_actually1a
    yo "It’s been a long time since I wore something this nice."
    yo "Business suits are one thing, but the last time I was in full formal wear was my prom. "

    show aiden_formal at left2
    show aiden confused2 at left2
    voice audio.aiden_v_aww2b
    a "Prom? I’ve never went to one. Too bad, ’cause I would’ve loved to go with you."

    show yoshi laugh1 at center
    voice audio.yoshi_v_laugh1
    yo "Haha, well it’s not too different from this except with dancing and some extra cringe."
    yo "And I don’t think it’d be nearly as memorable as this."

    show aiden comp2 at left2
    voice audio.aiden_v_unsure1b
    a "Hehe, I guess this could be fun just for tonight... Even though these clothes are stuffy, we do look good together, don’t we?"

    show yoshi happy2 at center
    voice audio.yoshi_v_yeah2
    yo "Yeah, we blend right in!"

    show aiden_formal at p4_1
    show aiden comp2 at p4_1
    show yoshi_formal at p4_2
    show yoshi happy2 at p4_2
    with move

    show goro_formal at p4_4
    show goro norm1 at p4_4
    show yuri_formal at p4_3
    show yuri excited3 at p4_3
    with dissolve

    voice audio.yuri_v_greet2a
    yu "Hiii guuuys!~"

    show goro happy1 at p4_4
    voice audio.goro_v_laugh2a
    g "You’re both here early. You weren’t lying when you said you’ll get dressed quickly."

    show yoshi amazed2 at p4_2
    voice audio.yoshi_v_amazed1c
    yo "Oh wow! You both look amazing!"

    show aiden amazed1 at p4_1
    voice audio.aiden_v_yuri3a
    a "*whistles* Yuri, you look beautiful! I’ve never seen you in a dress before!"

    show yuri comp4 at p4_3
    voice audio.yuri_v_aww2a
    yu "Aww~ Thanks, you guys! "

    show yuri tease2 at p4_3
    voice audio.yuri_v_laugh1a1
    yu "Hihi~ You both look really handsome too! Formal wear might be my new kink~"

    show aiden tease1 at p4_1
    voice audio.aiden_v_laugh1b2
    a "Hehe, good to know you’re still Yuri under there."

    show yoshi comp6 at p4_2
    voice audio.yoshi_v_laugh3
    yo "I figured we’d get at least one or two comments from you."

    show goro sigh1 at p4_4
    voice audio.goro_v_sigh1a
    g "She’s been talking nonstop about how excited she was to see you all dressed up..."

    show yuri play2 at p4_3
    voice audio.yuri_v_sarcastic1b2
    yu "Don’t let him fool you! He was just as excited as me, talking about you both while he was doing my hair and makeup!"

    show yoshi shock2 at p4_2
    voice audio.yoshi_v_what4
    yo "Wh-What? Sir Goro did that?"

    show aiden excited3 at p4_1
    voice audio.aiden_v_amazed2b2
    a "I had no idea those big manly hands could do something so pretty!"

    show goro explain2 at p4_4
    voice audio.goro_v_well1a
    g "Well… If you have a daughter, you have no choice but to learn at some point in your life…"
    g "Besides, Yuri takes too much time getting ready for something like this if I leave her to her own devices."

    show yuri irked1 at p4_3
    voice audio.yuri_v_hey3a
    yu "Hey! You’re just as bad as me! You spent half the time in front of the mirror deciding which tie matched the best!"

    show yoshi bold2 at p4_2
    voice audio.yoshi_v_sir1
    yo "You look great as usual, sir! Formal wear really ‘suits’ you!"

    show aiden sigh4 at p4_1
    voice audio.aiden_v_yoshi5a
    a "That was a seriously bad pun, Yoshi."

    show yuri happy1 at p4_3
    voice audio.yuri_v_actually1a
    yu "It’s actually pretty common for Dad to be in this kind of getup!"

    show goro_formal at p4_4
    show goro explain3 at p4_4
    voice audio.goro_v_ehem1a
    g "*ehem* This is a lot more sophisticated than what I usually wear. I even put on my special cologne for this occasion."

    show yuri confused4 at p4_3
    voice audio.yuri_v_oh1a
    yu "Oh, you mean that one bottle you've had for like a decade? What was it called…? Huge Boss?"

    show aiden tease2 at p4_1
    voice audio.aiden_v_laugh1b2
    a "More like Hung Boss… "

    show goro bored2 at p4_4
    voice audio.goro_v_hmph1a
    g "Excuse me, it’s called Elongated Musk! It’s my most expensive one to date."

    show aiden_formal at p6_1
    show aiden tease2 at p6_1
    show yoshi_formal at p6_2
    show yoshi bold2 at p6_2
    show yuri_formal at p6_3
    show yuri confused2 at p6_3
    show goro_formal at p6_4
    show goro bored2 at p6_4
    with move

    show darius_formal at p6_6
    show darius norm1 at p6_6
    show lloyd_formal at p6_5
    show lloyd talk2 at p6_5
    with dissolve

    voice audio.lloyd_v_shock1a3
    l "Oh! There they are! "
    l "Looks like we’re late for the party, huh?"

    show yoshi happy2 at p6_2
    voice audio.yoshi_v_disagree4a
    yo "Not really! We just got here too!"

    show yuri confused2 at p6_3
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

    show aiden laugh1 at p6_1
    voice audio.aiden_v_laugh2a1
    a "Haha! Why, is it like kid-size or something?"

    show goro confused2 at p6_4
    voice audio.goro_v_confused1a1
    g "It didn’t fit…? I could’ve sworn I’ve gotten your measurements before, right…?"

    show lloyd sigh5 at p6_5
    voice audio.lloyd_v_conj1c3
    l "W-Well, you did… But I didn’t know it was for something to wear! "

    show yoshi confused2 at p6_2
    voice audio.yoshi_v_wait1
    yo "Wait, I’m confused… Why didn’t your suit fit you then?"

    show darius bored2 at p6_6
    voice audio.darius_v_laugh1
    d "He lied to oversell his size."

    show lloyd tired5 at p6_5
    voice audio.lloyd_v_darius6a
    l "Dar… you didn’t have to put it so bluntly…"

    show aiden think2 at p6_1
    voice audio.aiden_v_actually3a
    a "To be fair, I just thought they were for camp records too when we got asked…"

    show lloyd angry2 at p6_5
    voice audio.lloyd_v_groan2a2
    l "Right?! I thought it was for like a physical checkup or something!"

    show goro talk3 at p6_4
    voice audio.goro_v_actually1a
    g "I didn’t know the reason Mr. Clermont asked for our measurements too, but I didn’t question it."

    show yoshi comp3 at p6_2
    voice audio.yoshi_v_well1
    yo "Well, it’s a good thing you had something semi-formal… You still look nice nonetheless! "

    show lloyd sigh1 at p6_5
    voice audio.lloyd_v_sigh2a
    l "*sigh* I look like a dork compared to you guys…"

    show darius comp5 at p6_6
    voice audio.darius_v_cute1
    d "I like your bowtie. It’s cute."

    show goro happy2 at p6_4
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

    show goro_formal at p6_4
    show goro bold2 at p6_4
    with move

    voice audio.goro_v_comp2a1
    g "I have a brooch that’s perfect for the occasion. It’s not much, but it’ll help a little bit."

    show lloyd amazed3 at p6_5
    voice audio.lloyd_v_amazed1a4
    l "Oh wow! Thank you, Sir Goro! "

    show yuri comp2 at p6_3
    voice audio.yuri_v_aww3a
    yu "Aww, look at that~! It kinda looks like a dad sending his son off to prom~"

    show darius laugh3 at p6_6
    voice audio.darius_v_amazed2
    d "It looks good on you, Lloyd."

    show lloyd think2 at p6_5
    voice audio.lloyd_v_unsure1a2
    l "I guess it is better… But I still look like your secretary or something, Dar…"

    show aiden happy3 at p6_1
    voice audio.aiden_v_yeah1a1
    a "Yeah, Darius looks like he’s a mob boss or something! "

    show goro play3 at p6_4
    voice audio.goro_v_heh1a
    g "He does look rather imposing… But in a good way…"

    show yoshi comp2 at p6_2
    voice audio.yoshi_v_unsure1a
    yo "Maybe if you wipe that blank look and smile more you’d be less intimidating?"

    show darius annoy2 at p6_6
    voice audio.darius_v_no1a
    d "No."

    show lloyd happy2 at p6_5
    voice audio.lloyd_v_agree2b1
    l "Try it, Dar! We wanna see! "

    show darius grin3 at p6_6
    d "..."

    show aiden_formal at p6_1
    show aiden comp2 at p6_1
    voice audio.aiden_v_oh4a
    a "Oh… Well… I guess we can work on that one…"

    show yuri bold2 at p6_3
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

    show yoshi think2 at p6_2
    voice audio.yoshi_v_anyway2
    yo "By the way, aren’t we missing someone from your group…?"

    show aiden_formal at p7_1
    show aiden comp2 at p7_1
    show yoshi_formal at p7_2
    show yoshi think2 at p7_2
    show yuri_formal at p7_3
    show yuri bold2 at p7_3
    show goro_formal at p7_4
    show goro play3 at p7_4
    show lloyd_formal2 at p7_5
    show lloyd sigh5 at p7_5
    show darius_formal at p7_6
    show darius laugh3 at p7_6
    with move

    show jin_formal at p7_7
    show jin awkward4 at p7_7
    with dissolve

    voice audio.jin_v_sorry1a2
    j "W-Wahh… I’m here! Sorry I’m late, guys…!"

    show aiden_formal at p7_1
    show aiden shock2 at p7_1
    voice audio.aiden_v_shock1d1
    a "Whoa! Jin you look so… different! "

    show yuri_formal at p7_3
    show yuri amazed3 at p7_3
    voice audio.yyuri_v_kyaa1
    yu "Kyaaa!! Look at you! You look like a pop idol!"
    yu "Who knew that cutie Jin can look as handsome as this?"

    show goro play2 at p7_4
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

    show yuri_formal at p7_3
    show yuri comp2 at p7_3
    voice audio.yuri_v_jin5b
    yu "Aww, are you still feeling nervous, Jin?"

    show jin comp3 at p7_7
    voice audio.jin_v_conj1c1
    j "A little bit, I only came because all of you were here."

    show yoshi comp2 at p7_2
    voice audio.yoshi_v_comp5
    yo "Don’t worry, Jin. I’m sure all of us will have a good time tonight!"

    show jin comp2 at p7_7
    voice audio.jin_v_yeah2a
    j "Yeah… I’d like to be less of a shut-in. Especially when it comes to spending time with you guys."
    j "This is the perfect chance for me to—"

    show aiden_formal at p8_1
    show aiden shock1 at p8_1
    show yoshi_formal at p8_2
    show yoshi shock1 at p8_2
    show yuri_formal at p8_3
    show yuri comp2 at p8_3
    show goro_formal at p8_4
    show goro shock1 at p8_4
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

    show yuri annoy2 at p8_3
    voice audio.yuri_v_ugh3a
    yu "Ugh…"

    show emilia_formal at p8_3
    show emilia bold3 at p8_3
    show yuri_formal at p8_4
    show yuri pout2 at p8_4
    show goro_formal at p8_5
    show goro flat1 at p8_5
    show lloyd_formal2 at p8_6
    show lloyd awkward2 at p8_6
    show darius_formal at p8_7
    show darius disgust1 at p8_7
    show jin_formal at p8_8
    show jin shy3 at p8_8
    with move

    all "..."

    show emilia annoy5 at p8_3
    voice audio.emilia_v_well2
    e "Well?! Not even one compliment? I didn’t put on a lovely dress just to be ignored!"

    show yoshi awkward3 at p8_2
    voice audio.yoshi_v_uh1a
    yo "Y-You look stunning, Emilia…"

    show emilia bold5 at p8_3
    voice audio.emilia_v_laugh3b
    e "*chuckles* I know~"
    e "I was pleasantly surprised to find out Mr. Clermont arranged a fine dining experience for us tonight! Truly such a treat~!"

    show emilia bold2 at p8_3
    voice audio.emilia_v_sigh2b
    e "It’s been a hot minute since my last one! But better late than never!"

    show goro bored2 at p8_5
    voice audio.goro_v_ehem1a
    g "You look wonderful, Ms. Komarova. But is this a different outfit than the one Mr. Clermont provided us?"

    show emilia play2 at p8_3
    voice audio.emilia_v_goro3
    e "You have a good eye for luxury, Mr. Nomoru~ Of course I’ve brought my own attire!"
    e "Dress to impress, after all! I wouldn’t be caught dead wearing a free tacky dress, unlike someone~"

    show yuri angry3 at p8_4
    voice audio.yuri_v_request3a
    yu "Listen here, you—"

    show goro talk2 at p8_5
    voice audio.goro_v_so1a
    g "Would you like me to call for the staff to take your coat and your bag? Just so you’d be more comfortable before our meal."

    show emilia play5 at p8_3
    voice audio.emilia_v_thanks1b
    e "No, thank you! Like they say, beauty is pain~"
    e "The gown? Cucci! The feathers? Verse-ace! The shoes? Louis Butt-on! The jewelry? Stiffany & Ho!"

    show emilia laugh1 at p8_3
    voice audio.emilia_v_amazed1a
    e "All custom made for me!"

    show yuri annoy4 at p8_4
    voice audio.yyuri_v_hmph1a
    yu "For the small price of two kidneys I bet."

    show yoshi_formal at p8_2
    show yoshi irked1 at p8_2
    voice audio.yoshi_v_yuri4
    yo "Hush, Yuri…!"

    show emilia bold1 at p8_3
    voice audio.emilia_v_laugh3a
    e "Teehee~ It’s no surprise anyone would be jealous. I mean… who wouldn’t be over someone like me?"
    e "Now! Where are we supposed to sit? Shouldn’t we be getting served right about now?"

    show emilia rage4 at p8_3
    voice audio.emilia_v_waiter1
    e "WAITER!"

    show aiden_formal at p9_2
    show aiden shock1 at p9_2
    show yoshi_formal at p9_3
    show yoshi irked1 at p9_3
    show emilia_formal at p9_4
    show emilia irked5 at p9_4
    show yuri_formal at p9_5
    show yuri annoy4 at p9_5
    show goro_formal at p9_6
    show goro talk2 at p9_6
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

    show emilia irked2 at p9_4
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
    r "For tonight, we will be serving a three-course meal that includes an appetizer, a main, and a dessert!"

    show reimond happy3 at p9_1
    voice audio.reimond_v_request1a1
    r "Take a look at our menu to see what we have for each course! Feel free to let us know if you have any specific requests and we’ll gladly prepare them for you!"
    r "Meanwhile, please help yourselves to some freshly prepared complimentary snacks and beverages while the party decides on—"

    show emilia bold5 at p9_7
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

    show emilia bold6 at p9_7
    voice audio.emilia_v_laugh3b
    e "First timers, am I right? "

    show reimond talk2 at p9_1
    voice audio.reimond_v_conj4a
    r "In the meantime, I shall relay madam’s order to our chef. I’ll be back soon to take the rest of your orders!"

    hide reimond_waiter
    hide reimond talk2
    with dissolve

    show jin_formal at p8_1
    show jin shy3 at p8_1
    show yuri_formal at p8_2
    show yuri annoy4 at p8_2
    show goro_formal at p8_3
    show goro talk3 at p8_3
    show yoshi_formal at p8_4
    show yoshi irked1 at p8_4
    show aiden_formal at p8_5
    show aiden shock1 at p8_5
    show emilia_formal at p8_6
    show emilia bold6 at p8_6
    show darius_formal at p8_7
    show darius disgust1 at p8_7
    show lloyd_formal2 at p8_8
    show lloyd confused2 at p8_8
    with move

    voice audio.lloyd_v_geez1a2
    l "Gee… Everything in this menu sounds like gibberish to me… even with all the descriptions, I can’t tell how it’ll taste…"

    show jin confuseddn3 at p8_1
    voice audio.jin_v_think2a3
    j "Honestly I can’t even pronounce some of this… Like this booyah…boys?"

    show emilia play3 at p8_6
    voice audio.emilia_v_worry3a
    e "That’s bouillabaisse my dear, it’s a good thing I’m here. If anyone needs help with the menu, I don’t mind educating you~"

    show yuri bold2 at p8_2
    voice audio.yuri_v_oh1b
    yu "Oh, let’s ask Aiden about it! He knows a lot about food!"

    show darius happy1 at p8_7
    voice audio.darius_v_praise1
    d "Ask the chef directly. Good idea."

    show aiden_formal at p8_5
    show aiden awkward2 at p8_5
    voice audio.aiden_v_unsure4a
    a "Ahh… Well… I haven’t really heard of most of these, but I recognize some of them from my dad’s cookbook…"

    show lloyd bold2 at p8_8
    voice audio.lloyd_v_shock1b1
    l "I’d like something fresh! What about foie gras? That sounds greeny!"

    show darius confused2 at p8_7
    voice audio.darius_v_think2b1
    d "I think you read that as grass…"

    show aiden worry2 at p8_5
    voice audio.aiden_v_think2a
    a "Uhh… That’s duck liver, Lloyd… I think…"

    show lloyd pain2 at p8_8
    voice audio.lloyd_v_disgust1b3
    l "Blech! No thanks, then!"

    show aiden awkward3 at p8_5
    voice audio.aiden_v_well1c1
    a "W-Well, you can have some fish for your main if you want something lighter…"

    show lloyd hungry3 at p8_8
    voice audio.lloyd_v_shock1b1
    l "Oh! The seafood menu has a lot of fancy sounding ones! Should I get the ceviche? The quenelle? Or the acqua pazza?"

    show aiden worry2 at p8_5
    voice audio.aiden_v_unsure4a
    a "Uhh… I-I’m not sure what kind of fish is used in any of those…"

    show lloyd think4 at p8_8
    voice audio.lloyd_v_unsure1a3
    l "I guess I’ll just order the longest-spelled one! "
    l "For Dar, which one of these is spicy?"

    show aiden think2 at p8_5
    voice audio.aiden_v_unsure5a1
    a "Maybe try the… uhh… korma?"

    show darius happy1 at p8_7
    voice audio.darius_v_praise1
    d "Sounds good."

    show yuri play2 at p8_2
    voice audio.yuri_v_aiden2d
    yu "Ooh! Aiden, should we get coq au vin? That sounds juicy~"

    show jin play2 at p8_1
    voice audio.jin_v_laugh8a
    j "P-Pfftt… coq…"

    show aiden sigh4 at p8_5
    voice audio.aiden_v_i1b2
    a "I, uh… don’t know what that is…"

    show goro talk2 at p8_3
    voice audio.goro_v_conj8a1
    g "This menu description says it’s chicken cooked in red wine. That should be good enough."

    show lloyd think5 at p8_8
    voice audio.lloyd_v_think1a3
    l "What should we get for the appetizers and dessert then?"

    show jin awkward3 at p8_1
    voice audio.jin_v_sigh2a
    j "I… I feel bad, I really don’t know what to get… even with the descriptions listed…"

    show yuri laugh2 at p8_2
    voice audio.yuri_v_idea2a
    yu "Aiden knows for sure what’s good just by looking at the ingredients!"

    show goro happy1 at p8_3
    voice audio.goro_v_aiden4a
    g "Ah, yes. If you don’t mind, Aiden, can you pick the meal courses for us? I trust your recommendations."

    show aiden worry5 at p8_5
    voice audio.aiden_v_think2a
    a "Uhh… G-Gimme a sec."

    show yoshi_formal at p8_4
    show yoshi think2 at p8_4
    voice audio.yoshi_v_uh1a
    yo "Umm, everyone? Maybe let’s just order something we’re all more familiar with?"

    show aiden comp3 at p8_5
    voice audio.aiden_v_alright3a2
    a "I-It’s alright, Yoshi! I know some of these…! "
    a "This one should be good, you guys…! Everyone likes bacon and cheese, right? Then something fruity for dessert?"

    show goro relief2 at p8_3
    voice audio.goro_v_relief1a
    g "That settles it then."

    show yoshi comp2 at p8_4
    voice audio.yoshi_v_aiden3
    yo "What about you, Aiden? Have you picked one for your main yet? I’ll have whatever you’re having."

    show aiden worry3 at p8_5
    voice audio.aiden_v_oh4a
    a "Oh…! I was just planning to get some porkchops with gravy, you like that too, right?"

    show emilia confused2 at p8_6
    voice audio.emilia_v_question4a
    e "Pardon my intrusion, but I can’t help but overhear your selections… Wouldn’t it be such a wasted opportunity to order something so basic?"
    e "For someone labeled as a chef, you seem to have a simple palette."

    show emilia sigh2 at p8_6
    voice audio.emilia_v_laugh2a
    e "I’m sure chances to experience high-class meals are once in a blue moon for you, so why not try something new for once to elevate yours and everyone’s taste level?"

    show aiden upset1 at p8_5
    a "..."

    show emilia bold2 at p8_6
    voice audio.emilia_v_comp1a
    e "Luckily, I’m in such a good mood today, so I don’t mind offering some suggestions~"
    e "For the main, the superior choice is obviously the slow roasted pork belly~ Flavorful and hearty."

    show yuri annoy4 at p8_2
    voice audio.yuri_v_response2a3
    yu "Sounds more like a heart attack."

    show goro bored1 at p8_3
    voice audio.goro_v_yuri7a
    g "Yuri, behave."

    show emilia bold3 at p8_6
    voice audio.emilia_v_lloyd3
    e "Mr. Sirius, if you prefer seafood with a higher price point, then the choice for you is lobster bisque! Black truffle dal for Mr. Najjar. And saffron chicken paella for everyone else~"
    e "As for the appetizers—"

    show yoshi talk1 at p8_4
    voice audio.yoshi_v_comp1
    yo "It’s alright, Emilia. We’re good with our orders."

    show emilia eyeroll4 at p8_6
    voice audio.emilia_v_hmph1a
    e "Hmph. Suit yourselves, then!"

    show jin_formal at p9_2
    show jin awkward3 at p9_2
    show yuri_formal at p9_3
    show yuri annoy4 at p9_3
    show goro_formal at p9_4
    show goro bored1 at p9_4
    show yoshi_formal at p9_5
    show yoshi talk1 at p9_5
    show aiden_formal at p9_6
    show aiden upset1 at p9_6
    show emilia_formal at p9_7
    show emilia eyeroll4 at p9_7
    show darius_formal at p9_8
    show darius happy1 at p9_8
    show lloyd_formal2 at p9_9
    show lloyd think5 at p9_9
    with move

    show reimond_waiter at p9_1
    show reimond happy1 at p9_1
    with dissolve

    voice audio.reimond_v_greet1a1
    r "Hello, has everyone decided on their orders?"

    show yoshi talk2 at p9_5
    voice audio.yoshi_v_yes1
    yo "Ah, yes! Here they are!"

    show reimond happy2 at p9_1
    voice audio.reimond_v_perfect1a1
    r "Perfect! I’ll relay these to our chef! "

    hide reimond_waiter
    hide reimond happy2
    with dissolve

    show jin_formal at p8_1
    show jin awkward3 at p8_1
    show yuri_formal at p8_2
    show yuri annoy4 at p8_2
    show goro_formal at p8_3
    show goro bored1 at p8_3
    show yoshi_formal at p8_4
    show yoshi talk1 at p8_4
    show aiden_formal at p8_5
    show aiden upset1 at p8_5
    show emilia_formal at p8_6
    show emilia eyeroll4 at p8_6
    show darius_formal at p8_7
    show darius happy1 at p8_7
    show lloyd_formal2 at p8_8
    show lloyd hungry2 at p8_8
    with move

    voice audio.lloyd_v_laugh1a1
    l "Is it just me, or is everyone else really excited too?"

    show jin happy3 at p8_1
    voice audio.jin_v_yes2a
    j "I-I am. I’ve never been to fine dining before…"

    show yuri tease2 at p8_2
    voice audio.yuri_v_laugh1a1
    yu "Hihi~ It’ll be a big leap compared to your instant-noodle diet."

    show jin bold2 at p8_1
    voice audio.jin_v_conj1b3
    j "I was actually curious, so I looked this restaurant up online before I got here… and it’s crazy how the food looked like art on a plate…"

    show darius play2 at p8_7
    voice audio.darius_v_worry1a
    d "Spoiler alert."

    show lloyd hungry4 at p8_8
    voice audio.lloyd_v_amazed1a2
    l "Oh boy! I can’t wait to see what we ordered then!"

    show jin happy4 at p8_1
    voice audio.jin_v_whoa3c
    j "This place also had complete five-out-of-five star positive reviews… "

    show goro shock2 at p8_3
    voice audio.goro_v_amazed1a2
    g "That’s quite a feat considering how expensive the price point here is…"

    show yuri explain4 at p8_2
    voice audio.yuri_v_well1a
    yu "Fancy doesn’t always mean good food! So, we’ll be the judge of that!"
    yu "We have pretty high standards when it comes to taste, all thanks to Aiden’s cooking~"

    show goro laugh3 at p8_3
    voice audio.goro_v_agree8a1
    g "That’s true. What Aiden makes back at camp sure is better than anything I get when I eat out."

    show aiden comp6 at p8_5
    voice audio.aiden_v_laugh1b1
    a "Ahehe… M-Maybe you guys just got too used to my cooking…"

    show yoshi happy2 at p8_4
    voice audio.yoshi_v_actually1a
    yo "For real though, Aiden. We wouldn’t always be looking forward to mealtimes if not for your cooking!"

    show emilia eyeroll3 at p8_6
    voice audio.emilia_v_disagree3a
    e "I beg to differ. A restaurant this high-caliber would definitely deliver more sophistication than just plain pork and beans."

    show yuri annoy2 at p8_2
    voice audio.yuri_v_sarcastic1b2
    yu "You mean the same pork and beans I always see you lick clean off your plate?"

    show emilia angry2 at p8_6
    voice audio.emilia_v_disgust1
    e "Why— There’s no way I’d behave with such disgusting table manners, even more so over commoner’s grub!"

    show lloyd confused2 at p8_8
    voice audio.lloyd_v_sus2a1
    l "I dunnoooo... You’re always the first one to arrive at the mess hall every morning too…"

    show darius bored5 at p8_7
    voice audio.darius_v_agree1a
    d "Can confirm."

    show emilia disgust2 at p8_6
    voice audio.emilia_v_agree1b2
    e "Of course, I have to make sure and be the first one up as the inspector! Don’t twist my actions into something else to fit your narrative."

    show yoshi confused3 at p8_4
    voice audio.yoshi_v_unsure3c
    yo "I guess we’re all trying to say you like Aiden’s cooking too. There’s no shame in admitting that, right…?"

    show jin_formal at p9_2
    show jin happy4 at p9_2
    show yuri_formal at p9_3
    show yuri annoy2 at p9_3
    show goro_formal at p9_4
    show goro laugh3 at p9_4
    show yoshi_formal at p9_5
    show yoshi confused3 at p9_5
    show aiden_formal at p9_6
    show aiden comp6 at p9_6
    show emilia_formal at p9_7
    show emilia angry2 at p9_7
    show darius_formal at p9_8
    show darius bored5 at p9_8
    show lloyd_formal2 at p9_9
    show lloyd confused2 at p9_9
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
    show jin thinkdn1 at p8_1
    show yuri_formal at p8_2
    show yuri annoy2 at p8_2
    show goro_formal at p8_3
    show goro laugh3 at p8_3
    show yoshi_formal at p8_4
    show yoshi confused3 at p8_4
    show aiden_formal at p8_5
    show aiden comp6 at p8_5
    show emilia_formal at p8_6
    show emilia angry2 at p8_6
    show darius_formal at p8_7
    show darius bored5 at p8_7
    show lloyd_formal2 at p8_8
    show lloyd confused2 at p8_8
    with move

    j "..."

    show darius awkward1 at p8_7
    d "..."

    show yuri confused2 at p8_2
    voice audio.yuri_v_what2a
    yu "This is it?!"

    show yoshi shy6 at p8_4
    voice audio.yoshi_v_think1a
    yo "T-The portions are kinda small, aren’t they…?"

    show aiden awkward2 at p8_5
    voice audio.aiden_v_think2a
    a "I swear I thought it was something like pizza…"

    show lloyd confused5 at p8_8
    voice audio.lloyd_v_confused2a2
    l "Uh… What’s going on? Are we being pranked…?"

    show goro_formal at p8_3
    show goro explain2 at p8_3
    voice audio.goro_v_ehem1a
    g "*ehem* Everyone, this is just the—"

    show emilia rage4 at p8_6
    voice audio.emilia_v_annoyed2
    e "Simpletons! These are just the appetizers! They’re supposed to be small!"

    show lloyd hungry1 at p8_8
    voice audio.lloyd_v_shock1a1
    l "Oh, well I’m done eating it. That just made me hungrier."

    show emilia angry5 at p8_6
    voice audio.emilia_v_hmph1a
    e "That’s the point! It’s meant to stimulate your senses, to build up your appetite for the main course! "

    show aiden sad5 at p8_5
    voice audio.aiden_v_hngh1b5
    a "I really thought it’d be bigger than just one-bite."

    show emilia angry3 at p8_6
    voice audio.emilia_v_question2a1
    e "Did you really think they’d serve pizza in a place like this? You really are out of touch!"
    e "And you’re not supposed to shove it down your throat and swallow it like a pill! You’re ruining the experience!"

    show emilia annoy3 at p8_6
    voice audio.emilia_v_request2b
    e "Look at how it’s done! I sliced mine into four equal parts, making sure each part has every ingredient, allowing me to savor each bite!"
    e "If only everyone had listened to my recommendations, then you wouldn’t have missed out~"

    show aiden sad4 at p8_5
    voice audio.aiden_v_sorry1c1
    a "S-Sorry, guys... I guess I made a mistake with the order."

    show yoshi comp2 at p8_4
    voice audio.yoshi_v_comp1
    yo "It’s fine, Aiden. This is a new experience for all of us."

    show jin_formal at p9_2
    show jin thinkdn1 at p9_2
    show yuri_formal at p9_3
    show yuri confused2 at p9_3
    show goro_formal at p9_4
    show goro explain2 at p9_4
    show yoshi_formal at p9_5
    show yoshi comp2 at p9_5
    show aiden_formal at p9_6
    show aiden sad4 at p9_6
    show emilia_formal at p9_7
    show emilia annoy3 at p9_7
    show darius_formal at p9_8
    show darius awkward1 at p9_8
    show lloyd_formal2 at p9_9
    show lloyd hungry1 at p9_9
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
    show fx5a 1 at fx_pos
    with dissolve
    voice audio.lloyd_vsa13_line1
    l "Now we’re talking! My mouth is watering from just looking at it!"

    voice audio.yuri_vsa13_line1
    yu "KYAA~! Talk about the plating and presentation!"

    voice audio.jin_vsa13_line1
    j "I wish I’d brought my camera to take a picture of this…"

    voice audio.goro_vsa13_line1
    g "We’ll let’s see if it tastes as good as it looks."

    voice audio.yoshi_vsa13_line1
    yo "Mmm… It’s delicious! It’s almost as good as yours, Aiden!"

    voice audio.aiden_vsa13_line1
    a "Oh… This is way better, though."

    voice audio.darius_vsa13_line1
    d "Melts in my mouth."

    voice audio.lloyd_vsa13_line2
    l "You should recreate this sometime, Aiden!"

    voice audio.yuri_vsa13_line2
    yu "That’s a great idea! It’d be nice to have our own fancy dining experience back at camp every now and then!"

    voice audio.darius_vsa13_line2
    d "I’d like that."

    show fx5a 2 at fx_pos with Dissolve(0.25)
    voice audio.aiden_vsa13_line2
    a "Uhh… I don’t think I could even if I tried… I can’t even figure out what they used to make these flavors."

    voice audio.yoshi_vsa13_line2
    yo "The taste does seem kind of complex, huh? It’s a totally different style from yours."

    voice audio.yuri_vsa13_line3
    yu "Oh, I’m sure Aiden can do it! He’s made everything from burgers to steaks!"

    voice audio.emilia_vsa13_line1
    e "Not with those horrible table manners, he can’t."

    show fx5a 3 at fx_pos with Dissolve(0.25)
    voice audio.emilia_vsa13_line2
    e "I mean… He’s using his dessert spoon for the main course, his elbows are on the table, and I can hear his chewing from over here! "

    voice audio.yuri_vsa13_line4
    yu "What does that have to do with anything?"

    voice audio.jin_vsa13_line2
    j "I thought we were talking about cooking… "

    voice audio.emilia_vsa13_line3
    e "It’s unrealistic to expect a homecook to replicate a dish like this if he’s not even aware of basic dining etiquette."

    voice audio.emilia_vsa13_line4
    e "Professionals have spent years in culinary school studying and mastering the craft."

    voice audio.goro_vsa13_line2
    g "I wouldn’t say that Aiden doesn’t have the experience – he’s been the chef at Camp Buddy for years now."

    voice audio.goro_vsa13_line3
    g "Not only that, but he comes from a family of excellent cooks as well."

    show fx5a 4 at fx_pos with Dissolve(0.25)
    voice audio.aiden_vsa13_line3
    a "W-We do know how to cook, but it’s definitely not anything like this…"

    voice audio.emilia_vsa13_line5
    e "See? He said it himself."

    voice audio.emilia_vsa13_line6
    e "It’s honestly quite a stretch to claim that bloodline has anything to do with technical skills like culinary arts."

    show fx5a 5 at fx_pos with Dissolve(0.25)
    voice audio.yuri_vsa13_line5
    yu "Aren’t you the one who always brags about your family background when it has nothing to do with your skills whatsoever?"

    voice audio.yuri_vsa13_line6
    yu "I bet you can’t even fry an egg."

    show fx5a 6 at fx_pos with Dissolve(0.25)
    voice audio.aiden_vsa13_line4
    a "C-Can’t we just enjoy the meal…? "

    show fx5a 7 at fx_pos with Dissolve(0.25)
    voice audio.emilia_vsa13_line7
    e "No, no. Let’s talk about it, since she’s questioning my abilities."

    voice audio.emilia_vsa13_line8
    e "I think I’ve proven how skilled I am over the last few months with actual results."

    voice audio.emilia_vsa13_line9
    e "Without me, your whole project wouldn’t have gotten this far, and we wouldn’t be sitting here enjoying this lovely dinner."

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

    $ renpy.music.stop(channel='music', fadeout = 2.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 2.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 2.0)
    $ renpy.pause (2.0, hard=True)
    hide cg fade2
    hide fx5a 10
    with dissolve

    play music heracleum_b loop
    show jin worry1 at p8_1
    show yuri annoy1 at p8_2
    show goro angry1 at p8_3
    hide yoshi_formal
    hide yoshi norm1
    show yoshi_formal at p8_4
    show yoshi angry1 at p8_4
    show aiden scared3 at p8_5
    show emilia rage4 at p8_6
    show darius worry1 at p8_7
    show lloyd awkward2 at p8_8
    voice audio.emilia_vsa13_line12
    e "It’s awfully convenient for all of you to point at me for your own shortcomings, isn’t it?"

    voice audio.emilia_vsa13_line13
    e "What about Mr. Scoutmaster Chef here who lacks any sort of professionalism?!"

    show emilia rage5 at p8_6
    voice audio.emilia_vsa13_line14
    e "You all let him get away with basically anything as if he wasn’t carrying the camp’s reputation with him!"

    voice audio.emilia_vsa13_line15
    e "Why, even here at an all-expense paid luxury resort, he lacks the dignity to not cause a commotion!"

    show emilia rage6 at p8_6
    voice audio.emilia_vsa13_line16
    e "He humiliated your beloved camp, putting the sponsorship at risk, by getting drunk and once again flaunting his obscenity in a public place!"

    voice audio.emilia_vsa13_line17
    e "Not only that, but he has zero credentials and no formal training whatsoever to be in a position of leadership!"

    show emilia rage1 at p8_6
    voice audio.emilia_vsa13_line18
    e "It’s really absurd that you all continue to humor this beggar and claim that he’s of such great value!"

    show yoshi rage1 at p8_4
    voice audio.yoshi_vsa13_line4
    yo "What did you just call him?!"

    voice audio.yoshi_vsa13_line5
    yo "This is where I really draw the line, Emilia!"

    show yoshi angry3 at p8_4
    voice audio.yoshi_vsa13_line6
    yo "Why do you keep trying to bring Aiden down?!"

    show aiden scared2 at p8_5
    voice audio.aiden_vsa13_line5
    a "Y-Yoshi, don’t—"

    show yoshi angry2 at p8_4
    voice audio.yoshi_vsa13_line7
    yo "When are you going to accept that he’s just as good a scoutmaster as the rest of us?!"

    voice audio.yoshi_vsa13_line8
    yo "There’s no way I’m going to let you trash him when you refuse to acknowledge the fact that he works the hardest out of everyone here!"

    show emilia rage4 at p8_6
    voice audio.emilia_vsa13_line19
    e "You won’t even consider the facts I’m stating! You’re just proving my point about how you ALWAYS cover for him! "

    voice audio.emilia_vsa13_line20
    e "If you want to keep feeding him false hope, then by all means! Let him live with all your pathetic lies!"

    show emilia eyeroll6 at p8_6
    voice audio.emilia_vsa13_line21
    e "No wonder he sticks around you so much, all you ever do is make him believe he belongs somewhere he never deserved to be!"

    show yoshi rage1 at p8_4
    voice audio.yoshi_vsa13_line9
    yo "Shut the hell up, Emilia! You know nothing about Aiden!"

    voice audio.yoshi_vsa13_line10
    yo "I won’t let you keep disrespecting him like this!"

    show yoshi rage3 at p8_4
    voice audio.yoshi_vsa13_line11
    yo "Take a good look at yourself and tell me who’s actually incompetent here!"

    show emilia scared4 at p8_6
    voice audio.emilia_vsa13_line22
    e "*gasp* "

    $ renpy.music.stop(channel='music', fadeout = 2.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 2.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 2.0)
    show jin scared1 at p8_1
    show yuri shock1 at p8_2
    show goro shock1 at p8_3
    show yoshi angry1 at p8_4
    show aiden scared1 at p8_5
    show emilia rage2 at p8_6
    show darius annoy1 at p8_7
    show lloyd scared1 at p8_8
    all "..."

    show yoshi scared2 at p8_4
    yo "{i}(Crap… I got carried away and let my anger get the best of me with Emilia…){/i}"
    yo "{i}(All that did was make Aiden extremely anxious… I can almost feel him shaking nervously from my seat…){/i}"

    $ working = False
    $ shuffle_menu()
    menu():
        yo "{i}(All that did was make Aiden extremely anxious… I can almost feel him shaking nervously from my seat…){/i}{fast}"
        "Stay silent.":
            $ working = True
            $ score_aiden += 1
            $ score_top += 1
            show yoshi sad2 at p8_4
            yo "{i}(I’d better just stay quiet… I don’t want to make this any worse…){/i}"
            yo "..."

            show goro talk1 at p8_3
            voice audio.goro_v_reimond1a
            g "Waiter!"

            show jin_formal at p9_2
            show jin scared1 at p9_2
            show yuri_formal at p9_3
            show yuri shock1 at p9_3
            show goro_formal at p9_4
            show goro shock1 at p9_4
            show yoshi_formal at p9_5
            show yoshi sad2 at p9_5
            show aiden_formal at p9_6
            show aiden scared1 at p9_6
            show emilia_formal at p9_7
            show emilia rage2 at p9_7
            show darius_formal at p9_8
            show darius annoy1 at p9_8
            show lloyd_formal2 at p9_9
            show lloyd panic1 at p9_9
            with move

            show reimond_waiter at p9_1
            show reimond confused2 at p9_1
            with dissolve

            voice audio.reimond_v_worry2a
            r "Is everything okay over here, sir? "

            show goro talk3 at p9_4
            voice audio.goro_v_agree1a1
            g "Yes. Could you please get us wine for the table?"

            show reimond talk3 at p9_1
            voice audio.reimond_v_agree1a1
            r "Of course, sir! Which would you prefer, red, white, or sparkling?"

            show goro explain2 at p9_4
            voice audio.goro_v_think1a1
            g "Red would be excellent. Give us the best one."

            show reimond happy1 at p9_1
            voice audio.reimond_v_greatchoice1b1
            r "Good choice, sir! I’ll be back in just a moment!"

            hide reimond_waiter
            hide reimond happy1
            with dissolve

            show jin_formal at p8_1
            show jin scared1 at p8_1
            show yuri_formal at p8_2
            show yuri shock1 at p8_2
            show goro_formal at p8_3
            show goro shock1 at p8_3
            show yoshi_formal at p8_4
            show yoshi sad2 at p8_4
            show aiden_formal at p8_5
            show aiden scared1 at p8_5
            show emilia_formal at p8_6
            show emilia rage2 at p8_6
            show darius_formal at p8_7
            show darius annoy1 at p8_7
            show lloyd_formal2 at p8_8
            show lloyd panic1 at p8_8
            with move

            yo "{i}(It looks like Sir Goro’s trying to defuse the situation…){/i}"
        "Apologize.":
            $ working = True
            $ score_aiden -= 2
            $ score_bot += 1
            show yoshi angry5 at p8_4
            voice audio.yoshi_v_ehem1b
            yo "*ehem* I-I suppose I took that too far... I apologize, everyone."

            show emilia rage4 at p8_6
            voice audio.emilia_v_angry1b
            e "As well you should! I can’t believe you—"

            show goro talk1 at p8_3
            voice audio.goro_v_reimond1a
            g "Waiter!"

            show jin_formal at p9_2
            show jin scared1 at p9_2
            show yuri_formal at p9_3
            show yuri shock1 at p9_3
            show goro_formal at p9_4
            show goro shock1 at p9_4
            show yoshi_formal at p9_5
            show yoshi sad2 at p9_5
            show aiden_formal at p9_6
            show aiden scared1 at p9_6
            show emilia_formal at p9_7
            show emilia rage2 at p9_7
            show darius_formal at p9_8
            show darius annoy1 at p9_8
            show lloyd_formal2 at p9_9
            show lloyd panic1 at p9_9
            with move

            show reimond_waiter at p9_1
            show reimond confused2 at p9_1
            with dissolve

            voice audio.reimond_v_worry2a
            r "Is everything okay over here, sir? "

            show goro talk3 at p9_4
            voice audio.goro_v_agree1a1
            g "Yes. Could you please get us wine for the table?"

            show reimond talk3 at p9_1
            voice audio.reimond_v_agree1a1
            r "Of course, sir! Which would you prefer, red, white, or sparkling?"

            show goro explain2 at p9_4
            voice audio.goro_v_think1a1
            g "Red would be excellent. Give us the best one."

            show reimond happy1 at p9_1
            voice audio.reimond_v_greatchoice1b1
            r "Good choice, sir! I’ll be back in just a moment!"

            hide reimond_waiter
            hide reimond happy1
            with dissolve

            show jin_formal at p8_1
            show jin scared1 at p8_1
            show yuri_formal at p8_2
            show yuri shock1 at p8_2
            show goro_formal at p8_3
            show goro shock1 at p8_3
            show yoshi_formal at p8_4
            show yoshi sad2 at p8_4
            show aiden_formal at p8_5
            show aiden scared1 at p8_5
            show emilia_formal at p8_6
            show emilia rage2 at p8_6
            show darius_formal at p8_7
            show darius annoy1 at p8_7
            show lloyd_formal2 at p8_8
            show lloyd panic1 at p8_8
            with move

            yo "{i}(It looks like Sir Goro’s trying to defuse the situation…){/i}"
        "Take Aiden away.":
            $ working = True
            $ score_aiden -= 1
            $ score_top += 1
            show yoshi angry2 at p8_4
            voice audio.yoshi_v_aiden4
            yo "Aiden, come with me. Let’s go back to our room for the night."

            show aiden worry5 at p8_5
            voice audio.aiden_v_yoshi6a
            a "W-We don’t have to do that, Yoshi! Let’s just get a drink to calm everyone down."

            show yoshi worry2 at p8_4
            voice audio.yoshi_v_alright3
            yo "Alright, if you’re sure…"

            show yoshi angry5 at p8_4
            voice audio.yoshi_v_greet2a1
            yo "Excuse me, waiter?"

            show jin_formal at p9_2
            show jin scared1 at p9_2
            show yuri_formal at p9_3
            show yuri shock1 at p9_3
            show goro_formal at p9_4
            show goro shock1 at p9_4
            show yoshi_formal at p9_5
            show yoshi angry5 at p9_5
            show aiden_formal at p9_6
            show aiden worry5 at p9_6
            show emilia_formal at p9_7
            show emilia rage2 at p9_7
            show darius_formal at p9_8
            show darius annoy1 at p9_8
            show lloyd_formal2 at p9_9
            show lloyd panic1 at p9_9
            with move

            show reimond_waiter at p9_1
            show reimond confused2 at p9_1
            with dissolve

            voice audio.reimond_v_worry2a
            r "Yes, sir? Is everything alright?"

            show yoshi talk1 at p9_5
            voice audio.yoshi_v_yes9
            yo "Y-Yes, of course… We’d just like to order a bottle of wine!"

            show reimond talk1 at p9_1
            voice audio.reimond_v_agree5a1
            r "Of course, sir! Which would you prefer, red, white, or sparkling?"

            show yoshi awkward4 at p9_5
            voice audio.yoshi_v_ah3
            yo "A-Ah, well…"

            show goro explain2 at p9_4
            voice audio.goro_v_think1a1
            g "Red would be excellent. Give us the best one."

            show reimond happy1 at p9_1
            voice audio.reimond_v_greatchoice1b1
            r "Good choice, sir! I’ll be back in just a moment!"

            hide reimond_waiter
            hide reimond happy1
            with dissolve

            show jin_formal at p8_1
            show jin scared1 at p8_1
            show yuri_formal at p8_2
            show yuri shock1 at p8_2
            show goro_formal at p8_3
            show goro explain2 at p8_3
            show yoshi_formal at p8_4
            show yoshi awkward4 at p8_4
            show aiden_formal at p8_5
            show aiden worry5 at p8_5
            show emilia_formal at p8_6
            show emilia rage2 at p8_6
            show darius_formal at p8_7
            show darius annoy1 at p8_7
            show lloyd_formal2 at p8_8
            show lloyd panic1 at p8_8
            with move

            yo "{i}(Thank goodness Sir Goro stepped in to help… I just wanted a distraction from that situation…){/i}"
        "Call for distraction.":
            $ working = True
            $ score_aiden += 2
            $ score_bot += 1
            show yoshi angry5 at p8_4
            voice audio.yoshi_v_ehem1b
            yo "*ehem* Waiter!"

            show jin_formal at p9_2
            show jin scared1 at p9_2
            show yuri_formal at p9_3
            show yuri shock1 at p9_3
            show goro_formal at p9_4
            show goro shock1 at p9_4
            show yoshi_formal at p9_5
            show yoshi angry5 at p9_5
            show aiden_formal at p9_6
            show aiden worry5 at p9_6
            show emilia_formal at p9_7
            show emilia rage2 at p9_7
            show darius_formal at p9_8
            show darius annoy1 at p9_8
            show lloyd_formal2 at p9_9
            show lloyd panic1 at p9_9
            with move

            show reimond_waiter at p9_1
            show reimond confused2 at p9_1
            with dissolve

            voice audio.reimond_v_worry2a
            r "Yes, sir? Is everything alright?"

            show yoshi talk1 at p9_5
            voice audio.yoshi_v_yes9
            yo "Y-Yes, of course… We’d just like to order a bottle of wine!"

            show reimond talk1 at p9_1
            voice audio.reimond_v_agree5a1
            r "Of course, sir! Which would you prefer, red, white, or sparkling?"

            show yoshi awkward4 at p9_5
            voice audio.yoshi_v_ah3
            yo "A-Ah, well…"

            show goro explain2 at p9_4
            voice audio.goro_v_think1a1
            g "Red would be excellent. Give us the best one."

            show reimond happy1 at p9_1
            voice audio.reimond_v_greatchoice1b1
            r "Good choice, sir! I’ll be back in just a moment!"

            hide reimond_waiter
            hide reimond happy1
            with dissolve

            show jin_formal at p8_1
            show jin scared1 at p8_1
            show yuri_formal at p8_2
            show yuri shock1 at p8_2
            show goro_formal at p8_3
            show goro explain2 at p8_3
            show yoshi_formal at p8_4
            show yoshi awkward4 at p8_4
            show aiden_formal at p8_5
            show aiden worry5 at p8_5
            show emilia_formal at p8_6
            show emilia rage2 at p8_6
            show darius_formal at p8_7
            show darius annoy1 at p8_7
            show lloyd_formal2 at p8_8
            show lloyd panic1 at p8_8
            with move

            yo "{i}(Thank goodness Sir Goro stepped in to help… I just wanted a distraction from that situation…){/i}"

    show yoshi worry1 at p8_4
    yo "{i}(This is so awkward… Everyone’s extra tense from that argument…){/i}"
    yo "{i}(I’m afraid that Aiden must be blaming himself for this…){/i}"

    show jin_formal at p9_2
    show jin scared1 at p9_2
    show yuri_formal at p9_3
    show yuri shock1 at p9_3
    show goro_formal at p9_4
    show goro shock1 at p9_4
    show yoshi_formal at p9_5
    show yoshi worry1 at p9_5
    show aiden_formal at p9_6
    show aiden worry5 at p9_6
    show emilia_formal at p9_7
    show emilia rage2 at p9_7
    show darius_formal at p9_8
    show darius annoy1 at p9_8
    show lloyd_formal2 at p9_9
    show lloyd panic1 at p9_9
    with move

    show reimond_waiter at p9_1
    show reimond happy1 at p9_1
    with dissolve

    voice audio.reimond_v_here1a
    r "Here you are, a vintage Cabernet Sauvignon! Allow me to serve the party—"

    show goro talk1 at p9_4
    voice audio.goro_v_thanks1a1
    g "Thanks, but that won’t be necessary. We’ll pour it ourselves."

    show reimond happy3 at p9_1
    voice audio.reimond_v_callme1b
    r "Of course. Call me if you need anything else."

    hide reimond_waiter
    hide reimond happy3
    with dissolve

    show jin_formal at p8_1
    show jin scared1 at p8_1
    show yuri_formal at p8_2
    show yuri shock1 at p8_2
    show goro_formal at p8_3
    show goro talk1 at p8_3
    show yoshi_formal at p8_4
    show yoshi talk2 at p8_4
    show aiden_formal at p8_5
    show aiden worry5 at p8_5
    show emilia_formal at p8_6
    show emilia rage2 at p8_6
    show darius_formal at p8_7
    show darius annoy1 at p8_7
    show lloyd_formal2 at p8_8
    show lloyd panic1 at p8_8
    with move

    voice audio.yoshi_v_confident2
    yo "Here, Aiden. Why don’t I pour you some wine?"

    show aiden worry2 at p8_5
    voice audio.aiden_v_alright3a2
    a "I-It’s alright, Yoshi…! I can do it…!"

    show yoshi worry2 at p8_4
    voice audio.yoshi_v_comp2
    yo "It’s okay, Aiden. Just hand me your glass!"

    show aiden worry3 at p8_5
    voice audio.aiden_v_hngh1b5
    a "N-No, it’s really okay, let me—"

    play sound sfx_winespill
    hide aiden_formal
    hide aiden panic5
    show aiden_formal2 at p8_5
    show aiden panic5 at p8_5
    voice audio.aiden_v_shock5b
    a "G-Gah!" with vpunch

    show yoshi awkward4 at p8_4
    voice audio.yoshi_v_aiden6
    yo "A-Aiden….!"

    play music heracleum_musicbox_a loop
    show emilia evil5 at p8_6
    voice audio.emilia_v_laugh3b
    e "Oh dear, and it’s all over that fine suit of yours – no, wait, that belongs to Mr. Clermont, doesn’t it?"

    show aiden panic5 at p8_5
    voice audio.aiden_v_alright3a1
    a "I-It’s alright, I can just wipe it up with my napkin and—"

    play sound sfx_forkclatter
    play bgsound2 sfxloop_crowd loop
    show aiden pain1 at p8_5
    voice audio.aiden_v_swear1a
    a "S-Shit, hold on, let me get that—" with vpunch

    show yoshi worry5 at p8_4
    voice audio.yoshi_v_comp2
    yo "I-It’s alright, Aiden! Calm down."

    show jin scared2 at p8_1
    voice audio.jin_v_ah3a
    j "A-Ah, people are starting to stare…"

    show aiden_formal2 at p8_1
    show aiden pain1 at p8_1
    show jin_formal at p8_2
    show jin scared1 at p8_2
    show yuri_formal at p8_3
    show yuri shock1 at p8_3
    show goro_formal at p8_4
    show goro talk1 at p8_4
    show yoshi_formal at p8_5
    show yoshi worry5 at p8_5
    show emilia_formal at p8_6
    show emilia rage2 at p8_6
    show darius_formal at p8_7
    show darius annoy1 at p8_7
    show lloyd_formal2 at p8_8
    show lloyd panic1 at p8_8
    with move

    voice audio.aiden_v_i1b2
    a "I-I’ll just go clean up…! B-Be right back…!"

    show jin_formal at p9_3
    show jin scared1 at p9_3
    show yuri_formal at p9_4
    show yuri shock1 at p9_4
    show goro_formal at p9_5
    show goro talk1 at p9_5
    show yoshi_formal at p9_6
    show yoshi worry5 at p9_6
    show aiden_formal2 at p9_2
    show aiden worry5 at p9_2
    show emilia_formal at p9_7
    show emilia evil5 at p9_7
    show darius_formal at p9_8
    show darius annoy1 at p9_8
    show lloyd_formal2 at p9_9
    show lloyd panic1 at p9_9
    with move

    show reimond_waiter at p9_1
    show reimond sad3 at p9_1
    with dissolve

    voice audio.reimond_v_ah1b
    r "I heard a commotion, is everything—"

    play sound sfx_crash
    show cg_fade at truecenter
    show fxa5 at fx_pos
    voice audio.reimond_v_woah1a
    r "Whoa!" with vpunch

    voice audio.aiden_vsa13_2_line1
    a "G-Gah…! I-I’m so sorry!"

    voice audio.aiden_vsa13_2_line2
    a "I-I have to go…!"

    hide reimond_waiter
    hide reimond sad3
    show reimond_waiter at p9_1
    show reimond sad3 at p9_1
    hide cg_fade
    hide fxa5
    with dissolve

    hide aiden_formal2
    hide aiden worry5
    with moveoutleft

    show yoshi shock3 at p9_6
    voice audio.yoshi_v_wait3a
    yo "A-Aiden! Wait!"

    hide yoshi_formal
    hide yoshi shock3
    with moveoutleft

    show reimond_waiter at p7_1
    #jey
    show reimond sad3 at p7_1
    show goro_formal at p7_2
    show goro worry3 at p7_2
    show jin_formal at p7_3
    show jin scared1 at p7_3
    show yuri_formal at p7_4
    show yuri shock1 at p7_4
    show emilia_formal at p7_5
    show emilia evil5 at p7_5
    show darius_formal at p7_6
    show darius annoy1 at p7_6
    show lloyd_formal2 at p7_7
    show lloyd panic1 at p7_7
    with move

    voice audio.goro_v_sorry2a2
    g "I’m sorry about that. Let me help you out. "

    show reimond comp1 at p7_1
    voice audio.reimond_v_gratitude1d2
    r "I-It’s quite alright and thank you."

    show emilia evil3 at p7_5
    voice audio.emilia_v_well2
    e "*sips* Well, that’s something you don’t see every day~"

    show yuri angry1 at p7_4
    voice audio.yuri_v_angry3a
    yu "Grr…"

    show lloyd worry2 at p7_7
    voice audio.lloyd_v_worry1c
    l "Are Aiden and Yoshi alright…? Should we go after them…?"

    show darius explain1 at p7_6
    voice audio.darius_v_comp3a
    d "They’ll be fine. Aiden just got overwhelmed."

    show jin panic3 at p7_3
    voice audio.jin_v_worry1b3
    j "I’m getting anxious… People are whispering and staring at us…"

    show emilia angry2 at p7_5
    voice audio.emilia_v_angry1a
    e "Well, maybe all of you shouldn’t have been so rude, then none of this would’ve happened."

    show yuri rage1 at p7_4
    voice audio.yuri_v_what5a
    yu "ALL OF US?! You’re the only one who’s been rude this whole time!!" with vpunch
    yu "You’re rotten to the core just like you were back then!"

    show yuri rage4 at p7_4
    voice audio.yuri_v_angry1a1
    yu "Step off that putrid high horse and get away from Camp Buddy already!"
    yu "You don’t belong with us, and you never will!"

    show emilia scared2 at p7_5
    e "...!"

    show goro rage1 at p7_2
    voice audio.goro_v_scold2a2
    g "That’s enough!" with vpunch

    show emilia panic6 at p7_5
    voice audio.emilia_v_question1c
    e "W-Why, I can’t believe you’re letting her humiliate me like this ag—"

    show goro angry3 at p7_2
    voice audio.goro_v_scold3a
    g "I said enough. We don’t need to hear anything else, especially from you Ms. Komarova."
    g "This dinner is over. All of you, back to your rooms."

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
    $quick_menu = True
    scene bg_hotel_room1_night_lightsout with fade

    play sound sfx_cardbeep
    $ renpy.pause (1.0, hard=True)
    play sound sfx_dooropen
    show yoshi_formal at center
    show yoshi worry4 at center
    with dissolve

    voice audio.yoshi_vsa14_line1
    yo "Aiden—"

    voice audio.yoshi_vsa14_line2
    yo "…I’m sure I saw him come in here."

    play sound sfx_washclothes
    show yoshi shock1 at center
    yo "...!"

    show yoshi_formal at left
    show yoshi shock1 at left
    with move

    show yoshi sad4 at left
    voice audio.yoshi_vsa14_line3
    yo "A-Are you in there, Aiden…?"

    play bgsound sfxloop_waterflow loop
    show cg fade at truecenter
    show fxa6 1 at fx_pos
    with dissolve

    voice audio.aiden_vsa14_line1
    a "Y-Yeah, Yoshi…!"

    voice audio.yoshi_vsa14_line4
    yo "Are you alright in there? You didn’t get hurt from that fall, did you?"

    voice audio.aiden_vsa14_line2
    a "I-I’m fine…! I’m just washing the stain off this suit…!"

    voice audio.yoshi_vsa14_line5
    yo "Oh…"

    show fxa6 2 with Dissolve(0.25)
    voice audio.aiden_vsa14_line3
    a "Y-You should go back to everyone… They’re waiting for you back there."

    voice audio.yoshi_vsa14_line6
    yo "But I need to know for sure you’re alright…"

    voice audio.aiden_vsa14_line4
    a "I’m totally alright, Yoshi…!"

    show fxa6 3 with Dissolve(0.25)
    voice audio.aiden_vsa14_line5
    a "I-I really don’t wanna ruin this suit… I don’t have the money to pay for something like this…"

    voice audio.yoshi_vsa14_line7
    yo "T-That’s not really important, Aiden… I’m sure Mr. Clermont won’t mind."

    voice audio.yoshi_vsa14_line8
    yo "And it’s not too late to go back to everyone, they’ll understand for sure."

    voice audio.aiden_vsa14_line6
    a "I-I’d really rather stay here, Yoshi… It’s really not a big deal, and I don’t want everyone to worry…"

    $ working = False
    $ shuffle_menu()
    menu():
        a "I-I’d really rather stay here, Yoshi… It’s really not a big deal, and I don’t want everyone to worry…{fast}"
        "I won't go without you.":
            $ working = True
            $ score_aiden -= 1
            $ score_bot += 1
            show fxa6 4a with Dissolve(0.25)
            voice audio.yoshi_vsa14_line9a
            yo "I won’t go without you."

            voice audio.aiden_vsa14_line7a
            a "Khh…"

            voice audio.yoshi_vsa14_line10a
            yo "Aiden, please…"

            show fxa6 4c with Dissolve(0.25)
            a "..."

            voice audio.yoshi_vsa14_line11a
            yo "Can we at least talk…?"
        "Open the door.":
            $ working = True
            $ score_aiden -= 1
            $ score_top += 1
            show fxa6 4a with Dissolve(0.25)
            voice audio.yoshi_vsa14_line9b
            yo "Just open the door, Aiden."

            voice audio.aiden_vsa14_line7b
            a "Kkh…!!"
        "I'm staying here.":
            $ working = True
            $ score_aiden += 1
            $ score_bot += 1
            show fxa6 4c with Dissolve(0.25)
            voice audio.yoshi_vsa14_line9c
            yo "I’m staying here with you."

            voice audio.aiden_vsa14_line7a
            a "Khh…"

            voice audio.yoshi_vsa14_line10c
            yo "Aiden, please…"
        "But you're not okay.":
            $ working = True
            $ score_aiden += 1
            $ score_top += 1
            show fxa6 4c with Dissolve(0.25)
            voice audio.yoshi_vsa14_line9d
            yo "You’re not okay, Aiden."

            voice audio.yoshi_vsa14_line10d
            yo "I’m worried about you more than everyone else."
            a "..."

    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    hide cg fade
    hide fxa6 4c
    hide fxa6 4a
    with dissolve

    play sound sfx_dooropen
    show yoshi_formal at right2
    show yoshi sad2 at right2
    with move

    show aiden_formal3 at left2
    show aiden upset4 at left2
    with dissolve

    a "..."

    show yoshi sad2 at right2
    voice audio.yoshi_vsa14_line12
    yo "Aiden…"

    scene cga5 1 with fade
    play music buddy_oath_aiden_sad loop
    a "..."
    yo "{i}(For all the time I’ve known Aiden, I’ve never seen him get into his head this badly…){/i}"
    yo "{i}(He can’t stop fidgeting, and I can see him breaking into a cold sweat…){/i}"

    show cga5 2 with Dissolve(0.25)
    voice audio.yoshi_vsa14_line13
    yo "Aiden, tell me what’s on your mind…"

    voice audio.aiden_vsa14_line8
    a "I… I don’t want to be here anymore, Yoshi…"

    voice audio.aiden_vsa14_line9
    a "It’s been so hard to pretend that I’m comfortable with everything, when I know I don’t really belong in a place like this…"

    show cga5 3 with Dissolve(0.25)
    voice audio.aiden_vsa14_line10
    a "I just… want to go home…"

    voice audio.yoshi_vsa14_line14
    yo "Today’s our last night here, Aiden… Just hold on for a little longer…"

    voice audio.yoshi_vsa14_line15
    yo "Everything will go back to the way it was once we get back to camp tomorrow…"

    voice audio.aiden_vsa14_line11
    a "I know, but… I just can’t help but feel guilty the whole time we were here…"

    voice audio.aiden_vsa14_line12
    a "You were doing everything you could to watch out for me ’cause I had trouble keeping up."

    voice audio.aiden_vsa14_line13
    a "It’s almost as if I’ve been dragging you down and keeping you from enjoying this trip…"

    show cga5 4 with Dissolve(0.25)
    voice audio.yoshi_vsa14_line16
    yo "But I had a great time spending this vacation with you, Aiden…! "

    voice audio.yoshi_vsa14_line17
    yo "I know it hasn’t been easy for you, but at the very least you tried your best to have fun with me and everyone else…"

    voice audio.aiden_vsa14_line14
    a "And I was so close to getting through it, then I just had to go and screw it up at the last moment…"

    voice audio.yoshi_vsa14_line18
    yo "What happened back there at the dinner wasn’t your fault at all though, Aiden."

    voice audio.yoshi_vsa14_line19
    yo "If anything, Emilia’s the one who’s been causing trouble ever since she showed up."

    voice audio.yoshi_vsa14_line20
    yo "Whenever she doesn’t get her way, she tends to say horrible things about you for no reason… "

    show cga5 5 with Dissolve(0.25)
    voice audio.aiden_vsa14_line15
    a "As awful as everything Emilia said about me back there was… She was right."

    voice audio.yoshi_vsa14_line21
    yo "A-About what…?"

    voice audio.aiden_vsa14_line16
    a "I’m not worth anything…"

    voice audio.aiden_vsa14_line17
    a "And the only reason I’m here is because of you…"

    voice audio.yoshi_vsa14_line22
    yo "Wh-What…? "

    voice audio.aiden_vsa14_line18
    a "Let’s be honest… I’m a nobody. It’s what I always was from the start…"

    voice audio.aiden_vsa14_line19
    a "I’m poor as dirt, I’m not educated, I have no actual skills… I’m nothing."

    voice audio.yoshi_vsa14_line23
    yo "Don’t let Emilia’s words get to you, Aiden! You know that’s not true…!"

    show cga5 6 with Dissolve(0.25)
    voice audio.aiden_vsa14_line20
    a "But it is, Yoshi! I would’ve screwed up on the project if you hadn’t covered for me this whole time!"

    voice audio.aiden_vsa14_line21
    a "You could have someone take my job at any time, and nothing would change!"

    voice audio.yoshi_vsa14_line24
    yo "But you’re so much more than that, Aiden! You’re—"

    voice audio.aiden_vsa14_line22
    a "Didn’t you see me back there? I didn’t know how to answer everyone’s questions about the only thing I’m supposed to be good at!"

    voice audio.aiden_vsa14_line23
    a "Heck, I can’t even hold the right spoon or pour a glass of wine!"

    voice audio.aiden_vsa14_line24
    a "I’m a fucking joke for believing that I had something special I could do…!"

    show cga5 7 with Dissolve(0.25)
    voice audio.aiden_vsa14_line25
    a "It was the only thing I could do to make you proud of me..."

    voice audio.aiden_vsa14_line26
    a "The reality is I was never meant for anything great in the first place. "

    show cga5 8 with Dissolve(0.25)
    voice audio.aiden_vsa14_line27
    a "I just can’t deny it anymore. That all I’ve always been was a burden and a disappointment…"

    voice audio.yoshi_vsa14_line25
    yo "I’ve never thought of you that way…! Not even once!"

    voice audio.aiden_vsa14_line28
    a "Even right now, you’re staying here, missing out because I can’t pull my shit together...!"

    voice audio.yoshi_vsa14_line26
    yo "That’s because I want to be here for you, Aiden…! More than anything else!"

    voice audio.aiden_vsa14_line29
    a "You’re just wasting your time on me, there’s nothing I can pay you back with…"

    voice audio.aiden_vsa14_line30
    a "I cause nothing but trouble to everyone, especially you, Yoshi…"

    voice audio.yoshi_vsa14_line27
    yo "What about all those years you’ve spent helping me and the camp…? Do you really believe we’d have gotten this far without you?"

    voice audio.yoshi_vsa14_line28
    yo "Out of everyone, you were the only one we could always rely on! Whether you were a scoutmaster or not, you’ve always done your best and given it your all!"

    show cga5 9 with Dissolve(0.25)
    voice audio.aiden_vsa14_line31
    a "Yoshi… Please, stop sugarcoating everything for me when we both know the truth…"

    voice audio.aiden_vsa14_line32
    a "The truth is that everything I have so far is because of pity…"

    voice audio.aiden_vsa14_line33
    a "My Dad and I were hired to work at Camp Buddy out of pity… I’ve become a scoutmaster out of pity… Everyone treated me nicely, all because of pity…"

    voice audio.aiden_vsa14_line34
    a "Even you… That’s how you’ve always seen me…"

    $working = False
    $shuffle_menu()
    menu():
        a "Even you… That’s how you’ve always seen me…{fast}"
        "Don't put words in my mouth!":
            $ score_aiden -= 2
            $ working = True
            show cga5 10a with Dissolve(0.25)
            voice audio.yoshi_vsa14_line29a
            yo "Don’t put words in my mouth, Aiden!"
        "How could you think that?!":
            $ score_aiden -= 1
            $ working = True
            show cga5 10a with Dissolve(0.25)
            voice audio.yoshi_vsa14_line29b
            yo "How could you think that after all we’ve been through, Aiden?!"
        "It's the opposite!":
            $ score_aiden += 1
            $ working = True
            show cga5 10b with Dissolve(0.25)
            voice audio.yoshi_vsa14_line29c
            yo "Pity is the exact opposite of what I think of you, Aiden!"
        "You're wrong!":
            $ score_aiden += 2
            $ working = True
            show cga5 10b with Dissolve(0.25)
            voice audio.yoshi_vsa14_line29d
            yo "You’re wrong, Aiden!"

    show cga5 11 with Dissolve(0.25)
    voice audio.yoshi_vsa14_line30
    yo "You don’t know how much I’ve looked up to you from the moment I met you!"

    voice audio.yoshi_vsa14_line31
    yo "You’re the most patient, resilient, and hardworking person I know… and you put others before yourself."

    voice audio.yoshi_vsa14_line32
    yo "But the most special thing about you is how you bring joy to people, always making sure we have a smile on our face."

    show cga5 12 with Dissolve(0.25)
    voice audio.yoshi_vsa14_line33
    yo "That’s why it honestly breaks my heart to see you like this… "

    voice audio.yoshi_vsa14_line34
    yo "Someone who had the brightest smile, while carrying all this pain in your heart for years, fighting this battle on your own."

    voice audio.yoshi_vsa14_line35
    yo "You’ve always hidden this – never letting anyone know what you’ve been through…"

    voice audio.yoshi_vsa14_line36
    yo "It’s okay to not be okay sometimes, Aiden… You don’t have to bear it alone anymore. "

    show cga5 13 with Dissolve(0.25)
    voice audio.aiden_vsa14_line35
    a "Why, Yoshi…?"

    voice audio.aiden_vsa14_line36
    a "If it wasn’t pity, then why would you do all this for me, since the beginning…?"

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.pause (2.0, hard=True)
    play music buddy_oath_musicbox
    scene cga6 1 with fade
    voice audio.yoshi_vsa14_line37
    yo "It’s because I love you…"

    $ renpy.pause (2.0, hard=True)
    show cga6 2 with Dissolve(0.25)
    voice audio.yoshi_vsa14_line38
    yo "I fell in love with you from the moment we first met and I saw your smile…   "

    voice audio.yoshi_vsa14_line39
    yo "I loved you more when I saw your strength to endure everything you’ve been through…  "

    voice audio.yoshi_vsa14_line40
    yo "And I love you the most because you gave me a purpose in my dull and gray life… "

    voice audio.yoshi_vsa14_line41
    yo "…And that is to protect that smile that gives me so much happiness."

    show cga6 3 with Dissolve(0.25)
    voice audio.aiden_vsa14_line37
    a "Yoshi…"

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

    $ location = location_rooftop
    $ day = "??"
    $ time = timeline_timenight
    $ season = season_summer
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene cga7 1 with fade
    play bgsound sfxloop_night loop
    play music go_with_the_flow_slow loop
    voice audio.yyoshi_vsa15_line1
    yo "This summer flew by really fast, huh, Aiden?"

    show cga7 2 with Dissolve(0.25)
    voice audio.yaiden_vsa15_line1
    a "Yeah… It feels like it was just yesterday that I met you. And suddenly we’re on the last day of the term…"

    show cga7 3 with Dissolve(0.25)
    voice audio.yyoshi_vsa15_line2
    yo "They say time flies when you’re having fun, and I’d say we had tons!"

    voice audio.yaiden_vsa15_line2
    a "You bet. I’m so lucky I got to stay here with you."

    voice audio.yyoshi_vsa15_line3
    yo "I’d say the same! I’ve never had someone that I’ve gotten as close with as you!"

    show cga7 4 with Dissolve(0.25)
    voice audio.yaiden_vsa15_line3
    a "To think, I just showed up here one day and before I knew it, I was stuck to you like glue, haha!"

    voice audio.yyoshi_vsa15_line4
    yo "I can’t help it! I just have so much fun hanging out with you!"

    show cga7 5 with Dissolve(0.25)
    voice audio.yyoshi_vsa15_line5
    yo "You might not believe it, but things wouldn’t have been the same without you."

    voice audio.yaiden_vsa15_line4
    a "I should be the one saying that though. "

    show cga7 6 with Dissolve(0.25)
    voice audio.yaiden_vsa15_line5
    a "So much has changed for me because of you."

    voice audio.yyoshi_vsa15_line6
    yo "Huh? What do you mean, Aiden?"

    show cga7 7 with Dissolve(0.25)
    voice audio.yaiden_vsa15_line6
    a "I’m sure I’ve told you before how Dad and I don’t really have much outside of Camp Buddy."

    voice audio.yaiden_vsa15_line7
    a "But the truth is, we really don’t have anywhere else to go."

    show cga7 8 with Dissolve(0.25)
    voice audio.yyoshi_vsa15_line7
    yo "Wh-What…?"

    show cga7 9 with Dissolve(0.25)
    voice audio.yaiden_vsa15_line8
    a "As much as Dad tried to hide it from me, I knew we were in a lot of debt."

    voice audio.yaiden_vsa15_line9
    a "He had to work multiple jobs at once, trying to earn enough for us both."

    voice audio.yaiden_vsa15_line10
    a "We had to keep moving around, too, until we found Camp Buddy."

    show cga7 10 with Dissolve(0.25)
    voice audio.yaiden_vsa15_line11
    a "And that’s when I met you! You were the reason Dad and I got a place to stay for good."

    voice audio.yaiden_vsa15_line12
    a "We finally didn’t have to worry about all that stuff as much anymore."

    show cga7 11 with Dissolve(0.25)
    voice audio.yyoshi_vsa15_line8
    yo "I didn’t know, Aiden… "

    voice audio.yyoshi_vsa15_line9
    yo "If only I knew more, I could’ve done something to help."

    show cga7 12 with Dissolve(0.25)
    voice audio.yaiden_vsa15_line13
    a "But that’s the thing, Yoshi. Even without knowing, you were able to pull my dad and I out of that situation!  "

    voice audio.yaiden_vsa15_line14
    a "And for that, I’ll always be thankful…"

    show cga7 13 with Dissolve(0.25)
    voice audio.yyoshi_vsa15_line10
    yo "I-I just never thought, after all this time together, that you were going through something like that…"

    voice audio.yaiden_vsa15_line15
    a "I didn’t want you to feel bad for me, or change the way you see me because of it."

    show cga7 14 with Dissolve(0.25)
    voice audio.yaiden_vsa15_line16
    a "And that’s because I really am happy with you, Yoshi."

    show cga7 15 with Dissolve(0.25)
    voice audio.yaiden_vsa15_line17
    a "You didn’t treat me any differently, always going out of your way to spend time with me or to make sure I was never left out."

    voice audio.yaiden_vsa15_line18
    a "And on top of that, you were always encouraging me to cook, the one thing I knew I loved doing."

    show cga7 16 with Dissolve(0.25)
    voice audio.yaiden_vsa15_line19
    a "You made me realize I could be more than I ever thought I could be."

    voice audio.yyoshi_vsa15_line11
    yo "Aiden…"

    show cga7 17 with Dissolve(0.25)
    voice audio.yaiden_vsa15_line20
    a "A-Ah! Sorry, I got carried away!"

    show cga7 18 with Dissolve(0.25)
    voice audio.yaiden_vsa15_line21
    a "I guess, I was just trying to tell you how grateful I am for everything this summer."

    voice audio.yaiden_vsa15_line22
    a "Especially knowing this could be our last night together… "

    show cga7 19 with Dissolve(0.25)
    voice audio.yyoshi_vsa15_line12
    yo "It won’t be, Aiden.  "

    voice audio.yyoshi_vsa15_line13
    yo "I’m leaving to study now so I can be a scoutmaster here one day!"

    voice audio.yaiden_vsa15_line23
    a "R-Really, Yoshi?!"

    show cga7 20 with Dissolve(0.25)
    voice audio.yyoshi_vsa15_line14
    yo "Yeah! I know it’ll take a really long time, but once that happens, I’ll be right back here with you!"

    voice audio.yaiden_vsa15_line24
    a "Then I’ll do everything I can to stay here, and I won’t just wait either… I’ll try to make something out of myself, too…!"

    show cga7 21 with Dissolve(0.25)
    voice audio.yyoshi_vsa15_line15
    yo "Should we seal the deal then?"

    voice audio.yaiden_vsa15_line25
    a "Yeah! "

    show cga8 1 with Dissolve(0.25)
    voice audio.yyoshi_vsa15_line16
    yo "Here’s to both of us coming back here together someday!"

    voice audio.yaiden_vsa15_line26
    a "No matter what happens, we’ll stay strong and keep doing our best until that day comes!"

    show cga8 2 with Dissolve(0.25)
    voice audio.yyoshiaiden_vsa15_line1
    yoa "It’s a promise!"

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
    jump day5_aiden
