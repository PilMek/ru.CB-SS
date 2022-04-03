label day7_aiden:
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
    show aiden2_sleep at p5_5
    show aiden2 sleepy4 at p5_5
    show goro_sleep at p5_4
    show goro norm2 at p5_4
    show jin_sleep at p5_3
    show jin_glasses at p5_3
    show jin norm1 at p5_3
    voice audio.aiden_v_yawn1
    a "*yawn*"

    hide aiden2_sleep
    hide aiden2 sleepy4
    show aiden_sleep at p5_5
    show aiden talk3 at p5_5
    voice audio.aiden_v_guys2b
    a "Oh hey, guys! Good morning! You’re all up early!"

    show goro happy1 at p5_4
    voice audio.goro_v_goodam1a1
    g "Good morning, Aiden."

    hide aiden_sleep
    hide aiden talk3
    show aiden2_sleep at p5_5
    show aiden2 confused2 at p5_5
    voice audio.aiden_v_confused1a2
    a "Eh? What’s going on over there?"

    show goro explain2 at p5_4
    voice audio.goro_v_actually1a
    g "Lloyd is doing some palm reading while we’re drinking coffee to start our day."

    hide aiden2_sleep
    hide aiden2 confused2
    show aiden_sleep at p5_5
    show aiden happy1 at p5_5
    voice audio.aiden_v_oho1a
    a "Oh~ Sounds interesting."

    show jin perv2 at p5_3
    voice audio.jin_v_gulp1a
    j "N-Not gonna lie, this is probably the longest time a guy has held my hand."

    show lloyd happy1 at p5_2
    voice audio.lloyd_v_aiden1c
    l "Hey, Aiden! Let me read yours! "

    show jin_sleep at p5_2
    show jin_glasses at p5_2
    show jin perv2 at p5_2
    show goro_sleep at p5_3
    show goro explain2 at p5_3
    show lloyd_sleep at p5_4
    show lloyd think1 at p5_4
    with move

    hide lloyd_sleep
    hide lloyd think1
    show lloyd_sleep at p5_4
    show lloyd think1 at p5_4
    voice audio.lloyd_v_think1a1
    l "Hmm… You seem to have a broken lifeline…"

    show aiden panic4 at p5_5
    voice audio.aiden_v_what4a
    a "What?! Broken?! Does that mean I’m gonna die?! "

    show lloyd shock3 at p5_4
    voice audio.lloyd_v_disagree1c1
    l "N-No! A lifeline is the part of the hand between the index finger and thumb, making a curve below the thumb."

    hide aiden_sleep
    hide aiden panic4
    show aiden2_sleep at p5_5
    show aiden2 worry2 at p5_5
    voice audio.aiden_v_confused1c2
    a "Eh…? But the name sounds really bad…"

    show lloyd comp5 at p5_4
    voice audio.lloyd_v_comp1b1
    l "Relax! It just means that it reflects losses, struggles, unexpected changes, and interruptions in a person’s lifestyle."
    l "Thinking about it, it makes sense, right?! Because you weren’t used to the hotel lifestyle before! "

    show jin shock2 at p5_2
    voice audio.jin_v_whoa1c
    j "Whoa! He’s right! That’s amazing!"

    hide aiden2_sleep
    hide aiden2 worry2
    show aiden_sleep at p5_5
    show aiden awkward2 at p5_5
    voice audio.aiden_v_response2a1
    a "Ah, gotcha…!"

    hide goro_sleep
    hide goro explain2
    show goro2_sleep at p5_3
    show goro2 confused5 at p5_3
    voice audio.goro_v_unsure1a1
    g "Not sure if this is just a youngster’s thing… But is it really alright for you guys to be basing your ‘destiny’ and ‘future’ on the creases of your hands…?"

    show darius play2 at p5_1
    voice audio.darius_v_lloyd1
    d "Lloyd is doing it for fun. I just like to play along."
    d "Listening to his magic first thing in the morning is entertaining with hot cocoa."

    show lloyd annoy2 at p5_4
    voice audio.lloyd_v_greet2c2
    l "Heyyy! There are plenty of studies that discuss these mystic energies! It’s totally legit!"

    show darius play5 at p5_1
    voice audio.darius_v_agree1a
    d "Yes, I believe you."

    show lloyd bold2 at p5_4
    voice audio.lloyd_v_laugh1a1
    l "Besides, it’s a nice ice breaker~!"

    show aiden talk1 at p5_5
    voice audio.aiden_v_yeah2a1
    a "By the way, where’s Yoshi? He’d normally still be asleep, but it looks like he’s already left."

    hide goro2_sleep
    hide goro2 confused5
    show goro_sleep at p5_3
    show goro talk3 at p5_3
    voice audio.goro_v_oh1a
    g "Oh, he went out not too long before you got up. I’m not sure what for though…"

    show jin think5 at p5_2
    voice audio.jin_v_think1a1
    j "He did seem to be in a hurry… He didn’t even drink his coffee… "

    show aiden comp2 at p5_5
    voice audio.aiden_v_laugh1b2
    a "Hehe, knowing Yoshi, maybe he’s already getting a head start and working on the site."
    a "Though I gotta say, I’m pretty surprised you’re up at a normal-person schedule, Jin."

    show jin comp3 at p5_2
    voice audio.jin_v_ah2a
    j "A-Ahh... Yeah… It’s still been kind of difficult, but Sir Goro suggested I try a morning coffee, and that’s helped a lot."

    show goro relief2 at p5_3
    voice audio.goro_v_relief1a
    g "I can’t work well without it, so I thought it’d give Jin a boost."

    show lloyd talk2 at p5_4
    voice audio.lloyd_v_sus1a1
    l "It’s crazy to me that you’re drinking yours iced, considering how cold it is outside, Jin! You sure are tougher than you look."

    show jin confuseddn2 at p5_2
    voice audio.jin_v_think2a1
    j "I believe drinking scalding black coffee alone with no cream or sugar like Sir Goro is a lot more concerning… "

    hide goro_sleep
    hide goro relief2
    show goro2_sleep at p5_3
    show goro2 explain4 at p5_3
    voice audio.goro_v_ehem1a
    g "*ehem* I prefer it this way. "

    show aiden tired1 at p5_5
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
    show goro_sleep at p5_3
    show goro talk1 at p5_3
    voice audio.goro_v_conj7a
    g "On that note, I guess we should get dressed and start our day as well. "

    show aiden happy1 at p5_5
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
    show goro_winter2 at p5_4
    show goro norm1 at p5_4
    show aiden_winter2 at p5_5
    show aiden norm1 at p5_5
    show jin_winter at p5_3
    show jin_glasses at p5_3
    show jin norm1 at p5_3
    show lloyd_winter2 at p5_2
    show lloyd happy1 at p5_2
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
    voice audio.yoshi_v_yessir1
    yo "Yes, sir. I figured we could really use the extra hands to get things done, so I called Yoichi and Taiga yesterday."

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

    show goro_winter2 at p12_4
    show goro sigh1 at p12_4
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

    show darius_winter2 at p12_2
    show darius norm1 at p12_2
    show jin_winter at p12_3
    show jin_glasses at p12_3
    show jin norm1 at p12_3
    show lloyd_winter2 at p12_1
    show lloyd happy1 at p12_1
    with dissolve

    show goro_winter2 at p12_1
    show goro sigh1 at p12_1
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
    show lloyd_winter2 at p12_2
    show lloyd happy1 at p12_2
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
    voice audio.taiga_v_agree3a
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
    show goro_winter2 at p6_3
    show goro norm1 at p6_3
    show hunter_winter2 at p6_2
    show hunter smile1 at p6_2
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
    hide hunter_winter2
    hide hunter worry1
    show hunter_winter2 at p6_2
    show hunter worry1 at p6_2
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
    show goro2 talk2 at p6_3
    voice audio.goro_v_ehem1a
    g "*ehem* Let’s not get too sentimental, we still have a lot of work to do."

    show yoshi laugh2 at p6_6
    voice audio.yoshi_v_laugh1
    yo "Hahaha! You’re not really used to the compliments, huh sir?"

    show jin daydream2 at p6_1
    voice audio.jin_v_fudan3a1
    j "C…Cute…"

    show hunter talking1 at p6_2
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
    hide goro2 talk2
    show goro_winter2 at p6_3
    show goro laugh5 at p6_3
    hide hunter_winter2
    hide hunter confused1
    show hunter_winter2 at p6_2
    show hunter confused1 at p6_2
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
    hide hunter_winter2
    hide hunter confused1
    show hunter_winter2 at p6_2
    show hunter confused1 at p6_2
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
    show keitaro_winter2 at p11_6
    show keitaro sigh2 at p11_6
    show natsumi_winter at p11_8
    show natsumi normal2 at p11_8
    show hunter_winter2 at p11_7
    show hunter normal1 at p11_7
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
    show jin think2 at p11_4
    show jin_glasses at p11_4
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
    show jin think2 at p11_4
    show jin_glasses at p11_4
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
    #voice audio.hiro_v_hey1b1
    voice audio.hiro_v_wait1a
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

    show darius excited4 at p12_2
    #jey
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
    play music brand_new_day_winter loop

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

    show emilia_sleep at left2
    show emilia eyeroll3 at left2
    show yoshi_winter at right2
    show yoshi shock2 at right2
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
    play music brand_new_day_winter
    scene bg_gororoom_winter_sunset with fade

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
    g "Our intent was to let Ms. Komarova recover, then inform you."

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

    show william shock2 at p4_3
    voice audio.william_v_agree4c
    w "Yes?"

    show goro talk1 at p4_4
    voice audio.goro_v_comp1d1
    g "I understand your decision to remove Ms.  Komarova as our inspector."
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
    yo "A-Ah…! Yes, sir."
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
    show aiden2_winter at p9_9
    show aiden2 scared2 at p9_9
    show darius_winter at p9_8
    show darius shock1 at p9_8
    show jin_winter at p9_6
    show jin_glasses at p9_6
    show jin awkward2 at p9_6
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
    yu "Come onnn!!! We rarely have this many people around during the winter season! And besides, the holidays are just around the corner!"
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
    hide lloyd_winter
    hide lloyd hungry4
    hide goro_winter
    hide goro excited3
    hide jin_winter
    hide jin_glasses
    hide jin sleepy3
    hide aiden_winter
    hide aiden bold2
    hide william_winter
    hide william play2
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
    show yoshi norm1 at p7_1
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
    show hiro surprised3 at p8_3
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

    hide lloyd_xmas
    hide lloyd sad4
    show lloyd_xmas at p4_2
    show lloyd sad4 at p4_2
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
    hide yuri_xmas
    hide yuri tease2
    show yuri_xmas at p4_3
    show yuri tease2 at p4_3
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

    show goro_xmas at p6_1
    show goro shy6 at p6_1
    with dissolve

    hide jin_xmas
    hide jin dizzy3
    show jin_xmas at p6_2
    show jin dizzy3 at p6_2
    voice audio.goro_v_yuridear4a
    g "Uhh… Dear… I think the outfit you gave me is a tad small…"
    g "Why can’t you just let me wear the costume I had from the last party?"

    show yuri angry3 at p6_5
    voice audio.yuri_v_no1a1
    yu "No way! That was such a missed opportunity! "
    yu "I could’ve made you wear something much better like a grunge leather daddy, a gladiator, or a caveman! Ugh… the wasted potential!"

    show yuri bold2 at p6_5
    voice audio.yuri_v_laugh1b1
    yu "I made sure not to make the same mistake again! You’re keeping that on, whether you like it or not!"

    show goro sigh4 at p6_1
    voice audio.goro_v_sigh1a
    g "*sigh* This is rather embarrassing, especially considering Mr. Clermont is attending this party…"

    show goro_xmas at p7_2
    show goro sigh4 at p7_2
    show jin_xmas at p7_3
    show jin dizzy3 at p7_3
    show darius_xmas at p7_4
    show darius explain4 at p7_4
    show lloyd_xmas at p7_5
    show lloyd think5 at p7_5
    show yuri_xmas at p7_6
    show yuri bold2 at p7_6
    show yoshi2_autumn at p7_7
    show yoshi2 sigh1 at p7_7
    with move

    show william_xmas at p7_1
    show william excited3 at p7_1
    with dissolve

    voice audio.william_v_excited1
    w "I beg to differ; I’ve never felt so alive! It’s been years since I’ve had this much fun!"

    show goro awkward5 at p7_2
    voice audio.goro_v_william4a
    g "M-Mr. Clermont…?!"

    show william amazed2 at p7_1
    voice audio.william_v_laugh3
    w "Back at the firm everyone is so stiff and formal – I’d love to be around people who can have a good time more often!"

    show yuri bold4 at p7_6
    voice audio.yuri_v_conj2d1
    yu "See? Mr. Clermont knows how to have fun!"

    show goro shy2 at p7_2
    voice audio.goro_v_really4a
    g "S-Sir, I can’t believe you’re really wearing that…"

    show william_xmas at p8_2
    show william amazed2 at p8_2
    show goro_xmas at p8_3
    show goro shy2 at p8_3
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

    show goro sigh1 at p8_3
    voice audio.goro_v_sigh1a
    g "I don’t know how you even find the time, dear…"

    show yuri explain3 at p8_7
    voice audio.yuri_v_jin3a
    yu "It wasn’t just me, Jin helped me plan them out too!"

    show jin scared2 at p8_4
    voice audio.jin_v_yuri3c
    j "Shhh! Don’t throw me under the bus, Yuri!"

    hide yoshi2_autumn
    hide yoshi2 sigh1
    show yoshi_autumn at p8_8
    show yoshi laugh1 at p8_8
    voice audio.yoshi_v_laugh1
    yo "Haha, I think it’s sweet you made these for everyone, Yuri."

    show darius bored5 at p8_5
    voice audio.darius_v_question2b2
    d "Says the guy not in one yet."

    show yoshi awkward4 at p8_8
    voice audio.yoshi_v_well3
    yo "W-Well, I haven’t seen Aiden yet either!"

    show lloyd talk3 at p8_6
    voice audio.lloyd_v_shock1a1
    l "Oh, he’s still cleaning up the kitchen. He really pulled through, cooking the party food at the last minute!"

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
    yu "Anyway, quit stalling! Go get in your costume and fetch Aiden!"

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
    yo "{i}Not wanting to aggravate Yuri, I went into the bathroom and put my costume on before heading to the kitchen to find Aiden…{/i}"

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
    play music go_with_the_flow loop

    show yoshi_xmas at center
    show yoshi happy1 at center
    voice audio.yoshi_v_aiden3
    yo "Hey, Aiden! Are you h—"

    show yoshi_xmas at right2
    show yoshi happy1 at right2
    with move

    show aiden_xmas at left2
    show aiden happy1 at left2
    with dissolve

    voice audio.aiden_v_yoshi3a
    a "Oh, hey Yoshi!"

    show yoshi shock3 at right2
    show yoshi_blush1 at right2
    voice audio.yoshi_v_shock1a
    yo "Whoa! Wh-What are you wearing?!"

    show aiden awkward5 at left2
    voice audio.aiden_v_confused1c1
    a "Eh… I’m not sure… Yuri just told me to put this on."

    hide yoshi_blush1
    show yoshi worry5 at right2
    voice audio.yoshi_v_uh1a
    yo "These costumes really are… something…"

    show aiden sigh2 at left2
    voice audio.aiden_v_agree4b
    a "Tell me about it. Somehow, she managed to make mine even more revealing than last year’s! "

    show yoshi confused3 at right2
    voice audio.yoshi_v_really1
    yo "Can you really say anything is revealing when you’re naked half the time anyway?"

    show aiden laugh2 at left2
    voice audio.aiden_v_laugh2b1
    a "Hahaha! Okay, that’s a fair point. It is a little chilly in this now, though."

    show yoshi comp3 at right2
    show yoshi_blush1 at right2
    voice audio.yoshi_v_conj3b
    yo "Your costumes are consistent, at least. Just like last time, I can see your ‘thing’ bulging so shamelessly…"

    show aiden tease1 at left2
    voice audio.aiden_v_laugh1b2
    a "So, that’s where you’re staring, huh~? Looks like someone’s wanting to get out of his winter blues~  "

    hide yoshi_blush1
    show yoshi shock3 at right2
    show yoshi_blush2 at right2
    voice audio.yoshi_v_shock3
    yo "G-Gah…! "

    show aiden tease2 at left2
    voice audio.aiden_v_tease2b
    a "Not that I blame you though, I’m feeling frisky after a few days too~"
    a "So… How do I look? "

    $working = False
    $shuffle_menu()
    menu():
        a "So… How do I look? {fast}"
        "Very horny.":
            $ working = True
            $ score_bot += 1
            hide yoshi_blush2 at right2
            show yoshi shy6 at right2
            show yoshi_blush1
            voice audio.yoshi_v_well3
            yo "Very horny."

            show aiden tease2 at left2
            voice audio.aiden_v_oho1a
            a "They say looks match what we’re feeling, so why don’t you find out if it’s true~"
        "One-horse open sleigh.":
            $ working = True
            $ score_top += 1
            hide yoshi_blush2 at right2
            show yoshi comp3 at right2
            show yoshi_blush1
            voice audio.yoshi_v_well3
            yo "Like a one-horse open sleigh."

            show aiden tease3 at left2
            voice audio.aiden_v_laugh1a1
            a "Hehe, well I have a free ticket to ride here, just for you~"
        "A breeding stud.":
            $ working = True
            $ score_aiden += 1
            $ score_bot += 1
            hide yoshi_blush2 at right2
            show yoshi shy6 at right2
            show yoshi_blush1
            voice audio.yoshi_v_well3
            yo "You look like a breeding stud."

            show aiden tease1 at left2
            voice audio.aiden_v_yeah2b2
            a "Oh yeah?"
            a "Then why don’t I fill you up?"
        "You look like you're ready for a ride.":
            $ working = True
            $ score_aiden += 1
            $ score_top += 1
            hide yoshi_blush2 at right2
            show yoshi comp3 at right2
            show yoshi_blush1
            voice audio.yoshi_v_well3
            yo "You look like you’re ready for a ride."

            show aiden tease1 at left2
            voice audio.aiden_v_yeah2b2
            a "Oh yeah? "
            a "Is your inner cowboy calling for action?"

    hide yoshi_blush2
    show yoshi awkward5 at right2
    voice audio.yoshi_v_gulp1a
    yo "*gulp*"

    show aiden laugh4 at left2
    voice audio.aiden_v_laugh2c1
    a "I’m supposed to be the reindeer, but you’re the one whose nose is turning red! Hahaha!"

    show yoshi shy2 at right2
    voice audio.yoshi_v_but3
    yo "I-I can’t help it with you looking like that…! It’s driving me crazy!"

    show aiden bold2 at left2
    show aiden_blush1
    voice audio.aiden_v_comeon1a1
    a "Then come on over and open your present~"

    $ position = 0
    if score_bot == score_top:
        $ position = renpy.random.randint(1, 2)

    if score_bot > score_top or position == 1:
        hide screen location
        hide screen timeline
        hide screen quick_menu
        $ quick_menu = False
        $ say_box = False
        $ fp_stage = 'mga3_f'
        $ success_jumpto = 'day7_aiden_5t'
        $ failed_jumpto = 'day7_aiden_aftersx'
        jump fp

    elif score_top > score_bot or position == 2:
        hide screen location
        hide screen timeline
        hide screen quick_menu
        $ quick_menu = False
        $ say_box = False
        $ fp_stage = 'mga3_b'
        $ success_jumpto = 'day7_aiden_5b'
        $ failed_jumpto = 'day7_aiden_aftersx'
        jump fp

