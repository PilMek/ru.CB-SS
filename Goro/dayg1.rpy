label day1_goro:
    $ day = "07"
    $ time = timeline_timeday
    $ location = location_cabin
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    $ working = True

    scene bg_quarters_autumn_day with fade
    play music brand_new_day loop
    play bgsound sfxloop_birds loop

    show yoshi2_sleep at center
    show yoshi2 sleepy3 at center
    voice audio.yoshi_v_groan1a
    yo "Nnn… *stretches*"

    show yoshi2_sleep at p6_1
    show yoshi2 sleepy3 at p6_1
    with move

    show goro_sleep at p6_2
    show goro talk1 at p6_2
    show darius_sleep at p6_4
    show darius norm1 at p6_4
    show lloyd_sleep at p6_3
    show lloyd norm1 at p6_3
    show aiden_sleep at p6_5
    show aiden norm1 at p6_5
    show jin_sleep at p6_6
    show jin_glasses at p6_6
    show jin norm1 at p6_6
    with dissolve

    voice audio.goro_v_ah1a
    g "Ah, you’re up, Yoshinori."

    show aiden happy2 at p6_5
    voice audio.aiden_v_yoshi1b
    a "Good morning, Yoshi!"

    hide yoshi2_sleep
    hide yoshi2 sleepy3
    show yoshi_sleep at p6_1
    show yoshi talk1 at p6_1
    voice audio.yoshi_v_goodam1
    yo "Good morning too, guys! "

    show yoshi happy1 at p6_1
    voice audio.yoshi_v_laugh1
    yo "Haha, looks like everyone really does get up earlier than me. "

    show goro explain2 at p6_2
    voice audio.goro_v_well1a
    g "Well, we figured we’d give our new inspector a better impression today."

    show aiden happy4 at p6_5
    voice audio.aiden_v_orderup1a
    a "That, and I made everyone some hot cocoa and coffee~!"

    show darius relief1 at p6_4
    voice audio.darius_v_think1a2
    d "*sip* Mmm… "

    show aiden talk1 at p6_5
    voice audio.aiden_v_jin3a
    a "Jin here was up all night!"

    show lloyd annoy5 at p6_3
    voice audio.lloyd_v_annoyed1a3
    l "As usual."

    show jin worry4 at p6_6
    voice audio.jin_v_sigh2a
    j "Emilia sent me an angry email last night with tons of work, so I kinda wanted to get that over with."

    show yoshi talk3 at p6_1
    voice audio.yoshi_v_oh1
    yo "Oh, I hope it wasn’t too difficult."

    show jin talk1 at p6_6
    voice audio.jin_v_denial2b2
    j "Not really. It’s database work, so it’s more on the tedious side."

    hide goro_sleep
    hide goro explain2
    show goro2_sleep at p6_2
    show goro2 confused3 at p6_2
    voice audio.goro_v_think1a1
    g "Sounds complicated. Shouldn’t you get some rest? "

    show jin happy2 at p6_6
    voice audio.jin_v_conj1d1
    j "I’m actually already done for the day, sir! Now I can hang out with you guys before I go to bed!"

    show aiden relief2 at p6_5
    voice audio.aiden_v_yeah1h1
    a "Yeaaahh! Come relax with us and have some breakfast. It’s still hella early anyways!"

    show yoshi happy2 at p6_1
    voice audio.yoshi_v_actually3a
    yo "It looks like you’re doing something fun, though! Are you guys playing cards?"

    show lloyd happy2 at p6_3
    voice audio.lloyd_v_shock1a1
    l "Oh, these aren’t playing cards, they’re tarot cards! I’m trying to foresee what Sir Goro has in store for his future!"

    show yoshi confused2 at p6_1
    voice audio.yoshi_v_really6
    yo "You... You can tell the future?"

    show lloyd confused2 at p6_3
    voice audio.lloyd_v_denial3a1
    l "Not just that! You see, tarot cards are used to gain insight into the past, present or future by formulating a question, then drawing and interpreting the cards~!"
    l "It’s up to the individual as to what they do with the knowledge seen on their path."

    show yoshi think2 at p6_1
    voice audio.yoshi_v_oh3
    yo "Oh… that’s interesting. So that’s what you were talking about last night, too."

    show lloyd grin1 at p6_3
    voice audio.lloyd_v_agree1a1
    l "Yup! "

    show aiden awkward2 at p6_5
    voice audio.aiden_v_actually2a
    a "He did mine a while ago and it was pretty spot-on about my past. I was really surprised and kinda spooked at the same time!"
    a "Slowly but surely, I’m starting to think Lloyd here is some kind of a leprechaun or something."

    show lloyd angry2 at p6_3
    voice audio.lloyd_v_greet2c1
    l "L-Leprechaun?! You could’ve at least called me a wizard!"

    show goro2 think3 at p6_2
    voice audio.goro_v_actually1a
    g "I’ve read a few books about tarot in the past as well, but it seems to have surged in popularity recently."

    show lloyd excited1 at p6_3
    voice audio.lloyd_v_agree2b1
    l "Yeah! People all over the internet love to get into discussions about the meanings!"

    show yoshi talk1 at p6_1
    voice audio.yoshi_v_lloyd5b
    yo "I’m curious. What did Sir Goro’s reading say, Lloyd?"

    show lloyd explain6 at p6_3
    voice audio.lloyd_v_conj1a3
    l "Well, after I drew the ‘Hanged Man’, ‘Emperor’, and ‘Death’, it sounded like Sir Goro would be undergoing some transformation!"

    hide aiden_sleep
    hide aiden awkward2
    show aiden2_sleep at p6_5
    show aiden2 panic3 at p6_5
    hide darius_sleep
    hide darius relief1
    show darius_sleep at p6_4
    show darius norm1 at p6_4
    hide lloyd_sleep
    hide lloyd explain6
    show lloyd_sleep at p6_3
    show lloyd explain6 at p6_3
    voice audio.aiden_v_what4a
    a "Wh-Wha? ‘Death’?! Does that mean Gramps is gonna die of something other than old age?!"

    hide goro2_sleep
    hide goro2 think3
    show goro_sleep at p6_2
    show goro irked3 at p6_2
    hide lloyd_sleep
    hide lloyd explain6
    show lloyd_sleep at p6_3
    show lloyd explain6 at p6_3
    voice audio.goro_v_aiden5a
    g "Cut out the ageism, Aiden."

    show lloyd shock3 at p6_3
    voice audio.lloyd_v_disagree1d2
    l "N-No! Don’t be intimidated, these cards can mean positive things like readjustment, accomplishment, and leadership! "

    show lloyd explain2 at p6_3
    voice audio.lloyd_v_stars1a3
    l "Although the hanged man usually depicts sacrifice, it can also mean wisdom, or making the right choices."
    l "You definitely have some interesting developments in store for you, Sir Goro! And maybe some tough decisions too."

    show lloyd explain3 at p6_3
    voice audio.lloyd_v_encourage1b
    l "Be firm with your volitions, and you’ll achieve your ideal happiness, or else it could lead to your ultimate regret!"

    hide yoshi_sleep
    hide yoshi talk1
    show yoshi2_sleep at p6_1
    show yoshi2 worry2 at p6_1
    voice audio.yoshi_v_oops1
    yo "E-Even though it sounds kind of vague, it still sounds grim… Is Sir Goro going to be alright?"

    hide goro_sleep
    hide goro irked3
    show goro2_sleep at p6_2
    show goro2 bored2 at p6_2
    voice audio.goro_v_well1a
    g "Well, I’ll just take it all with a grain of salt. "

    show darius happy1 at p6_4
    voice audio.darius_v_agree3
    d "That’s a good mindset for the whole thing."
    d "Lloyd kept foretelling the ‘Death’ one for me, too. But I’m still alive."

    show lloyd tease2 at p6_3
    voice audio.lloyd_v_greet2a1
    l "Hey! You never know! Maybe not for long!"

    show yoshi2_sleep at p7_2
    show yoshi2 worry2 at p7_2
    show aiden2_sleep at p7_6
    show aiden2 panic3 at p7_6
    show lloyd_sleep at p7_4
    show lloyd angry2 at p7_4
    show darius_sleep at p7_5
    show darius happy1 at p7_5
    show goro2_sleep at p7_3
    show goro2 bored2 at p7_3
    show jin_sleep at p7_7
    show jin_glasses at p7_7
    show jin happy2 at p7_7
    with move

    play sound sfx_doorslam
    show yuri_autumn at p7_1
    show yuri annoy1 at p7_1
    with dissolve

    hide goro2_sleep
    hide goro2 bored2
    show goro_sleep at p7_3
    show goro talk3 at p7_3
    hide lloyd_sleep
    hide lloyd angry2
    show lloyd_sleep at p7_4
    show lloyd angry2 at p7_4
    voice audio.goro_v_oh1a
    g "Oh, Yuri, dear. What brings you he—"

    show yuri annoy2 at p7_1
    voice audio.yuri_v_guys1b
    yu "Emilia wants everyone in the campsite. Now."

    hide yoshi2_sleep
    hide yoshi2 worry2
    show yoshi_sleep at p7_2
    show yoshi confused3 at p7_2
    voice audio.yoshi_v_huh1
    yo "It’s not call time for thirty more minutes. What’s going on?"

    show yuri pout1 at p7_1
    voice audio.yuri_v_unsure1b1
    yu "I don’t know, but she’s already gathered all the workers. You guys should just go and see for yourselves."

    hide yuri_autumn
    hide yuri pout1
    with dissolve

    show yoshi_sleep at p6_1
    show yoshi confused3 at p6_1
    show aiden2_sleep at p6_5
    show aiden2 sigh4 at p6_5
    show lloyd_sleep at p6_3
    show lloyd angry2 at p6_3
    show darius_sleep at p6_4
    show darius happy1 at p6_4
    show goro_sleep at p6_2
    show goro talk3 at p6_2
    show jin_sleep at p6_6
    show jin_glasses at p6_6
    show jin happy2 at p6_6
    with move

    voice audio.aiden_v_sheesh1a
    a "Sheesh… Sounds like someone woke up on the wrong side of the bed today, huh…? "

    show goro sigh2 at p6_2
    voice audio.goro_v_sigh1a
    g "*sigh* I wonder what Emilia did to get on her nerves so early in the morning…"

    hide aiden2_sleep
    hide aiden2 sigh4
    show aiden_sleep at p6_5
    show aiden think2 at p6_5
    voice audio.aiden_v_think1a1
    a "I’d expected her to spazz over how a bunch of guys slept together!"

    show lloyd think5 at p6_3
    voice audio.lloyd_v_think1a1
    l "I guess knowing her, it is odd. "

    show goro talk2 at p6_2
    voice audio.goro_v_conj4b
    g "Either way, we shouldn’t keep the inspector waiting. Come on, let’s get ready and head over. "

    show yoshi talk2 at p6_1
    voice audio.yoshi_v_right2
    yo "Right."

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
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_campgrounds_autumn_day with fade
    play music heracleum_a loop
    play bgsound sfxloop_birds loop

    show darius_autumn at p8_2
    show darius norm4 at p8_2
    show jin_autumn at p8_1
    show jin_glasses at p8_1
    show jin worry1 at p8_1
    show aiden_autumn at p8_5
    show aiden worry1 at p8_5
    show yuri_autumn at p8_4
    show yuri annoy1 at p8_4
    show lloyd_autumn at p8_3
    show lloyd norm4 at p8_3
    show yoshi_autumn at p8_6
    show yoshi norm3 at p8_6
    show goro_autumn at p8_7
    show goro norm3 at p8_7
    show emilia_autumn at p8_8
    show emilia eyeroll4 at p8_8
    voice audio.emilia_v_tsk1a
    e "Tsk, tsk. Late, just like I expected… "

    show yuri angry2 at p8_4
    voice audio.yuri_v_hmph1a
    yu "This meeting isn’t even on the schedule. "

    show emilia irked2 at p8_8
    voice audio.emilia_v_question2a1
    e "Scheduled or not, the management staff being the last ones to arrive is very telling."
    e "Whatever happened to this camp’s oath about being prepared for anything? "

    show yuri pout2 at p8_4
    yu "..."

    show yoshi worry1 at p8_6
    yo "..."

    show emilia evil3 at p8_8
    voice audio.emilia_v_sarcastic2b2
    e "I thought so."

    show yuri irked1 at p8_4
    voice audio.yuri_v_well1a
    yu "Well, we’re here now. What do you want?"

    hide goro_autumn
    hide goro norm3
    show goro2_autumn at p8_7
    show goro2 annoy2 at p8_7
    voice audio.goro_v_rush5a1
    g "Ladies, please. Let’s just get to business."

    show emilia talk1 at p8_8
    voice audio.emilia_v_agree1b2
    e "Of course! I’ve gathered you all here today to make a very IMPORTANT announcement regarding our productivity for the next few months."

    play sound sfx_paper
    e "After my inspection and a meticulous review of everyone’s progress so far – I have worked overnight to create a detailed timetable for the next few months."
    e "This new schedule includes every deadline for each aspect of the project!  "

    show emilia talk1 at p8_8
    voice audio.emilia_v_conj2a
    e "Do note that these due dates are GENEROUSLY calculated, so I’m expecting nothing less than for everyone to STRICTLY follow the schedule."
    e "Here are the instructions for each department head. "

    show emilia_autumn at p8_1
    show emilia confused2 at p8_1
    show jin_autumn at p8_2
    show jin_glasses at p8_2
    show jin norm4 at p8_2
    show darius_autumn at p8_3
    show darius shock4 at p8_3
    show lloyd_autumn at p8_4
    show lloyd norm3 at p8_4
    show yuri_autumn at p8_5
    show yuri annoy1 at p8_5
    show aiden_autumn at p8_6
    show aiden worry1 at p8_6
    show yoshi_autumn at p8_7
    show yoshi worry1 at p8_7
    show goro2_autumn at p8_8
    show goro2 annoy2 at p8_8
    with move

    voice audio.emilia_v_so1
    e "These folders contain each department’s tasks, concerns, and a reminder of how everything should be done. Make sure to read and follow the details carefully."

    show jin_autumn at p8_1
    show jin_glasses at p8_1
    show jin norm4 at p8_1
    show darius_autumn at p8_2
    show darius disgust1 at p8_2
    show emilia_autumn at p8_3
    show emilia talk3 at p8_3
    show lloyd_autumn at p8_4
    show lloyd confused1 at p8_4
    with move

    voice audio.emilia_v_conj3a
    e "Everything you need to know is in there, so I don’t want to hear any questions later."

    show lloyd_autumn at p8_3
    show lloyd confused1 at p8_3
    show yuri_autumn at p8_4
    show yuri annoy1 at p8_4
    show emilia_autumn at p8_6
    show emilia annoy2 at p8_6
    show aiden_autumn at p8_5
    show aiden panic1 at p8_5
    with move

    voice audio.emilia_v_scoff1
    e "I also expect you all to take my evaluations from yesterday into account. "

    show emilia annoy3 at p8_6
    voice audio.emilia_v_william2
    e "Mr. Clermont has invested a LOT into this venture, so I’m sure we can all agree to show him nothing but the best."

    show emilia_autumn at p8_7
    show emilia evil4 at p8_7
    show yoshi_autumn at p8_6
    show yoshi worry1 at p8_6
    show goro2_autumn at p8_8
    show goro2 annoy1 at p8_8
    with move

    voice audio.emilia_v_bossy4
    e "No hard feelings, it’s just business after all."

    show emilia bold2 at p8_7
    voice audio.emilia_v_see2b
    e "I’m sure if we all approach this with a positive attitude, we’ll achieve our collective goal. That’s what we all want, isn’t it?"

    show jin_autumn at p8_1
    show jin_glasses at p8_1
    show jin norm4 at p8_1
    show darius_autumn at p8_2
    show darius disgust1 at p8_2
    show lloyd_autumn at p8_3
    show lloyd confused1 at p8_3
    show yuri_autumn at p8_4
    show yuri pout2 at p8_4
    show aiden_autumn at p8_5
    show aiden worry1 at p8_5
    show yoshi_autumn at p8_6
    show yoshi norm4 at p8_6
    show emilia_autumn at p8_8
    show emilia bold5 at p8_8
    show goro2_autumn at p8_7
    show goro2 annoy1 at p8_7

    with move

    voice audio.emilia_v_conj3a
    e "Now, for all the workers, grab a copy of the schedule here. "

    show goro2 confused2 at p8_7
    voice audio.goro_v_sorry1c1
    g "Forgive me for interrupting, Ms. Komarova, but… "
    g "I’ve noticed that this schedule is similar to our previous one but now includes extensive work over the winter season."

    show emilia talk1 at p8_8
    voice audio.emilia_v_agree2a1
    e "Yes, it has come to my attention that the original timetable included a large unproductive break of several weeks."
    e "I think it would be a waste of time to stop, especially since we’ll have already built up our momentum by then."

    hide goro2_autumn
    hide goro2 confused2
    show goro_autumn at p8_7
    show goro explain2 at p8_7
    hide emilia_autumn
    hide emilia talk1
    show emilia_autumn at p8_8
    show emilia talk1 at p8_8
    voice audio.goro_v_think1a1
    g "If I may, the weather can get quite harsh during the winter around these parts…"
    g "It could potentially be a hazardous environment for our workers, and there would be additional costs for the necessary equipment to work in such conditions."

    show goro talk1 at p8_7
    voice audio.goro_v_comp2a1
    g "But don’t worry – the originally scheduled downtime has already been considered and it shouldn’t affect our targeted completion date."
    g "In fact, I’ve already consulted with Mr. Clermont and he has given his approval for the break."

    show goro confused3 at p8_7
    voice audio.goro_v_unsure2a
    g "It was in the e-mail chain you requested access to. Did you get a chance to read it?"

    show emilia angry2 at p8_8
    voice audio.emilia_v_agree1c1
    e "O-Of course I have! It’s my job to know all the details of the project after all!"
    e "I only adjusted the schedule based on the issues that were made apparent to me yesterday during my survey!"

    show emilia angry3 at p8_8
    voice audio.emilia_v_sarcastic2a
    e "It’s common sense to ensure that there is plenty of time at the tail-end of any project to allow for any setbacks, which was my main reason for the extended work period!"
    e "But if you want to do it your way, then so be it."

    show emilia eyeroll6 at p8_8
    voice audio.emilia_v_hmph1a
    e "Just be prepared for stricter deadlines and less room for error!"

    show yuri annoy2 at p8_4
    voice audio.yuri_v_so1a
    yu "Is that all? We’re wasting that ‘precious work time’ right now with this meeting."

    show emilia rage4 at p8_8
    voice audio.emilia_v_question4b
    e "Excuse me?!"

    show yoshi talk2 at p8_6
    voice audio.yoshi_v_ehem1b
    yo "Maybe we can move forward and discuss the specifics of the schedule?"

    show emilia angry3 at p8_8
    voice audio.emilia_v_angry1a
    e "I would have if I wasn’t so rudely interrupted."
    e "Anyway, I am left with no choice but to cede to the camp president’s decision, and will include this extensive break in our schedule."

    show emilia angry2 at p8_8
    voice audio.emilia_v_response1a
    e "That means we need to get as much work done as possible before the season ends."

    show emilia angry5 at p8_8
    voice audio.emilia_v_rush2
    e "Everyone should follow the instructions I’ve handed out today, but I will follow up with a revised schedule with STRICTER deadlines, as Mr. Nomoru requested."
    e "I’ll be checking on all of your progress at the end of the day. You’re all dismissed!"

    hide lloyd_autumn
    hide lloyd confused1
    hide darius_autumn
    hide darius disgust1
    hide jin_autumn
    hide jin_glasses
    hide jin norm4
    hide yuri_autumn
    hide yuri annoy2
    hide aiden_autumn
    hide aiden worry1
    with moveoutleft

    show goro_autumn at p5_1
    show goro confused1 at p5_1
    show yoshi_autumn at p5_2
    show yoshi norm4 at p5_2
    with move

    show emilia annoy1 at p8_8
    voice audio.emilia_v_yoshi2
    e "Yoshinori."

    show yoshi_autumn at p5_4
    show yoshi confused2 at p5_4
    show emilia_autumn at p5_5
    show emilia annoy1 at p5_5
    with move

    voice audio.yoshi_v_yes1
    yo "Yes, Emilia?"

    show emilia talk1 at p5_5
    voice audio.emilia_v_rush1b1
    e "Come with me for a moment. I’d like to talk about something."

    show yoshi awkward4 at p5_4
    voice audio.yoshi_v_oh3
    yo "Oh… Alright, then."
    yo "I’ll just catch up, Sir Goro."

    hide emilia_autumn
    hide emilia talk1
    hide yoshi_autumn
    hide yoshi awkward4
    with dissolve

    hide goro_autumn
    hide goro confused1
    show goro2_autumn at p5_1
    show goro2 annoy1 at p5_1
    g "..."

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

    $ location = location_lake
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_lake_autumn_day
    with fade
    play bgsound sfxloop_birds loop

    show yoshi2_autumn at left2
    show yoshi2 awkward1 at left2
    show emilia_autumn at right2
    show emilia relief2 at right2
    voice audio.emilia_v_laugh3a
    e "Lovely weather we’re having today, aren’t we?"

    show yoshi2 shy4 at left2
    voice audio.yoshi_v_yeah4
    yo "Y-Yeah."

    show emilia comp3 at right2
    voice audio.emilia_v_sigh2b
    e "Can you believe we have found ourselves again at the same place?"
    e "If you had told the me from almost ten years ago, I wouldn’t have believed it."

    show emilia relief5 at right2
    voice audio.emilia_v_conj4b
    e "But I do have to say, it is somewhat comforting that this place is the same as it used to be, as unfortunate as that sounds."
    e "I’d always come to this spot so no one could find me, and I wouldn’t have to deal with other people."

    show emilia sigh1 at right2
    voice audio.emilia_v_ugh1
    e "Every day I spent here was miserable. Everyone hated me for just saying things as they were."
    e "I know everyone was just jealous of my higher status, so the only thing they could do was to cast me out."

    show yoshi2 confused2 at left2
    voice audio.yoshi_v_uh1b
    yo "I’m sorry, but… Is… this what you really wanted to talk about…?"

    show emilia angry2 at right2
    voice audio.emilia_v_surprised2a1
    e "Goodness gracious, I was getting there… Am I not allowed to set the mood? "

    voice audio.emilia_v_hmph1a
    e "Hmph! Since when did you become such a buzzkill?"

    show yoshi2 worry1 at left2
    yo "..."

    show emilia bold2 at right2
    voice audio.emilia_v_conj5b
    e "Well, I figured that since we’re going to work so closely for the next couple of months, it would be nice to start fresh and catch up, on a more personal level~!"
    e "This is a huge project after all, you’re going to need my help!"
    e "Think of it as me returning the favor. I don’t want to let an old friend down, after all."

    show yoshi2 think2 at left2
    voice audio.yoshi_v_ah2
    yo "Ah, about that, Emilia…"

    hide yoshi2_autumn
    hide yoshi2 think2
    show yoshi_autumn at left2
    show yoshi explain2 at left2
    voice audio.yoshi_v_actually1b
    yo "Sir Goro already assigned me to help him out with managerial duties …"
    yo "I think the best way for me to improve would be to work in his department!"

    play music heracleum_a loop
    show emilia irked2 at right2
    voice audio.emilia_v_what2
    e "What…?!"
    e "With that old man?"

    show emilia annoy2 at right2
    voice audio.emilia_v_so3
    e "So, you’re telling me you’re just going to let things run as they are, refusing any changes for the sake of the camp? My ears must be broken!"

    show yoshi awkward4 at left2
    voice audio.yoshi_v_what4
    yo "W-What…?"

    show emilia angry2 at right2
    voice audio.emilia_v_question1b2
    e "And how can you grow and utilize your full potential as a future leader if you keep sitting on the sidelines?!"
    e "The Yoshinori I know aspired for greater things, and not allowing himself to be bossed around so easily!"

    show yoshi awkward3 at left2
    voice audio.yoshi_v_emilia7
    yo "Emilia! That’s not—"

    show yoshi_autumn at center
    show yoshi shock1 at center
    show emilia_autumn at right
    show emilia shock1 at right
    with move

    show goro2_autumn at left
    show goro2 annoy3 at left
    with dissolve

    voice audio.goro_v_worry1a
    g "What’s going on here? I thought the meeting was over."

    show yoshi shock2 at center
    voice audio.yoshi_v_sirgoro5
    yo "A-Ah, Sir Goro…!"

    show emilia angry2 at right
    voice audio.emilia_v_goro6
    e "Mr. Nomoru. Why did you adjust someone’s position in the camp without my knowledge?"
    e "Yoshinori was supposed to be under my wing, not yours. That’s how I wrote it in the outline I gave everyone today."

    show goro2 disappoint3 at left
    voice audio.goro_v_hmph1a
    g "That decision isn’t up to only you, Ms. Komarova. You need both mine and Yoshinori’s consent as well."

    show emilia angry3 at right
    voice audio.emilia_v_disagree3b
    e "But I’m the manager here!"

    show goro2 angry3 at left
    voice audio.goro_v_scold2a1
    g "And I’m the president. My decisions are the final say for the camp. Even Mr. Clermont asks for my permission before making changes."

    show emilia angry6 at right
    voice audio.emilia_v_response1a
    e "Fine then."
    e "You should know this is the last time I’ll try and advocate for you, Yoshinori. Don’t come crying to me when something goes wrong later."

    hide emilia_autumn
    hide emilia angry6
    with dissolve

    hide yoshi_autumn
    hide yoshi shock2
    show yoshi2_autumn at center
    show yoshi2 worry4 at center
    voice audio.yoshi_v_emilia1
    yo "Emillia—"

    show goro2 disappoint2 at left
    voice audio.goro_v_scold1a1
    g "Leave her be. Things didn’t exactly go the way she wanted today."
    g "With this incident, she’s already earned a strike from me. If she keeps up this behavior, I might have to take further action."

    show yoshi2 sad4 at center
    voice audio.yoshi_v_isee2
    yo "I see… "

    hide goro2_autumn
    hide goro2 disappoint2
    show goro_autumn at left
    show goro talk1 at left
    voice audio.goro_v_anyway1
    g "Anyway, the others are waiting for us to eat. Shall we go and join them?"

    hide yoshi2_autumn
    hide yoshi2 sad4
    show yoshi_autumn at center
    show yoshi talk3 at center
    voice audio.yoshi_v_yessir3
    yo "Oh, r-right! Yes, sir! "

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
    play bgsound sfxloop_crowd loop
    play music buddy_oath_casual loop

    show darius_autumn at p7_2
    show darius norm3 at p7_2
    show lloyd_autumn at p7_1
    show lloyd norm4 at p7_1
    show jin_autumn at p7_3
    show jin_glasses at p7_3
    show jin norm3 at p7_3
    show aiden_autumn at p7_5
    show aiden norm3 at p7_5
    show yuri_autumn at p7_4
    show yuri norm3 at p7_4

    show goro_autumn at p8_7
    show goro norm3 at p8_7
    show yoshi_autumn at p8_8
    show yoshi worry1 at p8_8
    show aiden talk4 at p7_5
    voice audio.aiden_v_oh1b
    a "Oh! They’re back, you guys!"
    a "Over here, Yoshi and Gramps!"

    show goro_autumn at p7_6
    show goro norm3 at p7_6
    show yoshi_autumn at p7_7
    show yoshi talk1 at p7_7
    with move

    hide yoshi_autumn
    hide yoshi talk1
    show yoshi2_autumn at p7_7
    show yoshi2 talk1 at p7_7
    voice audio.yoshi_v_ah1
    yo "Ah, looks like you guys are done with breakfast."

    hide aiden_autumn
    hide aiden talk4
    show aiden2_autumn at p7_5
    show aiden2 comp3 at p7_5
    hide yuri_autumn
    hide yuri norm3
    show yuri_autumn at p7_4
    show yuri norm3 at p7_4
    voice audio.aiden_v_yeah1b2
    a "Hehe, yeah… Your food’s gotten cold already."
    a "We were gonna wait for you guys, but everyone’s kinda in a hurry."

    show jin sigh1 at p7_3
    voice audio.jin_v_conj2c1
    j "W-We figured we’d show up for work early now that we have an inspector…"

    show lloyd confused2 at p7_1
    voice audio.lloyd_v_confused1a1
    l "Why did Sir Goro follow you and Emilia? Did something happen?"

    show yuri pout2 at p7_4
    voice audio.yuri_v_hmph1a
    yu "Hmph. Dad probably just stopped her from shit-talking all of us."

    hide yoshi2_autumn
    hide yoshi2 talk1
    show yoshi_autumn at p7_7
    show yoshi explain2 at p7_7
    voice audio.yoshi_v_no1
    yo "No, Yuri, it was nothing like that..."
    yo "She was asking if I planned to accept her offer about working with her for the rest of the project."

    show yuri angry2 at p7_4
    voice audio.yuri_v_confused2b1
    yu "Huh??? For what?"

    show jin think1 at p7_3
    voice audio.jin_v_emilia2a
    j "Ms. Emilia seems to be partial towards Yoshi, from observation."

    show yuri annoy4 at p7_4
    voice audio.yuri_v_conj1b1
    yu "Seriously, I think it’s just some excuse to get Yoshi to do her job or something."

    show darius confused3 at p7_2
    voice audio.darius_v_conj2a
    d "Did you take her up on the offer?"

    show yoshi talk1 at p7_7
    voice audio.yoshi_v_actually1b
    yo "No… I already promised I’d help Sir Goro with his admin tasks, so, I turned her down…"

    show aiden2 worry2 at p7_5
    voice audio.aiden_v_really1b
    a "How’d she take that?"

    hide yoshi_autumn
    hide yoshi talk1
    show yoshi2_autumn at p7_7
    show yoshi2 upset6 at p7_7
    voice audio.yoshi_v_sigh3a
    yo "Not well, honestly… She got pretty angry."

    show aiden2 worry2 at p7_5
    voice audio.aiden_v_shock2a1
    a "Yikes… I can only imagine…"

    show yoshi2 explain2 at p7_7
    voice audio.yoshi_v_but1
    yo "But luckily Sir Goro showed up and took control of the situation."

    hide goro_autumn
    hide goro norm3
    show goro2_autumn at p7_6
    show goro2 disappoint2 at p7_6
    voice audio.goro_v_annoyed1a1
    g "As soon as I arrived, I could tell she was trying to corner you."
    g "She doesn’t seem to take rejection well… Just like when I spoke up at the meeting earlier."

    show lloyd sigh5 at p7_1
    voice audio.lloyd_v_agree2c2
    l "Yeah… I can tell that lady does not like us at all."

    show darius annoy2 at p7_2
    voice audio.darius_v_ugh1
    d "Her tone was very... pointy."

    show yuri rage3 at p7_4
    voice audio.yuri_v_relief2b1
    yu "Oh, thank goodness, it’s not just me! "
    yu "Why did you even let her take charge, Dad? You've been in charge of everything this whole time just fine."

    show goro2 sigh1 at p7_6
    voice audio.goro_v_sigh1a
    g "I… didn’t expect that she would be going this far to be honest. I wasn’t informed that our inspector would also be getting involved in management…"

    show yuri rage1 at p7_4
    voice audio.yuri_v_response2b1
    yu "She didn’t even DO anything! All she did was make a crappy schedule and then agree to go back to the one you made, Dad."

    show goro2 think4 at p7_6
    voice audio.goro_v_think1a1
    g "Hmm… Perhaps Mr. Clermont directly ordered her to make those changes…"

    show yuri irked2 at p7_4
    voice audio.yuri_v_annoyed3a
    yu "I doubt it. Like you said back there, he already knew about the winter break. She’s just trying to nitpick and micromanage like she did yesterday!"

    show lloyd annoy2 at p7_1
    voice audio.lloyd_v_agree2c2
    l "Yeah… I don't understand why she labeled the construction department as ‘DELAYED’ in red ink and all caps. As far as I know we were doing just fine…"

    show jin worry2 at p7_3
    voice audio.jin_v_yeah2a
    j "She said the same thing to me yesterday, too… It’s why I was up working all night…"

    show yuri rage1 at p7_4
    voice audio.yuri_v_annoyed1a
    yu "It’s only her first day here and she’s already crossing the line!"

    show aiden2 comp3 at p7_5
    voice audio.aiden_v_comp3a
    a "Calm down, Yuri… I don’t think we have to take everything she said so personally."

    show goro2 talk1 at p7_6
    voice audio.goro_v_agree4a1
    g "Exactly. We don’t need to like her, but Mr. Clermont assigned her here for a reason. We have to trust his judgement."

    hide yoshi2_autumn
    hide yoshi2 explain2
    show yoshi_autumn at p7_7
    show yoshi talk1 at p7_7
    voice audio.yoshi_v_guys3
    yo "Let’s give her the benefit of the doubt for now. We know at the very least that we all have the same common goal."

    show yuri annoy2 at p7_4
    voice audio.yuri_v_unsure1b3
    yu "I don’t know about you guys, but I have a really bad gut feeling about that Emilia. "

    hide goro2_autumn
    hide goro2 talk1
    show goro_autumn at p7_6
    show goro talk1 at p7_6
    voice audio.goro_v_comp1c1
    g "I understand your concerns, Yuri. But we have to work together for now and stay professional, especially since she was sent directly by our sponsor."

    show yuri pout1 at p7_4
    voice audio.yuri_v_agree5a3
    yu "Ugh… Fine. I’ll try to not to stoop down to her level, and I’ll prove we can do our job."

    hide goro_autumn
    hide goro talk1
    show goro2_autumn at p7_6
    show goro2 talk2 at p7_6
    voice audio.goro_v_comp2a1
    g "And don’t worry, all of you. If Emilia insists on handling things immaturely, I won’t hesitate to reprimand her."

    hide aiden2_autumn
    hide aiden2 comp3
    show aiden_autumn at p7_5
    show aiden bold2 at p7_5
    voice audio.aiden_v_yeah1a3
    a "Yeah, tell her, Gramps! "

    show jin think2 at p7_3
    voice audio.jin_v_sigh1a
    j "On that note… I-I think I have to get to work before Emilia thinks I’m slacking… "

    voice audio.jin_v_bye1a3
    j "Please excuse me…"

    hide jin_autumn
    hide jin_glasses
    hide jin think2
    with dissolve

    show lloyd tired5 at p7_1
    voice audio.lloyd_v_unsure1a1
    l "I guess Dar and I better get to work too. Don’t wanna get marked as delayed again, right?  "

    show darius talk1 at p7_2
    voice audio.darius_v_bye1a
    d "Bye."

    hide lloyd_autumn
    hide lloyd tired5
    hide darius_autumn
    hide darius talk1
    with dissolve

    show aiden shock2 at p7_5
    voice audio.aiden_v_shock2a1
    a "Yikes, I just remembered I have to get the workers’ rooms cleaned up!"

    voice audio.aiden_v_bye1a
    a "Gotta go!"

    hide aiden_autumn
    hide aiden shock2
    with dissolve

    show yuri comp2 at p7_4
    voice audio.yuri_v_thanks2a
    yu "Thanks for reassuring everyone after this morning, Dad! "

    voice audio.yuri_v_bye2a
    yu "I’m off to check on the workers – see you boys later!"

    hide yuri_autumn
    hide yuri comp2
    with dissolve

    show goro2_autumn at left2
    show goro2 talk3 at left2
    show yoshi_autumn at right2
    show yoshi sad2 at right2
    with move

    hide goro2_autumn
    hide goro2 talk3
    show goro_autumn at left2
    show goro talk3 at left2
    voice audio.goro_v_unsure3a1
    g "I guess that’s our cue to get started as well, Yoshinori. "

    hide yoshi_autumn
    hide yoshi sad2
    show yoshi2_autumn at right2
    show yoshi2 sad2 at right2
    yo "..."

    hide goro_autumn
    hide goro talk3
    show goro2_autumn at left2
    show goro2 confused2 at left2
    voice audio.goro_v_yoshi6
    g "Yoshinori?"

    show yoshi2 worry2 at right2
    voice audio.yoshi_v_sorry4a
    yo "Ah, sorry. I was just thinking about how Emilia reacted back there."

    show goro2 think3 at left2
    voice audio.goro_v_worry2a
    g "What exactly are you worried about?"

    $ working = False
    $ shuffle_menu()
    menu():
        g "What exactly are you worried about?{fast}"
        "I don't want you to get stressed.":
            $ working = True
            $ score_goro -= 1
            $ score_top += 1
            show yoshi2 sad4 at right2
            voice audio.yoshi_v_well2
            yo "I don’t want you to get stressed because of Emilia."

            show goro2 talk1 at left2
            voice audio.goro_v_no2a1
            g "I won’t. And It doesn’t matter as long as we do our jobs."
        "Emilia might be more trouble than help.":
            $ working = True
            $ score_goro -= 1
            $ score_bot += 1
            show yoshi2 sad4 at right2
            voice audio.yoshi_v_well2
            yo "I’m afraid Emilia might cause us more trouble than help."

            show goro2 talk1 at left2
            voice audio.goro_v_no2a1
            g "Not on my watch."
        "I want us to enjoy this project.":
            $ working = True
            $ score_goro += 1
            $ score_top += 1
            show yoshi2 sad4 at right2
            voice audio.yoshi_v_well2
            yo "Well… I want us to enjoy this project, sir."

            show goro2 confused3 at left2
            voice audio.goro_v_think1c1
            g "Hmm? What makes you think otherwise?"

            show yoshi2 sigh1 at right2
            voice audio.yoshi_v_sigh3a
            yo "I feel like Emilia’s not going to make it easy for us for some reason…"
        "I really hope I can help.":
            $ working = True
            $ score_goro += 1
            $ score_bot += 1
            show yoshi2 sad4 at right2
            voice audio.yoshi_v_well2
            yo "Well… I just really hope I can help you with this project, sir."

            show goro2 confused3 at left2
            voice audio.goro_v_think1c1
            g "Hmm? What makes you think otherwise?"

            show yoshi2 sigh1 at right2
            voice audio.yoshi_v_sigh3a
            yo "I feel like Emilia’s not going to make it easy for us for some reason…"

    show goro2 explain2 at left2
    voice audio.goro_v_comp2a2
    g "Like I said to everyone earlier, you can count on me to put Emilia in her place if she gets out of bounds."

    show yoshi2 upset6 at right2
    voice audio.yoshi_v_but2
    yo "I have no doubts about that, sir… But I had just hoped that going into this season, you wouldn’t have to deal with something like this."

    hide goro2_autumn
    hide goro2 explain2
    show goro_autumn at left2
    show goro comp2 at left2
    voice audio.goro_v_thanks2a1
    g "I appreciate your honesty, Yoshinori. And I know exactly what you mean when you say that."

    hide goro_autumn
    hide goro comp2
    show goro2_autumn at left2
    show goro2 explain2 at left2
    voice audio.goro_v_conj1a1
    g "However, I need you to understand that I’m trying to change too. Or at least to be back to how I was long ago."
    g "As Camp Buddy’s leader, I should be able to do my job with patience and kindness. Not with strictness and heartless professionalism."

    hide goro2_autumn
    hide goro2 explain2
    show goro_autumn at left2
    show goro comp2 at left2
    voice audio.goro_v_encourage2a
    g "I want everyone, especially you, to be able to trust and count on me again, just like you did back then."

    hide yoshi2_autumn
    hide yoshi2 upset6
    show yoshi_autumn at right2
    show yoshi comp2 at right2
    voice audio.yoshi_v_sirgoro12
    yo "Sir Goro… "

    show goro bold2 at left2
    g "So, don’t worry, and just focus on the great work we’ll be doing together for Camp Buddy. It’ll be just like the good ol’ days!"

    voice audio.goro_v_confident1a
    g "Just follow my lead, and everything will be fine!"

    show yoshi laugh2 at right2
    voice audio.yoshi_v_yessir1
    yo "Yes, sir!"

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
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_campgrounds_autumn_day
    show mtgg1 at fx_pos
    with fade
    voice audio.yoshi_vsg7_line1
    play music buddy_oath_casual loop
    yo "For the next few weeks, Sir Goro and I worked side by side on our tasks."

    voice audio.yoshi_vsg7_line2
    yo "I was pretty shocked at how different and mentally taxing management could be."

    voice audio.yoshi_vsg7_line3
    yo "But thankfully, Sir Goro didn’t lose patience and guided me every step of the way until I was able to adjust."

    scene bg_site3_autumn_sunset
    $ day = "21"
    $location = location_site
    $time = timeline_timesunset
    show mtgg2 at fx_pos
    with Dissolve(0.25)
    voice audio.yoshi_vsa6_line3
    yo "With Emilia pushing a tight schedule, the construction moved forward at a very fast pace."

    voice audio.yoshi_vsg7_line4
    yo "Occasionally, Sir Goro and I would help Lloyd and Darius with their department to accelerate the progress, not hesitating to get our hands dirty."

    voice audio.yoshi_vsa6_line5
    yo "Everyone worked extra hard to meet the deadlines and we managed to accomplish every target Emilia set for us."

    voice audio.yoshi_vsa6_line6
    yo "Seeing the frameworks of the new cabins at the expansion site, we could already imagine how different the camp was going to look."

    scene bg_quarters_autumn_night
    $ day = "26"
    $location = location_quarters
    $time = timeline_timenight
    show mtgg3 at fx_pos
    with Dissolve(0.25)
    voice audio.yoshi_vsg7_line5
    yo "In the evenings, we’d work with Jin towards the technological goals of the project. Sometimes even joining him in his sleepless nights."

    voice audio.yoshi_vsg7_line6
    yo "We had to relaunch our website and keep it updated to cater for online enrollments and job applications."

    voice audio.yoshi_vsg7_line7
    yo "From what Jin explained, he also managed to secure an internet connection and a security system for the camp."

    scene bg_messhall_autumn_day
    $ day = "37"
    $location = location_messhall
    $time = timeline_timeday
    show mtgg4 at fx_pos
    with Dissolve(0.25)
    voice audio.yoshi_vsg7_line8
    yo "Meanwhile, Aiden was swamped with chores, as usual."

    voice audio.yoshi_vsg7_line9
    yo "Between cooking, laundry, repairs, and cleaning for a horde of workers, there was more to do than ever before."

    voice audio.yoshi_vsg7_line10
    yo "Thankfully, because Sir Goro and I were handling most of the management, Yuri was able to focus on assisting Aiden."

    voice audio.yoshi_vsg7_line11
    yo "I’m not exactly sure how helpful she’s been, knowing how distracted she could get when she’s around Aiden."

    scene bg_bathroom_autumn_sunset
    $ day = "41"
    $location = location_bathroom
    $time = timeline_timesunset
    show mtgg5 at fx_pos
    with Dissolve(0.25)
    voice audio.yoshi_vsg7_line12
    yo "Although, I’m pretty guilty of being distracted sometimes too."

    voice audio.yoshi_vsg7_line13
    yo "Ever since Sir Goro moved into our cabin, I started to see his more casual and playful side, which took some getting used to considering he’s my boss."

    scene bg_clermontoffice_day
    $ day = "43"
    $location = location_clermont
    $time = timeline_timeday
    show mtgg6 at fx_pos
    with Dissolve(0.25)
    voice audio.yoshi_vsg7_line14
    yo "On top of our other responsibilities, Sir Goro had me tag along to his meetings and appointments. With each one, I started to gain confidence and learn from him."

    voice audio.yoshi_vsg7_line15
    yo "It made me realize how easy it is to take for granted how much serious, but not always exciting, work Sir Goro does behind the scenes outside of the camp… "

    voice audio.yoshi_vsg7_line16
    yo "He never once complains about it though, and always get everything done without concern."

    scene bg_office_autumn_night
    $ day = "46"
    $location = location_office
    $time = timeline_timenight
    show mtgg7 at fx_pos
    with Dissolve(0.25)
    voice audio.yoshi_vsg7_line17
    yo "As we had expected, there were times when Emilia would criticize the way Sir Goro had been running things, making her grow more and more frustrated. "

    voice audio.yoshi_vsg7_line18
    yo "I could see how Sir Goro was trying his best to control himself and stay focused on the task. The least I could do was always keep him company."

    scene bg_entrance_autumn_sunset
    $ day = "61"
    $location = location_car
    $time = timeline_timesunset
    show mtgg8 at fx_pos
    with Dissolve(0.25)
    voice audio.yoshi_vsg7_line19
    yo "But even though our work could get overwhelming, he would always make sure we enjoyed the few peaceful moments we got to spend with just the two of us. It’s what encouraged me to keep doing my best."

    scene bg_gororoom_autumn_night_lightsout
    $ day = "65"
    $location = location_gororoom
    $time = timeline_timenight
    show mtgg9 at fx_pos
    with Dissolve(0.25)
    voice audio.yoshi_vsg7_line20
    yo "Feeling closer to Sir Goro made it all worth it."

    scene cg black with fade
    voice audio.yoshi_vsg7_line21
    yo "{i}Before we knew it, a month and a half had gone by and the season was about to change again…{/i}"

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    play sound sleeping_time
    $ time_transition_night_to_day_fall()
    jump day2_goro
