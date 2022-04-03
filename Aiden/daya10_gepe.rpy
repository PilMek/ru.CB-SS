image entrance_transition:
    "images/bgs/bg-w-entrance-day.png"
    pause 1.0
    "images/bgs/bg-p-entrance-day.png" with Dissolve(4.0)

label day10_aiden_gepe:
    $ day = "84"
    $ time = timeline_timeday
    $ location = location_cabin
    show screen location
    show screen timeline
    show screen quick_menu
    $ quick_menu = True
    $working = True
    scene bg_quarters_winter_day with fade
    play music go_with_the_flow_slow loop
    play bgsound sfxloop_birds loop

    show aiden2_autumn at left2
    show aiden2 sad4 at left2
    show yoshi_autumn at right2
    show yoshi sad1 at right2
    voice audio.william_v_aiden1d
    w "That’s truly unfortunate, Mr. Flynn… I had no doubt you would’ve been a breakout star in the culinary industry."

    hide aiden2_autumn
    hide aiden2 sad4
    show aiden_autumn at left2
    show aiden comp2 at left2
    voice audio.aiden_v_william2b
    a "I understand, Mr. Clermont, but I’m already satisfied with where I am."
    a "I know I’ll be happy being Camp Buddy’s special chef!"

    voice audio.william_v_laugh1
    w "Haha, well it sounds like you’ve fully made up your mind! I won’t try and convince you any further!"
    w "You can relax and not concern yourself about this anymore, but I would like to express that the offer will stay on the table!"
    w "Consider it an open opportunity should you ever change your mind."

    show aiden comp5 at left2
    voice audio.aiden_v_thanks2a
    a "I really appreciate your generosity, Mr. Clermont. Thank you for giving me a chance."

    voice audio.william_v_bye2b
    w "Of course! Until next time!"

    play sound sfx_phonebutton
    hide aiden_autumn
    hide aiden comp5
    show aiden2_autumn at left2
    show aiden2 sigh3 at left2
    voice audio.aiden_v_relief1b2
    a "Whew… Well, that happened."

    show yoshi comp2 at right2
    voice audio.yoshi_v_praise1
    yo "You did great, Aiden! You were very professional, and everything you said came from the heart.   "
    yo "You didn’t need my help talking to Mr. Clermont after all!"

    show aiden2 worry2 at left2
    voice audio.aiden_v_yeah1c2
    a "Yeah… Usually talking about serious stuff like that over the phone gives me a little bit of anxiety."
    a "Especially when it’s about turning down something I tried reaching for in the past."

    show aiden2 sad4 at left2
    voice audio.aiden_v_well1c2
    a "After my dad passed, I was so determined to pursue cooking knowing it was the one thing I was really good at."
    a "I went back to working all sorts of jobs to make money and save for a degree."

    show aiden2 sigh3 at left2
    voice audio.aiden_v_actually4a
    a "In my head, I wasn’t just following in my dad’s footsteps, but also trying to fulfill my end of our promise to be back together."

    hide yoshi_autumn
    hide yoshi comp2
    show yoshi2_autumn at right2
    show yoshi2 worry2 at right2
    voice audio.yoshi_v_aiden4
    yo "Aiden…"

    hide aiden2_autumn
    hide aiden2 sigh3
    show aiden_autumn at left2
    show aiden comp2 at left2
    voice audio.aiden_v_but1b1
    a "But then, in the middle of all that, I finally heard from you – asking me to come back to Camp Buddy."

    show yoshi2 sad4 at right2
    voice audio.yoshi_v_well2
    yo "Well… It was only when I got the job here that I found out you lost your dad… "
    yo "So as soon as I knew the camp needed help, you were the first person to come to mind..."

    hide yoshi2_autumn
    hide yoshi2 sad4
    show yoshi_autumn at right2
    show yoshi comp2 at right2
    voice audio.yoshi_v_gratitude2
    yo "I’m really glad you decided to accept."

    show aiden sad5 at left2
    voice audio.aiden_v_sigh1a
    a "Even still, I tried to save face by convincing everyone that I was only coming back to make enough money for college. "
    a "When deep inside… All I wanted was to be back."

    hide aiden_autumn
    hide aiden sad5
    show aiden2_autumn at left2
    show aiden2 sigh1 at left2
    voice audio.aiden_v_sigh3a
    a "I wish I’d had the courage to ask you how exactly things went down when we were apart."
    a "I knew you were trying to move on, so I didn’t want to bring it up unless you did."

    hide yoshi_autumn
    hide yoshi comp2
    show yoshi2_autumn at right2
    show yoshi2 sad4 at right2
    voice audio.yoshi_v_sorry2b
    yo "I know it’s inexcusable, especially since I’m the only one you would’ve counted on."

    hide aiden2_autumn
    hide aiden2 sigh1
    show aiden_autumn at left2
    show aiden comp2 at left2
    voice audio.aiden_v_comp1b2
    a "Don’t blame yourself, Yoshi. I was the one who chose to hide everything from you."
    a "You were on your first job as an official scoutmaster at the time."

    show aiden explain2 at left2
    voice audio.aiden_v_conj1
    a "And considering you were left in charge of the entire camp with lots of staff and scouts, I saw how much you were dealing with."
    a "I really didn’t want to burden you more… I was just happy enough to be with you again."

    show yoshi2 comp1 at right2
    voice audio.yoshi_v_aiden4
    yo "Aiden…"
    yo "…I’d say your best quality is the way you always hold your head high and look at things so positively."

    show aiden tease1 at left2
    voice audio.aiden_v_laugh1c1
    a "Hehe, you sure it’s not my jacked bod and charming personality?"

    hide yoshi2_autumn
    hide yoshi2 comp1
    show yoshi_autumn at right2
    show yoshi play5 at right2
    voice audio.yoshi_v_agree1b2
    yo "Of course, I love that about you just as much."

    show yoshi talk1 at right2
    voice audio.yoshi_v_but2
    yo "But in all seriousness, you never showed anyone a sign of what you had to go through."
    yo "Not only were you always cheerful, but you were ready to help me and the camp out any way you could."

    show yoshi explain2 at right2
    voice audio.yoshi_v_aiden4
    yo "Even when everyone left Camp Buddy after last year’s scandal, you were the only who stuck around."
    yo "I honestly don’t know where I’d have ended up if you weren’t there for me…"

    show yoshi comp2 at right2
    voice audio.yoshi_v_thanks6
    yo "So, I’m really thankful, Aiden…"

    show aiden comp2 at left2
    voice audio.aiden_v_aww2a
    a "Aww, you’re gonna make me tear up, Yoshi…"

    show aiden happy2 at left2
    voice audio.aiden_v_but1a1
    a "But hey, you’ve done as much for me. And not just by taking me back and giving me a home again."
    a "Working with you these last few years made me feel useful – it helped me to move past my pain."

    show aiden comp5 at left2
    voice audio.aiden_v_glad1a
    a "And once you guys made me a scoutmaster, I really felt like I belonged here."
    a "I couldn’t have asked for anything more… So, I just wanted that to last for as long as I could."

    show yoshi happy1 at right2
    voice audio.yoshi_v_laugh1
    yo "And now, with the choice you made, it’s going to last forever."

    show aiden happy1 at left2
    voice audio.aiden_v_yeah1a1
    a "Yeah, exactly!"
    a "I used to believe that I didn’t have a choice with what life threw at me, so I just let things happen and felt content as they were."

    show aiden explain3 at left2
    voice audio.aiden_v_but1a1
    a "But if there’s something I realized from all this… I’ve always been making decisions for myself."
    a "From choosing to try and pursue a career despite failing, to accepting your offer to return and staying despite everything that happened along the way…"

    show aiden happy1 at left2
    voice audio.aiden_v_so2
    a "Now, I chose something I truly want for myself."

    show aiden comp2 at left2
    voice audio.aiden_v_thanks1c1
    a "So, thanks for staying by my side and supporting my decision, Yoshi."

    show yoshi comp2 at right2
    voice audio.yoshi_v_agree1a
    yo "Of course, Aiden… I’ll always be here for you. "

    show aiden relief4 at left2
    voice audio.aiden_v_relief1a1
    a "Phew… Finally, I got all that off my chest… "
    a "Making that decision gave me some real closure."
    a "I’m done being stuck in my ways and just going with the flow, sweeping every bad thing under the rug and thinking it’d all go away."

    show aiden bold2 at left2
    voice audio.aiden_v_alright1a3
    a "From now on, I won’t let anything take my happiness away! "

    show yoshi happy1 at right2
    voice audio.yoshi_v_encourage3
    yo "I’m really proud of you, Aiden!"

    hide aiden_autumn
    hide aiden bold2
    show aiden2_autumn at left2
    show aiden2 sigh4 at left2
    voice audio.aiden_v_sheesh1a
    a "Sheesh, so this is what it’s like to be cheesy."
    a "Can’t believe it took me this long to catch it from you, considering how much we’re stuck together. Hahaha!"

    show yoshi play2 at right2
    voice audio.yoshi_v_laugh3
    yo "I hate to break it to you but you’re just gonna have to deal with me forever."

    show yoshi shock1 at right2
    hide aiden2_autumn
    hide aiden2 sigh4
    show aiden_autumn at left2
    show aiden tease2 at left2
    voice audio.aiden_v_oho1a
    a "Oho~ You tellin’ me we’re gonna be more than just boyfriends now?"

    show yoshi_autumn at right
    show yoshi shock1 at right
    show aiden_autumn at center
    show aiden tease2 at center
    with move

    show goro_winter at left
    show goro talk3 at left
    with dissolve
    voice audio.goro_v_ah1b
    g "Ah. There you are, you two!"

    show yoshi talk1 at right
    voice audio.yoshi_v_goodam1
    yo "Good morning, Sir Goro! Sorry for the delay. Aiden just had to give Mr. Clermont a call."

    show goro confused2 at left
    voice audio.goro_v_response3a1
    g "It’s fine. How did it go?"

    hide aiden_autumn
    hide aiden tease2
    show aiden2_autumn at center
    show aiden2 worry2 at center
    voice audio.aiden_v_well1c1
    a "Well, I ended up turning down the offer. I don’t think it was the right path for me, Gramps."

    hide goro_winter
    hide goro confused2
    show goro2_winter at left
    show goro2 play3 at left
    voice audio.goro_v_heh1a
    g "I had a feeling that you’d end up choosing that, Aiden."

    hide aiden2_autumn
    hide aiden2 worry2
    show aiden_autumn at center
    show aiden shock2 at center
    voice audio.aiden_v_confused1b1
    a "What?! I was sure you and everybody else’d be shocked."
    a "Pretty sure what I just did goes against the norm."

    hide goro2_winter
    hide goro2 play3
    show goro_winter at left
    show goro bold5 at left
    voice audio.goro_v_dismiss2a
    g "Nonsense! As long as you’re happy, whatever your decision, it’ll always be the right choice.   "
    g "I support you regardless. And I think that applies to the rest of us here at Camp Buddy as well."

    show aiden comp3 at center
    voice audio.aiden_v_laugh1a1
    a "Hehe, thanks, Gramps. "

    show goro talk1 at left
    voice audio.goro_v_conj4a
    g "Either way, I’m glad to see you both finally resolving things with each other. We’ll need you two more than ever from here on out."

    show aiden bold2 at center
    voice audio.aiden_v_confident1a
    a "Roger that, Gramps. You can count on us!"
    a "Now let’s get on with things before this cheese-train gets out of control."

    hide yoshi_autumn
    hide yoshi talk1
    show yoshi2_autumn at right
    show yoshi2 sigh1 at right
    voice audio.yoshi_v_sigh3a
    yo "*sigh* Aiden."

    hide goro_winter
    hide goro talk1
    show goro2_winter at left
    show goro2 explain2 at left
    voice audio.goro_v_ehem1a
    g "*ehem* I actually came here to fetch you two for our agenda today."
    g "The workers have just arrived and we’re gathering to discuss resuming our expansion project."

    show aiden talk4 at center
    voice audio.aiden_v_agree2e1
    a "Oh right… that’s today!"

    hide yoshi2_autumn
    hide yoshi2 sigh1
    show yoshi_autumn at right
    show yoshi talk2 at right
    voice audio.yoshi_v_laugh1
    yo "Looks like we’re back to the grind again, huh?"

    hide goro2_winter
    hide goro2 explain2
    show goro_winter at left
    show goro talk3 at left
    voice audio.goro_v_agree1a1
    g "Yes. Hopefully we’re through all the seasonal hiccups, and we have until spring to finish everything."

    show aiden bold2 at center
    voice audio.aiden_v_comp2a
    a "Now that I’m not going anywhere, I’m sure we can pull it off, hahaha!"

    hide goro_winter
    hide goro talk3
    show goro2_winter at left
    show goro2 play3 at left
    voice audio.goro_v_heh1a
    g "Heh. Said like a true scoutmaster."
    g "Shall we go meet the workers then? We’ll have a short briefing on each department’s status."

    show yoshi happy1 at right
    voice audio.yoshi_v_yessir1
    yo "Of course, sir! We’re right behind you."

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

    $ location = location_campsite
    show screen location
    show screen timeline
    show screen quick_menu
    $ quick_menu = True
    scene bg_campgrounds_winter_day with fade
    play music camping_time loop
    play bgsound sfxloop_crowd loop
    play bgsound2 sfxloop_birds loop

    show aiden_winter at p7_1
    show aiden norm1 at p7_1
    show yoshi_winter at p7_2
    show yoshi norm1 at p7_2
    show jin_winter at p7_3
    show jin_glasses at p7_3
    show jin norm1 at p7_3
    show yuri_winter at p7_4
    show yuri norm1 at p7_4
    show darius_winter at p7_5
    show darius norm1 at p7_5
    show emilia_winter at p7_6
    show emilia norm2 at p7_6
    show lloyd_winter at p7_7
    show lloyd relief2 at p7_7
    voice audio.lloyd_v_relief2a1
    l "Whew! It’s so nice to see the camp crowded again!"

    show darius happy2 at p7_5
    voice audio.darius_v_amazed3
    d "It’s lively."

    show aiden play2 at p7_1
    voice audio.aiden_v_laugh1c1
    a "Heh, wait till you see it with the campers. This place is cramped! "

    show yoshi happy2 at p7_2
    voice audio.yoshi_v_relief4
    yo "Good thing we expanded the camp… I don’t think we would’ve been able to accommodate everyone next term, if we hadn’t."

    show jin confused2 at p7_3
    voice audio.jin_v_really1c
    j "Were there only a few scouts last term?"

    show yuri think3 at p7_4
    voice audio.yuri_v_think1a1
    yu "Hmm, it was honestly our lowest turnout ever."

    show emilia angry2 at p7_6
    voice audio.emilia_v_what3b
    e "What? How the heck did you manage to get sponsored by Clermont with hardly anyone here then?!"

    show yuri comp2 at p7_4
    voice audio.yuri_v_well1a
    yu "Well, let’s just say the last batch really showed off the spirit of Camp Buddy."

    show darius confused2 at p7_5
    voice audio.darius_v_confused1b
    d "You mean Keitaro and his friends?"

    show yuri bold2 at p7_4
    voice audio.yuri_v_agree2a1
    yu "That’s right!"

    show lloyd laugh1 at p7_7
    voice audio.lloyd_v_laugh1a1
    l "They really left an impression on me even in the short time I spent with them."

    show jin thinkdn2 at p7_3
    voice audio.jin_v_think1a1
    j "Makes me curious about their story."

    show aiden_winter at p8_1
    show aiden play2 at p8_1
    show yoshi_winter at p8_2
    show yoshi happy2 at p8_2
    show jin_winter at p8_3
    show jin_glasses at p8_3
    show jin thinkdn2 at p8_3
    show yuri_winter at p8_4
    show yuri bold2 at p8_4
    show darius_winter at p8_5
    show darius confused2 at p8_5
    show emilia_winter at p8_6
    show emilia angry2 at p8_6
    show lloyd_winter at p8_7
    show lloyd laugh1 at p8_7
    with move

    show goro_winter at p8_8
    show goro talk1 at p8_8
    hide lloyd_winter
    hide lloyd laugh1
    show lloyd_winter at p8_7
    show lloyd laugh1 at p8_7
    voice audio.goro_v_alright1a1
    g "Alright everyone, I’ve relayed our plan to the workers. "
    g "Let me just summarize to each department what the upcoming tasks are."

    show goro talk2 at p8_8
    voice audio.goro_v_jin2a
    g "For the tech upgrades, Jin, you’ll be working alongside the construction department to set up the necessary groundwork for security cameras and internet connections."

    show jin talk2 at p8_3
    voice audio.jin_v_yessir1a
    j "Yes, sir! The layout is already prepared!"

    show goro happy1 at p8_8
    voice audio.goro_v_praise2a1
    g "Good! Other than that, you can continue working on the camp database website and any integrations."

    show goro talk1 at p8_8
    voice audio.goro_v_conj2a1
    g "Next, for the construction, aside from the tech integrations, your task is mostly continuing the infrastructure plans already being worked on."
    g "When I spoke with the workers, they were all expecting to need to do repairs, but were quite happy to learn that we had already completed the majority of them."

    show lloyd happy1 at p8_7
    voice audio.lloyd_v_unsure1a1
    l "I guess all our initiative paid off, then! We’ll get things back on track today, sir!"

    show darius bold2 at p8_5
    voice audio.darius_v_yessir1
    d "You can count on us."

    show goro happy2 at p8_8
    voice audio.goro_v_amazed2a1
    g "Good! Please let us know immediately if any other concerns come up!"
    g "For Aiden and Yoshinori, you’ll both continue your maintenance tasks and staff welfare duties."

    show aiden wink2 at p8_1
    voice audio.aiden_v_response2a2
    a "Gotcha, Gramps! You’ve got nothing to worry about!"

    show yoshi talk1 at p8_2
    voice audio.yoshi_v_sir1
    yo "We’ll keep updating you as usual if there are any issues in our department, sir."

    show goro happy3 at p8_8
    voice audio.goro_v_alright1a2
    g "Alright. In addition, Ms. Komarova will officially assist with the maintenance tasks, so please take her under your wing as well."

    show yuri play2 at p8_4
    voice audio.yuri_v_laugh1a1
    yu "Hihi~ Look how the tables have turned~"

    show emilia annoy2 at p8_6
    voice audio.emilia_v_hmph1a
    e "Don’t push it."

    show goro explain3 at p8_8
    voice audio.goro_v_yuri3a
    g "As for Yuri and I, we’ll keep handling all the required paperwork and coordination with Mr. Clermont. "
    g "We’ll make sure everything is taken care of for the next summer term on the admin side."

    show yuri sigh4 at p8_4
    voice audio.yuri_v_sigh2a
    yu "*sigh* More secretary work…"

    show emilia eyeroll3 at p8_6
    voice audio.emilia_v_tsun2a
    e "I’d switch tasks any day."

    show goro talk1 at p8_8
    voice audio.goro_v_request2a1
    g "That should be everything then. Is everyone clear on our goals?"

    show aiden happy3 at p8_1
    show yoshi bold2 at p8_2
    show jin happy1 at p8_3
    show yuri happy3 at p8_4
    show darius bold3 at p8_5
    show emilia happy1 at p8_6
    show lloyd talk2 at p8_7
    all "Yes, sir!"

    show goro bold2 at p8_8
    voice audio.goro_v_praise1a
    g "Excellent! That’s all for today’s meeting. Let’s get to work!"

    if sq_goro >= 2:
        $goro_ending = True
        hide lloyd_winter
        hide lloyd talk2
        hide darius_winter
        hide darius bold3
        hide jin_winter
        hide jin_glasses
        hide jin happy1
        hide emilia_winter
        hide emilia happy1
        hide yuri_winter
        hide yuri happy3
        with dissolve

        show aiden_winter at left
        show aiden happy3 at left
        show yoshi_winter at center
        show yoshi bold2 at center
        show goro_winter at right
        show goro bold2 at right
        with move
        $ renpy.music.stop(channel='music', fadeout = 1.0)
        $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
        $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)

        show yoshi comp6 at center
        voice audio.yoshi_vsa23_line1
        yo "Hehe, I love it when you take charge like that, Sir Goro. Reminds me of when we were scouts!"

        show aiden laugh2 at left
        voice audio.aiden_vsa23_line1
        a "Haha, here we go with fanboy Yoshi."

        play music old_familiar_home loop
        show yoshi talk1 at center
        voice audio.yoshi_vsa23_line2
        yo "I mean it, though! It’s one thing to lead the scouts, but it takes a whole other level of skill to coordinate a project like this."

        show aiden comp3 at left
        voice audio.aiden_vsa23_line2
        a "You don’t have to tell me twice – no way I’d be able to do what Gramps does, haha!"

        show goro happy2 at right
        voice audio.goro_vsa23_line1
        g "Thank you both. I only push through because of all of you."

        voice audio.goro_vsa23_line2
        g "I believe we all share the same sentiment that working at Camp Buddy is more than just a job for all of us."

        show goro relief2 at right
        voice audio.goro_vsa23_line3
        g "I’m pretty proud of what we’ve accomplished considering we’re a small group of people with humble beginnings. "

        voice audio.goro_vsa23_line4
        g "We may be just a temporary place for our scouts, but I’d like to believe that the memories we give them lasts forever."

        show goro comp2 at right
        voice audio.goro_vsa23_line5
        g "There’s a sense of fulfillment that what we’re doing here makes a difference even in the littlest way possible."

        hide aiden_winter
        hide aiden comp3
        show aiden2_winter at left
        show aiden2 sigh4 at left
        voice audio.aiden_vsa23_line3
        a "Sheesh… Now I know where Yoshi got his speeches from."

        show yoshi shock2 at center
        voice audio.yoshi_vsa23_line3
        yo "Aiden…!"

        show goro play2 at right
        voice audio.goro_vsa23_line6
        g "Speaking of which, Yoshinori here will have to take my place someday."

        hide aiden2_winter
        hide aiden2 sigh4
        show aiden_winter at left
        show aiden play2 at left
        voice audio.aiden_vsa23_line4
        a "Don’t you have a little over a decade before you retire, Gramps?"

        hide goro_winter
        hide goro play2
        show goro2_winter at right
        show goro2 explain2 at right
        voice audio.goro_vsa23_line7
        g "*ehem* I’m just saying that with the camp growing like it is, we need to get someone ready to carry on the torch. "

        show yoshi happy1 at center
        voice audio.yoshi_vsa23_line4
        yo "Did you ever expect Camp Buddy to blow up like this, sir?"

        hide goro2_winter
        hide goro2 explain2
        show goro_winter at right
        show goro talk3 at right
        voice audio.goro_vsa23_line8
        g "Honestly, no. I’m sure if my younger self could see me now, he’d be over the moon."

        show goro comp2 at right
        voice audio.goro_vsa23_line9
        g "But even then, a part of me always hoped this camp would become something more because we were all pouring our hearts into it."

        voice audio.goro_vsa23_line10
        g "There were plenty of hardships along the way, but I don’t regret any of them. They helped shape everything into what we have today."

        show aiden comp5 at left
        voice audio.aiden_vsa23_line5
        a "Sounds like I’m not the only one who’s got plenty to unpack~"

        hide goro_winter
        hide goro comp2
        show goro2_winter at right
        show goro2 explain5 at right
        voice audio.goro_vsa23_line11
        g "Well, I’d be glad to tell you more after everything settles down. So, let’s save that for a different time."

        show yoshi bold2 at center
        voice audio.yoshi_vsa23_line5
        yo "Yes, sir! We’ll make sure everything gets done on time!"

        hide goro2_winter
        hide goro2 explain5
        show goro_winter at right
        show goro happy3 at right
        voice audio.goro_vsa23_line12
        g "Good. I’m counting on you both! "

        hide goro_winter
        hide goro happy3
        with dissolve

        show aiden_winter at left2
        show aiden happy1 at left2
        show yoshi_winter at right2
        show yoshi bold2 at right2
        with move

        voice audio.aiden_vsa23_line6
        a "Gramps sounded exactly like he was back then, huh? Burning with passion."

        show yoshi talk3 at right2
        voice audio.yoshi_vsa23_line6
        yo "Yeah, to think that less than a year ago he wanted nothing to do with Camp Buddy, or us, anymore."

        show yoshi comp2 at right2
        voice audio.yoshi_vsa23_line7
        yo "I’m so glad he was able to move past all of that!"

        show aiden laugh2 at left2
        voice audio.aiden_vsa23_line7
        a "Same! I much prefer cuddly Gramps!"

        show yoshi laugh2 at right2
        voice audio.yoshi_vsa23_line8
        yo "Haha, me too. Now come on, let’s get started for the day!"
        $ last_end = "goro"
    if sq_jin >= 2:
        $jin_ending = True
        $ renpy.music.stop(channel='music', fadeout = 1.0)
        $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
        $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
        scene cg black
        $ renpy.pause (2.0, hard=True)
        hide screen location
        hide screen timeline
        hide screen quick_menu
        $ quick_menu = False
        with fade

        $ time = timeline_timeday
        $ location = location_messhall
        show screen location
        show screen timeline
        show screen quick_menu
        $ quick_menu = True
        $working = True
        scene bg_messhall_winter_day with fade
        play music buddy_oath_casual loop

        show aiden_winter at right2
        show aiden bold2 at right2
        show yoshi_winter at left2
        show yoshi norm1 at left2
        with dissolve
        voice audio.aiden_vsa24_line1
        a "Alright! We got a whole bunch of people here again, so there’s a lot of cooking to do!"

        show yoshi confused2 at left2
        voice audio.yoshi_vsa24_line1
        yo "Should we clean up the mess hall first, though? It’s probably a little dustier than usual…"

        show aiden happy1 at right2
        voice audio.aiden_vsa24_line2
        a "Sure thing, Yoshi!"

        show aiden_winter at right
        show aiden happy1 at right
        show yoshi_winter at center
        show yoshi confused2 at center
        with move

        show jin_winter at left
        show jin_glasses at left
        show jin norm1 at left
        with dissolve
        show yoshi talk3 at center
        voice audio.yoshi_vsa24_line2
        yo "Ah, hello, Jin! "

        show jin happy1 at left
        voice audio.jin_vsa24_line1
        j "Hello, you two!"

        show aiden talk1 at right
        voice audio.aiden_vsa24_line3
        a "What’s up? Did you want some breakfast before work today?"

        show jin talk2 at left
        voice audio.jin_vsa24_line2
        j "A-Ah, no, no, I actually wanted to show you guys something! "

        show yoshi confused3 at center
        voice audio.yoshi_vsa24_line3
        yo "Huh? What is it, Jin?"

        show jin explain2 at left
        voice audio.jin_vsa24_line3
        j "Well, remember that blog that we’ve been working on for the last couple of months?"

        voice audio.jin_vsa24_line4
        j "I was able to finish it! "

        show cg_fade at truecenter
        show fx8a at fx_pos
        with dissolve

        voice audio.yoshi_vsa24_line4
        yo "Wow! This is really amazing, Jin! It’s so nostalgic to see ourselves on the website like that!"

        voice audio.aiden_vsa24_line4
        a "Yeah, this looks like it took a lot of effort to do! "

        voice audio.jin_vsa24_line5
        j "Thanks, I’m really proud of it! I can’t wait to see what people say about it."

        voice audio.jin_vsa24_line6
        j "Yuri was super excited to see her journal digitized so she can view it anytime she wants."

        hide cg_fade
        hide fx8a
        with dissolve

        show aiden norm1 at right
        show yoshi norm1 at center
        show jin bold2 at left
        voice audio.jin_vsa24_line7
        j "If you guys want to check it out more and explore each page, I’d be happy to give you guys a soft copy!"

        show aiden amazed2 at right
        voice audio.aiden_vsa24_line5
        a "Wow, you really went all out on this, Jin… I hope it didn’t mess with your other work!"

        show jin relief2 at left
        voice audio.jin_vsa24_line8
        j "Not at all! Yoshinori was helping me out this whole time, and it’s more of a side project I did for fun!"

        show aiden happy2 at right
        voice audio.aiden_vsa24_line6
        a "Oh right! I remember a few times you got me and everybody else to throw a thing or two in there!"

        show jin comp2 at left
        voice audio.jin_vsa24_line9
        j "I guess in a way, this project helped me get to know you all better, and it made me feel like I was part of all the amazing memories you shared."

        voice audio.jin_vsa24_line10
        j "Working with you guys the last few months, I got to make amazing memories myself with all of you too."

        show aiden comp2 at right
        voice audio.aiden_vsa24_line7
        a "Aww, Jin~"

        show jin comp6 at left
        voice audio.jin_vsa24_line11
        j "I… I guess that’s another thing that I learned here – how to make friends."

        voice audio.jin_vsa24_line12
        j "I feel bad about being a shut-in for so long… I can’t help but feel like I’ve missed out on a lot."

        show jin sigh3 at left
        voice audio.jin_vsa24_line13
        j "I’ve gotten so used to having people around me just come and go, and I always found it easier to not deal with anyone but myself."

        voice audio.jin_vsa24_line14
        j "I wish I wasn’t such an introvert..."

        show yoshi comp3 at center
        voice audio.yoshi_vsa24_line5
        yo "But it’s part of who you are, Jin! "

        voice audio.yoshi_vsa24_line6
        yo "And besides, you pushed yourself out of your comfort zone knowing you’d have to deal with a lot of people when you signed up to work with us. "

        show aiden comp6 at right
        voice audio.aiden_vsa24_line8
        a "That takes a lotta guts, if you ask me~"

        show jin comp4 at left
        voice audio.jin_vsa24_line15
        j "Yeah… I guess I shouldn’t think of it as a bad thing."

        voice audio.jin_vsa24_line16
        j "I-It’s just… I’ve never had a place where I can express who I am and be accepted for the things I thought were bad about myself."

        show jin worry2 at left
        voice audio.jin_vsa24_line17
        j "And to think we only have a few months left ’til the project ends… I’ll be losing the closest thing I have to a ‘social circle’."

        voice audio.jin_vsa24_line18
        j "Just the thought of leaving Camp Buddy is so dreadful…"

        show aiden talk4 at right
        voice audio.aiden_vsa24_line9
        a "Oh, I totally get you! It’s why I turned down Mr. Clermont’s offer, too."

        voice audio.aiden_vsa24_line10
        a "Being a professional chef would be awesome, but I’m where I’m meant to be."

        show jin sad5 at left
        voice audio.jin_vsa24_line19
        j "Yeah, I understand that feeling now…"

        show aiden bold2 at right
        voice audio.aiden_vsa24_line11
        a "Then why don’t you stay here and work with us? Nobody else is good with computers like you are!"

        show jin shock2 at left
        voice audio.jin_vsa24_line20
        j "Wh-What…? L-Like, work here permanently?! "

        hide yoshi_winter
        hide yoshi comp3
        show yoshi2_winter at center
        show yoshi2 sigh1 at center
        voice audio.yoshi_vsa24_line7
        yo "Aiden, you shouldn’t pressure Jin with stuff like that. Mr. Clermont pays a lot more than we could, I’m sure."

        show aiden laugh1 at right
        voice audio.aiden_vsa24_line12
        a "Haha, it’s just if he wants to! I’m just saying it’s a possibility!"

        show jin think2 at left
        voice audio.jin_vsa24_line21
        j "Umm… I guess someone would probably need to stay to maintain most of the tech… "

        show aiden comp3 at right
        voice audio.aiden_vsa24_line13
        a "And what better person than the one who installed it!"

        show jin thinkdn3 at left
        voice audio.jin_vsa24_line22
        j "I… might think about it. "

        $ renpy.music.stop(channel='music', fadeout = 1.0)
        show aiden play2 at right
        voice audio.aiden_vsa24_line14
        a "—Ohh! I have an idea that would get you to stay~ "

        voice audio.aiden_vsa24_line15
        a "If you stick around, we’ll get Yoshi to serve food with me in just an apron every meal!"

        play music here_they_come_fast loop
        hide jin_winter
        hide jin_glasses
        hide jin thinkdn3
        show jin2_winter at left
        show jin2_blush at left
        show jin2_glasses at left
        show jin2 fudan3 at left
        voice audio.jin_vsa24_line23
        j "W-WAHHH!! What?!! "

        show yoshi2 annoy1 at center
        voice audio.yoshi_vsa24_line8
        yo "D-Don’t listen to him, Jin… He’s just messing with you. "

        show aiden tease2 at right
        voice audio.aiden_vsa24_line16
        a "Oh, come on, Yoshi! Aren’t we trying to poach Jin here?"

        show jin2 daydream4 at left
        voice audio.jin_vsa24_line24
        j "Hngh… Beefcakes everyday…"

        show yoshi2 sigh4 at center
        voice audio.yoshi_vsa24_line9
        yo "*sigh* Let’s get the food ready before Jin passes out."

        show aiden wink2 at right
        voice audio.aiden_vsa24_line17
        a "So we’ll give the naked apron show a dry run?"

        hide yoshi2_winter
        hide yoshi2 sigh4
        show yoshi_winter at center
        show yoshi play5 at center
        voice audio.yoshi_vsa24_line10
        yo "More like that’d make him run dry."

        show aiden laugh3 at right
        voice audio.aiden_vsa24_line18
        a "Hahaha!"

        $ last_end = "jin"
    if sq_emilia >= 2:
        $emilia_ending = True
        $ renpy.music.stop(channel='music', fadeout = 1.0)
        $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
        $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
        scene cg black
        $ renpy.pause (2.0, hard=True)
        hide screen location
        hide screen timeline
        hide screen quick_menu
        $ quick_menu = False
        with fade

        $ time = timeline_timeday
        $ location = location_kitchen
        show screen location
        show screen timeline
        show screen quick_menu
        $ quick_menu = True
        $working = True
        scene bg_kitchen_winter_day with fade
        play music go_with_the_flow loop

        show yoshi_winter at left2
        show yoshi norm1 at left2
        show aiden_winter at right2
        show aiden relief2 at right2
        voice audio.aiden_vsa25_line1
        a "Fwahh, feels good to be back in the kitchen! We got lots of mouths to feed today!"

        show yoshi happy2 at left2
        voice audio.yoshi_vsa25_line1
        yo "Haha, yeah! Although I think we left some dirty dishes last night…"

        hide aiden_winter
        hide aiden relief2
        show aiden2_winter at right2
        show aiden2 talk3 at right2
        voice audio.aiden_vsa25_line2
        a "Oh drats. Mind doing some washing while I get started prepping?"

        show yoshi talk1 at left2
        voice audio.yoshi_vsa25_line2
        yo "Sure, I—"

        play sound sfx_dishwashing
        hide yoshi_winter
        hide yoshi talk1
        show yoshi2_winter at left2
        show yoshi2 confused5 at left2
        voice audio.yoshi_vsa25_line3
        yo "Huh? Is somebody else in here?"

        show yoshi2_winter at left
        show yoshi2 confused5 at left
        show aiden2_winter at center
        show aiden2 talk3 at center
        with move

        show emilia_winter4 at right
        show emilia norm3 at right
        with dissolve

        hide aiden2_winter
        hide aiden2 talk3
        show aiden_winter at center
        show aiden shock2 at center
        voice audio.aiden_vsa25_line3
        a "Whoa, Emilia! Why are you washing dishes?"

        show emilia_winter4 at right
        show emilia annoy2 at right
        voice audio.emilia_vsa25_line1
        e "Would you rather have everyone eat off of dirty plates?"

        voice audio.emilia_vsa25_line2
        e "I’m simply performing my duties as an official member of the maintenance department."

        hide yoshi2_winter
        hide yoshi2 confused5
        show yoshi_winter at left
        show yoshi comp2 at left
        voice audio.yoshi_vsa25_line4
        yo "Emilia, you really amaze me every day with how much you’ve changed."

        show aiden talk3 at center
        voice audio.aiden_vsa25_line4
        a "Yeah, I feel like the old Emilia died and was replaced by an evil doppelganger."

        show emilia eyeroll6 at right
        voice audio.emilia_vsa25_line3
        e "Oh, you flatter me too much. Dishwashing isn’t that revolutionary to be so highly credited for."

        show aiden comp6 at center
        voice audio.aiden_vsa25_line5
        a "I guess accepting compliments wasn’t part of the job description."

        show emilia comp2 at right
        voice audio.emilia_vsa25_line4
        e "Seriously though, It’s the least I could do."

        voice audio.emilia_vsa25_line5
        e "Ever since Yuri and I became roommates, she’s been giving me a lot of advice."

        show emilia relief3 at right
        voice audio.emilia_vsa25_line6
        e "I’ve never had anyone as close as that before, so… I really just wanna give off the same energy."

        show aiden laugh2 at center
        voice audio.aiden_vsa25_line6
        a "Who would’ve thought the girls who pulled each other’s hair are besties now?"

        show emilia eyeroll3 at right
        voice audio.emilia_vsa25_line7
        e "She’s still annoying, don’t get me wrong. But we’re learning to deal with each other better."

        show emilia comp2 at right
        voice audio.emilia_vsa25_line8
        e "I guess, I should take the time to thank both of you as well… for having a constant open mind and giving someone like me a second chance."

        voice audio.emilia_vsa25_line9
        e "You all helped me to realize I don’t need to let my past dictate my present."

        show emilia sigh2 at right
        voice audio.emilia_vsa25_line10
        e "Especially when others have gone through their own pains and struggles similarly, if not worse than my own."

        voice audio.emilia_vsa25_line11
        e "My actions definitely have consequences and I’m the only one responsible for them."

        show emilia comp3 at right
        voice audio.emilia_vsa25_line12
        e "I know I’m nowhere near to making up for them… But it’s better late than never."

        show yoshi happy2 at left
        voice audio.yoshi_vsa25_line5
        yo "That’s a good way to look at it, Emilia! "

        voice audio.yoshi_vsa25_line6
        yo "What matters is that you’ve chosen the right path and are doing the right thing."

        show emilia play2 at right
        voice audio.emilia_vsa25_line13
        e "Oh, come on, haven’t you already given me that exact same advice multiple times?"

        voice audio.emilia_vsa25_line14
        e "I did something wrong, regardless of my reasons, so I will apologize. We are adults, after all."

        show aiden play2 at center
        voice audio.aiden_vsa25_line7
        a "That’s Yoshi for ya! He’s hard wired to give advice, so he can’t help it!"

        show yoshi awkward3 at left
        voice audio.yoshi_vsa25_line7
        yo "H-Hey!"

        play sound sfx_sink
        show emilia explain2 at right
        voice audio.emilia_vsa25_line15
        e "Whew! There we go, all done! "

        voice audio.emilia_vsa25_line16
        e "Sorry for taking up space in the kitchen. You’re good to start cooking now!"

        show emilia annoy2 at right
        voice audio.emilia_vsa25_line17
        e "Ugh, looks like I messed up the manicure Yuri gave me. I’ll just ask her to give me another one!"

        voice audio.emilia_vsa25_line18
        e "Tootles~"

        hide emilia_winter4
        hide emilia annoy2
        with dissolve

        show yoshi_winter at left2
        show yoshi comp1 at left2
        show aiden_winter at right2
        show aiden play2 at right2
        with move

        yo "…"

        hide aiden_winter
        hide aiden play2
        show aiden2_winter at right2
        show aiden2 annoy2 at right2
        voice audio.aiden_vsa25_line8
        a "Heyy… What’s with that dazed smile, Yoshi?"

        show yoshi comp3 at left2
        voice audio.yoshi_vsa25_line8
        yo "Oh, sorry Aiden! I’m just so overjoyed to see this side of Emilia."

        show aiden2 angry5 at right2
        voice audio.aiden_vsa25_line9
        a "Tsk, looking at other people like that, you’re gonna make me jealous."

        show yoshi awkward4 at left2
        voice audio.yoshi_vsa25_line9
        yo "H-Hey! I-It’s not like that! "

        show aiden2 pout1 at right2
        voice audio.aiden_vsa25_line10
        a "I dunno… She always called you a “special friend” back then."

        hide yoshi_winter
        hide yoshi awkward4
        show yoshi2_winter at left2
        show yoshi2 annoy3 at left2
        voice audio.yoshi_vsa25_line10
        yo "Oh, come on, Aiden! When are you ever gonna let that go?"

        hide aiden2_winter
        hide aiden2 pout1
        show aiden_winter at right2
        show aiden play2 at right2
        voice audio.aiden_vsa25_line11
        a "Eh, I guess there never was a chance. One of you just doesn’t swing that way."

        show yoshi2 sigh4 at left2
        voice audio.yoshi_vsa25_line11
        yo "*sigh* Can’t we get to work already? "

        show aiden bold2 at right2
        voice audio.aiden_vsa25_line12
        a "Yup! Let’s get cooking, good looking!"
        $ last_end = "emilia"
    if darius_ending == True:
        $ renpy.music.stop(channel='music', fadeout = 1.0)
        $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
        $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
        scene cg black with fade

        yo "{i}Aiden and I worked on a nice to-go lunch for all the workers at the construction site.{/i}"
        yo "{i}Once it was ready, we headed over there to deliver it!{/i}"

        scene cg black
        hide screen location
        hide screen timeline
        hide screen quick_menu
        $ quick_menu = False
        with fade
        $ renpy.pause (2.0, hard=True)

        $ time = timeline_timeday
        $ location = location_site
        show screen location
        show screen timeline
        show screen quick_menu
        $ quick_menu = True
        $working = True
        scene bg_site7_winter_day with fade
        play music sunset_stroll_winter loop
        play bgsound sfxloop_crowd loop
        play bgsound2 sfx_construction loop

        show yoshi_winter at left2
        show yoshi norm1 at left2
        show aiden_winter at right2
        show aiden shock2 at right2
        with dissolve
        voice audio.aiden_vsa26_line1
        a "Whoa, it’s bustling over here!"

        show yoshi laugh1 at left2
        voice audio.yoshi_vsa26_line1
        yo "Yeah, it feels strange after a couple weeks of quiet, haha!"

        show yoshi_winter at p4_1
        show yoshi laugh1 at p4_1
        show aiden_winter at p4_2
        show aiden talk3 at p4_2
        with move

        show lloyd_work2 at p4_3
        show lloyd happy3 at p4_3
        show darius_workw at p4_4
        show darius_goggles2 at p4_4
        show darius norm2 at p4_4
        with dissolve
        voice audio.aiden_vsa26_line2
        a "Oh, there’s Lloyd and Darius! They look busy~"

        show lloyd talk2 at p4_3
        voice audio.lloyd_vsa26_line1
        l "Okay, so based on the layout Jin gave us, there should be a satellite dish right over there."

        show darius relief2 at p4_4
        voice audio.darius_vsa26_line1
        d "I’ll put it up, don’t worry. "

        show lloyd bold2 at p4_3
        voice audio.lloyd_vsa26_line2
        l "Thanks, Dar. I knew I could count on you. "

        show darius smile1 at p4_4
        d "*pats Lloyd on the head*"

        show lloyd talk3 at p4_3
        voice audio.lloyd_vsa26_line3
        l "Alright, I’ll go drill the holes for the wires and give the workers their new tasks!"

        show darius_workw at p4_3
        show darius smile1 at p4_3
        show darius_goggles2 at p4_3
        show lloyd_work2 at p5_5
        show lloyd talk3 at p5_5
        with move

        show darius tease2 at p4_3
        voice audio.darius_vsa26_line2
        d "Aren’t you forgetting something?"

        show lloyd_work2 at p4_4
        show lloyd_blush1 at p4_4
        show lloyd pout1 at p4_4
        with move
        voice audio.lloyd_vsa26_line4
        l "Oh, come on! I’m literally just gonna go over there! "

        show darius annoy1 at p4_3
        d "…"

        hide lloyd_work2
        hide lloyd_blush1
        hide lloyd pout1
        show lloyd_work2 at p4_4
        show lloyd_blush1 at p4_4
        show lloyd angry5 at p4_4
        voice audio.lloyd_vsa26_line5
        l "F-Fine! "

        show lloyd_work2 at p5_4
        show lloyd_blush1 at p5_4
        show lloyd kiss1 at p5_4
        with move
        voice audio.lloyd_vsa26_line6
        l "Chuu~ "

        show darius tease4 at p4_3
        voice audio.darius_vsa26_line3
        d "Hehe…"

        voice audio.darius_vsa26_line4
        d "Good luck, cutie."

        show lloyd sigh4 at p5_4
        voice audio.lloyd_vsa26_line7
        l "Yeah, yeah… "

        hide lloyd_work2
        hide lloyd_blush1
        hide lloyd sigh4
        with dissolve

        show yoshi_winter at left
        show yoshi laugh1 at left
        show aiden_winter at center
        show aiden play3 at center
        show darius_workw at right
        show darius_goggles2 at right
        show darius tease4 at right
        with move
        voice audio.aiden_vsa26_line3
        a "Well, well, well! It looks like we’ve got a new couple here at camp!"

        show darius talk5 at right
        voice audio.darius_vsa26_line5
        d "Ah. Hello."

        show yoshi talk3 at left
        voice audio.yoshi_vsa26_line2
        yo "Wait... Since when did you and Lloyd start dating?"

        show darius happy2 at right
        voice audio.darius_vsa26_line6
        d "Since this morning."

        voice audio.darius_vsa26_line7
        d "Aiden gave me some advice the other day and it paid off. "

        show darius relief5 at right
        voice audio.darius_vsa26_line8
        d "All I needed was to ask Lloyd, after all. "

        show yoshi comp3 at left
        voice audio.yoshi_vsa26_line3
        yo "Well, I guess I shouldn’t be surprised. You two have been just as close as Aiden and I ever since we were scouts."

        show darius happy1 at right
        voice audio.darius_vsa26_line9
        d "Yes."

        show aiden bold2 at center
        voice audio.aiden_vsa26_line4
        a "Haha! Way to go making the moves on little Lloyd! "

        voice audio.aiden_vsa26_line5
        a "I didn’t expect you guys to be the PDA-type, though."

        show darius explain1 at right
        voice audio.darius_vsa26_line10
        d "It’s still new to me to initiate though."

        show yoshi confused3 at left
        voice audio.yoshi_vsa26_line4
        yo "Yeah, you’ve never really seemed like that kind of guy since we’ve known you."

        show darius talk2 at right
        voice audio.darius_vsa26_line11
        d "Yes, but I understand communication is needed."

        voice audio.darius_vsa26_line12
        d "I hope someday Lloyd and I will be as colorful as you two’s relationship."

        show aiden talk2 at center
        voice audio.aiden_vsa26_line6
        a "You shouldn’t compare what you and Lloyd have with others, though."

        voice audio.aiden_vsa26_line7
        a "We’re all different, so your dynamic with him has its own style!"

        show darius confused5 at right
        voice audio.darius_vsa26_line13
        d "Oh… I didn’t think of it that way."

        voice audio.darius_vsa26_line14
        d "I just see you two as a perfect example of what I want to have as a relationship."

        show darius comp2 at right
        voice audio.darius_vsa26_line15
        d "But you’re right. I will try to compare less and embrace what we have uniquely."

        voice audio.darius_vsa26_line16
        d "Once again I learn something new from you. "

        show aiden happy2 at center
        voice audio.aiden_vsa26_line8
        a "We learn something new every day, right~? "

        show darius play2 at right
        voice audio.darius_vsa26_line17
        d "Yes. Today I also learned Lloyd really likes being called cute."

        voice audio.darius_vsa26_line18
        d "Except I’m the only one allowed to say it."

        show yoshi comp2 at left
        voice audio.yoshi_vsa26_line5
        yo "Aww, that’s really sweet, Darius!"

        show darius tease2 at right
        voice audio.darius_vsa26_line19
        d "I am planning on taking Lloyd out on the holidays. We’re going deep in space."

        show aiden tease1 at center
        voice audio.aiden_vsa26_line9
        a "Oho~ Make him ride on your rocket and see stars!"

        show yoshi shy6 at left
        voice audio.yoshi_vsa26_line6
        yo "We’re talking about a planetarium here right…? Just so we’re clear."

        show darius tease3 at right
        voice audio.darius_vsa26_line20
        d "Yes. It’s gonna be a big bang."

        show aiden pout2 at center
        voice audio.aiden_vsa26_line10
        a "You know, Yoshi here has never taken me on an actual date! Maybe he could learn a thing or two from you~"

        show yoshi angry2 at left
        voice audio.yoshi_vsa26_line7
        yo "H-Hey! Aren’t you the one who’s been saying not to compare…? "

        show aiden happy1 at center
        voice audio.aiden_vsa26_line11
        a "Lemme know how it goes, Darius! I wanna stay up to date with you two! "

        show darius confused3 at right
        voice audio.darius_vsa26_line21
        d "That actually reminds me. How will we stay in touch after the contract ends?"

        voice audio.darius_vsa26_line22
        d "It’s sad knowing we’ll have to part ways after this. "

        show aiden worry2 at center
        voice audio.aiden_vsa26_line12
        a "Oh yeah… you’re right about that… "

        show darius comp2 at right
        voice audio.darius_vsa26_line23
        d "I’m really grateful for all the things you guys and Camp Buddy have done for me."

        voice audio.darius_vsa26_line24
        d "It’s where I met Lloyd, and coming back here gave me the chance to take things with him to the next level."

        show darius comp6 at right
        voice audio.darius_vsa26_line25
        d "I hope we get to continue this when we move on to our next job."

        hide darius_workw
        hide darius_goggles2
        hide darius comp6
        with dissolve

        show yoshi_winter at left2
        show yoshi norm1 at left2
        show aiden_winter at right2
        show aiden worry2 at right2
        with move

        show yoshi awkward4 at left2
        voice audio.yoshi_vsa26_line8
        yo "H-He just left again… "

        show aiden laugh1 at right2
        voice audio.aiden_vsa26_line13
        a "Hahaha! You should be used to it by now!"

        show yoshi happy2 at left2
        voice audio.yoshi_vsa26_line9
        yo "I’m glad Darius and Lloyd finally got their label. They’re a really good match for each other!"

        hide aiden_winter
        hide aiden laugh1
        show aiden2_winter at right2
        show aiden2 sigh1 at right2
        voice audio.aiden_vsa26_line14
        a "*sigh* I’m gonna miss them when all of this is over, though."

        show yoshi comp5 at left2
        voice audio.yoshi_vsa26_line10
        yo "Don’t worry! I’m sure we can keep in touch!"

        show aiden2 annoy2 at right2
        voice audio.aiden_vsa26_line15
        a "Says like the worst offender of all of us."

        show yoshi panic4 at left2
        voice audio.yoshi_vsa26_line11
        yo "Gah! I’ll be better this time, I swear!"

        hide aiden2_winter
        hide aiden2 annoy2
        show aiden_winter at right2
        show aiden happy1 at right2
        voice audio.aiden_vsa26_line16
        a "Yeah, yeah! Now come on, we need to distribute these lunches!"

        show yoshi talk3 at left2
        voice audio.yoshi_vsa26_line12
        yo "Oh, right!"
        $ last_end = "darius"

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black with fade
    #$ renpy.pause (2.0, hard=True)

    #If player doesn’t unlock any SQs or If Hyunjin SQ Ending is the last scene
    if (goro_ending == False and emilia_ending == False and darius_ending == False) or last_end == "jin":
        yo "{i}Aiden and I headed to the kitchen and got started cooking lunch for the workers, then spent the rest of the morning distributing them.{/i}"
        yo "{i}Once all the lunches had been handed out, we went around the camp doing maintenance tasks, and before we knew it, the sun was setting.{/i}"
    elif last_end == "emilia":
        yo "{i}Aiden and I spent the rest of the morning in the kitchen, making lunch for everyone and distributing them to all the workers.{/i}"
        yo "{i}Once all the lunches had been handed out, we went around the camp doing maintenance tasks, and before we knew it, the sun was setting.{/i}"
    elif last_end == "darius":
        yo "{i}Once we finished distributing the lunches to everyone, Aiden and I headed back to the kitchen to cleanup.{/i}"
        yo "{i}We then went around the camp doing all the maintenance tasks, and before we knew it, the sun was setting.{/i}"

    $ time_transition_day_to_sunset_winter2()
    $ time = timeline_timeday
    $ location = location_cabin
    show screen location
    show screen timeline
    show screen quick_menu
    $ quick_menu = True
    $working = True
    scene bg_quarters_winter_sunset with fade
    play music go_with_the_flow_slow loop

    show yoshi_sleep at left2
    show yoshi norm2 at left2
    show aiden2_sleep at right2
    show aiden2 tired5 at right2
    voice audio.aiden_v_relief1a1
    a "Whew! A nice hot shower really helped wash off all that sweat!"

    show yoshi relief2 at left2
    voice audio.yoshi_v_yeah1
    yo "Yeah. It’s nice to take a short break to rest our backs and breathe a little."

    hide aiden2_sleep
    hide aiden2 tired5
    show aiden_sleep at right2
    show aiden comp3 at right2
    voice audio.aiden_v_perv1
    a "Hehe, don’t get too relaxed, we only have an hour before we have to start prepping for dinner!"

    show yoshi comp3 at left2
    voice audio.yoshi_v_agree1a
    yo "Of course, of course."

    show aiden sigh4 at right2
    voice audio.aiden_v_sigh1a
    a "We’re gonna be crazy busy for the next few months again, huh?"

    show yoshi talk1 at left2
    voice audio.yoshi_v_yeah2
    yo "Yeah, definitely! It’s gonna be a long winter – we’ll be working till all the snow melts outside!"
    yo "I can’t believe that when we started this project months ago, I was worried about not being able to do anything."

    show aiden comp6 at right2
    voice audio.aiden_v_laugh1c1
    a "Hehe, you got more than what you asked for."

    show yoshi comp3 at left2
    voice audio.yoshi_v_sigh3a
    yo "Yeah, I couldn’t have been more wrong."
    yo "When I became a scoutmaster here I never stopped grinding, always afraid of screwing something up."

    show yoshi happy1 at left2
    voice audio.yoshi_v_but2
    yo "For the first time in years, I’m happy that Camp Buddy doesn’t have to deal with the risk of closure or damage control anymore."
    yo "It’s been nice to have some time to actually focus on ourselves, too!"

    show aiden talk1 at right2
    voice audio.aiden_v_yeah1a3
    a "Yeah, plus I wouldn’t have ever been able to deal with all that stuff from my past, so I’m glad."

    show yoshi explain4 at left2
    voice audio.yoshi_v_right9
    yo "Me too, it’s nice to know we both got some closure!"
    yo "From here on out, we can really focus on what’s ahead of us."

    show aiden laugh1 at right2
    voice audio.aiden_v_laugh2a1
    a "Haha, you could almost say this was a ‘scoutmaster season!’"

    hide aiden_sleep
    hide aiden laugh1
    show aiden2_sleep at right2
    show aiden2 sigh4 at right2
    voice audio.aiden_v_sheesh1b
    a "But sheesh… adulting really sucks. I kinda miss how simple our lives were during our first term."
    a "Now, every decision we make has either serious rewards or consequences – back then, everything was just one exciting thing after the next!"

    show aiden2 sigh3 at right2
    voice audio.aiden_v_sigh1a
    a "All we ever worried about was getting caught, stupid crushes, or promises we didn’t fully understand."

    show yoshi confused2 at left2
    voice audio.yoshi_v_unsure3a
    yo "I guess that’s why I’m so passionate about being a scoutmaster… it’s like I get to relive those memories through the scouts."

    hide aiden2_sleep
    hide aiden2 sigh3
    show aiden_sleep at right2
    show aiden happy2 at right2
    voice audio.aiden_v_well1a1
    a "Well, with twice as many enrollees, let’s see if you can handle all that ‘youthful energy’ haha!"

    show yoshi bold2 at left2
    voice audio.yoshi_v_confident1
    yo "After this off season, I’m ready to get back to it! I can’t wait to teach the scouts again! "

    show aiden bold2 at right2
    voice audio.aiden_v_alright1c
    a "Then let’s make sure that they have the best Camp Buddy to come back to! "

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    $ day = "85"
    $time = timeline_timeday
    scene cg white with fade
    scene cg8 1 with dissolve
    play music buddy_oath_acoustic loop

    voice audio.yoshi_vsa27_line1
    yo "Everyone proceeded to work for the rest of the winter, continuing where we left off with all the new goals set for us."

    voice audio.yoshi_vsa27_line2
    yo "Thankfully, the weather didn’t act up for the rest of the season, letting Lloyd, Darius, and all the workers continuously make progress on the construction."

    voice audio.yoshi_vsa27_line3
    yo "Jin was also able to finish the website and all the necessary tech integrations for the camp! "

    voice audio.yoshi_vsa27_line4
    yo "I don’t know how we would have been able to pull off all of these amazing changes if not for their expertise!"

    $ day = "86"
    $time = timeline_timesunset
    show cg8 2a with Dissolve(0.25)
    voice audio.yoshi_vsa27_line5
    yo "Meanwhile, Sir Goro kept the entire project well-managed, making sure we stayed on schedule."

    voice audio.yoshi_vsa27_line6
    yo "Thankfully, Yuri was there to assist him so he wasn’t as stressed with all the paperwork as he used to be!"

    $ day = "87"
    $time = timeline_timenight
    show cg8 3a with Dissolve(0.25)
    voice audio.yoshi_vsa27_line7
    yo "Aiden and I kept up our regular maintenance duties, but this time around we had Emilia doing most of the other chores like cleaning and laundry."

    voice audio.yoshi_vsa27_line8
    yo "She would complain as usual, but she did the job well and got it done on time!"

    voice audio.yoshi_vsa27_line9
    yo "With this, Aiden started having much more time for himself, and he used it to make our meals at camp much more special."

    voice audio.yoshi_vsa27_line10
    yo "I could tell that the opportunity he was offered made him more inspired and determined to try out new things!"

    $ day = "89"
    show cg8 4a with Dissolve(0.25)
    voice audio.yoshi_vsa27_line11
    yo "All in all, it was amazing to see everyone work towards a common goal, all while enjoying our time together."

    voice audio.yoshi_vsa27_line12
    yo "The days flew by, and we saw the fruits of our labor take shape as we came closer and closer to completion!"

    voice audio.yoshi_vsa27_line13
    yo "Even with all the work, we still managed to sneak in another party for the holidays!"

    voice audio.yoshi_vsa27_line14
    yo "And of all people, Yuri even suggested that we drink together! We all laughed and talked as we reminisced about old times!"

    voice audio.yoshi_vsa27_line15
    yo "We all felt like we were back at our very first term at Camp Buddy, and I wouldn’t have changed it for anything! "

    $ day = "200"
    $time = timeline_timeday
    scene entrance_transition
    voice audio.yoshi_vsa27_line16
    yo "The snow started to thaw, and with spring just around the corner, we could clearly see how much progress we made!"

    voice audio.yoshi_vsa27_line17
    yo "I can’t wait for the scouts to see how much this place has grown!"

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black
    hide screen location
    hide screen timeline
    hide screen quick_menu
    $quick_menu = False
    with fade
    $ time_transition_winter_to_spring()
    $ renpy.pause (2.0, hard=True)

    $ day = "221"
    $ season = season_spring
    $ location = location_site
    show screen location
    show screen timeline
    show screen quick_menu
    $ quick_menu = True
    scene bg_site8_spring_day with fade
    play music brand_new_day loop
    play bgsound sfxloop_birds loop

    show william_autumn at p9_6
    show william norm1 at p9_6
    show aiden_autumn at p9_3
    show aiden norm2 at p9_3
    show yoshi_autumn at p9_4
    show yoshi norm1 at p9_4
    show darius_autumn at p9_8
    show darius norm1 at p9_8
    show lloyd_autumn at p9_7
    show lloyd norm2 at p9_7
    show jin_autumn at p9_9
    show jin_glasses at p9_9
    show jin norm1 at p9_9
    show yuri_autumn at p9_2
    show yuri norm2 at p9_2
    show emilia_autumn at p9_1
    show emilia norm1 at p9_1
    show goro_autumn at p9_5
    show goro happy3 at p9_5
    voice audio.goro_v_praise2b1
    g "This is such a wonderful day for Camp Buddy. We’ve all been working towards this moment for so long!"
    g "Just a year ago, I couldn’t have dreamed that something like this was possible, and I have you all to thank for that."

    show goro laugh1 at p9_5
    voice audio.goro_v_glad1a
    g "This project has just been a reminder of how far we’ve all come as a team, and how much I owe each and every one of you."

    show goro happy4 at p9_5
    voice audio.goro_v_william2a
    g "I’d also like to give a special thanks to Mr. Clermont, as without him we’d never have had this opportunity to grow."

    show goro comp5 at p9_5
    voice audio.goro_v_thanks2a2
    g "Thank you again, sir, for everything you’ve done, and for being here to celebrate with us today!"

    show william comp4 at p9_6
    voice audio.william_v_comp1b
    w "It was my pleasure, Mr. Nomoru."

    show goro happy3 at p9_5
    voice audio.goro_v_conj2a1
    g "Lastly, I want to dedicate this success to the scouts. They may not be here right now, but their spirit is what allowed this place to endure."
    g "They are what makes this place worth fighting for."

    show goro bold2 at p9_5
    voice audio.goro_v_rush4b2
    g "Now, let’s all celebrate the completion of our goals!"

    show goro laugh5 at p9_5
    voice audio.goro_v_laugh1b1
    g "To Camp Buddy and to the future!"

    play sound sfx_ribboncut
    show goro grin5 at p9_5
    g "*cuts ribbon*"

    play sound sfx_applause
    $ renpy.pause (2.0, hard=True)

    show yoshi happy1 at p9_4
    voice audio.yoshi_v_guys3
    yo "Of course, this celebration wouldn’t be complete without a reward for everyone’s hard work."

    show yoshi relief2 at p9_4
    voice audio.yoshi_v_aiden3
    yo "Our wonderfully talented chef, Aiden, has prepared a reception party for our success!"
    yo "Let’s use the last of our time together as a team to remember the good memories and hard work on this project!"

    show yoshi bold2 at p9_4
    voice audio.yoshi_v_praise1
    yo "This is a truly momentous day, so eat your hearts out, and celebrate these final moments with each other!"

    show william norm1 at p9_6
    show aiden norm2 at p9_3
    show yoshi norm1 at p9_4
    show lloyd norm2 at p9_7
    show darius norm1 at p9_8
    show jin norm1 at p9_9
    show yuri norm2 at p9_2
    show emilia norm1 at p9_1
    show goro happy3 at p9_5
    play sound sfx_applause
    all "*cheering*"

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

    $ location = location_kitchen
    show screen location
    show screen timeline
    show screen quick_menu
    $ quick_menu = True
    scene bg_kitchen_past_day with fade
    play music go_with_the_flow loop

    show aiden_apron at center
    show aiden norm1 at center
    with dissolve

    show aiden_apron at left2
    show aiden norm1 at left2
    with move

    show yoshi2_autumn at right2
    show yoshi2 sigh4 at right2
    with dissolve
    voice audio.yoshi_v_relief1
    yo "Phew, I think that was the final order! "

    show aiden comp2 at left2
    voice audio.aiden_v_thanks1a1
    a "Thanks for waiting on the tables, Yoshi! How did everyone like the food?"

    hide yoshi2_autumn
    hide yoshi2 sigh4
    show yoshi_autumn at right2
    show yoshi happy1 at right2
    voice audio.yoshi_v_oh2
    yo "Oh, they loved it! If you didn’t notice, it started getting quiet out there, everyone’s so busy munching down on your food, haha! "

    hide aiden_apron
    hide aiden comp2
    show aiden2_apron at left2
    show aiden2 worry2 at left2
    voice audio.aiden_v_aww2a
    a "Aww, I wish I got to see their reactions! "

    hide yoshi_autumn
    hide yoshi happy1
    show yoshi2_autumn at right2
    show yoshi2 shy5 at right2
    voice audio.yoshi_v_well3
    yo "W-Well, you could have if you had at least worn pants…"

    hide aiden2_apron
    hide aiden2 worry2
    show aiden_apron at left2
    show aiden talk6 at left2
    voice audio.aiden_v_no1a1
    a "No way! The snow finally melted, and I actually missed going commando in my kitchen!"

    show aiden wink3 at left2
    voice audio.aiden_v_perv1
    a "You should know by now that’s my special secret to good cooking~!"

    hide yoshi2_autumn
    hide yoshi2 shy5
    show yoshi_autumn at right2
    show yoshi comp3 at right2
    voice audio.yoshi_v_response1b
    yo "I know, I know. But we don’t want people choking on their food on the last day, right?"

    show aiden play2 at left2
    voice audio.aiden_v_comeon2a
    a "Oh come on, Yoshi! I’m sure everyone’d like to have my cakes for dessert!"

    show yoshi sigh1 at right2
    voice audio.yoshi_v_sigh3a
    yo "Okay, I totally saw that coming. Except I thought you’d also make a pun out of choking."

    show aiden tease1 at left2
    voice audio.aiden_v_laugh1c1
    a "I’d like to see one of us choking~! And I bet you’d totally like to see ME coming~"

    show yoshi play2 at right2
    voice audio.yoshi_v_well1
    yo "Well then—"

    show yoshi_autumn at center
    show yoshi play2 at center
    with move

    show aiden shock1 at left2
    show yoshi play1 at center
    yo "*gropes Aiden’s butt*"

    show aiden shock3 at left2
    voice audio.aiden_v_shock1c1
    a "Wh-Whoa!"

    show yoshi play3 at center
    voice audio.yoshi_v_aiden13
    yo "I’ve been wanting to get my hands on you all morning…"

    show aiden tease2 at left2
    voice audio.aiden_v_oho1a
    a "Oho~ Now all of a sudden you don’t care that anyone can just walk in and see us?"

    show yoshi play5 at center
    voice audio.yoshi_v_laugh6
    yo "It’s been a while – we’ve been so busy with work, there hasn’t been time."
    yo "And now that we’re finished with everything, I feel like I could use a serious release…"

    show aiden laugh1 at left2
    voice audio.aiden_v_laugh2a1
    a "Haha, it figures you’d get turned on from finishing a project!"

    hide yoshi_autumn
    hide yoshi play5
    show yoshi2_autumn at center
    show yoshi2 angry2 at center
    voice audio.yoshi_v_hey3
    yo "H-Hey, that’s not it! And I thought you liked it when I made the first move!"
    yo "And how can I help it? Seeing you in only an apron is one of my favorite looks."

    show aiden tease2 at left2
    voice audio.aiden_v_laugh1c1
    a "Hehe~ Where was this pervy Yoshi at all this time?"

    hide yoshi2_autumn
    hide yoshi2 angry2
    show yoshi_autumn at center
    show yoshi bold5 at center
    voice audio.yoshi_v_rush3
    yo "*grabs Aiden’s crotch* Come on, Aiden… I’ll be quick, I promise."

    show aiden play3 at left2
    voice audio.aiden_v_alright2b
    a "Alright, alright~ But I’d rather you take your time~"

    scene cg black
    $ position = 0
    if score_bot == score_top:
        $ position = renpy.random.randint(1, 2)
    if score_top > score_bot or position == 1:
        hide screen location
        hide screen timeline
        hide screen quick_menu
        $ quick_menu = False
        with fade
        $ say_box = False
        $ fp_stage = 'mga4_b'
        $ success_jumpto = 'day10_aiden_7b'
        $ failed_jumpto = 'day10_aiden_aftersx'
        jump fp

    elif score_bot > score_top or position == 2:
        hide screen location
        hide screen timeline
        hide screen quick_menu
        $ quick_menu = False
        with fade
        $ say_box = False
        $ fp_stage = 'mga4_f'
        $ success_jumpto = 'day10_aiden_7t'
        $ failed_jumpto = 'day10_aiden_aftersx'
        jump fp


