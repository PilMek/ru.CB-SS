label day8_aiden:
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

    show aiden_sleep at left2
    show aiden happy2 at left2
    show yoshi2_sleep at right2
    show yoshi2 sleepy6 at right2
    voice audio.aiden_v_goodam1a2
    a "Good morning, Yoshi!"

    show yoshi2 sleepy6 at right2
    voice audio.yoshi_v_yawn1
    yo "*yawn* Good morning. I’m still feeling a bit groggy. "

    show aiden laugh1 at left2
    voice audio.aiden_v_laugh2a1
    a "Haha, seems like you might’ve partied a bit too much last night."

    show yoshi2 sleepy4 at right2
    voice audio.yoshi_v_yeah4
    yo "Y-Yeah… It’s been a while since Yuri let us all drink at the camp. And you know I have a pretty low tolerance for liquor…"

    show aiden comp5 at left2
    voice audio.aiden_v_agree4b
    a "Haha, same, but I held back on the beers this time – don’t wanna wake up to our sponsorship getting cancelled ’cause I lost all my clothes again!  "

    hide yoshi2_sleep
    hide yoshi2 sleepy4
    show yoshi_sleep at right2
    show yoshi laugh1 at right2
    voice audio.yoshi_v_laugh1
    yo "Hahaha!"
    yo "Where is everybody? Did I wake up late again…?"

    show aiden talk4 at left2
    voice audio.aiden_v_no2a1
    a "No, you didn’t! I actually woke up just a bit before you. "
    a "Lloyd and Darius are at the site doing some minor repairs before the workers arrive."

    show yoshi talk3 at right2
    voice audio.yoshi_v_right6
    yo "Oh right, they should be showing up in just a couple of days."

    show aiden explain2 at left2
    voice audio.aiden_v_well1a3
    a "Jin’s over at the mess hall having some coffee, and Gramps is in his office with Mr. Clermont."

    show yoshi confused2 at right2
    voice audio.yoshi_v_really1
    yo "I’m surprised Mr. Clermont hasn’t left yet. "

    show aiden explain3 at left2
    voice audio.aiden_v_unsure5b1
    a "Well, the holidays are just around the corner, so work must be slow for him right now."

    show aiden happy1 at left2
    voice audio.aiden_v_anyway1a
    a "Anyways, Yuri and Emilia left a while ago to take the scouts back home."

    show yoshi awkward4 at right2
    voice audio.yoshi_v_ah4
    yo "A-Ah, they didn’t have to do that! I was planning on driving them back today!"

    show aiden laugh2 at left2
    voice audio.aiden_v_laugh2a1
    a "Haha, I think Yuri wanted to sneak in some more time with them for her usual questioning."
    a "She’s probably gonna be talking about ‘cracks’ and ‘ships’ the entire way, whatever that means."

    hide yoshi_sleep
    hide yoshi awkward4
    show yoshi2_sleep at right2
    show yoshi2 comp6 at right2
    voice audio.yoshi_v_laugh6
    yo "Ahehe, I wonder how Emilia will deal with that…"

    show aiden play2 at left2
    voice audio.aiden_v_conj3a1
    a "Haha, with any luck, she’ll keep Yuri from going too crazy."

    hide yoshi2_sleep
    hide yoshi2 comp6
    show yoshi_sleep at right2
    show yoshi happy2 at right2
    voice audio.yoshi_v_well1
    yo "Well, it sounds like everyone is settling in again, at least. "

    hide aiden_sleep
    hide aiden play2
    show aiden2_sleep at left2
    show aiden2 sigh4 at left2
    voice audio.aiden_v_hngh1b3
    a "Yeah, it’s time to get back to the grind, even though I’m dragging a little bit."

    show yoshi think2 at right2
    voice audio.yoshi_v_yeah1
    yo "Me, too… Or maybe that’s just the hangover. "

    hide aiden2_sleep
    hide aiden2 sigh4
    show aiden_sleep at left2
    show aiden comp2 at left2
    voice audio.aiden_v_unsure6b
    a "Probably both."

    show yoshi talk1 at right2
    voice audio.yoshi_v_rush1
    yo "Oh well, I guess we better start our day as well and see what we can work on."

    show aiden happy1 at left2
    voice audio.aiden_v_agree3a2
    a "Sure, Yoshi! What’s the plan for today?"

    $working = False
    $shuffle_menu()
    menu():
        a "Sure, Yoshi! What’s the plan for today?{fast}"
        "Check on the construction.":
            $ working = True
            show yoshi talk2 at right2
            voice audio.yoshi_v_think4
            yo "Why don’t we head over to the construction site?"
            yo "Darius and Lloyd might need an extra pair of hands with the repairs."

            show aiden bold2 at left2
            voice audio.aiden_v_alright1a1
            a "Sure, I could use the exercise! "

            show yoshi happy2 at right2
            voice audio.yoshi_v_rush5
            yo "Let’s head over there!"

            jump day8_aiden_darius
        "Make the daily report.":
            $ working = True
            show yoshi talk2 at right2
            voice audio.yoshi_v_think4
            yo "We should go and make our daily report to Sir Goro. "

            show aiden tease1 at left2
            voice audio.aiden_v_laugh1b2
            a "You sure you wanna disturb him and Mr. Clermont? We could be interrupting something, hehe~"

            hide yoshi_sleep
            hide yoshi talk2
            show yoshi2_sleep at right2
            show yoshi2 shy5 at right2
            voice audio.yoshi_v_no4
            yo "I-I’m sure they’re just having a normal morning, Aiden."

            show aiden tease2 at left2
            voice audio.aiden_v_perv1
            a "You’re right, they probably did all the fun stuff last night."

            show yoshi2 sigh1 at right2
            voice audio.yoshi_v_sigh3a
            yo "*sigh* Come on, let’s go."

            show aiden laugh1 at left2
            voice audio.aiden_v_laugh2a1
            a "Hahaha, alright!"

            jump day8_aiden_goro
        "Have some breakfast.":
            $ working = True
            show yoshi talk2 at right2
            voice audio.yoshi_v_rush5
            yo "Let’s head over to the mess hall before we start our day. "

            show aiden happy1 at left2
            voice audio.aiden_v_agree3a1
            a "Sure thing! I can whip up a nice breakfast for you~!"

            jump day8_aiden_jin
        "Walk around the camp.":
            $ working = True
            show yoshi talk2 at right2
            voice audio.yoshi_v_think4
            yo "Why don’t we walk around for some fresh air first before we get to work?"

            show aiden play2 at left2
            voice audio.aiden_v_laugh1b2
            a "Hehe, trying to shake off your hangover?"

            hide yoshi_sleep
            hide yoshi talk2
            show yoshi2_sleep at right2
            show yoshi2 comp6 at right2
            voice audio.yoshi_v_yeah4
            yo "Y-Yeah, haha. Don’t want everyone thinking I partied too hard."

            show aiden happy1 at left2
            voice audio.aiden_v_rush1a1
            a "Let’s get dressed and go then!"

            jump day8_aiden_emilia

label day8_aiden_darius:
    $darius_ending = True
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
    scene bg_site6_winter_day with fade
    play music sunset_stroll_winter loop
    play bgsound sfx_construction loop

    show darius_workw at left2
    show darius_goggles2 at left2
    show darius happy2 at left2
    show taiga_winter at right2
    show taiga talking4 at right2
    voice audio.darius_v_sarcastic1c
    d "So, the framing where you place the actual roofing are called trusses."
    d "The reason why the webbings are assembled in a certain pattern is so that everything behaves as a single, rigid structure."

    show taiga talking4 at right2
    voice audio.taiga2_v_surprised1a
    t "Ohh… I’ve always wondered why it’s like that. Now I know."
    t "I have so much to learn when it comes to building stuff…"

    show darius explain4 at left2
    voice audio.darius_v_comp3a
    d "That’s okay. I only ever learned these things from my engineering course, and on-site experience."

    show taiga compassion3 at right2
    voice audio.taiga2_v_determined1a
    t "Teach me more about repairing, I think it’ll come in handy around here!  "

    show darius comp3 at left2
    voice audio.darius_v_praise2a
    d "With how interested you are, you’ll learn quick."

    show taiga grin2 at right2
    voice audio.taiga2_v_laugh1c
    t "Hehe, you think so?"

    show darius bold2 at left2
    voice audio.darius_v_agree1a
    d "Yes."

    show darius_workw at p4_3
    show darius_goggles2 at p4_3
    show darius bold2 at p4_3
    show taiga_winter at p4_4
    show taiga grin2 at p4_4
    with move

    show yoshi_winter2 at p4_1
    show yoshi norm1 at p4_1
    show aiden_winter2 at p4_2
    show aiden happy2 at p4_2
    with dissolve

    voice audio.aiden_v_hey2a2
    a "Hey, guys! "

    show yoshi happy2 at p4_1
    voice audio.yoshi_v_think1a
    yo "Looks like you guys are doing repairs as planned, and since we have some free time, we thought we’d come help!"

    show darius happy1 at p4_3
    voice audio.darius_v_celebrate1a
    d "Sure. The more, the merrier."

    show yoshi bold5 at p4_1
    voice audio.yoshi_v_taiga3
    yo "I see Taiga is helping out too! You should know he’s quite the craftsman!"

    show taiga compassion6 at p4_4
    voice audio.taiga2_v_denial3a
    t "Psh… Hardly."

    show darius laugh3 at p4_3
    voice audio.darius_v_amazed1
    d "He’s keeping up pretty nicely."
    d "And I heard you taught him a lot of woodworking yourself, Yoshi."

    show yoshi happy1 at p4_1
    voice audio.yoshi_v_oh1
    yo "Oh yeah! We worked together on some minor repairs and furniture assembly!"

    show darius amazed1 at p4_3
    voice audio.darius_v_laugh1
    d "You have a promising builder then."

    show taiga_winter at p4_4
    show taiga compassion1 at p4_4
    t "..."

    show aiden comp3 at p4_2
    voice audio.aiden_v_aww3a
    a "Aww~ He’s not used to being praised this much, hahaha!"

    show yoshi_winter2 at p5_1
    show yoshi happy1 at p5_1
    show aiden_winter2 at p5_2
    show aiden comp3 at p5_2
    show darius_workw at p5_3
    show darius_goggles2 at p5_3
    show darius amazed1 at p5_3
    show taiga_winter at p5_4
    show taiga compassion1 at p5_4
    with move

    show lloyd_work2 at p5_5
    show lloyd happy1 at p5_5
    with dissolve

    voice audio.lloyd_v_greet1a3
    l "Ah, perfect! You guys are here!"

    show yoshi talk3 at p5_1
    voice audio.yoshi_v_lloyd3
    yo "Oh hey, Lloyd! I was wondering where you were."

    show lloyd awkward3 at p5_5
    voice audio.lloyd_v_confused2a1
    l "I’m drawing some layouts and planning out the repairs, and uhh…"
    l "I kinda need help with the measurements because… I can’t reach them."

    hide taiga_winter
    hide taiga compassion1
    show taiga_winter at p5_4
    show taiga playful2 at p5_4
    voice audio.taiga_v_heh1
    t "Pfft. Arms too short?"

    show lloyd angry2 at p5_5
    voice audio.lloyd_v_greet2c1
    l "Hey! You’re not any taller!"

    show taiga sigh2 at p5_4
    voice audio.taiga_v_thinking1a
    t "I actually am though…"

    show yoshi bold2 at p5_1
    voice audio.yoshi_v_confident2
    yo "I can help you out! We came to assist you, after all!"

    show lloyd talk1 at p5_5
    voice audio.lloyd_v_rush1a2
    l "Ah perfect! Come with me then!"

    hide yoshi_winter2
    hide yoshi bold2
    hide lloyd_work2
    hide lloyd talk1
    with dissolve

    show taiga surprised2 at p5_4
    voice audio.taiga2_v_hey1h
    t "H-Hey, you forgot your measuring tape!"

    hide taiga_winter
    hide taiga surprised2
    with dissolve

    show aiden_winter2 at left2
    show aiden talk2 at left2
    show darius_workw at right2
    show darius_goggles2 at right2
    show darius amazed1 at right2
    with move

    voice audio.aiden_v_so2
    a "So, is there anything I can help with around here, bro?"

    show darius shy4 at right2
    voice audio.darius_v_agree1a
    d "Yes. But it’s not about the repairs."

    hide aiden_winter2
    hide aiden talk2
    show aiden2_winter2 at left2
    show aiden2 confused2 at left2
    voice audio.aiden_v_confused1a2
    a "Eh? "

    show darius confused5 at right2
    voice audio.darius_v_conj2a
    d "I need some advice."

    show aiden2 confused5 at left2
    voice audio.aiden_v_confused2a2
    a "Advice? From me? "

    show darius sigh4 at right2
    voice audio.darius_v_agree1b
    d "Yes…"

    hide aiden2_winter2
    hide aiden2 confused5
    show aiden_winter2 at left2
    show aiden happy2 at left2
    voice audio.aiden_v_greet1a
    a "Sure, What’s on your mind, big guy?"

    show darius talk3 at right2
    voice audio.darius_v_conj2b
    d "W-Well, I noticed how you and Yoshinori have gotten closer over the span of the project."
    d "And I was wondering what you did to take things to the next level?"

    hide aiden_winter2
    hide aiden happy2
    show aiden2_winter2 at left2
    show aiden2 awkward6 at left2
    voice audio.aiden_v_think2a
    a "Oh… Umm… Well, it depends on the situation actually… Is this about you and Lloyd?"

    show darius think1 at right2
    voice audio.darius_v_agree1b
    d "Yes."

    show aiden2 worry5 at left2
    voice audio.aiden_v_worry2a
    a "Why, is there something wrong? "

    show darius think2 at right2
    voice audio.darius_v_no1a
    d "No…"
    d "It’s just… We’ve been working together for the past decade and… we’ve stayed the same for years…"

    hide aiden2_winter2
    hide aiden2 worry5
    show aiden_winter2 at left2
    show aiden think5 at left2
    voice audio.aiden_v_really1b
    a "Isn’t that a good thing, though?"

    show darius talk1 at right2
    voice audio.darius_v_agree2c
    d "It is. But I want us to be more."

    hide aiden_winter2
    hide aiden think5
    show aiden2_winter2 at left2
    show aiden2 comp5 at left2
    voice audio.aiden_v_aww3a
    a "Aw, shucks, this is way too familiar for me, haha!"

    show darius think5 at right2
    voice audio.darius_v_agree2a
    d "It was obvious you and Yoshi were into each other when we were scouts, but it took a long time for you to make it official."

    show darius sigh2 at right2
    voice audio.darius_v_lloyd4a
    d "Meanwhile, Lloyd and I are stuck on that same label we were in the past."
    d "We’re still just… friends."

    show darius confused2 at right2
    voice audio.darius_v_sarcastic1c
    d "So, how did you do it?"

    show aiden2 think2 at left2
    voice audio.aiden_v_think1a1
    a "It’s kinda complicated to tell the whole story, but if I were to sum it up in one word, I guess it’s… communication?"

    show darius shy6 at right2
    voice audio.darius_v_think1a1
    d "I’m really embarrassed to start that conversation. It’s not like me to bring something up like that… Lloyd will be suspicious."

    show aiden2 play2 at left2
    voice audio.aiden_v_well1b2
    a "Well… have you tried the… you know… ol’ reliable sausage fight?"
    a "I mean that usually adds a lot of fuel to the flame."

    show darius confused5 at right2
    voice audio.darius_v_conj1a2
    d "We do… quite often."
    d "But afterwards, Lloyd acts as if nothing happened. "

    show aiden2 think6 at left2
    voice audio.aiden_v_think1a1
    a "Hmm… Lloyd’s not exactly shy with his thoughts, but it’s usually only about his own feelings."
    a "He doesn’t really pry into others unless he has to."

    show darius think1 at right2
    voice audio.darius_v_think1a1
    d "Sounds about right."

    hide aiden2_winter2
    hide aiden2 think6
    show aiden_winter2 at left2
    show aiden explain1 at left2
    voice audio.aiden_v_conj2a1
    a "Meanwhile, you’re normally a quiet and reserved guy who doesn’t show much emotion, either."
    a "It’s like you two are on opposite wavelengths!"

    show aiden happy2 at left2
    voice audio.aiden_v_lloyd2a
    a "I bet Lloyd feels the same way, but he’s holding back ’cause he thinks you’re comfortable with how things are."

    show darius talk1 at right2
    voice audio.darius_v_ah1c1
    d "I see… "

    show aiden comp2 at left2
    voice audio.aiden_v_encourage1a
    a "Try and talk to him, big guy! Let him know that there’s a fire in you that you want to share with him!"

    show aiden comp6 at left2
    voice audio.aiden_v_comp3a
    a "I totally get why it’s so hard to even bring something like that up, though… ’Cause sometimes we get too afraid, like what if the other person isn’t thinking the same, and we’re just risking what we already have?"
    a "But on the other hand, you can’t get any further if you keep playing it safe."

    show darius think4 at right2
    d "..."

    show darius sigh1 at right2
    voice audio.darius_v_agree3
    d "You’re right."
    d "I’ll do my best to communicate more. "

    show aiden bold2 at left2
    voice audio.aiden_v_actually1a
    a "You just did it with me! Use that same energy with Lloyd, and you’ll find your answers!"

    show darius comp2 at right2
    voice audio.darius_v_think2a1
    d "Thank you Aiden. I know what to do now."

    show aiden grin3 at left2
    voice audio.aiden_v_amazed1a1
    a "Awesome! I’m glad I was able to help you some!"

    show aiden_winter2 at left
    show aiden grin3 at left
    show darius_workw at center
    show darius_goggles2 at center
    show darius comp2 at center
    with move

    show lloyd_work2 at right
    show lloyd confused2 at right
    with dissolve

    voice audio.lloyd_v_darius4a
    l "Uhhh… Dar? I need another tall guy around… "

    show darius_workw at right2
    show darius_goggles2 at right2
    show darius smile3 at right2
    with move

    d "*pats Lloyd’s head*"

    show lloyd_blush2 at right
    show lloyd shock6 at right
    voice audio.lloyd_v_confused1b1
    l "H-huh…? What was that about?"

    hide aiden_winter2
    hide aiden bold5
    show aiden2_winter2 at left
    show aiden2 kiss1 at left
    voice audio.aiden_v_whistle2a
    a "*whistles*"

    show lloyd rage3 at right
    voice audio.lloyd_v_greet2c1
    l "H-Hey, what the heck did you two just talk about?!"

    hide aiden2_winter2
    hide aiden2 kiss1
    show aiden_winter2 at left
    show aiden play2 at left
    voice audio.aiden_v_no1a1
    a "Nothing~ I’m gonna go and work with Yoshi now! "

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black with fade
    yo "{i}Aiden and I spent the afternoon helping Lloyd and Darius with some of the repairs at the construction site.{/i}"
    yo "{i}Darius kept on making these strange flirty gestures at Lloyd, which seemed to fluster him too…{/i}"
    yo "{i}It was odd, but I’m glad to see them acting even closer!{/i}"
    yo "{i}Eventually, we finished with the repairs and headed back to our cabin.{/i}"

    jump day8_aiden_aftersq

