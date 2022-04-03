label day7_goro:
    $ day = "82"
    $ time = timeline_timeday
    $ location = location_cabin
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    $ working = True

    scene bg_quarters_winter_day with fade
    play music brand_new_day_winter loop
    play bgsound sfxloop_birds loop

    show darius_sleep at p5_1
    show darius norm3 at p5_1
    show lloyd_sleep at p5_2
    show lloyd norm1 at p5_2
    show jin_sleep at p5_3
    show jin_glasses at p5_3
    show jin norm1 at p5_3
    show aiden_sleep at p5_4
    show aiden norm1 at p5_4
    show goro_sleep at p5_5
    show goro tired3 at p5_5
    voice audio.goro_v_yawn1a
    g "*yawn* Good morning. You’re all up earlier than usual."

    show aiden happy2 at p5_4
    voice audio.aiden_v_goodam1a1
    a "G’morning, Gramps!  "
    a "I figured you’d be up soon, so I went ahead and made you some coffee!"

    show goro happy2 at p5_5
    voice audio.goro_v_thanks2a1
    g "Ah, thanks Aiden. "

    show darius happy1 at p5_1
    voice audio.darius_v_rush1
    d "Come chill with us for a bit, sir."

    show goro confused2 at p5_5
    voice audio.goro_v_think3
    g "What are you guys up to?"

    show aiden excited3 at p5_4
    voice audio.aiden_v_oh3a
    a "Ooh, Lloyd is doing some of his magic mumbo-jumbo again! This time he’s reading our palms!"

    show jin confuseddn3 at p5_3
    voice audio.jin_v_conj1c2
    j "N-Not gonna lie, this is probably the longest time a guy has held my hand."

    hide goro_sleep
    hide goro confused2
    show goro2_sleep at p5_5
    show goro2 think5 at p5_5
    voice audio.goro_v_think1a1
    g "Hmm, you have quite a lot of interesting hobbies, Lloyd."

    show lloyd relief3 at p5_2
    voice audio.lloyd_v_gratitude2b1
    l "Why, thank you, sir~ But I’ll admit I only know the basics of palm-reading."

    hide aiden_sleep
    hide aiden excited3
    show aiden2_sleep at p5_4
    show aiden2 comp6 at p5_4
    voice audio.aiden_v_laugh1b1
    a "Hehe, first it was the stars-thingy, then the spooky cards, and now this…"

    show lloyd annoy2 at p5_2
    voice audio.lloyd_v_greet2b1
    l "Heeey… You gotta admit they’re nice ice-breakers!"

    hide goro2_sleep
    hide goro2 think5
    show goro_sleep at p5_5
    show goro confused3 at p5_5
    voice audio.goro_v_really2a
    g "You’ve piqued my interest either way… how does it work…?"

    show jin_sleep at p5_2
    show jin_glasses at p5_2
    show jin norm1 at p5_2
    show aiden2_sleep at p5_3
    show aiden2 norm1 at p5_3
    show lloyd_sleep at p5_4
    show lloyd happy2 at p5_4
    with move

    voice audio.lloyd_v_conj1a3
    l "Well, you just look at someone’s hand like this and analyze specific creases!"

    show goro talk3 at p5_5
    voice audio.goro_v_oh3a
    g "What does mine say?"

    show lloyd think2 at p5_4
    voice audio.lloyd_v_think1a1
    l "Hmm… you seem to have a broken heart line..."

    show aiden2 worry3 at p5_3
    voice audio.aiden_v_oops2b
    a "Broken heart?! Wow, Lloyd you didn’t have to call out Gramps’ marriage like that."

    show lloyd shock6 at p5_4
    voice audio.lloyd_v_disagree1d1
    l "N-No! A heart line is located above the head line, and is the highest horizontal one on the palm!"

    show jin worry4 at p5_2
    voice audio.jin_v_hngh1a
    j "Hnghh… So many lines…"

    show lloyd happy2 at p5_4
    voice audio.lloyd_v_conj3a2
    l "Sir Goro’s heart line is only broken for the first third, though! The rest is continuously long and even has a fork at the end!"

    hide goro_sleep
    hide goro talk3
    show goro2_sleep at p5_5
    show goro2 confused2 at p5_5
    voice audio.goro_v_confused1a1
    g "And that means…?"

    show lloyd explain3 at p5_4
    voice audio.lloyd_v_conj6a1
    l "It reflects upheavals at the early stages of your romantic life, but in the latter part it shows a promising partnership that will last for a lifetime!"
    l "The fork, however, indicates the willingness to sacrifice everything for love!"

    hide aiden2_sleep
    hide aiden2 worry3
    show aiden_sleep at p5_3
    show aiden shock2 at p5_3
    voice audio.aiden_v_shock1d1
    a "Whoa… Why is Gramps’ fortune all about romance?"

    show jin confused5 at p5_2
    voice audio.jin_v_yeah2a
    j "Yeah… It seems so out of character…"

    show darius play2 at p5_1
    voice audio.darius_v_comp3a
    d "Lloyd is just doing it for fun. Don’t take it seriously."
    d "Listening to his magic first thing in the morning is entertaining with hot cocoa."

    show lloyd angry2 at p5_4
    voice audio.lloyd_v_greet2b1
    l "Heyyy! There are plenty of studies that talk about these mystic energies! It could be real!"

    show darius relief2 at p5_1
    voice audio.darius_v_agree1a
    d "Yes, I believe you."

    show lloyd disappoint2 at p5_4
    voice audio.lloyd_v_ignored1a1
    l "Like I said, I’m just using it as an ice-breaker!"

    hide goro2_sleep
    hide goro2 confused2
    show goro_sleep at p5_5
    show goro talk4 at p5_5
    voice audio.goro_v_conj7a
    g "Speaking of breaking ice, did Yoshinori already go to the site to work? I don’t see him."

    show aiden talk3 at p5_3
    voice audio.aiden_v_oh2a
    a "Oh, he left not long before you got up. I’m not sure what for though…"

    show jin think5 at p5_2
    voice audio.jin_v_think1a1
    j "He did seem to be in a hurry… He didn’t even drink his coffee… "

    show aiden confused2 at p5_3
    voice audio.aiden_v_actually1a
    a "Actually, that reminds me – since when have you had a normal person schedule, Jin?!"

    show jin comp3 at p5_2
    voice audio.jin_v_ah2a
    j "A-Ahh... Yeah… It’s still been kind of difficult, but ever since I started taking Sir Goro’s advice and drinking my morning coffee, it’s helped a lot."

    show goro relief2 at p5_5
    voice audio.goro_v_relief1a
    g "I can’t work well without it, so I thought it’d give you a boost too."

    show lloyd talk2 at p5_4
    voice audio.lloyd_v_sus1a1
    l "It’s crazy to me that you’re drinking yours iced, considering how cold it is outside, Jin! You sure are tougher than you look."

    show jin confuseddn2 at p5_2
    voice audio.jin_v_think2a1
    j "I believe drinking scalding black coffee alone with no cream or sugar like Sir Goro is a lot more concerning… "

    hide goro_sleep
    hide goro relief2
    show goro2_sleep at p5_5
    show goro2 explain4 at p5_5
    voice audio.goro_v_ehem1a
    g "*ehem* I prefer it this way. "

    show aiden tired1 at p5_3
    voice audio.aiden_v_anyway1a
    a "Either way, we’re all gonna need the energy! I assume we’ll be clearing out snow till we can’t feel our fingers again."

    show jin sleepy3 at p5_2
    voice audio.jin_v_hngh1a
    j "Ugh…"

    show lloyd comp2 at p5_4
    voice audio.lloyd_v_comp1a1
    l "Don’t worry, Jin! It’s gonna be a good morning exercise after all! "
    l "Just think of it as part of your road to being physically fit! Physically fit, fit, fit!"

    show darius tease2 at p5_1
    voice audio.darius_v_laugh2a
    d "Hehe… Seems like the coffee’s kicking in for Lloyd."

    hide goro2_sleep
    hide goro2 explain4
    show goro_sleep at p5_5
    show goro talk1 at p5_5
    voice audio.goro_v_conj7a
    g "On that note, I guess we should get dressed and start our day as well. "

    show aiden happy1 at p5_3
    voice audio.aiden_v_laugh2a1
    a "Yeah, we can’t let Yoshi finish everything up without us, haha!"

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
    scene bg_campgrounds_winter_day with fade
    play music sunset_stroll_winter loop

    show darius_winter2 at p5_1
    show darius norm1 at p5_1
    show lloyd_winter2 at p5_2
    show lloyd happy1 at p5_2
    show jin_winter at p5_3
    show jin_glasses at p5_3
    show jin norm1 at p5_3
    show goro_winter2 at p5_4
    show goro norm1 at p5_4
    show aiden_winter2 at p5_5
    show aiden norm1 at p5_5
    voice audio.lloyd_v_shock1a3
    l "Oh! Yoshi’s over there by the arch! And it looks like he’s with some people!"

    show goro confused2 at p5_4
    voice audio.goro_v_confused1a1
    g "Huh? Do we have visitors?"

    show aiden shock2 at p5_5
    voice audio.aiden_v_wait2b1
    a "Hold on… Isn’t that—"

    hide darius_winter2
    hide darius norm1
    hide lloyd_winter2
    hide lloyd happy1
    hide jin_winter
    hide jin_glasses
    hide jin norm1
    hide goro_winter2
    hide goro norm1
    hide aiden_winter2
    hide aiden shock2
    with dissolve

    show yoshi_winter2 at p7_1
    show yoshi happy1 at p7_1
    show keitaro_winter2 at p7_2
    show keitaro normal1 at p7_2
    show hiro_winter2 at p7_3
    show hiro normal1 at p7_3
    show yoichi_winter at p7_4
    show yoichi normal1 at p7_4
    show natsumi_winter at p7_5
    show natsumi normal1 at p7_5
    show hunter_winter2 at p7_6
    show hunter smile1 at p7_6
    show taiga_winter at p7_7
    show taiga normal3 at p7_7
    with dissolve

    voice audio.yoshi_v_ah1
    yo "Ah! Perfect timing! There they are!"

    show yoshi_winter2 at p9_3
    show yoshi happy1 at p9_3
    show keitaro_winter2 at p9_4
    show keitaro normal1 at p9_4
    show hiro_winter2 at p9_5
    show hiro normal1 at p9_5
    show yoichi_winter at p9_6
    show yoichi normal1 at p9_6
    show natsumi_winter at p9_7
    show natsumi normal1 at p9_7
    show hunter_winter2 at p9_8
    show hunter smile1 at p9_8
    show taiga_winter at p9_9
    show taiga normal3 at p9_9
    with move

    show goro_winter2 at p9_1
    show goro norm1 at p9_1
    show aiden_winter2 at p9_2
    show aiden excited3 at p9_2
    with dissolve

    voice audio.aiden_v_shock1a1
    a "Whoa! I can’t believe it!"

    show keitaro talking1 at p9_4
    voice audio.keitaro_v_greeting2
    k "Hello, Sir Aiden and Sir Goro!"

    show goro happy3 at p9_1
    voice audio.goro_v_goodam1a1
    g "Ah, welcome scouts! I wasn’t expecting a visit from all of you."

    show hunter talking1 at p9_8
    voice audio.hunter_v_apology1a
    hu "We’re sorry for coming at such short notice!"

    show aiden_winter2 at p9_4
    show aiden excited3 at p9_4
    show keitaro_winter2 at p9_3
    show keitaro talking1 at p9_3
    show yoshi_winter2 at p9_2
    show yoshi happy1 at p9_2
    with move

    show hiro laugh1 at p9_5
    voice audio.hiro_v_bro1b
    hi "Hey, bro! Long time, no see!"

    show aiden amazed2 at p9_4
    voice audio.aiden_v_aww2a
    a "Wah, I just realized how much I missed you all! Hahaha!"
    a "Yoshi! How come you didn’t tell us that the gang was coming over today?! "

    show yoshi comp6 at p9_2
    voice audio.yoshi_v_well3
    yo "W-Well, I figured it would be better as a surprise."

    show goro happy2 at p9_1
    voice audio.goro_v_so1a
    g "So, what brings you boys back here?"

    show natsumi excited1 at p9_7
    voice audio.natsumi_v_reportingforduty1
    n "We’re reporting for duty, sir!"

    show taiga talking4 at p9_9
    voice audio.taiga_v_agree1a
    t "Yeah, we’re here to help you guys clear out the snow."

    show yoichi playful1 at p9_6
    voice audio.yoichi_v_agree3a3
    yi "Heh~ I ain’t gonna miss the chance to flex my muscles!"
    yi "Besides, the pups were tired of being cooped up indoors, so I thought they could run around here for a while. "

    show goro comp5 at p9_1
    voice audio.goro_v_comp2a1
    g "It’ll get very cold in the evenings so everyone, including the pups, can stay in the cabins for the night. "
    g "I assume you’re the one who informed the scouts of our situation, Yoshinori?"

    show yoshi happy1 at p9_2
    voice audio.yoshi_v_yeah2
    yo "Yeah. I figured we could really use the extra hands to get things done, so I called Yoichi and Taiga yesterday."

    show natsumi talking1 at p9_7
    voice audio.natsumi_v_conjunction2
    n "Everyone’s been at Keitaro’s place since the snowstorm, and we wanted to come over when we heard the camp needed help! "

    show hiro annoyed2 at p9_5
    voice audio.hiro_v_yoichi6d
    hi "Stupid Wolfboy didn’t know how to use my phone and put Scoutmaster Yoshi on loudspeaker."

    show yoichi angry1 at p9_6
    voice audio.yoichi_v_greet1c1
    yi "Hey! You should be thanking me, Torch-head! You’re the one who wanted to come back here the most!"

    show yoshi laugh2 at p9_2
    voice audio.yoshi_v_laugh3
    yo "Hehe, I figured it would be a lot more fun if everyone came along, so I invited them too!"

    show aiden play2 at p9_4
    voice audio.aiden_v_laugh1b2
    a "Hehe~ You sure it’s not just an excuse to see the scouts again, Yoshi?"

    show goro confused3 at p9_1
    voice audio.goro_v_unsure1a2
    g "Are you boys sure it’s alright to spend the day working here, though? You aren’t skipping your studies, are you?"

    show hiro talking3 at p9_5
    voice audio.hiro_v_disagree2b1
    hi "Nah. Classes got cancelled thanks to the weather, so we’ve been stuck at home for days now!"

    show yoichi angry3 at p9_6
    voice audio.yoichi_v_bored1a
    yi "It was getting boring with these dorks too; all we do is just sit around and play stupid video games. "

    show taiga playful2 at p9_9
    voice audio.taiga_v_heh1
    t "Heh, just tell them you just suck at it."

    show yoichi awkward2 at p9_6
    voice audio.yoichi_v_request1c1
    yi "Sh-Shut up!"

    show keitaro compassion3 at p9_3
    voice audio.keitaro_v_dontworry1
    k "Don’t worry, Sir Goro! We’re really excited to be back! A buddy is always ready to help, after all!"

    show taiga worry1 at p9_9
    voice audio.taiga_v_sigh1
    t "I hope this many people is enough, though. I tried inviting Eduard and Lee, but they’re both busy today."

    show hunter thinking2 at p9_8
    voice audio.hunter_v_thinking1
    hu "I called Felix and Seto too, but they’re away on a vacation, sadly."

    show yoshi comp3 at p9_2
    voice audio.yoshi_v_comp2
    yo "It’s alright! You guys are a huge help already! "

    show goro sigh1 at p9_1
    voice audio.goro_v_sigh1a
    g "It’s a bit of a shame you boys have to see the camp in this state."

    show hunter amazed1 at p9_8
    voice audio.hunter_v_amazed1
    hu "I think the snow cover is really pretty, though..."

    show taiga playful2 at p9_9
    voice audio.taiga_v_laugh1a
    t "Hehe, don’t forget we’re here to get rid of it."

    show natsumi excited1 at p9_7
    voice audio.natsumi_v_excited1
    n "I’ve heard there’s plenty of new stuff being developed for the next term! It makes me excited to come back next summer!"

    show keitaro laugh1 at p9_3
    voice audio.keitaro_v_laugh2
    k "I guess we’re getting an exclusive sneak peek, then! "

    show hunter thinking2 at p9_8
    voice audio.hunter_v_conjunction2a
    hu "That’s not the only new thing I see though… I see some unfamiliar faces as well…"

    show taiga talking1 at p9_9
    voice audio.taiga2_v_surprised1c
    t "Oh yeah, you guys haven’t met the new crew! "

    show natsumi thinking1 at p9_7
    voice audio.natsumi_v_oh1
    n "Yoichi did mention there were new people working for the project."

    show yoshi talk3 at p9_2
    voice audio.yoshi_v_agree1b2
    yo "Ah, of course! Sorry for not introducing them right away, I got caught up with the reunion!"

    show goro_winter2 at p12_1
    show goro sigh1 at p12_1
    show aiden_winter2 at p12_5
    show aiden play2 at p12_5
    show yoshi_winter2 at p12_6
    show yoshi talk3 at p12_6
    show keitaro_winter2 at p12_7
    show keitaro laugh1 at p12_7
    show hiro_winter2 at p12_8
    show hiro talking3 at p12_8
    show yoichi_winter at p12_9
    show yoichi awkward2 at p12_9
    show natsumi_winter at p12_10
    show natsumi thinking1 at p12_10
    show hunter_winter2 at p12_11
    show hunter thinking2 at p12_11
    show taiga_winter at p12_12
    show taiga talking1 at p12_12
    with move

    show darius_winter2 at p12_3
    show darius norm1 at p12_3
    show lloyd_winter2 at p12_2
    show lloyd happy1 at p12_2
    show jin_winter at p12_4
    show jin_glasses at p12_4
    show jin norm1 at p12_4
    with dissolve

    show goro_winter2 at p12_1
    show goro sigh1 at p12_1
    show lloyd_winter2 at p12_2
    show lloyd happy1 at p12_2
    show darius_winter2 at p12_3
    show darius norm1 at p12_3
    show jin_winter at p12_4
    show jin_glasses at p12_4
    show jin norm1 at p12_4
    show aiden_winter2 at p12_5
    show aiden play2 at p12_5
    show yoshi_winter2 at p12_6
    show yoshi happy1 at p12_6
    show keitaro_winter2 at p12_7
    show keitaro laugh1 at p12_7
    show hiro_winter2 at p12_8
    show hiro talking3 at p12_8
    show yoichi_winter at p12_9
    show yoichi awkward2 at p12_9
    show natsumi_winter at p12_10
    show natsumi thinking1 at p12_10
    show hunter_winter2 at p12_11
    show hunter thinking2 at p12_11
    show taiga_winter at p12_12
    show taiga thinking1 at p12_12
    with move

    voice audio.yoshi_v_guys1
    yo "Everyone, these are the new developers that Mr. Clermont hired to help with the expansion project!"

    show yoshi happy2 at p12_6
    voice audio.yoshi_v_jin2
    yo "This is Hyunjin, he’s in charge of the technology department!"

    show hiro amazed1 at p12_8
    voice audio.hiro_v_amazed1c3
    hi "Wow! Camp Buddy is gonna be high-tech?!"

    show jin comp3 at p12_4
    voice audio.jin_v_no2a
    j "N-Not necessarily, I’m just here to make things easier on the management with some modern adjustments."
    j "Like for example, I’ve updated the camp’s website to allow online enrollment and developed a database for all important camp records."

    show aiden happy2 at p12_5
    voice audio.aiden_v_yeah1a2
    a "Yeah, we don’t have to read through tons and tons of application forms like we did last term!"

    show keitaro amazed1 at p12_7
    voice audio.keitaro_v_amazed1
    k "Wow, that sounds like a huge upgrade! "

    show goro comp3 at p12_1
    voice audio.goro_v_jin2a
    g "Jin has quite a few more upgrades he’s working on as well, but I was relieved to see that none of them would disrupt the spirit of the camp."

    show yoshi bold5 at p12_6
    voice audio.yoshi_v_anyway1a
    yo "These two are Lloyd and Darius. They’re in charge of designing and building all the new facilities."

    show lloyd bold3 at p12_2
    voice audio.lloyd_v_laugh1a1
    l "Mr. Sirius! Master Architect! "

    show darius happy1 at p12_3
    voice audio.darius_v_greet2
    d "I’m Dar, lead foreman. I build stuff."

    show yoichi playful1 at p12_9
    voice audio.yoichi_v_lloyd5c
    yi "Don’t mistake pipsqueak here for a scout like I did, he’s actually twice our age."

    show lloyd rage3 at p12_2
    voice audio.lloyd_v_question1c3
    l "P-Pipsqueak!?"

    show darius laugh3 at p12_3
    voice audio.darius_v_laugh2a
    d "Hehe… I like that nickname."

    show hunter_winter2 at p12_11
    show hunter amazed1 at p12_11
    voice audio.hunter_v_amazed1
    hu "Wow, an architect and a construction foreman… That sounds so official."

    show taiga talking4 at p12_12
    voice audio.taiga2_v_agree3a
    t "Oh, they’re the real deal. I’ve already learned a thing or two about design and carpentry from them."

    show darius comp2 at p12_3
    voice audio.darius_v_taiga1
    d "You’re very crafty, Taiga."

    show yoshi happy1 at p12_6
    voice audio.yoshi_v_conj5a
    yo "We have a team of construction workers too, but they’re on leave for a couple more days."

    show hunter confused3 at p12_11
    voice audio.hunter_v_confused1
    hu "Aren’t we missing someone…? I haven’t seen Ms. Yuri around."

    show yoshi talk3 at p12_6
    voice audio.yoshi_v_oh1
    yo "Oh, she’s still at the cabin! She’s been taking care of one of our other crew. You guys will meet them later, as soon as they’re ready!"

    show hunter confused1 at p12_11
    voice audio.hunter_v_compassion2a
    hu "I see…"

    show natsumi talking1 at p12_10
    voice audio.natsumi_v_laugh1
    n "It’s so interesting to see everyone not wearing our uniforms for once! I think our scoutmasters look really ‘cool’!"

    show yoichi annoyed6 at p12_9
    voice audio.yoichi_v_tease1c
    yi "Suck up."

    show natsumi playful2 at p12_10
    voice audio.natsumi_v_yoichi4
    n "You don’t get it, Yoichi? Cool! Cause it’s cold!"

    show yoichi angry1 at p12_9
    voice audio.yoichi_v_lame1a
    yi "No one cares! That is so freaking lame!!"

    hide goro_winter2
    hide goro comp3
    show goro2_winter2 at p12_1
    show goro2 explain1 at p12_1
    hide lloyd_winter2
    hide lloyd rage3
    show lloyd_winter2 at p12_2
    show lloyd rage3 at p12_2
    voice audio.goro_v_ehem1a
    g "*ehem* Anyway, thank you all for volunteering to help. We were a bit worried about the lack of manpower yesterday."

    hide goro2_winter2
    hide goro2 explain1
    show goro_winter2 at p12_1
    show goro comp2 at p12_1
    hide lloyd_winter2
    hide lloyd rage3
    show lloyd_winter2 at p12_2
    show lloyd rage3 at p12_2
    voice audio.goro_v_thanks2a1
    g "You’ve all already done so much for the camp during your term that it feels a bit embarrassing to ask for more, but I’m grateful nonetheless. "

    show keitaro laugh2 at p12_7
    voice audio.keitaro_v_compassion11
    k "It’s our pleasure, Sir Goro! We’re just excited to be back here before the next summer term! We’ve all missed it!"
    k "I know it’s only been a few months, but I could hardly wait to see everyone again!"

    show yoshi comp2 at p12_6
    voice audio.yoshi_v_aww1
    yo "You boys are the best scouts a scoutmaster could ask for!"
    yo "In all my years here, I’ve never seen a group of scouts that have the same sense of unity and camaraderie that you have for each other and the camp!"

    show yoshi relief2 at p12_6
    voice audio.yoshi_v_praise1
    yo "It’s such an honor to know that you’re a true testament to what this place stands for!"

    show taiga sigh2 at p12_12
    voice audio.taiga_v_sigh1
    t "*sigh* Bet you guys didn’t miss the speeches…"

    show yoshi bold2 at p12_6
    voice audio.yoshi_v_encourage3
    yo "All of you are truly living the ‘Buddy Oath’ to your core, just like a true scout!"
    yo "Like the second Buddy Law states, ‘Always help a buddy in need!’ And by volunteering to come here today, you’ve truly fulfilled—"

    show yoichi rage2 at p12_9
    voice audio.yoichi_v_aiden1a
    yi "BUTTCHEEKS! Do you have any food for us? I’m starving!"

    show natsumi angry2 at p12_10
    voice audio.natsumi_v_yoichi7
    n "Yoichi! We haven’t even started working yet…"

    show aiden bold3 at p12_5
    voice audio.aiden_v_confident1b
    a "Either way, I’m here to the save the day! Since today is turning out to be special, it’s only fair I cook something good too!"

    show hiro excited2 at p12_8
    voice audio.hiro_v_oh2b
    hi "Ooh, ooh! Can I help you out, bro?! I miss the kitchen here, it’s so much bigger than the one at home!"

    show yoichi angry1 at p12_9
    voice audio.yoichi_v_greet1c1
    yi "Hey! No avoiding chores, Torch-head!"

    show hiro pout2 at p12_8
    voice audio.hiro_v_shush1e
    hi "Shush, Wolfboy."

    show aiden comp3 at p12_5
    voice audio.aiden_v_hiro1a
    a "As happy as I am to have my little chef again, you can leave the kitchen work to me and spend fun time with everyone else!"

    show hiro compassion2 at p12_8
    voice audio.hiro_v_aww1c
    hi "Aww~ I missed being called ‘little chef’!"

    show aiden laugh1 at p12_5
    voice audio.aiden_v_alright1a3
    a "I’ll just call everyone when the food is ready!"

    show hiro sigh3 at p12_8
    voice audio.hiro_v_sigh1a
    hi "*sigh* Alright… I did promise to shovel today."

    show yoichi grin1 at p12_9
    voice audio.yoichi_v_agree3a2
    yi "Gimme those damn shovels and let’s get this over with! The more I shovel, the more food I’ll get!"

    show yoichi rage1 at p12_9
    voice audio.yoichi_v_angry2b1
    yi "GRAHHH!!! I’m pumped up!" with vpunch

    hide yoichi_winter
    hide yoichi rage1
    with dissolve

    show hunter compassion3 at p12_11
    voice audio.hunter_v_err1a
    hu "Does Yoichi realize that it doesn’t work that way…? We’ll get food regardless of how much we shovel…"

    show natsumi thinking1 at p12_10
    voice audio.natsumi_v_thinking3a
    n "I think it’s fine to let Yoichi do his thing. I mean, he’ll get a lot more work done this way."

    show taiga annoyed2 at p12_12
    voice audio.taiga_v_ugh1
    t "Am I gonna end up cleaning up after him again…? I bet he’ll just throw the snow at random places."

    show keitaro playful1 at p12_7
    voice audio.keitaro_v_scheming1a
    k "Hehe, by the looks of things, he’s doing just that."

    show hiro angry3 at p12_8
    voice audio.hiro_v_ugh2d
    hi "Ugh, he’s such a meathead."

    show jin confused2 at p12_4
    voice audio.jin_v_think2a1
    j "I-I don’t think he’s shoveling the right place either… The site’s way over there…"

    show taiga sigh2 at p12_12
    voice audio.taiga_v_sigh1
    t "*sigh* I’ll go tell him."

    hide taiga_winter
    hide taiga sigh2
    with dissolve

    show goro bold2 at p12_1
    voice audio.goro_v_anyway2
    g "Let’s make sure you boys are all properly geared up before we get to work."
    g "The snow boots should be in the shed. Come with me, scouts! "

    show keitaro talking1 at p12_7
    show natsumi talking1 at p12_10
    show hiro talking1 at p12_8
    show hunter talking1 at p12_11
    all "Yes, sir!"

    hide keitaro_winter2
    hide keitaro talking1
    hide hiro_winter2
    hide hiro talking1
    hide hunter_winter2
    hide hunter talking1
    hide natsumi_winter
    hide natsumi talking1
    hide goro_winter2
    hide goro bold2
    with dissolve

    show lloyd_winter2 at p5_1
    show lloyd bold3 at p5_1
    show darius_winter2 at p5_2
    show darius comp2 at p5_2
    show jin_winter at p5_3
    show jin_glasses at p5_3
    show jin comp3 at p5_3
    show yoshi_winter2 at p5_4
    show yoshi bold2 at p5_4
    show aiden_winter2 at p5_5
    show aiden laugh1 at p5_5
    with move

    j "What a lively bunch, aren’t they?"

    show aiden happy3 at p5_5
    voice audio.aiden_v_yeah2a2
    a "Oh yeah, they’re chaotic. But in a good way!"

    show yoshi laugh2 at p5_4
    voice audio.yoshi_v_laugh1
    yo "Hahaha, it looks like Sir Goro’s just as excited that the scouts are back and he just won’t admit it."
    yo "Just like how he was as a scoutmaster."

    show lloyd comp6 at p5_1
    voice audio.lloyd_v_aww1b3
    l "It feels really nostalgic… It reminds me of how we used to be back then."

    show darius comp5 at p5_2
    voice audio.darius_v_agree2a
    d "Yeah… I miss being a scout too."

    show jin worry2 at p5_3
    voice audio.jin_v_aww2a3
    j "Now I feel like I missed out. I never went to a summer camp in my younger days."

    show yoshi comp2 at p5_4
    voice audio.yoshi_v_comp5
    yo "Don’t worry, Jin! I’d say having you here working with us counts!"
    yo "We may be here at Camp Buddy for a different reason this time, but our experiences together will forever be a part of us, no matter where we are in life!"

    show yoshi comp5 at p5_4
    voice audio.yoshi_v_agree1b2
    yo "I know you guys have been successful with your careers, but know that Camp Buddy’s doors are always open to welcome you back!"

    show aiden comp3 at p5_5
    voice audio.aiden_v_yoshi5a
    a "Don’t get carried away with a speech again, Yoshi. Hahaha!"

    show jin comp3 at p5_3
    voice audio.jin_v_laugh1a
    j "Either way, that is very touching…"

    show lloyd happy2 at p5_1
    voice audio.lloyd_v_conj2a2
    l "Anyway, should we go start today’s shift? We don’t want the scouts doing all the work, right?"

    show darius bold2 at p5_2
    voice audio.darius_v_agree2a
    d "Yeah, I think that’s enough reunions for one day. We have a long day ahead."

    show aiden bold2 at p5_5
    voice audio.aiden_v_bye1a
    a "I’ll head to the kitchen and start cooking!"

    show yoshi happy2 at p5_4
    voice audio.yoshi_v_rush6
    yo "Let’s make this a productive day, everyone!"

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
    scene bg_site5_winter_day_semiclear with fade
    play music sunset_stroll_winter loop
    play bgsound sfxloop_snowshovel loop

    show yoshi_winter2 at center
    show yoshi happy1 at center
    voice audio.yoshi_v_alright2
    yo "Looks like everyone’s divided into groups and working hard already!"
    yo "With all the extra help, we’ll be done in no time!"

    voice audio.natsumi_v_yoichi7
    n "Using three shovels at the same time won’t make your work faster, Yoichi!"

    voice audio.yoichi_v_natsumi1a
    yi "I’ll make you eat your words, Mr. Perfect!"

    show yoshi_winter2 at p6_1
    show yoshi happy2 at p6_1
    with move

    show taiga_winter at p6_2
    show taiga sigh2 at p6_2
    show yoichi_winter at p6_3
    show yoichi normal1 at p6_3
    show natsumi_winter at p6_4
    show natsumi normal1 at p6_4
    show lloyd_winter2 at p6_5
    show lloyd norm2 at p6_5
    show darius_winter2 at p6_6
    show darius norm1 at p6_6
    with dissolve

    voice audio.yoshi_v_hey1
    yo "Hey there, guys! I hear Yoichi’s being a bit unruly again."

    show taiga sigh2 at p6_2
    voice audio.taiga_v_sigh1
    t "It’s nothing new honestly. At least he’s getting a lot done."

    show natsumi laugh1 at p6_4
    voice audio.natsumi_v_laugh2
    n "You know how Yoichi is, he has to make it fun in his own way!"

    show yoichi playful1 at p6_3
    voice audio.yoichi_v_agree1a1
    yi "Yeah, if we’re gonna get conned by these boomers into free labor, might as well make it entertaining, right?"

    show natsumi surprised3 at p6_4
    voice audio.natsumi_v_yoichi7
    n "Y-Yoichi…! D-Don’t listen to him, he’s being silly…!"

    show taiga compassion3 at p6_2
    voice audio.taiga_v_laugh1a
    t "Hehe, he’s got a point. "

    show lloyd think3 at p6_5
    voice audio.lloyd_v_think1a1
    l "Hmm, if I had to guess, based on your bold behavior, Yoichi – you’re either an Aries or an Aquarius!"

    show yoichi confused1 at p6_3
    voice audio.yoichi_v_question1a2
    yi "A what?! "

    show darius talk1 at p6_6
    voice audio.darius_v_laugh1
    d "He’s guessing your horoscope."

    show yoichi confused3 at p6_3
    voice audio.yoichi_v_confused1a1
    yi "Homoscope?! "

    show natsumi excited1 at p6_4
    voice audio.natsumi_v_oh1
    n "Oh! I’ve heard of that before, when I worked on my stargazing badge!"

    show yoichi annoyed4 at p6_3
    voice audio.yoichi_v_confused2a1
    yi "What is this mumbo jumbo?"

    show natsumi talking1 at p6_4
    voice audio.natsumi_v_conjunction2
    n "A horoscope is an ancient way to determine someone’s future, typically including a description of personalities or circumstances, based on the relative positions of the stars and planets at the time of that person's birth!"

    show taiga awkward3 at p6_2
    voice audio.taiga_v_confused1a
    t "You’re really a walking dictionary, huh Natsumi?"

    show lloyd excited1 at p6_5
    voice audio.lloyd_v_amazed1a1
    l "Wow, somebody has done their homework! "

    show yoshi laugh1 at p6_1
    voice audio.yoshi_v_actually1b
    yo "Haha, Natsumi is officially the best scout we have, and for three terms in a row now!"
    yo "In my entire time at the camp, nobody else has earned more badges than him!"

    show yoichi annoyed2 at p6_3
    voice audio.yoichi_v_lame1a
    yi "Pfft… Lame."

    show natsumi compassion1 at p6_4
    voice audio.natsumi_v_aww1
    n "Aww, Scoutmaster Yoshi! That’s really flattering!"

    show lloyd bold2 at p6_5
    voice audio.lloyd_v_horoscope1d
    l "With how professional and commanding you sound, I’m guessing you’re a Capricorn?"

    show natsumi grin1 at p6_4
    voice audio.natsumi_v_compassion6d
    n "Close, I’m a Gemini! "

    show lloyd disappoint2 at p6_5
    voice audio.lloyd_v_swear1a3
    l "Oh, drats! "

    show natsumi talking1 at p6_4
    voice audio.natsumi_v_but4
    n "You were right about Yoichi, though! He’s an Aquarius based on his birthday."
    n "Scoutmaster Yoshi is a Pisces and Taiga is a Cancer."

    show yoichi shock2 at p6_3
    voice audio.yoichi_v_question1c5
    yi "You called Dynamite a WHAT?!"

    show taiga angry5 at p6_2
    voice audio.taiga_v_dumbass1
    t "Dumbass, you’re thinking of a different cancer."

    show natsumi thinking1 at p6_4
    voice audio.natsumi_v_thinking3b
    n "I only know the signs according to the months, though. I’m really interested to know more about them!"

    show lloyd excited3 at p6_5
    voice audio.lloyd_v_confused1b1
    l "R-Really…?"

    show natsumi talking1 at p6_4
    voice audio.natsumi_v_agree8d
    n "Yeah! I think it’s cool! I’m sure Hunter would like it too!"

    show lloyd amazed4 at p6_5
    voice audio.lloyd_v_amazed3a1
    l "Y-You think… it’s COOL?! "

    show darius play2 at p6_6
    voice audio.darius_v_laugh2a
    d "You and Lloyd are gonna get along just fine."

    show lloyd amazed5 at p6_5
    voice audio.lloyd_v_amazed2a2
    l "We have GOT to have a mini divination session as soon we’re done today!"

    show darius laugh1 at p6_6
    voice audio.darius_v_cute1
    d "Hehe, isn’t he cute?"

    show lloyd pout4 at p6_5
    voice audio.lloyd_v_annoyed1a3
    l "Hmph… Are you trying to make fun of me, Dar?!"

    show yoshi laugh2 at p6_1
    voice audio.yoshi_v_lloyd3
    yo "It’s always been great to see you share your hobbies with us, Lloyd! This entire project wouldn’t be as fun without them."

    show yoichi playful3 at p6_3
    voice audio.yoichi_v_rush1a2
    yi "Well, my homoscope sense is telling ya’ll to hurry up and finish so we can eat!"

    show lloyd talk4 at p6_5
    voice audio.lloyd_v_shock1a3
    l "Oh right, sorry for the tangent."

    show natsumi excited1 at p6_4
    voice audio.natsumi_v_excited1
    n "I’ve got to hand it to you, Mr. Sirius! These new buildings are looking really cool so far! "

    show lloyd sigh1 at p6_5
    voice audio.lloyd_v_aww1a1
    l "It’s a shame that you guys have to see them worn down from the storm… "

    show taiga confused2 at p6_2
    voice audio.taiga_v_agree3a
    t "Yeah, I remember it looking a lot more polished before we left."

    show yoshi comp6 at p6_1
    voice audio.yoshi_v_comp2
    yo "It’s alright, things happen! We just have to make the best of it!"

    show natsumi laugh1 at p6_4
    voice audio.natsumi_v_laugh2
    n "Even still, I can already imagine how everything’s going to look!"

    show lloyd happy2 at p6_5
    voice audio.lloyd_v_darius1a
    l "I can’t take all the credit, though. Dar is the real MVP in making all my designs a reality."
    l "Not to mention our amazing construction team who does all the labor! "

    show darius happy1 at p6_6
    voice audio.darius_v_lloyd1
    d "Lloyd is really modest about these kinds of things."
    d "It was his incredible planning that let us build everything from the ground up. "

    show lloyd sigh5 at p6_5
    voice audio.lloyd_v_groan2a1
    l "More like tore it all down from being so unprepared for a freak storm…"

    show darius comp5 at p6_6
    voice audio.darius_v_aww1c1
    d "See? Modest."

    show lloyd talk1 at p6_5
    voice audio.lloyd_v_conj1a2
    l "Well, it’s not like I designed everything from scratch! I took most of the inspiration and even some plan layouts from the existing structures here!"

    show yoichi rage2 at p6_3
    voice audio.yoichi_v_greet1d1
    yi "HEY! If you guys would stop chit-chatting so much, you’d shovel a hell of a lot faster!"

    show yoshi talk3 at p6_1
    voice audio.yoshi_v_oh1
    yo "Oh, that reminds me, I should probably check on the other group too. There was quite a bit more snow over there…"
    yo "Are you all okay here if I leave for now?"

    show natsumi talking1 at p6_4
    voice audio.natsumi_v_response1
    n "No problem, Scoutmaster Yoshi! We’ll make sure Yoichi behaves!"

    hide darius_winter2
    hide lloyd_winter2
    hide darius comp5
    hide lloyd talk1
    hide natsumi_winter
    hide natsumi talking1
    hide yoichi_winter
    hide yoichi rage2
    hide taiga_winter
    hide taiga confused2
    with dissolve

    show yoshi_winter2 at center
    show yoshi explain2 at center
    with move

    voice audio.yoshi_v_think1a
    yo "Let’s see…"

    show yoshi_winter2 at p6_6
    show yoshi happy1 at p6_6
    with move

    show jin_winter at p6_1
    show jin_glasses at p6_1
    show jin norm1 at p6_1
    show hunter_winter2 at p6_2
    show hunter smile1 at p6_2
    show goro_winter2 at p6_3
    show goro norm1 at p6_3
    show hiro_winter2 at p6_4
    show hiro normal1 at p6_4
    show keitaro_winter2 at p6_5
    show keitaro normal1 at p6_5
    with dissolve

    voice audio.yoshi_v_hey1
    yo "Hey there, guys! How’s everything going here?"

    show keitaro talking1 at p6_5
    voice audio.keitaro_v_greeting2
    k "Hello, Scoutmaster Yoshi! "
    k "We’re doing alright, I think…! Not as fast as the other group, but we’re having fun."

    show hunter talking4 at p6_2
    voice audio.hunter_v_goro1c2
    hu "Sir Goro’s been doing most of the heavy lifting. He can work way faster than the rest of us."

    show hiro laugh1 at p6_4
    voice audio.hiro_v_laugh2a2
    hi "Haha, we’re mostly just cleaning up after him."

    show goro explain3 at p6_3
    voice audio.goro_v_rush4b2
    g "Now don’t discredit your work so far. All of your efforts count."

    show yoshi think2 at p6_6
    voice audio.yoshi_v_sirgoro6
    yo "I think this is the first time in a while that you’ve done a hands-on activity with the scouts, isn’t it, sir?"

    hide goro_winter2
    hide goro explain3
    show goro2_winter2 at p6_3
    show goro2 confused4 at p6_3
    voice audio.goro_v_think1a1
    g "Hmm… Outside of the fundraising we did last term… I guess you’re right."

    show keitaro compassion3 at p6_5
    voice audio.keitaro_v_conjunction2a
    k "I’m actually glad that we get to hang out with you, Sir Goro! We rarely got the chance to do that last year!"

    show hiro talking3 at p6_4
    voice audio.hiro_v_yeah1a4
    hi "Yeah! He’s not the grumpy-scary camp president anymore!"

    show jin shock5 at p6_1
    voice audio.jin_v_really1a
    j "Was he really…?"

    show hiro talking1 at p6_4
    voice audio.hiro_v_excited1a1
    hi "Oh boy, you don’t know the half of it! Almost every scout was afraid of him back then! "

    show hunter worry1 at p6_2
    voice audio.hunter_v_agree4d1
    hu "Yeah… We all got tongue tied whenever he was in the same room as us…"

    show jin think5 at p6_1
    voice audio.jin_v_think1a1
    j "I-I guess I did feel the same when I first met him… But that changed so quickly as soon as he started to talk."
    j "In my stay here so far, I find it kinda hard to imagine him that way… He’s like the calmest and gentlest boss I’ve ever had."

    hide goro2_winter2
    hide goro2 confused4
    show goro_winter2 at p6_3
    show goro sad2 at p6_3
    voice audio.goro_v_sigh1a
    g "They’re telling the truth, Jin. Even the scoutmasters were intimidated by me for the last couple years…  "

    show yoshi comp2 at p6_6
    voice audio.yoshi_v_but1
    yo "But it’s understandable, sir. You were dealing with a lot of things behind the scenes."

    show keitaro sad5 at p6_5
    voice audio.keitaro_v_agree4a
    k "Yeah… and there were times that we caused trouble too."

    show goro sigh1 at p6_3
    voice audio.goro_v_but1a
    g "Even still, it doesn’t excuse my unnecessarily steely demeanor. "
    g "As the figurehead, I should’ve served as a guiding example by handling everything with patience and compassion."

    show goro comp2 at p6_3
    voice audio.goro_v_glad1a
    g "But I’m glad everyone, including the scouts, kept an open mind and were able to give me time to change my ways."

    show keitaro talking1 at p6_5
    voice audio.keitaro_v_yessir1a
    k "That’s true, sir! We saw how you started changing during our term!"

    show hiro compassion3 at p6_4
    voice audio.hiro_v_laugh1a5
    hi "And it’s crazy how we can even joke around with you too, sir…"

    show hunter compassion5 at p6_2
    voice audio.hunter_v_sad1
    hu "He’s a real fluffy panda now…"

    hide goro_winter2
    hide goro comp2
    show goro2_winter2 at p6_3
    show goro2 explain2 at p6_3
    voice audio.goro_v_ehem1a
    g "*ehem* Let’s not get too sentimental, we still have a lot of work to do."

    show yoshi laugh2 at p6_6
    voice audio.yoshi_v_laugh1
    yo "Hahaha! You’re not really used to the compliments, huh sir?"

    show jin daydream2 at p6_1
    voice audio.jin_v_fudan3a1
    j "C…Cute…"

    show hunter thinking2 at p6_2
    voice audio.hunter_v_sigh1
    hu "But Sir Goro has a point… Compared to the other group, we’re lagging behind a bit."

    show hiro pout2 at p6_4
    voice audio.hiro_v_hmph1a
    hi "It’s not fair, we don’t have as many muscles as them!"

    show jin thinkdn2 at p6_1
    voice audio.jin_v_aiden4a
    j "Maybe I should’ve taken Aiden’s offer for a fitness routine so I could be more useful…"
    j "I just sit in front of my computer all day either doing work or playing games…"

    show hiro excited2 at p6_4
    voice audio.hiro_v_wait2a
    hi "Wait, you play video games too?!"

    show jin awkward6 at p6_1
    voice audio.jin_v_yes2c
    j "I… I do."

    show hiro amazed1 at p6_4
    voice audio.hiro_v_oh2a
    hi "Ooh, ooh! You should add me and maybe we can play together sometime!"

    show keitaro laugh1 at p6_5
    voice audio.keitaro_v_laugh3
    k "Haha, that’s mostly all we did at my house."

    show hiro confident2 at p6_4
    voice audio.hiro_v_laugh1a2
    hi "I’m a pretty good gamer, if I do say so myself~"
    hi "I’ve been telling these guys to livestream our game sessions!"

    show hunter sigh2 at p6_2
    voice audio.hunter_v_denial1
    hu "But you, Yoichi and Taiga can get so loud and hyper… Keitaro, Natsumi and I can’t even keep up…"

    show jin thinkdn1 at p6_1
    voice audio.jin_v_conj2a2
    j "Well, you could all be really popular with your unique personalities…"

    show hiro talking2 at p6_4
    voice audio.hiro_v_jin2a
    hi "What do you usually play, Hyunjin?"

    show jin comp6 at p6_1
    voice audio.jin_v_ah2a
    j "A-Aah… Well… An unhealthy amount of gacha games… "

    show keitaro confused3 at p6_5
    voice audio.keitaro_v_confused2
    k "Gacha? What’s that?"

    show hiro confident2 at p6_4
    voice audio.hiro_v_well1a1
    hi "It’s kinda like that capsule toy vending machine, Keitaro!"
    hi "In this case, you spend some money for a random chance to get stuff you can use to get better in the game!"

    show keitaro worry1 at p6_5
    voice audio.keitaro_v_thinking1
    k "With real money…?"

    show hunter talking1 at p6_2
    voice audio.hunter_v_agree1a
    hu "Yes. Most game developers nowadays use that as a business model. And it works."

    show hiro compassion3 at p6_4
    voice audio.hiro_v_relief1a1
    hi "The one time I tried playing a gacha game I had to quit – I got super unlucky and was too broke to keep going!"

    show jin perv5 at p6_1
    voice audio.jin_v_yeah1a
    j "Yeah, having a job means I have access to adult money… and that means I have the freedom to use it on whatever I want…"
    j "It hurts both me and my wallet… But if it’s for my 2-D husbandos, I don’t mind!"

    show hunter confused1 at p6_2
    voice audio.hunter_v_err1a
    hu "H-Husbandos…?"

    show jin comp5 at p6_1
    voice audio.jin_v_laugh2c
    j "I-I mean, characters…! Ahehehe…"

    show yoshi sigh1 at p6_6
    voice audio.yoshi_v_amazed1a
    yo "It baffles me how out of touch I am with modern times, that even something like games can be used as a business…"

    hide goro2_winter2
    hide goro2 explain2
    show goro_winter2 at p6_3
    show goro laugh5 at p6_3
    voice audio.goro_v_laugh2a
    g "Yeah, I agree… Could you imagine Camp Buddy as a gacha game?"

    show jin awkward1 at p6_1
    voice audio.jin_v_gulp1a
    j "*gulp*"

    show yoshi comp3 at p6_6
    voice audio.yoshi_v_laugh3
    yo "Looks like time has taken its toll on us, huh, sir?"

    show keitaro talking3 at p6_5
    voice audio.keitaro_v_yoshinori1
    k "Scoutmaster Yoshi, you’re not even that old! You shouldn’t be saying things like that."

    show hiro playful2 at p6_4
    voice audio.hiro_v_laugh1a
    hi "Hehe, you really had to leave out Sir Goro from that statement, huh, Keitaro? "

    show keitaro surprised2 at p6_5
    voice audio.keitaro_v_surprised1b
    k "A-Ack…!"

    hide goro_winter2
    hide goro laugh5
    show goro2_winter2 at p6_3
    show goro2 annoy2 at p6_3
    voice audio.goro_v_hey4a
    g "Hey, watch it, boy."

    show hiro panic1 at p6_4
    voice audio.hiro_v_surprised1d
    hi "Yikes! Scary Goro’s back!"

    show jin daydream4 at p6_1
    voice audio.jin_v_fudan4a2
    j "It’s kinda hot… I mean, it’s cold! It’s getting really cold out here, huh?!"

    hide goro2_winter2
    hide goro2 annoy2
    show goro_winter2 at p6_3
    show goro play3 at p6_3
    voice audio.goro_v_conj4a
    g "Either way, working at a summer camp exclusively puts people like Yoshinori and I at a disadvantage."

    show yoshi happy1 at p6_6
    voice audio.yoshi_v_yeah2
    yo "That’s why Jin’s here to bring us up to date!"

    show jin happy1 at p6_1
    voice audio.jin_v_yes1a
    j "Yes. We’ll start by having fast Wi-Fi, for sure."

    show hiro talking1 at p6_4
    voice audio.hiro_v_idea1c
    hi "Oh, I have an idea! You should add a lot of computers next term! Or maybe a few gaming consoles… or even better, VR!"

    show keitaro compassion2 at p6_5
    voice audio.keitaro_v_hiro4
    k "Hiro… I don’t think that’s a good idea…"

    show hiro excited2 at p6_4
    voice audio.hiro_v_aww1c
    hi "Why noooot? That could be a really cool camp activity! I can already see it… We’ll call it the Camp Budd-E-Sportsfest!"

    show hunter sigh2 at p6_2
    voice audio.hunter_v_sigh1
    hu "That was bad."

    show jin laugh3 at p6_1
    voice audio.jin_v_laugh1c
    j "Ahehe… "

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black with fade
    yo "{i}Everyone continued to work hard while we caught up, and after a few hours, we could really start to see the progress!{/i}"

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
    scene bg_site5_winter_day_piles with fade
    play music greatest_memories_casual loop

    show yoshi_winter2 at center
    show yoshi happy2 at center
    voice audio.yoshi_v_hey1
    yo "Hey, everyone! Why don’t we take a break?"

    show yoshi_winter2 at p11_5
    show yoshi happy2 at p11_5
    with move

    show goro_winter2 at p11_1
    show goro norm1 at p11_1
    show darius_winter2 at p11_2
    show darius norm3 at p11_2
    show jin_winter at p11_4
    show jin_glasses at p11_4
    show jin norm3 at p11_4
    show lloyd_winter2 at p11_3
    show lloyd norm4 at p11_3
    show natsumi_winter at p11_8
    show natsumi normal2 at p11_8
    show hunter_winter2 at p11_7
    show hunter normal1 at p11_7
    show keitaro_winter2 at p11_6
    show keitaro sigh2 at p11_6
    show hiro_winter2 at p11_9
    show hiro normal2 at p11_9
    show yoichi_winter at p11_10
    show yoichi normal1 at p11_10
    show taiga_winter at p11_11
    show taiga normal1 at p11_11
    with dissolve

    voice audio.keitaro_v_relief1
    k "Whew… There’s still so much left even after all that shoveling."

    show natsumi worry3 at p11_8
    voice audio.natsumi_v_confused2b
    n "I can’t imagine how the scoutmasters were planning to do it by themselves…"

    show jin think2 at p11_4
    voice audio.jin_v_yeah1a
    j "Yeah, by the looks of things I think we’ll need another day to finish up."

    show yoshi comp2 at p11_5
    voice audio.yoshi_v_conj3b
    yo "Either way, you scouts helping out is already a huge boost! We managed to clear out a huge chunk of ice and snow in a short time!"

    show darius happy1 at p11_2
    voice audio.darius_v_agree1a
    d "Yes, we’re in a much better state than yesterday. "

    show lloyd think2 at p11_3
    voice audio.lloyd_v_think1a1
    l "We’d be a lot faster if we had a snowplow, though. "
    l "But I guess it doesn’t make sense for Camp Buddy to have something like that on hand."

    show goro think3 at p11_1
    voice audio.goro_v_well1a
    g "Usually the local city hall sends their assistance, and I’ve been in touch with them since yesterday. Unfortunately, they’re still occupied clearing public roads.  "
    g "For now, we’ll have to make do."

    show hiro annoyed2 at p11_9
    voice audio.hiro_v_hmph1a
    hi "If we didn’t have to clean up after Wolfboy tossing snow around, we could’ve been done by now!"

    show yoichi angry3 at p11_10
    voice audio.yoichi_v_annoyed2b1
    yi "Gimme a break! I still shoveled a hell of a lot more snow than you did, you twiggy Torch-head!"

    show natsumi playful2 at p11_8
    voice audio.natsumi_v_thinking3a
    n "Maybe we should bring out Ms. Yuri to scare Yoichi into doing more work!"

    show hunter talking1 at p11_7
    voice audio.hunter_v_agree4c1
    hu "Oh yeah… We still haven’t seen Ms. Yuri. "
    hu "And I’m curious… Who is she busy taking care of?"

    hide yoshi_winter2
    hide yoshi comp2
    show yoshi2_winter2 at p11_5
    show yoshi2 awkward3 at p11_5
    hide jin_winter
    hide jin_glasses
    hide jin think2
    show jin_winter at p11_4
    show jin_glasses at p11_4
    show jin think2 at p11_4
    hide keitaro_winter2
    hide keitaro sigh2
    show keitaro_winter2 at p11_6
    show keitaro sigh2 at p11_6
    hide lloyd_winter2
    hide lloyd think2
    show lloyd_winter2 at p11_3
    show lloyd think2 at p11_3
    voice audio.yoshi_v_ah1
    yo "Ah, Yuri’s watching over Emilia, our inspector… sort of."

    show taiga confused2 at p11_11
    voice audio.taiga_v_confused1a
    t "Huh? What happened with her? Is she sick?"

    hide yoshi2_winter2
    hide yoshi2 awkward3
    show yoshi_winter2 at p11_5
    show yoshi comp2 at p11_5
    hide jin_winter
    hide jin_glasses
    hide jin think2
    show jin_winter at p11_4
    show jin_glasses at p11_4
    show jin think2 at p11_4
    hide keitaro_winter2
    hide keitaro sigh2
    show keitaro_winter2 at p11_6
    show keitaro sigh2 at p11_6
    hide lloyd_winter2
    hide lloyd think2
    show lloyd_winter2 at p11_3
    show lloyd think2 at p11_3
    voice audio.yoshi_v_yeah1
    yo "Yeah. But don’t worry, she’s doing a lot better now and just needs to continue resting! "
    yo "Yuri’s making sure of that while we’re out here!"

    show hunter talking4 at p11_7
    voice audio.hunter_v_surprised1
    hu "Oh, they must be close friends then. I bet we’ll like her too!"

    show yoichi angry1 at p11_10
    voice audio.yoichi_v_hunter1a
    yi "You’re way off, Twinkerbell! She’s been a prick ever since she got here a couple months ago!"

    show yoshi angry2 at p11_5
    voice audio.yoshi_v_yoichi1
    yo "Yoichi! That’s not a nice way to introduce someone! "

    show taiga angry5 at p11_11
    voice audio.taiga_v_ugh1
    t "For once, I agree with this hairball. I got nothing but bad vibes from her. But then I could be wrong.  "

    show hiro playful2 at p11_9
    voice audio.hiro_v_laugh1a
    hi "Oooh… Tea…"

    show lloyd think2 at p11_3
    voice audio.lloyd_v_think1b1
    l "Hmm… We won’t deny that she can be strict and demanding when it comes to doing her job. But you can’t judge a book by its cover."

    show darius talk1 at p11_2
    voice audio.darius_v_agree1a
    d "Yes. You never know what people are going through that makes them act a certain way."

    show jin sad2 at p11_4
    voice audio.jin_v_sigh2a
    j "We learned that during our trip…"

    show yoichi sigh2 at p11_10
    voice audio.yoichi_v_annoyed1a4
    yi "Meh, I don’t get it."

    show natsumi excited1 at p11_8
    voice audio.natsumi_v_oh1
    n "Oh, I do! It’s similar with Sir Goro, right? He was very ‘strict’ before, too! Now he’s all nice and friendly!"

    hide goro_winter2
    hide goro think3
    show goro2_winter2 at p11_1
    show goro2 sigh4 at p11_1
    voice audio.goro_v_sigh1a
    g "*sigh* Why am I in the spotlight again…?"

    show hiro laugh1 at p11_9
    voice audio.hiro_v_laugh3b
    hi "Psh! Why go further when you have Taiga right here? He was a total douche back then too, right?"

    show taiga panic4 at p11_11
    voice audio.taiga2_v_hey1h
    t "H-Hey! "

    show keitaro talking1 at p11_6
    voice audio.keitaro_v_excited2
    k "Either way, I can’t wait to meet her too! We’re already friends with Mr. Lloyd, Darius and Hyunjin!"

    show hiro angry1 at p11_9
    voice audio.hiro_v_keitaro3d
    hi "There you go again Keitaro, making everyone your best friend!"

    show goro2_winter2 at p12_1
    show goro2 sigh4 at p12_1
    show darius_winter2 at p12_2
    show darius talk1 at p12_2
    show lloyd_winter2 at p12_3
    show lloyd think2 at p12_3
    show jin_winter at p12_4
    show jin_glasses at p12_4
    show jin sad2 at p12_4
    show keitaro_winter2 at p12_6
    show keitaro talking1 at p12_6
    show hunter_winter2 at p12_7
    show hunter talking4 at p12_7
    show natsumi_winter at p12_8
    show natsumi excited1 at p12_8
    show hiro_winter2 at p12_9
    show hiro angry1 at p12_9
    show yoichi_winter at p12_10
    show yoichi sigh2 at p12_10
    show taiga_winter at p12_11
    show taiga panic4 at p12_11
    with move

    show aiden_winter2 at p12_12
    show aiden tasty1 at p12_12
    with dissolve

    hide taiga_winter
    hide taiga panic4
    show taiga_winter at p12_11
    show taiga panic4 at p12_11
    voice audio.aiden_v_todayspecial1a
    a "Lunchtime, everyone! I made a nice pot of chili, some corn muffins, and a warm pudding for dessert!"
    a "It’s all in the mess hall! Get it while it’s hot!"

    show yoichi excited1 at p12_10
    voice audio.yoichi_v_celebrate1a
    yi "Alright! I’m starving! Dibs on everything!"

    hide yoichi_winter
    hide yoichi excited1
    with moveoutright

    show hiro angry5 at p12_9
    voice audio.hiro_v_greet1b1
    hi "Hey! Leave some for me!"

    hide hiro_winter2
    hide hiro angry5
    with moveoutright

    show taiga talking1 at p12_11
    voice audio.taiga2_v_denial3a
    t "No way I’m gonna miss out on the food!"

    hide taiga_winter
    hide taiga talking1
    with moveoutright

    show natsumi surprised3 at p12_8
    voice audio.natsumi_v_annoyed4a
    n "H-Hey…! Everyone else has to eat too!"

    show keitaro playful1 at p12_6
    voice audio.keitaro_v_scheming1a
    k "Hehe, there’s no stopping them, Natsumi…"

    show hunter compassion3 at p12_7
    voice audio.hunter_v_thinking2
    hu "I guess we should go and join them."

    hide keitaro_winter2
    hide keitaro playful1
    hide hunter_winter2
    hide hunter compassion3
    hide natsumi_winter
    hide natsumi surprised3
    with moveoutright

    show lloyd hungry4 at p12_3
    voice audio.lloyd_v_amazed3a2
    l "Wah! You’re the best, Aiden! Steaming hot food is perfect for this kind of weather!"

    show darius grin1 at p12_2
    voice audio.darius_v_laugh1
    d "Yum."

    show jin talk2 at p12_4
    voice audio.jin_v_bye1a2
    j "I hope you guys don’t mind if I join the scouts… I’m actually really starving now."

    hide lloyd_winter2
    hide lloyd hungry4
    hide darius_winter2
    hide darius munch1
    hide jin_winter
    hide jin_glasses
    hide jin talk2
    with dissolve

    show goro2_winter2 at left
    show goro2 sigh4 at left
    show yoshi_winter2 at center
    show yoshi angry2 at center
    show aiden_winter2 at right
    show aiden tasty1 at right
    with move

    hide aiden_winter2
    hide aiden tasty1
    show aiden2_winter2 at right
    show aiden2 sigh5 at right
    voice audio.aiden_v_sigh1a
    a "*sigh* I really missed having the scouts around! They’re always so excited for anything I cook."

    hide goro2_winter2
    hide goro2 sigh4
    show goro_winter2 at left
    show goro happy1 at left
    voice audio.goro_v_agree7a
    g "I agree. Their presence here today really boosted our morale."
    g "I’m not going to lie, I was feeling rather stressed out after dealing with issues one after another since we left the hotel."

    show goro comp5 at left
    voice audio.goro_v_thanks2a1
    g "Thank you for taking the initiative and finding a solution to our issues, Yoshinori."

    hide aiden2_winter2
    hide aiden2 sigh5
    show aiden_winter2 at right
    show aiden comp2 at right
    voice audio.aiden_v_laugh2a1
    a "Yoshi is still the same model scout, always prepared for anything! "

    show yoshi comp6 at center
    voice audio.yoshi_v_laugh6
    yo "Ahehe, I’m just glad it turned into such a great day for everyone."

    show goro talk3 at left
    voice audio.goro_v_actually1a
    g "This actually leaves me a little bit of time to give an update to Mr. Clermont."
    g "He should be a bit relieved to hear that we got additional help today. "

    show aiden talk2 at right
    voice audio.aiden_v_yeah2a2
    a "Oh yeah… you’re the one doing that now since Emilia is tapped out."

    show yoshi think2 at center
    voice audio.yoshi_v_think1a
    yo "I should check on her today to see if she’s feeling any better."

    show aiden happy1 at right
    voice audio.aiden_v_praise3a
    a "Good idea! I’m supposed to hand over her lunch, but you can do that!"
    a "I’ll take over for you clearing out the snow! I gotta make up for my time in the kitchen, after all."

    show yoshi talk3 at center
    voice audio.yoshi_v_ah3
    yo "A-Ahh… Sure thing, Aiden! Thanks a lot!"

    show goro happy1 at left
    voice audio.goro_v_bye1a1
    g "See you later then, Yoshinori."

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

    $ location = location_gororoom
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_gororoom_winter_day with fade
    play music heracleum_b loop

    show yuri_autumn at left2
    show yuri explain3 at left2
    show emilia_sleep at right2
    show emilia think4 at right2
    voice audio.yuri_v_think1a1
    yu "… And whenever I try and give someone criticism, I always try and do it gently, so that they don’t beat themselves up too much."

    show emilia think5 at right2
    voice audio.emilia_v_yessir1
    e "R-Right… "

    show emilia sigh1 at right2
    voice audio.emilia_v_sigh1b
    e "*sigh* I guess I really thought people preferred the straightforwardness…"

    show yuri play4 at left2
    voice audio.yuri_v_laugh1a1
    yu "Hihi, well it DOES have it’s time and place, but maybe not all the time~"

    play sound sfx_doorknock
    show yuri_autumn at left
    show yuri play4 at left
    show emilia_sleep at center
    show emilia sigh1 at center
    with move

    show yoshi_winter at right
    show yoshi happy2 at right
    with dissolve

    voice audio.yoshi_v_greet1a2
    yo "Hello, you two! I brought your lunch, Emilia.  "
    yo "I hope I’m not interrupting anything."

    show yuri happy1 at left
    voice audio.yuri_v_no2a2
    yu "Not at all, I was just giving Emilia some advice."

    show yoshi shock2 at right
    voice audio.yoshi_v_shock1b
    yo "Whoa… I’m really surprised to hear that, Yuri."

    show yuri tease2 at left
    voice audio.yuri_v_well1a
    yu "Well, she asked for it. And I didn’t have much of a choice, since I AM the camp counselor you know."

    show emilia angry2 at center
    voice audio.emilia_v_hmph1a
    e "I-I could have handled myself just fine, thank you very much…!"

    show yuri play2 at left
    voice audio.yuri_v_sarcastic2a
    yu "Ah-ah-ah~, what did I tell you about relying on other people? It’s good to have a support system... and you couldn’t even find your meds a while ago!"

    show emilia explain2 at center
    voice audio.emilia_v_conj1a
    e "Just so you know, I’m feeling a lot stronger already. I’d say I’m almost back to normal."

    show yoshi comp2 at right
    voice audio.yoshi_v_well1
    yo "Well, I’m glad that you’re recovering just fine, Emilia!"

    show emilia talk1 at center
    voice audio.emilia_v_yuri2
    e "Yuri here has been listening to me ramble all day."
    e "I hate to admit it, but she made really great points that made me realize the mistakes I made about how I come across to everyone."

    show emilia shy5 at center
    voice audio.emilia_v_tsun1b
    e "She’s an excellent counselor, I must say."

    show yuri relief2 at left
    voice audio.yuri_v_well1a
    yu "Well, that is my job here after all~ And a counselor can only help if the person is willing to meet them halfway! "
    yu "You’ve been really open with me today, and it was thanks to that I was able to find some answers for you."

    show emilia comp3 at center
    voice audio.emilia_v_conj1a
    e "Having someone to tell all my thoughts to is still new to me. It really does help.  "

    show yoshi shock3 at right
    voice audio.yoshi_v_amazed1a
    yo "Wow, I never thought I’d hear that from you both!   "
    yo "Maybe you’ll end up as close friends after all, haha!"

    show emilia eyeroll4 at center
    voice audio.emilia_v_hmph1a
    e "Hmph, I doubt it! There’s no way I could deal with her strange hobbies and manic episodes!"

    show yuri pout1 at left
    voice audio.yuri_v_hey3b
    yu "Hey! It’s a lot better than being snobby and pretending to be rich!"

    show emilia pain4 at center
    voice audio.emilia_v_ugh1
    e "Hngh!"

    hide yoshi_winter
    hide yoshi shock3
    show yoshi2_winter at right
    show yoshi2 comp6 at right
    voice audio.yoshi_v_laugh6
    yo "Ahehe… Maybe I spoke too soon. "

    show yuri talk6 at left
    voice audio.yuri_v_anyway1b
    yu "Anyway, you guys must be super busy with groundwork, huh Yoshi? I’ve barely seen anyone all day long! "

    hide yoshi2_winter
    hide yoshi2 comp6
    show yoshi_winter at right
    show yoshi happy1 at right
    voice audio.yoshi_v_oh1
    yo "Oh, the scouts came by to help us shovel! I called Yoichi and Taiga last night, and the whole gang came along!"

    show yuri panic3 at left
    voice audio.yuri_v_what5a
    yu "WHAT?! And nobody told me?!" with vpunch
    yu "I gotta get out there – your turn now, Yoshi!"

    show yoshi shock2 at right
    voice audio.yoshi_v_wait3b
    yo "W-Wait, Yuri—"

    hide yuri_autumn
    hide yuri panic3
    with moveoutright

    show yoshi_winter at right2
    show yoshi shock2 at right2
    show emilia_sleep at left2
    show emilia eyeroll3 at left2
    with move

    voice audio.emilia_v_ugh2a
    e "Ugh… It’s about time she left."

    show yoshi comp3 at right2
    voice audio.yoshi_v_laugh3
    yo "Hehe, I’m really glad you two are getting along a little better now, Emilia… "

    show emilia sigh1 at left2
    voice audio.emilia_v_sigh1b
    e "*sigh* Barely… I’m just trying my best to keep my cool. "
    e "D-Don’t get me wrong, I am grateful for all her help."

    show emilia think2 at left2
    voice audio.emilia_v_well1
    e "I was discussing with Yuri about moving forward… and that includes my position here at the camp."
    e "I really appreciate that you all gave me a bit of time to calm down and stay here until I recover…"

    show emilia talk2 at left2
    voice audio.emilia_v_conj6
    e "But I found out from Yuri that none of you told Mr. Clermont the issue about my credentials…"

    hide yoshi_winter
    hide yoshi comp3
    show yoshi2_winter at right2
    show yoshi2 think5 at right2
    voice audio.yoshi_v_well1
    yo "Well, he was informed you weren’t feeling well, but we left the rest out for now."
    yo "After all, we still have a situation on the site to deal with."

    show emilia think3 at left2
    voice audio.emilia_v_response2b
    e "I see…"

    show emilia talk3 at left2
    voice audio.emilia_v_so1
    e "On that note, I was hoping to report my own mistakes to Mr. Clermont directly."
    e "I’m well aware of the severity of the error I made, which is why I need to be terminated from my position so that I don’t negatively affect the project further."

    hide yoshi2_winter
    hide yoshi2 think5
    show yoshi_winter at right2
    show yoshi worry2 at right2
    voice audio.yoshi_v_but1
    yo "But you don’t have to do that right now. We have everything under control with the work so far."

    show emilia sad2 at left2
    voice audio.emilia_v_regret2a
    e "It’s just… I need to face the consequences of my actions. "
    e "I don’t want to live a lie anymore…"

    show yoshi sigh1 at right2
    voice audio.yoshi_v_response1a
    yo "I understand, Emilia."

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black with fade
    yo "{i}After our serious talk, Emilia and I chatted a little bit more light-heartedly about the scouts coming back and when she’d get to meet them.{/i}"
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
    scene bg_entrance_winter_day with fade
    play music brand_new_day_winter loop

    show goro2_winter2 at center
    show goro2 sigh1 at center
    voice audio.goro_v_sigh1a
    g "*sigh* The roadway is still covered in snow…"
    g "At this rate, I don’t think the city would be able to help us anytime soon. "

    play sound sfx_carstop
    hide goro2_winter2
    hide goro2 sigh1
    show goro_winter2 at center
    show goro confused2 at center
    voice audio.goro_v_confused1a1
    g "Huh…? Who’s—"

    show goro_winter2 at right2
    show goro shock3 at right2
    with move

    show william_winter at left2
    show william norm2 at left2
    with dissolve

    voice audio.goro_v_william4a
    g "Mr. Clermont?! "

    show william happy1 at left2
    voice audio.william_v_goro1b
    w "Ah, Mr. Nomoru! Pardon my sudden visit, but I’ve brought some assistance!"

    show goro panic5 at right2
    voice audio.goro_v_confused2a1
    g "Wh-What do you mean, sir?"

    show william explain2 at left2
    voice audio.william_v_well1a
    w "Well, after your progress report yesterday, I had to see for myself how much damage the storm had done."
    w "That, and Ms. Komarova’s illness had me quite concerned."

    show william happy3 at left2
    voice audio.william_v_comp3
    w "I thought it would be best to head over straight away and assess what could be done, as well as bring some snow blowers to assist with your cleanup."
    w "They’re all brand new and belong to Camp Buddy now!"

    show goro awkward4 at right2
    voice audio.goro_v_but1a
    g "Once again, this is too much, sir… You’ve already given so much to the camp, and now you’re taking time to personally visit."

    show william comp4 at left2
    voice audio.william_v_dismiss2
    w "Nonsense. Think of it as part of the sponsorship."
    w "And don’t worry, I’m on leave at the moment! I thought it would be a nice change of scenery to see Camp Buddy again. I’m quite fond of it, now~ "

    show william play2 at left2
    voice audio.william_v_oh2
    w "Oh! And if you’d like, I can get out a bit of elbow grease and help you clear the snow myself too, haha!"

    show goro comp5 at right2
    voice audio.goro_v_dismiss3a
    g "That’s not necessary, sir! I do think with the combination of the machines that you brought and the extra help from the scouts, we may be able to finish everything today!"

    show william laugh1 at left2
    voice audio.william_v_laugh3
    w "Hahaha! I’m not as fragile as I look, you know! I used to be quite tough back in my more youthful days!  "
    w "But very well, I’ll leave the work to your team! "

    show william happy2 at left2
    voice audio.william_v_conj1a
    w "Now, should we get these snow blowers inside? I’m eager to see how quickly they can knock those piles away!"
    w "I’d also love to meet the scouts again! Is Mr. Nagame over there?"

    hide william_winter
    hide william happy2
    with dissolve

    show goro panic3 at right2
    voice audio.goro_v_wait2b1
    g "W-Wait, Mr. Clermont, please let me carry that!  "

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
    scene bg_site5_winter_day_piles with fade
    play music sunset_stroll_winter loop

    show william_winter at p7_1
    show william norm1 at p7_1
    show darius_winter2 at p7_3
    show darius norm1 at p7_3
    show lloyd_winter2 at p7_2
    show lloyd norm2 at p7_2
    show aiden_winter2 at p7_5
    show aiden norm2 at p7_5
    show jin_winter at p7_4
    show jin_glasses at p7_4
    show jin norm2 at p7_4
    show goro_winter2 at p7_6
    show goro norm1 at p7_6
    show yuri_winter2 at p7_7
    show yuri comp1 at p7_7
    show yoichi_winter at p12_1
    show yoichi excited1 at p12_1
    play sound sfx_snowblower
    voice audio.yoichi_v_celebrate2c
    yi "Whooooo!!!"
    yi "Screw digging, this is way more fun!"

    hide yoichi_winter
    hide yoichi excited1
    with moveoutright

    show natsumi_winter at p12_1
    show natsumi angry2 at p12_1
    with moveinleft

    voice audio.natsumi_v_yoichi7
    n "Yoichi! You’re making a huge mess! Stop playing around!"

    voice audio.yoichi_v_request1c1
    yi "Shut up, Mr. Perfect!"

    hide natsumi_winter
    hide natsumi angry2
    with moveoutright

    show yuri comp2 at p7_7
    voice audio.yuri_v_aww3a
    yu "Aww… Look at the scouts! They’re really enjoying themselves!"

    show goro laugh2 at p7_6
    voice audio.goro_v_laugh2a
    g "The way they’re using the snowblowers makes it look like it’s not even a chore anymore."

    show jin laugh3 at p7_4
    voice audio.jin_v_think1a1
    j "I kinda want to try one as well…"

    show lloyd laugh1 at p7_2
    voice audio.lloyd_v_laugh1a1
    l "These snowblowers are the best! We only need to shovel the bigger piles, and then just blow the rest!"

    show darius happy2 at p7_3
    voice audio.darius_v_conj1a1
    d "We can clear the entire site and start rebuilding by tomorrow at this rate."

    show william laugh1 at p7_1
    voice audio.william_v_laugh1
    w "Haha! I’m glad they helped! "

    show goro comp2 at p7_6
    voice audio.goro_v_thanks2a1
    g "I don’t know how to thank you, Mr. Clermont. You’ve done so much for us over these past few months."
    g "First it was the sponsorship, then our vacation, and now you’re taking time out of your busy life to help us with even minor inconveniences."

    show yuri tease2 at p7_7
    voice audio.yuri_v_laugh1a1
    yu "Hihi, you’re starting to fanboy again, Dad!"

    hide goro_winter2
    hide goro comp2
    show goro2_winter2 at p7_6
    show goro2 disappoint3 at p7_6
    voice audio.goro_v_ehem1a
    g "*ehem* I’m just being grateful!"

    show william comp4 at p7_1
    voice audio.william_v_comp1b
    w "Hahaha! Don’t mention it! I feel indebted to you all as well, you know."
    w "You were able to mold my son, Felix, to be quite the active and friendly person. And you helped me out with my business!"

    show william comp2 at p7_1
    voice audio.william_v_laugh2
    w "I wouldn’t have minded having an experience like Camp Buddy growing up too, haha! "
    w "Anyway, that’s enough reminiscing for now! If you don’t mind, I’d like to go and see Ms. Komarova to check on her condition."

    hide aiden_winter2
    hide aiden norm2
    show aiden2_winter2 at p7_5
    show aiden2 panic1 at p7_5
    show yuri panic1 at p7_7
    show lloyd shock1 at p7_2
    show darius shock1 at p7_3
    hide jin_winter
    hide jin_glasses
    hide jin laugh3
    show jin_winter at p7_4
    show jin_glasses at p7_4
    show jin scared1 at p7_4
    hide goro2_winter2
    hide goro2 disappoint3
    show goro_winter2 at p7_6
    show goro shy2 at p7_6
    voice audio.goro_v_ah1a
    g "Ah…"

    show william explain3 at p7_1
    voice audio.william_v_comp2a
    w "I won’t take up too much of her time, I just want to wish her well."

    show goro explain2 at p7_6
    voice audio.goro_v_alright1c1
    g "Alright, please follow me."

    hide goro_winter2
    hide goro explain2
    hide william_winter
    hide william explain3
    with dissolve

    show lloyd_winter2 at p5_1
    show lloyd shock1 at p5_1
    show darius_winter2 at p5_2
    show darius shock1 at p5_2
    show jin_winter at p5_3
    show jin_glasses at p5_3
    show jin scared2 at p5_3
    show aiden2_winter2 at p5_4
    show aiden2 panic1 at p5_4
    show yuri_winter2 at p5_5
    show yuri panic1 at p5_5
    with move

    voice audio.jin_v_worry1b3
    j "Oh no… Is Ms. Emilia gonna get in trouble…?"

    show darius worry2 at p5_2
    voice audio.darius_v_think1a1
    d "That’s what I’m thinking as well."

    show lloyd worry2 at p5_1
    voice audio.lloyd_v_think2a1
    l "But none of us told Mr. Clermont yet, right? "

    show yuri worry2 at p5_5
    voice audio.yuri_v_well1a
    yu "Well… Emilia was clear today about wanting to come clean. I just didn’t expect it to be this early."

    hide aiden2_winter2
    hide aiden2 panic1
    show aiden_winter2 at p5_4
    show aiden worry2 at p5_4
    voice audio.aiden_v_comp2b
    a "It’ll be fine, Yoshi and Gramps are gonna be there with her! "

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black
    hide screen location
    hide screen timeline
    hide screen quick_menu
    $quick_menu = False
    with fade
    $ time_transition_day_to_sunset_winter2()
    $ renpy.pause (2.0, hard=True)

    $ location = location_gororoom
    $ time = timeline_timesunset
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_gororoom_winter_sunset with fade
    play music brand_new_day_winter loop

    show yoshi_autumn at left2
    show yoshi confused1 at left2
    show emilia_sleep at right2
    show emilia norm3 at right2
    voice audio.yoshi_v_think1a
    yo "Hmm, it seems like there’s quite the commotion outside. I wonder if something happened."

    play sound sfx_doorknock
    show yoshi_autumn at p4_1
    show yoshi confused1 at p4_1
    show emilia_sleep at p4_2
    show emilia norm3 at p4_2
    with move

    show william_winter at p4_3
    show william happy1 at p4_3
    show goro_winter at p4_4
    show goro norm3 at p4_4
    with dissolve

    voice audio.william_v_greet2b
    w "Hello! Sorry for the surprise visit, but I wanted to check on our patient!"

    show emilia shock2 at p4_2
    voice audio.emilia_v_gasp1
    e "*gasp*"

    show yoshi panic1 at p4_1
    yo "...!"

    show goro talk1 at p4_4
    voice audio.goro_v_william2b
    g "Mr. Clermont came here after my report this morning… He brought in some equipment to help clear the grounds."

    show yoshi awkward4 at p4_1
    voice audio.yoshi_v_oh3
    yo "Oh… So that’s what I’ve been hearing outside."

    show william laugh1 at p4_3
    voice audio.william_v_goro1b
    w "Haha, it’s been a while since I’ve been to Camp Buddy and I wanted to have a little tour, and Mr. Nomoru was nice enough to give me a very good one."
    w "I also wanted to check myself once I heard one of our important staff members was ill!"

    show william comp2 at p4_3
    voice audio.william_v_emilia1c
    w "How are you, Emilia?"

    show emilia shy2 at p4_2
    voice audio.emilia_v_sir1
    e "I-I’m doing fine, sir. "
    e "But I have something very important I need to discuss with you."

    hide yoshi_autumn
    hide yoshi awkward4
    show yoshi2_autumn at p4_1
    show yoshi2 worry2 at p4_1
    voice audio.yoshi_v_emilia4
    yo "Emilia—"

    show emilia comp3 at p4_2
    voice audio.emilia_v_comp2a
    e "It’s alright, Yoshi. It’s about time Mr. Clermont hears the truth."

    show william confused2 at p4_3
    voice audio.william_v_confused1c
    w "I’m quite confused. What do you mean, Ms. Komarova?"

    show emilia sad2 at p4_2
    voice audio.emilia_v_sorry2
    e "I regret to inform you my professional identity has been far from the truth, sir."
    e "To start with, I falsified my credentials to get the job as an inspector. "

    show william shock2 at p4_3
    voice audio.william_v_what1b
    w "Wh-What?"

    show emilia sad4 at p4_2
    voice audio.emilia_v_conj4a
    e "In addition, I let my own personal issues with the other staff members here get in the way of progress, hindering the project multiple times."
    e "I am not qualified for the position and will be resigning effective immediately."

    show william sad3 at p4_3
    voice audio.william_v_sigh2
    w "I… am lost for words… I certainly wasn’t expecting this from you, Ms. Komarova."
    w "Did you know about this, Mr. Nomoru? Mr. Nagira?"

    show yoshi2 sad4 at p4_1
    voice audio.yoshi_v_sir3
    yo "W-We only learned recently, sir. During our stay at the hotel."

    show goro sad3 at p4_4
    voice audio.goro_v_well1a
    g "Our intent was to let Emilia recover, then inform you."

    show william sad2 at p4_3
    voice audio.william_v_isee1b
    w "I see…"

    show william sigh1 at p4_3
    voice audio.william_v_sigh1
    w "*sigh* To be honest, I didn’t come here just to help with the storm."
    w "I also wished to see if you all had been able to work out the issues I saw a week ago during our meeting."

    show william serious2 at p4_3
    voice audio.william_v_think1
    w "At first, I was impressed and happy that everything seemed to have worked out well… I actually came here to congratulate you personally."
    w "As unfortunate as this news is, I must commend you for your honesty, Ms. Komarova. "

    show william angry6 at p4_3
    voice audio.william_v_conj3b
    w "Regardless, I have to accept your resignation and not allow you to represent my company any longer. "

    show emilia sigh2 at p4_2
    voice audio.emilia_v_agree1c2
    e "I understand…"

    show william sad3 at p4_3
    voice audio.william_v_apology2
    w "Mr. Nomoru, allow me to sincerely apologize for this unacceptable oversight on behalf of the entire project."
    w "I personally prioritized those who had a familiarity with the camp during the application process."

    show william explain2 at p4_3
    voice audio.william_v_conj1a
    w "I understand now all the concerns your team expressed, and quite frankly this could have been avoided if the screening had been done properly."

    show goro sigh1 at p4_4
    voice audio.goro_v_sigh1a
    g "We weren’t aware of this matter either until recently like I said. You can at least be relieved to know that we managed to fix it amongst ourselves."
    g "But Mr. Clermont, if I may?"

    show william confused2 at p4_3
    voice audio.william_v_agree4c
    w "Yes?"

    show goro talk1 at p4_4
    voice audio.goro_v_comp1d1
    g "I understand your decision to remove Emilia as our inspector."
    g "However, with your permission, I’d like to offer her a position here at Camp Buddy."

    show emilia shock2 at p4_2
    voice audio.emilia_v_what3b
    e "Wh-What?!"

    show william confused3 at p4_3
    voice audio.william_v_really1a
    w "May I ask why you’re requesting this?"

    show goro explain2 at p4_4
    voice audio.goro_v_well1a
    g "I’ve been speaking with the rest of the staff and gathering their thoughts on the matter."

    show goro talk3 at p4_4
    voice audio.goro_v_yoshi2a
    g "Yoshinori, if you wouldn’t mind explaining?"

    hide yoshi2_autumn
    hide yoshi2 sad4
    show yoshi_autumn at p4_1
    show yoshi talk3 at p4_1
    voice audio.yoshi_v_ah3
    yo "A-Ah…! Yes...!"
    yo "I know that we all started off on the wrong foot with Emilia, but we moved past our differences."

    show yoshi explain2 at p4_1
    voice audio.yoshi_v_actually1a
    yo "We talked about it, and we all want her to continue working with us.  "
    yo "Even though she may have forged her credentials, her work ethic and commitment to the project are very much real."

    show yoshi comp2 at p4_1
    voice audio.yoshi_v_so1a
    yo "We believe it would be in the best interests of both Emilia and Camp Buddy to have her stay. "

    show william comp1 at p4_3
    w "..."

    show william comp2 at p4_3
    voice audio.william_v_laugh1
    w "You all never cease to amaze me. One surprise after another, huh?"
    w "If you all feel so strongly about it, then I’m in no place to disagree. You know what’s best for your camp."

    show william happy1 at p4_3
    voice audio.william_v_goro1d
    w "Mr. Nomoru will be my direct contact in place of Ms. Komarova, but I’m sure you have something planned for her."
    w "Ms. Komarova herself is free to accept or decline the offer – it’s up to her."

    show emilia panic3 at p4_2
    voice audio.emilia_v_sad1
    e "This is all so… overwhelming…"
    e "Everyone is going out of their way to help me… even after everything I’ve done…"

    show emilia cry2 at p4_2
    voice audio.emilia_v_disagree4a
    e "The people I mistreated are the ones who saved me from what I thought was inevitable…"

    show yoshi comp5 at p4_1
    voice audio.yoshi_v_conj4b
    yo "We’ve all gone through our own hardships, making mistakes along the way."
    yo "It’s about how you change from here on out."

    show yoshi bold2 at p4_1
    voice audio.yoshi_v_anyway1a
    yo "What I do know is all of us would be glad to work further with you, but now that choice is entirely up to you."

    show emilia cry3 at p4_2
    voice audio.emilia_v_thanks2
    e "I-I’m more than happy to accept and I’m nothing but grateful…!"

    show william happy3 at p4_3
    voice audio.william_v_well1a
    w "Well, it seems that everyone has mutual feelings here after all! "
    w "You’ve all resolved the issues I was worried about, even if they weren’t in ways I expected!"

    show william laugh1 at p4_3
    voice audio.william_v_impressed1b
    w "I think what I’ve witnessed here is a testament to the true Camp Buddy spirit!"
    w "I am more honored than ever to be your sponsor."

    play sound sfx_doorknock
    show yoshi_autumn at p9_1
    show yoshi bold2 at p9_1
    show emilia_sleep at p9_2
    show emilia cry3 at p9_2
    show william_winter at p9_3
    show william laugh1 at p9_3
    show goro_winter at p9_4
    show goro talk3 at p9_4
    with move

    show yuri_winter at p9_5
    show yuri bold1 at p9_5
    show jin_winter at p9_6
    show jin_glasses at p9_6
    show jin awkward2 at p9_6
    show aiden2_winter at p9_9
    show aiden2 scared2 at p9_9
    show darius_winter at p9_8
    show darius shock1 at p9_8
    show lloyd_winter at p9_7
    show lloyd shock1 at p9_7
    with moveinright

    hide emilia_sleep
    hide emilia cry3
    show emilia_sleep at p9_2
    show emilia cry3 at p9_2
    voice audio.aiden_v_yuri9b
    a "Yuri, I told you not to barge in… they aren’t done yet…! "

    show yuri amazed2 at p9_5
    voice audio.yuri_v_emilia3b
    yu "Emilia! I’m so glad you accepted the offer!"

    show darius laugh3 at p9_8
    voice audio.darius_v_laugh2a
    d "Welcome to the project, officially."

    show lloyd laugh2 at p9_7
    voice audio.lloyd_v_laugh1a1
    l "I’m glad it all worked out in the end!"

    show emilia comp2 at p9_2
    voice audio.emilia_v_worry1
    e "Everyone…"

    show yuri comp2 at p9_5
    voice audio.yuri_v_actually1a
    yu "We were so nervous when you confessed, but it was the right thing to do!"

    hide yoshi_autumn
    hide yoshi bold2
    show yoshi2_autumn at p9_1
    show yoshi2 annoy3 at p9_1
    voice audio.yoshi_v_really6
    yo "W-Were you all really eavesdropping?"

    show jin shy3 at p9_6
    voice audio.jin_v_conj2c1
    j "S-Sort of… But we didn’t mean to…"

    show goro comp2 at p9_4
    voice audio.goro_v_alright2a1
    g "It’s alright, everyone, we’re about finished. What brings you all here anyway?"

    show lloyd happy2 at p9_7
    voice audio.lloyd_v_agree2b1
    l "With the help of the scouts and the machines, we were able to finish clearing the site today!"

    show darius happy1 at p9_8
    voice audio.darius_v_agree2a
    d "We can start fixing the actual damage tomorrow."

    hide yoshi2_autumn
    hide yoshi2 annoy3
    show yoshi_autumn at p9_1
    show yoshi shock2 at p9_1
    hide emilia_sleep
    hide emilia comp2
    show emilia_sleep at p9_2
    show emilia comp2 at p9_2
    voice audio.yoshi_v_amazed1a
    yo "Wow! Everything’s cleared out? That’s amazing! I guess we’re officially back on track then! "

    show goro amazed1 at p9_4
    voice audio.goro_v_praise2b1
    g "Good job, everyone! "

    show yuri explain3 at p9_5
    voice audio.yuri_v_so2a
    yu "Soooo… We actually have one more surprise for everyone…"
    yu "Since we achieved this goal and everybody is here, along with Mr. Clermont and the scouts, I’ve decided to throw us a party!"

    show goro bored1 at p9_4
    voice audio.goro_v_yuri3a
    g "Yuri… We literally just came back from a vacation… Is this really necessary…?"

    show yuri angry2 at p9_5
    voice audio.yuri_v_rush1b1
    yu "Come ooon!!! We rarely have this many people around during the winter season! And besides, the holidays are just around the corner!"
    yu "We’ve already decorated and prepared everything!"

    hide yoshi_autumn
    hide yoshi shock2
    show yoshi2_autumn at p9_1
    show yoshi2 comp6 at p9_1
    voice audio.yoshi_v_unsure3a
    yo "I guess, we don’t really have a choice, sir… "

    hide aiden2_winter
    hide aiden2 scared2
    show aiden_winter at p9_9
    show aiden laugh2 at p9_9
    voice audio.aiden_v_laugh1b2
    a "Hehe, she’s been pushing us to finish all day so we’d have time for it."

    show jin sleepy3 at p9_6
    voice audio.jin_v_yeah2a
    j "Yeah… My fingers feel frozen from all the time outside today…"

    show yuri happy1 at p9_5
    voice audio.yuri_v_william3a
    yu "Mr. Clermont, I hope you’ll stay as well! It’s the least we could do after all your help today!"

    show william play2 at p9_3
    voice audio.william_v_agree1b
    w "I don’t see why not? I’d love to join the celebration!"

    show aiden bold2 at p9_9
    voice audio.aiden_v_alright1a1
    a "Alright! The party is on! Come on, there’s plenty of food in the mess hall!"

    show lloyd hungry4 at p9_7
    voice audio.lloyd_v_praise3b
    l "Awesome! I’m so hungry from all that work today! I can’t wait!"

    show darius bold3 at p9_8
    voice audio.darius_v_encourage1a
    d "Let’s get wild."

    show goro excited3 at p9_4
    voice audio.goro_v_alright1b1
    g "I’ll go get us some liquor!"

    hide darius_winter
    hide darius bold3
    hide william_winter
    hide william play2
    hide lloyd_winter
    hide lloyd hungry4
    hide goro_winter
    hide goro excited3
    hide jin_winter
    hide jin_glasses
    hide jin sleepy3
    hide aiden_winter
    hide aiden bold2
    with dissolve

    show yoshi2_autumn at left
    show yoshi2 comp6 at left
    show emilia_sleep at center
    show emilia upset1 at center
    show yuri_winter at right
    show yuri happy1 at right
    with move

    e "..."

    show yuri laugh1 at right
    voice audio.yuri_v_emilia3a
    yu "You should join us, Emilia! The scouts have been dying to meet you!"

    hide yoshi2_autumn
    hide yoshi2 comp6
    show yoshi_autumn at left
    show yoshi happy2 at left
    voice audio.yoshi_v_oh1
    yo "Oh yeah, let me introduce you! You’re going to love them!"

    show emilia sad3 at center
    voice audio.emilia_v_wait1c
    e "W-Wait… before we leave… I really want to take this opportunity to properly thank you both…"
    e "This is more than I could have ever hoped for, and I want to make sure the trust everyone placed in me is worth it."

    show yoshi bold2 at left
    voice audio.yoshi_v_encourage3
    yo "That’s the spirit, Emilia! You’re speaking like a true buddy now!"

    show yuri play2 at right
    voice audio.yuri_v_rush1c1
    yu "Come on, that’s enough cheese, you two! We’re having fun tonight!"
    yu "Now, Yoshi, go and fetch the scouts and bring them to the mess hall!"

    hide yuri_winter
    hide yuri play2
    show yuri2_winter at right
    show yuri2 laugh3 at right
    voice audio.yuri_v_excited1b
    yu "I can’t wait for them to see what I’ve done!!"

    show yoshi laugh2 at left
    voice audio.yoshi_v_right3
    yo "Right!"

    hide yoshi_autumn
    hide yoshi laugh2
    with dissolve

    hide yuri2_winter
    hide yuri2 laugh3
    show yuri_winter at right
    show yuri tease4 at right
    voice audio.yuri_v_alright1d1
    yu "Alright, Emilia! You’re coming with me! I have to put you into something ‘special’!"

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black
    hide screen location
    hide screen timeline
    hide screen quick_menu
    $quick_menu = False
    with fade
    $ time_transition_sunset_to_night_winter2()
    $ renpy.pause (2.0, hard=True)

    $ location = location_messhall
    $ time = timeline_timenight
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_messhall_winter_night_xmas with fade
    play music buddy_oath_holiday loop

    show yoshi_autumn at p7_1
    show yoshi grin3 at p7_1
    show hiro_winter at p7_2
    show hiro amazed1 at p7_2
    show hunter_winter at p7_3
    show hunter amazed2 at p7_3
    show keitaro_winter at p7_4
    show keitaro amazed1 at p7_4
    show natsumi_winter at p7_5
    show natsumi excited1 at p7_5
    show yoichi_winter at p7_6
    show yoichi grin1 at p7_6
    show taiga_winter at p7_7
    show taiga excited2 at p7_7
    voice audio.hunter_v_surprised4f
    hu "Wahhh… All the lights and decorations are so pretty! They make the mess hall look so festive!"

    show yoshi shock2 at p7_1
    voice audio.yoshi_v_amazed1a
    yo "Wow… Yuri really went all out again with this event, huh…?"

    show yoshi_autumn at p8_2
    show yoshi shock4 at p8_2
    show hiro_winter at p8_3
    show hiro surprised2 at p8_3
    show hunter_winter at p8_4
    show hunter surprised2 at p8_4
    show keitaro_winter at p8_5
    show keitaro surprised2 at p8_5
    show natsumi_winter at p8_6
    show natsumi surprised1 at p8_6
    show yoichi_winter at p8_7
    show yoichi awkward1 at p8_7
    show taiga_winter at p8_8
    show taiga surprised4 at p8_8
    with move

    show yuri_xmas at p8_1
    show yuri excited2 at p8_1
    voice audio.yuri_v_hey2c
    yu "Welcome to our wonderful Kris-My-Ass spectacular party! " with vpunch

    show yoshi panic4 at p8_2
    voice audio.yoshi_v_yuri8
    yo "Y-Yuri! What are you wearing!?"

    show yuri tease2 at p8_1
    voice audio.yuri_v_laugh2a1
    yu "What? It’s just a festive get-up to get in the mood! Don’t you like it?"

    hide yoshi_autumn
    hide yoshi panic4
    show yoshi2_autumn at p8_2
    show yoshi2 confused3 at p8_2
    hide yuri_xmas
    hide yuri tease2
    show yuri_xmas at p8_1
    show yuri tease2 at p8_1
    voice audio.yoshi_v_uh1a
    yo "I… Uhh… Yeah?"

    show yuri bold2 at p8_1
    voice audio.yuri_v_well1a
    yu "We’re having a holiday party, so we might as well play the part! "

    show yoichi annoyed5 at p8_7
    voice audio.yoichi_v_yuri6a
    yi "The holiday’s still a couple weeks away! Your calendar’s way off again, crazy lady!"

    show yuri excited2 at p8_1
    voice audio.yuri_v_conj5a
    yu "A long day of hard work calls for a celebration!"

    voice audio.yuri_v_here1a
    yu "Here, I even have party hats for everyone!"

    show yuri_xmas at p8_5
    show yuri excited2 at p8_5
    with move

    hide hiro_winter
    hide hiro surprised2
    hide hunter_winter
    hide hunter surprised2
    hide keitaro_winter
    hide keitaro surprised2
    hide natsumi_winter
    hide natsumi surprised2
    hide yoichi_winter
    hide yoichi annoyed5
    hide taiga_winter
    hide taiga surprised4
    show hiro_xmas at p8_3
    show hiro surprised2 at p8_3
    show hunter_xmas at p8_4
    show hunter surprised2 at p8_4
    show keitaro_xmas at p8_5
    show keitaro surprised2 at p8_5
    show natsumi_xmas at p8_6
    show natsumi surprised1 at p8_6
    show yoichi_xmas at p8_7
    show yoichi awkward1 at p8_7
    show taiga_xmas at p8_8
    show taiga surprised4 at p8_8
    with dissolve

    show yuri_xmas at p8_1
    show yuri amazed1 at p8_1
    with move

    voice audio.yuri_v_praise4a
    yu "Look how cute! Everyone matches the theme now!"

    show yoichi sigh2 at p8_7
    voice audio.yoichi_v_groan2a4
    yi "Thank god, it’s just a hat. I thought this was just another excuse to make us wear something kinky."

    show hiro angry1 at p8_3
    voice audio.hiro_v_yoichi6a
    hi "Don’t be such a party pooper, Wolfboy! Costumes are always fun!"

    show yuri explain1 at p8_1
    voice audio.yuri_v_actually1a
    yu "I actually would’ve picked some for you guys, had I known you were coming."
    yu "But I did get some lovely outfits for your scoutmasters, including you, Yoshi! What I’m wearing is just a taste of what’s to come!"

    show yoshi2 worry1 at p8_2
    voice audio.yoshi_v_gulp1a
    yo "*gulp*"

    show natsumi talking1 at p8_6
    voice audio.natsumi_v_unsure1d
    n "Well, I think you look really pretty, Ms. Yuri!"

    show yoichi annoyed1 at p8_7
    voice audio.yoichi_v_disgust1c
    yi "Pretty creepy!"

    show hiro annoyed4 at p8_3
    voice audio.hiro_v_shush1a
    hi "Shush, Wolfboy!"

    show hunter laugh1 at p8_4
    voice audio.hunter_v_agree4c1
    hu "I guess I do feel a lot more festive now wearing this~ "

    show keitaro laugh1 at p8_5
    voice audio.keitaro_v_laugh2
    k "Haha, this really reminds me of the costume party during camp. It feels nostalgic!"

    show taiga sigh2 at p8_8
    voice audio.taiga_v_keitaro1e
    t "Keitaro, that was literally this year… you’re making it sound like it’s been a long time…"

    show keitaro talking1 at p8_5
    voice audio.keitaro_v_well1
    k "Well, time moves slower when I’m not seeing you guys, after all!"

    show natsumi laugh1 at p8_6
    voice audio.natsumi_v_laugh1
    n "Hehe, leave it to Ms. Yuri to make any party a lot more colorful!"

    show yuri happy1 at p8_1
    voice audio.yuri_v_anyway1a
    yu "Anyway, make yourselves comfortable! You guys can start digging into the food Aiden prepared!"

    show yoichi excited1 at p8_7
    voice audio.yoichi_v_celebrate1c
    yi "Finally! Some good food after days of trash!"

    show taiga annoyed2 at p8_8
    voice audio.taiga2_v_hey1f
    t "Hey, fast food isn’t trash! That stuff is my favorite. "

    show yoichi annoyed1 at p8_7
    voice audio.yoichi_v_hiro1f
    yi "Stupid Torch-head didn’t even try to cook for us!"

    show hiro angry1 at p8_3
    voice audio.hiro_v_insult1a6
    hi "I still need ingredients, you stupid Wolfboy! I didn’t expect us to be locked up inside for so long."

    voice audio.hiro_v_mmm3d
    hi "Plus, I’m not complaining about some extra pizza~"

    show natsumi talking1 at p8_6
    voice audio.natsumi_v_agree3a
    n "I agree with Yoichi for once! We need some nutritious food back in our bodies!"

    show yoichi annoyed4 at p8_7
    voice audio.yoichi_v_groan2a5
    yi "Ugh, way to make it sound lame, Mr. Perfect."

    hide yoshi2_autumn
    hide yoshi2 worry1
    show yoshi_autumn at p8_2
    show yoshi comp2 at p8_2
    voice audio.yoshi_v_laugh1
    yo "Haha, it sounds like you guys have had your own struggles with the storm the last few days."

    show hunter talking1 at p8_4
    voice audio.hunter_v_compassion1b
    hu "It’s not been too bad, but like Hiro said, we weren’t really prepared to be stuck indoors."
    hu "We didn’t have much of a choice but to order out. "

    show keitaro compassion3 at p8_5
    voice audio.keitaro_v_agree4d
    k "Yeah… My sister and I aren’t great cooks, ahehe…"

    show yuri comp4 at p8_1
    voice audio.yuri_v_laugh1a2
    yu "Hehe, well feel free to eat as much as you want here, boys! There’s plenty for everyone~"

    show keitaro excited2 at p8_5
    voice audio.keitaro_v_rush2
    k "Let’s go, everyone!"

    hide keitaro_xmas
    hide keitaro excited2
    hide yoichi_xmas
    hide yoichi annoyed4
    hide hunter_xmas
    hide hunter talking1
    hide natsumi_xmas
    hide natsumi talking1
    hide hiro_xmas
    hide hiro angry1
    hide taiga_xmas
    hide taiga annoyed2
    with dissolve

    show yuri_xmas at left2
    show yuri comp4 at left2
    show yoshi_autumn at right2
    show yoshi comp2 at right2
    with move

    hide yoshi_autumn
    hide yoshi comp2
    show yoshi2_autumn at right2
    show yoshi2 confused2 at right2
    voice audio.yoshi_v_yuri6
    yo "H-How do you always manage to pull off things like this on such short notice, Yuri?"

    show yuri tease2 at left2
    voice audio.yuri_v_laugh1a2
    yu "Hihi, we have plenty of people and supplies for a party! It’s all about your drive and motivation~  "
    yu "Plus, I had my sturdy, manly, scoutmasters to help me move things around and decorate!"

    hide yoshi2_autumn
    hide yoshi2 confused2
    show yoshi_autumn at right2
    show yoshi talk3 at right2
    voice audio.yoshi_v_oh2
    yo "Oh yeah, where is everyone else? They all ran off suddenly and I haven’t seen them yet…"

    show yuri_xmas at p4_3
    show yuri tease2 at p4_3
    show yoshi_autumn at p4_4
    show yoshi talk3 at p4_4
    with move

    show lloyd_xmas at p4_2
    show lloyd sad4 at p4_2
    with dissolve

    voice audio.lloyd_v_geez1a3
    l "These pants are really short and tight… "

    show darius_xmas at p4_1
    show darius happy1 at p4_1
    with dissolve

    voice audio.darius_v_ugh1
    d "Hurr durr. Do you know… the muffin man?"

    show lloyd sigh4 at p4_2
    voice audio.lloyd_v_groan2a3
    l "Ugh… I should’ve known you would make me an elf, out of all things…"

    show darius play2 at p4_1
    voice audio.darius_v_cute1
    d "I think you look cute. I like your legs."

    show yuri amazed2 at p4_3
    voice audio.yuri_v_aww3a
    yu "Awwwww~!!! Look at you, Lloyd! You’re like a fun-sized toy! Darius can play with you all night, hihi~   "

    show lloyd pout1 at p4_2
    voice audio.lloyd_v_annoyed1b3
    l "See, I told you they’d laugh at me!"

    show darius explain4 at p4_1
    voice audio.darius_v_laugh1
    d "They’re not laughing at you; they’re laughing with you."

    show lloyd sigh1 at p4_2
    voice audio.lloyd_v_groan2a3
    l "Ugh… Easy for you to say… You have such a cool costume! You’re lucky that you’re wearing something less embarrassing."

    show darius confused5 at p4_1
    voice audio.darius_v_think3a
    d "Which part of this is less embarassing...? I look like Willy Wanker."

    show yuri tease2 at p4_3
    voice audio.yuri_v_lloyd7b
    yu "Don’t be shy, Lloyd! Go straight for that sweet surprise he’s hiding, I’m sure it’s extra-large and full of flavor!"

    hide yoshi_autumn
    hide yoshi talk3
    show yoshi2_autumn at p4_4
    show yoshi2 sigh1 at p4_4
    voice audio.yoshi_v_sigh3a
    yo "*sigh* I guess Yoichi was right about the costumes…"
    yo "I’m surprised that the other staff are okay with this."

    show lloyd think5 at p4_2
    voice audio.lloyd_v_conj4a2
    l "You know, after working with Yuri for a few months, you get used to it."

    show darius_xmas at p5_2
    show darius explain4 at p5_2
    show lloyd_xmas at p5_3
    show lloyd think5 at p5_3
    show yuri_xmas at p5_4
    show yuri tease2 at p5_4
    show yoshi2_autumn at p5_5
    show yoshi2 sigh1 at p5_5
    with move

    show jin_xmas at p5_1
    show jin daydream2 at p5_1
    with dissolve

    hide lloyd_xmas
    hide lloyd think5
    show lloyd_xmas at p5_3
    show lloyd think5 at p5_3
    voice audio.jin_v_laugh3a
    j "H-Hehe… I really like this event, Yuri… It reminds me of the filler arcs in anime specifically made for fanservice!"

    show yuri amazed3 at p5_4
    voice audio.yuri_v_response2a1
    yu "I know right?! Can you believe it!? It’s like a buffet of smoking hot men!"

    show jin awkward5 at p5_1
    voice audio.jin_v_confused2a2
    j "But…"

    show jin comic3 at p5_1
    voice audio.jin_v_hngh4a
    j "I didn’t expect to be included! I thought I was just going to be the observer!!"
    j "This outfit feels a bit contradictory, too… I’m an angel, but I’m definitely not having pure thoughts!"

    show yuri tease4 at p5_4
    voice audio.yuri_v_laugh1a2
    yu "Hihi, but that makes it all the more tantalizing! And your cute twink body blends right in with everyone! "

    show yuri excited4 at p5_4
    voice audio.yuri_v_kyaa1a
    yu "Kyaaa~! I can see you being manhandled by the other two, though!"
    yu "You can count on them to take you to heaven!"

    show jin dizzy3 at p5_1
    voice audio.jin_v_wah1b
    j "Guuuuuuuhhhhhhhh…!! Stop making scenarios in my head! I’m getting a nosebleed just thinking about it!"

    show jin_xmas at p6_2
    show jin dizzy3 at p6_2
    show darius_xmas at p6_3
    show darius explain4 at p6_3
    show lloyd_xmas at p6_4
    show lloyd think5 at p6_4
    show yuri_xmas at p6_5
    show yuri excited4 at p6_5
    show yoshi2_autumn at p6_6
    show yoshi2 sigh1 at p6_6
    with move

    show aiden_xmas at p6_1
    show aiden excited1 at p6_1
    with dissolve

    voice audio.aiden_v_flex1c
    a "Well, your fantasy’s about to get even better ’cause the breeding stud is here!"
    a "And the nose isn’t the only tip that’s red on this reindeer~"

    show yuri amazed3 at p6_5
    show jin comic4 at p6_2
    voice audio.jin_v_wah3c
    j "GAAAAHHH!! AIDEN?! YOU LOOK LIKE A STRIPPER AT A CIRCUIT PARTY!!!" with vpunch

    show aiden laugh3 at p6_1
    voice audio.aiden_v_agree3a1
    a "Not sure what that is, but sure! You had me at stripper!"

    show yuri excited4 at p6_5
    voice audio.yuri_v_kyaa1a
    yu "KYAAAAA! I knew it’d look perfect on you, Aiden!"

    show aiden relief2 at p6_1
    voice audio.aiden_v_relief1a2
    a "Ahh~ The things I do to tickle you guys’ pickle. "

    show lloyd shock2 at p6_4
    voice audio.lloyd_v_amazed3b1
    l "Damn… you even oiled yourself up, Aiden… "

    show darius play2 at p6_3
    voice audio.darius_v_praise2a
    d "Props to your commitment."

    show aiden play3 at p6_1
    voice audio.aiden_v_well1b1
    a "Well, the original suit Yuri gave me had more pieces, but I figured this was more my style."

    show yuri laugh2 at p6_5
    voice audio.yuri_v_agree1d1
    yu "It’s perfect, it’s perfect! Aiden you’re the beeeest!"

    show jin dizzy2 at p6_2
    voice audio.jin_v_hngh1c
    j "Hngh… I’m starting to feel giddy…"

    show aiden play2 at p6_1
    voice audio.aiden_v_oho1a
    a "What’s that, Jin? You wanna ride?"

    hide yoshi2_autumn
    hide yoshi2 sigh1
    show yoshi_autumn at p6_6
    show yoshi worry2 at p6_6
    voice audio.yoshi_v_wait4
    yo "W-Wait… Is it okay for you to wear something like this…? I mean, maybe if it’s just us, but Mr. Clermont is here too, right…?"

    show aiden_xmas at p7_2
    show aiden play2 at p7_2
    show jin_xmas at p7_3
    show jin dizzy3 at p7_3
    show darius_xmas at p7_4
    show darius explain4 at p7_4
    show lloyd_xmas at p7_5
    show lloyd think5 at p7_5
    show yuri_xmas at p7_6
    show yuri bold2 at p7_6
    show yoshi_autumn at p7_7
    show yoshi worry2 at p7_7
    with move

    show william_xmas at p7_1
    show william_pipe at p7_1
    show william excited3 at p7_1
    with dissolve

    voice audio.william_v_excited1
    w "Why yes, I am!"
    w "And I’ve never felt so alive! It’s been years since I’ve had this much fun!"

    hide yoshi2_autumn
    hide yoshi2 sigh1
    show yoshi_autumn at p7_7
    show yoshi shock2 at p7_7
    voice audio.yoshi_v_william7
    yo "M-Mr. Clermont…?!"

    show william amazed2 at p7_1
    voice audio.william_v_laugh3
    w "Back at the firm everyone is so stiff and formal – I’d love to be around people who can have a good time more often!"

    show yuri bold4 at p7_6
    voice audio.yuri_v_conj2d1
    yu "See? Mr. Clermont knows how to have fun!"

    hide yoshi_autumn
    hide yoshi shock2
    show yoshi2_autumn at p7_7
    show yoshi2 sigh4 at p7_7
    hide yuri_xmas
    hide yuri bold4
    show yuri_xmas at p7_6
    show yuri bold4 at p7_6
    voice audio.yoshi_v_sir4
    yo "S-Sir, I can’t believe you’re really wearing that…"

    show william_xmas at p8_2
    show william_pipe at p8_2
    show william amazed2 at p8_2
    show aiden_xmas at p8_3
    show aiden play2 at p8_3
    show jin_xmas at p8_4
    show jin dizzy3 at p8_4
    show darius_xmas at p8_5
    show darius explain4 at p8_5
    show lloyd_xmas at p8_6
    show lloyd think5 at p8_6
    show yuri_xmas at p8_7
    show yuri bold4 at p8_7
    show yoshi2_autumn at p8_8
    show yoshi2 sigh1 at p8_8
    with move

    show emilia_xmas at p8_1
    show emilia sigh1 at p8_1
    with dissolve

    voice audio.emilia_v_sigh2c
    e "I’m starting to rethink my decision about staying here…"

    show yuri amazed2 at p8_7
    voice audio.yuri_v_emilia3c
    yu "Kyaaaaaa!!! Emilia! You look soooo preeeettyyy! "

    show emilia shock2 at p8_1
    voice audio.emilia_v_question2a1
    e "R-Really?"

    show yuri amazed2 at p8_7
    voice audio.yuri_v_agree1b1
    yu "Yes! That ice queen costume suits you so well! Finally, a lady I can dress up as well!"

    show emilia confused5 at p8_1
    voice audio.emilia_v_tsun1b
    e "At least you chose something that matches me. "

    show yuri excited2 at p8_7
    voice audio.yuri_v_omg1a
    yu "That was supposed to be my costume this year, but it fits you so much better!"

    show emilia play2 at p8_1
    voice audio.emilia_v_conj1c1
    e "I’d say I’m impressed considering this is a cheap costume from the party store."

    show yuri annoy4 at p8_7
    voice audio.yuri_v_hey3a
    yu "Heeey, I put in a lot of work refitting them to everyone’s measurements! I’ve altered them to fit each of your personalities too!"

    show yoshi2 awkward4 at p8_8
    voice audio.yoshi_v_yuri4
    yo "I don’t know how you even find the time, Yuri…"

    show yuri explain3 at p8_7
    voice audio.yuri_v_jin3a
    yu "It wasn’t just me, Jin helped me plan them out too!"

    show jin scared2 at p8_4
    voice audio.jin_v_yuri3c
    j "Shhh! Don’t throw me under the bus, Yuri!"

    hide yoshi2_autumn
    hide yoshi2 awkward4
    show yoshi_autumn at p8_8
    show yoshi laugh1 at p8_8
    voice audio.yoshi_v_laugh1
    yo "Haha, I think it’s sweet you made these for everyone, Yuri."

    show darius bored5 at p8_5
    voice audio.darius_v_question2b2
    d "Says the guy not in one yet."

    show yoshi awkward4 at p8_8
    voice audio.yoshi_v_well3
    yo "W-Well, I haven’t seen Goro yet either!"

    show lloyd talk3 at p8_6
    voice audio.lloyd_v_shock1a1
    l "Oh, he said he went off to grab some booze for us! I think he’s pulling something special out of his office."

    show yuri excited4 at p8_7
    voice audio.yuri_v_excited1a
    yu "I’ve already given him his costume too! I can’t wait to see him in it~"

    hide yoshi_autumn
    hide yoshi awkward4
    show yoshi2_autumn at p8_8
    show yoshi2 sigh1 at p8_8
    hide yuri_xmas
    hide yuri excited4
    show yuri_xmas at p8_7
    show yuri excited4 at p8_7
    voice audio.yoshi_v_sigh3a
    yo "*sigh* You really were overprepared for this, Yuri…"

    show yuri tease2 at p8_7
    voice audio.yuri_v_laugh1a2
    yu "Hihi, I HAVE been planning this ever since our costume party, but I thought it would only be the four of us. "
    yu "Once the project started, I added the other’s costumes, but with the hotel vacation, I thought there wasn’t going to be time."

    show yuri laugh1 at p8_7
    voice audio.yuri_v_relief2b2
    yu "I’m glad we were able to find a way to still celebrate it!"

    show yuri worry3 at p8_7
    yu "It’s a bummer that the scouts don’t have a costume, though…"

    show yuri laugh1 at p8_7
    yu "We’re lucky the hats were left over from last year’s party! "

    show yuri tease4 at p8_7
    voice audio.yuri_v_anyway1a
    yu "Anyway, quit stalling! Go get in your costume and fetch Dad!"

    show lloyd rage3 at p8_6
    voice audio.lloyd_v_agree2b2
    l "Yeah! It’s not fair that we’re the only ones feeling embarrassed about this!"

    hide yoshi2_autumn
    hide yoshi2 sigh1
    show yoshi_autumn at p8_8
    show yoshi comp3 at p8_8
    voice audio.yoshi_v_conj2b
    yo "Alright, alright. "

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black with fade
    yo "{i}Not wanting to aggravate Yuri, I went into the bathroom and put my costume on before heading to the office to find Sir Goro…{/i}"

    scene cg black
    $ quick_menu = False
    hide screen location
    hide screen timeline
    hide screen quick_menu
    $quick_menu = False
    with fade
    play sound sfx_clotheschanging
    $ renpy.pause (2.0, hard=True)

    $ location = location_office
    $ quick_menu = True
    show screen location
    show screen timeline
    show screen quick_menu
    scene bg_office_winter_night_xmas with fade
    play music old_familiar_home loop

    show yoshi_xmas at center
    show yoshi confused3 at center
    voice audio.yoshi_v_goro7
    yo "Goro? Are you in here?"

    show yoshi_xmas at right2
    show yoshi shock3 at right2
    with move

    show goro_xmas at left2
    show goro talk3 at left2
    with dissolve

    voice audio.goro_v_yoshi2b
    g "Ah, Yoshinori. Yes, I’m here."

    show yoshi_blush1 at right2
    show yoshi shock6 at right2
    voice audio.yoshi_v_shock1c
    yo "W-Whoa! What are you wearing?!"

    show goro sigh1 at left2
    voice audio.goro_v_sigh1b
    g "*sigh* I'm not sure either, but Yuri was insistent that I wear it."
    g "She says that she regretted how 'covered' I was during the last costume party and wanted to give me more eye-candy this time."

    hide yoshi_blush1
    show yoshi shy6 at right2
    voice audio.yoshi_v_laugh6
    yo "Ahehe, I'd say she definitely succeeded..."

    show yoshi comp3 at right2
    voice audio.yoshi_v_unsure2b
    yo "Are you sure it’s alright to go out there with just that on…? I mean… Won’t you get cold?"

    show goro talk4 at left2
    voice audio.goro_v_actually1b
    g "I actually tried to close the jacket, but there's no buttons. I think she did that on purpose."

    show yoshi confused2 at right2
    voice audio.yoshi_v_unsure1b
    yo "I'm not sure it would close even with that... It looks tight on your arms already."

    show goro play3 at left2
    voice audio.goro_v_heh1a
    g "Heh, I’m surprised you noticed my arms from where you’ve been staring."

    show yoshi_blush1 at right2
    show yoshi panic4 at right2
    voice audio.yoshi_v_shock3
    yo "Gah… I can’t help it, I couldn’t keep my eyes off your…"

    $ working = False
    $ shuffle_menu()
    menu():
        yo "Gah… I can’t help it, I couldn’t keep my eyes off your…{fast}"
        "Wrapped package":
            $ working = True
            $ score_top += 1
            show yoshi scared1 at right2
            voice audio.yoshi_v_gulp1a
            yo "*gulp*"
            yo "Th-That package is wrapped really nicely…"

            show goro_blush1 at left2
            show goro play2 at left2
            voice audio.goro_v_really2b
            g "Really? Why don’t you come open it then~?"
        "Candy Cane":
            $ working = True
            $ score_bot += 1
            show yoshi scared1 at right2
            voice audio.yoshi_v_gulp1a
            yo "*gulp*"
            yo "I’d like a taste of that candy cane…"

            show goro_blush1 at left2
            show goro play2 at left2
            voice audio.goro_v_oh3b
            g "You can take a lick if you’d like~"
        "Jingle Balls":
            $ working = True
            $ score_top += 2
            show yoshi scared1 at right2
            voice audio.yoshi_v_gulp1a
            yo "*gulp*"
            yo "D-Do those balls jingle?"

            show goro_blush1 at left2
            show goro play2 at left2
            voice audio.goro_v_heh1a
            g "Depends on how you play with them. "
            g "Why don’t you give it a try?"
        "Stuffed Stocking":
            $ working = True
            $ score_bot += 2
            show yoshi scared1 at right2
            voice audio.yoshi_v_gulp1a
            yo "*gulp*"
            yo "Th-That stocking is stuffed…"

            show goro_blush1 at left2
            show goro play2 at left2
            voice audio.goro_v_heh2b
            g "It’s about to be stuffed somewhere else~"

    hide yoshi_blush1
    show yoshi_blush2 at right2
    show yoshi shock3 at right2
    voice audio.yoshi_v_goro3
    yo "G-Goro…!"

    show goro play3 at left2
    voice audio.goro_v_yoshi15a
    g "What? You’re dressed like you’re ready to crack some nuts, anyways."

    show yoshi sigh1 at right2
    voice audio.yoshi_v_sigh3a
    yo "*sigh* Have you been spending too much time around Aiden?"

    show goro tease2 at left2
    voice audio.goro_v_heh3a
    g "Hah! Hardly."
    g "Besides, let’s be honest, with how the last few days have been, we could both use some heat."

    voice audio.goro_v_rush2a1
    g "So, come over here and warm up with me before the party…"

    show yoshi_blush2 at right2
    show yoshi shy2 at right2
    yo "..."

    show yoshi_xmas at center
    show yoshi_blush2 at center
    show yoshi shy2 at center
    with move

    $ position = 0
    $ renpy.choice_for_skipping()
    if score_bot == score_top:
        $ position = renpy.random.randint(1, 2)

    if score_bot > score_top or position == 1:
        hide screen location
        hide screen timeline
        hide screen quick_menu
        $ quick_menu = False
        $ say_box = False
        $ fp_stage = 'mgg3_f'
        $ success_jumpto = 'day7_goro_5d'
        $ failed_jumpto = 'day7_goro_aftersx'
        jump fp

    elif score_top > score_bot or position == 2:
        hide screen location
        hide screen timeline
        hide screen quick_menu
        $ quick_menu = False
        $ say_box = False
        $ fp_stage = 'mgg3_b'
        $ success_jumpto = 'day7_goro_5s'
        $ failed_jumpto = 'day7_goro_aftersx'
        jump fp

