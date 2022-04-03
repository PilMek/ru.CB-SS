label day3_aiden:
    $ day = "78"
    $ time = timeline_timeday
    $ location = location_campsite
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    $ working = True

    scene bg_campgrounds_auwinter_day with fade
    play bgsound sfxloop_birds loop
    play music brand_new_day_winter loop

    show yoshi_winter at left
    show yoshi worry2 at left
    show yoichi_winter at center
    show yoichi normal1 at center
    show taiga_winter at right
    show taiga normal3 at right
    voice audio.yoshi_v_unsure2a
    yo "Are you two sure you’ll be alright? You’re free to come with us if you want, you know…"

    show yoichi annoyed1 at center
    voice audio.yoichi_v_annoyed2b1
    yi "Ugh, give me a break! We don’t need you babysitting us!"

    hide yoshi_winter
    hide yoshi
    show yoshi2_winter at left
    show yoshi2 comp2 at left
    voice audio.yoshi_v_well1
    yo "Well, I just feel a little bad we have to leave on such short notice… Mr. Clermont really surprised us with this trip."

    show taiga compassion5 at right
    voice audio.taiga2_v_compassion3a
    t "Don’t sweat it. It’s not like we’re sticking around the camp.  "
    t "We’re staying over at Keitaro’s place and our friends are gonna be there."

    hide yoshi2_winter
    hide yoshi2 comp2
    show yoshi_winter at left
    show yoshi excited1 at left
    voice audio.yoshi_v_ah1
    yo "Ah, so it’s gonna be like a little reunion! It’s been a couple months since you’ve all been together – you must really miss each other!"

    show taiga excited2 at right
    voice audio.taiga_v_thinking2a
    t "I guess you could say that. It’ll be a good chance to catch up."

    show yoichi talking2 at center
    voice audio.yoichi_v_agree1b1
    yi "Yeah! And it’s more fun than being stuck here with you old geezers! I wouldn’t wanna go on your boring business trip!"
    yi "Heck, the longer I can be away from this dump, the better!"

    show yoshi laugh2 at left
    voice audio.yoshi_v_laugh1
    yo "Haha, sounds like you’re very excited to see your friends, Yoichi~!"

    show yoichi sigh2 at center
    voice audio.yoichi_v_bored1a
    yi "Better than watching the grass die here."

    show yoshi talk1 at left
    voice audio.yoshi_v_worry2
    yo "It is getting colder every day too. Did you guys pack some warmer clothes?"

    show taiga sigh2 at right
    voice audio.taiga_v_sigh1
    t "I did, but I can’t say the same for this guy. I think he’s planning on running in the snow naked."

    show yoichi angry1 at center
    voice audio.yoichi_v_sarcastic1b
    yi "Duh! You should know I don’t pack my own stuff!"
    yi "Besides, we’re bringing the dogs too, and that’s enough work for me already!"

    show taiga angry5 at right
    voice audio.taiga_v_ugh1
    t "Ugh, can’t we just leave them here?"

    show yoichi angry3 at center
    voice audio.yoichi_v_insult1a
    yi "Don’t be stupid, they’ll starve to death here! They’re coming with us, whether you like it or not. "

    show taiga_winter at right
    show taiga angry2 at right
    voice audio.taiga_v_agree3b
    t "Fine, fine! Just make sure they don’t come near me and slobber all over my face!"

    show yoshi worry2 at left
    voice audio.yoshi_v_unsure2b
    yo "A-Are you sure you two don’t need me to— "

    show taiga talking1 at right
    voice audio.taiga_v_rush1b
    t "Yeah, stop worrying about us! Just go ahead already, everyone’s waiting for you out there!"

    show yoshi comp2 at left
    voice audio.yoshi_v_alright2
    yo "Alright, Taiga. I’ll leave you in charge of Yoichi…!"

    show yoichi playful3 at center
    voice audio.yoichi_v_hmph1a
    yi "No one’s the boss of me!"

    hide yoshi_winter
    hide yoshi comp2
    show yoshi2_winter at left
    show yoshi2 sigh4 at left
    voice audio.yoshi_v_yoichi2
    yo "*sigh* Yoichi… Please try not to cause too much trouble, alright?"

    show taiga playful2 at right
    voice audio.taiga_v_heh1
    t "Heh, you should know better by now, Yoshi."

    hide yoshi2_winter
    hide yoshi2 sigh4
    show yoshi_winter at left
    show yoshi happy2 at left
    voice audio.yoshi_v_bye1b
    yo "I’ll see you two in a few days! Stay safe!"

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

    $ location = location_entrance
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_entrance_auwinter_day with fade
    play bgsound sfxloop_birds loop
    play music brand_new_day_winter loop

    show goro_winter at p5_2
    show goro norm1 at p5_2
    show yuri_winter at p5_1
    show yuri norm1 at p5_1
    show aiden_winter at p5_3
    show aiden happy2 at p5_3
    show yoshi_winter at p5_5
    show yoshi norm1 at p5_5
    voice audio.aiden_v_yoshi1b
    a "There you are, Yoshi!"

    show yuri_winter at p4_1
    show yuri norm1 at p4_1
    show goro_winter at p4_2
    show goro norm1 at p4_2
    show aiden_winter at p4_4
    show aiden happy2 at p4_4
    show yoshi_winter at p4_3
    show yoshi happy1 at p4_3
    with move

    voice audio.yoshi_v_sorry2a
    yo "Sorry for the delay, everyone! I was just making sure Yoichi and Taiga were all set before we left!"

    show goro talk1 at p4_2
    voice audio.goro_v_response3a1
    g "It’s fine. The shuttle just arrived anyway."

    show yuri upset2 at p4_1
    voice audio.yuri_v_aww1a
    yu "Aww, I’m a little bummed they aren’t coming with us, though. "

    show aiden laugh2 at p4_4
    voice audio.aiden_v_no2a1
    a "Nah, they prefer to hang out with their friends – and that’s a good thing!"

    show yoshi relief2 at p4_3
    voice audio.yoshi_v_yeah2
    yo "Yeah. Last year’s batch was definitely one of the closest groups we’ve ever had at the camp."


    show yuri_winter at p7_1
    show yuri norm1 at p7_1
    show goro_winter at p7_2
    show goro talk1 at p7_2
    show yoshi_winter at p7_3
    show yoshi relief2 at p7_3
    show aiden_winter at p7_4
    show aiden laugh2 at p7_4
    with move

    show darius_winter at p7_6
    show darius norm1 at p7_6
    show lloyd_winter at p7_5
    show lloyd happy1 at p7_5
    show jin_winter at p7_7
    show jin norm1 at p7_7
    show jin_glasses at p7_7
    with dissolve

    voice audio.lloyd_v_greet2a1
    l "Hey, guys! We’ve finished loading up all the luggage!"

    show darius play2 at p7_6
    voice audio.darius_v_laugh1
    d "Dibs on the window seat."

    show lloyd angry2 at p7_5
    voice audio.lloyd_v_question1b2
    l "Wh-Wha?! I won’t get to see the view – you’re gonna block the whole window with your giant body!"

    show darius bored5 at p7_6
    voice audio.darius_v_comp1a2
    d "There’s no point. You’ll end up sleeping, anyway."

    show lloyd pout1 at p7_5
    voice audio.lloyd_v_annoyed1b3
    l "Hmph! I’ll get there before you then!"

    hide lloyd_winter
    hide lloyd pout1
    with dissolve

    show darius bold2 at p7_6
    voice audio.darius_v_no1a
    d "No, you won’t."

    hide darius_winter
    hide darius bold2
    with dissolve

    show yuri_winter at p5_1
    show yuri norm1 at p5_1
    show goro_winter at p5_2
    show goro talk1 at p5_2
    show yoshi_winter at p5_3
    show yoshi relief2 at p5_3
    show aiden_winter at p5_4
    show aiden laugh2 at p5_4
    show jin_winter at p5_5
    show jin norm1 at p5_5
    show jin_glasses at p5_5
    with move

    voice audio.yoshi_v_jin5
    yo "Speaking of sleep, did you get enough rest, Jin?"

    show jin comp6 at p5_5
    show jin_glasses at p5_5
    voice audio.jin_v_yeah3a
    j "Ah, y-yeah! I’m sorry for passing out on you guys last night…!"

    show aiden comp6 at p5_4
    voice audio.aiden_v_laugh2a1
    a "You were sleeping like a baby, so we didn’t want to bother you, haha!"

    show jin comp2 at p5_5
    show jin_glasses at p5_5
    voice audio.jin_v_laugh1a
    j "It’s the first time this year I’ve had a normal sleep schedule. I’ll try to keep up with it, like I promised…!"

    show yuri angry2 at p5_1
    voice audio.yuri_v_jin2a
    yu "Sleep whenever you like, Jin! Don’t let that Emilia tell you how to live your life!"

    hide goro_winter
    hide goro talk1
    show goro2_winter at p5_2
    show goro2 sigh1 at p5_2
    voice audio.goro_v_yuri5b
    g "*sigh* Yuri..."

    show yuri_winter at p7_3
    show yuri angry2 at p7_3
    show goro2_winter at p7_4
    show goro2 sigh1 at p7_4
    show yoshi_winter at p7_5
    show yoshi relief2 at p7_5
    show aiden_winter at p7_6
    show aiden comp6 at p7_6
    show jin_winter at p7_7
    show jin comp2 at p7_7
    show jin_glasses at p7_7
    with move

    show emilia_winter at p7_1
    show emilia annoy1 at p7_1
    with dissolve

    e "..."

    hide yoshi_winter
    hide yoshi relief2
    show yoshi2_winter at p7_5
    show yoshi2 awkward3 at p7_5
    voice audio.yoshi_v_goodam1
    yo "G-Good morning, Emilia. Do you need help with your—"

    show emilia disgust5 at p7_1
    voice audio.emilia_v_ugh2a
    e "Don’t talk to me."

    hide emilia_winter
    hide emilia disgust5
    with dissolve

    show yuri_winter at p5_1
    show yuri angry2 at p5_1
    show goro2_winter at p5_2
    show goro2 sigh1 at p5_2
    show yoshi2_winter at p5_3
    show yoshi2 awkward3 at p5_3
    show aiden_winter at p5_4
    show aiden comp6 at p5_4
    show jin_winter at p5_5
    show jin comp2 at p5_5
    show jin_glasses at p5_5
    with move

    hide aiden_winter
    hide aiden comp6
    show aiden2_winter at p5_4
    show aiden2 upset5 at p5_4
    voice audio.aiden_v_sheesh1a
    a "Sheesh… Someone woke up the wrong side of the bed again, huh?"

    show yuri pout2 at p5_1
    voice audio.yuri_v_hmph1a
    yu "Just ignore her! I’m not letting Ms. Sourpuss ruin this trip for us!"

    show yoshi2 sad1 at p5_3
    yo "..."

    show goro2_winter at p5_1
    show goro2 sigh1 at p5_1
    show yoshi2_winter at p5_2
    show yoshi2 sad1 at p5_2
    show aiden2_winter at p5_3
    show aiden2 upset5 at p5_3
    show jin_winter at p5_4
    show jin comp2 at p5_4
    show jin_glasses at p5_4
    show yuri_winter at p5_5
    show yuri excited2 at p5_5
    with move

    voice audio.yuri_v_conj2a1
    yu "Jin and I already decided we’ll have a nice BL-reading session on the whole ride~!"

    hide jin_winter
    hide jin comp2
    hide jin_glasses
    show jin2_winter at p5_4
    show jin2 scheme2 at p5_4
    voice audio.jin_v_yes6b
    j "My laptop is all charged up and I brought my hard-drive too! We’ll go through my stash and watch the best BL dramas of all time! "

    hide yuri_winter
    hide yuri excited2
    show yuri2_winter at p5_5
    show yuri2 laugh3 at p5_5
    voice audio.yuri_v_celebrate1a
    yu "Yieeee! Come on, let’s get going already!"

    hide yuri2_winter
    hide yuri2 laugh3
    hide jin2_winter
    hide jin2 scheme2
    with dissolve

    show goro2_winter at left
    show goro2 norm1 at left
    show yoshi2_winter at center
    show yoshi2 norm1 at center
    show aiden2_winter at right
    show aiden2 upset5 at right
    with move

    hide aiden2_winter
    hide aiden2 upset5
    show aiden_winter at right
    show aiden play2 at right
    voice audio.aiden_v_laugh1b1
    a "Hehe, everyone’s super excited, huh?"

    hide yoshi2_winter
    hide yoshi2 norm1
    show yoshi_winter at center
    show yoshi happy2 at center
    voice audio.yoshi_v_yeah1
    yo "Yeah, it feels like we’re going on a school field trip!"

    show aiden confused2 at right
    voice audio.aiden_v_think1a1
    a "Now I’m really curious about what kind of fun stuff we’ll see at that hotel~"

    hide goro2_winter
    hide goro2 norm1
    show goro_winter at left
    show goro talk3 at left
    voice audio.goro_v_rush1a1
    g "We should board the shuttle, then. We’ll find out once we get there. "

    hide goro_winter
    hide goro talk1
    with dissolve

    show aiden happy2 at right
    voice audio.aiden_v_amazed2b2
    a "Wow, Gramps can’t hide his excitement either, huh?"

    show yoshi laugh1 at center
    voice audio.yoshi_v_laugh1
    yo "Hahaha!"

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black
    hide screen location
    hide screen timeline
    hide screen quick_menu
    $quick_menu = False
    with fade
    play sound sfx_busdoor
    $ renpy.pause (2.0, hard=True)
    play sound sfx_busengine
    $ renpy.pause (2.0, hard=True)

    $ location = location_bus
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene cg7 1 with fade
    play bgsound sfxloop_carride loop
    play music buddy_oath_casual loop
    voice audio.aiden_vs8_line1
    a "Alright, it’s gonna be a long ride! Who’s up for some snacks?"

    voice audio.aiden_vs8_line2
    a "I brought everyone’s favorites~! All homemade too! "

    show cg7 2 with Dissolve(0.25)
    voice audio.yoshi_vs8_line1
    yo "Wow, you didn’t have to do all of this, Aiden! But I’ll always say yes to your pulled pork sandwich! "

    voice audio.aiden_vs8_line3
    a "It’s barbecue~! Just how you like it!"

    show cg7 3 with Dissolve(0.25)
    voice audio.lloyd_vs8_line1
    l "Ooh! Ooh! I want some too! "

    voice audio.aiden_vs8_line4
    a "Calm down, there’s plenty for everyone~!"

    voice audio.lloyd_vs8_line2
    l "This’ll be perfect with the chips I brought!"

    show cg7 4 with Dissolve(0.25)
    voice audio.darius_vs8_line1
    d "So much for healthy eating."

    voice audio.lloyd_vs8_line3
    l "It’s not a field trip without some junk food! And besides, it’s my cheat day!"

    show cg7 5 with Dissolve(0.25)
    voice audio.goro_vs8_line1
    g "I expect the hotel will have some nice food as well, so I’m betting today won’t be your only cheat day."

    show cg7 6 with Dissolve(0.25)
    voice audio.aiden_vs8_line5
    a "How about you, Jin? Want some?"

    show cg7 7 with Dissolve(0.25)
    voice audio.jin_vs8_line1
    j "*heaves*"

    voice audio.jin_vs8_line2
    j "N-No, thank you…"

    voice audio.yoshi_vs8_line2
    yo "Are you feeling unwell, Jin? "

    voice audio.yuri_vs8_line1
    yu "It looks like he’s a little bit car sick…"

    voice audio.yuri_vs8_line2
    yu "The moment the bus started moving, he started gagging..."

    voice audio.jin_vs8_line3
    j "I-I’m sorry… I didn’t expect the bus ride would make my tummy turn…"

    show cg7 8 with Dissolve(0.25)
    voice audio.aiden_vs8_line6
    a "Good thing I came prepared! Here’s some meds, Jin~! They might make you drowsy, though!"

    voice audio.jin_vs8_line4
    j "Th-Thanks… I’ll take anything to end this suffering…"

    voice audio.aiden_vs8_line7
    a "I brought some barf bags too in case you—"

    show cg7 9 with Dissolve(0.25)
    voice audio.jin_vs8_line5
    j "*heaves*"

    #voice audio.aiden_vs8_line8
    a "Aww, poor Jin…"

    show cg7 10 with Dissolve(0.25)
    voice audio.jin_vs8_line6
    j "S-Sorry, Yuri… I know you wanted to watch BL movies…"

    voice audio.yuri_vs8_line4
    yu "Oh dear, there’ll be plenty of other times for that! "

    voice audio.yuri_vs8_line5
    yu "Just lay back and I’ll take care of you~"

    show cg7 11 with Dissolve(0.25)
    voice audio.aiden_vs8_line9
    a "More snacks for us, then!"

    show cg7 12 with Dissolve(0.25)
    voice audio.lloyd_vs8_line4
    l "Woo! It’s starting to snow! Look! Look!"

    show cg7 13 with Dissolve(0.25)
    voice audio.darius_vs8_line2
    d "Lloyd, calm down. It’s just snow."

    voice audio.yoshi_vs8_line3
    yo "Winter has finally come, huh? It’s a good thing our vacation is going to be mostly indoors. "

    voice audio.goro_vs8_line2
    g "Either way, we have warm clothes packed."

    show cg7 14 with Dissolve(0.25)
    voice audio.yuri_vs8_line6
    yu "*ehem* I told you guys~"

    voice audio.aiden_vs8_line10
    a "Brr… I can already feel the cold, even from in here!"

    voice audio.goro_vs8_line3
    g "We still have a long way to go; the destination is in the capital, after all."

    show cg7 15 with Dissolve(0.25)
    #voice audio.yoshi_vs8_line4
    yo "Don’t worry, I brought my guitar along! We can pass the time with some carpool karaoke~!"

    voice audio.yoshi_vs8_line5
    yo "I hope you all know the lyrics to ‘Greatest Memories’! "

    voice audio.lloyd_vs8_line5
    l "To what…? "

    voice audio.emilia_vs8_line1
    e "*facepalms* Eugh…"
    d "..."

    voice audio.yuri_vs8_line7
    yu "Ugh, Yoshi… seriously?"

    show cg7 16 with Dissolve(0.25)
    voice audio.yoshi_vs8_line6
    yo "Wh-What…? A little entertainment wouldn’t hurt, right?"

    voice audio.aiden_vs8_line11
    a "I’m always down for a sing-along~!"

    voice audio.yuri_vs8_line8
    yu "Sing-along? We’re not campers anymore, Yoshi. "

    voice audio.goro_vs8_line4
    g "It’ll be just like having a campfire song."

    show cg7 17 with Dissolve(0.25)
    voice audio.yoshi_vs8_line7
    yo "See? Sir Goro and Aiden have the camping spirit, even when we’re on a bus!"

    voice audio.yoshi_vs8_line8
    yo "Give it up for ‘Camp Bus-sy’!"

    show cg7 18 with Dissolve(0.25)
    voice audio.jin_vs8_line7
    j "Pfft—!!"

    voice audio.yoshi_vs8_line9
    yo "Alright, come on everyone, I wanna hear you all sing~"

    voice audio.yuri_vs8_line9
    yu "Ugh… This is gonna be a long ride…"

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black with fade

    yo "{i}(I spent the next little while playing guitar and singing for everyone, and eventually, despite their protests, most of them got pretty into it!){/i}"
    yo "{i}(It didn’t take long for the bus ride to make us all tired though, and we ended up falling asleep for the rest of the journey…){/i}"
    yo "{i}(We woke up to the sound of the bus pulling up to the hotel…){/i}"

    scene cg black
    hide screen location
    hide screen timeline
    hide screen quick_menu
    $quick_menu = False
    with fade
    play sound sfx_busengine
    $ renpy.pause (2.0, hard=True)
    play sound sfx_busdoor
    $ renpy.pause (2.0, hard=True)

    $ location = location_hotellobby
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_hotel_lobby_day with fade
    play music buddy_oath_hotel loop

    show darius_winter at p7_1
    show darius shock1 at p7_1
    show aiden_winter at p7_3
    show aiden scared3 at p7_3
    show lloyd_winter at p7_2
    show lloyd excited6 at p7_2
    show yoshi_winter at p7_4
    show yoshi shock3 at p7_4
    show goro_winter at p7_5
    show goro shock2 at p7_5
    show yuri_winter at p7_6
    show yuri shock5 at p7_6
    show jin_winter at p7_7
    show jin_glasses at p7_7
    show jin shock1 at p7_7
    voice audio.yoshi_v_amazed1a
    yo "Wow… Look at this place! It’s like we stepped into a whole new world!"

    show goro panic4 at p7_5
    voice audio.goro_v_shock2b1
    g "I-I sort of expected something fancy from just the exterior, but this is far more extravagant than I what was prepared for. Mr. Clermont has really outdone himself…"

    show yuri amazed1 at p7_6
    voice audio.yuri_v_goro1b
    yu "How come you’ve never brought us somewhere like this before, Dad?!"

    show goro shy4 at p7_5
    voice audio.goro_v_yuridear4b
    g "Both the camp and I would go bankrupt if I did that, dear…"

    show lloyd amazed4 at p7_2
    voice audio.lloyd_v_amazed2a1
    l "The architecture of this place is AMAZING! Just look at the intricate designs! Where do I begin? It’s a sensory overload!"
    l "It would take a real expert to conceptualize and deliver this level of craftmanship! "

    show darius excited1 at p7_1
    voice audio.darius_v_confused1c
    d "Must be very expensive too."
    d "That ceiling alone must have cost a fortune."

    show jin shock2 at p7_7
    voice audio.jin_v_whoa3a
    j "I only see these kinds of fancy places in movies. It feels so surreal to actually be in one."

    hide aiden_winter
    hide aiden scared3
    show aiden2_winter at p7_3
    show aiden2 upset6 at p7_3
    voice audio.aiden_v_agree4a
    a "I know, right? Even the people walking around look hella rich… I kinda feel a little out of place here."

    show yoshi awkward4 at p7_4
    voice audio.yoshi_v_yeah1
    yo "Yeah, the fact that we’re staying here almost makes me feel guilty, if I’m being honest. "

    hide goro_winter
    hide goro shy4
    show goro2_winter at p7_5
    show goro2 shy6 at p7_5
    voice audio.goro_v_think1a1
    g "I feel the same way…"
    g "I’ve never been in a hotel as extravagant as this. I can only imagine how much Mr. Clermont spent on this trip…"

    show aiden2 panic5 at p7_3
    voice audio.aiden_v_hngh1b2
    a "Hngh… I don’t even wanna think about that…"

    show yuri comp2 at p7_6
    voice audio.yuri_v_guys1a
    yu "Oh, come on guys, we’re here for a vacation! Mr. Clermont expects us to have fun and relax here!"
    yu "So, I’ll do just that! Hahaha! I’ll make sure every cent he spent on us is worth it~!"

    show lloyd pain5 at p7_2
    voice audio.lloyd_v_groan2c3
    l "ARGH! I’m so mad I didn’t bring my DSLR camera for this trip! I wanna take a bunch of pictures of the interior for my design references!!"

    show jin awkward3 at p7_7
    voice audio.jin_v_think2b1
    j "U-Umm… I brought one with me… If you want, I can take the pictures for you."

    show lloyd comp2 at p7_2
    voice audio.lloyd_v_shock1b1
    l "Oh, you’re a lifesaver, Jin! Take a picture of that chandelier, and that column over there, and oooh! That statue in the corner too!"

    show darius annoy2 at p7_1
    voice audio.darius_v_comp2
    d "Give him a break, Lloyd. Jin might still be feeling car sick."

    show jin comp2 at p7_7
    voice audio.jin_v_comp8b1
    j "I-I’m fine…! Besides I already started taking pictures of you guys."

    show yoshi shock3 at p7_4
    voice audio.yoshi_v_oops1
    yo "Oh my goodness, you must’ve caught our jaws dropping when we walked in…"

    show jin laugh1 at p7_7
    voice audio.jin_v_laugh1a
    j "It’ll be good to document our experiences here. Besides, natural, candid shots are more fun to look at."

    hide goro2_winter
    hide goro2 shy6
    show goro_winter at p7_5
    show goro play2 at p7_5
    voice audio.goro_v_laugh2a
    g "Who knew Jin was also a photographer, haha! "

    show jin comp6 at p7_7
    voice audio.jin_v_ah2a
    j "A-Ah, I only do it for fun… I just got into it because I started taking pictures of cosplayers at anime conventions."

    hide yuri_winter
    hide yuri comp2
    show yuri2_winter at p7_6
    show yuri2 fangirl3 at p7_6
    voice audio.yuri_v_kyaa1a
    yu "Kyaaa! You should show me those pics some time, Jin~! I bet there’s some super sexy ones!"

    hide jin_winter
    hide jin comp6
    hide jin_glasses
    show jin2_winter at p7_7
    show jin2 fudan3 at p7_7
    show jin2_glasses2 at p7_7
    voice audio.jin_v_gulp1a
    j "*gulp* How did you know…"

    show yoshi comp2 at p7_4
    voice audio.yoshi_v_laugh1
    yo "Haha, everyone seems really overwhelmed with the hotel, and we’re only in the lobby. "

    show aiden2 worry2 at p7_3
    voice audio.aiden_v_yeah1g1
    a "Yeah, no kidding. This place is almost too perfect."

    show darius_winter at p8_2
    show darius annoy2 at p8_2
    show lloyd_winter at p8_1
    show lloyd comp2 at p8_1
    show aiden2_winter at p8_3
    show aiden2 worry2 at p8_3
    show yoshi_winter at p8_4
    show yoshi comp2 at p8_4
    show goro_winter at p8_5
    show goro play2 at p8_5
    show yuri2_winter at p8_6
    show yuri2 fangirl3 at p8_6
    show jin2_winter at p8_7
    show jin2 fudan3 at p8_7
    show jin2_glasses2 at p8_7
    with move

    show yuri_winter at p8_6
    show yuri comp2 at p8_6
    hide yuri2_winter
    hide yuri2 fangirl3

    show emilia_winter at p8_8
    show emilia pain4 at p8_8
    with dissolve

    hide darius_winter
    hide darius annoy2
    show darius_winter at p8_2
    show darius annoy2 at p8_2
    hide lloyd_winter
    hide lloyd comp2
    show lloyd_winter at p8_1
    show lloyd comp2 at p8_1
    voice audio.emilia_v_surprised1a
    e "Hnghhh…!! Why in the world is no one helping me with my luggage?!"

    hide jin2_winter
    hide jin2 fudan6
    hide jin2_glasses2
    show jin_winter at p8_7
    show jin worry1 at p8_7
    show jin_glasses at p8_7
    show yuri annoy2 at p8_6
    voice audio.yuri_v_aiden4a
    yu "Guess you spoke too soon, Aiden."

    show goro_winter at p8_4
    show goro play2 at p8_4
    show yuri_winter at p8_5
    show yuri annoy2 at p8_5
    show jin_winter at p8_6
    show jin worry1 at p8_6
    show jin_glasses at p8_6
    show yoshi_winter at p8_7
    show yoshi talk3 at p8_7
    with move

    voice audio.yoshi_v_ah3
    yo "A-Ah, Emilia, let me help you."

    show emilia angry2 at p8_8
    voice audio.emilia_v_disagree2a1
    e "Don’t bother. There are people here paid to be doing this."
    e "What kind of service does this place have!? A bellboy should have helped me with my bags the moment we got off that shuttle!"

    show emilia rage4 at p8_8
    voice audio.emilia_v_request4b
    e "I can’t believe no one welcomed me either, do they even know who sent us here?! Where’s my room?! I thought this was a five-star luxury hotel?! "
    e "I want to speak with the manager!!"

    hide yoshi_winter
    hide yoshi talk3
    show yoshi2_winter at p8_7
    show yoshi2 worry2 at p8_7
    hide jin_winter
    hide jin worry1
    hide jin_glasses
    show jin_winter at p8_6
    show jin worry1 at p8_6
    show jin_glasses at p8_6
    voice audio.yoshi_v_please1b
    yo "Emilia, please calm down. You can see the staff are busy… Just wait for a little…"

    show yuri annoy4 at p8_5
    voice audio.yuri_v_hmph1a
    yu "Told you she’s just gonna find something to complain about…"

    show jin worry4 at p8_6
    voice audio.jin_v_worry1a3
    j "It’s a little embarrassing that she’s making a scene… a lot of people are starting to look at us…"

    show lloyd worry3 at p8_1
    voice audio.lloyd_v_agree2c1
    l "Yeah… I don’t think screaming like that makes the service any faster…"

    show darius disgust5 at p8_2
    voice audio.darius_v_emilia5a
    d "She’s a Karen."

    show yuri irked1 at p8_5
    voice audio.yuri_v_ugh3a
    yu "I liked it better when she stayed quiet in the shuttle."

    show darius_winter at p9_2
    show darius disgust5 at p9_2
    show lloyd_winter at p9_3
    show lloyd worry3 at p9_3
    show aiden2_winter at p9_4
    show aiden2 worry2 at p9_4
    show goro_winter at p9_5
    show goro play2 at p9_5
    show yuri_winter at p9_6
    show yuri irked1 at p9_6
    show jin_winter at p9_7
    show jin worry4 at p9_7
    show jin_glasses at p9_7
    show yoshi2_winter at p9_8
    show yoshi2 worry2 at p9_8
    show emilia_winter at p9_9
    show emilia rage4 at p9_9
    with move

    show reimond_bellboy at p9_1
    show reimond happy1 at p9_1
    with dissolve

    voice audio.reimond_v_greet4a
    r "Greetings! Welcome to the Grand O’ Hotel. You deserve a release!"

    hide aiden2_winter
    hide aiden2 worry2
    show aiden_winter at p9_4
    show aiden awkward3 at p9_4
    voice audio.aiden_v_amazed2a1
    a "Wow… Even the crew here have fancy taglines."

    show emilia eyeroll6 at p9_9
    voice audio.emilia_v_ugh1
    e "Ugh! It’s about time!"

    show goro talk3 at p9_5
    voice audio.goro_v_goodam1a1
    g "Hello, we have a reservation made by Clermont Inc."

    show reimond happy2 at p9_1
    voice audio.reimond_v_ah1a
    r "Ah! Mr. Clermont’s party! One of our VIP Guests! We’ve been expecting you!"
    r "Allow me to explain all the amenities included in your package!"

    show reimond happy3 at p9_1
    voice audio.reimond_v_conj2a1
    r "Since you are VIP guests, your food, room, and entertainment are included in your stay, on top of priority access to all our facilities!"

    hide yoshi2_winter
    hide yoshi2 worry2
    show yoshi_winter at p9_8
    show yoshi shock2 at p9_8
    hide emilia_winter
    hide emilia eyeroll6
    show emilia_winter at p9_9
    show emilia eyeroll6 at p9_9
    voice audio.yoshi_v_shock1b
    yo "Whoa… It sounds like we’re going to be treated like royalty here…"

    show reimond happy1 at p9_1
    voice audio.reimond_v_agree4b
    r "Of course! This hotel offers maximum luxury, fit for kings and queens!"

    show emilia angry6 at p9_9
    voice audio.emilia_v_celebrate1c
    e "Finally. Something closer to home. "

    show reimond talk2 at p9_1
    voice audio.reimond_v_conj3a
    r "Now, Mr. Clermont has arranged four master king suites for the executive staff. "
    r "Each room can accommodate up to four people. Here are your room keys, please feel free to divide your party as you see fit!"
    r "Once you all have decided, I’ll have our staff move your luggage to your rooms!"

    show reimond explain2 at p9_1
    voice audio.reimond_v_callme1b
    r "If you need anything else, our front desk is available 24/7, so please don’t hesitate to call us!"

    show goro happy2 at p9_5
    voice audio.goro_v_thanks2a1
    g "Thank you, we’ll let you know if we need anything else."

    show reimond grin1 at p9_1
    voice audio.reimond_v_response1b1
    r "My pleasure~! I hope you all enjoy your stay here at the Grand O’."

    hide reimond_bellboy
    hide reimond grin1
    with dissolve

    show darius_winter at p8_1
    show darius disgust5 at p8_1
    show lloyd_winter at p8_2
    show lloyd excited1 at p8_2
    show aiden_winter at p8_3
    show aiden awkward3 at p8_3
    show goro_winter at p8_4
    show goro happy2 at p8_4
    show yuri_winter at p8_5
    show yuri irked1 at p8_5
    show jin_winter at p8_6
    show jin worry4 at p8_6
    show jin_glasses at p8_6
    show yoshi_winter at p8_7
    show yoshi shock2 at p8_7
    show emilia_winter at p8_8
    show emilia angry6 at p8_8
    with move

    voice audio.lloyd_v_amazed1b1
    l "Wow… I was expecting that we’d all just stay in one room…"

    show darius shock2 at p8_1
    voice audio.darius_v_agree4
    d "Me too."

    hide goro_winter
    hide goro happy2
    show goro2_winter at p8_4
    show goro2 confused6 at p8_4
    voice audio.goro_v_yeah1c2
    g "Yeah… It seems a little overkill to give us four master king suites with a party of our size… "

    hide aiden_winter
    hide aiden awkward3
    show aiden2_winter at p8_3
    show aiden2 awkward5 at p8_3
    voice audio.aiden_v_william7a
    a "It’s Mr. Clermont we’re talking about after all…"

    hide goro2_winter
    hide goro2 darius_v_confused1c
    show goro_winter at p8_4
    show goro talk1 at p8_4
    voice audio.goro_v_anyway2
    g "Anyway, there’s eight of us, so it’s only natural to split the rooms into pairs… Is everyone good with that?"

    show lloyd laugh2 at p8_2
    voice audio.lloyd_v_praise3a
    l "Pairs sound fun~ Me and Darius count as one!"

    show darius happy1 at p8_1
    voice audio.darius_v_agree3
    d "I have no objection. "

    show yuri worry2 at p8_5
    voice audio.yuri_v_think2a1
    yu "As the only girl here… Do I have to, uhh… bunk with… her?"

    show jin comp2 at p8_6
    voice audio.jin_v_conj2c1
    j "W-Well, I don’t mind sharing a room with you, Yuri… We can make up for the lost time on the bus ride watching BL."

    hide yuri_winter
    hide yuri worry2
    show yuri2_winter at p8_5
    show yuri2 drool2 at p8_5
    voice audio.yuri_v_agree1d1
    yu "YES! YES! Good idea!"

    hide goro_winter
    hide goro talk1
    show goro2_winter at p8_4
    show goro2 bored1 at p8_4
    voice audio.goro_v_ehem1a
    g "*ehem* You’re my daughter so you’re staying with me. It’s been a while since we had some father-daughter bonding time."

    hide yuri2_winter
    hide yuri2 drool2
    show yuri_winter at p8_5
    show yuri pout1 at p8_5
    voice audio.yuri_v_goro7a
    yu "Aww, Dad! Why did you have to pull the family card now…?"

    show jin shy5 at p8_6
    voice audio.jin_v_think2b1
    j "C-Can anyone else stay with me…?  "

    show lloyd tease2 at p8_2
    voice audio.lloyd_v_jin2c
    l "That’s the nice way of saying “anyone but Ms. Emilia”, Jin."

    show darius tease2 at p8_1
    voice audio.darius_v_shh1
    d "Shh, Lloyd. She’s right over there."

    show emilia annoy2 at p8_8
    voice audio.emilia_v_hmph1a
    e "Hmph, bold of you people to assume I want to share a room with the likes of you! "

    show emilia_winter at p8_4
    show emilia annoy1 at p8_4
    with move

    show emilia_winter at p8_8
    show emilia annoy1 at p8_8
    with move

    e "*snatches keys*"

    show emilia irked2 at p8_8
    voice audio.emilia_v_thanks3
    e "Just like at the camp, I require my own room, thank you very much."
    e "I hate to stay and listen to your pointless bickering, so I’d best be on my way."

    hide emilia_winter
    hide emilia irked2
    with dissolve

    show darius_winter at p7_1
    show darius tease2 at p7_1
    show lloyd_winter at p7_2
    show lloyd tease2 at p7_2
    show aiden2_winter at p7_3
    show aiden2 awkward5 at p7_3
    show goro2_winter at p7_4
    show goro2 bored1 at p7_4
    show yuri_winter at p7_5
    show yuri angry3 at p7_5
    show jin_winter at p7_6
    show jin comp2 at p7_6
    show jin_glasses at p7_6
    show yoshi_winter at p7_7
    show yoshi shock2 at p7_7
    with move

    voice audio.yuri_v_what5a
    yu "What a hog! She gets a room all to herself?! "

    hide yoshi_winter
    hide yoshi shock2
    show yoshi2_winter at p7_7
    show yoshi2 awkward3 at p7_7
    voice audio.yoshi_v_uh1a
    yo "That might be for the best. I don’t think any of us would want to share a room with her in the first place."

    show yuri think2 at p7_5
    voice audio.yuri_v_think1a1
    yu "Fair point. "

    show lloyd happy2 at p7_2
    voice audio.lloyd_v_conj1a3
    l "Well, we don’t mind sharing a room with Jin. Right, Dar?"

    show darius tease4 at p7_1
    voice audio.darius_v_comp3a
    d "I’m okay with a three-way."

    hide jin_winter
    hide jin comp2
    hide jin_glasses
    show jin2_winter at p7_6
    show jin2 dizzy2 at p7_6
    show jin2_glasses at p7_6
    voice audio.jin_v_wah1b
    j "*gulp* W-Wahhh…"

    hide yuri_winter
    hide yuri think2
    show yuri2_winter at p7_5
    show yuri2 jizz1 at p7_5
    voice audio.yuri_v_fujo3a
    yu "JSKAJDKWQAK WHAT?! "

    show lloyd tease3 at p7_2
    voice audio.lloyd_v_laugh1a2
    l "Besides, we need a trusty cameraman to film exciting videos for us~"

    show jin2 dizzy6 at p7_6
    voice audio.jin_v_gasp2a
    j "C-Cameraman?!"

    show yuri2 drool3 at p7_5
    voice audio.yuri_v_fujo5a
    yu "I-In the bedroom?! "

    show aiden2_winter at p7_1
    show aiden2 awkward5 at p7_1
    show goro2_winter at p7_2
    show goro2 bored1 at p7_2
    show yuri2_winter at p7_3
    show yuri2 drool3 at p7_3
    show darius_winter at p7_4
    show darius grin4 at p7_4
    show jin2_winter at p7_5
    show jin2 dizzy6 at p7_5
    show jin2_glasses at p7_5
    show lloyd_winter at p7_6
    show lloyd tease3 at p7_6
    with move

    voice audio.darius_v_rush1
    d "Come, Jin."

    show lloyd laugh3 at p7_6
    voice audio.lloyd_v_agree4a1
    l "We’re gonna have some fun tonight! "

    hide lloyd_winter
    hide lloyd laugh3
    hide darius_winter
    hide darius grin4
    hide jin2_winter
    hide jin2 dizzy6
    hide jin2_glasses
    with dissolve

    show aiden2_winter at p4_1
    show aiden2 awkward5 at p4_1
    show goro2_winter at p4_2
    show goro2 bored1 at p4_2
    show yuri2_winter at p4_3
    show yuri2 drool3 at p4_3
    show yoshi2_winter at p4_4
    show yoshi2 awkward3 at p4_4
    with move

    hide yoshi2_winter
    hide yoshi2 awkward3
    show yoshi_winter at p4_4
    show yoshi happy1 at p4_4
    voice audio.yoshi_v_so1a
    yo "That leaves Aiden and I sharing a room then! "

    hide aiden2_winter
    hide aiden2 awkward5
    show aiden_winter at p4_1
    show aiden happy1 at p4_1
    voice audio.aiden_v_alright1a1
    a "Alright~ It’s about time the two of us got some privacy!"

    show yuri2 jizz2 at p4_3
    voice audio.yuri_v_wait1e1
    yu "WAIT, WAIT! If there’s gonna be action in BOTH of the other rooms, CAN I CHANGE ROOMS?!"

    show goro2_winter at center
    show goro2 annoy3 at center
    with move

    voice audio.goro_v_rush3a1
    g "You’re coming with me. "

    show yuri2 scared2 at p4_3
    voice audio.yuri_v_no1c1
    yu "Nooooooo!!!!"

    hide yuri2_winter
    hide yuri2 scared2
    hide goro2_winter
    hide goro2 annoy3
    with dissolve

    show aiden_winter at left2
    show aiden happy1 at left2
    show yoshi_winter at right2
    show yoshi comp5 at right2
    with move

    voice audio.yoshi_v_well1
    yo "Well, I’m glad Yuri’s back to normal at least."

    show aiden laugh1 at left2
    voice audio.aiden_v_laugh2a1
    a "Hahaha! You know she can’t resist when it comes to her fantasies!"

    hide yoshi_winter
    hide yoshi comp5
    show yoshi2_winter at right2
    show yoshi2 annoy3 at right2
    voice audio.yoshi_v_sigh3a
    yo "You don’t exactly help with that either, you know."

    show aiden play2 at left2
    voice audio.aiden_v_hey1b2
    a "Hey, it’s fun to tease her! And you for that matter~"

    show yoshi2 shy5 at right2
    voice audio.yoshi_v_ehem1b
    yo "*ehem* A-Anyway, we should go check out our room."

    show aiden happy2 at left2
    voice audio.aiden_v_agree3a1
    a "Sure thing, Yoshi!"

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black
    hide screen location
    hide screen timeline
    hide screen quick_menu
    $quick_menu = False
    with fade
    play sound sfx_elevator
    $ renpy.pause (1.0, hard=True)
    play sound sfx_elevatordoor
    $ renpy.pause (2.0, hard=True)

    $ location = location_hotelroom
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_hotel_room1_day with fade
    play music close_distance loop

    show yoshi_winter at left2
    show yoshi shock2 at left2
    show aiden_winter at right2
    show aiden shock1 at right2
    voice audio.yoshi_v_shock1b
    yo "Whoa… I guess I shouldn’t be surprised, but the room is luxurious too…  "
    yo "Just look at that view, it’s like we’re in the sky…! "

    hide aiden_winter
    hide aiden shock1
    show aiden2_winter at right2
    show aiden2 sigh4 at right2
    voice audio.aiden_v_think2a
    a "I don’t know if I can relax in some place as fancy as this… You know me, I’d rather be outdoors.  "

    show yoshi comp3 at left2
    voice audio.yoshi_v_huh5
    yo "We’ve gotten so used to being surrounded by trees and staying in wooden cabins all the time, huh?"

    show aiden2 worry2 at right2
    voice audio.aiden_v_yeah1g1
    a "Yeah… Compared to Camp Buddy, this is a completely different world."

    hide yoshi_winter
    hide yoshi comp3
    show yoshi2_winter at left2
    show yoshi2 worry1 at left2
    yo "{i}Aiden seems like he’s a little overwhelmed from all the luxury…{/i}"

    $ working = False
    $ shuffle_menu()
    menu():
        yo "{i}Aiden seems like he’s a little overwhelmed from all the luxury…{/i}{fast}"
        "We're on vacation.":
            $working = True
            $score_aiden -= 1
            $score_bot += 1
            hide yoshi2_winter
            hide yoshi2 worry1
            show yoshi_winter at left2
            show yoshi comp5 at left2
            voice audio.yoshi_v_comp2
            yo "Isn’t that a good thing, though? We’re on vacation, after all!"

            hide aiden2_winter
            hide aiden2 worry2
            show aiden_winter at right2
            show aiden sigh1 at right2
            voice audio.aiden_v_agree2b1
            a "Yeah, you’re right… And I’ve been looking forward to spending some quality time with you, but I guess everything being so fancy caught me off guard…"

            show yoshi talk1 at left2
            voice audio.yoshi_v_well1
            yo "Well, it’s no fun if we just stay in the room. Why don’t we go and check out what else we could do here?"
            yo "They gave me a hotel brochure, so let’s take a look!"
        "We deserve the break.":
            $working = True
            $score_aiden -= 1
            $score_top += 1
            hide yoshi2_winter
            hide yoshi2 worry1
            show yoshi_winter at left2
            show yoshi comp2 at left2
            voice audio.yoshi_v_comp2
            yo "It’s nice to take a break in a place like this every once in a while. We’re not going to stay here forever, after all."

            hide aiden2_winter
            hide aiden2 worry2
            show aiden_winter at right2
            show aiden sigh1 at right2
            voice audio.aiden_v_agree2b1
            a "Yeah, you’re right… And I’ve been looking forward to spending some quality time with you, but I guess everything being so fancy caught me off guard…"

            show yoshi talk1 at left2
            voice audio.yoshi_v_well1
            yo "Well, it’s no fun if we just stay in the room. Why don’t we go and check out what else we could do here?"
            yo "They gave me a hotel brochure, so let’s take a look!"
        "Let's do something fun.":
            $working = True
            $score_aiden += 1
            $score_bot += 1
            hide yoshi2_winter
            hide yoshi2 worry1
            show yoshi_winter at left2
            show yoshi comp2 at left2
            voice audio.yoshi_v_think4
            yo "Why don’t we do something fun then, Aiden?"

            hide aiden2_winter
            hide aiden2 worry2
            show aiden_winter at right2
            show aiden tease1 at right2
            voice audio.aiden_v_oho1a
            a "Oho~ Looks like someone can’t wait to get the action going?"

            show yoshi talk1 at left2
            voice audio.yoshi_v_what4
            yo "W-What?! I-I meant around the hotel…"

            show aiden shock2 at right2
            voice audio.aiden_v_shock1d2
            a "Whoa, I didn’t think you were the type who’d like to do it in public too!"

            show yoshi explain2 at left2
            voice audio.yoshi_v_well2
            yo "What I’m trying to say is that we should go explore and check out what kind of fun stuff is here!"

            show aiden wink3 at right2
            voice audio.aiden_v_agree5b
            a "I know, I know, I’m just kidding, hahaha! You should see the look on your face!"

            show yoshi sigh1 at left2
            voice audio.yoshi_v_sigh3a
            yo "*sigh*"

            show aiden talk2 at right2
            voice audio.aiden_v_but1a2
            a "But you’re right, if we just stay in the room, we’ll probably get bored at some point."
            a "Unless~"

            hide yoshi_winter
            hide yoshi sigh1
            show yoshi2_winter at left2
            show yoshi2 think2 at left2
            voice audio.yoshi_v_ehem1b
            yo "*ehem* So, they gave me this hotel brochure. Let’s check it out."
        "Lay in bed with me.":
            $working = True
            $score_aiden += 1
            $score_top +=1
            hide yoshi2_winter
            hide yoshi2 worry1
            show yoshi_winter at left2
            show yoshi comp2 at left2
            voice audio.yoshi_v_encourage3
            yo "Either way, we better make the most out of it. "

            play sound sfx_clotheschanging
            show yoshi happy1 at left2
            voice audio.yoshi_v_think4
            yo "Here, why don’t you lay down with me?"

            hide aiden2_winter
            hide aiden2 worry2
            show aiden_winter at right2
            show aiden tease1 at right2
            voice audio.aiden_v_oho1a
            a "Oho~ Looks like someone can’t wait to get the action going?"

            show yoshi shock2 at left2
            voice audio.yoshi_v_what4
            yo "Wh-What—"

            show aiden bold2 at right2
            voice audio.aiden_v_excited2a
            a "Don’t mind if I do~!"

            show aiden_winter at center
            show aiden bold2 at center
            with move

            play sound sfx_clotheschanging
            a "*jumps into bed*"

            show aiden shock3 at center
            voice audio.aiden_v_shock1c2
            a "WHOA…!! These beds are damn soft… and the sheets even smell like flowers! Now, I could get used to this~"
            a "Wait… what’s that stuck in the pillows?"

            show yoshi talk3 at left2
            voice audio.yoshi_v_oh1
            yo "Oh, this must be the hotel brochure. Let’s take a look."

    #minimap mode
    $mm_talking = True
    $ daya3_choice = False
    $ day3_aiden = True
    $renpy.choice_for_skipping()
    show screen minimap()

    voice audio.aiden_v_swear2a1
    a "Damn, look at all this cool stuff! They have a spa, café, gym and, oooh! A bar!"

    voice audio.yoshi_v_shock1a
    yo "Whoa… This place really has everything… You could live like a king if you had the money to stay here for the rest of your life…"

    voice audio.aiden_v_really2a
    a "And all of these are free?!"

    voice audio.yoshi_v_actually1a
    yo "Apparently it’s all part of the package Mr. Clermont got for us…"

    voice audio.aiden_v_so2
    a "So, where do you think we should go first?"

    $ say_box = False
    $mm_talking = False
    $quick_menu = False
    $ renpy.pause (hard=True)

