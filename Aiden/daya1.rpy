label day1_aiden:
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
    voice audio.yoshi_v_yawn1
    yo "Nnn… *stretches*"

    show yoshi2_sleep at p6_1
    show yoshi2 sleepy3 at p6_1
    with move

    show aiden_sleep at p6_2
    show aiden happy2 at p6_2
    show darius_sleep at p6_4
    show darius norm1 at p6_4
    show lloyd_sleep at p6_3
    show lloyd norm1 at p6_3
    show goro_sleep at p6_5
    show goro norm1 at p6_5
    show jin_sleep at p6_6
    show jin_glasses at p6_6
    show jin norm1 at p6_6
    with dissolve

    voice audio.aiden_v_hey1b3
    a "Oh hey, you’re up, Yoshi!"

    show goro happy1 at p6_5
    voice audio.goro_v_goodam1a1
    g "Good morning, Yoshinori."

    hide yoshi2_sleep
    hide yoshi2 sleepy3
    show yoshi_sleep at p6_1
    show yoshi talk1 at p6_1
    voice audio.yoshi_v_goodam1
    yo "Good morning too, guys! "
    yo "Haha, looks like everyone really does get up earlier than me. "

    show aiden explain2 at p6_2
    voice audio.aiden_v_well1a3
    a "Well, we all wanna give that inspector a better impression today, like Gramps said last night."
    a "That, and I made everyone some hot cocoa and coffee~!"

    show darius relief2 at p6_4
    voice audio.darius_v_think1a2
    d "*sip* Mmm… "

    show aiden talk1 at p6_2
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

    hide aiden_sleep
    hide aiden explain2
    show aiden2_sleep at p6_2
    show aiden2 confused5 at p6_2
    hide yoshi_sleep
    hide yoshi talk3
    show yoshi_sleep at p6_1
    show yoshi talk3 at p6_1
    voice audio.aiden_v_shock2b1
    a "Sounds complicated to me. Shouldn’t you get some rest, buddy? "

    show jin happy2 at p6_6
    voice audio.jin_v_conj1d1
    j "I’m already done for the day, actually! Now I can hang out with you guys before I go to bed!"

    show goro happy2 at p6_5
    voice audio.goro_v_agree1a1
    g "Yes, come relax with us while we finish our breakfast. We’re way too early for today’s schedule, anyway."

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
    voice audio.lloyd_v_agree2a3
    l "Not just that! You see, tarot cards are used to gain insight into the past, present or future by formulating a question, then drawing and interpreting the cards~!"
    l "It’s up to the individual as to what they do with the knowledge seen on their path."

    show yoshi confused3 at p6_1
    voice audio.yoshi_v_oh3
    yo "Oh… that’s interesting. So that’s what you were talking about last night, too."

    show lloyd grin1 at p6_3
    voice audio.lloyd_v_agree1a1
    l "Yup! "

    show goro talk1 at p6_5
    voice audio.goro_v_actually1a
    g "Lloyd did mine a while ago and it was mostly accurate."

    show goro play2 at p6_5
    voice audio.goro_v_heh1a
    g "I don’t usually believe in things like these but… I must say, this is some lighthearted entertainment."

    show lloyd explain4 at p6_3
    voice audio.lloyd_v_ignored1a1
    l "*ehem* It’s a closely related sub-branch of astrology!"

    show yoshi talk1 at p6_1
    voice audio.yoshi_v_lloyd5b
    yo "I’m curious. What did Sir Goro’s reading say, Lloyd?"

    show lloyd explain6 at p6_3
    voice audio.lloyd_v_conj1a3
    l "Well, after I drew the ‘Sun, ‘World’, and ‘Fool’, we determined that they all encompass his persona and general approach to life!"

    show goro tease5 at p6_5
    voice audio.goro_v_heh3b
    g "Did he just call Aiden a… fool?"

    hide aiden2_sleep
    hide aiden2 confused5
    show aiden_sleep at p6_2
    show aiden angry3 at p6_2
    voice audio.aiden_v_hey1c2
    a "HEY!"

    show lloyd shock3 at p6_3
    voice audio.lloyd_v_disagree1d2
    l "N-No! Don’t misunderstand - these cards mean good things like free spirit, fullfilment and harmony!"

    show lloyd explain3 at p6_3
    voice audio.lloyd_v_conj4a1
    l "The sun references happiness, warmth and vitality, and when combined with the Fool emphasizes innocence and optimism!"
    l "When further combined with the World, it may reflect a lack of power over events, but with patience, a new opportunity can be expected!"

    show lloyd explain2 at p6_3
    voice audio.lloyd_v_think1a1
    l "Pains and struggles from the past are balanced out with boundless growth and inner strength…"
    l "So, face your choices firmly to achieve your ideal happiness, or else it could lead to your ultimate regret!"

    show yoshi worry2 at p6_1
    voice audio.yoshi_v_oops1
    yo "T-That sounds really ominous… Is Aiden going to be alright?"

    show aiden bold5 at p6_2
    voice audio.aiden_v_no2a1
    a "Naaaah~ I don’t really take it too seriously! Especially not from a leprechaun."

    show lloyd angry2 at p6_3
    voice audio.lloyd_v_greet2c1
    l "L-Leprechaun?! You could’ve at least called me a wizard!"

    show darius happy1 at p6_4
    voice audio.darius_v_agree3
    d "Either way, that’s a good mindset for the whole thing, Aiden."
    d "Lloyd kept foretelling the ‘Death’ one for me, too. But I’m still alive."

    show lloyd tease2 at p6_3
    voice audio.lloyd_v_greet2a1
    l "Hey! You never know! Maybe not for long!"

    show yoshi_sleep at p7_2
    show yoshi worry2 at p7_2
    show aiden_sleep at p7_3
    show aiden bold5 at p7_3
    show lloyd_sleep at p7_4
    show lloyd angry2 at p7_4
    show darius_sleep at p7_5
    show darius happy1 at p7_5
    show goro_sleep at p7_6
    show goro tease5 at p7_6
    show jin_sleep at p7_7
    show jin_glasses at p7_7
    show jin happy2 at p7_7
    with move

    play sound sfx_doorslam
    show yuri_autumn at p7_1
    show yuri annoy1 at p7_1
    with dissolve

    show goro_sleep at p7_6
    show goro talk3 at p7_6
    voice audio.goro_v_oh1a
    g "Oh, Yuri, dear. What brings you he—"

    show yuri annoy2 at p7_1
    voice audio.yuri_v_guys1b
    yu "Emilia wants everyone in the campsite. Now."

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
    show aiden_sleep at p6_2
    show aiden bold5 at p6_2
    show lloyd_sleep at p6_3
    show lloyd angry2 at p6_3
    show darius_sleep at p6_4
    show darius happy1 at p6_4
    show goro_sleep at p6_5
    show goro talk3 at p6_5
    show jin_sleep at p6_6
    show jin_glasses at p6_6
    show jin happy2 at p6_6
    with move

    hide aiden_sleep
    hide aiden bold5
    show aiden2_sleep at p6_2
    show aiden2 sigh4 at p6_2
    hide yoshi_sleep
    hide yoshi confused3
    show yoshi_sleep at p6_1
    show yoshi confused3 at p6_1
    voice audio.aiden_v_sheesh1a
    a "Sheesh… Sounds like someone woke up on the wrong side of the bed today, huh…? "

    show goro sigh2 at p6_5
    voice audio.goro_v_sigh1a
    g "*sigh* I wonder what Emilia did to get on her nerves so early in the morning…"

    hide aiden2_sleep
    hide aiden2 sigh4
    show aiden_sleep at p6_2
    show aiden think2 at p6_2
    voice audio.aiden_v_think1a1
    a "I’d expected her to spazz over how a bunch of guys slept together!"

    show lloyd think5 at p6_3
    voice audio.lloyd_v_think1a1
    l "I guess knowing her, it is odd. "

    show goro talk2 at p6_5
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
    play sound sfx_clotheschanging
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
    show darius shock4 at p8_2
    show goro_autumn at p8_4
    show goro norm3 at p8_4
    show aiden_autumn at p8_5
    show aiden worry1 at p8_5
    show yoshi_autumn at p8_6
    show yoshi norm3 at p8_6
    show yuri_autumn at p8_7
    show yuri annoy1 at p8_7
    show emilia_autumn at p8_8
    show emilia eyeroll4 at p8_8
    show jin_autumn at p8_1
    show jin worry1 at p8_1
    show jin_glasses at p8_1
    show lloyd_autumn at p8_3
    show lloyd norm3 at p8_3
    voice audio.emilia_v_tsk1a
    e "Tsk, tsk. Late, just like I expected… "

    show yuri angry2 at p8_7
    voice audio.yuri_v_hmph1a
    yu "This meeting isn’t even on the schedule. "

    show emilia irked2 at p8_8
    voice audio.emilia_v_question2a1
    e "Scheduled or not, the management staff being the last ones to arrive is very telling."
    e "Whatever happened to this camp’s oath about being prepared for anything? "

    show yuri pout2 at p8_7
    yu "..."

    show yoshi worry1 at p8_6
    yo "..."

    show emilia evil3 at p8_8
    voice audio.emilia_v_sarcastic2b2
    e "I thought so."

    show yuri irked1 at p8_7
    voice audio.yuri_v_well1a
    yu "Well, we’re here now. What do you want?"

    hide goro_autumn
    hide goro norm3
    show goro2_autumn at p8_4
    show goro2 annoy2 at p8_4
    hide lloyd_autumn
    hide lloyd norm3
    show lloyd_autumn at p8_3
    show lloyd norm3 at p8_3
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
    show jin norm4 at p8_2
    show jin_glasses at p8_2
    show darius_autumn at p8_3
    show darius shock4 at p8_3
    show lloyd_autumn at p8_4
    show lloyd norm3 at p8_4
    show goro2_autumn at p8_5
    show goro2 annoy2 at p8_5
    show aiden_autumn at p8_6
    show aiden worry1 at p8_6
    show yoshi_autumn at p8_7
    show yoshi worry1 at p8_7
    show yuri_autumn at p8_8
    show yuri irked1 at p8_8
    with move

    voice audio.emilia_v_so1
    e "These folders contain each department’s tasks, concerns, and a reminder of how everything should be done. Make sure to read and follow the details carefully."

    show jin_autumn at p8_1
    show jin norm4 at p8_1
    show jin_glasses at p8_1
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
    show emilia_autumn at p8_4
    show emilia annoy3 at p8_4
    show goro2_autumn at p8_5
    show goro2 bored2 at p8_5
    with move

    voice audio.emilia_v_william2
    e "Mr. Clermont has invested a LOT into this venture, so I’m sure we can all agree to show him nothing but the best."

    show goro2_autumn at p8_4
    show goro2 bored2 at p8_4
    show aiden_autumn at p8_5
    show aiden worry1 at p8_5
    show yoshi_autumn at p8_6
    show yoshi worry1 at p8_6
    show emilia_autumn at p8_7
    show emilia evil4 at p8_7
    show yuri_autumn at p8_8
    show yuri pout2 at p8_8
    with move

    voice audio.emilia_v_bossy4
    e "No hard feelings, it’s just business after all."

    show emilia_autumn at p8_6
    show emilia annoy2 at p8_6
    show yoshi_autumn at p8_7
    show yoshi worry1 at p8_7
    show yuri_autumn at p8_8
    show yuri pout2 at p8_8
    with move

    voice audio.emilia_v_scoff1
    e "Take special note with yours, I’ve added extra details addressing my concerns from yesterday."

    hide aiden_autumn
    hide aiden worry1
    show aiden2_autumn2 at p8_5
    show aiden2 worry5 at p8_5
    hide goro2_autumn
    hide goro2 bored2
    show goro2_autumn at p8_4
    show goro2 bored2 at p8_4
    hide lloyd_autumn
    hide lloyd confused1
    show lloyd_autumn at p8_3
    show lloyd confused1 at p8_3
    voice audio.aiden_v_shock1d1
    a "Whoa… I get a stack...?"

    show emilia sigh2 at p8_6
    voice audio.emilia_v_sigh1a
    e "I’m just as surprised, as I thought maintenance was fairly self-explanatory, but clearly you needed more guidance to do such a simple job."

    show aiden2 upset1 at p8_5
    a "..."

    show yoshi_autumn at p8_6
    show yoshi norm4 at p8_6
    show emilia_autumn at p8_7
    show emilia bold2 at p8_7
    with move

    voice audio.emilia_v_see2b
    e "I’m sure if we all approach this with a positive attitude, we’ll achieve our collective goal. That’s what we all want, isn’t it?"

    voice audio.emilia_v_conj3a
    e "Now, for all the workers, grab a copy of the schedule here. "

    show goro2 confused2 at p8_4
    voice audio.goro_v_sorry1c1
    g "Forgive me for interrupting, Ms. Komarova, but… "
    g "I’ve noticed that this schedule is similar to our previous one but now includes extensive work over the winter season."

    show emilia talk1 at p8_7
    voice audio.emilia_v_agree2a1
    e "Yes, it has come to my attention that the original timetable included a large unproductive break of several weeks."
    e "I think it would be a waste of time to stop, especially since we’ll have already built up our momentum by then."

    hide goro2_autumn
    hide goro2 confused2
    show goro_autumn at p8_4
    show goro explain2 at p8_4
    hide lloyd_autumn
    hide lloyd confused1
    show lloyd_autumn at p8_3
    show lloyd confused1 at p8_3
    voice audio.goro_v_think1a1
    g "If I may, the weather can get quite harsh during the winter around these parts…"
    g "It could potentially be a hazardous environment for our workers, and there would be additional costs for the necessary equipment to work in such conditions."

    show goro talk1 at p8_4
    voice audio.goro_v_comp2a1
    g "But don’t worry – the originally scheduled downtime has already been considered and it shouldn’t affect our targeted completion date."
    g "In fact, I’ve already consulted with Mr. Clermont and he has given his approval for the break."

    show goro confused3 at p8_4
    voice audio.goro_v_unsure2a
    g "It was in the e-mail chain you requested access to. Did you get a chance to read it?"

    show emilia angry2 at p8_7
    voice audio.emilia_v_agree1c1
    e "O-Of course I have! It’s my job to know all the details of the project after all!"
    e "I only adjusted the schedule based on the issues that were made apparent to me yesterday during my survey!"

    show emilia angry3 at p8_7
    voice audio.emilia_v_sarcastic2a
    e "It’s common sense to ensure that there is plenty of time at the tail-end of any project to allow for any setbacks, which was my main reason for the extended work period!"
    e "But if you want to do it your way, then so be it."

    show emilia eyeroll6 at p8_7
    voice audio.emilia_v_hmph1a
    e "Just be prepared for stricter deadlines and less room for error!"

    show yuri annoy2 at p8_8
    voice audio.yuri_v_so1a
    yu "Is that all? We’re wasting that ‘precious work time’ right now with this meeting."

    show emilia rage4 at p8_7
    voice audio.emilia_v_question4b
    e "Excuse me?!"

    show yuri_autumn at p8_8
    show yuri annoy2 at p8_8
    show yoshi_autumn at p8_7
    show yoshi talk2 at p8_7
    show emilia_autumn at p8_6
    show emilia rage4 at p8_6
    with move

    voice audio.yoshi_v_ehem1b
    yo "Maybe we can move forward and discuss the specifics of the schedule?"

    show emilia angry3 at p8_6
    voice audio.emilia_v_angry1a
    e "I would have if I wasn’t so rudely interrupted."
    e "Anyway, I am left with no choice but to cede to the camp president’s decision, and will include this extensive break in our schedule."

    show emilia angry2 at p8_6
    voice audio.emilia_v_response1a
    e "That means we need to get as much work done as possible before the season ends."

    show emilia angry5 at p8_6
    voice audio.emilia_v_rush2
    e "Everyone should follow the instructions I’ve handed out today, but I will follow up with a revised schedule with STRICTER deadlines, as Mr. Nomoru requested."
    e "I’ll be checking on all of your progress at the end of the day. You’re all dismissed!"

    hide lloyd_autumn
    hide lloyd confused1
    hide darius_autumn
    hide darius disgust1
    hide jin_autumn
    hide jin norm4
    hide jin_glasses
    hide goro_autumn
    hide goro confused3
    hide yuri_autumn
    hide yuri annoy2
    hide aiden2_autumn2
    hide aiden2 worry5
    with moveoutleft

    show yoshi_autumn at p5_1
    show yoshi norm4 at p5_1
    show emilia_autumn at p8_6
    show emilia annoy1 at p8_6
    voice audio.emilia_v_yoshi2
    with move
    e "Yoshinori."

    show yoshi_autumn at left2
    show yoshi confused2 at left2
    show emilia_autumn at right2
    show emilia annoy1 at right2
    with move

    voice audio.yoshi_v_yes1
    yo "Yes, Emilia?"

    show emilia talk1 at right2
    voice audio.emilia_v_rush1b1
    e "Come with me for a moment. I’d like to talk about something."

    show yoshi awkward4 at left2
    voice audio.yoshi_v_oh3
    yo "Oh… Alright, then."

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black
    hide screen location
    hide screen timeline
    hide screen quick_menu
    $quick_menu = False
    with fade
    $ renpy.pause (1.0, hard=True)

    $ location = location_lake
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_lake_autumn_day with fade
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
    e "Well, I figured that since we’re going to work so closely for the next couple of months, it would be nice to start fresh and catch up, on a more personal level~!"

    voice audio.emilia_v_conj5b
    e "This is a huge project after all, you’re going to need my help!"
    e "Think of it as me returning the favor. I don’t want to let an old friend down, after all."

    show yoshi2 think2 at left2
    voice audio.yoshi_v_ah2
    yo "Ah, about that, Emilia…"

    hide yoshi2_autumn
    hide yoshi2 think2
    show yoshi_autumn at left2
    show yoshi explain2 at left2
    voice audio.yoshi_v_well1
    yo "I thought it would be best if I concentrate my efforts on the construction and staff management departments."
    yo "Since those do have the most room for improvement, as you said back in the meeting. Aiden could really use some help with the oversight."

    play music heracleum_a loop
    show emilia irked2 at right2
    voice audio.emilia_v_what2
    e "What…? Aiden?"
    e "You mean the helper?"

    show emilia annoy2 at right2
    voice audio.emilia_v_so3
    e "So, you’re telling me your plan is to help wash dishes and unclog toilets to contribute to this project? My ears must be broken."

    show yoshi awkward4 at left2
    voice audio.yoshi_v_what4
    yo "W-What…?"

    show emilia angry2 at right2
    voice audio.emilia_v_question1b2
    e "Why in the world would you demote yourself to such grueling labor?!"
    e "You could be working in a position of leadership and instead you choose manual labor? You must not be the same person I remember!"

    show yoshi awkward3 at left2
    voice audio.yoshi_v_emilia7
    yo "Emilia! That’s not—"

    show emilia rage5 at right2
    voice audio.emilia_v_response1a
    e "So be it, Yoshinori. Don’t come crying to me when you are fully aware of how excruciatingly hectic the next few months are going to be!"

    hide emilia_autumn
    hide emilia rage5
    with dissolve

    hide yoshi_autumn
    hide yoshi awkward3
    show yoshi2_autumn at left2
    show yoshi2 worry1 at left2
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
    show goro_autumn at p7_5
    show goro norm3 at p7_5
    show jin_autumn at p7_3
    show jin norm3 at p7_3
    show jin_glasses at p7_3
    show yuri_autumn at p7_4
    show yuri norm3 at p7_4
    show aiden_autumn at p7_6
    show aiden norm3 at p7_6

    show yoshi2_autumn at p8_8
    show yoshi2 upset4 at p8_8
    show aiden_autumn at p7_6
    show aiden talk4 at p7_6
    voice audio.aiden_v_oh1b
    a "Oh! He’s back, you guys!"
    a "Over here, Yoshi!"

    show yoshi2_autumn at p7_7
    show yoshi2 talk1 at p7_7
    with move

    voice audio.yoshi_v_ah1
    yo "Ah, looks like you guys are done with breakfast."

    hide aiden_autumn
    hide aiden talk4
    show aiden2_autumn2 at p7_6
    show aiden2 comp3 at p7_6
    hide goro_autumn
    hide goro norm3
    show goro_autumn at p7_5
    show goro norm3 at p7_5
    hide yuri_autumn
    hide yuri norm3
    show yuri_autumn at p7_4
    show yuri norm3 at p7_4
    voice audio.aiden_v_yeah1b2
    a "Ahehe… Yeah… Your food’s gotten cold already.  "
    a "We were gonna wait for you, but everyone’s kinda in a hurry."

    show goro talk1 at p7_5
    voice audio.goro_v_sigh1a
    g "I figured we should show up for work early now that we have an inspector."

    show lloyd confused2 at p7_1
    voice audio.lloyd_v_confused1a1
    l "What did Emilia even drag you away for?"

    show yuri pout2 at p7_4
    voice audio.yuri_v_hmph1a
    yu "Hmph. Probably to talk shit about all of us."

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
    voice audio.yuri_v_emilia2a
    yu "Seriously, I think it’s just some excuse to get Yoshi to do her job or something."

    show darius confused3 at p7_2
    voice audio.darius_v_conj2a
    d "Did you take her up on the offer?"

    show yoshi talk1 at p7_7
    voice audio.yoshi_v_actually1b
    yo "No, actually. I’ve already decided to focus on working with Aiden."

    show aiden2 worry2 at p7_6
    voice audio.aiden_v_really1b
    a "How’d she take that?"

    hide yoshi_autumn
    hide yoshi talk1
    show yoshi2_autumn at p7_7
    show yoshi2 upset6 at p7_7
    voice audio.yoshi_v_well3
    yo "W-Well, let’s just say she was really expecting I’d say yes to her offer…"

    show aiden2 sigh4 at p7_6
    voice audio.aiden_v_sheesh1a
    a "Sheesh… I can only imagine her reaction."

    hide goro_autumn
    hide goro talk1
    show goro2_autumn at p7_5
    show goro2 think5 at p7_5
    voice audio.goro_v_think1a1
    g "She didn't seem to take it well when I spoke up at the meeting earlier."

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

    show goro2 sigh1 at p7_5
    voice audio.goro_v_sigh1a
    g "I… didn’t expect that she would be going this far to be honest. I wasn’t informed that our inspector would also be getting involved in management…"

    show yuri rage1 at p7_4
    voice audio.yuri_v_response2b1
    yu "She didn’t even DO anything! All she did was make a crappy schedule and then agree to go back to the one you made, Dad."

    show goro2 think4 at p7_5
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

    hide goro2_autumn
    hide goro2 think4
    show goro_autumn at p7_5
    show goro annoy3 at p7_5
    hide yuri_autumn
    hide yuri rage1
    show yuri_autumn at p7_4
    show yuri rage1 at p7_4
    voice audio.goro_v_scold1a1
    g "Calm down, Yuri… I don’t think we have to take everything she said so personally."
    g "We don’t need to like her, but Mr. Clermont assigned her here for a reason. We have to trust his judgement."

    hide yoshi2_autumn
    hide yoshi2 upset6
    show yoshi_autumn at p7_7
    show yoshi talk1 at p7_7
    voice audio.yoshi_v_guys3
    yo "Let’s give her the benefit of the doubt for now. We know at the very least that we all have the same common goal."

    show yuri annoy2 at p7_4
    voice audio.yuri_v_unsure1b3
    yu "I don’t know about you guys, but I have a really bad gut feeling about that Emilia. "

    show goro talk1 at p7_5
    voice audio.goro_v_comp1c1
    g "I understand your concerns, Yuri. But we have to work together for now and stay professional, especially since she was sent directly by our sponsor."

    show yuri pout1 at p7_4
    voice audio.yuri_v_agree5a3
    yu "Ugh… Fine. I’ll try to not to stoop down to her level, and I’ll prove we can do our job."

    show goro explain2 at p7_5
    voice audio.goro_v_rush3a1
    g "Come with me to the office and let’s calm your nerves a bit with some tea."

    show yuri angry6 at p7_4
    voice audio.yuri_v_sigh2a
    yu "*sigh* Okay, dad."

    hide yuri_autumn
    hide goro_autumn
    hide yuri angry6
    hide goro explain2
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

    show jin sleepy3 at p7_3
    voice audio.jin_v_bye1a3
    j "I guess I’ll go ahead as well… With all these new deadlines, I might need to get some more work done before bed…"

    hide jin_autumn
    hide jin sleepy3
    hide jin_glasses
    with dissolve


    show yoshi_autumn at right2
    show yoshi talk1 at right2
    show aiden2_autumn2 at left2
    show aiden2 worry2 at left2
    with move

    hide yoshi_autumn
    hide yoshi talk1
    show yoshi2_autumn at right2
    show yoshi2 talk1 at right2
    voice audio.aiden_v_confused2b1
    a "Things are really starting to change around here, huh Yoshi?"

    show yoshi2 shy5 at right2
    voice audio.yoshi_v_laugh1
    yo "Haha, yeah…"

    show aiden2 awkward6 at left2
    voice audio.aiden_v_unsure7a
    a "Are you sure you’re really alright with working with me? It must’ve been awkward having that talk with Emilia."

    hide yoshi2_autumn
    hide yoshi2 shy5
    show yoshi_autumn at right2
    show yoshi comp2 at right2
    voice audio.yoshi_v_comp4
    yo "Don’t worry about it, Aiden. Like I said yesterday, I’m really looking forward to working with you for the rest of the project."
    yo "Are you worried about all the assignments you’ve been given?"

    show aiden2 comp6 at left2
    voice audio.aiden_v_laugh1b1
    a "Ahehe… You knew exactly what I’m thinking, huh?"
    a "But yeah, I kinda took a peek inside those stacks of papers while you were gone, and she’s added a bunch of extra maintenance tasks on top of all my other work…"

    show aiden2 upset6 at left2
    voice audio.aiden_v_sigh1a
    a "She wants me to clean up after the construction workers at the site every day, and write these super detailed reports that I don’t even know how to do…"
    a "It’s just… a lot of expectations for someone like me."

    $working = False
    $shuffle_menu()
    menu():
        a "It’s just… a lot of expectations for someone like me.{fast}"
        "Don't doubt yourself.":
            $working = True
            $score_aiden -= 1
            $score_bot += 1
            show yoshi comp3 at right2
            voice audio.yoshi_v_comp2
            yo "Don’t doubt yourself, Aiden."
            yo "We rely on you a lot more than you think!"

            show aiden2 worry5 at left2
            voice audio.aiden_v_well1c1
            a "W-Well, that’s kinda what I’m afraid of. "
            a "I’m so used to doing simple chores, and I really have no idea how to do the ‘management’ stuff."

            show yoshi bold2 at right2
            voice audio.yoshi_v_comp5
            yo "Don’t worry, Aiden! I’ll lead the way, and you follow!"

            hide aiden2_autumn2
            hide aiden2 worry5
            show aiden_autumn at left2
            show aiden comp3 at left2
            voice audio.aiden_v_encourage2a
            a "I’ll try my best then! I’m counting on you, Yoshi…!"
        "I'll cover for you.":
            $working = True
            $score_aiden -= 1
            $score_top += 1
            show yoshi comp3 at right2
            voice audio.yoshi_v_confident2
            yo "I’ll cover for you, Aiden! "

            show aiden2 worry5 at left2
            voice audio.aiden_v_actually3a
            a "That’s kinda what I feel guilty about…"
            a "I’m so used to doing simple chores, and I really have no idea how to do the ‘management’ stuff."

            show yoshi bold2 at right2
            voice audio.yoshi_v_comp5
            yo "Don’t worry, Aiden! I’ll lead the way, and you follow!"

            hide aiden2_autumn2
            hide aiden2 worry5
            show aiden_autumn at left2
            show aiden comp3 at left2
            voice audio.aiden_v_encourage2a
            a "I’ll try my best then! I’m counting on you, Yoshi…!"
        "I know you can do it.":
            $working = True
            $score_aiden += 1
            $score_bot += 1
            show yoshi comp3 at right2
            voice audio.yoshi_v_encourage1
            yo "I know you can do it, Aiden!"
            yo "Especially since we’re gonna have each other backs!"

            show aiden2 comp3 at left2
            voice audio.aiden_v_conj1
            a "Besides, I’m a lot more used to doing simple chores, so I’m really glad you got the ‘management’ stuff covered!"

            show yoshi bold2 at right2
            voice audio.yoshi_v_confident1
            yo "Yeah! You can count on me, Aiden!"

            hide aiden2_autumn2
            hide aiden2 comp3
            show aiden_autumn at left2
            show aiden bold2 at left2
            voice audio.aiden_v_encourage2a
            a "You lead the way and I’ll follow!"
        "That's what I'm here for.":
            $working = True
            $score_aiden += 1
            $score_top += 1
            show yoshi comp3 at right2
            voice audio.yoshi_v_comp5
            yo "That’s what I’m here for, Aiden!"
            yo "If I’m always around, I’m sure we can work things out!"

            show aiden2 comp3 at left2
            voice audio.aiden_v_conj1
            a "Besides, I’m a lot more used to doing simple chores, so I’m really glad you got the ‘management’ stuff covered!"

            show yoshi bold2 at right2
            voice audio.yoshi_v_confident1
            yo "Yeah! You can count on me, Aiden!"

            hide aiden2_autumn2
            hide aiden2 comp3
            show aiden_autumn at left2
            show aiden bold2 at left2
            voice audio.aiden_v_encourage2a
            a "You lead the way and I’ll follow!"

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
    show mtga1 at fx_pos
    with fade
    play music buddy_oath_casual loop

    voice audio.yoshi_vsa6_line1
    yo "For the next few weeks, Aiden and I worked side by side on our tasks."

    voice audio.yoshi_vsa6_line2
    yo "I had been assigned to manage the construction team, while Aiden handled staff welfare and overall camp maintenance."

    scene bg_site3_autumn_sunset
    $ day = "21"
    $location = location_site
    $time = timeline_timesunset
    show mtga2 at fx_pos
    with Dissolve(0.25)
    voice audio.yoshi_vsa6_line3
    yo "With Emilia pushing a tight schedule, the construction moved forward at a very fast pace."

    voice audio.yoshi_vsa6_line4
    yo "Aiden and I didn’t hesitate to get our hands dirty, and we both learned a bunch of new things about construction from Darius and Lloyd."

    voice audio.yoshi_vsa6_line5
    yo "Everyone worked extra hard to meet the deadlines and we managed to accomplish every target Emilia set for us."

    voice audio.yoshi_vsa6_line6
    yo "Seeing the frameworks of the new cabins at the expansion site, we could already imagine how different the camp was going to look."

    scene bg_quarters_autumn_night
    $ day = "26"
    $location = location_quarters
    $time = timeline_timeday
    show mtga3 at fx_pos
    with Dissolve(0.25)
    voice audio.yoshi_vsa6_line7
    yo "While we were busy with our tasks, Jin spent many sleepless nights working on the technological goals of the project."

    voice audio.yoshi_vsa6_line8
    yo "He relaunched our website, and included online enrollments and job applications."

    voice audio.yoshi_vsa6_line9
    yo "From what he explained, he also secured an internet connection and a security system for the camp."

    scene bg_office_autumn_night
    $ day = "37"
    $location = location_office
    $time = timeline_timenight
    show mtga4 at fx_pos
    with Dissolve(0.25)
    voice audio.yoshi_vsa6_line10
    yo "Meanwhile, Sir Goro was swamped with legal work regarding the sponsorship, as usual. "

    voice audio.yoshi_vsa6_line11
    yo "Between that and processing all the new applications from the brand-new website, there was more work than ever."

    voice audio.yoshi_vsa6_line12
    yo "Thankfully, because Aiden and I were handling the construction team, Yuri was able to focus on assisting Sir Goro."

    voice audio.yoshi_vsa6_line13
    yo "Together they managed the project’s documentation, and each report sent to Emilia validated each department’s progress. "

    scene bg_site3_autumn_sunset
    $ day = "41"
    $location = location_site
    $time = timeline_timesunset
    show mtga5 at fx_pos
    with Dissolve(0.25)
    voice audio.yoshi_vsa6_line14
    yo "On top of our other responsibilities, Aiden and I made sure that the camp was well-maintained and that the staff was properly cared for."

    scene bg_outshed_autumn_day
    $ day = "43"
    $location = location_shed
    $time = timeline_timeday
    show mtga6 at fx_pos
    with Dissolve(0.25)
    voice audio.yoshi_vsa6_line15
    yo "Almost all of our time was spent working, but I made sure to take advantage of our shared tasks and spend plenty of quality time with him."

    scene bg_bathroom_autumn_night
    $ day = "46"
    $location = location_bathroom
    $time = timeline_timenight
    show mtga7 at fx_pos
    with Dissolve(0.25)
    voice audio.yoshi_vsa6_line16
    yo "We received many critiques from Emilia’s inspections, and she grew more and more frustrated. "

    voice audio.yoshi_vsa6_line17
    yo "I could see Aiden beginning to rethink his role at the camp from all the criticisms, and all I could do was try to have his back and reassure him."

    scene bg_kitchen_autumn_sunset
    $ day = "61"
    $location = location_kitchen
    $time = timeline_timesunset
    show mtga8 at fx_pos
    with Dissolve(0.25)
    voice audio.yoshi_vsa6_line17_2
    yo "As much as the work was physically exhausting, he kept smiling through everything, and it really encouraged me to keep doing my best."

    scene bg_messhall_autumn_night
    $ day = "65"
    $location = location_messhall
    $time = timeline_timenight
    show mtga9 at fx_pos
    with Dissolve(0.25)
    voice audio.yoshi_vsa6_line18
    yo "Seeing Aiden happy with my company made it all worth it."

    hide screen location
    hide screen timeline
    scene cg black
    with fade
    voice audio.yoshi_vsa6_line19
    yo "{i}Before we knew it, a month and a half had gone by, and the season was about to change again…{/i}"

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    play sound sleeping_time
    $ time_transition_night_to_day_fall()
    $ renpy.pause (2.0, hard=True)
    jump day2_aiden
