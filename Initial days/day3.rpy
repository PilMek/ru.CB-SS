label day3:
    $ day = "03"
    $ time = timeline_timeday
    $ location = location_cabin
    $ working = True
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_quarters_autumn_day with fade
    play music buddy_oath_casual loop
    play bgsound sfx_construction loop

    show yoshi2_sleep at center
    show yoshi2 sleepy4 at center
    voice audio.yoshi_v_groan1b
    yo "Hnn…"

    play sound sfx_truckbeep
    show yoshi2 sleepy2 at center
    yo "..."

    play sound sfx_bang
    show yoshi2 awkward4 at center
    voice audio.yoshi_v_worry3a
    yo "Wh-Wha…? What’s going on out there?" with vpunch

    show yoshi2_sleep at right
    show yoshi2 shock2 at right
    with move

    voice audio.yoshi_v_what2
    yo "Wh-What?! Don’t tell me the construction crew is here already?! I thought they were supposed to arrive a little later today?!"

    hide yoshi2_sleep
    hide yoshi2 shock2
    show yoshi2_sleep at right
    show yoshi2 shy4 at right
    yo "If I had known, I would’ve woken up sooner! "

    hide yoshi2_sleep
    hide yoshi2 shy4
    show yoshi_sleep at right
    show yoshi awkward3 at right
    voice audio.yoshi_v_ah4
    yo "I have to get ready quick!"

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black
    play sound sfx_clotheschanging
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
    play music brand_new_day loop
    play bgsound sfxloop_crowd loop

    show yuri_autumn at left
    show yuri norm1 at left
    show aiden_autumn at center
    show aiden happy2 at center
    show yoshi_autumn at right
    show yoshi norm4 at right
    voice audio.aiden_v_oh1a
    a "Oh, you’re awake, Yoshi!"

    show yuri tease2 at left
    voice audio.yuri_v_laugh1a1
    yu "Hihi~ You’re not the first one up for once!"

    show yoshi worry2 at right
    voice audio.yoshi_v_why1
    yo "Why didn’t you guys wake me up? I didn’t know the workers were coming this early."

    show yuri talk2 at left
    voice audio.yuri_v_oh1a
    yu "Oh, they aren’t the workers, Yoshi! They’re just here to deliver the building materials!"
    yu "They were supposed to show up at the same time as the workers later, but they got here earlier than scheduled. "

    show aiden comp5 at center
    voice audio.aiden_v_yeah1a1
    a "Yeah, good thing I was up extra early when they arrived or else nobody would’ve been around to let them in! "

    show yoshi sigh1 at right
    voice audio.yoshi_v_relief4
    yo "Oh, that’s a relief… For a minute there, I thought I’d be late on our first day of renovations."

    show yuri laugh1 at left
    voice audio.yuri_v_yeah1a1
    yu "If it weren’t for the ruckus outside, I wouldn’t have woken up either."

    show yoshi talk1 at right
    voice audio.yoshi_v_think1b
    yo "It looks like we need to be more prepared for the unexpected from here on. "

    show yuri talk2 at left
    voice audio.yuri_v_anyway1b
    yu "Speaking of which, Mr. Clermont gave us the specifics of today’s agenda this morning. Dad told me to relay the info to you guys!"

    hide aiden_autumn
    hide aiden comp5
    show aiden2_autumn at center
    show aiden2 confused5 at center
    voice audio.aiden_v_goro5a
    a "Where’s Gramps anyways? Shouldn’t he be the one briefing us on all of this?"

    show yuri confused2 at left
    voice audio.yuri_v_think1a1
    yu "Dad left super early a while ago… He said he’s gonna run some errands… He didn’t tell me what they were though…"

    show yoshi think2 at right
    voice audio.yoshi_v_conj3b
    yo "Based on yesterday’s meeting, I believe he’s out today handling the permits at city hall. "
    yo "Either way, we should be able to take care of everything ourselves! "

    show yuri happy1 at left
    voice audio.yuri_v_agree1b1
    yu "Yes! There are only two things Dad assigned for today – matching the deliveries with the materials list and prepare for the workers’ arrival."

    show yoshi talk1 at right
    voice audio.yoshi_v_confident3
    yo "Let me handle the deliveries, Yuri. You can go and prepare the cabins the workers are staying at. "

    show yuri excited2 at left
    voice audio.yuri_v_oh1a
    yu "Oh, I already took care of those! I was up past midnight dusting off the floors and putting sheets on the beds."
    yu "Besides, I think I’ll enjoy managing the deliveries. All I need to do is to watch over these… uhh… muscular… sweaty…  and maybe half-naked delivery boys… Hihihi~"

    hide yoshi_autumn
    hide yoshi think2
    show yoshi2_autumn at right
    show yoshi2 awkward3 at right
    voice audio.yoshi_v_yuri6
    yo "Y-Yuri… You’re getting distracted already… Try to make sure you fully check and count all the materials properly."

    hide aiden2_autumn
    hide aiden2 confused5
    show aiden_autumn at center
    show aiden tease1 at center
    voice audio.aiden_v_laugh1c1
    a "Heh, knowing Yuri, she’ll do a full check alright~ "

    show yuri relief2 at left
    voice audio.yuri_v_fujo1b1
    yu "Ahh… To be blessed with such a show all for myself~ I love this job so much!"

    show yoshi2 angry5 at right
    voice audio.yoshi_v_ehem1a
    yo "*ehem* Anyway, did we get an update on the number of workers moving in later today?"

    show yuri talk2 at left
    voice audio.yuri_v_agree1a3
    yu "Ah, yes, we’re expecting the first batch to be approximately thirty people."

    hide aiden_autumn
    hide aiden tease1
    show aiden2_autumn at center
    show aiden2 panic4 at center
    voice audio.aiden_v_shock2a1
    a "Yikes! You mean I have to feed that many too?! I only prepared for half of that last night…!"

    $working = False
    $shuffle_menu()
    menu():
        a "Yikes! You mean I have to feed that many too?! I only prepared for half of that last night…!{fast}"
        "Can you finish in time?":
            $working = True
            $score_aiden -= 1
            show yoshi2 worry2 at right
            voice audio.yoshi_v_worry2
            yo "Will you be able to have everything prepped in time, Aiden? It seems like a lot to do…"

            show aiden2 sigh4 at center
            voice audio.aiden_v_yeah1a1
            a "Yeah, I could seriously use a hand. "
            a "If you’re not too busy, maybe you can help me out, Yoshi?"

            show yoshi2 worry5 at right
            voice audio.yoshi_v_unsure2a
            yo "Are you sure? I’m not much use in the kitchen… "

            hide aiden2_autumn
            hide aiden2 sigh4
            show aiden_autumn at center
            show aiden talk4 at center
            voice audio.aiden_v_no1a1
            a "No way, you could help me cut up the ingredients at least!"

            hide yoshi2_autumn
            hide yoshi2 worry5
            show yoshi_autumn at right
            show yoshi happy1 at right
            voice audio.yoshi_v_alright2
            yo "Alright, if it’ll help!"

            show aiden laugh2 at center
            voice audio.aiden_v_praise1a
            a "Great! Let’s go then!"
        "I don't have any plans.":
            $working = True
            show yoshi2 think5 at right
            voice audio.yoshi_v_worry2
            yo "I don’t have any plans until the workers arrive, and since Yuri’s got the deliveries covered…"

            hide aiden2_autumn
            hide aiden2 laugh2
            show aiden_autumn at center
            show aiden amazed2 at center
            voice audio.aiden_v_oh1a
            a "Oh! How about you come with me then?"

            hide yoshi2_autumn
            hide yoshi2 think5
            show yoshi_autumn at right
            show yoshi happy1 at right
            voice audio.yoshi_v_sure2
            yo "Sure, I don’t mind!"

            show aiden laugh2 at center
            voice audio.aiden_v_praise1a
            a "Great! Let’s go then!"
        "Why don't I give you a hand?":
            $working = True
            $score_aiden += 1
            hide yoshi2_autumn
            hide yoshi2 angry5
            show yoshi_autumn at right
            show yoshi happy1 at right
            voice audio.yoshi_v_worry2
            yo "Why don’t I give you a hand, Aiden? I’m sure it’ll make your job easier!"

            hide aiden2_autumn
            hide aiden2 panic4
            show aiden_autumn at center
            show aiden amazed2 at center
            voice audio.aiden_v_thanks1a1
            a "You’re a lifesaver, Yoshi! I’m not sure I could do it all by myself in time!"

            show yoshi laugh1 at right
            voice audio.yoshi_v_laugh1
            yo "Haha, I’ve seen you pull off even tighter deadlines. But I’m happy to make it easier on you today!"

            show aiden laugh2 at center
            voice audio.aiden_v_comeon1a1
            a "Thanks, Yoshi! Come on, let’s go!"
        "I'll help you cook.":
            $working = True
            $score_aiden += 2
            hide yoshi2_autumn
            hide yoshi2 angry5
            show yoshi_autumn at right
            show yoshi bold2 at right
            voice audio.yoshi_v_worry2
            yo "Let me help you cook, Aiden! You sound like you could use an assistant chef!"
            yo "I can help you prep and cut up the ingredients to save you some time!"

            hide aiden2_autumn
            hide aiden2 panic4
            show aiden_autumn at center
            show aiden amazed2 at center
            voice audio.aiden_v_thanks1a1
            a "That sounds great, Yoshi! I’d love to have you in the kitchen with me!"

            show yoshi happy1 at right
            voice audio.yoshi_v_rush5
            yo "Let’s go then!"

    hide yoshi_autumn
    hide yoshi happy1
    hide yoshi laugh1
    hide aiden_autumn
    hide aiden laugh2
    hide aiden amazed2
    with dissolve

    show yuri_autumn at center
    show yuri excited2 at center
    with move

    voice audio.yuri_v_laugh2a1
    yu "Hehe… Now, where did I put my camera~?"