label day3_aiden_spa:
    $sq_goro += 1
    $quick_menu = True
    $a3_spa = True
    $mm_talking = True
    $say_box = True
    voice audio.yoshi_v_think4
    yo "It’d be nice to relax a little bit, so how about we try the spa?"

    if daya3_choice == False:
        voice audio.aiden_v_praise3b
        a "Ooh! Good idea! I could really use that after a long trip! "
    else:
        voice audio.aiden_v_agree3a1
        a "Sure thing! I’ve been wanting to check it out, too!"

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
    play sound sfx_splash
    $ renpy.pause (2.0, hard=True)

    if daya3_choice == False:
        $ location = location_hotelspa
        show screen location
        show screen timeline
        show screen quick_menu
        $quick_menu = True
        scene bg_hotel_spa_day with fade
        play music old_familiar_home loop
        play bgsound sfxloop_waterflow loop
    else:
        $ location = location_hotelspa
        show screen location
        show screen timeline
        show screen quick_menu
        $quick_menu = True
        scene bg_hotel_spa_sunset with fade
        play music old_familiar_home loop
        play bgsound sfxloop_waterflow loop

    show yoshi_towel at left2
    show yoshi relief1 at left2
    show aiden_towel at right2
    show aiden relief4 at right2
    voice audio.aiden_v_relief2a
    a "Ahh~ That hits the spot!  "

    show yoshi relief4 at left2
    voice audio.yoshi_v_yeah2
    yo "Yeah… I can’t remember the last time I took an actual bath… We’ve only had showers back at camp."

    show aiden confused2 at right2
    voice audio.aiden_v_whistle1a
    a "I don’t know how they did it, but even the water here feels expensive…"

    show yoshi relief5 at left2
    voice audio.yoshi_v_think1a
    yo "I think they put some kind of lavender scent in it…"

    show aiden tease1 at right2
    voice audio.aiden_v_tease2b
    a "I gotta say, it’s making me feel a little tingle, if you know what I mean~"

    hide yoshi_towel
    hide yoshi relief5
    show yoshi2_towel at left2
    show yoshi2 shy5 at left2
    voice audio.yoshi_v_gulp1a
    yo "*gulp* A-Aiden… There’s a lot of other people here…"

    show aiden talk4 at right2
    voice audio.aiden_v_oh1a
    a "Oh! Look over there, Yoshi! Isn’t that—"

    show yoshi2_towel at p5_1
    show yoshi2 shy5 at p5_1
    show aiden_towel at p5_2
    show aiden talk4 at p5_2
    with move

    show goro_towel at p5_5
    show goro relief1 at p5_5
    with dissolve

    show aiden happy1 at p5_2
    voice audio.aiden_v_goro1b
    a "Hey, Gramps! "

    show yoshi2_towel at left
    show yoshi2 shy5 at left
    show aiden_towel at center
    show aiden happy1 at center
    show goro_towel at right
    show goro happy1 at right
    with move

    voice audio.goro_v_ah2c
    g "Ah, I didn’t notice you two were here as well…"
    g "This place is so relaxing, I haven’t been paying much attention to anything else."

    hide yoshi2_towel
    hide yoshi2 shy5
    show yoshi_towel at left
    show yoshi laugh2 at left
    voice audio.yoshi_v_laugh1
    yo "Haha, I’m not too surprised that this is your kind of place, sir."

    show goro relief2 at right
    voice audio.goro_v_relief1a
    g "I’ll admit, I’ve always been fond of bath houses… There’s something very soothing about them."
    g "This place here is on another level, though. Did you know they’ll serve you drinks while you’re in the water?  "

    show yoshi shock2 at left
    voice audio.yoshi_v_shock1a
    yo "Whoa, you can do that?"

    show goro happy2 at right
    voice audio.goro_v_agree1a1
    g "Yes. Mostly herbal teas and other relaxing beverages, though."
    g "They even offer massages. In fact, I’ve already booked one for after my soak."

    show aiden happy3 at center
    voice audio.aiden_v_amazed2a2
    a "Wow Gramps, it sounds like you plan on spending the day here – making the most of it, right?"

    show goro relief4 at right
    voice audio.goro_v_actually1a
    g "Yes, although going to bathhouses isn’t new to me. Back in the day, I would go to one whenever I needed to release the stress of running the camp.   "
    g "It was nowhere near as grand as this one, that’s for sure"

    show aiden tease1 at center
    voice audio.aiden_v_laugh1b2
    a "Hehe, are you sure you didn’t come here for a special kind of ‘release’?"

    hide goro_towel
    hide goro relief4
    show goro2_towel at right
    show goro2 confused2 at right
    voice audio.goro_v_think1d1
    g "Hm? What are you trying to say?"

    show aiden play3 at center
    voice audio.aiden_v_comeon2b
    a "Oh, come on! People go to places like this looking for a ‘spicy’ kind of fun~"
    a "Everywhere you look, we’re surrounded by naked guys! A bathhouse is basically a sex hotspot! "

    show yoshi awkward4 at left
    voice audio.yoshi_v_aiden6
    yo "A-Aiden!!"

    show aiden play6 at center
    voice audio.aiden_v_what2b
    a "What? I’m just telling it like I see it!"
    a "Looking at the crowd, I can easily tell who’s only here for a good time."

    show aiden tease1 at center
    voice audio.aiden_v_oho1a
    a "Just look at that guy over there – he’s definitely showing off, with his towel over his shoulder and his dong dangling free!"

    show goro2 disappoint3 at right
    voice audio.goro_v_ehem1a
    g "*ehem* I did not come here to hook up with random strangers."

    show aiden tease2 at center
    voice audio.aiden_v_goro10a
    a "Some of them are pretty hunky. You sure you didn’t see anyone you fancy, Gramps? "

    show goro2 disappoint2 at right
    voice audio.goro_v_annoyed1a1
    g "Like I said, I only came here to relax."

    show aiden bold2 at center
    voice audio.aiden_v_laugh1b2
    a "Having sex is also a way to ‘relax’~ So don’t be shy to admit it, Gramps!"

    hide goro2_towel
    hide goro2 disappoint2
    show goro_towel at right
    show goro explain2 at right
    voice audio.goro_v_sigh1a
    g "There’s a proper time and place for that, Aiden. "

    show aiden tease2 at center
    voice audio.aiden_v_confused1c1
    a "Eh, I guess you really are too old for this kind of stuff. Just when I thought you were finally one of the cool kids for once…  "

    show goro irked3 at right
    g "...!"

    show yoshi annoy3 at left
    voice audio.yoshi_v_aiden4
    yo "A-Aiden, stop teasing Sir Goro…"

    show goro rage1 at right
    voice audio.goro_v_angry1a1
    g "I-I’ll have you know, two not-so-gentle men approached me earlier and asked me to join them in the sauna for a chat…!"

    show aiden drunk2 at center
    voice audio.aiden_v_really2b
    a "Oh really? What happened then?"

    hide goro_towel
    hide goro rage1
    show goro2_towel at right
    show goro2 disappoint3 at right
    voice audio.goro_v_hmph2a
    g "As soon as I stood up, they looked directly at my crotch and started asking for something else."
    g "I will never agree to being the subject of a ‘fellatio conga line’, especially with a bunch of strangers! "

    show yoshi confused2 at left
    voice audio.yoshi_v_what1
    yo "A what now?"

    show aiden explain3 at center
    voice audio.aiden_v_oh3a
    a "He must be talking ’bout a blowjob train! You know, it’s when a bunch of guys take turns to suck—"

    show yoshi shock3 at left
    voice audio.yoshi_v_shock3
    yo "GAH! I get it, I get it, you don’t have to say it out loud, Aiden!"

    show aiden laugh3 at center
    voice audio.aiden_v_laugh2a1
    a "Hahaha! Honestly, I can’t blame those guys after seeing Gramps’ monster cock."

    show goro2 disappoint5 at right
    voice audio.goro_v_sigh2a
    g "*sigh* You’re insufferable…"

    show yoshi_towel at p4_1
    show yoshi shock3 at p4_1
    show aiden_towel at p4_2
    show aiden laugh3 at p4_2
    show goro2_towel at p4_3
    show goro2 disappoint5 at p4_3
    with move

    show reimond_masseur at p4_4
    show reimond talk2 at p4_4
    with dissolve

    voice audio.reimond_v_goro2b
    m "Mr. Nomoru? The massage room is ready! "

    hide goro2_towel
    hide goro2 disappoint5
    show goro_towel at p4_3
    show goro talk1 at p4_3
    voice audio.goro_v_ah2b
    g "Ah, just in time. Do you two want to come with me?"

    show aiden explain4 at p4_2
    voice audio.aiden_v_no1a1
    a "Nope, I’m good! Not a real fan of massages. It gets too ticklish for me."

    show goro tease5 at p4_3
    voice audio.goro_v_really2a
    g "That’s surprising. For someone as virile you, I was sure you’d be into it. What do you and Yoshinori prefer then?"

    $working = False
    $shuffle_menu()
    menu():
        g "That’s surprising. For someone as virile you, I was sure you’d be into it. What do you and Yoshinori prefer then?{fast}"
        "Something quick.":
            $working = True
            $score_aiden += 1
            $score_bot += 1
            show yoshi think2 at p4_1
            voice audio.yoshi_v_well1
            yo "We’d rather do something that doesn’t take too long."

            show aiden happy1 at p4_2
            voice audio.aiden_v_yeah2a1
            a "You mean a quickie, right? I’m down – let’s go right here and now!"

            show yoshi irked2 at p4_1
            voice audio.yoshi_v_sigh3a
            yo "I-I knew you were gonna say something like that…!"
        "Something filling.":
            $working = True
            $score_aiden += 1
            $score_bot += 1
            show yoshi think2 at p4_1
            voice audio.yoshi_v_well1
            yo "I’d rather have something that fills me up."

            show aiden tease1 at p4_2
            voice audio.aiden_v_oho1a
            a "Oh, I’ll fill you up alright~! You wanna do it right here and now?"

            show yoshi irked2 at p4_1
            voice audio.yoshi_v_aiden6
            yo "A-Aiden…!! I meant eating…!!"
        "Something that makes us sweat.":
            $working = True
            $score_aiden += 1
            $score_top += 1
            show yoshi happy1 at p4_1
            voice audio.yoshi_v_well1
            yo "We’d rather do something that makes us sweat!"

            show aiden happy1 at p4_2
            voice audio.aiden_v_agree1a1
            a "Yep! Like raw, hardcore sex!"

            show yoshi irked2 at p4_1
            voice audio.yoshi_v_sigh3a
            yo "I-I knew you were gonna say something like that…!"
        "Something rougher.":
            $working = True
            $score_aiden += 1
            $score_top += 1
            show yoshi happy1 at p4_1
            voice audio.yoshi_v_well1
            yo "We’d rather do something rougher together."

            show aiden happy1 at p4_2
            voice audio.aiden_v_agree1a1
            a "Yep! Like raw, hardcore sex!"

            show yoshi irked2 at p4_1
            voice audio.yoshi_v_sigh3a
            yo "I-I knew you were gonna say something like that…!"

    hide goro_towel
    hide goro tease5
    show goro2_towel at p4_3
    show goro2 disappoint3 at p4_3
    voice audio.goro_v_ehem1a
    g "*ehem* Well, if that’s the case, I’ll be on my way. You two have a good time."

    hide goro2_towel
    hide goro2 tease5
    hide reimond_masseur
    hide reimond talk2
    with dissolve

    show yoshi_towel at left2
    show yoshi irked2 at left2
    show aiden_towel at right2
    show aiden tease2 at right2
    with move

    voice audio.aiden_v_laugh1b2
    a "Guess I was wrong about Gramps. He’s not as stuck-up as I thought, ’cuz that massage definitely has a happy ending."

    show yoshi shock3 at left2
    voice audio.yoshi_v_what4
    yo "Wh-What?! H-How could you tell"

    show aiden play3 at right2
    voice audio.aiden_v_tease2b
    a "Didn’t you see the look on that masseur’s face when he called him? The guy was totally checking him out!"
    a "And after he saw what Gramps was packing, that perv’s eyes were definitely sparkling. "

    hide yoshi_towel
    hide yoshi shock3
    show yoshi2_towel at left2
    show yoshi2 sigh4 at left2
    voice audio.yoshi_v_sigh3a
    yo "*sigh* Aiden, I don’t know how you think of all this…"

    show aiden laugh1 at right2
    voice audio.aiden_v_laugh2a1
    a "Hahaha! "

    if daya3_choice == False:
        $ daya3_choice = True
        $ renpy.music.stop(channel='music', fadeout = 1.0)
        $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
        $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
        scene cg black with fade

        yo "{i}After Sir Goro left, Aiden and I continued to chat and soak in the bath.{/i}"
        yo "{i}We were both so relaxed that we didn’t even notice how long we’d spent there, and by the time we got out, it was already sunset…{/i}"
        yo "{i}Our bodies were really pruney, and Aiden couldn’t resist poking me all over and teasing about it!{/i}"

        $ renpy.pause (1.0, hard=True)
        yo "{i}Eventually, we decided to go and explore another area of the hotel! {/i}"

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

        yo "{i}After Sir Goro left, Aiden and I continued to chat and soak in the bath.{/i}"
        yo "{i}We were both so relaxed that we didn’t even notice how long we’d spent there, and by the time we got out, it was already dark out…{/i}"
        yo "{i}Our bodies were really pruney, and Aiden couldn’t resist poking me all over and teasing about it!{/i}"

        $ renpy.pause (1.0, hard=True)
        yo "{i}It was already late, but we spotted one more place for us to go… {/i}"

        scene cg black
        hide screen location
        hide screen timeline
        hide screen quick_menu
        $quick_menu = False
        with fade
        $ time_transition_sunset_to_night_winter()
        $ renpy.pause (2.0, hard=True)
        jump day3_aiden_after

