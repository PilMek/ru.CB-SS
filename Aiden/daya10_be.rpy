image entrance_transition:
    "images/bgs/bg-w-entrance-day.png"
    pause 1.0
    "images/bgs/bg-p-entrance-day.png" with Dissolve(4.0)

label day10_aiden_be:
    $ day = "84"
    $ time = timeline_timeday
    $ location = location_office
    show screen location
    show screen timeline
    show screen quick_menu
    $ quick_menu = True
    $ working = True

    scene bg_office_autumn_day with fade
    play music brand_new_day loop

    show aiden_autumn at left2
    show aiden norm3 at left2
    show yoshi_autumn at right2
    show yoshi norm3 at right2
    voice audio.william_v_amazed3
    w "That’s splendid news! I was hoping that you’d accept this opportunity!"

    show aiden talk1 at left2
    voice audio.aiden_v_thanks1c1
    a "Thank you, Mr. Clermont for seeing something in me and giving me the chance to use my talents in the best possible way I can."

    voice audio.william_v_agree1b
    w "Of course! I will send the details of how you have to prepare, along with the school information, dates, and curriculum as soon as possible!"

    show aiden talk2 at left2
    voice audio.aiden_v_yessir1b1
    a "Yes, sir. I’ll study it very carefully."

    hide aiden_autumn
    hide aiden talk2
    show aiden2_autumn at left2
    show aiden2 worry2 at left2
    voice audio.aiden_v_but1b1
    a "A-Although, if I could make a request... Can you at least let me finish my role in the expansion project before I pursue this opportunity?"

    voice audio.william_v_disagree1b
    w "Why of course! We don’t need to be in such a hurry! You wouldn’t be required to move until the end of spring!"
    w "By then, the project is scheduled to be complete! So, please enjoy your time at Camp Buddy for a few more months!"

    hide aiden2_autumn
    hide aiden2 worry2
    show aiden_autumn at left2
    show aiden comp2 at left2
    voice audio.aiden_v_william7a
    a "Thank you, Mr. Clermont!"

    voice audio.william_v_bye2b
    w "Well then, I’m looking forward to seeing you out there soon, Mr. Flynn! Have a lovely day!"

    play sound sfx_phonebutton

    hide aiden_autumn
    hide aiden comp2
    show aiden2_autumn at left2
    show aiden2 sigh1 at left2
    voice audio.aiden_v_sigh1a
    a "Whew… Well, that happened."

    show yoshi comp2 at right2
    voice audio.yyoshi_v_praise1
    yo "You did great, Aiden! You were very professional, and everything you said came from the heart."
    yo "You didn’t need my help talking to Mr. Clermont after all!"

    show aiden2 worry2 at left2
    voice audio.aiden_v_yeah1d1
    a "Yeah… Usually talking about serious stuff like that over the phone gives me a little bit of anxiety."
    a "Especially when it’s about something I tried reaching for in the past."

    show aiden2 explain2 at left2
    voice audio.aiden_v_sigh1a
    a "After my dad passed, I was so determined to pursue cooking knowing it was the one thing I was really good at."
    a "I went back to working all sorts of jobs to make money and save for a degree."

    show aiden2 comp2 at left2
    voice audio.aiden_v_but1b1
    a "But then, in the middle of all that, I finally heard from you – asking me to come back to Camp Buddy."

    show yoshi worry2 at right2
    voice audio.yoshi_v_well1
    yo "Well… It was only when I got the job here that I found out that you lost your dad… "
    yo "So as soon as I knew the camp needed help, you were the first person to come to mind..."

    show yoshi comp3 at right2
    voice audio.yoshi_v_gratitude2
    yo "I’m really glad you decided to accept."

    hide aiden2_autumn
    hide aiden2 comp2
    show aiden_autumn at left2
    show aiden comp3 at left2
    voice audio.aiden_v_yoshi15a
    a "I was afraid of what would happen if I showed up empty-handed, but you never looked down on me or judged me."
    a "You treated me the same way as when we first met."

    hide aiden_autumn
    hide aiden comp3
    show aiden2_autumn at left2
    show aiden2 sigh1 at left2
    voice audio.aiden_v_sigh1a
    a "Even still, I tried to save face by convincing everyone that I was only coming back to make enough money for college."

    hide aiden2_autumn
    hide aiden2 sigh1
    show aiden_autumn at left2
    show aiden talk1 at left2
    voice audio.aiden_v_so1
    a "Now I get to follow that dream for real and make something relevant out of myself."
    a "I’ll be able to really contribute and truly belong at Camp Buddy one day!"

    show yoshi comp5 at right2
    voice audio.yoshi_v_aiden15b
    yo "Well, you’re already doing that, Aiden! But this time around, you'll get to help with something much bigger out there!"
    yo "That’s why I’m really glad you made this decision, and see just how much potential you have, Aiden!"

    show yoshi worry2 at right2
    voice audio.yoshi_v_sigh3a
    yo "I was worried you’d miss out on this amazing chance."

    show aiden comp5 at left2
    voice audio.aiden_v_thanks1c1
    a "Thanks a lot for changing my mind, Yoshi. I won’t let you guys down!"

    show aiden_autumn at left
    show aiden comp5 at left
    show yoshi_autumn at center
    show yoshi worry2 at center
    with move

    show goro_winter at right
    show goro talk3 at right
    with dissolve
    voice audio.goro_v_ah1b
    g "Ah. There you are, you two!"

    show yoshi talk1 at center
    voice audio.yoshi_v_goodam1
    yo "Good morning, Sir Goro! Sorry for the delay. Aiden just had to give Mr. Clermont a call."

    show goro confused3 at right
    voice audio.goro_v_response3a1
    g "It’s fine. How did it go?"

    show aiden explain1 at left
    voice audio.aiden_v_well1c1
    a "Well, I ended up accepting the offer. I think it was the right path for me after all, Gramps."

    show goro explain2 at right
    voice audio.goro_v_think1a1
    g "As long as you’re happy, whatever your decision, it’ll always be the right choice."

    show aiden comp3 at left
    voice audio.aiden_v_laugh1b1
    a "Hehe, thanks, Gramps. "

    show goro talk1 at right
    voice audio.goro_v_conj4a
    g "Either way, I’m glad to see you both finally resolving things with each other. We’ll need you two more than ever from here on out."

    show aiden bold2 at left
    voice audio.aiden_v_confident1a
    a "Roger that, Gramps. You can count on us!"
    a "Now let’s get on with things before this cheese-train gets out of control."

    hide yoshi_autumn
    hide yoshi talk1
    show yoshi2_autumn at center
    show yoshi2 sigh1 at center
    voice audio.yoshi_v_sigh3a
    yo "*sigh* Aiden."

    hide goro_winter
    hide goro talk1
    show goro2_winter at right
    show goro2 explain2 at right
    voice audio.goro_v_ehem1a
    g "*ehem* I actually came here to fetch you two for our agenda today."
    g "The workers have just arrived and we’re gathering to discuss resuming our expansion project."

    show aiden talk4 at left
    voice audio.aiden_v_agree2e1
    a "Oh right… that’s today!"

    hide yoshi2_autumn
    hide yoshi2 sigh1
    show yoshi_autumn at center
    show yoshi talk2 at center
    voice audio.yoshi_v_laugh1
    yo "Looks like we’re back to the grind again, huh?"

    hide goro2_winter
    hide goro2 explain2
    show goro_winter at right
    show goro talk3 at right
    voice audio.goro_v_agree1a1
    g "Yes. Hopefully we’re through all the seasonal hiccups, and we have until spring to finish everything."

    show aiden bold2 at left
    voice audio.aiden_v_comp2a
    a "Now that I’m not going anywhere, I’m sure we can pull it off, hahaha!"

    hide goro_winter
    hide goro talk3
    show goro2_winter at right
    show goro2 play3 at right
    voice audio.goro_v_heh1a
    g "Heh. Said like a true scoutmaster."
    g "Shall we go meet the workers then? We’ll have a short briefing on each department’s status."

    show yoshi happy1 at center
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
    with dissolve
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

    $ day = "89"
    show cg8 4a with Dissolve(0.25)
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
    $ quick_menu = False
    with fade

    $ location = location_entrance
    show screen location
    show screen timeline
    show screen quick_menu
    $ quick_menu = True
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
    show aiden2_autumn at p8_7
    show aiden2 sad4  at p8_7
    show yoshi_autumn at p8_6
    show yoshi confused2 at p8_6
    show goro_autumn at p8_8
    show goro norm4 at p8_8
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
    l "Regardless, this was quite the experience."

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
    voice audio.yuri_v_jin8c
    yu "Nooooo! Jin… my only fudanshi friend… Don’t leave me!!"

    show jin comp6 at p8_3
    voice audio.jin_v_comp1a2
    j "It’s okay, Yuri, we can always share online! I gave you my Dicksword ID."

    show lloyd happy1 at p8_1
    voice audio.lloyd_v_laugh1a1
    l "We could always hang out outside of Camp Buddy too, right?! A little get together?!"

    show aiden2 sigh1 at p8_7
    voice audio.aiden_v_sigh1a
    a "*sigh* I’d love to, but the culinary school I’m headed to is two flights away."
    a "I’m actually scheduled for my entrance exam later today too."

    show lloyd amazed3 at p8_1
    voice audio.lloyd_v_amazed3b1
    l "Wahh, congrats again on your exciting career, Aiden! "

    show darius comp2 at p8_2
    voice audio.darius_v_comp3a
    d "I’m sure you’ll ace it."

    show jin comp2 at p8_3
    voice audio.jin_v_comp2a1
    j "Y-You can do it, Aiden!"

    hide aiden2_autumn
    hide aiden2 sigh1
    show aiden_autumn at p8_7
    show aiden comp2 at p8_7
    voice audio.aiden_v_guys6a
    a "Thanks, guys!"

    show yuri pain3 at p8_5
    voice audio.yuri_v_aww1a
    yu "Huhuhu!! First Lloyd, Darius, and Jin are leaving, and now Aiden too! I can’t take all of this! I’m gonna cry!"

    show emilia angry6 at p8_4
    voice audio.emilia_v_wait1a1
    e "Calm down, Yuri… It’s not like they’re dying."

    show goro talk3 at p8_8
    voice audio.goro_v_alright2b2
    g "I’m sure everyone here will do their best to stay in touch."

    show lloyd pout5 at p8_1
    voice audio.lloyd_v_annoyed1a3
    l "Hmph! Emilia is lucky she gets to stay! "

    show emilia explain3 at p8_4
    voice audio.emilia_v_well1
    e "Well, I have nowhere else to be anyway… and I’ll probably be taking over Aiden’s job."
    e "I’ve grown quite fond of this place, after all.  And I’m even adjusting to a simpler life!"

    show emilia bold2 at p8_4
    voice audio.emilia_v_so2a
    e "So, call me Chef Emilia from now on~!"

    show aiden comp3 at p8_7
    voice audio.aiden_v_alright3b2
    a "Just don’t forget all the recipes I taught you, alright?"

    show yuri rage1 at p8_5
    voice audio.yuri_v_no1c1
    yu "NOOOOO! She’s a terrible cook, Aiden! She literally managed to burn an egg to a crisp!"

    show emilia rage4 at p8_4
    voice audio.emilia_v_angry1a
    e "HEY! That was just an experiment!"

    show darius worry2 at p8_2
    voice audio.darius_v_agree2c
    d "We’re all going to miss Aiden’s cooking."

    show lloyd laugh1 at p8_1
    voice audio.lloyd_v_shock1b1
    l "Ooh, ooh! We better get reserved VIP seats at your restaurant someday, alright Aiden?!"

    show aiden comp6 at p8_7
    voice audio.aiden_v_agree7b
    a "O-Of course!"

    show goro comp2 at p8_8
    voice audio.goro_v_comp2b1
    g "You all don’t have to worry about us here at Camp Buddy too. You have helped us more than enough, especially you, Aiden."

    hide aiden_autumn
    hide aiden comp6
    show aiden2_autumn at p8_7
    show aiden2 worry2 at p8_7
    hide yoshi_autumn
    hide yoshi confused2
    show yoshi_autumn at p8_6
    show yoshi confused2 at p8_6
    voice audio.aiden_v_aww1a
    a "Aww, Gramps…"

    play sound sfx_busdoor
    show lloyd shock2 at p8_1
    voice audio.lloyd_v_shock4a1
    l "Oop! There’s our shuttle! I think that’s our cue to go."

    show yoshi happy2 at p8_6
    voice audio.yoshi_v_bye1b
    yo "Goodbye, guys! It’s been a pleasure working with everyone!"

    show goro comp5 at p8_8
    voice audio.goro_v_bye1b1
    g "Camp Buddy will always be here for you all."

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
    $ renpy.pause (1.0, hard=True)

    $ renpy.music.stop(channel='sound', fadeout = 2.0)
    show yuri panic3 at p8_5
    voice audio.yuri_v_shock2a
    yu "Oh no! I forgot to take one last group picture! "
    yu "C-Come back!!!"

    hide yuri_autumn
    hide yuri panic3
    with moveoutleft

    show emilia panic3 at p8_4
    voice audio.emilia_v_yuri1
    e "Y-Yuri?! You’re not gonna catch that bus on foot! Are you stupid?!"

    hide emilia_autumn
    hide emilia panic3
    with moveoutleft

    show goro explain2 at p8_8
    voice audio.goro_v_alright1a1
    g "I suppose I should go and report to Mr. Clermont that everyone departed safely."
    g "You’re going with him, right, Aiden?"

    hide goro_autumn
    hide goro explain2
    with dissolve

    show yoshi_autumn at left2
    show yoshi happy2 at left2
    show aiden2_autumn at right2
    show aiden2 sigh1 at right2
    with move
    voice audio.aiden_v_yeah1d2
    a "Yeah… I guess that’s my cue to pack up too."

    show yoshi talk3 at left2
    voice audio.yoshi_v_oh1
    yo "Oh, I’ll help you out, Aiden!"

    hide aiden2_autumn
    hide aiden2 worry2
    show aiden_autumn at right2
    show aiden sad4 at right2
    voice audio.aiden_v_thanks1c1
    a "Thanks, Yoshi…"

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

    $ location = location_cabin
    show screen location
    show screen timeline
    show screen quick_menu
    $ quick_menu = True
    scene bg_quarters_autumn_day with fade
    play music go_with_the_flow_slow loop

    show yoshi_autumn at left2
    show yoshi norm3 at left2
    show aiden2_autumn at right2
    show aiden2 sad4 at right2
    with dissolve
    a "..."

    show yoshi comp2 at left2
    voice audio.yoshi_v_uh1a
    yo "Are you excited for the first day of your culinary career?"

    hide aiden2_autumn
    hide aiden2 sad4
    show aiden_autumn at right2
    show aiden upset6 at right2
    voice audio.aiden_v_well1c1
    a "Well… I am… but I’m also sad that I’ll be leaving… you know, same old, same old."

    show yoshi comp3 at left2
    voice audio.yoshi_v_comp3
    yo "You’ll be fine, Aiden. We have our phones to stay in touch!"

    hide aiden_autumn
    hide aiden_ upset6
    show aiden2_autumn at right2
    show aiden2 upset3 at right2
    voice audio.aiden_v_yeah1d2
    a "Yeah… But with the curriculum I have, I’m gonna be really busy."
    a "I’m really worried about being away from you… especially since we just started dating…"

    show yoshi explain4 at left2
    voice audio.yoshi_v_comp6
    yo "I promise we’ll be fine, Aiden! Long distance is hard, but we can make it work."

    show aiden2 worry2 at right2
    voice audio.aiden_v_unsure1a
    a "I guess you’re right… We’ll just have to find a way!"

    hide yoshi_autumn
    hide yoshi explain4
    show yoshi2_autumn at left2
    show yoshi2 worry2 at left2
    voice audio.yoshi_v_aww1
    yo "I will miss you though, Aiden… "

    show aiden2 sigh1 at right2
    voice audio.aiden_v_sigh1a
    a "Me too. "

    $ renpy.pause (1.0, hard=True)
    show aiden2 worry2 at right2
    voice audio.aiden_v_anyway2b
    a "I guess that’s all of my stuff. I’m ready to leave now…"

    hide yoshi2_autumn
    hide yoshi2 worry2
    show yoshi_autumn at left2
    show yoshi talk1 at left2
    voice audio.yoshi_v_alright1
    yo "You got your plane ticket ready, right? Your passport? IDs? "

    show aiden sad4 at right2
    voice audio.aiden_v_yeah1d1
    a "Yeah… You packed them for me yesterday. "

    show yoshi happy1 at left2
    voice audio.yoshi_v_okay2
    yo "Okay, great!"

    hide aiden_autumn
    hide aiden sad4
    show aiden2_autumn at right2
    show aiden2 sad5 at right2
    a "..."

    show aiden2 sad4 at right2
    voice audio.aiden_v_yoshi4a
    a "Well… Goodbye, Yoshi."

    show yoshi comp2 at left2
    voice audio.yoshi_v_aiden4
    yo "Good luck, Aiden… I’ll be cheering for you."
    yo "I love you!"

    show yoshi_autumn at p6_4
    show yoshi smile1 at p6_4
    with move
    yo "*kisses Aiden’s cheek*"

    show aiden2 upset5 at right2
    voice audio.aiden_v_sigh1a
    a "Love you too."

    show yoshi_autumn at left2
    show yoshi comp3 at left2
    with move
    voice audio.yoshi_v_rush5
    yo "I’ll call everyone to send you off now, alright?"

    hide aiden2_autumn
    hide aiden2 upset5
    show aiden_autumn at right2
    show aiden sigh1 at right2
    voice audio.aiden_v_okay2b
    a "Okay…"

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black with fade

    play sound sfx_carstart
    yo "{i}Aiden was really upset to leave Camp Buddy… And I have to admit, it was hard to watch him go…{/i}"
    yo "{i}Even though I’d rather him be here with me, I’m sure that this was the right call so Aiden could follow his dreams.{/i}"
    yo "{i}All of this will be worth it in the end… {/i}"

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
    jump day10_aiden_be_aftercredits