label day7_aiden_aftersx:
    $ location = location_messhall
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_messhall_winter_night_xmas with fade
    play music buddy_oath_holiday loop
    play bgsound sfxloop_crowd loop

    show aiden_xmas at left2
    show aiden norm1 at left2
    show yoshi_xmas at right2
    show yoshi sigh1 at right2
    voice audio.yoshi_v_sigh3a
    yo "*sigh* This costume Yuri gave me is so tight-fitting… I can’t even button it all the way up…"

    show aiden comp2 at left2
    voice audio.aiden_v_laugh1b2
    a "Hehe, you’re lucky you’re covered from the cold at least. I’m just relieved mine came with spare matching pants."

    show yoshi confused2 at right2
    voice audio.yoshi_v_why1
    yo "Of all things she’d dress me in, why a nutcracker?"

    show aiden tease1 at left2
    voice audio.aiden_v_laugh2a1
    a "Aren’t you one? You just cracked mine a while ago, hahaha!"

    show yoshi explain2 at right2
    voice audio.yoshi_v_sigh3a
    yo "I had that coming."

    show aiden tease2 at left2
    voice audio.aiden_v_perv1
    a "No, YOU had me cumming!"

    show yoshi awkward4 at right2
    voice audio.yoshi_v_aiden6
    yo "Sshh, Aiden! Everyone can hear us…!"

    show aiden_xmas at center
    show aiden tease2 at center
    show yoshi_xmas at right
    show yoshi awkward4 at right
    with move

    show yuri_xmas at left
    show yuri rage1 at left
    with dissolve

    voice audio.yuri_v_greet1a
    yu "There you two are! You missed the champagne popping! What took you so long?!"

    show aiden kiss1 at center
    voice audio.aiden_v_whistle2a
    a "*whistles*"

    show yoshi shy6 at right
    voice audio.yoshi_v_ah3
    yo "A-Ah… Well… We just had a bit of trouble with our costumes…"

    show aiden wink2 at center
    voice audio.aiden_v_perv1
    a "Yeah, and we had to clean up a spill on the kitchen floor *wink*"

    show yuri annoy2 at left
    voice audio.yuri_v_hey3a
    yu "Hey! Why are you two acting so sus?"
    yu "You know what? Nevermind. Just come join the party already! Everyone’s doing their own thing now!  "

    hide yuri_xmas
    hide yuri annoy2
    with dissolve

    show aiden happy1 at center
    voice audio.aiden_v_so2
    a "So, what do you wanna do for the night, Yoshi?"

    $working = False
    $shuffle_menu()
    menu():
        a "So, what do you wanna do for the night, Yoshi?"
        "Enjoy the buffet.":
            $working = True
            jump day7_aiden_darius
        "Hangout and talk.":
            $working = True
            jump day7_aiden_jin
        "Have drinks.":
            $working = True
            jump day7_aiden_goro
        "No idea.":
            $working = True
            jump day7_aiden_emilia