label day7_goro_aftersx:
    $ location = location_messhall
    show screen location
    show screen timeline
    $quick_menu = True
    show screen quick_menu
    scene bg_messhall_winter_night_xmas with fade
    play music buddy_oath_holiday loop
    play bgsound sfxloop_crowd loop

    show goro_xmas at left2
    show goro norm1 at left2
    show yoshi_xmas at right2
    show yoshi sigh1 at right2
    voice audio.yoshi_v_sigh3a
    yo "*sigh* This costume Yuri gave me is so tight-fitting… I can’t even button it all the way up…"

    show goro think2 at left2
    voice audio.goro_v_annoyed1a1
    g "The sides of my jacket don’t even connect. Closing it is impossible."
    g "It’s also not much better than being naked in this weather… The cold outside felt miserable."

    show goro tease2 at left2
    voice audio.goro_v_heh1a
    g "Good thing you warmed me up beforehand."

    show yoshi comp6 at right2
    voice audio.yoshi_v_laugh6
    yo "A-Ahehe…"

    show goro tease3 at left2
    voice audio.goro_v_yoshi15a
    yo "I have to say though, your costume suits you very well. You’re quite the expert at nut cracking, as I saw."

    show yoshi sigh4 at right2
    voice audio.yoshi_v_really6
    yo "*sigh* You already made that joke..."

    show goro tease5 at left2
    voice audio.goro_v_laugh1a1
    g "But I’m not joking."

    show goro_xmas at center
    show goro norm1 at center
    show yoshi_xmas at right
    show yoshi awkward1 at right
    with move

    show yuri_xmas at left
    show yuri rage1 at left
    with dissolve

    voice audio.yuri_v_greet1a
    yu "There you two are!! What took you so long?! You missed the champagne popping!"

    show goro play6 at center
    voice audio.goro_v_well2a
    g "I was popping something else."

    show yoshi shock2 at right
    voice audio.yoshi_v_ah4
    yo "A-Ah! W-We had trouble putting on our costumes! "

    show yuri irked2 at left
    voice audio.yuri_v_yoshi11a
    yu "Yoshi, this is no different than when you put on your camp uniform! And Dad, yours is literally a two-piece outfit!"
    yu "You both should’ve moved at double time since we were waiting for you!"

    show yoshi shy6 at right
    voice audio.yoshi_v_well3
    yo "W-Well…"

    show goro play2 at center
    voice audio.goro_v_rush2c1
    g "Give us a break, Yuri. We spent the whole day outside digging."
    g "Poor Yoshinori here was panting like a dog a few minutes ago."

    show yoshi_blush1 at right
    show yoshi panic1 at right
    yo "...!"

    show yuri annoy2 at left
    voice audio.yuri_v_hey3a
    yu "Hey! Why are you two acting so sus?"
    yu "You know what? Nevermind. Just come join the party already! Everyone’s doing their own thing now!  "

    hide yuri_xmas
    hide yuri annoy2
    with dissolve

    hide yoshi_blush1
    show goro_xmas at left
    show goro happy2 at left
    with move

    voice audio.goro_v_so1a
    g "So, what do you want to do for the night, Yoshinori?"

    $ working = False
    $ shuffle_menu()
    menu():
        g "So, what do you want to do for the night, Yoshinori?{fast}"
        "Enjoy the buffet.":
            $working = True
            jump day7_goro_aiden
        "Join the games.":
            $working = True
            jump day7_goro_yuri
        "Have drinks.":
            $working = True
            jump day7_goro_lloyd
        "Chill out.":
            $working = True
            jump day7_goro_jin