label day8_aiden_goro:
    $sq_goro += 1
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
    play music old_familiar_home loop

    #play sound sfx_puppies
    show yoichi_winter at left
    show yoichi excited1 at left
    with moveinleft

    hide yoichi_winter
    hide yoichi excited1
    with moveoutright

    show goro_winter2 at center
    show goro_vein at center
    show goro irked3 at center
    with dissolve

    voice audio.goro_v_yoichi5b
    g "Yoichi! Would you stop running around already?! You’re not supposed to chase after them!"

    show yoichi_winter at left
    show yoichi angry1 at left
    with moveinleft

    voice audio.yoichi_v_request1a1
    yi "Shut up, old geezer! We’re having fun! "

    hide yoichi_winter
    hide yoichi angry1
    with moveoutright

    hide goro_vein
    show goro_winter2 at left
    show goro irked3 at left
    with move

    show yoshi_winter2 at center
    show yoshi talk3 at center
    show aiden_winter2 at right
    show aiden norm1 at right
    with dissolve

    voice audio.yoshi_v_oh1
    yo "Oh, Sir Goro! I thought you were in the office."

    show aiden talk2 at right
    voice audio.aiden_v_yeah1e2
    a "Yeah, and isn’t Mr. Clermont with you?"

    show goro talk1 at left
    voice audio.goro_v_actually1a
    g "He’s taking a short nap."

    show aiden tease1 at right
    voice audio.aiden_v_goro10a
    a "Hehe, you wore him out that bad, huh, Gramps? "

    hide yoshi_winter2
    hide yoshi talk3
    show yoshi2_winter2 at center
    show yoshi2 awkward3 at center
    voice audio.yoshi_v_aiden6
    yo "A-Aiden, he’s probably just a little tired from the party."

    hide goro_winter2
    hide goro talk1
    show goro2_winter2 at left
    show goro2 explain2 at left
    voice audio.goro_v_ehem1a
    g "*ehem* Exactly, Yoshinori."

    hide goro2_winter2
    hide goro2 explain2
    show goro_winter2 at left
    show goro talk1 at left
    voice audio.goro_v_anyway2
    g "Anyway, I wanted to give him some privacy and decided to step outside for a walk."
    g "It just so happens that I stumbled upon Yoichi here playing with his puppies and—"

    show goro rage1 at left
    voice audio.goro_v_yoichi4a
    g "Yoichi, stop peeing in the snow! "

    voice audio.yoichi_v_request1c1
    yi "Shut up! I can piss wherever I want! "

    hide goro_winter2
    hide goro rage1
    show goro2_winter2 at left
    show goro2 sigh4 at left
    voice audio.goro_v_sigh1a
    g "*sigh* How do you control this scout, Yoshinori…"

    hide yoshi2_winter2
    hide yoshi2 awkward3
    show yoshi_winter2 at center
    show yoshi comp5 at center
    voice audio.yoshi_v_laugh1
    yo "Haha, it takes quite a bit of getting used to."
    yo "Yoichi can be just as wild as his puppies. "

    hide goro2_winter2
    hide goro2 sigh4
    show goro_winter2 at left
    show goro talk3 at left
    voice audio.goro_v_agree8a1
    g "That’s true. And normally, I don’t mind letting him and the pups run around during the off-season."
    g "But with Mr. Clermont here, I want to make sure there’s no incidents."

    show yoshi comp3 at center
    voice audio.yoshi_v_right2
    yo "That makes sense."

    show goro_winter2 at p4_2
    show goro talk3 at p4_2
    show yoshi_winter2 at p4_3
    show yoshi comp3 at p4_3
    show aiden_winter2 at p4_4
    show aiden tease1 at p4_4
    with move

    show yoichi_winter at p4_1
    show yoichi laugh2 at p4_1
    with dissolve

    voice audio.yoichi_v_laugh1d1
    yi "Hahaha! Who’s the fluffy pups? Yes, you are!"

    show aiden talk4 at p4_4
    voice audio.aiden_v_amazed2a1
    a "Wow, they really love to play in the snow, huh?"

    show yoichi talking2 at p4_1
    voice audio.yoichi_v_agree1b1
    yi "Yeah! It’s their first winter, and I think this is their new favorite weather!"

    show yoshi comp2 at p4_3
    voice audio.yoshi_v_unsure3a
    yo "I guess they were still too little to be active during the summer and fall, too. "

    show goro happy2 at p4_2
    voice audio.goro_v_laugh2a
    g "I have to admit, I have gotten quite attached to these pups over the last few months."

    show yoshi laugh2 at p4_3
    voice audio.yoshi_v_laugh1
    yo "Haha, you do spend a lot of time with them now, sir."
    yo "I think the puppies might like you more than me actually!"

    show yoichi confused2 at p4_1
    voice audio.yoichi_v_agree1a2
    yi "Yeah, for some weird reason they like this old geezer. "
    yi "Are you secretly bribing them with food like Sheriff Brokeback over here?"

    show goro laugh3 at p4_2
    voice audio.goro_v_comp2a1
    g "Haha not at all, Yoichi. I leave their care one hundred percent to you."

    show aiden play2 at p4_4
    voice audio.aiden_v_unsure5b1
    a "Maybe they just like the way Gramps smells."

    show yoichi panic3 at p4_1
    voice audio.yoichi_v_shock3a6
    yi "Gah! Stay away from my pups before you contaminate them with your old-man-stink!"

    hide yoichi_winter
    hide yoichi panic3
    with moveoutleft

    show goro_winter2 at left
    show goro laugh3 at left
    show yoshi_winter2 at center
    show yoshi comp2 at center
    show aiden_winter2 at right
    show aiden play2 at right
    with move

    voice audio.yoshi_v_aww1
    yo "Yoichi has come a really long way since he first came here, hasn’t he?"

    hide goro_winter2
    hide goro laugh3
    show goro2_winter2 at left
    show goro2 play3 at left
    voice audio.goro_v_heh1a
    g "Heh, when you first brought him, you had no idea how to handle him either, Yoshinori."

    show yoshi comp3 at center
    voice audio.yoshi_v_sir1
    yo "I’m just glad you let me take him into the camp to begin with, sir."

    hide goro2_winter2
    hide goro2 play3
    show goro_winter2 at left
    show goro comp5 at left
    voice audio.goro_v_well1a
    g "It’s the least I could’ve done. I could tell you honestly wanted to do your best to help him."

    show aiden comp5 at right
    voice audio.aiden_v_aww3a
    a "Aww~ You two are sounding like a proud dad and grand-dad~!"

    hide goro_winter2
    hide goro comp5
    show goro2_winter2 at left
    show goro2 explain2 at left
    voice audio.goro_v_ehem1a
    g "*ehem* Well, back then I was so busy that I couldn’t be as responsible for Yoichi as Yoshinori was."

    show aiden laugh1 at right
    voice audio.aiden_v_laugh2a1
    a "Haha, Yoshi’s always had a knack for reaching out to people."
    a "Heck, just look at me – I wouldn’t even be here if Yoshi hadn’t bugged you to keep me around, Gramps!"

    hide yoshi_winter2
    hide yoshi comp3
    show yoshi2_winter2 at center
    show yoshi2 relief2 at center
    voice audio.yoshi_v_well3
    yo "W-Well, if I see a situation where I can make a difference, I do my best to try and help."
    yo "Especially when I know I have people who have my back."

    hide goro2_winter2
    hide goro2 explain2
    show goro_winter2 at left
    show goro comp2 at left
    voice audio.goro_v_praise2a1
    g "It’s thanks to that attitude that Yoichi is who he is today. "
    g "And, quite frankly, why both myself and Camp Buddy are even still around."

    show aiden comp3 at right
    voice audio.aiden_v_laugh1b2
    a "Haha, Yoshi’s stuck his nose all over the place, huh?"

    show yoshi2 shy5 at center
    voice audio.yoshi_v_aiden4
    yo "I-I wouldn’t phrase it like that, Aiden…"

    show goro comp3 at left
    voice audio.goro_v_agree6a1
    g "It’s true though, Yoshinori. You’ve been a fine leader to the scouts, and quite the father figure for Yoichi."
    g "I hope I’m able to help influence Yoichi’s growth in a positive way from here on out as well."

    show goro happy2 at left
    voice audio.goro_v_so1a
    g "I’ve spent enough time detached from him and the rest of the camp, so hopefully I can earn his trust and respect too."

    hide yoshi2_winter2
    hide yoshi2 shy5
    show yoshi_winter2 at center
    show yoshi comp1 at center
    voice audio.yoshi_v_sirgoro4a
    yo "Sir Goro…"

    show aiden comp6 at right
    voice audio.aiden_v_aww3a
    a "Aww, Gramps! I’m sure Yoichi already trusts and respects you – like I said, you’re basically as much his grandpa as Yoshi is his dad!"

    show goro comp5 at left
    voice audio.goro_v_unsure3a2
    g "Maybe. But I hope with patience—"

    #play sound sfx_snowball
    show goro doom2 at left
    voice audio.goro_v_shock2a1
    g "Oof!" with vpunch

    show yoichi_winter at p9_1
    show yoichi laugh1 at p9_1
    with moveinleft

    voice audio.yoichi_v_goro5a
    yi "Haha! That’s what you get for not paying attention to what’s around you, geezer!"

    hide goro_winter2
    hide goro doom2
    show goro2_winter2 at left
    show goro2 angry5 at left
    #jey
    show yoshi angry2 at center
    voice audio.yoshi_v_yoichi7
    yo "Y-Yoichi! Is that…"

    show aiden scared2 at right
    voice audio.aiden_v_oops2b
    a "Was that really a... yellow snowball? Uh-oh."

    show yoichi laugh3 at p9_1
    voice audio.yoichi_v_laugh1d1
    yi "Hahaha! I told him he couldn’t tell me where to piss!"

    hide goro2_winter2
    hide goro2 doom1
    show goro_winter2 at left
    show goro_vein at left
    show goro comic1 at left
    voice audio.goro_v_insult2b1
    g "LISTEN HERE, YOU BRAT! GET OVER HERE RIGHT NOW!" with vpunch

    show yoichi excited2 at p9_1
    voice audio.yoichi_v_tease1a
    yi "Nyeeeh! Come and get me!"

    hide yoichi_winter
    hide yoichi excited2
    with moveoutleft

    show goro comic2 at left
    voice audio.goro_v_angry2c
    g "I SAID GET OVER HERE, YOU FLEABAG!"

    hide goro_winter2
    hide goro comic2
    hide goro_vein
    with moveoutleft

    hide yoshi_winter2
    hide yoshi angry2
    show yoshi2_winter2 at center
    show yoshi2 sigh1 at center
    voice audio.yoshi_v_sigh3a
    yo "*sigh* Looks like Yoichi set him off."

    show aiden laugh3 at right
    voice audio.aiden_v_laugh2a1
    a "Hahaha, so much for patience, huh? That’s the first time I’ve seen Gramps blow a gasket in a while!"

    show yoshi2 comp6 at center
    voice audio.yoshi_v_laugh6
    yo "Ahehe, I guess Yoichi does know how to push his buttons…"

    hide yoshi2_winter2
    hide yoshi2 comp6
    show yoshi_winter2 at center
    show yoshi happy1 at center
    voice audio.yoshi_v_rush1
    yo "Come on, let’s go see if we can help him wrangle Yoichi and the pups."

    show aiden happy1 at right
    voice audio.aiden_v_agree3a1
    a "Haha, sure thing, Yoshi!"

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black with fade
    yo "{i}Aiden and I helped Sir Goro get control of Yoichi and the pups, and then we actually stayed outside and played in the snow with them for a while.{/i}"
    yo "{i}Eventually, Sir Goro went to check on Mr. Clermont, and Aiden and I headed back to our cabin.{/i}"

    jump day8_aiden_aftersq