label day7_aiden_darius:
    show yoshi happy2 at right
    voice audio.yoshi_v_actually1a
    yo "I’m actually kind of hungry, so let’s go get some food!"

    show aiden tease1 at center
    voice audio.aiden_v_laugh1b2
    a "Hehe, you worked up an appetite in there, didn’t you~?"

    show yoshi angry2 at right
    voice audio.yoshi_v_aiden6
    yo "Aiden! Am I gonna have to deal with your dirty puns all night?"

    show aiden laugh1 at center
    voice audio.aiden_v_agree1b1
    a "Yup! You know that by now!"

    show aiden_xmas at p6_1
    show aiden laugh1 at p6_1
    show yoshi_xmas at p6_2
    show yoshi angry2 at p6_2
    with move

    show darius_xmas at p6_3
    show darius confused1 at p6_3
    show lloyd_xmas at p6_4
    show lloyd confused1 at p6_4
    show yoichi_xmas at p6_5
    show yoichi grin1 at p6_5
    show hiro_xmas at p6_6
    show hiro pout2 at p6_6
    with dissolve

    voice audio.hiro_v_hngh1c
    hi "Shubby Funny!"

    show yoichi laugh1 at p6_5
    voice audio.yoichi_v_laugh1d7
    yi "Bahaha! That’s six marshmallows, no way you can handle more!"

    show hiro pout1 at p6_6
    voice audio.hiro_v_hmph1a
    hi "I fan foo!"

    show yoichi playful3 at p6_5
    voice audio.yoichi_v_laugh1b5
    yi "What was that? I can’t understand you, hahaha!"

    show yoshi confused2 at p6_2
    voice audio.yoshi_v_uh1a
    yo "Uhhh… What’s going on over here?"

    show lloyd confused2 at p6_4
    voice audio.lloyd_v_conj4a1
    l "Actually, we aren’t sure either."

    show darius confused2 at p6_3
    voice audio.darius_v_think1a1
    d "They’re playing a game."

    show hiro hungry1 at p6_6
    voice audio.hiro_v_worry3a1
    hi "*gulp*"

    show hiro talking2 at p6_6
    voice audio.hiro_v_agree1b1
    hi "Yup! It’s called ‘chubby buddy!’"
    hi "You see how many marshmallows you can fit in your mouth while saying ‘Chubby Buddy.’"

    show yoichi talking2 at p6_5
    voice audio.yoichi_v_hiro1a
    yi "Torch-head’s record is six, and mine is ten!"

    show yoshi sigh1 at p6_2
    voice audio.yoshi_v_sigh3a
    yo "There’s plenty of delicious food to enjoy and they decide to do this instead."

    show aiden happy2 at p6_1
    voice audio.aiden_v_unsure5b2
    a "Haha, maybe it’s their dessert!"

    show lloyd laugh2 at p6_4
    voice audio.lloyd_v_laugh1a1
    l "It’s been fun to watch them."

    show yoichi angry1 at p6_5
    voice audio.yoichi_v_lloyd5a
    yi "Well, quit watching and join us then, Pipsqueak! "

    show lloyd shock6 at p6_4
    voice audio.lloyd_v_confused1b1
    l "Huh?! No way! That sounds embarrassing! And would you stop calling me that?!"

    show hiro laugh1 at p6_6
    voice audio.hiro_v_laugh1a
    hi "It’s not, it’s fun! Plus, you get to eat a bunch of marshmallows~"

    show lloyd angry2 at p6_4
    voice audio.lloyd_v_disagree1c1
    l "That sounds terrible for my body! I can’t have that much sugar in one sitting!"
    l "Dar! You do it!"

    show darius think5 at p6_3
    voice audio.darius_v_agree1a
    d "I do like marshmallows. I put them in my cocoa all the time."

    show yoichi excited1 at p6_5
    voice audio.yoichi_v_celebrate1a
    yi "Hell yeah! Come over here and try then."

    show darius_xmas at p6_4
    show darius confused3 at p6_4
    show lloyd_xmas at p6_3
    show lloyd angry2 at p6_3
    with move

    voice audio.darius_v_think2b3
    d "How does this work again?"

    show hiro excited2 at p6_6
    voice audio.hiro_v_alright2a3
    hi "It’s super easy! Just put a marshmallow in your mouth and say ‘Chubby Buddy!’"

    show darius talk1 at p6_4
    voice audio.darius_v_agree3
    d "Alright."

    show darius confused2 at p6_4
    voice audio.darius_v_ah1a1
    #jey
    d "Chubby Buddy."

    show hiro talking2 at p6_6
    voice audio.hiro_v_alright1b1
    hi "That’s one! Try another!"

    show darius confused3 at p6_4
    voice audio.darius_v_ah1c1
    #jey
    d "Chubby Buddy."

    show yoichi angry1 at p6_5
    voice audio.yoichi_v_rush1b1
    yi "This is taking way too long! Stack a bunch in there!"

    show yoshi talk3 at p6_2
    voice audio.yoshi_v_yoichi7
    yo "Y-Yoichi, he just started—"

    show darius talk1 at p6_4
    voice audio.darius_v_comp3a
    d "It’s fine."

    show yoichi excited1 at p6_5
    voice audio.yoichi_v_rush2b1
    yi "Here! Take ten!"

    show yoichi_xmas at p6_4
    show yoichi excited1 at p6_4
    with move

    show yoichi_xmas at p6_5
    show yoichi excited1 at p6_5
    with move

    show darius awkward2 at p6_4
    voice audio.darius_v_ugh1
    d "Mmf!"

    show yoichi excited2 at p6_5
    voice audio.yoichi_v_darius1a
    yi "Now say it!"

    show darius confused5 at p6_4
    voice audio.darius_v_ah1b1
    d "Ch-Chubby Buddy."

    show yoichi shock2 at p6_5
    voice audio.yoichi_v_question2b1
    yi "What the hell?! He can still talk?!"

    show hiro laugh1 at p6_6
    voice audio.hiro_v_laugh2a1
    hi "Haha, there goes your record you stupid Wolfboy!"

    show lloyd shock3 at p6_3
    voice audio.lloyd_v_amazed3a1
    l "Woah, way to go Dar!"

    show aiden tease1 at p6_1
    voice audio.aiden_v_perv1
    a "Yeah, you must be used to stuffing things in your mouth, huh bro?"

    show yoshi irked1 at p6_2
    voice audio.yoshi_v_aiden6
    yo "A-Aiden!"

    show yoichi playful3 at p6_5
    voice audio.yoichi_v_rush2b1
    yi "Here! Take three more!"

    show yoichi_xmas at p6_4
    show yoichi playful3 at p6_4
    with move

    show yoichi_xmas at p6_5
    show yoichi playful3 at p6_5
    with move

    show darius awkward2 at p6_4
    voice audio.darius_v_ugh1
    d "M-Mmgh…"

    show darius excited4 at p6_4
    voice audio.darius_v_ugh1
    d "Sh…Soggy Daddy."

    show yoichi laugh2 at p6_5
    voice audio.yoichi_v_laugh1a1
    yi "Hah! There’s the limit!"

    show darius excited4 at p6_4
    #voice audio.darius_v_
    d "*gulp*"

    show hiro amazed1 at p6_6
    voice audio.hiro_v_amazed1a1
    hi "That’s seventeen marshmallows though! That was basically the whole bag!"

    show lloyd worry3 at p6_3
    voice audio.lloyd_v_darius5b
    l "A-Are you okay, Dar? That didn’t choke you, did it?"

    show darius smile1 at p6_4
    voice audio.darius_v_denial1a1
    d "Nope, it was tasty."

    show yoichi grin1 at p6_5
    voice audio.yoichi_v_angry1d
    yi "I didn’t expect he’d play along. Thought you were just a boring giant."

    show lloyd happy1 at p6_3
    voice audio.lloyd_v_shock1a1
    l "Oh boy, you don’t know the half of it. Dar might not look it, but he’s quite the comedian, too!"

    show darius play5 at p6_4
    voice audio.darius_v_thanks1a1
    d "Thanks, Shorty Hubby."

    show lloyd angry2 at p6_3
    voice audio.lloyd_v_greet2c2
    l "Hey, the game’s over already! And you’re not supposed to call me nicknames too, Dar!"

    show hiro laugh1 at p6_6
    voice audio.hiro_v_oh2b
    hi "Now I wanna see if Bro-Aiden and Scoutmaster Yoshi can beat Darius’ record!"

    show aiden bold2 at p6_1
    voice audio.aiden_v_alright1a1
    a "Alright! I’ll go grab some more mallows!"

    show yoshi shock2 at p6_2
    voice audio.yoshi_v_wait2a
    yo "Wait…! Are we really going to—"

    show yoichi excited1 at p6_5
    voice audio.yoichi_v_agree1b4
    yi "Yes, you are! No backing out now!"
    yi "And you’re not out of the woods yet, Pipsqueak!"

    show lloyd rage3 at p6_3
    voice audio.lloyd_v_question1c3
    l "Wh-What?! I already said no!"

    show darius tease4 at p6_4
    voice audio.darius_v_laugh1
    d "Don’t worry, Lloyd. You’ve stuffed bigger things in your mouth."

    show lloyd scared4 at p6_3
    voice audio.lloyd_v_darius5a
    l "D-Dar!!"

    show aiden laugh3 at p6_1
    voice audio.aiden_v_laugh2a1
    a "Hahaha!"

    scene cg black with fade
    a "{i}Yoichi and Hiro kept getting Aiden, Lloyd, Darius and I to play ‘interesting’ games with them and we ended up having a lot of fun!{/i}"

    jump day7_aiden_aftersq