label day7_goro_aiden:
    $sq_aiden += 1
    show yoshi happy1 at right
    voice audio.yoshi_v_think4
    yo "Why don’t we get something to eat?"

    show goro play2 at left
    voice audio.goro_v_oh3a
    g "Oh? You still have an appetite after your ‘meal’ earlier?"

    show yoshi shock3 at right
    voice audio.yoshi_v_shock3
    yo "G-Gah! You’d think after a couple months, I’d be used to you teasing me like this, sir…"

    show goro laugh1 at left
    voice audio.goro_v_laugh2a
    g "Hahaha! I understand why Aiden does it so often. You make it too easy."

    show yoshi awkward3 at right
    voice audio.yoshi_v_anyway3a
    yo "A-Anyway, let’s check out the food bar. "

    show goro_xmas at p5_1
    show goro confused1 at p5_1
    show yoshi_xmas at p5_2
    show yoshi confused2 at p5_2
    with move

    voice audio.yoshi_v_think1a
    yo "Hmm, it looks your favorite meatballs ran out, sir."

    show goro talk3 at p5_1
    voice audio.goro_v_unsure3a2
    g "Maybe there’s still some left in the kitchen."

    show yoshi talk3 at p5_2
    voice audio.yoshi_v_yeah1
    yo "Oh yeah. I don’t see Aiden around. Maybe he’s making another serving!"

    show goro happy2 at p5_1
    voice audio.goro_v_rush1d1
    g "Why don’t we go and see then?"

    show yoshi happy1 at p5_2
    voice audio.yoshi_v_sure2
    yo "Sure thing!"

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
    scene bg_kitchen_winter_night_xmas with fade
    play music buddy_oath_holiday loop

    show aiden_xmas at left2
    show aiden happy1 at left2
    show hiro_xmas at right2
    show hiro normal1 at right2
    voice audio.aiden_v_alright4a1
    a "You got the sauce simmering, little chef?"

    show hiro talking1 at right2
    voice audio.hiro_v_agree1b1
    hi "Yup! It should be good, I’m just starting on the meatballs now!"

    show aiden laugh1 at left2
    voice audio.aiden_v_encourage1a
    a "Alright! Keep it up, bro!"

    show aiden_xmas at p4_3
    show aiden norm1 at p4_3
    show hiro_xmas at p4_4
    show hiro normal1 at p4_4
    with move

    show yoshi_xmas at p4_1
    show yoshi talk1 at p4_1
    show goro_xmas at p4_2
    show goro norm1 at p4_2
    with dissolve

    voice audio.yoshi_v_greet1a1
    yo "Hey there, Aiden! …And Hiro?"

    show hiro talking2 at p4_4
    voice audio.hiro_v_greet2a
    hi "Oh, heya Scoutmaster Yoshi and Sir Goro!"

    show goro confused2 at p4_2
    voice audio.goro_v_unsure1a1
    g "Looks like you’ve put Hiro to work here, Aiden. Shouldn’t he be out partying with his friends?"

    show hiro compassion3 at p4_4
    voice audio.hiro_v_disagree1a1
    hi "It’s not like that, sir! I was actually dying to get in the kitchen and help Bro Aiden out!"

    show aiden comp5 at p4_3
    voice audio.aiden_v_agree1b1
    a "Haha, yup! The little guy was begging to come help, and I just couldn’t say no that face."

    play sound sfx_ovending
    show aiden talk2 at p4_3
    voice audio.aiden_v_oops1a
    a "Woops, looks like the rolls are done."

    show hiro talking1 at p4_4
    voice audio.hiro_v_confident1a
    hi "On it, bro!"

    show hiro_xmas at p4_3
    show hiro normal1 at p4_3
    show aiden_xmas at p4_4
    show aiden norm1 at p4_4
    with move

    show yoshi happy2 at p4_1
    voice audio.yoshi_v_amazed1a
    yo "Wow, you two are really in sync with each other. It’s almost like you’ve been cooking together forever."

    show hiro laugh1 at p4_3
    voice audio.hiro_v_well1a1
    hi "Haha, well I did spend most of the summer helping Bro Aiden out in here."
    hi "He taught me a lot about what it’s like to cook for a crowd, and how to be quicker in the kitchen~"

    show aiden excited3 at p4_4
    voice audio.aiden_v_oh3a
    a "Not only that, but he’s leveled up his cooking skills too, you guys should try some of his snacks!"

    show yoshi happy1 at p4_1
    voice audio.yoshi_v_sure2
    yo "Oh, sure! I’d love to."

    show hiro_xmas at center
    show hiro confident2 at center
    with move

    hide hiro_xmas
    hide hiro confident2
    show hiro_xmas at center
    show hiro confident2 at center
    voice audio.hiro_v_alright1a1
    hi "Here you guys go! Tell me what you think~"

    show goro norm3 at p4_2
    show yoshi munch1 at p4_1
    yog "..."

    show goro shock1 at p4_2
    show yoshi shock1 at p4_1
    yog "...!"

    show yoshi amazed1 at p4_1
    voice audio.yoshi_v_amazed1c
    yo "Th-This is amazing, Hiro!"

    show hiro surprised3 at center
    voice audio.hiro_v_really3a
    hi "Wah, really?!"

    show goro amazed2 at p4_2
    voice audio.goro_v_praise2a1
    g "Yes, it’s as good as Aiden’s. "

    show aiden comp2 at p4_4
    voice audio.aiden_v_aww2a
    a "Awww, look how much my little chef has grown!"

    show hiro excited2 at center
    voice audio.hiro_v_alright1b1
    hi "Alright! I’m gonna bring it out to the group then, bro!"
    hi "I really want ‘him’ to taste this—"

    show yoshi_xmas at p5_2
    show yoshi shock1 at p5_2
    show goro_xmas at p5_3
    show goro shock1 at p5_3
    show hiro_xmas at p5_4
    show hiro surprised2 at p5_4
    show aiden_xmas at p5_5
    show aiden shock1 at p5_5
    with move

    show yoichi_xmas at p5_1
    show yoichi rage2 at p5_1
    voice audio.yoichi_v_hiro1a
    yi "BUTTCHEEKS! TORCH-HEAD!" with vpunch
    yi "Where the hell’s the food?! I’m starving!"

    show hiro angry3 at p5_4
    voice audio.hiro_v_ugh2d
    hi "Ugh, shouldn’t you have assigned feeding times already, Wolfboy? "

    show yoichi annoyed5 at p5_1
    voice audio.yoichi_v_request1a4
    yi "Shut it! And why are these old geezers in here? Are they getting to eat the new batch before the rest of us?!"

    show yoichi_xmas at p5_4
    show yoichi sniff1 at p5_4
    with move

    show hiro angry5 at p5_4

    show yoichi_xmas at p5_1
    show yoichi sniff1 at p5_1
    with move

    voice audio.hiro_v_greet1c1
    hi "HEY! "
    yi "*munch, munch* "

    show yoichi confident3 at p5_1
    voice audio.yoichi_v_response1a1
    yi "Eh, not bad."

    show hiro angry6 at p5_4
    voice audio.hiro_v_what5a
    hi "WHAT?! You just wolfed down half the plate and all you can say is ‘not bad?!’  "

    show yoichi annoyed5 at p5_1
    voice audio.yoichi_v_agree1a2
    yi "Yeah, I’ve had better. But I guess this’ll do."

    hide yoichi_xmas
    hide yoichi annoyed5
    with dissolve

    show hiro angry1 at p5_4
    voice audio.hiro_v_yoichi5a
    hi "Hey! What the hell, I worked hard on that!"
    hi "Bring it back!"

    hide hiro_xmas
    hide hiro angry1
    with dissolve

    show yoshi_xmas at left
    show yoshi comp5 at left
    show goro_xmas at center
    show goro comp1 at center
    show aiden_xmas at right
    show aiden comp1 at right
    with move

    voice audio.yoshi_v_laugh6
    yo "Ahehe, I guess Hiro and Yoichi still argue as much as they did before…"

    show aiden laugh3 at right
    voice audio.aiden_v_laugh2b1
    a "Hahaha, but that just shows how good of friends they are!"

    show goro happy4 at center
    voice audio.goro_v_amazed1a1
    g "Still, I’m impressed by his cooking. I don’t think we’ve had another scout since you that was that capable, Aiden."

    show goro play3 at center
    voice audio.goro_v_heh1a
    g "Heh, maybe he’d like a job as your sous chef one day."

    show aiden bold2 at right
    voice audio.aiden_v_amazed1a1
    a "I’d like that! He and I get along great in the kitchen! With a little more experience, he’ll be as good as me… or even better!"

    show yoshi comp3 at left
    voice audio.yoshi_v_alright3
    yo "J-Just don’t teach him all your habits, alright?"

    show aiden tease1 at right
    voice audio.aiden_v_laugh1b2
    a "Why not~? He’ll get real friendly with the other campers then, hehe~"

    show goro explain2 at center
    voice audio.goro_v_ehem1a
    g "*ehem* Anyway, we just came to get some of those meatballs."

    show aiden tease2 at right
    voice audio.aiden_v_oho1a
    a "Oho~ You’re feeling forward tonight, are you Gramps~?"
    a "There’s enough ‘meat’ and ‘balls’ for you both! "

    show yoshi sigh4 at left
    voice audio.yoshi_v_aiden11
    yo "*sigh* Aiden…"

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black with fade
    yo "{i}After getting some snacks from Aiden, we munched on them and chatted with him and Hiro for a while longer.{/i}"
    yo "{i}Hiro told us about all the stuff he’d been trying in the kitchen since leaving camp, and before long he and Aiden were totally wrapped up in conversation about it!{/i}"
    yo "{i}I’m glad he and Aiden have such a strong bond!{/i}"

    jump day7_goro_aftersq