label day8_aiden_jin:
    $sq_jin += 1
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
    #scene bg_messhall_winter_day with fade
    scene bg_messhall_autumn_day with fade
    play music here_they_come loop
    show aiden2_winter at p5_1
    show aiden2 sleepy2 at p5_1
    show yoshi_winter at p5_2
    show yoshi norm1 at p5_2
    show jin_autumn at p5_5
    show jin_glasses at p5_5
    show jin norm2 at p5_5
    voice audio.aiden_v_hngh1a2
    a "Brrr… It’s really chilly. Lemme go and make us some hot soup."

    show yoshi talk4 at p5_2
    voice audio.yoshi_v_wait1
    yo "Oh wait, Aiden. I almost forgot Jin’s here too. Why don’t we ask him if he wants some soup as well?"

    show aiden2_winter at left
    show aiden2 sleepy2 at left
    show yoshi_winter at center
    show yoshi happy2 at center
    show jin_autumn at right
    show jin_glasses at right
    show jin norm2 at right
    with move

    voice audio.yoshi_v_goodam1
    yo "Good morning, Jin!"

    #play sound sfx_mouseclick
    show jin thinkdn2 at right
    j "..."

    show aiden2 confused5 at left
    voice audio.aiden_v_think2a
    a "Uhh… He’s got his earphones on."

    show jin annoy2 at right
    voice audio.jin_v_oof1b
    j "Oh crap… Don’t tell me I got the bad ending on this route…"

    hide yoshi_winter
    hide yoshi happy2
    show yoshi2_winter at center
    show yoshi2 confused2 at center
    voice audio.yoshi_v_think1a
    yo "He looks quite busy on his computer…"

    show aiden2_winter at center
    show aiden2 confused5 at center
    show yoshi2_winter at left
    show yoshi2 confused2 at left
    with move

    hide aiden2_winter
    hide aiden2 confused5
    show aiden_winter at center
    show aiden excited3 at center
    hide yoshi2_winter
    hide yoshi2 confused2
    show yoshi_winter at left
    show yoshi awkward2 at left
    voice audio.aiden_v_jin1b
    a "JIN! MY, MAN~! " with vpunch

    hide jin_autumn
    hide jin_glasses
    hide jin annoy2
    show jin2_autumn at right
    show jin2_glasses at right
    show jin2 comic1 at right
    voice audio.jin_v_shock2c
    j "GWAAH…!! "
    j "Wh-When did you guys get here?!"

    show aiden play2 at center
    voice audio.aiden_v_greet1c
    a "Just now~! So, whatcha doin’? "

    hide jin2_autumn
    hide jin2 comic1
    hide jin2_glasses
    show jin_autumn at right
    show jin_glasses at right
    show jin scared1 at right
    j "...!"

    show yoshi annoy3 at left
    voice audio.yoshi_v_rush4
    yo "Come on, Aiden… Don’t disturb Jin’s work…"

    show aiden tease1 at center
    voice audio.aiden_v_oho2a
    a "Two guys hugging on screen doesn’t look like work to me~"

    hide jin2_autumn
    hide jin2_glasses
    hide jin2 scared1
    show jin_autumn at right
    show jin_glasses at right
    show jin comic1 at right
    voice audio.jin_v_wah1a
    j "G-Gah! This is embarrassing…"

    show yoshi awkward4 at left
    voice audio.yoshi_v_oh3
    yo "O-Oh… I’m guessing it’s one of those BL movies?"

    show jin shy2 at right
    voice audio.jin_v_conj1c2
    j "A-Actually it’s a BL game this time… Yuri gave me a copy of one of her favorites, and I guess I got a bit too immersed…"

    show aiden tease2 at center
    voice audio.aiden_v_comeon1a1
    a "Haha, are you really still embarrassed about it? We’re all so used to it by now!"
    a "Besides, are you sure you wanna play a game when the real thing is right in front of you~?"

    hide jin_autumn
    hide jin_glasses
    hide jin shy2
    show jin2_autumn at right
    show jin2_glasses at right
    show jin2 fudan3 at right
    voice audio.jin_v_what4a
    j "GAHHHH!!! WHAAT?!!!" with vpunch

    hide yoshi_winter
    hide yoshi awkward4
    show yoshi2_winter at left
    show yoshi2 sigh1 at left
    voice audio.yoshi_v_sigh3a
    yo "*sigh* Aiden… You ought to know he’s just teasing you by now, Jin."

    show jin2 daydream4 at right
    voice audio.jin_v_sigh2a
    j "Still, every time it gives me a heart attack… {p=1.0}And each time I secretly hope it’s a real request…"

    hide yoshi2_winter
    hide yoshi2 sigh1
    show yoshi_winter at left
    show yoshi confused3 at left
    voice audio.yoshi_v_think1a
    yo "You know, I never asked, but how did you and Yuri actually get into this stuff anyway?"
    yo "Even before I knew her, this was one of her hobbies…"

    show aiden confused2 at center
    voice audio.aiden_v_yeah1e1
    a "Yeah, and that gives me another question!"
    a "If you guys like dudes so much, why not go and get one~?"

    show aiden happy2 at center
    voice audio.aiden_v_jin3a
    a "You’re a cute guy, Jin, I bet you could find a boyfriend in no time!"

    hide jin2_autumn
    hide jin2_glasses
    hide jin2 daydream4
    show jin_autumn at right
    show jin_glasses at right
    show jin explain1 at right
    voice audio.jin_v_conj2c1
    j "W-Well, usually when people are fans of BL it’s either as a kink or an escape from reality…"

    show jin think2 at right
    voice audio.jin_v_conj3a1
    j "For me, It’s the latter… BL is an escape from my ever-lingering social anxiety issues."
    j "I’ve been alone my entire life and it’s mostly because I simply don’t know how to interact with people… "
    j "I’ve tried a few times, but they all ended up in disappointment… The real world can be cruel and heartless sometimes…"

    show jin fudan2 at right
    voice audio.jin_v_confused2a1
    j "But by entering the fantasy world of BL, there are so many options! It’s vast, colorful, and full of any kind of romance you can think of!"
    j "It can range from wholesome and cute friends falling in love, to hardcore, smut BDSM cock and ball torture! "

    hide yoshi_winter
    hide yoshi confused3
    show yoshi2_winter at left
    show yoshi2 awkward4 at left
    voice audio.yoshi_v_what3
    yo "What was that last part?!"

    show jin play5 at right
    voice audio.jin_v_laugh1a
    j "And it’s all fiction, so there’s no reason to take anything seriously~!"
    j "Call it delusional or cut from reality but it’s what makes me happy. It helped me not to feel alone."

    show aiden think2 at center
    voice audio.aiden_v_agree2a1
    a "I see, I see… I kinda understand now. We all need an outlet after all!"

    show jin think6 at right
    voice audio.jin_v_yuri2b
    j "In Yuri’s case, though… I think she just likes the art aspect of it… She is a very creative person."
    j "Whenever we look at BL together, she always appreciates the drawings, character designs and how well-written the stories are."

    hide yoshi2_winter
    hide yoshi2 awkward4
    show yoshi_winter at left
    show yoshi think2 at left
    voice audio.yoshi_v_isee1
    yo "That makes sense… Yuri did like to draw and write back then. And she really encourages the scouts to have a creative outlet."

    hide aiden_winter
    hide aiden think2
    show aiden2_winter at center
    show aiden2 think5 at center
    voice audio.aiden_v_think1a1
    a "Thinking about it, She’s the only scoutmaster that does that… You and Gramps usually like the traditional stuff."

    hide aiden2_winter
    hide aiden2 think5
    show aiden_winter at center
    show aiden talk2 at center
    voice audio.aiden_v_actually1a
    a "I always prefer the sporty stuff too, so I’ve got the athletic scouts covered!"

    show jin happy2 at right
    voice audio.jin_v_yeah1b
    j "Yeah, having Yuri around actually made me feel a lot more comfortable. She’s actually my first IRL friend that I can share the same interests with! "

    show aiden comp2 at center
    voice audio.aiden_v_aww3a
    a "Aww, Jin~ We’re your friends too! We don’t mind you telling us about your hobbies!"
    a "There’s no judgment here! C’mere!  "

    hide yoshi_winter
    hide yoshi think2
    show yoshi2_winter at left
    show yoshi2 awkward3 at left
    voice audio.yoshi_v_aiden6
    yo "A-Aiden, I’m not sure if Jin—"

    show aiden explain3 at center
    voice audio.aiden_v_comeon1a1
    a "Hush and just join in!"

    show yoshi2 confused2 at left
    voice audio.yoshi_v_uh1a
    yo "Uhh… Okay?"

    show jin_autumn at center
    show jin_glasses at center
    show jin happy2 at center
    show yoshi2_winter at left2
    show yoshi2 confused2 at left2
    show aiden_winter at right2
    show aiden explain3 at right2
    with move

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    hide jin_autumn
    hide jin_glasses
    hide jin happy2
    show jin2_autumn at center
    show jin2_glasses at center
    show jin2 fudan2 at center
    voice audio.jin_v_hngh1b
    j "Hnghh!!!"

    hide yoshi2_winter
    hide yoshi2 confused2
    show yoshi_winter at left2
    show yoshi comp5 at left2
    voice audio.yoshi_v_aww1
    yo "I hope you don’t feel too pressured when interacting with us, Jin. "

    show aiden play2 at right2
    voice audio.aiden_v_yeah1h3
    a "Yeah! Maybe you can make Camp Buddy into your own fantasy world~"

    play music here_they_come_fast loop
    show jin2 daydream1 at center
    j "..."

    show yoshi confused2 at left2
    voice audio.yoshi_v_jin5
    yo "Jin…?"

    show jin2 perv5 at center
    voice audio.jin_v_wah1c
    j "W-Wahh… Big… Squishy… Pecs…"
    j "It’s like being smushed by two giant marshmallows… "

    show jin2 perv4 at center
    voice audio.jin_v_relief1b2
    j "I can die here now… This is definitely a real-life representation of my fantasies. "

    hide aiden_winter
    hide aiden play2
    show aiden2_winter at right2
    show aiden2 comp3 at right2
    voice audio.aiden_v_think2a
    a "I think we broke him."

    hide yoshi_winter
    hide yoshi confused2
    show yoshi2_winter at left2
    show yoshi2 shy5 at left2
    voice audio.yoshi_v_uh1a
    yo "Sh-Should we let go? He’s starting to grope my chest…"

    show jin2 daydream4 at center
    voice audio.jin_v_fudan3a2
    j "I-It’s so much better than my mousepad…"

    hide aiden2_winter
    hide aiden2 comp3
    show aiden_winter at right2
    show aiden comp5 at right2
    voice audio.aiden_v_no2a1
    a "Nah, let him have his moment! He’s earned it!"

    show yoshi2 sigh1 at left2
    voice audio.yoshi_v_sigh3a
    yo "*sigh* Alright…"

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black with fade
    yo "{i}After chatting with Jin, Aiden went to make some soup for all three of us.{/i}"
    yo "{i}We ate our meal, then decided to leave Jin to his business while Aiden and I headed back to our cabin.{/i}"

    jump day8_aiden_aftersq

