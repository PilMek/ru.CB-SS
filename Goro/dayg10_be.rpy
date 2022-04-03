image entrance_transition:
    "images/bgs/bg-w-entrance-day.png"
    pause 1.0
    "images/bgs/bg-p-entrance-day.png" with Dissolve(4.0)

label day10_goro_be:
    $ day = "84"
    $ time = timeline_timeday
    $ location = location_office
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    $ working = True

    scene bg_office_winter_day with fade
    play music brand_new_day_winter loop
    play bgsound sfxloop_birds loop

    show goro2_autumn at left2
    show goro2 shy5 at left2
    show yoshi_autumn at right2
    show yoshi norm3 at right2
    voice audio.william_v_sigh2
    w "That’s truly unfortunate… I was certain that Mr. Nomoru would accept this offer."

    show yoshi talk1 at right2
    voice audio.yoshi_v_please1a
    yo "I hope you understand, Mr. Clermont, but we’re more than satisfied with the state of Camp Buddy."
    yo "We also believe that it will allow us to maintain the spirit and quality of the camp better than we otherwise could."

    voice audio.william_v_well1a
    w "Well, it sounds like he’s fully made up his mind! I won’t try and convince you all any further!"
    w "You can relax and not concern yourself about this anymore, but I would like to express that the offer will stay on the table!"

    voice audio.william_v_comp3
    w "Consider it an open opportunity should Mr. Nomoru ever change his mind."

    show yoshi comp2 at right2
    voice audio.yoshi_v_gratitude2
    yo "I really appreciate your generosity, Mr. Clermont. Thank you for giving us a chance."

    voice audio.william_v_bye2b
    w "Of course! Until next time!"

    play sound sfx_phonebutton
    show yoshi sigh1 at right2
    voice audio.yoshi_v_relief1
    yo "Whew…! That’s done!"
    yo "I think we settled it in the best way possible, Goro. Now I’m glad it’ll finally be off your chest!"

    show goro2 shy6 at left2
    voice audio.goro_v_sigh2a
    g "I still feel guilty about all this… And you even had to make the call, too…"

    show yoshi talk2 at right2
    voice audio.yoshi_v_confident3
    yo "Like I told you, I’ll try and take over more things from now on! You don’t have to worry about a single thing!"
    yo "I think this is a good start if we’re really planning on easing the work away from you!"

    show goro2 shy3 at left2
    voice audio.goro_v_well1a
    g "Well… I still am serious about completing the project at least. "

    show yoshi comp2 at right2
    voice audio.yoshi_v_well1
    yo "Well, there’s not too much of that left! It’ll only take a few more months until we’re completely done!"

    show goro2 sigh1 at left2
    voice audio.goro_v_unsure2a
    g "All of a sudden, I’m doubting if this was the right decision…"

    hide yoshi_autumn
    hide yoshi comp2
    show yoshi2_autumn at right2
    show yoshi2 sigh1 at right2
    voice audio.yoshi_v_sigh3a
    yo "*sigh* You must still be thinking you have to be responsible for everyone…"

    hide goro2_autumn
    hide goro2 sigh1
    show goro_autumn at left2
    show goro worry2 at left2
    voice audio.goro_v_agree1b1
    g "I am… It’s what I’ve done for so long… It’s pretty much hard-wired into me."
    g "And it just felt so surreal turning down something I spent my whole life working towards…"

    show goro explain2 at left2
    voice audio.goro_v_conj10a1
    g "After the first term, I kept building up the camp until it had grown and spread."
    g "Then I found myself managing several branches at once, and I used them as an excuse to shut away my pain, and fill the emptiness in my heart."

    show goro sad3 at left2
    voice audio.goro_v_conj1a1
    g "I lost myself along the way, and despite expanding the camp to what I thought was successful, all of it became meaningless…"

    show yoshi2 worry2 at right2
    voice audio.yoshi_v_oops2
    yo "And yet you pushed yourself throughout this project too…"
    yo "If only I had known sooner, I could’ve at least taken some of the load off of you…"

    show goro upset5 at left2
    voice audio.goro_v_conj9a1
    g "Honestly, I was so distracted by our time together…"
    g "Every moment I spent outside of work, it made me realize what I had been missing out on for so long…  "

    hide yoshi2_autumn
    hide yoshi2 worry2
    show yoshi_autumn at right2
    show yoshi comp2 at right2
    voice audio.yoshi_v_but1
    yo "But now, you finally get to start over! And for real, this time!"

    show goro sigh4 at left2
    voice audio.goro_v_thanks1b1
    g "I don’t know what I’ll do yet… But regardless, thank you for supporting my decision, Yoshinori."

    show yoshi comp3 at right2
    voice audio.yoshi_v_agree1a
    yo "Of course, Goro… "

    show yoshi_autumn at center
    show yoshi shock1 at center
    show goro_autumn at left
    show goro shock1 at left
    with move

    show yuri_winter at right
    show yuri irked1 at right
    with dissolve

    voice audio.yuri_v_goro9a
    yu "Ah, there you are, Dad!"

    show goro talk3 at left
    voice audio.goro_v_goodam1a1
    g "Good morning, Yuri."

    show yuri angry3 at right
    voice audio.yuri_v_angry2a1
    yu "Don’t ‘good morning’ me! You’ve got a lot of explaining to do!"
    yu "What was that all about yesterday? Did you really turn down Mr. Clermont’s offer?!"

    show goro explain2 at left
    voice audio.goro_v_agree1b1
    g "Yes… In fact, Yoshinori just called him earlier to confirm it…"

    show yuri worry2 at right
    voice audio.yuri_v_but2a
    yu "Wh-Why…?"

    show goro worry2 at left
    voice audio.goro_v_well1a
    g "Well, dear… I’m sure you remember how we tried this together before…"
    g "You saw how difficult and inefficient things were because we weren’t prepared."

    show goro sad3 at left
    voice audio.goro_v_sigh2a
    g "And after experiencing what we all thought was the peak of Camp Buddy, it turns out it wasn’t really a good thing."

    show yuri sad4 at right
    voice audio.yuri_v_oh4a
    yu "Oh…"

    show goro sigh1 at left
    voice audio.goro_v_conj4a
    g "All I’m saying is that we should be content with where all of us are now…"
    g "We don’t need anything more than what we already have… "

    show yuri worry4 at right
    voice audio.yuri_v_comp1c1
    yu "I understand, Dad… "

    show yuri sad4 at right
    voice audio.yuri_v_conj5a
    yu "Honestly, I’d hate to risk seeing you at your worst again…   "
    yu "We’ve come such a long way just to fix things and return to how it was when we started…"

    show goro comp2 at left
    voice audio.goro_v_relief1a
    g "I’m relieved you see it too, dear."

    show yuri sigh1 at right
    voice audio.yuri_v_sigh2a
    yu "*sigh* You can just be so reckless sometimes, you know?"
    yu "I mean… You could’ve just told us that to begin with!"

    show goro worry3 at left
    voice audio.goro_v_agree1b1
    g "Yes… I’m sorry. I had to sort things out with Yoshinori first before I could tell everyone."

    show yuri talk2 at right
    voice audio.yuri_v_yeah2a1
    yu "Speaking of that! You two came home so late last night… and with a motorcycle too!"
    yu "You have to explain it to everyone else! They wouldn’t stop asking me what was going on all morning!"

    show yoshi talk1 at center
    voice audio.yoshi_v_think1a
    yo "I think everyone’s at the mess hall having breakfast. Maybe we should take the chance to talk before work begins today."

    hide goro_autumn
    hide goro worry3
    show goro2_autumn at left
    show goro2 talk1 at left
    voice audio.goro_v_agree6a2
    g "You’re right. Everyone needs to know."

    show yuri confused1 at right
    yu "...?"

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
    scene bg_messhall_winter_day with fade
    play music buddy_oath_casual loop
    play bgsound sfxloop_crowd loop

    show darius_winter at p8_1
    show darius norm3 at p8_1
    show aiden2_autumn at p8_3
    show aiden2 talk5 at p8_3
    show lloyd_winter at p8_2
    show lloyd norm3 at p8_2
    show yoshi_autumn at p8_4
    show yoshi norm3 at p8_4
    show goro2_autumn at p8_5
    show goro2 norm3 at p8_5
    show yuri_autumn at p8_6
    show yuri norm3 at p8_6
    show emilia_winter3 at p8_7
    show emilia norm3 at p8_7
    show jin_autumn at p8_8
    show jin_glasses at p8_8
    show jin norm3 at p8_8
    voice audio.aiden_v_oh3a
    a "Oooohhh… I didn’t know that was happening at all yesterday…"

    show lloyd worry2 at p8_2
    voice audio.lloyd_v_agree2c1
    l "Yeah… That was a huge decision to make, and honestly Sir Goro made the right call."

    show darius explain2 at p8_1
    voice audio.darius_v_think1a1
    d "Rebuilding other branches is a life’s worth of work."

    show jin worry2 at p8_8
    voice audio.jin_v_yeah2a
    j "Y-Yeah… Even this project takes so much time and effort to make happen…"

    show emilia explain3 at p8_7
    voice audio.emilia_v_conj1c1
    e "At first I was baffled too, but hearing just how big of an undertaking it was… It might be too much for a small group of people like us…"

    hide goro2_autumn
    hide goro2 norm3
    show goro_autumn at p8_5
    show goro worry3 at p8_5
    voice audio.goro_v_glad1a
    g "I’m glad you all understand… "
    g "Expanding the camp we have right now is manageable, but opening another branch is a totally different story."

    show yoshi explain2 at p8_4
    voice audio.yoshi_v_think1a
    yo "We thought it would be best if we concentrated our efforts and made one perfect Camp Buddy."

    hide goro_autumn
    hide goro worry3
    show goro2_autumn at p8_5
    show goro2 explain2 at p8_5
    voice audio.goro_v_ehem1a
    g "I’d also like to take this chance to tell you all something very important…"

    show yuri confused2 at p8_6
    voice audio.yuri_v_oh3a
    yu "Oh? What is it, Dad?"

    show goro2 talk1 at p8_5
    voice audio.goro_v_request2a1
    g "Starting the next term, Yoshinori will be taking my place as the camp president."

    hide aiden2_autumn
    hide aiden2 talk5
    show aiden_autumn at p8_3
    show aiden shock3 at p8_3
    hide lloyd_winter
    hide lloyd worry2
    show lloyd_winter at p8_2
    show lloyd worry2 at p8_2
    voice audio.aiden_v_shock1a1
    a "WHOA!"

    show lloyd excited3 at p8_2
    voice audio.lloyd_v_amazed2a1
    l "Oh my god, that’s amazing, Yoshi!"

    show darius happy1 at p8_1
    voice audio.darius_v_amazed1
    d "Congrats."

    show emilia play2 at p8_7
    voice audio.emilia_v_laugh1a
    e "Hehe, that sounds about right~!"

    hide yuri_autumn
    hide yuri confused2
    show yuri2_autumn at p8_6
    show yuri2 excited2 at p8_6
    voice audio.yuri_v_kyaa1a
    yu "KYAAA! This has been your dream, hasn’t it, Yoshi?!"

    show yoshi comp3 at p8_4
    voice audio.yoshi_v_thanks3
    yo "Thank you, everyone… I promise I’ll do my best!"

    show jin worry4 at p8_8
    voice audio.jin_v_confused2b5
    j "B-But what about Sir Goro?"

    show aiden confused3 at p8_3
    voice audio.aiden_v_yeah2a1
    a "Oh yeah, Gramps! Does this mean you’re officially retiring too?"

    show goro2 shy6 at p8_5
    voice audio.goro_v_think1a1
    g "I will still finish my commitment to this project, but after that I’m not sure…"
    g "One thing I know is that it’s for the best if I have some time outside of Camp Buddy."

    hide yuri2_autumn
    hide yuri2 excited2
    show yuri_autumn at p8_6
    show yuri comp2 at p8_6
    voice audio.yuri_v_celebrate1a
    yu "Yay, Dad! I’m so happy you’re finally giving yourself a well-deserved break!"

    show goro2 shy4 at p8_5
    voice audio.goro_v_no3a1
    g "I… don’t think I’ll come back to the job, dear."

    show yuri worry2 at p8_6
    voice audio.yuri_v_oh4a
    yu "Oh… You’re resigning permanently…?"

    show goro2 talk2 at p8_5
    voice audio.goro_v_agree1b2
    g "Yes."

    show lloyd worry3 at p8_2
    voice audio.lloyd_v_think1a1
    l "I don’t mean anything bad, but… are you sure about that, sir? I mean… this has been your life’s work! "

    show darius talk2 at p8_1
    voice audio.darius_v_agree3
    d "Exactly, Lloyd. He’s been doing this for a long time."

    hide aiden_autumn
    hide aiden confused3
    show aiden2_autumn at p8_3
    show aiden2 worry2 at p8_3
    hide lloyd_winter
    hide lloyd worry3
    show lloyd_winter at p8_2
    show lloyd worry3 at p8_2
    voice audio.aiden_v_unsure7a
    a "Isn’t there a way around this? Like, you know, Gramps can just lay back and let us do all the work!"

    show emilia think3 at p8_7
    voice audio.emilia_v_think1
    e "I think that defeats the purpose. If Sir Goro sticks around, it would be in his nature to assist the camp in every way he can. "
    e "He won’t be able to have time for himself if that’s the case."

    show jin sad2 at p8_8
    voice audio.jin_v_unsure1a2
    j "I don’t think things will be the same without Sir Goro…"

    show yuri irked1 at p8_6
    voice audio.yuri_v_rush1b1
    yu "Come on, guys! That’s why Yoshi’s stepping up to take his place! I’m sure Dad thought all of this out!"

    show yoshi talk1 at p8_4
    voice audio.yoshi_v_right5
    yo "Yuri’s right, everyone. Instead, we should all be grateful for all the hard work and time Goro dedicated to the camp since we were scouts!"

    show lloyd talk3 at p8_2
    voice audio.lloyd_v_shock1a1
    l "Oh, of course, of course!"

    show aiden2 sigh1 at p8_3
    voice audio.aiden_v_well1a1
    a "Well, if that’s what’ll make Gramps happy, then I guess…"

    show jin comp2 at p8_8
    voice audio.jin_v_thanks1a3
    j "Thank you for your service, Sir Goro."

    hide goro2_autumn
    hide goro2 talk2
    show goro_autumn at p8_5
    show goro comp2 at p8_5
    voice audio.goro_v_thanks2b1
    g "Thank you all again for understanding… "

    show yuri comp2 at p8_6
    voice audio.yuri_v_aww2c
    yu "This’ll be really good for you, Dad! You’re finally letting go of all these responsibilities! I’m so excited for your retirement!"
    yu "And you chose the best person to pass the torch to! With Yoshi, the camp will be in good hands!"

    hide goro_autumn
    hide goro comp2
    show goro2_autumn at p8_5
    show goro2 explain2 at p8_5
    voice audio.goro_v_agree4a1
    g "Exactly. I’m sure the camp’s future is guaranteed with Yoshinori."

    show goro2 talk1 at p8_5
    voice audio.goro_v_conj1a1
    g "However, as I said earlier, I will continue to lead alongside Yoshinori for the remaining span of the project, so nothing will change until then!"
    g "We still have a long winter ahead – let’s make sure the scouts have the best version of Camp Buddy to come back to!"

    show yoshi talk2 at p8_4
    show lloyd talk2 at p8_2
    show darius talk1 at p8_1
    show yuri talk2 at p8_6
    show emilia talk2 at p8_7
    show jin talk2 at p8_8
    hide aiden2_autumn
    hide aiden2 sigh1
    show aiden_autumn at p8_3
    show aiden talk6 at p8_3
    all "Yes, sir! "

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg white with fade
    $ day = "85"
    $time = timeline_timeday
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
    show cg8 2g with Dissolve(0.25)
    voice audio.yoshi_vsg29_line1
    yo "Meanwhile, Aiden kept up his regular maintenance duties, but this time around he had Emilia doing most of the other chores, like cleaning and laundry."

    voice audio.yoshi_vsa27_line8
    yo "She would complain as usual, but she did the job well and got it done on time!"

    $ day = "87"
    $time = timeline_timenight
    show cg8 3g with Dissolve(0.25)
    voice audio.yoshi_vsg29_line2
    yo "Goro and I kept the entire project well-managed, making sure we stayed on schedule, while Yuri assisted us and Aiden’s department on the side."

    $ day = "89"
    show cg8 4g with Dissolve(0.25)
    voice audio.yoshi_vsa27_line11
    yo "All in all, it was amazing to see everyone work towards a common goal, all while enjoying our time together."

    voice audio.yoshi_vsa27_line12
    yo "The days flew by, and we saw the fruits of our labor take shape as we came closer and closer to completion!"

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
    $quick_menu = True
    scene bg_site9_spring_day with fade
    play music brand_new_day loop
    play bgsound sfxloop_birds loop

    show emilia_autumn at p9_1
    show emilia norm1 at p9_1
    show yuri_autumn at p9_2
    show yuri norm1 at p9_2
    show aiden_autumn at p9_3
    show aiden norm1 at p9_3
    show yoshi_semiformal at p9_4
    show yoshi norm1 at p9_4
    show goro_semiformal at p9_5
    show goro talk1 at p9_5
    show william_formal at p9_6
    show william norm1 at p9_6
    show lloyd_autumn at p9_7
    show lloyd norm1 at p9_7
    show darius_autumn at p9_8
    show darius norm1 at p9_8
    show jin_autumn at p9_9
    show jin_glasses at p9_9
    show jin norm1 at p9_9
    voice audio.goro_v_conj2a1
    g "Finally, after months of hard work, we’ve all reached the project completion we’ve been aiming for."
    g "You’ve all worked extremely hard, and I want to express my gratitude to your dedication and commitment to seeing things through."

    show goro talk2 at p9_5
    voice audio.goro_v_william2a
    g "I’d also like to give a special thanks to Mr. Clermont, as without him we’d never have had this opportunity to grow."

    show goro talk3 at p9_5
    voice audio.goro_v_thanks2b1
    g "Thank you again, sir, for everything you’ve done, and for being here with us today."

    show william comp4 at p9_6
    voice audio.william_v_comp1b
    w "It was my pleasure, Mr. Nomoru."

    show goro explain2 at p9_5
    voice audio.goro_v_conj7a
    g "Lastly, I want to wish you all the best in your future endeavors. The completion of this project marks a culmination of my career here as the camp’s president. "
    g "I continue to wish for this place’s success, and hope that Camp Buddy will prosper for many years to come."

    show goro talk1 at p9_5
    voice audio.goro_v_rush4b2
    g "Now, to the future and whatever it might hold."

    play sound sfx_ribboncut
    show goro norm3 at p9_5
    g "*cuts ribbon*"

    play sound sfx_applause
    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black with fade
    yo "{i}Now that our project was officially complete, everyone began packing their things to leave.{/i}"
    yo "{i}It also meant that the time had come for us to say goodbye to our friends as well.{/i}"

    scene cg black
    hide screen location
    hide screen timeline
    hide screen quick_menu
    $quick_menu = False
    with fade
    $ renpy.pause (2.0, hard=True)

    $ location = location_entrance
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_entrance_past_day with fade
    play music ready_for_tomorrow loop
    play bgsound sfxloop_birds loop

    show darius_autumn at p8_2
    show darius norm3 at p8_2
    show lloyd_autumn at p8_1
    show lloyd worry1 at p8_1
    show jin_autumn at p8_3
    show jin_glasses at p8_3
    show jin worry1 at p8_3
    show emilia_autumn at p8_4
    show emilia norm3 at p8_4
    show yuri_autumn at p8_5
    show yuri sad1 at p8_5
    show yoshi_autumn at p8_6
    show yoshi confused2 at p8_6
    show aiden2_autumn at p8_8
    show aiden2 upset1 at p8_8
    show goro2_autumn at p8_7
    show goro2 norm3 at p8_7
    voice audio.yoshi_v_alright1
    yo "I think that’s the last of it, right guys?"

    show darius talk1 at p8_2
    voice audio.darius_v_agree1a
    d "Yes."

    show lloyd sigh4 at p8_1
    voice audio.lloyd_v_aww1a2
    l "Aww… I hate to leave… I’m gonna miss you guys so much!!!"

    show darius sigh1 at p8_2
    voice audio.darius_v_conj2b
    d "It can’t be helped, Lloyd… Our job is contractual after all…"

    show lloyd talk1 at p8_1
    voice audio.lloyd_v_agree2a3
    l "Yeah, and Mr. Clermont has already set us up with another gig!"
    l "Regardless, this was quite the experience. "

    show darius comp2 at p8_2
    voice audio.darius_v_laugh2a
    d "It’ll definitely be hard to top."

    show jin sigh3 at p8_3
    voice audio.jin_v_sigh2a
    j "I’m pretty bummed too… This is the first time I really had friends as close as you guys…"

    show darius sigh3 at p8_2
    voice audio.darius_v_aww1b1
    d "The consequences of being an adult… We really don’t have time in our busy lives…"

    show jin comp3 at p8_3
    voice audio.jin_v_confused2a2
    j "I’ll still come visit every now and then, though! You guys will need some tech maintenance after all."

    show yuri pain6 at p8_5
    voice audio.yuri_v_no1c3
    yu "Nooooo! Jin… my only fudanshi friend… Don’t leave me!!"

    show jin comp6 at p8_3
    voice audio.jin_v_comp1a2
    j "It’s okay, Yuri, we can always share online! I gave you my Dicksword ID."

    show lloyd happy1 at p8_1
    voice audio.lloyd_v_laugh1a1
    l "We could always hang out outside of Camp Buddy too, right?! A little get together?!"

    hide aiden2_autumn
    hide aiden2 sad1
    show aiden_autumn at p8_8
    show aiden happy2 at p8_8
    voice audio.aiden_v_yeah1a1
    a "Yeah! I’m sure Yoshi, Yuri, and I can sneak away from time to time!"
    a "And Gramps is retired now, so he has all the time in the world!"

    show goro2 explain2 at p8_7
    voice audio.goro_v_well1a
    g "Well, we’ll see. I’m not sure how often I’ll be in the area."

    show lloyd comp3 at p8_1
    voice audio.lloyd_v_aww1b1
    l "Aww, if you’re around, please call us! I’d love to hear stories about your retirement!"

    show darius play2 at p8_2
    voice audio.darius_v_celebrate1a
    d "Unlimited vacay."

    show jin perv5 at p8_3
    voice audio.jin_v_laugh3a
    j "And if you ever need a ‘hand’, I’ll gladly do the ‘job’!"

    hide goro2_autumn
    hide goro2 explain2
    show goro_autumn at p8_7
    show goro talk1 at p8_7
    voice audio.goro_v_thanks2b1
    g "Thank you, all. "

    show yuri pain3 at p8_5
    voice audio.yuri_v_aww1a
    yu "Huhuhu!! First Lloyd, Darius, and Jin are leaving, and soon Dad too! I can’t take all of this! I’m gonna cry!"

    show emilia angry6 at p8_4
    voice audio.emilia_v_wait1a1
    e "Calm down, Yuri… It’s not like they’re dying."

    show goro comp2 at p8_7
    voice audio.goro_v_comp2a1
    g "Don’t worry, dear. You and I will still talk all the time."

    show lloyd pout5 at p8_1
    voice audio.lloyd_v_annoyed1a3
    l "Hmph! Emilia is lucky she gets to stay! "

    show emilia explain3 at p8_4
    voice audio.emilia_v_well1
    e "Well, I have nowhere else to be anyway… and Aiden’s gonna need all the help he can get!"
    e "I’ve grown quite fond of this place, after all.  And I’m even adjusting to a simpler life!"

    show yuri annoy2 at p8_5
    voice audio.yuri_v_ugh3a
    yu "Ugh, you can say that AFTER you stop spending every paycheck on fancy clothes and makeup!"

    show emilia eyeroll4 at p8_4
    voice audio.emilia_v_hmph1a
    e "Hmph, I don’t see you complaining whenever I let you wear them!"

    show lloyd sigh4 at p8_1
    voice audio.lloyd_v_sigh2a
    l "You know, I think I’ll even miss this bantering."

    show darius tease2 at p8_2
    voice audio.darius_v_laugh1
    d "I’ll play fight with you if you want."

    show jin scheme2 at p8_3
    voice audio.jin_v_oh6a
    j "S-Sword fight…?"

    show yoshi explain2 at p8_6
    voice audio.yoshi_v_ehem1a
    yo "*ehem* You all don’t have to worry about us here at Camp Buddy. You have helped us more than enough, especially you, Goro."

    hide goro_autumn
    hide goro comp2
    show goro2_autumn at p8_7
    show goro2 shy5 at p8_7
    g "..."

    play sound sfx_busdoor
    show lloyd shock2 at p8_1
    voice audio.lloyd_v_shock4a1
    l "Oops! There’s our shuttle! I think that’s our cue to go. "

    show yoshi happy2 at p8_6
    voice audio.yoshi_v_bye1b
    yo "Goodbye, guys! It’s been a pleasure working with everyone!"

    show aiden comp2 at p8_8
    voice audio.aiden_v_aww2a
    a "Camp Buddy will always be here for ya’ll!"

    show yuri pain6 at p8_5
    voice audio.yuri_v_ugh3a
    yu "Huhuhuhu…"

    show darius happy2 at p8_2
    voice audio.darius_v_bye1b
    d "Goodbye now."

    hide darius_autumn
    hide darius happy2
    with dissolve

    show jin comp5 at p8_3
    voice audio.jin_v_bye1b1
    j "We’re just one message away…! "

    hide jin_autumn
    hide jin_glasses
    hide jin comp5
    with dissolve

    show lloyd comp2 at p8_1
    voice audio.lloyd_v_bye2a
    l "I’ll miss all of you guys!"

    hide lloyd_autumn
    hide lloyd comp2
    with dissolve

    play sound sfx_busengine
    show emilia_autumn at p5_1
    show emilia worry1 at p5_1
    show yuri_autumn at p5_2
    show yuri comp2 at p5_2
    show yoshi_autumn at p5_3
    show yoshi norm3 at p5_3
    show goro2_autumn at p5_4
    show goro2 confused1 at p5_4
    show aiden_autumn at p5_5
    show aiden worry1 at p5_5
    with move

    $ renpy.music.stop(channel='sound', fadeout = 2.0)
    voice audio.yuri_v_goro4a
    yu "*sniff* Even though I’m sad to see everyone go, I guess I should congratulate you, Dad…"

    show goro2 confused3 at p5_4
    voice audio.goro_v_think1c1
    g "Hm? What for?"

    show yuri comp4 at p5_2
    voice audio.yuri_v_well1a
    yu "Well, it is your first day of retirement now officially! You’re free to do whatever you want!"

    hide goro2_autumn
    hide goro2 confused3
    show goro_autumn at p5_4
    show goro talk3 at p5_4
    voice audio.goro_v_conj6a1
    g "Ah… About that."

    show yuri confused2 at p5_2
    voice audio.yuri_v_confused2a1
    yu "Huh? Did you suddenly change your mind or something?"

    show goro explain2 at p5_4
    voice audio.goro_v_no1a1
    g "No. But I think I’ll use the next few months as a chance to prepare Yoshinori here for all that awaits him."
    g "He’s been learning plenty from me, but there’s still more to turnover before the next summer term."

    hide goro_autumn
    hide goro explain2
    show goro2_autumn at p5_4
    show goro2 talk1 at p5_4
    voice audio.goro_v_conj5a
    g "I’ll stick around here for now, and make sure that he has everything he needs."

    show yoshi comp2 at p5_3
    voice audio.yoshi_v_thanks3
    yo "Thank you, Goro. I’ll make you proud!"

    show goro2 shy6 at p5_4
    voice audio.goro_v_okay2a
    g "…Right."

    show yuri happy2 at p5_2
    voice audio.yuri_v_alright1a1
    yu "Alright! That delays a little bit of my sadness at least. "
    yu "Why don’t we head to the mess hall? We can have a little snack!"

    show emilia explain5 at p5_1
    voice audio.emilia_v_well1
    e "I suppose I could whip us something up~"

    show yuri irked2 at p5_2
    voice audio.yuri_v_ugh3b
    yu "Eugh, please don’t. Come on, you guys!"

    hide goro2_autumn
    hide goro2 shy6
    show goro_autumn at p5_4
    show goro talk3 at p5_4
    voice audio.goro_v_agree3d1
    g "Right behind you, dear."

    hide goro_autumn
    hide goro talk3
    hide yuri_autumn
    hide yuri irked2
    hide emilia_autumn
    hide emilia explain5
    with dissolve

    show yoshi_autumn at left2
    show yoshi shock1 at left2
    show aiden_autumn at right2
    show aiden worry2 at right2
    with move

    voice audio.aiden_v_wait2b1
    a "Hey, Yoshi! Hold up a sec."

    show yoshi confused2 at left2
    voice audio.yoshi_v_oh4
    yo "Oh, what is it, Aiden?"

    hide aiden_autumn
    hide aiden worry2
    show aiden2_autumn at right2
    show aiden2 worry5 at right2
    voice audio.aiden_v_well1c1
    a "Well… It’s about you and Gramps."
    a "I know we’ve been so busy with the project, but I haven’t got the chance to check in."

    show aiden2 worry4 at right2
    voice audio.aiden_v_worry1a
    a "How have you two been doing, you know… relationship-wise?"

    hide yoshi_autumn
    hide yoshi confused2
    show yoshi2_autumn at left2
    show yoshi2 worry2 at left2
    voice audio.yoshi_v_ah2
    yo "A-Ah, well… Honestly, we haven’t been able to do much together thanks to all the work."
    yo "And by the sound of things, we’ll probably be pretty busy from now till the start of next term, too."

    show aiden2 upset6 at right2
    voice audio.aiden_v_oh4a
    a "I see…"

    hide yoshi2_autumn
    hide yoshi2 worry2
    show yoshi_autumn at left2
    show yoshi comp2 at left2
    voice audio.yoshi_v_comp4
    yo "But don’t worry, Aiden! Goro and I are going to make things work!"
    yo "He and I already talked about it, and we’re on the same page."

    show aiden2 comp2 at right2
    voice audio.aiden_v_alright1a3
    a "Alright… I just wanted to make sure."

    show yoshi comp5 at left2
    voice audio.yoshi_v_agree1a
    yo "Of course. Now come on, let’s catch up with the others. There’s still so much more to do!"

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black with fade
    yo "{i}With just a short time left before the summer term started, Goro stayed true to his word and made sure to teach me everything else I needed.{/i}"
    yo "{i}It was honestly overwhelming to take it all in, and I sometimes wished it didn’t have to be this way… If only Goro would stay here…{/i}"
    yo "{i}But I can’t force him, and I want him to be happy too… I even tried to make the time special for us and make each day memorable as best I could.{/i}"
    yo "{i}Aiden’s questions continued to echo in my mind, and a part of me was unsure of what would become of Goro and I after this final push…{/i}"
    yo "{i}I just have to stay resolute, and remember that all of this is for the sake of the camp and Goro’s happiness…{/i}"
    yo "{i}It will all be worth it in the end…{/i}"

    scene cg white
    hide screen location
    hide screen timeline
    hide screen quick_menu
    $ quick_menu = False
    with Dissolve(3.0)

    #credits
    $renpy.movie_cutscene("images/Camp Buddy Scoutmaster Season Credits.webm")
    jump day10_goro_be_aftercredits