label day7_goro_yuri:
    $sq_yuri += 1
    show yoshi talk3 at right
    voice audio.yoshi_v_think1a
    yo "It looks like Yuri’s hosting a game with some of the scouts."

    show goro happy2 at left
    voice audio.goro_v_rush1d1
    g "Want to check it out?"

    show yoshi happy2 at right
    voice audio.yoshi_v_yeah2
    yo "Yeah! Maybe we can join in too!"

    show goro comp5 at left
    voice audio.goro_v_laugh1a1
    g "Hehe, Yoshinori… We're not that young anymore…"

    show goro_xmas at p5_1
    show goro norm1 at p5_1
    show yoshi_xmas at p5_2
    show yoshi norm1 at p5_2
    with move

    show yuri_xmas at p5_3
    show yuri excited1 at p5_3
    show hunter_xmas at p5_4
    show hunter shy2 at p5_4
    show natsumi_xmas at p5_5
    show natsumi confused2 at p5_5
    with dissolve

    voice audio.natsumi_v_confused3a
    n "Like this…?"

    show yuri excited2 at p5_3
    voice audio.yuri_v_natsumi1a
    yu "Bend your hips a little, Natsumi! You’re too stiff!"

    show natsumi confused4 at p5_5
    voice audio.natsumi_v_thinking2a
    n "Uhh… I’m not sure modeling is something I’m good at, Ms. Yuri."

    show hunter worry1 at p5_4
    voice audio.hunter_v_natsumi2
    hu "Hngh… Stay still, Natsumi…"

    show yoshi confused2 at p5_2
    voice audio.yoshi_v_hey1
    yo "Hey there! Looks like something’s interesting’s going on here."

    show yuri pout1 at p5_3
    voice audio.yuri_v_greet2a
    yu "Oh hey, Dad, Yoshi! Good of you two to finally join the party with everyone!"

    show goro confused2 at p5_1
    voice audio.goro_v_confused2a1
    g "What game are you all playing…? Natsumi’s doing some really... provocative poses."

    show hunter talking1 at p5_4
    voice audio.hunter_v_surprised2
    hu "O-Oh… We’re not playing a game, sir. I’m sketching up a fanfic for Ms. Yuri, and Natsumi’s modeling for the cover."

    show yuri relief2 at p5_3
    voice audio.yuri_v_fujo1b2
    yu "Ahhh, yes~ I’m still working on the title. I’m stuck choosing between ‘Schlonging for You’~ or ‘Booty and the Feast!’"

    show yoshi awkward3 at p5_2
    voice audio.yoshi_v_uh1a
    yo "Both of them sound… wrong."

    show natsumi excited1 at p5_5
    voice audio.natsumi_v_oh1
    n "Oh, it’s actually interesting though, sir! It’s a romantic story of two partners separated by fate! They’re desperate for each other, but torn apart by destiny! "

    show goro irked3 at p5_1
    voice audio.goro_v_sigh2a
    g "*sigh* Yuri… Why are you making the scouts work during a party?"

    show yuri bold2 at p5_3
    voice audio.yuri_v_oh1a
    yu "Oh, this isn’t ‘just’ work! I’m giving Hunter here some training for his blooming art career!"

    show hunter talking4 at p5_4
    voice audio.hunter_v_agree5a
    hu "Y-Yes… Creative writing is also part of my college curriculum, and I figured I could learn a lot from Ms. Yuri on how to coordinate it with my art."

    show yoshi_xmas at p5_1
    show yoshi shock1 at p5_1
    show yuri_xmas at p5_2
    show yuri shock1 at p5_2
    show hunter_xmas at p5_3
    show hunter surprised2 at p5_3
    show goro_xmas at p5_4
    show goro disappoint3 at p5_4
    with move

    voice audio.goro_v_rush3a1
    g "*sigh* You two are coming with me. We’re going to party."

    show natsumi surprised3 at p5_5
    voice audio.natsumi_v_wait2
    n "S-Sir Goro, wait…!"

    hide natsumi_xmas
    hide natsumi surprised3
    hide hunter_xmas
    hide hunter surprised2
    hide goro_xmas
    hide goro disappoint3
    with moveoutright

    show yoshi_xmas at left2
    show yoshi comp1 at left2
    show yuri_xmas at right2
    show yuri worry5 at right2
    with move

    voice audio.yuri_v_aww4a
    yu "Awwwww… There goes my artist AND subject."

    show yoshi laugh1 at left2
    voice audio.yoshi_v_laugh1
    yo "Haha, it’s really nice to see you get excited when it comes to anything art related."

    show yuri comp4 at right2
    voice audio.yuri_v_yeah1a1
    yu "Yeah, I’m not really good at it myself, but a part of me kinda wishes I was."

    show yoshi bold2 at left2
    voice audio.yoshi_v_encourage1
    yo "Even though it’d take a lot of time and effort, I think you could do it! "

    show yuri explain1 at right2
    voice audio.yuri_v_well1c
    yu "Well… The funny thing is I used to try when I was younger, but as soon as Dad and I found out that we both enjoyed camping, I shifted my focus."
    yu "Not that I blame Dad, he always supported me no matter what my interests were."

    show yoshi confused2 at left2
    voice audio.yoshi_v_well1
    yo "Well, what’s stopping you from going back to it now?"

    show yuri think3 at right2
    voice audio.yuri_v_think1a1
    yu "Well… when everyone left after the first term, my only goal was helping Dad run the camps. And I had to relocate to handle one of the other branches."
    yu "Things were so crazy busy for the both of us that we didn’t have time for ourselves, you know?"

    show yoshi worry2 at left2
    voice audio.yoshi_v_yeah3
    yo "Yeah, I can understand that…"

    show yuri happy1 at right2
    voice audio.yuri_v_but1a
    yu "But now… I think I might just have the chance again, after everything settles down with this project."

    show yoshi happy1 at left2
    voice audio.yoshi_v_well2
    yo "Well, I think this off-season is the perfect time to start! "
    yo "You have some time to train, and you’d be able to come up with some really fun activities for the scouts!"

    show yoshi relief2 at left2
    voice audio.yoshi_v_confident3
    yo "We may be in the middle of our work, but Sir Goro and I have the management stuff covered!"

    show yuri comp2 at right2
    voice audio.yuri_v_yeah1d1
    yu "Yeaaah I really owe you big time for taking over my job as Dad’s secretary."
    yu "Even though I’ve been at it for years, you honestly already handle it much better than me."

    show yuri sigh3 at right2
    voice audio.yuri_v_sigh2a
    yu "Since he’s my dad, I can get complacent working with him and complain a lot, which he tolerates for some reason."
    yu "With you, he’s much more productive! And considering how much he’s mellowed out recently, I don’t think I have to worry about him as much anymore!"

    show yoshi bold2 at left2
    voice audio.yoshi_v_comp5
    yo "Haha, you can count on me, Yuri~ Take the chance you have and do the things you always wanted to."

    show yuri excited2 at right2
    voice audio.yuri_v_alright1a2
    yu "Alright! I’m pumped up! Thanks, Yoshi!"
    yu "I’m going to get my sketchbook and get started right now!"

    show yoshi shock2 at left2
    voice audio.yoshi_v_wait3a
    yo "W-Wait, Yuri…! What about the—"

    hide yuri_xmas
    hide yuri excited2
    with moveoutright

    show yoshi comp6 at left2
    voice audio.yoshi_v_laugh6
    yo "…party."

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black with fade
    yo "{i}Yuri and Goro have always shared such a close bond, and I can tell how much they’ve both sacrificed for each other.{/i}"
    yo "{i}I’m glad Yuri’s finally getting to explore herself a bit more!{/i}"

    $ renpy.pause (2.0, hard=True)
    yo "{i}After Yuri ran off, I went over to Goro and chatted with him and the scouts for the rest of the night.{/i}"

    jump day7_goro_aftersq