label day3_aiden_cafe:
    $sq_yuri += 1
    $quick_menu = True
    $say_box = True
    $mm_talking = True
    $a3_cafe = True

    voice audio.yoshi_v_think4
    yo "The café seems like it might be a nice place to hang out at!"

    if daya3_choice == False:
        voice audio.aiden_v_praise3b
        a "Ooh! Good idea! Those snacks were good on the ride, but I’m craving some real food! "
    else:
        voice audio.aiden_v_agree3a2
        a "Sure thing! I’m curious what the food there is like, anyway!"

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

    if daya3_choice == False:
        $ location = location_hotelcafe
        show screen location
        show screen timeline
        show screen quick_menu
        $quick_menu = True
        scene bg_hotel_cafe_day with fade
        play music close_distance loop
    else:
        $ location = location_hotelcafe
        show screen location
        show screen timeline
        show screen quick_menu
        $quick_menu = True
        scene bg_hotel_cafe_sunset with fade
        play music close_distance loop

    show yoshi_autumn at left2
    show yoshi shock1 at left2
    show aiden_autumn at right2
    show aiden awkward2 at right2
    voice audio.aiden_v_swear2a1
    a "Damn… Does every single place in this building have to be so extra? "
    a "I mean just look at that view… You can see the entire city from here…"

    show yoshi shock2 at left2
    voice audio.yoshi_v_unsure3b
    yo "I guess it lives up to its name as the best hotel around…"

    show aiden talk2 at right2
    voice audio.aiden_v_yuri5a
    a "Oh, and isn’t that Yuri over there?"

    show yoshi_autumn at p5_1
    show yoshi talk1 at p5_1
    show aiden_autumn at p5_2
    show aiden talk2 at p5_2
    with move

    show yuri_autumn at p5_5
    show yuri norm1 at p5_5
    with dissolve

    voice audio.yoshi_v_rush1
    yo "Let’s see what she’s up to."

    show yoshi_autumn at left
    show yoshi happy1 at left
    show aiden_autumn at center
    show aiden talk2 at center
    show yuri_autumn at right
    show yuri norm1 at right
    with move

    voice audio.yoshi_v_greet1a1
    yo "Hi, Yuri!"

    show yuri happy1 at right
    voice audio.yuri_v_greet2a
    yu "Oh, hello there, Yoshi, Aiden!"
    yu "I’m pretty surprised to see you both here! A café doesn’t seem like your style. "

    show aiden pout1 at center
    voice audio.aiden_v_hey1e2
    a "Heeeey, what’s that supposed to mean?"

    show yoshi laugh1 at left
    voice audio.yoshi_v_laugh1
    yo "Haha, we were just looking around for a place to hang out! Staying in our room can get boring, after all."

    show yuri laugh1 at right
    voice audio.yuri_v_actually1a
    yu "The moment I saw this on the brochure, I had to go check it out!"
    yu "But yeah! You guys came to the right place~ Isn’t the view here amazing?"

    show yuri bold2 at right
    voice audio.yuri_v_fujo1a2
    yu "It’s perfect with the delicious dessert, fruity drinks, and all the hardcore smut I can read! "

    show yoshi shy6 at left
    voice audio.yoshi_v_yuri6
    yo "Those are some seriously contradicting things, Yuri. "

    show yuri relief2 at right
    voice audio.yuri_v_laugh1a1
    yu "I’m living the dream! "

    show yuri play2 at right
    voice audio.yuri_v_here1a
    yu "Here, why don’t you check out some of these fanfics I’m reading~! Maybe you can pick up a tip or two~"

    hide yoshi_autumn
    hide yoshi shy6
    show yoshi2_autumn at left
    show yoshi2 confused5 at left
    voice audio.yoshi_v_uh1a
    yo "This one is on… B.D.S.M… What does that even mean?"

    show yuri serious3 at right
    voice audio.yuri_v_yoshi9a
    yu "My goodness, Yoshi! Shouldn’t you know that at your age?! Just what kind of remote area do you live in?!"

    show aiden tease1 at center
    voice audio.aiden_v_laugh1b2
    a "Hehe, Camp Buddy apparently~"

    hide yoshi2_autumn
    hide yoshi2 confused5
    show yoshi_autumn at left
    show yoshi awkward3 at left
    voice audio.yoshi_v_hey4
    yo "H-Hey! Stuff like this isn’t common knowledge…!"

    show yuri serious4 at right
    voice audio.yuri_v_ugh2a
    yu "It sure is, you hillbilly! The letters stand for Bondage and Discipline, Sadism and Masochism, and Submission and Dominance! "

    hide yoshi_autumn
    hide yoshi awkward3
    show yoshi2_autumn at left
    show yoshi2 confused6 at left
    voice audio.yoshi_v_think1a
    yo "That sounds like… a lot."

    show yuri excited2 at right
    voice audio.yuri_v_laugh1b1
    yu "Did any of those spark an interest for you? "

    show yoshi2 sigh4 at left
    voice audio.yoshi_v_sigh3a
    yo "*sigh* Do I really have to choose, Yuri?"

    show aiden confused3 at center
    voice audio.aiden_v_actually1a
    a "I kinda wanna know too. What are you into, Yoshi?"

    $working = False
    $shuffle_menu()
    menu():
        a "I kinda wanna know too. What are you into, Yoshi?{fast}"
        "Bondage and Discipline.":
            $working = True
            $score_aiden -= 1
            $score_bot += 1
            show yoshi2 confused5 at left
            voice audio.yoshi_v_unsure3c
            yo "From the options, I guess… Bondage and discipline? Although I’m not sure how scolding someone can be interesting…"

            hide aiden_autumn
            hide aiden confused3
            show aiden2_autumn at center
            show aiden2 awkward5 at center
            voice audio.aiden_v_no1a1
            a "Yeah, I’m with Yoshi on this one, not into those."

            show yuri tease4 at right
            voice audio.yuri_v_aww4a
            yu "Aww, come on guys! Don’t you think Aiden would look good tied up~?"
        "Sadism and Masochism.":
            $working = True
            $score_aiden -= 1
            $score_top += 1
            show yoshi2 confused5 at left
            voice audio.yoshi_v_unsure3c
            yo "From the options, I guess… Sadism and masochism? But that just sounds dark…"

            hide aiden_autumn
            hide aiden confused3
            show aiden2_autumn at center
            show aiden2 awkward5 at center
            voice audio.aiden_v_no1a1
            a "Yeah, I’m with Yoshi on this one, not into those."

            show yuri tease4 at right
            voice audio.yuri_v_aww4a
            yu "Aww, come on guys! A little bit of pain can lead to a lot of pleasure, you know~"
        "Submission.":
            $working = True
            $score_aiden += 1
            $score_bot += 1
            show yoshi2 confused5 at left
            voice audio.yoshi_v_unsure3c
            yo "From the options, I guess… Submission? I can at least see the appeal here…"

            show aiden tease1 at center
            voice audio.aiden_v_oho1a
            a "Oho~ Wanting someone else to take charge? "
            a "Don’t worry, Yoshi, I can take a hint!"

            hide yuri_autumn
            hide yuri excited2
            show yuri2_autumn at right
            show yuri2 ahegao1 at right
            voice audio.yuri_v_kyaa1a
            yu "KYAAA! Yes, take him right now, Aiden! Assert yourself!"
        "Dominance.":
            $working = True
            $score_aiden += 1
            $score_top += 1
            show yoshi2 confused5 at left
            voice audio.yoshi_v_unsure3c
            yo "From the options, I guess… Dominance? I can at least see the appeal here…"

            show aiden tease1 at center
            voice audio.aiden_v_oho1a
            a "Oho~ Wanting to take control, Yoshi?"
            a "Just say the word and I’m all yours!"

            hide yuri_autumn
            hide yuri excited2
            show yuri2_autumn at right
            show yuri2 ahegao1 at right
            voice audio.yuri_v_kyaa1a
            yu "KYAAA! Yes, take him right now, Yoshi! Assert yourself!"

    show yoshi2 sigh1 at left
    show yoshi2_blush2 at left
    voice audio.yoshi_v_sigh3a
    yo "*sigh* Don’t get carried away, you two. "
    yo "And do you guys really think it’s okay to talk about this kind of stuff out in public…?"

    hide yuri_autumn
    hide yuri excited2
    show yuri2_autumn at right
    show yuri2 ahegao3 at right
    voice audio.yuri_v_comp1a3
    yu "Nobody’s paying attention to us anyway! And if they were, they’d be into it too!"

    hide aiden2_autumn
    hide aiden2 awkward5
    show aiden_autumn at center
    show aiden laugh3 at center
    voice audio.aiden_v_laugh2a1
    a "Hahaha! Yoshi’s turned all red again!"

    hide yoshi2_autumn
    hide yoshi2 sigh1
    hide yoshi2_blush2
    show yoshi_autumn at left
    show yoshi irked3 at left
    voice audio.yoshi_v_ehem1b
    yo "*ahem* A-Anyway, what else have you been up to, Yuri? It’s been a while since you’ve had time for yourself like this."

    hide yuri2_autumn
    hide yuri2 ahegao3
    show yuri_autumn at right
    show yuri laugh1 at right
    voice audio.yuri_v_yeah1b1
    yu "Yeah, and I’ve just been hanging out here at the café! I think this will be my chill spot for the trip~"
    yu "It’s quiet and peaceful, and there’s no big distractions like work!"

    show yuri irked1 at right
    voice audio.yuri_v_sigh2a
    yu "The only thing that’s still irritating me is Emilia being on the trip with us. But I guess you can’t have everything, huh?"

    show aiden worry2 at center
    voice audio.aiden_v_sigh1a
    a "She really does push your buttons, doesn’t she? "

    show yuri irked2 at right
    voice audio.yuri_v_unsure1b2
    yu "I just don’t understand how she can get away with so much… I mean, I know she’s a QA manager but she always demands the most unnecessary stuff!"

    show aiden upset6 at center
    voice audio.aiden_v_well1c1
    a "You were getting super cranky with her this morning when we were checking in."

    show yuri angry2 at right
    voice audio.yuri_v_rush1d1
    yu "Who wouldn’t be annoyed at that?! If I had to listen to her Karen-ing for another minute—"

    show yoshi explain2 at left
    voice audio.yoshi_v_comp9
    yo "Now, now, Yuri. We’re here to relax, so don’t get worked up again."

    show yuri pout1 at right
    voice audio.yuri_v_hmph1a
    yu "Hmph! It’s because you changed the topic!"

    show aiden talk1 at center
    voice audio.aiden_v_but1a1
    a "But seriously, it could’ve been worse. Compared to how she was the last few months, this is pretty tame."

    show yuri sigh2 at right
    voice audio.yuri_v_unsure3a
    yu "I guess that’s true… I was almost sure she’d flip out when nobody wanted to share a room with her. "

    show aiden think2 at center
    voice audio.aiden_v_unsure5a2
    a "Maybe that meeting yesterday was a reality check for her."

    show yuri confused4 at right
    voice audio.yuri_v_conj6a
    yu "Although, something’s been bugging me…"

    show aiden confused2 at center
    voice audio.aiden_v_confused1a2
    a "Eh? What is it?"

    show yuri think2 at right
    voice audio.yuri_v_well1a
    yu "Well, isn’t she, like, super rich? Like born-and-raised-rich? That was her whole shtick back then!"
    yu "Why would she keep working at a job where no one likes her?"

    show yuri explain2 at right
    yu "And from the way she’s been acting, she hates the job too."

    hide aiden_autumn
    hide aiden confused2
    show aiden2_autumn at center
    show aiden2 think4 at center
    voice audio.aiden_v_think1a1
    a "Now that you mention it, yeah… "

    show aiden2 tease2 at center
    a "Hehe… Maybe she’s just trying to score with Yoshi."

    hide yoshi_autumn
    hide yoshi explain2
    show yoshi2_autumn at left
    show yoshi2 sigh4 at left
    voice audio.yoshi_v_sigh3a
    yo "*sigh* That’s not funny… "

    show yuri angry2 at right
    voice audio.yuri_v_sus2a
    yu "But I’m calling it right now, there’s something really off about that girl… And I’m not just talking about her attitude!"

    hide yoshi2_autumn
    hide yoshi2 sigh4
    show yoshi_autumn at left
    show yoshi worry2 at left
    voice audio.yoshi_v_uh1a
    yo "I… don’t think we should be gossiping about her like this… It might just make things worse."
    yo "Let’s just give her the b—"

    show yuri pout4 at right
    voice audio.yuri_v_yeah1h1
    yu "“Benefit of the doubt”. Yeah, you’ve said that like a hundred times already, Yoshi."
    yu "Either way, I’m keeping a close eye on her! "

    show aiden2 worry2 at center
    voice audio.aiden_v_think2a
    a "Won’t that mess up your vacation?"
    a "It’s not like Emilia’s gonna be at Camp Buddy forever, you know! Just endure her ’til we finish the project!"

    show yoshi happy1 at left
    voice audio.yoshi_v_right5
    yo "See? That’s the healthy way of thinking about it!"
    yo "A-Anyway, I’m sorry for changing subjects, why don’t we go back to what we were talking about before?"

    hide yuri_autumn
    hide yuri pout4
    show yuri2_autumn at right
    show yuri2 fangirl2 at right
    voice audio.yuri_v_omg1a
    yu "OMG! Alright, I have tons more fanfics of all different genres! Let’s find the one that suits you the best!!"

    hide yoshi_autumn
    hide yoshi happy1
    show yoshi2_autumn at left
    show yoshi2 sigh4 at left
    voice audio.yoshi_v_sigh3a
    yo "*sigh* I meant about the café, but sure, why not…"

    if daya3_choice == False:
        $ daya3_choice = True
        $ renpy.music.stop(channel='music', fadeout = 1.0)
        $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
        $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
        scene cg black with fade

        yo "{i}Thankfully, Yuri was eager to talk about her fanfics, so she was distracted from her concerns with Emilia…{/i}"
        yo "{i}We ended up sitting and chatting with her for a long time, eating snacks and laughing at all the stories she told.{/i}"
        yo "{i}Before we realized, it was already sunset, and we decided to check out another area of the hotel! {/i}"

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

        yo "{i}Thankfully, Yuri was eager to talk about her fanfics, so she was distracted from her concerns with Emilia…{/i}"
        yo "{i}We ended up sitting and chatting with her for a long time, eating snacks and laughing at all the stories she told.{/i}"
        yo "{i}Before we realized, it was already dark out, but we spotted one more place for us to go… {/i}"

        scene cg black
        hide screen location
        hide screen timeline
        hide screen quick_menu
        $quick_menu = False
        with fade
        $ time_transition_sunset_to_night_winter()
        $ renpy.pause (2.0, hard=True)
        jump day3_aiden_after