label day8_aiden_emilia:
    $sq_emilia += 1
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
    scene bg_entrance_winter_day with fade
    play music sunset_stroll_winter loop

    show aiden_winter2 at left2
    show aiden norm1 at left2
    show yoshi_winter2 at right2
    show yoshi relief2 at right2
    voice audio.yoshi_v_relief1
    yo "Whew… It’s a good thing we’re having a sunny winter, especially after that storm."

    show aiden tired4 at left2
    voice audio.aiden_v_excited1b
    a "I can’t wait for this season to be over though. I really prefer the heat."

    show yoshi play2 at right2
    voice audio.yoshi_v_laugh3
    yo "Just so you have an excuse to strip, right?"

    show aiden laugh2 at left2
    voice audio.aiden_v_laugh1b2
    a "You know me too well."

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    show aiden_winter2 at p4_1
    show aiden laugh2 at p4_1
    show yoshi_winter2 at p4_2
    show yoshi play2 at p4_2
    with move

    show emilia_winter2 at p4_3
    show emilia eyeroll4 at p4_3
    show yuri_winter2 at p4_4
    show yuri rage1 at p4_4
    with dissolve

    play music heracleum_a loop
    voice audio.yuri_v_ugh2a
    yu "Ugh! I can’t believe you! It’s literally the only thing I asked you to do!"

    show emilia angry2 at p4_3
    voice audio.emilia_v_question4b
    e "Hey! Don’t blame me! You’re the one who forgot it!"

    show yoshi shock2 at p4_2
    voice audio.yoshi_v_shock1a
    yo "Woah, woah! What are you two arguing about?"

    show emilia eyeroll6 at p4_3
    voice audio.emilia_v_ugh1
    e "I don’t know, ask this pink thing what’s grinding her gears!! "

    show yuri serious2 at p4_4
    voice audio.yuri_v_well1a
    yu "Well, we brought the scouts back home and I thought it would be a good idea to do a grocery run on the way back."
    yu "But Emilia over here forgot the shopping list!"

    show emilia angry3 at p4_3
    voice audio.emilia_v_request1a
    e "For your information, I put it in your phone, and you left that too!"
    e "And who in the world writes shopping lists on paper nowadays?!"

    show yoshi explain2 at p4_2
    voice audio.yoshi_v_comp8a
    yo "Now, calm down both of you. Especially you, Emilia, you just recovered!"

    show yuri serious4 at p4_4
    voice audio.yuri_v_yeah1b1
    yu "Yeah! I kept telling her to stay behind and wait, but she insisted on coming along!"

    show emilia angry6 at p4_3
    voice audio.emilia_v_tsun2a
    e "I told you all, I’m fine already! I’m not helpless!"

    hide aiden_winter2
    hide aiden laugh2
    show aiden2_winter2 at p4_1
    show aiden2 awkward2 at p4_1
    voice audio.aiden_v_shock1d1
    a "I’m surprised you two even agreed to go out and do chores together…"

    show yuri angry6 at p4_4
    voice audio.yuri_v_hmph1a
    yu "It’s not like I have much of a choice since she moved in with me!"

    hide aiden2_winter2
    hide aiden2 awkward2
    show aiden_winter2 at p4_1
    show aiden shock2 at p4_1
    voice audio.aiden_v_wait1a1
    a "Wait, you two are roommates now?"

    show yuri serious2 at p4_4
    voice audio.yuri_v_yeah1a1
    yu "Yeah, Emilia asked to stay with me so Mr. Clermont could stay in her room for now."

    show yoshi shock2 at p4_2
    voice audio.yoshi_v_laugh1
    yo "And to think, you were the one always demanding your own private space."

    show emilia annoy3 at p4_3
    voice audio.emilia_v_hmph1a
    e "That’s only because I was hiding something. There’s no need to do that anymore~"

    show yuri annoy2 at p4_4
    voice audio.yuri_v_sus1a
    yu "Why are you saying that so confidently…?"

    hide yoshi_winter2
    hide yoshi shock2
    show yoshi2_winter2 at p4_2
    show yoshi2 awkward3 at p4_2
    voice audio.yoshi_v_so1a
    yo "S-So how was your first night together?"

    show emilia shy2 at p4_3
    voice audio.emilia_v_tsun1b
    e "I suppose it was alright. I taught Yuri a thing or two about makeup since she clearly knows nothing."

    show yuri rage1 at p4_4
    voice audio.yuri_v_hey3a
    yu "Hey! What’s that supposed to mean?"

    show aiden talk1 at p4_1
    voice audio.aiden_v_well1a2
    a "Well, it sounds to me like you two had fun at least."

    show yuri sigh1 at p4_4
    voice audio.yuri_v_sigh2a
    yu "Yeah, so much so she’s staying permanently. "

    show yoshi2 awkward4 at p4_2
    voice audio.yoshi_v_really3
    yo "R-Really?"

    show yuri play2 at p4_4
    voice audio.yuri_v_unsure3b
    yu "Yup! I guess I can’t blame her, though, my room is a lot neater and cleaner than hers anyway~"

    show emilia evil4 at p4_3
    voice audio.emilia_v_ugh1
    e "Don’t make it sound like you hated the idea… You’re the one who’s been going on about having a gal-pal, finally!"
    e "You couldn’t stop showing me those fanfics of yours all night long!"

    show yoshi2 shock2 at p4_2
    voice audio.yoshi_v_wait3a
    yo "W-Wait, you read her fanfics, Emilia…?"

    show emilia confused5 at p4_3
    voice audio.emilia_v_agree2a1
    e "Yeah… I was confused at first, but I think I got the gist of it. But damn, you guys have no idea how much weird stuff this woman is into."

    show yuri angry3 at p4_4
    voice audio.yuri_v_what5a
    yu "I thought you liked my fanfics?! "

    show emilia sigh1 at p4_3
    voice audio.emilia_v_sigh1b
    e "I mean, they were fine, but not great when it’s ten chapters in one sitting!"

    show yuri annoy5 at p4_4
    voice audio.yuri_v_rush1d1
    yu "Can we just go get the groceries already?! I really don’t wanna spend all day outside on my feet…"

    show emilia relief2 at p4_3
    voice audio.emilia_v_oh1a
    e "Oh, I actually know a nice foot spa recipe that’ll ease that right away! Add some cucumbers and a mud mask, and we’ll have a proper spa day!"

    show yuri excited2 at p4_4
    voice audio.yuri_v_oh1a
    yu "Oooohhh~ That sounds nice! I’ll add those to the list!"

    hide yuri_winter2
    hide yuri excited2
    hide emilia_winter2
    hide emilia relief2
    with dissolve

    show aiden_winter2 at left2
    show aiden talk1 at left2
    show yoshi2_winter2 at right2
    show yoshi2 shock2 at right2
    with move

    hide yoshi2_winter2
    hide yoshi2 shock2
    show yoshi_winter2 at right2
    show yoshi comp2 at right2
    voice audio.yoshi_v_amazed1b
    yo "It’s crazy how close those two have gotten over the last few days…"

    show aiden talk3 at left2
    voice audio.aiden_v_yeah1a3
    a "Yeah, a week or two ago Yuri wanted to get rid of Emilia, and now they’re acting like besties."

    show yoshi happy1 at right2
    voice audio.yoshi_v_anyway1a
    yo "Anyway, are you ready to continue with our walk? We've just started the patrol."

    show aiden comp2 at left2
    voice audio.aiden_v_oops1a
    a "Whoops! You're right – let's hope we don't run into anyone else to distract us, haha!"

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black with fade
    yo"{i}After catching up with Emilia and Yuri, Aiden and I finished our walk around the campgrounds.{/i}"
    yo"{i}Eventually, it started to feel too cold to keep going, and we realized there wasn't much to check on anyway.{/i}"
    yo"{i}We headed back to our cabin to warm up.{/i}"

    jump day8_aiden_aftersq

label day8_aiden_aftersq:
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

    $ location = location_cabin
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_quarters_winter_day with fade
    play music buddy_oath_casual loop

    show yoshi_sleep at left2
    show yoshi norm2 at left2
    show aiden2_sleep at right2
    show aiden2 sleepy4 at right2
    voice audio.aiden_v_yawn1
    a "*yawn* Today feels like it’s lasting forever – even after all the stuff we did, it’s still early."
    a "Everyone else is busy doing their own thing out there."

    show yoshi happy1 at left2
    voice audio.yoshi_v_yeah1
    yo "Yeah, I guess there’s not too much we can do without the other workers around."

    hide aiden2_sleep
    hide aiden2 sleepy4
    show aiden_sleep at right2
    show aiden sigh4 at right2
    voice audio.aiden_v_agree1b1
    a "You bet. And it’s too cold outside to do anything fun, unlike in the summer."

    show yoshi laugh2 at left2
    voice audio.yoshi_v_laugh1
    yo "Haha, at least it’s cozy in here with the heater on."

    hide aiden_sleep
    hide aiden sigh4
    show aiden2_sleep at right2
    show aiden2 sad5 at right2
    voice audio.aiden_v_hngh1b2
    a "Hngh… I don’t wanna sound like a downer, but… I can’t wait for the winter to end."

    $working = False
    $shuffle_menu()
    menu():
        a "Hngh… I don’t wanna sound like a downer, but… I can’t wait for the winter to end.{fast}"
        "It'll be over soon.":
            $ working = True
            $ score_aiden -= 1
            $ score_bot += 1
            show yoshi talk1 at left2
            voice audio.yoshi_v_comp7
            yo "Just hang in there a little longer, Aiden. Time flies fast, and before you know it, it’ll be summer again."

            show aiden2 tired5 at right2
            voice audio.aiden_v_hngh1b3
            a "Ughh… I’m just so boooored…"
            a "All this lying in bed is making it worse too."
        "Work will be back soon.":
            $ working = True
            $ score_aiden -= 1
            $ score_top += 1
            show yoshi talk1 at left2
            voice audio.yoshi_v_comp5
            yo "Don’t worry, Aiden. Work will start up again soon, and before you know it, it’ll be summer."

            show aiden2 tired5 at right2
            voice audio.aiden_v_hngh1b3
            a "Ughh… I’m just so boooored…"
            a "All this lying in bed is making it worse too."
        "We can still have fun indoors.":
            $ working = True
            $ score_aiden += 1
            $ score_bot += 1
            show yoshi think2 at left2
            voice audio.yoshi_v_well1
            yo "Well, we can still make things fun even when we’re cooped up indoors."

            show aiden2 confused2 at right2
            voice audio.aiden_v_what1a
            a "Got any ideas?"
        "We can do something else to warm up.":
            $ working = True
            $ score_aiden += 1
            $ score_top += 1
            show yoshi think2 at left2
            voice audio.yoshi_v_well1
            yo "Well, how about we move around to warm up? All this lying around will just make you bored."

            show aiden2 confused2 at right2
            voice audio.aiden_v_what1a
            a "Got any ideas?"

    show yoshi think1 at left2
    voice audio.yoshi_v_think4
    yo "Hmm… How about we workout together? It’s been a while since we stretched our muscles, after all!"

    hide aiden2_sleep
    hide aiden2 confused2
    hide aiden2 tired5
    show aiden_sleep at right2
    show aiden play2 at right2
    voice audio.aiden_v_oho1a
    a "Oho~ I like the sound of that~"

    show yoshi talk1 at left2
    voice audio.yoshi_v_actually1a
    yo "Even though we’ve been working at the site a lot lately, thanks to the snow I haven’t even been breaking a sweat."
    yo "It’s about time we got down and dirty!"

    show aiden bold2 at right2
    voice audio.aiden_v_excited2b
    a "Now you got me hyped up! Grab some weights, and let’s get pumping already!"

    show yoshi laugh2 at left2
    voice audio.yoshi_v_alright2
    yo "Haha, alright, alright."

    show aiden_sleep at p5_5
    show aiden bold3 at p5_5
    show yoshi_sleep at p5_1
    show yoshi laugh2 at p5_1
    with move

    voice audio.aiden_v_flex1a
    a "FLEX!{p=0.5}THOSE!! {p=0.5}GUNS!!!"

    show yoshi comp3 at p5_1
    voice audio.yoshi_v_aiden1
    yo "Don’t go too fast, Aiden. You might pull a muscle."

    hide aiden_sleep
    hide aiden bold3
    show aiden2_sleep at p5_5
    show aiden2 tease5 at p5_5
    voice audio.aiden_v_comp1a1
    a "*stretches* Oh don't worry, we'll get to the ‘pulling’ part later~"

    show yoshi play5 at p5_1
    voice audio.yoshi_v_laugh3
    yo "*scoffs* Aiden…"

    show yoshi comp1 at p5_1
    yo "{i}(Watching Aiden get excited over the simplest things we do together really makes me happy.){/i}"
    yo "{i}(Even though he’s changed a lot physically, he’s still the same energetic guy I’ve always liked.){/i}"

    show aiden2 tease4 at p5_5
    voice audio.aiden_v_sheesh1a
    a "Sheesh, Yoshi. Did you only invite me to work out for the gunshow?"

    show yoshi talk3 at p5_1
    voice audio.yoshi_v_oh3
    yo "O-Oh, I was just thinking how much you’ve really bulked up over time."

    hide aiden2_sleep
    hide aiden2 tease4
    show aiden_sleep at p5_5
    show aiden happy1 at p5_5
    voice audio.aiden_v_conj2a3
    a "A lot can change in nine years, you know! "
    a "I realized back then that there’s so much more I could do to help if I was stronger and healthier."

    show aiden laugh2 at p5_5
    voice audio.aiden_v_agree7b
    a "And of course, I sorta wanted to impress you when we met again. Hahaha!"

    show yoshi happy2 at p5_1
    voice audio.yoshi_v_well1
    yo "Well, I’ll be honest. I was shocked when you returned to Camp Buddy. I could barely recognize you."
    yo "Don’t get me wrong, I was just happy to see you back, buff or not!"

    show aiden play3 at p5_5
    voice audio.aiden_v_agree4b
    a "Same! Although I didn't mind you turning into a hunk~"
    a "But I could tell it was you right away thanks to that cheesy personality of yours!"

    hide yoshi_sleep
    hide yoshi happy2
    show yoshi2_sleep at p5_1
    show yoshi2 sigh1 at p5_1
    voice audio.yoshi_v_sigh3a
    yo "*sigh* So I’ve always been ‘cheesy’?"

    show aiden laugh1 at p5_5
    voice audio.aiden_v_agree1b1
    a "Yup! That’s one thing I’m glad that’s never changed ’bout you, hahaha!"

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    show aiden happy2 at p5_5
    voice audio.aiden_v_anyway1c
    a "Anyway, I’m done with the weights! "

    hide yoshi2_sleep
    hide yoshi2 sigh1
    show yoshi_sleep at p5_1
    show yoshi talk3 at p5_1
    voice audio.yoshi_v_oh1
    yo "Oh, that quickly?"

    show aiden comp3 at p5_5
    voice audio.aiden_v_yeah1a3
    a "Yeaaah, I’m still kinda sore from all the shoveling yesterday. I wanna focus on my core and lower body today!"

    show yoshi happy1 at p5_1
    voice audio.yoshi_v_rush5
    yo "Alright let’s do legs then!"

    show aiden bold2 at p5_5
    voice audio.aiden_v_alright1a2
    a "Alright, lemme stretch some!"

    play music here_they_come loop
    show cg fade at truecenter
    show fxa7 1 at fx_pos
    with dissolve

    voice audio.aiden_vsa17_line1
    a "Nnnn…!"

    show fxa7 2 at fx_pos with Dissolve(0.25)
    voice audio.aiden_vsa17_line2
    a "Phew… The cold’s really made my leg muscles stiff and tight!"
    yo "{i}(Sitting down to stretch across from Aiden, I could see that his legs were spread wide and open right in front of me…){/i}"
    yo "{i}(Not that it surprises me, but it’s easy to notice that he’s not wearing anything under his shorts…){/i}"

    show fxa7 3 at fx_pos with Dissolve(0.25)
    voice audio.aiden_vsa17_line3
    a "Hey, Yoshi. Help me out some, will ya?"

    $working = False
    $shuffle_menu()
    menu():
        a "Hey, Yoshi. Help me out some, will ya?{fast}"
        "Press on his arms.":
            $ working = True
            $ score_bot += 1
            show fxa7 4a at fx_pos with Dissolve(0.25)
            yo "{i}(Pressing on Aiden’s arms, I felt him tense up under my hands. ){/i}"

            show fxa7 5a at fx_pos with Dissolve(0.25)
            voice audio.aiden_vsa17_line4a
            a "A-Ahehe… Copping a feel on my biceps, huh Yoshi?"

            show fxa7 6a at fx_pos with Dissolve(0.25)
            yo "{i}(I watched intently as the droplets of cold sweat started to drip down the crevices of his body…){/i}"
            yo "{i}(While continuing to exert more force, I couldn’t take my eyes off his crotch, hoping his shorts would slip up to reveal his package.){/i}"

            show fxa7 7a at fx_pos with Dissolve(0.25)
            voice audio.aiden_vsa17_line5
            a "Mnghh…!"
            yo "{i}(Noticing that I was getting carried away, I took my weight off of Aiden, making him exhale from all the pressure.){/i}"
        "Pull on his arms.":
            $ working = True
            $ score_top += 1
            show fxa7 4b at fx_pos with Dissolve(0.25)
            yo "{i}(Pulling on Aiden’s arms, I could feel a little restraint from his body.){/i}"

            show fxa7 5b at fx_pos with Dissolve(0.25)
            voice audio.aiden_vsa17_line4b
            a "A-Ahehe… Tryin’ to stretch me to my limits, huh Yoshi?"

            show fxa7 6bc at fx_pos with Dissolve(0.25)
            yo "{i}(I watched intently as the droplets of cold sweat started to drip down the crevices of his body…){/i}"
            yo "{i}(While continuing to exert more force, I couldn’t take my eyes off his crotch, hoping his shorts would slip up to reveal his package.){/i}"

            show fxa7 7bc at fx_pos with Dissolve(0.25)
            voice audio.aiden_vsa17_line5
            a "Mnghh…!"
            yo "{i}(Noticing that I was getting carried away, I took my weight off of Aiden, making him exhale from all the pressure.){/i}"
        "Press on his legs.":
            $ working = True
            $ score_bot += 2
            show fxa7 4c at fx_pos with Dissolve(0.25)
            yo "{i}(Pressing against Aiden’s legs, I felt him tense up under my hands. ){/i}"

            show fxa7 5c at fx_pos with Dissolve(0.25)
            yo "{i}(The harder I pressed, the more his crotch seemed to squish down against the floor.){/i}"

            show fxa7 6bc at fx_pos with Dissolve(0.25)
            yo "{i}(I watched intently as the droplets of cold sweat started to drip down the crevices of his body…){/i}"
            yo "{i}(While continuing to exert more force, I couldn’t take my eyes off his crotch, hoping his shorts would slip up to reveal his package.){/i}"

            show fxa7 7bc at fx_pos with Dissolve(0.25)
            voice audio.aiden_vsa17_line5
            a "Mnghh…!"
            yo "{i}(Noticing that I was getting carried away, I took my weight off of Aiden, making him exhale from all the pressure.){/i}"
        "Press on his back.":
            $ working = True
            $ score_top += 2
            show fxa7 4d at fx_pos with Dissolve(0.25)
            yo "{i}(Pressing slowly but firmly, I felt the definition of Aiden’s back against my palms.){/i}"

            show fxa7 5d at fx_pos with Dissolve(0.25)
            yo "{i}(His loose shirt was sliding open to show half of his pec, exposing his nipple.){/i}"

            show fxa7 6d at fx_pos with Dissolve(0.25)
            yo "{i}(I watched intently as the droplets of cold sweat started to drip down the crevices of his body…){/i}"
            yo "{i}(While continuing to exert more force, I couldn’t take my eyes off his crotch, hoping his shorts would slip up to reveal his package.){/i}"

            show fxa7 7d at fx_pos with Dissolve(0.25)
            voice audio.aiden_vsa17_line5
            a "Mnghh…!"
            yo "{i}(Noticing that I was getting carried away, I took my weight off of Aiden, making him exhale from all the pressure.){/i}"

    show fxa7 8 at fx_pos with Dissolve(0.25)
    voice audio.aiden_vsa17_line6
    a "Fwah~ That was a nice stretch! "

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black with fade
    yo "{i}After we finished our stretch, Aiden and I continued our workout.{/i}"
    yo "{i}I have to admit that I was having a hard time focusing with the teasing views and positions Aiden was doing… It almost ended up going in a different direction…{/i}"

    scene cg black
    hide screen location
    hide screen timeline
    hide screen quick_menu
    $quick_menu = False
    with fade
    $ time_transition_day_to_sunset_winter2()
    $ renpy.pause (2.0, hard=True)

    $ location = location_cabin
    $ time = timeline_timesunset
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_quarters_winter_sunset with fade
    play music buddy_oath_casual loop

    show yoshi_sleep at left2
    show yoshi norm1 at left2
    show aiden2_sleep at right2
    show aiden2 relief2 at right2
    voice audio.aiden_v_relief1a1
    a "Whew~ Look at all this sweat! I can finally feel the burn!"

    show yoshi tired3 at left2
    voice audio.yoshi_v_yeah1
    yo "Yeah… It’s getting really steamy in here. Let me just take my shirt off…"

    hide yoshi_sleep
    hide yoshi tired3
    show yoshi_sleep2 at left2
    show yoshi relief1 at left2
    with dissolve

    hide aiden2_sleep
    hide aiden2 relief2
    show aiden_sleep at right2
    show aiden tease1 at right2
    voice audio.aiden_v_oho1a
    a "Oho~ Look at you being the one who strips first now."

    show yoshi play2 at left2
    voice audio.yoshi_v_laugh3
    yo "Hehe, I couldn’t help it – look how drenched in sweat it is."
    yo "Normally it wouldn’t be this bad, but with the windows closed and the heater on, I feel like I’m starting to get sticky."

    show aiden tease2 at right2
    voice audio.aiden_v_unsure3a
    a "I dunno, I’m kinda digging it~"
    a "Dripping sweat, flexing muscles…"

    show aiden_sleep at center
    show aiden tease3 at center
    with move

    voice audio.aiden_v_laugh1b2
    a "And my favorite part, that nice musky scent you give off ~!"

    hide yoshi_sleep2
    hide yoshi play2
    show yoshi2_sleep2 at left2
    show yoshi2 confused2 at left2
    voice audio.yoshi_v_huh1
    yo "My scent…? "

    show aiden bold2 at center
    voice audio.aiden_v_yeah1h2
    a "Yeah! You have this manly, almost vanilla-like smell when you sweat. "

    show yoshi2 think2 at left2
    voice audio.yoshi_v_really3
    yo "R-Really? Huh… Must be the soap I use."

    show aiden bold5 at center
    voice audio.aiden_v_no1a1
    a "Nope, pretty sure it’s just your body. Trust me, you’ve had that since I first met you!"
    a "And I really like it~"

    hide yoshi2_sleep2
    hide yoshi2 think2
    show yoshi_sleep2 at left2
    show yoshi laugh2 at left2
    voice audio.yoshi_v_laugh1
    yo "Haha, well I guess I won’t complain about that then."

    show aiden play3 at center
    voice audio.aiden_v_anyway1c
    a "Anyway, don’t mind if I strip down too~"

    hide aiden_sleep
    hide aiden play3
    show aiden_sleep2 at center
    show aiden play1 at center
    with dissolve

    hide yoshi_sleep2
    hide yoshi laugh2
    show yoshi2_sleep2 at left2
    show yoshi2 sigh1 at left2
    voice audio.yoshi_v_sigh3a
    yo "*sigh* Of course you’d take everything off…"

    show aiden tease2 at center
    voice audio.aiden_v_what1b
    a "What?? We’re the only ones here."

    #if score_goro >= 15:
        #jump day8_aiden_cracksx
    #else:
    jump day8_aiden_workoutsx

