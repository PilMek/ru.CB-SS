image entrance_transition:
    "images/bgs/bg-w-entrance-day.png"
    pause 1.0
    "images/bgs/bg-p-entrance-day.png" with Dissolve(4.0)

label day10_goro_gepe:
    $ day = "84"
    $ time = timeline_timeday
    $ location = location_office
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    $ working = True

    scene bg_office_winter_day with fade
    play music brand_new_day_winter loop
    play bgsound sfxloop_birds loop

    show goro_autumn at left2
    show goro_ring1 at left2
    show goro worry1 at left2
    show yoshi_autumn at right2
    show yoshi_ring1 at right2
    show yoshi norm3 at right2
    voice audio.william_v_sigh2
    w "That’s truly unfortunate, Mr. Nomoru… I was certain that you would accept this offer!"

    show goro worry2 at left2
    voice audio.goro_v_request4b1
    g "I hope you understand, Mr. Clermont, but I’m more than satisfied with the state of Camp Buddy."
    g "I also believe that continuing to work alongside Yoshinori will allow us to maintain the spirit and quality of the camp better than we otherwise could."

    voice audio.william_v_laugh1
    w "Haha, well it sounds like you’ve fully made up your mind! I won’t try and convince you any further!"

    voice audio.william_v_comp2a
    w "You can relax and not concern yourself about this anymore, but I would like to express that the offer will stay on the table!"
    w "Consider it an open opportunity should you ever change your mind."

    show goro comp2 at left2
    voice audio.goro_v_thanks3a
    g "I really appreciate your generosity, Mr. Clermont. Thank you for giving us a chance."

    voice audio.william_v_bye2b
    w "Of course! Until next time!"

    play sound sfx_phonebutton
    hide goro_autumn
    hide goro_ring1
    hide goro comp2
    show goro2_autumn at left2
    show goro2 sigh1 at left2
    voice audio.goro_v_sigh2a
    g "*sigh* Well, the deed is done…"

    show yoshi comp3 at right2
    voice audio.yoshi_v_comp1
    yo "I think you settled it in the best way possible, Goro. Now I’m glad it’ll finally be off your chest."

    show goro2 worry3 at left2
    voice audio.goro_v_yeah1b1
    g "Yeah, but I have to admit, it felt surreal turning down something I spent my whole life working towards…"
    g "After the first term, I kept building up the camp until it had grown and spread."

    hide goro2_autumn
    hide goro2 worry3
    show goro_autumn at left2
    show goro_ring1 at left2
    show goro sad3 at left2
    voice audio.goro_v_conj10a1
    g "Then I found myself managing several branches at once, and I used them as an excuse to shut away my pain, and fill the emptiness in my heart."
    g "I lost myself along the way, and despite expanding the camp to what I thought was successful, all of it became meaningless…"

    show goro sigh3 at left2
    voice audio.goro_v_conj1a1
    g "And when I found out that you were returning, I couldn’t feel a thing…"
    g "Being reunited with you was something I was waiting for all along, yet I didn’t know where or how I’d begin to reconnect…"

    hide yoshi_autumn
    hide yoshi_ring1
    hide yoshi comp3
    show yoshi2_autumn at right2
    show yoshi2_ring1 at right2
    show yoshi2 worry2 at right2
    voice audio.yoshi_v_goro4
    yo "Goro…"
    yo "I wish I’d had the courage to ask you exactly what happened when we were apart.  "

    show yoshi2 sad4 at right2
    voice audio.yoshi_v_sorry6b
    yo "When I came back to Camp Buddy, it was nothing like before…"
    yo "I didn’t know my way around, and I was so overwhelmed with how different it had become…"

    show yoshi2 sigh1 at right2
    voice audio.yoshi_v_sad1
    yo "I was lost for guidance, yet I couldn’t bring myself to approach you, thinking that it would only burden you more… "
    yo "I knew how busy and stressed you were, so I tried my hardest on my own, hoping that I could make things good for you…"

    show yoshi2 worry2 at right2
    voice audio.yoshi_v_but2
    yo "But even then, I failed you at one point, putting us in a position that caused all the trouble we had to solve today."

    show goro sad2 at left2
    voice audio.goro_v_but2a
    g "That wouldn’t have happened to begin with if I was there guiding you…"
    g "I’ve witnessed the camp change in ways I never wished for… from the scoutmasters losing their passion to the scouts becoming uninterested and unruly…"

    show goro disappoint3 at left2
    voice audio.goro_v_sorry1b1
    g "I only had myself to blame for being at the top of all of it… and it only made me more bitter at my own inaction."
    g "In my head, I was counting on you, Yoshinori, to succeed… begging you to bring back the spirit that was lost…"

    show goro worry2 at left2
    voice audio.goro_v_sigh2a
    g "I refused to guide you and believed there was nothing I could do to help, considering how helpless I was myself…"
    g "It only made me shut off even more, and I felt like all our hardships were for nothing… It was a cycle of self-destruction…"

    show goro comp2 at left2
    voice audio.goro_v_but1a
    g "But all of that is finally over…"
    g "And I have you to thank for it."

    show yoshi2 comp2 at right2
    voice audio.yoshi_v_disagree2
    yo "But it wasn’t me who made all of these changes possible…"
    yo "It was you all along, Goro… I was only there to listen, and allow you to grow at your own pace…"

    hide yoshi2_autumn
    hide yoshi2_ring1
    hide yoshi2 comp2
    show yoshi_autumn at right2
    show yoshi_ring1 at right2
    show yoshi comp3 at right2
    voice audio.yoshi_v_conj3a
    yo "…I’d say your best quality is the way you always persevere no matter the predicament you face, coming out stronger than you were before each time."

    show goro comp3 at left2
    voice audio.goro_v_glad1a
    g "I’m glad you see that in me, Yoshinori…"

    show yoshi comp5 at right2
    voice audio.yoshi_v_laugh1
    yo "That’s what I love about you the most…!"

    show goro happy2 at left2
    voice audio.goro_v_conj9a1
    g "And what I love the most about you is your dedication."
    g "Despite all the struggles we’ve had and the times that things got muddled between us… You always stayed…"

    show goro comp2 at left2
    voice audio.goro_v_praise2a1
    g "You were doing everything you could to help the camp… and to help me."
    g "You’ve been patient and understanding even when I didn’t deserve it... And I admit there was a time when I took that for granted."

    show goro relief2 at left2
    voice audio.goro_v_rush4b1
    g "Now, I can finally do things right, and treat you the way you deserve and more…"
    g "So, thanks for staying by my side and supporting my decision, Yoshinori."

    show yoshi comp3 at right2
    voice audio.yoshi_v_agree1b1
    yo "Of course, Goro… I’ll always be here for you. "

    hide goro_autumn
    hide goro_ring1
    hide goro relief2
    show goro2_autumn at left2
    show goro2 explain3 at left2
    voice audio.goro_v_ehem1a
    g "*ehem*, I think our conversation got way too sentimental. "

    hide yoshi_autumn
    hide yoshi_ring1
    hide yoshi comp3
    show yoshi2_autumn at right2
    show yoshi2_ring1 at right2
    show yoshi2 comp6 at right2
    voice audio.yoshi_v_laugh6
    yo "Ahehe… I-I don’t mind, really… In fact, I think it’s really sweet coming from you."

    show goro2 annoy2 at left2
    voice audio.goro_v_well1a
    g "Well, if you keep pointing it out like that, you’re going to make me want to do it less."

    hide yoshi2_autumn
    hide yoshi2_ring1
    hide yoshi2 comp6
    show yoshi_autumn at right2
    show yoshi_ring1 at right2
    show yoshi laugh2 at right2
    voice audio.yoshi_v_comp5
    yo "Haha! Don’t be shy, you can act however you want whenever you’re around me, Goro!"

    show goro2 comp3 at left2
    voice audio.goro_v_heh1a
    g "Heh…"

    show goro2_autumn at left
    show goro2 comp3 at left
    show yoshi_autumn at center
    show yoshi_ring1 at center
    show yoshi shock1 at center
    with move

    show yuri_winter at right
    show yuri shock2 at right
    with dissolve

    voice audio.yuri_v_goro7a
    yu "Ah, there you are, Dad!"

    hide goro2_autumn
    hide goro2 comp3
    show goro_autumn at left
    show goro_ring1 at left
    show goro happy2 at left
    voice audio.goro_v_goodam1a1
    g "Good morning, Yuri."

    show yuri angry2 at right
    voice audio.yuri_v_angry2a1
    yu "Don’t ‘good morning’ me! You’ve got a lot of explaining to do!"
    yu "What was that all about yesterday? Did you really turn down Mr. Clermont’s offer?!"

    show goro worry2 at left
    voice audio.goro_v_agree1b1
    g "Yes… In fact, I just called him earlier to confirm it…"

    show yuri worry2 at right
    voice audio.yuri_v_worry1a
    yu "Wh-Why…?"

    hide goro_autumn
    hide goro_ring1
    hide goro worry2
    show goro2_autumn at left
    show goro2 sigh1 at left
    voice audio.goro_v_well1a
    g "Well, dear… I’m sure you remember how we tried this together before…"
    g "You saw how difficult and inefficient things were because we weren’t prepared."
    g "And after experiencing what we all thought was the peak of Camp Buddy, it turns out it wasn’t really a good thing."

    show yuri worry4 at right
    voice audio.yuri_v_oh2a
    yu "Oh…"

    hide goro2_autumn
    hide goro2 sigh1
    show goro_autumn at left
    show goro_ring1 at left
    show goro comp2 at left
    voice audio.goro_v_request4a1
    g "All I’m saying is that I’m happy where all of us are now…"
    g "And I don’t think we need anything more than what we already have… "

    show goro comp5 at left
    voice audio.goro_v_conj1a1
    g "Instead, we should do our best to cherish it and make sure we don’t lose sight of what’s truly important…"

    show yuri sad4 at right
    voice audio.yuri_v_comp2a1
    yu "I understand, Dad… I really do."
    yu "Honestly, I’d hate to risk seeing you at your worst again…   And we’ve come such a long way just to fix things and return to how it was when we started…"

    show goro comp3 at left
    voice audio.goro_v_glad1a
    g "I’m relieved you see it too, dear."

    show yuri sigh1 at right
    voice audio.yuri_v_sigh2a
    yu "*sigh* You can just be so reckless sometimes, you know?"
    yu "I mean… You could’ve just told us that to begin with!"

    show goro worry3 at left
    voice audio.goro_v_sorry2a1
    g "Yes… I’m sorry. I had to sort things out with Yoshinori first before I could tell everyone."

    show yuri irked1 at right
    voice audio.yuri_v_yeah2a1
    yu "Speaking of that! You two came home so late last night… and with a motorcycle too!"

    hide yoshi_autumn
    hide yoshi_ring1
    hide yoshi laugh2
    show yoshi2_autumn at center
    show yoshi2_ring1 at center
    show yoshi2 shy5 at center
    voice audio.yoshi_v_ah2
    yo "Ah well, about that…"

    show yuri angry3 at right
    voice audio.yuri_v_worry1a
    yu "What the hell is going on with you both?!"

    hide goro_autumn
    hide goro_ring1
    hide goro worry3
    show goro2_autumn at left
    show goro2 explain3 at left
    voice audio.goro_v_rush4b1
    g "Now, now… There’s a perfectly good explanation for that, Yuri…"

    show yuri angry2 at right
    voice audio.yuri_v_sarcastic2a
    yu "You have to explain it to everyone else! They wouldn’t stop asking me about that bike all morning!"

    show goro2 confused5 at left
    voice audio.goro_v_ah1c
    g "Ah… I figured that’d cause a commotion."

    hide yoshi2_autumn
    hide yoshi2_ring1
    hide yoshi2 shy5
    show yoshi_autumn at center
    show yoshi_ring1 at center
    show yoshi comp2 at center
    voice audio.yoshi_v_think1a
    yo "I think everyone’s at the mess hall having breakfast. Maybe we should take the chance to talk about it before work begins today."

    hide goro2_autumn
    hide goro2 confused5
    show goro_autumn at left
    show goro_ring1 at left
    show goro talk3 at left
    voice audio.goro_v_alright1a1
    g "Alright. Let’s go then."

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
    scene bg_messhall_winter_day with fade
    play music buddy_oath_casual loop
    play bgsound sfxloop_crowd loop

    show darius_winter at p8_1
    show darius norm3 at p8_1
    show aiden2_autumn at p8_3
    show aiden2 talk5 at p8_3
    show lloyd_winter at p8_2
    show lloyd norm3 at p8_2
    show yoshi_autumn at p8_4
    show yoshi_ring1 at p8_4
    show yoshi comp1 at p8_4
    show goro_autumn at p8_5
    show goro_ring1 at p8_5
    show goro norm2 at p8_5
    show yuri_autumn at p8_6
    show yuri norm3 at p8_6
    show emilia_winter3 at p8_7
    show emilia norm3 at p8_7
    show jin_autumn at p8_8
    show jin_glasses at p8_8
    show jin norm4 at p8_8
    voice audio.aiden_v_oh3a
    a "Oooohhh… I didn’t know that was happening at all yesterday…"

    show lloyd worry2 at p8_2
    voice audio.lloyd_v_agree2c1
    l "Yeah… That was a huge decision to make, and honestly Sir Goro made the right call."

    show darius explain2 at p8_1
    voice audio.darius_v_think1a1
    d "Rebuilding other branches is a life’s worth of work."

    show jin worry2 at p8_8
    voice audio.jin_v_yeah2a
    j "Y-Yeah… Even this project takes so much time and effort to make happen…"

    show emilia explain3 at p8_7
    voice audio.emilia_v_conj1c1
    e "At first I was baffled too, but hearing just how big of an undertaking it was… It might be too much for a small group of people like us…"

    show goro worry3 at p8_5
    voice audio.goro_v_glad1a
    g "I’m glad you all understand… "
    g "Expanding the camp we have right now is manageable, but opening another branch is a totally different story."
    g "I thought it would be best if we concentrated our efforts and made one perfect Camp Buddy."

    show goro worry2 at p8_5
    voice audio.goro_v_but1a
    g "But I still would like to apologize for not consulting all of you first…"

    hide aiden2_autumn
    hide aiden2 talk5
    show aiden_autumn at p8_3
    show aiden comp6 at p8_3
    hide lloyd_winter
    hide lloyd worry2
    show lloyd_winter at p8_2
    show lloyd worry2 at p8_2
    voice audio.aiden_v_psh1a
    a "Psssh, It’s fine Gramps! You’re the president, so we leave the hard choices up to you!"

    show goro explain2 at p8_5
    voice audio.goro_v_conj5a
    g "That may be so, but I value all of your opinions. Yoshinori and I are leading this place, but all of you are what make it happen."
    g "Thank you again for all of your understanding, and also for bearing with me while I was gone."

    show aiden excited3 at p8_3
    voice audio.aiden_v_yeah2a1
    a "Oh yeah! That’s even more important than all this – what the heck were you doing?!"
    a "And why is there a sweet bike parked by your office all of a sudden?!"

    show lloyd shock6 at p8_2
    voice audio.lloyd_v_agree4b1
    l "Oh yeaaaah, where did that come from?!"

    show darius happy1 at p8_1
    voice audio.darius_v_amazed3
    d "It looks dope."

    hide goro_autumn
    hide goro_ring1
    hide goro explain2
    show goro2_autumn at p8_5
    show goro2 think2 at p8_5
    voice audio.goro_v_ah1c
    g "Ah… well, I’m sure you all remember that I mentioned months ago that I was in a biker’s club during my youth…"

    show emilia panic6 at p8_7
    voice audio.emilia_v_what4a
    e "WHAT?! "

    show jin explain2 at p8_8
    voice audio.jin_v_conj1c1
    j "I-It’s true, Emilia… Sir Goro was the gang leader too…"

    show emilia shock2 at p8_7
    voice audio.emilia_v_surprised2a2
    e "Th-This is news to me!"

    show aiden play3 at p8_3
    voice audio.aiden_v_so2
    a "So, is that the same bike you rode back then? It looks pretty vintage!"

    hide goro2_autumn
    hide goro2 think2
    show goro_autumn at p8_5
    show goro_ring1 at p8_5
    show goro happy2 at p8_5
    voice audio.goro_v_agree1a1
    g "Yes, it is. I had it restored and tuned up yesterday… which explains why I was gone."

    show aiden play2 at p8_3
    voice audio.aiden_v_swear2a1
    a "Damn… All of a sudden, you’re the coolest guy in the camp, Gramps…"

    show lloyd excited3 at p8_2
    voice audio.lloyd_v_shock1b1
    l "Ooh, ooh! Can you give me a ride one day?!"

    show darius happy2 at p8_1
    voice audio.darius_v_agree4
    d "Me too."

    hide goro_autumn
    hide goro_ring1
    hide goro happy2
    show goro2_autumn at p8_5
    show goro2 confused3 at p8_5
    voice audio.goro_v_think3
    g "Uhh… Sure. Only one at a time though."

    hide jin_autumn
    hide jin_glasses
    hide jin explain2
    show jin2_autumn at p8_8
    show jin2_glasses at p8_8
    show jin2 perv5 at p8_8
    voice audio.jin_v_fudan4a1
    j "I want to ride Sir Goro too…"

    show yuri laugh1 at p8_6
    voice audio.yuri_v_laugh1a3
    yu "Hihihi~ Looks like everyone’s interested in your new bike, Dad~"

    show yoshi laugh2 at p8_4
    voice audio.yoshi_v_laugh1
    yo "Haha, maybe he’ll have to lead a new bike club soon."

    show emilia angry2 at p8_7
    voice audio.emilia_v_wait1a1
    e "Wait a minute, Yoshinori!"

    hide yoshi_autumn
    hide yoshi_ring1
    hide yoshi laugh2
    show yoshi2_autumn at p8_4
    show yoshi2_ring1 at p8_4
    show yoshi2 confused2 at p8_4
    voice audio.yoshi_v_what3
    yo "Wh-Wha…?"

    hide goro2_autumn
    hide goro2 confused3
    show goro_autumn at p8_5
    show goro_ring1 at p8_5
    show goro shock1 at p8_5
    show emilia angry3 at p8_7
    voice audio.emilia_v_request3
    e "Show me your hand!"

    show yoshi2 confused5 at p8_4
    voice audio.yoshi_v_uh1a
    yo "Umm… Okay?"

    show emilia scared3 at p8_7
    voice audio.emilia_v_worry1
    e "NO WAY…! That’s a real diamond!! Embedded on a titanium band too!"

    show yoshi2 shy5 at p8_4
    voice audio.yoshi_v_really1
    yo "Y-You noticed?"

    show emilia rage4 at p8_7
    voice audio.emilia_v_agree1c1
    e "Duh! I can sense bougie jewelry from a mile away! Real diamonds have a distinct sparkle to them that really catches the eye!"
    e "Looks good on you, though~ Since when did you become interested in— "

    show emilia irked2 at p8_7
    voice audio.emilia_v_wait1c
    e "Wait a minute… YOU DIDN’T—"

    show emilia scared4 at p8_7
    voice audio.emilia_v_gasp1
    e "SIR GORO!!!" with vpunch

    hide goro_autumn
    hide goro_ring1
    hide goro shock1
    show goro2_autumn at p8_5
    show goro2 comp5 at p8_5
    voice audio.goro_v_heh1a
    g "Cat’s out of the bag, I guess…"

    show yuri confused2 at p8_6
    voice audio.yuri_v_worry1b
    yu "Wh-What’s going on?"

    hide jin2_autumn
    hide jin2_glasses
    hide jin2 perv5
    show jin_autumn at p8_8
    show jin_glasses at p8_8
    show jin think2 at p8_8
    voice audio.jin_v_think2a1
    j "Yuri… S-Sir Goro’s wearing the same ring…"

    show yuri confused2 at p8_6
    voice audio.yuri_v_so1b
    yu "And?"

    show aiden shock3 at p8_3
    voice audio.aiden_v_shock3a2
    a "HOLY CRAP! YOSHI AND GRAMPS ARE ENGAGED?!" with vpunch

    show yoshi2 comp6 at p8_4
    voice audio.yoshi_v_laugh6
    yo "Ahehe… Surprise?"

    show lloyd shock3 at p8_2
    show darius shock3 at p8_1
    show aiden shock6 at p8_3
    show yuri shock5 at p8_6
    show emilia scared3 at p8_7
    hide jin_autumn
    hide jin_glasses
    hide jin think2
    show jin2_autumn at p8_8
    show jin2_glasses at p8_8
    show jin2 fudan3 at p8_8
    all "WHAT?!" with vpunch

    show goro2 play3 at p8_5
    voice audio.goro_v_laugh1a1
    g "Hehe… I did it, everyone. You can call him “Mr. Nomoru” too from now on."

    show yoshi2 annoy3 at p8_4
    voice audio.yoshi_v_hey3
    yo "H-Hey… We haven’t decided on that yet…"

    show aiden amazed2 at p8_3
    voice audio.aiden_v_amazed1a2
    a "What the heck, that’s awesome news! Congrats! I’m super happy for you two!"

    show lloyd comp5 at p8_2
    voice audio.lloyd_v_aww1b1
    l "Awwwww~ I’m so jelly, I wanna get married toooooo~"

    show darius tease2 at p8_1
    voice audio.darius_v_wait1a
    d "Soon TM."

    show yuri panic3 at p8_6
    voice audio.yuri_v_wait1d1
    yu "Wait, wait, wait, wait, WAIT! This has got to be a joke, right?!"
    yu "S-Since when have you two been together?!"

    hide jin2_autumn
    hide jin2_glasses
    hide jin2 fudan3
    show jin_autumn at p8_8
    show jin_glasses at p8_8
    show jin shock2 at p8_8
    voice audio.jin_v_really2a
    j "Y-You didn’t know, Yuri…?"

    show yuri rage1 at p8_6
    voice audio.yuri_v_what5a
    yu "What do you mean ‘you didn’t know’?! "

    show lloyd talk2 at p8_2
    voice audio.lloyd_v_rush1b1
    l "They started dating back at the hotel, Yuri! I thought that was obvious!"

    show yuri rage4 at p8_6
    voice audio.yuri_v_angry2a2
    yu "EXCUSE ME?!"
    yu "So, you’re telling me, this whole time we’ve all been hanging out, everyone knew, except for me?!"

    show emilia annoy5 at p8_7
    voice audio.emilia_v_request2b
    e "Are you serious? They’ve been literally inseparable since we started the project, wasn’t that enough of a sign for you?"

    show darius comp2 at p8_1
    voice audio.darius_v_question2a2
    d "You not knowing is more shocking news than the engagement, honestly."

    show yuri rage3 at p8_6
    voice audio.yuri_v_angry4a1
    yu "I don’t get it! How did this slip by my radar?! "

    show yoshi2 shy6 at p8_4
    voice audio.yoshi_v_well3
    yo "W-Well maybe because Goro is your Dad…?"

    hide aiden_autumn
    hide aiden amazed2
    show aiden2_autumn at p8_3
    show aiden2 tease5 at p8_3
    hide lloyd_winter
    hide lloyd talk2
    show lloyd_winter at p8_2
    show lloyd talk2 at p8_2
    voice audio.aiden_v_wait2b2
    a "Hold that thought, Yoshi… Does this mean you’re also gonna be… Yuri’s dad?"

    show yuri rage4 at p8_6
    voice audio.yuri_v_what5b
    yu "WHAAAAAAAT?!! " with vpunch

    show lloyd laugh4 at p8_2
    voice audio.lloyd_v_laugh1b1
    l "Hahaha! Your reaction is priceless!!"

    show darius play2 at p8_1
    voice audio.darius_v_naughty1a
    d "Daddy Yoshi."

    hide aiden2_autumn
    hide aiden2 tease5
    show aiden_autumn at p8_3
    show aiden tease1 at p8_3
    hide lloyd_winter
    hide lloyd laugh4
    show lloyd_winter at p8_2
    show lloyd laugh4 at p8_2
    voice audio.aiden_v_oho1a
    a "So, when’s the honeymoon, Gramps?!"

    show yuri rage1 at p8_6
    voice audio.yuri_v_ugh2a
    yu "THAT IS SO GROSS!! EW, EW, EW!!"
    yu "Of all the ships to become real, why the two of you?!"

    show goro2 relief2 at p8_5
    voice audio.goro_v_well1a
    g "Well, dear. You can save your objections for our wedding. Although, it won’t really change much, haha."

    hide yuri_autumn
    hide yuri rage1
    show yuri2_autumn at p8_6
    show yuri2 scared2 at p8_6
    voice audio.yuri_v_no1c1
    yu "NOOOOOOOOOOOO!!"

    hide yuri2_autumn
    hide yuri2 scared2
    with moveoutleft

    show yoshi2 worry2 at p8_4
    voice audio.yoshi_v_uh1a
    yo "I-Is she gonna be okay…?"

    hide goro2_autumn
    hide goro2 relief2
    show goro_autumn at p8_5
    show goro_ring1 at p8_5
    show goro laugh1 at p8_5
    voice audio.goro_v_laugh2b1
    g "Hahaha, yeah. Just let her process it."

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black with fade
    yo "{i}Everyone kept asking Goro and I questions as we ate our meal… We had to tell the whole story of how it happened for them to be satisfied.{/i}"
    yo "{i}Goro looked a little embarrassed, but happy too… He finally seems truly content to be taking this new step in his life.{/i}"
    yo "{i}Eventually, we finished up and everyone headed to work on their separate departments.{/i}"
    scene cg black
    hide screen location
    hide screen timeline
    hide screen quick_menu
    $quick_menu = False
    with fade
    $ renpy.pause (2.0, hard=True)

    if sq_aiden >= 2:
        $aiden_ending = True
        $ location = location_kitchen
        show screen location
        show screen timeline
        show screen quick_menu
        $quick_menu = True
        scene bg_kitchen_winter_day with fade
        play music go_with_the_flow loop

        show yoshi_autumn at left
        show yoshi_ring1 at left
        show yoshi norm1 at left
        show goro_autumn at center
        show goro_ring1 at center
        show goro talk3 at center
        show aiden_apron at right
        show aiden norm2 at right
        voice audio.goro_vsg25_line1
        g "Here’s the last of the dishes, Aiden."

        show aiden happy2 at right
        voice audio.aiden_vsg25_line1
        a "Oh, hey there you two! Thanks for bringing them and helping clean up!"

        show yoshi happy1 at left
        voice audio.yoshi_vsg25_line1
        yo "No problem, Aiden! "

        hide goro_autumn
        hide goro_ring1
        hide goro talk3
        show goro2_autumn at center
        show goro2 sigh4 at center
        voice audio.goro_vsg25_line2
        g "*sigh* I see you’re already in your usual attire."

        show aiden relief2 at right
        voice audio.aiden_vsg25_line2
        a "Of course! I got a lot of work to do in here, so it’s gonna get hot!"

        voice audio.aiden_vsg25_line3
        a "Plus, I gotta keep the fanservice going if I wanna end up with a relationship like you two!"

        hide yoshi_autumn
        hide yoshi_ring1
        hide yoshi happy1
        show yoshi2_autumn at left
        show yoshi2_ring1 at left
        show yoshi2 annoy2 at left
        voice audio.yoshi_vsg25_line2
        yo "I-I don’t think that’s how we got started, Aiden…"

        show aiden laugh1 at right
        voice audio.aiden_vsg25_line4
        a "Haha, I know! But I seriously am happy for you two!"

        hide aiden_apron
        hide aiden laugh1
        show aiden2_apron at right
        show aiden2 excited3 at right
        voice audio.aiden_vsg25_line5
        a "Seeing how you’ve gotten so close over the last few months, all leading up to a proposal… wow!"

        voice audio.aiden_vsg25_line6
        a "You must’ve really flipped a switch in Gramps, Yoshi, ’cause I can’t imagine him doing a romantic thing like that, haha!"

        show goro2 disappoint2 at center
        voice audio.goro_vsg25_line3
        g "*ehem* I’m plenty capable of romance, you know."

        hide aiden2_apron
        hide aiden2 excited3
        show aiden_apron at right
        show aiden play2 at right
        voice audio.aiden_vsg25_line7
        a "Obviously! Otherwise, there wouldn’t be a ring on Yoshi’s finger~"

        voice audio.aiden_vsg25_line8
        a "Now I wanna get fingered too!"

        show yoshi2 awkward4 at left
        voice audio.yoshi_vsg25_line3
        yo "I-I think that means something else."

        show aiden tease1 at right
        voice audio.aiden_vsg25_line9
        a "No. I know exactly what I meant~ If you need a side-hoe, you know where to find me!"

        if crack_sx == True:
            show goro2 annoy2 at center
            voice audio.goro_vsg25_line4a
            g "No chance, kiddo."
        else:
            show goro2 annoy2 at center
            voice audio.goro_vsg25_line4b
            g "That was a one-time deal, kiddo."

        hide aiden_apron
        hide aiden play2
        show aiden2_apron at right
        show aiden2 comp5 at right
        voice audio.aiden_vsg25_line10
        a "Aww… Maybe on a different route."

        hide aiden2_apron
        hide aiden2 comp5
        show aiden_apron at right
        show aiden bold2 at right
        voice audio.aiden_vsg25_line11
        a "Now if you’ll excuse me, I gotta get lunch started ’cause I got hungry workers to feed!"

        voice audio.aiden_vsg25_line12
        a "You two lovebirds have a good working day~   "

        hide aiden_apron
        hide aiden bold2
        with dissolve

        show goro2 sigh4 at center
        voice audio.goro_vsg25_line5
        g "*sigh* He’s as insufferable as ever."

        hide yoshi2_autumn
        hide yoshi2_ring1
        hide yoshi2 awkward4
        show yoshi_autumn at left
        show yoshi_ring1 at left
        show yoshi laugh1 at left
        voice audio.yoshi_vsg25_line4
        yo "Haha, but I think he’s really happy for us!"

        hide goro2_autumn
        hide goro2 sigh4
        show goro_autumn at center
        show goro_ring1 at center
        show goro comp2 at center
        voice audio.goro_vsg25_line6
        g "True, and Aiden has always been a big supporter of everyone here. "

        voice audio.goro_vsg25_line7
        g "But that’s enough chitchat. Come on, let’s get to work!"

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

    if sq_jin >= 2:
        $jin_ending = True
        $ location = location_messhall
        show screen location
        show screen timeline
        show screen quick_menu
        $quick_menu = True
        scene bg_messhall_winter_day with fade
        play music buddy_oath_casual loop

        show yoshi_autumn at left2
        show yoshi_ring1 at left2
        show yoshi norm1 at left2
        show goro_autumn at right2
        show goro_ring1 at right2
        show goro talk3 at right2
        voice audio.goro_vsg26_line1
        g "Alright, I suppose we should get started for the day as well, Yoshinori."

        show yoshi happy1 at left2
        voice audio.yoshi_vsg26_line1
        yo "Sure thing!"

        show yoshi_autumn at p5_1
        show yoshi_ring1 at p5_1
        show yoshi norm1 at p5_1
        show goro_autumn at p5_2
        show goro_ring1 at p5_2
        show goro norm1 at p5_2
        with move

        show jin_autumn at p5_5
        show jin_glasses at p5_5
        show jin talk5 at p5_5
        with dissolve

        voice audio.jin_vsg26_line1
        j "A-Ah, wait you two!"

        show yoshi_autumn at left
        show yoshi_ring1 at left
        show yoshi talk3 at left
        show goro_autumn at center
        show goro_ring1 at center
        show goro norm1 at center
        show jin_autumn at right
        show jin_glasses at right
        show jin talk5 at right
        with move

        voice audio.yoshi_vsg26_line2
        yo "Oh, Jin…! Did you need anything?"

        show jin happy2 at right
        voice audio.jin_vsg26_line2
        j "A-Actually, yes! I was so caught up in you guys’ news that I didn’t remember, but I wanted to show you both something…"

        show goro confused2 at center
        voice audio.goro_vsg26_line2
        g "What is it?"

        show jin laugh2 at right
        voice audio.jin_vsg26_line3
        j "…I finished the blog project, sir!  Please check it out!"

        show cg_fade at truecenter
        show fx8g at fx_pos
        with dissolve

        voice audio.yoshi_vsa24_line4
        yo "Wow! This is really amazing, Jin! It’s so nostalgic to see ourselves on the website like that!"

        voice audio.goro_vsg26_line3
        g "I’m impressed. This looks like it took a lot of work."

        voice audio.jin_vsa24_line5
        j "Thanks, I’m really proud of it! I can’t wait to see what people say about it."

        voice audio.jin_vsa24_line6
        j "Yuri was super excited to see her journal digitized so she can view it anytime she wants."

        hide cg_fade
        hide fx8g
        with dissolve

        show goro2 norm1 at center
        show yoshi norm1 at left
        show jin bold2 at right
        voice audio.jin_vsa24_line7
        j "If you guys want to check it out more and explore each page, I’d be happy to give you a separate soft copy!"

        hide goro_autumn
        hide goro_ring1
        hide goro norm1
        show goro2_autumn at center
        show goro2 happy2 at center
        voice audio.goro_vsg26_line4
        g "You really went the extra mile for this, Jin. I hope it didn’t affect your other work too much."

        show jin relief2 at right
        voice audio.jin_vsa24_line8
        j "Not at all! Yoshinori was helping me out this whole time, and it’s more of a side project I did for fun!"

        hide goro2_autumn
        hide goro2 happy2
        show goro_autumn at center
        show goro_ring1 at center
        show goro relief2 at center
        voice audio.goro_vsg26_line5
        g "That’s good. I do remember helping out a few times as well… It was enjoyable."

        show jin comp2 at right
        voice audio.jin_vsa24_line9
        j "I guess in a way, this project helped me get to know you all better, and it made me feel like I was part of all the amazing memories you shared."

        voice audio.jin_vsa24_line10
        j "Working with you guys the last few months, I got to make amazing memories myself with all of you too."

        hide yoshi_autumn
        hide yoshi_ring1
        hide yoshi norm1
        show yoshi2_autumn at left
        show yoshi2_ring1 at left
        show yoshi2 comp2 at left
        voice audio.yoshi_vsg26_line3
        yo "Aww, Jin…"

        show jin comp6 at right
        voice audio.jin_vsa24_line11
        j "I… I guess that’s another thing that I learned here – how to make friends."

        voice audio.jin_vsa24_line12
        j "I feel bad about being a shut-in for so long… I can’t help but feel like I’ve missed out on a lot."

        show jin sigh3 at right
        voice audio.jin_vsa24_line13
        j "I’ve gotten so used to having people around me just come and go, and I always found it easier to not deal with anyone but myself."

        voice audio.jin_vsa24_line14
        j "I wish I wasn’t such an introvert..."

        hide yoshi2_autumn
        hide yoshi2_ring1
        hide yoshi2 comp2
        show yoshi_autumn at left
        show yoshi_ring1 at left
        show yoshi comp3 at left
        voice audio.yoshi_vsa24_line5
        yo "But it’s part of who you are, Jin! "

        voice audio.yoshi_vsa24_line6
        yo "And besides, you pushed yourself out of your comfort zone knowing you’d have to deal with a lot of people when you signed up to work with us. "

        show goro comp2 at center
        voice audio.goro_vsg26_line6
        g "That’s not an easy thing to do, either. "

        show jin comp4 at right
        voice audio.jin_vsa24_line15
        j "Yeah… I guess I shouldn’t think of it as a bad thing."

        voice audio.jin_vsa24_line16
        j "I-It’s just… I’ve never had a place where I can express who I am and be accepted for the things I thought were bad about myself."

        show jin worry2 at right
        voice audio.jin_vsa24_line17
        j "And to think we only have a few months left ’til the project ends… I’ll be losing the closest thing I have to a ‘social circle’."

        voice audio.jin_vsa24_line18
        j "Just the thought of leaving Camp Buddy is so dreadful…"

        show goro explain2 at center
        voice audio.goro_vsg26_line7
        g "I understand, Jin. It’s already hard as a leader to watch people leave, especially when you’ve grown fond of them."

        voice audio.goro_vsg26_line8
        g "It’s just a thought, but have you considered joining our staff?"

        show jin shock2 at right
        voice audio.jin_vsa24_line20
        j "Wh-What…? L-Like, work here permanently?! "

        show yoshi shock3 at left
        voice audio.yoshi_vsg26_line4
        yo "W-Whoa, are you offering Jin a job, sir?!"

        hide goro_autumn
        hide goro_ring1
        hide goro explain2
        show goro2_autumn at center
        show goro2 play2 at center
        voice audio.goro_vsg26_line9
        g "I am. Jin here has done excellent work for us over the course of the project, and I’d hate to lose him. "

        show jin think2 at right
        voice audio.jin_vsa24_line21
        j "Umm… I guess someone would probably need to stay to maintain most of the tech… "

        show goro2 play5 at center
        voice audio.goro_vsg26_line10
        g "Exactly, and there’s no one more suited for the job than the person who set it up."

        show jin explain3 at right
        voice audio.jin_vsa24_line22
        j "I… might think about it. "

        show goro2 tease3 at center
        voice audio.goro_vsg26_line11
        g "Well, I leave it up to you. But it would give me pleasure if you’d submit to me."

        hide jin_autumn
        hide jin_glasses
        hide jin explain3
        show jin2_autumn at right
        show jin2_glasses at right
        show jin2 fudan2 at right
        voice audio.jin_vsg26_line4
        j "Wh-What…?"

        show yoshi bold2 at left
        voice audio.yoshi_vsg26_line5
        yo "A-Ah, I think he’s just saying that we’re willing to receive you, Jin!"

        show jin2 dizzy2 at right
        voice audio.jin_vsg26_line5
        j "Guuuuuh… Maybe I should stay after all…"

        hide yoshi_autumn
        hide yoshi_ring1
        hide yoshi bold2
        show yoshi2_autumn at left
        show yoshi2_ring1 at left
        show yoshi2 comp6 at left
        voice audio.yoshi_vsg26_line6
        yo "Ahehe, I think he’s misunderstanding us, sir…"

        show goro2 tease5 at center
        voice audio.goro_vsg26_line12
        g "Heh, but that’s part of the fun."

        show yoshi2 comp3 at left
        voice audio.yoshi_vsg26_line7
        yo "M-Maybe we should go before we give him another nosebleed."

        show goro2 laugh1 at center
        voice audio.goro_vsg26_line13
        g "Haha, alright. Just let me know in the future, Jin!"

        hide jin2_autumn
        hide jin2_glasses
        hide jin2 dizzy2
        show jin_autumn at right
        show jin_glasses at right
        show jin shock3 at right
        voice audio.jin_vsg26_line6
        j "Y-Yes sir…!"

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

    if lloyd_ending == True:
        $ location = location_site
        show screen location
        show screen timeline
        show screen quick_menu
        $quick_menu = True
        scene bg_site7_winter_day with fade
        play music sunset_stroll_winter loop

        show yoshi_winter2 at p4_1
        show yoshi_ring1 at p4_1
        show yoshi happy1 at p4_1
        show goro_winter2 at p4_2
        show goro_ring1 at p4_2
        show goro norm2 at p4_2
        show darius_workw at p4_3
        show darius_goggles2 at p4_3
        show darius norm1 at p4_3
        show lloyd_work2 at p4_4
        show lloyd norm1 at p4_4
        voice audio.yoshi_vsg27_line1
        yo "Hey there, you two! "

        show lloyd happy1 at p4_4
        voice audio.lloyd_vsg27_line1
        l "Oh, heya Yoshi and Sir Goro! What brings you here?"

        show goro talk3 at p4_2
        voice audio.goro_vsg27_line1
        g "Yoshinori was telling me we had a delivery yesterday – I just wanted to check it out."

        show lloyd bold2 at p4_4
        voice audio.lloyd_vsg27_line2
        l "Sure thing, sir! I’ll show you!"

        show darius talk2 at p4_3
        voice audio.darius_vsg27_line1
        d "I’m gonna get started on the other work."

        show lloyd play3 at p4_4
        voice audio.lloyd_vsg27_line3
        l "Sure thing, babe. Love ya!"

        show darius_blush1 at p4_3
        show darius shy1 at p4_3
        d "..."

        show lloyd tease2 at p4_4
        voice audio.lloyd_vsg27_line4
        l "EHEM, what do you sayyyyy?"

        show darius shy4 at p4_3
        voice audio.darius_vsg27_line2
        d "L-Love you too…"

        show lloyd_work2 at p4_3
        show lloyd smile4 at p4_3
        with move

        show lloyd_work2 at p4_4
        show lloyd smile4 at p4_4
        with move

        voice audio.lloyd_vsg27_line5
        l "Mwahh!"

        show lloyd tease3 at p4_4
        voice audio.lloyd_vsg27_line6
        l "Thank youuuuu~"

        show darius comp2 at p4_3
        voice audio.darius_vsg27_line3
        d "Y-You’re welcome…"

        hide darius_workw
        hide darius_goggles2
        hide darius_blush1
        hide darius comp2
        with dissolve

        show yoshi_winter2 at left
        show yoshi_ring1 at left
        show yoshi shock2 at left
        show goro_winter2 at center
        show goro_ring1 at center
        show goro shock1 at center
        show lloyd_work2 at right
        show lloyd smile4 at right
        with move

        voice audio.yoshi_vsg27_line2
        yo "Wh-Whoa! I’ve never seen you two like that before, Lloyd!"

        hide goro_winter2
        hide goro_ring1
        hide goro shock1
        show goro2_winter2 at center
        show goro2 play2 at center
        voice audio.goro_vsg27_line2
        g "Looks like we weren’t the only couple around here, huh?"

        show lloyd happy2 at right
        voice audio.lloyd_vsg27_line7
        l "Oh, it’s actually new! After we played that game the other day, Dar and I had a serious talk."

        voice audio.lloyd_vsg27_line8
        l "I was tired of us not having a label and being all secretive of our relationship around everyone."

        show lloyd pout4 at right
        voice audio.lloyd_vsg27_line9
        l "I mean, come on! We’ve been together for 9 years now! What point is there in hiding?"

        hide goro2_winter2
        hide goro2 play2
        show goro_winter2 at center
        show goro_ring1 at center
        show goro sigh4 at center
        voice audio.goro_vsg27_line3
        g "I know exactly what that’s like..."

        show lloyd talk2 at right
        voice audio.lloyd_vsg27_line10
        l "Well, it turns out that Dar felt the same way, and all we had to do was talk about it!"

        show goro comp2 at center
        voice audio.goro_vsg27_line4
        g "That’s really great to hear, Lloyd. I’m happy to see you two finally working things out together."

        show lloyd comp3 at right
        voice audio.lloyd_vsg27_line11
        l "Well, I was actually inspired by you, sir!"

        hide goro_winter2
        hide goro_ring1
        hide goro comp2
        show goro2_winter2 at center
        show goro2 confused2 at center
        voice audio.goro_vsg27_line5
        g "Me? How so?"

        show lloyd bold2 at right
        voice audio.lloyd_vsg27_line12
        l "Ever since we came back here, I’ve seen how you’ve been getting closer to Yoshi, even including the proposal!"

        voice audio.lloyd_vsg27_line13
        l "I really admire all the confidence and guts it took to do that, and I figured I needed to start having some of that myself!"

        show goro2 shy6 at center
        voice audio.goro_vsg27_line6
        g "I-I see… I didn’t realize I’d had such an impact on you, Lloyd."

        show lloyd laugh2 at right
        voice audio.lloyd_vsg27_line14
        l "Haha, what can I say? You’ve always been my role model after all!"

        show goro2_blush1 at center
        show goro2 shy5 at center
        g "..."

        hide yoshi_winter2
        hide yoshi_ring1
        hide yoshi shock2
        show yoshi2_winter at left
        show yoshi2_ring1 at left
        show yoshi2 comp3 at left
        voice audio.yoshi_vsg27_line3
        yo "Aww, I think you embarrassed him, Lloyd, hehe…"

        show goro2 shy2 at center
        voice audio.goro_vsg27_line7
        g "N-No, I was just thinking about it for a moment…!"

        hide goro2_blush1
        show goro2 shy4 at center
        voice audio.goro_vsg27_line8
        g "A-And in any case, I’m just happy to be of service."

        voice audio.goro_vsg27_line9
        g "Now, should we go and see about those materials?"

        show lloyd talk4 at right
        voice audio.lloyd_vsg27_line15
        l "Oh, right! I almost forgot haha!"

        voice audio.lloyd_vsg27_line16
        l "Come on, they’re over here!"

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

    if sq_yuri >= 2:
        $yuri_ending = True
        $ location = location_office
        show screen location
        show screen timeline
        show screen quick_menu
        $quick_menu = True
        scene bg_office_winter_day with fade
        play music old_familiar_home loop

        play sound sfx_doorknock
        $ renpy.pause (1.0, hard=True)
        show yoshi_autumn at left
        show yoshi_ring1 at left
        show yoshi norm1 at left
        show goro_autumn at right
        show goro_ring1 at right
        show goro talk3 at right
        voice audio.goro_vsg28_line1
        g "Come in."

        show goro_autumn at center
        show goro_ring1 at center
        show goro norm1 at center
        with move

        show yuri_winter at right
        show yuri talk2 at right
        with dissolve

        voice audio.yuri_vsg28_line1
        yu "Oh…! Hey there, Dad! "

        hide goro_autumn
        hide goro_ring1
        hide goro norm1
        show goro2_autumn at center
        show goro2 play2 at center
        voice audio.goro_vsg28_line2
        g "Which one?"

        show yuri rage1 at right
        voice audio.yuri_vsg28_line2
        yu "ARGHHH… Come ooon… Don’t do this to meee…."

        show goro2 laugh1 at center
        voice audio.goro_vsg28_line3
        g "Hahaha."

        show yoshi confused2 at left
        voice audio.yoshi_vsg28_line1
        yo "What brings you here, Yuri?"

        show yuri talk2 at right
        voice audio.yuri_vsg28_line3
        yu "I just had to drop off a report from the workers! I’ll be heading out to work with Emilia soon."

        voice audio.yuri_vsg28_line4
        yu "Buuuut since I’m here! I wanna talk to you both!"

        hide yoshi_autumn
        hide yoshi_ring1
        hide yoshi confused2
        show yoshi2_autumn at left
        show yoshi2_ring1 at left
        show yoshi2 confused5 at left
        voice audio.yoshi_vsg28_line2
        yo "O-Oh, about what?"

        show yuri rage3 at right
        voice audio.yuri_vsg28_line5
        yu "Eughhhhhh… It pains me to say it, but… I am actually really happy for you two."

        show goro2 comp2 at center
        voice audio.goro_vsg28_line4
        g "Th-That doesn’t sound very happy, dear…"

        show yuri angry2 at right
        voice audio.yuri_vsg28_line6
        yu "I mean it! It’s about time that you had someone who can take care of you properly, Dad."

        show yuri comp2 at right
        voice audio.yuri_vsg28_line7
        yu "And honestly, I can’t think of anyone better than Yoshi here."

        voice audio.yuri_vsg28_line8
        yu "He’s been the obvious pick all this time, I guess I just didn’t see it for some reason."

        show yoshi2 comp3 at left
        voice audio.yoshi_vsg28_line3
        yo "Th-Thank you, Yuri. I’m sorry that we didn’t tell you sooner, though."

        show yuri sigh4 at right
        voice audio.yuri_vsg28_line9
        yu "Honestly, it’s not you guys’ fault. I should’ve noticed the signs…"

        voice audio.yuri_vsg28_line10
        yu "And I’m usually so good at that! What’s wrong with me?!"

        hide goro2_autumn
        hide goro2 comp2
        show goro_autumn at center
        show goro_ring1 at center
        show goro happy2 at center
        voice audio.goro_vsg28_line5
        g "Haha, I think this is just a bit of a different situation, dear."

        show yuri comp4 at right
        voice audio.yuri_vsg28_line11
        yu "Maybe, but either way, I’m grateful for Yoshi. Now I don’t have to worry about you as much, Dad!"

        voice audio.yuri_vsg28_line12
        yu "I can finally fully focus on myself~ There’s so much BL I have to catch up on!"

        show yoshi2 sigh4 at left
        voice audio.yoshi_vsg28_line4
        yo "*sigh* I’m not surprised that’s the first thought you had…"

        show yuri pout1 at right
        voice audio.yuri_vsg28_line13
        yu "Hmph, it actually wasn’t! I’ll have you know you two almost ruined that for me too!"

        show yuri pain6 at right
        voice audio.yuri_vsg28_line14
        yu "The thought of you two… *shivers*"

        voice audio.yuri_vsg28_line15
        yu "I can’t even think about it!"

        show yoshi2_autumn at p4_1
        show yoshi2_ring1 at p4_1
        show yoshi2 shock1 at p4_1
        show goro_autumn at p4_2
        show goro_ring1 at p4_2
        show goro norm1 at p4_2
        show yuri_winter at p4_3
        show yuri shock1 at p4_3
        with move

        show emilia_winter at p4_4
        show emilia angry2 at p4_4
        with dissolve

        voice audio.emilia_vsg28_line1
        e "Yuri! What the hell are you doing?! I’ve been waiting for half an hour!"

        show yuri talk3 at p4_3
        voice audio.yuri_vsg28_line16
        yu "Oh, thank god you’re here Emilia. I’m losing it with Dad and Yoshi…!"

        show emilia evil3 at p4_4
        voice audio.emilia_vsg28_line2
        e "Oh~? Don’t you mean with ‘Dad’ and ‘Dad’?"

        show yuri rage4 at p4_3
        voice audio.yuri_vsg28_line17
        yu "BLECH! WOULD EVERYONE STOP SAYING THAT?!"

        show emilia play5 at p4_4
        voice audio.emilia_vsg28_line3
        e "It’s true though~ When are you gonna make her call you that, Yoshi?"

        show yoshi2 awkward4 at p4_1
        voice audio.yoshi_vsg28_line5
        yo "I-I, uh—"

        show yuri rage1 at p4_3
        voice audio.yuri_vsg28_line18
        yu "NEVER, THAT’S WHEN!"

        hide yuri_winter
        hide yuri rage1
        with moveoutright

        show emilia angry3 at p4_4
        voice audio.emilia_vsg28_line4
        e "H-Hey! Where do you think you’re going?!"

        hide emilia_winter
        hide emilia angry3
        with moveoutright

        show yoshi2 comp6 at p4_1
        voice audio.yoshi_vsg28_line6
        yo "Ahehe… Yuri is really having a hard time with this, huh?"

        hide goro_autumn
        hide goro_ring1
        hide goro norm1
        show goro2_autumn at p4_2
        show goro2 laugh1 at p4_2
        voice audio.goro_vsg28_line6
        g "Haha, I never thought I’d see the day that she wouldn’t enjoy shipping someone, as she calls it."

        voice audio.goro_vsg28_line7
        g "But I suppose as her father, it is different."

        show yoshi2 shy5 at p4_1
        voice audio.yoshi_vsg28_line7
        yo "Y-Yeah… I can’t even think of her as a daughter… It’s too strange."

        show goro2 annoy2 at p4_2
        voice audio.goro_vsg28_line8
        g "It even feels weird with you saying it."

        voice audio.goro_vsg28_line9
        g "Now come on, let’s finish up work so we can wrap up for today."

        hide yoshi2_autumn
        hide yoshi2_ring1
        hide yoshi2 shy5
        show yoshi_autumn at p4_1
        show yoshi_ring1 at p4_1
        show yoshi happy1 at p4_1
        voice audio.yoshi_vsg28_line8
        yo "Right!"

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

    $ time_transition_day_to_sunset_winter2()
    $ location = location_gororoom
    $ time = timeline_timesunset
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_gororoom_winter_sunset with fade
    play music old_familiar_home_slow loop

    show yoshi_sleep at left2
    show yoshi_ring1 at left2
    show yoshi comp1 at left2
    show goro_sleep at right2
    show goro_ring1 at right2
    show goro relief2 at right2
    voice audio.goro_v_relief1a
    g "Ahhh… A nice hot shower after a long day of work really takes the edge off."

    show yoshi relief2 at left2
    voice audio.yoshi_v_yeah1
    yo "Yeah. It’s nice to take a short break to rest our backs and breathe a little."

    hide goro_sleep
    hide goro_ring1
    hide goro relief2
    show goro2_sleep at right2
    show goro2 play2 at right2
    voice audio.goro_v_heh1a
    g "Heh, don’t get too settled in, though. We still have to deliver our daily report to Mr. Clermont."

    show yoshi comp3 at left2
    voice audio.yoshi_v_agree1a
    yo "Ah, yes of course."

    hide goro2_sleep
    hide goro2 play2
    show goro_sleep at right2
    show goro_ring1 at right2
    show goro confused2 at right2
    voice audio.goro_v_confused1a1
    g "The next few months are looking quite full, aren’t they?"

    show yoshi talk1 at left2
    voice audio.yoshi_v_yeah2
    yo "Yeah, definitely! It’s gonna be a long winter – we’ll be working till all the snow melts outside!"
    yo "I can’t believe that when we started this project months ago, I was worried about not being able to do anything."

    hide goro_sleep
    hide goro_ring1
    hide goro confused2
    show goro2_sleep at right2
    show goro2 comp3 at right2
    voice audio.goro_v_heh1a
    g "Heh, it turned out you got more than you bargained for."

    show yoshi comp3 at left2
    voice audio.yoshi_v_sigh3a
    yo "Yeah, I couldn’t have been more wrong."
    yo "When I became a scoutmaster here I never stopped grinding, always afraid of screwing something up."

    show yoshi happy1 at left2
    voice audio.yoshi_v_but2
    yo "For the first time in years, I’m happy that Camp Buddy doesn’t have to deal with the risk of closure or damage control anymore."
    yo "It’s been nice to have some time to actually focus on ourselves, too!"

    hide goro2_sleep
    hide goro2 comp3
    show goro_sleep at right2
    show goro_ring1 at right2
    show goro relief4 at right2
    voice audio.goro_v_agree7a
    g "I agree. I’m glad we were finally able to put our pasts behind us."

    show yoshi explain4 at left2
    voice audio.yoshi_v_right9
    yo "Me too, it’s nice to know we both got some closure!"
    yo "From here on out, we can really focus on what’s ahead of us."

    hide goro_sleep
    hide goro_ring1
    hide goro relief4
    show goro2_sleep at right2
    show goro2 play3 at right2
    voice audio.goro_v_heh1a
    g "Heh, you could almost say this was a ‘scoutmaster season’.  "
    g "Our problems and struggles have changed over the years, but now we get to overcome them together."

    hide goro2_sleep
    hide goro2 play3
    show goro_sleep at right2
    show goro_ring1 at right2
    show goro bold5 at right2
    voice audio.goro_v_confident1a
    g "I’m ready to share our experiences with the next generation of scouts!"

    show yoshi bold2 at left2
    voice audio.yoshi_v_confident1
    yo "Me too!  I can’t wait to teach the scouts again! "

    show goro bold2 at right2
    voice audio.goro_v_rush1a1
    g "Then let’s make sure they have the best version of Camp Buddy to come back to!"

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg white with fade
    $ day = "85"
    $time = timeline_timeday
    scene cg8 1 with dissolve
    play music buddy_oath_acoustic loop

    voice audio.yoshi_vsa27_line1
    yo "Everyone proceeded to work for the rest of the winter, continuing where we left off with all the new goals set for us."

    voice audio.yoshi_vsa27_line2
    yo "Thankfully, the weather didn’t act up for the rest of the season, letting Lloyd, Darius, and all the workers continuously make progress on the construction."

    voice audio.yoshi_vsa27_line3
    yo "Jin was also able to finish the website and all the necessary tech integrations for the camp! "

    voice audio.yoshi_vsa27_line4
    yo "I don’t know how we would have been able to pull off all of these amazing changes if not for their expertise!"

    $ day = "86"
    $time = timeline_timesunset
    show cg8 2g with Dissolve(0.25)
    voice audio.yoshi_vsg29_line1
    yo "Meanwhile, Aiden kept up his regular maintenance duties, but this time around he had Emilia doing most of the other chores, like cleaning and laundry."

    voice audio.yoshi_vsa27_line8
    yo "She would complain as usual, but she did the job well and got it done on time!"

    $ day = "87"
    $time = timeline_timenight
    show cg8 3g with Dissolve(0.25)
    voice audio.yoshi_vsg29_line2
    yo "Goro and I kept the entire project well-managed, making sure we stayed on schedule, while Yuri assisted us and Aiden’s department on the side."

    voice audio.yoshi_vsg29_line3
    yo "I continued to learn more management skills from Goro, and soon we were both so in sync that the meetings and paperwork gave us no trouble!"

    voice audio.yoshi_vsg29_line4
    yo "In our spare time, Goro would take me out on his motorcycle to different places. We made a habit of going on dates on the weekend."

    voice audio.yoshi_vsg29_line5
    yo "Goro was brighter and happier than I’d ever seen him before – we were both looking forward to the future, with the camp and with each other!"

    $ day = "89"
    show cg8 4g with Dissolve(0.25)
    voice audio.yoshi_vsa27_line11
    yo "All in all, it was amazing to see everyone work towards a common goal, all while enjoying our time together."

    voice audio.yoshi_vsa27_line12
    yo "The days flew by, and we saw the fruits of our labor take shape as we came closer and closer to completion!"

    voice audio.yoshi_vsa27_line13
    yo "Even with all the work, we still managed to sneak in another party for the holidays!"

    voice audio.yoshi_vsa27_line14
    yo "And of all people, Yuri even suggested that we drink together! We all laughed and talked as we reminisced about old times!"

    voice audio.yoshi_vsa27_line15
    yo "We all felt like we were back at our very first term at Camp Buddy, and I wouldn’t have changed it for anything! "

    $ day = "200"
    $time = timeline_timeday
    scene entrance_transition
    voice audio.yoshi_vsa27_line16
    yo "The snow started to thaw, and with spring just around the corner, we could clearly see how much progress we made!"

    voice audio.yoshi_vsa27_line17
    yo "I can’t wait for the scouts to see how much this place has grown!"

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black
    hide screen location
    hide screen timeline
    hide screen quick_menu
    $quick_menu = False
    with fade
    $ time_transition_winter_to_spring()
    $ renpy.pause (2.0, hard=True)

    $ day = "221"
    $ season = season_spring
    $ location = location_site
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_site8_spring_day with fade
    play music brand_new_day loop
    play bgsound sfxloop_birds loop

    show emilia_autumn at p9_1
    show emilia norm1 at p9_1
    show yuri_autumn at p9_2
    show yuri norm1 at p9_2
    show aiden_autumn at p9_3
    show aiden norm1 at p9_3
    show yoshi_semiformal at p9_4
    show yoshi_ring1 at p9_4
    show yoshi norm1 at p9_4
    show goro_semiformal at p9_5
    show goro_ring1 at p9_5
    show goro happy3 at p9_5
    show william_formal at p9_6
    show william norm1 at p9_6
    show darius_autumn at p9_8
    show darius norm1 at p9_8
    show lloyd_autumn at p9_7
    show lloyd norm1 at p9_7
    show jin_autumn at p9_9
    show jin_glasses at p9_9
    show jin norm1 at p9_9
    voice audio.goro_v_praise2b1
    g "This is such a wonderful day for Camp Buddy. We’ve all been working towards this moment for so long!"
    g "Just a year ago, I couldn’t have dreamed that something like this was possible, and I have you all to thank for that."

    show goro laugh1 at p9_5
    voice audio.goro_v_glad1a
    g "This project has been a reminder of just how far we’ve all come as a team, and how much I owe each and every one of you."

    show goro happy4 at p9_5
    voice audio.goro_v_william2a
    g "I’d also like to give a special thanks to Mr. Clermont, as without him we’d never have had this opportunity to grow."

    show goro comp5 at p9_5
    voice audio.goro_v_thanks2a2
    g "Thank you again, sir, for everything you’ve done, and for being here to celebrate with us today!"

    show william comp4 at p9_6
    voice audio.william_v_comp1b
    w "It was my pleasure, Mr. Nomoru."

    show goro happy3 at p9_5
    voice audio.goro_v_conj2a1
    g "Lastly, I want to dedicate this success to the scouts. They may not be here right now, but their spirit is what allowed this place to endure."
    g "They are what makes this place worth fighting for."

    show goro bold2 at p9_5
    voice audio.goro_v_rush4b2
    g "Now, let’s all celebrate the completion of our goals!"

    show goro laugh5 at p9_5
    voice audio.goro_v_laugh1a1
    g "To Camp Buddy and to the future!"

    play sound sfx_ribboncut
    show goro grin5 at p9_5
    g "*cuts ribbon*"

    play sound sfx_applause
    $ renpy.pause (2.0, hard=True)
    show yoshi happy1 at p9_4
    voice audio.yoshi_v_guys3
    yo "Of course, this celebration wouldn’t be complete without a reward for everyone’s hard work."

    show yoshi relief2 at p9_4
    voice audio.yoshi_v_aiden3
    yo "Our wonderfully talented chef, Aiden, has prepared a reception party for our success!"
    yo "Let’s use the last of our time together as a team to remember the good memories and hard work on this project!"

    show yoshi bold2 at p9_4
    voice audio.yoshi_v_praise1
    yo "This is a truly momentous day, so eat your hearts out, and celebrate these final moments with each other!"

    play sound sfx_applause
    show aiden excited4 at p9_3
    show emilia grin1 at p9_1
    show yuri amazed1 at p9_2
    show william laugh1 at p9_6
    show lloyd laugh4 at p9_7
    show darius grin2 at p9_8
    show jin laugh2 at p9_9
    all "*cheering*"

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

    $ location = location_office
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_office_past_day with fade
    play music old_familiar_home loop
    play bgsound sfxloop_birds loop

    show goro_semiformal at left2
    show goro_ring1 at left2
    show goro relief2 at left2
    show yoshi_semiformal at right2
    show yoshi_ring1 at right2
    show yoshi norm2 at right2
    voice audio.goro_v_relief1a
    g "Whew… The ceremony was a success!"

    show yoshi shock2 at right2
    voice audio.yoshi_v_wait1
    yo "Wait… Were you nervous the whole time, Goro?"

    show goro shy6 at left2
    voice audio.goro_v_well1a
    g "Well, not exactly… I was just ecstatic about all of the things we accomplished when I delivered that speech."
    g "I guess it only now hit me that we’ve finally reached the finish line."

    show goro comp2 at left2
    voice audio.goro_v_annoyed4c
    g "I can’t believe we really made it this far."

    show yoshi comp3 at right2
    voice audio.yoshi_v_laugh1
    yo "Hehe, I really like seeing your soft side."

    show goro disappoint2 at left2
    voice audio.goro_v_ehem1a
    g "*ehem* don’t call me soft."

    show yoshi_semiformal at center
    show yoshi_ring1 at center
    show yoshi play2 at center
    with move

    voice audio.yoshi_v_well1
    yo "Well, let me at least get you out of that suit and into something better for the party."
    yo "I’m sure you’ll be able to relax there."

    show goro play2 at left2
    voice audio.goro_v_yeah1d1
    g "You know what’d really help me relax?"
    g "*gropes Yoshinori’s butt*"

    show yoshi shock3 at center
    voice audio.yoshi_v_shock3
    yo "GAH! You startled me…!" with vpunch

    show goro tease2 at left2
    voice audio.goro_v_heh1a
    g "Heh, I know you like it."

    show yoshi shy6 at center
    voice audio.yoshi_v_yeah3
    yo "I-I do…"

    show goro tease3 at left2
    voice audio.goro_v_yoshi15a
    g "I could really use a reward for all that hard work~"
    g "*gropes Yoshinori’s chest*"

    show yoshi scared2 at center
    voice audio.yoshi_v_groan1a
    yo "Hngh… Everybody’s waiting for us at the party… A-Are we doing a quickie?"

    show goro tease5 at left2
    voice audio.goro_v_think2b1
    g "Why don’t we take our time instead? "
    g "*fondles Yoshinori’s crotch*"

    show yoshi_blush1 at center
    show yoshi upset2 at center
    voice audio.yoshi_v_groan1b
    yo "Nngh…"

    show goro bold5 at left2
    voice audio.goro_v_think1d1
    g "Mmmhh… It’s been a while, hasn’t it…?"

    show yoshi comp3 at center
    voice audio.yoshi_v_but1
    yo "B-But we’ve been doing it every night and morning…"

    show goro tease3 at left2
    voice audio.goro_v_well1a
    g "Well, too bad… I just can’t get enough of you… *kisses Yoshinori’s neck*"

    show yoshi shy6 at center
    voice audio.yoshi_v_ah2
    yo "Ahh…"

    show goro play3 at left2
    voice audio.goro_v_laugh1a1
    g "Hehe… All of a sudden you don’t care that anyone can just walk in and see us, huh?"

    show yoshi relief2 at center
    voice audio.yoshi_v_please1b
    yo "I just want you right now…"

    show goro_blush1 at left2
    show goro tease3 at left2
    voice audio.goro_v_taunt1a
    g "Well, how about you show me how much you really want it…?"
    g "You gotta work hard if you want a reward too~"

    show yoshi comp2 at center
    voice audio.yoshi_v_goro14
    yo "Goro…"

    scene cg black
    $ position = 0
    if score_bot == score_top:
        $ position = renpy.random.randint(1, 2)
    if score_bot > score_top or position == 1:
        hide screen location
        hide screen timeline
        hide screen quick_menu
        $ quick_menu = False
        with fade
        $ say_box = False
        $ fp_stage = 'mgg4_f'
        $ success_jumpto = 'day10_goro_7d'
        $ failed_jumpto = 'day10_goro_aftersx'
        jump fp

    elif score_top > score_bot or position == 2:
        hide screen location
        hide screen timeline
        hide screen quick_menu
        $ quick_menu = False
        with fade
        $ say_box = False
        $ fp_stage = 'mgg4_b'
        $ success_jumpto = 'day10_goro_7s'
        $ failed_jumpto = 'day10_goro_aftersx'
        jump fp

