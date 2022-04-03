label day3_goro:
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
    show yoichi worry2 at center
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

    show yuri_winter at p5_1
    show yuri norm1 at p5_1
    show goro_winter at p5_2
    show goro norm1 at p5_2
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

    show aiden happy2 at p4_4
    voice audio.aiden_v_response1a
    a "It’s fine! The shuttle just arrived anyway."

    show yuri upset2 at p4_1
    voice audio.yuri_v_aww1a
    yu "Aww, I’m a little bummed they aren’t coming with us, though. "

    show goro explain3 at p4_2
    voice audio.goro_v_think1a1
    g "They prefer to hang out with their friends – and that’s a good thing."

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
    show jin_winter at p7_7
    show jin_glasses at p7_7
    show jin norm1 at p7_7
    show lloyd_winter at p7_5
    show lloyd happy1 at p7_5
    with dissolve

    hide yuri_winter
    hide yuri norm1
    show yuri_winter at p7_1
    show yuri norm1 at p7_1
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
    show jin_glasses at p5_5
    show jin norm1 at p5_5
    with move

    voice audio.yoshi_v_jin5
    yo "Speaking of sleep, did you get enough rest, Jin?"

    show jin comp6 at p5_5
    voice audio.jin_v_yeah3a
    j "Ah, y-yeah! I’m sorry for passing out on you guys last night…!"

    show goro tease3 at p5_2
    voice audio.goro_v_heh1a
    g "You were sleeping like a baby, so we didn’t want to bother you, hehe."

    show jin comp2 at p5_5
    voice audio.jin_v_laugh1a
    j "It’s the first time this year I’ve had a normal sleep schedule. I’ll try to keep up with it, like I promised…!"

    show yuri angry2 at p5_1
    voice audio.yuri_v_jin2a
    yu "Sleep whenever you like, Jin! Don’t let that Emilia tell you how to live your life!"

    hide goro_winter
    hide goro tease3
    show goro2_winter at p5_2
    show goro2 sigh1 at p5_2
    voice audio.goro_v_yuri5b
    g "*sigh* Yuri..."

    show yuri_winter at p7_3
    show yuri angry2 at p7_3
    show goro2_winter at p7_4
    show goro2 norm3 at p7_4
    show yoshi_winter at p7_5
    show yoshi relief2 at p7_5
    show aiden_winter at p7_6
    show aiden comp6 at p7_6
    show jin_winter at p7_7
    show jin_glasses at p7_7
    show jin comp2 at p7_7
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
    show goro2 norm3 at p5_2
    show yoshi2_winter at p5_3
    show yoshi2 awkward3 at p5_3
    show aiden_winter at p5_4
    show aiden comp6 at p5_4
    show jin_winter at p5_5
    show jin_glasses at p5_5
    show jin comp2 at p5_5
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
    show goro2 norm3 at p5_1
    show yoshi2_winter at p5_2
    show yoshi2 sad1 at p5_2
    show aiden2_winter at p5_3
    show aiden2 upset5 at p5_3
    show jin_winter at p5_4
    show jin_glasses at p5_4
    show jin comp2 at p5_4
    show yuri_winter at p5_5
    show yuri excited2 at p5_5
    with move

    voice audio.yuri_v_conj2a1
    yu "Jin and I already decided we’ll have a nice BL-reading session on the whole ride~!"

    hide jin_winter
    hide jin_glasses
    hide jin comp2
    show jin2_winter at p5_4
    show jin2_glasses at p5_4
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
    hide jin2_glasses
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
    hide lloyd_winter
    hide lloyd amazed4
    show lloyd_winter at p7_2
    show lloyd amazed4 at p7_2
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

    show yoshi shock2 at p7_4
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
    show yuri2 fangirl1 at p7_6
    voice audio.yuri_v_kyaa1a
    yu "Kyaaa! You should show me those pics some time, Jin~! I bet there’s some super sexy ones!"

    hide jin_winter
    hide jin_glasses
    hide jin comp6
    show jin2_winter at p7_7
    show jin2_glasses at p7_7
    show jin2 fudan6 at p7_7
    voice audio.jin_v_gulp1a
    j "*gulp* How did you know…"

    show yoshi comp2 at p7_4
    voice audio.yoshi_v_laugh1
    yo "Haha, everyone seems really overwhelmed with the hotel, and we’re only in the lobby. "

    hide yuri2_winter
    hide yuri2 fudan1
    show yuri_winter at p7_6
    show yuri norm1 at p7_6
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
    show yuri_winter at p8_6
    show yuri annoy1 at p8_6
    show jin2_winter at p8_7
    show jin2_glasses at p8_7
    show jin2 fudan6 at p8_7
    with move

    show emilia_winter at p8_8
    show emilia pain4 at p8_8
    with dissolve

    hide darius_winter
    hide darius annoy2
    hide lloyd_winter
    hide lloyd comp2
    show darius_winter at p8_2
    show darius annoy2 at p8_2
    show lloyd_winter at p8_1
    show lloyd comp2 at p8_1
    voice audio.emilia_v_surprised1a
    e "Hnghhh…!! Why in the world is no one helping me with my luggage?!"

    hide jin2_winter
    hide jin2_glasses
    hide jin2 fudan6
    show jin_winter at p8_7
    show jin_glasses at p8_7
    show jin worry1 at p8_7
    show yuri annoy2 at p8_6
    voice audio.yuri_v_aiden4a
    yu "Guess you spoke too soon, Aiden."

    show goro_winter at p8_4
    show goro play2 at p8_4
    show yuri_winter at p8_5
    show yuri annoy2 at p8_5
    show jin_winter at p8_6
    show jin_glasses at p8_6
    show jin worry1 at p8_6
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
    hide jin_glasses
    hide jin worry1
    show jin_winter at p8_6
    show jin_glasses at p8_6
    show jin worry1 at p8_6
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
    show jin_glasses at p9_7
    show jin worry4 at p9_7
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
    hide jin_winter
    hide jin_glasses
    hide jin worry4
    show jin_winter at p9_7
    show jin_glasses at p9_7
    show jin worry4 at p9_7
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

    show emilia angry1 at p9_9
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
    show jin_glasses at p8_6
    show jin worry4 at p8_6
    show yoshi_winter at p8_7
    show yoshi shock2 at p8_7
    show emilia_winter at p8_8
    show emilia angry1 at p8_8
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
    show goro2 explain2 at p8_4
    voice audio.goro_v_conj7a
    g "If that’s the case, then I suppose I’ll share a room with you, Yoshinori. "

    show yoshi happy1 at p8_7
    voice audio.yoshi_v_agree1b1
    yo "Oh! Of course, sir!"

    show aiden2 pout5 at p8_3
    voice audio.aiden_v_aww1a
    a "Aww, dammit! You beat me to it, Gramps!"

    show aiden2 worry2 at p8_3
    voice audio.aiden_v_think2a
    a "Does that leave me sharing rooms with you-know-who…?"

    hide yuri2_winter
    hide yuri2 drool2
    show yuri_winter at p8_5
    show yuri annoy1 at p8_5
    show emilia annoy2 at p8_8
    voice audio.emilia_v_hmph1a
    e "Hmph, bold of you to assume I want to share a room with the likes of you! "

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
    show darius play1 at p7_1
    show lloyd_winter at p7_2
    show lloyd tease2 at p7_2
    show aiden2_winter at p7_3
    show aiden2 awkward5 at p7_3
    show goro2_winter at p7_4
    show goro2 bored1 at p7_4
    show yuri_winter at p7_5
    show yuri angry3 at p7_5
    show jin_winter at p7_6
    show jin_glasses at p7_6
    show jin comp2 at p7_6
    show yoshi_winter at p7_7
    show yoshi shock2 at p7_7
    with move

    voice audio.yuri_v_what5a
    yu "What a hog! She gets a room all to herself?! "

    hide yoshi_winter
    hide yoshi shock2
    show yoshi2_winter at p7_7
    show yoshi2 awkward3 at p7_7
    hide jin_winter
    hide jin_glasses
    hide jin comp2
    show jin_winter at p7_6
    show jin_glasses at p7_6
    show jin comp2 at p7_6
    voice audio.yoshi_v_uh1a
    yo "That might be for the best. I don’t think any of us would want to share a room with her in the first place."

    show yuri think2 at p7_5
    voice audio.yuri_v_think1a1
    yu "Fair point. "

    show lloyd happy2 at p7_2
    voice audio.lloyd_v_conj1a3
    l "Well, we don’t mind sharing a room with Aiden. Right, Dar?"

    show darius tease4 at p7_1
    voice audio.darius_v_comp3a
    d "I’m okay with a three-way."

    hide jin_winter
    hide jin_glasses
    hide jin comp2
    show jin2_winter at p7_6
    show jin2_glasses at p7_6
    show jin2 dizzy2 at p7_6
    voice audio.jin_v_wah1b
    j "*gulp* W-Wahhh…"

    hide yuri_winter
    hide yuri angry3
    show yuri2_winter at p7_5
    show yuri2 jizz1 at p7_5
    voice audio.yuri_v_fujo3a
    yu "*splutters* WHAT?! "

    show lloyd tease3 at p7_2
    voice audio.lloyd_v_laugh1a2
    l "Besides, Aiden knows how to have a good time~!"

    show jin2 scheme2 at p7_6
    voice audio.jin_v_laugh4a
    j "I’m reconsidering my decision…"

    hide aiden2_winter
    hide aiden2 awkward5
    show aiden_winter at p7_3
    show aiden tease2 at p7_3
    voice audio.aiden_v_perv1
    a "Well, the room can fit one more~ Think you can handle three guys at the same time, Jin?"

    show jin2 perv5 at p7_6
    voice audio.jin_v_yes6c
    j "Okay, you’re in – I-I mean, I’m in."
    j "Goodbye, Yuri."

    show yuri2 jizz2 at p7_5
    voice audio.yuri_v_wait1e1
    yu "WAIT, NO! Let me come with you guys!!!"
    yu "Screw the other room! I’ll sleep on the floor! You won’t even know I’m there!"

    show goro2 angry4 at p7_4
    voice audio.goro_v_scold2a1
    g "No, Yuri. To your room. NOW."

    show yuri2 fangirl3 at p7_5
    voice audio.yuri_v_angry1a1
    yu "DO I LOOK LIKE I CARE?! There’s no way I’ll miss all of the action!!"

    show aiden comp2 at p7_3
    voice audio.aiden_v_goro3a
    a "Haha, didn’t work this time, Gramps."

    show yuri2 fangirl1 at p7_5
    voice audio.yuri_v_kyaa1a
    yu "This is gonna be the smuttiest orgy I’ll ever have the chance to witness in my puny, trash existence!"

    show jin2 daydream4 at p7_6
    voice audio.jin_v_laugh2b
    j "Heehheehhe… And me, their willing subject…"

    show lloyd shock2 at p7_2
    voice audio.lloyd_v_wait1c1
    l "Wait, what?"

    show darius laugh3 at p7_1
    voice audio.darius_v_laugh2a
    d "*chuckles*"

    show yoshi2 comp6 at p7_7
    voice audio.yoshi_v_awkward2
    yo "Maybe it’s a bad idea if Yuri and Jin stay with you guys…? They’ll pass out way too often…"

    show goro2 sigh1 at p7_4
    voice audio.goro_v_sigh1b
    g "*sigh* If that’s the case…"

    hide goro2_winter
    hide goro2 sigh1
    show goro_winter at p7_4
    show goro angry3 at p7_4
    voice audio.goro_v_jin1a
    g "Hyunjin!"

    show jin2 fudan2 at p7_6
    voice audio.jin_v_hngh2b
    j "Hngh!"

    hide goro_winter
    hide goro angry3
    show goro2_winter at p7_4
    show goro2 disappoint3 at p7_4
    voice audio.goro_v_request1a2
    g "Escort Yuri to her room. Stay with her and keep her out of trouble. No objections."

    show jin2 fudan3 at p7_6
    voice audio.jin_v_daddy2b
    j "Y-Yes, Daddy! I mean… Sir Goro!"

    show yuri2 scared2 at p7_5
    voice audio.yuri_v_no1c1
    yu "NOOOOOOOoooooooo!!!"

    show jin2_winter at p7_5
    show jin2_glasses at p7_5
    show jin2 fudan3 at p7_5
    with move

    hide jin2_winter
    hide jin2_glasses
    hide jin2 fudan3
    hide yuri2_winter
    hide yuri2 scared2
    with moveoutright

    show aiden excited3 at p7_3
    voice audio.aiden_v_shock1d1
    a "Ooh, clever using some powerplay, Gramps~"

    show goro2 annoy2 at p7_4
    voice audio.goro_v_aiden5a
    g "They wouldn’t get so worked up if you hadn’t pushed their buttons, Aiden."

    show darius tease2 at p7_1
    voice audio.darius_v_laugh2a
    d "Hehe. Aiden always adds fuel to the fire."

    show aiden bold5 at p7_3
    voice audio.aiden_v_atyourservice1
    a "I do what I do best."

    show lloyd talk2 at p7_2
    voice audio.lloyd_v_rush1a1
    l "Come on, guys! Quit the chit-chat and let’s check out what our room looks like!"

    show aiden bold2 at p7_3
    voice audio.aiden_v_alright1a1
    a "Right behind ’ya!"

    hide aiden_winter
    hide aiden bold2
    hide lloyd_winter
    hide lloyd talk2
    hide darius_winter
    hide darius tease2
    with dissolve

    show goro2_winter at left2
    show goro2 annoy2 at left2
    show yoshi2_winter at right2
    show yoshi2 comp5 at right2
    with move

    hide yoshi2_winter
    hide yoshi2 comp5
    show yoshi_winter at right2
    show yoshi comp5 at right2
    voice audio.yoshi_v_well1
    yo "Well, I’m glad Yuri’s back to normal at least."

    hide goro2_winter
    hide goro2 annoy2
    show goro_winter at left2
    show goro sigh1 at left2
    voice audio.goro_v_yeah1b2
    g "Yeah. I’d rather her act like this than be stressed about Emilia."

    show yoshi think2 at right2
    voice audio.yoshi_v_actually1a
    yo "I actually thought you’d be bunking with Yuri though, sir. Since she’s your daughter after all."

    hide goro_winter
    hide goro sigh1
    show goro2_winter at left2
    show goro2 annoy3 at left2
    voice audio.goro_v_rush2b1
    g "Oh, come on, don’t use the father card on me… "
    g "And don’t pretend like you wouldn’t be jealous if I didn’t stay with you."

    hide yoshi_winter
    hide yoshi think2
    show yoshi2_winter at right2
    show yoshi2 shy5 at right2
    voice audio.yoshi_v_ah2
    yo "A-Ah… Well…"

    show goro2 disappoint2 at left2
    voice audio.goro_v_ehem1a
    g "*ehem* Anyway, let’s head to our room."

    hide yoshi2_winter
    hide yoshi2 shy5
    show yoshi_winter at right2
    show yoshi talk3 at right2
    voice audio.yoshi_v_yessir1
    yo "Yes, sir…!"

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
    play music old_familiar_home loop

    show yoshi_winter at left2
    show yoshi shock2 at left2
    show goro_winter at right2
    show goro shock1 at right2
    voice audio.yoshi_v_shock1b
    yo "Whoa… "

    show goro shock2 at right2
    voice audio.goro_v_unsure3a1
    g "I guess I shouldn’t be surprised, but the room is luxurious too."
    g "Just look at that view, it’s like we’re in the sky."

    hide goro_winter
    hide goro shock2
    show goro2_winter at right2
    show goro2 grin5 at right2
    voice audio.goro_v_heh1a
    g "Heh… Booking us a penthouse room in the most expensive hotel in the city. Mr. Clermont really went overboard with this one."
    g "I bet the facilities included in our package will be just as extravagant.  I can’t wait to try them with you."

    show yoshi shy2 at left2
    yo "..."

    show goro2 confused2 at right2
    voice audio.goro_v_yoshi6
    g "What’s with that look, Yoshinori?"

    hide yoshi_winter
    hide yoshi shy2
    show yoshi2_winter at left2
    show yoshi2 awkward4 at left2
    voice audio.yoshi_v_sorry2b
    yo "O-Oh, I’m sorry, sir! I totally spaced out… I just realized that—"

    $ working = False
    $ shuffle_menu()
    menu():
        yo "O-Oh, I’m sorry, sir! I totally spaced out… I just realized that—{fast}"
        "All of this is new to me.":
            $ working = True
            $ score_goro -= 1
            $ score_top += 1
            show yoshi2 sigh1 at left2
            voice audio.yoshi_v_sigh3a
            yo "All of this is actually new to me. I’m so out of my element. "
            yo "I’ve gotten used to being surrounded by trees and staying in wooden cabins all the time."

            show yoshi2 awkward3 at left2
            voice audio.yoshi_v_think3
            yo "Compared to Camp Buddy, this is a completely different world."

            show goro2 play3 at right2
            voice audio.goro_v_heh1a
            g "Heh… You’ve always been the country kind of guy, Yoshinori. It’s about time you get a taste of city life."
            g "On that note, why don’t we go out and try something already? I’ve got this hotel brochure from earlier, so let’s take a look."
        "I'm on a vacation with my boss.":
            $ working = True
            $ score_goro -= 1
            $ score_bot += 1
            show yoshi2 sigh1 at left2
            voice audio.yoshi_v_sigh3a
            yo "I’m on a vacation with my boss…"

            show goro2 explain2 at right2
            voice audio.goro_v_confused2a1
            g "I don’t see the issue here."
            g "More importantly, just relax around me. We’re not here for work."

            hide goro2_winter
            hide goro2 explain2
            show goro_winter at right2
            show goro talk1 at right2
            voice audio.goro_v_conj9a1
            g "That’s all you’ve been focusing on the past few months, and you deserve a break."

            show yoshi2 awkward3 at left2
            voice audio.yoshi_v_unsure3a
            yo "I guess…"

            show goro happy2 at right2
            voice audio.goro_v_well1a
            g "Well, let’s get started doing something to get work off your mind! Check out this hotel brochure I got."
        "I don't even know where to start.":
            $ working = True
            $ score_goro += 1
            $ score_top += 1
            show yoshi2 sigh1 at left2
            voice audio.yoshi_v_sigh3a
            yo "I-I don’t even know where to start."
            yo "It sounds like there’ll be so many new things to try out here…!"

            hide goro2_winter
            hide goro2 explain2
            show goro_winter at right2
            show goro laugh1 at right2
            voice audio.goro_v_laugh1a1
            g "Hahaha!  You’ve always been the country kind of guy, Yoshinori. It’ll really be interesting to see you get a taste of city life."

            show yoshi2 comp6 at left2
            voice audio.yoshi_v_laugh5a
            yo "Ahehe… Compared to Camp Buddy, this is a completely different world."

            hide goro_winter
            hide goro laugh1
            show goro2_winter at right2
            show goro2 play2 at right2
            voice audio.goro_v_agree5a1
            g "Which makes it more exciting don’t you think?"

            hide yoshi2_winter
            hide yoshi2 comp6
            show yoshi_winter at left2
            show yoshi happy2 at left2
            voice audio.yoshi_v_yeah2
            yo "Y-Yeah! Although, I’m totally clueless about what kind of activities there are here…"

            hide goro2_winter
            hide goro2 play2
            show goro_winter at right2
            show goro happy2 at right2
            voice audio.goro_v_well1a
            g "Well, why don’t we go and try something out? Take a look at this brochure."
        "There's only one bed...":
            $ working = True
            $ score_goro += 1
            $ score_bot += 1
            show yoshi2 sigh1 at left2
            voice audio.yoshi_v_sigh3a
            yo "There’s only one bed…"

            hide goro2_winter
            hide goro2 explain2
            show goro_winter at right2
            show goro talk3 at right2
            voice audio.goro_v_oh1a
            g "Oh. I didn’t even notice that."
            g "But don’t worry, I’m pretty sure we’ll fit together."

            show yoshi2 awkward3 at left2
            voice audio.yoshi_v_ah2
            yo "Ah, well… That’s exactly it…"

            hide goro_winter
            hide goro talk3
            show goro2_winter at right2
            show goro2 tease2 at right2
            voice audio.goro_v_oh4b
            g "Sounds to me like you’re imagining something else! Can’t wait til’ the evening?"

            hide yoshi2_winter
            hide yoshi2 awkward3
            show yoshi_winter at left2
            show yoshi shock3 at left2
            voice audio.yoshi_v_shock3
            yo "G-GAH—"

            hide goro2_winter
            hide goro2 tease2
            show goro_winter at right2
            show goro laugh2 at right2
            voice audio.goro_v_laugh2d1
            g "HAHAHA! We’ve been staying in the same cabin for months now, Yoshinori! This isn’t that new!"

            show yoshi shock2 at left2
            voice audio.yoshi_v_but1
            yo "B-But not in the same bed, sir…!"

            show goro happy2 at right2
            voice audio.goro_v_well1a
            g "Save it for later, and check out this hotel brochure I got."

    #minimap mode
    $dayg3_choice = False
    $day3_goro = True
    $renpy.choice_for_skipping()
    scene mm_goro_final with fade
    voice audio.yoshi_v_shock1b
    yo "Whoa… This place really has everything… You could live like royalty for the rest of your life if you had the money to stay here…"

    voice audio.goro_v_amazed1a2
    g "And all of this is free. It’s all part of the package Mr. Clermont got for us."

    voice audio.yoshi_v_amazed1d
    yo "There’s a bar, café, gym, and so much more… I can’t even pick… "

    voice audio.goro_v_comp2a2
    g "Don’t worry, Yoshinori. There’s plenty of time for us to try everything out. "

    voice audio.goro_v_confident1a
    g "For now, leave it to me. I know exactly where we should go."

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

    $ location = location_hotelspa
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_hotel_spa_day with fade
    play music close_distance loop
    play bgsound sfxloop_waterflow loop

    show goro_towel at left2
    show goro relief2 at left2
    show yoshi_towel at right2
    show yoshi relief1 at right2
    voice audio.goro_v_ah1c
    g "Ahhh… This is the life…"

    show yoshi relief2 at right2
    voice audio.yoshi_v_relief1
    yo "Whew… It’s really nice here, sir."

    show goro happy2 at left2
    voice audio.goro_v_glad1a
    g "I figured you’d enjoy it, especially after that long bus ride."

    hide yoshi_towel
    hide yoshi relief2
    show yoshi2_towel at right2
    show yoshi2 comp2 at right2
    voice audio.yoshi_v_yeah1
    yo "Yeah… I can’t remember the last time I took an actual bath… We only have showers back at the camp, after all."

    hide goro_towel
    hide goro happy2
    show goro2_towel at left2
    show goro2 grin5 at left2
    voice audio.goro_v_agree4a1
    g "Exactly. I’m calling it already – this will be my favorite part of the day."

    hide yoshi2_towel
    hide yoshi2 comp2
    show yoshi_towel at right2
    show yoshi comp3 at right2
    voice audio.yoshi_v_sirgoro15
    yo "It’s been a while since I’ve seen you smile that wide, Sir Goro."

    hide goro2_towel
    hide goro2 grin5
    show goro_towel at left2
    show goro relief4 at left2
    voice audio.goro_v_heh1a
    g "I can’t help it. You know how I love going to places like this."

    show yoshi laugh1 at right2
    voice audio.yoshi_v_laugh1
    yo "Haha, yeah! I remember that you’d make it a point to go to the local sauna once a week when I was a scout."

    hide goro_towel
    hide goro relief4
    show goro2_towel at left2
    show goro2 explain2 at left2
    voice audio.goro_v_think1a1
    g "I still do, but between the last term and this project, there’s not really been any chance."
    g "It’s how I usually release all the stress and soreness from working the entire week. I’m not getting any younger after all."

    hide goro2_towel
    hide goro2 explain2
    show goro_towel at left2
    show goro talk3 at left2
    voice audio.goro_v_conj5a
    g "Besides, I only go to public bathhouses or small massage places. They’re nothing compared to this one."

    hide goro_towel
    hide goro talk3
    show goro2_towel at left2
    show goro2 grin5 at left2
    voice audio.goro_v_heh1a
    g "Heh, in here, I feel like I’m a king in his royal chambers!"
    g "I mean… Just look at this place, what other bathhouses have you seen with waiters going around delivering you drinks?"

    hide yoshi_towel
    hide yoshi laugh1
    show yoshi2_towel at right2
    show yoshi2 think2 at right2
    voice audio.yoshi_v_yeah1
    yo "Yeah, even the water feels expensive… It’s kinda sparkly and it smells like flowers…"
    yo "Not to mention it’s really spacious, even considering how many guests are in here."

    hide goro2_towel
    hide goro2 grin5
    show goro_towel at left2
    show goro confused2 at left2
    voice audio.goro_v_confused1a1
    g "Speaking of space, why are you sitting so far over there?"
    g "Scoot a little closer, will you?"

    show yoshi2 shy5 at right2
    voice audio.yoshi_v_yessir3
    yo "A-Ah…! Yes, sir…!"

    show goro_towel at left3
    show goro play2 at left3
    show yoshi2_towel at right3
    show yoshi2 shy5 at right3
    with move

    voice audio.goro_v_agree6a2
    g "That’s more like it."

    show yoshi2 shy3 at right3
    voice audio.yoshi_v_gulp1a
    yo "*gulp*"

    show goro relief2 at left3
    voice audio.goro_v_actually1b
    g "You know, this is exactly what I was looking forward to as soon as I found out we were going on a vacation."
    g "After grinding for months, wearing our bodies out day and night, we really deserve this."

    show yoshi2 shy4 at right3
    yo "..."

    show goro relief5 at left3
    voice audio.goro_v_relief1a
    g "Just the two of us, relaxing… without a single care in the world…"

    show yoshi2 awkward1 at right3
    yo "{i}(I’m barely hearing Sir Goro’s words… Being so close to him is too distracting!){/i}"

    show goro confused2 at left3
    voice audio.goro_v_yoshi6
    g "Yoshinori?"

    show yoshi2 scared1 at right3
    yo "{i}(The fact we’re in this kind of setting isn’t helping either… I can’t keep my eyes off of his—){/i}"

    hide goro_towel
    hide goro confused2
    show goro2_towel at left3
    show goro2 angry3 at left3
    voice audio.goro_v_yoshi12a
    g "YOSHINORI."

    hide yoshi2_towel
    hide yoshi2 scared1
    show yoshi_towel at right3
    show yoshi scared2 at right3
    voice audio.yoshi_v_shock4
    yo "G-GAH…! Wh-Wha?!" with vpunch

    show goro2 confused5 at left3
    voice audio.goro_v_worry2a
    g "Why are you so jittery? Your back’s hunched and your muscles are all tensed up."
    g "And you aren’t listening to what I’m saying, are you?"

    hide yoshi_towel
    hide yoshi scared2
    show yoshi2_towel at right3
    show yoshi2 panic2 at right3
    voice audio.yoshi_v_sorry2c
    yo "I-I’m sorry, sir!"

    hide goro2_towel
    hide goro2 confused5
    show goro_towel at left3
    show goro sigh1 at left3
    voice audio.goro_v_sigh1b
    g "*sigh* You don’t have to be so polite.  We’re not at camp anymore."

    show yoshi2 awkward3 at right3
    voice audio.yoshi_v_ah2
    yo "A-Ah… I didn’t mean to."

    show goro worry2 at left3
    voice audio.goro_v_well1a
    g "I just want you to be as comfortable around me as you were back then."

    show yoshi2 confused3 at right3
    voice audio.yoshi_v_awkward2
    yo "Like… when I was a scout?"

    show goro sigh4 at left3
    voice audio.goro_v_yeah1c1
    g "Yeah. Our dynamic was still the same, with me being your superior, but you still managed to always be your carefree self."

    show yoshi2 shy5 at right3
    voice audio.yoshi_v_sir4
    yo "Th-That was a long time ago, sir…"

    hide goro_towel
    hide goro sigh4
    show goro2_towel at left3
    show goro2 shy6 at left3
    voice audio.goro_v_but2a
    g "Things have changed since then, I know. But I really do miss it."

    show goro2_towel at center
    show goro2 norm3 at center
    show yoshi2_towel at right
    show yoshi2 shock1 at right
    with move

    show reimond_masseur at left
    show reimond happy1 at left
    with dissolve

    voice audio.reimond_v_greet1a3
    m "Good day, fine gentlemen~! Enjoying your time here at Spa Ankhme~?"
    m "I hope I’m not interrupting an intimate moment, but may I interest you in some drinks?"

    hide goro2_towel
    hide goro2 norm3
    show goro_towel at center
    show goro talk2 at center
    voice audio.goro_v_no1a1
    g "No, we’re good. "

    show reimond confused2 at left
    voice audio.reimond_v_question2a1
    m "How about a massage? We take pride in our quality ‘extra service’ with guaranteed ‘happy endings!’"

    show goro explain1 at center
    voice audio.goro_v_response3a1
    g "It’s fine. We prefer to relax by ourselves."

    show reimond happy2 at left
    voice audio.reimond_v_ah1a
    m "Oh, we have just the perfect thing! May I offer a private sauna room to such a lovely couple~?"

    $ working = False
    $ shuffle_menu()
    menu():
        m "Oh, we have just the perfect thing! May I offer a private sauna room to such a lovely couple~?{fast}"
        "We're not.":
            $ working = True
            $ score_goro -= 2
            $ deny_goro = True
            show goro shock1 at center
            hide yoshi2_towel
            hide yoshi2 shock1
            show yoshi_towel at right
            show yoshi panic4 at right
            voice audio.yoshi_v_no5
            yo "A-Ah! Please don’t get the wrong idea, we’re just co-workers…!"

            show reimond think2 at left
            voice audio.reimond_v_oh1a
            m "Oh, I apologize for my assumption."
        "He's my boss.":
            $ working = True
            $ score_goro -= 1
            $ deny_goro = True
            show goro shock1 at center
            hide yoshi2_towel
            hide yoshi2 shock1
            show yoshi_towel at right
            show yoshi panic4 at right
            voice audio.yoshi_v_no5
            yo "A-Ah! Please don’t get the wrong idea, he’s my boss…!"

            show reimond think2 at left
            voice audio.reimond_v_oh1a
            m "Oh, my apologies. It really looked like something else."
        "It's not up to me.":
            $ working = True
            $ score_goro += 1
            $ deny_goro = False
            show goro shock1 at center
            hide yoshi2_towel
            hide yoshi2 shock1
            show yoshi_towel at right
            show yoshi think2 at right
            voice audio.yoshi_v_well3
            yo "W-Well… it’s not up to me."
        "Sir Goro.":
            $ working = True
            $ score_goro += 2
            $ deny_goro = False
            show goro shock1 at center
            hide yoshi2_towel
            hide yoshi2 shock1
            show yoshi_towel at right
            show yoshi think2 at right
            voice audio.yoshi_v_well3
            yo "Uhh… Sir Goro?"

    hide goro_towel
    hide goro shock1
    show goro2_towel at center
    show goro2 explain2 at center
    voice audio.goro_v_alright1a1
    g "We’ll take the room."

    show reimond relief3 at left
    voice audio.reimond_v_rush1a1
    m "It should be right along the hallway! Please follow m—"

    hide goro2_towel
    hide goro2 explain2
    show goro_towel at center
    show goro talk1 at center
    voice audio.goro_v_dismiss3a
    g "Thanks, but there’s no need to escort us."

    play sound sfx_splash
    show cg_fade at truecenter
    show fxg3 at fx_pos
    with dissolve

    yo "...!!!"

    voice audio.goro_vsg10_line1
    g "Come with me, Yoshinori. "

    voice audio.yoshi_vsg10_line1
    yo "S-Sir Goro…! Y-You’re…"

    voice audio.goro_vsg10_line2
    g "Take it and let’s get you loosened up."

    hide cg_fade
    hide fxg3 with dissolve

    show reimond play5 at left
    voice audio.reimond_v_request1d1
    m "Have a wonderful time, you two~"

    hide yoshi_towel
    hide yoshi panic4
    hide yoshi think2
    hide goro_towel
    hide goro talk1
    with dissolve

    show naoto_towel at right
    show naoto happy1 at right
    with dissolve

    voice audio.naoto_v_greeting2a
    nag "Hey, there. Can you get me a room too?"

    show naoto_towel at right2
    show naoto happy1 at right2
    show reimond_masseur at left2
    show reimond play2 at left2
    with move

    voice audio.reimond_v_agree4a
    m "Why, of course, handsome guest!"
    m "Would you like a special massage service along with your room?"

    show naoto tease2 at right2
    voice audio.naoto_v_thinking2b
    nag "I wouldn’t mind a masseuse or two… or even three."

    show reimond tease2 at left2
    voice audio.reimond_v_conj1b1
    m "Well, that can be arranged! I can guarantee you a good time~"

    show naoto tease3 at right2
    voice audio.naoto_v_laugh2b
    na "Name’s Naoto. Think you can handle me, bro?"

    show reimond tease3 at left2
    voice audio.reimond_v_teasing1a
    m "Don’t underestimate me, bro~"

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

    $ location = location_hotelsauna
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_hotel_sauna with fade
    play music on_the_edge loop

    show goro_towel at left2
    show goro confused2 at left2
    show yoshi2_towel at right2
    show yoshi2 awkward1 at right2
    voice audio.goro_v_yoshi6
    g "Feeling warm, Yoshinori?"

    show yoshi2 awkward3 at right2
    voice audio.yoshi_v_yessir4
    yo "Y-Yes, sir..."

    show goro relief2 at left2
    voice audio.goro_v_relief1a
    g "Just relax your body and feel the wood on your back… "

    show yoshi2 awkward4 at right2
    voice audio.yoshi_v_alright3
    yo "Alright…"

    show yoshi2 shy3 at right2
    yo "{i}(My chest is pounding thanks to all the dirty thoughts swimming in my head…){/i}"
    yo "{i}(How am I supposed to calm down and relax when Sir Goro’s been nearly naked right beside me since we got here...?!){/i}"

    show yoshi2 shy4 at right2
    yo "{i}(It doesn’t help that I got a peek at that giant thing of his… It makes me want to put it in my…){/i}"

    show goro tease5 at left2
    voice audio.goro_v_heh1a
    g "Feeling thirsty?"

    hide yoshi2_towel
    hide yoshi2 shy4
    show yoshi_towel at right2
    show yoshi awkward2 at right2
    yo "...!!"

    hide goro_towel
    hide goro tease5
    show goro2_towel at left2
    show goro2 play5 at left2
    voice audio.goro_v_well1a
    g "You know you could’ve just asked…"

    hide yoshi_towel
    hide yoshi awkward2
    show yoshi2_towel at right2
    show yoshi2 awkward4 at right2
    voice audio.yoshi_v_what2
    yo "Wh-Wha?"

    show goro2 tease2 at left2
    voice audio.goro_v_rush2a2
    g "You’re always like this when you want something from me…"
    g "If it weren’t for the other people out there at the bath, I would’ve given it to you already."

    show yoshi2 panic4 at right2
    voice audio.yoshi_v_disagree2
    yo "I-I don’t know what you’re talking about sir…!"

    show goro2 tease3 at left2
    voice audio.goro_v_taunt2a
    g "There’s no use denying it. The moment I stood up from the pool, your bulge did the same."

    hide yoshi2 panic4
    hide yoshi2_towel
    show yoshi_towel at right2
    show yoshi panic3 at right2
    voice audio.yoshi_v_shock4
    yo "G-GAH…! S-Sorry, sir!"

    show goro2 play6 at left2
    voice audio.goro_v_heh3a
    g "You think after all these years, I don’t know when you’re in the mood?"

    hide yoshi_towel
    hide yoshi panic3
    show yoshi2_towel at right2
    show yoshi2 pain1 at right2
    voice audio.yoshi_v_groan1b
    yo "Hngh… I couldn’t help it… It’s been in my head since we got here…"

    show goro2 play3 at left2
    voice audio.goro_v_heh1a
    g "Heh... That’s exactly why I brought you here."

    show yoshi2 shock3 at right2
    voice audio.yoshi_v_what2
    yo "Wh-What?! Y-You planned this all along, sir?"

    hide goro2_towel
    hide goro2 play3
    show goro_towel at left2
    show goro relief2 at left2
    voice audio.goro_v_well1a
    g "Well, I would’ve liked to get to this point sooner. But I admit I got a bit carried away with the small talk."
    g "It was entertaining seeing how long you could keep yourself calm~"

    $ working = False
    $ shuffle_menu()
    menu():
        g "It was entertaining seeing how long you could keep yourself calm~{fast}"
        "I thought you were serious.":
            $ working = True
            $ score_goro -= 1
            $ score_top +=1
            show yoshi2 awkward3 at right2
            voice audio.yoshi_v_shock3
            yo "And I thought you were being serious…"

            hide goro_towel
            hide goro relief2
            show goro2_towel at left2
            show goro2 talk4 at left2
            voice audio.goro_v_think1a1
            g "Well, I did mean everything I said."
        "That wasn't funny.":
            $ working = True
            $ score_goro -= 1
            $ score_bot +=1
            show yoshi2 panic2 at right2
            voice audio.yoshi_v_shock3
            yo "Th-That wasn’t funny, Sir Goro…!"

            hide goro_towel
            hide goro relief2
            show goro2_towel at left2
            show goro2 talk1 at left2
            voice audio.goro_v_rush2b1
            g "Come on, lighten up Yoshinori."
        "That's so embarassing.":
            $ working = True
            $ score_goro += 1
            $ score_top +=2
            show yoshi2 panic2 at right2
            voice audio.yoshi_v_shock3
            yo "G-Gah… That’s so embarrassing, Sir Goro…"

            hide goro_towel
            hide goro relief2
            show goro2_towel at left2
            show goro2 play3 at left2
            voice audio.goro_v_laugh1b2
            g "Hehe, that’s the point."
        "That’s so mean.":
            $ working = True
            $ score_goro += 1
            $ score_bot +=2
            show yoshi2 panic2 at right2
            voice audio.yoshi_v_shock3
            yo "G-Gah… That’s so mean, Sir Goro…"

            hide goro_towel
            hide goro relief2
            show goro2_towel at left2
            show goro2 play3 at left2
            voice audio.goro_v_laugh1b2
            g "Well, aren’t you adorable...?"

    show yoshi2 sigh1 at right2
    voice audio.yoshi_v_sigh3a
    yo "*sigh* Since when were you this much of a tease, sir…"

    show goro2 bold2 at left2
    voice audio.goro_v_confident1a
    g "Trust me, this isn’t new. I just save it for special occasions."
    g "Like right now."

    show goro2_towel at center
    show goro2 bold2 at center
    with move

    $sx_g3 = False
    jump day3_goro_2