label day7_aiden_jin:
    $sq_jin += 1
    show yoshi happy2 at right
    voice audio.yoshi_v_think4
    yo "Let’s just relax and chat for a bit! "

    show aiden tease2 at center
    voice audio.aiden_v_yeah1a1
    a "Yeah, I wouldn’t mind taking it easy after working up a sweat~"

    show yoshi play2 at right
    voice audio.yoshi_v_think1a
    yo "Do you mean from the cooking, or…?"

    show aiden tease1 at center
    voice audio.aiden_v_comeon1a1
    a "Come on, Yoshi. You already know the answer."

    show yoshi_xmas at p5_2
    show yoshi play2 at p5_2
    show aiden_xmas at p5_1
    show aiden tease1 at p5_1
    with move

    show jin_xmas at edger
    show jin fudan1 at edger
    with moveinright

    voice audio.jin_v_hngh1b
    j "Hngh…"

    show yoshi sigh1 at p5_2
    voice audio.yoshi_v_sigh3a
    yo "*sigh* Yeah, I figured. Every time we do it, you get materials for fresh jokes."

    show jin fudan2 at edger
    voice audio.jin_v_fudan1a2
    j "Do… it…?"

    show aiden laugh1 at p5_1
    voice audio.aiden_v_agree1b1
    a "Haha, yup! But you were the instigator tonight, Yoshi~"

    show yoshi play3 at p5_2
    voice audio.yoshi_v_actually1b
    yo "You’re not wrong. Even now, your costume is still a tease."

    show jin perv5 at edger
    voice audio.jin_v_fudan4a1
    j "Such a tease…"

    show aiden confused2 at p5_1
    voice audio.aiden_v_think2a
    a "Uh, Yoshi? Why is Jin peeking over there?"

    show yoshi confused2 at p5_2
    voice audio.yoshi_v_huh1
    yo "Huh? Jin, what are you doing?"

    show jin shock3 at edger
    voice audio.jin_v_worry1c1
    j "O-Oh no, I’ve been spotted…!"

    show aiden happy2 at p5_1
    voice audio.aiden_v_jin1a
    a "Jin! Come over here, lemme check out your costume!"

    show jin shy2 at edger
    voice audio.jin_v_gulp1a
    j "*gulp* A-Alright…"

    show aiden_xmas at left
    show aiden happy2 at left
    show yoshi_xmas at center
    show yoshi confused2 at center
    show jin_xmas at right
    show jin shy2 at right
    with move

    show aiden play2 at left
    voice audio.aiden_v_oho1a
    a "Oho~ You’re showing a lot of skin in that outfit, I see! With some muscles, you could put mine to shame, haha!"

    show jin perv6 at right
    show jin_nosebleed at right
    voice audio.jin_v_think2a1
    j "I-I beg to differ…"

    show yoshi worry2 at center
    voice audio.yoshi_v_jin5
    yo "Jin, is your nose bleeding again…?"

    show jin daydream2 at right
    voice audio.jin_v_comp8b1
    j "I-I’m fine, I’m just getting woozy from the view."

    show yoshi sigh1 at center
    voice audio.yoshi_v_rush1
    yo "I’ll get you some tissues."

    show jin perv2 at right
    voice audio.jin_v_agree1c2
    j "A-Alright… I might need them for a different reason, though…"

    show aiden_xmas at p5_3
    show aiden play2 at p5_3
    show yoshi_xmas at p5_4
    show yoshi worry2 at p5_4
    show jin_xmas at p5_5
    show jin_nosebleed at p5_5
    show jin perv2 at p5_5
    with move

    show hunter_xmas at p5_1
    show hunter talking4 at p5_1
    show natsumi_xmas at p5_2
    show natsumi excited1 at p5_2
    with dissolve

    voice audio.natsumi_v_reportingforduty1
    n "Did I hear tissues?! The cleanliness police are here to for the rescue!"

    show hunter talking4 at p5_1
    voice audio.hunter_v_err1a
    hu "H-Here you go, Scoutmaster Yoshi…"

    hide jin_nosebleed
    with dissolve

    show yoshi talk3 at p5_4
    voice audio.yoshi_v_oh3
    yo "O-Oh, thanks Natsumi and Hunter…!"

    show natsumi laugh1 at p5_2
    voice audio.natsumi_v_response3
    n "You’re most welcome, sir! We’re here to make sure the party is as smooth and TIDY as possible!"

    show aiden confused2 at p5_3
    voice audio.aiden_v_confused1c2
    a "Eh? You’re supposed to be having fun, not cleaning, you two!"

    show yoshi comp2 at p5_4
    voice audio.yoshi_v_natsumi1
    yo "Yeah, Natsumi… We’ve been working all day, surely you can take this chance to enjoy the time with everyone!"

    show hunter sigh2 at p5_1
    voice audio.hunter_v_sigh1
    hu "*sigh* That’s what I’ve been telling him… But he’s so excited to clean up for some reason."

    show natsumi thinking1 at p5_2
    voice audio.natsumi_v_unsure1
    n "Well, I don’t want it to end like our last costume party, with the scoutmasters cleaning up after us."

    show jin shock2 at p5_5
    voice audio.jin_v_wait2a
    j "W-Wait, you had a costume party during the summer too?"

    show natsumi talking1 at p5_2
    voice audio.natsumi_v_agree1a
    n "We did! And Ms. Yuri had a whole bunch of costumes for us to choose from then!"
    n "I was a police officer, and Scoutmaster Yoshi was a sheriff! We were kind of like a dynamic duo!"

    show jin perv2 at p5_5
    voice audio.jin_v_think1a1
    j "S-So figures of authority… I guess that means you’re both the tops…"

    show natsumi playful2 at p5_2
    voice audio.natsumi_v_laugh4d
    n "Meanwhile, Hunter was a play-bunny boy! It was actually a really cute outfit~"

    show hunter worry1 at p5_1
    voice audio.hunter_v_doubt1
    hu "You say that, Natsumi, but it was kind of embarrassing…"
    hu "If I didn’t have that shawl, I’d have basically been naked."

    show jin upset5 at p5_5
    voice audio.jin_v_hngh4c
    j "Hnnghhh… I can’t believe I missed out…"

    show natsumi laugh1 at p5_2
    voice audio.natsumi_v_laugh2
    n "It was a ton of fun! We have lots of stories about it, haha!"

    show jin happy1 at p5_5
    voice audio.jin_v_conj2c1
    j "W-Well, if you’re interested, we could write a blog post for it too!"

    show hunter talking1 at p5_1
    voice audio.hunter_v_surprised1
    hu "Oh, you have your own blog, Mr. Jin?"

    show jin laugh2 at p5_5
    voice audio.jin_v_please2a
    j "P-Please, just call me Jin!"
    j "And not exactly. It’s actually for Camp Buddy. "

    show yoshi happy2 at p5_4
    voice audio.yoshi_v_yeah2
    yo "Yup! We’re actually chronicling the memories going all the way back to my term as a scout to post on there!"

    show natsumi excited1 at p5_2
    voice audio.natsumi_v_compliment1a
    n "Oh wow! Like a camp history!"

    show hunter amazed1 at p5_1
    voice audio.hunter_v_amazed1
    hu "That sounds really cool…!"

    show jin happy2 at p5_5
    voice audio.jin_v_conj4b1
    j "So, you want to help? I’d love to hear more about the party!"
    j "Especially the costumes…"

    show natsumi talking1 at p5_2
    voice audio.natsumi_v_agree5a
    n "Sure! We’d love to!"

    show hunter talking4 at p5_1
    voice audio.hunter_v_yoshinori3
    hu "Want to join us, Scoutmaster Yoshi and Sir Aiden?"

    show aiden tease2 at p5_3
    voice audio.aiden_v_yeah1a3
    a "Yeah, totally! After all, I’m sure Jin would wanna hear what costume I had on that night~"

    show jin fudan2 at p5_5
    voice audio.jin_v_gulp1a
    j "*gulp* Wh-What was it…?"

    show hunter thinking2 at p5_1
    voice audio.hunter_v_aiden2
    hu "Sir Aiden was dressed up like an ancient pharaoh…"

    show natsumi talking3 at p5_2
    voice audio.natsumi_v_oh1
    n "Oh, that reminds me…! Were you able to take off the ring stuck on your thing?"

    show jin fudan3 at p5_5
    voice audio.jin_v_gasp1a
    j "R-Ring? Th-Thing…?"

    show yoshi angry5 at p5_4
    voice audio.yoshi_v_ehem1b
    yo "*ehem* Let’s not confuse Jin here… Let’s just tell him how the party went for the blog."

    show aiden tease3 at p5_3
    voice audio.aiden_v_oho2a
    a "Don’t forget about the after party~"

    show jin perv2 at p5_5
    voice audio.jin_v_fudan1a3
    j "Oh my… Let me get my laptop and we’ll get started!"

    # JMA5
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
    $ minigame_id = 'jmA4'
    $ renpy.call(minigame_id, 'night')