label day7_goro_lloyd:
    show yoshi happy2 at right
    voice audio.yoshi_v_rush6
    yo "Let’s go have some drinks!"

    show goro play3 at left
    voice audio.goro_v_laugh1a1
    g "Hehe, now we’re talking!"

    show yoshi talk3 at right
    voice audio.yoshi_v_think1a
    yo "I see Lloyd and Darius with Mr. Clermont doing just that over there! Let’s join them!"

    show goro_xmas at p5_1
    show goro norm1 at p5_1
    show yoshi_xmas at p5_2
    show yoshi happy1 at p5_2
    with move

    show william_xmas at p5_3
    show william_pipe at p5_3
    show william norm1 at p5_3
    show lloyd_xmas at p5_4
    show lloyd norm1 at p5_4
    show darius_xmas at p5_5
    show darius norm1 at p5_5
    with dissolve

    voice audio.yoshi_v_goodpm1
    yo "Good evening! Mind if we join in?"

    show william happy2 at p5_3
    voice audio.william_v_yoshi2b
    w "Ah, Yoshinori, Goro, please take a seat!"

    show lloyd happy1 at p5_4
    voice audio.lloyd_v_shock1a1
    l "We were just chatting with Mr. Clermont about our time as Camp Buddy scouts!"

    show darius relief2 at p5_5
    voice audio.darius_v_laugh1
    d "That and having booze."

    show william play4 at p5_3
    voice audio.william_v_laugh1
    w "Isn’t it amusing to see a bunch of grown men in such costumes enjoying a tall glass of beer?"

    show goro sigh1 at p5_1
    voice audio.goro_v_sigh1a
    g "*sigh* I hope it’s not too unbecoming of your prestigious reputation, sir."

    show william play2 at p5_3
    voice audio.william_v_fine1b
    w "Come now, Goro. We’re outside the workspace, we can be more personal and call each other by our names!"

    show goro comp2 at p5_1
    voice audio.goro_v_thanks2b1
    g "Th-Thank you, sir, but it would feel far too inappropriate…"

    show william laugh1 at p5_3
    voice audio.william_v_alright1b
    w "Haha, whatever you like, then! "

    show william happy2 at p5_3
    voice audio.william_v_anyway1
    w "Anyway, I was just chatting with Lloyd and Darius here about how fortunate we were to find them!"
    w "Would you believe it was less than a day after we posted the application that they responded?"

    show yoshi shock2 at p5_2
    voice audio.yoshi_v_shock1a
    yo "Whoa! Really?!"

    show william happy3 at p5_3
    voice audio.william_v_agree4a
    w "Yes! From my understanding, Lloyd was quite eager to return here in particular."

    show darius happy1 at p5_5
    voice audio.darius_v_conj1a1
    d "It’s true."

    show lloyd bold2 at p5_4
    voice audio.lloyd_v_agree2b1
    l "Yeah! It was actually destined from way before!"

    show goro confused2 at p5_1
    voice audio.goro_v_think1d1
    g "Hmm? How so?"

    show lloyd explain4 at p5_4
    voice audio.lloyd_v_conj1a3
    l "Well, Dar and I had just finished a really crappy job right before the posting."
    l "I was telling him that I wanted to do something more meaningful, and figured I should consult my tarots! "

    show william play2 at p5_3
    voice audio.william_v_oh3
    w "Oh, you’re an occult fan, Lloyd?"

    show lloyd excited3 at p5_4
    voice audio.lloyd_v_agree5a
    l "Yes, sir! I absolutely LOVE it!"

    show darius play2 at p5_5
    voice audio.darius_v_cute1
    d "He’s a fanatic."

    show william laugh2 at p5_3
    voice audio.william_v_laugh3
    w "Haha! That’s quite fascinating."

    show lloyd happy1 at p5_4
    voice audio.lloyd_v_conj2a2
    l "Anyway, when I was trying to get my cards out, I stumbled on my old badge collection from Camp Buddy."
    l "I hadn’t seen it in years and I had a crazy thought…"

    show lloyd excited1 at p5_4
    voice audio.lloyd_v_stars1b1
    l "Maybe I could use it for a divination!"

    show goro think3 at p5_1
    voice audio.goro_v_think3
    g "I literally never thought the badges would be used like that…"

    show lloyd explain6 at p5_4
    voice audio.lloyd_v_ignored1a1
    l "*ehem* So I started stacking up the patches like a deck of cards, and drew three to foretell my fate."
    l "Lo and behold, it showed me the ‘Camping’ badge, the ‘Buddy’ badge, and my ‘Crafting badge’! "

    show darius explain3 at p5_5
    voice audio.darius_v_think1a1
    d "Which are the only three badges you earned."

    show lloyd annoy2 at p5_4
    voice audio.lloyd_v_angry1a1
    l "Shush, Dar."
    l "I knew it must’ve a sign! My future showed that I would be ‘Crafting in Camp Buddy’!"

    show yoshi confused2 at p5_2
    voice audio.yoshi_v_really6
    yo "H-How else could you have read that…?"

    show lloyd rage3 at p5_4
    voice audio.lloyd_v_annoyed1b4
    l "Let me finish!"
    l "After that, I searched for Camp Buddy on the internet, and the first thing that popped up was Mr. Clermont’s job opening! "

    show darius laugh1 at p5_5
    voice audio.darius_v_laugh2a
    d "He came running and screaming to see me as soon as he saw it."

    show lloyd amazed3 at p5_4
    voice audio.lloyd_v_amazed2a1
    l "I couldn’t help it! It was more perfectly-timed than any reading I’ve ever had! "

    show yoshi awkward3 at p5_2
    voice audio.yoshi_v_uh1a
    yo "I don’t think it was even a reading…"

    show lloyd rage1 at p5_4
    voice audio.lloyd_v_denial2a1
    l "It definitely was! How else could you explain all those things happening?! "

    show william laugh1 at p5_3
    voice audio.william_v_laugh4
    w "Hahaha! Well, maybe it really was fate then that landed you here!"

    show lloyd laugh1 at p5_4
    voice audio.lloyd_v_agree2b1
    l "Yes, sir! I really believe it was!"

    show william happy3 at p5_3
    voice audio.william_v_well1c
    w "Well, let’s have a toast then! To the whims of fate!"

    show goro_xmas at p6_1
    show goro shock1 at p6_1
    show yoshi_xmas at p6_2
    show yoshi shock1 at p6_2
    show william_xmas at p6_3
    show william_pipe at p6_3
    show william shock1 at p6_3
    show lloyd_xmas at p6_4
    show lloyd shock1 at p6_4
    show darius_xmas at p6_5
    show darius shock1 at p6_5
    with move

    show yoichi_xmas at p6_6
    show yoichi angry1 at p6_6
    voice audio.yoichi_v_william1a
    yi "Aha! So, you’re the one who took my booze, Snow-BALLS!" with vpunch

    show william think2 at p6_3
    voice audio.william_v_oh3
    w "I believe he is referring to me."

    show yoshi angry2 at p6_2
    voice audio.yoshi_v_yoichi7
    yo "Y-Yoichi! Call him Mr. Clermont!"

    show yoichi playful1 at p6_6
    voice audio.yoichi_v_question1a5
    yi "Why not? He’s Snowball’s dad, and it’s what he looks like!"

    show william confused3 at p6_3
    voice audio.william_v_think4
    w "Are you referring to my son, Felix?"

    show goro shy6 at p6_1
    voice audio.goro_v_yoichi2a
    g "A-Ah, Yoichi here just likes to give out nicknames to people he likes, sir…"

    show yoichi laugh2 at p6_6
    voice audio.yoichi_v_agree1b1
    yi "Yeah! That’s Frogboy, he’s Geezer, and that’s Buttcheeks and Sheriff Brokeback!"

    show yoshi sigh1 at p6_2
    voice audio.yoshi_v_sigh3a
    yo "*sigh* This is embarrassing…"

    show william laugh2 at p6_3
    voice audio.william_v_laugh3
    w "Hahaha! What a fun idea! Tell me all the other nicknames you have, lad! "

    show yoichi grin1 at p6_6
    voice audio.yoichi_v_laugh1a1
    yi "Pour me a drink and you got it!"

    show goro shy4 at p6_1
    voice audio.goro_v_sigh1a
    g "So much for a peaceful evening…"

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black with fade
    yo "{i}Lloyd claimed it was all due to ‘fortune’, but it was clear he was the captain of his own destiny.{/i}"
    $ renpy.pause (2.0, hard=True)
    yo "{i}Goro and I ended up spending the evening drinking with Mr. Clermont, Lloyd and Darius, while the rest of the scouts ate and played games.{/i}"

    jump day7_goro_aftersq