label day3_aiden_gym:
    $quick_menu = True
    $say_box = True
    $mm_talking = True
    $a3_gym = True
    voice audio.yoshi_v_think4
    yo "Why don’t we check out the gym, Aiden? "

    if daya3_choice == False:
        voice audio.aiden_v_praise3b
        a "Ooh! Good idea! My muscles need some stretching after sitting on that bus for hours! "
    else:
        voice audio.aiden_v_agree3a2
        a "Sure thing! My muscles could use a stretch!"

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

    if daya3_choice == False:
        $ location = location_hotelgym
        show screen location
        show screen timeline
        show screen quick_menu
        $quick_menu = True
        scene bg_hotel_gym_day with fade
        play music buddy_oath_hotel loop
    else:
        $ location = location_hotelgym
        show screen location
        show screen timeline
        show screen quick_menu
        $quick_menu = True
        scene bg_hotel_gym_sunset with fade
        play music close_distance loop

    show yoshi_autumn at left2
    show yoshi shock2 at left2
    show aiden_autumn at right2
    show aiden norm1 at right2
    voice audio.yoshi_v_amazed1a
    yo "Wow… Check out all the fancy equipment they have here!  "
    yo "It must be easy to bulk up when you’ve got a place like this!"

    show aiden laugh1 at right2
    voice audio.aiden_v_laugh2a1
    a "Haha, I’d run out of money way before I had any gains to show from a membership at this gym."
    a "Besides, do you really need all these contraptions? I think I’ve done pretty good with just a couple weights and some body workouts!"

    show yoshi happy1 at left2
    voice audio.yoshi_v_well1
    yo "Well, we’re already here! It won’t hurt to try at least one of them, right?"

    show aiden comp3 at right2
    voice audio.aiden_v_agree2e1
    a "Hehe, I guess, you’re right! What do you wanna work on?"

    $working = False
    $shuffle_menu()
    menu():
        a "Hehe, I guess, you’re right! What do you wanna work on?{fast}"
        "Biceps.":
            $working = True
            $score_top += 1
            show yoshi bold2 at left2
            voice audio.yoshi_v_think4
            yo "Why don’t we try this curl machine? It looks like it focuses on your biceps!"

            show aiden confused3 at right2
            voice audio.aiden_v_oh1a
            a "Oh, arms, huh? I’m kinda surprised you wanna work on those, Yoshi!"
            a "You tryin’ to get crazy ripped guns like Gramps?"

            show yoshi comp3 at left2
            voice audio.yoshi_v_well3
            yo "W-Well, I thought it would be easier to carry stuff around if I was stronger."

            show aiden tease1 at right2
            voice audio.aiden_v_perv1
            a "Fair enough. You could lift me around better that way~"

            show yoshi happy2 at left2
            voice audio.yoshi_v_anyway3a
            yo "A-Anyway, I actually used to work out on something like this back in college!"

            show aiden bold2 at right2
            voice audio.aiden_v_agree3a1
            a "Haha, alright, sure! Show me the how it’s done!"
        "Pecs.":
            $working = True
            $score_bot += 1
            show yoshi bold2 at left2
            voice audio.yoshi_v_think4
            yo "Why don’t we try this press machine? It focuses on your pecs!"

            show aiden tease1 at right2
            voice audio.aiden_v_oh1a
            a "Pecs, huh? Don’t you think you’ve already got  ‘bara tiddies’?"

            hide yoshi_autumn
            hide yoshi bold2
            show yoshi2_autumn at left2
            show yoshi2 sigh4 at left2
            voice audio.yoshi_v_sigh3a
            yo "*sigh* You heard that from Yuri, didn’t you?"

            show aiden laugh1 at right2
            voice audio.aiden_v_agree1a2
            a "Yup! Hahaha!"

            hide yoshi2_autumn
            hide yoshi2 sigh4
            show yoshi_autumn at left2
            show yoshi happy2 at left2
            voice audio.yoshi_v_anyway3a
            yo "A-Anyway, I actually used to work out on something like this back in college!"

            show aiden bold2 at right2
            voice audio.aiden_v_agree3a1
            a "Haha, alright, sure! Show me the how it’s done!"
        "Abs.":
            $working = True
            $score_top += 2
            show yoshi bold2 at left2
            voice audio.yoshi_v_think4
            yo "Why don’t we try that crunch machine? It focuses on your abs!"

            show aiden tease1 at right2
            voice audio.aiden_v_oho1a
            a "Oooh, really going for that washboard look, huh, Yoshi?"
            a "I don’t blame you, though! I know you like to ogle mine, so I make sure they’re strong and solid for you~"

            show yoshi comp3 at left2
            voice audio.yoshi_v_ah3
            yo "A-Ah, well… I didn’t realize you noticed how often I look at them."

            show aiden laugh1 at right2
            voice audio.aiden_v_laugh2a1
            a "Hahaha! I pay attention~"

            show yoshi play2 at left2
            voice audio.yoshi_v_well2
            yo "Well, you’re always distracting me with yours, so I figured I should return the favor."

            show yoshi happy2 at left2
            voice audio.yoshi_v_anyway3a
            yo "Anyway, I actually used to work out on something like this back in college!"

            show aiden bold2 at right2
            voice audio.aiden_v_oh1a
            a "Oh, so that’s how you got jacked! Count me in, then! "
        "Glutes":
            $working = True
            $score_bot += 2
            show yoshi bold2 at left2
            voice audio.yoshi_v_think4
            yo "Why don’t we try this squat machine? It focuses on your glutes!"

            show aiden tease1 at right2
            voice audio.aiden_v_oho1a
            a "You tryin’ to clap those cheeks, Yoshi? All you had to do was ask~"

            hide yoshi_autumn
            hide yoshi bold2
            show yoshi2_autumn at left2
            show yoshi2 sigh4 at left2
            voice audio.yoshi_v_sigh3a
            yo "*sigh* Aiden…"

            show aiden tease2 at right2
            voice audio.aiden_v_what2b
            a "Whaaat? Not my fault you’re so easy and fun to tease~"
            a "But hey, I wouldn’t say no to seeing you with a juicier butt~"

            hide yoshi2_autumn
            hide yoshi2 sigh4
            show yoshi_autumn at left2
            show yoshi play2 at left2
            voice audio.yoshi_v_laugh6
            yo "Maybe then the scouts would call me Buttcheeks too, huh?"

            show aiden laugh1 at right2
            voice audio.aiden_v_laugh2a1
            a "Hahaha!"

            show yoshi happy2 at left2
            voice audio.yoshi_v_anyway3a
            yo "A-Anyway, I actually just noticed this one because I used to work out on something like it in college!"

            show aiden bold2 at right2
            voice audio.aiden_v_oh1a
            a "Oh, so that’s how you got jacked! Count me in, then! "

    show aiden_autumn at p5_4
    show aiden talk4 at p5_4
    show yoshi_autumn at p5_5
    show yoshi happy2 at p5_5
    with move

    show darius_yoga at p5_1
    show darius norm3 at p5_1
    with dissolve

    voice audio.aiden_v_wait2b1
    a "Oh! Hold that thought Yoshi, it’s Darius!"

    show darius_yoga at left
    show darius norm3 at left
    show aiden_autumn at center
    show aiden happy1 at center
    show yoshi_autumn at right
    show yoshi happy2 at right
    with move

    voice audio.aiden_v_darius1b
    a "Heyyy, Darius, my man! How’s it going?"

    show darius happy1 at left
    voice audio.darius_v_greet1a1
    d "Hi."

    show aiden happy3 at center
    voice audio.aiden_v_flex1d
    a "Building up those muscles I see!"

    show darius talk1 at left
    voice audio.darius_v_agree1a
    d "Yes. I didn’t want to skip a day of my routine. "

    show yoshi confused2 at right
    voice audio.yoshi_v_huh1
    yo "Where’s Lloyd? I thought you were with him."

    show darius think5 at left
    voice audio.darius_v_conj1a2
    d "He’s busy taking pictures of the building."

    show yoshi talk3 at right
    voice audio.yoshi_v_isee1
    yo "Oh, I see…!"

    show darius confused2 at left
    voice audio.darius_v_confused2a
    d "Why do you ask? "

    show yoshi comp2 at right
    voice audio.yoshi_v_well1
    yo "Ah well, I’m just not used to seeing you without Lloyd. "

    show aiden talk2 at center
    voice audio.aiden_v_actually1a
    a "You two are usually stuck together like glue – it’s weird seeing you apart!"

    show darius think3 at left
    voice audio.darius_v_conj2a
    d "We both have different hobbies, and I like for him to spend time doing what he enjoys."

    show yoshi comp3 at right
    voice audio.yoshi_v_laugh1
    yo "He’s quite the energetic person, huh…?  "

    show darius comp2 at left
    voice audio.darius_v_agree1a
    d "Yes, he is. He’s always eager and ready to try something new. It’s something I admire about him."

    show yoshi talk2 at right
    voice audio.yoshi_v_darius5a
    yo "How about you, Darius? Don’t you have a hobby?"

    show darius bored1 at left
    voice audio.darius_v_think2a1
    d "Building."

    show aiden comp3 at center
    voice audio.aiden_v_bro1a
    a "That’s your main thing, bro! A job doesn’t count! "
    a "It has to be something that you do just for fun~ "

    show darius sad1 at left
    voice audio.darius_v_sorry1a
    d "I know it’s boring. I don’t have any ‘fun’ hobbies."

    show yoshi confused3 at right
    voice audio.yoshi_v_really1
    yo "Really? There must be something you do outside of work that always makes you happy!"

    show darius think2 at left
    voice audio.darius_v_lloyd5b
    d "Lloyd, maybe?"

    hide yoshi_autumn
    hide yoshi confused3
    show yoshi2_autumn at right
    show yoshi2 confused5 at right
    voice audio.yoshi_v_uh1a
    yo "Y-You’re happy when you’re doing… Lloyd?"

    show darius bored4 at left
    voice audio.darius_v_no1a
    d "I mean, I’m happy when Lloyd is around. "

    hide yoshi2_autumn
    hide yoshi2 confused5
    show yoshi_autumn at right
    show yoshi awkward4 at right
    voice audio.yoshi_v_oh1
    yo "Oh."

    show darius sigh1 at left
    voice audio.darius_v_conj2a
    d "Everything is less interesting without him, so I prefer it when he’s with me."

    show yoshi think2 at right
    voice audio.yoshi_v_isee2
    yo "I see…"

    show darius awkward1 at left
    d "..."

    show yoshi explain2 at right
    voice audio.yoshi_v_ehem1b
    yo "*ehem* You know, I’ve been wondering about this for a while, but… "
    yo "Is there a reason, why you’re always so quiet?"

    show darius awkward2 at left
    d "..."

    show darius confused5 at left
    voice audio.darius_v_denial1a1
    d "Not really. It’s just the way I am."

    hide aiden_autumn
    hide aiden comp3
    show aiden2_autumn at center
    show aiden2 annoy6 at center
    voice audio.aiden_v_yoshi8b
    a "Yoshi, you don’t just ask people why they’re quiet, it’s like asking someone why they never shut up."

    show yoshi panic4 at right
    voice audio.yoshi_v_shock3
    yo "A-Ack, I apologize! I wasn’t trying to be rude!"

    show darius comp2 at left
    voice audio.darius_v_comp3a
    d "Don’t worry. I didn’t take any offense from it. "
    d "It’s nothing new anyway. People call me ‘Serious Darius’ for a reason."

    show darius sigh2 at left
    voice audio.darius_v_i1a
    d "They’re either scared of me or think I’m boring. "

    hide aiden2_autumn
    hide aiden2 annoy6
    show aiden_autumn at center
    show aiden shock2 at center
    voice audio.aiden_v_what2a
    a "Wha— but that’s not true at all, Darius! I’ve always thought you were interesting!"
    a "Besides, you’ve got that mysterious vibe going for you that makes people want to get to know you more~!"

    show darius sad2 at left
    voice audio.darius_v_thanks1a1
    d "Thanks for the compliment, but…"
    d "Nobody really approaches me. "

    hide yoshi_autumn
    hide yoshi panic4
    show yoshi2_autumn at right
    show yoshi2 worry2 at right
    voice audio.yoshi_v_think1a
    yo "D-Doesn’t that upset you…?"

    show darius talk2 at left
    voice audio.darius_v_denial1a1
    d "Not really. I prefer it that way."

    show aiden think1 at center
    voice audio.aiden_v_unsure1b
    a "I guess it does make sense though. You’re so tall and buff, so being quiet on top of that can come off intimidating to others."

    show darius play2 at left
    voice audio.darius_v_praise1
    d "Good to know it works. It helps me protect Lloyd. "

    hide aiden_autumn
    hide aiden think1
    show aiden2_autumn at center
    show aiden2 confused2 at center
    voice audio.aiden_v_confused1a2
    a "Eh? What do you mean?"

    show darius comp2 at left
    voice audio.darius_v_lloyd5a
    d "Lloyd is the complete opposite of me. He has interesting hobbies, he’s not as tall and he likes to talk a lot."
    d "That made him an easy target for bullies in the past. Which made him cry often."

    show darius sad2 at left
    voice audio.darius_v_i1a
    d "And I couldn’t protect him. "

    hide yoshi2_autumn
    hide yoshi2 worry2
    show yoshi_autumn at right
    show yoshi sad4 at right
    voice audio.yoshi_v_huh5
    yo "…I never knew."

    show darius disappoint3 at left
    voice audio.darius_v_conj3a
    d "Even as adults, many people in our industry underestimate him or don’t give him the respect he deserves."
    d "They stop doing those things whenever they see me with Lloyd."

    show darius talk2 at left
    voice audio.darius_v_laugh1
    d "That’s why I try my best to be his bodyguard. And make sure he always has a smile on his face. "

    hide aiden2_autumn
    hide aiden2 confused2
    show aiden_autumn at center
    show aiden comp2 at center
    voice audio.aiden_v_aww3a
    a "Aww… Now if that isn’t the sweetest thing I’ve ever heard, I don’t know what is!"

    show yoshi comp2 at right
    voice audio.yoshi_v_encourage3
    yo "That’s very chivalrous of you, Darius… Lloyd is a lucky person then!"

    show darius comp3 at left
    voice audio.darius_v_conj1a1
    d "I’m the lucky one."

    show yoshi laugh2 at right
    voice audio.yoshi_v_laugh1
    yo "Haha, it’s really nice to talk with you like this, Darius!"
    yo "You probably don’t notice it, but… You tend to speak a lot whenever we talk about Lloyd."

    show darius worry3 at left
    voice audio.darius_v_sorry2b
    d "I’m sorry if it weirded you out."

    show aiden comp5 at center
    voice audio.aiden_v_actually1a
    a "No, no, it’s actually charming, bro~!"

    show yoshi happy1 at right
    voice audio.yoshi_v_yes2
    yo "Yes! I feel like we’re one step closer to trusting each other, too! "

    show darius comp1 at left
    voice audio.darius_v_praise1
    d "I’m glad. I’ll try to be more open with you guys. It’ll take some time getting used to."

    show aiden bold2 at center
    voice audio.aiden_v_flex1a
    a "We’ll be here all day~! Now come on, let’s work up a sweat! "

    if daya3_choice == False:
        $daya3_choice = True
        $ renpy.music.stop(channel='music', fadeout = 1.0)
        $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
        $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
        scene cg black with fade

        yo "{i}We spent the rest of the afternoon working out with Darius and chatting… I really enjoyed seeing him open up like that!{/i}"
        yo "{i}Eventually, Lloyd came looking for us and we realized it was already sunset! {/i}"
        yo "{i}We decided to finish up our workout, take a quick shower, and check out another place in the hotel!{/i}"

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
        $ renpy.music.stop(channel='music', fadeout = 1.0)
        $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
        $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
        scene cg black with fade

        yo "{i}We spent the rest of the afternoon working out with Darius and chatting… I really enjoyed seeing him open up like that!{/i}"
        yo "{i}Eventually, Lloyd came looking for us and we realized it was already dark out! {/i}"
        yo "{i}We decided to finish up our workout, take a quick shower, and check out one more place in the hotel that I spotted… {/i}"

        scene cg black
        hide screen location
        hide screen timeline
        hide screen quick_menu
        $quick_menu = False
        with fade
        $ time_transition_sunset_to_night_winter()
        $ renpy.pause (2.0, hard=True)
        jump day3_aiden_after