label day7_aiden_postmg:

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

    $ location = location_lake
    $ day = "??"
    $ time = timeline_timenight
    $ season = season_summer
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_lake_past_night with fade
    play music go_with_the_flow loop
    play bgsound sfxloop_night loop

    show aiden_costume at center
    show aiden happy1 at center
    voice audio.aiden_v_yoshi1b
    a "Over here, Yoshi!"

    show aiden_costume at right2
    show aiden happy1 at right2
    with move

    show yoshi_costume at p5_1
    show yoshi talk1 at p5_1
    with dissolve

    voice audio.yoshi_v_wait5
    yo "Coming! "

    show yoshi_costume at left2
    show yoshi relief2 at left2
    with move

    voice audio.yoshi_v_relief1
    yo "Ahh… The grass feels good on my back."

    show aiden relief2 at right2
    voice audio.aiden_v_relief2a
    a "I know right? It’s been a while since we hung out here. And it looks like we got the whole pier to ourselves!"

    show yoshi tired3 at left2
    voice audio.yoshi_v_response2a
    yo "I don’t mind that – I could use the peace and quiet. Hosting the party tonight really drained me."

    show yoshi comp2 at left2
    voice audio.yoshi_v_thanks4
    yo "Thanks for helping me clean up earlier, Aiden! I know you were already tired from cooking the food too."

    show aiden bold2 at right2
    voice audio.aiden_v_atyourservice1
    a "No problem, always at your service! Everything seemed to go well tonight, too. "

    show yoshi comp5 at left2
    voice audio.yoshi_v_yeah1
    yo "Yeah, it’s been such a long week working with the scouts on the fundraiser, and this was a great way to celebrate."

    show aiden tease1 at right2
    voice audio.aiden_v_agree3a2
    a "You bet! I’d say everyone had extra fun with Yuri’s costume party idea."
    a "Especially you, Yoshi~ "

    show yoshi confused2 at left2
    voice audio.yoshi_v_huh3a
    yo "H-Huh?"

    show aiden tease2 at right2
    voice audio.aiden_v_perv1
    a "You might as well be an archeologist with all digging you’ve been doing with those eyes."
    a "I know that look when I see it~"

    show yoshi explain2 at left2
    voice audio.yoshi_v_ehem1b
    yo "*ehem* I’ve been trying hard not to look your way, especially since Yuri gave you such a revealing costume."

    show aiden wink2 at right2
    voice audio.aiden_v_agree2a2
    a "Uh-huh~"

    show yoshi play2 at left2
    voice audio.yoshi_v_well3
    yo "D-Don’t get me wrong, it really suits you. You look really good in it, in fact…"

    show aiden play3 at right2
    voice audio.aiden_v_oho1a
    a "You too! You really make the perfect sexy cowboy~"
    a "But then again, your wild west style makes me wild and wet."

    show yoshi sigh1 at left2
    voice audio.yoshi_v_sigh3a
    yo "There you go teasing me again, Aiden."

    show aiden laugh1 at right2
    voice audio.aiden_v_laugh2a1
    a "Haha! Can’t help it, you make it so easy for me!"

    show yoshi think2 at left2
    voice audio.yoshi_v_unsure3c
    yo "M-Maybe we should’ve gotten changed first before chilling out here."

    show aiden sigh5 at right2
    voice audio.aiden_v_sigh1a
    a "I wish I could! Trust me I tried, but that ring’s stuck on there!"

    show yoshi confused3 at left2
    voice audio.yoshi_v_huh3b
    yo "R-Ring…? Y-You mean the one’s that’s on your…"

    show aiden bold2 at right2
    voice audio.aiden_v_agree1b1
    a "Ding, ding, dick!"

    show yoshi sigh4 at left2
    voice audio.yoshi_v_sigh3a
    yo "*sigh* Why did you even put it there in the first place…"

    show aiden tease2 at right2
    voice audio.aiden_v_well1b2
    a "Well, maybe you can help me take it off~?"

    show yoshi awkward1 at left2
    voice audio.yoshi_v_gulp1a
    yo "*gulp*"

    show aiden tease1 at right2
    voice audio.aiden_v_here1b
    a "Here, lemme give you a clearer view~"

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black with fade
    yo "{i}After such a long week, I didn’t even try to resist Aiden as he pulled himself up from the grass and positioned himself right on top me.{/i}"
    yo "{i}I laid down on my back, eager for what came next…{/i}"

    scene cg black
    hide screen location
    hide screen timeline
    hide screen quick_menu
    $quick_menu = False
    with fade
    $ renpy.pause (2.0, hard=True)

    jump day7_aiden_ma4

