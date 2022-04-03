label day9_aiden:
    $ day = "83"
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

    show aiden2_sleep at left2
    show aiden2 tired5 at left2
    show yoshi_sleep at right2
    show yoshi happy1 at right2
    voice audio.aiden_v_yawn2
    a "*yawn*"

    show yoshi happy1 at right2
    voice audio.yoshi_v_goodam1
    yo "Good morning, Aiden."

    show aiden2 sleepy2 at left2
    voice audio.aiden_v_goodam1b3
    a "Mmhh… Morning, Yoshi~"

    show aiden2_sleep at center
    show aiden2 shock1 at center
    show yoshi_sleep at right
    show yoshi happy1 at right
    with move

    show goro_winter at left
    show goro talk3 at left
    with dissolve

    voice audio.goro_v_ah1b
    g "Ah, I’m glad you two are awake."

    hide aiden2_sleep
    hide aiden2 shock1
    show aiden_sleep at center
    show aiden shock2 at center
    voice audio.aiden_v_sheesh1a
    a "Sheesh, Gramps! You startled me!"

    hide goro_winter
    hide goro talk3
    show goro2_winter at left
    show goro2 tease2 at left
    voice audio.goro_v_heh1a
    g "Did I interrupt your cuddle session, lovebirds?"

    hide yoshi_sleep
    hide yoshi happy1
    show yoshi2_sleep at right
    show yoshi2 awkward4 at right
    voice audio.yoshi_v_ah3
    yo "A-Ah, well…"

    show aiden talk1 at center
    voice audio.aiden_v_confused2a2
    a "You’re dressed up so early, Gramps. Headed somewhere?"

    hide goro2_winter
    hide goro2 tease2
    show goro_winter at left
    show goro talk1 at left
    voice audio.goro_v_agree1a1
    g "Yes, I have some urgent business to take care of at the city hall and I’m already running late."

    hide yoshi2_sleep
    hide yoshi2 awkward4
    show yoshi_sleep at right
    show yoshi talk1 at right
    voice audio.yoshi_v_confident2
    yo "I can drive for you, sir!"

    show goro explain2 at left
    voice audio.goro_v_comp2a1
    g "There’s no need. I do have a favor to ask though."

    show aiden confused2 at center
    voice audio.aiden_v_greet1a
    a "What is it, Gramps?"

    show goro confused3 at left
    voice audio.goro_v_think1a1
    g "Can you sort these documents and bring them over to the office for me?"
    g "It’s a report from Jin about the technical progress… I didn’t have time to read it last night, and this morning I’ve been rushing to get to town."

    show aiden tease1 at center
    voice audio.aiden_v_laugh1b2
    a "Hehe, you sure all that techie jargon didn’t just confuse you?"

    hide goro_winter
    hide goro confused3
    show goro2_winter at left
    show goro2 annoy3 at left
    voice audio.goro_v_hmph1a
    g "Hmph. I doubt you’d comprehend it either. "

    show aiden laugh1 at center
    voice audio.aiden_v_laugh2a1
    a "Fair point, haha!"
    a "But you can leave those docs to me, Gramps! I know where to put ‘em!"

    hide goro2_winter
    hide goro2 annoy3
    show goro_winter at left
    show goro talk3 at left
    voice audio.goro_v_thanks1a1
    g "Thanks. Now if you don’t mind, I really have to go."

    show yoshi happy2 at right
    voice audio.yoshi_v_worry1a
    yo "Drive safe, sir!"

    show goro happy1 at left
    voice audio.goro_v_bye1a1
    g "Of course. See you later."

    hide goro_winter
    hide goro happy1
    with dissolve

    show yoshi_sleep at right2
    show yoshi happy2 at right2
    show aiden_sleep at left2
    show aiden laugh1 at left2
    with move

    hide aiden_sleep
    hide aiden laugh1
    show aiden2_sleep at left2
    show aiden2 relief5 at left2
    voice audio.aiden_v_relief2a
    a "*stretches* Hnnn~ Now where were we?"

    show yoshi comp2 at right2
    voice audio.yoshi_v_think1a
    yo "Wanna sleep in some more? It seems like everyone else is still down."

    hide aiden2_sleep
    hide aiden2 relief5
    show aiden_sleep at left2
    show aiden laugh1 at left2
    voice audio.aiden_v_no2a1
    a "Nah, I’m pretty awake now – Gramps gave me quite the jump scare."

    show yoshi talk3 at right2
    voice audio.yoshi_v_well1
    yo "Well, should we get up then?"

    show aiden think2 at left2
    voice audio.aiden_v_well1a1
    a "Today’s pretty much a vacant day again, isn’t it?"

    show yoshi think2 at right2
    voice audio.yoshi_v_think1a
    yo "Hmm… The workers are scheduled to arrive tomorrow, so maybe we can prepare for that?"

    show aiden happy2 at left2
    voice audio.aiden_v_praise3a
    a "Oh, good idea Yoshi! If we do all the prep work today, I can cook up something special for them tomorrow!"
    a "Gotta learn some new tricks in the kitchen if I’m gonna be a chef, am I right?"

    show yoshi happy1 at right2
    voice audio.yoshi_v_yeah2
    yo "Yeah! That’s the spirit, Aiden!"

    show aiden talk2 at left2
    voice audio.aiden_v_anyway1a
    a "Though, I gotta drop this stuff by Gramps’ desk first! You can go get started in the kitchen for me, Yoshi!"

    show yoshi happy2 at right2
    voice audio.yoshi_v_sure2
    yo "Sure thing!"

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

    $ location = location_office
    show screen location
    show screen timeline
    show screen quick_menu
    $ quick_menu = True
    scene bg_office_winter_day with fade
    play music brand_new_day loop

    show aiden2_winter at right
    show aiden2 confused5 at right
    voice audio.aiden_v_sheesh1a
    a "Sheesh… There’s so much stuff on Gramps’ desk… How can he even tell which stack of paper he’s working on? "
    a "And I’m about to add more to the pile too… "

    show aiden2_winter at center
    show aiden2 confused5 at center
    with move

    hide aiden2_winter
    hide aiden2 confused5
    show aiden_winter at center
    show aiden bold2 at center
    voice audio.aiden_v_alright1a1
    a "There we go! Errand finished!"

    hide aiden_winter
    hide aiden bold2
    show aiden2_winter at center
    show aiden2 think2 at center
    voice audio.aiden_v_question1a
    a "Seriously, this stuff should all be digital by now. "
    a "I mean who even uses a landline and a fax machine nowadays?"

    show aiden2_winter at left2
    show aiden2 think4 at left2
    with move

    voice audio.aiden_v_think1a1
    a "Hmm…"
    a "Since I’m here, I might as well…"

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
    scene bg_kitchen_winter_day with fade
    play music go_with_the_flow loop
    play bgsound sfxloop_chopping loop

    show yoshi_autumn at left2
    show yoshi talk3 at left2
    show aiden2_winter at p5_5
    show aiden2 worry1 at p5_5
    voice audio.yoshi_v_ah1
    yo "Ah, you’re here, Aiden! I wondered what was taking so long."

    show aiden2 awkward6 at p5_5
    voice audio.aiden_v_oh1a
    a "Oh, I just had to, uhh… do a few chores along the way. "
    a "You know how Gramps is, his office was a disaster! I straightened it up for him."

    show yoshi laugh1 at left2
    voice audio.yoshi_v_laugh1
    yo "Haha! I guess I can’t help but tidy up his office whenever I go by there, too. "

    hide aiden2_winter
    hide aiden2 awkward6
    show aiden_winter at p5_5
    show aiden talk1 at p5_5
    voice audio.aiden_v_anyway2c
    a "A-Anyway, let me help out with the prep – I can’t let you do everything!"

    show aiden_winter at right2
    show aiden talk1 at right2
    with move

    hide aiden_winter
    hide aiden talk1
    show aiden2_winter at right2
    show aiden2 norm3 at right2
    a "*starts chopping*"

    hide yoshi_autumn
    hide yoshi laugh1
    show yoshi2_autumn at left2
    show yoshi2 confused2 at left2
    voice audio.yoshi_v_uh1a
    yo "Uh? Aren’t you going to wash your hands, first?"

    show aiden2 confused5 at right2
    voice audio.aiden_v_what1b
    a "Wha?"

    show yoshi2 confused5 at left2
    voice audio.yoshi_v_think1a
    yo "And you forgot to put your apron on."

    hide aiden2_winter
    hide aiden2 confused5
    show aiden_winter at right2
    show aiden awkward2 at right2
    voice audio.aiden_v_agree2b2
    a "O-Oh, right…!"

    show aiden_winter at right3
    show aiden awkward2 at right3
    with move

    hide aiden_winter
    hide aiden awkward2
    show aiden2_autumn at right3
    show aiden2 norm3 at right3
    with dissolve

    show yoshi2 confused1 at left2
    yo "..."

    show aiden2_autumn at right2
    show aiden2 think3 at right2
    with move

    hide aiden2_autumn
    hide aiden2 think3
    show aiden2_apron3 at right2
    show aiden2 think3 at right2
    with dissolve

    a "..."

    show yoshi2 think1 at left2
    yo "{i}(Hmm… Aiden’s acting a bit strange… I wonder what’s going on?){/i}"

    $working = False
    $shuffle_menu()
    menu():
        yo "{i}(Hmm… Aiden’s acting a bit strange… I wonder what’s going on?){/i}{fast}"
        "Want to call Mr. Clermont today?":
            $ working = True
            $ score_aiden -= 2
            hide yoshi2_autumn
            hide yoshi2 think1
            show yoshi_autumn at left2
            show yoshi talk1 at left2
            voice audio.yoshi_v_so2
            yo "S-So Aiden, I was thinking… When do you want to go and call Mr. Clermont today?"
            yo "We could do it right now, if you’re ready!"
        "Excited about the offer?":
            $ working = True
            $ score_aiden -= 1
            hide yoshi2_autumn
            hide yoshi2 think1
            show yoshi_autumn at left2
            show yoshi talk1 at left2
            voice audio.yoshi_v_so2
            yo "Excited about Mr. Clermont’s offer?"
        "Having second thoughts?":
            $ working = True
            $ score_aiden +=1
            hide yoshi2_autumn
            hide yoshi2 think1
            show yoshi_autumn at left2
            show yoshi talk1 at left2
            voice audio.yoshi_v_so2
            yo "Having second thoughts about Mr. Clermont’s offer?"
        "Worried about the offer?":
            $ working = True
            $ score_aiden += 2
            hide yoshi2_autumn
            hide yoshi2 think1
            show yoshi_autumn at left2
            show yoshi talk1 at left2
            voice audio.yoshi_v_so2
            yo "Are you worried about Mr. Clermont’s offer?"

    show aiden2 awkward5 at right2
    voice audio.aiden_v_confused1b2
    a "E-Eh? Where’d that come from?"

    hide yoshi_autumn
    hide yoshi talk1
    show yoshi2_autumn at left2
    show yoshi2 awkward4 at left2
    voice audio.yoshi_v_oh3
    yo "O-Oh, it’s nothing, I just thought you were acting different compared to this morning. Is something wrong?"

    show aiden2 explain2 at right2
    voice audio.aiden_v_no2a1
    a "Nah, I’m fine, Yoshi."

    show yoshi2 worry2 at left2
    voice audio.yoshi_v_rush3
    yo "Come on, Aiden. You should know by now that I can tell when something’s on your mind."

    show aiden2 sigh3 at right2
    voice audio.aiden_v_sigh1a
    a "*sigh* Yeah, you got me. I was thinking about it."

    hide yoshi2_autumn
    hide yoshi2 worry2
    show yoshi_autumn at left2
    show yoshi comp2 at left2
    voice audio.yoshi_v_confident2
    yo "If you’re worried about how to talk to Mr. Clermont, I have some good talking points and questions to ask during the call!"
    yo "I did a bunch of interviews for my part-time jobs back in college, so I think I can give you some tips!"

    show aiden2 confused5 at right2
    voice audio.aiden_v_think1a1
    a "Hmm… But the thing is… I don’t feel so sure, after thinking about it."

    hide yoshi_autumn
    hide yoshi comp2
    show yoshi2_autumn at left2
    show yoshi2 awkward4 at left2
    voice audio.yoshi_v_oh2
    yo "Oh… I thought you made up your mind last night?"

    show aiden2 worry2 at right2
    voice audio.aiden_v_conj3b2
    a "I mean, I just got this offer yesterday… Maybe I got myself way too hyped up about it in the moment. "
    a "I don’t wanna rush the decision. It could be a huge change for me, and you, after all."

    hide yoshi2_autumn
    hide yoshi2 awkward4
    show yoshi_autumn at left2
    show yoshi confused2 at left2
    voice audio.yoshi_v_think1a
    yo "Hmm… Do you think it’d help if we ask the others about it? So that it’s not just my opinion?"

    show aiden2 worry5 at right2
    voice audio.aiden_v_confused1c2
    a "Ehh… I dunno about that…"

    show aiden2_apron3 at p4_2
    show aiden2 worry2 at p4_2
    show yoshi_autumn at p4_1
    show yoshi confused2 at p4_1
    with move

    show emilia_winter at p4_4
    show emilia tired3 at p4_4
    show yuri_winter at p4_3
    show yuri serious1 at p4_3
    with dissolve

    voice audio.emilia_v_yuri3
    e "Yuri… I already broke a nail doing the laundry… Can I take a break from all of these menial jobs…?"

    show yuri serious4 at p4_3
    voice audio.yuri_v_rush1d1
    yu "These jobs aren’t menial! You’re gonna work your ass off till you can see how essential these tasks are since—"

    show emilia eyeroll6 at p4_4
    voice audio.emilia_v_tsun4
    e "“It’S tHe sAmE jOb yOu wErE bAdMoUtHiNg BaCk ThEn” Fine, fine! I get it… geez…"

    show yuri tease2 at p4_3
    voice audio.yuri_v_conj2a3
    yu "See, you’re getting the hang of it~"

    show yoshi talk1 at p4_1
    voice audio.yoshi_v_goodam1
    yo "Oh, hey there, you two! Good morning!"

    show yuri happy1 at p4_3
    voice audio.yuri_v_greet2a
    yu "Hello, Yoshi and Aiden~"

    show emilia confused2 at p4_4
    voice audio.emilia_v_oh2a
    e "You’re not just in an apron today – what’s the occasion?"

    show aiden2 comp3 at p4_2
    voice audio.aiden_v_laugh1b1
    a "Ahehe, well it has gotten pretty cold lately…"

    show emilia annoy2 at p4_4
    voice audio.emilia_v_sarcastic4
    e "I still don’t understand how you got away with being naked in the kitchen all those other times. I’m pretty sure that’s a sanitary code violation."

    hide aiden2_apron3
    hide aiden2 comp3
    show aiden_apron3 at p4_2
    show aiden talk1 at p4_2
    voice audio.aiden_v_hey1e2
    a "Hey… I make sure the food is clean… and tasty~! "

    show yoshi bold2 at p4_1
    voice audio.yoshi_v_comp2
    yo "It’s okay, Emilia, We’re approved by The Health Inspection Culinary Collective Association or T.H.I.C.C. Ass.  "

    show emilia irked2 at p4_4
    voice audio.emilia_v_question2b
    e "Did you just make that up…?"

    show yoshi shock2 at p4_1
    voice audio.yoshi_v_what3
    yo "Wh-What? Of course not! That’s a legitimate food safety committee…!"

    show emilia annoy3 at p4_4
    voice audio.emilia_v_question3
    e "And how did you manage to pull that approval off with Aiden over here running around the camp? Did you hide him in the closet?"

    hide aiden_apron3
    hide aiden talk1
    show aiden2_apron3 at p4_2
    show aiden2 think5 at p4_2
    voice audio.aiden_v_think2a
    a "I wear clothes during the inspections…"

    show yuri tease4 at p4_3
    voice audio.yuri_v_laugh1a1
    yu "Hihi, you’re not the only one who knows how to get clever with screening applications, Emilia~"

    show emilia panic5 at p4_4
    voice audio.emilia_v_ah2b
    e "G-Gah…!"

    hide yoshi_autumn
    hide yoshi shock2
    show yoshi2_autumn at p4_1
    show yoshi2 think2 at p4_1
    voice audio.yoshi_v_ehem1b
    yo "*ehem* What brings you two here anyway?"

    show yuri talk3 at p4_3
    voice audio.yuri_v_oh1a
    yu "Oh, Emilia and I were grabbing supplies to clean the mess hall thoroughly before the workers arrived. "

    hide aiden2_apron3
    hide aiden2 think5
    show aiden_apron3 at p4_2
    show aiden awkward2 at p4_2
    voice audio.aiden_v_amazed2a2
    a "Clean? Wow… Emilia, you’re actually taking stuff off my list."

    show emilia sigh1 at p4_4
    voice audio.emilia_v_sigh1b
    e "It’s not like I have a choice… I’d much rather have a desk job than this."

    show yuri excited2 at p4_3
    voice audio.yuri_v_excited1a
    yu "Speaking of jobs! I heard from Dad that someone got quite the job offer~"
    yu "Is it true? Are you really going to be a pro chef now, Aiden?!"

    hide aiden_apron3
    hide aiden awkward2
    show aiden2_apron3 at p4_2
    show aiden2 awkward5 at p4_2
    voice audio.aiden_v_ah1a
    a "A-Ah, well…"

    hide yoshi2_autumn
    hide yoshi2 think2
    show yoshi_autumn at p4_1
    show yoshi talk2 at p4_1
    voice audio.yoshi_v_actually1a
    yo "Actually, Aiden still hasn’t made up his mind about it."

    show emilia angry2 at p4_4
    voice audio.emilia_v_what2
    e "What?!"
    e "I’m appalled to hear that you’d even consider turning it down! "

    show emilia angry3 at p4_4
    voice audio.emilia_v_bossy1a
    e "An opportunity as big as this is once in a lifetime!"
    e "With someone of Mr. Clermont’s caliber, he’d really put your name out there! "

    hide yuri_winter
    hide yuri excited2
    show yuri2_winter at p4_3
    show yuri2 fangirl1 at p4_3
    voice audio.yuri_v_omg1a
    yu "Oh my god, Aiden!! Don’t forget us when you’re famous!"

    show emilia excited1 at p4_4
    voice audio.emilia_v_conj4a
    e "And that’s not even mentioning the money – you’d be pulling in almost five figures a month with the clientele he refers!"

    show aiden2 worry2 at p4_2
    voice audio.aiden_v_unsure1b
    a "I-I guess that is a lot of cash…"

    show emilia sigh1 at p4_4
    voice audio.emilia_v_sigh1b
    e "*sigh* I remember when my bank account had a hundred thousand just as petty cash…"
    e "After losing all that and having to live life so frugally, you really get to see what a difference it makes."

    show emilia explain2 at p4_4
    voice audio.emilia_v_tsun2a
    e "I’m not trying to be callous here, and I’m sure we all know, but Aiden has never really gotten to experience financial freedom."
    e "Now that you have the chance to change that, the decision here seems so obvious!"

    show emilia bold3 at p4_4
    voice audio.emilia_v_hmph1a
    e "I’m a go-getter, so if I were in your shoes, I’d fight for that position! "

    $ working = False
    $ shuffle_menu()
    menu():
        e "I’m a go-getter, so if I were in your shoes, I’d fight for that position!{fast}"
        "She has a point.":
            $ working = True
            $ score_aiden -= 2
            hide yoshi_autumn
            hide yoshi talk2
            show yoshi2_autumn at p4_1
            show yoshi2 talk3 at p4_1
            voice audio.yoshi_v_think1a
            yo "Emilia’s got a point – it’s such a great opportunity!"

            show aiden2 upset6 at p4_2
            voice audio.aiden_v_yeah1g1
            a "Y-Yeah, but there’s more to consider besides just the money…"
        "Maybe that makes it a little bit clearer for Aiden.":
            $ working = True
            $ score_aiden -= 1
            hide yoshi_autumn
            hide yoshi talk2
            show yoshi2_autumn at p4_1
            show yoshi2 talk3 at p4_1
            voice audio.yoshi_v_think1a
            yo "Maybe that makes things a little bit clearer for you, Aiden?"

            show aiden2 upset6 at p4_2
            voice audio.aiden_v_yeah1g1
            a "Y-Yeah, but there’s more to consider besides just the money…"
        "There's a lot to consider besides just money.":
            $ working = True
            $ score_aiden += 1
            hide yoshi_autumn
            hide yoshi talk2
            show yoshi2_autumn at p4_1
            show yoshi2 talk3 at p4_1
            voice audio.yoshi_v_well1
            yo "Well… There’s a lot of things to consider besides just the money, after all…"
        "Aiden is different.":
            $ working = True
            $ score_aiden += 2
            hide yoshi_autumn
            hide yoshi talk2
            show yoshi2_autumn at p4_1
            show yoshi2 talk3 at p4_1
            voice audio.yoshi_v_well1
            yo "Aiden’s not the same as you though, Emilia."
            yo "Sure, money is important, but there are other things to consider as well."

    show emilia annoy3 at p4_4
    voice audio.emilia_v_sarcastic2a
    e "It’s a JOB! It’s always about the money!"

    hide yuri2_winter
    hide yuri2 fangirl1
    show yuri_winter at p4_3
    show yuri angry3 at p4_3
    voice audio.yuri_v_emilia5a
    yu "Emilia, not everything is about that! Sometimes it’s about your passion and what makes you happy in the long run! "
    yu "You wouldn’t wanna work in a job that pays you well but makes you depressed and upset the whole time, would you?"

    show yuri explain2 at p4_3
    voice audio.yuri_v_conj5a
    yu "Either way, I understand Aiden! I know he isn’t used to that kind of environment, so it makes sense if he needs more time to decide!"

    show emilia evil2 at p4_4
    voice audio.emilia_v_tsk1a
    e "You’re wasting time if you ask me~ If you don’t want it, teach me how to cook and I’ll gladly take your spot!"

    show yuri annoy4 at p4_3
    voice audio.yuri_v_sarcastic1a2
    yu "Oh, please! You’d manage to burn cereal if we let you in the kitchen!"
    yu "Don’t listen to Emilia, Aiden. She doesn’t know what she’s talking about."

    show yuri_winter at p5_4
    show yuri tease2 at p5_4
    with move

    voice audio.yuri_v_bye2a
    yu "Now if you’ll excuse us, I’m gonna take this ‘go-getter’ and get her started mopping!"

    show emilia scared3 at p4_4
    voice audio.emilia_v_wait1c
    e "H-Hey, let go of me!"

    hide emilia_winter
    hide emilia scared3
    hide yuri_winter
    hide yuri tease2
    with moveoutright

    show aiden2_apron3 at right2
    show aiden2 sigh1 at right2
    show yoshi2_autumn at left2
    show yoshi2 talk3 at left2
    with move

    voice audio.aiden_v_sigh1a
    a "*sigh* "

    hide yoshi2_autumn
    hide yoshi2 talk3
    show yoshi_autumn at left2
    show yoshi worry2 at left2
    voice audio.yoshi_v_hey2
    yo "Hey, are you alright?"

    show aiden2 worry2 at right2
    voice audio.aiden_v_yeah1g2
    a "Yeah, what Emilia and Yuri said just got me thinking…"

    show yoshi comp2 at left2
    voice audio.yoshi_v_comp9
    yo "Take it with a grain of salt, Aiden. I’m sure they’re just sharing their opinions based on their experiences. "

    show aiden2 sigh3 at right2
    voice audio.aiden_v_unsure1b
    a "Yeah, I guess you’re right…"

    hide aiden2_apron3
    hide aiden2 sigh3
    show aiden_apron3 at right2
    show aiden talk1 at right2
    voice audio.aiden_v_anyway2b
    a "Anyway, why don’t we get back to work? Let’s cook our meals for today while we’re at it."

    show yoshi talk3 at left2
    voice audio.yoshi_v_alright2
    yo "Oh right, the guys will probably be up soon."

    show aiden explain2 at right2
    voice audio.aiden_v_rush1a2
    a "I’ll go ahead and preheat the oven."

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black with fade
    yo "{i}As I worked with Aiden, he stayed quiet and lost in his thoughts the entire time.{/i}"
    yo "{i}It’s just like back at the hotel… He keeps trying to change the topic and act as if everything is fine.{/i}"
    yo "{i}I knew he couldn’t get the advice about the offer off his mind.{/i}"
    yo "{i}A part of me hopes that I’m wrong, and just overthinking it.{/i}"
    $ renpy.pause (2.0, hard=True)
    yo "{i}Shortly after we finished cooking, we headed over to the construction site to bring everyone lunch and see what else we could do.{/i}"

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
    scene bg_site7_winter_day with fade
    play music sunset_stroll_winter loop

    show darius_workw at p5_1
    show darius_goggles2 at p5_1
    show darius bored1 at p5_1
    show lloyd_work2 at p5_2
    show lloyd norm2 at p5_2
    show jin_winter at p5_3
    show jin_glasses at p5_3
    show jin norm3 at p5_3
    show yoichi_winter at p5_4
    show yoichi annoyed3 at p5_4
    show taiga_winter at p5_5
    show taiga angry2 at p5_5
    voice audio.taiga_v_dumbass1
    t "Don’t swing the hammer that hard, you dumbass! You’re bending all the nails!"

    show yoichi annoyed1 at p5_4
    voice audio.yoichi_v_question2a1
    yi "How the hell else am I supposed to get them in, then?!"

    show taiga angry5 at p5_5
    voice audio.taiga_v_angry3a
    t "I’ve been showing you how but you keep ignoring me! Seriously, you have the attention span of a goldfish!"

    show yoichi angry1 at p5_4
    voice audio.yoichi_v_request1c1
    yi "What did you call me?! Take that back, Dynamite!"

    show jin scheme2 at p5_3
    voice audio.jin_v_fudan1a2
    j "*whispers* Now, kiss."

    show lloyd bored3 at p5_2
    voice audio.lloyd_v_geez1a3
    l "Geez, those two have been bickering nonstop since we started."

    show jin scheme3 at p5_3
    voice audio.jin_v_laugh2c
    j "I don’t mind… I will go down with this ship…"

    show lloyd sigh2 at p5_2
    voice audio.lloyd_v_sigh2a
    l "*sigh* I probably should’ve made Yoichi work on something else, huh…?"

    show darius bored5 at p5_1
    voice audio.darius_v_agree1b
    d "Yes."
    d "How about breaking down the scrap materials?"

    show lloyd amazed1 at p5_2
    voice audio.lloyd_v_shock1b1
    l "Ooh, good idea, Dar!"

    show lloyd happy1 at p5_2
    voice audio.lloyd_v_yoichi1c
    l "Hey, Yoichi! I’ve got something more fun for you to do! "
    l "See that pile of broken bricks over there? I want you to smash ’em to smaller pieces!"

    show yoichi excited1 at p5_4
    voice audio.yoichi_v_celebrate1a
    yi "Hell yeah! That’s more like it!"

    show yoichi_winter at p5_5
    show yoichi excited1 at p5_5
    show taiga_winter at p5_4
    show taiga annoyed2 at p5_4
    with move

    voice audio.taiga_v_ugh1
    t "Ugh. Good riddance."

    show darius_workw at p7_3
    show darius_goggles2 at p7_3
    show darius bored5 at p7_3
    show lloyd_work2 at p7_4
    show lloyd happy1 at p7_4
    show jin_winter at p7_5
    show jin_glasses at p7_5
    show jin scheme2 at p7_5
    show yoichi_winter at p7_7
    show yoichi excited1 at p7_7
    show taiga_winter at p7_6
    show taiga annoyed2 at p7_6
    with move

    show yoshi_winter2 at p7_1
    show yoshi norm1 at p7_1
    show aiden_winter2 at p7_2
    show aiden talk1 at p7_2
    with dissolve

    voice audio.aiden_v_guys3a
    a "Hey, guys, take a little break! We brought lunch!"

    show lloyd hungry4 at p7_4
    voice audio.lloyd_v_praise3a
    l "Alright! I’m starving!"

    show yoichi annoyed4 at p7_7
    voice audio.yoichi_v_annoyed1a5
    yi "That better not be some green, healthy crap you’re feeding us."

    show aiden happy2 at p7_2
    voice audio.aiden_v_orderup1a
    a "I made some burgers actually! Thought you guys need the extra protein from all that manual labor!"

    show yoshi talk3 at p7_1
    voice audio.yoshi_v_jin3
    yo "I’m surprised to see you here, Jin. Are you helping with the repairs?"

    show jin happy1 at p7_5
    voice audio.jin_v_yeah2a
    j "Y-Yeah… I stopped by after I finished up some coding."

    show lloyd talk1 at p7_4
    voice audio.lloyd_v_jin2b
    l "Since our workout yesterday, Jin wanted to continue being more physically active."

    show aiden comp3 at p7_2
    voice audio.aiden_v_glad1a
    a "Building those muscles, eh? Good for you!"

    show yoichi playful1 at p7_7
    voice audio.yoichi_v_hmph1a
    yi "Scrawny muscles! You’ll look like Dynamite over here!"

    show taiga laugh1 at p7_6
    voice audio.taiga_v_boastful2
    t "What’s wrong with that? I’m hot!"

    show yoichi pain1 at p7_7
    voice audio.yoichi_v_disgust1a
    yi "Blech, you’re just malnourished."

    show taiga annoyed2 at p7_6
    voice audio.taiga_v_sarcastic1
    t "You don’t even know what that word means."

    show jin sigh2 at p7_5
    voice audio.jin_v_sigh2a
    j "I can only dream that I’d have a body as nice as any of you guys…"

    show yoshi laugh2 at p7_1
    voice audio.yoshi_v_laugh1
    yo "Haha, it takes time, Jin! You don’t build muscle in a day, after all."

    show lloyd think2 at p7_4
    voice audio.lloyd_v_agree2a3
    l "I told him that too, but he’s determined to get fit for some cosplay!"

    show taiga talking5 at p7_6
    voice audio.taiga_v_surprised1a
    t "Oh, you cosplay, Jin? "

    show jin think5 at p7_5
    voice audio.jin_v_think1a1
    j "I’ve always looked at them but never tried it myself. "

    show yoichi angry1 at p7_7
    voice audio.yoichi_v_aiden1a
    yi "Hey, Buttcheeks! Where’s the ketchup?! " with vpunch

    show aiden talk4 at p7_2
    voice audio.aiden_v_oops1a
    a "Oh, woops, looks like I left it in the messhall!"

    show yoichi angry3 at p7_7
    voice audio.yoichi_v_groan2b1
    yi "Ugh! What was the point of bringing all this out here then?!"

    show aiden comp2 at p7_2
    voice audio.aiden_v_sorry1a1
    a "Haha, sorry, Yoichi! It must’ve slipped my mind."
    a "You can go and get it if you want."

    show yoichi talking2 at p7_7
    voice audio.yoichi_v_agree4a2
    yi "Fine! But I’m getting some marshmallows too!"

    hide yoichi_winter
    hide yoichi talking2
    with dissolve

    show yoshi_winter2 at p6_1
    show yoshi talk3 at p6_1
    show aiden_winter2 at p6_2
    show aiden comp2 at p6_2
    show darius_workw at p6_3
    show darius_goggles2 at p6_3
    show darius bored5 at p6_3
    show lloyd_work2 at p6_4
    show lloyd think2 at p6_4
    show jin_winter at p6_5
    show jin_glasses at p6_5
    show jin think5 at p6_5
    show taiga_winter at p6_6
    show taiga talking5 at p6_6
    with move

    voice audio.lloyd_v_sigh2a
    l "He’s not coming back, is he?"

    #show taiga munch2 at p6_6
    #jey
    voice audio.taiga_v_heh1
    t "Goodt, more for ursh!"

    hide yoshi_winter2
    hide yoshi talk3
    show yoshi2_winter2 at p6_1
    show yoshi2 sigh1 at p6_1
    voice audio.yoshi_v_sigh3a
    yo "*sigh* Chew your food well before talking, Taiga. You might choke."

    show taiga compassion5 at p6_6
    voice audio.taiga2_v_relief2c
    t "*gulp* Can’t help it. Aiden’s burgers are bajillion times better than the fast food ones I usually get."

    show jin happy2 at p6_5
    voice audio.jin_v_yeah1a
    j "I agree – I don’t think I could ever go back to my old diet after being here."

    show darius happy2 at p6_3
    voice audio.darius_v_thanks1a1
    d "Thanks for the food, Aiden. It’s delicious as always."

    show lloyd happy1 at p6_4
    voice audio.lloyd_v_idea1a
    l "You know, you could totally start your own restaurant and I’d be your loyal customer with how good your food is."

    hide aiden_winter2
    hide aiden comp2
    show aiden2_winter2 at p6_2
    show aiden2 comp6 at p6_2
    hide yoshi2_winter2
    hide yoshi2 sigh1
    show yoshi2_winter2 at p6_1
    show yoshi2 sigh1 at p6_1
    voice audio.aiden_v_laugh1b1
    a "A-Ahehe… You guys always flatter me too much."

    show lloyd bold2 at p6_4
    voice audio.lloyd_v_conj4a1
    l "I’m being serious here! If you made a career out of your talent, you’d be really successful!"
    l "I can already see it, “Camp Buddy, an origin story of where a master chef started his culinary journey”."

    show taiga laugh1 at p6_6
    voice audio.taiga2_v_idea1a
    t "‘Master Chef Aiden’ has such a nice ring to it! Don’t you think so?"

    $ working = False
    $ shuffle_menu()
    menu():
        t "‘Master Chef Aiden’ has such a nice ring to it! Don’t you think so?{fast}"
        "He actually got an offer.":
            $ working = True
            $ score_aiden -= 2
            hide yoshi2_winter2
            hide yoshi2 sigh1
            show yoshi_winter2 at p6_1
            show yoshi talk1 at p6_1
            voice audio.yoshi_v_conj3a
            yo "In fact, before Mr. Clermont left yesterday, he actually offered Aiden a chance at a professional certification to be a chef."

            show aiden2 awkward6 at p6_2
            voice audio.aiden_v_ah1a
            a "A-Ah, you didn’t have to tell them about that, Yoshi…!"
        "I think so too.":
            $ working = True
            $ score_aiden -= 1
            hide yoshi2_winter2
            hide yoshi2 sigh1
            show yoshi_winter2 at p6_1
            show yoshi happy1 at p6_1
            voice audio.yoshi_v_yeah1
            yo "I think so too. Aiden could really make it big out there."

            show yoshi explain2 at p6_1
            voice audio.yoshi_v_conj4a
            yo "In fact, before Mr. Clermont left yesterday, he actually offered Aiden a chance at a professional certification to be a chef."

            show aiden2 awkward6 at p6_2
            voice audio.aiden_v_ah1a
            a "A-Ah, you didn’t have to tell them about that, Yoshi…!"
        "He already is.":
            $ working = True
            $ score_aiden += 1
            hide yoshi2_winter2
            hide yoshi2 sigh1
            show yoshi_winter2 at p6_1
            show yoshi talk1 at p6_1
            voice audio.yoshi_v_actually1a
            yo "He already kinda is."

            show aiden2 confused5 at p6_2
            voice audio.aiden_v_confused1c2
            a "Ehh… It’s not official without the title."

            show darius confused2 at p6_3
            voice audio.darius_v_think1a1
            d "Hm? What do you mean?"

            show aiden2 awkward6 at p6_2
            voice audio.aiden_v_ah1a
            a "Ah, well… Before Mr. Clermont left yesterday, he sorta gave me a shot at being a pro chef."
        "If that's what Aiden wants.":
            $ working = True
            $ score_aiden += 2
            hide yoshi2_winter2
            hide yoshi2 sigh1
            show yoshi_winter2 at p6_1
            show yoshi talk1 at p6_1
            voice audio.yoshi_v_actually1a
            yo "If that’s what Aiden wants, there’s actually a chance."

            show aiden2 confused5 at p6_2
            voice audio.aiden_v_confused1c2
            a "Ehh… I’m still thinking about it."

            show darius confused2 at p6_3
            voice audio.darius_v_think1a1
            d "Hm? What do you mean?"

            show aiden2 awkward6 at p6_2
            voice audio.aiden_v_ah1a
            a "Ah, well… Before Mr. Clermont left yesterday, he sorta gave me a shot at being a pro chef."

    show jin amazed1 at p6_5
    voice audio.jin_v_whoa3a
    j "Whoa, that’s great news, Aiden! Congrats!"

    show lloyd happy2 at p6_4
    voice audio.lloyd_v_laugh1a1
    l "I’m sure you said yes, right? We could be co-workers! I mean… have the same boss at least, haha!"

    show darius play2 at p6_3
    voice audio.darius_v_confused1b
    d "Aren’t we already?"

    show lloyd talk3 at p6_4
    voice audio.lloyd_v_agree4b1
    l "Oh yeah… But you guys get my point! A job at Clermont Inc. is really as prestigious as it gets! It’ll be really good for your resume!"

    show yoshi talk2 at p6_1
    voice audio.yoshi_v_actually1b
    yo "Aiden hasn’t said yes yet, actually. He’s still giving it some time to think about."

    show darius confused3 at p6_3
    voice audio.darius_v_confused2a
    d "What’s holding you back, Aiden?"

    show aiden2 worry2 at p6_2
    voice audio.aiden_v_well1c1
    a "W-Well… I’m just feeling kinda pressured ’bout the whole thing. "

    show taiga confused2 at p6_6
    voice audio.taiga_v_confused1a
    t "Huh? Why? Isn’t that already the same thing you’re doing here?"

    show darius explain2 at p6_3
    voice audio.darius_v_denial1a1
    d "Not at all, especially if we’re talking about restaurants."

    show lloyd explain2 at p6_4
    voice audio.lloyd_v_agree2a1
    l "Yeah, Darius and I designed a few industrial kitchens before and we know that it gets pretty hectic in there."
    l "You make food to order and there’s always people to feed as long as the shop sign says open."

    show aiden2 upset6 at p6_2
    voice audio.aiden_v_yeah1g1
    a "Yeah… Unlike here at the camp, I can have a meal planned for the week to prep and cook everything in advance."

    show lloyd sigh1 at p6_4
    voice audio.lloyd_v_conj1a2
    l "Don’t get me wrong, what you’re doing now is just as labor intensive, but it’s the stress factor that’s often worse."

    show darius talk1 at p6_3
    voice audio.darius_v_think1a1
    d "Just like most professions out there."

    show jin confuseddn2 at p6_5
    voice audio.jin_v_yeah4b
    j "I guess the work environment could make or break it too. I get along better with everyone here at Camp Buddy than anywhere else I’ve worked."
    j "At least, post-Emilia filler arc…"

    show lloyd talk2 at p6_4
    voice audio.lloyd_v_conj6a2
    l "So, yeah! We totally get why you feel iffy about it! All that pressure would make me boil over too!"

    show taiga annoyed2 at p6_6
    voice audio.taiga_v_rush1a
    t "Come on, you guys. You’re not supposed to discourage him."

    show lloyd worry2 at p6_4
    voice audio.lloyd_v_ah1b1
    l "A-Ah, sorry! I wasn’t trying to…!"

    show taiga talking2 at p6_6
    voice audio.taiga2_v_encourage3a
    t "Like yeah, a new opportunity is scary, but you’ll never know unless you try. "
    t "And if you're worried about big changes, take it from me, it's much better on the other side."

    show taiga thinking3 at p6_6
    voice audio.taiga2_v_denial2b
    t "I know my situation was different, but if I hadn't taken that chance I'd have never been here with you guys, and made all my friends."

    show jin comp2 at p6_5
    voice audio.jin_v_think1a1
    j "Th-That's true... It's because I pushed myself out of my comfort zone that I met all of you too."
    j "So maybe taking risks isn't so bad...?"

    show lloyd bold2 at p6_4
    voice audio.lloyd_v_agree2b1
    l "Yeah! Once you get the hang of it, learn certain skills and how things work, it’s gonna get easier!"

    show darius comp2 at p6_3
    voice audio.darius_v_aiden2
    d "Aiden is tough and diligent. He can take anything you throw at him and make things work."

    show taiga talking3 at p6_6
    voice audio.taiga_v_heh1
    t "Sounds to me like the answer’s pretty obvious then. "

    show aiden2 awkward5 at p6_2
    voice audio.aiden_v_well1c2
    a "W-Well…"

    show yoshi_winter2 at p7_1
    show yoshi norm3 at p7_1
    show aiden2_winter2 at p7_2
    show aiden2 awkward5 at p7_2
    show darius_workw at p7_3
    show darius_goggles2 at p7_3
    show darius comp2 at p7_3
    show lloyd_work2 at p7_4
    show lloyd bold2 at p7_4
    show jin_winter at p7_5
    show jin_glasses at p7_5
    show jin comp2 at p7_5
    show taiga_winter at p7_6
    show taiga thinking3 at p7_6
    with move

    show yoichi_winter at p7_7
    show yoichi angry1 at p7_7
    voice audio.yoichi_v_greet1a5
    yi "Hey! I can’t find the freakin’ mallows! Where’d you guys hide them?!" with vpunch

    show lloyd shock2 at p7_4
    voice audio.lloyd_v_shock1a1
    l "Oh, look at that. He came back after all."

    show taiga angry5 at p7_6
    voice audio.taiga_v_ugh1
    t "Can’t you use your dog nose to sniff them out?"

    show yoichi angry6 at p7_7
    voice audio.yoichi_v_request1a3
    yi "Shut up, Dynamite! I wasn’t talking to you!"

    show jin comp3 at p7_5
    voice audio.jin_v_yoichi1a
    j "I have some of my burger left if you’re still hungry, Yoichi… I’m already full."

    show yoichi_winter at p7_6
    show yoichi excited1 at p7_6
    show taiga_winter at p7_7
    show taiga angry5 at p7_7
    with move

    voice audio.yoichi_v_agree1b4
    yi "Score!"

    show darius talk1 at p7_3
    voice audio.darius_v_aiden4
    d "What were you going to say, Aiden? We got interrupted."

    show aiden2 awkward2 at p7_2
    voice audio.aiden_v_oh3b
    a "O-Oh, nothing, really!"

    hide aiden2_winter2
    hide aiden2 awkward2
    show aiden_winter2 at p7_2
    show aiden explain2 at p7_2
    voice audio.aiden_v_actually3a
    a "A-Actually, I just remembered, I gotta see if the laundry’s dry on the line!  "
    a "See ya later, guys…!"

    hide aiden_winter2
    hide aiden explain2
    with dissolve

    show yoshi shock1 at p7_1
    show yoichi confused1 at p7_6
    voice audio.yoichi_v_confused1a1
    yi "Huh? What’s wrong with Buttcheeks?"

    show taiga angry2 at p7_7
    voice audio.taiga_v_dumbass1
    t "You talked over him, dumbass."

    show lloyd confused2 at p7_4
    voice audio.lloyd_v_confused2a2
    l "Also, he’s drying stuff outdoors… in winter? Wouldn’t it just get frozen? "

    show yoshi awkward4 at p7_1
    voice audio.yoshi_v_greet2b2
    yo "Ah, excuse me, guys. I need to catch up with Aiden."

    hide yoshi_winter2
    hide yoshi awkward4
    with dissolve

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

    $ location = location_lake
    show screen location
    show screen timeline
    show screen quick_menu
    $ quick_menu = True
    scene bg_lake_winter_day with fade
    play bgsound sfxloop_windy loop

    show aiden2_winter at center
    show aiden2 worry1 at center
    a "..."

    show aiden2_winter at right2
    show aiden2 worry1 at right2
    with move

    show yoshi_winter at left2
    show yoshi confused2 at left2
    with dissolve

    voice audio.yoshi_vsa20_line1
    yo "Hey, Aiden... What are you doing here?"

    hide aiden2_winter
    hide aiden2 worry1
    show aiden_winter at right2
    show aiden worry2 at right2
    voice audio.aiden_vsa20_line1
    a "Ah, Yoshi…!"

    hide yoshi_winter
    hide yoshi confused2
    show yoshi2_winter at left2
    show yoshi2 worry2 at left2
    voice audio.yoshi_vsa20_line2
    yo "Are you alright…? You’ve been acting off for a while now. "

    hide aiden_winter
    hide aiden worry2
    show aiden2_winter at right2
    show aiden2 worry5 at right2
    voice audio.aiden_vsa20_line2
    a "Wh-What? Am I?"

    show yoshi2 sad4 at left2
    voice audio.yoshi_vsa20_line3
    yo "Yeah… I mean, you were just trying to avoid the conversation…"

    show aiden2 worry1 at right2
    a "..."

    hide yoshi2_winter
    hide yoshi2 sad4
    show yoshi_winter at left2
    show yoshi worry3 at left2
    voice audio.yoshi_vsa20_line4
    yo "Look, I know you’re getting frustrated today with all the talk about the offer especially when you’re still thinking about it, but…"

    $ working = False
    $ shuffle_menu()
    menu():
        yo "Look, I know you’re getting frustrated today with all the talk about the offer especially when you’re still thinking about it, but…{fast}"
        "You're making everyone worry.":
            $ working = True
            $ score_aiden -= 2
            hide yoshi_winter
            hide yoshi worry3
            show yoshi2_winter at left2
            show yoshi2 sad6 at left2
            voice audio.yoshi_vsa20_line5a
            yo "You’re going to make everyone worry."
        "Obviously, you're upset.":
            $ working = True
            $ score_aiden -= 1
            hide yoshi_winter
            hide yoshi worry3
            show yoshi2_winter at left2
            show yoshi2 sad6 at left2
            voice audio.yoshi_vsa20_line5b
            yo "You're obviously upset, Aiden."

            voice audio.yoshi_vsa20_line6b
            yo "Tell me what's wrong."
        "You don't have to bottle it up.":
            $ working = True
            $ score_aiden += 1
            hide yoshi_winter
            hide yoshi worry3
            show yoshi2_winter at left2
            show yoshi2 sad6 at left2
            voice audio.yoshi_vsa20_line5c
            yo "You don't have to bottle up what you're feeling and deal with it on your own."
        "I need you to tell me what's on your mind.":
            $ working = True
            $ score_aiden += 2
            hide yoshi_winter
            hide yoshi worry3
            show yoshi2_winter at left2
            show yoshi2 sad6 at left2
            voice audio.yoshi_vsa20_line5d
            yo "Can you at least tell me what’s on your mind right now?"

            voice audio.yoshi_vsa20_line6d
            yo "I’ll listen…"

    show aiden2 upset1 at right2
    a "..."

    show aiden2 upset6 at right2
    voice audio.aiden_vsa20_line3
    a "*sigh* I… "

    voice audio.aiden_vsa20_line4
    a "I really don’t know, if I should take it or not, Yoshi…"

    show yoshi2 worry2 at left2
    voice audio.yoshi_vsa20_line7
    yo "What’s with the change of heart…? I thought you were already sure?"

    voice audio.yoshi_vsa20_line8
    yo "You were even so excited last night… especially when you were talking about your dad…"

    show aiden2 sad4 at right2
    voice audio.aiden_vsa20_line5
    a "Yeah… I know… "

    show yoshi2 worry3 at left2
    voice audio.yoshi_vsa20_line9
    yo "Are you worried it'd be difficult to adjust and learn the new skills? Or is it about the environment, like back at the hotel?"

    hide yoshi2_winter
    hide yoshi2 worry3
    show yoshi_winter at left2
    show yoshi comp2 at left2
    voice audio.yoshi_vsa20_line10
    yo "If you want, we can call Mr. Clermont right now and it’ll help clear your doubts!"

    voice audio.yoshi_vsa20_line11
    yo "Without knowing the details, it’s no wonder you’re feeling anxious and hesitant, so let’s fix that."

    show aiden2 panic2 at right2
    voice audio.aiden_vsa20_line6
    a "N-No it’s not that… I just—"

    show yoshi comp5 at left2
    voice audio.yoshi_vsa20_line12
    yo "I understand you’re feeling pressured about the whole thing, but I promise that you’ll be fine!"

    voice audio.yoshi_vsa20_line13
    yo "I’m here to help you!"

    hide aiden2_winter
    hide aiden2 panic2
    show aiden_winter at right2
    show aiden rage2 at right2
    show yoshi shock1 at left2
    voice audio.aiden_vsa20_line7
    a "Can we stop talking about the damn offer for one minute?!" with vpunch

    play music where_am_i loop
    yo "...!"

    show aiden rage4 at right2
    voice audio.aiden_vsa20_line8
    a "Everyone’s been bringing it up nonstop, all day long! It’s driving me insane! "

    voice audio.aiden_vsa20_line9
    a "I already told you I need more time to think about it!"

    show aiden rage6 at right2
    voice audio.aiden_vsa20_line10
    a "And I can’t think straight with all of you being so damn persistent!!" with vpunch

    hide aiden_winter
    hide aiden rage6
    show aiden2_winter at right2
    show aiden2 angry4 at right2
    $ renpy.pause (2.0, hard=True)
    a "..."

    hide yoshi_winter
    hide yoshi shock1
    show yoshi2_winter at left2
    show yoshi2 worry2 at left2
    voice audio.yoshi_vsa20_line14
    yo "I-I’m sorry, Aiden… I didn’t mean to be… "

    voice audio.yoshi_vsa20_line15
    yo "I’m just really confused with what changed all of a sudden…"

    show aiden2 upset5 at right2
    voice audio.aiden_vsa20_line11
    a "It’s because I already called Mr. Clermont…"

    show yoshi2 awkward4 at left2
    voice audio.yoshi_vsa20_line16
    yo "Wh-What…? When?"

    show aiden2 sigh1 at right2
    voice audio.aiden_vsa20_line12
    a "When I went to the office this morning… "

    voice audio.aiden_vsa20_line13
    a "I told him I was interested in the whole thing… and then he told me the details…"

    show yoshi2 worry5 at left2
    #jey
    voice audio.yoshi_vsa20_line17
    yo "What did he say?"

    show aiden2 sad4 at right2
    voice audio.aiden_vsa20_line14
    a "To get the certification I need, I have to enroll in the training course for it."

    voice audio.aiden_vsa20_line15
    a "He’s gonna sponsor everything, from my accommodations to the actual scholarships…"

    hide yoshi2_winter
    hide yoshi2 worry5
    show yoshi_winter at left2
    show yoshi talk3 at left2
    voice audio.yoshi_vsa20_line18
    yo "Oh, then that’s good news…! Isn’t it…? "

    show aiden2 sad5 at right2
    voice audio.aiden_vsa20_line16
    a "The catch is… it’d take at least two years… "

    show yoshi comp2 at left2
    voice audio.yoshi_vsa20_line19
    yo "That’s normal, though… it takes time to hone your craft! It’s what I went through to get my degree!"

    show aiden2 upset6 at right2
    voice audio.aiden_vsa20_line17
    a "Exactly… Just like what you had to do, I’d have to leave, too… and go abroad…"

    voice audio.aiden_vsa20_line18
    a "That means I won’t get to come back here ’til I finish the whole thing…"

    show aiden2 upset5 at right2
    voice audio.aiden_vsa20_line19
    a "And who knows, once I get the title and all, I’d have to work elsewhere too…"

    show yoshi confused2 at left2
    voice audio.yoshi_vsa20_line20
    yo "But that’s the whole point, right? It would be a waste if you work that hard and only end up back at Camp Buddy…"

    voice audio.yoshi_vsa20_line21
    yo "If that’s what it takes to finally pursue your lifelong dream, I’m sure it’d be worth it!"

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    show aiden2 upset2 at right2
    a "..."

    play music buddy_oath_aiden_sad loop
    hide aiden2_winter
    hide aiden2 upset2
    show aiden_winter at right2
    show aiden angry2 at right2
    voice audio.aiden_vsa20_line20
    a "I’m turning it down."

    hide yoshi_winter
    hide yoshi confused2
    show yoshi2_winter at left2
    show yoshi2 worry4 at left2
    voice audio.yoshi_vsa20_line22
    yo "Wh-What? "

    hide aiden_winter
    hide aiden angry2
    show aiden2_winter at right2
    show aiden2 sad5 at right2
    voice audio.aiden_vsa20_line21
    a "I don’t want to leave… "

    show yoshi2 worry2 at left2
    voice audio.yoshi_vsa20_line23
    yo "Wait, I don’t understand… Why?!"

    show aiden2 sad4 at right2
    voice audio.aiden_vsa20_line22
    a "I’d rather stay here… with you…"

    hide yoshi2_winter
    hide yoshi2 worry2
    show yoshi_winter at left2
    show yoshi worry2 at left2
    voice audio.yoshi_vsa20_line24
    yo "Aiden… It’s not like we’d never see each other again."

    voice audio.yoshi_vsa20_line25
    yo "Remember when I left to study? We made a promise that night on the rooftop that I’d come back. And I did!"

    show yoshi talk3 at left2
    voice audio.yoshi_vsa20_line26
    yo "This is basically the same thing, but it’s your turn this time!"

    voice audio.yoshi_vsa20_line27
    yo "And besides, I’m sure I can find a way to see you every once in a while, and you—"

    hide aiden2_winter
    hide aiden2 sad4
    show aiden_winter at right2
    show aiden rage2 at right2
    voice audio.aiden_vsa20_line23
    a "It’s not gonna be the same…!" with vpunch

    $ working = False
    $ shuffle_menu()
    menu():
        a "It’s not gonna be the same…!{fast}"
        "It's for your own good!":
            $ working = True
            $ score_aiden -= 2
            show yoshi worry5 at left2
            voice audio.yoshi_vsa20_line28a
            yo "I know it may not be as ideal and comfortable as you wanted it to be, but… it’s for your own good!"
        "There's a way to make it happen!":
            $ working = True
            $ score_aiden -= 1
            show yoshi worry5 at left2
            voice audio.yoshi_vsa20_line28b
            yo "Look, what I’m saying is, there’s a way we can solve what you’re worried about and achieve your dreams at the same time! A middle ground."
        "I know it's a lot...":
            $ working = True
            $ score_aiden += 1
            show yoshi worry5 at left2
            voice audio.yoshi_vsa20_line28c
            yo "I know it sounds overwhelming, but it'd be worth it in the end, I'm sure!"
        "I know you're afraid...":
            $ working = True
            $ score_aiden += 2
            show yoshi worry5 at left2
            voice audio.yoshi_vsa20_line28d
            yo "I understand why you’d be afraid of something like this, but I think it'll be worth it in the long run!"

    voice audio.yoshi_vsa20_line29
    yo "Don’t let me be the reason you stop reaching for your dream! "

    show aiden upset2 at right2
    voice audio.aiden_vsa20_line24
    a "Yoshi…! The more you corner me like this, the more I don’t want to!"

    $ working = False
    $ shuffle_menu()
    menu():
        a "Yoshi…! The more you corner me like this, the more I don’t want to!{fast}"
        "Don't be so shallow!":
            $ working = True
            $ score_aiden -= 2
            show yoshi angry2 at left2
            voice audio.yoshi_vsa20_line30a
            yo "Don’t be so shallow, Aiden!"

            show aiden rage6 at right2
            voice audio.aiden_vsa20_line25a
            a "Sh-Shallow?!"
        "I'm not forcing you!":
            $ working = True
            $ score_aiden -= 1
            show yoshi angry2 at left2
            voice audio.yoshi_vsa20_line30b
            yo "But I’m not forcing you, Aiden! I’m just trying to—"
        "I'm only thinking of what's best for you!":
            $ working = True
            $ score_aiden += 1
            show yoshi angry2 at left2
            voice audio.yoshi_vsa20_line30c
            yo "But I’m only thinking of what’s best for you, Aiden!"

            show aiden rage6 at right2
            voice audio.aiden_vsa20_line25c
            a "B-Best for me?!"
        "You can't just give up either!":
            $ working = True
            $ score_aiden += 2
            show yoshi angry2 at left2
            voice audio.yoshi_vsa20_line30d
            yo "Wh-What kind of reasoning is that? You can’t just give up, Aiden!"

            show aiden rage6 at right2
            voice audio.aiden_vsa20_line25d
            a "B-But I’m not giving up…!"

    show aiden rage2 at right2
    voice audio.aiden_vsa20_line26
    a "This just proves you don’t understand what I had to go through…!"

    voice audio.aiden_vsa20_line27
    a "Why are you even pushing this so hard?!"

    show aiden angry3 at right2
    voice audio.aiden_vsa20_line28
    a "I thought you told me that I was already good enough…?"

    voice audio.aiden_vsa20_line29
    a "That I didn’t need to be more than what I am today…"

    hide yoshi_winter
    hide yoshi angry2
    show yoshi2_winter at left2
    show yoshi2 panic4 at left2
    voice audio.yoshi_vsa20_line31
    yo "A-Aiden, th-that’s not what I meant… I-I just thought the time we’d be apart would be worth it for—  "

    show aiden rage5 at right2
    voice audio.aiden_vsa20_line30
    a "That’s easy for you to say, Yoshi! You’re the one who left me in the past, so how would you know anyway?!"

    hide aiden_winter
    hide aiden rage2
    with dissolve

    show yoshi2 sad1 at left2
    yo "..."

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black with fade
    yo "{i}Watching Aiden leave, I couldn’t even stop him… I was too stunned to say anything else…{/i}"
    yo "{i}Right away, I began to regret pushing Aiden, despite knowing how badly he’s been bothered today…{/i}"
    yo "{i}Hearing the pain and frustration in his voice, I feel like I failed Aiden… Especially since there’s something about him that I don’t understand even after all these years.{/i}"

    scene cg black
    hide screen location
    hide screen timeline
    hide screen quick_menu
    $ quick_menu = False
    with fade
    $ time_transition_day_to_sunset_winter2()
    $ renpy.pause (2.0, hard=True)

    $ location = location_campsite
    $ time = timeline_timesunset
    show screen location
    show screen timeline
    show screen quick_menu
    $ quick_menu = True
    scene bg_campgrounds_winter_sunset with fade
    play music buddy_oath_goro_sad loop

    show yoshi2_winter at center
    show yoshi2 worry2 at center
    voice audio.yoshi_v_aiden4
    yo "Aiden… Where are you…?"

    show yoshi2_winter at left2
    show yoshi2 worry2 at left2
    with move

    show goro_winter at right2
    show goro talk2 at right2
    with dissolve

    voice audio.goro_v_yoshi7
    g "Yoshinori…?"

    hide yoshi2_winter
    hide yoshi2 worry2
    show yoshi_winter at left2
    show yoshi panic2 at left2
    voice audio.yoshi_v_sirgoro1
    yo "Sir Goro…!"

    show goro confused2 at right2
    voice audio.goro_v_worry2b
    g "I just got back. Are you alright…? You look troubled…"

    hide yoshi_winter
    hide yoshi panic2
    show yoshi2_winter at left2
    show yoshi2 sad4 at left2
    voice audio.yoshi_v_sorry2a
    yo "I-I’m sorry, sir… I was just looking for Aiden… He ran off and I can’t find him…"

    show goro shock2 at right2
    voice audio.goro_v_confused1a1
    g "Huh? What happened?"

    show yoshi2 upset6 at left2
    voice audio.yoshi_v_well3
    yo "We… had an argument a while ago, and he left before we could properly resolve it…"

    show goro worry3 at right2
    voice audio.goro_v_really4b
    g "Really? You two almost never argue… Mind if I ask what was it about? "

    show yoshi2 sigh1 at left2
    voice audio.yoshi_v_actually2a
    yo "Aiden was worried about the offer from Mr. Clermont, and everyone tried to give advice when they found out. "
    yo "It only made him more anxious, so I tried to motivate him to accept it."

    show yoshi2 upset5 at left2
    voice audio.yoshi_v_but2
    yo "But he ultimately decided not to take it, just because he’d be separated from Camp Buddy… and me…"

    hide goro_winter
    hide goro worry3
    show goro2_winter at right2
    show goro2 sad1 at right2
    g "..."

    hide yoshi2_winter
    hide yoshi2 upset5
    show yoshi_winter at left2
    show yoshi worry2 at left2
    voice audio.yoshi_v_sigh3a
    yo "I wanted him to realize that he can finally achieve the dream he wanted for so long…"
    yo "And that he shouldn’t turn it down just because he’s afraid of the future…"

    hide yoshi_winter
    hide yoshi worry2
    show yoshi2_winter at left2
    show yoshi2 sad4 at left2
    voice audio.yoshi_v_sad1
    yo "But the way I handled it only made things worse."

    show goro2 sad2 at right2
    voice audio.goro_v_isee4a
    g "I see…"

    show yoshi2 worry3 at left2
    voice audio.yoshi_v_unsure1b
    yo "It just doesn’t make sense why he’d give up like that…"
    yo "I’ve been with him long enough to know he’s the kind of person who always perseveres no matter what…"

    show yoshi2 worry4 at left2
    voice audio.yoshi_v_why1
    yo "So why did something like this make him crumble?"

    hide goro2_winter
    hide goro2 sad2
    show goro_winter at right2
    show goro sad3 at right2
    voice audio.goro_v_yoshi4
    g "Aiden must have a reason that stems from something much deeper, Yoshinori… "
    g "If pursuing his passion would mean he’d be away from all of us, and that was enough for him to turn away from his dream… "

    show goro sigh1 at right2
    voice audio.goro_v_sigh1a
    g "Then he must be afraid of being alone again…"
    g "After all, we all know what happened with his father…"

    show yoshi2 sad6 at left2
    voice audio.yoshi_v_yessir4
    yo "…Yes, sir."

    show goro sad3 at right2
    voice audio.goro_v_well1a
    g "None of us were with Aiden when Andre passed…"
    g "I’m sure you can imagine how difficult that must’ve been to handle on his own…"

    show yoshi2 sad1 at left2
    yo "..."

    show goro sad2 at right2
    voice audio.goro_v_so1a
    g "As much as we wish we could’ve been there for him, we were all on our own separate paths after the first term."
    g "After you left for your studies, Aiden and Andre had to leave too."

    hide yoshi2_winter
    hide yoshi2 sad1
    show yoshi_winter at left2
    show yoshi panic2 at left2
    voice audio.yoshi_v_what3
    yo "Wh-What…? I-I didn’t know that…"
    yo "I thought all along that Aiden stayed at Camp Buddy until his dad passed away."

    hide goro_winter
    hide goro sad2
    show goro2_winter at right2
    show goro2 think5 at right2
    voice audio.goro_v_think1a1
    g "Hmm… It seems Aiden kept that from you then…"
    g "I don’t have any right to talk about his personal life to others, but I think it would help you understand better if you knew how things happened…"

    show cg_fade at truecenter
    show fxa10 at fx_pos with dissolve

    voice audio.goro_vsa212_line1
    g "Once the term was over, Andre began struggling with the work around camp due to an illness."

    voice audio.goro_vsa212_line2
    g "I knew about his health from when he applied to the camp, but he wanted to keep it hidden from everyone."

    voice audio.goro_vsa212_line3
    g "It didn't affect his ability to work at first, but eventually he needed medical treatment."

    voice audio.goro_vsa212_line4
    g "He didn't have enough money to afford all the expenses, so I insisted on contributing to help him."

    voice audio.goro_vsa212_line5
    g "His condition continued to worsen until he could no longer work at the camp, and Aiden focused on both caring for him and taking over his job."

    voice audio.goro_vsa212_line6
    g "Even though I offered for them to continue staying at the camp and helping with their bills, Andre ultimately decided it was best for he and Aiden to no longer continue to burden the camp, so they left."

    hide fxa10
    show fxa11 at fx_pos with Dissolve(0.25)
    voice audio.goro_vsa212_line7
    g "I'll never forget the gratitude in his smile and the hopefulness in his face, so I respected his decision and let them go."

    voice audio.goro_vsa212_line8
    g "That was the last time I heard from him… "

    hide fxa11
    hide cg_fade
    with dissolve

    hide yoshi_winter
    hide yoshi panic2
    show yoshi2_winter at left2
    show yoshi2 panic4 at left2
    voice audio.yoshi_v_sorry6b
    yo "I can't believe I didn't know about this... How were they able to find work or a place to stay after they left with Andre being sick?"

    hide goro2_winter
    hide goro2 think5
    show goro_winter at right2
    show goro sigh4 at right2
    voice audio.goro_v_think1a1
    g "That... I'm not sure. All we know is how things ended up."

    show yoshi2 sad1 at left2
    yo "..."

    show goro talk1 at right2
    voice audio.goro_v_but1a
    g "But the reason I'm telling you this is to give you a different perspective on why Aiden might have made the decision he did."
    g "Knowing how much Aiden endured in his past will help you understand his actions today."

    $ working = False
    $ shuffle_menu()
    menu():
        g "Knowing how much Aiden endured in his past will help you understand his actions today.{fast}"
        "I can still change his mind.":
            $ working = True
            $ score_aiden -= 2
            hide yoshi2_winter
            hide yoshi2 sad1
            show yoshi_winter at left2
            show yoshi worry2 at left2
            voice audio.yoshi_v_but2
            yo "But the past shouldn’t affect his future... There must be a way I can still change his mind!"

            hide goro_winter
            hide goro talk1
            show goro2_winter at right2
            show goro2 explain2 at right2
            voice audio.goro_v_ehem1a
            g "Just remember to not lose track of what matters most, Yoshinori. "

            hide goro2_winter
            hide goro2 explain2
            show goro_winter at right2
            show goro talk3 at right2
            g "Now, go find him… I’m sure he’s waiting for you"
        "It's up to him to decide.":
            $ working = True
            $ score_aiden -= 1
            hide yoshi2_winter
            hide yoshi2 sad1
            show yoshi_winter at left2
            show yoshi angry2 at left2
            voice audio.yoshi_v_right5
            yo "That’s right. No matter my opinion, it's up to him to decide."

            hide goro_winter
            hide goro talk1
            show goro2_winter at right2
            show goro2 explain2 at right2
            voice audio.goro_v_ehem1a
            g "What you say to him still matters, Yoshinori."

            hide goro2_winter
            hide goro2 explain2
            show goro_winter at right2
            show goro talk3 at right2
            g "Now, go find him… I’m sure he’s waiting for you"
        "I'll support him no matter what.":
            $ working = True
            $ score_aiden += 1
            hide yoshi2_winter
            hide yoshi2 sad1
            show yoshi_winter at left2
            show yoshi angry2 at left2
            voice audio.yoshi_v_right5
            yo "That’s right... I need to support him no matter what choice he makes."

            show goro talk3 at right2
            voice audio.goro_v_rush4b2
            g "Now, go find Aiden, Yoshinori… I’m sure he’s waiting for you."
        "His happiness is what matters.":
            $ working = True
            $ score_aiden += 2
            hide yoshi2_winter
            hide yoshi2 sad1
            show yoshi_winter at left2
            show yoshi angry2 at left2
            voice audio.yoshi_v_right5
            yo "That’s right… Aiden’s happiness is what matters the most!"
            yo "I’m going to do whatever it takes for him!"

            show goro talk3 at right2
            voice audio.goro_v_rush4b2
            g "Now, go find Aiden, Yoshinori… I’m sure he’s waiting for you."

    show yoshi talk1 at left2
    voice audio.yoshi_v_right3
    yo "Right…! Thank you, sir!"

    hide yoshi_winter
    hide yoshi talk1
    with dissolve

    if score_aiden <= 0:
        $ renpy.music.stop(channel='music', fadeout = 1.0)
        $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
        $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
        scene cg black
        hide screen location
        hide screen timeline
        hide screen quick_menu
        $ quick_menu = False
        with fade
        $ time_transition_sunset_to_night_winter2()
        $ time = timeline_timenight
        $ renpy.pause (2.0, hard=True)

        jump day9_aiden_we
    elif score_aiden > 0 and score_aiden <=24:
        $ renpy.music.stop(channel='music', fadeout = 1.0)
        $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
        $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
        scene cg black
        hide screen location
        hide screen timeline
        hide screen quick_menu
        $ quick_menu = False
        with fade
        $ time_transition_sunset_to_night_winter2()
        $ time = timeline_timenight
        $ renpy.pause (2.0, hard=True)

        jump day9_aiden_be
    elif score_aiden > 24 and score_aiden <= 49:
        $ renpy.music.stop(channel='music', fadeout = 1.0)
        $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
        $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
        scene cg black
        hide screen location
        hide screen timeline
        hide screen quick_menu
        $ quick_menu = False
        with fade
        $ time_transition_sunset_to_night_winter2()
        $ time = timeline_timenight
        $ renpy.pause (2.0, hard=True)

        jump day9_aiden_ge_pe
    else:
        $ renpy.music.stop(channel='music', fadeout = 1.0)
        $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
        $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
        scene cg black
        hide screen location
        hide screen timeline
        hide screen quick_menu
        $ quick_menu = False
        with fade
        $ time_transition_sunset_to_night_winter3()
        $ time = timeline_timenight
        $ renpy.pause (2.0, hard=True)

        jump day9_aiden_ge_pe