label day8_aiden_cracksx:
    show yoshi2_sleep2 at center
    show yoshi2 sigh1 at center
    show aiden_sleep2 at right
    show aiden tease2 at right
    with move

    show goro_winter at left
    show goro explain1 at left
    with dissolve

    voice audio.goro_v_relief1a
    g "Whew… Finally, some alone ti—"

    show goro comic1 at left
    voice audio.goro_v_what2
    g "WHAT THE?!" with vpunch

    hide yoshi2_sleep2
    hide yoshi2 sigh1
    show yoshi_sleep2 at center
    show yoshi shock2 at center
    voice audio.yoshi_v_shock4
    yo "G-Gah, Sir Goro…!"

    show aiden happy2 at right
    voice audio.aiden_v_goro1a
    a "Heya, Gramps! How’s it hanging?"

    hide goro_winter
    hide goro comic1
    show goro2_winter at left
    show goro2 disappoint3 at left
    voice audio.goro_v_sigh1a
    g "*sigh* Am I interrupting something here?"

    hide yoshi_sleep2
    hide yoshi shock2
    show yoshi2_sleep2 at center
    show yoshi2 awkward3 at center
    voice audio.yoshi_v_disagree3
    yo "N-Not at all, sir…! Aiden I were just working out…!"

    hide goro2_winter
    hide goro2 disappoint3
    show goro_winter at left
    show goro bored1 at left
    voice audio.goro_v_hmph1a
    g "Right. Naked. In the middle of winter."

    show aiden laugh1 at right
    voice audio.aiden_v_agree1b1
    a "Yup! It got pretty sticky and steamy in here~"

    show goro bored2 at left
    voice audio.goro_v_sigh1a
    g "I can see that very clearly."

    show aiden play2 at right
    voice audio.aiden_v_perv1
    a "Why don’t you come and join us? You look like you could use some sweating yourself~!"

    $ working = False
    $ shuffle_menu()
    menu():
        a "Why don’t you come and join us? You look like you could use some sweating yourself~!{fast}"
        "Don't rope Sir Goro into this.":
            $ working = True
            $ score_top -= 1
            show yoshi2 sigh1 at center
            voice audio.yoshi_v_sigh3a
            yo "*sigh* Don’t rope Sir Goro into this, Aiden."

            show goro explain2 at left
            voice audio.goro_v_annoyed1a1
            g "I already got a work out in this morning."
            g "Besides, haven’t you two been working out the whole day? It’s already sunset."

            show aiden shock2 at right
            voice audio.aiden_v_swear3b
            a "Oh crap! I didn’t notice the time! Haha, guess we had too much fun, huh Yoshi?"

            show yoshi2 comp6 at center
            voice audio.yoshi_v_laugh6
            yo "A-Ahehe… yeah…"

            show goro talk1 at left
            voice audio.goro_v_well1a
            g "Well, why don’t you two head to the showers. You look like you could both use one."

            show aiden comp5 at right
            voice audio.aiden_v_alright2a
            a "Alright, alright. Let’s wash up, then!"

            scene cg black with fade
            yo "{i}Even though it was embarrassing Sir Goro caught us, I’m glad Aiden and I got to work out together today.{/i}"
            yo "{i}However, I wonder what Aiden really meant when he asked Sir Goro to join in…{/i}"

            jump day8_aiden_aftersx
        "We're done working out.":
            $ working = True
            $ score_bot -= 1
            show yoshi2 confused2 at center
            voice audio.yoshi_v_well3
            yo "W-Well, I thought we were about to go cool down, Aiden?"

            hide aiden_naked
            hide aiden play2
            show aiden2_naked at right
            show aiden2 sad4 at right
            voice audio.aiden_v_aww2a
            a "Aww… I wanted to work out some more."

            hide yoshi2_sleep2
            hide yoshi2 confused2
            show yoshi_sleep2 at center
            show yoshi comp6 at center
            voice audio.yoshi_v_laugh1
            yo "Haha, it’s already sunset though. I think we’ve worked out enough for today."

            show goro explain2 at left
            voice audio.goro_v_agree7a
            g "I agree. You two look like you could use a shower too."

            hide aiden2_naked
            hide aiden2 sad4
            show aiden_naked at right
            show aiden comp5 at right
            voice audio.aiden_v_alright2a
            a "Alright, alright. Let’s wash up, then!"

            scene cg black with fade
            yo "{i}Even though it was embarrassing Sir Goro caught us, I’m glad Aiden and I got to work out together today.{/i}"
            yo "{i}However, I wonder what Aiden really meant when he asked Sir Goro to join in…{/i}"

            jump day8_aiden_aftersx
        "I don't mind.":
            $ working = True
            $ score_top += 1
            hide yoshi2_sleep2
            hide yoshi2 awkward3
            show yoshi_sleep2 at center
            show yoshi relief2 at center
            voice audio.yoshi_v_well1
            yo "As long as Sir Goro wants to, I don’t mind."

            show aiden play3 at right
            voice audio.aiden_v_comeon1a1
            a "C’mon, Gramps! You never do stuff with us!"

            show goro play3 at left
            voice audio.goro_v_confused1a1
            g "Huh… But I have to be naked too, don’t I?"

            show aiden tease1 at right
            voice audio.aiden_v_laugh1b2
            a "What’s the matter? Worried to show us your dad bod?"

            hide goro_winter
            hide goro play3
            show goro2_winter at left
            show goro2 disappoint3 at left
            voice audio.goro_v_hmph1a
            g "Hmph. Don’t get so full of yourself. You have a long way to go before you get as buff as I am."

            show aiden_naked at right2
            show aiden tease2 at right2
            with move

            voice audio.aiden_v_yeah2b1
            a "Oh yeah? Why don’t you show us then?"

            hide goro2_winter
            hide goro2 disappoint3
            show goro2_undie2 at left
            show goro2 tease1 at left
            with dissolve

            hide yoshi_sleep2
            hide yoshi relief2
            show yoshi2_sleep2 at center
            show yoshi2 awkward1 at center
            voice audio.yoshi_v_gulp1a
            yo "*gulp*"

            show goro2_undie2 at left2
            show goro2 tease1 at left2
            with move

            show goro2 tease5 at left2
            voice audio.goro_v_taunt2a
            g "Hmph. Bigger’s always better."

            show aiden bold5 at right2
            voice audio.aiden_v_really2b
            a "What’s the point of size, if you don’t have any spunk left, Gramps?"

            show goro2 angry4 at left2
            voice audio.goro_v_what3a
            g "Wh-What…?"
            g "I’ll have you know, I’m not as rusty as you think. I’m far more ‘experienced' than you."

            show aiden tease3 at right2
            voice audio.aiden_v_oho3a
            a "Ohoho, you should ask Yoshi just how good I am in bed~"

            hide yoshi2_sleep2
            hide yoshi2 awkward1
            show yoshi_sleep2 at center
            show yoshi awkward3 at center
            voice audio.yoshi_v_aiden6
            yo "A-Aiden…!"

            hide goro2_undie2
            hide goro2 rage1
            show goro_undie2 at left
            show goro tease3 at left
            voice audio.goro_v_insult1a1
            g "Are you challenging me again, kiddo?"

            if d5_goro == True:
                hide goro_undie2
                hide goro tease3
                show goro2_undie2 at left
                show goro2 play6 at left
                voice audio.goro_v_heh1a
                g "I’ve already beaten you once."

                show aiden pout1 at right2
                voice audio.aiden_v_hey1c2
                a "That wasn’t fair, you grabbed Yoshi before I could take him!"

                hide goro2_undie2
                hide goro2 play6
                show goro_undie2 at left
                show goro tease3 at left
                voice audio.goro_v_hmph1a
                g "Looks like we’ve got some unfinished business."

                show aiden angry2 at right2
                voice audio.aiden_v_agree8a1
                a "Then let’s settle this for good! First one to make Yoshi cum, wins!"
            elif d5_aiden == True:
                show aiden tease2 at right2
                voice audio.aiden_v_
                a "What’s the point? We both know, Yoshi’s gonna choose me again~"

                show goro angry3 at left
                voice audio.goro_v_dismiss2a
                g "He didn’t choose you. You just ran off with him."

                show aiden bold2 at right2
                voice audio.aiden_v_agree8a1
                a "We should settle this, then! First one to make Yoshi cum, wins!"

            show yoshi panic3 at center
            voice audio.yoshi_v_what4
            yo "W-Wait, what…?!"

            jump day8_aiden_cracka
        "The more, the merrier.":
            $ working = True
            $ score_bot += 1
            hide yoshi2_sleep2
            hide yoshi2 awkward3
            show yoshi_sleep2 at center
            show yoshi relief2 at center
            voice audio.yoshi_v_actually1a
            yo "The more, the merrier!"

            show aiden play3 at right
            voice audio.aiden_v_comeon1a1
            a "C’mon, Gramps! You never do stuff with us!"

            show goro play3 at left
            voice audio.goro_v_confused1a1
            g "Huh… But I have to be naked too, don’t I?"

            show aiden tease1 at right
            voice audio.aiden_v_laugh1b2
            a "What’s the matter? Worried to show us your dad bod?"

            hide goro_winter
            hide goro play3
            show goro2_winter at left
            show goro2 disappoint3 at left
            voice audio.goro_v_hmph1a
            g "Hmph. Don’t get so full of yourself. You have a long way to go before you get as buff as I am."

            show aiden_naked at right2
            show aiden tease2 at right2
            with move

            voice audio.aiden_v_yeah2b1
            a "Oh yeah? Why don’t you show us then?"

            hide goro2_winter
            hide goro2 disappoint3
            show goro2_undie2 at left
            show goro2 tease1 at left
            with dissolve

            hide yoshi_sleep2
            hide yoshi relief2
            show yoshi2_sleep2 at center
            show yoshi2 awkward1 at center
            voice audio.yoshi_v_gulp1a
            yo "*gulp*"

            show goro2_undie2 at left2
            show goro2 tease1 at left2
            with move

            show goro2 tease5 at left2
            voice audio.goro_v_taunt2a
            g "Hmph. Bigger’s always better."

            show aiden bold5 at right2
            voice audio.aiden_v_really2b
            a "What’s the point of size, if you don’t have any spunk left, Gramps?"

            show goro2 angry4 at left2
            voice audio.goro_v_what3a
            g "Wh-What…?"
            g "I’ll have you know, I’m not as rusty as you think. I’m far more ‘experienced' than you."

            show aiden tease3 at right2
            voice audio.aiden_v_oho3a
            a "Ohoho, you should ask Yoshi just how good I am in bed~"

            hide yoshi2_sleep2
            hide yoshi2 awkward1
            show yoshi_sleep2 at center
            show yoshi awkward3 at center
            voice audio.yoshi_v_aiden6
            yo "A-Aiden…!"

            hide goro2_undie2
            hide goro2 rage1
            show goro_undie2 at left
            show goro tease3 at left
            voice audio.goro_v_insult1a1
            g "Are you challenging me again, kiddo?"

            if d5_goro == True:
                hide goro_undie2
                hide goro tease3
                show goro2_undie2 at left
                show goro2 play6 at left
                voice audio.goro_v_heh1a
                g "I’ve already beaten you once."

                show aiden pout1 at right2
                voice audio.aiden_v_hey1c2
                a "That wasn’t fair, you grabbed Yoshi before I could take him!"

                hide goro2_undie2
                hide goro2 play6
                show goro_undie2 at left
                show goro tease3 at left
                voice audio.goro_v_hmph1a
                g "Looks like we’ve got some unfinished business."

                show aiden angry2 at right2
                voice audio.aiden_v_agree8a1
                a "Then let’s settle this for good! First one to make Yoshi cum, wins!"
            elif d5_aiden == True:
                show aiden tease2 at right2
                voice audio.aiden_v_
                a "What’s the point? We both know, Yoshi’s gonna choose me again~"

                show goro angry3 at left
                voice audio.goro_v_dismiss2a
                g "He didn’t choose you. You just ran off with him."

                show aiden bold2 at right2
                voice audio.aiden_v_agree8a1
                a "We should settle this, then! First one to make Yoshi cum, wins!"

            show yoshi panic3 at center
            voice audio.yoshi_v_what4
            yo "W-Wait, what…?!"
            jump day8_aiden_cracka