label day7_aiden_postfb:
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
    show aiden_xmas at p5_1
    show aiden play1 at p5_1
    show yoshi_xmas at p5_2
    show yoshi norm3 at p5_2
    show jin_xmas at p5_3
    show jin_blush2 at p5_3
    show jin_nosebleed at p5_3
    show jin perv2 at p5_3
    show hunter_xmas at p5_4
    show hunter normal1 at p5_4
    show natsumi_xmas at p5_5
    show natsumi confused2 at p5_5
    voice audio.natsumi_v_thinking2a
    n "So… Did the ring ever come off?"

    show aiden tease2 at p5_1
    voice audio.aiden_v_agree1b1
    a "Yup! But let’s just say it took some special lube~ "

    show yoshi explain2 at p5_2
    voice audio.yoshi_v_ehem1b
    yo "*ehem* I think that’s enough for that story! Jin’s got plenty for his blog!"

    show jin perv2 at p5_3
    voice audio.jin_v_think2a1
    j "I-I could use some more details… It sounds like Aiden was about to get to the juicy part."

    show aiden tease1 at p5_1
    voice audio.aiden_v_perv1
    a "Oh, there were plenty of juices, alright~"

    show jin dizzy2 at p5_3
    voice audio.jin_v_hngh4c
    j "HNGH…!! Please do a re-enactment right now!"
    j "SEND THIS ANGEL BOY TO BL HEAVEN!"

    show hunter surprised2 at p5_4
    voice audio.hunter_v_err1a
    hu "He really is just like Ms. Yuri…"

    show natsumi laugh1 at p5_5
    voice audio.natsumi_v_laugh3
    n "Hahaha!"

    scene cg black with fade
    yo "{i}We worked on the blog with Natsumi and Hunter, excitedly telling Jin stories from the previous term.{/i}"

    jump day7_aiden_aftersq

