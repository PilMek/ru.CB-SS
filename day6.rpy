label day6:
    $ day = "06"
    $ time = timeline_timeday
    $ location = location_cabin
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    $working = True

    mys "{i}Yeah… That’s right… {/i}"
    mys "{i}It feels good, huh? {/i}"
    yo "{i}A-Ahh… Y-Yeah…{/i}"
    mys "{i}It’s been so long… I forgot how good you were in bed…{/i}"
    mys "{i}That’s right… Go slow… I like it that way…{/i}"

    scene bg_quarters_autumn_day with fade
    play music brand_new_day loop
    play bgsound sfxloop_birds loop

    show yoshi_sleep3 at center
    show yoshi_blush at center
    show yoshi shock6 at center
    voice audio.yoshi_v_shock4
    yo "G-Gah…! "
    yo "It was just a dream…"

    hide yoshi_sleep3
    hide yoshi_blush
    hide yoshi shock6
    show yoshi2_sleep3 at center
    show yoshi2_blush at center
    show yoshi2 shy3 at center
    voice audio.yoshi_v_think1a
    yo "That was strange… and also very sexual…"
    yo "Now I’m turned on too… Good thing nobody is around right now to see this… "

    show yoshi2 sigh4 at center
    voice audio.yoshi_v_sigh3a
    yo "*sigh* This must be because of what happened last night… It made me so pent up…"
    yo "I couldn’t even sleep properly thanks to that… Holding it in wasn’t a good idea, after all."

    show yoshi2 shy4 at center
    voice audio.yoshi_v_unsure3c
    yo "I guess it can’t be helped… I haven’t had time for anything like that in a long time… "

    if d5_aiden == True:
        show yoshi2 think4 at center
        voice audio.yoshi_v_aiden4
        yo "Aiden always tells me when I get urges like this that it’s best not to ignore them…"
        yo "If he were here, he would definitely help me jack off…"

        show yoshi2 shy4 at center
        voice audio.yoshi_v_unsure3c
        yo "I guess I can handle it alone this time…"
    elif d5_goro == True:
        show yoshi2 think4 at center
        voice audio.yoshi_v_sirgoro7
        yo "Sir Goro once told me that nothing beats the company of someone else when you have to relieve yourself of this kind of urge…"
        yo "Now that I think about it… I wonder if that was a subtle invite…"

        show yoshi2 shy4 at center
        voice audio.yoshi_v_unsure3c
        yo "I guess I can handle it alone this time…"

    jump day6_yoshi_1