label day3_aiden_room:
    $sq_jin += 1
    $quick_menu = True
    $say_box = True
    $mm_talking = True
    $a3_room = True

    voice audio.yoshi_v_think4
    yo "Why don’t we go check on our friends?"

    if daya3_choice == False:
        voice audio.aiden_v_praise3b
        a "Ooh! Good idea! Maybe they’re up to something fun! "
    else:
        voice audio.aiden_v_agree3a2
        a "Sure thing! I could use some chill time after earlier!"

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

    if daya3_choice == False:
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
    j "O-Oh…! I’m coming!"

    play sound sfx_dooropen
    show jin_autumn at left
    show jin_glasses at left
    show jin talk2 at left
    with move

    show aiden_autumn at center
    show aiden norm1 at center
    show yoshi_autumn at right
    show yoshi happy2 at right
    with dissolve

    voice audio.yoshi_v_greet1a1
    yo "Hey there, Jin! "

    show jin happy1 at left
    voice audio.jin_v_greet1b3
    j "A-Ah, hey guys, please come in!"

    if daya3_choice == False:
        show aiden confused2 at center
        voice audio.aiden_v_confused1c2
        a "Eh? Where is everybody?"

        show jin talk1 at left
        voice audio.jin_v_conj1c1
        j "Oh, if you’re looking for Lloyd and Darius, they already went downstairs to do stuff around the hotel."

        show aiden happy1 at center
        voice audio.aiden_v_unsure7b
        a "Don’t you wanna go out too? We could all go together if you want!"

        show jin comp2 at left
        voice audio.jin_v_comp8b1
        j "I-It’s alright! I’m not really the type to go out and party. I’m fine just staying in a cozy room like this!"
        j "B-Besides, my stomach is still recovering from the bus ride this morning."

        hide aiden_autumn
        hide aiden happy1
        show aiden2_autumn at center
        show aiden2 worry2 at center
        voice audio.aiden_v_oh1a
        a "Oh, you still feel a little sick?"
    else:
        show yoshi talk3 at right
        voice audio.yoshi_v_greet2a1
        yo "I hope we didn’t bother you!"

        show jin comp2 at left
        voice audio.jin_v_denial2b1
        j "N-Not at all! I was just resting!"

        hide aiden_autumn
        hide aiden norm1
        show aiden2_autumn at center
        show aiden2 worry2 at center
        voice audio.aiden_v_shock2b1
        a "Yikes, do you still feel sick from the bus ride this morning?"

    show jin comp3 at left
    voice audio.jin_v_yeah5b
    j "Yeah… it kinda takes a while before its gone…"

    show yoshi happy2 at right
    voice audio.yoshi_v_well1
    yo "Well, I hope you don’t mind if we hang out here with you then!"

    show jin talk4 at left
    voice audio.jin_v_no1b
    j "O-Oh no, I wouldn’t want you guys to miss out on all the fun stuff around the hotel! "

    hide aiden2_autumn
    hide aiden2 worry2
    show aiden_autumn at center
    show aiden talk2 at center
    voice audio.aiden_v_no2a1
    a "Nah, it’s fine! We kinda needed to rest a little anyways!"

    show yoshi confused2 at right
    voice audio.yoshi_v_jin5
    yo "What do you usually do for fun though, Jin?"

    show jin daydream2 at left
    voice audio.jin_v_laugh2c
    j "I-It depends… I have several definitions of fun..."

    show aiden tease1 at center
    voice audio.aiden_v_oho1a
    a "Oho~ "

    show yoshi explain2 at right
    voice audio.yoshi_v_well3
    yo "W-Well, I remember that you enjoy the same stuff as Yuri. But is there something else that maybe… you know? We could do together?"

    show jin fudan1 at left
    voice audio.jin_v_gulp1a
    j "*gulp*"

    show aiden laugh1 at center
    voice audio.aiden_v_laugh2a1
    a "Hahaha! Now we’re talking, Yoshi!"

    hide yoshi_autumn
    hide yoshi explain2
    show yoshi2_autumn at right
    show yoshi2 sigh4 at right
    voice audio.yoshi_v_sigh3a
    yo "*sigh* Don’t put words in my mouth, Aiden…"

    show aiden tease2 at center
    voice audio.aiden_v_what1b
    a "What? Do you want us to put something else in there?"

    show jin perv2 at left
    voice audio.jin_v_fudan1a2
    j "Oh my…"

    hide yoshi2_autumn
    hide yoshi2 sigh4
    show yoshi_autumn at right
    show yoshi awkward3 at right
    voice audio.yoshi_v_think4
    yo "H-How about we do something with your computer, Jin?! You use that for fun too, right?"

    show jin scheme4 at left
    voice audio.jin_v_yes1c
    j "Yes, I read my BL there."

    show yoshi tired4 at right
    voice audio.yoshi_v_sigh3a
    yo "Okay, I give up…"

    show jin thinkdn2 at left
    voice audio.jin_v_conj2c1
    j "W-Well, I also play games and watch anime on it, if that’s the answer you’re looking for…"

    show yoshi comp3 at right
    voice audio.yoshi_v_yeah4
    yo "Y-Yeah! Why don’t we do that?"

    show jin talk5 at left
    voice audio.jin_v_conj1b1
    j "Oh! Actually, we could continue with that journal project maybe? I had a lot of fun last time we did it together!"

    show aiden annoy2 at center
    voice audio.aiden_v_bro5b
    a "Bro. You fell asleep in less than fifteen minutes."

    show jin awkward4 at left
    voice audio.jin_v_comp2b1
    j "I-I promise I’ll stay up this time!"

    # JMA2
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
    $ minigame_id = 'jmA2'
    if daya3_choice == False:
        $ renpy.call(minigame_id, 'day')
    else:
        $ renpy.call(minigame_id, 'sunset')