label day8_aiden_aftercrack:
    $ location = location_bathroom
    $ time = timeline_timenight
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_bathroom_winter_night with fade
    play music here_they_come loop
    play bgsound sfxloop_shower loop

    if crack_sx == True:
        show goro_towel at left
        show goro relief1 at left
        show yoshi2_towel at center
        show yoshi2 awkward1 at center
        show aiden_towel at right
        show aiden relief2 at right
        voice audio.aiden_v_relief1a1
        a "Whew! I feel much better after that!"

        show yoshi2 tired4 at center
        voice audio.yoshi_v_groan1a
        yo "I just feel even more worn out…"

        show goro tease2 at left
        voice audio.goro_v_well2a
        g "Well, I have to say, Yoshinori… You’re a pretty good middle man."

        show yoshi2 sigh4 at center
        voice audio.yoshi_v_sigh3a
        yo "*sigh* I don’t know how to feel about that compliment."

        show aiden happy2 at right
        voice audio.aiden_v_so3
        a "So, I guess we can call this one a tie, right Gramps?"

        show goro tease5 at left
        voice audio.goro_v_heh1a
        g "I’m pretty sure I got a double knockout."

        show aiden angry2 at right
        voice audio.aiden_v_no1a1
        a "No way, it was me who made you both explode with my butt!"

        show goro tease3 at left
        voice audio.goro_v_taunt1b
        g "Smells like a rematch is underway."

        hide yoshi2_towel
        hide yoshi2 sigh4
        show yoshi_towel at center
        show yoshi shock3 at center
        voice audio.yoshi_v_what3
        yo "Wh-What?! I-I thought this was a one-time deal?!"

        show aiden bold2 at right
        voice audio.aiden_v_oho1a
        a "Well, I’m down to that! Maybe next time we can try fitting us both into Yoshi!"

        show yoshi panic3 at center
        voice audio.yoshi_v_shock4
        yo "GAH! NO! That’ll kill me!"

        show goro explain3 at left
        voice audio.goro_v_think1a1
        g "I have to say, I’m surprised you two aren’t exclusive. But then again, Aiden’s really not the possessive type."

        show aiden tease2 at right
        voice audio.aiden_v_perv1
        a "Yeah! Sharing is caring!"

        show yoshi sigh4 at center
        voice audio.yoshi_v_sigh3a
        yo "There’s nothing caring about that…"

        show goro_towel at p6_4
        show goro explain3 at p6_4
        show yoshi_towel at p6_5
        show yoshi sigh4 at p6_5
        show aiden_towel at p6_6
        show aiden tease2 at p6_6
        with move
    else:
        show yoshi_towel at left2
        show yoshi norm1 at left2
        show aiden_towel at right2
        show aiden relief2 at right2
        voice audio.aiden_v_relief1a1
        a "Whew! I feel much better after that!"

        show yoshi relief2 at left2
        voice audio.yoshi_v_relief1
        yo "That workout really got my blood pumping!"

        show aiden play2 at right2
        voice audio.aiden_v_sad2a
        a "It’s a bummer Gramps barged in just when things were really heating up."

        show yoshi_towel at center
        show yoshi relief2 at center
        show aiden_towel at right
        show aiden play2 at right
        with move

        show goro2_sleep at left
        show goro2 explain2 at left
        with dissolve

        voice audio.goro_v_ehem1a
        g "*ehem* This is a shared cabin, you know?"

        show yoshi shock2 at center
        voice audio.yoshi_v_shock3
        yo "G-Gah, Sir Goro…!"

        show aiden tease2 at right
        voice audio.aiden_v_hey2a2
        a "Oh, hey Gramps! Didn’t see you there! Finished taking a dump? "

        hide goro2_sleep
        hide goro2 explain2
        show goro_sleep at left
        show goro irked3 at left
        voice audio.goro_v_annoyed1a1
        g "Listen here, boy—"

        show goro_sleep at p6_4
        show goro irked3 at p6_4
        show yoshi_towel at p6_5
        show yoshi shock2 at p6_5
        show aiden_towel at p6_6
        show aiden tease2 at p6_6
        with move

    show jin_sleep at p6_1
    show jin_glasses at p6_1
    show jin tired6 at p6_1
    show lloyd_sleep at p6_2
    show lloyd tired4 at p6_2
    show darius_sleep at p6_3
    show darius norm1 at p6_3
    with dissolve

    voice audio.jin_v_hngh1c
    j "Hnghh… My body’s all sore… You guys were too rough on me…"

    show lloyd laugh3 at p6_2
    voice audio.lloyd_v_laugh1a1
    l "Haha, you were moaning so loud too!"

    show darius talk1 at p6_3
    voice audio.darius_v_conj2a
    d "Well, we really pushed his body to the limit."

    show aiden tease2 at p6_6
    voice audio.aiden_v_oho1a
    a "Oho~ Sounds like you guys did something ‘fun’?"

    show lloyd happy1 at p6_2
    voice audio.lloyd_v_greet2a3
    l "Hey there, you guys! Yeah, we just had a group workout after the site repairs today!"

    show yoshi talk1 at p6_5
    voice audio.yoshi_v_ah1
    yo "Ah, we just finished a workout of our own too!"

    show jin daydream2 at p6_1
    voice audio.jin_v_fudan3a3
    j "Th-That explains the towel fanservice…"

    show goro talk1 at p6_4
    voice audio.goro_v_actually1a
    g "I’m surprised you were able to drag Jin into it. I never pegged him as someone who’d be interested in fitness."

    show jin perv6 at p6_1
    voice audio.jin_v_sigh2a
    j "They told me they were going to work on my body… And I think I might have had a different idea before I agreed…"

    show lloyd bold2 at p6_2
    voice audio.lloyd_v_stayfit1b
    l "I’d say it’s worth it! No pain, no gain!"

    show jin pain2 at p6_1
    voice audio.jin_v_oof1b
    j "But all I gained was pain…"
    j "It was quite the experience with you guys though…"

    show jin perv2 at p6_1
    voice audio.jin_v_laugh2c
    j "Having two men being ‘hands-on’ really motivated me…!"

    show aiden bold2 at p6_6
    voice audio.aiden_v_well1a1
    a "Well, that’s a good start at least! If you keep it up, you’ll be fit in no time!"

    show lloyd happy2 at p6_2
    voice audio.lloyd_v_idea1a
    l "We should do this all together next time, though! I wanna show off my favorite yoga pose!"

    show jin scheme2 at p6_1
    voice audio.jin_v_think2a1
    j "You mean like the one you called… Downward Dog Style? "

    hide yoshi_towel
    hide yoshi talk1
    show yoshi2_towel at p6_5
    show yoshi2 confused2 at p6_5
    voice audio.yoshi_v_uh1a
    yo "That sounds like something else…"

    show darius tease2 at p6_3
    voice audio.darius_v_laugh2a
    d "Hehe. You should see it in action. "

    jump day8_aiden_aftereverything

label day8_aiden_workoutsx:
    hide yoshi2_sleep2
    hide yoshi2 awkward3
    hide yoshi2 confused2
    show yoshi_sleep2 at left2
    show yoshi sigh1 at left2
    voice audio.yoshi_v_sigh3a
    yo "Anyone could walk back in you know. But then that’s not even a concern for you."

    show aiden laugh1 at center
    voice audio.aiden_v_agree1b1
    a "Yup! You know that by now!"

    hide yoshi_sleep2
    hide yoshi sigh1
    show yoshi2_sleep2 at left2
    show yoshi2 think2 at left2
    voice audio.yoshi_v_ehem1b
    yo "*ehem* Should we continue our work out then?"

    show aiden happy1 at center
    voice audio.aiden_v_agree3a1
    a "Sure thing! I feel extra loose like this~"

    show yoshi2 awkward3 at left2
    voice audio.yoshi_v_alright1
    yo "I-I’ll lay down and do some crunches."

    if score_top > score_bot:
        show aiden_sleep2 at left3
        show aiden tease1 at left3
        with move

        voice audio.aiden_v_well1b2
        a "Well, don’t mind if I join in~"

        hide yoshi2_sleep2
        hide yoshi2 awkward3
        show yoshi_sleep2 at left2
        show yoshi shock1 at left2
        yo "...!"

        jump day8_aiden_6b
    elif score_bot > score_top:
        show yoshi2_sleep2 at left2
        show yoshi2 awkward3  at left2
        with move

        show yoshi2_sleep2 at left2
        show yoshi2 awkward3 at left2
        show aiden tease1 at center
        voice audio.aiden_v_well1b2
        a "Well, don’t mind if I do some squats right over…"

        show aiden tease2 at center
        voice audio.aiden_v_here1a
        a "Here~"

        jump day8_aiden_6t
    else:
        $position = renpy.random.randint(1,2)
        if position == 1:
            show aiden_sleep2 at left3
            show aiden tease1 at left3
            with move

            voice audio.aiden_v_well1b2
            a "Well, don’t mind if I join in~"

            hide yoshi2_sleep
            hide yoshi2 awkward3
            show yoshi_sleep2 at left2
            show yoshi shock1 at left2
            yo "...!"

            jump day8_aiden_6b
        elif position == 2:
            show yoshi2_sleep2 at left2
            show yoshi2 awkward3  at left2
            with move

            hide yoshi2_sleep2
            hide yoshi2 awkward3
            show yoshi_sleep2 at left2
            show yoshi shock1 at left2
            show aiden tease1 at center
            voice audio.aiden_v_well1b2
            a "Well, don’t mind if I do some squats right over…"

            show aiden tease2 at center
            voice audio.aiden_v_here1a
            a "Here~"

            jump day8_aiden_6t