label day10_goro_aftersx:
    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    $ location = location_office
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_office_past_day
    play music here_they_come_fast loop
    play bgsound sfxloop_birds loop

    show yoshi_semiformal2 at p4_1
    show yoshi_ring1 at p4_1
    show yoshi panic1 at p4_1
    show goro_semiformal2 at p4_2
    show goro_ring1 at p4_2
    show goro shock1 at p4_2
    show yuri2_autumn at p4_3
    show yuri2 disgust2 at p4_3
    show jin2_autumn at p4_4
    show jin2_blush2 at p4_4
    show jin2_nosebleed at p4_4
    show jin2_glasses at p4_4
    show jin2 fudan1 at p4_4
    voice audio.yuri_vsxg7d_line2
    yu "LOOOOOOOOOONG!!!!!!" with vpunch

    show jin2 fudan3 at p4_4
    voice audio.jin_v_wah4a
    j "GAHHHHHHHHHHHH!!!!!!!!!!" with vpunch

    show yoshi panic4 at p4_1
    voice audio.yoshi_v_oops1
    yo "Oh no! G-Goro, toss me my pants…!"

    show yuri2 scared2 at p4_3
    voice audio.yuri_v_no1c1
    yu "MY EYES!! MY EEEEYES!!"

    hide yuri2_autumn
    hide yuri2 scared2
    with moveoutright

    show goro sigh4 at p4_2
    voice audio.goro_v_sigh2a
    g "*sigh* Guess we had that coming."

    show jin2 comic4 at p4_4
    voice audio.jin_v_hngh4a
    j "S-SO MUCH MUSCLE!! SO MUCH SWEAT!! SO MUCH SEMEN!!"

    show yoshi pain3 at p4_1
    voice audio.yoshi_v_oww1
    yo "HNGH! I can’t get up from the table…! G-Goro, cover Jin’s eyes!!"

    show jin2 comic5 at p4_4
    voice audio.jin_v_fudan4c1
    j "D-DO YOU NEED A WHEELCHAIR?! OR PERHAPS COLON SURGERY?!"

    show goro talk3 at p4_2
    voice audio.goro_v_conj10a1
    g "I think it’s too late for that, Yoshinori…"

    show yoshi_semiformal2 at p6_1
    show yoshi_ring1 at p6_1
    show yoshi panic1 at p6_1
    show goro_semiformal2 at p6_2
    show goro_ring1 at p6_2
    show goro shock1 at p6_2
    show jin2_autumn at p6_3
    show jin2_nosebleed at p6_3
    show jin2_blush2 at p6_3
    show jin2_glasses at p6_3
    show jin2 comic1 at p6_3
    with move

    show aiden_autumn at p6_4
    show aiden talk3 at p6_4
    show lloyd_autumn at p6_5
    show lloyd shock1 at p6_5
    show darius_autumn at p6_6
    show darius shock1 at p6_6
    with dissolve

    voice audio.aiden_v_greet1a
    a "Hey! What’s going on in here?! Yuri was screaming and running away from—"

    show aiden shock3 at p6_4
    voice audio.aiden_v_oho1a
    a "O-HOLE~"

    show lloyd shock6 at p6_5
    voice audio.lloyd_v_shock3b1
    l "Oh… my… god, that table is covered in cum."

    show darius tease3 at p6_6
    voice audio.darius_v_laugh1
    d "Yoshi – the not-so-virgin sacrifice."

    show yoshi angry3 at p6_1
    voice audio.yoshi_v_guys4
    yo "G-Get out, you guys…! Th-There’s nothing to see here!"

    show jin2 dizzy6 at p6_3
    voice audio.jin_v_fudan2b
    j "*mouth foams*"

    show goro disappoint3 at p6_2
    voice audio.goro_v_scold1a1
    g "Get a hold of yourself, Jin. Somebody help the poor boy."

    show aiden comp6 at p6_4
    voice audio.aiden_v_confident1a
    a "I’ll take care of him! You guys go finish up and come over to the mess hall for the meal!"

    show lloyd annoy2 at p6_5
    voice audio.lloyd_v_annoyed1a1
    l "I think they’re way more than finished."

    show darius tease2 at p6_6
    voice audio.darius_v_naughty1a
    d "Hehe, and it looks like Yoshi’s full already~ "

    show yoshi worry4 at p6_1
    voice audio.yoshi_v_shock4
    yo "W-We’ll clean up right away and catch up, everyone..!"

    show aiden tease2 at p6_4
    voice audio.aiden_v_bye1a
    a "Seeya at the party then~"

    hide aiden_autumn
    hide aiden tease2
    hide jin2_autumn
    hide jin2_glasses
    hide jin2 dizzy6
    hide jin2_nosebleed
    hide jin2_blush2
    hide lloyd_autumn
    hide lloyd annoy2
    hide darius_autumn
    hide darius tease2
    with dissolve

    show yoshi_semiformal2 at left2
    show yoshi_ring1 at left2
    show yoshi sigh3 at left2
    show goro_semiformal2 at right2
    show goro_ring1 at right2
    show goro play1 at right2
    with move

    voice audio.yoshi_v_oops2
    yo "Oh god… that was so embarrassing, Goro…"

    show goro laugh2 at right2
    voice audio.goro_v_laugh1c1
    g "Hahaha!"

    show yoshi angry3 at left2
    voice audio.yoshi_v_why4a
    yo "Why are you so unphased by this?!"

    show goro laugh1 at right2
    voice audio.goro_v_heh3a
    g "I-It’s just so funny to me, how we’ve been careful this whole time and the first time we get caught, what they see is your gaping cum-filled asshole! "

    show goro comic3 at right2
    voice audio.goro_v_laugh2d1
    g "GAHAHAHA!"

    show yoshi angry6 at left2
    voice audio.yoshi_v_rush4
    yo "Th-That’s not funny…!!"

    show goro laugh5 at right2
    voice audio.goro_v_sorry2b1
    g "I-It really is, Yoshinori! I’m sorry! Hahaha! "

    show yoshi angry2 at left2
    voice audio.yoshi_v_disagree3
    yo "No fair! Everyone’s already seen your dick!"

    show goro laugh1 at right2
    voice audio.goro_v_laugh2d2
    g "Fuck, my sides are hurting, hahaha!!"

    show yoshi angry5 at left2
    voice audio.yoshi_v_rush4
    yo "J-Just help me up already…!"

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
    scene bg_messhall_past_day_celebration with fade
    play music buddy_oath_casual loop
    play bgsound sfxloop_crowd loop

    show yoshi_autumn at p9_1
    show yoshi_ring1 at p9_1
    show yoshi norm1 at p9_1
    show goro_autumn at p9_2
    show goro_ring1 at p9_2
    show goro norm1 at p9_2
    show william_autumn at p9_3
    show william relief2 at p9_3
    show darius_autumn at p9_5
    show darius play1 at p9_5
    show lloyd_autumn at p9_4
    show lloyd norm2 at p9_4
    show aiden_autumn at p9_6
    show aiden play1 at p9_6
    show jin2_autumn at p9_7
    show jin2_blush2 at p9_7
    show jin2_glasses at p9_7
    show jin2 fudan1 at p9_7
    show emilia_autumn at p9_8
    show emilia norm2 at p9_8
    show yuri_autumn at p9_9
    show yuri pain3 at p9_9
    voice audio.william_v_surprised1b
    w "Ahh, it’s so nice to be enjoying everyone’s company again!"
    w "And a little bird told me that someone here got engaged last year~"

    show goro talk3 at p9_2
    voice audio.goro_v_agree2a1
    g "Ah, yes. That would be Yoshinori and I, sir."

    show william happy3 at p9_3
    voice audio.william_v_amazed3
    w "Congratulations, you two! You make quite the wonderful couple!"

    hide yoshi_autumn
    hide yoshi_ring1
    hide yoshi norm1
    show yoshi2_autumn at p9_1
    show yoshi2_ring1 at p9_1
    show yoshi2 comp3 at p9_1
    voice audio.yoshi_v_thanks3
    yo "Th-Thank you, Mr. Clermont…"

    show william comp4 at p9_3
    voice audio.william_v_conj8
    w "I must say, this wasn’t really a surprise to me. Your pair has always had a special closeness."

    show aiden tease1 at p9_6
    voice audio.aiden_v_laugh3a
    a "Pfft… Well, they were definitely extra close earlier."

    hide goro_autumn
    hide goro_ring1
    hide goro norm1
    show goro2_autumn at p9_2
    show goro2 disappoint3 at p9_2
    voice audio.goro_v_ehem1c
    g "*cough* *cough*"

    show william happy3 at p9_3
    voice audio.william_v_agree3a
    w "It is true, though. Yoshinori here is quite the perfect fit for you, Goro. "

    show lloyd tease2 at p9_4
    voice audio.lloyd_v_conj1a4
    l "Let’s just say—"

    show darius tease2 at p9_5
    voice audio.darius_v_laugh1
    d "—if it fits, Yoshi sits."

    show jin2 fudan2 at p9_7
    voice audio.jin_v_hngh1a
    j "Hnghhh…"

    show yuri pain6 at p9_9
    voice audio.yuri_v_shock2a
    yu "*gags*"

    show emilia confused3 at p9_8
    voice audio.emilia_v_question4b
    e "Can somebody tell me what’s going on?"
    e "Yuri’s sitting way over here on the verge of choking, and you’re all talking like there’s an inside joke."

    show aiden wink3 at p9_6
    voice audio.aiden_v_well1b2
    a "Well, there definitely was some choking."

    show goro2 play2 at p9_2
    voice audio.goro_v_alright3a
    g "Are you alright, dear?"

    show yuri rage4 at p9_9
    voice audio.yuri_v_no1c3
    yu "NO, I’M NOT ALRIGHT! I’M TRAUMATIZED!" with vpunch

    show lloyd laugh1 at p9_4
    voice audio.lloyd_v_laugh1a1
    l "Haha! Somehow I enjoy this Yuri more."

    show yuri rage1 at p9_9
    voice audio.yuri_v_request1a
    yu "Could we please, PLEASE, change the topic?!"

    show william laugh2 at p9_3
    voice audio.william_v_laugh1
    w "Looks like someone woke up on the wrong side of the bed today, hahaha!"

    show emilia angry2 at p9_8
    voice audio.emilia_v_rush1c
    e "Yeah, lighten up, will you?! We literally finished the project; you should be celebrating!"

    hide yoshi2_autumn
    hide yoshi2_ring1
    hide yoshi2 comp3
    show yoshi_autumn at p9_1
    show yoshi_ring1 at p9_1
    show yoshi happy2 at p9_1
    voice audio.yoshi_v_shock1d
    yo "It’s quite surreal that the project is really done, huh? Camp Buddy is two times bigger than it was."

    hide jin2_autumn
    hide jin2_glasses
    hide jin2_blush2
    hide jin2 fudan2
    show jin_autumn at p9_7
    show jin_glasses at p9_7
    show jin thinkdn3 at p9_7
    voice audio.jin_v_yeah2a
    j "Y-Yeah, I feel like I’m having withdrawals already – after so much work the last few months, I feel like I should be working still…"

    show lloyd happy1 at p9_4
    voice audio.lloyd_v_celebrate1a1
    l "But we managed to get everything done! We’ve all earned this break!"

    show yuri comp1 at p9_9
    show yoshi sad4 at p9_1
    voice audio.yoshi_v_aww1
    yo "It’s bittersweet too, though… Everyone’s going to be leaving soon."

    hide yoshi_autumn
    hide yoshi_ring1
    hide yoshi sad4
    show yoshi2_autumn at p9_1
    show yoshi2_ring1 at p9_1
    show yoshi2 sigh1 at p9_1
    voice audio.yoshi_v_sigh3a
    yo "*sigh* I know that we’ve done a good job and all, but I’m really gonna miss working with you guys…"

    hide aiden_autumn
    hide aiden wink3
    show aiden2_autumn at p9_6
    show aiden2 shock2 at p9_6
    hide darius_autumn
    hide darius tease2
    show darius_autumn at p9_5
    show darius tease2 at p9_5
    hide lloyd_autumn
    hide lloyd happy1
    show lloyd_autumn at p9_4
    show lloyd happy1 at p9_4
    voice audio.aiden_v_oops2a
    a "Uh-oh, here come the waterworks."

    hide yoshi2_autumn
    hide yoshi2_ring1
    hide yoshi2 sigh1
    show yoshi_autumn at p9_1
    show yoshi_ring1 at p9_1
    show yoshi worry2 at p9_1
    voice audio.yoshi_v_but2
    yo "Having you all here has been one of the best times I’ve had working here!"
    yo "It’s really going to be different without you guys…"

    show lloyd awkward2 at p9_4
    l "..."

    show darius awkward1 at p9_5
    d "..."

    show jin confuseddn1 at p9_7
    j "..."

    hide yoshi_autumn
    hide yoshi_ring1
    hide yoshi worry2
    show yoshi2_autumn at p9_1
    show yoshi2_ring1 at p9_1
    show yoshi2 awkward3 at p9_1
    voice audio.yoshi_v_what3
    yo "Wh-What…? Did I say something?"

    show emilia comp6 at p9_8
    voice audio.emilia_v_sigh1a
    e "Go on, tell the poor fool, he’s close to tears."

    show yoshi2 confused2 at p9_1
    voice audio.yoshi_v_huh1
    yo "T-Tell me what?"

    show jin explain3 at p9_7
    voice audio.jin_v_conj2c1
    j "Well… Me and the others have been talking… "
    j "We all decided that we want to stay here at Camp Buddy if that’s alright...?"

    hide goro2_autumn
    hide goro2 play2
    show goro_autumn at p9_2
    show goro_ring1 at p9_2
    show goro shock1 at p9_2
    g "...!"

    hide yoshi2_autumn
    hide yoshi2_ring1
    hide yoshi2 awkward3
    show yoshi_autumn at p9_1
    show yoshi_ring1 at p9_1
    show yoshi shock3 at p9_1
    voice audio.yoshi_v_what4
    yo "Wh-What?! "

    hide aiden2_autumn
    hide aiden2 shock2
    show aiden_autumn at p9_6
    show aiden excited3 at p9_6
    voice audio.aiden_v_really3a
    a "W-Woah?! REALLY?! That’s so cool!"

    show lloyd happy1 at p9_4
    voice audio.lloyd_v_agree2b1
    l "Yeah! We loved it here so much we don’t wanna leave anymore!"

    show darius happy2 at p9_5
    voice audio.darius_v_conj1a1
    d "We’re ready for a change of pace from all the construction work."

    show yoshi shock2 at p9_1
    voice audio.yoshi_v_wait3a
    yo "W-Wait, a-are you all sure?! "

    show emilia angry2 at p9_8
    voice audio.emilia_v_what1
    e "What? You don’t want them to stay?! Isn’t this what you’ve been tearing up about for the past two minutes?"

    hide yoshi_autumn
    hide yoshi_ring1
    hide yoshi shock2
    show yoshi2_autumn at p9_1
    show yoshi2_ring1 at p9_1
    show yoshi2 awkward4 at p9_1
    voice audio.yoshi_v_no5
    yo "N-No, I mean… "

    show lloyd explain3 at p9_4
    voice audio.lloyd_v_conj1a3
    l "Well, we all thought about it over the last few months, after we realized that staying was a possibility. "

    show yuri happy1 at p9_9
    voice audio.yuri_v_actually1a
    yu "They actually coordinated it already with Mr. Clermont, and he agreed as well."

    hide yoshi2_autumn
    hide yoshi2_ring1
    hide yoshi2 awkward4
    show yoshi_autumn at p9_1
    show yoshi_ring1 at p9_1
    show yoshi shock5 at p9_1
    voice audio.yoshi_v_yuri5
    yo "Yuri? You were in on this? "

    show yuri laugh1 at p9_9
    voice audio.yuri_v_laugh2b1
    yu "We thought it would be nice to leave it as a surprise for you, Aiden, and Dad."

    hide yoshi_autumn
    hide yoshi_ring1
    hide yoshi shock5
    show yoshi2_autumn at p9_1
    show yoshi2_ring1 at p9_1
    show yoshi2 worry4 at p9_1
    voice audio.yoshi_v_why1
    yo "B-But… Wh-Why? Don’t you guys all have great career opportunities ahead of you?"

    show jin think2 at p9_7
    voice audio.jin_v_conj1b1
    j "I have a lot of extra income online, not to mention my crypto… So, it doesn’t really matter for me…"

    show jin comp2 at p9_7
    voice audio.jin_v_confused2a1
    j "And… seeing how everyone here was part of Camp Buddy in the past, I feel I missed a part of my youth."
    j "I want to experience being a scout and taking part in the activities too!"

    show jin comp6 at p9_7
    voice audio.jin_v_conj4a1
    j "More importantly, someone needs to maintain the new tech and even do some upgrades down the line."
    j "It’d be much easier for everyone to have an in-house technician, right? I’d say that’s a win-win!"

    hide yuri_autumn
    hide yuri laugh1
    show yuri2_autumn at p9_9
    show yuri2 laugh3 at p9_9
    voice audio.yuri_v_celebrate1a
    yu "Yiieee! My fanfic buddy is staying! "

    show lloyd bold2 at p9_4
    voice audio.lloyd_v_comp1a1
    l "Dar and I plan to apply as scoutmasters, so you don’t have to worry about us either!"

    show darius explain4 at p9_5
    voice audio.darius_v_conj5b
    d "We both really enjoyed teaching Taiga and Yoichi over the project, and want to share our knowledge with the rest of the scouts."
    d "Plus, Aiden’s cooking is worth staying for."

    show lloyd excited3 at p9_4
    voice audio.lloyd_v_encourage1a
    l "As for the financial part, we have a plan for it as well! "
    l "While we’re here, we’ll be running a nice side hustle – a design consultancy firm! "

    show lloyd bold3 at p9_4
    voice audio.lloyd_v_laugh1a3
    l "We call it D-L-Do! “Darius and Lloyd will do it all for you~” "

    show darius bold3 at p9_5
    voice audio.darius_v_agree3
    d "We’ve been in the industry for years already as contractors… it’s about time we started our own firm."
    d "With Lloyd and I working together, we thought it would be the perfect opportunity to make this decision."

    show william happy1 at p9_3
    voice audio.william_v_actually1
    w "It was actually all quite impressive – they laid out not only their personal plans but also ideas for the camp as well."
    w "Lloyd and Darius came up with a woodworking and construction curriculum for your scouts, and they’re quite passionate about it!"

    show william explain3 at p9_3
    voice audio.william_v_conj3b
    w "Personally, I’d love to see them all join the camp, but it’s up to the president’s final say!"

    show jin comp3 at p9_7
    voice audio.jin_v_yeah3b
    j "Y-Yeah… We decided this on our own, and we don’t really want to force it if it’s not—"

    show goro happy3 at p9_2
    voice audio.goro_v_agree3a1
    g "I have no objections – I would be honored to have all these talented and dedicated people as scoutmasters!"

    show william laugh2 at p9_3
    voice audio.william_v_laugh1
    w "Haha, I knew you’d approve them right away."

    show lloyd excited2 at p9_4
    voice audio.lloyd_v_amazed2a1
    l "Awesome! We got the job, Dar!"

    show darius amazed1 at p9_5
    voice audio.darius_v_celebrate1a
    d "Hooray."

    show emilia explain2 at p9_8
    voice audio.emilia_v_so1
    e "As for me, I’m going to stick with the helper role. "

    show aiden confused2 at p9_6
    voice audio.aiden_v_confused1c1
    a "Eh…? You’re not gunning to be a scoutmaster too?"

    show emilia talk1 at p9_8
    voice audio.emilia_v_no4
    e "No… I noticed during my time as both an inspector and these last few months that Aiden does all the maintenance work by himself, both during the on and off season. "
    e "I… want to help alleviate some of his workload so he can focus more on what he’s really passionate about, cooking."

    show emilia happy1 at p9_8
    voice audio.emilia_v_conj1a
    e "Plus, doing chores over the last few months has been strangely… enjoyable."
    e "I never experienced them growing up, and always was disgusted by ‘dirty work.’"

    show emilia bold2 at p9_8
    voice audio.emilia_v_conj5b
    e "Now, I feel a real sense of fulfilment when I complete them, seeing everyone enjoy the comfort as a direct result of my hard work."
    e "Not to mention that I’m learning new skills as well."

    hide yoshi2_autumn
    hide yoshi2_ring1
    hide yoshi2 worry4
    show yoshi_autumn at p9_1
    show yoshi_ring1 at p9_1
    show yoshi comp2 at p9_1
    voice audio.yoshi_v_praise1
    yo "That’s great, Emilia! You’ve got such a wonderful mindset about it all now!"

    hide yuri2_autumn
    hide yuri2 laugh3
    show yuri_autumn at p9_9
    show yuri bold2 at p9_9
    voice audio.yuri_v_laugh1a1
    yu "Hihi, with all this extra help, I can also focus more on being a counselor for the scouts that need it!"

    show yoshi comp5 at p9_1
    voice audio.yoshi_v_guys4
    yo "E-Everyone… You don’t know how happy this makes me…"

    show aiden shock3 at p9_6
    voice audio.aiden_v_swear3a
    a "Oh no! Here come the waterworks for real! "

    show yoshi comp3 at p9_1
    voice audio.yoshi_v_amazed2b
    yo "I-I can’t help it… you guys… "

    show goro laugh1 at p9_2
    voice audio.goro_v_alright2c2
    g "Let it all out, Yoshinori.  "

    show jin excited3 at p9_7
    voice audio.jin_v_oh3a
    j "O-Oh! Since everyone is here, I think this is the perfect time for us to take a victory selfie! "

    show yuri excited2 at p9_9
    voice audio.yuri_v_oh1a
    yu "Oooooh~! Good idea! I think we could also add it to our website! "

    show jin bold2 at p9_7
    voice audio.jin_v_response3a1
    j "Definitely! I was already planning to make the expansion project my next feature on there!"
    j "I’ll setup the camera! Everyone, huddle up!"

    show yoshi_autumn at p10_1
    show yoshi_ring1 at p10_1
    show yoshi norm1 at p10_1
    show goro_autumn at p10_2
    show goro_ring1 at p10_2
    show goro norm1 at p10_2
    show william_autumn at p10_3
    show william norm1 at p10_3
    show lloyd_autumn at p10_4
    show lloyd norm1 at p10_4
    show darius_autumn at p10_5
    show darius norm1 at p10_5
    show aiden_autumn at p10_6
    show aiden norm1 at p10_6
    show emilia_autumn at p10_7
    show emilia norm1 at p10_7
    show yuri_autumn at p10_8
    show yuri norm1 at p10_8
    show jin_autumn at p10_10
    show jin_glasses at p10_10
    show jin bold5 at p10_10
    with move

    voice audio.jin_v_response1a1
    j "And… the timer is set!"

    show jin_autumn at p10_9
    show jin_glasses at p10_9
    show jin happy1 at p10_9
    with move

    voice audio.jin_v_laugh1a
    j "Everybody say, ‘Camp Buddy!’"

    $ renpy.music.stop(channel='music', fadeout = 2.0)
    show yoshi grin3 at p10_1
    show goro norm1 at p10_2
    show william smile2 at p10_3
    show lloyd grin2 at p10_4
    show darius smile1 at p10_5
    show aiden grin4 at p10_6
    show emilia laugh3 at p10_7
    show yuri laugh1 at p10_8
    show jin grin3 at p10_9
    all "Camp Buddy!"

    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    play sound sfx_camerashot
    scene cg10 with flash
    play music buddy_oath_acoustic loop
    voice audio.yoshi_vsa28_line1
    yo "Seasons have come and gone since we started this amazing project… And everything that happened was the opposite of what I thought it’d be."

    voice audio.yoshi_vsa28_line2
    yo "It was quite the ride – we encountered problems that couldn’t be predicted from when we were scouts, or even from before we returned to camp."

    voice audio.yoshi_vsa28_line3
    yo "Things didn’t always work out the way we planned, and we were challenged way past our limits."

    voice audio.yoshi_vsg30_line1
    yo "And in these darkest moments, Goro’s best trait really shined – his fortitude. It was the reason why I could move forward too."

    voice audio.yoshi_vsa28_line5
    yo "I am so grateful we had the chance to continue where our stories left off… and it helped me learn even more about him and his past."

    voice audio.yoshi_vsa28_line6
    yo "I know now where his happiness and pain comes from, and from this, we were able to make our new promise to each other."

    voice audio.yoshi_vsa28_line7
    yo "And I owe it all to Camp Buddy… That’s why we’re going to give it everything we’ve got and face the future with the brightest smile."

    voice audio.yoshi_vsa28_line8
    yo "Forever, it’s our buddy oath!"

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg white
    hide screen location
    hide screen timeline
    hide screen quick_menu
    $ quick_menu = False
    with Dissolve(3.0)

    #credits
    $renpy.movie_cutscene("images/Camp Buddy Scoutmaster Season Credits.webm")
    jump day10_goro_gepe_aftercredits