label day3_aiden_postmg:
    $say_box = True
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

    $ location = location_kitchen
    $ day = "??"
    $ time = timeline_timeday
    $ season = season_summer
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_kitchen_past_day with fade
    play music adventure loop

    show yyoshi_camp at left
    show yyoshi shock3 at left
    show yaiden_apron2 at center
    show yaiden norm1 at center
    show andre_camp2 at right
    show andre norm1 at right
    voice audio.yyoshi_v_amazed1a
    yo "Wow… I never knew you guys had to do this much work every day…"

    show andre talk1 at right
    voice audio.andre_v_agree4a
    u "Ah, yes. When you have to feed a hundred people three times a day, it takes a lot of time and effort."

    show yaiden sigh1 at center
    voice audio.yaiden_v_sigh1a
    a "I dunno how Dad did it all by himself before either."

    show andre comp4 at right
    voice audio.andre_v_conj3a1
    u "Haha! It is much easier with you two around! "

    show yyoshi comp5 at left
    voice audio.yyoshi_v_laugh5
    yo "A-Ahehe… I’m just chopping up veggies though… I’m not very good at cooking, haha."

    show yaiden happy1 at center
    voice audio.yaiden_v_alright3a
    a "It’s alright! It saves us a lot of work!"

    show andre play2 at right
    voice audio.andre_v_laugh1a2
    u "Haha, and it’s always been one of Aiden’s least favorite tasks, so I’m sure he’s happy to pawn it off on a friend~"

    show yaiden awkward3 at center
    voice audio.yaiden_v_dad5a
    a "D-Dad! Shhh!"

    show andre talk1 at right
    voice audio.andre_v_conj2a
    u "By the way, Aiden. Is your sauce ready? I need it over here."

    show yaiden talk2 at center
    voice audio.yaiden_v_oh1a
    a "Oh! Sure thing, pops!"

    show yaiden_apron2 at right2
    show yaiden talk2 at right2
    with move

    show yyoshi shock2 at left
    voice audio.yyoshi_v_aiden2
    yo "Aiden, don’t go so fast—"

    show yyoshi shock1 at left
    show yaiden shock3 at right2
    hide andre_camp2
    hide andre talk1
    show andre_camp3 at right
    show andre shock1 at right
    voice audio.yaiden_v_shock1c1
    a "WHOA!" with vpunch

    show andre sigh1 at right
    voice audio.andre_v_sigh1a
    u "And there goes the sauce."

    show yaiden_apron2 at center
    show yaiden panic2 at center
    with move

    voice audio.yaiden_v_shock2b1
    a "Yikes. Sorry, Dad."

    show yyoshi comp6 at left
    voice audio.yyoshi_v_aiden4
    yo "Ahehe… You’re always so clumsy, Aiden."

    show andre play2 at right
    voice audio.andre_v_laugh2a1
    u "You should know Aiden’s quite talented when it comes to tripping and falling by now. "

    show yaiden angry2 at center
    voice audio.yaiden_v_hey1c
    a "H-Hey!"

    show andre explain2 at right
    voice audio.andre_v_conj1a3
    u "Anyway, let me take this shirt off before it stains."

    hide andre_apron2
    hide andre explain2
    show andre_camp4 at right
    show andre explain2 at right
    with dissolve

    show cg fade at truecenter
    show fxmga2 1 at fx_pos
    with dissolve

    voice audio.yyoshi_vsa74_line1
    yo "W-Woah, what’s that?"

    voice audio.andre_vsa74_line1
    u "Hmm? What is it, Yoshinori?"

    voice audio.yyoshi_vsa74_line2
    yo "I’m just surprised you have another tattoo, Mr. Andre. And it’s a big one too."

    show fxmga2 2 at fx_pos
    voice audio.andre_vsa74_line2
    u "Oh, this? Yep! It’s something I got in my younger years, before Aiden was around, haha."

    voice audio.yaiden_vsa74_line1
    a "My dad was a gangster, you know?"

    voice audio.yyoshi_vsa74_line3
    yo "Wah! Really?!"

    show fxmga2 3 at fx_pos
    voice audio.andre_vsa74_line3
    u "*sigh* No, of course not. Aiden’s being silly."

    voice audio.yaiden_vsa74_line2
    a "Sheesh… You could’ve gone along with it for a minute, dad."

    voice audio.yyoshi_vsa74_line4
    yo "It looks like a lizard. Does it stand for anything?"

    show fxmga2 4 at fx_pos
    voice audio.andre_vsa74_line4
    u "It means positivity, flexibility and regeneration, three things that matter when facing challenges in life!"

    voice audio.andre_vsa74_line5
    u "When I look at this tattoo, I remember that things will always look up."

    voice audio.yyoshi_vsa74_line5
    yo "Wow! That’s really inspiring!"

    show fxmga2 5 at fx_pos
    voice audio.yaiden_vsa74_line3
    a "Right? That’s why I wanna get a lizard like that too, but Dad keeps stopping me!"

    voice audio.yaiden_vsa74_line4
    a "He always talks about how painful it would be to get it done, but I could take it!"

    voice audio.andre_vsa74_line6
    u "You’re leaving out the most important reason though, Aiden."

    voice audio.andre_vsa74_line7
    u "A tattoo is a lifelong mark, and you’ll carry it with you forever. You have to make sure there’s a good reason to get it, or it’ll be a huge regret for you down the line."

    voice audio.andre_vsa74_line8
    u "You can’t just get one ’cause your old man has one!"

    hide fxmga2 5
    hide cg fade
    with dissolve

    show yaiden pout5 at center
    voice audio.yaiden_v_hmph1a
    a "Hmph, I already have one on my wrist! You didn’t care about that!"

    show andre angry5 at right
    voice audio.andre_v_aiden5a
    u "That’s different from a giant lizard on your shoulder, son."

    show yyoshi comp2 at left
    voice audio.yyoshi_v_yeah3
    yo "Yeah, Aiden… Are you sure you’d want something that big? Everyone would see it all the time!"

    show yaiden angry2 at center
    voice audio.yaiden_v_confused1c1
    a "If it’s not gonna be seen then what’s the point?"
    a "Even if it was on my butt, I’d want the whole world to see!"

    show yyoshi scared1 at left
    voice audio.yyoshi_v_aiden9
    yo "Aiden! That’s too far!"

    show andre laugh3 at right
    voice audio.andre_v_yoshi1b
    u "Hahaha! Yoshinori, I’m glad you’re around to be a voice of reason for my son here."
    u "Do me a favor and watch over him so that he doesn’t sneak off and get one behind my back."

    show yyoshi happy1 at left
    voice audio.yyoshi_v_yessir2a
    yo "Y-Yes, sir! You can count on me!"

    show yaiden angry3 at center
    voice audio.yaiden_v_hey1c
    a "Hey, that’s no fair using Yoshi against me!"

    show andre laugh2 at right
    voice audio.andre_v_laugh1c1
    u "Hahaha!"

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

label day3_aiden_postfb:

    if daya3_choice == False:
        $ day = "78"
        $ time = timeline_timeday
        $ season = season_winter
        $ location = location_room
        show screen location
        show screen timeline
        show screen quick_menu
        $quick_menu = True
        scene bg_hotel_room2_day with fade
    else:
        $ day = "78"
        $ time = timeline_timesunset
        $ season = season_winter
        $ location = location_room
        show screen location
        show screen timeline
        show screen quick_menu
        $quick_menu = True
        scene bg_hotel_room2_sunset with fade

    play music here_they_come loop
    show jin_autumn at left
    show jin norm1 at left
    show jin_glasses at left
    show aiden2_autumn at center
    show aiden2 annoy2 at center
    show yoshi_autumn at right
    show yoshi norm1 at right
    voice audio.aiden_v_hey1e2
    a "I just realized something… Did you trick us into working on our vacation?!"

    show jin comp6 at left
    voice audio.jin_v_denial2b1
    j "W-Well… Not exactly… "

    show yoshi comp2 at right
    voice audio.yoshi_v_hey1
    yo "Hey, at least we had fun, Aiden."

    hide aiden2_autumn
    hide aiden2 annoy2
    show aiden_autumn at center
    show aiden wink2 at center
    voice audio.aiden_v_alright2b
    a "Okay, now you guys have to listen to me! We’ll have some REAL fun out there!"

    show jin sleepy4 at left
    voice audio.jin_v_oof2a
    j "Hnn… But my tummy’s still turning…"

    show aiden annoy2 at center
    voice audio.aiden_v_laugh1b2
    a "Nice try, Jin. You just don’t wanna leave this room, huh?"

    show yoshi laugh2 at right
    voice audio.yoshi_v_laugh1
    yo "Haha, let Jin be, Aiden. As long as he’s enjoying his vacation, then he can do whatever he wants!"

    show aiden explain1 at center
    voice audio.aiden_v_agree8b2
    a "Fine! But one of these days, you’re gonna be out partying with the rest of us! "

    if daya3_choice == False:
        $daya3_choice = True
        $ renpy.music.stop(channel='music', fadeout = 1.0)
        $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
        $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
        scene cg black with fade

        yo "{i}As we left Jin to rest, we suddenly realized that it was already sunset!{/i}"
        yo "{i}We decided to go check out another area of the hotel before it got dark.{/i}"

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
        $ renpy.music.stop(channel='music', fadeout = 1.0)
        $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
        $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
        scene cg black with fade

        yo "{i}As we left Jin to rest, we suddenly realized that it was already dark out, but we spotted one more place for us to go… {/i}"

        scene cg black
        hide screen location
        hide screen timeline
        hide screen quick_menu
        $quick_menu = False
        with fade
        $ time_transition_sunset_to_night_winter()
        $ renpy.pause (2.0, hard=True)
        jump day3_aiden_after

label day3_aiden_lobby:
    $sq_emilia += 1
    $quick_menu = True
    $say_box = True
    $mm_talking = True
    $a3_lobby = True
    voice audio.yoshi_v_think4
    yo "Maybe we can go back to the lobby?"

    voice audio.aiden_v_confused1c2
    a "The lobby? Did you forget something?"

    voice audio.yoshi_v_disagree4a
    yo "Not really. I just don’t have any other ideas."

    voice audio.aiden_v_unsure1b
    a "I guess that’ll kill some time. Sure, why not!"

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

    if daya3_choice == False:
        $ location = location_hotellobby
        show screen location
        show screen timeline
        show screen quick_menu
        $quick_menu = True
        scene bg_hotel_lobby_day with fade
        play music buddy_oath_hotel loop
    else:
        $ location = location_hotellobby
        show screen location
        show screen timeline
        show screen quick_menu
        $quick_menu = True
        scene bg_hotel_lobby_sunset with fade
        play music buddy_oath_hotel loop

    show aiden2_autumn at left2
    show aiden2 confused6 at left2
    show yoshi_autumn at right2
    show yoshi norm3 at right2
    voice audio.aiden_v_so2
    a "Sooo… Why exactly are we back here again?"

    show aiden2_autumn at p5_1
    show aiden2 confused6 at p5_1
    show yoshi_autumn at p5_2
    show yoshi norm3 at p5_2
    with move

    show emilia_autumn at p5_5
    show emilia norm3 at p5_5
    with dissolve

    hide aiden2_autumn
    hide aiden2 confused6
    show aiden_autumn at p5_1
    show aiden shock2 at p5_1
    voice audio.aiden_v_swear3b
    a "Oh, crap, Emilia’s here too! Quick, Yoshi, let’s scram!"

    show yoshi confused2 at p5_2
    voice audio.yoshi_v_huh5
    yo "Huh… I thought she’d be in her room… I wonder what she's doing here by herself."

    show aiden sigh4 at p5_1
    voice audio.aiden_v_sigh1a
    a "Probably waiting to speak with the manager again…"

    hide yoshi_autumn
    hide yoshi confused2
    show yoshi2_autumn at p5_2
    show yoshi2 sigh4 at p5_2
    voice audio.yoshi_v_sigh3a
    yo "*sigh* She’s gonna cause a commotion if we don’t stop her."

    show aiden shock2 at p5_1
    voice audio.aiden_v_wait1a1
    a "Wait… Don’t tell me you’re gonna go and talk to her?"

    hide yoshi2_autumn
    hide yoshi2 sigh4
    show yoshi_autumn at p5_2
    show yoshi talk1 at p5_2
    voice audio.yoshi_v_well1
    yo "Well, only to make sure she’s not going to get herself in trouble."

    hide aiden_autumn
    hide aiden shock2
    show aiden2_autumn at p5_1
    show aiden2 comp6 at p5_1
    voice audio.aiden_v_laugh1b1
    a "Ahehe… You really are too nice, Yoshi."

    show yoshi talk2 at p5_2
    voice audio.yoshi_v_comp4
    yo "Don’t worry, I’ll make it quick."

    show yoshi_autumn at p5_4
    show yoshi talk2 at p5_4
    with move

    show aiden2 sigh1 at p5_1
    voice audio.aiden_v_sigh1a
    a "*sigh*"

    $ renpy.music.stop(channel='music', fadeout = 2.0)
    show aiden2 awkward1 at p5_1
    show yoshi talk3 at p5_4
    voice audio.yoshi_v_emilia3
    yo "Hey there, Emilia."

    show emilia shock2 at p5_5
    voice audio.emilia_v_gasp1
    e "*gasp* " with vpunch
    e "Goodness fucking gracious! How dare you sneak up on me like that!"

    show yoshi awkward4 at p5_4
    voice audio.yoshi_v_ah3
    yo "A-Ah, I’m sorry. I didn’t mean to."

    show emilia irked2 at p5_5
    voice audio.emilia_v_what2
    e "What the hell do you want? "

    show yoshi explain2 at p5_4
    voice audio.yoshi_v_well1
    yo "I was just passing by and happened to see you here."
    yo "What are you doing all by yourself?"

    show emilia annoy2 at p5_5
    voice audio.emilia_v_dismiss1a
    e "Now all of a sudden you’re interested? It’s none of your business. Leave me alone."

    show yoshi annoy4 at p5_4
    voice audio.yoshi_v_rush4
    yo "Come on, Emilia… We’re on a vacation… Do you really want to spend your time here being sour?"

    show emilia annoy4 at p5_5
    voice audio.emilia_v_hmph1a
    e "For your information, I was having a good time before you came along."

    hide yoshi_autumn
    hide yoshi annoy4
    show yoshi2_autumn at p5_4
    show yoshi2 think5 at p5_4
    voice audio.yoshi_v_well3
    yo "W-Well I just thought you'd enjoy some company."

    show emilia disgust5 at p5_5
    voice audio.emilia_v_sarcastic2a
    e "I don’t need other people to enjoy a vacation! Especially now that I’m finally in a place up to my standards."

    hide yoshi2_autumn
    hide yoshi2 think5
    show yoshi_autumn at p5_4
    show yoshi explain2 at p5_4
    voice audio.yoshi_v_sigh3a
    yo "Either way, you know where to find me."

    play music heracleum_a loop
    show emilia rage4 at p5_5
    voice audio.emilia_v_ugh1
    e "Would you stop that already?!"

    show yoshi awkward4 at p5_4
    voice audio.yoshi_v_what3
    yo "Wh-Wha… Stop what…?"

    show emilia eyeroll6 at p5_5
    voice audio.emilia_v_scoff1
    e "You know what you’re doing! You’re acting like that goody-two-shoes scout that pretends to care about everything!"
    e "I know better now than to get tricked by fake people like you!"

    show yoshi awkward3 at p5_4
    voice audio.yoshi_v_but3
    yo "Emilia… That’s not—"

    show emilia rage4 at p5_5
    voice audio.emilia_v_angry4b
    e "If you came here to ruin my oh-so-perfect-day. Congratulations, you just did."

    hide emilia_autumn
    hide emilia rage4
    with dissolve

    hide yoshi_autumn
    hide yoshi awkward3
    show yoshi2_autumn at p5_4
    show yoshi2 sigh4 at p5_4
    voice audio.yoshi_v_sigh3a
    yo "*sigh*"

    $ renpy.music.stop(channel='music', fadeout = 2.0)
    show aiden2_autumn at left2
    show aiden2 worry2 at left2
    show yoshi2_autumn at right2
    show yoshi2 sigh4 at right2
    with move

    voice audio.aiden_v_sheesh1a
    a "Sheesh... I knew that was a bad idea."

    show yoshi2 worry2 at right2
    voice audio.yoshi_v_yeah3
    yo "Yeah, I don’t even know why I tried."

    show aiden2 sad4 at left2
    voice audio.aiden_v_agree6b
    a "I know you just wanna help, but you just can't change some people, Yoshi..."

    show yoshi2 sad4 at right2
    voice audio.yoshi_v_but2
    yo "I just can't help but think about how almost everyone gave up on her when we were scouts."
    yo "And even though we're much older, she's still stuck in her ways."

    show yoshi2 sad6 at right2
    voice audio.yoshi_v_conj1b
    yo "And I'm worried that if I stop trying, then who will?"

    show aiden2 upset1 at left2
    a "..."

    hide yoshi2_autumn
    hide yoshi2 sad4
    show yoshi_autumn at right2
    show yoshi worry3 at right2
    voice audio.yoshi_v_ah3
    yo "Ah, I’m sorry, Aiden! I didn't mean to dig so deeply into that."
    yo "We should be trying to do something fun out here."

    show aiden2 comp6 at left2
    voice audio.aiden_v_yeah1g1
    a "Ahehe… Yeah…"

    show yoshi talk3 at right2
    voice audio.yoshi_v_alright1
    yo "Alright, let’s check out where we should go next!"

    if daya3_choice == False:
        $ daya3_choice = True
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
        $say_box = False
        $mm_talking = False
        $renpy.choice_for_skipping()
        show screen minimap()
        $ renpy.pause (hard=True)

    else:
        $ renpy.music.stop(channel='music', fadeout = 1.0)
        $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
        $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
        scene cg black
        hide screen location
        hide screen timeline
        hide screen quick_menu
        $quick_menu = False
        with fade
        $ time_transition_sunset_to_night_winter()
        $ renpy.pause (2.0, hard=True)
        jump day3_aiden_after