label day8_aiden_aftersx:
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

    $ location = location_bathroom
    $ time = timeline_timenight
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_bathroom_winter_night with fade
    play music here_they_come loop

    show yoshi_towel at left2
    show yoshi norm1 at left2
    show aiden_towel at right2
    show aiden relief2 at right2
    voice audio.aiden_v_relief1a1
    a "Now that’s what I call a workout! "

    show yoshi relief2 at left2
    voice audio.yoshi_v_relief1
    yo "That was a lot wilder than usual… I almost can’t feel my legs."

    show aiden tease1 at right2
    voice audio.aiden_v_perv1
    a "My third leg’s pretty sore too~"

    hide yoshi_towel
    hide yoshi relief2
    show yoshi2_towel at left2
    show yoshi2 awkward4 at left2
    voice audio.yoshi_v_sigh3a
    yo "Goodness, Aiden… "

    show aiden laugh2 at right2
    voice audio.aiden_v_laugh2a1
    a "Hahaha! I do feel better after a hot shower, though!"

    hide yoshi2_towel
    hide yoshi2 awkward4
    show yoshi_towel at left2
    show yoshi sigh1 at left2
    voice audio.yoshi_v_relief4
    yo "It’s a good thing no one walked in on us, or that would’ve been—"

    show yoshi_towel at p6_5
    show yoshi sigh1 at p6_5
    show aiden_towel at p6_6
    show aiden laugh2 at p6_6
    with move

    show jin_sleep at p6_1
    show jin_glasses at p6_1
    show jin tired6 at p6_1
    show lloyd_sleep at p6_2
    show lloyd tired4 at p6_2
    show darius_sleep at p6_3
    show darius norm1 at p6_3
    show goro_sleep at p6_4
    show goro norm2 at p6_4
    with dissolve

    voice audio.jin_v_hngh1c
    j "Hnghh… My body’s all sore… You guys were too rough on me…"

    show lloyd laugh3 at p6_2
    voice audio.lloyd_v_laugh1a1
    l "Haha, you were moaning so loud too!"

    show darius talk1 at p6_3
    voice audio.darius_v_conj2a
    d "Well, we really pushed his body to the limit."

    show goro play2 at p6_4
    voice audio.goro_v_heh1a
    g "I thought he was going to pass out."

    show aiden tease1 at p6_6
    voice audio.aiden_v_oho1a
    a "Oho~ Sounds like you guys did something ‘fun’?"

    show lloyd happy1 at p6_2
    voice audio.lloyd_v_greet2a3
    l "Hey there, you guys! Yeah, we just had a group workout after the site repairs today!"

    show yoshi talk1 at p6_5
    voice audio.yoshi_v_ah1
    yo "Ah, we just finished a workout of our own too!"

    show jin daydream2 at p6_1
    voice audio.jin_v_fudan3a3
    j "Th-That explains the towel fanservice…"

    show goro talk1 at p6_4
    voice audio.goro_v_actually1a
    g "I’m surprised we were able to drag Jin into it. I never pegged him as someone who’d be interested in fitness."

    show jin perv6 at p6_1
    voice audio.jin_v_sigh2a
    j "I think I had something different in mind when you guys said you were going to work on my body… "

    show lloyd bold2 at p6_2
    voice audio.lloyd_v_stayfit1b
    l "I’d say it’s worth it!  No pain, no gain!"

    show jin pain2 at p6_1
    voice audio.jin_v_oof1b
    j "But all I gained was pain…"
    j "It was quite the experience with you guys though…"

    show jin perv2 at p6_1
    voice audio.jin_v_laugh2c
    j "Having three men being ‘hands-on’ really motivated me…!"

    show aiden bold2 at p6_6
    voice audio.aiden_v_well1a1
    a "Well, that’s a good start at least! If you keep it up, you’ll be fit in no time!"

    show lloyd happy2 at p6_2
    voice audio.lloyd_v_idea1a
    l "We should do this all together next time, though! I wanna show off my favorite yoga pose!"

    show jin scheme2 at p6_1
    voice audio.jin_v_think2a1
    j "You mean like the one you called… Downward Dog Style? "

    hide yoshi_towel
    hide yoshi talk1
    show yoshi2_towel at p6_5
    show yoshi2 confused2 at p6_5
    voice audio.yoshi_v_uh1a
    yo "That sounds like something else…"

    show darius tease2 at p6_3
    voice audio.darius_v_laugh2a
    d "Hehe. You should see it in action."

    jump day8_aiden_aftereverything