label day7_aiden_goro:
    $sq_goro += 1
    show yoshi happy2 at right
    voice audio.yoshi_v_think4
    yo "Let’s go have some drinks!"

    show aiden excited1 at center
    voice audio.aiden_v_excited2a
    a "Now we’re talking!"
    a "I see Gramps and Mr. Clermont doing just that over there! Let’s join ’em!"

    show aiden_xmas at p5_1
    show aiden excited1 at p5_1
    show yoshi_xmas at p5_2
    show yoshi happy1 at p5_2
    with move

    show goro_xmas at p5_4
    show goro norm1 at p5_4
    show william_xmas at p5_5
    show william norm1 at p5_5
    with dissolve

    voice audio.yoshi_v_goodpm1
    yo "Good evening! Mind if we join in?"

    show william happy2 at p5_5
    voice audio.william_v_yoshi2b
    w "Ah, Yoshinori, please take a seat!"

    show aiden_xmas at p4_1
    show aiden excited1 at p4_1
    show yoshi_xmas at p4_2
    show yoshi happy1 at p4_2
    show goro_xmas at p4_3
    show goro play3 at p4_3
    show william_xmas at p4_4
    show william happy2 at p4_4
    with move

    voice audio.goro_v_heh1a
    g "Heh, Yuri can’t impose our liquor ban now, so we’re drinking ’til the sun goes up! "

    show aiden shock2 at p4_1
    voice audio.aiden_v_shock1e2
    a "Whoa, whoa, Gramps! You don’t wanna be a sobbing mess in front of our sponsor!"

    show goro explain1 at p4_3
    voice audio.goro_v_ehem1a
    g "*ehem* Don’t listen to him, Mr. Clermont."

    show william play4 at p4_4
    voice audio.william_v_laugh1
    w "Isn’t it amusing to see a bunch of grown men in such costumes enjoying a tall glass of beer?"

    show goro sigh1 at p4_3
    voice audio.goro_v_sigh1a
    g "*sigh* I hope it’s not too unbecoming of your prestigious reputation, sir."

    show william play2 at p4_4
    voice audio.william_v_fine1b
    w "Come on, Goro. We’re outside the workspace now, we can be more personal and call each other by our names!"

    show goro comp2 at p4_3
    voice audio.goro_v_thanks2b1
    g "Th-Thank you, sir, but it would feel far too inappropriate…"

    show william laugh1 at p4_4
    voice audio.william_v_alright1b
    w "Haha, whatever you like, then! "

    show aiden_xmas at p5_2
    show aiden shock2 at p5_2
    show yoshi_xmas at p5_3
    show yoshi happy1 at p5_3
    show goro_xmas at p5_4
    show goro comp2 at p5_4
    show william_xmas at p5_5
    show william laugh1 at p5_5
    with move

    show keitaro_xmas at p5_1
    show keitaro talking1 at p5_1
    with dissolve

    voice audio.keitaro_v_greeting7a
    k "Good evening, sirs! I hope I’m not interrupting, but I brought some oysters…! I heard they go well with beer!"

    show goro happy2 at p5_4
    voice audio.goro_v_amazed2a1
    g "That’s perfect, Keitaro. Thanks. Who taught you that, though?"

    show aiden play5 at p5_2
    voice audio.aiden_v_atyourservice1
    a "*ehem* Yours truly~"

    show william happy1 at p5_5
    voice audio.william_v_keitaro1c
    w "Ah, Mr. Nagame, why don’t you sit here with us for a moment?"

    show keitaro worry1 at p5_1
    voice audio.keitaro_v_oh4
    k "O-Oh! I-I’m sorry, I don’t drink, sir…!"

    show william explain3 at p5_5
    voice audio.william_v_well1a
    w "Well, just for some small talk! There’s something I’ve been meaning to tell your scoutmasters!"

    show keitaro talking1 at p5_1
    voice audio.keitaro_v_okay1
    k "O-Okay, sir…!"

    show aiden_xmas at p5_1
    show aiden play5 at p5_1
    show yoshi_xmas at p5_2
    show yoshi happy1 at p5_2
    show keitaro_xmas at p5_3
    show keitaro talking1 at p5_3
    with move

    show william happy1 at p5_5
    voice audio.william_v_anyway1
    w "So, as we all know, Mr. Nagame’s book from last term was one of our bestselling novels in a long time!"

    show aiden laugh1 at p5_1
    voice audio.aiden_v_amazed2b1
    a "Does that make him a world-renowned author now? Haha!"

    show keitaro laugh1 at p5_3
    voice audio.keitaro_v_laugh3
    k "I-I don’t know about that, Sir Aiden, hehe…"

    show william amazed2 at p5_5
    voice audio.william_v_actually1
    w "It’s actually a fairly accurate statement! Why, we’re already working on several foreign language translations for your work as well!"
    w "With any luck, we’ll have them out soon and reach an even broader audience."

    show keitaro surprised2 at p5_3
    voice audio.keitaro_v_amazed3
    k "Th-This is really surreal, sir…"

    show william laugh1 at p5_5
    voice audio.william_v_laugh1
    w "Haha, I’m sure, which is what brings me to what I’ve wanted to say…"
    w "Considering the book’s success, I’ve personally offered Mr. Nagame here a percentage of the sales."

    show aiden shock3 at p5_1
    voice audio.aiden_v_keitaro1a
    a "Whoa! Does that mean you’re rich now, Keitaro?!"

    show goro shock1 at p5_4
    show william explain3 at p5_5
    voice audio.william_v_well1a
    w "That’s the thing. He declined the offer."

    show yoshi shock2 at p5_2
    voice audio.yoshi_v_what4
    yo "Wh-What? Why?"

    show keitaro compassion3 at p5_3
    voice audio.keitaro_v_well2
    k "I-I figured I couldn’t have done it if it weren’t for Camp Buddy, so it was better to put it into the sponsorship."

    show william amazed3 at p5_5
    voice audio.william_v_agree4b
    w "Yes! And that’s exactly what we did!"
    w "While this expansion project’s funding is a separate investment for me, I’ve made sure to respect Mr. Nagame’s wishes, and pool in his royalties alongside this sponsorship!"

    show goro shock2 at p5_4
    voice audio.goro_v_ah2c
    g "I’m lost for words…"

    show yoshi amazed1 at p5_2
    voice audio.yoshi_v_thanks2
    yo "Th-Thank you so much, Keitaro!"
    yo "I promise we’re doing our best to make it all worth it, so the camp can have an amazing future!"

    show keitaro excited2 at p5_3
    voice audio.keitaro_v_yessir1a
    k "Yes, sir! I can’t wait to be back for the next summer!"

    show william laugh2 at p5_5
    voice audio.william_v_amazed1
    w "Good! Now come on, let’s have a toast!"

    show aiden_xmas at p6_1
    show aiden shock3 at p6_1
    show yoshi_xmas at p6_2
    show yoshi amazed1 at p6_2
    show keitaro_xmas at p6_3
    show keitaro excited2 at p6_3
    show goro_xmas at p6_4
    show goro shock2 at p6_4
    show william_xmas at p6_5
    show william laugh2 at p6_5
    with move

    show yoichi_autumn at p6_6
    show yoichi talking2 at p6_6
    with dissolve

    voice audio.yoichi_v_greet1a3
    yi "Hey, why didn’t you call everyone over for the booze?!"

    show keitaro worry1 at p6_3
    voice audio.keitaro_v_thinking1
    k "I don’t think we’re supposed to—"

    show yoichi angry1 at p6_6
    voice audio.yoichi_v_william1a
    yi "Aha! So, you’re the one who took my oysters, Snow-BALLS!"

    show william think2 at p6_5
    voice audio.william_v_oh3
    w "I believe he is referring to me."

    show yoshi angry2 at p6_2
    voice audio.yoshi_v_yoichi7
    yo "Y-Yoichi! Call him Mr. Clermont!"

    show yoichi playful1 at p6_6
    voice audio.yoichi_v_question1a5
    yi "Why not? He’s Snowball’s dad, and it’s what he looks like!"

    show william confused3 at p6_5
    voice audio.william_v_think4
    w "Are you referring to my son, Felix?"

    show goro shy6 at p6_4
    voice audio.goro_v_yoichi2a
    g "A-Ah, Yoichi here just likes to give out nicknames to people he likes, sir…"

    show yoichi laugh2 at p6_6
    voice audio.yoichi_v_agree1b1
    yi "Yeah! That’s Frogboy, he’s Geezer, and that’s Buttcheeks and Sheriff Brokeback!"

    show yoshi sigh1 at p6_2
    voice audio.yoshi_v_sigh3a
    yo "*sigh* This is embarrassing…"

    show william laugh2 at p6_5
    voice audio.william_v_laugh3
    w "Hahaha! What a fun idea! Tell me all the other nicknames you have, lad! "

    show yoichi grin1 at p6_6
    voice audio.yoichi_v_laugh1a1
    yi "Pour me a drink and you got it!"

    show goro shy4 at p6_4
    voice audio.goro_v_sigh1a
    g "So much for a peaceful evening…"

    scene cg black with fade
    yo "{i}Aiden and I ended up spending the evening drinking with Mr. Clermont and Sir Goro, while the rest of the scouts ate and played games.{/i}"

    jump day7_aiden_aftersq