label day3_goro_aftersx:
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

    $ location = location_hotelspa
    show screen location
    show screen timeline
    $say_box = True
    $quick_menu = True
    show screen quick_menu
    if sx_g3 == True:
        scene bg_hotel_spa_day with fade
        play music here_they_come loop
        show goro_towel at left2
        show goro confused2 at left2
        voice audio.goro_v_alright3a
        g "Yoshinori… Are you alright?"

        show yoshi2_towel at right
        show yoshi2 pain2 at right
        with dissolve

        voice audio.yoshi_v_groan1a
        yo "Nngh… Y-Yeah… It’s just a little hard to walk…"

        show goro_towel at center
        show goro confused2 at center
        with move

        show goro_towel at left3
        show goro grin5 at left3
        show yoshi2_towel at right3
        show yoshi2 pain2 at right3
        with move

        hide goro_towel
        hide goro grin5
        show goro2_towel at left3
        show goro2 grin5 at left3
        voice audio.goro_v_laugh1b2
        g "Hehe… You took it like a champ. Good boy."

        show yoshi2 worry3 at right3
        voice audio.yoshi_v_rush3
        yo "Come on, Sir Goro… Stop teasing me already…"

        hide goro2_towel
        hide goro2 grin5
        show goro_towel at left3
        show goro confused3 at left3
        voice audio.goro_v_think1a1
        g "Maybe a dip back in the bath will help."

        hide yoshi2_towel
        hide yoshi2 worry3
        show yoshi_towel at right3
        show yoshi panic2 at right3
        voice audio.yoshi_v_oops1
        yo "Oh no, no, no, NO."
        yo "That’d be a really bad idea, sir."

        show goro laugh1 at left3
        voice audio.goro_v_laugh1a1
        g "Haha! You think you’ve got the energy left to tour around the hotel?"

        hide yoshi_towel
        hide yoshi panic2
        show yoshi2_towel at right3
        show yoshi2 pain1 at right3
        voice audio.yoshi_v_yeah1
        yo "Yeah, but just give me a sec… I feel like my insides are sinking…"

        hide goro_towel
        hide goro laugh1
        show goro2_towel at left3
        show goro2 play3 at left3
        voice audio.goro_v_rush2a1
        g "Come on, Yoshinori. Don’t act like this is your first time."

        show yoshi2 sigh4 at right3
        voice audio.yoshi_v_well1
        yo "Well, it’s been so long since the last. And honestly, if it weren’t for the heat, I don’t think I’d have been able to take it."

        hide goro2_towel
        hide goro2 play3
        show goro_towel at left3
        show goro relief2 at left3
        voice audio.goro_v_well1a
        g "Well, that’s why I had you in a hot bath and sauna in the first place. "

        hide yoshi2_towel
        hide yoshi2 sigh4
        show yoshi_towel at right3
        show yoshi shock2 at right3
        voice audio.yoshi_v_wait1
        yo "Wait… Was that part of the plan too?"

        hide goro_towel
        hide goro relief2
        show goro2_towel at left3
        show goro2 tease2 at left3
        voice audio.goro_v_agree1a1
        g "Yes. Don’t want you getting hurt down there."

        hide yoshi_towel
        hide yoshi shock2
        show yoshi2_towel at right3
        show yoshi2 sigh1 at right3
        voice audio.yoshi_v_sigh3a
        yo "*sigh* I think I have trust issues now…"

        hide goro2_towel
        hide goro2 tease2
        show goro_towel at left3
        show goro laugh5 at left3
        voice audio.goro_v_laugh2d2
        g "Hahaha!"

        scene cg black with fade
        yo "{i}After letting myself rest a little, Sir Goro and I washed up and headed out to check out the other areas of the hotel.{/i}"

        #minimap mode
        $day3_goro = True
        $dayg3_choice = False
        $renpy.choice_for_skipping()
        show screen minimap()
        $mm_talking = True
        voice audio.goro_v_alright1a1
        g "Alright, Yoshinori. I picked first, so it’s your turn."
        g "Where to next?"

        $say_box = False
        hide screen quick_menu
        $quick_menu = False
        $mm_talking = False
        $ renpy.pause (hard=True)
    else:
        #minimap mode
        $day3_goro = True
        $dayg3_choice = False
        $renpy.choice_for_skipping()
        show screen minimap()
        $mm_talking = True
        voice audio.yoshi_v_relief1
        yo "Whew… We almost got carried away in there."

        voice audio.goro_v_annoyed1a1
        g "I would’ve liked it better if we did."

        voice audio.yoshi_v_uh1a
        yo "M-Maybe next time…"

        voice audio.goro_v_laugh1a1
        g "Haha, there’s still a few days left in the trip after all."

        voice audio.goro_v_anyway1
        g "Anyway, Yoshinori. I picked first, so it’s your turn."
        g "Where to next?"

        $say_box = False
        hide screen quick_menu
        $quick_menu = False
        $mm_talking = False
        $ renpy.pause (hard=True)