label day3_aiden_after:
    show screen location
    show screen timeline
    show screen quick_menu
    scene mm_aiden_final
    $quick_menu = True
    with fade
    $ time = timeline_timenight
    $say_box = True
    voice audio.yoshi_v_oh1
    yo "Oh, look! They have a bar here, Aiden! "

    voice audio.aiden_v_excited2a
    a "Now you’re talking! Let’s grab some drinks, then!"

    voice audio.yoshi_v_but1
    yo "Although I don’t think it’s included in our room package, unlike the other areas."

    voice audio.aiden_v_aww3a
    a "Aww… That’s a bummer."

    voice audio.yoshi_v_comp5
    yo "Don’t worry, though! It’s my treat!"

    voice audio.aiden_v_really3a
    a "Wah, really, Yoshi?! Let’s go then!!"

    voice audio.yoshi_v_wait3a
    yo "H-Hey, wait for me…!!"

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

    $ location = location_hotelclub
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_hotel_bar_night with fade
    play music on_the_edge_club loop

    show yoshi_autumn at left2
    show yoshi confused1 at left2
    show aiden_autumn at right2
    show aiden shock1 at right2
    yo "..."

    show aiden awkward3 at right2
    voice audio.aiden_v_shock1d2
    a "This place is… interesting… It’s nothing like the bars we go to back home!"
    a "I mean… look at all those servers and dancers! They sure know how to entertain their guests, huh?"

    show yoshi confused2 at left2
    voice audio.yoshi_v_think1a
    yo "Yeah, this place is a lot more like a party club than a casual pub…"

    show aiden comp3 at right2
    voice audio.aiden_v_yeah1c2
    a "Considering how fancy everything was so far, I think that’s what they were going for!"

    show yoshi_autumn at center
    show yoshi confused2 at center
    show aiden_autumn at right
    show aiden comp3 at right
    with move

    show justin_bar at left
    show justin_glasses at left
    show justin happy1 at left
    with dissolve

    voice audio.justin_v_greet3a
    bt "Hello! Welcome to Bottom’s Up!  We pride ourselves on our ‘top’ service!"
    bt "What can I get you two fine gentlemen? Fancy a drink?"

    show aiden tease2 at right
    voice audio.aiden_v_oho1a
    a "Fine gentlemen, I like the sound of that~ "

    show yoshi think2 at center
    voice audio.yoshi_v_uh1a
    yo "Uh… We’re fairly new here, so we don’t really know what to get…"

    show justin happy2 at left
    voice audio.justin_v_ofcourse1a
    bt "Of course! I’d be happy to help you out~ What liquor do you usually fancy? Rum? Whiskey? Tequila? "

    hide aiden_autumn
    hide aiden tease2
    show aiden2_autumn at right
    show aiden2 think5 at right
    voice audio.aiden_v_think2a
    a "Uh… We usually just drink canned beer. "

    show justin play2 at left
    voice audio.justin_v_ehem1a1
    bt "Do you really want canned beer in a place like this? Take a look at our menu~!"

    show aiden2 awkward5 at right
    voice audio.aiden_v_oops3b
    a "Oof... Help me out here, Yoshi…"

    show yoshi confused1 at center
    yo "{i}(Looking at the options… Aiden would like…){/i}"

    $working = False
    $shuffle_menu()
    menu():
        yo "{i}(Looking at the options… Aiden would like…){/i}{fast}"
        "Slippery Nipple.":
            $working = True
            $score_aiden -= 1
            $score_bot += 1
            $drink = 1
            show yoshi talk1 at center
            voice audio.yoshi_v_think4
            yo "I think you’d like a ‘Slippery Nipple!’"

            show aiden2 confused5 at right
            voice audio.aiden_v_confused1a2
            a "Eh, what’s that?"

            hide yoshi_autumn
            hide yoshi talk1
            show yoshi2_autumn at center
            show yoshi2 shy5 at center
            voice audio.yoshi_v_conj4a
            yo "H-Honestly, I have no idea…"

            show justin explain3 at left
            voice audio.justin_v_conj2a1
            bt "It’s cream liqueur mixed with sambuca!"

            show aiden2 awkward6 at right
            voice audio.aiden_v_confused2a1
            a "S-Sambuca…?"

            hide yoshi2_autumn
            hide yoshi2 shy5
            show yoshi_autumn at center
            show yoshi happy1 at center
            voice audio.yoshi_v_well3
            yo "W-Well, let’s just try it, Aiden!"

            show justin happy1 at left
            voice audio.justin_v_catchphrase2a
            bt "Alright then! Two ‘Slippery Nipples’ coming up!"

            show justin_bar at p5_1
            show justin_glasses at p5_1
            show justin comp3 at p5_1
            with move

            hide aiden2_autumn
            hide aiden2 awkward6
            show aiden_autumn at right
            show aiden comp3 at right
            voice audio.aiden_v_unsure1a
            a "I guess we should’ve brought Gramps with us, huh…? He usually knows these kinds of things…"

            hide yoshi_autumn
            hide yoshi happy1
            show yoshi2_autumn at center
            show yoshi2 comp6 at center
            voice audio.yoshi_v_yeah4
            yo "Y-Yeah…"
        "Sit on my Face.":
            $working = True
            $score_aiden -= 1
            $score_top += 1
            $drink = 2
            show yoshi think2 at center
            voice audio.yoshi_v_think4
            yo "How about you try ‘Sit on my Face’, Aiden?"

            show aiden2 confused5 at right
            voice audio.aiden_v_confused1a2
            a "Eh, what’s that?"

            hide yoshi_autumn
            hide yoshi think2
            show yoshi2_autumn at center
            show yoshi2 shy5 at center
            voice audio.yoshi_v_conj4a
            yo "H-Honestly, I have no idea…"

            show justin explain3 at left
            voice audio.justin_v_conj1a1
            bt "It’s a mix of cream, coffee and hazelnut liqueur!"

            show aiden2 awkward6 at right
            voice audio.aiden_v_unsure1b
            a "That sounds nice, I guess…?"

            hide yoshi2_autumn
            hide yoshi2 shy5
            show yoshi_autumn at center
            show yoshi comp3 at center
            voice audio.yoshi_v_well1
            yo "Well, we won’t know until we try!"

            hide aiden2_autumn
            hide aiden2 awkward6
            show aiden_autumn at right
            show aiden explain1 at right
            voice audio.aiden_v_alright2a
            a "Alright, alright."

            show justin happy1 at left
            voice audio.justin_v_catchphrase2a
            bt "‘Sit on my Face’ times two coming up, then! "

            show justin_bar at p5_1
            show justin_glasses at p5_1
            show justin happy1 at p5_1
            with move

            show aiden comp3 at right
            voice audio.aiden_v_unsure1a
            a "I guess we should’ve brought Gramps with us, huh…? He usually knows these kinds of things…"

            hide yoshi_autumn
            hide yoshi comp3
            show yoshi2_autumn at center
            show yoshi2 comp6 at center
            voice audio.yoshi_v_yeah4
            yo "Y-Yeah…"
        "Blow Job Shots.":
            $working = True
            $score_aiden += 1
            $score_bot += 2
            $drink = 3
            show yoshi happy1 at center
            voice audio.yoshi_v_think4
            yo "Let’s get some ‘Blow Job Shots’, Aiden!"

            hide aiden2_autumn
            hide aiden2 awkward5
            show aiden_autumn at right
            show aiden bold2 at right
            voice audio.aiden_v_oho1a
            a "Oho~! I like the sound of that~!"

            show yoshi bold2 at center
            voice audio.yoshi_v_actually1a
            yo "It’s cream and coffee liqueur! You’ll love it!"

            show aiden excited1 at right
            voice audio.aiden_v_oh1a
            a "Ooh, sweet!"

            show justin happy1 at left
            voice audio.justin_v_catchphrase2a
            bt "Alright~ Two ‘Blow Job Shots’ coming up! "

            show justin_bar at p5_1
            show justin_glasses at p5_1
            show justin happy1 at p5_1
            with move

            show aiden comp3 at right
            voice audio.aiden_v_relief1a1
            a "Good thing you know about these kinds of drinks, Yoshi! I swear I almost ordered a soda just so I didn’t embarrass myself."

            show yoshi laugh2 at center
            voice audio.yoshi_v_laugh1
            yo "I only know them from college parties, honestly. I have no idea about the rest of the menu either, hahaha!"
        "Sex on the Beach.":
            $working = True
            $score_aiden += 1
            $score_top += 2
            $drink = 4
            show yoshi happy1 at center
            voice audio.yoshi_v_think4
            yo "I bet you’ll like ‘Sex on the Beach’, Aiden!"

            hide aiden2_autumn
            hide aiden2 awkward5
            show aiden_autumn at right
            show aiden bold2 at right
            voice audio.aiden_v_laugh2a1
            a "Hahaha! I like the sound of that~!"

            show yoshi bold2 at center
            voice audio.yoshi_v_actually1a
            yo "It’s a mix of vodka, peach schnapps, cranberry and orange! "

            show aiden excited1 at right
            voice audio.aiden_v_oh1a
            a "Ooh, fruity~"

            show justin happy1 at left
            voice audio.justin_v_catchphrase2a
            bt "Alright~ A pair of ‘Sex on the Beach’ coming up! "

            show justin_bar at p5_1
            show justin_glasses at p5_1
            show justin happy1 at p5_1
            with move

            show aiden comp3 at right
            voice audio.aiden_v_relief1a1
            a "Good thing you know about these kinds of drinks, Yoshi! I swear I almost ordered a soda just so I didn’t embarrass myself."

            show yoshi laugh2 at center
            voice audio.yoshi_v_laugh1
            yo "I only know them from college parties, honestly. I have no idea about the rest of the menu either, hahaha!"
    show justin talk4 at p5_1
    voice audio.justin_v_hmm1a
    bt "You two seem like you’re not from around the city. Where are you guys from?"

    hide yoshi2_autumn
    hide yoshi2 laugh2
    hide yoshi2 comp6
    show yoshi_autumn at center
    show yoshi talk3 at center
    voice audio.yoshi_v_ah3
    yo "A-Ah…! We’re from Camp Buddy."

    show justin confused2 at p5_1
    voice audio.justin_v_unsure1a
    bt "I’m not familiar… Is that some kind of gentleman’s club?"

    show yoshi talk1 at center
    voice audio.yoshi_v_oh2
    yo "O-Oh, no, it’s a scout-themed summer camp. "

    show justin happy2 at p5_1
    voice audio.justin_v_question1a1
    bt "Well, that’s something you don’t hear about every day. Aren’t you guys too old to be in a summer camp?"

    show aiden happy1 at right
    voice audio.aiden_v_laugh2a1
    a "Hahaha! We’re scoutmasters!"

    show justin talk4 at p5_1
    voice audio.justin_v_oh1a1
    bt "Oh, that makes sense. What brings you two to a place like this?  "

    show yoshi explain2 at center
    voice audio.yoshi_v_well2
    yo "Well, our sponsor brought us here for a team-building vacation."

    show justin think2 at p5_1
    voice audio.justin_v_intresting1a
    bt "Interesting… Must be some boujee summer camp to get the most expensive hotel in the city."

    show aiden laugh3 at right
    voice audio.aiden_v_no2a1
    a "Nah, we actually almost went bankrupt, hahaha!"

    show justin sad2 at p5_1
    voice audio.justin_v_oof1a
    bt "Oh, that sounds rough…"

    show yoshi happy2 at center
    voice audio.yoshi_v_comp2
    yo "We did manage to hold a fundraiser and find a sponsor, so it’s all good now!"

    show justin grin2 at p5_1
    voice audio.justin_v_laugh1
    bt "Glad you guys were able to pull through!"

    hide yoshi_autumn
    hide yoshi happy2
    show yoshi2_autumn at center
    show yoshi2 comp6 at center
    voice audio.yoshi_v_unsure3a
    yo "I guess you could say it was a lucky break…"

    show justin_bar at left
    show justin_glasses at left
    show justin happy1 at left
    with move

    voice audio.justin_v_conj5a
    bt "Here are your drinks! "

    if drink == 1:
        hide aiden_autumn
        hide aiden laugh3
        show aiden2_autumn at right
        show aiden2 confused6 at right
        voice audio.aiden_v_confused2a1
        a "This… looks interesting."

        hide yoshi2_autumn
        hide yoshi2 comp6
        show yoshi_autumn at center
        show yoshi comp5 at center
        voice audio.yoshi_v_encourage2
        yo "Let’s try it!"

        hide aiden2_autumn
        hide aiden2 confused6
        show aiden_autumn at right
        show aiden think1 at right
        a "*sip*"

        hide yoshi_autumn
        hide yoshi comp5
        show yoshi2_autumn at center
        show yoshi2 pain3 at center
        voice audio.yoshi_v_shock4
        yo "*cough* *cough* S-So strong… "

        hide aiden_autumn
        hide aiden
        show aiden2_autumn at right
        show aiden2 pain2 at right
        voice audio.aiden_v_hngh1a2
        a "Tastes like anise…"

        show justin play5 at left
        voice audio.justin_v_catchphrase1a
        bt "Bingo! That’s what sambuca is!"

        show aiden2 awkward3 at right
        voice audio.aiden_v_think2a
        a "Don’t you use that for cooking?"

        show yoshi2 comp3 at center
        voice audio.yoshi_v_uh1a
        yo "M-Maybe let’s just order something else…"

        show justin laugh1 at left
        voice audio.justin_v_laugh2
        bt "Haha! There’s plenty of other drinks I’d recommend!"

        show justin comp3 at left
        voice audio.justin_v_conj1a1
        bt "Here, I’ll make something new for you both."
        bt "While you wait, why don’t you consider joining some of the events tonight?"
    elif drink == 2:
        hide aiden_autumn
        hide aiden laugh3
        show aiden2_autumn at right
        show aiden2 confused6 at right
        voice audio.aiden_v_confused2a1
        a "This… looks interesting."

        hide yoshi2_autumn
        hide yoshi2 comp6
        show yoshi_autumn at center
        show yoshi comp5 at center
        voice audio.yoshi_v_encourage2
        yo "Let’s try it!"

        hide aiden2_autumn
        hide aiden2 confused6
        show aiden_autumn at right
        show aiden think1 at right
        a "*sip*"

        hide aiden_autumn
        hide aiden
        show aiden2_autumn at right
        show aiden2 pain2 at right
        voice audio.aiden_v_hngh1a2
        a "T-Too sweet…"

        hide yoshi_autumn
        hide yoshi comp5
        show yoshi2_autumn at center
        show yoshi2 pain3 at center
        voice audio.yoshi_v_shock4
        yo "*cough* *cough* Yeah, I don’t think this is for me, either."

        show justin laugh1 at left
        voice audio.justin_v_laugh2
        bt "Haha! How about I get you two something else? There’s plenty of other drinks I’d recommend!"

        show justin comp3 at left
        voice audio.justin_v_conj1a1
        bt "Here, I’ll make something new for you both."
        bt "While you wait, why don’t you consider joining some of the events tonight?"
    elif drink == 3:
        show aiden excited3 at right
        voice audio.aiden_v_shock1d1
        a "Whoa… It even has whipped cream?!"

        hide yoshi2_autumn
        hide yoshi2 comp6
        show yoshi_autumn at center
        show yoshi happy1 at center
        voice audio.yoshi_v_encourage1
        yo "Go ahead, Aiden! Try it!"

        show aiden tasty1 at right
        a "*sip*"

        show aiden amazed2 at right
        voice audio.aiden_v_swear2a1
        a "HOLY… Is this really alcohol?! It’s so good!"

        show yoshi laugh1 at center
        voice audio.yoshi_v_laugh1
        yo "Haha! I knew you were gonna like it! "

        show aiden bold3 at right
        voice audio.aiden_v_oho2a
        a "Ohoho~ I’m gonna enjoy drinking more of this all night~!"

        show yoshi play2 at center
        voice audio.yoshi_v_comp8b
        yo "Don’t drink too fast, Aiden! The night is still young, haha!"

        show justin happy1 at left
        voice audio.justin_v_compliment5a
        bt "That’s right! There’s still plenty of events for the rest of the night!"
    elif drink == 4:
        show aiden excited3 at right
        voice audio.aiden_v_shock1d1
        a "Whoa… These look colorful. It’s even got a teeny-tiny umbrella, haha!"

        hide yoshi2_autumn
        hide yoshi2 comp6
        show yoshi_autumn at center
        show yoshi happy1 at center
        voice audio.yoshi_v_encourage1
        yo "Go ahead, Aiden! Try it!"

        show aiden tasty1 at right
        a "*sip*"

        show aiden amazed2 at right
        voice audio.aiden_v_swear2a1
        a "HOLY… Is this really alcohol?! It’s so good!"

        show yoshi laugh1 at center
        voice audio.yoshi_v_laugh1
        yo "Haha! I knew you were gonna like it! "

        show aiden bold3 at right
        voice audio.aiden_v_oho2a
        a "Ohoho~ I’m gonna enjoy drinking more of this all night~!"

        show yoshi play2 at center
        voice audio.yoshi_v_comp8b
        yo "Don’t drink too fast, Aiden! The night is still young, haha!"

        show justin happy1 at left
        voice audio.justin_v_compliment5a
        bt "That’s right! There’s still plenty of events for the rest of the night!"

    hide yoshi2_autumn
    hide yoshi2 comp3
    hide yoshi2 pain3
    show yoshi_autumn at center
    show yoshi confused2 at center
    voice audio.yoshi_v_huh5
    yo "The entertainment here is really… unique, huh?"

    show justin tease2 at left
    voice audio.justin_v_ofcourse1a
    bt "Of course! Bottom’s Up guarantees our guests quality ‘top’ service just like our slogan says~"

    hide aiden2_autumn
    hide aiden2 awkward3
    hide aiden2 pain2
    show aiden_autumn at right
    show aiden talk4 at right
    voice audio.aiden_v_yeah1a1
    a "Yeah, I can see that… all the staff here are hella gorgeous."

    show justin tease5 at left
    voice audio.justin_v_conj1a1
    bt "Well, I think you two would pass off as entertainers if I do say so myself! Handsome, hunky, and must be packing too~!"
    bt "And I would bet money that if you were up for grabs, you’d be booked solid!"

    show justin wink3 at left
    voice audio.justin_v_laugh5
    bt "By me included~ *wink*"

    show aiden play2 at right
    voice audio.aiden_v_laugh1b2
    a "Hehe, Yoshi would be popular for sure~! He’s quite the beefcake!"

    hide yoshi_autumn
    hide yoshi confused2
    show yoshi2_autumn at center
    show yoshi2 shy5 at center
    voice audio.yoshi_v_aiden5
    yo "Aiden… You’re the one who likes going bare in front of others… I think you’d blend in here more than me."

    show justin happy1 at left
    voice audio.justin_v_catchphrase1a
    bt "There we go, you guys already have the qualities for it! "
    bt "You can always join in the fun~ We have private booths in the back if you want to hit up one of them~"

    show justin play3 at left
    voice audio.justin_v_bold1a
    bt "I’m sure with guys of your caliber, a lot of the staff would be happy to volunteer to have some fun."
    bt "Maybe even fight over it."

    show aiden tease3 at right
    voice audio.aiden_v_laugh3b
    a "Pffft—"

    show yoshi2 awkward3 at center
    voice audio.yoshi_v_ah3
    yo "A-Ah… That won’t be necessary…"

    show justin talk3 at left
    voice audio.justin_v_oops1a
    bt "Oops— I apologize, sorry for not noticing it sooner! You two must be a couple!"

    $working = False
    $shuffle_menu()
    menu():
        bt "Oops— I apologize, sorry for not noticing it sooner! You two must be a couple!{fast}"
        "Not at all.":
            $ working = True
            $ score_aiden -= 2
            $ aiden_deny = True
            hide aiden_autumn
            hide aiden tease3
            show aiden2_autumn at right
            show aiden2 upset4 at right
            hide yoshi2_autumn
            hide yoshi2 awkward3
            show yoshi_autumn at center
            show yoshi panic4 at center
            voice audio.yoshi_v_no5
            yo "A-Ah! Please don’t get the wrong idea, we’re just co-workers…!"

            show justin think2 at left
            voice audio.justin_v_oh1a1
            bt "Oh, I guess my hunch was wrong this time~"
        "We're just friends.":
            $ working = True
            $ score_aiden -= 1
            $ aiden_deny = True
            hide aiden_autumn
            hide aiden tease3
            show aiden2_autumn at right
            show aiden2 upset4 at right
            hide yoshi2_autumn
            hide yoshi2 awkward3
            show yoshi_autumn at center
            show yoshi panic4 at center
            voice audio.yoshi_v_no5
            yo "A-Ah! Please don’t get the wrong idea, we’re just friends!"

            show justin think2 at left
            voice audio.justin_v_oh1a1
            bt "Oh, my bad. It really looked like something else."
        "I wish.":
            $ working = True
            $ score_aiden += 1
            $ aiden_deny = False
            hide aiden_autumn
            hide aiden tease3
            show aiden2_autumn at right
            show aiden2 shy1 at right
            show aiden2_blush1 at right
            hide yoshi2_autumn
            hide yoshi2 awkward3
            show yoshi_autumn at center
            show yoshi sigh4 at center
            show yoshi_blush1 at center
            voice audio.yoshi_v_sigh3a
            yo "I wish that were true, we’ve known each other for so long."

            show justin play2 at left
            voice audio.justin_v_laugh5
            bt "Why not make it happen then~?"
        "Sort of.":
            $ working = True
            $ score_aiden += 2
            $ aiden_deny = False
            hide aiden_autumn
            hide aiden tease3
            show aiden2_autumn at right
            show aiden2 shy1 at right
            show aiden2_blush1 at right
            hide yoshi2_autumn
            hide yoshi2 awkward3
            show yoshi_autumn at center
            show yoshi think2 at center
            show yoshi_blush1 at center
            voice audio.yoshi_v_unsure3c
            yo "I-I guess you could say that. Aiden and I are pretty close…"

            show justin play2 at left
            voice audio.justin_v_laugh5
            bt "That’s good enough for me~"

    hide aiden2_autumn
    hide aiden2 upset4
    hide aiden2 shy1
    hide aiden2_blush1
    show aiden_autumn at right
    show aiden kiss2 at right
    show aiden_blush1 at right
    a "*gulps his drink*"

    play sound sfx_shotglass
    show aiden drunk6 at right
    hide aiden_blush1
    hide yoshi_blush1
    voice audio.aiden_v_relief2a
    a "AAAH!"
    a "More shots!"

    show justin play3 at left
    voice audio.justin_v_oh1c1
    bt "Ohh~ Now we’re talking~!"

    show yoshi shock2 at center
    voice audio.yoshi_v_comp7
    yo "S-Slow down, Aiden…! "

    show justin tease3 at left
    voice audio.justin_v_catchphrase3a
    bt "Chill out! Have fun, let loose and don’t think about anything else!"

    show aiden bold2 at right
    voice audio.aiden_v_yeah1a1
    a "Yeah! Listen to Mr. Bartender and live a little, Yoshi~!"

    show justin happy2 at left
    voice audio.justin_v_intro1a
    ju "Name’s Justin by the way! I’m afraid we didn’t really introduce ourselves properly before."

    show yoshi happy2 at center
    voice audio.yoshi_v_greet11
    yo "Nice to meet you, Justin. I’m Yoshinori and this is Aiden."

    show justin laugh1 at left
    voice audio.justin_v_conj1a1
    ju "Well, Yoshinori and Aiden, order as many drinks as you want! "

    show aiden laugh3 at right
    voice audio.aiden_v_drunk4a
    a "Woooo! Keep the bartender’s special coming then! I’d like to try them all! "

    show justin laugh2 at left
    voice audio.justin_v_catchphrase2a
    ju "Coming right up!"

    scene cg black with fade
    yo "{i}The bartender kept serving Aiden and I drinks for a while, and we really enjoyed our conversation with him.{/i}"
    yo "{i}Eventually, he had to take care of some other customers, leaving us with more rounds than we ordered.{/i}"
    yo "{i}It wasn’t too long before we were both starting to feel a little tipsy…{/i}"

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

    $ location = location_hotelclub
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_hotel_bar_night with fade
    play music on_the_edge_club loop
    play bgsound sfxloop_nightclub loop

    show yoshi_autumn at left2
    show yoshi drunk1 at left2
    show yoshi_blush2 at left2
    show aiden_autumn at right2
    show aiden drunk1 at right2
    show aiden_blush2 at right2
    voice audio.yoshi_v_gulp1a
    yo "*hic* This is the most I’ve drank in a while… I think it’s starting to get to me… "
    yo "We might’ve taken a little more than we could—"

    show aiden drunk6 at right2
    voice audio.aiden_v_drink1a
    a "Gahhhh! "

    show aiden laugh3 at right2
    voice audio.aiden_v_drunk4b
    a "Shots, shots, shots! Wooo! " with vpunch

    show yoshi worry5 at left2
    voice audio.yoshi_v_aiden8
    yo "Aiden, I already lost count of how much you’ve had. Don’t you think you’ve had enough…?"

    show aiden excited3 at right2
    voice audio.aiden_v_no1a1
    a "No way, Yoshi! This stuff is bussin’! "
    a "You only live once, so make the most of it!"

    hide yoshi_autumn
    hide yoshi worry5
    hide yoshi_blush2
    show yoshi2_autumn at left2
    show yoshi2 sigh4 at left2
    show yoshi2_blush2 at left2
    voice audio.yoshi_v_sigh3a
    yo "*sigh* You know that if I drink too much, I’ll start acting weird… "

    show aiden drunk2 at right2
    voice audio.aiden_v_drunk3a
    a "That’s the point! You’re way more fun when you’re drunk!"
    a "You get hella flirty and your tongue gets loose, if you know what I mean~"

    show aiden drunk5 at right2
    voice audio.aiden_v_drunk2b1
    a "Just like that one time you loaded me up and we could barely walk after!"

    hide yoshi2_autumn
    hide yoshi2 sigh4
    hide yoshi2_blush2
    show yoshi_autumn at left2
    show yoshi angry2 at left2
    show yoshi_blush2 at left2
    voice audio.yoshi_v_wait3b
    yo "A-Aiden!! People can hear us…!"

    show aiden drunk3 at right2
    voice audio.aiden_v_confident2a
    a "I don’t care what others think! I already walk around the camp naked every day!"
    a "Everybody likes to see my bod! They say it’s my best quality after all!"

    show yoshi worry2 at left2
    voice audio.yoshi_v_aiden5
    yo "Aiden…"

    show aiden laugh3 at right2
    voice audio.aiden_v_laugh2a1
    a "Maybe the bartender was right, I’d be great as an entertainer here…! Hahaha!"
    a "And you’ll be my first lap dance, cowboy!"

    show aiden_autumn at center
    show aiden drunk2 at center
    show aiden_blush2 at center
    with move

    voice audio.aiden_v_perv1
    a "Let’s see what’s hiding in those pants and get this show going!"
    a "Ugh… Is it me, or is it getting hot in here?! "

    show yoshi sigh1 at left2
    voice audio.yoshi_v_think1a
    yo "Your face is flushed, and you’re all covered in sweat… You definitely drank too much…"

    show aiden tired5 at center
    voice audio.aiden_v_psh1a
    a "Psh… I’m fine! I’m just HOT!"
    a "I swear, I’m sweating bullets in this shirt! "

    #blush hiden and shown otherwise it won't appear on top of char
    hide aiden_autumn
    hide aiden tired5
    hide aiden_blush2
    show aiden_shirtless at center
    show aiden drunk6 at center
    show aiden_blush2 at center
    with dissolve

    voice audio.aiden_v_relief1a1
    a "Ahhh~! That’s more like it!"

    show yoshi panic4 at left2
    voice audio.yoshi_v_wait6
    yo "A-Aiden, w-we’re in public…!!"

    show aiden bold2 at center
    voice audio.aiden_v_confident2c
    a "So what?! I’ll teach them how to put on a show~!"

    show aiden excited2 at center
    voice audio.aiden_v_atyourservice2a1
    a "I see you all looking~! Wanna see what I’m packing~?!"

    play sound sfx_clubcheer
    show yoshi scared2 at left2
    voice audio.yoshi_v_aiden6
    yo "A-Aiden! If you keep stripping, people are gonna start putting money in your pants…!"

    show aiden excited3 at center
    voice audio.aiden_v_drunk3a
    a "I won’t say no to some free cash!! Drinks are on me now!"

    show yoshi panic3 at left2
    voice audio.yoshi_v_wait3a
    yo "N-No! Wait—"

    hide aiden_shirtless
    hide aiden excited1
    show aiden_undie at center
    show aiden laugh4 at center
    show aiden_blush2 at center
    show cg fade at truecenter
    show fxa3 at fx_pos
    with dissolve

    play sound sfx_clubcheer
    voice audio.aiden_vsa72_line1
    a "WHOOO!!! MAKE IT RAIN!!"

    voice audio.yoshi_vsa72_line1
    yo "AIDEN?! WHERE ARE YOUR PANTS?!"

    voice audio.aiden_vsa72_line2
    a "Can’t you see the crowd loves it?!"

    play sound sfx_clubcheer
    voice audio.yoshi_vsa72_line2
    yo "G-Get down from there, Aiden…! They’re starting to take pictures!"

    voice audio.aiden_vsa72_line3
    a "Come and grab me then!"

    hide cg fade
    hide fxa3
    with dissolve

    show yoshi_autumn at center
    show yoshi panic3 at center
    show yoshi_blush2 at center
    with move

    show yoshi_autumn at p5_1
    show yoshi panic3 at p5_1
    show yoshi_blush2 at p5_1
    show aiden_undie at p5_2
    show aiden laugh4 at p5_2
    with move

    hide aiden_blush2
    show aiden pout4 at p5_2
    show aiden_blush2 at p5_2
    voice audio.yoshi_v_comp7
    yo "S-Seriously, Aiden…! You’re way too drunk!"

    voice audio.aiden_v_drunk1a
    a "Whaaaaaatttt??? I can take in mooooooore than you think!"

    show naoto_club at p5_5
    show naoto tease2 at p5_5
    show naoto_strip at p5_5
    with dissolve

    voice audio.naoto_v_impressed1b
    nas "Looks like we have a new breakout star over here~!"
    nas "We’re already getting some requests for you in the back room, bro!"

    show naoto_club at right
    show naoto tease2 at right
    show naoto_strip at right
    show aiden_undie at center
    show aiden_blush2 at center
    show aiden laugh3 at center
    show yoshi_autumn at left
    show yoshi_blush2 at left
    show yoshi panic3 at left
    with move

    voice audio.aiden_v_drunk2c1
    a "Hahaha! They really want a piece of me, don’t they~?"

    show naoto happy1 at right
    voice audio.naoto_v_agree3a
    nas "Heck yeah!  A face like yours with a hunky body, anybody would want a taste!"

    show aiden drunk2 at center
    voice audio.aiden_v_bro2a
    a "You’re quite jacked too, bro! Hold on… You look real familiar…"

    show naoto gentle2 at right
    voice audio.naoto_v_laugh2a
    nas "Hehe, do I? Why don’t you come with me and get to know me better?"

    show yoshi_autumn at center
    show yoshi shock3 at center
    show yoshi_blush2 at center
    show aiden_undie at left
    show aiden drunk2 at left
    show aiden_blush2 at left
    with move

    voice audio.yoshi_v_wait3a
    yo "W-Wait, he’s not what you think…!"

    show naoto confused2 at right
    voice audio.naoto_v_surprised1c
    nas "Oh, are you his pimp? "

    show yoshi awkward3 at center
    voice audio.yoshi_v_no5
    yo "N-No, not at all…!"

    show naoto gentle3 at right
    voice audio.naoto_v_agree1c1
    nas "It’s a threesome then! Take your clothes off and let’s go put on a great show~!"

    show yoshi worry5 at center
    voice audio.yoshi_v_confident3
    yo "You don’t understand, we’re here as guests…! And I need to take Aiden with me."

    show naoto talk1 at right
    voice audio.naoto_v_surprised1a1
    nas "Oh, my bad! I didn’t realize you two were exclusive."

    show naoto tease2 at right
    voice audio.naoto_v_laugh2b
    nas "Hehe, funny how I’d find that out in a place like this!"

    hide yoshi_autumn
    hide yoshi worry5
    hide yoshi_blush2
    show yoshi2_autumn at center
    show yoshi2 confused2 at center
    show yoshi2_blush2 at center
    voice audio.yoshi_v_huh1
    yo "Huh? Do we know you…?"

    show naoto tease3 at right
    voice audio.naoto_v_thinking2b
    nas "Maybe? Maybe not?"

    hide yoshi2_autumn
    hide yoshi2 confused2
    hide yoshi2_blush2
    show yoshi_autumn at center
    show yoshi awkward3 at center
    show yoshi_blush2 at center
    voice audio.yoshi_v_anyway4a
    yo "A-Anyways, can you help us get one of those private booths?"

    show naoto happy1 at right
    voice audio.naoto_v_response3a
    nas "Sure, it’s right over there in the corner~"

    show yoshi comp2 at center
    voice audio.yoshi_v_thanks4
    yo "Ah, thanks! It’s just what we need! "

    show naoto gentle2 at right
    voice audio.naoto_v_relief1b
    nas "If you guys are looking to find some triple action to spice things up, you know where to find me~!"

    hide yoshi_autumn
    hide yoshi comp2
    hide yoshi_blush2
    show yoshi2_autumn at center
    show yoshi2 comp5 at center
    show yoshi2_blush2 at center
    voice audio.yoshi_v_right3
    yo "Right… We’ll be on our way!"

    hide yoshi2_autumn
    hide yoshi2 comp5
    hide yoshi2_blush2
    hide aiden_undie
    hide aiden drunk2
    hide aiden_blush2
    with moveoutleft

    show naoto_club at center
    show naoto_strip at center
    show naoto gentle2 at center
    with move

    show naoto laugh1 at center
    voice audio.naoto_v_laugh2b
    nas "Hehe, maybe in another timeline. "

    show justin_bar at p5_5
    show justin_glasses at p5_5
    show justin talk1 at p5_5
    with dissolve

    voice audio.justin_v_naoto1a
    ju "Hey, Naoto! You got a client asking for a bro job!"

    show naoto happy1 at center
    voice audio.naoto_v_agree1b
    na "That’s my cue!"

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

    $ location = location_hotelclub
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_hotel_bar_vip with fade
    play bgsound sfxloop_nightclub loop
    play music on_the_edge_club loop

    show yoshi2_autumn at left2
    show yoshi2 annoy1 at left2
    show aiden_undie at right2
    show aiden drunk2 at right2
    voice audio.aiden_v_laugh1d1
    a "Hehehehe… Did you see how much… they cheered for me out there…?"

    show yoshi2 sigh4 at left2
    voice audio.yoshi_v_sigh3a
    yo "*sigh* Of course, Aiden… You gave them quite the show, they got to see you naked…"

    show aiden drunk5 at right2
    voice audio.aiden_v_perv1
    a "They get to look but you get to touch~"

    show aiden_undie at center
    show aiden awkward2 at center
    with move
    show yoshi2 awkward2 at left2
    voice audio.yoshi_v_hey3
    yo "H-Hey, Aiden… Not here… This booth isn’t exactly private…"

    show aiden drunk3 at center
    voice audio.aiden_v_glad1a
    a "Good. Just how I like it."

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    show yoshi2 at left2
    voice audio.yoshi_v_rush3
    yo "Come on, Aiden… Let’s get you dressed before—"

    jump day3_aiden_2