label day10_aiden_aftersx:
    $ location = location_kitchen
    show screen location
    show screen timeline
    show screen quick_menu
    $ quick_menu = True
    scene bg_kitchen_past_day
    play music here_they_come_fast loop

    show aiden_apron at p4_1
    show aiden shock1 at p4_1
    show yoshi_autumn at p4_2
    show yoshi_blush2 at p4_2
    show yoshi panic1 at p4_2
    show jin2_autumn at p4_3
    show jin2_glasses at p4_3
    show jin2_nosebleed at p4_3
    show jin2_blush2 at p4_3
    show jin2 comic1 at p4_3
    show yuri2_autumn at p4_4
    show yuri2_blush2 at p4_4
    show yuri2 ahegao1 at p4_4
    voice audio.yuri_v_kyaa1a
    yu "KYAAAAAA!!" with vpunch

    show jin2 fudan3 at p4_3
    voice audio.jin_v_wah4a
    j "GAHHHHHHHHHHHH!!!!!!!!!!" with vpunch

    hide yoshi_autumn
    hide yoshi_blush2
    hide yoshi panic1
    show yoshi2_autumn at p4_2
    show yoshi2_blush2 at p4_2
    show yoshi2 panic4 at p4_2
    voice audio.yoshi_v_oops1
    yo "Oh no! A-Aiden, put something on…!"

    show yuri2 drool2 at p4_4
    voice audio.yuri_v_fujo5d
    yu "It’s been nearly a decade, and now I finally get to witness this most awaited moment with my own two eyes~!"

    hide aiden_apron
    hide aiden shock1
    show aiden2_apron at p4_1
    show aiden2_blush2 at p4_1
    show aiden2 comp6 at p4_1
    voice audio.aiden_v_laugh1a1
    a "A-Ahehe…"

    show yuri2 ahegao3 at p4_4
    voice audio.yuri_v_fujo4a
    yu "To think Yoshi’s baking his hotdog in Aiden’s lovin’ oven while all of us were having a meal outside!"

    show jin2 dizzy2 at p4_3
    voice audio.jin_v_fudan1c1
    j "Th-there so much ‘cream’ all over the kitchen… "

    show yuri2 drool6 at p4_4
    voice audio.yuri_v_omg1b
    yu "OMJIZZ! You think that’s been the secret ingredient this whole time?!"

    hide yoshi2_autumn
    hide yoshi2_blush2
    hide yoshi2 panic4
    show yoshi_autumn at p4_2
    show yoshi_blush2 at p4_2
    show yoshi angry3 at p4_2
    voice audio.yoshi_v_no2
    yo "My goodness, Yuri! NO!"

    show jin2 dizzy3 at p4_3
    voice audio.jin_v_gulp1a
    j "*gulp* M-My mouth’s watering… I want some too…"

    hide aiden2_apron
    hide aiden2_blush2
    hide aiden2 comp6
    show aiden_apron at p4_1
    show aiden_blush2 at p4_1
    show aiden tease1 at p4_1
    voice audio.aiden_v_well1a1
    a "Well, why don’t we give you a huge serving then?"

    show aiden tease2 at p4_1
    voice audio.aiden_v_perv1
    a "Think you can take us both…? Hmmm~?"

    show yoshi angry2 at p4_2
    voice audio.yoshi_v_aiden10
    yo "A-Aiden!!!"

    show jin2 fudan3 at p4_3
    voice audio.jin_v_hngh5a
    j "GHUHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH!!!!!! "

    play sound sfx_bodydrop
    hide jin2_autumn
    hide jin2_nosebleed
    hide jin2_blush2
    hide jin2_glasses
    hide jin2 fudan3
    with moveoutbottom

    show yuri2 ahegao2 at p4_4
    voice audio.yuri_v_kyaa1a
    yu "Kyaaaaaaaaaaaaaaa!!!!!!!!!! AAAAAAAAHHHH!!!!!!!!! "

    play sound sfx_bodydrop
    hide yuri2_autumn
    hide yuri2_blush2
    hide yuri2 ahegao2
    with moveoutbottom

    show yoshi_autumn at p6_1
    show yoshi_blush2 at p6_1
    show yoshi angry2 at p6_1
    show aiden_apron at p6_2
    show aiden_blush2 at p6_2
    show aiden tease2 at p6_2
    with move

    show goro_autumn at p6_3
    show goro confused3 at p6_3
    show lloyd_autumn at p6_4
    show lloyd shock1 at p6_4
    show darius_autumn at p6_5
    show darius shock1 at p6_5
    show emilia_autumn at p6_6
    show emilia disgust1 at p6_6
    with dissolve
    voice audio.goro_v_worry1a
    g "I heard screams, what’s going—"

    hide goro_autumn
    hide goro confused3
    show goro2_autumn at p6_3
    show goro2 shy6 at p6_3
    voice audio.goro_v_oh1a
    g "Oh."

    show emilia disgust3 at p6_6
    voice audio.emilia_v_disgust1
    e "Nope. I’m out."

    hide emilia_autumn
    hide emilia disgust3
    with dissolve

    show yoshi_autumn at p5_1
    show yoshi_blush2 at p5_1
    show yoshi angry2 at p5_1
    show aiden_apron at p5_2
    show aiden_blush2 at p5_2
    show aiden tease2 at p5_2
    show goro2_autumn at p5_3
    show goro2 shy6 at p5_3
    show lloyd_autumn at p5_4
    show lloyd shock1 at p5_4
    show darius_autumn at p5_5
    show darius shock1 at p5_5
    with move

    show darius shock3 at p5_5
    voice audio.darius_v_shock1a
    d "Wow… Daring…"

    show lloyd rage3 at p5_4
    voice audio.lloyd_v_question1b1
    l "What the hell!? I thought my meal was vegetarian?!"

    show goro2 sigh1 at p5_3
    voice audio.goro_v_sigh2a
    g "*sigh* Haven’t I warned you both about this before? Yuri easily passes out and Jin might lose too much blood. "

    hide aiden_apron
    hide aiden_blush2
    hide aiden tease2
    show aiden2_apron at p5_2
    show aiden2 comp3 at p5_2
    voice audio.aiden_v_sorry1a1
    a "Hehe, sorry, Gramps! We got carried away…"

    hide yoshi_autumn
    hide yoshi_blush2
    hide yoshi angry2
    show yoshi2_autumn at p5_1
    show yoshi2_blush2 at p5_1
    show yoshi2 worry2 at p5_1
    voice audio.yoshi_v_sorry2c
    yo "W-We’ll clean up right away. I’m so sorry, sir!"

    show goro2 disappoint3 at p5_3
    voice audio.goro_v_ehem1a
    g "*ehem* It’s alright, just uh… don’t let anyone else see next time."

    show darius tease4 at p5_5
    voice audio.darius_v_encourage1a
    d "You should try that position, Lloyd."

    show lloyd tease1 at p5_4
    voice audio.lloyd_v_response2b1
    l "Easy~ Did you forget how flexible I am?"

    hide goro2_autumn
    hide goro2 disappoint3
    show goro_autumn at p5_3
    show goro annoy2 at p5_3
    voice audio.goro_v_no1a1
    g "Not now, you two. Help me carry Yuri and Jin out."

    hide goro_autumn
    hide goro annoy2
    hide lloyd_autumn
    hide lloyd tease1
    hide darius_autumn
    hide darius tease4
    with dissolve

    show aiden2_apron at right2
    show aiden2 comp3 at right2
    show yoshi2_autumn at left2
    show yoshi2_blush2 at left2
    show yoshi2 sigh4 at left2
    with move
    voice audio.yoshi_v_sigh3a
    yo "Oh god… that was so embarrassing, Aiden…  Everybody saw you covered in… you know."

    hide aiden2_apron
    hide aiden2 comp3
    show aiden_apron at right2
    show aiden bold5 at right2
    voice audio.aiden_v_confident2a
    a "What’s new~? Everybody knows we’re together anyway and besides, it looked like they were enjoying the show!"
    a "I think it’s kinda funny to get caught~"

    show yoshi2 annoy3 at left2
    voice audio.yoshi_v_aiden5
    yo "You really are an exhibitionist, Aiden…"

    show aiden bold2 at right2
    voice audio.aiden_v_laugh1c1
    a "With a sexy bod like this? Why wouldn’t I want to show it off~?"

    hide yoshi2_autumn
    hide yoshi2_blush2
    hide yoshi2 annoy3
    show yoshi_autumn at left2
    show yoshi_blush2 at left2
    show yoshi sigh1 at left2
    voice audio.yoshi_v_unsure3a
    yo "*sigh* I guess."

    show aiden happy2 at right2
    voice audio.aiden_v_rush1a1
    a "Now let’s go join them! All that boning made me hungry!"

    show yoshi angry2 at left2
    voice audio.yoshi_v_no2
    yo "You haven’t even cleaned up yet! Or gotten dressed!"

    hide aiden_apron
    hide aiden happy2
    show aiden2_apron at right2
    show aiden2 worry3 at right2
    voice audio.aiden_v_aww2a
    a "Aww, do I have to?"

    show yoshi angry3 at left2
    voice audio.yoshi_v_rush2
    yo "Yes! Come on, I’ll wash you off!"

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black
    hide screen location
    hide screen timeline
    hide screen quick_menu
    $ quick_menu = False
    with fade

    $ location = location_messhall
    show screen location
    show screen timeline
    show screen quick_menu
    $ quick_menu = True
    scene bg_messhall_past_day_celebration with fade
    play music buddy_oath_casual loop
    play bgsound sfxloop_crowd loop

    show yoshi_autumn at p9_1
    show yoshi awkward1 at p9_1
    show aiden_autumn at p9_2
    show aiden norm1 at p9_2
    show william_autumn at p9_3
    show william relief2 at p9_3
    show goro_autumn at p9_4
    show goro norm3 at p9_4
    show yuri2_autumn at p9_5
    show yuri2_blush at p9_5
    show yuri2 jizz1 at p9_5
    show jin2_autumn at p9_6
    show jin2_blush at p9_6
    show jin2_glasses at p9_6
    show jin2 fudan1 at p9_6
    show emilia_autumn at p9_7
    show emilia norm1 at p9_7
    show darius_autumn at p9_9
    show darius norm1 at p9_9
    show lloyd_autumn at p9_8
    show lloyd norm1 at p9_8
    voice audio.william_v_surprised1a
    w "Ahh, it’s so nice to be enjoying your cooking again, Aiden!"
    w "I believe I could eat your meals every day and be quite happy!"

    show aiden comp3 at p9_2
    voice audio.aiden_v_thanks1a1
    a "Aww thanks~ The secret ingredient is ‘love.’"

    show emilia eyeroll4 at p9_7
    voice audio.emilia_v_ugh1
    e "Yes, we all saw just exactly what that ‘love’ entails."

    show jin2 fudan2 at p9_6
    show yuri2 jizz5 at p9_5
    yuj "Hnghh!"

    show darius play2 at p9_9
    voice audio.darius_v_laugh1
    d "Be careful or Yuri and Jin might need to see a doctor."

    show lloyd play3 at p9_8
    voice audio.lloyd_v_laugh1a1
    l "Haha, it’s always fun to watch them gush about this stuff though! Dar and I have learned to trigger them too~"

    show aiden happy1 at p9_2
    voice audio.aiden_v_conj2b1
    a "See, Lloyd understands! I always love poking at these two~!"

    hide goro_autumn
    hide goro norm3
    show goro2_autumn at p9_4
    show goro2 disappoint2 at p9_4
    voice audio.goro_v_ehem1a
    g "*ehem* Behave, all of you."

    show william laugh1 at p9_3
    voice audio.william_v_laugh1
    w "Haha, I’ll have to start making more regular trips here to join in on the fun!"
    w "It’s a totally different world from my usual work! Everything is always bright and full of laughter! Not to mention the good food!"

    show aiden comp3 at p9_2
    voice audio.aiden_v_agree7a
    a "You’re always welcome here, sir! And I’ll be sure to cook you something nice every time~"

    show william play2 at p9_3
    voice audio.william_v_please1a
    w "You’re tempting me to put on some weight with an offer like that, Aiden, hahaha!"

    hide goro2_autumn
    hide goro2 disappoint2
    show goro_autumn at p9_4
    show goro confused2 at p9_4
    hide yuri2_autumn
    hide yuri2 jizz5
    hide yuri2_blush
    show yuri_autumn at p9_5
    show yuri norm1 at p9_5
    hide jin2_autumn
    hide jin2_glasses
    hide jin2_blush
    hide jin2 fudan2
    show jin_autumn at p9_6
    show jin_glasses at p9_6
    show jin norm1 at p9_6
    voice audio.goro_v_yoshi6
    g "Yoshinori, are you alright? It’s been a while since I saw you so lost in your thoughts. "

    show yoshi talk3 at p9_1
    voice audio.yoshi_v_oh1
    yo "O-Oh! I was just thinking about how surreal everything is… the project is done, and Camp Buddy is two times bigger than it was."

    show jin thinkdn2 at p9_6
    voice audio.jin_v_yeah2a
    j "Yeah, I feel like I’m having withdrawals already – after so much work the last few months, I feel like I should be working still…"

    show yuri happy3 at p9_5
    voice audio.yuri_v_but1a
    yu "But we managed to get everything done! We’ve all earned this break!"

    show yoshi sad4 at p9_1
    yo "It’s bittersweet too, though… Everyone’s going to be leaving soon."

    hide yoshi_autumn
    hide yoshi sad4
    show yoshi2_autumn at p9_1
    show yoshi2 sigh1 at p9_1
    voice audio.yoshi_v_sigh3a
    yo "*sigh* I know that we’ve done a good job and all, but I’m really gonna miss working with you guys…"

    hide aiden_autumn
    hide aiden comp3
    show aiden2_autumn at p9_2
    show aiden2 shock2 at p9_2
    hide yoshi2_autumn
    hide yoshi2 sigh1
    show yoshi2_autumn at p9_1
    show yoshi2 worry2 at p9_1
    voice audio.aiden_v_oops2a
    a "Uh-oh, here come the waterworks."

    hide yoshi2_autumn
    hide yoshi2 sigh1
    show yoshi_autumn at p9_1
    show yoshi worry2 at p9_1
    voice audio.yoshi_v_but2
    yo "Having you all here has been one of the best times I’ve had working here!"
    yo "It’s really going to be different without you guys…"

    show lloyd awkward2 at p9_8
    l "..."

    show darius awkward1 at p9_9
    d "..."

    show jin confuseddn1 at p9_6
    j "..."

    hide yoshi_autumn
    hide yoshi worry2
    show yoshi2_autumn at p9_1
    show yoshi2 awkward3 at p9_1
    voice audio.yoshi_v_what3
    yo "Wh-What…? Did I say something?"

    show emilia comp6 at p9_7
    voice audio.emilia_v_sigh1a
    e "Go on, tell the poor fool, he’s close to tears."

    show yoshi2 confused2 at p9_1
    voice audio.yoshi_v_huh1
    yo "T-Tell me what?"

    show jin explain3 at p9_6
    voice audio.jin_v_conj2c1
    j "Well… Me and the others have been talking… "
    j "We all decided that we want to stay here at Camp Buddy if that’s alright...?"

    hide goro2_autumn
    hide goro2 play2
    show goro_autumn at p9_4
    show goro shock1 at p9_4
    hide yuri_autumn
    hide yuri explain3
    show yuri_autumn at p9_5
    show yuri explain3 at p9_5
    g "...!"

    hide yoshi2_autumn
    hide yoshi2 awkward3
    show yoshi_autumn at p9_1
    show yoshi shock3 at p9_1
    voice audio.yoshi_v_what4
    yo "Wh-What?! "

    hide aiden2_autumn
    hide aiden2 shock2
    show aiden_autumn at p9_2
    show aiden excited3 at p9_2
    voice audio.aiden_v_really3a
    a "W-Woah?! REALLY?! That’s so cool!"

    show lloyd happy1 at p9_8
    voice audio.lloyd_v_agree2b1
    l "Yeah! We loved it here so much we don’t wanna leave anymore!"

    show darius happy2 at p9_9
    voice audio.darius_v_conj1a1
    d "We’re ready for a change of pace from all the construction work."

    show yoshi shock2 at p9_1
    voice audio.yoshi_v_wait3a
    yo "W-Wait, a-are you all sure?! "

    show emilia angry2 at p9_7
    voice audio.emilia_v_what1
    e "What? You don’t want them to stay?! Isn’t this what you’ve been tearing up about for the past two minutes?"

    hide yoshi_autumn
    hide yoshi shock2
    show yoshi2_autumn at p9_1
    show yoshi2 awkward4 at p9_1
    voice audio.yoshi_v_no5
    yo "N-No, I mean… "

    show lloyd explain3 at p9_8
    voice audio.lloyd_v_conj1a3
    l "Well, we all thought about it over the last few months, after we realized that staying was a possibility. "

    show yuri happy1 at p9_5
    voice audio.yuri_v_actually1a
    yu "They actually coordinated it already with Mr. Clermont, and he agreed as well."

    hide yoshi2_autumn
    hide yoshi2 awkward4
    show yoshi_autumn at p9_1
    show yoshi shock5 at p9_1
    voice audio.yoshi_v_yuri5
    yo "Yuri? You were in on this? "

    show yuri laugh1 at p9_5
    voice audio.yuri_v_laugh2b1
    yu "We thought it would be nice to leave it as a surprise for you, Aiden, and Dad."

    hide yoshi_autumn
    hide yoshi shock5
    show yoshi2_autumn at p9_1
    show yoshi2 worry4 at p9_1
    voice audio.yoshi_v_why1
    yo "B-But… Wh-Why? Don’t you guys all have great career opportunities ahead of you?"

    show jin think2 at p9_6
    voice audio.jin_v_conj1b1
    j "I have a lot of extra income online, not to mention my crypto… So, it doesn’t really matter for me…"

    show jin comp2 at p9_6
    voice audio.jin_v_confused2a1
    j "And… seeing how everyone here was part of Camp Buddy in the past, I feel I missed a part of my youth."
    j "I want to experience being a scout and taking part in the activities too!"

    show jin comp6 at p9_6
    voice audio.jin_v_conj4a1
    j "More importantly, someone needs to maintain the new tech and even do some upgrades down the line."
    j "It’d be much easier for everyone to have an in-house technician, right? I’d say that’s a win-win!"

    hide yuri_autumn
    hide yuri laugh1
    show yuri2_autumn at p9_5
    show yuri2 laugh3 at p9_5
    voice audio.yuri_v_celebrate1a
    yu "Yiieee! My fanfic buddy is staying! "

    show lloyd bold2 at p9_8
    voice audio.lloyd_v_comp1a1
    l "Dar and I plan to apply as scoutmasters, so you don’t have to worry about us either!"

    show darius explain4 at p9_9
    voice audio.darius_v_conj5b
    d "We both really enjoyed teaching Taiga and Yoichi over the project, and want to share our knowledge with the rest of the scouts."
    d "Plus, Aiden’s cooking is worth staying for."

    show lloyd excited3 at p9_8
    voice audio.lloyd_v_encourage1a
    l "As for the financial part, we have a plan for it as well! "
    l "While we’re here, we’ll be running a nice side hustle – a design consultancy firm! "

    show lloyd bold3 at p9_8
    voice audio.lloyd_v_laugh1a3
    l "We call it D-L-Do! “Darius and Lloyd will do it all for you~” "

    show darius bold3 at p9_9
    voice audio.darius_v_agree3
    d "We’ve been in the industry for years already as contractors… it’s about time we started our own firm."
    d "With Lloyd and I working together, we thought it would be the perfect opportunity to make this decision."

    show william happy1 at p9_3
    voice audio.william_v_actually1
    w "It was actually all quite impressive – they laid out not only their personal plans but also ideas for the camp as well."
    w "Lloyd and Darius came up with a woodworking and construction curriculum for your scouts, and they’re quite passionate about it!"

    show william explain3 at p9_3
    voice audio.william_v_conj3b
    w "Personally, I’d love to see them all join the camp, but it’s up to the president’s final say!"

    show jin comp3 at p9_6
    voice audio.jin_v_yeah3b
    j "Y-Yeah… We decided this on our own, and we don’t really want to force it if it’s not—"

    show goro happy3 at p9_4
    voice audio.goro_v_agree3a1
    g "I have no objections – I would be honored to have all these talented and dedicated people as scoutmasters!"

    show william laugh2 at p9_3
    voice audio.william_v_laugh1
    w "Haha, I knew you’d approve them right away."

    show lloyd excited2 at p9_8
    voice audio.lloyd_v_amazed2a1
    l "Awesome! We got the job, Dar!"

    show darius amazed1 at p9_9
    voice audio.darius_v_celebrate1a
    d "Hooray."

    show emilia explain2 at p9_7
    voice audio.emilia_v_so1
    e "As for me, I’m going to stick with the helper role. "

    show aiden confused2 at p9_2
    voice audio.aiden_v_confused1c1
    a "Eh…? You’re not gunning to be a scoutmaster too?"

    show emilia talk1 at p9_7
    voice audio.emilia_v_no4
    e "No… I noticed during my time as both an inspector and these last few months that Aiden does all the maintenance work by himself, both during the on and off season. "
    e "I… want to help alleviate some of his workload so he can focus more on what he’s really passionate about, cooking."

    show emilia happy1 at p9_7
    voice audio.emilia_v_conj1a
    e "Plus, doing chores over the last few months has been strangely… enjoyable."
    e "I never experienced them growing up, and always was disgusted by ‘dirty work.’"

    show emilia bold2 at p9_7
    voice audio.emilia_v_conj5b
    e "Now, I feel a real sense of fulfilment when I complete them, seeing everyone enjoy the comfort as a direct result of my hard work."
    e "Not to mention that I’m learning new skills as well."

    hide yoshi2_autumn
    hide yoshi2 worry4
    show yoshi_autumn at p9_1
    show yoshi comp2 at p9_1
    voice audio.yoshi_v_praise1
    yo "That’s great, Emilia! You’ve got such a wonderful mindset about it all now!"

    hide yuri2_autumn
    hide yuri2 laugh3
    show yuri_autumn at p9_5
    show yuri bold2 at p9_5
    voice audio.yuri_v_laugh1a1
    yu "Hihi, with all this extra help, I can also focus more on being a counselor for the scouts that need it!"

    show yoshi comp5 at p9_1
    voice audio.yoshi_v_guys4
    yo "E-Everyone… You don’t know how happy this makes me…"

    show aiden shock3 at p9_2
    voice audio.aiden_v_swear3a
    a "Oh no! Here come the waterworks for real! "

    show yoshi comp3 at p9_1
    voice audio.yoshi_v_amazed2b
    yo "I-I can’t help it… you guys… "

    show goro laugh1 at p9_4
    voice audio.goro_v_alright2c2
    g "Let it all out, Yoshinori.  "

    show jin excited3 at p9_6
    voice audio.jin_v_oh3a
    j "O-Oh! Since everyone is here, I think this is the perfect time for us to take a victory selfie! "

    show yuri excited2 at p9_5
    voice audio.yuri_v_oh1a
    yu "Oooooh~! Good idea! I think we could also add it to our website! "

    show jin bold2 at p9_6
    voice audio.jin_v_response3a1
    j "Definitely! I was already planning to make the expansion project my next feature on there!"
    j "I’ll setup the camera! Everyone, huddle up!"

    show yoshi_autumn at p10_1
    show yoshi norm1 at p10_1
    show goro_autumn at p10_4
    show goro norm1 at p10_4
    show william_autumn at p10_3
    show william norm1 at p10_3
    show lloyd_autumn at p10_7
    show lloyd norm1 at p10_7
    show darius_autumn at p10_8
    show darius norm1 at p10_8
    show aiden_autumn at p10_2
    show aiden norm1 at p10_2
    show emilia_autumn at p10_6
    show emilia norm1 at p10_6
    show yuri_autumn at p10_5
    show yuri norm1 at p10_5
    show jin_autumn at p10_10
    show jin_glasses at p10_10
    show jin bold5 at p10_10
    with move

    voice audio.jin_v_response1a1
    j "And… the timer is set!"

    show jin_autumn at p10_9
    show jin_glasses at p10_9
    show jin happy1 at p10_9
    with move

    voice audio.jin_v_laugh1a
    j "Everybody say, ‘Camp Buddy!’"

    $ renpy.music.stop(channel='music', fadeout = 2.0)
    show yoshi grin3 at p10_1
    show goro norm1 at p10_4
    show william smile2 at p10_3
    show lloyd grin2 at p10_7
    show darius smile1 at p10_8
    show aiden grin4 at p10_2
    show emilia laugh3 at p10_6
    show yuri laugh1 at p10_5
    show jin grin3 at p10_9
    all "Camp Buddy!"

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    play sound sfx_camerashot
    scene cg10 with flash
    play music buddy_oath_acoustic loop
    voice audio.yoshi_vsa28_line1
    yo "Seasons have come and gone since we started this amazing project… And everything that happened was the opposite of what I thought it’d be."

    voice audio.yoshi_vsa28_line2
    yo "It was quite the ride – we encountered problems that couldn’t be predicted from when we were scouts, or even from before we returned to camp."

    voice audio.yoshi_vsa28_line3
    yo "Things didn’t always work out the way we planned, and we were challenged way past our limits."

    voice audio.yoshi_vsa28_line4
    yo "And in these darkest moments, Aiden’s best trait really shined – his perseverance. It was the reason why I could move forward too."

    voice audio.yoshi_vsa28_line5
    yo "I am so grateful we had the chance to continue where our stories left off… and it helped me learn even more about him and his past."

    voice audio.yoshi_vsa28_line6
    yo "I know now where his happiness and pain comes from, and from this, we were able to make our new promise to each other."

    voice audio.yoshi_vsa28_line7
    yo "And I owe it all to Camp Buddy… That’s why we’re going to give it everything we’ve got and face the future with the brightest smile."

    voice audio.yoshi_vsa28_line8
    yo "Forever, it’s our buddy oath!"

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg white
    hide screen location
    hide screen timeline
    hide screen quick_menu
    $ quick_menu = False
    with Dissolve(3.0)

    #credits
    $renpy.movie_cutscene("images/Camp Buddy Scoutmaster Season Credits.webm")
    jump day10_aiden_gepe_aftercredits