label day6_after:
    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black with fade
    yo "{i}After relieving myself, I hurriedly cleaned up my mess and got ready for the day…{/i}"
    yo "{i}Since everyone else was gone from the cabin again this morning, they must’ve already gotten to work… I’d have to catch up.{/i}"
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

    show darius_autumn at p9_2
    show darius norm3 at p9_2
    show lloyd_autumn at p9_3
    show lloyd norm4 at p9_3
    show aiden_autumn at p9_4
    show aiden norm3 at p9_4
    show goro_autumn at p9_6
    show goro norm3 at p9_6
    show emilia_autumn2 at p9_7
    show emilia play3 at p9_7
    show jin_autumn at p9_1
    show jin norm3 at p9_1
    show jin_glasses at p9_1
    show yuri_autumn at p9_5
    show yuri norm3 at p9_5

    show yoshi_autumn at p9_9
    show yoshi confused1 at p9_9
    yo "{i}(Oh, we have a visitor! And she looks so… well-dressed.){/i}"

    show emilia play3 at p9_7
    voice audio.emilia_v_ah3
    mys_e "Ahhh~ There he is! The man of the hour~ I was waiting for you, Yoshinori!"

    show jin_autumn at p8_1
    show jin norm3 at p8_1
    show jin_glasses at p8_1
    show darius_autumn at p8_2
    show darius norm3 at p8_2
    show lloyd_autumn at p8_3
    show lloyd norm4 at p8_3
    show aiden_autumn at p8_4
    show aiden norm3 at p8_4
    show yuri_autumn at p8_5
    show yuri norm3  at p8_5
    show yoshi_autumn at p8_6
    show yoshi confused1 at p8_6
    show emilia_autumn2 at p8_7
    show emilia confused2 at p8_7
    show goro_autumn at p8_8
    show goro norm3 at p8_8
    with move

    voice audio.emilia_vs7_line1
    mys_e "Since when were you the tardy person, hmm? Have all these years at Camp Buddy really changed you that much?"

    # show cg emilia
    show yoshi shock2 at p8_6
    voice audio.yoshi_vs7_line1
    yo "Wh-What…? "

    show emilia shock2 at p8_7
    voice audio.emilia_vs7_line2
    mys_e "Wait, don’t tell me you don’t remember me?!"

    voice audio.emilia_vs7_line3
    mys_e "And here I was, hoping that you’d be the one to introduce me to everyone because you knew me the best!"

    show yoshi shock3 at p8_6
    voice audio.yoshi_vs7_line2
    yo "W-Wait a minute. Emilia?! I-Is that you?"

    show emilia happy4 at p8_7
    voice audio.emilia_vs7_line4
    e "Bingo~! You got that right! I’ll give you a pass for that lapse in memory, since this place is so far away from civilization~"

    show yoshi talk3 at p8_6
    voice audio.yoshi_vs7_line3
    yo "I… can’t believe it. It’s been so long, I barely recognized you!"

    show emilia evil2 at p8_7
    voice audio.emilia_vs7_line5
    e "I could say the same for you! And… well, everyone for that matter. "

    show yoshi confused2 at p8_6
    voice audio.yoshi_vs7_line4
    yo "What brings you back here to Camp Buddy? This is the last place I’d expect to see you… "

    show emilia confused3 at p8_7
    voice audio.emilia_vs7_line6
    e "Why that’s not a very hospitable way to welcome back an alumnus. Let’s just say I’m here on very important business."

    show goro explain2 at p8_8
    voice audio.goro_vs7_line1
    g "Ms. Komarova here was chosen to be the inspector for the whole project by Clermont Inc."

    show yoshi shock2 at p8_6
    voice audio.yoshi_vs7_line5
    yo "Whoa, really?!"

    show emilia play2 at p8_7
    voice audio.emilia_vs7_line7
    e "You seem surprised~! I hope that’s a good thing!"

    hide yoshi_autumn
    hide yoshi shock2
    show yoshi2_autumn at p8_6
    show yoshi2 shy5 at p8_6
    hide yuri_autumn
    hide yuri norm3
    show yuri_autumn at p8_5
    show yuri norm3 at p8_5
    voice audio.yoshi_vs7_line6
    yo "Oh, it’s just… It’s so unexpected! I didn’t know you worked for Mr. Clermont, especially for a job like this…"

    show emilia bold5 at p8_7
    voice audio.emilia_vs7_line8
    e "I can’t blame you for holding me to such a high standard even after all these years – I come from an unforgettably prestigious background after all~"

    voice audio.emilia_vs7_line9
    e "But after seeing the opportunity, I just knew that I was the perfect fit!"

    show emilia bold2 at p8_7
    voice audio.emilia_vs7_line10
    e "And there’s no better time than the present, so let’s get started!"

    show goro talk1 at p8_8
    voice audio.goro_v_conj5a
    g "Before anything else, I believe we should at least introduce you to the team."

    show emilia explain2 at p8_7
    voice audio.emilia_v_disagree2a2
    e "The only people I need to know are already familiar faces, so there’s no need for that."
    e "And for those new ones, you’ll know me when you know me. "

    show emilia talk3 at p8_7
    voice audio.emilia_v_conj3a
    e "Now, shall we proceed with the preliminary inspection?"

    hide yoshi2_autumn
    hide yoshi2 shy5
    show yoshi_autumn at p8_6
    show yoshi confused3 at p8_6
    voice audio.yoshi_v_wait1
    yo "Wait… I thought the inspection was scheduled for the end of the week though?"

    show emilia bold2 at p8_7
    voice audio.emilia_v_william1
    e "I told Mr. Clermont I would be arriving ahead of schedule. The best inspections are done unexpectedly, after all."

    hide yoshi_autumn
    hide yoshi confused3
    show yoshi2_autumn at p8_6
    show yoshi2 think5 at p8_6
    hide yuri_autumn
    hide yuri norm3
    show yuri_autumn at p8_5
    show yuri norm3 at p8_5
    voice audio.yoshi_v_isee2
    yo "I see…"

    show emilia play5 at p8_7
    voice audio.emilia_v_conj5b
    e "After all, you’ve hooked a pretty big fish – having Clermont Inc. sponsor this camp."
    e "Thankfully, for all of you, I’m here to make sure he gets his money’s worth~"

    hide yoshi2_autumn
    hide yoshi2 think5
    hide emilia_autumn2
    hide emilia play5
    hide goro_autumn
    hide goro talk1
    with dissolve

    show jin_autumn at p5_1
    show jin confused3 at p5_1
    show jin_glasses at p5_1
    show darius_autumn at p5_2
    show darius think4 at p5_2
    show lloyd_autumn at p5_3
    show lloyd think5 at p5_3
    show aiden_autumn at p5_4
    show aiden norm3 at p5_4
    show yuri_autumn at p5_5
    show yuri annoy2 at p5_5
    with move

    voice audio.jin_v_psst1a
    j "Pssst… Can you guys fill me in on who she is? Seems like she knows the rest of you."
    j "And she looks like she isn’t a fan of introductions either…"

    show lloyd think5 at p5_3
    voice audio.lloyd_v_shock1a1
    l "Oh… She’s that rich girl from back then. Can’t forget about her."

    show darius think4 at p5_2
    voice audio.darius_v_conj1a2
    d "I did."

    hide aiden_autumn
    hide aiden norm3
    show aiden2_autumn at p5_4
    show aiden2 confused5 at p5_4
    voice audio.aiden_v_unsure4a
    a "I’m not sure I remember right, but… I think she used to hang out with Yoshi a lot…"

    show jin shock2 at p5_1
    voice audio.jin_v_whoa1c
    j "Whoa! Yoshinori? Really?"

    show aiden2 sigh4 at p5_4
    voice audio.aiden_v_confused1c1
    a "Ehh… I think the more accurate term was ‘clingy’. Yoshi’s super nice to everyone, after all."

    show yuri annoy2 at p5_5
    voice audio.yuri_v_ugh2a
    yu "You mean, Yoshi’s the only one who tolerated her. Ugh… Why does she have to be the inspector, of all people?"

    show jin worry4 at p5_1
    voice audio.jin_v_think2a1
    j "Sounds like everyone isn’t a fan of her…"

    show yuri sigh2 at p5_5
    voice audio.yuri_v_sigh2a
    yu "It can’t be helped. She made quite the impression from the very start."

    hide aiden2_autumn
    hide aiden2 sigh4
    show aiden_autumn at p5_4
    show aiden explain2 at p5_4
    voice audio.aiden_v_yeah2a1
    a "Oh yeah… It was on a camping trip, if I remember right…"

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

    $ location = location_fields
    $ day = "??"
    $ time = timeline_timeday
    $ season = season_summer
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_fields_past_day with fade
    play music adventure loop
    play bgsound sfxloop_windy loop

    show ygoro_camp at center
    show ygoro talk1 at center
    voice audio.ygoro_v_alright1a
    g "Alright, we’ve arrived at our destination! "
    g "For this camping trip, I want you all to work together in groups of six to set up camp!"

    show ygoro explain2 at center
    voice audio.ygoro_v_response1b1
    g "I’ve assigned different tasks for each group, and everyone needs to finish before sunset!"
    g "Your scoutmasters will be watching, and if we see any of you slacking off, you’ll get a demerit badge!"

    show ygoro_camp at p4_1
    show ygoro explain2 at p4_1
    with move

    show yyoshi_camp at p4_2
    show yyoshi bold2 at p4_2
    show yyuri_camp2 at p4_3
    show yyuri norm2 at p4_3
    show yaiden_casual at p4_4
    show yaiden norm1 at p4_4
    with dissolve

    voice audio.yyoshi_v_sirgoro2
    yo "Oh, Sir Goro! I can be in charge of the tents! "

    show ygoro laugh1 at p4_1
    voice audio.goro_v_laugh2a
    g "Hahaha! Getting dibs on the most difficult one, I see. "

    show yyoshi bold5 at p4_2
    voice audio.yyoshi_v_response3a
    yo "That’s not a problem, Sir Goro! I already have Yuri and Aiden with me anyway! We just need to get three more people!"

    show ygoro happy3 at p4_1
    voice audio.ygoro_v_alright1a
    g "*pats head* Alright! I’ll leave that up to you, and I’ll check on your group myself before sunset!"

    show yyoshi bold2 at p4_2
    voice audio.yyoshi_v_yessir2a
    yo "Yes, sir! Thank you, sir!"

    show ygoro bold2 at p4_1
    voice audio.ygoro_v_dismiss2a
    g "I’ll attend to the other groups! Get to work!"

    hide ygoro_camp
    hide ygoro bold2
    with dissolve

    show yyoshi_camp at left
    show yyoshi bold5 at left
    show yyuri_camp2 at center
    show yyuri annoy2 at center
    show yaiden_casual at right
    show yaiden at right
    with move

    voice audio.yyuri_v_yoshi11a
    yu "Yoshi, why did you have to choose the most boring chore…? We could’ve gone exploring and finding stuff like firewood or something!"

    show yyoshi happy2 at left
    voice audio.yyoshi_v_what1a
    yo "We already did that last camping trip! We don’t want to do the same thing over and over, right?"
    yo "Besides, it’ll show the scoutmasters how flexible we are, no matter the task!"

    show yyuri annoy4 at center
    voice audio.yyuri_v_hmph1a
    yu "You’re such a dork, Yoshi."

    show yaiden happy2 at right
    voice audio.yaiden_v_hey1a1
    a "I think it’ll be fun! It’s my first time actually joining you guys camping, after all!"

    show yyoshi play3 at left
    voice audio.yyoshi_v_confident5
    yo "See? Aiden gets it! Where’s your camping spirit, Yuri?"

    show yyuri sigh1 at center
    voice audio.yyuri_v_sigh2a
    yu "*sigh* Fine, you guys win. "
    yu "Where are we gonna get three more people though? We definitely need the help, ’cause I'm not good at building like Yoshi."

    show yyoshi_camp at p5_3
    show yyoshi play3 at p5_3
    show yyuri_camp2 at p5_4
    show yyuri sigh1 at p5_4
    show yaiden_casual at p5_5
    show yaiden happy2 at p5_5
    with move

    show ydarius_camp at p5_1
    show ydarius norm2 at p5_1
    show ylloyd_camp at p5_2
    show ylloyd excited3 at p5_2
    with dissolve

    voice audio.ylloyd_v_excited1b
    l "Did somebody say BUILDING?!"
    l "Look no more, the Dar-Lloyd Builder Duo is here to save the day!"

    show yyuri talk2 at p5_4
    voice audio.yyuri_v_oh1a
    yu "Oh, it’s Little Lloyd and Serious Darius! "

    show ylloyd angry2 at p5_2
    voice audio.ylloyd_v_greet2d1
    l "HEY! Do you want our help or not?!"

    show yaiden grin1 at p5_5
    voice audio.yaiden_v_praise3a
    a "Cool! With Darius on our team, this will be a piece of cake!"

    show ylloyd angry5 at p5_2
    voice audio.ylloyd_v_annoyed2a
    l "Hello?! I’m here!"

    show ydarius happy1 at p5_1
    voice audio.ydarius_v_greet1a3
    d "Hi."

    show yyoshi happy1 at p5_3
    voice audio.yyoshi_v_praise2
    yo "Great, that’s two more! Welcome to the group!"

    show yaiden happy1 at p5_5
    voice audio.yaiden_v_oh1a
    a "Just one left, then!"

    show yyoshi think2 at p5_3
    voice audio.yyoshi_v_think1a
    yo "Yeah… Hmm, let’s see…"
    yo "Everyone else seems to have their own groups already…"

    show ylloyd_camp at p7_1
    show ylloyd angry5 at p7_1
    show ydarius_camp at p7_2
    show ydarius happy1 at p7_2
    show yyoshi_camp at p7_3
    show yyoshi talk3 at p7_3
    show yyuri_camp2 at p7_4
    show yyuri talk2 at p7_4
    show yaiden_casual at p7_5
    show yaiden happy1 at p7_5
    with move

    show yemilia_camp at p7_7
    show yemilia upset4 at p7_7
    with dissolve

    voice audio.yyoshi_v_wait2
    yo "Oh, wait, how about her? She looks like she’s just standing there alone. Why don’t we invite her?"

    show yyuri confused2 at p7_4
    voice audio.yyuri_v_confused2a1
    yu "The new girl? "

    show yyoshi happy1 at p7_3
    voice audio.yyoshi_v_yeah2
    yo "Yeah!"

    show yyuri explain1 at p7_4
    voice audio.yyuri_v_unsure1b3
    yu "I don’t know… I’ve heard a lot of things about her… So, I just try and stay away."

    show yyoshi awkward4 at p7_3
    voice audio.yyoshi_v_really4
    yo "What? Really?"

    show ylloyd think2 at p7_1
    voice audio.ylloyd_v_agree4b4
    l "Oh yeah, I heard she made quite the scene when she was enrolled here a few days ago…"

    show yyuri confused6 at p7_4
    voice audio.yyuri_v_think1a1
    yu "Dad said she’s from a very wealthy family… I don’t think she’s used to a more “rustic” lifestyle…"
    yu "Rumor is that she screamed, scratched and cursed at the scoutmasters ’cause she didn’t want to be here. "

    show yaiden scared1 at p7_5
    voice audio.yaiden_v_shock2b1
    a "Yikes, sounds like a red flag."

    show ydarius disgust2 at p7_2
    voice audio.ydarius_v_tease1a
    d "Stranger danger."

    show yyuri talk4 at p7_4
    voice audio.yyuri_v_really2a
    yu "I didn’t hear anything like that from Dad though… Is that really true?"

    show yyoshi at p7_3
    voice audio.yyoshi_v_yeah2
    yo "Yeah! Maybe some people just made that up! I really don’t like it when others gossip like that!"
    yo "Besides, we haven’t even met her yet! We can’t judge anyone without getting to know them first!"

    show yyoshi talk1 at p7_3
    voice audio.yyoshi_v_conj3a
    yo "Either way, we need one more person, so I’ll invite her!"

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    hide ylloyd_camp
    hide ylloyd think2
    hide ydarius_camp
    hide ydarius disgust2
    hide yaiden_casual
    hide yaiden scared1
    hide yyuri_camp2
    hide yyuri talk4
    with dissolve

    show yyoshi_camp at p7_6
    show yyoshi happy2 at p7_6
    with move

    show yyoshi_camp at left2
    show yyoshi happy2 at left2
    show yemilia_camp at right2
    show yemilia norm3 at right2
    with move

    play music heracleum_a loop
    voice audio.yyoshi_v_greet1a
    yo "Hello! "

    show yemilia annoy1 at right2
    e "..."

    show yyoshi happy3 at left2
    voice audio.yyoshi_v_intro1
    yo "My name is Yoshinori Nagira! "

    show yyoshi happy1 at left2
    voice audio.yyoshi_v_question1a
    yo "What’s yours?"

    show yemilia annoy2 at right2
    voice audio.yemilia_v_question1b
    e "Umm, why are you talking to me?"

    show yyoshi shy5 at left2
    voice audio.yyoshi_v_well2
    yo "Well… You were by yourself over here, so I thought you might want to join our group for the activity!"
    yo "Do you want to help us set up tents?"

    show yemilia pain5 at right2
    voice audio.yemilia_v_disgust2b
    e "Ew, disgusting! I’m not getting my hands dirty on something like that!"

    show yyoshi play2 at left2
    voice audio.yyoshi_v_rush3
    yo "Come on! It’ll be fun! You’ll get in trouble if you just stand there after all!"

    show yemilia angry2 at right2
    voice audio.yemilia_v_praise1a
    e "Good. I’d rather be expelled from this place then forced to do menial labor."

    show yyoshi confused2 at left2
    voice audio.yyoshi_v_huh1
    yo "If you really hate it here so much why did you join?"

    show yemilia angry6 at right2
    voice audio.yemilia_v_annoyed2a
    e "It’s none of your business. Just leave me alone."

    show yyoshi explain2 at left2
    voice audio.yyoshi_v_alright5
    yo "Well, I guess you’re gonna have to spend the night out in the cold, then."
    yo "Sleeping on the grass, getting wet from the morning dew, and then there’s the bugs…"

    show yyoshi confused5 at left2
    voice audio.yyoshi_v_oh1
    yo "Oh, and did I mention there’s always a risk of getting mauled by a bear while you sleep?"

    show yemilia panic3 at right2
    voice audio.yemilia_v_what2
    e "Wh-What?! Do you mean we’re staying here overnight?!"

    show yyoshi comp3 at left2
    voice audio.yyoshi_v_imean1
    yo "I mean… We are at “Camp” Buddy… Why else would we be setting up tents and making a campfire?"

    show yemilia annoy1 at right2
    e "..."

    show yemilia sigh1 at right2
    voice audio.yemilia_v_ugh1
    e "I swear this godforsaken camp will be the end of me! I’m surrounded by idiots! "

    show yyoshi laugh1 at left2
    voice audio.yyoshi_v_rush2
    yo "Come on, don’t be so dramatic!"

    show yemilia angry3 at right2
    voice audio.yemilia_v_question4c1
    e "Dramatic?! You have no idea how terrible this is compared to my high-end lifestyle!"
    e "They could’ve sent at least one butler for me to order around!"

    show yemilia rage4 at right2
    voice audio.yemilia_v_annoyed1b
    e "Ugh! Why did my parents even send me here?! I can’t believe they spent money just for me to be forced into labor!"

    show yyoshi bold2 at left2
    voice audio.yyoshi_v_confident6
    yo "It’s not just work! It’s a learning experience, and it’ll be fun! "

    show yemilia annoy2 at right2
    voice audio.yemilia_v_disagree3b
    e "There’s nothing ‘fun’ about setting up tents. And I don’t need to learn how, especially when I have people to do it for me."

    show yyoshi angry2 at left2
    voice audio.yyoshi_v_rush3
    yo "Oh, come on, that’s not what the camp spirit is about! "

    show yemilia eyeroll4 at right2
    voice audio.yemilia_v_ugh1
    e "Eugh…"

    show yyoshi grin1 at left2
    voice audio.yyoshi_v_well1
    yo "You can roll your eyes all you want, but you’re here at Camp Buddy! "
    yo "Don’t you think it would be a lot better if you try and enjoy your time here instead of sulking all day?"

    show yyoshi play2 at left2
    voice audio.yyoshi_v_laugh1
    yo "If you keep this up, you’ll be bear food later tonight!"

    show yemilia shy6 at right2
    voice audio.yemilia_v_laugh2
    e "Oh, shut up! Do you really think I’m stupid enough to believe that?"

    show yyoshi laugh2 at left2
    voice audio.yyoshi_v_laugh2a
    yo "Haha, I’m just kidding! You’ve been frowning this whole time – you don’t want wrinkles on your face, do you?"

    show yemilia confused3 at right2
    voice audio.yemilia_v_what2
    e "Wh-What…? Wrinkles…? "

    show yemilia shy4 at right2
    voice audio.yemilia_v_pft1b
    e "Pffft!! "

    show yyoshi comp6 at left2
    voice audio.yyoshi_v_laugh5
    yo "A-Ahehe…"

    show yemilia shy3 at right2
    voice audio.yemilia_v_laugh1
    e "You’re such a weirdo, what the heck?!"

    show yyoshi comp2 at left2
    voice audio.yyoshi_v_response2a
    yo "I’ve been called that a couple of times, but I try to take it as a compliment."

    show yemilia tease2 at right2
    voice audio.yemilia_v_surprised1a1
    e "Are you for real?!"

    show yyoshi bold3 at left2
    voice audio.yyoshi_v_confident1
    yo "“The best scout around,” say the scoutmasters! I’m as real as you can get!"

    show yemilia comp2 at right2
    voice audio.yemilia_v_isee1b
    e "You’re not like the other people around here huh…?  "

    show yyoshi bold2 at left2
    voice audio.yyoshi_v_laugh1
    yo "They did say I stand out from the crowd, after all."

    show yemilia bold4 at right2
    voice audio.yemilia_v_laugh2
    e "*chuckles*"

    show yyoshi happy2 at left2
    voice audio.yyoshi_v_so3
    yo "So, you wanna join our tent-building group?"

    show yemilia explain2 at right2
    voice audio.yemilia_v_response1a2
    e "Fine. I’ll join your group. But you won’t see me doing any of that filthy work. "

    show yyoshi laugh2 at left2
    voice audio.yyoshi_v_alright5
    yo "Alright! Come with me then!"

    show yyoshi_camp at p6_5
    show yyoshi at p6_5
    show yemilia_camp at p6_6
    show yemilia at p6_6
    with move

    show ylloyd_camp at p6_1
    show ylloyd norm3 at p6_1
    show ydarius_camp at p6_2
    show ydarius norm3 at p6_2
    show yyuri_camp2 at p6_3
    show yyuri norm3 at p6_3
    show yaiden_casual at p6_4
    show yaiden norm3 at p6_4
    with dissolve

    voice audio.yyoshi_v_awkward1
    yo "Here she is! This is… umm… uhh…"
    yo "I think you forgot to tell me your name!"

    show yemilia annoy2 at p6_6
    voice audio.yemilia_v_sarcastic2b
    e "I just chose not to tell you, stupid."

    show yyoshi comp3 at p6_5
    voice audio.yyoshi_v_laugh5
    yo "A-Ahehe…"

    show yemilia talk1 at p6_6
    voice audio.yemilia_v_intro1
    e "It’s Emilia. Emilia Komarova."

    show yyoshi laugh1 at p6_5
    voice audio.yyoshi_v_emilia2
    yo "Emilia! That’s a nice name!~ "
    yo "Well, Emilia, I’d like to introduce you to your new teammates!"

    show yemilia explain2 at p6_6
    voice audio.yemilia_v_disagree2a
    e "No need for introductions, I already know about them. "

    show yyuri annoy1 at p6_3
    show yaiden shock1 at p6_4
    e "Pink hair’s the scoutmaster’s daughter, the one not in a uniform is part of the help…"

    show yemilia think2 at p6_6
    voice audio.yemilia_v_lloyd3a
    e "Oh, and the other two are just regular background characters."

    show ylloyd angry2 at p6_1
    voice audio.ylloyd_v_question1c4
    l "B-Background?!"

    show yemilia talk1 at p6_6
    voice audio.yemilia_v_bossy5
    e "I’ve already reviewed who the people around me are without actually talking to them. "
    e "I always like to be a step ahead of everybody else."

    show yyoshi talk3 at p6_5
    voice audio.yyoshi_v_unsure3b
    yo "Well, maybe we could get to know you instead? "

    show yemilia bold4 at p6_6
    voice audio.yemilia_v_disagree4a
    e "There’s no need, you’ll know me when you know me."

    show yyuri annoy2 at p6_3
    voice audio.yyuri_v_well3a
    yu "Well, I’m learning about you right now."

    show yaiden talk4 at p6_4
    voice audio.yaiden_v_oops3a
    a "and I oop—"

    show yyoshi shy5 at p6_5
    voice audio.yyoshi_v_anyway2
    yo "A-Anyway, why don’t we just focus on the task at hand? We have to build these tents!"

    show yemilia annoy2 at p6_6
    voice audio.yemilia_v_dismiss2
    e "Yeah, I’m still not doing that."

    show yyuri irked2 at p6_3
    voice audio.yyuri_v_sarcastic1a1
    yu "So much for being “a step ahead of everybody else.”"
    yu "Why did you invite her to our group again, Yoshi?"

    show yaiden comp6 at p6_4
    voice audio.yaiden_v_yuri6a
    a "Yuri, chill!"

    show yemilia angry2 at p6_6
    voice audio.yemilia_v_question4a
    e "Excuse me, I wasn’t ‘invited’. I simply had no choice since Yoshinori here wouldn’t take ‘no’ for an answer."
    e "And I don’t lie about things I can’t do. I’m not supposed to know everything, hmph!"

    show yyoshi bold2 at p6_5
    voice audio.yyoshi_v_confident2
    yo "Well, I’ll help you get started if you don’t know the basics! I promise it’s not that complicated!"

    show yemilia confused4 at p6_6
    e "..."

    show yemilia angry5 at p6_6
    voice audio.yemilia_v_response1a1
    e "Fine!"
    e "But only because you’re doing a better job at giving me the special treatment I deserve than everyone else."

    show yyuri_camp2 at p6_4
    show yyuri angry6 at p6_4
    show yaiden_casual at p6_3
    show yaiden angry2 at p6_3
    with move

    voice audio.yyuri_v_ugh1a
    yu "Ugh… Do we really have to work with her…?"

    show yyoshi angry2 at p6_5
    voice audio.yyoshi_v_yuri9b
    yo "Come on, Yuri! Give her a chance! "

    show yemilia angry3 at p6_6
    voice audio.yemilia_v_well1
    e "Well, are you going to keep me waiting?"

    show yyoshi comp3 at p6_5
    voice audio.yyoshi_v_request2a
    yo "Ah, of course! Let me lead the way!"

    hide yyoshi_camp
    hide yyoshi comp3
    hide yemilia_camp
    hide yemilia angry3
    with dissolve

    show ylloyd_camp at p4_1
    show ylloyd sigh5 at p4_1
    show ydarius_camp at p4_2
    show ydarius comp2 at p4_2
    show yaiden_casual at p4_3
    show yaiden kiss2 at p4_3
    show yyuri_camp2 at p4_4
    show yyuri angry3 at p4_4
    with move

    $ renpy.music.stop(channel='music', fadeout = 3.0)
    voice audio.yaiden_v_whistle1a
    a "*whistles* That’s one spicy girl… And I’m not a fan of spicy."

    show ylloyd sigh5 at p4_1
    voice audio.ylloyd_v_i1
    l "I… can’t believe she called us background characters…"

    show ydarius comp2 at p4_2
    voice audio.ydarius_v_lloyd7c
    d "You’re a main character to me."

    show ylloyd sigh4 at p4_1
    voice audio.ylloyd_v_sigh2b
    l "Th-That… doesn’t help at all."

    show yyuri angry3 at p4_4
    voice audio.yyuri_v_sus2a
    yu "This is the reason why I didn’t want her on our team… There’s something really off about her."
    yu "But I guess Yoshi sees something in her that we don’t."

    show yaiden comp2 at p4_3
    voice audio.yaiden_v_celebrate1a
    a "Haha, Yoshi does have a good eye for people, so maybe we should just give her a chance! "

    show ylloyd confused2 at p4_1
    voice audio.ylloyd_v_think1a1
    l "Maybe she’s the kind that mellows out as you hang out with her more."

    show yyuri angry6 at p4_4
    voice audio.yyuri_v_sigh2a
    yu "*sigh* I hope you guys are right. But she still doesn’t pass my vibe check. "
    yu "It’s a girl’s intuition. You guys wouldn’t understand."

    show yaiden comp5 at p4_3
    voice audio.yaiden_v_laugh1b1
    a "Hehe, can’t argue with that~"

    show yyuri annoy4 at p4_4
    voice audio.yyuri_v_anyway2a
    yu "Anyways, let’s help Yoshi out before he gets pushed around all day!"

    scene cg white with Dissolve(2.0)
    $past_scene = False

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
    $ day = "06"
    $ time = timeline_timeday
    $ season = season_autumn
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_campgrounds_autumn_day with fade
    play bgsound sfxloop_birds loop
    play music heracleum_a loop

    show jin_autumn at p8_1
    show jin norm4 at p8_1
    show jin_glasses at p8_1
    # show lloyd_autumn at p8_2
    # show lloyd norm4 at p8_2
    show darius_autumn at p8_3
    show darius norm3 at p8_3
    show aiden_autumn at p8_4
    show aiden norm3 at p8_4
    show yuri_autumn at p8_5
    show yuri annoy1 at p8_5
    show yoshi_autumn at p8_6
    show yoshi norm3 at p8_6
    # show emilia_autumn2 at p8_7
    # show emilia talk1 at p8_7
    show goro_autumn at p8_8
    show goro norm3 at p8_8

    hide lloyd_autumn
    hide lloyd norm4
    show lloyd_autumn at p8_2
    show lloyd norm4 at p8_2
    hide emilia_autumn2
    hide emilia talk1
    show emilia_autumn2 at p8_7
    show emilia talk1 at p8_7

    voice audio.emilia_v_conj2a
    e "Okay, that’s enough chitchat and reunions for today!"
    e "I came here for work, and there’s a LOT of stuff I need to inspect on my checklist, after all."

    show emilia explain3 at p8_7
    voice audio.emilia_v_greet1
    e "You may all resume your scheduled tasks, as I would rather conduct my evaluation while everyone is at work in their departments. "

    show goro talk3 at p8_8
    voice audio.goro_v_agree2a2
    g "Ah, yes, of course… Let me give you a tour."

    show emilia confused5 at p8_7
    voice audio.emilia_v_disagree2a2
    e "That won’t be necessary. Not much has changed here, so I still know my way around."
    e "More importantly, I would prefer to have an uninterrupted, unbiased assessment."

    show goro confused1 at p8_8
    show emilia explain3 at p8_7
    voice audio.emilia_v_conj5b
    e "As the camp president, you would unintentionally leave out flaws that an inspector should know about. Not that anything’s wrong with that – I’m sure you understand."

    show goro disappoint2 at p8_8
    voice audio.goro_v_isee1b
    g "Hm… Very well, then."

    show emilia relief3 at p8_7
    voice audio.emilia_v_response2a
    e "But I don’t mind having a different escort, if you truly insist."
    e "Yoshinori!"

    show yoshi shock2 at p8_6
    voice audio.yoshi_v_huh4b
    yo "H-Huh?"

    show emilia play2 at p8_7
    voice audio.emilia_v_rush1b1
    e "You’ll be happy to assist me with my inspection, yes?"

    show yoshi comp2 at p8_6
    voice audio.yoshi_v_agree1b1
    yo "O-Of course. "

    show emilia laugh1 at p8_7
    voice audio.emilia_v_amazed1b
    e "Perfect! I’d expect nothing less from you, after all~"

    show yoshi talk3 at p8_6
    voice audio.yoshi_v_request2b
    yo "Alright, then. Please follow me."

    hide yoshi_autumn
    hide yoshi talk3
    hide emilia_autumn2
    hide emilia laugh1
    with dissolve

    show jin_autumn at p6_1
    show jin norm4 at p6_1
    show jin_glasses at p6_1
    show lloyd_autumn at p6_2
    show lloyd norm4 at p6_2
    show darius_autumn at p6_3
    show darius norm3 at p6_3
    show aiden_autumn at p6_4
    show aiden sigh4 at p6_4
    show yuri_autumn at p6_5
    show yuri irked2 at p6_5
    show goro_autumn at p6_6
    show goro sigh1 at p6_6
    with move

    voice audio.aiden_v_relief1a1
    a "Whew, she’s still as feisty as ever!"

    show goro sigh1 at p6_6
    voice audio.goro_v_hmph1a
    g "I’d say it’s still an improvement compared to how she acted as a scout."

    show yuri irked2 at p6_5
    voice audio.yuri_v_sigh2a
    yu "*sigh* She’s still the same snooty person if you ask me."

    show goro talk1 at p6_6
    voice audio.goro_v_well1a
    g "Well, we don’t have a choice. Mr. Clermont handpicked her for the position."
    g "Now, let’s go back to work."

    show aiden talk6 at p6_4
    show yuri annoy2 at p6_5
    show jin talk2 at p6_1
    show lloyd talk2 at p6_2
    show darius talk2 at p6_3
    all "Yes, sir!"

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
    scene bg_site2_autumn_day with fade
    play bgsound sfxloop_birds loop
    play music brand_new_day loop

    show emilia_autumn2 at left2
    show emilia norm1 at left2
    show yoshi_autumn at right2
    show yoshi talk1 at right2
    voice audio.yoshi_v_anyway2
    yo "—The east is the intended site for additional cabins, while the west is meant for the proposed function hall."
    yo "As you can see, the construction department has nearly entirely cleared the site despite some minor delays. I’ve been told by our architect that we can proceed with earthworks very soon."

    show yoshi talk2 at right2
    voice audio.yoshi_v_conj3a
    yo "If you’d like to take a closer look, I can walk you around the site for—"

    show emilia talk5 at left2
    voice audio.emilia_v_worry5
    e "My, my, Yoshinori. Slow down a little. My heels are killing me."

    show yoshi awkward4 at right2
    voice audio.yoshi_v_sorry1a1
    yo "O-Oh, I-I apologize…! "

    show emilia annoy2 at left2
    voice audio.emilia_v_question1b1
    e "It’s just the two of us here, why are you in such a hurry? All you’ve talked about is work ever since I got here."

    hide yoshi_autumn
    hide yoshi awkward4
    show yoshi2_autumn at right2
    show yoshi2 confused2 at right2
    voice audio.yoshi_v_uh1b
    yo "I thought that you needed a quick and concise inspection…"

    show emilia sad3 at left2
    voice audio.emilia_v_agree2a1
    e "Well yes, but what I mean is that you haven't really told me anything about yourself!"

    show yoshi2 awkward3 at right2
    voice audio.yoshi_v_what3
    yo "Wh-What?"

    show emilia play2 at left2
    voice audio.emilia_v_well1
    e "It’s been almost what…? A decade? Aren’t you going to let me catch up with what’s been happening in your life?"

    show yoshi2 think5 at right2
    voice audio.yoshi_v_well1
    yo "Well… It’s been okay. For the most part."

    show emilia disgust3 at left2
    voice audio.emilia_v_ugh1
    e "That is the blandest response I’ve ever heard from you! Aren’t you supposed to be the sunshine scout around here?"

    show yoshi2 shy3 at right2
    voice audio.yoshi_v_ah3
    yo "A-Ah… I just wasn’t expecting a question like that during this inspection…"

    show emilia angry1 at left2
    voice audio.emilia_v_scoff1
    e "Hmph! I’m a little disappointed, I thought you’d be more eager to catch up with an old colleague!"

    hide yoshi2_autumn
    hide yoshi2 shy3
    show yoshi_autumn at right2
    show yoshi worry2 at right2
    voice audio.yoshi_v_sorry3a
    yo "I’m so sorry about that, Emilia. But don’t get me wrong, I am actually glad to see you again! "
    yo "And to answer your question - Not much has changed for me, except that I’m a scoutmaster now!"

    show emilia talk1 at left2
    voice audio.emilia_v_conj4b
    e "I’d say that’s the least surprising change. I knew from the moment we met that you’d end up back at this place. "

    show yoshi talk1 at right2
    voice audio.yoshi_v_well3
    yo "W-Well, I did have a bit of a rocky start for my first couple of terms, but thankfully, things have turned out fine."

    show emilia confused2 at left2
    voice audio.emilia_v_question2b
    e "Really? I thought someone like you would’ve pulled off this kind of job without a hitch."

    show yoshi comp6 at right2
    voice audio.yoshi_v_laugh1
    yo "Haha, the job’s not all the fun and games I thought when we were young, but I couldn’t be any happier here. This is more than just a job to me, after all."

    show emilia think2 at left2
    voice audio.emilia_v_disagree3a
    e "I’d beg to differ. You didn’t seem so enthused showing me around. You looked rather stressed, actually."
    e "Like waking up last and being so frantic about this inspection. "

    show yoshi comp3 at right2
    voice audio.yoshi_v_ah1
    yo "Ah… I’m so embarrassed that you noticed…"
    yo "I’ve been trying to be as useful as I can ever since this project started, and sometimes it just gets overwhelming, is all!"

    show emilia shock6 at left2
    voice audio.emilia_v_surprised1b2
    e "My goodness… You? Overwhelmed with work? That doesn’t sound like you at all."
    e "Weren’t you such the go-getter back then? Since that was how you and I ended up as acquaintances!"

    show emilia think2 at left2
    voice audio.emilia_v_scoff1
    e "*scoffs* Unlike the other scouts."
    e "Anyway, would you mind telling me exactly what you’re having difficulty with about your work?"

    hide yoshi_autumn
    hide yoshi comp3
    show yoshi2_autumn at right2
    show yoshi2 confused5 at right2
    voice audio.yoshi_v_uh1a
    yo "Is this… part of your review…? "

    show emilia shock6 at left2
    voice audio.emilia_v_what1
    e "What? No! Of course not! "
    e "Although, now that you’ve said it – you could consider it a check for a healthy working environment."

    hide yoshi2_autumn
    hide yoshi2 confused5
    show yoshi_autumn at right2
    show yoshi explain2 at right2
    voice audio.yoshi_v_conj4b
    yo "It’s not that serious, honestly. I’m probably just adjusting to all the changes around here slower than everyone else."

    show emilia confused2 at left2
    voice audio.emilia_v_question3
    e "Is that so…?"

    show yoshi talk1 at right2
    voice audio.yoshi_v_but1
    yo "Like I said, please don’t worry about it! In fact, I’ve already brought it up with someone and am trying to work on it!"
    yo "You have my word that it won’t affect the work we’re doing here!"

    show emilia explain4 at left2
    voice audio.emilia_v_response1b2
    e "Fine. I’ll take that with a grain of salt."

    show yoshi talk2 at right2
    voice audio.yoshi_v_uh1b
    yo "Should we continue with our tou—"

    show emilia laugh3 at left2
    voice audio.emilia_v_laugh1b
    e "I have to admit, I was thrilled when I confirmed you were working here at Camp Buddy. It’s just a pleasure to be reunited, don’t you think so?"

    hide yoshi_autumn
    hide yoshi talk2
    show yoshi2_autumn at right2
    show yoshi2 shy5 at right2
    voice audio.yoshi_v_ah3
    yo "A-Ah…"

    show emilia confused3 at left2
    voice audio.emilia_v_what2
    e "What’s wrong? "

    show yoshi2 confused6 at right2
    voice audio.yoshi_v_sorry1a2
    yo "Forgive me for the assumption… But I thought you disliked your time here at the camp, along with everyone in it."
    yo "In fact, I never heard anything from you after we all finished our first term."

    show emilia think3 at left2
    voice audio.emilia_v_sarcastic2b2
    e "That should’ve been obvious, don’t you think? I’m the only heir to my family’s grandiose conglomerate after all, so of course I’d be busy."

    show yoshi2 confused5 at right2
    voice audio.yoshi_v_think3
    yo "That’s why I’m really surprised that you’re excited to be back."

    show emilia bold5 at left2
    voice audio.emilia_v_well1
    e "Well, you’re not wrong, I was quite the sniveller during my stay here as a scout. But that’s so long ago."
    e "You made that summer bearable for me to say the least, so that must mean something, yes?"

    show yoshi2 think3 at right2
    voice audio.yoshi_v_isee2
    yo "I see…"

    show emilia evil2 at left2
    voice audio.emilia_v_comp1a
    e "Don’t misunderstand. I still have the same sophistication as before~ "
    e "But I’ll try to be more tolerant this time, especially with you around to make my stay pleasant again."

    show yoshi2 shy5 at right2
    voice audio.yoshi_v_right4
    yo "I-I’ll do what I can…"

    hide yoshi2_autumn
    hide yoshi2 shy5
    show yoshi_autumn at right2
    show yoshi awkward3 at right2
    voice audio.yoshi_v_anyway3a
    yo "Anyway, shall we continue the tour? I noticed you haven’t listed anything from our first department…"

    show emilia panic4 at left2
    e "...!"

    show yoshi talk1 at right2
    voice audio.yoshi_v_confident2
    yo "Do you need help or am I distracting you from the inspection?"

    show emilia angry2 at left2
    voice audio.emilia_v_angry1b
    e "Talk about rude! I’m just trying to have a conversation with you!"
    e "Goodness gracious, when did you get so impatient?!"

    show yoshi shock2 at right2
    voice audio.yoshi_v_no4
    yo "N-No, that’s not what I meant—"

    show emilia rage2 at left2
    voice audio.emilia_v_request1b1
    e "And for your information, I KNOW what I’m doing. "
    e "Mr. Clermont hired me as the quality assurance manager here because I have all the right certifications and have far exceeded the qualifications!"

    hide yoshi_autumn
    hide yoshi shock2
    show yoshi2_autumn at right2
    show yoshi2 worry5 at right2
    voice audio.yoshi_v_emilia4
    yo "I… didn’t mean it like that, Emilia…"

    show emilia angry5 at left2
    voice audio.emilia_v_hmph1b
    e "If you’re going to act like this, let’s get this tour over with!"
    e "Come on, this checklist won’t check itself!"

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black with fade
    yo "{i}(I must’ve upset Emilia by bringing up work too much during our talk…){/i}"
    yo "{i}(For the rest of the day, she was much stricter and snippier about each department we inspected, asking a lot of questions, and going into every detail…){/i}"
    yo "{i}(Eventually, we had finished everything she wanted to see, and the scoutmasters gathered in the office for her report.){/i}"

    scene cg black
    hide screen location
    hide screen timeline
    hide screen quick_menu
    $quick_menu = False
    with fade
    $ renpy.pause (2.0, hard=True)
    $ time_transition_day_to_sunset_fall()

    $ location = location_office
    $ time = timeline_timesunset
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_office_autumn_sunset with fade
    play music heracleum_b loop

    show aiden_autumn at p5_1
    show aiden worry1 at p5_1
    show yoshi_autumn at p5_2
    show yoshi worry1 at p5_2
    show emilia_autumn2 at p5_3
    show emilia annoy2 at p5_3
    show goro_autumn at p5_4
    show goro norm3 at p5_4
    show yuri_autumn at p5_5
    show yuri annoy1 at p5_5
    voice audio.emilia_v_greet1
    e "I’ll get straight to the point."
    e "Based on how the inspection went today, EVERYTHING is off from their initial targets."

    show emilia angry6 at p5_3
    voice audio.emilia_v_conj3a
    e "I will be giving general feedback on each department I had an issue with."
    e "Note that this report will be sent to Mr. Clermont, but I will enumerate all my concerns just so everyone knows where they missed the mark."

    play sound sfx_paper
    show aiden_autumn at p6_2
    show aiden worry1 at p6_2
    with move

    hide aiden_autumn
    hide aiden worry1
    show aiden2_autumn at p6_2
    show aiden2 worry5 at p6_2
    voice audio.aiden_v_sheesh1a
    a "Sheesh, Yoshi… What the heck made her so mad during the inspection?"

    hide yoshi_autumn
    hide yoshi worry1
    show yoshi2_autumn at p5_2
    show yoshi2 sad6 at p5_2
    voice audio.yoshi_v_well1
    yo "Well… I don’t think it has to do with the inspection, to be honest…"

    show aiden2 worry3 at p6_2
    voice audio.aiden_v_shock2b1
    a "I hope we’re not in trouble, then…"

    show emilia disgust5 at p5_3
    voice audio.emilia_v_question4a
    e "Um, excuse me? I need everyone’s full attention. This is very important."

    hide yoshi2_autumn
    hide yoshi2 sad6
    show yoshi_autumn at p5_2
    show yoshi awkward4 at p5_2
    voice audio.yoshi_v_sorry3b
    yo "Ah, sorry about that!"

    show aiden2_autumn at p5_1
    show aiden2 awkward4 at p5_1
    with move

    hide emilia_autumn2
    hide emilia disgust5
    show emilia_autumn2 at p5_3
    show emilia talk3 at p5_3
    voice audio.emilia_v_so1
    e "So, I’ve divided my concerns into four categories – construction, staff, technology, and management."
    e "Let’s start with construction, shall we? "

    show emilia explain4 at p5_3
    voice audio.emilia_v_think2b
    e "According to the schedule, the site should’ve been cleared yesterday. Yet, I saw it was still in progress, and took up this whole workday to finish."

    show yuri talk3 at p5_5
    voice audio.yuri_v_agree1a1
    yu "Ah, yes. It’s a good thing our staff was able to help the construction team. Or else we would’ve been delayed further."

    show emilia irked5 at p5_3
    voice audio.emilia_v_tsk1a
    e "That’s not a good thing at all. I’m concerned that we’re experiencing delays already and the project has barely started."
    e "Not to mention over a task as minor as site clearing."

    show yuri confused2 at p5_5
    voice audio.yuri_v_really2b
    yu "It’s not a big setback at all, is it? Everyone really worked hard to make up for it too."

    show emilia angry2 at p5_3
    voice audio.emilia_v_question1b2
    e "That brings me to another point: why were non-construction staff involved in the first place?"
    e "If they had been supervising as per the plan, these issues might not have happened."

    show goro talk1 at p5_4
    voice audio.goro_v_sorry1a1
    g "Ah, we apologize for stepping out of scope. There were some unforeseen difficulties that required more manpower to complete the site clearing in time."

    show emilia eyeroll3 at p5_3
    voice audio.emilia_v_tsun1b
    e "Everyone did what they thought was best in the moment, but that doesn’t change the outcome."
    e "Even if we disregarded today’s delay, there is still debris on the site. "

    show emilia irked3 at p5_3
    voice audio.emilia_v_question2b
    e "That doesn’t look like a cleared site now, does it?"

    show yuri irked1 at p5_5
    voice audio.yuri_v_actually1a
    yu "That isn't debris. We plan to recycle it as firewood for the incoming winter."

    show emilia confused2 at p5_3
    voice audio.emilia_v_disagree4a
    e "That’s not an excuse to just leave it on the site. This camp has a storage shed to keep all clutter, am I not correct?"

    show yoshi talk1 at p5_2
    voice audio.yoshi_v_alright3
    yo "We’ll make sure to work on that right away."

    show emilia talk3 at p5_3
    voice audio.emilia_v_conj3a
    e "Moving on, let’s discuss staff welfare. There’s a very peculiar rumor going around amongst the workers during my survey."
    e "I overheard that one of the management staff was being too “friendly” with the construction crew, which was causing a lot of distractions."

    hide aiden2_autumn
    hide aiden2 awkward4
    show aiden_autumn at p5_1
    show aiden scared1 at p5_1
    show yoshi talk1 at p5_2
    show emilia disgust3 at p5_3
    show goro sigh1 at p5_4
    show yuri shock1 at p5_5
    voice audio.emilia_v_disgust1
    e "One even mentioned… a “beefcake show”???"

    hide yoshi_autumn
    hide yoshi talk1
    show yoshi2_autumn at p5_2
    show yoshi2 awkward1 at p5_2
    voice audio.yoshi_v_gulp1a
    yo "*gulp*"

    show emilia disgust6 at p5_3
    voice audio.emilia_v_aiden4
    e "I am not sure what that means, but this concerns you, Mr. Flynn. "

    hide aiden_autumn
    hide aiden scared1
    show aiden2_autumn at p5_1
    show aiden2 awkward5 at p5_1
    voice audio.aiden_v_well1c1
    a "W-Well, I didn’t mean to cause any trouble… I was just trying to make the workers happy."

    show emilia irked2 at p5_3
    voice audio.emilia_v_request4b
    e "Your job isn’t to entertain them. You’re supposed to take care of their essential needs, nothing more."

    hide aiden2_autumn
    hide aiden2 awkward5
    show aiden_autumn at p5_1
    show aiden comp3 at p5_1
    voice audio.aiden_v_confused1c1
    a "Eh… I’m doing that already. I’m sure a little chit-chat here and there won’t hurt anybody, haha!"

    show emilia angry2 at p5_3
    voice audio.emilia_v_bossy1a
    e "Take this job seriously! You’re a scoutmaster, aren’t you?"

    hide aiden_autumn
    hide aiden comp3
    show aiden2_autumn at p5_1
    show aiden2 scared2 at p5_1
    voice audio.aiden_v_sorry1c1
    a "A-Ahh… Right, sorry."

    show emilia explain4 at p5_3
    voice audio.emilia_v_conj2b
    e "Next topic, technology. I consulted with Mr. Choi a while ago, and he explained all his tasks so far."
    e "Looking at the original scope of the project, I’ve noticed that some of the offered technology integration was declined?"

    show goro talk2 at p5_4
    voice audio.goro_v_ah1a
    g "Ah, I’m responsible for that. "
    g "There’s a good reason why I removed some of the proposed integrations."

    show goro talk3 at p5_4
    voice audio.goro_v_think1a1
    g "I wanted technological implementation kept to an essential minimum so that we can maintain the true essence of the camp."

    show emilia annoy3 at p5_3
    voice audio.emilia_v_tsun2b
    e "Don’t take this the wrong way, but a decision like that is nothing more than a missed opportunity."
    e "Everything is already served on a silver platter. It’s all PAID, and you just have to say yes."

    show emilia think3 at p5_3
    voice audio.emilia_v_sarcastic4
    e "These changes are inevitable anyways, so there’s no reason to hold back now."

    show goro shy1 at p5_4
    g "..."

    show emilia angry6 at p5_3
    voice audio.emilia_v_conj3b1
    e "Now, what’s causing all these issues? Everything boils down to the management department."
    e "This establishment is SEVERELY understaffed to begin with, and to be honest, most of your roles are scattered and hard to pin down. "

    show yuri annoy1 at p5_5
    show emilia annoy2 at p5_3
    voice audio.emilia_v_yuri4
    e "For example, Ms. Nomoru isn’t well-versed enough to be supervising the entire construction department."

    show aiden2 sad5 at p5_1
    show emilia angry2 at p5_3
    voice audio.emilia_v_aiden4
    e "Is Mr. Flynn really a scoutmaster, or still a helper? He contrastingly handles maintenance and culinary tasks, which are supposed to be done by two different people."

    show yoshi2 shy3 at p5_2
    show emilia annoy5 at p5_3
    voice audio.emilia_v_yoshi3
    e "And most importantly, it has come to my attention that Yoshinori has no permanent role around the camp!"

    show goro annoy1 at p5_4
    e "I personally know that he is skillful in management; but I assume it’s hard for him to step up if the figure of authority is not allowing him to use his full potential."

    show aiden2 sad4 at p5_1
    show yoshi2 upset1 at p5_2
    show goro flat1 at p5_4
    show yuri annoy1 at p5_5
    all "..."

    show emilia explain2 at p5_3
    voice audio.emilia_v_bossy2a2
    e "That sums up all of my concerns. I hope everyone paid attention."

    show goro disappoint2 at p5_4
    voice audio.goro_v_comp1b2
    g "We understand, and I take responsibility as the camp president."
    g "It’s my duty to prevent these issues and direct everyone to achieve our mutual goals. "

    show yuri worry2 at p5_5
    voice audio.yuri_v_goro6a
    yu "Dad… "

    show goro talk1 at p5_4
    voice audio.goro_v_but1b
    g "I will do my best to make everything right from hereon."

    show emilia talk1 at p5_3
    voice audio.emilia_v_response2a
    e "Very well. Mr. Clermont chose me to guarantee that this sponsorship meets his expectations."
    e "With that in mind and considering your staffing issue, I will personally stay here for the span of this project."

    show emilia bold5 at p5_3
    voice audio.emilia_v_so1
    e "This will ensure a stricter schedule and allow me to serve as a bridge of communication between Camp Buddy and Clermont Inc."

    show yuri irked1 at p5_5
    voice audio.yuri_v_question1b
    yu "Is that really necessary? We regularly receive our tasks from Mr. Clermont himself. And as far as I know we haven’t had any problems when it comes to communication."

    show emilia irked2 at p5_3
    voice audio.emilia_v_william2
    e "Mr. Clermont is a very busy man, and it’s unreasonable to expect to maintain direct communication with him throughout the entire project."
    e "He doesn’t have time to handle every issue that arises. So, that’s where I come in."

    show emilia irked5 at p5_3
    voice audio.emilia_v_bossy4
    e "My job is to prevent problems. I can already see cracks forming in the work done so far, and I need to resolve them as early as possible."
    e "Do you want to wait until a serious concern arises? Do you want to break Mr. Clermont’s trust on this project? I assume the answer to both is no."

    show aiden2 worry1 at p5_1
    show yoshi2 upset1 at p5_2
    show yuri pout2 at p5_5
    show goro annoy1 at p5_4
    all "..."

    show emilia explain4 at p5_3
    voice audio.emilia_v_comp1a
    e "Don’t take any of this personally, it’s just my job after all."

    $working = False
    $shuffle_menu()
    menu():
        e "Don’t take any of this personally, it’s just my job after all.{fast}"
        "We'll do better next time.":
            $working = True
            $score_aiden += 1
            hide yoshi2_autumn
            hide yoshi2 upset1
            show yoshi_autumn at p5_2
            show yoshi talk1 at p5_2
            yo "We’ll do better next time."

            show emilia evil3 at p5_3
            voice audio.emilia_v_bossy3b
            e "As you should."
        "We understand your concerns.":
            $working = True
            $score_goro += 1
            hide yoshi2_autumn
            hide yoshi2 upset1
            show yoshi_autumn at p5_2
            show yoshi talk1 at p5_2
            yo "We understand your concerns."

            show emilia evil3 at p5_3
            voice audio.emilia_v_bossy3b
            e "As you should."
        "We'll try to meet your expectations.":
            $working = True
            $score_aiden += 2
            hide yoshi2_autumn
            hide yoshi2 upset1
            show yoshi_autumn at p5_2
            show yoshi talk1 at p5_2
            yo "We’ll try our best to meet your expectations."

            show emilia evil3 at p5_3
            voice audio.emilia_v_see2b
            e "See? Yoshinori understands!"
        "Whatever's best for the camp.":
            $working = True
            $score_goro += 2
            hide yoshi2_autumn
            hide yoshi2 upset1
            show yoshi_autumn at p5_2
            show yoshi talk1 at p5_2
            yo "We’ll do whatever’s best for the camp."

            show emilia evil3 at p5_3
            voice audio.emilia_v_see2b
            e "See? Yoshinori understands!"

    show emilia think5 at p5_3
    voice audio.emilia_v_oh1a
    e "Oh! And one more thing."
    e "All the cabins seem to be fully occupied, and it would be inappropriate for me to share a room with the workers."

    show emilia explain3 at p5_3
    voice audio.emilia_v_think1
    e "I’ll be needing a room of my own to stay in."

    show yuri annoy4 at p5_5
    voice audio.yuri_v_well1a
    yu "Well, too bad. We don’t have any—"

    show goro explain1 at p5_4
    voice audio.goro_v_emilia11a
    g "You can stay in my quarters here in the office, Ms. Komarova. "
    g "It’s clean and well-maintained, as well as the biggest room in the camp. It should meet all of your requirements."

    show goro talk2 at p5_4
    voice audio.goro_v_think1a1
    g "I’ll just move into the staff quarters. There should be an extra bed there, anyway."

    show emilia bold3 at p5_3
    voice audio.emilia_v_amazed1b
    e "That’s perfect! I’ll take it."

    show goro talk1 at p5_4
    voice audio.goro_v_aiden4a
    g "Aiden, why don’t you move Ms. Komarova’s stuff? Yuri, you can help me pack my things as well."

    hide aiden2_autumn
    hide aiden2 worry1
    show aiden_autumn at p5_1
    show aiden worry2 at p5_1
    voice audio.aiden_v_yessir1b1
    a "Yes, sir."

    show yuri pout4 at p5_5
    show emilia evil2 at p5_3
    voice audio.yyuri_v_hmph1a
    yu "Hmph. Fine."

    hide yuri_autumn
    hide yuri pout4
    hide goro_autumn
    hide goro talk1
    hide aiden_autumn
    hide aiden worry2
    with dissolve

    show yoshi_autumn at left2
    show yoshi talk1 at left2
    show emilia_autumn2 at right2
    show emilia evil2 at right2
    with move

    hide yoshi_autumn
    hide yoshi talk1
    show yoshi2_autumn at left2
    show yoshi2 worry2 at left2
    voice audio.yoshi_v_but2
    yo "I’m sorry for asking but… did you really think everything was that bad so far?"

    show emilia explain2 at right2
    voice audio.emilia_v_well1
    e "Well, it’s my job to point out concerns, and I only commented on what I found on my inspection."

    $persistent.profile_unlock.append("emilia")
    if score_aiden > score_goro:
        jump day0_aiden
    elif score_goro > score_aiden:
        jump day0_goro
    else:
        $ route = renpy.random.randint(1,2)
        if route == 1:
            jump day0_aiden
        else:
            jump day0_goro