label day10_goro_gepe_aftercredits:
    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black
    hide screen location
    hide screen timeline
    hide screen quick_menu
    $quick_menu = False
    with fade
    $time_transition_spring_to_summer()
    $ renpy.pause (2.0, hard=True)

    $ location = location_lake
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_lake_day_wedding with fade
    play music old_familiar_home_string loop

    show goro_wedding at p5_1
    show goro_ring1 at p5_1
    show goro comp1 at p5_1
    show yuri_wedding at p5_2
    show yuri angry2 at p5_2
    show lloyd_wedding at p5_4
    show lloyd pain1 at p5_4
    show darius_wedding at p5_5
    show darius worry1 at p5_5
    voice audio.yuri_v_rush1c1
    yu "Lift the banner higher! NO, HIGHER!"

    show lloyd pain3 at p5_4
    voice audio.lloyd_v_groan1c1
    l "Th-This is as high as my arms can reach!!"

    show darius tease2 at p5_5
    voice audio.darius_v_laugh1
    d "Need a piggyback? "

    show yuri angry3 at p5_2
    voice audio.yuri_v_rush1d1
    yu "Come on, boys! There’s no time! The ceremony will be starting soon!!"

    show goro comp2 at p5_1
    voice audio.goro_v_think3
    g "Uh… Yuri-dear… Maybe you should relax a little…?"

    show yuri comp2 at p5_2
    voice audio.yuri_v_comp1a1
    yu "Oh, don’t worry, Dad! I’m just making sure everything’s perfect for you and Yoshi~"
    yu "It’s your most special day, after all!"

    show yuri rage4 at p5_2
    voice audio.yuri_v_hmph1a
    yu "…Which will be ruined if SOMEONE doesn’t finish setting up those chairs!"

    show lloyd scared3 at p5_4
    voice audio.lloyd_v_sad1a1
    l "Huhuhu I’m moving as fast as I can…"

    show darius worry4 at p5_5
    voice audio.darius_v_naughty1a
    d "She’s a real domme."

    show goro comp3 at p5_1
    voice audio.goro_v_thanks2a1
    g "R-Right, well, thank you for getting everyone to help, Yuri. I know it’s been difficult setting this all up last minute."

    show yuri comp4 at p5_2
    voice audio.yuri_v_alright2b1
    yu "Not at all, Dad! You know parties are my specialty after all~"
    yu "Just leave it to me and I’ll have it all handled!"

    show lloyd_wedding at p5_3
    show lloyd excited2 at p5_3
    show darius_wedding at p5_4
    show darius norm1 at p5_4
    with move

    voice audio.lloyd_v_agree3a1
    l "Okay! That’s all the chairs set up! I think we’re—"

    show yuri angry2 at p5_2
    voice audio.yuri_v_sarcastic1a1
    yu "Ah, ah, ah! I had three more bouquets of flowers back at the mess hall that you FORGOT!"

    show lloyd scared1 at p5_3
    show darius worry1 at p5_4
    voice audio.lloyd_v_shock2c1
    l "Hngh!"

    show yuri rage1 at p5_2
    voice audio.yuri_v_rush3a
    yu "Go get them and be back here in FIVE MINUTES!"

    show darius sigh1 at p5_4
    voice audio.darius_v_agree1c
    d "Yes, ma’am…"

    hide darius_wedding
    hide darius sigh1
    hide lloyd_wedding
    hide lloyd scared1
    with moveoutright

    show goro awkward2 at p5_1
    show yuri relief2 at p5_2
    voice audio.yuri_v_relief1b1
    yu "Fwahhh, I love weddings~"

    show goro_wedding at p8_1
    show goro_ring1 at p8_1
    show goro norm1 at p8_1
    show yuri_wedding at p8_2
    show yuri norm1 at p8_2
    with move

    show keitaro_wedding at p8_3
    show keitaro talking1 at p8_3
    show taiga_wedding at p8_4
    show taiga normal3 at p8_4
    show natsumi_wedding at p8_5
    show natsumi normal1 at p8_5
    show hunter_wedding at p8_6
    show hunter smile1 at p8_6
    show hiro_wedding at p8_7
    show hiro normal1 at p8_7
    show yoichi_wedding at p8_8
    show yoichi normal1 at p8_8
    with dissolve

    voice audio.keitaro_v_greeting1
    k "Hello, Sir Goro!"

    show goro happy2 at p8_1
    voice audio.goro_v_glad1a
    g "Ah, scouts! I’m so glad to see you all here!"

    show keitaro compassion3 at p8_3
    voice audio.keitaro_v_agree2
    k "Of course, sir! We wouldn’t miss something this important!"

    show hunter amazed1 at p8_6
    voice audio.hunter_v_amazed1
    hu "You and Ms. Yuri looks so good too – I’ve never seen you both so dressed up."

    show yuri comp2 at p8_2
    voice audio.yuri_v_aww2a
    yu "Aww, thank you sweetie~ You boys have been a big help today too!"

    show goro confused3 at p8_1
    voice audio.goro_v_oh4b
    g "Oh? I didn’t realize they were assisting with the preparations."

    show taiga talking5 at p8_4
    voice audio.taiga2_v_agree3b
    t "Yup! I helped Lloyd and Darius make the arch!"

    show hiro confident2 at p8_7
    voice audio.hiro_v_laugh1a2
    hi "And obviously I helped Bro-Aiden with the cooking~"

    show yoichi angry1 at p8_8
    voice audio.yoichi_v_greet1d1
    yi "HEY! Tell ’em what I did!"

    show taiga playful1 at p8_4
    voice audio.taiga2_v_boastful1a
    t "We kept the dumbass busy by letting him blow up balloons."

    show yoichi pout1 at p8_8
    voice audio.yoichi_v_hmph1a
    yi "You said that was important!"

    show keitaro laugh1 at p8_3
    voice audio.keitaro_v_scheming1a
    k "Y-You did great, Yoichi."

    show natsumi compassion1 at p8_5
    voice audio.natsumi_v_celebrate1
    n "I can’t believe that my scoutmasters are actually getting married… *sniff* It’s just so heartwarming…"

    show yoichi annoyed4 at p8_8
    voice audio.yoichi_v_groan2b1
    yi "Ugh, this is like the fifth time he’s cried today."

    show hunter compassion3 at p8_6
    voice audio.hunter_v_compassion1a
    hu "I-It’s alright, Natsumi… "

    show natsumi worry3 at p8_5
    voice audio.natsumi_v_apology2
    n "I just wish we had known sooner! We could’ve at least worn something more formal…"

    show goro laugh1 at p8_1
    voice audio.goro_v_comp2a1
    g "Haha, no need to apologize, Natsumi. Having you all with us today is all Yoshinori and I could’ve wanted."
    g "I hope you’ll stick around for the after party as well."

    show keitaro amazed1 at p8_3
    voice audio.keitaro_v_agree2
    k "Of course, sir! We wouldn’t miss it!"

    show taiga talking2 at p8_4
    voice audio.taiga2_v_conjunction2a
    t "Anyway, we should probably get our seats. Looks like everyone else is moving in too."

    show yoichi angry3 at p8_8
    voice audio.yoichi_v_rush1a5
    yi "This better not take too long or I’ll start snoring."

    show hiro annoyed2 at p8_7
    voice audio.hiro_v_shush1a
    hi "If you do, I’ll smack you!"

    show hunter laugh1 at p8_6
    voice audio.hunter_v_laugh1
    hu "Congratulations again, Sir Goro!"

    hide keitaro_wedding
    hide keitaro amazed1
    hide taiga_wedding
    hide taiga talking2
    hide natsumi_wedding
    hide natsumi worry3
    hide hunter_wedding
    hide hunter laugh1
    hide hiro_wedding
    hide hiro annoyed2
    hide yoichi_wedding
    hide yoichi angry3
    with dissolve

    show goro_wedding at left2
    show goro_ring1 at left2
    show goro comp1 at left2
    show yuri_wedding at right2
    show yuri laugh1 at right2
    with move

    voice audio.yuri_v_laugh1a1
    yu "Hihi, I’m so glad I called them to join today~"

    show goro happy2 at left2
    voice audio.goro_v_agree7a
    g "Me too. If it weren’t for them, I’m not sure we’d be standing here today."

    show yuri happy2 at right2
    voice audio.yuri_v_oh1b
    yu "Oh, and speaking of reasons we’re here…"

    show goro_wedding at left
    show goro happy2 at left
    show yuri_wedding at center
    show yuri happy2 at center
    with move

    show william_wedding at right
    show william happy2 at right
    with dissolve

    voice audio.william_v_greet2b
    w "Hello, Goro and Yuri! It’s a beautiful day for a wedding!"

    show goro happy4 at left
    voice audio.goro_v_william2a
    g "Ah, Mr. Clermont! Thank you so much for coming, sir!"

    show william laugh2 at right
    voice audio.william_v_agree1b
    w "Why, I wouldn’t miss it for the world! I just wanted to swing over for a moment and give you a little wedding gift before the ceremony~"

    show william_wedding at left
    show william norm1 at left
    with move

    show william_wedding at right
    show william norm1 at right
    with move

    show goro shock2 at left
    voice audio.goro_v_ah1c
    g "Th-This is…!"

    show william happy3 at right
    voice audio.william_v_comp3
    w "An all-expense paid trip to one of my company’s resort islands! I thought you and Yoshinori deserved to have a wonderful honeymoon!"

    show yuri excited2 at center
    voice audio.yuri_v_kyaa1a
    yu "Kyaaa! That’s so exciting for you and Yoshi, Dad! "

    show goro amazed1 at left
    voice audio.goro_v_thanks3a
    g "Th-Thank you so much, sir! We’ll gladly take you up on the offer!"

    voice audio.goro_v_heh1a
    g "Heh, Yoshinori is going to freak out when he finds out!"

    show william laugh2 at right
    voice audio.william_v_laugh1
    w "Haha, I hope so! Thank you again for the invite, and I’ll look forward to another fun gathering with you all~"

    hide william_wedding
    hide william laugh2
    with dissolve

    show goro comp5 at left
    voice audio.goro_v_laugh1a1
    g "Mr. Clermont continues to be quite generous, doesn’t he?"

    show yuri play2 at center
    voice audio.yuri_v_laugh1a2
    yu "Hihi, I almost expect it at this point~"

    show goro comp6 at left
    voice audio.goro_v_ehem1a
    g "L-Let’s not get carried away with that mindset, Yuri."

    show yuri angry2 at center
    voice audio.yuri_v_anyway1a
    yu "Anyway, where’s our ringbearer and flower girl? I haven’t seen them yet!"

    show goro_wedding at p4_1
    show goro_ring1 at p4_1
    show goro norm1 at p4_1
    show yuri_wedding at p4_2
    show yuri annoy1 at p4_2
    with move

    show emilia_wedding at p4_3
    show emilia norm2 at p4_3
    show jin_wedding at p4_4
    show jin talk2 at p4_4
    with dissolve

    voice audio.jin_v_greet1c1
    j "R-Right here!"

    show yuri angry3 at p4_2
    voice audio.yuri_v_celebrate2a
    yu "Finally! What took you two so long?!"

    show jin worry3 at p4_4
    voice audio.jin_v_sorry1b1
    j "S-Sorry, Yuri! I just wanted to be extra careful holding the rings… I was scared I’d drop them."

    show emilia relief2 at p4_3
    voice audio.emilia_v_sarcastic2b1
    e "And obviously, I had plenty of prep work to do before hand – looking this good takes time after all~"

    show yuri annoy2 at p4_2
    voice audio.yuri_v_ugh3a
    yu "Ugh, why am I not surprised to hear that? You could’ve made us late!"

    show emilia eyeroll4 at p4_3
    voice audio.emilia_v_so1
    e "So? We’re not exactly at the fanciest of venues here! A little delay won’t hurt anything!"

    show emilia relief5 at p4_3
    voice audio.emilia_v_ah3
    e "Ahhhh, this just gets me thinking about how differently I’D do my wedding~"
    e "A fancy hotel on a private island… Or maybe on the top of a beautiful mountain?"

    show emilia amazed1 at p4_3
    voice audio.emilia_v_oh1a
    e "Oh! Or maybe—"

    show yuri angry2 at p4_2
    voice audio.yuri_v_angry1b1
    yu "Shush, you! I’ll help you plan your wedding some other day! "
    yu "Now go get into your positions!"

    show jin shock2 at p4_4
    voice audio.jin_v_response1b1
    j "R-Right!"

    hide jin_wedding
    hide jin shock2
    hide emilia_wedding
    hide emilia amazed1
    with dissolve

    show yuri happy2 at p4_2
    voice audio.yuri_v_alright1a1
    yu "Alright, that’s almost everyone!"

    show yuri shock5 at p4_2
    voice audio.yuri_v_wait1c1
    yu "Wait, NO! We’re still missing the most important guest!"
    yu "Where the heck is Yoshi and the best man?!"

    show yoshi_wedding at p4_3
    show yoshi_ring1 at p4_3
    show yoshi talk3 at p4_3
    show aiden_wedding at p4_4
    show aiden comp1 at p4_4
    with dissolve

    voice audio.yoshi_v_ah2
    yo "A-Ah, hello guys! We’re sorry we’re late!"

    show goro comp2 at p4_1
    voice audio.goro_v_yoshi16a
    yo "You look wonderful, Yoshinori."

    show yoshi comp2 at p4_3
    voice audio.yoshi_v_thanks3
    yo "Th-Thank you, Goro. You look extra handsome as well."

    show aiden comp2 at p4_4
    voice audio.aiden_v_aww2a
    a "Awww, would you look at these lovebirds~ Can’t even wait for the altar!"

    show yuri rage1 at p4_2
    voice audio.yuri_v_aiden7a
    yu "Aiden! What the heck took you so long?! You were supposed to have Yoshi here an hour ago!"

    show aiden comp6 at p4_4
    voice audio.aiden_v_laugh1b1
    a "Aheheh, well you know I was cooking everything for the reception, and I was struggling to put my tie on! Good thing Yoshi came to help!"

    show yuri rage3 at p4_2
    voice audio.yuri_v_conj1a1
    yu "You were supposed to help Yoshi dress up! Not the other way around!"

    show yoshi comp3 at p4_3
    voice audio.yoshi_v_actually1a
    yo "I had actually been dressed for a half an hour already, and went looking for Aiden. "
    yo "When I found him, he was in just his apron in the kitchen as usual, hehe."

    show aiden play2 at p4_4
    voice audio.aiden_v_hey1a1
    a "Hey, if you’d have let me, I’d be at the ceremony in just that, too!"

    show yuri angry6 at p4_2
    voice audio.yuri_v_ugh2a
    yu "Ugh, well at least you’re here now!"

    show aiden comp5 at p4_4
    voice audio.aiden_v_comp3a
    a "Haha, relax, Yuri! It’s these two’s big day, after all! We should congratulate them!"

    show yuri angry2 at p4_2
    voice audio.yuri_v_rush1d1
    yu "We will! After the ceremony! Now come on, let’s get to the altar!"

    show yuri_wedding at p4_3
    show yuri angry1 at p4_3
    show yoshi_wedding at p4_2
    show yoshi_ring1 at p4_2
    show yoshi shock1 at p4_2
    with move

    show aiden shock2 at p4_4
    voice audio.aiden_v_shock5a
    a "Wah, Yuri!"

    show yuri happy2 at p4_3
    voice audio.yuri_v_alright1a1
    yu "Alright, Dad and Yoshi~ This is your big moment!"

    hide yuri_wedding
    hide yuri happy2
    hide aiden_wedding
    hide aiden shock2
    with moveoutright

    show goro_wedding at left2
    show goro_ring1 at left2
    show goro comp1 at left2
    show yoshi_wedding at right2
    show yoshi_ring1 at right2
    show yoshi sigh4 at right2
    with move

    voice audio.yoshi_v_relief1
    yo "Whew… It’s finally happening…"

    show goro play3 at left2
    voice audio.goro_v_heh1a
    g "Heh, feeling nervous, Yoshinori?"

    show yoshi comp3 at right2
    voice audio.yoshi_v_yeah4
    yo "Y-Yeah, I am a bit… My heart is pounding!"

    show goro comp2 at left2
    voice audio.goro_v_comp2a1
    g "You and I are together now, Yoshinori… "

    show yoshi comp1 at right2
    yo "..."

    show yoshi comp2 at right2
    voice audio.yoshi_v_right2
    yo "You’re right, Goro. "

    show goro comp3 at left2
    voice audio.goro_v_rush1d1
    g "Let’s go?"

    show yoshi comp3 at right2
    voice audio.yoshi_v_rush5
    yo "Together?"

    show goro happy1 at left2
    voice audio.goro_v_agree5a1
    g "Always..."

    $ renpy.music.stop(channel='music', fadeout=1.0)
    $ renpy.music.stop(channel='bgsound', fadeout=1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout=1.0)

    hide screen location
    hide screen timeline
    hide screen quick_menu
    $quick_menu = False
    scene cg white
    with Dissolve(2.0)
    $ renpy.pause (2.0, hard=True)

    play music old_familiar_home_string loop
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene cgg13 1
    with fade
    voice audio.officiator_vsg31_line1
    o "We are gathered here today to celebrate the union of Goro Nomoru and Yoshinori Nagira."

    voice audio.officiator_vsg31_line2
    o "They have both prepared their own vows, and I would like to give them this opportunity to share them with each other. Mr. Nagira?"

    $ renpy.pause (1.0, hard=True)
    voice audio.yoshi_vsg31_line1
    yo "Goro… We’ve both come so far since we first met here so many years ago."

    voice audio.yoshi_vsg31_line2
    yo "We’ve been apart, struggled when we’re together, and learned more about each other than we ever thought possible."

    voice audio.yoshi_vsg31_line3
    yo "I never thought the day would come where I could stand here with you, like this."

    voice audio.yoshi_vsg31_line4
    yo "But I couldn’t be happier than I am right now."

    voice audio.officiator_vsg31_line3
    o "Mr. Nomoru?"

    $ renpy.pause (1.0, hard=True)
    voice audio.goro_vsg31_line1
    g "Yoshinori… Even when I was at my lowest, you’ve always stayed by my side, helping me to overcome all the many challenges we’ve faced together."

    voice audio.goro_vsg31_line2
    g "Meeting and getting to know you was the best thing that’s ever happened to me, and I can’t believe it took so long for me to realize it."

    voice audio.goro_vsg31_line3
    g "Standing here now, I’m ready to spend the rest of my life with you. "

    voice audio.officiator_vsg31_line4
    o "And now, Goro Nomoru, do you take Yoshinori Nagira to be your husband?"

    voice audio.goro_vsg31_line4
    g "I do."

    voice audio.officiator_vsg31_line5
    o "Yoshinori Nagira, do you take Goro Nomoru to be your husband?"

    voice audio.yoshi_vsg31_line5
    yo "I do!"

    show cgg13 2 with Dissolve(0.25)
    voice audio.officiator_vsg31_line6
    o "I now declare you married! You may now kiss!"
    all "*cheering*"

    hide screen location
    hide screen timeline
    hide screen quick_menu
    $quick_menu = False
    scene cg white
    with Dissolve(2.0)
    $ renpy.pause (2.0, hard=True)
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene cg black
    with fade
    yo "{i}After the ceremony, we all went back to the mess hall for the reception. Everyone had a great time, and I loved every minute of the start of my new life with Goro.{/i}"
    yo "{i}I can’t wait to share the rest of my days with him!{/i}"

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black
    hide screen location
    hide screen timeline
    hide screen quick_menu
    $quick_menu = False
    with fade
    $ time_transition_spring_to_summer()
    $ renpy.pause (2.0, hard=True)

    $ season = season_summer
    $ day = "284"
    $ location = location_site
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_site9_spring_day with fade
    play music greatest_memories_casual loop
    play bgsound sfxloop_birds loop

    show yuri_autumn at left2
    show yuri norm1 at left2
    show emilia_autumn at right2
    show emilia relief2 at right2
    voice audio.emilia_v_relief2a
    e "Ah, it’s so nice to see this new part of our camp in full bloom. I feel like a proud mother seeing all my plants grow so prettily~"

    show yuri angry2 at left2
    voice audio.yuri_v_hey3a
    yu "Hey, I’m not letting you take all the credit! They’re my babies too!"

    show emilia explain4 at right2
    voice audio.emilia_v_think1
    e "It’s so hard to believe that we’ve been doing absolutely nothing for the past few weeks… considering how full our hands were for over half a year."

    show yuri sigh3 at left2
    voice audio.yuri_v_sigh2a
    yu "Yeah… I don’t think I’ll ever get used to being this laid back."

    show emilia talk3 at right2
    voice audio.emilia_v_conj1a
    e "Summer is right around the corner, though. The scouts will be coming back soon.  "

    show yuri excited2 at left2
    voice audio.yuri_v_yeah1b1
    yu "Yeah, I can’t wait to see the look on their faces when they see how big the camp is now! "
    yu "We should give them a tour on the first day, don’t you think? I think they’d really love that!"

    show emilia happy1 at right2
    voice audio.emilia_v_conj4b
    e "Honestly, I’m eager to meet the scouts. I’ll definitely give them a proper introduction."
    e "But they’d better not get on my bad side."

    show yuri play2 at left2
    voice audio.yuri_v_tease1b1
    yu "Ohhh… Are you gonna be our disciplinary committee? "

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    show emilia talk2 at right2
    voice audio.emilia_v_oh1a
    e "Speaking of which… looks like some people really can’t wait for summer."

    show emilia_autumn at p7_7
    show emilia norm3 at p7_7
    show yuri_autumn at p7_6
    show yuri norm1 at p7_6
    with move

    show darius_autumn at p7_2
    show darius norm1 at p7_2
    show lloyd_autumn at p7_1
    show lloyd angry2 at p7_1
    show yoichi_camp at p7_3
    show yoichi annoyed3 at p7_3
    show taiga_camp at p7_4
    show taiga annoyed1 at p7_4
    show jin_camp at p7_5
    show jin_glasses at p7_5
    show jin shock1 at p7_5
    with dissolve
    play music camping_time loop

    voice audio.lloyd_v_rush1a2
    l "Attention! Straighten your back! "
    l "You! Stop being all limp!"

    show jin shock2 at p7_5
    voice audio.jin_v_what3a
    j "Wh-What…? This is my normal posture, Lloyd…"

    show lloyd angry5 at p7_1
    voice audio.lloyd_v_annoyed1a1
    l "That’s SCOUTGRANDMASTER LLOYD to you!"
    l "From now on, you’ll do yoga two hours every morning to fix your posture!"

    show darius confused2 at p7_2
    voice audio.darius_v_think2b1
    d "Aren’t you being too harsh?"

    show yoichi playful1 at p7_3
    voice audio.yoichi_v_lloyd4a
    yi "Sorry I can’t hear your orders from up here, Pipsqueak!"
    yi "Grow five inches taller and then maybe I’ll listen."

    show lloyd rage3 at p7_1
    voice audio.lloyd_v_greet2d2
    l "HEY! That’s not how these things work!"

    show taiga playful2 at p7_4
    voice audio.taiga2_v_agree3a
    t "True. It’s too late for you to grow."

    show lloyd disappoint5 at p7_1
    voice audio.lloyd_v_ignored1c1
    l "EHEM, lucky for you two, I’m a professional, so I’ll let that slide!"

    show jin confused5 at p7_5
    voice audio.jin_v_think2a1
    j "So… What’s next?"

    show darius talk2 at p7_2
    voice audio.darius_v_think1a1
    d "Camping."

    show lloyd talk2 at p7_1
    voice audio.lloyd_v_agree3a1
    l "Right, camping! Let’s make a fire out of these two sticks!"

    show jin sigh6 at p7_5
    voice audio.jin_v_sigh1a
    j "I’m starting to regret this decision…"

    show yoichi angry3 at p7_3
    voice audio.yoichi_v_denial3a
    yi "I’m out. I have dogs to feed."

    show taiga angry2 at p7_4
    voice audio.taiga_v_whatthe1a
    t "Hell no! You’re not ditching, and leaving me to play house with these dorks!"
    t "Besides, it’d be really good training for them to deal with the wildest pinhead in the camp!"

    show yoichi annoyed1 at p7_3
    voice audio.yoichi_v_confused1a1
    yi "Who you calling pinhead?"

    show darius play2 at p7_2
    voice audio.darius_v_laugh1
    d "If you two join, I’ll give you a treat. Heard you like burgers and mallows."

    show taiga angry5 at p7_4
    show yoichi angry3 at p7_3
    yt "Ugh, fine."

    show lloyd excited3 at p7_1
    voice audio.lloyd_v_rush1c1
    l "Alright! March! Three two one! Three two one!"

    show jin confuseddn3 at p7_5
    voice audio.jin_v_confused1a3
    j "It’s supposed to be the other way around…"

    show darius relief2 at p7_2
    voice audio.darius_v_wait1a
    d "Shh…"

    show lloyd_autumn at p8_1
    show lloyd norm1 at p8_1
    show darius_autumn at p8_2
    show darius norm1 at p8_2
    show yoichi_camp at p8_3
    show yoichi normal1 at p8_3
    show taiga_camp at p8_4
    show taiga normal1 at p8_4
    show jin_camp at p8_5
    show jin_glasses at p8_5
    show jin shock1 at p8_5
    show emilia_autumn at p8_7
    show emilia norm3 at p8_7
    show yuri_autumn at p8_6
    show yuri norm1 at p8_6
    with move

    show aiden_camp at p8_8
    show aiden happy1 at p8_8
    with dissolve

    voice audio.aiden_v_hey2a1
    a "Hey, ya’ll! Food’s ready! I made hotdogs and burgers!"

    show taiga excited1 at p8_4
    voice audio.taiga2_v_excited2a
    t "*gasp* Burgers!"

    show yoichi playful1 at p8_3
    voice audio.yoichi_v_agree3a1
    yi "Alright! I’m done playing house with you, dorks! "

    hide taiga_camp
    hide taiga excited1
    hide yoichi_camp
    hide yoichi playful1
    with moveoutright

    show lloyd_autumn at p6_1
    show lloyd annoy2 at p6_1
    show darius_autumn at p6_2
    show darius norm1 at p6_2
    show jin_camp at p6_3
    show jin_glasses at p6_3
    show jin norm1 at p6_3
    show yuri_autumn at p6_4
    show yuri norm1 at p6_4
    show emilia_autumn at p6_5
    show emilia norm1 at p6_5
    show aiden_camp at p6_6
    show aiden norm1 at p6_6
    with move

    voice audio.lloyd_v_groan2a1
    l "And… There go my scouts."

    show aiden laugh1 at p6_6
    voice audio.aiden_v_laugh2a1
    a "Haha! Looks like y’all are having fun being scoutmasters! I bet you it’s gonna be way more fun when the real term starts!"

    show darius happy2 at p6_2
    voice audio.darius_v_excited1a1
    d "I’m excited."

    show jin perv5 at p6_3
    voice audio.jin_v_laugh1a
    j "I’m really looking forward to you all dominating me…"
    j "…with orders of course."

    show aiden tease1 at p6_6
    voice audio.aiden_v_perv1
    a "That’s more Gramps’ style! And trust me, he can get real rough!"

    show jin fudan2 at p6_3
    voice audio.jin_v_fudan1a1
    j "Oh my…"

    if score_goro > 24 and score_goro <= 49:
        show emilia confused2 at p6_5
        voice audio.emilia_v_conj3a
        e "Speaking of Sir Goro… When are he and Yoshi going to be back? "

        show yuri irked2 at p6_4
        voice audio.yuri_v_rush1d1
        yu "Give them a break, Emilia! Let them enjoy their special honeymoon!"

        show emilia angry2 at p6_5
        voice audio.emilia_v_annoyed2
        e "How come those two are allowed to go on dates and we’re not?!"

        show aiden play2 at p6_6
        voice audio.aiden_v_alright3b2
        a "No one’s stopping you~"

        show emilia rage4 at p6_5
        voice audio.emilia_v_what3a
        e "What?! So, you’re telling me I could’ve been out on a vacation instead of digging up soil and weeding for weeks?!"

        show darius relief2 at p6_2
        voice audio.darius_v_conj2a
        d "Well, you didn’t ask."

        show yuri tease2 at p6_4
        voice audio.yuri_v_hmph1a
        yu "Don’t act like you didn’t enjoy being here with us, Emilia! You were always the first one up doing all the chores!"

        show emilia eyeroll6 at p6_5
        voice audio.emilia_v_hmph1a
        e "It’s because I thought there was nothing else to do! I’ve been scammed!"

        show yuri tease4 at p6_4
        voice audio.yuri_v_conj2c2
        yu "Now you know what it feels like."

        show aiden relief2 at p6_6
        voice audio.aiden_v_glad1a
        a "Honestly, I’m glad those two spent some time together before we get busy again for the next term."

        show yuri laugh1 at p6_4
        voice audio.yuri_v_response2a1
        yu "I know right? It’s a really nice vacation do-over for them!"

        show lloyd laugh1 at p6_1
        voice audio.lloyd_v_aww1b1
        l "They’d been so excited for this since their wedding. It’s so adorable to see those two so madly in love."

        show yuri rage2 at p6_4
        voice audio.yuri_v_ugh3a
        yu "Maybe it’s adorable to YOU."

        show emilia angry2 at p6_5
        voice audio.emilia_v_bossy1a
        e "Hey, don’t change the subject! We need to go on a vacation too!"

        show yuri happy2 at p6_4
        voice audio.yuri_v_laugh1a1
        yu "If it helps, they texted me that they’re already on their way back."

        show emilia bold3 at p6_5
        voice audio.emilia_v_amazed1a
        e "If that’s the case, then pack your bags, Yuri! We’re going to see that new ‘JS’ movie!"

        hide yuri_autumn
        hide yuri happy2
        show yuri2_autumn at p6_4
        show yuri2 fangirl2 at p6_4
        voice audio.yuri_v_kyaa1a
        yu "KYAAAA! YES, YES! Count me in!"

        hide emilia_autumn
        hide emilia bold3
        hide yuri2_autumn
        hide yuri2 fangirl2
        with moveoutright

        show lloyd_autumn at p4_1
        show lloyd annoy1 at p4_1
        show darius_autumn at p4_2
        show darius bored1 at p4_2
        show jin_camp at p4_3
        show jin_glasses at p4_3
        show jin shock1 at p4_3
        show aiden_camp at p4_4
        show aiden wink2 at p4_4
        with move

        voice audio.aiden_v_alright1a1
        a "Alright now that the girls are gone, circlejerk anyone?!"

        show jin fudan3 at p4_3
        voice audio.jin_v_yes6a
        j "YES."

        show lloyd explain4 at p4_1
        voice audio.lloyd_v_disagree1a1
        l "Pass. I’ll go for the hotdogs."

        show darius tease2 at p4_2
        voice audio.darius_v_laugh1
        d "And I’ll go for your buns."

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
        scene cgg14:
            yalign 1.0 xalign 0.5
        with Dissolve(2.0)
        play music buddy_oath_casual loop
        play bgsound sfxloop_birds loop
        voice audio.goro_vsg32_line1
        g "Ahh… It’s good to be back…"

        voice audio.yoshi_vsa29_line1
        yo "We’ve only been gone for a couple days, but I missed Camp Buddy already."

        voice audio.yoshi_vsg32_line1
        yo "But I have to say, that honeymoon trip is the most fun I’ve ever had."

        voice audio.goro_vsg32_line2
        g "I’m glad you enjoyed it, Yoshinori. I was hoping we’d be able to go somewhere special once everything settled down."

        voice audio.goro_vsg32_line3
        g "And today marks exactly six months since we started dating, five months and 26 days since our engagement... and a month since our wedding."

        voice audio.yoshi_vsg32_line2
        yo "You kept count of all that?!"

        voice audio.goro_vsg32_line4
        g "Of course. It’s really special to me."

        voice audio.yoshi_vsg32_line3
        yo "Aww that’s really sweet, Goro…! "

        voice audio.goro_vsg32_line5
        g "*clears thoat* But now that we’ve had our fun, it’s time for us to get back to work."

        voice audio.yoshi_vsa29_line5
        yo "Yeah! The next term is only a few days away and the scouts are finally gonna see everything we worked hard on."

        voice audio.goro_vsg32_line6
        g "I can’t wait to see the look on their faces when they do. All the new buildings and the fun new activities we’ve prepared."

        voice audio.yoshi_vsg32_line4
        yo "Me too, Goro!"

        voice audio.goro_vsg32_line7
        g "Let’s go in, then? I’m sure everybody’s waiting for us inside."

        voice audio.yoshi_vsa29_line7
        yo "Yeah! We’re finally home!"

        $ renpy.music.stop(channel='music', fadeout = 6.0)
        $ renpy.music.stop(channel='bgsound', fadeout = 6.0)
        $ renpy.music.stop(channel='bgsound2', fadeout = 6.0)
        hide screen location
        hide screen timeline
        hide screen quick_menu
        $ quick_menu = False
        $ say_box = False
        show cgg14:
            yalign 1.0 xalign 0.5
            linear 5 yalign 0.0
        $ renpy.pause(6.0, hard=True)
        scene cg white with Dissolve(3.0)
        $ renpy.pause (2.0, hard=True)

        scene bg_theend with dissolve
        $ renpy.pause (5.0, hard=True)

        $persistent.routes_completed.append("goro")
        $renpy.save_persistent()
        #the end

        return

    elif score_goro > 49:
        show emilia confused2 at p6_5
        voice audio.emilia_v_conj3a
        e "Speaking of Sir Goro… where are he and Yoshi?! I haven’t seen them today."

        show yuri annoy2 at p6_4
        voice audio.yuri_v_yeah2a3
        yu "Oh, yeah, they’re both gone. They better not be sneaking around again and surprise me with daddy buttsex…!"

        show aiden shock2 at p6_6
        voice audio.aiden_v_wait1a1
        a "Wait, don’t you guys know? Today’s their honeymoon! "

        show lloyd talk4 at p6_1
        voice audio.lloyd_v_agree4b1
        l "Oh yeaaaahhh... I almost forgot about that. Mr. Clermont got them some special tickets to an island resort, right?!"

        show darius relief2 at p6_2
        voice audio.darius_v_amazed3
        d "Lucky."

        show jin daydream2 at p6_3
        voice audio.jin_v_fudan4a1
        j "I can only imagine all the sweaty, wet, island sex they’ll have there."

        show yuri rage3 at p6_4
        voice audio.yuri_v_ugh2a
        yu "Uh-uh, no thank you!"

        show emilia think3 at p6_5
        voice audio.emilia_v_think1
        e "Going out would be the best thing to do with so much free time. "

        show yuri amazed3 at p6_4
        voice audio.yuri_v_tease1b2
        yu "Ooooh! How about we go to the movies?! I heard there’s some new one called ‘JS’ out today~ "

        show emilia happy1 at p6_5
        voice audio.emilia_v_agree1a1
        e "Sure, I think I’ve finished all the chores for the day. Turns out they aren’t so bad when nobody is around."

        show yuri excited4 at p6_4
        voice audio.yuri_v_celebrate1a
        yu "I’ll go get my coat! Yipeee~"

        hide yuri_autumn
        hide yuri excited4
        hide emilia_autumn
        hide emilia happy1
        with moveoutright

        show lloyd_autumn at p4_1
        show lloyd annoy1 at p4_1
        show darius_autumn at p4_2
        show darius bored1 at p4_2
        show jin_camp at p4_3
        show jin_glasses at p4_3
        show jin shock1 at p4_3
        show aiden_camp at p4_4
        show aiden wink2 at p4_4
        with move

        voice audio.aiden_v_alright1a1
        a "Alright now that the girls are gone, circlejerk anyone?!"

        show jin fudan3 at p4_3
        voice audio.jin_v_yes6a
        j "YES."

        show lloyd explain4 at p4_1
        voice audio.lloyd_v_disagree1a1
        l "Pass. I’ll go for the hotdogs."

        show darius tease2 at p4_2
        voice audio.darius_v_laugh1
        d "And I’ll go for your buns."

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

        $ location = location_hotelroom
        show screen location
        show screen timeline
        show screen quick_menu
        $quick_menu = True
        scene bg_beach_resort_day with fade
        play music beachside_day loop
        play bgsound sfxloop_wavesday loop

        show goro_swim at p5_4
        show goro_ring2 at p5_4
        show goro comp1 at p5_4
        show yoshi_swim at p5_5
        show yoshi_ring2 at p5_5
        show yoshi relief2 at p5_5
        voice audio.yoshi_v_relief1
        yo "Whew! That was such a nice swim!"

        show goro relief2 at p5_4
        voice audio.goro_v_yeah1a1
        g "Yeah, this place is amazing. Our room even has a balcony overlooking the entire island…"

        show yoshi bold2 at p5_5
        voice audio.yoshi_v_oh2
        yo "Oh, I wanna check that out!"

        show goro play2 at p5_4
        voice audio.goro_v_think2a1
        g "Why don’t we sit there then while we’re drying off?"

        show goro_swim at left2
        show goro_ring2 at left2
        show goro relief1 at left2
        show yoshi_swim at right2
        show yoshi_ring2 at right2
        show yoshi relief4 at right2
        with move

        voice audio.yoshi_v_ah6
        yo "Ahhh… This is the life…"

        show goro relief4 at left2
        voice audio.goro_v_relief1a
        g "Just being here with you, bathing in the sun, with a cold drink in our hands… It feels like we’re in paradise."

        show yoshi comp2 at right2
        voice audio.yoshi_v_yeah2
        yo "Yeah… I’ve never been so spoiled in my life… I almost feel guilty about it."

        hide goro_swim
        hide goro_ring2
        hide goro relief4
        show goro2_swim at left2
        show goro2 play2 at left2
        voice audio.goro_v_comp2a1
        g "Well, don’t. We earned this trip. And the only things I really had to spend money on were the upgrades and extra amenities."

        hide yoshi_swim
        hide yoshi_ring2
        hide yoshi comp2
        show yoshi2_swim at right2
        show yoshi2_ring2 at right2
        show yoshi2 comp5 at right2
        voice audio.yoshi_v_unsure3a
        yo "I guess if you put it that way…"

        hide yoshi2_swim
        hide yoshi2_ring2
        hide yoshi2 comp5
        show yoshi_swim at right2
        show yoshi_ring2 at right2
        show yoshi bold2 at right2
        voice audio.yoshi_v_but2
        yo "But don’t get me wrong…! I’m really having fun today!"
        yo "For once, I can really enjoy my time with you without any work or distractions, knowing that we finished our project!"

        hide goro2_swim
        hide goro2 play2
        show goro_swim at left2
        show goro_ring2 at left2
        show goro comp2 at left2
        voice audio.goro_v_glad1a
        g "I’m glad you’re enjoying this, Yoshinori. I’ve been really looking forward to going somewhere special like this once everything settled down."

        show yoshi play3 at right2
        voice audio.yoshi_v_well1
        yo "Well, you have been taking me out on a lot of road trips ever since we got engaged!"

        show goro relief2 at left2
        voice audio.goro_v_satisfied1a
        g "I can’t help it. I just love spending time with you that much."
        g "And to be honest, this trip is extra special."

        show yoshi confused2 at right2
        voice audio.yoshi_v_oh1
        yo "Oh? What for?"

        hide goro_swim
        hide goro_ring2
        hide goro relief2
        show goro2_swim at left2
        show goro2 happy2 at left2
        voice audio.goro_v_actually1a
        g "Today marks exactly six months since we started dating, five months and 26 days since our engagement... and a month since our wedding."

        show yoshi shock2 at right2
        voice audio.yoshi_v_really3
        yo "You kept count of all that?!"

        hide goro2_swim
        hide goro2 happy2
        show goro_swim at left2
        show goro_ring2 at left2
        show goro comp3 at left2
        voice audio.goro_v_agree3a1
        g "Of course. It’s really special to me."
        g "And to celebrate that… I got something for you…"

        show goro_swim at center
        show goro_ring2 at center
        show goro comp1 at center
        with move

        show yoshi_necklace at right2
        with dissolve

        show yoshi shock3 at right2
        voice audio.yoshi_v_shock3
        yo "Wahh…! A necklace…?!"

        show goro relief2 at center
        voice audio.goro_v_satisfied2a
        g "Ah… It suits you perfectly…"

        hide yoshi_swim
        hide yoshi shock3
        hide yoshi_ring2
        hide yoshi_necklace
        show yoshi2_swim at right2
        show yoshi2_ring2 at right2
        show yoshi2_necklace at right2
        show yoshi2 awkward4 at right2
        voice audio.yoshi_v_amazed1a
        yo "Th-This looks crazy expensive…!! You didn’t have to."

        hide goro_swim
        hide goro_ring2
        hide goro relief2
        show goro2_swim at center
        show goro2 play3 at center
        voice audio.goro_v_well1a
        g "Well, since this trip was paid for, I had to use my honeymoon budget somewhere, right?"
        g "Besides, you’re more than worth it…"

        show yoshi2 comp2 at right2
        voice audio.yoshi_v_goro14
        yo "Goro… you’re way too romantic…"

        show goro2 play2 at center
        voice audio.goro_v_so3a
        g "Well, do you like it?"

        hide yoshi2_swim
        hide yoshi2_ring2
        hide yoshi2_necklace
        hide yoshi2 comp2
        show yoshi_swim at right2
        show yoshi_ring2 at right2
        show yoshi_necklace at right2
        show yoshi comp5 at right2
        voice audio.yoshi_v_thanks2
        yo "I do! I love it! Thank you!"
        yo "*kisses Goro*"

        hide goro2_swim
        hide goro2 play2
        show goro_swim at center
        show goro_ring2 at center
        show goro comp2 at center
        voice audio.goro_v_glad1a
        g "That makes me happy…"

        hide yoshi_swim
        hide yoshi_ring2
        hide yoshi_necklace
        hide yoshi comp5
        show yoshi2_swim at right2
        show yoshi2_ring2 at right2
        show yoshi2_necklace at right2
        show yoshi2 comp6 at right2
        voice audio.yoshi_v_aww1
        yo "Now I feel bad I didn’t get anything for you…"

        show goro relief4 at center
        voice audio.goro_v_alright2a1
        g "You don’t have to. I’m more than happy to be here with you…"

        show yoshi2 comp3 at right2
        voice audio.yoshi_v_rush1
        yo "At least let me make up for it…!"

        hide goro_swim
        hide goro_ring2
        hide goro relief4
        show goro2_swim at center
        show goro2 tease2 at center
        voice audio.goro_v_well1a
        g "Well…"
        g "I’d really love to see you in… nothing but that necklace…"

        show yoshi2 shy5 at right2
        voice audio.yoshi_v_agree1c
        yo "O-Of course…"

        hide yoshi2_swim
        hide yoshi2_ring2
        hide yoshi2_necklace
        hide yoshi2 shy5
        show yoshi2_naked2 at right2
        show yoshi2_ring2 at right2
        show yoshi2_necklace at right2
        show yoshi2_blush1 at right2
        show yoshi2 play1 at right2
        yo "..."

        show goro2_blush1 at center
        show goro2 tease5 at center
        voice audio.goro_v_laugh1a1
        g "Hehe… You’re already hard too…?"

        show yoshi2_naked2 at right3
        show yoshi2_ring2 at right3
        show yoshi2_necklace at right3
        show yoshi2_blush1 at right3
        show yoshi2 play2 at right3
        with move

        voice audio.yoshi_v_laugh1
        yo "I can’t help it… I’ve been thinking about doing it with you all day…"

        show goro2 tease3 at center
        voice audio.goro_v_agree5a1
        g "Me too… "

        scene cg black
        hide screen location
        hide screen timeline
        hide screen quick_menu
        $ quick_menu = False
        with fade

        jump day10_goro_8
        # if score_bot == score_top:
        #     $ position = renpy.random.randint(1, 2)
        #
        # if score_top > score_bot or position == 1:
        #     hide screen location
        #     hide screen timeline
        #     hide screen quick_menu
        #     $ quick_menu = False
        #     with fade
        #     $ say_box = False
        #     $ fp_stage = 'mgg5_b'
        #     $ success_jumpto = 'day10_goro_8'
        #     $ failed_jumpto = 'day10_goro_pe_aftersx'
        #     jump fp
        #
        # elif score_bot > score_top or position == 2:
        #     hide screen location
        #     hide screen timeline
        #     hide screen quick_menu
        #     $ quick_menu = False
        #     with fade
        #     $ say_box = False
        #     $ fp_stage = 'mgg5_f'
        #     $ success_jumpto = 'day10_goro_8'
        #     $ failed_jumpto = 'day10_goro_pe_aftersx'
        #     jump fp