label day10_aiden_gepe_aftercredits:
    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black
    hide screen location
    hide screen timeline
    hide screen quick_menu
    $quick_menu = False
    with fade
    $time_transition_spring_to_summer()
    $ renpy.pause (2.0, hard=True)

    $ season = season_summer
    $ day = "284"
    $ location = location_site
    show screen location
    show screen timeline
    show screen quick_menu
    $ quick_menu = True
    scene bg_site9_spring_day with fade
    play music buddy_oath_casual loop
    play bgsound sfxloop_birds loop

    show goro_autumn2 at left
    show goro norm1 at left
    show yuri_autumn at center
    show yuri norm1 at center
    show emilia_autumn at right
    show emilia relief2 at right
    with dissolve
    voice audio.emilia_v_relief2a
    e "Ah, it’s so nice to see this new part of our camp in full bloom. I feel like a proud mother seeing all my plants grow so prettily~"

    show yuri angry2 at center
    voice audio.yuri_v_hey3a
    yu "Hey, I’m not letting you take all the credit! They’re my babies too!"

    hide goro_autumn2
    hide goro norm1
    show goro2_autumn2 at left
    show goro2 explain2 at left
    voice audio.goro_v_ehem1a
    g "*ehem* You both seem to be forgetting it was Aiden who taught you both gardening."

    show yuri pout2 at center
    voice audio.yuri_v_hmph1a
    yu "You’re just jealous ’cause you’ve literally been a bum since the project was over, Dad!"

    show goro2 sigh4 at left
    voice audio.goro_v_sigh2a
    g "I’d try and argue with you, but you’re right."
    g "It’s so hard to believe that we’ve been doing absolutely nothing for the past few weeks… considering how full our hands were for over half a year."

    show yuri sigh3 at center
    voice audio.yuri_v_sigh2a
    yu "Yeah… I don’t think I’ll ever get used to being this laid back."

    show emilia angry2 at right
    voice audio.emilia_v_rush1c
    e "Come on you two! Learn to relax, we deserve it after all!"

    hide goro2_autumn2
    hide goro2 sigh4
    show goro_autumn2 at left
    show goro talk3 at left
    voice audio.goro_v_yeah1b1
    g "Yeah… I know. The only thing left to do is to wait for the scouts."
    g "Summer is right around the corner, though. The scouts will be coming back soon."

    show yuri happy2 at center
    voice audio.yuri_v_yeah1b1
    yu "Yeah, I can’t wait to see the look on their faces when they see how big the camp is now! "
    yu "We should give them a tour on the first day, don’t you think? I think they’d really love that!"

    show goro think2 at left
    voice audio.goro_v_unsure3a1
    g "Maybe we should leave the activities for Yoshinori to take care of, since it’s what he does best. "
    g "He does always come up with ways to make them fun for everyone."

    show emilia confused2 at right
    voice audio.emilia_v_question2b
    e "Like what? Arts and crafts?"

    show yuri tease2 at center
    voice audio.yuri_v_laugh2b1
    yu "That’s way better than a flopped obstacle course reveal, if you ask me~!"

    show emilia happy1 at right
    voice audio.emilia_v_conj4b
    e "Honestly, I’m eager to meet the scouts. I’ll definitely give them a proper introduction."
    e "But they’d better not get on my bad side."

    show yuri play2 at center
    voice audio.yuri_v_tease1b1
    yu "Ohhh… Is Emilia gonna be our disciplinary committee? "

    show goro play3 at left
    voice audio.goro_v_heh1a
    g "I’d like to take you up on that offer. I’m getting too old for this."

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    show emilia talk2 at right
    voice audio.emilia_v_oh1a
    e "Oh, speaking of which… looks like some people really can’t wait for summer."

    play music camping_time loop

    show goro_autumn2 at p8_1
    show goro play3 at p8_1
    show yuri_autumn at p8_2
    show yuri play2 at p8_2
    show emilia_autumn at p8_3
    show emilia happy1 at p8_3
    with move

    show darius_autumn at p8_5
    show darius norm1 at p8_5
    show lloyd_autumn at p8_4
    show lloyd angry2 at p8_4
    show jin_camp at p8_6
    show jin_glasses at p8_6
    show jin shock1 at p8_6
    show taiga_camp at p8_7
    show taiga annoyed1 at p8_7
    show yoichi_camp at p8_8
    show yoichi annoyed3 at p8_8
    with dissolve

    hide yuri_autumn
    hide yuri play2
    show yuri_autumn at p8_2
    show yuri play2 at p8_2
    voice audio.lloyd_v_rush1a2
    l "Attention! Straighten your back! "
    l "You! Stop being all limp!"

    show jin shock2 at p8_6
    voice audio.jin_v_what3a
    j "Wh-What…? This is my normal posture, Lloyd…"

    show lloyd angry5 at p8_4
    voice audio.lloyd_v_annoyed1a1
    l "That’s SCOUTGRANDMASTER LLOYD to you!"
    l "From now on, you’ll do yoga two hours every morning to fix your posture!"

    show darius confused2 at p8_5
    voice audio.darius_v_think2b1
    d "Aren’t you being too harsh?"

    show yoichi playful1 at p8_8
    voice audio.yoichi_v_lloyd4a
    yi "Sorry I can’t hear your orders from up here, Pipsqueak!"
    yi "Grow five inches taller and then maybe I’ll listen."

    show lloyd rage3 at p8_4
    voice audio.lloyd_v_greet2d2
    l "HEY! That’s not how these things work!"

    show taiga playful2 at p8_7
    voice audio.taiga_v_agree3a
    t "True. It’s too late for you to grow."

    show lloyd disappoint5 at p8_4
    voice audio.lloyd_v_think2a1
    l "*EHEM* Lucky for you two, I’m a professional, so I’ll let that slide!"

    show jin confused5 at p8_6
    voice audio.jin_v_think2a1
    j "So… What’s next?"

    show darius talk2 at p8_5
    voice audio.darius_v_agree3
    d "Camping."

    show lloyd talk2 at p8_4
    voice audio.lloyd_v_agree3a1
    l "Right, camping! Let’s make a fire out of these two sticks!"

    show jin sigh1 at p8_6
    voice audio.jin_v_sigh1a
    j "I’m starting to regret this decision…"

    show yoichi angry3 at p8_8
    voice audio.yoichi_v_denial3a
    yi "I’m out. I have dogs to feed."

    show taiga angry2 at p8_7
    voice audio.taiga_v_whatthe1a
    t "Hell no! You’re not ditching, and leaving me to play house with these dorks!"
    t "Besides, it’d be really good training for them to deal with the wildest pinhead in the camp!"

    show yoichi annoyed1 at p8_8
    voice audio.yoichi_v_confused1a1
    yi "Who you calling pinhead?"

    show darius play2 at p8_5
    voice audio.darius_v_laugh1
    d "If you two join, I’ll give you a treat. Heard you like burgers and mallows."

    show taiga angry5 at p8_7
    show yoichi angry3 at p8_8
    yt "Ugh, fine."

    show lloyd excited3 at p8_4
    voice audio.lloyd_v_rush1c1
    l "Alright! March! Three two one! Three two one!"

    show jin confuseddn3 at p8_6
    voice audio.jin_v_confused1a3
    j "It’s supposed to be the other way around…"

    show darius relief2 at p8_5
    voice audio.darius_v_wait1a
    d "Shh…"

    hide lloyd_autumn
    hide lloyd excited3
    hide darius_autumn
    hide darius relief2
    hide jin_camp
    hide jin_glasses
    hide jin confuseddn3
    hide yoichi_camp
    hide yoichi angry3
    hide taiga_camp
    hide taiga angry5
    with dissolve

    show goro_autumn2 at left
    show goro play3 at left
    show yuri_autumn at center
    show yuri play2 at center
    show emilia_autumn at right
    show emilia confused6 at right
    with move
    voice audio.emilia_v_think1
    e "I guess… they’re getting the hang of it…"

    show goro comp5 at left
    voice audio.goro_v_laugh1a1
    g "Haha, give them some time. It takes some getting used to."

    show yuri comp2 at center
    voice audio.yuri_v_laugh2b1
    yu "Hehe, I remember my first time leading the scouts… I was just as clueless as they were."
    yu "I usually let Yoshi handle most of that stuff!"


    #Good Ending
    if score_aiden > 24 and score_aiden <= 49:
        show emilia confused2 at right
        voice audio.emilia_v_yoshi3
        e "Speaking of Yoshi… When are he and Aiden going to be back? "

        show yuri irked2 at center
        voice audio.yuri_v_rush1d1
        yu "Give them a break, Emilia! Let them enjoy their special honeymoon!"

        show emilia angry2 at right
        voice audio.emilia_v_annoyed2
        e "How come those two are allowed to go on dates and we’re not?!"

        show goro confused2 at left
        voice audio.goro_v_think1a1
        g "I don’t remember forbidding it."

        show emilia rage4 at right
        voice audio.emilia_v_what3a
        e "What?! So, you’re telling me I could’ve been out on a vacation instead of digging up soil and weeding for weeks?!"

        show goro explain2 at left
        voice audio.goro_v_well1b
        g "Well, you didn’t ask."

        show yuri tease2 at center
        voice audio.yuri_v_hmph1a
        yu "Don’t act like you didn’t enjoy being here with us, Emilia! You were always the first one up doing all the chores!"

        show emilia eyeroll6 at right
        voice audio.emilia_v_hmph1a
        e "It’s because I thought there was nothing else to do! I’ve been scammed!"

        show yuri tease4 at center
        voice audio.yuri_v_conj2c2
        yu "Now you know what it feels like."

        show goro happy2 at left
        voice audio.goro_v_conj9a1
        g "Honestly, I’m glad those two spent some time together before we get busy again for the next term."

        show yuri laugh1 at center
        voice audio.yuri_v_response2a1
        yu "I know right? It’s a really nice vacation do-over for Aiden!"

        show goro comp3 at left
        voice audio.goro_v_laugh1a1
        g "Yoshinori had been planning this surprise date for a while now. It’s actually adorable to see those two so madly in love."

        show yuri play2 at center
        voice audio.yuri_v_goro5a
        yu "Now you get what I feel, Dad?!"

        show emilia angry2 at right
        voice audio.emilia_v_bossy1a
        e "Hey, don’t change the subject! We need to go on a vacation too!"

        show goro happy2 at left
        voice audio.goro_v_actually2a
        g "If it helps, they texted me that they’re already on their way back."

        show emilia bold3 at right
        voice audio.emilia_v_amazed1a
        e "If that’s the case then pack your bags, Yuri! We’re going to see that new ‘JS’ movie!"

        hide yuri_autumn
        hide yuri play2
        show yuri2_autumn at center
        show yuri2 fangirl2 at center
        voice audio.yuri_v_kyaa1a
        yu "KYAAAA! YES, YES! Count me in!"

        hide emilia_autumn
        hide emilia bold3
        hide yuri2_autumn
        hide yuri2 fangirl2
        with dissolve

        show goro comp1 at left
        g "…"

        $ renpy.music.stop(channel='music', fadeout = 1.0)
        $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
        $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
        scene cg white
        hide screen location
        hide screen timeline
        hide screen quick_menu
        $ quick_menu = False
        with Dissolve(3.0)

        $ location = location_entrance
        show screen location
        show screen timeline
        show screen quick_menu
        scene cga13:
            yalign 1.0 xalign 0.5
        with Dissolve(2.0)
        $ quick_menu = True
        play music buddy_oath_casual loop
        play bgsound sfxloop_birds loop
        voice audio.aiden_vsa29_line1
        a "Ahh… It’s good to be back!"

        voice audio.yoshi_vsa29_line1
        yo "We’ve only been gone for a couple days, but I missed Camp Buddy already."

        voice audio.aiden_vsa29_line2
        a "Me too! But I gotta say, going on a vacation with you was really fun too!"

        voice audio.yoshi_vsa29_line2
        yo "I’m glad you enjoyed it, Aiden! I did promise you I’d take you on an actual date once everything settled down."

        voice audio.yoshi_vsa29_line3
        yo "And today marks exactly six months since we started dating."

        voice audio.aiden_vsa29_line3
        a "You kept count?!"

        voice audio.yoshi_vsa29_line4
        yo "Of course! It’s really special to me."

        voice audio.aiden_vsa29_line4
        a "Aww that’s really sweet, Yoshi! You’re special to me tooooo~"

        voice audio.aiden_vsa29_line5
        a "But now that we’ve had our fun, it’s time for us to get back to work!"

        voice audio.yoshi_vsa29_line5
        yo "Yeah! The next term is only a few days away and the scouts are finally gonna see everything we worked hard on."

        voice audio.aiden_vsa29_line6
        a "I can’t wait to see the look on their faces when they do! And of course, when they try my new and improved menu!"

        voice audio.yoshi_vsa29_line6
        yo "Me too, Aiden!"

        voice audio.aiden_vsa29_line7
        a "Let’s go in, then? I’m sure everybody’s waiting for us too!"

        voice audio.yoshi_vsa29_line7
        yo "Yeah! We’re finally home!"

        #scroll up

        $ renpy.music.stop(channel='music', fadeout = 6.0)
        $ renpy.music.stop(channel='bgsound', fadeout = 6.0)
        $ renpy.music.stop(channel='bgsound2', fadeout = 6.0)

        hide screen location
        hide screen timeline
        hide screen quick_menu
        $ quick_menu = False
        $ say_box = False
        show cga13:
            yalign 1.0 xalign 0.5
            linear 5 yalign 0.0
        $ renpy.pause(6.0, hard=True)
        scene cg white with Dissolve(3.0)
        $ renpy.pause (2.0, hard=True)

        scene bg_theend with dissolve
        $ renpy.pause (5.0, hard=True)

        $persistent.routes_completed.append("aiden")
        $renpy.save_persistent()

        return

    #Perfect Ending
    else:
        show emilia confused2 at right
        voice audio.emilia_v_yoshi3
        e "Speaking of Yoshi… Where is he?! I haven’t seen him today."

        show yuri tease2 at center
        voice audio.yuri_v_yeah2a3
        yu "Oh, yeah, he and Aiden are both gone. Hihi, are they sneaking around again?"

        show goro talk3 at left
        voice audio.goro_v_actually1a
        g "Yoshinori actually requested a day off for both of them, since we don’t have anything going on."
        g "He mentioned that since the hotel trip wasn’t relaxing for Aiden, he wanted to make up for it."

        show yuri excited2 at center
        voice audio.yuri_v_tease1a2
        yu "Ohhh~ They went on a little date then, huh? "
        yu "I guess that’s the best thing to do with so much free time. Why don’t we go somewhere too?!"

        show emilia sigh1 at right
        voice audio.emilia_v_sigh1a
        e "Yeah… I’d kill to be in a nice, air-conditioned establishment too…"

        show yuri amazed3 at center
        voice audio.yuri_v_tease1b2
        yu "Ooooh! How about we go to the movies?! I heard there’s some new one called ‘JS’ out today~ "

        show emilia happy1 at right
        voice audio.emilia_v_agree1a1
        e "Sure, I think I’ve finished all the chores for the day. Turns out they aren’t so bad when nobody is around."

        show yuri excited4 at center
        voice audio.yuri_v_celebrate1a
        yu "I’ll go get my coat! Yipeee~"

        show emilia shock2 at right
        voice audio.emilia_v_wait1c
        e "W-Wait, Sir Goro didn’t even say yes yet…!"

        show goro comp2 at left
        voice audio.goro_v_alright2a2
        g "It’s alright Emilia, you girls go ahead. I’ll take charge here."

        show yuri laugh1 at center
        voice audio.yuri_v_thanks1a
        yu "There’s your yes, Emilia! Thanks, Dad~!"

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
        $ quick_menu = True
        scene bg_beach_summer_day with fade
        play music coastal_groove loop
        play bgsound sfxloop_wavesday loop

        show aiden_swim at left2
        show aiden relief4 at left2
        show yoshi_swim at right2
        show yoshi relief1 at right2
        voice audio.aiden_v_relief2a
        a "Fwahhh! Now this is the life! "
        a "Say… What made you decide on this trip all of a sudden?"

        show yoshi relief2 at right2
        voice audio.yoshi_v_well1
        yo "Well… I promised you that I’d take you on an actual date once everything settled down, remember?"

        show aiden amazed2 at left2
        voice audio.aiden_v_amazed2a2
        a "Wow, I already forgot about that, hahaha!"

        show yoshi laugh1 at right2
        voice audio.yoshi_v_laugh1
        yo "And, today is also exactly six months since we started dating."

        show aiden happy2 at left2
        voice audio.aiden_v_really1a
        a "You kept count?!"

        show yoshi comp2 at right2
        voice audio.yoshi_v_agree1b1
        yo "Of course. It’s really special to me."

        show aiden comp2 at left2
        voice audio.aiden_v_aww2a
        a "Aww that’s really sweet, Yoshi! You’re special to me tooooo~"
        a "I wish I had a surprise for you, but you really caught me off guard when you said we were going out today. "

        show aiden sigh3 at left2
        voice audio.aiden_v_sigh1a
        a "I was surprised when you woke me up this morning and our bags were already packed, and all you’d say was that we were driving somewhere!"

        show yoshi comp3 at right2
        voice audio.yoshi_v_relief3
        yo "Well, I’ve been planning this for a while now, so I’m glad everything went smoothly!"

        show aiden laugh1 at left2
        voice audio.aiden_v_laugh2a1
        a "Haha, I guess I shouldn’t be surprised by your preparedness. You really are a scout at heart."

        show yoshi bold2 at right2
        voice audio.yoshi_v_laugh1
        yo "We have Buddy Law #1 to thank for that!"

        show aiden play2 at left2
        voice audio.aiden_v_yoshi3a
        a "I gotta say, Yoshi~ You picked the perfect spot for us to have a vacation! "

        show yoshi happy2 at right2
        voice audio.yoshi_v_excited1
        yo "I knew you’d like this place! The beach is nice and private, with nobody telling us what to do! "

        show aiden play3 at left2
        voice audio.aiden_v_yeah2b2
        a "You know what else is good about being somewhere so private~?"

        show yoshi confused2 at right2
        voice audio.yoshi_v_what1
        yo "What?"

        hide aiden_swim
        hide aiden play3
        show aiden_naked at left2
        show aiden relief2 at left2
        voice audio.aiden_v_relief1a1
        a "I don’t have to worry about wearing anything! Just let it all hang loose and let the breeze flow through your legs."

        hide yoshi_swim
        hide yoshi confused2
        show yoshi2_swim at right2
        show yoshi2 laugh2 at right2
        voice audio.yoshi_v_laugh1
        yo "Haha, why am I not surprised that’s what you wanted to do?"
        yo "Guess I’ll join you skinny-dipping, Aiden."

        hide yoshi2_swim
        hide yoshi2 laugh2
        show yoshi_naked at right2
        show yoshi relief2 at right2
        voice audio.yoshi_v_relief1
        yo "Ahhh, this does feel good~ "

        hide aiden_naked
        hide aiden relief2
        show aiden_naked2 at left2
        show aiden tease1 at left2
        voice audio.aiden_v_laugh1c1
        a "Hehe, you know what will make this a lot better?"

        show yoshi play2 at right2
        voice audio.yoshi_v_well1
        yo "If we fooled around?"

        show aiden pout4 at left2
        voice audio.aiden_v_swear2a1
        a "Dang it. You know me too well."

        hide yoshi_naked
        hide yoshi play2
        show yoshi_naked2 at right2
        show yoshi play6 at right2
        voice audio.yoshi_v_laugh6
        yo "If your dick wasn’t standing to attention at me, maybe I wouldn’t have gotten the hint."

        show aiden tease1 at left2
        voice audio.aiden_v_oho1a
        a "You say that, but you’re already rock hard too!"

        show yoshi_naked2 at center
        show yoshi play3 at center
        with move
        voice audio.yoshi_v_rush5
        yo "What are we waiting for then?"

        scene cg black
        hide screen location
        hide screen timeline
        hide screen quick_menu
        $ quick_menu = False
        with fade

        jump day10_aiden_8
        # if score_bot == score_top:
        #     $ position = renpy.random.randint(1, 2)
        #
        # if score_top > score_bot or position == 1:
        #     hide screen location
        #     hide screen timeline
        #     hide screen quick_menu
        #     $ quick_menu = False
        #     with fade
        #     $ say_box = False
        #     $ fp_stage = 'mga5_b'
        #     $ success_jumpto = 'day10_aiden_8'
        #     $ failed_jumpto = 'day10_aiden_pe_aftersx'
        #     jump fp
        #
        # elif score_bot > score_top or position == 2:
        #     hide screen location
        #     hide screen timeline
        #     hide screen quick_menu
        #     $ quick_menu = False
        #     with fade
        #     $ say_box = False
        #     $ fp_stage = 'mga5_f'
        #     $ success_jumpto = 'day10_aiden_8'
        #     $ failed_jumpto = 'day10_aiden_pe_aftersx'
        #     jump fp