label day10_aiden_be_aftercredits:
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

    mys "A few months later…"
    scene bg_site9_spring_day with fade
    play music buddy_oath_musicbox loop

    play sound sfx_phonering
    show yoshi_autumn at center
    show yoshi talk3 at center
    voice audio.yoshi_v_oh1
    yo "Oh Aiden! Why did you call? How have you been? "

    voice audio.aiden_v_well1c1
    a "W-Well… busy as usual… The instructors here are really strict… and the exams are really hard…"
    a "Some of my grades are actually starting to go down…"

    show yoshi talk3 at center
    voice audio.yoshi_v_oh1
    yo "Oh no, Aiden… It’s okay though! You can do it! I believe in you."

    voice audio.aiden_v_yeah1d2
    a "Yeah…"
    a "How about you? The next term should’ve started by now right?"

    show yoshi happy2 at center
    voice audio.yoshi_v_yes8
    yo "Oh, yes! A lot of the scouts have come back, and well… they really miss you…"
    yo "There’s also a lot of new scouts and scoutmasters as well. It’s been really busy around here…"

    show yoshi sigh1 at center
    voice audio.yoshi_v_sigh3a
    yo "I think even Sir Goro and Yuri are getting overwhelmed, so I stepped in a little bit on the managerial side."

    voice audio.aiden_v_response2b2
    a "I see… It sounds fun there."

    hide yoshi_autumn
    hide yoshi sigh1
    show yoshi2_autumn at center
    show yoshi2 comp3 at center
    voice audio.yoshi_v_yeah4
    yo "Yeah… Hell, but still fun…"

    voice audio.aiden_v_think2a
    a "Hey, uh… Yoshi… Are we gonna meet up soon? We haven’t seen each other in person for months now…"

    show yoshi2 worry5 at center
    voice audio.yoshi_v_ah2
    yo "A-Ahh… Well… Like I mentioned, it’s been a little busy over here… I’m not sure if I can afford to take time off… You know how the summer is."
    yo "And now with twice as many scouts, it’s really overwhelming."

    show yoshi2 sad4 at center
    voice audio.yoshi_v_sorry2b
    yo "I’m sorry…"

    voice audio.aiden_v_alright3a1
    a "It’s alright… I understand…"

    $ renpy.pause (2.0, hard=True)
    a "…"

    show yoshi2 worry3 at center
    voice audio.yoshi_v_aiden4
    yo "Aiden… Are you okay…?"

    voice audio.aiden_v_yoshi4a
    a "Yoshi…"
    a "I don’t think this will work for us… "

    show yoshi2 panic2 at center
    voice audio.yoshi_v_huh3a
    yo "Huh…? Wh-What are you saying, Aiden…?"

    voice audio.aiden_v_well1c1
    a "Well… I’m so overwhelmed with school… I haven’t made any friends here… and it’s so hard to be alone…"
    a "I’m just so lonely again… it’s… reminding me of back then when you left for school…"

    voice audio.aiden_v_i1a1
    a "I… really want you to be here, and to hear that you can’t come… it’s really disappointing…"

    show yoshi2 at center
    voice audio.yoshi_v_sorry4c1
    yo "I’m really sorry, Aiden… I promise I’ll make it up to you… maybe you just need time to—"

    voice audio.aiden_v_sigh1a
    a "It’s been months since we last saw each other, Yoshi. You always say you’ll make it up to me, but nothing’s changed."
    a "How long do I have to wait… again?"

    show yoshi2 sad6 at center
    voice audio.yoshi_v_aiden4
    yo "I’m really sorry, Aiden, I wish I had more time. It’s really just the distance that’s been making things hard…"

    voice audio.aiden_v_but1b1
    a "That’s the thing… you’re taking it for granted yet again… LDR doesn’t work for us obviously."
    a "I know this is sounding unfair to you, but… I’ve been lonely like this for far too long…"

    voice audio.aiden_v_unsure2a
    a "You know how much being apart hurts me… I lost my dad, I lost all my friends and now I can’t even see you…"
    a "This is too much for me, Yoshi…"

    show yoshi2 upset1 at center
    yo "…"

    voice audio.aiden_v_sigh1a
    a "Now here I am, alone in my room, wondering… if all of this is worth it…"

    voice audio.aiden_v_i1a1
    a "I… want to make a choice for myself once and for all. I’m tired of going with the flow…"
    a "Ever since we’ve been in a relationship, I started having these expectations, and I can’t help but wonder if that was a mistake too…"

    show yoshi2 panic2 at center
    voice audio.yoshi_v_what3
    yo "Wh-What…?"

    voice audio.aiden_v_sorry1c1
    a "I’ve thought about it for a long time, Yoshi… I think we should just be friends… at least for now…"

    show yoshi2 panic3 at center
    voice audio.yoshi_v_aiden10
    yo "A-Aiden…! I-I’m sorry, please let me make this right!  I’ll drop everything I’m doing right now! Let me fight for us!"

    voice audio.aiden_v_yoshi4a
    a "N-No, Yoshi, I’m not asking you… I’ve made up my mind already…"
    a "I think this was meant to happen all along. And it’s actually for the best, in a way we didn’t realize before."

    voice audio.aiden_v_sigh1a
    a "I’ve always anchored myself to you, and it’s about time I find my direction."
    a "Pursuing this opportunity will help me find my own meaning in life."
    a "I’m not turning away from you, especially not to the promise we made back then…"
    a "I will come back to Camp Buddy… Once I become a professional chef…"

    voice audio.aiden_v_yoshi4b
    a "So please, understand why I’m doing this, Yoshi…"

    show yoshi2 sad1 at center
    yo "…"

    show yoshi2 sad5 at center
    voice audio.yoshi_v_response1c
    yo "I understand, Aiden…"

    voice audio.aiden_v_thanks2a
    a "Thank you, Yoshi."

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black with fade

    yo "{i}After that call, Aiden set boundaries for us, and I couldn’t contact him any more…{/i}"
    yo "{i}In my heart, I realized how much I failed him by pushing him to make a choice I thought was for the best…{/i}"
    yo "{i}That’s why this time around, I had to respect his decision and let him go…{/i}"

    scene cg black
    hide screen location
    hide screen timeline
    hide screen quick_menu
    $ quick_menu = False
    with fade

    $ location = location_entrance
    show screen location
    show screen timeline
    show screen quick_menu
    $ quick_menu = True
    scene bg_entrance_past_day with fade
    play bgsound sfxloop_birds loop

    yo "{i}A year later, Aiden and I had remained out of touch with each other. {/i}"
    yo "{i}Until I received the news that he had finally become a professional chef.{/i}"
    yo "{i}Each day, I would wait at the arches of Camp Buddy, holding on to his promise, waiting for him to come home to me again…{/i}"

    scene cg black with fade
    hide screen location
    hide screen timeline
    hide screen quick_menu
    $ quick_menu = False
    $ renpy.pause (2.0, hard=True)

    scene bg_gameover with dissolve
    $ renpy.pause (5.0, hard=True)

    $persistent.routes_completed.append("aiden")
    $renpy.save_persistent()

    #gameover
    $ MainMenu(confirm=False)()