label day10_goro_pe_aftersx:
    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black
    hide screen location
    hide screen timeline
    hide screen quick_menu
    $quick_menu = False
    with fade
    $ time_transition_day_to_sunset_summer()
    $ renpy.pause (2.0, hard=True)

    $ location = location_hotelroom
    $ time = timeline_timesunset
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene sxg8 20 with fade
    play music old_familiar_home_slow loop
    play bgsound sfxloop_wavesday loop

    voice audio.yoshi_vsg33_line1
    yo "Ahh… This was the perfect day, Goro…"

    voice audio.yoshi_vsg33_line2
    yo "We got to swim and fool around all day… and to top it all off, now we get to cuddle while watching the sunset… "

    voice audio.goro_vsg33_line1
    g "It really was a great day, wasn’t it Yoshinori?"

    show sxg8 21 with Dissolve(0.25)
    voice audio.goro_vsg33_line2
    g "But to be honest, I lost count of how many rounds we did this time."

    voice audio.goro_vsg33_line3
    g "I was getting worried you’d be sore from all that beating."

    voice audio.yoshi_vsg33_line3
    yo "I-I’m used to it… And I love it when you’re rough on me…"

    show sxg8 22 with Dissolve(0.25)
    voice audio.goro_vsg33_line4
    g "Hehe~ Sounds to me like you haven’t gotten enough even after all that."

    voice audio.yoshi_vsg33_line4
    yo "W-Well… I guess I could use a bit of a break to just chill here with you."

    show sxg8 23 with Dissolve(0.25)
    voice audio.goro_vsg33_line5
    g "Yeah… I’d like that too."

    show sxg8 24 with Dissolve(0.25)
    voice audio.goro_vsg33_line6
    g "Thank goodness I realized I really was content with the camp…"

    voice audio.goro_vsg33_line7
    g "And that I had the courage to propose to you…"

    voice audio.yoshi_vsg33_line5
    yo "Yeah… If it weren’t for that, we wouldn’t be together… "

    show sxg8 25 with Dissolve(0.25)
    voice audio.goro_vsg33_line8
    g "To think that we’ve only just begun this chapter… I can’t wait for what else we’ll do out there."

    voice audio.goro_vsg33_line9
    g "My future is bright as long as you’re in it…"

    voice audio.yoshi_vsg33_line6
    yo "Goro…"

    show sxg8 26 with Dissolve(0.25)
    voice audio.goro_vsg33_line10
    g "I love you, Yoshinori…"

    voice audio.yoshi_vsg33_line7
    yo "I love you too..."

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg white
    hide screen location
    hide screen timeline
    hide screen quick_menu
    $ quick_menu = False
    with Dissolve(3.0)
    $ renpy.pause (2.0, hard=True)

    scene bg_theend with dissolve
    $ renpy.pause (5.0, hard=True)

    $persistent.routes_completed.append("goro")
    $renpy.save_persistent()

    #the end