label day8_aiden_aftereverything:
    if crack_sx == True:
        show jin_sleep at p7_2
        show jin_glasses at p7_2
        show jin scheme2 at p7_2
        show lloyd_sleep at p7_3
        show lloyd happy2 at p7_3
        show darius_sleep at p7_4
        show darius tease2 at p7_4
        show goro_towel at p7_5
        show goro talk1 at p7_5
        show yoshi2_towel at p7_6
        show yoshi2 confused2 at p7_6
        show aiden_towel at p7_7
        show aiden bold2 at p7_7
        with move
        hide yoshi2_towel
        hide yoshi2 confused2
        show yoshi_towel at p7_6
        show yoshi talk1 at p7_6
    else:
        show jin_sleep at p7_2
        show jin_glasses at p7_2
        show jin scheme2 at p7_2
        show lloyd_sleep at p7_3
        show lloyd happy2 at p7_3
        show darius_sleep at p7_4
        show darius tease2 at p7_4
        show goro_sleep at p7_5
        show goro talk1 at p7_5
        show yoshi2_towel at p7_6
        show yoshi2 confused2 at p7_6
        show aiden_towel at p7_7
        show aiden bold2 at p7_7
        with move
        hide yoshi2_towel
        hide yoshi2 confused2
        show yoshi_towel at p7_6
        show yoshi talk1 at p7_6

    show emilia_winter3 at p7_1
    show emilia scared3 at p7_1
    with dissolve

    voice audio.emilia_v_ah2b
    e "AAAAAH! What the hell?! Why are you all here?!"

    show lloyd annoy5 at p7_3
    voice audio.lloyd_v_ignored1a1
    l "Duh, it’s our bathroom! And you’re the one who barged in!"

    show emilia disgust1 at p7_1
    voice audio.emilia_v_tsun2a
    e "I thought nobody was in here since the cabin was empty and the bathroom was unlocked…!"

    show darius annoy2 at p7_4
    voice audio.darius_v_ugh1
    d "Ever heard of knocking?"

    show emilia disgust5 at p7_1
    voice audio.emilia_v_disgust1
    e "Just for the record… What’s up with you guys’ room?! It totally reeks! "
    e "It smells like sweat and protein shakes…! Try opening up a window!"

    show aiden happy3 at p7_7
    voice audio.aiden_v_no1a1
    a "Haha, no can do! The cold messes up our workouts!"

    show yoshi talk2 at p7_6
    voice audio.yoshi_v_emilia5
    yo "What brings you here, Emilia? "

    show emilia sigh1 at p7_1
    voice audio.emilia_v_ugh1
    e "I-I’m here to get your dirty laundry."

    show lloyd explain3 at p7_3
    voice audio.lloyd_v_shock1b1
    l "Ooh! Just in time! I have some over here! Catch!"

    show lloyd_sleep at p7_2
    show lloyd explain3 at p7_2
    show jin_sleep at p7_3
    show jin_glasses at p7_3
    show jin scheme2 at p7_3
    with move

    show emilia panic6 at p7_1
    voice audio.emilia_v_gasp1
    e "Eek! "
    e "Goodness gracious… This is your used underwear! I think I’m gonna puke!"

    show lloyd angry2 at p7_2
    voice audio.lloyd_v_greet2b1
    l "Heeey! I practice excellent hygiene, just so you know!"

    show darius play5 at p7_4
    voice audio.darius_v_cute1
    d "He does. He’s as clean as a baby."

    show lloyd blep1 at p7_2
    voice audio.lloyd_v_sigh2a
    l "That comparison doesn’t help at all, Dar!"

    show emilia angry6 at p7_1
    voice audio.emilia_v_ugh1
    e "Ugh… This is what my life has become… "

    show aiden talk4 at p7_7
    voice audio.aiden_v_oh1a
    a "Oh, I was planning to bring all this to the laundry room later – why are you working on it, Emilia? "

    show emilia sigh1 at p7_1
    voice audio.emilia_v_sigh1b
    e "I asked Yuri to teach me to do some chores today. But ugh… I didn’t sign up for… this."
    e "She probably knew I would hate this one and took advantage of my initiative! That witch!"

    if crack_sx == True:
        show goro_towel at p7_1
        show goro talk1 at p7_1
        with move

        show goro_towel at p7_5
        show goro relief2 at p7_5
        with move
    else:
        show goro_sleep at p7_1
        show goro talk1 at p7_1
        with move

        show goro_sleep at p7_5
        show goro relief2 at p7_5
        with move

    voice audio.goro_v_glad1a
    g "Still, it’s good to see you willing to help. It shows how much you’ve grown."

    show emilia irked2 at p7_1
    voice audio.emilia_v_hmph1a
    e "You know, I should be flattered by that statement…"
    e "But you saying that while you’re handing me your sweat-soaked shirt kinda ruins the mood."

    show goro comp3 at p7_5
    voice audio.goro_v_laugh1b1
    g "Hehe, sorry about that."

    show emilia talk1 at p7_1
    voice audio.emilia_v_conj2b
    e "A-Anyway, I checked on Mr. Clermont a while ago and he’s already packing up to leave. "
    e "I was going to send him off, but I still have to work on this laundry."

    show yoshi happy1 at p7_6
    voice audio.yoshi_v_confident3
    yo "You can leave Mr. Clermont to us! We just finished here too, anyways!"

    show aiden excited3 at p7_7
    voice audio.aiden_v_idea1a3
    a "Ooh, I’ll go make some dinner for him! I just had an idea!"

    hide aiden_towel
    hide aiden excited3
    with moveoutright

    show yoshi shock3 at p7_6
    voice audio.yoshi_v_hey4
    yo "H-Hey, Aiden! You’re not going out there in just a towel…!"

    hide yoshi_towel
    hide yoshi shock3
    with moveoutright

    show goro sigh4 at p7_5
    voice audio.goro_v_sigh1a
    g "*sigh* I’ll go with them just to make sure we don’t give a bad last impression…"

    if crack_sx == True:
        hide goro_towel
        hide goro sigh4
        with dissolve
    else:
        hide goro_sleep
        hide goro sigh4
        with dissolve

    show darius happy1 at p7_4
    voice audio.darius_v_encourage1a
    d "Time for our shower then."

    hide darius_sleep
    hide darius happy1
    hide lloyd_sleep
    hide lloyd blep1
    show darius_naked at p7_4
    show darius norm1 at p7_4
    show lloyd_naked at p7_2
    show lloyd norm2 at p7_2
    with dissolve

    hide jin_sleep
    hide jin_glasses
    hide jin scheme2
    show jin2_sleep at p7_3
    show jin2_blush2 at p7_3
    show jin2_nosebleed at p7_3
    show jin2_glasses at p7_3
    show jin2 comic4 at p7_3
    show emilia rage4 at p7_1
    voice audio.emilia_v_what4a
    e "AAAHHH, WHAT THE FUCK?!" with vpunch

    show lloyd talk2 at p7_2
    voice audio.lloyd_v_rush1a1
    l "Oh, right. You’re still here..."

    show jin2 dizzy2 at p7_3
    j "*faints*"

    hide jin2_sleep
    hide jin2_blush2
    hide jin2_nosebleed
    hide jin2_glasses
    hide jin2 dizzy2
    with moveoutbottom

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
    scene bg_messhall_winter_night with fade
    play music ready_for_tomorrow_winter loop

    show goro_autumn at left
    show goro happy2 at left
    show william_autumn at center
    show william norm1 at center
    show yoshi_autumn at right
    show yoshi norm1 at right
    voice audio.goro_v_thanks1a1
    g "Thanks for agreeing to one more meal before you leave, Mr. Clermont."

    show william laugh1 at center
    voice audio.william_v_thanks1b
    w "I’m the one who should be thanking you! You’ve all been so hospitable these last two days!"

    show william happy3 at center
    voice audio.william_v_actually1
    w "In fact, I’d say this is one of the best mini vacations I’ve taken in a long time!"
    w "With everything going on at work, I needed a bit of time away from the stress, and the rustic lifestyle was perfect for me."

    show yoshi laugh1 at right
    voice audio.yoshi_v_laugh1
    yo "Haha, we’re glad you enjoyed being here so much, sir. We wouldn’t have been able to clean up everything as quickly without your help, either. "

    show william comp4 at center
    voice audio.william_v_conj4
    w "Like I said, think nothing of it! It’s the least I could do. "
    w "I would like to extend my apologies again about what transpired with Ms. Komarova at the hotel, however. "

    show william sigh1  at center
    voice audio.william_v_sigh2
    w "I was not aware of the severity of her well-being at the time… "

    show goro explain2 at left
    voice audio.goro_v_alright2b1
    g "It’s quite alright, sir. I don’t think any of us were aware, so you can’t be blamed."

    show william comp2 at center
    voice audio.william_v_conj6
    w "Regardless, I am glad that she is surrounded by supportive people."

    show goro_autumn at p4_1
    show goro norm1 at p4_1
    show william_autumn at p4_2
    show william norm1 at p4_2
    show yoshi_autumn at p4_4
    show yoshi norm1 at p4_4
    with move

    show aiden_autumn at p4_3
    show aiden bold2 at p4_3
    with dissolve

    voice audio.aiden_v_orderup1a
    a "Order up! A very special meal for our lovely guest, Mr. Clermont! "
    a "Don’t think I forgot about you guys either, Yoshi and Gramps! There’s plenty for everyone!"

    show cg_fade at truecenter
    show fxa8 at fx_pos with dissolve
    #voice audio.william_vsa18_line1
    #jey
    w "My, my, what a way to end this trip! This looks delectable!"

    voice audio.yoshi_vsa18_line1
    yo "Whoa, the plating looks just like in the hotel restaurant! You made this, Aiden?!"

    voice audio.aiden_vsa18_line1
    a "I picked up a trick or two from that fancy hotel! You know what they say, if you can’t beat ’em, join them!"

    #voice audio.william_vsa18_line2
    w "Well I think I speak for all of us when I say I can’t wait to try it!"

    voice audio.aiden_vsa18_line2
    a "Haha, I hope it meets your expectations!"

    hide cg_fade
    hide fxa8
    with dissolve

    show william amazed1 at p4_2
    voice audio.william_v_amazed3
    w "Good heavens! This is delicious! "

    show aiden grin1 at p4_3
    voice audio.aiden_v_thanks1b1
    a "Glad you like it, Mr. Clermont!"

    show william amazed3 at p4_2
    voice audio.william_v_impressed2a
    w "As someone who’s eaten in restaurants around the world, I can say your cooking is still one of the best I’ve ever had! "

    hide aiden_autumn
    hide aiden grin1
    show aiden2_autumn at p4_3
    show aiden2 comp2 at p4_3
    voice audio.aiden_v_aww3a
    a "Aww, thanks Mr. Clermont… I’m flattered! But are you sure you’re not just hungry?"

    show william comp4 at p4_2
    voice audio.william_v_agree1b
    w "I’m pretty sure. I think you’re underestimating yourself, lad."

    show aiden2 comp5 at p4_3
    voice audio.aiden_v_laugh1b1
    a "Ahehe…"

    show william confused3 at p4_2
    voice audio.william_v_oh3
    w "I’m curious, where did you learn to cook?"

    hide aiden2_autumn
    hide aiden2 comp5
    show aiden_autumn at p4_3
    show aiden happy2 at p4_3
    voice audio.aiden_v_actually1a
    a "From my dad! He used to be the cook here at Camp Buddy when it first opened."

    show william talk3 at p4_2
    voice audio.william_v_surprised1a
    w "Ah, was your father a professional chef of some kind?"

    show aiden comp3 at p4_3
    voice audio.aiden_v_laugh1b1
    a "Ahehe, not at all – cooking was just his passion! And he just passed it down to me!"

    show william amazed1 at p4_2
    voice audio.william_v_amazed2
    w "No culinary background, and yet this talented! Very interesting."
    w "On that note, I think you have what it takes to pursue the culinary arts. All that’s missing is a certification."

    show william excited3 at p4_2
    voice audio.william_v_actually1
    w "And considering your skills, that would be quite easy to acquire if you put in the work and time! "
    w "As a food connoisseur, I actually have quite a few connections with the best chefs and their masterclasses from around the world, if you’re interested~"

    show aiden awkward2 at p4_3
    voice audio.aiden_v_wait1b2
    a "W-wait, are you serious…?"

    show william laugh2 at p4_2
    voice audio.william_v_agree1b
    w "Of course! I pride myself on cultivating talent!"

    hide aiden_autumn
    hide aiden awkward2
    show aiden2_autumn at p4_3
    show aiden2 shy2 at p4_3
    voice audio.aiden_v_confused1c2
    a "Ehh… I-I’m really flattered you think that, Mr. Clermont… But I don’t think I’m cut out for the big time…"
    a "Not only that, but phew, the prices for classes are something else… "

    show william happy3 at p4_2
    voice audio.william_v_comp2b
    w "I’m sure that could be negotiated! "

    show aiden2 awkward6 at p4_3
    voice audio.aiden_v_ah1a
    a "A-Ahh… Well…"

    $ working = False
    $ shuffle_menu()
    menu():
        a "A-Ahh… Well…{fast}"
        "The answer is obvious.":
            $ working = True
            $ score_aiden -= 2
            show yoshi amazed1 at p4_4
            voice audio.yoshi_v_encourage3
            yo "The answer is obvious, Aiden!"

            show aiden2 confused5 at p4_3
            voice audio.aiden_v_unsure2a
            a "I dunno… Maybe I should think about it some more…?"
        "You should go for it.":
            $ working = True
            $ score_aiden -= 1
            show yoshi amazed1 at p4_4
            voice audio.yoshi_v_encourage3
            yo "You should go for it, Aiden!"

            show aiden2 confused5 at p4_3
            voice audio.aiden_v_unsure2a
            a "I dunno… Maybe I should think about it some more…?"
        "There's no pressure.":
            $ working = True
            $ score_aiden += 1
            show yoshi comp5 at p4_4
            voice audio.yoshi_v_comp5
            yo "There’s no pressure, Aiden! You don’t have to decide right away."
        "You don't need to answer right now.":
            $ working = True
            $ score_aiden += 2
            show yoshi comp2 at p4_4
            voice audio.yoshi_v_william5
            yo "You don’t need an answer right now, do you, Mr. Clermont?"

            show william comp4 at p4_2
            voice audio.william_v_dismiss1
            w "Of course not! "

    show william comp2 at p4_2
    voice audio.william_v_comp3
    w "I understand that it’s a sudden offer, and a rather intimidating prospect, so please take your time to consider!"

    show goro happy3 at p4_1
    voice audio.goro_v_agree7a
    g "I agree. I think it’s worth giving it some more thought, Aiden. This is a huge decision, after all."

    show william relief2 at p4_2
    voice audio.william_v_well1a
    w "Either way, my line is always open whenever you decide! Just give me a call!"

    hide aiden2_autumn
    hide aiden2 confused5
    hide aiden2 awkward6
    show aiden_autumn at p4_3
    show aiden comp2 at p4_3
    voice audio.aiden_v_think2b
    a "Thanks for the opportunity, Mr. Clermont! I’ll think about it!"

    show william happy3 at p4_2
    voice audio.william_v_amazed1
    w "Great! And with that, I think it’s about time for me to leave."

    show aiden talk4 at p4_3
    voice audio.aiden_v_oh2b
    a "Oh? Don’t you wanna stay for dessert? I can whip up something fancy again!"

    show william comp4 at p4_2
    voice audio.william_v_alright2b
    w "It’s alright! I’m quite full already. Besides, I have several appointments tomorrow, too!"

    show goro talk1 at p4_1
    voice audio.goro_v_comp1e1
    g "Ah, we understand! We’re glad to have had you around, sir!"

    show william comp2 at p4_2
    voice audio.william_v_thanks1b
    w "Once again, thank you all for your hospitality! I hope that I didn’t put you out too much."

    show goro comp5 at p4_1
    voice audio.goro_v_laugh2a
    g "Oh, not at all, Mr. Clermont! You’re welcome here at the camp anytime you want!"

    show yoshi happy2 at p4_4
    voice audio.yoshi_v_right5
    yo "That’s right! Please feel free to come back and visit, sir!"

    show william laugh2 at p4_2
    voice audio.william_v_thanks2
    w "Thank you, your kindness is greatly appreciated."

    show william happy3 at p4_2
    voice audio.william_v_conj6
    w "In addition, if Camp Buddy comes upon a concern or issue, especially in the case of the project, please do let me know right away!"
    w "I’m always happy to assist!"

    show yoshi laugh1 at p4_4
    voice audio.yoshi_v_response1b
    yo "We’ll keep that in mind, sir."

    show william happy2 at p4_2
    voice audio.william_v_well1a
    w "Well, my driver just arrived! I hope to see you all again sometime soon, and hopefully for good news!"

    show william play2 at p4_2
    voice audio.william_v_oh2
    w "Oh, and Mr. Flynn, please do let me know! I have high hopes for you!"
    w "Ciao~"

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black with fade
    yo "{i}I couldn’t believe what an amazing opportunity Mr. Clermont was offering Aiden… {/i}"
    yo "{i}I’m sure he’s excited for the chance! I’m so happy for him!{/i}"
    $ renpy.pause (2.0, hard=True)
    yo "{i}After Mr. Clermont left, Sir Goro headed over to the construction site to inspect the work for the day, while Aiden and I started to clean up at the kitchen.{/i}"

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
    scene bg_kitchen_winter_night with fade
    play music go_with_the_flow_slow loop
    play bgsound sfx_dishwashing loop

    show yoshi_autumn at left2
    show yoshi happy1 at left2
    show aiden_autumn at right2
    show aiden norm1 at right2
    voice audio.yoshi_vsa19_line1
    yo "I really gotta hand it to you, Aiden. You really impressed Mr. Clermont with your cooking."

    show aiden comp3 at right2
    voice audio.aiden_vsa19_line1
    a "Ahehe, I didn’t expect he would dig it that much!"

    show yoshi comp5 at left2
    voice audio.yoshi_vsa19_line2
    yo "I’d say I’m not surprised, but you caught me off guard as well. "

    voice audio.yoshi_vsa19_line3
    yo "I thought we were just having a regular dinner, but you came out there with that really fancy dish."

    show aiden happy1 at right2
    voice audio.aiden_vsa19_line2
    a "I’m really glad you all liked it! I wasn’t sure if it’s just because of the presentation or something."

    show yoshi laugh2 at left2
    voice audio.yoshi_vsa19_line4
    yo "Our plates were almost licked clean. I think that speaks for itself, haha!"

    show aiden laugh2 at right2
    voice audio.aiden_vsa19_line3
    a "I guess it was a good idea to take a risk and try something new, huh?"

    show yoshi bold2 at left2
    voice audio.yoshi_vsa19_line5
    yo "Yeah, definitely! It really looked crazy fancy, just like the stuff at the hotel!"

    show aiden shy2 at right2
    voice audio.aiden_vsa19_line4
    a "Whew… I’m just happy I pulled it off…. I was trying so hard to remember how it looked, hahaha! "

    show yoshi confused2 at left2
    voice audio.yoshi_vsa19_line6
    yo "I was wondering though, what made you decide to do that all of a sudden…?"

    show aiden think2 at right2
    voice audio.aiden_vsa19_line5
    a "Well, at first, I thought I’d make something extra special for Mr. Clermont on his last day. He’s done a lot for us and the camp, after all."

    show aiden talk5 at right2
    voice audio.aiden_vsa19_line6
    a "But if I’m gonna be honest, ever since that whole fiasco back at the hotel, I’ve been wanting to try some new things."

    voice audio.aiden_vsa19_line7
    a "I thought there’s no time like the present to pick up some skills!"

    show yoshi worry2 at left2
    voice audio.yoshi_vsa19_line7
    yo "Oh, I see…! I hope you’re not stressing yourself out, though."

    show aiden comp3 at right2
    voice audio.aiden_vsa19_line8
    a "Not at all! I’m making sure I’m taking things at my own pace and having fun with it! "

    $ renpy.music.stop('bgsound', fadeout=1.0)
    show aiden bold2 at right2
    voice audio.aiden_vsa19_line9
    a "And I’ll let you in on a little secret! That dish I made… was actually my dad’s specialty!"

    voice audio.aiden_vsa19_line10
    a "I just fancied it up on the plate and added my own twist!"

    show yoshi shock2 at left2
    voice audio.yoshi_vsa19_line8
    yo "Oh, wow…!"

    show aiden comp5 at right2
    voice audio.aiden_vsa19_line11
    a "I never tried making it before, ’cause I knew I couldn’t cook it the same way my Dad did… But I’d say it was pretty close!"

    show yoshi talk3 at left2
    voice audio.yoshi_vsa19_line9
    yo "You know… I’ve always wondered, how did you and Mr. Andre get so good at cooking?"

    show aiden talk1 at right2
    voice audio.aiden_vsa19_line12
    a "Oh yeah… I don’t think I told you, but it was actually my dad’s dream to become a chef."

    show aiden sad4 at right2
    voice audio.aiden_vsa19_line13
    a "But things didn’t work out for him ’cause he couldn’t afford to get a degree even though he was pretty good at it."

    voice audio.aiden_vsa19_line14
    a "It was already hard enough trying to raise me, keep a roof over our heads and put food on the table all by himself!"

    show yoshi sad4 at left2
    voice audio.yoshi_vsa19_line10
    yo "…I can’t imagine how difficult that was."

    show aiden happy2 at right2
    voice audio.aiden_vsa19_line15
    a "But the thing is… I don’t see it as all that bad!"

    voice audio.aiden_vsa19_line16
    a "Even though we never had much, Dad always made things work. I never felt like I was missing out on anything growing up."

    show aiden comp2 at right2
    voice audio.aiden_vsa19_line17
    a "Dad always made sure to cook something special for me after coming home from work."

    voice audio.aiden_vsa19_line18
    a "I was always so amazed at how he could turn the simplest and cheapest stuff into something amazing, so I got interested in it too."

    show aiden comp6 at right2
    voice audio.aiden_vsa19_line19
    a "Eventually, I started doing it for dad ‘cause I know how tired he always was from work."

    show cg fade at truecenter
    show fxa9 at fx_pos
    with dissolve

    voice audio.aiden_vsa19_line20
    a "After that, it became something we’d always bond over. He started calling me his ‘little chef’ and we’d always cook and eat together!"

    voice audio.aiden_vsa19_line21
    a "No matter how difficult our life was, Dad would always smile whenever I made something for him."

    voice audio.aiden_vsa19_line22
    a "He’s the reason why I always try to look on the bright side and cherish what I have!"

    voice audio.yoshi_vsa19_line11
    yo "Aiden…"

    hide cg fade
    hide fxa9
    with dissolve

    show aiden comp5 at right2
    voice audio.aiden_vsa19_line23
    a "And I guess you know the rest, since after that we got to Camp Buddy!"

    show yoshi comp2 at left2
    voice audio.yoshi_vsa19_line12
    yo "Yeah… It’s amazing how far you’ve come since then, Aiden."

    hide aiden_autumn
    hide aiden comp5
    show aiden2_autumn at right2
    show aiden2 sad4 at right2
    voice audio.aiden_vsa19_line24
    a "I do kinda wish my old man was still here to see all this…"

    voice audio.aiden_vsa19_line25
    a "If he heard about me having an opportunity to become a pro chef, he’d be over the moon."

    show yoshi comp1 at left2
    voice audio.yoshi_vsa19_line13
    yo "I’m sure he’d be so proud of you right now…!"

    show aiden2 talk3 at right2
    voice audio.aiden_vsa19_line26
    a "Yeah, I never thought I’d get a real shot to chase after something I felt was never meant for me."

    $working = False
    $shuffle_menu()
    menu():
        a "Yeah, I never thought I’d get a real shot to chase after something I felt was never meant for me.{fast}"
        "You can take things to a new level!":
            $ working = True
            $ score_aiden -= 2
            show yoshi bold2 at left2
            voice audio.yoshi_vsa19_line14a
            yo "This is the perfect opportunity to change that, Aiden!"

            show aiden2 awkward5 at right2
            voice audio.aiden_vsa19_line27a
            a "Well, it is a really big change though…"

            show yoshi talk1 at left2
            voice audio.yoshi_vsa19_line15a
            yo "Yeah, but that’s how it goes, and I know you’d be successful at it!"
        "Do it for your dad!":
            $ working = True
            $ score_aiden -= 1
            show yoshi bold2 at left2
            voice audio.yoshi_vsa19_line14b
            yo "It used to be your dad’s dream, and now you get to fulfill that for him!"

            show aiden2 comp3 at right2
            voice audio.aiden_vsa19_line27b
            a "Ahehe… Thanks a lot, pops. Now the pressure’s on me!"
        "Don't miss the chance.":
            $ working = True
            $ score_aiden += 1
            show yoshi bold2 at left2
            voice audio.yoshi_vsa19_line14c
            yo "That’s why you shouldn’t miss this chance, Aiden!"

            show yoshi happy1 at left2
            voice audio.yoshi_vsa19_line15c
            yo "It’s perfect for you, and you’d be a huge success at it!"

            hide aiden2_autumn
            hide aiden2 talk3
            show aiden_autumn at right2
            show aiden bold2 at right2
            voice audio.aiden_vsa19_line27c
            a "Yeah, you’re right, Yoshi!"
        "You have everything it takes!":
            $ working = True
            $ score_aiden += 2
            show yoshi bold2 at left2
            voice audio.yoshi_vsa19_line14d
            yo "Haha, you already had everything you needed to succeed from the start."

            show yoshi comp2 at left2
            voice audio.yoshi_vsa19_line15d
            yo "You’re talented and hard-working, so now all you have to do is take that next step!"

            hide aiden2_autumn
            hide aiden2 talk3
            show aiden_autumn at right2
            show aiden comp2 at right2
            voice audio.aiden_vsa19_line27d
            a "Aww, Yoshi… "

    hide aiden2_autumn
    hide aiden2 talk3
    hide aiden2 comp3
    hide aiden2 awkward5
    show aiden_autumn at right2
    show aiden bold2 at right2
    voice audio.aiden_vsa19_line28
    a "Alright, I made up my mind! I’m going for it!"

    voice audio.aiden_vsa19_line29
    a "You know, I thought I’d need a lot longer to think about it…"

    show aiden comp3 at right2
    voice audio.aiden_vsa19_line30
    a "’Cause as thrilled as I was to hear about the offer, I felt it was too good to be true."

    voice audio.aiden_vsa19_line31
    a "But now, knowing that there’s nothing to lose and everything to gain, I can finally make a choice for myself!"

    show yoshi happy2 at left2
    voice audio.yoshi_vsa19_line16
    yo "I’m glad you see it that way! "

    show aiden comp5 at right2
    voice audio.aiden_vsa19_line32
    a "I’m really glad I talked to you about it. Thanks for always believing in me, Yoshi!"

    show yoshi comp2 at left2
    voice audio.yoshi_vsa19_line17
    yo "I’ll always be here for you, Aiden!"

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black with fade
    yo "{i}Seeing Aiden with a newfound determination was proof of how much he’s changed… He’s finally making the effort to pursue something for his own future. {/i}"
    yo "{i}I’m gonna make sure I help him in every way I can!{/i}"

    scene cg black
    hide screen location
    hide screen timeline
    hide screen quick_menu
    $quick_menu = False
    with fade
    play sound sleeping_time
    $ time_transition_night_to_day_winter2()
    $ renpy.pause (2.0, hard=True)
    jump day9_aiden