label day7_aiden_emilia:
    $sq_emilia += 1
    show yoshi think2 at right
    voice audio.yoshi_v_unsure3c
    yo "I don’t know, honestly. I’m pretty drained after working all day on site."

    show aiden laugh1 at center
    voice audio.aiden_v_laugh2a1
    a "And you worked on me on top of that. Hahaha!"

    show yoshi_xmas at p5_2
    show yoshi think2 at p5_2
    show aiden_xmas at p5_1
    show aiden laugh1 at p5_1
    with move

    show emilia_xmas at p5_4
    show emilia norm3 at p5_4
    show taiga_xmas at p5_5
    show taiga normal3 at p5_5
    with dissolve

    voice audio.aiden_v_oh1a
    a "Oh, Yoshi, look over there! Are you seeing what I’m seeing?"

    show yoshi confused2 at p5_2
    voice audio.yoshi_v_huh1
    yo "Emilia and Taiga talking to each other…? What an unlikely pair."

    show aiden happy2 at p5_1
    voice audio.aiden_v_rush1a1
    a "Let’s go check on them!"

    show yoshi_xmas at p4_2
    show yoshi talk1 at p4_2
    show aiden_xmas at p4_1
    show aiden happy2 at p4_1
    show emilia_xmas at p4_3
    show emilia norm3 at p4_3
    show taiga_xmas at p4_4
    show taiga normal3 at p4_4
    with move

    voice audio.yoshi_v_goodpm1
    yo "Good evening, you two! Enjoying the party so far?"

    show emilia evil2 at p4_3
    voice audio.emilia_v_celebrate1b1
    e "It’s about time you got in costume too, Yoshi."

    show aiden talk3 at p4_1
    voice audio.aiden_v_hey2a1
    a "What’s going on here? You two looked like you were talking about something serious."

    show taiga talking2 at p4_4
    voice audio.taiga_v_conjunction3b
    t "Well… She was just telling me everything that happened while we were gone."
    t "And I was telling her about the last two terms."

    show emilia talk2 at p4_3
    voice audio.emilia_v_taiga1
    e "It seems that Taiga and I have a lot in common, believe it or not."

    show aiden awkward2 at p4_1
    voice audio.aiden_v_really2a
    a "Now that’s unexpected…"

    show yoshi explain2 at p4_2
    voice audio.yoshi_v_unsure3a
    yo "I guess I can understand why… You both went through a lot that you wanted to make up for."

    show emilia sigh1 at p4_3
    voice audio.emilia_v_agree2a1
    e "Exactly. But in my case, I’m just getting started."

    show taiga sigh2 at p4_4
    voice audio.taiga2_v_determined3a
    t "Well, you can make up for it faster than you think. Honestly, I feel so different from who I was half a year ago…"
    t "And I owe it to everyone here for giving me another chance."

    show taiga compassion2 at p4_4
    voice audio.taiga2_v_compliment2b
    t "We’re lucky we have lots of open-minded people who let stuff go."

    show emilia talk3 at p4_3
    voice audio.emilia_v_agree1b2
    e "And you’re right that I’ve got to put in the work too. "
    e "I’m trying to think of ways to really show how much I’m willing to change…"

    show yoshi worry2 at p4_2
    voice audio.yoshi_v_emilia3
    yo "You just recovered. You don’t have to pressure yourself like that, Emilia. "

    show aiden comp2 at p4_1
    voice audio.aiden_v_yeah1a1
    a "Yeah, as long as you’re being genuine with your actions, things should work out fine!"
    a "No one’s keeping a check list of things you have to make up for, haha!"

    show taiga sigh2 at p4_4
    voice audio.taiga_v_agree3a
    t "Yeah, or else I’d be less than halfway through the list."

    show taiga annoyed2 at p4_4
    voice audio.taiga_v_ugh1
    t "Don’t give Yoichi any ideas either, or he’ll start using that as an excuse to boss me around."

    show aiden laugh2 at p4_1
    voice audio.aiden_v_laugh2a1
    a "Hahaha! He totally would!"

    show emilia comp3 at p4_3
    voice audio.emilia_v_conj1a
    e "It’s still surreal though, you seem so calm and well-put together now for your age. "
    e "I have a hard time imagining you being in a similar position as I was."

    show taiga talking4 at p4_4
    voice audio.taiga2_v_compassion2b
    t "Just ask everyone and they’ll tell you for sure."

    show aiden happy3 at p4_1
    voice audio.aiden_v_agree1b1
    a "Yup! He was a real ball of angst! Yoichi was spot on calling him Dynamite, hahaha!"

    show emilia think5 at p4_3
    voice audio.emilia_v_think1
    e "Now I wonder what I’m going to be called from now on…"

    show taiga sigh2 at p4_4
    voice audio.taiga_v_sigh1
    t "Whatever it is, you’re better off just accepting the title, trust me."

    show yoshi comp2 at p4_2
    voice audio.yoshi_v_aww1
    yo "I’m so happy to see you two bonding so well and owning up to your past actions like this!"
    yo "Taiga, to think that you would be the scout who brings motivation to even your scoutmasters!"

    show yoshi relief2 at p4_2
    voice audio.yoshi_v_amazed2b
    yo "It brings a tear to my eye. Why I remember—"

    show yoshi_xmas at p5_2
    show yoshi relief2 at p5_2
    show aiden_xmas at p5_1
    show aiden happy3 at p5_1
    show emilia_xmas at p5_3
    show emilia think5 at p5_3
    show taiga_xmas at p5_4
    show taiga sigh2 at p5_4
    with move

    show yuri_xmas at p5_5
    show yuri angry2 at p5_5
    with dissolve

    voice audio.yuri_v_yoshi9a
    yu "Yoshi?! Are you monologuing again?!"

    show yoshi happy1 at p5_2
    voice audio.yoshi_v_oh1
    yo "Oh, I was only acknowledging Taiga and Emilia’s redemption journey!"

    show yuri angry6 at p5_5
    voice audio.yuri_v_ugh2a
    yu "Haven’t you gushed over everyone enough today?!"

    show taiga annoyed3 at p5_4
    voice audio.taiga_v_ugh1
    t "See, this is why I didn’t ever want to listen to him back then."

    show yuri bold1 at p5_5
    voice audio.yuri_v_rush1a3
    yu "Come with me, you two! I have party games to play with everyone!"

    show taiga annoyed4 at p5_4
    voice audio.taiga_v_suspicious1
    t "Depends on what your definition of a ‘party game’ is."

    show yuri tease4 at p5_5
    voice audio.yuri_v_laugh2b1
    yu "I promise it’s not pervy at all! Hihihi~"

    show emilia annoy1 at p5_3
    voice audio.emilia_v_well1
    e "Well, I’m not risking it. I’m staying here. "

    show yuri_xmas at p6_5
    show yuri excited4 at p6_5
    with move

    voice audio.yuri_v_well1a
    yu "Well, suit yourself~! It’s gonna be a boys-only strip show then!"

    show taiga panic1 at p5_4
    voice audio.taiga_v_surprised4a
    t "Wh-What?! I knew it…!"

    show yuri excited2 at p6_5
    voice audio.yuri_v_rush1c1
    yu "You’re coming with me~"

    hide yuri_xmas
    hide yuri excited2
    hide taiga_xmas
    hide taiga panic1
    with moveoutright

    show yoshi bold5 at p5_2
    voice audio.yoshi_v_ehem1b
    yo "—And that’s why you should always strive to be honest with yourself, so you can… Wait a minute, where did Taiga go?"

    show aiden comp2 at p5_1
    voice audio.aiden_v_yoshi7a
    a "Haha, you got carried away with your speech again, Yoshi."

    show emilia happy1 at p5_3
    voice audio.emilia_v_comp2b
    e "Well, I don’t mind hearing more…! They always inspire me, believe it or not!"

    show yoshi bold2 at p5_2
    voice audio.yoshi_v_laugh1
    yo "See, Aiden? Emilia gets it! Now where was I… "

    show aiden sigh5 at p5_1
    voice audio.aiden_v_sigh1a
    a "*sigh* This is gonna be a real long night…"

    scene cg black with fade
    yo "{i}I continued to talk to Emilia for a little bit longer until Aiden and Taiga brought us some food.{/i}"

    jump day7_aiden_aftersq

label day7_aiden_aftersq:
    yo "{i}Eventually, after we finished, we joined the rest of the group and partied for the remainder of the evening!{/i}"
    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black
    hide screen location
    hide screen timeline
    hide screen quick_menu
    $quick_menu = False
    with fade
    play sound sleeping_time
    $persistent.profile_unlock.append("cameos")
    $ time_transition_night_to_day_winter2()
    $ renpy.pause (2.0, hard=True)
    jump day8_aiden