label day3_aiden_aftersx:
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

    $ location = location_hotelclub
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_hotel_bar_vip with fade
    play bgsound sfxloop_nightclub loop
    play music on_the_edge_club loop

    show yoshi_sleep2 at left2
    show yoshi awkward4 at left2
    show aiden_naked at right2
    show aiden sleepy3 at right2
    voice audio.yoshi_v_ah2
    yo "Ahh… We made a mess, Aiden… We should—"

    show aiden sleepy4 at right2
    voice audio.aiden_v_sleep1
    a "ZzzzzzZZ… Zzzzzz…"

    show yoshi comp1 at left2
    yo "..."

    show yoshi comp6 at left2
    voice audio.yoshi_v_alright1
    yo "Alright, Aiden… Let’s get you back to our room…"

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black with fade
    yo "{i}(I hurriedly cleaned us both up before anyone outside of our booth noticed, and then quickly put Aiden's clothes back on him.){/i}"
    yo "{i}(Putting Aiden on my back, we both left the booth to cross through the club.){/i}"

    scene cg black
    hide screen location
    hide screen timeline
    hide screen quick_menu
    $quick_menu = False
    with fade
    play sound sfx_clotheschanging
    $ renpy.pause (2.0, hard=True)

    $ location = location_hotelclub
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_hotel_bar_night with fade
    play bgsound sfxloop_nightclub loop
    play music on_the_edge_club loop

    show aiden_shirtless at p5_1
    show aiden sleepy3 at p5_1
    show yoshi_autumn at p5_2
    show yoshi tired4 at p5_2
    show justin_bar at p5_5
    show justin_glasses at p5_5
    show justin tease1 at p5_5
    voice audio.yoshi_v_pant1
    yo "*huff* *huff* "

    show justin tease2 at p5_5
    voice audio.justin_v_tease1a
    ju "‘Crazy’ night, huh?"

    show aiden_shirtless at left2
    show aiden sleepy3 at left2
    show yoshi_autumn at center
    show yoshi tired4 at center
    show justin_bar at right
    show justin_glasses at right
    show justin tease2 at right
    with move

    hide yoshi_autumn
    hide yoshi tired4
    show yoshi2_autumn at center
    show yoshi2 shy5 at center
    voice audio.yoshi_v_yeah4
    yo "A-Ahh… Y-Yeah…"

    show justin tease3 at right
    voice audio.justin_v_laugh1
    ju "Bottom’s Up Nightclub is really living up to its name!"

    show yoshi2 shy6 at center
    voice audio.yoshi_v_uh1a
    yo "A-About that, we—"

    show justin play5 at right
    voice audio.justin_v_compassion2a1
    ju "Don’t worry, your secret is safe with me~ *wink*"
    ju "Need me to call for room assistance?"

    hide yoshi2_autumn
    hide yoshi2 shy6
    show yoshi_autumn at center
    show yoshi awkward4 at center
    voice audio.yoshi_v_no4
    yo "N-No… I think I can handle it from here! Thank you for your hospitality!"

    show justin happy3 at right
    voice audio.justin_v_bye1a
    ju "Alright then~! See you again!"

    hide yoshi_autumn
    hide yoshi awkward4
    hide aiden_shirtless
    hide aiden sleepy3
    with dissolve

    show emilia_autumn at p5_1
    show emilia confused1 at p5_1
    with dissolve

    e "..."

    show justin happy1 at right
    voice audio.justin_v_greet3a
    ju "Welcome to Bottom’s Up! What can I get for you?"

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black
    hide screen location
    hide screen timeline
    hide screen quick_menu
    $quick_menu = False
    with fade
    play sound sfx_cardbeep
    $ renpy.pause (1.0, hard=True)

    play sound sfx_dooropen
    $ renpy.pause (1.0, hard=True)

    play sound sfx_doorclose
    $ renpy.pause (1.0, hard=True)

    play sound sfx_bedfluff
    $ renpy.pause (1.0, hard=True)

    $ location = location_room
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_hotel_room1_night with fade

    show yoshi_autumn at left2
    show yoshi sigh4 at left2
    show aiden_shirtless at right2
    show aiden sleepy3 at right2
    voice audio.yoshi_v_relief1
    yo "Haaaah! There we go… "

    show aiden sleepy4 at right2
    voice audio.aiden_v_sleep1
    a "ZzzzZZZ… zzzZZZzz…"

    show yoshi comp1 at left2
    yo "{i}(After everything that happened tonight, now Aiden looks so peaceful… I rarely get to see him like this…){/i}"

    $working = False
    $shuffle_menu()
    menu():
        yo "{i}(After everything that happened tonight, now Aiden looks so peaceful… I rarely get to see him like this…){/i}{fast}"
        "Tuck him in.":
            $working = True
            $score_bot += 1
            show yoshi comp2 at left2
            voice audio.yoshi_v_think1a
            yo "I’ll just tuck you in, Aiden…"

            show yoshi_autumn at center
            show yoshi comp2 at center
            with move

            show aiden relief1 at right2
            voice audio.aiden_v_mmm1a
            a "Mmmnn… "
        "Kiss his forehead.":
            $working = True
            $score_top += 1
            show yoshi comp3 at left2
            yo "*kisses Aiden on the forehead*"

            show yoshi_autumn at center
            show yoshi comp3 at center
            with move

            show aiden relief1 at right2
            voice audio.aiden_v_mmm1a
            a "Mmmnn… "
        "Wipe him down.":
            $working = True
            $score_bot += 2
            show yoshi comp2 at left2
            voice audio.yoshi_v_think1a
            yo "I better clean you up before going to bed…"

            show yoshi_autumn at center
            show yoshi comp2 at center
            with move

            play sound sfx_clotheschanging
            hide aiden_shirtless
            hide aiden sleepy4
            show aiden_undie at right2
            show aiden relief1 at right2
            with dissolve

            voice audio.aiden_v_mmm1a
            a "Mmmnn… Thanks, Yoshi…."
        "Take his clothes off.":
            $working = True
            $score_top += 2
            show yoshi comp2 at left2
            voice audio.yoshi_v_think1a
            yo "I better get these dirty clothes off of you and get you comfortable…"

            show yoshi_autumn at center
            show yoshi comp2 at center
            with move

            play sound sfx_clotheschanging
            hide aiden_shirtless
            hide aiden sleepy4
            show aiden_undie at right2
            show aiden relief1 at right2
            with dissolve

            voice audio.aiden_v_mmm1a
            a "Mmmnn… Thanks, Yoshi…."

    show yoshi comp5 at center
    voice audio.yoshi_v_goodpm5
    yo "Good night, Aiden."

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black
    hide screen location
    hide screen timeline
    hide screen quick_menu
    $quick_menu = False
    with fade
    $ time_transition_night_to_day_winter()
    play sound sleeping_time
    $ renpy.pause (2.0, hard=True)
    jump day4_aiden