label day3_goro_cafe:
    $sq_yuri += 1
    $say_box = True
    $quick_menu = True
    $mm_talking = True
    $g3_cafe = True
    if dayg3_choice == False:
        voice audio.yoshi_v_think1a
        yo "I’m feeling a little hungry after all that… "

        voice audio.goro_v_rush1a1
        g "Let’s head over to the café and grab something to eat then."
    else:
        voice audio.yoshi_v_think1a
        yo "I’m feeling really hungry…"

        voice audio.goro_v_rush1a1
        g "Let’s head over to the café and grab some dinner then."

    voice audio.yoshi_v_alright1
    yo "Alright, sir! "

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

    if dayg3_choice == False:
        $ location = location_hotelcafe
        show screen location
        show screen timeline
        show screen quick_menu
        $quick_menu = True
        scene bg_hotel_cafe_day with fade
        play music old_familiar_home loop
    else:
        $ location = location_hotelcafe
        $ time = timeline_timesunset
        show screen location
        show screen timeline
        show screen quick_menu
        $quick_menu = True
        scene bg_hotel_cafe_sunset with fade
        play music old_familiar_home loop

    show goro_autumn at left2
    show goro shock2 at left2
    show yoshi_autumn at right2
    show yoshi shock1 at right2
    voice audio.goro_v_amazed1a1
    g "As expected… this place is just as amazing. It’s got that same picturesque view as our room."
    g "I guess it lives up to its name as the best hotel around…"

    show yoshi talk3 at right2
    voice audio.yoshi_v_oh1
    yo "Oh, sir! Isn’t that Yuri over there?"

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    show yuri_autumn at p9_9
    show yuri norm1 at p9_9
    with dissolve

    show goro talk4 at left2
    voice audio.goro_v_rush1a1
    g "Let’s see what she’s up to."

    show goro_autumn at left
    show goro happy2 at left
    show yoshi_autumn at center
    show yoshi norm1 at center
    show yuri_autumn at right
    show yuri norm1 at right
    with move
    play music here_they_come loop

    voice audio.goro_v_yuridear1a
    g "Yuri-dear."

    show yuri happy1 at right
    voice audio.yuri_v_greet2a
    yu "Oh, Hi Dad, Yoshi! I haven’t seen you guys since we split up at the lobby!"

    show goro talk3 at left
    voice audio.goro_v_agree2a1
    g "Ah, yes. Yoshinori and I were hanging around earlier and decided to grab a meal."

    show yuri explain3 at right
    voice audio.yuri_v_well1a
    yu "Well, you came to the right place~! Come and sit here with me~"

    show goro_autumn at center
    show goro norm1 at center
    show yoshi_autumn at left
    show yoshi norm1 at left
    with move

    if sx_g3 == True:
        hide yoshi_autumn
        hide yoshi norm1
        show yoshi2_autumn at left
        show yoshi2 pain1 at left
        voice audio.yoshi_v_oww1
        yo "O-Oof…! "

        show yuri worry2 at right
        voice audio.yuri_v_worry2a
        yu "Oh! You okay, Yoshi?"

        show yoshi2 comp3 at left
        voice audio.yoshi_v_comp2
        yo "I just forgot I shouldn’t sit down so quickly…! H-Haha…!"

        hide goro_autumn
        hide goro norm1
        show goro2_autumn at center
        show goro2 play3 at center
        voice audio.goro_v_heh1a
        g "He’s having some cramps in his humps."

        show yuri confused2 at right
        voice audio.yuri_v_oh2a
        yu "Oh…"

        show yuri relief2 at right
        voice audio.yuri_v_anyway1a
        yu "Well, anyways! Isn’t the view here amazing?"
    else:
        show yuri play2 at right
        voice audio.yuri_v_laugh1a1
        yu "Hihi~ Isn’t the view here amazing?"

    show yuri bold2 at right
    voice audio.yuri_v_fujo1a2
    yu "It’s perfect with the delicious dessert, fruity drinks, and all the hardcore smut I can read! "

    hide yoshi2_autumn
    hide yoshi2 comp3
    show yoshi_autumn at left
    show yoshi shy6 at left
    voice audio.yoshi_v_yuri6
    yo "Those are some seriously contradicting things, Yuri. "

    show yuri relief2 at right
    voice audio.yuri_v_laugh1a1
    yu "I’m living the dream! "
    yu "Here, why don’t you check out some of these fanfics I’m reading~! Who knows maybe it’s your cup of tea~?"

    hide yoshi_autumn
    hide yoshi shy6
    show yoshi2_autumn at left
    show yoshi2 confused5 at left
    voice audio.yoshi_v_uh1a
    yo "This one is on… B.D.S.M… What does that even mean?"

    hide goro_autumn
    hide goro norm1
    show goro2_autumn at center
    show goro2 disappoint2 at center
    voice audio.goro_v_ehem1a
    g "*cough* *cough*"

    show yuri serious3 at right
    voice audio.yuri_v_yoshi9a
    yu "My goodness, Yoshi! Shouldn’t you know that at your age?! Just what kind of backwards area do you live in?!"

    show yoshi2 confused2 at left
    voice audio.yoshi_v_awkward1
    yo "Uh… Camp Buddy…?"

    show goro2 explain5 at center
    voice audio.goro_v_well1a
    g "It stands for Bondage and Discipline, Sadism and Masochism, and Submission and Dominance."

    show yoshi2 awkward4 at left
    voice audio.yoshi_v_sir4
    yo "Why do you know this, sir…? "

    show yuri irked1 at right
    voice audio.yuri_v_conj1a2
    yu "That’s common knowledge, you know!"

    show yoshi2 think2 at left
    voice audio.yoshi_v_think1a
    yo "It sounds like a lot, and I feel like I should be concerned…"

    show yuri excited2 at right
    voice audio.yuri_v_laugh1b1
    yu "Well, did any of those spark an interest for you? "

    show yoshi2 sigh4 at left
    voice audio.yoshi_v_sigh3a
    yo "*sigh* Do I really have to choose?"

    show goro2 confused2 at center
    voice audio.goro_v_think1a1
    g "Just hypothetically… Which one would you see yourself subjecting to, Yoshinori?"

    $ working = False
    $ shuffle_menu()
    menu():
        g "Just hypothetically… Which one would you see yourself subjecting to, Yoshinori?{fast}"
        "Dominance.":
            $ working = True
            $ score_goro -= 1
            $ score_top += 1
            show yoshi2 confused5 at left
            voice audio.yoshi_v_unsure3c
            yo "From the options, I guess… dominance? Being in control would be a bit new for me though."

            show yuri comp4 at right
            voice audio.yuri_v_yeah1d1
            yu "Yeaaahh…  I rarely see you take charge, Yoshi."

            show goro2 tease2 at center
            voice audio.goro_v_heh1a
            g "Just leave that to the expert."
        "Sadism and Masochism.":
            $ working = True
            $ score_goro -= 1
            $ score_bot += 1
            show yoshi2 confused5 at left
            voice audio.yoshi_v_unsure3c
            yo "From the options, I guess… sadism and masochism? But that just sounds dark…"

            show yuri bold2 at right
            voice audio.yuri_v_tease1a3
            yu "Ooohh~ I didn’t know you had it in you, Yoshi~"

            show goro2 explain1 at center
            voice audio.goro_v_annoyed1a1
            g "As long as there’s no actual pain involved."
        "Bondage and Discipline.":
            $ working = True
            $ score_goro += 1
            $ score_top += 1
            show yoshi2 confused5 at left
            voice audio.yoshi_v_unsure3c
            yo "From the options, I guess… bondage and discipline? I’m not sure I know what I’m talking about…"

            show yuri bold2 at right
            voice audio.yuri_v_tease1a3
            yu "Ooohh~ I didn’t know you had it in you, Yoshi~"

            show goro2 tease2 at center
            voice audio.goro_v_heh1a
            g "That’s interesting. Notes taken."

            voice audio.yoshi_v_gulp1a
            yo "*gulp*"
        "Submission.":
            $ working = True
            $ score_goro += 1
            $ score_bot += 1
            show yoshi2 confused5 at left
            voice audio.yoshi_v_unsure3c
            yo "From the options, I guess… submission? That’s mostly how I am, right...?"

            show yuri comp4 at right
            voice audio.yuri_v_yeah1d1
            yu "Yeaahhh, that’s what I thought for you too, Yoshi."

            show goro2 tease2 at center
            voice audio.goro_v_heh1a
            g "Just the way it should be."

            voice audio.yoshi_v_gulp1a
            yo "*gulp*"
    show yoshi2 awkward3 at left
    voice audio.yoshi_v_well3
    yo "W-Well, should we really be talking about something like this in a public café...?"

    show yuri angry5 at right
    voice audio.yuri_v_comp1a3
    yu "Psssh, no one cares~! Besides, I don’t ever get a chance to talk about my hobbies to the two of you without getting scolded."

    hide goro2_autumn
    hide goro2 tease2
    hide goro2 explain1
    show goro_autumn at center
    show goro comp2 at center
    voice audio.goro_v_yuri2a
    g "Well, you know I always support your interests, Yuri. As long as you don’t get over-excited about them and faint."

    show yuri excited2 at right
    voice audio.yuri_v_but1b
    yu "But that’s exactly the magic of it – BL itself is such an amazing artform~!"
    yu "With so many different mediums it could be presented in, you can really appreciate the creative process involved in making it!"

    hide yoshi2_autumn
    hide yoshi2 awkward3
    show yoshi_autumn at left
    show yoshi talk3 at left
    voice audio.yoshi_v_right3
    yo "Oh, right… A lot of what you read includes pictures too, right?"

    show yuri bold4 at right
    voice audio.yuri_v_agree1b2
    yu "Yes, I’m into doujinshis more! I really appreciate the ways a small artist or writer can evoke my senses and convey intense emotions!"
    yu "It takes a lot of skill to write a script, let alone visualize it with hand-drawn illustrations!"

    hide yoshi_autumn
    hide yoshi talk3
    show yoshi2_autumn at left
    show yoshi2 think5 at left
    voice audio.yoshi_v_think1a
    yo "When you think about it… that does sound like a lot of work…"

    show yuri bold2 at right
    voice audio.yuri_v_yeah1b1
    yu "Yeah! Some people usually take these things for granted, when in fact the author puts weeks and even months into creating something so amazing."
    yu "Trust me, I’ve tried it myself and it’s just not for me, so I stick to appreciating it instead."

    show goro happy1 at center
    voice audio.goro_v_glad1a
    g "Yuri’s always been the artistic type. It’s why she often leads similar activities with the scouts."

    hide yoshi2_autumn
    hide yoshi2 think5
    show yoshi_autumn at left
    show yoshi talk3 at left
    voice audio.yoshi_v_oh2
    yo "Oh yeah… Everything makes so much more sense now. "

    show yuri explain3 at right
    voice audio.yuri_v_well1a
    yu "Well, BL to me is more than just the art!"
    yu "I find the genre itself so special! Seeing two men allowing themselves to be vulnerable and passionate towards each other, never fails to light a fire in me that words can’t explain!"

    hide goro_autumn
    hide goro happy1
    show goro2_autumn at center
    show goro2 shy5 at center
    show yuri comp2 at right
    voice audio.yuri_v_think1a1
    yu "It’s so wildly different from the idea I had of relationships, especially after what I saw growing up."

    hide yoshi_autumn
    hide yoshi talk3
    show yoshi2_autumn at left
    show yoshi2 awkward3 at left
    voice audio.yoshi_v_but1
    yo "But flipping through these pages… I only see good-looking men… with no clothes… and LOTS of fluids. "

    show yuri play2 at right
    voice audio.yuri_v_laugh2b1
    yu "Well, if we’re talking about the superficial level, then yes! I love me some good porn!"

    show goro2 think6 at center
    voice audio.goro_v_think1a1
    g "Hmm… I guess I can appreciate how much work was put into this… even the way the genitals are drawn are very detailed."

    hide yoshi2_autumn
    hide yoshi2 awkward3
    show yoshi_autumn at left
    show yoshi shock2 at left
    voice audio.yoshi_v_shock3
    yo "G-Gah, Sir Goro…!"

    show yuri amazed3 at right
    voice audio.yuri_v_tease1a1
    yu "Ooh, ooh! I have one here that you’d maybe like, Dad! It’s about two cowboys having raw bareback sex, all while riding a horse towards the sunset!"

    hide yoshi_autumn
    hide yoshi shock2
    show yoshi2_autumn at left
    show yoshi2 pain1 at left
    voice audio.yoshi_v_oww1
    yo "Th-That just sounds painful…"

    hide goro2_autumn
    hide goro2 think6
    show goro_autumn at center
    show goro talk3 at center
    voice audio.goro_v_okay2a
    g "Sure, I’ll give it a read, dear."

    show yuri amazed4 at right
    voice audio.yuri_v_celebrate1a
    yu "Yay! You better tell me what you think about it, promise?!"
    yu "And who knows, maybe you’ll break your decade-long single curse, Dad!"

    hide yoshi2_autumn
    hide yoshi2 pain1
    show yoshi_autumn at left
    show yoshi panic3 at left
    voice audio.yoshi_v_yuri7
    yo "Y-Yuri…!"

    hide goro_autumn
    hide goro talk3
    show goro2_autumn at center
    show goro2 sigh1 at center
    voice audio.goro_v_sigh1b
    g "*sigh*"

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black with fade
    yo "{i}We ended up sitting and talking with Yuri about her fanfics for a long time, all while eating our meal.{/i}"

    if dayg3_choice == False:
        $ dayg3_choice = True
        yo "{i}Before we realized, the sun had already set, and we decided to check out another area of the hotel for the evening! {/i}"

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
        yo "{i}Before we realized, it had gotten late, so we headed back to our room to call it a night. {/i}"

        scene cg black
        hide screen location
        hide screen timeline
        hide screen quick_menu
        $quick_menu = False
        with fade
        $ time_transition_sunset_to_night_winter()
        $ renpy.pause (2.0, hard=True)
        jump day3_goro_after