label day10_aiden_pe_aftersx:
    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black
    hide screen location
    hide screen timeline
    hide screen quick_menu
    $ quick_menu = False
    with Dissolve(3.0)
    $ time_transition_day_to_sunset_summer()
    $ renpy.pause (2.0, hard=True)

    $ location = location_beach
    $ time = timeline_timesunset
    show screen location
    show screen timeline
    show screen quick_menu
    $ quick_menu = True
    scene cga14 1 with fade
    play music go_with_the_flow_slow loop
    play bgsound sfxloop_wavesday loop

    voice audio.aiden_vsa30_line1
    a "Ahh… This was the perfect day, Yoshi!"

    voice audio.aiden_vsa30_line2
    a "We got to swim and fool around all day, and to top it all off with a romantic sunset dinner… Damn you really outdid yourself this time!"

    voice audio.yoshi_vsa30_line1
    yo "I’m glad you enjoyed it, Aiden…"

    voice audio.aiden_vsa30_line3
    a "Heh! Just you wait for my turn and I’ll blow you away with my style!"

    voice audio.yoshi_vsa30_line2
    yo "Oh yeah? I’d like to see you try."

    voice audio.aiden_vsa30_line4
    a "Eh, I guess that’s a lotta work for simple me. How about I just blow you instead?"

    voice audio.yoshi_vsa30_line3
    yo "Hahaha! Don’t you think we did lots of that already?"

    voice audio.aiden_vsa30_line5
    a "Hehe~ You know I can’t get enough of you though, Yoshi~"

    voice audio.aiden_vsa30_line6
    a "But eh, just chillin’ and watching the sunset with you is way better."

    voice audio.yoshi_vsa30_line4
    yo "Oh, really now? That doesn’t sound like you at all, Aiden."

    voice audio.aiden_vsa30_line7
    a "I’m serious! To think I’d be missing out on all of this if I had made a different choice."

    voice audio.yoshi_vsa30_line5
    yo "Yeah… If it weren’t for that, I wouldn’t be sitting here with you… "

    voice audio.yoshi_vsa30_line6
    yo "I’m really glad you stayed, Aiden…"

    voice audio.yoshi_vsa30_line7
    yo "Every moment I have with you is worth a thousand lifetimes."

    voice audio.aiden_vsa30_line8
    a "Yoshi…"

    show cga14 2 with Dissolve(0.25)
    voice audio.yoshi_vsa30_line8
    yo "I love you Aiden…"

    voice audio.aiden_vsa30_line9
    a "I love you too..."

    $ renpy.music.stop(channel='music', fadeout = 3.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 3.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 3.0)
    scene cg white
    hide screen location
    hide screen timeline
    hide screen quick_menu
    $ quick_menu = False
    with Dissolve(3.0)
    $ renpy.pause (2.0, hard=True)

    scene bg_theend with dissolve
    $ renpy.pause (5.0, hard=True)

    $persistent.routes_completed.append("aiden")
    $renpy.save_persistent()