label debug:
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
    scene bg_kitchen_autumn_day with fade
    play music go_with_the_flow loop

    show aiden_apron2 at left2
    show aiden talk3 at left2
    show yoshi_autumn at right2
    show yoshi norm1 at right2
    voice audio.aiden_v_really1b
    a "Hey, you sure you’re gonna work with all those clothes on? "

    show yoshi comp3 at right2
    voice audio.yoshi_v_comp2
    yo "A-Ah… I’m fine, Aiden! Won’t you get cold like that though?"

    show aiden explain3 at left2
    voice audio.aiden_v_no2a1
    a "Nah! It’s gonna be really hot in here later once we start cooking everything up!"

    show yoshi bold2 at right2
    voice audio.yoshi_v_so2
    yo "S-So, what are we making today, and how can I help?"

    hide aiden_apron2
    hide aiden explain3
    show aiden2_apron2 at left2
    show aiden2 think4 at left2
    voice audio.aiden_v_think1b
    a "Hmmmm… Since I’m cooking for a bunch of active dudes, I’m expecting them to have huge appetites!"

    hide aiden2_apron2
    hide aiden2 think4
    show aiden_apron2 at left2
    show aiden bold2 at left2
    voice audio.aiden_v_excited2b
    a "A nice, hearty meal packed with protein and nutrients should keep their energy up after a long day!"
    a "Luckily for me, that’s usually the same category of food the scouts love, so I have a menu that I prepped before that we can use!"

    show yoshi shock2 at right2
    voice audio.yoshi_v_amazed1d
    yo "Oh wow… This seems like a lot to do… and you have to make thirty servings of this?!"

    show aiden laugh1 at left2
    voice audio.aiden_v_yeah1a2
    a "Haha, yeah! Welcome to my world! That’s why my little chef, Hiro, was such a big help back during the summer!"

    show aiden excited1 at left2
    voice audio.aiden_v_actually1a
    a "To be honest, though, I’m really excited! It’s been a while since I cooked for a lot of people, haha! "
    a "And with your help, this’ll be a breeze! You’ll be my sous chef! "

    show yoshi comp5 at right2
    voice audio.yoshi_v_unsure1b
    yo "It really has been a while since I’ve helped out in the kitchen. I hope we can finish in time."

    show aiden laugh2 at left2
    voice audio.aiden_v_laugh2a1
    a "Haha, yeah, it’s like a pressure cooker in here, ’specially when the people start coming inside the mess hall!"
    a "Speaking of which, put on an apron and let's start prepping these ingredients already!"

    show yoshi happy1 at right2
    voice audio.yoshi_v_right3
    yo "Right!"

    hide yoshi_autumn
    hide yoshi happy1
    show yoshi_autumn3 at right2
    show yoshi happy1 at right2
    with dissolve

    scene cga2 1 with fade
    play bgsound sfxloop_chopping loop
    voice audio.aiden_vsa3_line1
    a "Hehe, it feels so nostalgic to have you in the kitchen again, Yoshi."

    voice audio.aiden_vsa3_line2
    a "Ever since you became a full-fledged scoutmaster, you hardly get to help me cook! "

    voice audio.yoshi_vsa3_line1
    yo "A-Ah…"

    show cga2 2 with Dissolve(0.25)
    voice audio.aiden_vsa3_line3
    a "I don’t blame you though. You have way more important duties now anyways."

    voice audio.yoshi_vsa3_line2
    yo "W-Well, I do try to help you out sometimes when my schedule is loose."

    voice audio.aiden_vsa3_line4
    a "Yeah, like once or twice every term! "

    voice audio.yoshi_vsa3_line3
    yo "I’m not sure if I’m even helping though… I’m not as good of a cook as you are. "

    show cga2 3 with Dissolve(0.25)
    voice audio.aiden_vsa3_line5
    a "It’s not about the skill, it’s about the company! Food made with TLC is the best kind! "

    voice audio.yoshi_vsa3_line4
    yo "That stands for tomatoes, lettuce, and cheese, right…? I didn’t know we were making burgers today."

    show cga2 4 with Dissolve(0.25)
    voice audio.aiden_vsa3_line6
    a "I meant tender loving care, silly! Sheesh…"

    voice audio.aiden_vsa3_line7
    a "Having someone to cook with or cook for is what makes a dish a lot more special."

    voice audio.yoshi_vsa3_line5
    yo "I guess you do have a point… I mean, I know I have more fun with my job here at the camp, especially when the scouts are around. "

    show cga2 5 with Dissolve(0.25)
    voice audio.aiden_vsa3_line8
    a "Yeah, you always get hyped up about any activities you get to do with them."

    voice audio.aiden_vsa3_line9
    a "Just like when you did them as a scout! You wanted to try everything and be good at all of it!"

    voice audio.aiden_vsa3_line10
    a "That kinda reminds me of when you were interested in cooking a long time ago – we used to spend so much time in the kitchen together!"

    voice audio.yoshi_vsa3_line6
    yo "Ahh, yeah… I remember!  That was when you were helping me earn my cooking badge."

    show cga2 6 with Dissolve(0.25)
    voice audio.aiden_vsa3_line11
    a "Ugh… That stupid cooking badge. As soon as you got it, you stopped trying to get better at cooking."

    $working = False
    $shuffle_menu()
    menu():
        a "Ugh… That stupid cooking badge. As soon as you got it, you stopped trying to get better at cooking.{fast}"
        "You were always so much better at it.":
            $working = True
            $score_aiden -= 2
            show cga2 7a with Dissolve(0.25)
            voice audio.yoshi_vsa3_line7a
            yo "Well, you were always so much better at it than I was. "

            voice audio.yoshi_vsa3_line8ab
            yo "You saw the stuff I cooked back then, and it was barely edible. That’s why I felt like cooking wasn’t for me to begin with."

            show cga2 8ab with Dissolve(0.25)
            voice audio.aiden_vsa3_line12ab
            a "It’s a good thing you got the hang of it in the end though! "
        "Cooking isn't my strongest suit.":
            $working = True
            $score_aiden -= 1
            show cga2 7b with Dissolve(0.25)
            voice audio.yoshi_vsa3_line7b
            yo "W-Well, it’s not that I wasn’t interested anymore. I just thought it wasn’t my strongest suit."

            voice audio.yoshi_vsa3_line8ab
            yo "You saw the stuff I cooked back then, and it was barely edible. That’s why I felt like cooking wasn’t for me to begin with."

            show cga2 8ab with Dissolve(0.25)
            voice audio.aiden_vsa3_line12ab
            a "It’s a good thing you got the hang of it in the end though! "
        "I prefer your cooking.":
            $working = True
            $score_aiden += 1
            show cga2 7cd with Dissolve(0.25)
            voice audio.yoshi_vsa3_line7c
            yo "I’d much rather have your cooking than mine!"

            voice audio.yoshi_vsa3_line8c
            yo "You’ve always been so good at it, so I never needed to get any better."

            show cga2 8c with Dissolve(0.25)
            voice audio.aiden_vsa3_line12c
            a "Hehe, I guess if you put it that way."

            voice audio.aiden_vsa3_line13cd
            a "After all, I’ve seen and tasted the stuff you made, and I have to say – I never thought I’d see meat and chocolate in a dish together…"

            show cga2 9cd with Dissolve(0.25)
            voice audio.yoshi_vsa3_line9cd
            yo "G-Gah! I swear I didn’t mean to do that! "

            show cga2 10cd with Dissolve(0.25)
            voice audio.aiden_vsa3_line14cd
            a "Hahaha! That’s the same look you had every time you messed up, even after I taught you!"
        "You're always there to cook for me.":
            $working = True
            $score_aiden += 2
            show cga2 7cd with Dissolve(0.25)
            voice audio.yoshi_vsa3_line7d
            yo "Haha, why would I need to when I have you around to cook for me~?"

            voice audio.yoshi_vsa3_line8d
            yo "Your food is already the best, so there’s no way anyone could compete!"

            show cga2 8d with Dissolve(0.25)
            voice audio.aiden_vsa3_line12d
            a "Hmm, well, since you’re flirting, I guess I can give you a pass~ "

            show cga2 8c with Dissolve(0.25)
            voice audio.aiden_vsa3_line13cd
            a "After all, I’ve seen and tasted the stuff you made, and I have to say – I never thought I’d see meat and chocolate in a dish together…"

            show cga2 9cd with Dissolve(0.25)
            voice audio.yoshi_vsa3_line9cd
            yo "G-Gah! I swear I didn’t mean to do that! "

            show cga2 10cd with Dissolve(0.25)
            voice audio.aiden_vsa3_line14cd
            a "Hahaha! That’s the same look you had every time you messed up, even after I taught you!"

    show cga2 11 with Dissolve(0.25)
    voice audio.yoshi_vsa3_line10
    yo "Yeah, I did struggle earning that cooking badge… but I had a lot of fun with you because of it!"

    voice audio.aiden_vsa3_line15
    a "You know, I'm really thankful for that badge – if it wasn't for it, I probably wouldn't have met you."

    voice audio.aiden_vsa3_line16
    a "It was the reason I got to stay here at Camp Buddy in the first place!"

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

    $ location = location_messhall
    $ day = "??"
    $ time = timeline_timeday
    $ season = season_summer
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_messhall_autumn_day with fade
    play music go_with_the_flow_slow loop
    play bgsound sfxloop_birds loop

    show yaiden_casual at left2
    show yaiden norm3 at left2
    show andre_camp at right2
    show andre talk3 at right2
    voice audio.andre_v_agree2a2
    u "Okay, Aiden, I know I promised that I’d take care of you today, but we have an emergency staff meeting…"
    u "I’m not allowed to bring visitors as per the camp policy, but luckily Sir Goro made an exception and is letting you wait here due to our circumstances… "

    show andre talk2 at right2
    voice audio.andre_v_question1a
    u "I need you to stay put for a while until the meeting is over. I promise I won’t be gone for too long, so don’t go goofing around, okay?"

    show yaiden talk3 at left2
    voice audio.yaiden_v_okay3b
    a "Okay, Dad. I don’t mind waiting."

    show andre happy1 at right2
    voice audio.andre_v_agree1a3
    u "Great! I’ll be back soon, Aiden!"

    hide andre_camp
    hide andre happy1
    with dissolve

    show yaiden norm3 at left2
    a "..."

    show yaiden_casual at p5_1
    show yaiden norm3 at p5_1
    with move

    show yyoshi_camp at p5_4
    show yyoshi angry2 at p5_4
    show yyuri_camp at p5_5
    show yyuri annoy1 at p5_5
    with dissolve

    voice audio.yyoshi_v_yuri9a
    yo "Come on, Yuri! I really need that cooking badge! Come and taste the food I made! "

    show yyuri sigh1 at p5_5
    voice audio.yyuri_v_yoshi11a
    yu "Yoshi… You’ve already made me eat five horrible dishes today! How is this one any different?!"

    show yyoshi bold2 at p5_4
    voice audio.yyoshi_v_confident4
    yo "I’m sure I seasoned this one just right! You’ll see!"

    show yaiden_casual at left
    show yaiden norm3 at left
    show yyoshi_camp at center
    show yyoshi talk3 at center
    show yyuri_camp at right
    show yyuri sigh1 at right
    with move

    voice audio.yyoshi_v_oh2
    yo "Oh! "

    show yaiden awkward1 at left
    a "...!"

    show yyoshi happy2 at center
    voice audio.yyoshi_v_greet1a
    yo "Hello! You don’t look familiar, are you a new scout?"

    show yaiden awkward2 at left
    voice audio.yaiden_v_think3a
    a "I… Uhh… No—"

    show yyuri talk5 at right
    voice audio.yyuri_v_wait1a1
    yu "Wait, I know you! I saw you come by today with Mr. Andre! Are you his son?"

    show yaiden awkward3 at left
    voice audio.yaiden_v_yeah1c1
    a "Y-Yeah…"

    show yyoshi comp5 at center
    voice audio.yyoshi_v_well1
    yo "Well, a friend of Mr. Andre is a friend of ours! My name’s Yoshinori! "

    show yyuri happy1 at right
    voice audio.yyuri_v_intro1a
    yu "I’m Yuri! "

    show yyoshi happy2 at center
    voice audio.yyoshi_v_greet3a
    yo "Welcome to Camp Buddy! What’s your name? "

    show yaiden talk3 at left
    voice audio.yaiden_v_intro1
    a "Aiden… "

    show yyoshi laugh1 at center
    voice audio.yyoshi_v_greet5a
    yo "Nice to meet you, Aiden! What are you doing over here all alone?  "

    show yaiden explain3 at left
    voice audio.yaiden_v_oh1d
    a "Oh, I’m just waiting for Dad to finish his staff meeting… He asked me to stay put and wait here..."

    show yyoshi talk3 at center
    voice audio.yyoshi_v_isee1
    yo "Oh, I see… Well, they’re gonna take a while in there for sure! If you want, you can help me with my badge-earning activity!"
    yo "I’m trying to earn my cooking badge today, and I could use another person to try out the food I made!"

    show yyoshi bold2 at center
    voice audio.yyoshi_v_think2
    yo "Since your dad is the chef here, then that means you should know a thing or two about cooking, right?"

    show yaiden awkward2 at left
    voice audio.yaiden_v_unsure5a1
    a "I guess… I do know a little bit about it, yeah…"

    show yyuri laugh1 at right
    voice audio.yyuri_v_praise2a
    yu "What a good idea, Yoshi! That means you won’t need me to do the taste-testing after all!"

    show yyoshi angry3 at center
    voice audio.yyoshi_v_hey3
    yo "H-Hey! You’re not off the hook! Aiden hasn’t agreed yet!"

    show yyuri rage3 at right
    voice audio.yyuri_v_ugh2a
    yu "UGHhhh…"

    show yyoshi norm1 at center
    show yaiden worry2 at left
    voice audio.yaiden_v_think3a
    a "I don’t know… Dad told me to stay here and—"

    show yyuri comp6 at right
    voice audio.yyuri_v_no1b1
    yu "No, no! It’ll be fine! Those meetings take HOURS anyways! He won’t even know you’re gone! Just say yes already!!"

    show yaiden worry5 at left
    voice audio.yaiden_v_think1a
    a "A-Are you sure I’m not gonna get in trouble…?"

    show yyuri play2 at right
    voice audio.yyuri_v_hey1a
    yu "My dad’s the president of this camp! We can get away with everything!"

    show yaiden shock2 at left
    voice audio.yaiden_v_really1a
    a "Wow, really?"

    show yyuri angry6 at right
    voice audio.yyuri_v_agree1b1
    yu "Yes, really! So, please, PLEASE, save me from having another tummy ache today, Aiden!!"

    show yyoshi awkward4 at center
    voice audio.yyoshi_v_aiden2
    yo "D-Don’t listen to her, Aiden, I made a really yummy pizza back in the kitchen! If you come with me, I’ll let you have the whole thing!"

    play sound sfx_stomachgrowl
    show yaiden hungry3 at left
    voice audio.yaiden_v_amazed2b1
    a "Pizza?! *tummy grumbles*"

    show yyoshi excited1 at center
    voice audio.yyoshi_v_laugh1
    yo "Sounds like you could use some pizza! It’s gonna be ooey-gooey with cheese too once I heat it up!"

    show yaiden hungry2 at left
    voice audio.yaiden_v_oh1a
    a "Ahh… That sounds delicious!  I guess… a quick bite wouldn’t hurt."

    show yyuri amazed3 at right
    voice audio.yyuri_v_celebrate3a
    yu "Yay! You’re a lifesaver, Aiden! I think we’re gonna be really good friends! *whispers* If you survive the pizza, that is…"

    show yyoshi play3 at center
    voice audio.yyoshi_v_unsure2a
    yo "Are you sure you really don’t want to come with us, Yuri? I can cook up another one for you, if you’d like!"

    show yyuri play2 at right
    voice audio.yyuri_v_nothankyou1a
    yu "No, thank youuuuuu~~"
    yu "Oh, and Aiden, make sure to tell Yoshi what you REALLY think about his cooking, okay?!"

    show yaiden talk4 at left
    voice audio.yaiden_v_alright2a
    a "O-Okay…!"

    show yyuri tease2 at right
    voice audio.yyuri_v_tease2a
    yu "Have fun on your date with the cute new guy, Yoshi~! "

    hide yyuri_camp
    hide yyuri tease2
    with dissolve

    show yyoshi angry2 at center
    voice audio.yyoshi_v_no2
    yo "I-It’s not a date!! "

    show yyoshi explain2 at center
    voice audio.yyoshi_v_anyway2
    yo "*ehem* Anyway, the food’s waiting in the kitchen! Come on!"

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
    scene bg_kitchen_past_day with fade
    play music go_with_the_flow loop

    show yyoshi_camp at left2
    show yyoshi norm1 at left2
    show yaiden_casual at right2
    show yaiden shock3 at right2
    a "..."

    show yyoshi comp3 at left2
    voice audio.yyoshi_v_okay1
    yo "Okay, a little warning, I don’t have a lot of experience cooking, so please don’t expect too much!"
    yo "I did try my best making this food though! I used a recipe, but I made sure to add my own twist, and—"

    show yyoshi confused2 at left2
    voice audio.yyoshi_v_aiden7b
    yo "Aiden…? Are you listening?"

    show yaiden shock2 at right2
    voice audio.yaiden_v_sorry1c1
    a "O-Oh! I’m sorry, Yoshinori…! It’s just… I’ve never seen a really fancy kitchen like this in person before…"

    show yaiden excited3 at right2
    voice audio.yaiden_v_amazed2b2
    a "A two-door fridge, a built-in oven, and a cooking hob with a range hood too…"
    a "We don’t have anything like these back at home… "

    show yyoshi shock2 at left2
    voice audio.yyoshi_v_really1
    yo "Oh, really? That kinda surprises me, considering how good everything Mr. Andre makes here is!"

    play sound sfx_microwavebeep
    show yyoshi happy2 at left2
    voice audio.yyoshi_v_ah4
    yo "Ah! It’s ready!"

    show yyoshi_camp at p5_1
    show yyoshi play2 at p5_1
    with move

    show yyoshi_camp at left2
    show yyoshi play2 at left2
    with move

    voice audio.yyoshi_v_here1
    yo "Here’s the pizza I made! Fresh from the “meekrowahvé”!"

    show yaiden confused2 at right2
    voice audio.yaiden_v_wait1a1
    a "You cooked pizza… in the microwave?"

    show yyoshi bold2 at left2
    voice audio.yyoshi_v_yeah2
    yo "Yeah! Go ahead, try it!"

    show yaiden awkward3 at right2
    voice audio.yaiden_v_alright2b
    a "Alright… "

    show yaiden munch1 at right2
    a "*munch*"

    show yyoshi talk4 at left2
    voice audio.yyoshi_v_so3
    yo "Sooo, how is it? Good, right?"

    show yaiden comp3 at right2
    voice audio.yaiden_v_yeah1c1
    a "Umm… Y-Yeah…"

    show yyoshi confused3 at left2
    voice audio.yyoshi_v_think1a
    yo "I sensed a bit of hesitation there… Don’t be shy, you can tell me what’s wrong!"

    show yaiden think2 at right2
    voice audio.yaiden_v_unsure5b1
    a "M-Maybe it’s a little undercooked… I bit into some raw dough underneath."

    show yyoshi worry2 at left2
    voice audio.yyoshi_v_aww1
    yo "Aww, really? Where did I go wrong…? I followed the recipe exactly."

    show yaiden explain2 at right2
    voice audio.yaiden_v_think1a
    a "I think it would be a lot better if you used the oven and cooked it a bit longer, since the dough you made is a little thick."

    show yyoshi think5 at left2
    voice audio.yyoshi_v_actually1
    yo "I actually used packaged dough from the freezer since I didn’t know how to make bread… And I didn’t know how to use the oven either…"

    show yyoshi talk3 at left2
    voice audio.yyoshi_v_think1b
    yo "H-How about the taste though? I probably can’t get that wrong, right? It’s just pizza!"

    show yaiden awkward2 at right2
    voice audio.yaiden_v_well1c1
    a "W-Well… the taste is very… interesting… Did you really follow a recipe for this?"

    show yyoshi comp6 at left2
    voice audio.yyoshi_v_unsure4
    yo "Sort of… Some of the ingredients weren’t available, so I did a little bit of substituting…"
    yo "I used ketchup for the sauce since it’s made of tomatoes, and I found some bleu cheese in the fridge, so I thought it would be fancy!"

    show yaiden comp3 at right2
    voice audio.yaiden_v_laugh1b1
    a "Ehehe… It doesn’t work the same way…"

    show yyoshi sigh1 at left2
    voice audio.yyoshi_v_sigh2
    yo "*sigh* Aww, man… I thought I would’ve been able to pull it off this time! "

    show yaiden comp2 at right2
    voice audio.yaiden_v_alright3a
    a "It’s alright! At least you gave it a try! It did make me stuffed, so it’s a win either way!"

    show yyoshi comp2 at left2
    voice audio.yyoshi_v_thanks4
    yo "Thanks for being honest and giving me some tips, Aiden. You’re a really nice guy!"

    show yaiden comp5 at right2
    voice audio.yaiden_v_thanks2b1
    a "And thank you for letting me eat your food, Yoshinori!"

    show yyoshi laugh2 at left2
    voice audio.yyoshi_v_response6a
    yo "You’re welcome! Since we’re friends now, just call me Yoshi!"

    show yaiden talk3 at right2
    voice audio.yaiden_v_alright2a
    a "A-Alright, Yoshi!"

    show yyoshi sigh4 at left2
    voice audio.yyoshi_v_sigh2
    yo "Well, I guess I need more practice cooking… *sigh* So much for earning that badge…"

    show yaiden comp3 at right2
    voice audio.yaiden_v_unsure5a1
    a "If you want, maybe I could watch you this time and give you some pointers…?"

    show yyoshi excited1 at left2
    voice audio.yyoshi_v_idea1
    yo "Oh! I have an even better idea! How about you show me how to do it instead? Maybe I’ll learn faster that way!"

    show yaiden shock2 at right2
    voice audio.yaiden_v_what4a
    a "Wh-What? Right now? I’m not a scout here… Is that really okay? "

    show yyoshi comp5 at left2
    voice audio.yyoshi_v_confident3
    yo "We’re not doing anything against the rules, so I’m sure it’ll be fine, Aiden! Trust me!"
    yo "Besides, don’t you wanna use the kitchen here too?"

    show yaiden amazed2 at right2
    voice audio.yaiden_v_amazed3a
    a "Wahh… I-I do…"

    show yyoshi bold2 at left2
    voice audio.yyoshi_v_praise2
    yo "Great, then show me how it’s done and let’s get that cooking badge! "

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
    scene bg_kitchen_past_day with fade
    play music go_with_the_flow loop

    play sound sfx_ovending
    show yaiden_casual at left2
    show yaiden happy2 at left2
    show yyoshi_camp at right2
    show yyoshi talk3 at right2
    voice audio.yaiden_v_oh1a
    a "Oh, it’s done!"

    show yyoshi tasty1 at right2
    voice audio.yyoshi_v_mmm1
    yo "Mmm… It smells so good!"

    show yaiden happy3 at left2
    voice audio.yaiden_v_here1a
    a "Here, let me take it out of the oven!"

    show yaiden_casual at p5_1
    show yaiden happy3 at p5_1
    with move

    show yaiden_casual at left2
    show yaiden happy3 at left2
    with move

    show cg fade at truecenter
    show fxa1 at fx_pos
    with dissolve

    voice audio.yaiden_v_excited2a
    a "Tada! And that’s how I make pizza! "

    voice audio.yyoshi_v_amazed1a
    yo "Woooow!!! My mouth is watering just looking at it! "

    voice audio.yaiden_v_sorry1a1
    a "Sorry, it took a little longer since I had to make the dough and sauce from scratch."

    voice audio.yyoshi_v_amazed2a
    yo "Are you kidding? I can’t believe you made this in less than an hour! I was up all night making mine, hahaha!"

    voice audio.yaiden_v_well1a1
    a "Well, luckily for me, the kitchen here had everything I needed to make it faster. It was my first time trying a food processor, mixer, and an oven!"

    voice audio.yyoshi_v_amazed3
    yo "But you were using the whole kitchen like a pro! It was super cool!"

    voice audio.yaiden_v_laugh1b1
    a "Ah, hehe… I was honestly just tinkering with it until I figured it out – turns out it was pretty simple. "

    voice audio.yaiden_v_anyway1a
    a "Anyways, go ahead, give it a taste while it’s still hot!"

    voice audio.yyoshi_v_alright4
    yo "I thought you’d never ask!"

    hide cg fade
    hide fxa1
    with dissolve

    show yyoshi tasty2 at right2
    yo "*munch*"

    show yaiden worry2 at left2
    voice audio.yaiden_v_think3a
    a "H-How is it?"

    show yyoshi amazed1 at right2
    voice audio.yyoshi_v_amazed1c
    yo "IT’S SO YUMMY!!! This is the best pizza I’ve ever tasted in my entire life!" with vpunch

    show yaiden comp3 at left2
    voice audio.yaiden_v_ah1a
    a "A-Ahh… I think you’re exaggerating…"

    show yyoshi excited1 at right2
    voice audio.yyoshi_v_noway1
    yo "I’m not! I never thought I’d like pineapples on my pizza!"

    show yaiden comp5 at left2
    voice audio.yaiden_v_aww2a
    a "Aww… Well, I’m really glad you like my cooking, Yoshi! "

    show yaiden_casual at center
    show yaiden comp5 at center
    show yyoshi_camp at right
    show yyoshi excited1 at right
    with move

    show andre_camp at left
    show andre shock3 at left
    with dissolve

    voice audio.andre_v_aiden4b
    u "Th-There you are, Aiden! I’ve been looking for you! "

    show yaiden shock3 at center
    voice audio.yaiden_v_dad5a
    a "D-Dad…! "

    show andre sigh1 at left
    voice audio.andre_v_sigh1a
    u "*sigh* Didn’t I tell you to stay in the mess hall?"

    show yyoshi worry2 at right
    voice audio.yyoshi_v_sorry2a
    yo "Oh, I’m sorry about that, Mr. Andre…! I was the one who invited Aiden to help me with my badge-earning activity!"

    show andre sigh2 at left
    voice audio.andre_v_relief2a
    u "Whew… It’s a good thing he ran into you. I was worried he ran off somewhere outside Camp Buddy…"

    show yyoshi talk1 at right
    voice audio.yyoshi_v_andre2
    yo "Hey, Mr. Andre! How come you’ve never brought Aiden here before? He’s a really great guy, and his cooking is amazing, just like yours!"

    show andre talk1 at left
    voice audio.andre_v_conj3b2
    u "He’s been by himself back at home ever since I started working here, so I asked Sir Goro a favor to let me bring him for today. "

    show yyoshi happy1 at right
    voice audio.yyoshi_v_laugh1
    yo "You should bring him more often, then! I’d be happy for him to tag along with me all day!"

    show andre worry2 at left
    voice audio.andre_v_ah1b1
    u "Ah, we’re not really allowed to bring visitors to the camp, actually… Today was just an exception since we had a meeting, and I’ll be working until late tonight."

    show yyoshi excited1 at right
    voice audio.yyoshi_v_idea1
    yo "Oh, how about enrolling him here as a scout, then? That would be so fun!! Don’t you think so, Aiden?!"

    show yaiden excited3 at center
    voice audio.yaiden_v_oh1a
    a "Oh…!"

    show yyoshi amazed1 at right
    voice audio.yyoshi_v_excited1
    yo "We can do all the activities together! We can go hiking, fishing, and you can teach me how to cook until I get my cooking badge!"

    show andre worry3 at left
    voice audio.andre_v_yoshi3c
    u "A-Ah, well, Yoshinori… I’m not sure if that’s possible…"

    show yaiden sad1 at center
    show yyoshi worry3 at right
    voice audio.yyoshi_v_oh3
    yo "O-Oh…"

    show andre sad4 at left
    voice audio.andre_v_unsure2b
    u "I do wish he could come with me more often, but Sir Goro has already done enough for me that I don’t want to ask any more of him. "

    show yyoshi sad4 at right
    voice audio.yyoshi_v_isee2
    yo "I see… That’s a shame…"

    show yaiden comp1 at center
    yo "Aiden is a really talented cook just like you are, Mr. Andre! Look, he made this really yummy pizza from scratch just a little while ago! "

    show andre comp4 at left
    voice audio.andre_v_laugh1a2
    u "Ah, haha… I’d like to say I’m surprised, but cooking has been Aiden’s favorite thing to do since he was little! "
    u "That's why I understand how you feel about Aiden not being able to be a part of the camp."

    $working = False
    $shuffle_menu()
    menu():
        u "That's why I understand how you feel about Aiden not being able to be a part of the camp.{fast}"
        "It's too bad he can't stay.":
            $working = True
            $score_aiden -= 1
            show yyoshi upset6 at right
            voice audio.yyoshi_v_sad2
            yo "It really is too bad he can’t stay, then… I think he could really make a difference at the camp."

            show yaiden sad2 at center
            a "..."

            show andre sad3 at left
            voice audio.andre_v_unsure1a
            u "As much as I’d like that… I don’t know how…"
        "I wish he could stay.":
            $working = True
            show yyoshi upset6 at right
            voice audio.yyoshi_v_sad3
            yo "If only there was some way to have Aiden stay here…"

            show andre sad3 at left
            voice audio.andre_v_unsure1a
            u "As much as I’d like that… I don’t know how…"
        "Aiden would make a great chef.":
            $working = True
            $score_aiden += 1
            show yyoshi think2 at right
            voice audio.yyoshi_v_sad3
            yo "There must be a way to have Aiden here at the camp. I’m sure he’d become, like, the best chef ever!"

            show yaiden shock1 at center
            a "...!"

            show andre worry2 at left
            voice audio.andre_v_ah1b1
            u "Ah…"
        "We could have fun together.":
            $working = True
            $score_aiden += 2
            show yyoshi think2 at right
            voice audio.yyoshi_v_unsure1b
            yo "There must be a way to have Aiden here at the camp. He wouldn’t be alone back at home anymore, and we could have so much fun together!"

            show yaiden shock1 at center
            a "...!"

            show andre worry2 at left
            voice audio.andre_v_ah1b1
            u "Ah…"

    show yaiden talk1 at center
    voice audio.yaiden_v_unsure5b1
    a "M-Maybe I could help you out with the chores, Dad?"

    show andre confused3 at left
    voice audio.andre_v_wait2a
    u "You mean… You want to work with me, Aiden?"

    show yaiden happy2 at center
    voice audio.yaiden_v_yeah1a3
    a "Yeah…! I can help us earn some money, and you won’t have to worry about me being at home alone, since we’ll be together all the time!"

    show andre worry2 at left
    voice audio.andre_v_aiden1a
    u "Aiden…"

    $ renpy.pause (1.0, hard=True)
    show andre comp2 at left
    voice audio.andre_v_agree1a2
    u "Alright. I guess I can talk to Sir Goro about it."

    show yyoshi amazed1 at right
    show yaiden amazed2 at center
    voice audio.yaiden_v_amazed3a
    a "Wah…! Really?!"

    show andre comp4 at left
    voice audio.andre_v_compassion1a1
    u "I can’t promise you it’ll work, but I’ll do my best to convince him, okay?"

    show yyoshi bold2 at right
    voice audio.yyoshi_v_confident2
    yo "Oh, let me help too, Mr. Andre! I’m sure Sir Goro would love to have Aiden here too! Let me just grab Yuri, and we’ll go ask him right away!"

    hide yyoshi_camp
    hide yyoshi bold2
    with moveoutright

    show andre shock3 at left
    voice audio.andre_v_yoshi2b
    u "W-Wait, Yoshinori…!"

    show andre_camp at left2
    show andre sigh1 at left2
    show yaiden_casual at right2
    show yaiden amazed2 at right2
    with move

    voice audio.andre_v_sigh1a
    u "*sigh* That boy is hyper as always… "
    u "I guess you really won him over with your cooking, didn’t you, Aiden?"

    show yaiden comp3 at right2
    voice audio.yaiden_v_ah1a
    a "A-Ah… Well…"

    show andre laugh1 at left2
    voice audio.andre_v_conj1a3
    u "Either way, I’m really glad you made a new friend! Now, come on, let’s go after him!"

    show yaiden laugh1 at right2
    voice audio.yaiden_v_yeah1a2
    a "Yeah!"

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

    $ location = location_kitchen
    $ day = "03"
    $ time = timeline_timeday
    $ season = season_autumn
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene cga2 12 with fade
    play bgsound sfxloop_chopping loop
    play music go_with_the_flow_slow loop

    voice audio.aiden_vsa3_line17
    a "Thinking about it, it’s crazy how things ended up back then.  "

    voice audio.aiden_vsa3_line18
    a "Growing up, it was just Dad and I, and we didn’t have much."

    voice audio.aiden_vsa3_line19
    a "Cooking was the thing we bonded over, but it actually led me to you…"

    voice audio.aiden_vsa3_line20
    a "And then, thanks to your determination, I was able to start working here!"

    show cga2 13 with Dissolve(0.25)
    voice audio.yoshi_vsa3_line11
    yo "It was worth it too! I’ve been able to eat all the delicious food you’ve made over the years, and it’s still the best I’ve ever had! "

    voice audio.aiden_vsa3_line21
    a "Well, look at you, Mr. Smooth-Talker! Keep complimenting my cooking like that, and I’ll serve you today's special, if you catch my drift~"

    show cga2 14 with Dissolve(0.25)
    voice audio.yoshi_vsa3_line12
    yo "A-Aiden…! "

    voice audio.aiden_vsa3_line22
    a "Look at you, you're as red as a tomato! You’re still that same dorky scout, hahaha!"

    voice audio.yoshi_vsa3_line13
    yo "L-Let’s just finish cooking! We have to finish before the workers arrive, and we’re getting distracted!"

    voice audio.aiden_vsa3_line23
    a "Alright, alright! Hahaha!"

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black with fade
    yo "{i}It was really nostalgic to work with Aiden in the kitchen… No wonder he was reminiscing about the past.{/i}"
    yo "{i}It’s not often he and I have a conversation like that, but I’m glad that we were able to look back and spend time together like we used to.{/i}"

    scene cg black
    hide screen location
    hide screen timeline
    hide screen quick_menu
    $quick_menu = False
    with fade
    $ renpy.pause (2.0, hard=True)
    play sound sfx_ovending

    $ location = location_kitchen
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_kitchen_autumn_day with fade
    play music go_with_the_flow loop
    play bgsound sfxloop_kitchen loop

    show aiden_apron2 at left2
    show aiden bold5 at left2
    show yoshi_autumn3 at right2
    show yoshi norm1 at right2
    voice audio.aiden_v_relief1a1
    a "Whew! Mashed potatoes, check! Greens, check! We’ve got two pots of stew simmering and lots of barbecue ribs sitting in the oven, and those should be ready in a few minutes! "

    show yoshi bold2 at right2
    voice audio.yoshi_v_praise1
    yo "That’s great, Aiden! I’m sure the workers will go nuts over your cooking! I can tell how good it is just from the smell! "

    hide aiden_apron2
    hide aiden bold5
    show aiden_apron2 at left2
    show aiden wink2 at left2
    voice audio.aiden_v_well1b2
    a "Well, it’s all thanks to my assistant chef today! If it weren’t for you helping me, I’d probably be scrambling right now trying to get all this done."

    show yoshi comp1 at right2
    voice audio.yoshi_v_response3b
    yo "No problem! I’m just glad we managed to finish everything before the workers even arrived!"

    show aiden_apron2 at p4_1
    show aiden wink2 at p4_1
    show yoshi_autumn3 at p4_2
    show yoshi bold2 at p4_2
    with move

    show taiga_autumn at p4_3
    show taiga talking1 at p4_3
    show yoichi_autumn at p4_4
    show yoichi normal1 at p4_4
    with dissolve

    voice audio.taiga_v_greeting3a
    t "Hey, Yoshi! Yuri told us to fetch you, ’cause the workers are already here!"

    show yoshi happy1 at p4_2
    voice audio.yoshi_v_ah1
    yo "Ah, speaking of, that’s my cue!"

    show yoichi annoyed5 at p4_4
    voice audio.yoichi_v_wait2b
    yi "Wait, what?! You said we came here to snatch some mallows?!"

    show taiga playful2 at p4_3
    voice audio.taiga_v_conjunction2c
    t "Well, I knew you wouldn’t come with me unless I tricked you with treats. "
    t "And I’m not gonna let you bark at the new guys and scare them out of the camp."

    show yoichi_autumn at p5_4
    show yoichi rage2 at p5_4
    with move

    voice audio.yoichi_v_angry2b1
    yi "GRAH!!! You’re gonna get it, you sneaky cat-boy!"

    show taiga panic1 at p4_3
    voice audio.taiga_v_surprised4b
    t "WAH! Get off me, you dog! Shoo!!"

    hide yoshi_autumn3
    hide yoshi rage2
    show yoshi2_autumn3 at p4_2
    show yoshi2 comp5 at p4_2
    voice audio.yoshi_v_laugh1
    yo "Hahaha… Maybe it is a good idea to have you both stay in here…"

    show aiden happy3 at p4_1
    voice audio.aiden_v_comp1a2
    a "Yeah, you can leave these guys to me! I’ll make sure they don’t cause a fuss later, hahaha!"

    hide yoshi2_autumn3
    hide yoshi2 comp5
    show yoshi_autumn3 at p4_2
    show yoshi happy2 at p4_2
    voice audio.yoshi_v_thanks4
    yo "Thanks, Aiden! I’ll bring the workers here soon for lunch so you can meet them too!"

    show aiden excited3 at p4_1
    voice audio.aiden_v_praise1a
    a "Oh, that’s great! I’ve been dying to meet the new guys!"

    hide yoshi_autumn3
    hide yoshi happy2
    show yoshi2_autumn3 at p4_2
    show yoshi2 comp6 at p4_2
    voice audio.yoshi_v_sigh3a
    yo "…Just don’t forget to put on a shirt, okay?"

    show aiden laugh3 at p4_1
    voice audio.aiden_v_laugh2a1
    a "Hahaha! Alright, alright! But just because you helped me today!"
    a "Now go! They must be waiting already!"

    hide yoshi2_autumn3
    hide yoshi2 comp6
    show yoshi_autumn3 at p4_2
    show yoshi happy1 at p4_2
    voice audio.yoshi_v_alright2
    yo "Alright!"

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
    scene bg_entrance_autumn_day with fade
    play music brand_new_day loop
    play bgsound sfxloop_birds loop
    play bgsound2 sfxloop_crowd loop

    show yoshi_autumn at center
    show yoshi shock3 at center
    voice audio.yoshi_v_shock1a
    yo "Whoa…! They weren’t kidding when they said they’d be sending thirty people here…"

    show yoshi_autumn at left2
    show yoshi shock3 at left2
    with move

    show yuri_autumn at right2
    show yuri talk3 at right2
    with dissolve

    voice audio.yuri_v_greet1a
    yu "Ah, there you are, Yoshi! The shuttle just finished unloading the workers and their luggage. I’m getting a little overwhelmed trying to assist everyone."

    show yoshi talk1 at left2
    voice audio.yoshi_v_worry2
    yo "How can I help, Yuri?"

    show yuri confused4 at right2
    voice audio.yuri_v_oh1a
    yu "Oh, I need you to talk with the representatives. I’m sure you’re way better than me when it comes to that kind of formal talk."

    show yoshi happy1 at left2
    voice audio.yoshi_v_alright2
    yo "Alright, Yuri. I’ll take it from here!"

    show yuri_autumn at p4_1
    show yuri confused4 at p4_1
    show yoshi_autumn at p4_2
    show yoshi happy2 at p4_2
    with move

    show lloyd_autumn2 at p4_3
    show lloyd norm2 at p4_3
    show darius_autumn at p4_4
    show darius norm3 at p4_4
    with dissolve

    voice audio.yoshi_v_greet3a1
    yo "Hello! Welcome to Camp Buddy! I’m Yoshinori Nagira, and I’m the one in charge of your move-in today! This is Yuri Nomoru, my fellow scoutmaster."

    show lloyd talk1 at p4_3
    voice audio.lloyd_v_ah1a1
    ar "Ah, we met earlier. Though it’s nice to finally meet you again, Yoshinori! "

    hide yoshi_autumn
    hide yoshi happy2
    show yoshi2_autumn at p4_2
    show yoshi2 confused1 at p4_2
    yo "{i}(Huh? What did he mean by… \“again\”?){/i}"

    show lloyd happy1 at p4_3
    voice audio.lloyd_v_conj6a2
    ar "They call me Architect Sirius, and this is Foreman Najjar."

    show darius talk1 at p4_4
    voice audio.darius_v_greet1a1
    fo "Hi."

    show lloyd bold2 at p4_3
    voice audio.lloyd_v_william2c
    ar "The men behind me are my construction team. As I’m sure you know, we’ve been selected by Clermont Inc. to design and construct all the new buildings and amenities as per the official plan!"
    ar "You can expect nothing but the best from our group! I’m a specialist in both the architectural and structural aspects of the project!"

    show lloyd laugh1 at p4_3
    voice audio.lloyd_v_conj6a2
    ar "If you need any carpentry or masonry work done skillfully, my partner here has mastered both crafts!"

    show darius talk2 at p4_4
    voice audio.darius_v_agree1a
    fo "Yes. "

    hide yoshi2_autumn
    hide yoshi2 confused1
    show yoshi_autumn at p4_2
    show yoshi amazed1 at p4_2
    voice audio.yoshi_v_amazed3
    yo "That’s amazing! We’re looking forward to working with you and making this place the best it can be!"

    show lloyd happy2 at p4_3
    voice audio.lloyd_v_gratitude2a2
    ar "Us as well! It’s a privilege to be here!"

    show yoshi happy1 at p4_2
    voice audio.yoshi_v_conj6a
    yo "Before we get into business, we’d like to invite you over for a lunch that we prepared. I know you all must be exhausted from the trip here."

    show lloyd grin1 at p4_3
    voice audio.lloyd_v_praise3a
    ar "That’s perfect! "

    show yoshi bold2 at p4_2
    voice audio.yoshi_v_alright2
    yo "Alright! Yuri and I will help you to your cabins so you can drop off your belongings first!"
    yo "We’ve prepared lodging for all your workers in some of our unused cabins, while you two can stay with us in our scoutmaster quarters, if that’s alright?"

    show lloyd happy1 at p4_3
    voice audio.lloyd_v_agree2b1
    ar "Sure thing! That sounds like a great chance to catch up!"

    show yuri happy1 at p4_1
    voice audio.yuri_v_rush4a
    yu "Great, then please follow me!"

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black with fade

    yo "{i}Yuri and I took the supervisors and their teams to their respective cabins and gave them time to unpack their belongings.{/i}"
    yo "{i}The whole time I’ve been with them, I can’t shake the feeling that I’ve met them before… But I can’t remember when or where.{/i}"
    yo "{i}I can figure that out later! For now, I just need to do my best to give them a proper welcome and instructions!{/i}"

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
    scene bg_messhall_autumn_day with fade #jey bg_messhall_autumn_day_crowd
    play music buddy_oath_casual loop
    play bgsound sfxloop_messhall loop

    show darius_autumn at p4_1
    show darius norm3 at p4_1
    show lloyd_autumn2 at p4_2
    show lloyd norm2 at p4_2
    show yoshi_autumn at p4_3
    show yoshi norm1 at p4_3
    show yuri_autumn at p4_4
    show yuri norm1 at p4_4
    voice audio.yuri_v_alright1a1
    yu "Food’s coming right up soon! I’ve already told our chef we were here!"

    show lloyd hungry2 at p4_2
    voice audio.lloyd_v_gratitude3a
    ar "We appreciate the hospitality! I’m starving!"
    ar "Also, thanks for helping us move in! Things have barely changed here at all, haven’t they?"

    show yoshi happy1 at p4_3
    voice audio.yoshi_v_yes1
    yo "Yes! We’ve tried to keep all the spaces the same throughout the years to keep the classic feel of the place. I knew you would appreciate it, being an architect!"

    show lloyd explain1 at p4_2
    voice audio.lloyd_v_conj1a3
    ar "Well, I kinda meant it in a nostalgic sense!"

    show yoshi talk3 at p4_3
    voice audio.yoshi_v_right7
    yo "Ah, right…!"
    yo "Though, I have to say, you must be a genius to be an architect at such an early age, Mr. Sirius!"

    show lloyd angry3 at p4_2
    voice audio.lloyd_v_greet2c2
    ar "Early age?! I’m about as old as you are!"

    hide yoshi_autumn
    hide yoshi talk3
    show yoshi2_autumn at p4_3
    show yoshi2 confused2 at p4_3
    voice audio.yoshi_v_really5
    yo "Wait… Really? I just thought that—"

    show lloyd rage3 at p4_2
    voice audio.lloyd_v_ignored1c3
    ar "Is that because I’m short?!"

    show darius bored5 at p4_1
    voice audio.darius_v_comp1a1
    fo "Calm down."

    show lloyd pout4 at p4_2
    voice audio.lloyd_v_annoyed1b3
    ar "Hmph!"

    show darius shy5 at p4_1
    voice audio.darius_v_sorry3
    fo "I’m sorry about that. Topics about his height trigger him."

    show yoshi2 panic4 at p4_3
    voice audio.yoshi_v_sorry1a1
    yo "Ah, I apologize, that’s not what I meant…!"

    show yuri sigh3 at p4_4
    voice audio.yuri_v_sigh2a
    yu "*sigh* Yoshi, what’s wrong with you…"

    show lloyd angry5 at p4_2
    voice audio.lloyd_v_conj1a2
    ar "Well, I’ll let it slide for now, for old time’s sake."

    show lloyd happy1 at p4_2
    voice audio.lloyd_v_conj2b1
    ar "Anyways, there’s another thing that didn’t change – this place smells as good as I remember!"

    show yuri laugh1 at p4_4
    voice audio.yuri_v_laugh1a1
    yu "You must’ve been looking forward to it, knowing how good the food here is!"

    show yoshi2 confused1 at p4_3
    yo "{i}(What’s going on…? Am I missing something here? ){/i}"

    show darius talk1 at p4_1
    voice audio.darius_v_shock1a
    fo "Oh, the food’s coming."

    show darius_autumn at p5_2
    show darius talk1 at p5_2
    show lloyd_autumn2 at p5_3
    show lloyd happy1 at p5_3
    show yoshi2_autumn at p5_4
    show yoshi2 confused1 at p5_4
    show yuri_autumn at p5_5
    show yuri laugh1 at p5_5
    with move

    show aiden_apron3 at p5_1
    show aiden bold2 at p5_1
    with dissolve

    voice audio.aiden_v_orderup1a
    a "Order up! Four servings of a full-course barbecue meal with sides!"

    hide aiden_apron3
    hide aiden bold2
    show aiden2_apron3 at p5_1
    show aiden2 shock3 at p5_1
    voice audio.aiden_v_wait2b2
    a "Hold on… You’re…"

    hide yoshi2_autumn
    hide yoshi2 confused1
    hide aiden2_apron3
    hide aiden2 bold2
    show yoshi_autumn at p5_4
    show yoshi shock1 at p5_4
    show aiden_apron3 at p5_1
    show aiden excited1 at p5_1
    voice audio.aiden_v_shock3a2
    a "No way! Is that you, Darius?!" with vpunch

    show darius happy2 at p5_2
    voice audio.darius_v_aiden3
    d "Aiden. "

    show aiden amazed1 at p5_1
    voice audio.aiden_v_greet1c
    a "How are you, man?! It’s been forever!"

    show darius happy3 at p5_2
    voice audio.darius_v_response2b
    d "I’m good. I didn’t know you worked here too…"

    show aiden excited3 at p5_1
    voice audio.aiden_v_swear2a1
    a "DAMN! You grew, like, a thousand feet tall! I barely recognized you!"

    show darius tease2 at p5_2
    voice audio.darius_v_thanks1a1
    d "You too. You’ve been working out?"

    show aiden laugh3 at p5_1
    voice audio.aiden_v_flex1a
    a "Yeah, gotta flex to impress, right?! "
    a "It’s really nice to see you after all these years! I thought I’d never see you again!"

    show darius comp5 at p5_2
    voice audio.darius_v_agree4
    d "Me too."

    show aiden excited3 at p5_1
    voice audio.aiden_v_wait1a2
    a "Wait... Don’t tell me you’re part of the team that’s gonna work here, too?!"

    show darius happy1 at p5_2
    voice audio.darius_v_agree2a
    d "Yeah."

    show aiden amazed2 at p5_1
    voice audio.aiden_v_amazed3b
    a "SWEET! You’re gonna have a great time here with us, just like the good ol’ days! "

    show lloyd confused2 at p5_3
    voice audio.lloyd_v_darius4a
    ar "You know this guy, Dar?"

    show darius confused2 at p5_2
    voice audio.darius_v_rush2
    d "He’s the cook’s son. Don’t you remember?"

    show aiden shock3 at p5_1
    voice audio.aiden_v_what2b
    a "And who’s the kid? Wait— Don’t tell me you have a son already?! Sheesh, has it really been that long?!"

    show lloyd rage3 at p5_3
    voice audio.lloyd_v_question1b1
    ar "WHAT?!"

    show aiden laugh2 at p5_1
    voice audio.aiden_v_amazed1a1
    a "You should enroll him here for the next term! Camp Buddy is definitely at its peak right now— "

    show lloyd rage4 at p5_3
    voice audio.lloyd_v_conj3b1
    ar "FIRST OFF, I’M NOT A KID! And I’m definitely NOT HIS SON!"

    show darius explain2 at p5_2
    voice audio.darius_v_lloyd2
    d "This is Lloyd, my business partner. He’s older than me, Aiden."

    hide aiden_apron3
    hide aiden laugh2
    show aiden2_apron3 at p5_1
    show aiden2 comp3 at p5_1
    voice audio.aiden_v_laugh1b1
    a "Oh... hehe… My bad, little guy!"

    show lloyd annoy4 at p5_3
    voice audio.lloyd_v_groan1d3
    l "HNGH!! LITTLE?! How dare you!"

    show yuri tease2 at p5_5
    voice audio.yuri_v_laugh1b2
    yu "Hihihi, you can’t seem to catch a break."

    show lloyd pout1 at p5_3
    voice audio.lloyd_v_annoyed1b3
    l "Hmph! I’m starting to have second thoughts about coming back here!"

    show yuri angry1 at p5_5
    voice audio.yuri_v_aiden1a
    yu "Aiden, stop teasing our lead architect! He and Darius will be helping us with the renovations!"

    show aiden2 kiss1 at p5_1
    voice audio.aiden_v_whistle1a
    a "*whistle* An architect, huh? Wow, my bad for missing that! It’s just that you look—"

    show lloyd rage1 at p5_3
    l "*glares*"

    show aiden2 comp3 at p5_1
    voice audio.aiden_v_think2b
    a "…youthful?? "

    show lloyd laugh2 at p5_3
    voice audio.lloyd_v_laugh1a1
    l "People do tend to say that about me, haha!"

    show darius tease4 at p5_2
    voice audio.darius_v_excited1a1
    d "Nice save."

    hide aiden2_apron3
    hide aiden2 comp3
    show aiden_apron3 at p5_1
    show aiden excited1 at p5_1
    voice audio.aiden_v_amazed1a2
    a "But that’s super awesome though! This project is gonna be a lot more exciting with you guys here!"

    show yuri laugh2 at p5_5
    voice audio.yuri_v_yeah1b2
    yu "Yeah, it’s as if the stars aligned and we’re all having a reunion, aren’t we?"

    show lloyd excited1 at p5_3
    voice audio.lloyd_v_shock1a3
    l "Oh, you can say that again! My horoscope this month told me that I was going to \“meet familiar faces on the roads ahead.\”"
    l "…And now I’m here, reconnecting with you guys! Coincidence? I think not!"

    hide aiden_apron3
    hide aiden excited1
    show aiden2_apron3 at p5_1
    show aiden2 confused2 at p5_1
    voice audio.aiden_v_confused2a2
    a "Isn't that the same kinda thing you read in a fortune cookie…?"

    hide yoshi_autumn
    hide yoshi shock1
    show yoshi2_autumn at p5_4
    show yoshi2 confused5 at p5_4
    voice audio.yoshi_v_uh1b
    yo "U-Uh… I’m really sorry about this, but I’m confused… How do you guys know each other?"
    yo "I don’t wanna be rude, but… I did think something was oddly familiar about you both since we first met…"

    show yuri shock4 at p5_5
    voice audio.yuri_v_wait1a1
    yu "Wait… You mean, you didn’t know this whole time, Yoshi?! "
    yu "We’ve been talking with them all morning – you should’ve at least figured out who they are by now!"

    hide yoshi2_autumn
    hide yoshi2 confused1
    show yoshi_autumn at p5_4
    show yoshi panic5 at p5_4
    voice audio.yoshi_v_shock3
    yo "GAH! I-I’m so sorry…!"

    show yuri confused4 at p5_5
    voice audio.yuri_v_request3a
    yu "This is Lloyd Sirius and Darius Najjar! They’re Camp Buddy alumni! "
    yu "How could you not remember?! You were in the same batch as them!"

    hide yoshi_autumn
    hide yoshi panic5
    show yoshi2_autumn at p5_4
    show yoshi2 worry5 at p5_4
    voice audio.yoshi_v_think1b
    yo "Umm…"

    show yuri irked2 at p5_5
    voice audio.yuri_v_ugh3a
    yu "Ugh… I can’t believe you, Yoshi! "
    yu "*slams a book on the table*"

    show yuri bold2 at p5_5
    voice audio.yuri_v_here1b
    yu "Here they are! Luckily, we have pictures of them in my old journal!"

    show aiden2 awkward2 at p5_1
    voice audio.aiden_v_confused1a1
    a "D-Do you just carry that around…?"

    show cg fade at truecenter
    show fx4 at fx_pos
    with dissolve

    yo "..."

    voice audio.yoshi_vs4_line1
    yo "O-Oh!!! Now I remember! Little Lloyd and Serious Darius from the first term?!"

    voice audio.yuri_vs4_line1
    yu "YES! Oh my god, no wonder you were acting so weird!!!"

    voice audio.lloyd_vs4_line1
    l "Geez… Took you a while to recognize us…"

    voice audio.darius_vs4_line1
    d "That’s funny."

    voice audio.yuri_vs4_line2
    yu "I guess my dad isn’t the only one getting old."

    voice audio.lloyd_vs4_line2
    l "And I thought he was just being his usual goody-two-shoes self, trying to act all serious for business."

    hide cg fade
    hide fx4
    with dissolve

    hide yoshi2_autumn
    hide yoshi2 worry5
    show yoshi_autumn at p5_4
    show yoshi amazed2 at p5_4
    voice audio.yoshi_v_amazed2a
    yo "Would you look at that… Little Lloyd… I can’t believe it’s really you!"

    show lloyd annoy2 at p5_3
    voice audio.lloyd_v_groan2a3
    l "Ugh. Can we please stop with the nicknames?! We already put up with them the entire time we were at camp!"

    hide yoshi_autumn
    hide yoshi amazed2
    show yoshi2_autumn at p5_4
    show yoshi2 think6 at p5_4
    voice audio.yoshi_v_actually2b
    yo "Now that I think about it… you still haven’t grown any taller since then… Not that it’s a bad thing! "

    show lloyd rage3 at p5_3
    voice audio.lloyd_v_greet2d1
    l "HEY, THAT’S NOT TRUE!! Tell him, Dar! You measured it, right?"

    show darius bored5 at p5_2
    voice audio.darius_v_agree2a
    d "Around 160 centimeters, yeah. Shoes included. "
    d "You’ve grown one centimeter since we last saw them."

    show lloyd confused3 at p5_3
    voice audio.lloyd_v_aiden2c
    l "I’ll admit though, I also am guilty of forgetting someone. I don’t think I remember you at all, Aiden."

    hide aiden2_apron3
    hide aiden2 awkward2
    show aiden_apron3 at p5_1
    show aiden comp6 at p5_1
    voice audio.aiden_v_alright3b2
    a "Hehe, it’s alright! I wasn’t a scout back then, so that’s probably why you don’t recognize me."
    a "But Yoshi here has no excuse… I still can’t believe you didn’t recognize them, especially Darius!"

    show yoshi2 awkward4 at p5_4
    voice audio.yoshi_v_ah2
    yo "Aaah… This is so embarrassing… I-I’m so sorry, Darius. It’s just, you look nothing like I remember, and it didn’t even cross my mind that you’re the same person."

    show darius comp5 at p5_2
    voice audio.darius_v_comp3a
    d "It’s okay. "
    d "Almost everyone says the same."

    show aiden amazed1 at p5_1
    voice audio.aiden_v_oho1a
    a "Yeah, who knew you’d turn out to be such a hunk!"

    show yuri tease2 at p5_5
    voice audio.yuri_v_agree2a1
    yu "You said it, Aiden~ Such a fine gentleman with a mysteriously deep voice and menacing eyes~"

    show lloyd rage3 at p5_3
    voice audio.lloyd_v_question1d2
    l "What the hell?! You guys have all these good things to say about Dar, while I get a bunch of height insults?!"
    l "That’s not fair!"

    show aiden laugh2 at p5_1
    voice audio.aiden_v_comp3b
    a "Like Yoshi said, we don’t mean it in a bad way! There’s lots of perks to being fun-sized!"

    show lloyd annoy2 at p5_3
    voice audio.lloyd_v_annoyed1a3
    l "Oh yeah? Like what?"

    hide aiden_apron3
    hide aiden laugh2
    show aiden2_apron3 at p5_1
    show aiden2 think4 at p5_1
    a "..."

    show aiden2 think6 at p5_1
    voice audio.aiden_v_think2a
    a "Uhh… More legroom in vehicles…?"

    show lloyd think4 at p5_3
    l "..."

    show yuri comp2 at p5_5
    voice audio.yuri_v_praise4a
    yu "I think you’re super cute and charming, Lloyd! You have the blessing of eternal youth coursing through your veins! "
    yu "The Forever Twinky One, am I right?!"

    show lloyd angry2 at p5_3
    voice audio.lloyd_v_request2c
    l "Can we stop talking about my height already?! I don’t know how we’re always coming back to this topic! "

    show yoshi2 shy5 at p5_4
    voice audio.yoshi_v_sorry5b
    yo "W-We’re sorry about that, Lloyd! Either way, it’s really nice to have past members of Camp Buddy back here sharing their skills!"

    show lloyd talk2 at p5_3
    voice audio.lloyd_v_agree2a3
    l "Yeah. I’m definitely not surprised that you ended up being a scoutmaster here, Yoshinori. You’ve always been the model scout."

    hide yoshi2_autumn
    hide yoshi2 awkward4
    show yoshi_autumn at p5_4
    show yoshi happy1 at p5_4
    voice audio.yoshi_v_actually1a
    yo "It’s kinda crazy how we’ve all come full circle and are sharing a common goal once again! "

    show yuri confused2 at p5_5
    voice audio.yuri_v_conj6a
    yu "I am curious though, how did you guys end up getting hired to work for Camp Buddy? Was it really a twist in fate? "

    show lloyd talk4 at p5_3
    voice audio.lloyd_v_shock1a1
    l "Oh, Clermont Inc. actually reached out to a bunch of different construction firms with the basics of the project."
    l "When Dar and I saw that it was for Camp Buddy, we got excited and immediately sent an application in."

    show lloyd happy1 at p5_3
    voice audio.lloyd_v_laugh1a1
    l "We were overqualified for Mr. Clermont’s criteria, and once he heard we were past scouts from Camp Buddy as well, we were immediately given the job."
    l "It also worked out really well – since I spent a lot of time at this camp as a scout, my architectural style became focused around rustic and cozy designs!"

    show yoshi talk1 at p5_4
    voice audio.yoshi_v_so1a
    yo "So will the new cabins be your main focus while you’re both here?"

    show lloyd explain1 at p5_3
    voice audio.lloyd_v_conj1a3
    l "Well, as far as I know, that will take the most of our time, but there's a few other projects as well."
    l "We’ll also be building an events hall, an infirmary, and some guest lodging along the lake."

    show yoshi talk3 at p5_4
    voice audio.yoshi_v_really5
    yo "That’s quite a lot… Is it really possible to build all of that in such a short amount of time?"

    show lloyd happy2 at p5_3
    voice audio.lloyd_v_darius2b
    l "Well, that’s why Dar is around! He works wonders when it comes to construction!"

    hide aiden2_apron3
    hide aiden2 think6
    show aiden_apron3 at p5_1
    show aiden happy1 at p5_1
    voice audio.aiden_v_darius3a
    a "Darius has always been a super crafty guy, even back when we were scouts! He actually gave me my first lesson in carpentry, and I’ve still got those skills!  "
    a "Thanks to that, I was able to help Yoshi with some projects over the past few years. Just last summer, we worked with a few scouts to fix some of the really busted up cabins!"

    show aiden happy3 at p5_1
    voice audio.aiden_v_oh1b
    a "And we built a really huge obstacle course too! "

    show lloyd shock3 at p5_3
    voice audio.lloyd_v_amazed3a1
    l "Whoa! You mean like the ones on those TV game shows?!"

    show yoshi happy1 at p5_4
    voice audio.yoshi_v_yes2
    yo "Yes! It was my very first project when I started working here!"

    show lloyd shock3 at p5_3
    voice audio.lloyd_v_amazed2a1
    l "And you worked on that with just the two of you?!"

    show yoshi comp3 at p5_4
    voice audio.yoshi_v_yeah2
    yo "For the most part, yeah…! It took a few years for it to actually be useable though."

    show lloyd excited1 at p5_3
    voice audio.lloyd_v_laugh1a1
    l "You’ll have to show us around, then! I want to see the whole camp after all these years. "
    l "It’ll also give me an idea of what we’re dealing with for the project."

    show yoshi happy2 at p5_4
    voice audio.yoshi_v_agree1b2
    yo "Of course! We’re scheduled to give you a full tour of the camp after lunch!"

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black with fade
    yo "{i}The five of us spent the next little while in the mess hall finishing up our lunch and catching up on old times, but before long it was time to get back to work.{/i}"
    yo "{i}Yuri took the other workers back to their cabins to help them get settled in, while Aiden dragged Yoichi and Taiga to help him clean the kitchen after the workers finished. {/i}"
    yo "{i}Meanwhile, I took Darius and Lloyd on a tour of the camp, showing them all the changes and discussing the work they’d be doing in more detail… {/i}"

    scene cg black
    hide screen location
    hide screen timeline
    hide screen quick_menu
    $quick_menu = False
    with fade
    $ renpy.pause (2.0, hard=True)
    $ time_transition_day_to_sunset_fall()

    $ location = location_campsite
    $ time = timeline_timesunset
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_campgrounds_autumn_sunset with fade
    play music sunset_stroll loop

    show yoshi_autumn at left
    show yoshi happy1 at left
    show darius_autumn at center
    show darius norm1 at center
    show lloyd_autumn2 at right
    show lloyd norm2 at right
    voice audio.yoshi_v_bye6a
    yo "And I think that covers all the locations around the camp! Did you guys see everything you wanted? "

    show lloyd happy1 at right
    voice audio.lloyd_v_agree2b2
    l "Yeah, I think Darius and I got a pretty good look at the site. I also got most of the measurements I needed."
    l "I had already drafted most of the stuff before I got here today, but after seeing the actual site, there will need to be some adjustments."

    show lloyd talk1 at right
    voice audio.lloyd_v_conj6a2
    l "We’ll start preparing the site first thing tomorrow. Our aim is to clear out the land of trees and debris, level the ground, then move all the building materials there by the end of this week."

    show yoshi talk1 at left
    voice audio.yoshi_v_response1a
    yo "I understand. I’ll be around to help and supervise as needed."

    show lloyd talk2 at right
    voice audio.lloyd_v_conj2b1
    l "Now, if you’ll excuse me, I’ll head out and get started on those adjustments to the plan!"

    show yoshi happy2 at left
    voice audio.yoshi_v_alright2
    yo "Alright. If you need anything at all, you know where to find me."

    show lloyd happy2 at right
    voice audio.lloyd_v_response2a1
    l "Sure. I’ll be working in our cabin for now. See you tomorrow! "

    hide lloyd_autumn2
    hide lloyd happy2
    with dissolve

    show yoshi_autumn at left2
    show yoshi happy2 at left2
    show darius_autumn at right2
    show darius shy3 at right2
    with move

    d "..."

    hide yoshi_autumn
    hide yoshi happy2
    show yoshi2_autumn at left2
    show yoshi2 confused4 at left2
    yo "..."

    show yoshi2 confused5 at left2
    voice audio.yoshi_v_darius5a
    yo "Uhh… Darius? Aren’t you gonna go with Lloyd? "

    show darius shy4 at right2
    voice audio.darius_v_no1a
    d "No. Lloyd likes to work alone, undisturbed."

    show yoshi2 think6 at left2
    voice audio.yoshi_v_isee2
    yo "Oh… I see…"

    show darius shy1 at right2
    d "..."

    show yoshi2 shy3 at left2
    yo "{i}(This is awkward… Darius is just standing there, staring at me… I’m not sure if I should leave or say something—){/i}"

    show yoshi2_autumn at center
    show yoshi2 shy3 at center
    show darius_autumn at right
    show darius shy1 at right
    with move

    show aiden_autumn at left
    show aiden happy2 at left
    with dissolve

    voice audio.aiden_v_hey2a2
    a "Hey there, you two!"

    hide yoshi2_autumn
    hide yoshi2 shy3
    show yoshi_autumn at center
    show yoshi awkward4 at center
    voice audio.yoshi_v_hey3
    yo "O-Oh! Hey there, Aiden! "

    hide aiden_autumn
    hide aiden happy2
    show aiden2_autumn at left
    show aiden2 shock2 at left
    voice audio.aiden_v_confused1a1
    a "Huh? Why are you two just standing here, looking weird?"

    show yoshi explain2 at center
    voice audio.yoshi_v_ah3
    yo "A-Aah, well, I just finished giving Lloyd and Darius their tour. Lloyd just left for our cabin to do some work."

    hide aiden2_autumn
    hide aiden2 shock2
    show aiden_autumn at left
    show aiden amazed2 at left
    voice audio.aiden_v_shock3a2
    a "No way, they’re gonna be staying with us too?! "
    a "Sweet! We’re gonna be roomies, Dar!"

    show darius happy2 at right
    voice audio.darius_v_excited1a1
    d "Nice."

    show aiden happy1 at left
    voice audio.aiden_v_actually1a
    a "I just finished everything in the kitchen for today. Looks like you guys are on break now too!"

    show yoshi comp2 at center
    voice audio.yoshi_v_unsure3a
    yo "I guess you could say that… Today turned out to be a busy day."

    show aiden happy3 at left
    voice audio.aiden_v_anyway1a
    a "Anyways, Darius! You didn’t really get much of a chance to talk a while ago! How are you, my good man~?"

    show darius happy1 at right
    voice audio.darius_v_response2a
    d "I’m good. Excited for the project."

    hide aiden_autumn
    hide aiden happy3
    show aiden2_autumn at left
    show aiden2 kiss2 at left
    voice audio.aiden_v_sheesh1a
    a "Sheesh, you don’t sound excited at all. Come on, tell us more! How have you been all these years?"

    hide yoshi_autumn
    hide yoshi comp2
    show yoshi2_autumn at center
    show yoshi2 awkward3 at center
    voice audio.yoshi_v_aiden13
    yo "Aiden… You don’t have to force him to speak up…"

    show darius sad2 at right
    voice audio.darius_v_no1a
    d "No, he’s right."
    d "I just don’t know what to say sometimes."

    hide aiden2_autumn
    hide aiden2 kiss2
    show aiden_autumn at left
    show aiden laugh2 at left
    voice audio.aiden_v_laugh2a1
    a "Haha! You’ve always been the quiet kind, but I thought you’d get over that after so many years! "

    show darius awkward1 at right
    d "..."

    show aiden happy1 at left
    voice audio.aiden_v_conj2a3
    a "See, Darius here was kinda like a brother to me back in my scout days, Yoshi."
    a "He didn’t have many friends because the other scouts were easily intimidated by him."

    show darius sigh1 at right
    voice audio.darius_v_confident1
    d "It’s true."

    hide yoshi2_autumn
    hide yoshi2 awkward3
    show yoshi_autumn at center
    show yoshi think2 at center
    voice audio.yoshi_v_think1a
    yo "I do remember seeing you with him sometimes whenever we were at the mess hall."

    show aiden grin1 at left
    voice audio.aiden_v_yeah1b1
    a "Yeah! He usually hung out there whenever he wasn’t with his cabinmate."

    hide yoshi_autumn
    hide yoshi think2
    show yoshi2_autumn at center
    show yoshi2 shy5 at center
    voice audio.yoshi_v_unsure3c
    yo "I-I guess I kinda didn’t know how to get close to him back then since everyone was calling him Serious Darius… I thought it was because he was a troublemaker or something…"

    show aiden bold2 at left
    voice audio.aiden_v_bro1b
    a "That’s why you gotta speak up more bro, so people like Yoshi won’t get scared of you."

    show darius sad3 at right
    voice audio.darius_v_sorry2b
    d "I’m sorry if I’m scary."

    hide yoshi2_autumn
    hide yoshi2 shy5
    show yoshi_autumn at center
    show yoshi comp2 at center
    voice audio.yoshi_v_no5
    yo "N-No you’re not, Darius! I understand now that you’re just a quiet person – I’m the one in the wrong for not trying to get to know you back then."

    show darius talk2 at right
    voice audio.darius_v_conj1b1
    d "I want to get along with everyone. But unlike Lloyd, I can’t keep a conversation going."

    show aiden relief2 at left
    voice audio.aiden_v_comp1a1
    a "Just let it all loose and don’t think about it too much!"

    show darius comp2 at right
    voice audio.darius_v_thanks1a1
    d "Thanks, I’ll keep that in mind. "
    d "Lloyd usually does the speaking for me. "

    show aiden comp3 at left
    voice audio.aiden_v_unsure1b
    a "I guess it makes sense that a quiet person needs someone active around to balance things out."

    show darius explain2 at right
    voice audio.darius_v_agree3
    d "I agree. It’s convenient that I don’t have to say anything when Lloyd is around."
    d "Some people find him rude and annoying because it seems like he’s always talking over me."

    show darius comp2 at right
    voice audio.darius_v_conj5b
    d "But... Honestly, it’s the other way around. I like how expressive he is. It’s something I wish I was."

    show aiden tease1 at left
    voice audio.aiden_v_oho1b
    a "Look at you Mr. \“I’m-not-good-at-conversations\”~"

    show darius shock5 at right
    voice audio.darius_v_ah1d3
    d "A-Ah… "

    show yoshi awkward3 at center
    voice audio.yoshi_v_aiden6
    yo "Aiden! Don’t tease him like that!"

    show darius comp5 at right
    voice audio.darius_v_comp3a
    d "It’s okay. I’m used to Aiden joking around."
    d "It’s how I got to know him in the first place."

    show aiden laugh1 at left
    voice audio.aiden_v_laugh2a1
    a "Haha! Yoshi’s known me for forever, and he’s still not used to it!"

    show yoshi annoy3 at center
    voice audio.yoshi_v_well3
    yo "W-Well, I am! Just not when you do it to other people!"

    show darius tease2 at right
    voice audio.darius_v_question1c
    d "Are you jealous?"

    hide yoshi_autumn
    hide yoshi annoy3
    show yoshi2_autumn at center
    show yoshi2 awkward4 at center
    voice audio.yoshi_v_what4
    yo "Wh-Wha…?"

    show aiden laugh4 at left
    voice audio.aiden_v_laugh2c1
    a "Hahahaha! Good one, bro!"

    hide yoshi2_autumn
    hide yoshi2 awkward4
    show yoshi_autumn at center
    show yoshi comp3 at center
    voice audio.yoshi_v_anyway3a
    yo "A-Anyway, I just want to say that I’m glad to get to know you better, Darius!"
    yo "I hope we both can enjoy our time here at camp together this time around! It’s never too late to make friends, after all. "

    show darius comp2 at right
    voice audio.darius_v_thanks2a1
    d "Thank you. You guys are very friendly."

    hide darius_autumn
    hide darius comp2
    with dissolve

    hide yoshi_autumn
    hide yoshi comp3
    show yoshi2_autumn at center
    show yoshi2 panic2 at center
    voice audio.yoshi_v_ah3
    yo "A-Ah… Did I say anything wrong…?"

    show aiden comp5 at left
    voice audio.aiden_v_no2a1
    a "Hahaha! I don’t think so, I think Darius just thought the conversation was over."

    show aiden comp5 at left2
    show aiden_autumn at left2
    show yoshi2_autumn at right2
    show yoshi2 confused5 at right2
    with move

    voice audio.yoshi_v_isee1
    yo "Ohh… I see… Darius is a really interesting guy, isn’t he?"

    show aiden comp2 at left2
    voice audio.aiden_v_well1b2
    a "You’re just not used to handling stoic people, Yoshi. You tend to hang around the more active types."
    a "I mean, I’m living proof! "

    hide yoshi2_autumn
    hide yoshi2 confused5
    show yoshi_autumn at right2
    show yoshi comp3 at right2
    voice audio.yoshi_v_right9
    yo "Haha, I guess you’re right, Aiden."

    show aiden happy1 at left2
    voice audio.aiden_v_anyway1a
    a "Anyways, now that everything’s done for today, why don’t we head back and get some rest?"

    show yoshi explain2 at right2
    voice audio.yoshi_v_well1
    yo "Well, I still have to write down a report for Sir Goro about everything that happened today."

    hide aiden_autumn
    hide aiden happy1
    show aiden2_autumn at left2
    show aiden2 sleepy2 at left2
    voice audio.aiden_v_amazed2a1
    a "Wow… Sounds exciting."

    show yoshi talk2 at right2
    voice audio.yoshi_v_hey1
    yo "Hey, someone’s gotta do it."

    hide aiden2_autumn
    hide aiden2 sleepy2
    show aiden_autumn at left2
    show aiden explain1 at left2
    voice audio.aiden_v_agree5b
    a "I know, I know. Your job is very important after all~ "

    hide aiden_autumn
    hide aiden explain1
    show aiden2_autumn at left2
    show aiden2 sigh1 at left2
    voice audio.aiden_v_unsure1b
    a "I guess in a way I understand how Darius feels. "
    a "I’m really lucky to have you around, too, because you do all this cool stuff that I could never see myself doing in a million years!"

    show yoshi comp2 at right2
    voice audio.yoshi_v_disagree2
    yo "That’s not true, Aiden. You could do things like this too, if you tried!"

    hide aiden2_autumn
    hide aiden2 sigh1
    show aiden_autumn at left2
    show aiden happy1 at left2
    voice audio.aiden_v_no2a1
    a "Nah, as long as you’re around, then I’m sure you’ll always have my back! "
    a "…Bareback."

    show yoshi awkward3 at right2
    voice audio.yoshi_v_aiden10
    yo "Aiden!!!"

    show aiden laugh2 at left2
    voice audio.aiden_v_laugh2c1
    a "Hahaha! Anyways, I’ll tag along with you~ I can just chill on the couch at the office while you work!"

    show yoshi happy2 at right2
    voice audio.yoshi_v_gratitude1
    yo "Thanks, Aiden.  I appreciate the company."

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

    $ location = location_office
    $ time = timeline_timenight
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_office_autumn_night with fade
    play music ready_for_tomorrow loop

    show yoshi_autumn at left
    show yoshi norm1 at left
    show aiden_autumn at center
    show aiden norm1 at center
    show yuri_autumn at right
    show yuri tired4 at right
    voice audio.yuri_v_ugh3a
    yu "Ughhh… I am sooooo tired…"

    show yoshi happy1 at left
    voice audio.yoshi_v_yuri2
    yo "Hey there, Yuri! How was the orientation?"

    show yuri worry4 at right
    voice audio.yuri_v_no3a1
    yu "I thought greeting thirty men would be fun, but it was so much more work than I expected."

    show yoshi comp3 at left
    voice audio.yoshi_v_well3
    yo "W-Well… You had to tell them all about the camp rules and set them up in their cabins… It’s no wonder you’re tired."

    show yuri think4 at right
    voice audio.yuri_v_yeah1d2
    yu "Yeaaahh… I had to make sure everyone was comfortable, so I kept checking on them every now and then."
    yu "It’s so different when we had to take care of the scouts. Bigger men have bigger needs, if you know what I mean?"

    show aiden talk2 at center
    voice audio.aiden_v_response2b3
    a "I getcha. It’s been a while since I’ve served and cleaned up for that many people!"

    show yoshi bold2 at left
    voice audio.yoshi_v_excited1
    yo "It’s kind of exciting though, isn’t it? We’ve had such a quiet last couple of weeks so some hustle and bustle is fun for a change!"

    show yuri confused3 at right
    voice audio.yuri_v_conj4a
    yu "Shouldn’t you be resting now too? I saw you with Lloyd and Darius going around the camp all afternoon."

    show yoshi talk1 at left
    voice audio.yoshi_v_sigh3a
    yo "I’m tired, quite frankly… but I had to finish this report of everyone’s work today for Sir Goro."

    show aiden confused3 at center
    voice audio.aiden_v_yeah2a1
    a "Oh yeah, speaking of Gramps, shouldn’t he be back by now?"

    show yoshi_autumn at p4_2
    show yoshi talk1 at p4_2
    show aiden_autumn at p4_3
    show aiden confused3 at p4_3
    show yuri_autumn at p4_4
    show yuri confused3 at p4_4
    with move

    show goro_autumn at p4_1
    show goro sigh1 at p4_1
    with dissolve

    voice audio.goro_v_sigh1a
    g "*sigh*"

    show yuri talk2 at p4_4
    voice audio.yuri_v_goro1b
    yu "Oh, speak of the devil! Welcome back, Dad!"

    show goro talk1 at p4_1
    voice audio.goro_v_goodpm2a1
    g "Ah, good evening, everyone. "
    g "Did everything go according to schedule today?"

    show yoshi happy1 at p4_2
    voice audio.yoshi_v_yessir1
    yo "Yes, sir! Yuri managed the deliveries, workers, and got everyone settled into their accommodations, while Aiden made sure they were all well fed."

    show yoshi bold5 at p4_2
    voice audio.yoshi_v_conj5b
    yo "Meanwhile, I handled the foremen and gave them a tour, and discussed their plans for the next few days."
    yo "I’ve written down a full report for you on their plans, and you can see it on your desk when you get the chance!"

    show goro happy1 at p4_1
    voice audio.goro_v_thanks2a1
    g "Thank you, Yoshinori. That’s perfect."

    show aiden excited3 at p4_3
    voice audio.aiden_v_goro1b
    a "Oh, and guess what, Gramps? The foremen are actually two former campers of ours, Darius and Lloyd! Remember them?"

    hide goro_autumn
    hide goro happy1
    show goro2_autumn at p4_1
    show goro2 play2 at p4_1
    voice audio.goro_v_really2a
    g "Really? That’s a relief – they’ll know the place even better than an outside contractor would."
    g "I wonder if Mr. Clermont did that on purpose…"

    show yoshi happy1 at p4_2
    voice audio.yoshi_v_actually1a
    yo "Actually, when we were discussing it with them, both Lloyd and Darius told us that they saw the opening was for work on Camp Buddy and signed up right away."
    yo "They must have been excited to come back and help out here after the good times they spent in the past! "

    hide goro2_autumn
    hide goro2 play2
    show goro_autumn at p4_1
    show goro comp2 at p4_1
    voice audio.goro_v_glad1a
    g "I’m glad to hear it. It sounds like we can really rely on them for support. Great work handling everything, you three."

    show yuri talk1 at p4_4
    voice audio.yuri_v_goro5a
    yu "How were your errands though, Dad? What did you end up doing today?"

    show goro talk3 at p4_1
    voice audio.goro_v_oh1a
    g "Oh, I handled more of the permit work that Mr. Clermont needed down at the city hall. "
    g "We should be all set now for the work that’s going to be happening over the next few days."

    show yoshi excited1 at p4_2
    voice audio.yoshi_v_praise1
    yo "That’s great, sir! I have to admit, I was kind of nervous seeing all those people arrive today, but it sounds like we’ve got it all taken care of now."

    hide goro_autumn
    hide goro talk3
    show goro2_autumn at p4_1
    show goro2 explain2 at p4_1
    voice audio.goro_v_no1a1
    g "Not quite, Yoshinori. I also spent some time reviewing the paperwork that Mr. Clermont had prepared, and we can expect even more specialists to arrive starting tomorrow."

    hide goro2_autumn
    hide goro2 explain2
    show goro_autumn at p4_1
    show goro talk2 at p4_1
    voice audio.goro_v_yoshi2a
    g "Yoshinori, I’ll need you to escort them as well, just like you did today for Lloyd and Darius. Is that clear?"

    show yoshi bold2 at p4_2
    voice audio.yoshi_v_confident1
    yo "Yes, sir! You can count on me!"

    show goro talk1 at p4_1
    voice audio.goro_v_think1a1
    g "It seems today was just scratching the surface of the work that’s going to be done here, and our first big trial is going to be an inspection in a week’s time."
    g "We’ll have to work hard to make sure everything is ready by then, so I’ll be expecting you all to be prepared for what’s to come."

    show goro talk4 at p4_1
    voice audio.goro_v_request2a1
    g "Is that clear?"

    show yoshi happy1 at p4_2
    show aiden happy1 at p4_3
    show yuri happy1 at p4_4
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
    play sound sleeping_time
    $ time_transition_night_to_day_fall()
    $ renpy.pause (2.0, hard=True)
    $persistent.profile_unlock.append("lloyd")
    $persistent.profile_unlock.append("darius")
    jump day4