label day3_goro_gym:
    $quick_menu = True
    $say_box = True
    $mm_talking = True
    $g3_gym = True
    if dayg3_choice == True:
        voice audio.yoshi_v_think4
        yo "Now, that I’m recharged, maybe we should check out the gym, sir?"

        voice audio.goro_v_laugh1b2
        g "Hehe… Are you sure your body can handle it?"

        voice audio.yoshi_v_well1
        yo "Well, I mostly just want to see what’s available!"

        voice audio.goro_v_alright1a1
        g "Alright then, don’t say I didn’t warn you."
    else:
        voice audio.yoshi_v_oh1
        yo "Oh, I want to check the gym out, sir!"

        voice audio.goro_v_okay2a
        g "Sure thing, Yoshinori. We’ll sweat even more before the day’s over, heh."

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

    if dayg3_choice == False:
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
    show goro_autumn at right2
    show goro norm1 at right2
    voice audio.yoshi_v_amazed1a
    yo "Wow… Check out all the fancy equipment they have here!"
    yo "It must be easy to bulk up when you’ve got a place like this!"

    show goro explain3 at right2
    voice audio.goro_v_think1a1
    g "Makes me wish we had our own setup back at camp. We mostly stay in shape with only body workouts and a couple of weights."

    show yoshi happy1 at left2
    voice audio.yoshi_v_well1
    yo "I kinda wanna try some of them!"

    if sx_g3 == True:
        show goro confused2 at right2
        voice audio.goro_v_alright3a
        g "Are you sure you want to push your muscles even further today?"

        hide yoshi_autumn
        hide yoshi happy1
        show yoshi2_autumn at left2
        show yoshi2 comp3 at left2
        voice audio.yoshi_v_comp1
        yo "I-It should be fine, sir! I think… "

        show goro talk3 at right2
        voice audio.goro_v_well1a
        g "Well, just take it easy, alright? What are you planning to work on anyway? "
    else:
        show goro talk3 at right2
        voice audio.goro_v_well1a
        g "Well, what part are you planning to work on?"

    $ working = False
    $ shuffle_menu()
    menu():
        g "Well, what part are you planning to work on?{fast}"
        "Abs.":
            $ working = True
            $ score_top += 1
            hide yoshi2_autumn
            hide yoshi2 comp3
            show yoshi_autumn at left2
            show yoshi bold2 at left2
            voice audio.yoshi_v_think4
            yo "I want to try the crunch machine? It focuses on my abs!"
            yo "I kind of want mine to be as nice as yours, Sir Goro…"

            hide goro_autumn
            hide goro talk3
            show goro2_autumn at right2
            show goro2 play3 at right2
            voice audio.goro_v_heh1a
            g "Heh… I know you like to ogle mine. They’re pretty strong and solid to the touch too."

            show yoshi comp3 at left2
            voice audio.yoshi_v_ah3
            yo "A-Ah, well… I didn’t realize you noticed how often I look at them."

            show goro2 play5 at right2
            voice audio.goro_v_hmph1a
            g "I pay attention."

            show yoshi play2 at left2
            voice audio.yoshi_v_well2
            yo "Well, I figured I should return the favor and distract you too, sir."

            hide goro2_autumn
            hide goro2 play5
            show goro_autumn at right2
            show goro laugh1 at right2
            voice audio.goro_v_laugh2d2
            g "Hahaha! Teasing doesn’t suit you, Yoshinori."

            show yoshi awkward3 at left2
            voice audio.yoshi_v_hey3
            yo "H-Hey…!"

            show goro play2 at right2
            voice audio.goro_v_well1a
            g "Well, if you really to want to give me a show, then start working out. "
            g "I’ll watch. "
        "Pecs.":
            $ working = True
            $ score_bot += 1
            hide yoshi2_autumn
            hide yoshi2 comp3
            show yoshi_autumn at left2
            show yoshi bold2 at left2
            voice audio.yoshi_v_think4
            yo "I want to try the press machine? It focuses on my pecs!"
            yo "I kind of want mine to be as nice as yours, Sir Goro…"

            hide goro_autumn
            hide goro talk3
            show goro2_autumn at right2
            show goro2 play3 at right2
            voice audio.goro_v_heh1a
            g "Heh… Mine are pretty huge, so it’d take you some time before you get there."

            show yoshi comp3 at left2
            voice audio.yoshi_v_laugh1
            yo "Well, I think it’d be nice to be able to bounce them a little bit!"

            hide goro2_autumn
            hide goro2 play3
            show goro_autumn at right2
            show goro laugh1 at right2
            voice audio.goro_v_laugh2d2
            g "Hahaha, do you want to give me something to gawk at so badly?"

            hide yoshi_autumn
            hide yoshi comp3
            show yoshi2_autumn at left2
            show yoshi2 comp6 at left2
            voice audio.yoshi_v_well3
            yo "W-Well… It’s not fair that I’m the only who gets teased around you, sir."

            show goro play2 at right2
            voice audio.goro_v_well1a
            g "Well, if you really to want to give me a show, then start working out. "
            g "I’ll watch. "
        "Biceps.":
            $ working = True
            $ score_top += 2
            hide yoshi2_autumn
            hide yoshi2 comp3
            show yoshi_autumn at left2
            show yoshi bold2 at left2
            voice audio.yoshi_v_think4
            yo "I want to try this curl machine! It looks like it focuses on my arms!"
            yo "I kind of want mine to be as nice as yours, Sir Goro…"

            hide goro_autumn
            hide goro talk3
            show goro2_autumn at right2
            show goro2 play3 at right2
            voice audio.goro_v_heh1a
            g "Heh… Mine are pretty huge, so it’d take you some time before you get there."
            g "Besides, your arms look great as they are."

            show yoshi comp3 at left2
            voice audio.yoshi_v_well3
            yo "W-Well, I thought it would be easier to carry stuff around if I was stronger."
            yo "Maybe one day, I’ll be able to lift you too, sir."

            hide goro2_autumn
            hide goro2 play3
            show goro_autumn at right2
            show goro bold2 at right2
            voice audio.goro_v_heh3a
            g "Hah, is that a challenge?"

            hide yoshi_autumn
            hide yoshi comp3
            show yoshi2_autumn at left2
            show yoshi2 shy5 at left2
            voice audio.yoshi_v_ehem1a
            yo "*ehem* I-I guess I’ll go ahead and start."
        "Glutes.":
            $ working = True
            $ score_bot += 2
            hide yoshi2_autumn
            hide yoshi2 comp3
            show yoshi_autumn at left2
            show yoshi bold2 at left2
            voice audio.yoshi_v_think4
            yo "I want to try the squat machine, sir! It focuses on my glutes!"

            hide goro_autumn
            hide goro talk3
            show goro2_autumn at right2
            show goro2 play3 at right2
            voice audio.goro_v_oh3a
            g "Oh~?"

            hide yoshi_autumn
            hide yoshi bold2
            show yoshi2_autumn at left2
            show yoshi2 confused2 at left2
            voice audio.yoshi_v_what2
            yo "Wh-What’s with the face, sir…?"

            show goro2 tease2 at right2
            voice audio.goro_v_heh1a
            g "Guess I don’t mind having bigger cheeks to smack."

            hide yoshi2_autumn
            hide yoshi2 confused2
            show yoshi_autumn at left2
            show yoshi panic3 at left2
            voice audio.yoshi_v_shock4
            yo "G-GAH…!"

            show goro2 bold5 at right2
            voice audio.goro_v_what1
            g "What? I’m just saying."

            hide yoshi_autumn
            hide yoshi panic3
            show yoshi2_autumn at left2
            show yoshi2 sigh1 at left2
            voice audio.yoshi_v_sigh3a
            yo "*sigh* You’re really enjoying teasing me today, huh, sir?"

            show goro2 play2 at right2
            voice audio.goro_v_laugh2d2
            g "It’s not my fault you make it so easy for me."

            hide yoshi_autumn
            hide yoshi comp3
            show yoshi2_autumn at left2
            show yoshi2 shy5 at left2
            voice audio.yoshi_v_ehem1a
            yo "*ehem* I-I guess I’ll go ahead and start."

    hide yoshi2_autumn
    hide yoshi2 shy5
    hide yoshi2 comp6
    show yoshi_autumn at left2
    show yoshi norm1 at left2
    hide goro2_autumn
    hide goro2 play2
    show goro_autumn at right2
    show goro norm1 at right2
    $ renpy.pause (1.0, hard=True)

    show yoshi_autumn at p5_4
    show yoshi shock1 at p5_4
    show goro_autumn at p5_5
    show goro shock1 at p5_5
    with move

    show lloyd_yoga at p5_1
    show lloyd happy2 at p5_1
    with dissolve

    voice audio.lloyd_v_goro1b
    l "Sir Goro!"

    show lloyd_yoga at left
    show lloyd talk4 at left
    show yoshi_autumn at center
    show yoshi norm1 at center
    show goro_autumn at right
    show goro norm1 at right
    with move

    voice audio.lloyd_v_shock1a1
    l "Oh, you’re with Yoshi too!"

    show goro happy2 at right
    voice audio.goro_v_goodam2a1
    g "Hello, Lloyd. Looking fit today."

    show lloyd laugh1 at left
    voice audio.lloyd_v_gratitude1a2
    l "Thanks, sir! I just finished doing some yoga~. You know I don’t skip a day of my routine!"
    l "Looks like you guys are working out too, huh?"

    show yoshi happy1 at center
    voice audio.yoshi_v_yeah2
    yo "Yeah! We’re just about to start, though! "

    show goro talk3 at right
    voice audio.goro_v_oh3a
    g "I’m surprised Darius isn’t with you."

    show lloyd talk4 at left
    voice audio.lloyd_v_conj4a1
    l "Oh, he’s actually on his way here! Maybe he’s in the changing room by now!"

    show yoshi talk3 at center
    voice audio.yoshi_v_laugh1
    yo "It’s really rare to see you two apart. You guys are usually stuck together like glue!"

    show goro happy1 at right
    voice audio.goro_v_agree7a
    g "I agree. Ever since the first term, you two have had one of the closest bonds amongst all the scouts."

    show lloyd think2 at left
    voice audio.lloyd_v_conj1a3
    l "Well, I don’t know how to explain it, ’cause Dar’s pretty much the opposite of me."
    l "The only thing we had in common back then is how we were both sort of outcasts."

    show yoshi confused2 at center
    voice audio.yoshi_v_right5
    yo "This was before we all became roommates, right?"

    show lloyd comp3 at left
    voice audio.lloyd_v_agree2a1
    l "Yeah. I’m sure you guys remember how I was way too excitable in my younger days."
    l "And let’s just say some of the other scouts found me and my hobbies kinda annoying."

    show lloyd sigh4 at left
    voice audio.lloyd_v_sigh1a
    l "Nobody took me seriously because of it. And it doesn’t help that I’m short AF too."

    show goro worry2 at right
    voice audio.goro_v_sigh1b
    g "As your scoutmaster, I feel bad I didn’t know about all this…"

    show lloyd comp2 at left
    voice audio.lloyd_v_denial1b1
    l "Nah, Sir Goro! It’s just how things are with immature teenagers."

    show lloyd bold2 at left
    voice audio.lloyd_v_conj5a
    l "Besides, if it weren’t for that, I wouldn’t have gotten close to Dar."
    l "The other scouts used to stay away from him because of how quiet he was."
    l "Everyone just assumes he’s either intimidating or uninteresting, which wasn’t really fair ’cause they didn’t even try to get to know him!"

    show lloyd bold5 at left
    voice audio.lloyd_v_laugh1a1
    l "All I needed to do was approach him, and everything just clicked since then!"

    show yoshi comp2 at center
    voice audio.yoshi_v_aww2
    yo "Darius is really lucky he has you, Lloyd."

    show lloyd talk2 at left
    voice audio.lloyd_v_denial2a1
    l "No way! I’m actually the lucky one here!"
    l "He always listens to everything I have to say, and you guys know I run my mouth a lot."

    show lloyd comp3 at left
    voice audio.lloyd_v_praise2a
    l "And when it comes to my interests, he always tries to enjoy them with me! Even though he does like to tease me about them still…"

    show yoshi comp6 at center
    voice audio.yoshi_v_laugh5a
    yo "Darius does like to tease."

    show lloyd comp5 at left
    voice audio.lloyd_v_response1b1
    l "I don’t mind though! He always does his best to make me feel like I don’t have to change anything about myself!"
    l "Whether it’s my hyperness, my temper, or even my height! He accepts all of them!"

    show lloyd bold2 at left
    voice audio.lloyd_v_conj4a1
    l "Heck, the reason why I’m even into yoga is because of him! He taught me how to find my ‘inner peace’!"

    show goro happy4 at right
    voice audio.goro_v_glad1a
    g "That’s an amazing thing to hear, Lloyd. I’m sure Darius feels the same about you."

    show lloyd_yoga at p4_2
    show lloyd shock1 at p4_2
    show yoshi_autumn at p4_3
    show yoshi shock1 at p4_3
    show goro_autumn at p4_4
    show goro shock1 at p4_4
    with move

    show darius_yoga at p4_1
    show darius tease2 at p4_1
    with dissolve

    voice audio.darius_v_greet1a1
    d "Boo."

    show lloyd_blush1 at p4_2
    show lloyd shock3 at p4_2
    voice audio.lloyd_v_shock4a1
    l "GAHH! You startled me, Dar!"

    show darius tease4 at p4_1
    voice audio.darius_v_laugh2a
    d "Hehe. I heard my name. "
    d "Were you talking about me, Lloyd?"

    show darius_yoga at p5_1
    show darius shock1 at p5_1
    show lloyd_yoga at p5_2
    show lloyd_blush1 at p5_2
    show lloyd shy2 at p5_2
    with move

    voice audio.lloyd_v_denial2b1
    l "Nope! You didn’t hear anything! "

    show lloyd shy6 at p5_2
    voice audio.lloyd_v_rush1a2
    l "Come on, Dar! it’s time to do some yoga! Bye, guys!"

    hide darius_yoga
    hide darius shock1
    hide lloyd_yoga
    hide lloyd_blush1
    hide lloyd shy6
    with moveoutleft

    show yoshi_autumn at left2
    show yoshi confused2 at left2
    show goro_autumn at right2
    show goro norm1 at right2
    with move

    hide yoshi_autumn
    hide yoshi confused2
    show yoshi2_autumn at left2
    show yoshi2 confused2 at left2
    voice audio.yoshi_v_uh1a
    yo "Didn’t Lloyd say he was done with yoga?"

    show goro laugh2 at right2
    voice audio.goro_v_laugh2d2
    g "Hahaha, he looked really embarrassed."

    show goro happy2 at right2
    voice audio.goro_v_conj1a1
    g "However, I must admit, I feel like a proud father seeing those two like this…"

    show yoshi2 comp3 at left2
    voice audio.yoshi_v_laugh5a
    yo "That made you sound really old, sir… and cheesy."

    hide goro_autumn
    hide goro happy2
    show goro2_autumn at right2
    show goro2 explain2 at right2
    voice audio.goro_v_ehem1a
    g "*ehem* We got sidetracked. "
    g "Back to our workout!"

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black with fade

    if dayg3_choice == False:
        $ dayg3_choice = True
        yo "{i}We spent the rest of the afternoon working out until we realized the sun had already set.{/i}"
        yo "{i}We decided to finish up, take a quick shower, and check out another place in the hotel for the evening.{/i}"

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
        yo "{i}We spent the rest of the evening working out until we realized it was already late.{/i}"
        yo "{i}We decided to finish up, take a quick shower, and head back to our room to call it a night.{/i}"

        scene cg black
        hide screen location
        hide screen timeline
        hide screen quick_menu
        $quick_menu = False
        with fade
        $ time_transition_sunset_to_night_winter()
        $ renpy.pause (2.0, hard=True)
        jump day3_goro_after


