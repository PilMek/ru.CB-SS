label day2:
    $ day = "02"
    $ time = timeline_timeday
    $ location = location_office
    $ working = True
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_office_autumn_day with fade
    play music buddy_oath_casual loop

    show goro_semiformal at center
    show goro explain2 at center
    voice audio.goro_v_alright1a2
    g "Alright… Better make sure I didn’t forget anything…"

    play sound sfx_doorknock
    $ renpy.pause (1.0, hard=True)
    show goro talk1 at center
    voice audio.goro_v_greet2a1
    g "Come in."

    show yoshi_autumn at p5_5
    show yoshi happy1 at p5_5
    with dissolve

    voice audio.yoshi_v_goodam1
    yo "Good morning, Sir Goro!"

    show goro_semiformal at left2
    show goro talk1 at left2
    show yoshi_autumn at right2
    show yoshi happy1 at right2
    with move

    hide yoshi_autumn
    hide yoshi happy1
    show yoshi_autumn at right2
    show yoshi amazed1 at right2
    voice audio.yoshi_v_praise3
    yo "Y-You look dashing, sir. Are you going somewhere today?"

    show goro talk3 at left2
    voice audio.goro_v_agree2a1
    g "Ah, yes, I am. I have a meeting scheduled with Mr. Clermont. "

    hide yoshi amazed1
    show yoshi talk1 at right2
    voice audio.yoshi_v_oh1
    yo "Oh. What’s on the agenda, if I may ask?"

    show goro explain2 at left2
    voice audio.goro_v_comp2a1
    g "It’s just the usual weekly meeting to discuss the progress of the sponsorship. I figured it wasn’t worth mentioning."

    show yoshi comp6 at right2
    voice audio.yoshi_v_laugh3
    yo "Hehe, you do tend to be private with your work, sir. "
    yo "Though, I’m a bit curious – aren’t you a little nervous to be meeting him today? "

    show goro confused3  at left2
    voice audio.goro_v_no2a1
    g "No, not at all. Why would you ask that? "

    hide yoshi_autumn
    hide yoshi comp6
    show yoshi2_autumn at right2
    show yoshi2 comp2 at right2
    voice audio.yoshi_v_well3
    yo "W-Well, the last time Mr. Clermont was here, you acted quite differently from your usual self. I mean… I’ve never seen you that frantic before."

    hide goro confused3
    show goro annoy2 at left2
    voice audio.goro_v_hey5a
    g "Hey, I was calm the whole time I was showing him around… I made sure not to show my excitement until after he left."
    g "After all, Mr. Clermont is someone I’ve looked up to for a long time. I didn’t think I’d ever meet him in person, so his visit really caught me off guard."

    hide goro annoy2
    show goro explain5 at left2
    voice audio.goro_v_think1a1
    g "His works really inspired me to do some self-reflection in the past. "

    show yoshi2 shy5 at right2
    voice audio.yoshi_v_right4
    yo "R-Right…"

    show goro talk1 at left2
    voice audio.goro_v_anyway2
    g "Anyway, what brings you to the office, Yoshinori?"

    hide yoshi2_autumn
    hide yoshi2 shy5
    show yoshi_autumn at right2
    show yoshi talk3 at right2
    voice audio.yoshi_v_actually1a
    yo "Oh… Actually, I was planning to ask for my weekly task list, but it can wait since you’re busy!"
    yo "I can just do maintenance tasks around the camp and keep things in tip-top shape. "

    hide goro_semiformal
    hide goro talk1
    show goro_semiformal at left2
    show goro think2 at left2
    voice audio.goro_v_yoshi2a
    g "Actually, Yoshinori…"

    hide goro_semiformal
    hide goro think2
    show goro_semiformal at left2
    show goro talk2 at left2
    g "Why don’t you come with me today?"

    show yoshi awkward4 at right2
    voice audio.yoshi_v_really1
    yo "Really, sir? I don’t want to get in your way, especially in an important meeting."

    show goro happy2 at left2
    voice audio.goro_v_dismiss2a
    g "Nonsense. Sooner or later, you’re going to have to be attending these anyway."
    g "You will need a formal outfit, however. I have a spare suit here that you can use. It’s older, but it should fit you."

    show goro talk3 at left2
    voice audio.goro_v_response1b1
    g "We’ll leave as soon as you get changed."

    show yoshi happy2 at right2
    voice audio.yoshi_v_yessir1
    yo "Y-Yes, sir!"

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black
    play sound sfx_carstart
    hide screen location
    hide screen timeline
    hide screen quick_menu
    $quick_menu = False
    with fade
    $ renpy.pause (2.0, hard=True)

    $ location = location_car
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene cgg2 1 with fade
    play music old_familiar_home loop
    play bgsound sfxloop_carride loop

    yo "{i}(I don’t know why, but even though we’re only going out for a business errand… I’m really excited to be with Sir Goro today.){/i}"
    yo "{i}(It’s almost like those old scouting trips we used to take.){/i}"
    g "..."

    show cgg2 2 with Dissolve(0.25)
    yo "{i}(It's rare that Sir Goro and I are on the road together like this, but we've hardly talked since we headed out this morning…){/i}"
    yo "{i}(I should probably say something to break the ice…){/i}"

    $working = False
    $shuffle_menu()
    menu():
        yo "{i}(I should probably say something to break the ice…){/i}{fast}"
        "Stay quiet.":
            $working = True
            $score_goro -= 1
            show cgg2 3a with Dissolve(0.25)
            yo "{i}(I really don't want it to seem like I'm not taking this errand seriously, so maybe I should just stay quiet.){/i}"

            show cgg2 5 with Dissolve(0.25)
            voice audio.goro_vsg3_line2ab
            g "*ahem* So, Yoshinori."

            voice audio.yoshi_vsg3_line2ab
            yo "Oh! Yes, sir?"

            voice audio.goro_vsg3_line3ab
            g "I can’t help but notice the brooch you attached to your suit."
        "Talk about the weather.":
            $working = True
            show cgg2 3b with Dissolve(0.25)
            voice audio.yoshi_vsg3_line1b
            yo "Th-The weather’s really nice today, isn’t it, sir…?"

            show cgg2 4b with Dissolve(0.25)
            voice audio.goro_vsg3_line1b
            g "Yeah, it is."

            yo "{i}(Well, that went nowhere… ){/i}"

            show cgg2 5 with Dissolve(0.25)
            voice audio.goro_vsg3_line2ab
            g "*ahem* So, Yoshinori."

            voice audio.yoshi_vsg3_line2ab
            yo "Oh! Yes, sir?"

            voice audio.goro_vsg3_line3ab
            g "I can’t help but notice the brooch you attached to your suit."
        "Talk about the meeting.":
            $working = True
            $score_goro += 1
            show cgg2 3cd with Dissolve(0.25)
            voice audio.yoshi_vsg3_line1c
            yo "Th-Thank you again for letting me tag along today, sir…!"

            voice audio.yoshi_vsg3_line2c
            yo "I’m not sure how exactly I can help, but I’m glad you’re letting me see what you’ve been working on with Mr. Clermont these past few weeks."

            show cgg2 4c with Dissolve(0.25)
            voice audio.goro_vsg3_line1c
            g "I'm glad you're excited for this. I can tell by how much you've been fidgeting with your suit this whole time."

            voice audio.yoshi_vsg3_line3c
            yo "Aah…! I didn’t realize I was doing that…!"

            show cgg2 5 with Dissolve(0.25)
            voice audio.goro_vsg3_line3cd
            g "Although… I can’t help but notice the brooch you attached to it."
        "Talk about the suit.":
            $working = True
            $score_goro += 2
            show cgg2 3cd with Dissolve(0.25)
            voice audio.yoshi_vsg3_line1d
            yo "Th-Thanks again for lending me your suit, sir…! It’s been so long since I’ve worn something this formal!"

            show cgg2 4d with Dissolve(0.25)
            voice audio.goro_vsg3_line1d
            g "Ah, hopefully the fit isn’t too loose on you. "

            voice audio.yoshi_vsg3_line2d
            yo "Not at all, sir! It’s actually perfect for this season’s weather too!"

            voice audio.goro_vsg3_line2d
            g "That’s good. I knew that style and color would suit you well..."

            show cgg2 5 with Dissolve(0.25)
            voice audio.goro_vsg3_line3cd
            g "Although… I can’t help but notice the brooch you attached to it."

    show cg fade at truecenter
    show fxg1 at fx_pos
    with dissolve

    voice audio.goro_vsg3_line4
    g "Wasn’t that the one I gave you back when you were a scout?"

    voice audio.yoshi_vsg3_line4
    yo "Yes, it is, sir…!   "

    voice audio.goro_vsg3_line5
    g "I haven’t seen that in years. I’m surprised you still have it."

    voice audio.yoshi_vsg3_line5
    yo "Of course, it meant a lot to me, so I kept it safe."

    voice audio.yoshi_vsg3_line6
    yo "I thought it might be a bit of a good luck charm for today!"

    hide cg fade
    hide fxg1
    with dissolve

    show cgg2 6 with Dissolve(0.25)
    voice audio.goro_vsg3_line6
    g "Hahaha, and you thought I was the one being nervous earlier."

    voice audio.yoshi_vsg3_line7
    yo "Ah… Hehehe…"

    show cgg2 7 with Dissolve(0.25)
    voice audio.goro_vsg3_line7
    g "You know, Yuri was quite jealous when I gave you that brooch."

    voice audio.goro_vsg3_line8
    g "She even accused me of picking favorites among the campers."

    voice audio.goro_vsg3_line9
    g "It couldn’t be helped though… You were quite the showoff when you were a scout."

    voice audio.yoshi_vsg3_line8
    yo "R-Really? I hardly remember how I was back then…"

    show cgg2 8 with Dissolve(0.25)
    voice audio.goro_vsg3_line10
    g "Not much has changed, if I do say so myself… You’re still that go-getting, active scout that I remember."

    voice audio.goro_vsg3_line11
    g "You really stood out amongst your peers, especially on that first camping trip we had."

    voice audio.goro_vsg3_line12
    g "In fact, that was when I gave you that brooch."

    show cgg2 9 with Dissolve(0.25)
    voice audio.yoshi_vsg3_line9
    yo "Yeah, I remember…"

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    hide screen location
    hide screen timeline
    hide screen quick_menu
    $quick_menu = False
    scene cg white with Dissolve(2.0)
    $past_scene = True

    scene cg black
    hide screen location
    hide screen timeline
    hide screen quick_menu
    $quick_menu = False
    with fade
    $ renpy.pause (2.0, hard=True)

    $ location = location_entrance
    $ day = "??"
    $ time = timeline_timeday
    $ season = season_summer
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_entrance_past_day with fade
    play music camping_time loop
    play bgsound sfxloop_birds loop

    show ygoro_camp at center
    show ygoro talk1 at center
    voice audio.ygoro_v_attention1a
    g "Listen up, scouts! We’ll be heading out on a hike to the fields in just a few moments!"

    show ygoro explain2 at center
    g "I want everyone to find their assigned partner and double-check both of your gear."

    show ygoro talk3 at center
    voice audio.ygoro_v_dismiss2b
    g "That’s all for now! We’ll be leaving in five minutes!"

    hide ygoro_camp
    hide ygoro talk3
    with dissolve

    show yyoshi_camp at left2
    show yyoshi norm1 at left2
    show yyuri_camp2 at right2
    show yyuri annoy5 at right2
    with dissolve

    voice audio.yyuri_v_ugh3c
    yu "Ughhhh… five more minutes? Can’t we go already? It’s been two hours since we woke up!"

    show yyoshi talk3 at left2
    voice audio.yyoshi_v_yuri9a
    yo "Come on, Yuri. We used most of that time to get dressed and have our breakfast."
    yo "More importantly, you know how much all these checks matter."

    show yyuri angry3 at right2
    voice audio.yyuri_v_but1b
    yu "But you already checked our stuff, like, three times this morning!"

    show yyoshi play2 at left2
    voice audio.yyoshi_v_laugh5
    yo "And if I hadn’t, I wouldn’t have found out that you packed nothing but your notebooks."

    show yyuri pout3 at right2
    voice audio.yyuri_v_hmph1a
    yu "They’re called fanfics, hmph!"

    show yyoshi_camp at left
    show yyoshi play2 at left
    show yyuri_camp2 at center
    show yyuri pout3 at center
    with move

    show ygoro_camp at right
    show ygoro comp3 at right
    with dissolve

    voice audio.ygoro_v_yuridear1
    g "And that’s why I paired Yoshinori with you, dear. Hahaha."

    show yyuri annoy4 at center
    voice audio.yyuri_v_question1b
    yu "It’s only a one-night trip, so how much stuff could we need?"

    show ygoro explain4 at right
    voice audio.ygoro_v_well1
    g "Well, if you’d been paying attention to our lessons, you would know to bring the basics, such as your navigation tools, adequate food and water, a first-aid kit, and more!"

    show yyoshi bold2 at left
    voice audio.yyoshi_v_sir2
    yo "We packed extra clothing, bug spray, and toiletries too, sir!"

    show ygoro play3 at right
    voice audio.ygoro_v_see5a
    g "See? Yoshinori here clearly took notes!"

    show yyuri rage3 at center
    voice audio.yyuri_v_rush3b
    yu "Well, your five minutes are up and we’re all ready, so let’s goooooo!"

    show ygoro comp2 at right
    voice audio.ygoro_v_alright1a
    g "Alright, alright, I’ll get everyone started."

    show yyoshi_camp at p6_1
    show yyoshi bold2 at p6_1
    show yyuri_camp2 at p6_2
    show yyuri rage3 at p6_2
    show ygoro_camp at center
    show ygoro comp2 at center
    with move

    show ygoro happy1 at center
    voice audio.ygoro_v_okay2a
    g "Okay, scouts! Form up into a line and find your buddies! We’re going to begin our march."

    show ygoro happy3 at center
    voice audio.ygoro_v_rush1b1
    g "Follow me!"

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black
    hide screen location
    hide screen timeline
    hide screen quick_menu
    $quick_menu = False
    with fade
    play sound sfx_trekking
    $ renpy.pause (2.0, hard=True)

    $ location = location_forest
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_forest_past_day with fade
    play music adventure loop
    play bgsound sfxloop_birds loop

    show ygoro_camp at center
    show ygoro talk3 at center
    voice audio.ygoro_v_worry1a
    g "How’s everyone holding up? "
    g "This path I chose for our first camping trip is a short and safe one to help everyone familiarize themselves with the trail for our future hikes!"

    show ygoro talk4 at center
    voice audio.ygoro_v_comp2a1
    g "Just make sure to stay close to your buddy and keep following my lead, alright scouts?"
    all "Yes, sir!"

    show ygoro explain2 at center
    voice audio.ygoro_v_rush4
    g "Now, some of you might be wondering why I’ve assigned you all in pairs. The reason for this is to improve your sense of cooperation, especially in times of emergency!"
    g "If your team gets separated, it’s important to stay calm and find a solution with your partner!"

    show ygoro talk2 at center
    voice audio.ygoro_v_conj7a
    g "You have access to your navigation tools to help get you both back on track, reach the destination, or return to camp."

    show ygoro explain5 at center
    voice audio.ygoro_v_comp2a1
    g "In case you truly get lost, do not panic, remember to conserve your energy, and stay in place."
    g "You can make use of your survival items, such as your flint, flashlight and sleeping bag, to set up a temporary camp."

    show ygoro talk2 at center
    voice audio.ygoro_v_conj2a1
    g "Creating a fire is especially helpful, as the smoke could help rescue teams locate you faster. "

    show ygoro bold2 at center
    voice audio.ygoro_v_request2a1
    g "With all of these survival tools and knowledge from the lessons we’ve had, you’ll definitely be able to handle an emergency!"

    show ygoro_camp at p5_5
    show ygoro bold2 at p5_5
    with move

    show yyuri_camp2 at p5_1
    show yyuri fangirl1 at p5_1
    show yyoshi_camp at p5_2
    show yyoshi norm1 at p5_2
    with dissolve

    voice audio.yyuri_v_kyaa1
    yu "Kyaa! I can’t believe we’re finally doing something exciting!"
    yu "Staying in the campgrounds all day long was starting to bore me!"

    show yyoshi angry2 at p5_2
    voice audio.yyoshi_v_yuri9b
    yo "Don’t say that, Yuri! I’m sure Sir Goro had a good reason to keep us in the camp, and he did his best to make everything interesting there!"

    show yyuri angry6 at p5_1
    voice audio.yyuri_v_yeah1h1
    yu "Yeah, yeah, I know! But did we really HAVE to wait for two weeks to actually start camping at a summer camp?"

    show yyoshi explain2 at p5_2
    voice audio.yyoshi_v_conj1a
    yo "I’m sure trips like these needed a lot of planning and preparation to make sure everything goes perfectly!"
    yo "Besides, isn’t it great we get to learn all this cool, new stuff from Sir Goro? "

    show yyuri sigh1 at p5_1
    voice audio.yyuri_v_sigh1a
    yu "*sigh* I already know all of this…"

    show yyuri_camp2 at left
    show yyuri norm1 at left
    show yyoshi_camp at center
    show yyoshi norm1 at center
    show ygoro_camp at right
    show ygoro bold2 at right
    with move

    show ygoro disappoint2 at right
    voice audio.ygoro_v_ehem1a
    g "*ahem* Not everyone had a head start like you, dear."

    show yyoshi shock2 at center
    voice audio.yyoshi_v_sirgoro10a
    yo "A-Ah, Sir Goro…!"

    show ygoro happy2 at right
    voice audio.ygoro_v_well1
    g "Yuri here has been interested in nature for a long time, so most of the things I’ve been teaching here are things she already knows."

    show yyuri happy1 at left
    voice audio.yyuri_v_yeah1b1
    yu "Yeah! Dad bought me a lot of books about camping and survival!"

    show ygoro explain3 at right
    voice audio.ygoro_v_conj6a1
    g "The actual experience is always different though! Just like you, most of your fellow scouts have never even tried camping or exploring the great outdoors. "

    show ygoro talk1 at right
    voice audio.ygoro_v_conj1a1
    g "It’s my duty as a scoutmaster to prepare everyone for a trip like this through the exercises and lessons we’ve done so far."
    g "Everything I taught you all will guarantee that everyone has a fun and safe time today!"

    show yyuri sigh1 at left
    voice audio.yyuri_v_unsure3a
    yu "I guess you have a point…"

    show ygoro comp2 at right
    voice audio.ygoro_v_yuridear1
    g "Now be more patient, dear.  Use this opportunity to share the knowledge you’ve learned!"

    show yyuri talk3 at left
    voice audio.yyuri_v_but1a
    yu "But it sounds like Yoshi knows everything already too."

    show yyoshi comp2 at center
    voice audio.yyoshi_v_oh2
    yo "O-Oh! I only learned it all from Sir Goro’s lessons…!"
    yo "We’re really lucky to have you teaching and guiding us, sir!"

    show yyuri tease2 at left
    voice audio.yyuri_v_laugh2b1
    yu "Hehehe… Look at you, sucking up to my dad like that~"

    show yyoshi awkward4 at center
    voice audio.yyoshi_v_shock3
    yo "W-Wah…! I-I’m just telling the truth!"
    yo "All the activities Sir Goro made for us back at camp were great preparations for today, especially the group ones!"

    show yyoshi happy2 at center
    voice audio.yyoshi_v_laugh1
    yo "We all got to know each other a lot better through them, and we learned how to work together!"

    show ygoro bold2 at right
    voice audio.ygoro_v_laugh1a
    g "You should be more enthusiastic like Yoshinori here, dear. It seems he got the point of the lessons exactly right!"

    show ygoro play2 at right
    voice audio.ygoro_v_rush4
    g "Now, shall we resume our hike? We’re almost at our destination!"

    play sound sfx_phonering
    show yyoshi shock1 at center
    show ygoro shock2 at right
    voice audio.ygoro_v_oh2
    g "O-Oh...! On second thought, I need to take this call."

    show ygoro_camp at p5_5
    show ygoro talk3 at p5_5
    show yyuri_camp2 at p5_1
    show yyuri pout1 at p5_1
    show yyoshi_camp at p5_2
    show yyoshi shock1 at p5_2
    with move

    voice audio.ygoro_v_ehem1a
    g "Attention, scouts! We’ll be taking a short break! "
    g "Make sure to use this time to have some snacks and hydrate. "

    show ygoro explain2 at p5_5
    voice audio.ygoro_v_bye4a
    g "I’ll be right back!"

    hide ygoro_camp
    hide ygoro explain2
    with dissolve

    show yyuri_camp2 at left2
    show yyuri  sigh1 at left2
    show yyoshi_camp at right2
    show yyoshi shock1 at right2
    with move

    voice audio.yyuri_v_sigh2a
    yu "*sigh* Not again… Just when I thought everything was going well today."

    show yyoshi confused2 at right2
    voice audio.yyoshi_v_huh1
    yo "H-Huh? What do you mean, Yuri?"

    show yyuri annoy4 at left2
    voice audio.yyuri_v_annoyed1a
    yu "I really don’t want to talk about it. There’s nothing we can do about it anyways."

    show yyoshi worry2 at right2
    voice audio.yyoshi_v_unsure2a
    yo "A-Are you sure? Maybe there’s something we can do to help Sir G—"

    show yyuri_camp2 at center
    show yyuri annoy4 at center
    with move
    voice audio.yyuri_v_hmph2a
    yu "*pinches Yoshinori*"

    show yyoshi pain3 at right2
    voice audio.yyoshi_v_oww1
    yo "O-Ow! Wh-What was that for, Yuri??"

    show yyuri angry2 at center
    voice audio.yyuri_v_annoyed3a
    yu "I told you it’s no use! Let’s just stay out of it! "

    show yyoshi angry2 at right2
    voice audio.yyoshi_v_hmph1b
    yo "You didn’t have to pinch me so hard…"

    show yyuri angry5 at center
    voice audio.yyuri_v_rush1b2
    yu "Come on, let’s just distribute some snacks and water to everyone while we wait!"

    show yyoshi talk3 at right2
    voice audio.yyoshi_v_right7
    yo "Oh… alright."

    hide yyuri_camp2
    hide yyuri angry5
    with dissolve

    show yyoshi worry1 at right2
    yo "..."

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

    $ location = location_forest
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_forest_past_day with fade
    play music old_familiar_home_slow loop
    play bgsound sfxloop_birds loop

    show ygoro_camp at center
    show ygoro worry3 at center
    voice audio.ygoro_vsg4_line1
    g "…What do you mean you can’t come? It’s okay if you’re going to be late, we don’t mind waiting."

    show ygoro worry1 at center
    g "..."

    show ygoro angry3 at center
    voice audio.ygoro_vsg4_line2
    g "How can you not have time?! You know I’ve been planning this activity for weeks, and—"

    show ygoro angry1 at center
    g "..."

    show ygoro angry4 at center
    voice audio.ygoro_vsg4_line3
    g "Yuri’s been looking forward to today! Can’t you understand how important this is? "

    show yyoshi_camp at p5_5
    show yyoshi worry1 at p5_5
    with dissolve

    yo "..."

    show ygoro disappoint4 at center
    voice audio.ygoro_vsg4_line4
    g "You’re never around, Vera! This is the only time I asked you to be together as a family!"

    voice audio.ygoro_vsg4_line5
    g "What are you even busy with?!"

    show ygoro panic1 at center
    g "..."

    show ygoro panic2 at center
    voice audio.ygoro_vsg4_line6
    g "N-No, I’m not trying to accuse you of anything! "

    show ygoro worry4 at center
    voice audio.ygoro_vsg4_line7
    g "I know having a family was never our plan, but it’s been nineteen years! "

    voice audio.ygoro_vsg4_line8
    g "Just please come over, at least for Yuri…"

    play sound sfx_phonebutton
    show ygoro worry2 at center
    voice audio.ygoro_vsg4_line9
    g "H-Hello? "

    show ygoro sigh1 at center
    voice audio.ygoro_vsg4_line10
    g "*sigh*"

    show ygoro shock3 at center
    voice audio.ygoro_vsg4_line11
    g "A-Ah! Yoshinori…! "

    show ygoro_camp at left2
    show ygoro shock3 at left2
    show yyoshi_camp at right2
    show yyoshi worry2 at right2
    with move

    voice audio.yyoshi_vsg4_line1
    yo "Uhh… Sir? Is everything alright…?"

    show ygoro awkward3 at left2
    voice audio.ygoro_vsg4_line12
    g "Y-Yes. It’s just a personal matter, nothing for you to worry about."

    voice audio.ygoro_vsg4_line13
    g "What brings you here though? "

    $working = False
    $shuffle_menu()
    menu():
        g "What brings you here though? {fast}"
        "When are we starting our hike again?":
            $working = True
            $score_goro -= 2
            show yyoshi talk1 at right2
            voice audio.yyoshi_vsg4_line2a
            yo "I just wanted to ask when we'd start our hike again, sir!"

            show ygoro explain2 at left2
            voice audio.ygoro_vsg4_line14a
            g "I see. I apologize for the short delay. Let me come back right away."

            show yyoshi explain2 at right2
            voice audio.yyoshi_vsg4_line4ab
            yo "W-Well… I also came to ask you about something I thought I could help you with, sir…!"

            show ygoro confused3 at left2
            voice audio.ygoro_vsg4_line16ab
            g "Oh, what is it?"
        "I'm here to report.":
            $working = True
            show yyoshi talk1 at right2
            voice audio.yyoshi_vsg4_line2b
            yo "I’m here to make a report, sir…!"

            show ygoro confused2 at left2
            voice audio.ygoro_vsg4_line14b
            g "Hm? Is everything alright back there?"

            show yyoshi talk2 at right2
            voice audio.yyoshi_vsg4_line3b
            g "Y-Yes, sir! In fact, Yuri and I handed out some drinks and snacks to the other scouts while we were waiting…!"

            show ygoro explain2 at left2
            voice audio.ygoro_vsg4_line15b
            g "Ah, good job, Yoshinori. Let me come back right away and resume our hike."

            show yyoshi explain2 at right2
            voice audio.yyoshi_vsg4_line4ab
            yo "W-Well… I also came to ask you about something I thought I could help you with, sir…!"

            show ygoro confused3 at left2
            voice audio.ygoro_vsg4_line16ab
            g "Oh, what is it?"
        "I wanted to check on you.":
            $working = True
            $score_goro += 1
            show yyoshi talk1 at right2
            voice audio.yyoshi_vsg4_line2c
            yo "I-I wanted to check on you, sir…!"

            voice audio.yyoshi_vsg4_line3c
            yo "Yuri and I were handing out some drinks and snacks to the other scouts while we were waiting."

            voice audio.yyoshi_vsg4_line4c
            yo "And I thought a drink might help you relax some too, so I came looking for you as soon as we finished…!"

            show ygoro comp1 at left2
            g "..."

            show ygoro comp2 at left2
            voice audio.ygoro_vsg4_line14cd
            g "Thank you for your concern, Yoshinori. I’m fine."

            show yyoshi worry2 at right2
            voice audio.yyoshi_vsg4_line4cd
            yo "I-I’m sorry for prying, but… if there’s anything I can do, please let me help you, sir…"
        "I noticed you seemed a little upset.":
            $working = True
            $score_goro += 2
            show yyoshi talk1 at right2
            voice audio.yyoshi_vsg4_line2d
            yo "I noticed you seemed a bit upset when you got the call… So, I thought you might need some company!"

            voice audio.yyoshi_vsg4_line3d
            yo "You don’t have to worry about the other scouts too! Yuri and I just finished handing out drinks and snacks to them!"

            show ygoro comp1 at left2
            g "..."

            show ygoro comp2 at left2
            voice audio.ygoro_vsg4_line14cd
            g "Thank you for your concern, Yoshinori. I’m fine."

            show yyoshi worry2 at right2
            voice audio.yyoshi_vsg4_line4cd
            yo "I-I’m sorry for prying, but… if there’s anything I can do, please let me help you, sir…"

    show yyoshi comp2 at right2
    voice audio.yyoshi_vsg4_line5
    yo "I-If it’s okay with you, I can actually lead the scouts for the rest of the hike! You don’t have to worry about any of us getting lost since I’ve got the map memorized!"

    voice audio.yyoshi_vsg4_line6
    yo "O-Oh, and we can set up the camp at the fields in advance, so we’ll have more time to do an outdoor activity for the rest of the day…!"

    show ygoro talk3 at left2
    voice audio.ygoro_vsg4_line17
    g "I really appreciate your intentions, Yoshinori, but you don’t have to take over."

    show yyoshi worry3 at right2
    voice audio.yyoshi_vsg4_line7
    yo "B-But, sir…"

    show ygoro sigh1 at left2
    voice audio.ygoro_vsg4_line18
    g "*sigh* I knew you weren’t going to give up that easily…"

    voice audio.ygoro_vsg4_line19
    show ygoro comp1 at left2
    g "Why don’t we lead the scouts together, then?"

    show yyoshi shock1 at right2
    yo "...!"

    show ygoro comp2 at left2
    voice audio.ygoro_vsg4_line20
    g "I will let you take the front end of the march, and I will watch over your side to make sure everyone follows your lead. What do you think?"

    show ygoro comp1 at left2
    show yyoshi bold2 at right2
    voice audio.yyoshi_vsg4_line8
    yo "I’d be honored, sir! Thank you for letting me help!"

    voice audio.yyoshi_vsg4_line9
    yo "I’ll gather everyone immediately…!"

    show yyoshi_camp at p6_6
    show yyoshi excited1 at p6_6
    with move

    show ygoro talk3 at left2
    voice audio.ygoro_vsg4_line21
    g "Ah, Yoshinori… One more thing."

    show yyoshi_camp at right2
    show yyoshi talk3 at right2
    with move

    voice audio.yyoshi_vsg4_line10
    yo "Y-Yes, sir…?"

    show ygoro comp2 at left2
    voice audio.ygoro_vsg4_line22
    g "I want you to have this…"

    show ygoro_camp at center
    show ygoro comp2 at center
    with move

    show cg fade at truecenter
    show fxg1 at fx_pos
    with dissolve

    voice audio.ygoro_vsg4_line23
    g "It’s something I made way back when I was preparing for Camp Buddy’s launch."

    voice audio.yyoshi_vsg4_line11
    yo "Oh, it’s the same symbol that’s around the camp and on our uniforms…!"

    voice audio.ygoro_vsg4_line24
    g "Yes, the insignia represents the core meaning of this camp."

    voice audio.ygoro_vsg4_line25
    g "A star that always burns bright, no matter what; just like someone you can count on to help you through even the darkest times."

    voice audio.ygoro_vsg4_line26
    g "This may not mean much right now, but I assure you it will make sense one day."

    hide cg fade
    hide fxg1
    with dissolve

    show yyoshi comp2 at right2
    voice audio.yyoshi_vsg4_line12
    yo "Th-Thank you very much, sir! I’m really honored to have this…!"

    show ygoro comp5 at center
    voice audio.ygoro_vsg4_line27
    g "You’re welcome, Yoshinori. Now let’s get going. Everyone must’ve finished with their break."

    show yyoshi bold2 at right2
    voice audio.yyoshi_vsg4_line13
    yo "Yes, sir!"

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

    $ location = location_car
    $ day = "02"
    $ time = timeline_timeday
    $ season = season_autumn
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene cgg2 10 with fade
    play music old_familiar_home loop
    play bgsound sfxloop_carride loop

    voice audio.yoshi_vsg3_line10
    yo "N-Now I’m kinda embarrassed of how I acted back then… I didn’t realize how much of a showoff I was…"

    voice audio.goro_vsg3_line13
    g "Well, it’s not exactly a bad thing. I understood that you were just thrilled to be at the camp."

    show cgg2 11 with Dissolve(0.25)
    voice audio.goro_vsg3_line14
    g "I probably wouldn’t have given you that brooch if it weren’t for that quality of yours."

    voice audio.yoshi_vsg3_line11
    yo "A-Ah… I’m not sure if I should take that as a compliment, sir. "

    show cgg2 12 with Dissolve(0.25)
    voice audio.goro_vsg3_line15
    g "Hmm… Let’s just say I just saw something promising in you, from the way you acted, to the way you were willing to lead and take charge."

    voice audio.goro_vsg3_line16
    g "I wanted to give you some form of acknowledgement for it."

    show cgg2 13 with Dissolve(0.25)
    voice audio.goro_vsg3_line17
    g "Heh, and it turns out I was right too. Just look at how far you’ve come today. "

    voice audio.yoshi_vsg3_line12
    yo "Th-Thank you, sir. It really honors me to know that you place so much faith in me and my abilities."

    voice audio.yoshi_vsg3_line13
    yo "Although, I have to admit, every time you tell me that I’ll be next in line for your role at Camp Buddy, I always wonder if I can really do it."

    show cgg2 14 with Dissolve(0.25)
    voice audio.goro_vsg3_line18
    g "Come on, where’s that overflowing enthusiasm you had back then? "

    voice audio.goro_vsg3_line19
    g "If I had told the younger Yoshinori that he was going to be in charge, he’d never have been able to calm down! "

    voice audio.goro_vsg3_line20
    g "And besides, you’ve been leading this camp for many years now. While we had some setbacks, your performance the previous term was enough to prove that you have what it takes to carry the torch someday."

    show cgg2 15 with Dissolve(0.25)
    voice audio.yoshi_vsg3_line14
    yo "You flatter me too much, sir…"

    voice audio.goro_vsg3_line21
    g "You know, the reason I gave you that badge is the same reason I brought you to this business meeting today."

    voice audio.goro_vsg3_line22
    g "As much as I’m your superior, I want us to lead Camp Buddy side by side, just like we did back then…"

    voice audio.goro_vsg3_line23
    g "I know that your intentions are in the right place, and they go beyond just for the sake of the camp, exactly like what I saw in you that day.  "

    voice audio.yoshi_vsg3_line15
    yo "Sir Goro…"

    show cgg2 16 with Dissolve(0.25)
    voice audio.goro_vsg3_line24
    g "So, you better pay close attention to this meeting and learn something from it, or else I won’t let you come along next time!  "

    voice audio.yoshi_vsg3_line16
    yo "Yes, sir! I’ll do my best!"

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black with fade

    yo "{i}Sir Goro is trying his best to open up around me, reminiscing about the past and chatting casually.{/i}"
    yo "{i}It’s really refreshing to be able to talk to him on such a personal level, and not just about work… {/i}"
    yo "{i}I’ll make sure to show Sir Goro that he was right to place his trust in me!{/i}"

    scene cg black
    hide screen location
    hide screen timeline
    hide screen quick_menu
    $quick_menu = False
    with fade
    $ renpy.pause (2.0, hard=True)

    $ location = location_clermont
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_clermontlobby_day with fade
    play music close_distance loop

    show goro_semiformal at left2
    show goro norm1 at left2
    show yoshi_semiformal at right2
    show yoshi shock3 at right2
    voice audio.yoshi_v_amazed1d
    yo "W-Wow… So, this is where Mr. Clermont works…?"

    show goro play3 at left2
    voice audio.goro_v_heh1a
    g "Yeah… Fancy, isn’t it? I was surprised too the first time I came here."

    show yoshi awkward4 at right2
    voice audio.yoshi_v_amazed2b
    yo "I still can’t believe that someone like Mr. Clermont really sponsored Camp Buddy…"

    show goro comp2 at left2
    voice audio.goro_v_conj9a1
    g "We really have to thank Mr. Nagame and his friends for that… "
    g "While Mr. Clermont was impressed by our camp, I think their story was really what convinced him to support us like this."

    hide yoshi_semiformal
    hide yoshi awkward4
    show yoshi_semiformal at right2
    show yoshi norm3 at right2
    show goro shock1 at left2
    fd "Mr. Nomoru? Mr. Clermont would like to see you now!"

    show goro happy2 at left2
    voice audio.goro_v_rush1d1
    g "That’s our cue. Let’s go!"

    hide yoshi_semiformal
    hide yoshi norm3
    show yoshi_semiformal at right2
    show yoshi shy2 at right2
    voice audio.yoshi_v_gulp1a
    yo "*gulp* Suddenly, I’m feeling nervous."

    hide goro_semiformal
    hide goro happy2
    show goro_semiformal at left2
    show goro bold2 at left2
    voice audio.goro_v_confident1a
    g "It’ll be fine, Yoshinori. Just follow my lead."

    hide yoshi_semiformal
    hide yoshi shy2
    show yoshi_semiformal at right2
    show yoshi talk1 at right2
    voice audio.yoshi_v_right4
    yo "R-Right!"

    scene cg black
    hide screen location
    hide screen timeline
    hide screen quick_menu
    $quick_menu = False
    with fade
    $ renpy.pause (2.0, hard=True)

    $ location = location_clermont
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_clermontoffice_day with fade
    play music old_familiar_home loop

    show william_formal at left
    show william norm1 at left
    show goro_semiformal at center
    show goro happy1 at center
    show yoshi_semiformal at right
    show yoshi norm3 at right
    voice audio.goro_v_goodam2a2
    g "Good day, Mr. Clermont."

    show william happy1 at left
    voice audio.william_v_surprised1b
    w "Ahh! It’s been a while, Mr. Nomoru!"

    show goro happy2 at center
    voice audio.goro_v_request4a1
    g "I hope you don’t mind, but I brought my head scoutmaster with me today – this is Yoshinori Nagira."
    g "I apologize for not informing you beforehand."

    show william comp4 at left
    voice audio.william_v_comp1b
    w "No problem at all! I believe we met when I visited your camp the first time, didn’t we, Mr. Nagira?"

    show yoshi happy2 at right
    voice audio.yoshi_v_yessir1
    yo "Yes, sir! It’s a pleasure to meet you again as well, Mr. Clermont!"

    show william explain3 at left
    voice audio.william_v_request1
    w "And we’re right on time, so let’s get straight to business, shall we?"

    show goro talk1 at center
    voice audio.goro_v_yessir1a1
    g "Yes, sir."

    show william happy2 at left
    voice audio.william_v_anyway1
    w "So, I’ve got a bit of good news for you – as you may know, the little book “Greatest Memories” that we’ve published has been on the shelves and online stores for over a month."
    w "I’d like to congratulate you both, as it’s our most outstanding release yet! It generated a lot more sales than we anticipated!"

    show yoshi shock5 at right
    voice audio.yoshi_v_amazed1d
    yo "O-Oh, wow… That’s really amazing! "

    show william laugh2 at left
    voice audio.william_v_laugh1
    w "It seemed the public recognized the potential I saw from it and your camp. It was such a breath of fresh air from anything that’s out there in the market!"

    show william amazed3 at left
    voice audio.william_v_conj1a
    w "And as they say, “strike while the iron is hot”; the good publicity we’re getting from the book is a great opportunity to divert into the camp itself!"
    w "With the majority of the sales being allocated for upgrades around Camp Buddy, we’re able to offer a full sponsorship for many years to come!"

    show goro comp5 at center
    voice audio.goro_v_thanks3a
    g "Thank you so much again for seeing the worth of our camp, Mr. Clermont. "

    show william happy2 at left
    voice audio.william_v_conj4
    w "I believe this is more than just a business – it’s about what your place stands for in this generation!"

    show goro happy1 at center
    voice audio.goro_v_glad1a
    g "I’m glad we’re on the same page, sir!"

    show william think2 at left
    voice audio.william_v_conj5
    w "Moving forward, let’s discuss our upgrade plans."
    w "You are familiar with the Federation of Unified Camping Boy Scouts, or FUCBoyS, I believe?"

    show goro talk3 at center
    voice audio.goro_v_agree3a1
    g "Yes, of course, we follow their guidelines for most of our camp activities."

    show william talk1 at left
    voice audio.william_v_think1
    w "I have conducted a meeting with their association and asked for a business consultation on how to improve the camp."
    w "The insight from these professionals gave us a huge scope of potential upgrades with the budget that we have."

    show william comp2 at left
    voice audio.william_v_agree1a
    w "Of course, with the camp president’s approval and go signal."

    show goro confused3 at center
    voice audio.goro_v_ah1b
    g "Ah… May I ask what upgrades they specifically suggested?"

    show william laugh1 at left
    voice audio.william_v_well1a
    w "Well, we would be here all day if we discussed each and every bullet."
    w "But to give you a preface, it’s mostly expansions to the camp! "

    show cg fade at truecenter
    show fx3 at fx_pos
    with dissolve

    voice audio.william_v_conj3a
    w "I was made aware that the annex area beside the camp was meant for upgrades. This was the biggest job that they suggested."
    w "The FUCBoyS Association figured that since we’re expecting more campers next term, they would like to build more cabins and facilities!"

    voice audio.goro_v_actually1a
    g "It’s something we’ve foreseen as well. In fact, we actually began refurbishing old, run-down cabins last summer in preparation for the next term."

    hide cg fade
    hide fx3
    with dissolve

    show william amazed2 at left
    voice audio.william_v_amazed2
    w "That’s great! That should help us get a head start on the biggest chunk of the work."
    w "However, there are equally important suggestions on top of this, such as technology integration, gear upgrades and a new curriculum to establish safety interests."

    hide goro_semiformal
    hide goro confused3
    show goro_semiformal at center
    show goro shock2 at center
    voice audio.goro_v_oh2b
    g "Oh… This is beyond what I expected…"

    show william happy2 at left
    voice audio.william_v_comp3
    w "I’ll email you the specifics on each topic so you can consider them thoroughly."

    hide goro_semiformal
    hide goro shock2
    show goro_semiformal at center
    show goro talk1 at center
    voice audio.goro_v_response1c2
    g "Understood. I’ll make sure to review everything carefully."
    g "I appreciate all the work you’ve put into sponsoring our camp, Mr. Clermont. I am extremely grateful."

    show yoshi comp2 at right
    voice audio.yoshi_v_thanks2
    yo "Yes, we can’t thank you enough, Mr. Clermont!"

    show william comp4 at left
    voice audio.william_v_comp1a
    w "Like I said before, it’s my pleasure to be a part of your cause."

    show william talk1 at left
    voice audio.william_v_conj1a
    w "Now, let’s move on and discuss when the project is expected to be completed."
    w "We are going to maintain the same target of at least a month before next year’s summer term begins."

    hide goro_semiformal
    hide goro talk1
    show goro_semiformal at center
    show goro think2 at center
    voice audio.goro_v_think1a1
    g "I would like to raise a concern about that, sir. "
    g "Just for the renovations alone, I don’t think our current staff will be capable of performing the construction labor in several months’ time."

    show william laugh1 at left
    voice audio.william_v_laugh3
    w "Hahahaha! Why, I wouldn’t put you in such an impossible situation, Mr. Nomoru!"
    w "It’s unreasonable to ask your team of four people to handle all of this. "

    hide goro_semiformal
    hide goro think5
    show goro_semiformal at center
    show goro talk2 at center
    voice audio.goro_v_conj7a
    g "On that note, please allow me some time to gather the required manpower to cater for all this work."

    show william happy3 at left
    voice audio.william_v_comp3
    w "I’ve already got it covered – I signed on with a contractor who will provide us a team of professionals with the best expertise to handle the work."

    hide goro_semiformal
    hide goro talk2
    show goro_semiformal at center
    show goro shock2 at center
    voice audio.goro_v_unsure1a1
    g "Oh… Isn’t that too much, sir? I mean… you’ve already funded the entire expansion."

    show william comp4 at left
    voice audio.william_v_impressed1a
    w "Consider this as part of the sponsorship. All you’ll need to do as the camp president is give me your approval on the upgrade plans we proposed."
    w "That, and to assign one of your staff to coordinate with whichever representatives I will send to the site on my behalf. Now, isn’t that convenient for both of us?"

    hide goro_semiformal
    hide goro shock2
    show goro_semiformal at center
    show goro amazed2 at center
    voice audio.goro_v_thanks2a1
    g "It is, sir. Thank you very much for your generosity."
    g "When is our official starting date for the project, if I may ask?"

    show william talk2 at left
    voice audio.william_v_rush1a
    w "I would say as soon as possible since our deadline is tight. "
    w "As a matter of fact, I can send a team as early as tomorrow to give them ample time to settle in and familiarize with the site, if that’s alright on your end."

    hide yoshi_semiformal
    hide yoshi comp2
    show yoshi_semiformal at right
    show yoshi awkward4 at right
    voice audio.yoshi_v_what3
    yo "Wh-What…? Tomorrow?"

    show goro happy1 at center
    voice audio.goro_v_agree7a
    g "I agree with you, Mr. Clermont. I’ll have my staff prepare for their arrival. We’ll allot some of the vacant cabins for temporary housing throughout the construction."

    show william explain2 at left
    voice audio.william_v_think1
    w "We’ll set a daily schedule and send off teams by their specialty until all the required workforce has been fully mobilized at the camp."
    w "I know this may be a little overwhelming, but I assume it’s not new to you to be handling a large amount of people working on a common goal."

    show goro bold2 at center
    voice audio.goro_v_agree6a2
    g "That’s right. I’m confident we can manage."

    show william talk3 at left
    voice audio.william_v_conj7
    w "Lastly, we have to cover the legal side of this project. If we’re aiming to move in tomorrow and start immediately, we’ll require the documentations and permits."

    show goro talk1 at center
    voice audio.goro_v_conj6a1
    g "About that, I’ve been working with the local city hall ever since the end of the previous term. The good news is that I was able to secure all the necessary paperwork."
    g "I will make the needed adjustments based on the updated scope we discussed today, and I’ll head there tomorrow to claim all the permits."

    show william happy3 at left
    voice audio.william_v_impressed2b
    w "Excellent! It really shows how much you have prepared for this, Mr. Nomoru."

    show goro comp2 at center
    voice audio.goro_v_response2a2
    g "It’s honestly the least I could do, sir. "
    g "You can count on my staff and I to do our part throughout this entire project. "

    show william laugh1 at left
    voice audio.william_v_laugh2
    w "Hahaha, of course. Now, I believe we’ve covered all matters that needed to be discussed today?"

    show goro happy1 at center
    voice audio.goro_v_response1a2
    g "Indeed. We won’t take up any more of your time."

    show william happy1 at left
    voice audio.william_v_bye1b
    w "Alright then, this meeting is adjourned! We’ll see each other next week for another meeting."

    show goro laugh3 at center
    voice audio.goro_v_thanks2a1
    g "Yes, sir. Thank you for today."

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

    $ location = location_clermont
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_clermontlobby_day with fade
    play music close_distance loop

    show yoshi_semiformal at left2
    show yoshi sigh1 at left2
    show goro_semiformal at right2
    show goro norm1 at right2
    voice audio.yoshi_v_relief1
    yo "Whew…"

    show goro play3 at right2
    voice audio.goro_v_so3a
    g "So…? How was your first professional meeting?"

    $working = False
    $shuffle_menu()
    menu():
        g "So…? How was your first professional meeting?{fast}"
        "It was a little stressful.":
            $working = True
            $score_goro -= 1
            show yoshi worry2 at left2
            voice audio.yoshi_v_conj4a
            yo "Honestly, it stressed me out a little. "

            show yoshi sigh1 at left2
            voice audio.yoshi_v_sigh2
            yo "The conversation moved so fast that I didn’t know when I was supposed to talk, or even have time to process the information! "
            yo "At some point, I felt bad that I wasn’t contributing anything to the discussion."

            show goro comp2 at right2
            voice audio.goro_v_comp2a2
            g "Don’t worry, I wasn’t expecting you to actively participate. I understand that this was something out of your comfort zone."

            show goro explain3 at right2
            voice audio.goro_v_conj5a
            g "Regardless, it’s a good thing to experience."
            g "A busy man like Mr. Clermont can only spare us a little time, so it’s important to get straight to the point and accomplish as much as possible in every meeting."

            hide yoshi_semiformal
            hide yoshi sigh1
            show yoshi_semiformal at left2
            show yoshi talk1 at left2
            voice audio.yoshi_v_response1a
            yo "I understand, sir."
        "It's so different from back at camp.":
            $working = True
            $score_goro -= 1
            show yoshi worry2 at left2
            voice audio.yoshi_v_conj4a
            yo "It was… pretty nerve-racking… It’s so different from the ones we usually have back at camp."

            show yoshi sigh1 at left2
            voice audio.yoshi_v_sigh2
            yo "The conversation moved so fast that I didn’t know when I was supposed to talk, or even have time to process the information!"
            yo "At some point, I felt bad that I wasn’t contributing anything to the discussion."

            show goro comp2 at right2
            voice audio.goro_v_comp2a2
            g "Don’t worry, I wasn’t expecting you to actively participate. I understand that this was something out of your comfort zone."

            show goro explain3 at right2
            voice audio.goro_v_conj5a
            g "Regardless, it’s a good thing to experience."
            g "A busy man like Mr. Clermont can only spare us a little time, so it’s important to get straight to the point and accomplish as much as possible in every meeting."

            hide yoshi_semiformal
            hide yoshi sigh1
            show yoshi_semiformal at left2
            show yoshi talk1 at left2
            voice audio.yoshi_v_response1a
            yo "I understand, sir."
        "It's a good thing you were there.":
            $working = True
            $score_goro += 1
            hide yoshi_semiformal
            hide yoshi sigh1
            show yoshi_semiformal at left2
            show yoshi comp2 at left2
            voice audio.yoshi_v_amazed3
            yo "It’s a good thing you were there, sir."
            yo "Mr. Clermont brought up a lot of things that required decisions on the spot, and you were able to cater to all of them."

            show yoshi sigh1 at left2
            voice audio.yoshi_v_sigh2
            yo "I could barely keep up with the pace of the discussion. I wish I could've contributed as much as you did!"

            show goro comp2 at right2
            voice audio.goro_v_comp2a2
            g "You’ll learn with more experience. A busy man like Mr. Clermont can only spare us so much time, so I had to be sure to respect that. "
            g "It’s important to get straight to the point and accomplish as much as possible in every meeting."

            show goro comp5 at right2
            voice audio.goro_v_conj9a1
            g "But honestly, they aren’t that different from our own meetings back at camp."

            show yoshi happy1 at left2
            voice audio.yoshi_v_response1b
            yo "I understand, sir!"
        "You had everything under control.":
            $working = True
            $score_goro += 2
            hide yoshi_semiformal
            hide yoshi sigh1
            show yoshi_semiformal at left2
            show yoshi bold2 at left2
            voice audio.yoshi_v_amazed3
            yo "I was really impressed at how well you handled everything, sir!"
            yo "Even though the conversation moved quickly, you were able to keep up with every concern Mr. Clermont brought up."

            show yoshi sigh1 at left2
            voice audio.yoshi_v_sigh2
            yo "You even made a lot of important decisions on the spot… I’m not sure I could have done that!"

            show goro comp2 at right2
            voice audio.goro_v_comp2a2
            g "You’ll learn with more experience. A busy man like Mr. Clermont can only spare us so much time, so I had to be sure to respect that. "
            g "It’s important to get straight to the point and accomplish as much as possible in every meeting."

            show goro comp5 at right2
            voice audio.goro_v_conj9a1
            g "But honestly, they aren’t that different from our own meetings back at camp."

            show yoshi happy1 at left2
            voice audio.yoshi_v_response1b
            yo "I understand, sir!"

    hide goro_semiformal
    hide goro play3
    show goro_semiformal at right2
    show goro tease5 at right2
    voice audio.goro_v_heh1a
    g "Heh, you should’ve seen the look on your face the entire meeting, Yoshinori. You looked like a lost kid in a mall."

    show yoshi panic4 at left2
    voice audio.yoshi_v_shock4
    yo "G-Gah…! Was it that bad? I hope Mr. Clermont didn’t notice."

    hide goro_semiformal
    hide goro tease5
    show goro_semiformal at right2
    show goro laugh5 at right2
    voice audio.goro_v_laugh2b1
    g "It seems like your lucky charm didn’t work one bit. Hahaha!"

    hide yoshi_semiformal
    hide yoshi panic4
    show yoshi_semiformal at left2
    show yoshi sigh3 at left2
    voice audio.yoshi_v_sigh3a
    yo "*sigh* I don’t know how you do it, sir."

    show goro happy1 at right2
    voice audio.goro_v_comp4a
    g "If you do a certain thing over and over, you’ll realize it’s not as complicated as you think."

    hide goro_semiformal
    hide goro happy1
    show goro_semiformal at right2
    show goro happy2 at right2
    voice audio.goro_v_conj3a1
    g "But I have to admit, it was nice to have your company here for once."
    g "In a way, it made me more confident having you around for the meeting."

    show goro tease2 at right2
    voice audio.goro_v_heh1a
    g "Also, watching you sweat from nervousness was rather entertaining. "

    show yoshi shy6 at left2
    voice audio.yoshi_v_unsure1b
    yo "Now I’m not sure if you should let me tag along next time…."

    hide goro_semiformal
    hide goro tease2
    show goro_semiformal at right2
    show goro laugh1 at right2
    voice audio.goro_v_laugh2b1
    g "Hahaha!"

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black with fade

    yo "{i}Sir Goro continued to tease and chat with me on the car ride back… It was actually really fun to see him loosened up like that.{/i}"
    yo "{i}Time flew by, and before I knew it, we were back at Camp Buddy.{/i}"
    yo "{i}Sir Goro immediately called a meeting with the other scoutmasters to prepare for the workers’ arrival tomorrow.{/i}"

    scene cg black
    hide screen location
    hide screen timeline
    hide screen quick_menu
    $quick_menu = False
    with fade
    $ renpy.pause (2.0, hard=True)
    $ time_transition_day_to_sunset_fall()

    $ location = location_office
    $ time = timeline_timesunset
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_office_autumn_sunset with fade
    play music ready_for_tomorrow loop

    show goro_semiformal at p4_1
    show goro talk1 at p4_1
    show yoshi_semiformal at p4_2
    show yoshi norm1 at p4_2
    show aiden_autumn at p4_3
    show aiden norm1 at p4_3
    show yuri_autumn at p4_4
    show yuri norm1 at p4_4
    voice audio.goro_v_so1a
    g "So that wraps up everything. I’ve given you the in-depth details of the renovations that Mr. Clermont gave me so that we’re all equally clear."

    show aiden shock5 at p4_3
    voice audio.aiden_v_shock1b1
    a "Woah, this is a really huge deal, Gramps… Looking at everything, this is gonna cost a fortune!"

    show yuri explain2 at p4_4
    voice audio.yuri_v_well1a
    yu "Well, Dad said that everything in the construction will be covered by the sponsorship."

    show yoshi talk1 at p4_2
    voice audio.yoshi_v_right5
    yo "That’s right. The only things that are not covered are the miscellaneous stuff that we need. But all of that should be handled by the fundraising that we did last year."

    show goro talk3 at p4_1
    voice audio.goro_v_anyway2
    g "Anyway, is everyone clear on the tasks I’ve given you?"

    show yuri happy1 at p4_4
    voice audio.yuri_v_agree1b1
    yu "Yes! I’ll be coordinating with the contractors tomorrow to tour them around the camp and provide them accommodations!"

    show aiden laugh1 at p4_3
    voice audio.aiden_v_agree1a1
    a "Yep, and I’ll be making sure the workers are fed and keeping up the regular maintenance."

    show goro explain2 at p4_1
    voice audio.goro_v_yoshi2a
    g "As for you, Yoshinori. I will leave you in charge of overseeing the schedule we have planned for this week while I take care of the remaining paperwork."

    show yoshi happy1 at p4_2
    voice audio.yoshi_v_yessir2
    yo "Yes, sir! You can count on me!"

    show goro happy1 at p4_1
    voice audio.goro_v_amazed2a1
    g "Great! If we’re all clear, then this meeting is adjourned."

    hide yuri_autumn
    hide yuri happy1
    show yuri2_autumn at p4_4
    show yuri2 excited3 at p4_4
    voice audio.yuri_v_kyaa1a
    yu "Kyaa~ I’m really excited! If everything goes well, I’m sure it’ll be Camp Buddy’s peak! "
    yu "Just imagine all of the activities I’ll be able to do now that we have a bigger budget, hehehe…"

    show aiden tease1 at p4_3
    voice audio.aiden_v_laugh1a1
    a "Hehe, knowing you, you’d probably throw another costume party."

    hide yuri2_autumn
    hide yuri2 excited3
    show yuri_autumn at p4_4
    show yuri excited2 at p4_4
    voice audio.yuri_v_laugh2a4
    yu "That was one of the best ideas I had last summer! I have plenty of other “sexier” ideas for everyone to enjoy~! Hehehe…"

    hide yoshi_semiformal
    hide yoshi happy1
    show yoshi_semiformal at p4_2
    show yoshi sigh4 at p4_2
    voice audio.yoshi_v_sigh3a
    yo "*sigh* You know we’re supposed to use the budget for improvements, Yuri…"

    hide goro_semiformal
    hide goro happy1
    show goro_semiformal at p4_1
    show goro disappoint2 at p4_1
    voice audio.goro_v_ehem1a
    g "*ahem* Yoshinori’s right. Let’s not go overboard and stick to our plans. "

    show yuri pout4 at p4_4
    voice audio.yuri_v_idea2a
    yu "I know, I know! Now, why don’t you two get out of your fancy suits and take the rest of the night off? "

    show aiden play3 at p4_3
    voice audio.aiden_v_wait2b1
    a "Hold on, they do look sleek and stylish in those outfits! How about we celebrate first? "
    a "I have a huge roasted chicken sitting in the oven, and I’m sure it would go well with some champagne!"

    show aiden bold2 at p4_3
    voice audio.aiden_v_rush1a1
    a "We might not get a chance for something like this again with how busy we’ll get, after all! "

    show yuri angry2 at p4_4
    voice audio.yuri_v_what5a
    yu "What?! You’re gonna drink again?! No way! Especially when we’re expecting new people tomorrow! "
    yu "The last thing I want is you guys being groggy and hungover as our first impression!"

    show goro sigh1 at p4_1
    voice audio.goro_v_sigh1a
    g "*sigh* As much as I would love a drink tonight to relax… Yuri has a point. "

    show yuri annoy2 at p4_4
    voice audio.yuri_v_alright1d1
    yu "We can celebrate with the roasted chicken, but let’s lay off on the alcohol for now, alright?!"

    show aiden wink1 at p4_3
    voice audio.aiden_v_alright2a
    a "Alright, alright. No drinks for tonight! Right, Yoshi and Gramps? *wink wink*"

    show yuri pout1 at p4_4
    voice audio.yuri_v_hey3a
    yu "Hey, I saw that!!"

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

    $ location = location_messhall
    $ time = timeline_timenight
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_messhall_autumn_night with fade
    play music sunset_stroll loop

    show taiga_autumn at p6_1
    show taiga normal3 at p6_1
    show yoichi_autumn at p6_2
    show yoichi angry6 at p6_2
    show yuri_autumn at p6_3
    show yuri norm1 at p6_3
    show aiden_autumn at p6_4
    show aiden norm1 at p6_4
    show yoshi_semiformal at p6_5
    show yoshi norm1 at p6_5
    show goro_semiformal at p6_6
    show goro norm1 at p6_6
    voice audio.yoichi_v_groan2c4
    yi "UGH! FINALLY, you old geezers are here! We’ve been waiting here all day!"

    show taiga annoyed4 at p6_1
    voice audio.taiga_v_yoichi8
    t "Yoichi, it’s only been ten minutes. "

    show yoichi angry3 at p6_2
    voice audio.yoichi_v_shock3a7
    yi "Gah! I don’t care! Time moves slower when I’m hungry!"

    show yoshi comp2 at p6_5
    voice audio.yoshi_v_sorry5a
    yo "We’re sorry about that! We just had a meeting to take care of! "

    hide yoichi_autumn
    hide yoichi angry3
    show yoichi_autumn at p6_2
    show yoichi annoyed6 at p6_2
    voice audio.yoichi_v_angry1d
    yi "Tch. You guys keep acting so busy even when there’s nobody here.  "
    yi "And I bet you forgot about us again! I haven’t seen any of you since yesterday!"

    show taiga sigh2 at p6_1
    voice audio.taiga_v_ugh1
    t "Ugh… He’s always like this when it’s his feeding time… I told him we could just heat up whatever’s in the fridge."

    hide yoichi_autumn
    hide yoichi annoyed6
    show yoichi_autumn at p6_2
    show yoichi annoyed4 at p6_2
    voice audio.yoichi_v_disagree1a5
    yi "No way I’m eating leftovers again! Besides, I can smell they’re hiding the goods here! This nose doesn’t lie!"

    show yuri laugh1 at p6_3
    voice audio.yuri_v_yoichi7a
    yu "Well, today’s your lucky day, Yoichi~! Aiden cooked up something special for dinner!"

    show aiden laugh1 at p6_4
    voice audio.aiden_v_laugh2a1
    a "Haha! I better get that ready to serve before Yoichi loses it! Be right back!"

    hide aiden_autumn
    hide aiden laugh1
    with dissolve

    show taiga_autumn at p5_1
    show taiga sigh2 at p5_1
    show yoichi_autumn at p5_2
    show yoichi annoyed4 at p5_2
    show yuri_autumn at p5_3
    show yuri laugh1 at p5_3
    show yoshi_semiformal at p5_4
    show yoshi comp2 at p5_4
    show goro_semiformal at p5_5
    show goro norm1 at p5_5
    with move

    show taiga_autumn at p5_1
    show taiga confused1 at p5_1
    voice audio.taiga_v_confused2a
    t "Soooo… what’s up with the suits? It’s been a long time since I’ve seen you guys wear something so formal."

    show yoshi talk3 at p5_4
    voice audio.yoshi_v_ah1
    yo "Ah, we had a meeting with Mr. Clermont earlier today."

    show yoichi confused3 at p5_2
    voice audio.yoichi_v_confused1a4
    yi "Why’d you dress like pimps for a boring meeting?"

    show goro sigh3 at p5_5
    voice audio.goro_v_sigh1a
    g "*sigh* To think I spent so much on this outfit just to look like that…"

    show yoichi talking2 at p5_2
    voice audio.yoichi_v_laugh1a5
    yi "Pimps have a lot of money too, you know."

    show yoshi angry2 at p5_4
    voice audio.yoshi_v_yoichi7
    yo "Yoichi! There’s no way either of us, especially Sir Goro, would do something like that!"

    show yoichi talking4 at p5_2
    voice audio.yoichi_v_hmph1a
    yi "Whatever you say, simp. "

    show yoshi sigh4 at p5_4
    voice audio.yoshi_v_sigh3a
    yo "*sigh*"

    show taiga confused3 at p5_1
    voice audio.taiga2_v_thinking2a
    t "What was the meeting about anyway? It must’ve been super important for you guys to dress up like that."

    show yoshi happy1 at p5_4
    voice audio.yoshi_v_actually3a
    yo "It was a huge deal, actually… Keitaro’s book did so well on the market that Mr. Clermont offered an even bigger budget to improve the camp."

    show goro talk2 at p5_5
    voice audio.goro_v_request2a2
    g "With the sponsorship going into effect, things are going to be busy from now on, and I expect you both to do your best to help out as much as you can."

    show taiga excited1 at p5_1
    voice audio.taiga2_v_excited2a
    t "Not sure about Yoichi here, but I’ve been waiting for something to work on! Time here has been really slow during the off-season, after all."

    show yoichi_autumn at p5_2
    show yoichi talking2 at p5_2
    voice audio.yoichi_v_greet1b1
    yi "Hey, it’s better than dying of boredom. These muscles could use some working out anyways."

    show yoshi bold2 at p5_4
    voice audio.yoshi_v_encourage3
    yo "Now that’s the spirit! I hope you’ll keep that positive attitude for when all the new workers arrive tomorrow and start working!"

    show yoichi_autumn at p5_2
    show yoichi annoyed4 at p5_2
    voice audio.yoichi_v_groan2a1
    yi "Oh, great… New people. "

    hide yoshi_semiformal
    hide yoshi bold2
    show yoshi_semiformal at p5_4
    show yoshi comp3 at p5_4
    voice audio.yoshi_v_please1a
    yo "Please at least try and get along with them, Yoichi."

    show yoichi_autumn at p5_2
    show yoichi annoyed1 at p5_2
    voice audio.yoichi_v_well1b
    yi "Well, I guess I could use some new faces around here. I’m tired of seeing Dynamite and hearing him nag every day. "

    show taiga angry5 at p5_1
    voice audio.taiga_v_disagree1
    t "You’re one to talk! Being stuck here with you is so exhausting – it made me miss having Eduard and Lee around instead."

    show yoichi annoyed5 at p5_2
    voice audio.yoichi_v_angry1d
    yi "Same goes for you! I’d rather hang out with Mr. Perfect or Twinkerbell, or even that annoying Torch-head!"

    show yuri comp2 at p5_3
    voice audio.yuri_v_aww2a
    yu "Aww~ look at you guys, missing your friends! That’s really cute! Have you been keeping in touch at least?"

    show taiga compassion5 at p5_1
    voice audio.taiga2_v_agree3a
    t "Yeah, we have! Even though everyone has started getting busy with their own things, we still find time to catch up with each other.  "

    show yoichi playful1 at p5_2
    voice audio.yoichi_v_agree1a1
    yi "Yeah, I guess that time we had a group call was kinda fun. Better than hearing Dynamite’s annoying voice all the time."

    show taiga_autumn at p5_1
    show taiga angry6 at p5_1
    voice audio.taiga_v_ugh1
    t "Ugh…"

    show yuri tease2 at p5_3
    voice audio.yuri_v_well1a
    yu "Well, aren’t you two getting along just nicely~"

    show taiga_autumn at p6_1
    show taiga angry6 at p6_1
    show yoichi_autumn at p6_2
    show yoichi playful1 at p6_2
    show yuri_autumn at p6_3
    show yuri tease2 at p6_3
    show yoshi_semiformal at p6_4
    show yoshi comp3 at p6_4
    show goro_semiformal at p6_5
    show goro talk2 at p6_5
    with move

    show aiden_autumn at p6_6
    show aiden comp5 at p6_6
    with dissolve
    voice audio.aiden_v_sorry1a1
    a "Sorry it took so long! I had to whip up some mashed potatoes too! "

    show taiga_autumn at p6_1
    show taiga angry6 at p6_1
    show yuri_autumn at p6_2
    show yuri tease2 at p6_2
    show yoshi_semiformal at p6_3
    show yoshi comp3 at p6_3
    show goro_semiformal at p6_4
    show goro talk2 at p6_4
    show yoichi_autumn at p6_5
    show yoichi playful1 at p6_5
    with move

    voice audio.yoichi_v_groan2c2
    yi "UGH, GREAT!!! I’m starving!! "

    show yuri_autumn at p6_1
    show yuri tease2 at p6_1
    show yoshi_semiformal at p6_2
    show yoshi comp3 at p6_2
    show goro_semiformal at p6_3
    show goro talk2 at p6_3
    show taiga_autumn at p6_4
    show taiga angry6 at p6_4
    with move

    show taiga_autumn at p6_4
    show taiga angry2 at p6_4
    voice audio.taiga2_v_hey1h
    t "H-Hey! Stop hogging all the food! Save the thigh part of the chicken for me! "

    show yoichi playful3 at p6_5
    voice audio.yoichi_v_bye2b
    yi "You snooze, you lose! "

    show aiden comp3 at p6_6
    voice audio.aiden_v_conj4a
    a "Now, now, there’s plenty for everybody! "

    show yuri excited2 at p6_1
    voice audio.yuri_v_bye3a
    yu "I’ll go set the table!"

    hide yuri_autumn
    hide yuri excited2
    with dissolve

    show yoshi_semiformal at p6_1
    show yoshi comp3 at p6_1
    show goro_semiformal at p6_2
    show goro talk2 at p6_2
    with move

    hide yoshi_semiformal
    hide yoshi comp3
    show yoshi_semiformal at p6_1
    show yoshi comp1 at p6_1
    yo "..."

    hide goro_semiformal
    hide goro talk2
    show goro_semiformal at p6_2
    show goro play3 at p6_2
    voice audio.goro_v_laugh1a1
    g "Hehe… I told you, you’re already doing a good job. Just look how much those two have grown."

    show yoshi comp2 at p6_1
    voice audio.yoshi_v_right9
    yo "You’re right, sir… I couldn’t be prouder."

    hide goro_semiformal
    hide goro play3
    show goro_semiformal at p6_2
    show goro bold2 at p6_2
    voice audio.goro_v_rush2a1
    g "Why don’t we join them? We had a long day, and I think we’ve earned a good meal."

    show yoshi happy1 at p6_1
    voice audio.yoshi_v_right2
    yo "R-Right! "

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black with fade
    yo "{i}After a busy day handling all the camp’s business with Sir Goro, we made sure to enjoy our time together, just the six of us. {/i}"
    yo "{i}Knowing how much change was coming starting tomorrow, it makes me feel thankful for the simple times like this I get to spend with everyone.{/i}"

    $persistent.profile_unlock.append("taiga")
    $persistent.profile_unlock.append("yoichi")
    $persistent.profile_unlock.append("william")
    scene cg black
    hide screen location
    hide screen timeline
    hide screen quick_menu
    $quick_menu = False
    with fade
    play sound sleeping_time
    $ time_transition_night_to_day_fall()
    $ renpy.pause (2.0, hard=True)
    jump day3
