label day0_aiden:
    show emilia explain2 at right2
    e "If you want me to be even more honest, I think the staff concerns are what troubles me the most."

    show emilia confused3 at right2
    voice audio.emilia_v_bossy4
    e "As you may have noticed from our meeting earlier, your fellow scoutmasters aren’t as ‘mature’ when it comes to their shortcomings in managing their departments."

    show yoshi2 confused2 at left2
    voice audio.yoshi_v_huh3a
    yo "Are you talking about Aiden?"

    show emilia eyeroll6 at right2
    voice audio.emilia_v_scoff1
    e "Who else would I be talking about?"
    e "It’s not normal for the leadership to engage in behavior like he does. And frankly, it makes the whole camp look bad."

    show yoshi2 think2 at left2
    voice audio.yoshi_v_think1a
    yo "I… don’t think Aiden’s personal habits ever caused us trouble before. Are you sure you’re just not looking too much into it?"

    show emilia disgust3 at right2
    voice audio.emilia_v_question2b
    e "Do you really want to wait until it becomes a problem? It’s better to deal with it now."
    e "Even putting aside his habits, he has no management skills whatsoever."

    show emilia angry2 at right2
    voice audio.emilia_v_hmph1a
    e "It makes no sense why he has the same position as you given that he doesn’t meet the qualifications."
    e "That will hinder this project in many ways we do not want to see."

    show yoshi2 worry1 at left2
    yo "..."

    show emilia eyeroll4 at right2
    voice audio.emilia_v_ugh1
    e "Eugh. Don’t give me that look, Yoshinori. It’s just business."

    show emilia sigh2 at right2
    voice audio.emilia_v_sigh1a
    e "Look, I know criticism isn’t easy to take in, but someone has to point these things out."
    e "You know me- I prefer to be straightforward, especially when it comes to work."

    show yoshi2 sad5 at left2
    voice audio.yoshi_v_response1c
    yo "I… understand."

    show emilia annoy2 at right2
    voice audio.emilia_v_worry5
    e "That doesn’t sound too enthusiastic. Did my comment about your role upset you?"

    show emilia tired2 at right2
    voice audio.emilia_v_ugh1
    e "You must be so tired of having no consistent responsibility for this project…"
    e "But don’t worry, I’m here to help!~ "

    show emilia bold2 at right2
    voice audio.emilia_v_so2a
    e "Starting tomorrow, you and I will be in charge of both managing the construction as well as handling all staff concerns."

    show yoshi2 confused3 at left2
    voice audio.yoshi_v_what2
    yo "Are you saying we’ll take over both Aiden and Yuri’s tasks?"

    show emilia confused5 at right2
    voice audio.emilia_v_comp1a
    e "They’ll still be working in these departments, but you will be the one responsible for ensuring satisfactory results."

    show yoshi2 awkward1 at left2
    yo "..."

    show emilia talk3 at right2
    voice audio.emilia_v_conj2a
    e "Anyway, I’ll make sure that you know exactly what to do in both of these fields from now on."
    e "Since I’ll be staying here for the QA work, I thought I’d go out of my way to make sure you get a clearer perspective!"

    show emilia bold5 at right2
    voice audio.emilia_v_laugh1a
    e "There’s nobody better suited for the task, since it’s my job to oversee the entire project! We can take charge and lead together."

    show yoshi2 think1 at left2
    yo "..."

    show emilia play2 at right2
    voice audio.emilia_v_so3
    e "So? What do you say? Partners?"

    show yoshi2 explain2 at left2
    voice audio.yoshi_v_unsure1b
    yo "I… I’m not sure about this, Emilia… "

    show emilia irked2 at right2
    voice audio.emilia_v_annoyed1
    e "Why, that’s not the right answer!"
    e "You should be grateful; I’m offering to fix the exact issue you just mentioned."

    show emilia irked5 at right2
    voice audio.emilia_v_sarcastic4
    e "It baffles me why you’re having second thoughts about this. Help is literally being served to you on a silver—no, gold platter!"

    show yoshi2 worry2 at left2
    voice audio.yoshi_v_no4
    yo "I-It’s not that I don’t appreciate your offer, but I was trying to make a plan to resolve it myself…"

    show emilia disgust3 at right2
    voice audio.emilia_v_sarcastic1
    e "And that plan is…?"

    show yoshi2 sigh1 at left2
    voice audio.yoshi_v_well1
    yo "W-Well… I haven’t completely figured it out yet."
    yo "Can you at least give me a little time to think about what you’re proposing? It’s all very sudden, after all…"

    show emilia eyeroll6 at right2
    voice audio.emilia_v_response1a
    e "Fine. I’ll give you until tomorrow morning to decide."
    e "Let me emphasize this one last time though, since you seem to not be getting it."

    show emilia explain3 at right2
    voice audio.emilia_v_rush1c
    e "I’m a professional with exactly the experience you need, and I’m going out of my way to help you. The right choice is obvious."
    e "You need some guidance, and we can catch up! I don’t see any loss here."

    hide yoshi2_autumn
    hide yoshi2 sigh1
    show yoshi_autumn at left2
    show yoshi talk1 at left2
    voice audio.yoshi_v_alright3
    yo "I’ll keep that in mind, Emilia…"

    show emilia evil2 at right2
    voice audio.emilia_v_amazed1a
    e "Excellent~! I expect nothing but great things from you, Yoshinori! It’s a pleasure to work with you again!"

    show emilia bold2 at right2
    voice audio.emilia_v_comp2a
    e "Everything will be alright now that I’m here!"
    e "Now, all this serious business has made me tired, not to mention all the walking around the camp to inspect!"

    show emilia bold6 at right2
    voice audio.emilia_v_bye2a
    e "I’ll take my leave for now and rest up! I still have to send an email report to Mr. Clermont, after all!"

    hide yoshi_autumn
    hide yoshi talk1
    show yoshi2_autumn at left2
    show yoshi2 talk3 at left2
    voice audio.yoshi_v_right4
    yo "R-Right. Goodnight, Emilia."

    show emilia happy4 at right2
    voice audio.emilia_v_bye1a
    e "Toodles~ "

    hide emilia_autumn2
    hide emilia happy4
    with dissolve

    $ renpy.pause (2.0, hard=True)
    show yoshi2 think1 at left2
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
    $ time_transition_sunset_to_night_fall()

    $ location = location_cabin
    $ time = timeline_timenight
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_quarters_autumn_night with fade
    play music ready_for_tomorrow loop
    play bgsound sfxloop_night loop

    play sound sfx_bagdrop
    show lloyd_autumn at p6_1
    show lloyd norm4 at p6_1
    show darius_autumn at p6_2
    show darius norm3 at p6_2
    show jin_autumn at p6_3
    show jin norm3 at p6_3
    show jin_glasses at p6_3
    show goro_autumn at p6_4
    show goro norm3 at p6_4
    show aiden_autumn at p6_5
    show aiden talk1 at p6_5
    show yoshi_autumn at p6_6
    show yoshi worry1 at p6_6
    a "Alright, Gramps! That should be all your stuff! "

    show goro talk1 at p6_4
    voice audio.goro_v_thanks1a1
    g "Thanks for helping me move in."

    show aiden comp3 at p6_5
    voice audio.aiden_v_alright3d
    a "Don’t mention it!"

    show jin worry2 at p6_3
    voice audio.jin_v_goro3b
    j "I hope it won’t be a hassle for you to stay here with us, Sir Goro…"

    show goro explain2 at p6_4
    voice audio.goro_v_response2a2
    g "It’s no problem. I don’t mind having some extra company."

    show aiden tease1 at p6_5
    voice audio.aiden_v_goro10a
    a "Haha, looks like you got demoted, huh Gramps?"

    show lloyd talk1 at p6_1
    voice audio.lloyd_v_aiden2c
    l "Careful what you say, Aiden. Sir Goro’s still in charge! You could get fired with one snap!"

    show aiden explain2 at p6_5
    voice audio.aiden_v_agree5b
    a "I know, I know, I’m just kidding around. Everyone hasn’t cracked a smile since that meeting."

    show jin sigh3 at p6_3
    voice audio.jin_v_emilia2c
    j "Looks like Ms. Emilia really said some upsetting things back there, huh?"

    hide goro_autumn
    hide goro explain2
    show goro2_autumn at p6_4
    show goro2 disappoint3 at p6_4
    voice audio.goro_v_think1a1
    g "The criticisms were rather trifling, but we don’t have much of a choice except to try and make do since Mr. Clermont placed her here."

    show aiden worry2 at p6_5
    voice audio.aiden_v_yeah1c3
    a "Yeah… And Yuri didn’t take it so well… I’ve never seen her lose her temper like that!"

    show lloyd happy1 at p6_1
    voice audio.lloyd_v_stars1a2
    l "On the upside, I think we’re all destined to connect better thanks to the divination I did earlier while you guys were in that meeting!"
    l "I interpreted my reading as “New Beginnings,” and that’s already true from the changes happening so far!"

    show jin confused2 at p6_3
    voice audio.jin_v_think2a1
    j "I still have no clue what you’re trying to say…"

    show darius happy1 at p6_2
    voice audio.darius_v_conj2a
    d "He means it’s good luck."

    show aiden happy1 at p6_5
    voice audio.aiden_v_yeah1a1
    a "Whatever mumbo jumbo Lloyd is saying, I agree! "
    a "Let’s look on the bright side, especially since we’ll be way busier starting tomorrow!"

    hide goro2_autumn
    hide goro2 disappoint3
    show goro_autumn at p6_4
    show goro talk1 at p6_4
    voice audio.goro_v_agree6a1
    g "That’s a very good mindset to have, Aiden."

    show lloyd tired1 at p6_1
    voice audio.lloyd_v_agree2a3
    l "Yeah, I bet the only time we’ll have to casually chat with each other will be at night after work, like this!"

    show goro talk3 at p6_4
    voice audio.goro_v_conj7a
    g "With that being said, we should all try and get up earlier than usual "
    g "Let’s not give our new inspector any reason to think we’re not taking this sponsorship seriously."

    show aiden tease1 at p6_5
    voice audio.aiden_v_oops1a
    a "Uh-oh, it’s bedtime already and Gramps is getting cranky~. "

    show goro sigh1 at p6_4
    voice audio.goro_v_sigh1a
    g "*sigh* Aiden…"

    show lloyd talk2 at p6_1
    voice audio.lloyd_v_sir1d
    l "You can take my bunk, sir! I’m sharing a bed with Dar!"

    show goro confused2 at p6_4
    voice audio.goro_v_unsure1a1
    g "Are you sure that’s alright with you two?"

    show darius tease2 at p6_2
    voice audio.darius_v_response1
    d "It’s fine. He won’t take up much space."

    show lloyd angry2 at p6_1
    voice audio.lloyd_v_greet2c1
    l "Hey! Not you too, Dar!"

    show jin talk2 at p6_3
    voice audio.jin_v_rush2a1
    j "You guys go ahead. I’m gonna take a shower since I’m just about to start my day."

    show goro talk2 at p6_4
    voice audio.goro_v_goodpm3a1
    g "Alright. Good night, then."

    show darius relief2 at p6_2
    voice audio.darius_v_goodpm1
    d "Night."

    hide darius_autumn
    hide lloyd_autumn
    hide jin_autumn
    hide jin talk2
    hide jin_glasses
    hide darius tease2
    hide lloyd angry2
    hide goro_autumn
    hide goro talk2
    with dissolve

    show aiden_autumn at left2
    show aiden tease1 at left2
    show yoshi_autumn at right2
    show yoshi worry1 at right2
    with move

    hide aiden_autumn
    hide aiden tease1
    show aiden2_autumn at left2
    show aiden2 confused6 at left2
    voice audio.aiden_v_so1
    a "So, you wanna tell me why you’re spacing out again, Yoshi?"
    a "Don’t tell me Emilia got under your skin too?!"

    hide yoshi_autumn
    hide yoshi worry1
    show yoshi2_autumn at right2
    show yoshi2 sigh1 at right2
    voice audio.yoshi_v_no4
    yo "Not exactly, but she did give me something to think about earlier."

    show aiden2 worry2 at left2
    voice audio.aiden_v_worry1b
    a "She didn’t have a problem with you, did she?"

    hide yoshi2_autumn
    hide yoshi2 sigh1
    show yoshi_autumn at right2
    show yoshi talk1 at right2
    voice audio.yoshi_v_actually1b
    yo "Quite the opposite, actually…"
    yo "She told me that she wanted to work with me to help clear up my role on this project."

    show yoshi explain2 at right2
    voice audio.yoshi_v_think1a
    yo "You know… the same thing I’ve been thinking about for the past week…"

    show aiden2 worry5 at left2
    voice audio.aiden_v_well1c1
    a "Did you… accept her offer?"

    hide yoshi_autumn
    hide yoshi explain2
    show yoshi2_autumn at right2
    show yoshi2 shy4 at right2
    voice audio.yoshi_v_no3
    yo "I didn’t give her an answer just yet…"

    hide aiden2_autumn
    hide aiden2 worry5
    show aiden_autumn at left2
    show aiden sigh5 at left2
    voice audio.aiden_v_sigh1a
    a "If I’m being honest, you’re probably the only one who can get along with her when it comes to work…"

    show yoshi2 sigh4 at right2
    voice audio.yoshi_v_yeah1
    yo "I know… And I think she genuinely wants to help me out too, but that evaluation a while ago really seemed unnecessarily harsh."

    hide aiden_autumn
    hide aiden sigh5
    show aiden2_autumn at left2
    show aiden2 sad4 at left2
    voice audio.aiden_v_yeah1c2
    a "Yeah, tell me about it. She really put me in the spotlight back there and called me out in front of you guys."
    a "If that meeting had lasted any longer, I bet she’d really have started digging into me."

    show aiden2 upset6 at left2
    voice audio.aiden_v_unsure2a
    a "With an inspector keeping an eye on us all the time, I’m worried I might just cause trouble for everyone…"

    hide yoshi2_autumn
    hide yoshi2 sigh4
    show yoshi_autumn at right2
    show yoshi talk1 at right2
    voice audio.yoshi_v_actually1a
    yo "That’s what got me thinking, Aiden. It seems like she was making a huge deal out of your department and using that as a way to take over. "
    yo "She’s also expecting me to work with her at the same time…"

    hide aiden2_autumn
    hide aiden2 upset6
    show aiden_autumn at left2
    show aiden upset3 at left2
    voice audio.aiden_v_yoshi8b
    a "Well, this is Emilia we’re talking about, Yoshi. Everyone knows how she was in the past."
    a "That, and I think she just doesn’t like me for some reason. It’s just so different from how she acts around you."

    show yoshi worry3 at right2
    voice audio.yoshi_v_right9
    yo "You’re right. I did notice that."

    show yoshi comp2 at right2
    voice audio.yoshi_v_aiden2
    yo "And that’s where I come in, Aiden."
    yo "I figured that if we focused on the same departments, then we can guarantee that Emilia won’t have anything to call us out for!"

    show aiden excited3 at left2
    voice audio.aiden_v_oh1b
    a "Oh, we’re gonna work together? Now I can’t say no to that! "
    a "Not gonna lie, I was about to ask you for help after that nightmare feedback I got, so I’m really glad you ended up asking me!"

    show yoshi bold2 at right2
    voice audio.yoshi_v_well1
    yo "Well, I’m really looking forward to it! I finally made up my mind about what my role in this project really is!"

    show aiden confused2 at left2
    voice audio.aiden_v_unsure7a
    a "What about Emilia though? She’s gonna be bummed if she finds out you’re turning her offer down."

    show yoshi comp2 at right2
    voice audio.yoshi_v_comp4
    yo "I’m sure I can find a way to tell her as professionally as possible. What’s more important to me right now is taking the opportunity to help you."

    show aiden comp2 at left2
    voice audio.aiden_v_aww2b
    a "Aww, Yoshi~"

    show yoshi play2 at right2
    voice audio.yoshi_v_laugh6
    yo "You might have to start putting on more clothes, though. We can’t have her inspecting your butt too."

    show aiden tease1 at left2
    voice audio.aiden_v_laugh2a1
    a "Hahaha! Yeah, ‘cause that’s your job, right?"

    show yoshi laugh1 at right2
    voice audio.yoshi_v_right5
    yo "Haha! That’s right!"

    show aiden talk3 at left2
    voice audio.aiden_v_anyway2a
    a "But in all seriousness, I’ll try to act more pro too. I’d really hate it if I dragged everyone down just because of my habits…"

    show yoshi comp3 at right2
    voice audio.yoshi_v_comp7
    yo "Take it easy, Aiden. I’d really rather you be yourself."
    yo "And like I said, I’ll be staying by your side throughout this whole thing!"

    show aiden comp3 at left2
    voice audio.aiden_v_oho1a
    a "Oh, look at you~ You’re acting all positive again, just like when you were a scout!"

    hide yoshi_autumn
    hide yoshi comp3
    show yoshi2_autumn at right2
    show yoshi2 comp6 at right2
    voice audio.yoshi_v_laugh6
    yo "Ahehe… You’re the one bringing it out for me."

    show aiden relief4 at left2
    voice audio.aiden_v_thanks1a1
    a "But really, thanks a lot, Yoshi. I feel better already."

    hide yoshi2_autumn
    hide yoshi2 comp6
    show yoshi_autumn at right2
    show yoshi happy1 at right2
    voice audio.yoshi_v_agree1b2
    yo "Of course! Now come on, let’s get to sleep – we have a busy day tomorrow!"

    show aiden comp2 at left2
    voice audio.aiden_v_agree3a1
    a "Sure thing! Goodnight, Yoshi!"

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
    $ time_transition_night_to_day_fall()
    $ renpy.pause (2.0, hard=True)
    $aiden_route = True

    jump day1_aiden