label day3_goro_room:
    $sq_jin += 1
    $say_box = True
    $quick_menu = True
    $mm_talking = True
    $g3_room = True
    voice audio.yoshi_v_think4
    yo "Maybe we should check on what the others are doing?"

    if dayg3_choice == True:
        voice audio.goro_v_response3a1
        g "I don’t mind. Maybe they’re up to something interesting. "
    else:
        voice audio.goro_v_response3a1
        g "I don’t mind. It’s almost the end of the day anyway."

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

    if dayg3_choice == False:
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

    show jin_autumn at right
    show jin_glasses at right
    show jin norm1 at right
    with move

    show jin_autumn at left
    show jin_glasses at left
    show jin norm1 at left
    with move

    show goro_autumn at right
    show goro norm1 at right
    show yoshi_autumn at center
    show yoshi happy2 at center
    with dissolve

    play sound sfx_dooropen
    voice audio.yoshi_v_greet1a1
    yo "Hey there, Jin! "

    show jin happy1 at left
    voice audio.jin_v_greet1b3
    j "A-Ah, hey guys, please come in!"

    if dayg3_choice == True:
        show goro confused2 at right
        voice audio.goro_v_think1d1
        g "Hm? Where’s Yuri? Shouldn’t she be with you?"

        show jin awkward5 at left
        voice audio.jin_v_wah2a
        j "G-Gah, I’m sorry, sir! I couldn’t keep her under control!"

        show goro talk3 at right
        voice audio.goro_v_oh1a
        g "Oh, you’re not in trouble. I was just wondering why you stayed in. There’s so much to do out there. "

        show jin comp2 at left
        voice audio.jin_v_comp8b1
        j "I-It’s alright. sir! I’m not really the type to go out and party. I’m fine just staying in a cozy room like this!"
        j "B-Besides, my stomach is still recovering from the bus ride this morning."

        show yoshi worry2 at center
        voice audio.yoshi_v_oops1
        yo "Oh no, do you still feel a little sick?"
    else:
        show yoshi talk3 at center
        voice audio.yoshi_v_greet2a1
        yo "I hope we didn’t bother you!"

        show jin comp2 at left
        voice audio.jin_v_denial2b1
        j "N-Not at all! I was just resting!"

        show yoshi worry2 at center
        voice audio.yoshi_v_oops1
        yo "Oh no, do you still feel sick from the bus ride this morning?"

    show jin comp3 at left
    voice audio.jin_v_yeah5b
    j "Yeah… it kinda takes a while before its gone…"

    show yoshi worry1 at center
    voice audio.yoshi_v_unsure2a
    yo "Are you alright in here by yourself? "

    show jin comp2 at left
    voice audio.jin_v_yes1c
    j "Oh, yes! I’ll be fine… Honestly, I prefer to stay in the room anyway."

    hide goro_autumn
    hide goro talk3
    hide goro norm1
    show goro2_autumn at right
    show goro2 confused2 at right
    voice audio.goro_v_really2a
    g "Really? Why’s that?"

    show jin think2 at left
    voice audio.jin_v_conj2c1
    j "W-Well, I’m not really used to going on trips with a large group, and I’m not actually sure what to do…"

    show goro2 think3 at right
    voice audio.goro_v_think1a1
    g "Hmmm, I suppose a vacation with tons of options like this could be a bit overwhelming."
    g "Maybe something a little more outdoorsy and natural would have suited you better."

    show yoshi happy2 at center
    voice audio.yoshi_v_oh1
    yo "Oh, you mean like our beach trip, sir?"

    hide jin_autumn
    hide jin_glasses
    hide jin think2
    show jin2_autumn at left
    show jin2_glasses at left
    show jin2 fudan3 at left
    voice audio.jin_v_gasp2a
    j "*gasp* A beach episode?!"

    hide goro2_autumn
    hide goro2 think3
    show goro_autumn at right
    show goro talk3 at right
    voice audio.goro_v_ah1a
    g "Ah, that’s right, you weren’t here last term, Jin. Yes, we took the campers to the beach for a few days during the summer this year."
    g "Getting into a swimsuit with the summer sun and ocean breeze was quite relaxing."

    show jin2 fudan6 at left
    voice audio.jin_v_what4a
    j "W-What?! Sir Goro… in a SKIMPY SWIMSUIT?!"

    hide yoshi_autumn
    hide yoshi happy2
    show yoshi2_autumn at center
    show yoshi2 comp6 at center
    voice audio.yoshi_v_laugh6
    yo "I-I wouldn’t say skimpy, but it was definitely tiny enough to be distracting…"

    hide goro_autumn
    hide goro talk3
    show goro2_autumn at right
    show goro2 explain2 at right
    voice audio.goro_v_ehem1a
    g "*ehem* Well, if it weren’t for you lei-ing me, it would’ve been too distracting for the scouts."

    show jin2 fudan2 at left
    voice audio.jin_v_hngh2a
    j "W-What?! LAYING?! You have to tell me the details, right now!"

    show goro2 play2 at right
    voice audio.goro_v_jin2c
    g "Don’t get the wrong idea, Jin. I assure you it’s safe enough that you could maybe even use it for that journal project of yours."

    show yoshi2 shy5 at center
    voice audio.yoshi_v_uh1a
    yo "I-Is it, though sir…? I don’t think that’s appropriate for-"

    show jin2 scheme4 at left
    voice audio.jin_v_yes6c
    j "YES, IT IS! I INSIST!"
    j "LET ME GRAB MY LAPTOP RIGHT NOW!"

    show goro2 play3 at right
    voice audio.goro_v_yoshi15a
    g "Looks like we’re invested now, Yoshinori."

    show yoshi2 sigh1 at center
    voice audio.yoshi_v_sigh3a
    yo "*sigh* I guess we’re doing this…"

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
    $ minigame_id = 'jmG3'
    if dayg3_choice == False:
        $ renpy.call(minigame_id, 'day')
    else:
        $ renpy.call(minigame_id, 'sunset')