label day7_goro_jin:
    $sq_jin += 1
    show yoshi relief2 at right
    voice audio.yoshi_v_think4
    yo "Let’s just chill out for a while."

    show goro play2 at left
    voice audio.goro_v_laugh1a1
    g "Hehe, I figured you’d want to relax, especially after working up a sweat."

    show yoshi talk1 at right
    voice audio.yoshi_v_sigh3a
    yo "It’s not easy being a receiver, you know… Especially with someone your size."

    show goro relief2 at left
    voice audio.goro_v_no2a1
    g "Nonsense. You’re already used to it."

    show jin_xmas at p9_9
    show jin fudan1 at p9_9
    with moveinright

    voice audio.jin_v_hngh1b
    j "Hngh…"

    show yoshi happy2 at right
    voice audio.yoshi_v_confident2
    yo "We should try switching it up sometimes, though… I want to be able to do it to you too."

    show jin fudan2 at p9_9
    voice audio.jin_v_fudan1a2
    j "Do… it…?"

    show goro bored1 at left
    voice audio.goro_v_no1a1
    g "No thanks. I prefer giving rather than taking. I’m generous like that."

    show yoshi sigh4 at right
    voice audio.yoshi_v_rush3
    yo "*sigh* Come on, Goro. Just once, let me try it too."

    show goro tease2 at left
    voice audio.goro_v_well2a
    g "Well, if you’re going to beg like that."

    show jin perv5 at p9_9
    voice audio.jin_v_fudan4a1
    j "Beg for daddy…"

    show yoshi confused2 at right
    voice audio.yoshi_v_uh1a
    yo "Uh… Why is Jin peeking over there?"

    show goro talk3 at left
    voice audio.goro_v_jin5a
    g "Hello, Jin. What are you doing?"

    show jin shock3 at p9_9
    voice audio.jin_v_worry1c1
    j "O-Oh no, I’ve been spotted…!"

    show goro happy2 at left
    voice audio.goro_v_rush2a2
    g "Come over here. I want to see your costume."

    show jin shy2 at p9_9
    voice audio.jin_v_gulp1a
    j "*gulp* A-Alright…"

    show jin_xmas at center
    show jin shy2 at center
    with move

    show goro play2 at left
    voice audio.goro_v_agree2a1
    g "Ah, would you look at that. This angel outfit really shows off your innocence."

    show jin perv6 at center
    show jin_nosebleed at center
    voice audio.jin_v_think2a1
    j "I-I beg to differ…"

    show yoshi worry2 at right
    voice audio.yoshi_v_jin5
    yo "Jin, is your nose bleeding again…?"

    show jin daydream2 at center
    voice audio.jin_v_comp8b1
    j "I-I’m fine, I’m just getting woozy from the view."
    j "Sir Goro’s costume just looks so hot— I mean, cool!"

    hide jin_nosebleed
    show goro_xmas at p5_1
    show goro norm1 at p5_1
    show jin_xmas at p5_2
    show jin daydream2 at p5_2
    show yoshi_xmas at p5_3
    show yoshi norm1 at p5_3
    with move

    show taiga_xmas at p5_4
    show taiga talking4 at p5_4
    show keitaro_xmas at p5_5
    show keitaro normal1 at p5_5
    with dissolve

    voice audio.taiga_v_heh1
    t "Hah! If you think that’s cool then you should’ve seen what I wore last summer!"

    show keitaro talking1 at p5_5
    voice audio.keitaro_v_greeting1
    k "Hello, Sir Goro and Scoutmaster Yoshi! "

    show goro confused3 at p5_1
    voice audio.goro_v_goodpm2a1
    g "Good evening, you two. Not hanging out with your friends?"

    show taiga playful1 at p5_4
    voice audio.taiga2_v_disagree1c
    t "Nahhh. Hanging out with those dorks over the weekend was already enough for me."

    show keitaro worry1 at p5_5
    voice audio.keitaro_v_taiga4
    k "Ssssh, Taiga! Hiro and Yoichi might hear you…!"

    show jin shock2 at p5_2
    voice audio.jin_v_wait2a
    j "W-Wait, wait… Did you have a costume party during the summer too?!"

    show keitaro talking1 at p5_5
    voice audio.keitaro_v_agree1
    k "Yeah! It was just like this where Ms. Yuri had costumes ready for everyone!"

    show taiga confident3 at p5_4
    voice audio.taiga_v_heh1
    t "Heh, I’m pretty proud to say I made mine, though~ "

    show yoshi laugh1 at p5_3
    voice audio.yoshi_v_laugh1
    yo "Haha, you should know Taiga’s quite the crafty scout!"

    show goro think2 at p5_1
    voice audio.goro_v_think1a1
    g "Didn’t you add some custom body paint as well?"

    show taiga talking4 at p5_4
    voice audio.taiga_v_boastful1
    t "My idea was sort of a savage warrior, and it was super dope!"

    show jin shock5 at p5_2
    voice audio.jin_v_whoa3a
    j "Wow… That sounds… wild…"

    show jin upset5 at p5_2
    voice audio.jin_v_hngh4c
    j "Hnnghhh… I can’t believe I missed out…"
    j "Now I’m really curious how that party went."

    show keitaro laugh1 at p5_5
    voice audio.keitaro_v_laugh2
    k "Hehe, I’d say it was pretty fun! I have lots of memories about it!"

    show jin happy1 at p5_2
    voice audio.jin_v_conj2c1
    j "W-Well, if you’re interested, we could write a blog post for it too!"

    show taiga confused1 at p5_4
    voice audio.taiga2_v_surprised1c
    t "Oh, you have your own blog?"

    show jin comp3 at p5_2
    voice audio.jin_v_denial2b1
    j "Not exactly. It’s actually for Camp Buddy. "

    show yoshi happy2 at p5_3
    voice audio.yoshi_v_yeah2
    yo "We’re actually chronicling the memories going all the way back to my term as a scout to post on there!"

    show keitaro amazed1 at p5_5
    voice audio.keitaro_v_oh3
    k "Ohhh, is it like a digital journal?"

    show jin happy2 at p5_2
    voice audio.jin_v_conj4b1
    j "Yes! Do you want to help? I’d love to hear more about the party!"

    show jin daydream2 at p5_2
    voice audio.jin_v_laugh2c
    j "Especially the costumes…"

    show keitaro talking1 at p5_5
    voice audio.keitaro_v_agree2
    k "Yeah! Taiga and I like to write too!"
    k "Where do we even start though…?"

    show taiga playful1 at p5_4
    voice audio.taiga2_v_teasing1b
    t "Let’s start with Sir Goro’s costume, he wore the lamest one out of everyone! Hahaha!"

    show goro explain2 at p5_1
    voice audio.goro_v_ehem1a
    g "*ehem* You should know that panda onesie was a back-up costume."

    show yoshi think2 at p5_3
    voice audio.yoshi_v_yeah4
    yo "Oh, yeah…! You had a much more risqué one you were supposed to wear…"

    show jin perv2 at p5_2
    voice audio.jin_v_really2b
    j "R-Risque? I’m listening…"

    show goro tease3 at p5_1
    voice audio.goro_v_well2a
    g "Well, I did end up showing it during the after party. I’m sure you remember, Yoshinori."

    show yoshi awkward2 at p5_3
    voice audio.yoshi_v_gulp1a
    yo "*gulp*"

    show jin fudan2 at p5_2
    voice audio.jin_v_hngh2a
    j "Hnghh! An after party?!"

    show jin fudan3 at p5_2
    voice audio.jin_v_fudan1a3
    j "L-Let me get my laptop and we’ll get started!"

    $renpy.choice_for_skipping()
    scene cg white with Dissolve(2.0)
    $ quick_menu = False
    $ say_box = False
    hide screen location
    hide screen timeline
    hide screen quick_menu
    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    $ global minigame_id
    $ minigame_id = 'jmG4'
    $ renpy.call(minigame_id)