label day10_goro_be_aftercredits:
    scene cg black
    hide screen location
    hide screen timeline
    hide screen quick_menu
    $quick_menu = False
    with fade
    $ time_transition_spring_to_summer()
    $ renpy.pause (2.0, hard=True)

    $ season = season_summer
    $ day = "284"
    $ location = location_entrance
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_entrance_past_day with fade
    play music old_familiar_home_slow loop
    play bgsound sfxloop_birds loop

    show goro2_biker at left2
    show goro2 shy1 at left2
    show yoshi_autumn at right2
    show yoshi confused2 at right2
    voice audio.yoshi_v_think1a
    yo "Do you have everything you need?"

    show goro2 shy4 at left2
    voice audio.goro_v_agree1b1
    g "Yes. Yuri already scheduled a moving truck for all my stuff."

    show yoshi confused3 at right2
    voice audio.yoshi_v_conj6a
    yo "Have you said goodbye to everyone as well?"

    show goro2 shy6 at left2
    voice audio.goro_v_agree3d2
    g "Of course. Aiden was still trying to convince me to stay."

    show yoshi comp5 at right2
    voice audio.yoshi_v_comp4
    yo "Don’t worry, I’m sure he’ll understand eventually."
    yo "But you must be excited that your retirement is finally here!"

    show goro2 talk1 at left2
    voice audio.goro_v_agree1b2
    g "Yes. I’ve been looking forward to it, especially since we had to work the entire spring just to get everything in place for your takeover."

    show yoshi confused2 at right2
    voice audio.yoshi_v_worry2
    yo "Do you have your bike fully checked and tuned up? It’s going to be a long drive to where you’re going."

    show goro2 disappoint3 at left2
    voice audio.goro_v_response3a1
    g "Yeah. You don’t need to check everything for me now, Yoshinori. I can handle myself."

    hide yoshi_autumn
    hide yoshi confused2
    show yoshi2_autumn at right2
    show yoshi2 comp2 at right2
    voice audio.yoshi_v_well2
    yo "Well… If you’re really going now, just don’t forget to call me, alright?"
    yo "O-Oh…! We should schedule a road trip, too! How about every weekend?"

    hide goro2_biker
    hide goro2 disappoint3
    show goro_biker at left2
    show goro sigh1 at left2
    voice audio.goro_v_sigh2a
    g "*sigh* You already forgot about all the appointments you need to attend to. "
    g "The next term is only a week away. Can I really leave the camp to you like this?"

    show yoshi2 worry2 at right2
    voice audio.yoshi_v_ah3
    yo "A-Ah! Sorry about that…!"
    yo "I-I was just thinking that maybe when things settle down a bit during the summer, we can find time!"

    hide goro_biker
    hide goro sigh1
    show goro2_biker at left2
    show goro2 shy1 at left2
    g "..."

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    show goro2 shy2 at left2
    voice audio.goro_v_yoshi2a
    g "You know that’s not going to happen, Yoshinori."

    hide yoshi2_autumn
    hide yoshi2 worry2
    show yoshi_autumn at right2
    show yoshi worry3 at right2
    voice audio.yoshi_v_well1
    yo "Well, maybe if you visit us here at least once a month?"

    show goro2 disappoint2 at left2
    voice audio.goro_v_no1a1
    g "No. What I mean is… I don’t think this will work for us…"

    hide yoshi_autumn
    hide yoshi worry3
    show yoshi2_autumn at right2
    show yoshi2 panic2 at right2
    voice audio.yoshi_v_huh3a
    yo "Huh…? Wh-What are you saying, Goro...?"

    show goro2 annoy3 at left2
    voice audio.goro_v_scold2a1
    g "We had the chance the entire spring… last year… and all the time before that…"
    g "And it’s given me more than enough time to think about us…"

    show goro2 disappoint3 at left2
    voice audio.goro_v_conj10a1
    g "Ever since we started dating, I started having these plans, and dreams for our future…"

    play music buddy_oath_goro_sad loop
    show goro2 sad3 at left2
    voice audio.goro_v_but2a
    g "But I realized it was a mistake, all along…"

    show yoshi2 panic4 at right2
    voice audio.yoshi_v_what3
    yo "Wh-What…?"

    show goro2 sigh1 at left2
    voice audio.goro_v_sigh2a
    g "Let’s admit it… Being partners was never meant for us…"

    show yoshi2 panic3 at right2
    voice audio.yoshi_v_wait3a
    yo "W-Wait, you can’t be serious… "

    show goro2 disappoint5 at left2
    voice audio.goro_v_conj10b1
    g "We’ve had all these experiences together... all these chances... and we still ended up in the same place as before…"
    g "I want us to be more… And that’s not possible."

    show yoshi2 worry4 at right2
    voice audio.yoshi_v_goro10
    yo "G-Goro..! I-I’m so sorry! Wh-What have I done wrong…?! And what can I do to make this right?! "

    show goro2 angry2 at left2
    voice audio.goro_v_no3a2
    g "That’s not the case, Yoshinori… I’ve made up my mind already. "
    g "I’m making this choice for myself… I need to prove that I can find happiness on my own without attaching it to the camp… attaching it to you…"

    show goro2 disappoint3 at left2
    voice audio.goro_v_annoyed1a1
    g "I’ve spent my whole life giving up everything until there was nothing left to give."
    g "It’s time for me to find myself again."

    hide goro2_biker
    hide goro2 disappoint3
    show goro_biker at left2
    show goro worry2 at left2
    voice audio.goro_v_request5a1
    g "So, please. The last thing I’ll ask of you is to understand and set me free…"

    show yoshi2 sad1 at right2
    yo "..."

    show yoshi2 sigh1 at right2
    voice audio.yoshi_v_response1c
    yo "I understand, Goro…"

    show goro_biker at center
    show goro worry1 at center
    with move

    g "*hugs Yoshinori*"

    show yoshi2 upset1 at right2
    yo "..."

    show goro_biker at left2
    show goro sad2 at left2
    with move

    voice audio.goro_v_sigh2a
    g "I’ll keep in touch… And I’ll make time if the camp needs my help."
    g "But I know all of you will do your best."

    show yoshi2 upset6 at right2
    voice audio.yoshi_v_yessir4
    yo "Y-Yes, sir…"

    play sound sfx_harleystart
    show goro sad3 at left2
    voice audio.goro_v_bye1b1
    g "Goodbye, Yoshinori."

    show yoshi2 sad4 at right2
    voice audio.yoshi_v_bye4b
    yo "Goodbye, Goro…"

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    play sound sfx_harleydeparthard
    scene cg black with fade
    yo "{i}(I stood at the arches of Camp Buddy as I watched Goro drive away…){/i}"
    yo "{i}(Left to wonder about the choices I’ve made… the only right thing I knew was to respect his decision and let him go…){/i}"
    yo "{i}(Even though I thought we had gained so much throughout the seasons… In the end what I lost was more important.){/i}"
    yo "{i}(My only hope now is for Goro to be truly happy out there… and that maybe one day he’ll come back for good…){/i}"

    scene cg black with fade
    hide screen location
    hide screen timeline
    hide screen quick_menu
    $ quick_menu = False
    $ renpy.pause (2.0, hard=True)

    scene bg_gameover with dissolve
    $ renpy.pause (5.0, hard=True)

    $persistent.routes_completed.append("goro")
    $renpy.save_persistent()

    #gameover