label day3_goro_postmg:
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

    show yoshi_swim at left2
    show yoshi norm1 at left2
    show aiden_swim at right2
    show aiden talk5 at right2
    voice audio.aiden_v_comeon1b1
    a "Come on, Yoshi! We already setup the campsite, what the heck else do ya gotta do?!"

    show yoshi talk3 at left2
    voice audio.yoshi_v_oh1
    yo "Oh, it’s nothing major, Aiden! I’m just crafting something!"
    yo "You can go on ahead without me."

    hide aiden_swim
    hide aiden talk5
    show aiden2_swim at right2
    show aiden2 sigh5 at right2
    voice audio.aiden_v_sheesh2a
    a "Sheesh, Yoshi… Shouldn’t you be taking it easy? The sportsfest is over, and we’re on vacation! We should be relaxing!"

    show yoshi explain4 at left2
    voice audio.yoshi_v_well2
    yo "Well, this is the first time Sir Goro has gone on a trip with us in a while, and I just want to make sure he has a great time!"
    yo "He’s been really satisfied with all of our progress so far, and I want to keep the streak going."

    show aiden2 sigh1 at right2
    voice audio.aiden_v_sigh1a
    a "*sigh* You’re always so worried about what Gramps will think of us… But then again, I guess it can’t be helped."
    a "He HAS been a crank-o-potamus for years after all!"

    show yoshi explain2 at left2
    voice audio.yoshi_v_ehem1a
    yo "*ehem* I’m sure Sir Goro is just going through a lot. Which is exactly why I want to use this trip as a chance for him to destress!"

    show aiden2 pout2 at right2
    voice audio.aiden_v_agree8a1
    a "Alright, fine… Guess I could go and start doing a little prepwork for lunch before I swim."
    a "Maybe some fresh fish’ll lighten his mood too!"

    show yoshi happy2 at left2
    voice audio.yoshi_v_encourage3
    yo "That sounds great, Aiden! I’ll help you catch some as soon as I’m done here!"

    hide aiden2_swim
    hide aiden2 pout2
    show aiden_swim at right2
    show aiden talk2 at right2
    voice audio.aiden_v_agree3a1
    a "Sure thing, Yoshi."

    hide aiden_swim
    hide aiden talk2
    with dissolve

    show yoshi think2 at left2
    voice audio.yoshi_v_think1a
    yo "Let’s see…. The flowers go here…"

    play sound sfx_grassrustle
    show yoshi confused2 at left2
    voice audio.yoshi_v_huh1
    yo "Huh?"

    play sound sfx_grassrustle
    hide yoshi_swim
    hide yoshi confused2
    show yoshi2_swim at left2
    show yoshi2 confused5 at left2
    voice audio.yoshi_v_uh1a
    yo "Is someone in the bushes…?"

    show yoshi2_swim at p5_2
    show yoshi2 confused5 at p5_2
    with move

    show goro_swim3 at p5_1
    show goro norm3 at p5_1
    with dissolve

    hide yoshi2_swim
    hide yoshi2 confused5
    show yoshi_swim at p5_2
    show yoshi shock3 at p5_2
    voice audio.yoshi_v_shock4
    yo "GAH! S-Sir?!"

    show goro_swim3 at left2
    show goro norm3 at left2
    show yoshi_swim at right2
    show yoshi shock2 at right2
    with move

    voice audio.yoshi_v_worry3
    yo "W-What are you doing here, Sir Goro?!"

    show goro disappoint2 at left2
    voice audio.goro_v_hmph1a
    g "Hmph, I should be asking you. I didn’t expect you to try and sneak up on me while I’m getting dressed."

    hide yoshi_swim
    hide yoshi shock2
    show yoshi2_swim at right2
    show yoshi2 panic3 at right2
    voice audio.yoshi_v_shock2a
    yo "A-Ack! I didn’t know sir… I thought you’d be getting dressed in your tent."

    show goro explain2 at left2
    voice audio.goro_v_well1a
    g "Well, I would normally, but Yuri’s not comfortable with me changing in there."
    g "It’s just easier if I do it out here."

    hide yoshi2_swim
    hide yoshi2 panic3
    show yoshi2_swim at right2
    show yoshi2 shy1 at right2
    show yoshi2_blush1 at right2
    yo "..."

    show goro play2 at left2
    voice audio.goro_v_oh3a
    g "Oh? Something catch your eye?"

    show yoshi2 shy5 at right2
    voice audio.yoshi_v_uh1b
    yo "Uhh…."

    show goro angry3 at left2
    voice audio.goro_v_yoshi12a
    g "YOSHINORI." with vpunch

    show yoshi2 panic3 at right2
    voice audio.yoshi_v_shock4
    yo "GAH! W-What is it, sir?"

    show goro annoy2 at left2
    voice audio.goro_v_really1a
    g "If you want to ogle my body, you could at least try and be a little more subtle about it."

    show yoshi2 worry2 at right2
    voice audio.yoshi_v_sorry2b
    yo "S-Sorry, sir…! I didn’t mean to!"

    show goro sigh1 at left2
    voice audio.goro_v_sigh2a
    g "*sigh* I can’t really blame you… Even this shirt is several sizes too small."
    g "Yuri is terrible at picking out what I wear – she’s never paid attention to my body type, after all."

    show yoshi2 shy6 at right2
    voice audio.yoshi_v_gulp1a
    yo "*gulp* T-That explains the suit as well…"

    show goro play3 at left2
    voice audio.goro_v_heh1a
    g "Heh, watch where you’re looking."

    show yoshi2 awkward4 at right2
    voice audio.yoshi_v_uh1a
    yo "I, uh…"

    show goro confused2 at left2
    voice audio.goro_v_anyway1
    g "Anyway, what do you have in your hand there?"

    hide yoshi2_swim
    hide yoshi2 awkward4
    hide yoshi2_blush1
    show yoshi_swim at right2
    show yoshi talk3 at right2
    voice audio.yoshi_v_oh2
    yo "O-Oh, this? It’s actually a flower necklace I was making!"

    show goro think2 at left2
    voice audio.goro_v_confused1b1
    g "Huh… I’d forgotten how delicate you can be when it comes to crafting."

    show yoshi happy2 at right2
    voice audio.yoshi_v_well2
    yo "W-Well, I owe that to all the badges I’ve hand-knitted over the years."
    yo "But I actually made this one for you, sir!"

    show goro shock2 at left2
    voice audio.goro_v_really2a
    g "…Really? What for?"

    show yoshi comp2 at right2
    voice audio.yoshi_v_so1a
    yo "I know how busy you’ve been, and how rare it is for us to get to spend a vacation together, so…"
    yo "I thought it’d be a great way to welcome you back for the trip!"

    show goro_blush1 at left2
    show goro awkward1 at left2
    g "..."

    hide yoshi_swim
    hide yoshi happy2
    show yoshi2_swim at right2
    show yoshi2 comp3 at right2
    voice audio.yoshi_v_comp3
    yo "Y-You don’t have to wear it though, sir! I know it’s a bit different from your style-"

    show goro awkward4 at left2
    voice audio.goro_v_alright1a1
    g "I’ll take it."

    hide goro_swim3
    hide goro awkward3
    hide goro_blush1
    show goro_swim at left2
    show goro relief2 at left2
    with dissolve

    voice audio.goro_v_relief1a
    g "Matches my getup, anyways."

    hide yoshi2_swim
    hide yoshi2 comp3
    show yoshi_swim at right2
    show yoshi comp5 at right2
    voice audio.yoshi_v_laugh1
    yo "I-It really does, sir… It looks good on you…!"

    hide goro_swim
    hide goro relief2
    show goro2_swim at left2
    show goro2 comp2 at left2
    voice audio.goro_v_ehem1a
    g "*ehem* Thank you, Yoshinori."

    show yoshi comp6 at right2
    voice audio.yoshi_v_response3a
    yo "You’re welcome, sir! I’m so glad you like it!"

    hide goro2_swim
    hide goro2 comp2
    show goro_swim at left2
    show goro comp3 at left2
    voice audio.goro_v_heh1a
    g "Heh…"

    show yoshi happy2 at right2
    voice audio.yoshi_v_anyway1b
    yo "A-Anyway, I’ll get back to my other duties, and let you-"

    hide goro_swim
    hide goro comp3
    show goro2_swim at left2
    show goro2 play2 at left2
    voice audio.goro_v_wait3a1
    g "Hold on, Yoshinori."

    hide yoshi_swim
    hide yoshi happy2
    show yoshi2_swim at right2
    show yoshi2 confused2 at right2
    voice audio.yoshi_v_huh1
    yo "O-Oh, what is it, sir?"

    show goro2 tease2 at left2
    voice audio.goro_v_laugh1b1
    g "You’re not just going to leave with unfinished business, are you?"

    show yoshi2 awkward4 at right2
    voice audio.yoshi_v_sir4
    yo "Wh-What are you trying to say, sir…?"

    show goro2 tease5 at left2
    voice audio.goro_v_well2a
    g "You’re the one who just ‘leid’ me – don’t you think I should return the favor?"

    hide yoshi2_swim
    hide yoshi2 awkward4
    show yoshi_swim at right2
    show yoshi_blush1 at right2
    show yoshi panic3 at right2
    voice audio.yoshi_v_what4
    yo "W-WHAT?!"

    show goro2 play5 at left2
    voice audio.goro_v_rush2b1
    g "Don’t act so innocent, Yoshinori – We both know why you’ve been staring at me this whole time."
    g "And don’t think I haven’t noticed that bulge in your shorts."

    show yoshi panic1 at right2
    yo "…!!"

    show goro2 bold2 at left2
    voice audio.goro_v_rush1a1
    g "You’re not the only one who wants to get off here, Yoshinori."
    g "Now, get on your knees."

    show yoshi awkward4 at right2
    voice audio.yoshi_v_yessir1
    yo "*gulp* Y-Yes, sir…!"

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black with fade
    yo "{i}Following Sir Goro’s command, I knelt on the ground and began to pull down his suit…{/i}"

    scene cg black
    hide screen location
    hide screen timeline
    hide screen quick_menu
    $quick_menu = False
    with fade
    jump day3_goro_mg1