label day7_goro_postmg:
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

    $ location = location_shed
    $ day = "??"
    $ time = timeline_timenight
    $ season = season_summer
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_shed_night with fade
    play music old_familiar_home loop
    play bgsound sfxloop_night loop

    show aiden_costume at left
    show aiden drunk6 at left
    show yoshi_costume at center
    show yoshi drunk1 at center
    show goro2_costume at right
    show goro2 drunk5 at right
    voice audio.aiden_v_relief2a
    a "Fwahhh! You really brought out the good stuff tonight, Gramps!"

    show goro2 drunk2 at right
    voice audio.goro_v_heh1a
    g "Heh, it’s a celebration after all. No reason not to drink my finest booze."

    show aiden laugh3 at left
    voice audio.aiden_v_drunk2c1
    a "Hahaha! I could get drunk on this stuff every night! Damn, it’s tasty!"

    show yoshi worry2 at center
    voice audio.yoshi_v_aiden10
    a "A-Aiden, shh! If Yuri finds us out here, she’ll kill us!"

    show aiden drunk3 at left
    voice audio.aiden_v_aww2b
    a "Aww, come on, Yoshi, relax! She’s already in bed! "
    a "We deserve this break, anyway. We just worked super hard on the fundraiser all week long!"

    show goro2 angry3 at right
    voice audio.goro_v_annoyed3b1
    g "You two quit chit-chatting and get back to the game. Don’t think I’ll let you quit while I’m winning!"

    show aiden drunk5 at left
    voice audio.aiden_v_agree4a
    a "Haha, you’re right, Gramps. A couple more rounds and you’ll have Yoshi and I stripped bare."

    show yoshi annoy3 at center
    voice audio.yoshi_v_disagree1b
    yo "It’ll take you way longer than that, Aiden! Your costume has too many layers!"

    show aiden drunk2 at left
    voice audio.aiden_v_perv1
    a "You’re not wrong, but do these layers really count? Ya’ll can already see my dick and I’m still fully clothed."

    show goro2 angry4 at right
    voice audio.goro_v_rush2b1
    g "Come on, show your hands already! I’m at seven."

    show aiden bold2 at left
    voice audio.aiden_v_laugh1b2
    a "Hah! I’ve got nine."

    show yoshi drunk6 at center
    voice audio.yoshi_v_laugh1
    yo "Twelve for me, so looks like I win!"

    show goro2 disappoint4 at right
    voice audio.goro_v_swear1a
    g "Damn!"

    show aiden laugh4 at left
    voice audio.aiden_v_laugh2b1
    a "Hahaha! So much for your winning streak, Gramps!"
    a "And speaking of streak, come on! Off with the onesie!"

    show goro2 shock1 at right
    g "...!"

    show yoshi awkward4 at center
    voice audio.yoshi_v_unsure2a
    yo "A-Aiden, is it really fair to make him do that since he’s only wearing one thing…?"

    show aiden tease1 at left
    voice audio.aiden_v_agree1b2
    a "Yup! He agreed to the rules! Besides, what’s the problem? You ain’t naked under there are you Gramps?"

    show goro2 shy4 at right
    voice audio.goro_v_ehem1a
    g "*ehem* No, but—"

    show aiden bold5 at left
    voice audio.aiden_v_no1a1
    a "No buts! Get rid of the onesie!"

    show goro2 shy6 at right
    voice audio.goro_v_response3a1
    g "Fine."

    hide goro2_costume
    hide goro2 shy6
    show goro2_costume2 at right
    show goro2 shy5 at right
    with dissolve

    show yoshi shock4 at center
    voice audio.yoshi_v_shock3
    yo "GAH!"

    show aiden shock3 at left
    voice audio.aiden_v_shock1b1
    a "WHOA! What the hell is that, Gramps?!"

    show goro2 sigh4 at right
    voice audio.goro_v_sigh2a
    g "*sigh* This is the costume I had originally picked out… I intended it to be a match with Yoshinori."
    g "I thought about wearing it to the party, but Yuri didn’t want anyone to see me like this."

    show aiden drunk2 at left
    voice audio.aiden_v_laugh1b2
    a "So instead, you were sneaking around in it under a blanket. Kinky~"

    show goro2 angry2 at right
    voice audio.goro_v_insult2b1
    g "Th-That’s not what it was for, you brat!"

    show yoshi shy1 at center
    yo "..."

    show aiden tease2 at left
    voice audio.aiden_v_laugh3a
    a "Pfft, something on your mind, Yoshi~?"

    show yoshi awkward4 at center
    voice audio.yoshi_v_huh4b
    yo "H-Huh? What?"

    show aiden drunk6 at left
    voice audio.aiden_v_rush1b1
    a "I know Gramps’ costume is some serious eye candy, but we got another round to play! Quit staring and let’s go!"

    show yoshi angry3 at center
    voice audio.yoshi_v_agree2b1
    yo "A-Aiden! I wasn’t… but fine! Let’s go!"

    show aiden excited1 at left
    voice audio.aiden_v_alright1a3
    a "Alright! Final round, so loser drinks what’s left in the bottle AND has to do what the winner says!"

    show yoshi sigh4 at center
    voice audio.yoshi_v_sigh3a
    yo "*sigh* Aiden, you’re really drunk now, aren’t you?"

    show aiden laugh2 at left
    voice audio.aiden_v_agree1b1
    a "Yup! But I’m doing you a favor and letting you pick which of our hot bods you want on your plate tonight~"

    show yoshi angry2 at center
    voice audio.yoshi_v_aiden10
    yo "A-Aiden!"

    show goro2 sigh1 at right
    voice audio.goro_v_sigh2a
    g "*sigh*"

    show aiden drunk6 at left
    voice audio.aiden_v_drunk2b1
    a "*hic* Now read ’em and weep! I got a… a…"

    show aiden sleepy4 at left
    voice audio.aiden_v_yawn1
    a "*snores*"

    play sound sfx_bodydrop
    hide aiden_costume
    hide aiden sleepy4
    with moveoutbottom

    show yoshi shock2 at center
    voice audio.yoshi_v_shock3
    yo "Gah! Is he alright?!"

    show goro2 play2 at right
    voice audio.goro_v_heh1a
    g "Heh, looks like he passed out. That boy can never handle his liquor."

    show yoshi sigh4 at center
    voice audio.yoshi_v_sigh3a
    yo "*sigh* I guess we should get him to bed then."

    show goro2 tease2 at right
    voice audio.goro_v_wait3c1
    g "Not so fast, Yoshinori. I believe we have a game to finish."

    show yoshi awkward4 at center
    voice audio.yoshi_v_but3
    yo "Eh? B-But sir, that was just Aiden—"

    show goro2 tease5 at right
    voice audio.goro_v_rush2a2
    g "Come on, Yoshinori. Chickening out now?"

    show yoshi shy6 at center
    voice audio.yoshi_v_unsure2b
    yo "N-No, sir! I-I guess we can keep playing…"

    show goro2 bold2 at right
    voice audio.goro_v_alright1b1
    g "Alright! I’ve got ten. And you?"

    show yoshi worry2 at center
    voice audio.yoshi_v_uh1a
    yo "Two…"

    show goro2 laugh1 at right
    voice audio.goro_v_heh3a
    g "Hah! Looks like I pulled through for the win. "
    g "Guess you’re doing whatever I say now, Yoshinori."

    show yoshi shock3 at center
    voice audio.yoshi_v_what4
    yo "Wh-What?! But that was just Aiden’s drunk idea! We never—"

    show goro2_costume2 at right2
    show goro2 drunk2 at right2
    with move

    voice audio.goro_v_comp2a1
    g "Don’t worry, Yoshinori. I’ll cover half of your bet."
    g "*swigs the alcohol*"

    show yoshi panic4 at center
    voice audio.yoshi_v_sir3
    yo "S-Sir!"

    show goro2 bold5 at right2
    voice audio.goro_v_relief1a
    g "Hahhhh! So, now that I’ve taken care of that, it looks like you owe me. "

    show yoshi awkward2 at center
    voice audio.yoshi_v_gulp1a
    yo "*gulp*"

    show goro2 tease3 at right2
    voice audio.goro_v_yoshi14b
    g "Come on, cowboy. Let’s see how you handle a hot-blooded bull."

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

    jump day7_goro_mg4