label day3_goro_postfb:

    if dayg3_choice == False:
        $ location = location_hotelroom
        show screen location
        show screen timeline
        show screen quick_menu
        $quick_menu = True
        scene bg_hotel_room2_day with fade
    else:
        $ location = location_hotelroom
        show screen location
        show screen timeline
        show screen quick_menu
        $quick_menu = True
        scene bg_hotel_room2_sunset with fade

    play music here_they_come loop
    show jin2_autumn at left
    show jin2_glasses at left
    show jin2_nosebleed at left
    show jin2_blush2 at left
    show jin2 dizzy2 at left
    show goro_autumn at center
    show goro norm1 at center
    show yoshi2_autumn at right
    show yoshi2 think1 at right
    voice audio.jin_v_fudan4a1
    j "B-Beach… W-White foam…"

    show yoshi2 think2 at right
    voice audio.yoshi_v_actually1a
    yo "You know, it was probably a good thing you brought me to the water, sir, or there would’ve been no way to clean up that mess."
    yo "*sigh* And I remember my thing feeling numb for the rest of the day after that too."

    show goro relief2 at center
    voice audio.goro_v_heh1a
    g "Not me. I felt relaxed for the entire day after."

    show jin2 dizzy3 at left
    show jin2_blush2 at left
    voice audio.jin_v_fudan2c
    j "Cream… Pie…"

    show yoshi2 sigh4 at right
    voice audio.yoshi_v_sigh3a
    yo "It was a miracle nobody found us, or else it would’ve been a disaster."
    yo "I can’t even imagine what would’ve happened if the scouts or Aiden caught us… Or worse, Yuri…"

    hide goro_autumn
    hide goro relief2
    show goro2_autumn at center
    show goro2 explain2 at center
    voice audio.goro_v_ehem1a
    g "*ehem* I’d prefer not to think about that, Yoshinori."

    show jin2 dizzy1 at left
    show jin2_nosebleed at left
    j "…"

    hide yoshi2_autumn
    hide yoshi2 sigh4
    show yoshi_autumn at right
    show yoshi confused2 at right
    voice audio.yoshi_v_uh1a
    yo "Uhh… We might’ve overloaded him again, sir…"

    show goro2 shy2 at center
    voice audio.goro_v_think3
    g "Uhh… Look at his pants."

    show yoshi shock2 at right
    voice audio.yoshi_v_shock4
    yo "Gah! J-Jin!"

    show jin2 dizzy5 at left
    voice audio.jin_v_bye2b2
    j "I have to go… to the bathroom… "

    hide jin2_autumn
    hide jin2 dizzy5
    hide jin2_glasses
    hide jin2_nosebleed
    hide jin2_blush2
    with dissolve

    show goro2 confused2 at center
    voice audio.goro_v_think1a1
    g "Seems he was really having stomach issues."

    hide yoshi_autumn
    hide yoshi shock2
    show yoshi2_autumn at right
    show yoshi2 sigh1 at right
    voice audio.yoshi_v_sigh3a
    yo "*sigh* But it looks like he didn’t even write anything down on his laptop."

    hide yoshi2_autumn
    hide yoshi2 sigh1
    show yoshi_autumn at right
    show yoshi talk2 at right
    voice audio.yoshi_v_but1
    yo "Although, that might be for the best… We shouldn’t publish anything like that on the blog."
    yo "Let’s just fill out a story about the activities while Jin, uhh… takes care of his business."

    show goro2 think3 at center
    voice audio.goro_v_unsure3a1
    g "Perhaps I can check on him in the bathroom and see if I can help anything with his gagging…"

    voice audio.jin_v_hngh5c
    j "HNGHGHGHGGHH!" with vpunch

    hide yoshi_autumn
    hide yoshi talk2
    show yoshi2_autumn at right
    show yoshi2 sigh4 at right
    voice audio.yoshi_v_sigh3a
    yo "*sigh*"

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black with fade
    yo "{i}We spent the next while typing out some of the fun events we’d done at the beach on Jin’s laptop.{/i}"
    yo "{i}After he calmed down, Jin joined us and helped get the next entry ready.{/i}"
    $ renpy.pause (1.0, hard=True)

    if dayg3_choice == False:
        $ dayg3_choice = True
        yo "{i}As we left Jin to rest, we suddenly realized that the sun had already set.{/i}"
        yo "{i}We decided to go check out another area of the hotel before it got too late.{/i}"
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
        yo "{i}As we left Jin to rest, we suddenly realized how late it was, and decided to head back to our own room and call it a night.{/i}"
        scene cg black
        hide screen location
        hide screen timeline
        hide screen quick_menu
        $quick_menu = False
        with fade
        $ time_transition_sunset_to_night_winter()
        $ renpy.pause (2.0, hard=True)
        jump day3_goro_after

label day3_goro_lobby:
    $sq_emilia += 1
    $say_box = True
    $quick_menu = True
    $mm_talking = True
    $g3_lobby = True
    voice audio.yoshi_v_sir1
    yo "Let’s go back to the lobby, sir!"

    voice audio.goro_v_alright1c2
    g "There’s not much to see there, but I guess it’ll help kill some time."

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

    if dayg3_choice == False:
        $ location = location_hotellobby
        show screen location
        show screen timeline
        show screen quick_menu
        $quick_menu = True
        scene bg_hotel_lobby_day with fade
        play music buddy_oath_casual loop
    else:
        $ location = location_hotellobby
        show screen location
        show screen timeline
        show screen quick_menu
        $quick_menu = True
        scene bg_hotel_lobby_sunset with fade
        play music heracleum_a loop

    show yoshi_autumn at right2
    show yoshi norm1 at right2
    show goro_autumn at left2
    show goro think2 at left2
    voice audio.goro_v_think1a1
    g "Hmm… Let me ask the receptionist if there any events for tonight."

    show goro_autumn at p5_1
    show goro shock1 at p5_1
    show yoshi_autumn at p5_2
    show yoshi talk1 at p5_2
    with move

    show emilia_autumn at p5_5
    show emilia norm1 at p5_5
    with dissolve

    voice audio.yoshi_v_wait1
    yo "Oh, wait! Isn’t that Emilia over there?"

    hide goro_autumn
    hide goro shock1
    show goro2_autumn at p5_1
    show goro2 confused2 at p5_1
    voice audio.goro_v_confused1a1
    g "Huh… I thought she’d be in her room… I hope she’s not causing a commotion again. "

    hide yoshi_autumn
    hide yoshi talk1
    show yoshi2_autumn at p5_2
    show yoshi2 worry2 at p5_2
    voice audio.yoshi_v_think1a
    yo "Maybe I should check just to make sure she doesn’t."

    hide goro2_autumn
    hide goro2 confused2
    show goro_autumn at p5_1
    show goro awkward3 at p5_1
    voice audio.goro_v_wait2a1
    g "Wait… Don’t tell me you’re going to talk to her?"

    hide yoshi2_autumn
    hide yoshi2 worry2
    show yoshi_autumn at p5_2
    show yoshi comp2 at p5_2
    voice audio.yoshi_v_please1a
    yo "I promise I’ll be quick, sir."

    hide goro_autumn
    hide goro awkward3
    show goro2_autumn at p5_1
    show goro2 sigh1 at p5_1
    voice audio.goro_v_response3a1
    g "*sigh* Fine. "

    show yoshi_autumn at p5_4
    show yoshi norm1 at p5_4
    with move

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

    show goro2_autumn at left2
    show goro2 explain2 at left2
    show yoshi2_autumn at right2
    show yoshi2 sad1 at right2
    with move

    voice audio.goro_v_sigh1a
    g "I knew that was a bad idea."

    show yoshi2 worry2 at right2
    voice audio.yoshi_v_yeah3
    yo "Yeah, I don’t even know why I tried."

    show goro2 talk1 at left2
    voice audio.goro_v_but1b
    g "I know we’re supposed to work on our relationship with her, especially after what happened yesterday."
    g "But I don’t think she’s ready to have that conversation yet."

    show yoshi2 sad4 at right2
    voice audio.yoshi_v_but2
    yo "I just can't help but think about how almost everyone gave up on her when we were scouts."
    yo "And even though we're much older, she's still stuck in her ways."

    show yoshi2 sad6 at right2
    voice audio.yoshi_v_conj1b
    yo "And I'm worried that if I stop trying, then who will?"

    show goro2 shy1 at left2
    g "..."

    hide yoshi2_autumn
    hide yoshi2 sad6
    show yoshi_autumn at right2
    show yoshi panic3 at right2
    voice audio.yoshi_v_ah3
    yo "Ah, I’m sorry, sir! I didn't mean to dig so deeply into it."

    if dayg3_choice == False:
        $dayg3_choice = True
        yo "We should be trying to do something fun out here."

        show goro2 shy2 at left2
        voice audio.goro_v_agree1c1
        g "Yes. "

        show yoshi talk3 at right2
        voice audio.yoshi_v_alright1
        yo "Alright, let’s decide where we should go next!"

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
        $ say_box = False
        $mm_talking = False
        $renpy.choice_for_skipping()
        show screen minimap()
        $ renpy.pause (hard=True)
    else:
        show goro2 shy2 at left2
        voice audio.goro_v_rush1c1
        g "Let’s just head back to our room and call it a night."

        hide yoshi_autumn
        hide yoshi panic3
        show yoshi2_autumn at right
        show yoshi2 worry2 at right
        voice audio.yoshi_v_yessir3
        yo "Yes, sir…"

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
        jump day3_goro_after