label day7_goro_postfb:
    $ location = location_messhall
    $ day = "82"
    $ time = timeline_timenight
    $ season = season_winter
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_messhall_winter_night_xmas with fade
    play music buddy_oath_holiday loop
    play bgsound sfxloop_crowd loop

    show goro_xmas at p5_1
    show goro norm3 at p5_1
    show jin_xmas at p5_2
    show jin_blush2 at p5_2
    show jin_nosebleed at p5_2
    show jin dizzy2 at p5_2
    show yoshi_xmas at p5_3
    show yoshi awkward1 at p5_3
    show taiga_xmas at p5_4
    show taiga normal3 at p5_4
    show keitaro_xmas at p5_5
    show keitaro compassion2 at p5_5
    voice audio.jin_v_whoa3a
    j "A s-secret strip show…"

    show keitaro compassion3 at p5_5
    voice audio.keitaro_v_surprised7
    k "I-I didn’t think you guys were up to something like that…"

    show taiga playful2 at p5_4
    voice audio.taiga2_v_boastful1c
    t "Somehow, I think you’re both cooler now."

    show keitaro surprised2 at p5_5
    voice audio.keitaro_v_taiga5
    k "Taiga!"

    show goro explain2 at p5_1
    voice audio.goro_v_ehem1a
    g "*ehem* Well, once we’ve had a few drinks, things tend to get a little ‘looser.’"

    show goro tease5 at p5_1
    voice audio.goro_v_heh1a
    g "Heh, right Yoshinori?"

    show yoshi shock3 at p5_3
    voice audio.yoshi_v_shock3
    yo "Gah!"

    show jin fudan3 at p5_2
    voice audio.jin_v_hngh1a
    j "Hngh!"

    show taiga sigh2 at p5_4
    voice audio.taiga_v_sigh1
    t "*sigh* These two aren’t very subtle with their innuendos."

    show keitaro confused3 at p5_5
    voice audio.keitaro_v_question7
    k "Eh? What was it?"

    show taiga annoyed4 at p5_4
    voice audio.taiga2_v_confused1a
    t "Seriously, Keitaro?"

    show yoshi awkward4 at p5_3
    voice audio.yoshi_v_anyway3a
    yo "A-Anyway, I think Jin has enough information! Thanks for helping, you two!"

    show keitaro laugh1 at p5_5
    voice audio.keitaro_v_agree5a
    k "No problem, Scoutmaster Yoshi!"

    show goro happy2 at p5_1
    voice audio.goro_v_rush2a1
    g "Come on, let’s all get back to the party. "

    show taiga playful1 at p5_4
    voice audio.taiga2_v_boastful1c
    t "And get Jin some tissues for whatever other ‘fluids’ he needs to get rid of."

    scene cg black with fade
    yo "{i}After working on the blog, we all headed to get some snacks and told Jin more stories about the previous term.{/i}"
    yo "{i}Eventually, after we finished, we joined the rest of the group and partied for the remainder of the evening!{/i}"

    jump day7_goro_aftersq

label day7_goro_aftersq:
    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black
    hide screen location
    hide screen timeline
    hide screen quick_menu
    $quick_menu = False
    with fade
    $persistent.profile_unlock.append("cameos")
    play sound sleeping_time
    $ time_transition_night_to_day_winter2()
    $ renpy.pause (2.0, hard=True)
    jump day8_goro