label day3_goro_club:
    $sq_aiden += 1
    $say_box = True
    $mm_talking = True
    $quick_menu = True
    $g3_club = True
    voice audio.yoshi_v_think4
    yo "Oh, how about we head over to the bar, sir?"

    if dayg3_choice == False:
        voice audio.goro_v_heh1a
        g "Heh, I was hoping you’d say that. Let’s go."
    else:
        voice audio.goro_v_alright1a1
        g "Sounds like the perfect way to end the day. Let’s go."

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

    if dayg3_choice == False:
        $ location = location_hotelclub
        show screen location
        show screen timeline
        show screen quick_menu
        $quick_menu = True
        scene bg_hotel_bar_day with fade
        play music close_distance loop

        show goro_autumn at left2
        show goro norm1 at left2
        show yoshi_autumn at right2
        show yoshi shock2 at right2
        voice audio.yoshi_v_shock1a
        yo "Whoa… This place looks cozy!"

        show goro happy2 at left2
        voice audio.goro_v_heh1a
        g "I bet it’s completely different at night."

        hide yoshi_autumn
        hide yoshi shock2
        show yoshi2_autumn at right2
        show yoshi2 think2 at right2
        voice audio.yoshi_v_think1a
        yo "Maybe it’s a lot more like a club than a casual pub…"
    else:
        $ location = location_hotelclub
        show screen location
        show screen timeline
        show screen quick_menu
        $quick_menu = True
        scene bg_hotel_bar_night with fade
        play music on_the_edge_club loop

        show goro_autumn at left2
        show goro norm1 at left2
        show yoshi_autumn at right2
        show yoshi shock2 at right2
        voice audio.yoshi_v_shock1a
        yo "Whoa! This place looks lively…!"

        show goro happy2 at left2
        voice audio.goro_v_confused1a1
        g "Nothing like the bars we go to back home, huh?"

        hide yoshi_autumn
        hide yoshi shock2
        show yoshi2_autumn at right2
        show yoshi2 think2 at right2
        voice audio.yoshi_v_yeah1
        yo "Yeah, this place is a lot more like a club than a casual pub…"

        show goro think3 at left2
        voice audio.goro_v_heh1a
        g "Definitely, especially with all of these entertainers."

    show goro_autumn at center
    show goro norm1 at center
    show yoshi2_autumn at right
    show yoshi2 norm1 at right
    with move

    show justin_bar at left
    show justin_glasses at left
    show justin happy1 at left
    with dissolve

    hide yoshi2_autumn
    hide yoshi2 norm1
    show yoshi_autumn at right
    show yoshi norm1 at right
    voice audio.justin_v_greet3a
    bt "Hello! Welcome to Bottom’s Up!  We pride ourselves on our ‘top’ service!"
    bt "What can I get you two fine gentlemen? Fancy a drink?"

    show goro talk3 at center
    voice audio.goro_v_agree2c1
    g "Ah, yes. Can we have the menu please?"

    show justin grin1 at left
    voice audio.justin_v_ofcourse2a
    bt "Here you go, sir!"

    show justin_bar at center
    show justin_glasses at center
    show justin grin1 at center
    with move

    show justin_bar at left
    show justin_glasses at left
    show justin grin1 at left
    with move

    hide goro_autumn
    hide goro talk3
    show goro2_autumn at center
    show goro2 think4 at center
    voice audio.goro_v_think1b1
    g "Hmmm… "

    show yoshi shock2 at right
    voice audio.yoshi_v_shock1b
    yo "Whoa… I only recognize a few of these drinks, sir…"

    hide goro2_autumn
    hide goro2 think4
    show goro_autumn at center
    show goro explain2 at center
    voice audio.goro_v_but1b
    g "I would usually have whiskey. But with how many options there are, it’d be a shame to not try something new."

    hide goro_autumn
    hide goro explain2
    show goro2_autumn at center
    show goro2 play3 at center
    voice audio.goro_v_heh1a
    g "Heh, how about you pick for the two of us, Yoshinori?"

    show yoshi think1 at right
    yo "{i}(Looking at the options… Sir Goro would like…){/i}"

    $ working = False
    $ shuffle_menu()
    menu():
        yo "{i}(Looking at the options… Sir Goro would like…){/i}{fast}"
        "Liquid Viagra.":
            $ working = True
            $ score_goro -= 1
            $ score_top += 1
            show yoshi talk3 at right
            voice audio.yoshi_v_think1a
            yo "I think we could use some ‘Liquid Viagra’!"

            show justin explain3 at left
            voice audio.justin_v_conj2a1
            bt "It’s a simple mix of digestif and energy drink!"

            show goro2 annoy2 at center
            voice audio.goro_v_no1a1
            g "Hard pass."

            show yoshi comp3 at right
            voice audio.yoshi_v_think4
            yo "How about we order your specialty mix instead?"

            show justin happy1 at left
            voice audio.justin_v_catchphrase2a
            bt "Magical! Two ‘Sailor Moan’, coming up!"
        "Screaming Orgasm.":
            $ working = True
            $ score_goro -= 1
            $ score_bot += 1
            show yoshi talk3 at right
            voice audio.yoshi_v_think1a
            yo "Maybe we’ll have a ‘Screaming Orgasm’?"

            show goro2 confused5 at center
            voice audio.goro_v_confused1a1
            g "Huh… I’m not sure I’d be into that."

            show justin explain3 at left
            voice audio.justin_v_conj1a1
            bt "It’s a simple mix of coffee and vodka!"

            show goro2 annoy2 at center
            voice audio.goro_v_no1a1
            g "I like coffee. I like alcohol. But not together."

            show yoshi comp3 at right
            voice audio.yoshi_v_think4
            yo "How about we order your specialty mix instead?"

            show justin happy1 at left
            voice audio.justin_v_catchphrase2a
            bt "Magical! Two ‘Sailor Moan’, coming up!"
        "Cocksucking Cowboy.":
            $ working = True
            $ score_goro += 1
            $ score_top += 2
            show yoshi happy2 at right
            voice audio.yoshi_v_sir1
            yo "You like a ‘Cocksucking Cowboy’, right sir?"

            show goro2 play2 at center
            voice audio.goro_v_amazed2a1
            g "Heh, that sounds like a mouthful."
            g "Butterscotch, schnapps, and a whole lotta cream… "

            show justin happy1 at left
            voice audio.justin_v_catchphrase2a
            bt "Alright~ Two ‘Cocksucking Cowboys’, coming up!"
        "Leg Spreader.":
            $ working = True
            $ score_goro += 1
            $ score_bot += 2
            show yoshi happy2 at right
            voice audio.yoshi_v_sir1
            yo "Sounds like you’d enjoy a ‘Leg Spreader’, sir!"

            show goro2 play2 at center
            voice audio.goro_v_amazed2a1
            g "Heh, you know me well."
            g "Tequila, vodka, gin, and rum all together. A total homewrecker."

            show justin happy1 at left
            voice audio.justin_v_catchphrase2a
            bt "Alright~ A pair of ‘Leg Spreaders’ coming up!"
    bt "While you wait, we’ll send over our hottest, newest entertainer to your table! Be right back!"

    hide yoshi_autumn
    hide yoshi happy2
    show yoshi2_autumn at right
    show yoshi2 confused2 at right
    voice audio.yoshi_v_uh1a
    yo "Uhh… I don’t think we—"

    hide justin_bar
    hide justin_glasses
    hide justin happy1
    with dissolve

    show aiden_shirtless at left
    show aiden drunk3 at left
    with dissolve

    voice audio.aiden_v_hey2a1
    a "Hey there~! Wanna have some fun toni-"

    hide goro2_autumn
    hide goro2 play2
    hide goro2 annoy2
    show goro_autumn at center
    show goro comic1 at center
    hide yoshi2_autumn
    hide yoshi2 confused2
    show yoshi_autumn at right
    show yoshi panic3 at right
    yog "AIDEN?!"

    show aiden panic3 at left
    voice audio.aiden_v_shock2a1
    a "WAH! Gramps, Yoshi! What are you two doing here?!"

    show yoshi angry3 at right
    voice audio.yoshi_v_aiden10
    yo "W-We should be the ones asking you that…!!"

    show goro angry3 at center
    voice audio.goro_v_aiden5a
    g "Good heavens, Aiden…  Even out here, you can’t keep a shirt on?"

    show aiden drunk6 at left
    voice audio.aiden_v_well1a1
    a "Well, my boss said that’s the dress code around here~"

    show goro irked3 at center
    voice audio.goro_v_what1
    g "What? First of all, I’m your boss. Second of all, you don’t work here!"

    show aiden talk2 at left
    voice audio.aiden_v_drunk1a
    a "It’s only a one-night gig, Gramps! They said I could get all those fancy drinks I can’t pronounce in exchange!"
    a "’Cause holy fuck, did you guys see how crazy the prices are? It’s more than my daily salary!"

    hide goro_autumn
    hide goro irked3
    show goro2_autumn at center
    show goro2 disappoint3 at center
    voice audio.goro_v_sigh1b
    g "*sigh* We’re on vacation, Aiden. Sit your ass here and drink with us. I’m paying."

    show aiden excited4 at left
    voice audio.aiden_v_drunk4a
    a "WOOOHOOO! Don’t mind if I do, sugar daddy!"

    show goro2_autumn at left
    show goro2 disappoint3 at left
    show aiden_shirtless at center
    show aiden excited4 at center
    with move

    show yoshi annoy3 at right
    voice audio.yoshi_v_really5
    yo "You’re drunk, aren’t you, Aiden?"

    show aiden drunk6 at center
    voice audio.aiden_v_drunk3a
    a "Yup! *burp*"

    hide goro2_autumn
    hide goro2 disappoint3
    show goro_autumn at left
    show goro comp3 at left
    voice audio.goro_v_well1a
    g "Well, it’s good to see you enjoying yourself at least. You’ve been working nonstop at camp, and I’m not talking about just on the project."

    show aiden drunk3 at center
    voice audio.aiden_v_yeah2c2
    a "Oh, you bet! I’m having the time of my life here!"
    a "I’m waiting for the entertainment later! I heard it’s gonna be a blast!"

    show yoshi shock2 at right
    voice audio.yoshi_v_amazed1a
    yo "Wow! Like a live show?"

    show aiden drunk2 at center
    voice audio.aiden_v_agree1b1
    a "Yep! You guys are free to join if you want! They said that audience interaction is welcome!"

    hide yoshi_autumn
    hide yoshi shock2
    show yoshi2_autumn at right
    show yoshi2 awkward3 at right
    voice audio.yoshi_v_oh3
    yo "Oh… It’s that kind of show…"

    show aiden drunk5 at center
    voice audio.aiden_v_drunk2b1
    a "I bet a lot of people would love to have a piece of Gramps over here! Even right now, a couple are checking him out!"

    show goro explain1 at left
    voice audio.goro_v_ehem1a
    g "That event sounds more up your alley, Aiden."

    show aiden excited3 at center
    voice audio.aiden_v_amazed2b1
    a "Yep! I’m already booked for a VIP session later! Who knew you can make tons of cash off of it?!"

    hide yoshi2_autumn
    hide yoshi2 awkward3
    show yoshi_autumn at right
    show yoshi angry3 at right
    voice audio.yoshi_v_what4
    yo "WHAT?! Aiden, do you know what you’re getting yourself into?!"

    show aiden comp5 at center
    voice audio.aiden_v_comp1a2
    a "Don’t worry! It’s just ‘look, don’t touch’, and I’ll keep my pants on!"

    hide goro_autumn
    hide goro explain1
    show goro2_autumn at left
    show goro2 confused2 at left
    voice audio.goro_v_so1a
    g "So, a tamer version of what you already do back at camp."

    show aiden drunk2 at center
    voice audio.aiden_v_conj3a1
    a "Although I wouldn’t mind getting some action too~"

    show goro2_autumn at p4_2
    show goro2 confused2 at p4_2
    show aiden_shirtless at p4_3
    show aiden drunk2 at p4_3
    show yoshi_autumn at p4_4
    show yoshi angry3 at p4_4
    with move

    show justin_bar at p4_1
    show justin wink3 at p4_1
    show justin_glasses at p4_1
    with dissolve

    voice audio.justin_v_aiden3a
    bt "Hey there, Aiden! Your client’s looking for you!"

    show aiden talk2 at p4_3
    voice audio.aiden_v_bye1a
    a "Ooh, that’s my cue, guys! Seeya!"

    hide aiden_shirtless
    hide aiden talk2
    with moveoutleft

    show yoshi panic3 at p4_4
    voice audio.yoshi_v_wait3a
    yo "Aiden, wait—!"

    show goro2 explain2 at p4_2
    voice audio.goro_v_wait3a1
    g "He’s old enough, Yoshinori. Let the boy have a good time. "

    hide yoshi_autumn
    hide yoshi panic3
    show yoshi2_autumn at p4_4
    show yoshi2 sigh4 at p4_4
    voice audio.yoshi_v_sigh3a
    yo "*sigh* I guess…"

    show justin grin1 at p4_1
    voice audio.justin_v_conj1a1
    bt "Well, I have your drinks ready now! Please enjoy!"

    hide goro2_autumn
    hide goro2 explain2
    show goro_autumn at p4_2
    show goro happy1 at p4_2
    voice audio.goro_v_laugh1a1
    g "Cheers, Yoshinori."

    if dayg3_choice == False:
        $ dayg3_choice = True
        $ renpy.music.stop(channel='music', fadeout = 1.0)
        $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
        $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
        scene cg black with fade
        yo "{i}(We spent the rest of the evening enjoying our drinks and chatting casually.){/i}"
        yo "{i}(By the time it was dark out, we figured we’d stop before we got drunk so we can still check out other areas of the hotel.){/i}"

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
        yo "{i}(We spent the rest of the night enjoying our drinks and chatting casually.){/i}"
        yo "{i}(We decided to call it a night and stop before we got too drunk, and headed back to our room...){/i}"

        scene cg black
        hide screen location
        hide screen timeline
        hide screen quick_menu
        $quick_menu = False
        with fade
        $ time_transition_sunset_to_night_winter()
        $ renpy.pause (2.0, hard=True)
        jump day3_goro_after

label day3_goro_after:
    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    $ time = timeline_timenight
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
    scene bg_hotel_room1_night with fade
    $ say_box = True
    play music ready_for_tomorrow loop

    show goro_sleep at left2
    show goro norm2 at left2
    show yoshi_sleep at right2
    show yoshi relief2 at right2
    voice audio.yoshi_v_relief1
    yo "Whew, I’m so beat…! It’s been a while since I had so much fun."

    show goro relief2 at left2
    voice audio.goro_v_yeah1a1
    g "Yeah, me too. It’s a nice feeling compared to a long day of work."

    show yoshi comp2 at right2
    voice audio.yoshi_v_yeah2
    yo "I agree, sir. I’m ready for a good night sleep."

    show goro happy2 at left2
    voice audio.goro_v_rush2a1
    g "Come over and lay down here then. The bed’s really comfortable."

    hide yoshi_sleep
    hide yoshi comp2
    show yoshi2_sleep at right2
    show yoshi2 shy5 at right2
    voice audio.yoshi_v_ah2
    yo "Ah, well…"

    hide goro_sleep
    hide goro happy2
    show goro2_sleep at left2
    show goro2 confused2 at left2
    voice audio.goro_v_what1
    g "What? Don’t tell me you’re still thinking twice about sleeping with me."
    g "You’ve already done way more than that with me today."

    show yoshi2_blush1 at right2
    show yoshi2 sigh4 at right2
    voice audio.yoshi_v_unsure3c
    yo "*sigh* I guess…"

    show goro2_sleep at left3
    show goro2 relief5 at left3
    show yoshi2_sleep at right3
    show yoshi2 sigh4 at right3
    show yoshi2_blush1 at right3
    with move

    voice audio.goro_v_relief1a
    g "See? It’s big enough for the both of us."

    hide yoshi2_sleep
    hide yoshi2_blush1
    hide yoshi2 sigh4
    show yoshi_sleep at right3
    show yoshi worry2 at right3
    voice audio.yoshi_v_sorry2b
    yo "I-I’m sorry I’ve been so antsy about it, sir. "
    yo "It’s just really hard to wrap my head around the fact we’re doing all of this together."

    hide goro2_sleep
    hide goro2 relief5
    show goro_sleep at left3
    show goro talk3 at left3
    voice audio.goro_v_think1a1
    g "Hopefully that’s not a bad thing."

    $ working = False
    $ shuffle_menu()
    menu():
        g "Hopefully that’s not a bad thing.{fast}"
        "It feels wrong.":
            $ working = True
            $ score_goro -= 2
            show yoshi comp3 at right3
            voice audio.yoshi_v_well1
            yo "I’m enjoying it so much that it almost feels wrong."

            show goro explain2 at left3
            voice audio.goro_v_well1a
            g "Well, just don’t overthink it and enjoy the moment."
        "It's different.":
            $ working = True
            $ score_goro -= 1
            show yoshi comp3 at right3
            voice audio.yoshi_v_well1
            yo "It’s just so different from our usual routine."

            show goro explain2 at left3
            voice audio.goro_v_well1a
            g "Well, just don’t overthink it and enjoy the moment."
        "It feels familiar.":
            $ working = True
            $ score_goro += 1
            show yoshi comp3 at right3
            voice audio.yoshi_v_disagree3
            yo "Not at all, sir! Spending time with you feels so familiar."
            yo "It’s just like when I was a scout and everything was fresh and exciting!"

            show goro explain3 at left3
            voice audio.goro_v_well1a
            g "Well, that’s how it’s supposed to be. Just enjoy the moment."
        "It brings me back.":
            $ working = True
            $ score_goro += 2
            show yoshi comp3 at right3
            voice audio.yoshi_v_disagree3
            yo "Not at all, sir. It actually brings me back."
            yo "It’s just like when I was a scout and everything was fresh and exciting!"

            show goro explain3 at left3
            voice audio.goro_v_well1a
            g "Well, that’s how it’s supposed to be. Just enjoy the moment."

    show goro happy2 at left3
    voice audio.goro_v_request5a1
    g "This’ll help you chill out. *hands over a glass of whiskey* "

    show yoshi shock2 at right3
    voice audio.yoshi_v_shock1a
    yo "Whoa! Where did that drink come from?"

    hide goro_sleep
    hide goro happy2
    show goro2_sleep at left3
    show goro2 play3 at left3
    voice audio.goro_v_laugh1b2
    g "Hehe, our room has a mini-bar."

    if g3_club == False:
        show yoshi confused2 at right3
        voice audio.yoshi_v_uh1a
        yo "We’re gonna drink tonight, sir??"
    else:
        show yoshi confused2 at right3
        voice audio.yoshi_v_uh1a
        yo "We’re gonna drink more, sir…?!"

    hide goro2_sleep
    hide goro2 play3
    show goro_sleep at left3
    show goro relief4 at left3
    voice audio.goro_v_relief1b
    g "Just to relax, until you feel sleepy."

    show yoshi comp2 at right3
    voice audio.yoshi_v_alright1
    yo "Alright…"

    show goro happy2 at left3
    voice audio.goro_v_amazed2a1
    g "Look out the window, we’ve got a really pretty view of the city at night. "
    g "One day, I’ll be able to take you to newer places. So, get used to the new sights."

    show yoshi relief4 at right3
    voice audio.yoshi_v_relief1
    yo "I-I’d like that, sir…"

    scene cg black with fade
    yo "{i}After such an eventful day, Sir Goro and I managed to spend a really peaceful night together.{/i}"
    yo "{i}With the alcohol warming my system, I eventually fell asleep without even realizing it.{/i}"

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
    $ time_transition_night_to_day_winter()
    $ renpy.pause (2.0, hard=True)
    jump day4_goro
