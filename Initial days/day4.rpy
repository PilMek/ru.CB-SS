label day4:
    $ day = "04"
    $ time = timeline_timeday
    $ location = location_campsite
    $ working = True
    show screen quick_menu
    $quick_menu = True
    show screen timeline
    show screen location

    scene bg_campgrounds_autumn_day with fade
    play music buddy_oath_casual loop
    play bgsound sfxloop_birds loop

    show yoshi_autumn at center
    show yoshi explain2 at center
    voice audio.yoshi_v_relief1
    yo "Whew, it’s much quieter this morning. "

    hide yoshi_autumn
    hide yoshi explain2
    show yoshi2_autumn at center
    show yoshi2 think4 at center
    voice audio.yoshi_v_think4
    yo "I got up earlier than yesterday just in case something happened again."
    yo "Lloyd and Darius were gone from our cabin already so I thought their work might’ve started for the day, but I guess not."
    yo "The specialists probably won’t arrive for a while too… Maybe I should go out for a morning patrol first… "

    show yoshi2_autumn at p5_5
    show yoshi2 shock1 at p5_5
    with move

    show darius_yoga at p5_1
    show darius norm3 at p5_1
    show lloyd_yoga at p5_2
    show lloyd pain5 at p5_2
    with dissolve

    voice audio.lloyd_v_tired1b3
    l "Hnghhh!!! *huff* *huff*"

    show darius talk1 at p5_1
    voice audio.darius_v_wait1b
    d "Hold it for five more seconds."

    show lloyd tired5 at p5_2
    voice audio.lloyd_v_sigh2a
    l "Haaaa!"

    show darius happy2 at p5_1
    voice audio.darius_v_celebrate1b
    d "Great."

    show darius_yoga at left
    show darius talk1 at left
    show lloyd_yoga at center
    show lloyd tired5 at center
    show yoshi2_autumn at right
    show yoshi2 shock1 at right
    with move

    hide yoshi2_autumn
    hide yoshi2 shock1
    show yoshi_autumn at right
    show yoshi happy2 at right
    voice audio.yoshi_v_goodam1
    yo "G-Good morning, Lloyd and Darius!"

    show darius happy1 at left
    voice audio.darius_v_goodam2
    d "Good morning."

    show yoshi talk1 at right
    voice audio.yoshi_v_think3
    yo "What are you guys up to…?"

    show darius relief2 at left
    voice audio.darius_v_laugh1
    d "I’m sipping hot cocoa."

    show lloyd happy1 at center
    voice audio.lloyd_v_greet2a3
    l "Oh, hey, Yoshinori. I’m just doing my daily morning yoga."
    l "I always make sure to do plenty of stretching, especially if there’s gonna be a lot of physical labor during the day. "

    show lloyd talk2 at center
    voice audio.lloyd_v_conj2b3
    l "I hope you don’t mind the incense though. It helps me relax and loosen up."

    show yoshi comp2 at right
    voice audio.yoshi_v_comp2
    yo "It’s alright! It smells good, actually!"

    show lloyd laugh1 at center
    voice audio.lloyd_v_stayfit1b
    l "There’s also a lot of studies that say yoga makes you happier, healthier, and more flexible!"

    show darius tease2 at left
    voice audio.darius_v_conj1a2
    d "He’s doing it to be taller."

    show lloyd sigh5 at center
    voice audio.lloyd_v_darius6c
    l "Dar, I left that out for a reason, you know…"

    show yoshi comp5 at right
    voice audio.yoshi_v_well1
    yo "Well, it’s nice you’re taking good care of your health! I usually chop wood in the morning to wake my muscles up!"

    show lloyd happy2 at center
    voice audio.lloyd_v_yoshi2c
    l "You should join me sometime! If you’re stressed, I have cleansing crystals that could help too! You’ll be feeling rejuvenated in no time!"

    hide yoshi_autumn
    hide yoshi comp5
    show yoshi2_autumn at right
    show yoshi2 comp3 at right
    voice audio.yoshi_v_sure2
    yo "S-Sure, I’ll let you know when I need it…! "

    show lloyd talk4 at center
    voice audio.lloyd_v_conj6a1
    l "So, do you always wake up this early too? "

    hide yoshi2_autumn
    hide yoshi2 comp3
    show yoshi_autumn at right
    show yoshi happy1 at right
    voice audio.yoshi_v_yes1
    yo "During the summer term, yes! But, this time, I just wanted to be available in case anyone needs something."

    show lloyd laugh2 at center
    voice audio.lloyd_v_laugh1a1
    l "Haha, you’re quite the role model, as always! Believe it or not, you’re one of the people I looked up to when it came to leadership."

    hide yoshi_autumn
    hide yoshi happy1
    show yoshi2_autumn at right
    show yoshi2 think5 at right
    voice audio.yoshi_v_really1
    yo "Ah… R-Really? "

    show lloyd happy1 at center
    voice audio.lloyd_v_agree2b1
    l "Yeah! You always had a way of getting everyone to work together while making sure they were having fun too!"
    l "If only you knew how much of that I was able to apply in my job as an architect."

    hide yoshi2_autumn
    hide yoshi2 think5
    show yoshi_autumn at right
    show yoshi talk3 at right
    voice audio.yoshi_v_response1a
    yo "I can imagine. You must be used to working with a lot of people to get a project done."

    show lloyd happy2 at center
    voice audio.lloyd_v_agree2b2
    l "Yeah! In a sense, it’s like your job as a scoutmaster!"
    l "And now, you’re kinda dealing with something even more than that – having to oversee not only my team, but the other incoming specialists too."

    show darius think5 at left
    voice audio.darius_v_think3a
    d "Uh… I’m sorry to interrupt you two, but…"
    d "There’s a guy who’s been walking around the entrance for a while now."

    hide yoshi_autumn
    hide yoshi talk3
    show yoshi2_autumn at right
    show yoshi2 confused2 at right
    voice audio.yoshi_v_what3
    yo "Wh-What? "

    show darius_yoga at p6_1
    show darius think5 at p6_1
    show lloyd_yoga at p6_2
    show lloyd happy2 at p6_2
    show yoshi2_autumn at p6_3
    show yoshi2 confused2 at p6_3
    with move

    show jin_autumn at p6_6
    show jin tired6 at p6_6
    show jin_glasses at p6_6
    with dissolve

    voice audio.jin_v_pant2c
    mys_jin "*pant* *pant*"

    show jin worry4 at p6_6
    voice audio.jin_v_worry1b3
    mys_jin "Oh no, where is everybody…? "

    show lloyd confused2 at p6_2
    voice audio.lloyd_v_confused1a3
    l "He’s not one of your staff, is he?"

    show yoshi2 confused3 at p6_3
    voice audio.yoshi_v_no4
    yo "N-No, I don’t recognize him at all."

    show darius think4 at p6_1
    voice audio.darius_v_think1a1
    d "I think he’s lost."

    hide yoshi2_autumn
    hide yoshi2 confused3
    show yoshi_autumn at p6_3
    show yoshi talk1 at p6_3
    voice audio.yoshi_v_greet2b1
    yo "Let me go and talk to him!"

    show yoshi_autumn at p6_5
    show yoshi happy1 at p6_5
    with move

    voice audio.yoshi_v_goodam1
    yo "Good morning! I’m Yoshinori Nagira, a scoutmaster here at Camp Buddy. How can I help you?"

    #jin cg
    show jin sigh3 at p6_6
    show jin_glasses at p6_6
    voice audio.jin_vs5_line1
    mys_jin "O-Oh, thank goodness I’m in the right place!"

    voice audio.jin_vs5_line2
    mys_jin "Please forgive my intrusion – 'I uhhh let myself into the property."

    show jin talk3 at p6_6
    show jin_glasses at p6_6
    voice audio.jin_vs5_line3
    mys_jin "I am looking for a… Mr. Goro Nomoru? I have an appointment with him today…!"

    show yoshi talk3 at p6_5
    voice audio.yoshi_vs5_line1
    yo "Ah! I assume Clermont Inc. sent you?"

    show jin happy2 at p6_6
    voice audio.jin_vs5_line4
    j "Y-Yes, my name is Hyunjin Choi…! "

    voice audio.jin_vs5_line5
    j "I’m an IT specialist, and I’m here to perform an inspection and determine the camp’s technological needs."

    show yoshi happy2 at p6_5
    voice audio.yoshi_vs5_line2
    yo "It’s a pleasure to meet you, uhh… Mr. Choi?"

    show jin smile1 at p6_6
    voice audio.jin_vs5_line6
    j "Please, just call me Jin!"

    #end cg

    show yoshi happy1 at p6_5
    voice audio.yoshi_v_agree1b1
    yo "Of course, and you can call me Yoshi! "
    yo "Here with me are Architect Sirius and Foreman Najjar! They were also sent by Clermont Inc. to work on this expansion project!"

    show darius_yoga at p4_1
    show darius think4 at p4_1
    show lloyd_yoga at p4_2
    show lloyd confused2 at p4_2
    show yoshi_autumn at p4_3
    show yoshi happy1 at p4_3
    show jin_autumn at p4_4
    show jin happy1 at p4_4
    show jin_glasses at p4_4
    with move

    voice audio.lloyd_v_greet2a3
    l "Hey, it’s nice to meet you, man! You can just call me Lloyd – looking forward to working with you!"

    show jin relief2 at p4_4
    voice audio.jin_v_relief2b
    j "It’s a relief to know I’ll be working with someone around my age too, Lloyd! "

    show lloyd laugh2 at p4_2
    voice audio.lloyd_v_laugh1a1
    l "I’m a lot older than you think, but I get that a lot, haha!"

    show darius happy1 at p4_1
    voice audio.darius_v_greet2
    d "I’m Darius. *shakes Hyunjin’s hand*"

    show jin awkward3 at p4_4
    voice audio.jin_v_oof1c
    j "O-Oof… Y-You have really big hands, Darius… And a tight grip too…"

    show darius bold5 at p4_1
    voice audio.darius_v_agree2a
    d "I use them a lot."

    show jin awkward5 at p4_4
    voice audio.jin_v_conj4b1
    j "A-Anyway…! I-I apologize if I’m late! I was up all night preparing for this…!"

    show yoshi talk1 at p4_3
    voice audio.yoshi_v_ah1
    yo "Ah, you’re actually quite early – almost everyone else is still in their cabins, so please don’t worry about it!"

    show lloyd comp2 at p4_2
    voice audio.lloyd_v_agree2a3
    l "Yeah, man. It’s only, like, 6:00 AM! Chill!"

    show jin scared2 at p4_4
    voice audio.jin_v_sorry1b2
    j "I-I’m sorry…! It’s just, I was supposed to be here a day earlier, but I had to reschedule."
    j "I-I’m not really used to working with a large group of people, so I’ve been preparing myself since this is a big job opportunity for me."

    show lloyd talk2 at p4_2
    voice audio.lloyd_v_shock1a1
    l "Oh, I get you! I never jump into the action without proper prep, or else it’d really hurt my ass!"
    l "That’s why I always make sure to have Dar here to help me, so things will go smoothly and be much more enjoyable!"

    show darius talk1 at p4_1
    voice audio.darius_v_agree1a
    d "Yes."

    show jin perv5 at p4_4
    voice audio.jin_v_ah2a
    j "A-Ah, r-right…! In a project sense, of course…!"

    show yoshi talk3 at p4_3
    voice audio.yoshi_v_anyway2
    yo "Will you be staying here at camp for the span of this project too?"

    show jin happy1 at p4_4
    voice audio.jin_v_yes1a
    j "Yes…! I was informed that I need to stay and work here on-site to ensure maximum output since we have a tight schedule."

    show yoshi happy2 at p4_3
    voice audio.yoshi_v_alright1
    yo "Alright! I hope you don’t mind sharing the same quarters I’m in though. All the other cabins have been occupied by the construction workers."

    show jin comp5 at p4_4
    voice audio.jin_v_oh3a
    j "O-Oh…! I… don’t mind that at all! "

    show yoshi explain2 at p4_3
    voice audio.yoshi_v_conj2a
    yo "If that’s the case, shall we get you and your suitcases settled in? You must be tired from your trip."

    show jin talk6 at p4_4
    voice audio.jin_v_ah2a
    j "A-Ah, that won’t be necessary for now!"
    j "I also don’t want to be late for my meeting with the camp president…! "

    show yoshi talk3 at p4_3
    voice audio.yoshi_v_agree1b1
    yo "Oh, of course! Let me bring you to his office!"
    yo "We’ll go ahead, you two! Sorry to cut our conversation short! "

    show lloyd happy1 at p4_2
    voice audio.lloyd_v_response1b1
    l "It’s fine! We need to start working too! It was a pleasure meeting you, Jin!"

    show jin laugh3 at p4_4
    voice audio.jin_v_comp4a
    j "The pleasure’s all mine! "

    show yoshi happy1 at p4_3
    voice audio.yoshi_v_request2a
    yo "Right this way, Jin! "

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
    scene bg_office_autumn_day with fade
    play music old_familiar_home loop

    play sound sfx_doorknock
    $ renpy.pause (1.0, hard=True)
    show goro_autumn at center
    show goro talk2 at center
    voice audio.goro_v_greet2a1
    g "Come in."

    show goro_autumn at p4_1
    show goro talk1 at p4_1
    with move

    show yoshi_autumn at p4_3
    show yoshi happy1 at p4_3
    show jin_autumn at p4_4
    show jin awkward1 at p4_4
    show jin_glasses at p4_4
    with dissolve

    voice audio.yoshi_v_goodam1
    yo "Good morning, sir! Mr. Hyunjin Choi just arrived. He’s the IT specialist scheduled for a meeting with you today."

    show goro talk3 at p4_1
    voice audio.goro_v_agree2a2
    g "Ah, yes. I’ve been expecting you, Mr. Choi. Please, take a seat."

    show yoshi_autumn at left
    show yoshi happy1 at left
    show goro_autumn at center
    show goro talk3 at center
    show jin_autumn at right
    show jin awkward4 at right
    show jin_glasses at right
    with move

    voice audio.jin_v_greet1d1
    j "I hope I’m not interrupting you by coming earlier than scheduled, Mr. Nomoru."

    show goro happy2 at center
    voice audio.goro_v_response2a1
    g "It’s no problem. I’m just having my morning coffee."
    g "Is it alright with you if we address each other by our first names?"

    show jin comp3 at right
    voice audio.jin_v_yessir2b
    j "O-Of course, sir! You can even call me Jin, for short!"

    show goro happy3 at center
    voice audio.goro_v_amazed2a1
    g "Great. I want to make sure you’re comfortable during your stay here. Mr. Clermont told me quite a lot about you and your work."

    show jin happy4 at right
    voice audio.jin_v_really2a
    j "O-Oh, really? He must be talking about the online bookstore I developed for his publishing company…!"

    show goro play2 at center
    voice audio.goro_v_amazed1a1
    g "He did show me that in one of our meetings. Pretty impressive work."

    show jin laugh4 at right
    voice audio.jin_v_thanks1b3
    j "Thank you, Sir Goro!"

    show goro bold2 at center
    voice audio.goro_v_actually1a
    g "I have to say, I'm pleasantly surprised meeting you today. When Mr. Clermont said he’d send an IT expert, I thought it would be someone who’s a lot older."

    show jin happy1 at right
    voice audio.jin_v_yeah3b
    j "I-I was thinking the same thing, sir…! You look so stylish for a camp president!"

    show goro laugh1 at center
    voice audio.goro_v_laugh2b1
    g "Hahaha, spare me the compliments, Jin. "

    show yoshi shock2 at left
    voice audio.yoshi_v_amazed1a
    yo "Wow… This is probably the first time a new guy hasn’t been intimidated meeting you, sir…"

    hide goro_autumn
    hide goro laugh1
    show goro2_autumn at center
    show goro2 think3 at center
    voice audio.goro_v_think1a1
    g "Apparently, it’s always better to be gentle with any first time."

    show jin comp6 at right
    voice audio.jin_v_laugh3c
    j "Ah… Hehehe…"

    hide goro2_autumn
    hide goro2 think3
    show goro_autumn at center
    show goro disappoint3 at center
    voice audio.goro_v_sigh1a
    g "To give you a bit of history, Jin – as this camp’s president, I used to lead strictly, always charging in with an iron fist."

    show jin awkward3 at right
    voice audio.jin_v_gulp1a
    j "*gulp*"

    show goro happy2 at center
    voice audio.goro_v_but2b
    g "But I gave my word to Yoshinori here that I’ll try to take things slowly and make people more relaxed with this approach."

    show yoshi laugh1 at left
    voice audio.yoshi_v_laugh1
    yo "Haha, it seems like you’re working on your people-handling skills!"

    show jin awkward4 at right
    voice audio.jin_v_oh4c
    j "Oh… "

    show goro happy1 at center
    voice audio.goro_v_well1b
    g "I’m doing just that with Jin here, and he seems to be very pleased."

    show jin comp3 at right
    voice audio.jin_v_thanks2a
    j "A-Ahh… W-Well, I really appreciate it, sir. "
    j "I hope you can use me… and my skills… for the camp!"

    show goro happy3 at center
    voice audio.goro_v_rush5a1
    g "That is great to hear. Now, let’s get on to business."

    show goro talk3 at center
    voice audio.goro_v_jin2a
    g "Jin, I have appointed Yoshinori here as your guide while you conduct an inspection of the camp. "
    g "You’ll be identifying what’s needed to implement all of the technological goals of the approved proposal. "

    show goro explain2 at center
    voice audio.goro_v_comp1c1
    g "I understand that we’re quite far behind when it comes to adapting to the digital age, so we’re counting on your knowledge and recommendations to make the necessary improvements."
    g "Please also bear with us for being so outdated, even about the simplest of things. We’re hoping you can better educate us and help us adapt throughout this entire project."

    show jin happy2 at right
    voice audio.jin_v_yessir1a
    j "Yes, sir!"
    j "If it’s alright with you, I’d like to start here in your office!"

    hide goro_autumn
    hide goro explain2
    show goro2_autumn at center
    show goro2 think5 at center
    voice audio.goro_v_think1a2
    g "Hmm… The only piece of technology we have here is our personal computer."

    show jin talk4 at right
    voice audio.jin_v_oh4a
    j "Oh… "

    show yoshi explain2 at left
    voice audio.yoshi_v_well1
    yo "We know it’s fairly outdated… and it runs pretty slow, so we barely touch it most days."

    show jin_autumn at right2
    show jin shock2 at right2
    show jin_glasses at right2
    with move

    voice audio.jin_v_whoa3a
    j "Whoa… This computer is at least a decade old…"

    hide goro2_autumn
    hide goro2 think5
    show goro_autumn at center
    show goro shy6 at center
    voice audio.goro_v_sigh1a
    g "I believe it’s even older than that, since I got it before the camp was even established…"

    show jin shock4 at right2
    voice audio.jin_v_shock1a
    j "Oh wow, so it’s basically a prehistoric relic…"
    j "Well, let’s give it a chance and take a closer look."

    play sound sfx_pcboot
    show jin confused1 at right2
    voice audio.jin_v_think1a1
    j "Hmm…"
    j "None of the fans are running – I’m shocked it even boots up at all…! "

    show yoshi think2 at left
    voice audio.yoshi_v_think1a
    yo "It does take a while to turn on… We usually just go to the internet café nearby if we need something done digitally."
    yo "One of our tech-savvy scouts last term actually went there to upload a promotional video for our fundraising campaign."

    show jin confused5 at right2
    voice audio.jin_v_yeah1a
    j "Yeah, I don’t think this one was even built to connect to the internet."

    hide yoshi_autumn
    hide yoshi think2
    show yoshi2_autumn at left
    show yoshi2 shy5 at left
    voice audio.yoshi_v_well3
    yo "W-Well… We just thought we didn’t need it… since we’re an adventure-themed summer camp…"
    yo "Gadgets are also banned from our daily activities…"

    show jin shock2 at right2
    voice audio.jin_v_wait1b
    j "Wait, does that mean even the scoutmasters don’t carry phones around?"

    $working = False
    $shuffle_menu()
    menu():
        j "Wait, does that mean even the scoutmasters don’t carry phones around?{fast}"
        "We should've allowed devices.":
            $working = True
            $score_goro -= 2
            show yoshi2 think5 at left
            voice audio.yoshi_v_yeah4
            yo "Yeah… Thinking about it, we probably should’ve allowed devices."
            yo "It would’ve been much safer for the campers that way."

            hide goro_autumn
            hide goro shy6
            show goro2_autumn at center
            show goro2 disappoint3 at center
            voice audio.goro_v_hmph1a
            g "Hmph. It’s not as simple as it sounds, Yoshinori."
            g "We can’t efficiently educate the campers on survival skills with technology to distract them."

            show goro2 disappoint2 at center
            voice audio.goro_v_conj2a1
            g "It also goes against the spirit of the camp, especially the social aspect of it."
        "I'm not sure why we don't.":
            $working = True
            $score_goro -= 1
            show yoshi2 think5 at left
            voice audio.yoshi_v_yeah4
            yo "Yeah… I-I’m actually not sure why we don’t…"

            show goro disappoint3 at center
            voice audio.goro_v_sigh1a
            g "*sigh* How could you forget, Yoshinori?"
            g "Here at Camp Buddy, we encourage practical and survival skills not only for the sake of tradition, but also for the spirit of the camp itself."
        "We try to encourage survival skills.":
            $working = True
            $score_goro += 1
            hide yoshi2_autumn
            hide yoshi2 shy5
            show yoshi_autumn at left
            show yoshi talk2 at left
            voice audio.yoshi_v_yes1
            yo "Yes, but for a reason."
            yo "We try to encourage practical and survival skills in the more traditional way as much as possible."

            show goro talk1 at center
            voice audio.goro_v_agree6a2
            g "That’s right. If the scouts are allowed to rely on technology, they’d be less focused on the lessons we’re trying to teach them."
            g "This could actually put them in more danger because they lack the knowledge needed to adapt in any given situation."
        "It would defeat the spirit of the camp.":
            $working = True
            $score_goro += 2
            hide yoshi2_autumn
            hide yoshi2 shy5
            show yoshi_autumn at left
            show yoshi talk2 at left
            voice audio.yoshi_v_yes1
            yo "Yes, we want to set a good example for our scouts."
            yo "More so, we believe it would go against the spirit of the camp, especially the social aspect of it."

            show goro talk1 at center
            voice audio.goro_v_agree5a1
            g "Definitely. We encourage our campers to engage with one another on a personal level."
            g "They enrolled here to experience and enjoy activities that they wouldn’t get to normally, where technology is often present."

    show jin think1 at right2
    voice audio.jin_v_think1a1
    j "Hmm… I understand that it’s due to the nature of this camp… But for the sake of emergencies, productivity, and marketing, we really need to consider integrating technology, at least on the administrative end."
    j "For example, installing security cameras and putting a hub here in the office will allow the staff to maintain safety, reducing the need for daily patrols."

    hide yoshi2_autumn
    hide yoshi2 think5
    hide yoshi2 talk2
    show yoshi_autumn at left
    show yoshi think2 at left
    voice audio.yoshi_v_think1a
    yo "Yeah… And that would give me more time to do other important tasks…"

    hide goro2_autumn
    hide goro2 disappoint2
    hide goro disappoint3
    hide goro talk1
    show goro_autumn at center
    show goro think3 at center
    voice audio.goro_v_think1a1
    g "We’ve been so stuck in our ways that we didn’t even consider all of this before…"

    show jin comp3 at right
    show jin_autumn at right
    show jin_glasses at right
    with move
    voice audio.jin_v_agree2a2
    j "I understand, sir. People are usually afraid of change because it’s something they’re not familiar with and are worried to impair what already works."
    j "But I assure you, with my services, we’ll be able to integrate new things without having to compromise on the true spirit of your camp!"

    show goro happy1 at center
    voice audio.goro_v_praise1a
    g "Excellent. I see now why Mr. Clermont chose you for this job."

    show jin daydream2 at right
    voice audio.jin_v_thanks1c2
    j "Th-Thank you, sir! I’ll make sure I’m worth your thrust… I mean, trust!"

    show goro happy3 at center
    voice audio.goro_v_anyway2
    g "Anyway, I believe we’ve covered everything for this introductory meeting. Welcome to the team, Jin!"

    show jin laugh3 at right
    voice audio.jin_v_comp4a
    j "It’s my pleasure, sir! Thank you for having me…!"

    show goro talk1 at center
    voice audio.goro_v_conj7a
    g "Now, if you don’t mind, I’ll be heading out for a while. Yoshinori, please assist Jin here with whatever he needs for today."

    show yoshi talk1 at left
    voice audio.yoshi_v_yessir1
    yo "Yes, sir!"

    hide goro_autumn
    hide goro talk1
    with dissolve

    show yoshi_autumn at left2
    show yoshi confused2 at left2
    show jin_autumn at right2
    show jin laugh3 at right2
    show jin_glasses at right2
    with move

    voice audio.yoshi_v_jin5
    yo "Should we get you moved into our cabin now, Jin? Or get you some breakfast first, at least?"

    show jin talk5 at right2
    voice audio.jin_v_think1a2
    j "Ah, I would like to work right away, if that’s okay. Thanks for the offer though."

    show yoshi happy1 at left2
    voice audio.yoshi_v_response3a
    yo "No problem. Is there anything I can help you with now?"

    show jin talk2 at right2
    voice audio.jin_v_conj1a2
    j "It’s the other way around, actually! I’ve been told that you don’t have a stay-in computer technician here at camp. "
    j "So, I would like to teach you how to work with the computer and troubleshoot it in case no one is around to fix it."

    show yoshi comp2 at left2
    voice audio.yoshi_v_response1b
    yo "That makes sense! To be honest, the most I’ve ever done with the computer is turn it on to read e-mails…"

    show jin sigh5 at right2
    voice audio.jin_v_oof1c
    j "Oof… We’re gonna have to take the whole day to get you all caught up…"

    show yoshi worry2 at left2
    voice audio.yoshi_v_sorry1a1
    yo "Ah… I apologize. I’m probably going to be a lot to deal with when it comes to using computers – I barely know how the old one here works."

    show jin explain3 at right2
    voice audio.jin_v_conj2a3
    j "Well, we’re not going to use that PC anymore. I think using it would cause more headaches instead."
    j "In its current state, it won’t even scratch off a portion of our scope. It would be much faster and cheaper to build a new one."

    show jin bold2 at right2
    voice audio.jin_v_comp2a1
    j "Luckily, I came prepared! I assumed the worst and that the camp didn’t have a working PC, so I have a pre-built one for you guys in one of my suitcases here!"

    show yoshi talk3 at left2
    voice audio.yoshi_v_oh1
    yo "Oh… So that’s what you’ve been carrying… "

    show jin grin1 at right2
    voice audio.jin_v_yeah4a
    j "Yup! It will take me a little while to assemble this new one though."
    j "You can assist me, and I’ll show you what each part does and how everything works!"

    show yoshi happy1 at left2
    voice audio.yoshi_v_sure1
    yo "Sure! Feel free to order me around to do whatever you like! I’m your personal slave for the day!"

    show jin shy2 at right2
    voice audio.jin_v_ah3a
    j "A-Ahh… The way you say it sounds like… "
    j "A-Anyway, let’s get started…!"

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
    $ time_transition_day_to_sunset_fall()

    $ location = location_office
    $ time = timeline_timesunset
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_office_autumn_sunset with fade
    play music sunset_stroll loop

    show jin_autumn at left2
    show jin happy1 at left2
    show jin_glasses at left2
    show yoshi_autumn at right2
    show yoshi norm1 at right2
    voice audio.jin_v_okay1c
    j "Okay… This new PC is all set up! It just needs to finish installing all of the software and programs, then it should be good to go!"

    show yoshi happy1 at right2
    voice audio.yoshi_v_amazed3
    yo "That’s awesome! After helping you, I’ve started to understand a little better how everything works!"

    show yoshi comp2 at right2
    voice audio.yoshi_v_thanks2
    yo "Thank you for taking so much time to teach me. The way you explained everything to me step by step made me realize how simple it actually was."
    yo "I do feel bad that it took us all afternoon though… You probably could’ve finished a lot faster if it weren’t for me."

    show jin laugh1 at left2
    voice audio.jin_v_comp5a1
    j "Oh, it’s not a problem! It was actually fun teaching someone the stuff I do!"
    j "Besides, the internet here is super slow, so it’s taking a long time to download everything anyway—"

    play sound sfx_stomachgrowl
    show jin awkward5 at left2
    $ renpy.pause(2.0, hard=True)
    voice audio.jin_v_sorry2a1
    j "A-Ah, sorry about that…! I forgot to have breakfast before I showed up today, haha! "

    show yoshi worry2 at right2
    voice audio.yoshi_v_oops1
    yo "Oh no! And we worked all the way through lunch too! You must be starving!"

    show jin comp3 at left2
    voice audio.jin_v_comp1a1
    j "It’s okay…! I’m used to skipping meals anyway! I tend to work on a very weird schedule… "
    j "Whenever I realize I’m hungry, I just go to the nearest convenience store and grab something there."

    show yoshi happy2 at right2
    voice audio.yoshi_v_disagree3
    yo "Oh, you don’t have to do that here! Our chef prepares three meals a day for everyone at camp!"
    yo "We should really get you something to eat. Let’s head to the mess hall – dinner should be about ready!"

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
    scene bg_messhall_autumn_sunset with fade
    play bgsound sfxloop_crowd loop

    show yoshi_autumn at left2
    show yoshi norm1 at left2
    show jin_autumn at right2
    show jin shock2 at right2
    show jin_glasses at right2
    voice audio.jin_v_whoa2c
    j "Wh-Whoa…! This place is so crowded!"

    show yoshi talk3 at left2
    voice audio.yoshi_v_yes8
    yo "Ah, yes! The mess hall is usually full during mealtimes. It’s a bit more packed than usual since the workers for the project moved in yesterday!"

    show jin shy5 at right2
    voice audio.jin_v_think2b1
    j "You guys have quite the crowd here, huh? And most of them are… buff… guys…?"

    show yoshi happy2 at left2
    voice audio.yoshi_v_laugh1
    yo "Oh, haha! Most of them are construction workers, so they do tend to be more fit."

    show jin awkward3 at right2
    voice audio.jin_v_agree3b1
    j "I… see."

    show yoshi comp5 at left2
    voice audio.yoshi_v_comp5
    yo "I hope you’re not intimidated by them, everyone here is very friendly!"

    show yoshi_autumn at p7_1
    show yoshi comp5 at p7_1
    show jin_autumn at p7_2
    show jin awkward3 at p7_2
    show jin_blush at p7_2
    show jin_glasses at p7_2
    with move

    show aiden_apron2 at p7_7
    show aiden happy1 at p7_7
    with dissolve

    play music go_with_the_flow loop
    voice audio.aiden_v_orderup1b
    a "Order up! Two steak slabs coming right up!"

    show jin shock1 at p7_2
    j "…!"

    show darius_autumn at p7_5
    show darius norm1 at p7_5
    show lloyd_autumn at p7_4
    show lloyd happy1 at p7_4
    with dissolve

    voice audio.lloyd_v_aiden1a
    l "Over here, Aiden!"

    show aiden_apron2 at p7_6
    show aiden play2 at p7_6
    with move

    voice audio.aiden_v_atyourservice1
    a "I put some of my creamy special sauce on it, since you liked it so much yesterday~ "

    show lloyd relief5 at p7_4
    voice audio.lloyd_v_agree2b1
    l "Yeah, it’s so good covering your meat, I can never get enough of it. "

    show darius bold2 at p7_5
    voice audio.darius_v_amazed3
    d "Stuff me up."

    show aiden tease2 at p7_6
    voice audio.aiden_v_perv1
    a "Make sure to savor the taste when you swallow, alright~?"

    hide jin_autumn
    hide jin shock1
    hide jin_blush
    hide jin_glasses
    show jin2_autumn at p7_2
    show jin2_blush at p7_2
    show jin2 fudan3 at p7_2
    show jin2_glasses at p7_2
    voice audio.jin_v_wah2c
    j "WAH! Wh-What’s going on here?! Where am I exactly?!"

    show yoshi confused2 at p7_1
    voice audio.yoshi_v_huh2
    yo "Huh? What’s the matter, Jin?"

    show jin2 fudan2 at p7_2
    voice audio.jin_v_amazed1a1
    j "I-Is no one else seeing what I’m seeing…?!"

    show jin2 fudan3 at p7_2
    voice audio.jin_v_fudan5a1
    j "Th-That guy over there…! H-He’s serving food… NAKED! "

    hide yoshi_autumn
    hide yoshi confused2
    show yoshi2_autumn at p7_1
    show yoshi2 shy5 at p7_1
    hide jin2_autumn
    hide jin2 fudan3
    hide jin2_blush
    hide jin2_glasses
    show jin2_autumn at p7_2
    show jin2 fudan3 at p7_2
    show jin2_blush at p7_2
    show jin2_glasses at p7_2
    voice audio.yoshi_v_oh2
    yo "Oh… That’s actually one of our scoutmasters… He’s in charge of food service and camp maintenance."
    yo "And about his attire… I forgot to tell you ahead of time, but he has this habit of wearing “less” to cool down from all his work…"

    show yoshi2 shy6 at p7_1
    voice audio.yoshi_v_laugh1
    yo "As strange as it sounds, it’s actually quite normal around here…"

    show aiden shock1 at p7_6
    show jin2 comic4 at p7_2
    voice audio.jin_v_what4a
    j "THIS IS NORMAL HERE?!" with vpunch

    hide lloyd_autumn
    hide lloyd relief5
    hide darius_autumn
    hide darius norm1
    with dissolve

    show yoshi2_autumn at left
    show yoshi2 shy6 at left
    show jin2_autumn at center
    show jin2 comic4 at center
    show jin2_blush at center
    show jin2_glasses at center
    show aiden_apron2 at right
    show aiden happy1 at right
    with move

    voice audio.aiden_v_yoshi1b
    a "Oh~ Hey, Yoshi! "

    hide yoshi2_autumn
    hide yoshi2 shy6
    show yoshi_autumn at left
    show yoshi sigh4 at left
    voice audio.yoshi_v_aiden11
    yo "Aiden, how many times have we talked about this…? You knew there were new people coming today…"
    yo "You could’ve at least put something on so you don’t catch our guests off guard."

    show aiden pout2 at right
    voice audio.aiden_v_hey1c1
    a "Hey!! I am wearing something! See?! I’m wearing undies underneath right now! "

    show jin2 comic1 at center
    voice audio.jin_v_wah4b
    j "WAHHH!! BULGE!!!"

    show yoshi angry3 at left
    voice audio.yoshi_v_aiden12
    yo "Aiden! Put your apron down! "

    show aiden tease1 at right
    voice audio.aiden_v_oho1a
    a "Oho~ Is this the new guy? He’s quite the twink!"

    show jin2 fudan5 at center
    voice audio.jin_v_hngh3a
    j "Hngh! T-Twink?!"

    show yoshi talk1 at left
    voice audio.yoshi_v_ehem1b
    yo "This is Jin, he’s our new technology specialist. I was going to bring him here earlier, but we had to get to work first!"

    show jin2 shy3 at center
    voice audio.jin_v_greet1d4
    j "H-Hello… Mr.… Uhh—"

    show aiden laugh1 at right
    voice audio.aiden_v_greet2c
    a "—Aiden! Nice to meet you, Jin! "
    a "You look like you could use a meal or two! You’ve come to the right place!"

    show aiden tease2 at right
    voice audio.aiden_v_jin8a
    a "How about I whip out my nice footlong, think that’ll fill you up?"

    show jin2 dizzy2 at center
    voice audio.jin_v_fudan1a1
    j "F-Footlong?!"

    show yoshi irked3 at left
    voice audio.yoshi_v_aiden12
    yo "A-Aiden!! "

    show aiden laugh3 at right
    voice audio.aiden_v_comp1a2
    a "Haha! I’m just kidding, Jin! I just love teasing newcomers like you!  "

    show aiden_apron2 at right2
    show aiden laugh3 at right2
    with move

    a "Something tells me that you and I are gonna have a good time here at camp~!"

    hide jin2_autumn
    hide jin2 dizzy2
    hide jin2_blush
    hide jin2_glasses
    show jin_autumn at center
    show jin comp6 at center
    show jin_blush at center
    show jin_glasses at center
    voice audio.jin_v_laugh3a
    j "A-Ahehe… I’m sure we… *gulp* definitely will…"

    show yoshi angry5 at left
    voice audio.yoshi_v_ehem1b
    yo "*ehem* I apologize, Jin. Aiden is a very friendly person, and he can often be quite… physical as well."

    show jin perv5 at center
    voice audio.jin_v_comp8b1
    j "I-It’s fine… I’m sure I can get used to it… "

    show aiden_apron2 at right
    show aiden wink2 at right
    with move

    voice audio.aiden_v_laugh2a1
    a "Haha! I like this guy! He knows how to “ride” along ~"

    hide yoshi_autumn
    hide yoshi angry5
    show yoshi2_autumn at left
    show yoshi2 sigh4 at left
    voice audio.yoshi_v_sigh3a
    yo "*sigh* Aiden, can we just get something to eat? Jin hasn’t had a meal yet today."

    show aiden happy1 at right
    voice audio.aiden_v_agree2a1
    a "Oh, right on time! I just finished serving everyone else, so we can have dinner together!"

    show aiden tease1 at right
    voice audio.aiden_v_oho2a
    a "It’s the perfect chance for me to get to know Jin more… intimately. "

    show aiden relief2 at right
    voice audio.aiden_v_celebrate1a2
    a "Finally! It’s about time we had an official tech guy around here!"
    a "I’m the closest they’ve got since I know a thing or two about electrical work. But boy, let me tell you, it’s not the same at all, not one bit!"

    hide jin_blush
    show jin talk4 at center
    voice audio.jin_v_oh3a
    j "O-Oh…! I thought you were just the chef here?"

    show aiden happy2 at right
    voice audio.aiden_v_well1b1
    a "Well, I am! I’m also the laundryman, gardener, pool-boy, or any kind of “job” you want me to do – I’m at your service!"

    show jin think6 at center
    voice audio.jin_v_shock1b
    j "You’re pretty “well rounded”, I see…"

    show aiden tease1 at right
    voice audio.aiden_v_oho1a
    a "Oho~ Looks like you want some “buns” with your dinner~"

    show jin awkward2 at center
    voice audio.jin_v_gulp1a
    j "*gulp*"

    hide yoshi2_autumn
    hide yoshi2 sigh4
    show yoshi_autumn at left
    show yoshi angry3 at left
    voice audio.yoshi_v_no2
    yo "Not in front of our salad, Aiden…!"

    hide yoshi_autumn
    hide yoshi angry3
    show yoshi2_autumn at left
    show yoshi2 sigh1 at left
    voice audio.yoshi_v_sigh3a
    yo "*sigh* I’m so sorry about him, Jin."

    show jin awkward4 at center
    voice audio.jin_v_comp7a
    j "I-It’s not a big deal though…!"

    show aiden tease4 at right
    voice audio.aiden_v_laugh1a1
    a "Hehe, “deal-though”…"

    show jin comp2 at center
    voice audio.jin_v_conj1c2
    j "I-I’d much prefer that you guys are comfortable with yourselves around me!"
    j "It’s just… my imagination has been running wild since I arrived here for some reason… "

    show aiden happy3 at right
    voice audio.aiden_v_conj2b1
    a "See, Yoshi? Jin’s cool with it!"

    show jin daydream2 at center
    voice audio.jin_v_fudan3a1
    j "M-More like hot actually…"

    hide yoshi2_autumn
    hide yoshi2 sigh1
    show yoshi_autumn at left
    show yoshi explain2 at left
    voice audio.yoshi_v_ehem1b
    yo "*ehem* But as Aiden was saying, feel free to approach him if you need something as well."

    show jin comp5 at center
    voice audio.jin_v_okay2a
    j "Okay…!"
    j "There’s one thing I wanted to ask though… How come only one person does all the chores?"

    $working = False
    $shuffle_menu()
    menu():
        j "There’s one thing I wanted to ask though… How come only one person does all the chores?{fast}"
        "It's what he likes doing.":
            $working = True
            $score_aiden -= 2
            show yoshi happy2 at left
            voice audio.yoshi_v_comp2
            yo "I’m sure Aiden doesn’t mind them! It’s what he likes doing after all!"

            hide aiden_apron2
            hide aiden happy3
            show aiden2_apron2 at right
            show aiden2 shy2 at right
            voice audio.aiden_v_think2a
            a "Yeah. I, uhh… guess you could say that."
        "We're looking to hire more people to help.":
            $working = True
            $score_aiden -= 1
            show yoshi think2 at left
            voice audio.yoshi_v_actually1a
            yo "We actually used to have more staff a couple years ago to do these tasks."
            yo "Thankfully, we’re planning to hire more people to help, starting next term. "

            show aiden comp6 at right
            voice audio.aiden_v_comp1b2
            a "Either way, I really don’t mind doing them. It’s what keeps these muscles alive after all!"
        "I wish I could've helped him more.":
            $working = True
            $score_aiden += 1
            show yoshi comp2 at left
            voice audio.yoshi_v_yeah1
            yo "Yeah, I know how difficult it must’ve been for Aiden to solo the past couple years. I wish I could’ve helped him more."

            show aiden comp6 at right
            voice audio.aiden_v_yoshi3b
            a "Oh, come on, Yoshi! We both know you’ve been busy with your own tasks during the term. Besides, you’ve really been helping me with chores this off-season!"
        "We wouldn't have made it this far without him.":
            $working = True
            $score_aiden += 2
            show yoshi comp2 at left
            voice audio.yoshi_v_actually1a
            yo "Aiden is really skilled at anything he does! We honestly wouldn’t have made it this far without him."

            show aiden comp6 at right
            voice audio.aiden_v_yoshi3b
            a "Oh, shucks, Yoshi. You’re flattering me too much in front of Jin, hahaha!"

            show yoshi comp5 at left
            voice audio.yoshi_v_but3
            yo "But really, it never fails to amaze me just how much work you do around here compared to the rest of us."
    show jin think5 at center
    voice audio.jin_v_conj3a1
    j "I do have to admit, when I saw in the job briefing that there are only four full-time employees here at the camp, I wondered how you all managed to keep everything running…"
    j "Especially during the summer term when you have so many scouts around…"

    show yoshi talk1 at left
    voice audio.yoshi_v_ah3
    yo "A-Ah, that’s actually what I’m in charge of! I usually engage the campers with activities and make sure their time here at camp is memorable and meaningful. "

    show jin happy1 at center
    voice audio.jin_v_laugh1a
    j "It must’ve been nice that you guys had a little bit of a break before this project began then, huh?"

    hide aiden2_apron2
    hide aiden2 shy2
    show aiden_apron2 at right
    show aiden comp2 at right
    voice audio.aiden_v_aww3a
    a "Haha, not exactly – poor Yoshi here’s been losing his mind without stuff to keep him busy!"

    show yoshi think2 at left
    voice audio.yoshi_v_well1
    yo "Before the workers arrived, there wasn’t much to do, even when I helped you with the chores. "
    yo "It’s different from the work that I’m used to, but I’m just glad to be useful again."

    show jin talk4 at center
    voice audio.jin_v_agree3a1
    j "Ah, I see..."

    show yoshi_autumn at p5_1
    show yoshi think2 at p5_1
    show jin_autumn at p5_2
    show jin talk4 at p5_2
    show jin_glasses at p5_2
    show aiden_apron2 at p5_3
    show aiden comp2 at p5_3
    with move

    show yoichi_autumn at p5_4
    show yoichi laugh2 at p5_4
    show taiga_autumn at p5_5
    show taiga normal3 at p5_5
    with dissolve

    voice audio.yoichi_v_laugh1a5
    yi "Hah, I knew I picked up a different scent today! The smell of coffee and old clothes is coming from that K-drama guy over there!"

    show taiga confused1 at p5_5
    voice audio.taiga_v_doubt1
    t "Seriously? How do you even keep track of everyone’s scent here?!"

    show yoichi angry1 at p5_4
    voice audio.yoichi_v_yoshi1a
    yi "Hey, Sheriff Brokeback! Who is this guy?"

    show yoshi confused2 at p5_1
    voice audio.yoshi_v_yoichi7
    yo "Yoichi, I thought you were over calling me that nickname!"

    show yoshi talk3 at p5_1
    voice audio.yoshi_v_jin3
    # yo "Jin, this is Yoichi and Taiga. They’re scouts here, but they stayed on as full-time volunteers."

    show jin happy2 at p5_2
    voice audio.jin_v_oh1b
    j "Oh, I see! Hello, nice to meet you guys! I’m Jin! I was sent here to work on tech upgrades for the camp!"

    hide yoichi_autumn
    hide yoichi angry1
    show yoichi_autumn at p5_4
    show yoichi annoyed1 at p5_4
    voice audio.yoichi_v_lame2a
    yi "Great. Another nerd who looks like he doesn’t have friends, —"

    show jin shock2 at p5_2
    voice audio.jin_v_shock2a
    j "Ack!"

    show yoichi angry3 at p5_4
    voice audio.yoichi_v_groan2a1
    yi "—never goes out of his house, and only lives off instant noodles."

    show yoshi angry2 at p5_1
    voice audio.yoshi_v_yoichi1
    yo "Yoichi! Where are your manners?!"

    show taiga angry5 at p5_5
    voice audio.taiga_v_whatthe2b
    t "Wow, he read you to filth, huh…?"

    hide yoichi_autumn
    hide yoichi angry3
    show yoichi_autumn at p5_4
    show yoichi panic3 at p5_4
    voice audio.yoichi_v_disgust1a
    yi "Eugh! Since when did you start talking like Spaghetti-boy?!"

    hide yoshi_autumn
    hide yoshi angry2
    show yoshi2_autumn at p5_1
    show yoshi2 angry5 at p5_1
    voice audio.yoshi_v_sigh3a
    yo "*sigh* I’m so sorry about Yoichi’s behavior, Jin. He’s rather hostile when it comes to meeting strangers…"

    show taiga sigh2 at p5_5
    voice audio.taiga_v_sigh1
    t "He annoys everyone else here too, but you’ll get used to him."

    show yoichi angry1 at p5_4
    voice audio.yoichi_v_taiga5a
    yi "Shut up, Dynamite!"

    show jin sigh5 at p5_2
    voice audio.jin_v_sigh2a
    j "H-He’s not wrong though..."
    j "I am kind of a shut-in, so I don’t often get the chance to make new friends, even online."

    show jin comp2 at p5_2
    voice audio.jin_v_thanks3a
    j "That’s why I’m really thankful of Mr. Clermont for putting me in a job where I have to be outdoors and around plenty of people to work with."
    j "I really needed a change in scenery, and to stop coding all alone in a dark room."

    show jin confuseddn2 at p5_2
    voice audio.jin_v_conj3a3
    j "Though I’m surprised he was able to pick all that up from just my smell… "

    show taiga playful2 at p5_5
    voice audio.taiga_v_agree3a
    t "Yeah, he’s part dog, so don’t be too surprised if he pees in your room to mark his territory."

    show yoichi rage2 at p5_4
    voice audio.yoichi_v_greet1d1
    yi "HEY!"

    hide yoshi2_autumn
    hide yoshi2 angry5
    show yoshi_autumn at p5_1
    show yoshi irked1 at p5_1
    voice audio.yoshi_v_ehem1b
    yo "*ehem* Please give Jin some space to enjoy his meal properly, you two."

    show yoichi annoyed4 at p5_4
    voice audio.yoichi_v_wait2a
    yi "Speaking of which, how come Gayvid and Goliath get steak for dinner while the rest of us get fish and grass?!"

    show jin confused3 at p5_2
    voice audio.jin_v_think2a1
    j "Is he talking about Lloyd and Darius…?"

    show taiga talking3 at p5_5
    voice audio.taiga_v_conjunction3c
    # t "Yeah, we met them a little while ago. Everything was going well until Yoichi called them names."
    t "Shorty was fuming, so I had to drag him away before the giant finished him."

    show aiden happy3 at p5_3
    voice audio.aiden_v_no2a1
    a "Nah, Darius wouldn’t hurt a fly! "

    show yoichi playful1 at p5_4
    voice audio.yoichi_v_laugh1a1
    yi "Hah! He may be twice as huge, but I can still put up a fight! Wait till he sees how I take his meat!!"

    show jin sigh5 at p5_2
    voice audio.jin_v_sigh1b
    j "…Okay. I give up."

    show yoshi talk1 at p5_1
    voice audio.yoshi_v_anyway2
    yo "Anyway, Yoichi. If you’re still hungry, you’re welcome to join us."

    show aiden tasty1 at p5_3
    voice audio.aiden_v_orderup1a
    a "Two salmon fillets and Caesar salads coming right up!"

    show yoichi pain1 at p5_4
    show taiga pain2 at p5_5
    yt "BLECH!"

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black with fade

    yo "{i}After our dinner, Jin and I went back to the office to finish up the computer setup.{/i}"

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
    play bgsound sfxloop_night loop
    play music ready_for_tomorrow loop

    show yoshi_autumn at left2
    show yoshi norm1 at left2
    show jin_autumn at right2
    show jin norm2 at right2
    show jin_glasses at right2
    voice audio.jin_v_response1a2
    j "There we go! Everything’s installed and ready to go!"

    show yoshi shock2 at left2
    voice audio.yoshi_v_amazed1a
    yo "Wow, it’s so different from our old PC… and it runs so fast too!"

    show jin happy2 at right2
    voice audio.jin_v_comp2a3
    j "It’ll run faster once we get your internet here upgraded! But that’s work for another day!"

    show yoshi_autumn at p5_1
    show yoshi shock2 at p5_1
    show jin_autumn at p5_2
    show jin norm4 at p5_2
    show jin_glasses at p5_2
    with move

    show yuri_autumn at p5_5
    show yuri shock3 at p5_5
    with dissolve

    voice audio.yuri_v_oh3c
    yu "O-Oh! Sorry! I thought there was nobody in here!"

    show yuri bold2 at p5_5
    voice audio.yuri_v_shock1c1
    yu "Oh my! Who’s this fine gentleman?"

    show yoshi happy2 at p5_1
    voice audio.yoshi_v_ah1
    yo "Ah, I believe you two haven’t met yet! This is Jin! He’s the tech specialist that we were expecting today!"
    yo "Jin, this is Yuri, one of my fellow scoutmasters. She is also Sir Goro’s daughter."

    show yuri comp2 at p5_5
    voice audio.yuri_v_sorry1a1
    yu "I’m sorry I couldn’t meet you a little earlier, Jin! The workers kept me busy all day long today!"
    yu "I hope you’ve found Camp Buddy welcoming at least!"

    show jin fudan1 at p5_2
    j "..."

    show yoshi confused2 at p5_1
    voice audio.yoshi_v_huh1
    yo "What’s with all the stuff you’re carrying?"

    show yuri laugh1 at p5_5
    voice audio.yuri_v_oh1a
    yu "Oh, these? It’s just some stuff I unboxed from some of my crates when I finished work today."

    show jin fudan5 at p5_2
    j "A-Aaa…"

    show jin_autumn at p5_4
    show jin fudan5 at p5_4
    show jin_glasses at p5_4
    with move

    $ renpy.music.stop(channel='music', fadeout = 2.0)
    show yuri doom2 at p5_5
    voice audio.yuri_v_confused1a2
    yu "E-Eh…?"

    show jin scheme2 at p5_4
    voice audio.jin_v_sorry1b1
    j "I-I’m s-sorry… but… that book you’re holding…"
    j "Is that… the limited edition… rare… unavailable-on-the-market…"

    play music here_they_come loop
    hide jin_autumn
    hide jin scheme2
    hide jin_glasses
    show jin2_autumn at p5_4
    show jin2 excited4 at p5_4
    show jin2_glasses at p5_4
    voice audio.jin_v_fudan1b3
    j "…“HOMERUN!” DOUJINSHI?!" with vpunch

    hide yuri_autumn
    hide yuri doom2
    show yuri2_autumn at p5_5
    show yuri2 fangirl4 at p5_5
    voice audio.yuri_v_shock2a
    yu "*GASP*"
    yu "H-How did you know?!"

    show jin2 amazed1 at p5_4
    voice audio.jin_v_amazed2a
    j "I… played the game that comic is based on… and I’m a big, no… HUGE fan!"

    show yuri2 fangirl3 at p5_5
    voice audio.yuri_v_confused4a1
    yu "*gasp* Are you…? C-Could it be?!"

    hide yoshi_autumn
    hide yoshi confused2
    show yoshi2_autumn at p5_1
    show yoshi2 awkward3 at p5_1
    voice audio.yoshi_v_uh1a
    yo "Uhh… What’s going on…?"

    show yuri2 fangirl2 at p5_5
    voice audio.yuri_v_shock1a1
    yu "Y-You like BL too?!"

    show jin2 amazed3 at p5_4
    voice audio.jin_v_yes6c
    j "Yes!!! I LOVE IT!!"

    show yuri2 laugh3 at p5_5
    voice audio.yuri_v_omg1b
    yu "OMG, I CAN’T BELIEVE I FOUND ANOTHER ONE LIKE ME!!!"

    show jin2 excited4 at p5_4
    voice audio.jin_v_amazed1a1
    j "H-How did you get your hands on that?! It’s been phased out for years!"

    show yuri2 drool1 at p5_5
    voice audio.yuri_v_response2a1
    yu "I know, right?! It took me so long to get this copy! But the yaoi gods blessed me when I saw on a forum that a store was selling one signed copy! "

    hide yuri2_autumn
    hide yuri2 drool1
    show yuri_autumn at p5_5
    show yuri amazed3 at p5_5
    voice audio.yuri_v_conj2d1
    yu "Yoshinori was even kind enough to buy it at the capital for me!"

    show jin2 bold2 at p5_4
    voice audio.jin_v_whoa1a
    j "This is the only one I was missing from my collection at home! I already have everything from this artist circle except for this!"
    j "I pledged to myself that if I found someone selling it, I’d definitely buy it – no matter how high the price!"

    show jin2 shock3 at p5_4
    voice audio.jin_v_confused2a2
    j "But… I’m very up to date on all the forums! How could I have missed this sale?!"

    show yuri excited2 at p5_5
    voice audio.yuri_v_laugh1a1
    yu "Hehe! Well, you’re looking at the number one bidder in BL black market! "

    show jin2 comic5 at p5_4
    voice audio.jin_v_wait5b
    j "WAIT! DON’T TELL ME… YOU’RE PINKBUTTERFLY69?!"

    show yuri bold4 at p5_5
    voice audio.yuri_v_agree2a1
    yu "Hihi~ That’s right~"

    show jin2 amazed3 at p5_4
    voice audio.jin_v_amazed1a1
    j "I can’t believe it! You’re a legend! I’ve read all your fanfics! I love them so much!"

    hide yuri_autumn
    hide yuri bold4
    show yuri2_autumn at p5_5
    show yuri2 scared2 at p5_5
    voice audio.yuri_v_omg1a
    yu "OMG! I can’t believe you’ve read them! How embarrassing! "
    yu "What’s your favorite genre? "

    show jin2 perv5 at p5_4
    voice audio.jin_v_conj2c1
    j "W-Well, I like them all, but I prefer… *ehem* muscles the most!"

    show yuri2 drool1 at p5_5
    voice audio.yuri_v_kyaa1b
    yu "Kyaaa! Who doesn’t like muscles, right?!"

    show jin2 excited4 at p5_4
    voice audio.jin_v_fudan1a3
    j "I really can’t believe that I’m talking to THE pinkbutterfly69… and I’m looking at the long-lost “HomeRun!” doujinshi… "

    hide yuri2_autumn
    hide yuri2 drool1
    show yuri_autumn at p5_5
    show yuri happy3 at p5_5
    voice audio.yuri_v_well1a
    yu "Well, you can borrow it if you want~ "

    show jin2 amazed1 at p5_4
    voice audio.jin_v_really5c
    j "You’d let me?! Really?! Awww!! Thank you so much!! You’re a goddess from heaven!"
    j "Oh! In return, I’ll lend you my 10TB hard drive full of hardcore BL! They’re all uncensored too! Fresh off MyBreedingManGagged!"

    hide yuri_autumn
    hide yuri happy3
    show yuri2_autumn at p5_5
    show yuri2 ahegao1 at p5_5
    voice audio.yuri_v_kyaa1a
    yu "Kyaaaaaaaa!!!! I’d love that so, so much!! It’s a deal! "

    hide jin2_glasses
    hide yoshi2_autumn
    hide yoshi2 confused2
    show yoshi2_autumn at left
    show yoshi2 awkward3 at left
    show jin2_autumn at center
    show jin2 amazed1 at center
    show jin2_glasses at center
    show yuri2_autumn at right
    show yuri2 ahegao1 at right
    with move

    hide yoshi2_autumn
    hide yoshi2 awkward3
    show yoshi_autumn at left
    show yoshi awkward3 at left
    voice audio.yoshi_v_awkward2
    yo "Err…"
    yo "Y-You’re really into this stuff too… Jin? "

    hide jin2_autumn
    hide jin2 amazed1
    hide jin2_glasses
    show jin_autumn at center
    show jin awkward6 at center
    show jin_glasses at center
    voice audio.jin_v_ah4a
    j "A-Ahh… S-Sorry… I lost my composure… I’m just overwhelmed!"

    show yoshi laugh2 at left
    voice audio.yoshi_v_laugh1
    yo "Haha! It’s quite alright, I’m used to Yuri having moments like this all the time! "
    yo "I’m actually surprised you two resonate so much! "

    hide yuri2_autumn
    hide yuri2 ahegao1
    show yuri_autumn at right
    show yuri tease2 at right
    voice audio.yuri_v_agree3a
    yu "Hehe! Of course, Yoshi, us BL lovers gotta stick together! "

    show yoshi happy2 at left
    voice audio.yoshi_v_think3
    yo "I was wondering why you were acting a little odd while I was touring you around today. I guess this explains a lot."

    show jin sigh3 at center
    voice audio.jin_v_sorry1b1
    j "I’m sorry… I tried to hide it since it was inappropriate behavior…"
    j "But everyone I met kept saying suggestive things left and right… I wasn’t sure if everyone knew my dirty little secret…"

    show yoshi comp2 at left
    voice audio.yoshi_v_comp2
    yo "Oh, don’t think like that, Jin! We encourage everyone’s hobbies and interests here at Camp Buddy! So please feel free to express yourself!"

    show jin shy2 at center
    voice audio.jin_v_conj2c3
    j "W-Well… I just don’t want to make anyone feel uncomfortable… I promised myself I’d do my best to keep everything professional at this job."

    show yoshi comp5 at left
    voice audio.yoshi_v_well1
    yo "Well, you’ve already worked hard, even on your first day! I think you deserve to loosen up a little!"

    show jin sigh5 at center
    voice audio.jin_v_sigh1c
    j "*sigh* You did it again…"

    show yoshi confused3 at left
    voice audio.yoshi_v_huh4b
    yo "H-Huh??"

    show yuri happy1 at right
    voice audio.yuri_v_anyway2a
    yu "Anywaaay, what did you boys work on today?"

    show yoshi happy2 at left
    voice audio.yoshi_v_ah1
    yo "Ah! Jin replaced our office computer with a much better one! He even taught me how to use and troubleshoot it!"

    show yuri amazed2 at right
    voice audio.yuri_v_yeah2a3
    yu "Oh yeah, I noticed it as soon as I got in here! It looks really cool, Jin! Thank you!"

    show jin comp3 at center
    voice audio.jin_v_comp6b3
    j "Y-You’re welcome."

    show yuri tease1 at right
    voice audio.yuri_v_actually1a
    yu "I’m actually shocked you were able to teach Yoshi about computers too. He’s such a caveman when it comes to anything tech. Must’ve taken the whole day, am I right?"

    show yoshi annoy3 at left
    voice audio.yoshi_v_rush1
    yo "Come on, you don’t have to rub it in my face, Yuri."

    show yuri talk2 at right
    voice audio.yuri_v_oh1a
    yu "Oh, and I noticed we have a new printer too?"

    show jin happy1 at center
    voice audio.jin_v_yeah4a
    j "Yeah. It’s ten times more ink-efficient than the old one. I recommended this one when I found that you guys print out a lot of pamphlets and ad materials."
    j "I-It also has a scanner too, Yuri…! Mr. Clermont wanted to make sure you guys have all the basic office equipment."

    hide yuri_autumn
    hide yuri talk2
    show yuri2_autumn at right
    show yuri2 fangirl2 at right
    voice audio.yuri_v_kyaa1a
    yu "Kyaa! That means I don’t have to go out and get the side-eye at internet cafés whenever I ask them to scan naked gay men making love to each other!"

    show jin scheme2 at center
    voice audio.jin_v_please3b
    j "O-Once you make soft copies of your collection, please share them with me too…"

    hide yuri2_autumn
    hide yuri2 fangirl2
    show yuri_autumn at right
    show yuri amazed3 at right
    voice audio.yuri_v_omg1a
    yu "OMG! That gives me an idea, Jin! I could get a physical copy of all your stuff too! You’ll let me print them out, right?!"

    hide yoshi_autumn
    hide yoshi annoy3
    show yoshi2_autumn at left
    show yoshi2 sigh4 at left
    voice audio.yoshi_v_sigh3a
    yo "*sigh* Try not to go overboard, Yuri…"

    show yuri pout1 at right
    voice audio.yuri_v_hmph1a
    yu "Hmph, killjoy! Young Yoshi would’ve said yes!"

    show jin shock4 at center
    voice audio.jin_v_confused1a1
    j "Huh? You guys grew up together??"

    hide yoshi2_autumn
    hide yoshi2 sigh4
    show yoshi_autumn at left
    show yoshi talk3 at left
    voice audio.yoshi_v_oh2
    yo "O-Oh… Sort of! Yuri, Aiden, Lloyd, Darius and I were actually from the very first batch of Camp Buddy scouts. Sir Goro was even our scoutmaster back then!"

    show jin shock2 at center
    voice audio.jin_v_whoa1a
    j "Whoa! That’s big news to me…! "

    show yoshi laugh1 at left
    voice audio.yoshi_v_laugh1
    yo "Haha, we’re just as surprised! Even though we took different paths after that first term, we ended up being reunited like this – and for the future of the camp too!"

    show jin thinkdn3 at center
    voice audio.jin_v_think1a3
    j "That’s really interesting… It makes me want to know more about this camp’s history…"

    show yuri bold2 at right
    voice audio.yuri_v_here1a
    yu "Look no more! I have the perfect thing right here!"

    show cg fade at truecenter
    show fx1 at fx_pos
    with dissolve

    voice audio.yoshi_v_really6
    yo "D-Do you really carry that around all the time, Yuri…?"

    voice audio.yuri_v_agree1b1
    yu "Yup! This journal has all my precious scout memories! And they’re mostly about Camp Buddy’s debut!"

    hide cg fade
    hide fx1
    with dissolve

    show jin happy2 at center
    voice audio.jin_v_amazed2c
    j "That’s really cool! I would love to read through it and learn the history of the camp."
    j "I think understanding the camp’s origins would really help me with my work here."

    show yoshi talk3 at left
    voice audio.yoshi_v_ah1
    yo "Ah! That actually gives me an idea!"
    yo "Why don’t we work together to transcribe the journal and its pictures online? We could set up a section on the website Jin will be making called “The History of Camp Buddy”!"

    show yuri confused4 at right
    voice audio.yuri_v_praise3a
    yu "That’s a great idea, Yoshi! But… so many of the pictures have deteriorated over the years, I’m not sure if they’ll really be useful."

    show yoshi bold2 at left
    voice audio.yoshi_v_oh2
    yo "Oh, but I bet Jin can fix those! He’s got so many computer skills, surely that’s one of them too!"

    show yuri sigh3 at right
    voice audio.yuri_v_sigh2a
    yu "*sigh* That’s not exactly the same as programming, Yoshi…"

    show jin laugh2 at center
    voice audio.jin_v_laugh5c
    j "Haha, actually, I know a thing or two about multimedia editing too! In fact, I used to do photo restoration as a side job before."

    show yuri amazed1 at right
    voice audio.yuri_v_amazed2a
    yu "Wow! You can really do that?!"

    show jin bold2 at center
    voice audio.jin_v_excited1b
    j "Yeah, I’d love to! I’ll be honest, I’m very intrigued about all these photos you have!"
    j "I know this is just my first day, but, for some reason, you guys make me feel like I’ve been a part of this for a long time!"

    show yuri comp4 at right
    voice audio.yuri_v_aww3a
    yu "Awwww, Jin! You’re such a softboi! We must protect you at all costs!!!"

    show jin bold1 at center
    voice audio.jin_v_enocurage1a
    j "I say we give it a shot right away! You guys can help me fix up the photos correctly based on your memory, and then we’ll transcribe the events from that day!"

    show yoshi happy1 at left
    voice audio.yoshi_v_rush6
    yo "Sounds like a plan!"

    # JM1
    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    $renpy.choice_for_skipping()
    scene cg white with Dissolve(2.0)
    $ quick_menu = False
    $ say_box = False
    hide screen location
    hide screen timeline
    hide screen quick_menu
    $ global minigame_id
    $ minigame_id = 'jm1'
    $ renpy.call(minigame_id, 'night')

label day4_postmg:
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

    $ location = location_entrance
    $ day = "??"
    $ time = timeline_timeday
    $ season = season_summer
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_entrance_past_day with fade
    play music camping_time loop
    play bgsound sfxloop_birds loop

    show yyuri_camp2 at left
    show yyuri excited1 at left
    show ygoro_camp at center
    show ygoro norm1 at center
    show andre_camp at right
    show andre happy2 at right
    voice audio.andre_v_service2a
    u "The staff is ready for the scouts inside. The meal for the reception party is all prepared as well, sir!"

    show ygoro happy2 at center
    voice audio.ygoro_v_thanks2a1
    g "Thank you, Andre. You can return to your post now. "
    g "My daughter and I will wait here to welcome the scouts! "

    show andre smile1 at right
    voice audio.andre_v_yessir1c
    u "Yes, sir!"

    hide andre_camp
    hide andre smile1
    with dissolve

    show yyuri_camp2 at left2
    show yyuri excited1 at left2
    show ygoro_camp at right2
    show ygoro bold2 at right2
    with move

    voice audio.ygoro_v_alright1a
    g "Alright, dear! Everything should be ready now for our first official day of Camp Buddy!"

    show yyuri excited2 at left2
    voice audio.yyuri_v_shock3a
    yu "Wah… I can’t believe it’s actually happening, Dad! I’m so excited for all the activities and to make new friends!"

    show ygoro excited1 at right2
    voice audio.ygoro_v_laugh1a
    g "I’m excited as well.  I’m sure we’ll have a memorable first term considering how much we’ve prepared for this!"

    show yyuri amazed3 at left2
    voice audio.yyuri_v_goro1a
    yu "I can help you teach everyone, Dad! I’ve learned a lot from our camping days together, after all!"

    show ygoro laugh2 at right2
    voice audio.ygoro_v_well1
    g "Well, you can leave all the work to me, dear! I’m a scoutmaster now, and your job as a scout is to have fun and learn as much as you can!"

    show yyuri pout1 at left2
    voice audio.yyuri_v_agree5a1
    yu "Fine! But you better not bore everyone with your lectures!"

    show ygoro comp6 at right2
    voice audio.ygoro_v_laugh2a
    g "Haha, I promise we’ll have all sorts of activities to suit everyone’s interests!"

    hide yyuri_camp2
    hide yyuri amazed4
    show yyuri_camp2 at p5_1
    show yyuri amazed4 at p5_1
    show ygoro_camp at p5_2
    show ygoro comp6 at p5_2
    with move

    play sound sfx_busdoor
    show yyoshi_casual at p5_5
    show yyoshi norm1 at p5_5
    with dissolve

    voice audio.yyuri_v_look1a
    yu "Oh, oh! Look, Dad! Someone just got here!"

    show ygoro happy2 at p5_2
    voice audio.ygoro_v_rush2b1
    g "Come on, let’s greet our first scout!"

    show yyuri_camp2 at left
    show yyuri amazed4 at left
    show ygoro_camp at center
    show ygoro happy1 at center
    show yyoshi_casual at right
    show yyoshi norm1 at right
    with move

    voice audio.ygoro_v_greet2a1
    g "Hello! Welcome to Camp Buddy!"

    show yyoshi happy1 at right
    voice audio.yyoshi_v_goodam1
    yo "Good morning, sir! I’m Yoshinori Nagira! I registered here for the summer!"

    show ygoro happy3 at center
    voice audio.ygoro_v_laugh1a
    g "My name is Goro Nomoru! I’m the camp president, and I’ll be your scoutmaster for this term!"

    show yyoshi bold2 at right
    voice audio.yyoshi_v_greet5a
    yo "It’s nice to meet you, Sir Goro! Thank you for having me!"

    show ygoro play2 at center
    voice audio.ygoro_v_yoshi2
    g "Looks like you’re quite the early bird, Yoshinori! The assembly is still an hour from now!"

    show yyoshi relief4 at right
    voice audio.yyoshi_v_relief1
    yo "Phew… I thought I was late when I saw there was already a scout here, haha…!"

    show ygoro play3 at center
    voice audio.ygoro_v_well1
    g "Quite the contrary, you’re the first one to arrive! And this scout beside me is my daughter!"

    show yyuri happy3 at left
    voice audio.yyuri_v_greet2a
    yu "Hi, Yoshinori~! I’m Yuri! Nice to meet you!"

    show yyoshi happy2 at right
    voice audio.yyoshi_v_greet5b
    yo "It’s nice to meet you too, Yuri! You can call me Yoshi!"

    show yyuri laugh2 at left
    voice audio.yyuri_v_yoshi3a
    yu "We’re gonna have so much fun this summer, Yoshi! There’s plenty of others coming soon, and there’ll be at least a hundred of us!"

    show yyoshi excited1 at right
    voice audio.yyoshi_v_shock2a
    yo "Wah, that’s exciting! I read from the brochure we’re also gonna learn a lot, too!"

    show ygoro bold2 at center
    voice audio.ygoro_v_agree6a
    g "That’s right! Camp Buddy is a scout-themed summer camp, after all!"
    g "We’re taking the survival, teamwork and leadership skills from scouting and mixing them up with all the fun, recreational activities of a summer camp!"

    show yyoshi bold3 at right
    voice audio.yyoshi_v_yessir2a
    yo "That’s exactly what I signed up for, sir!"
    yo "I never got the chance to join something like this when I was little, so I’m really looking forward to experiencing it now!"

    show ygoro bold3 at center
    voice audio.ygoro_v_praise1a
    g "Now that’s the spirit! I really appreciate your enthusiasm!"

    show yyuri fangirl2 at left
    voice audio.yyuri_v_kyaa1b
    yu "Kyaaaa! We should get you in your uniform already, Yoshi~!"

    show yyuri bold2 at right2
    show yyuri_camp2 at right2
    with move

    voice audio.yyuri_v_idea2a
    yu "Let’s get you dressed! I have the perfect tie color for you!"

    show yyoshi talk3 at right
    voice audio.yyoshi_v_okay2
    yo "O-Okay…!"

    hide yyoshi_casual
    hide yyoshi talk3
    hide yyuri_camp2
    hide yyuri bold2
    with moveoutright

    show ygoro laugh1 at center
    voice audio.ygoro_v_laugh1a
    g "Looks like we’re in for a great year!"

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
    jump day4_postfb

label day4_postfb:
    $ location = location_cabin
    $ day = "04"
    $ time = timeline_timenight
    $ season = season_autumn
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_quarters_autumn_night with fade
    play music ready_for_tomorrow loop
    play bgsound sfxloop_night loop

    show yoshi_sleep at left2
    show yoshi happy2 at left2
    show jin_sleep at right2
    show jin norm2 at right2
    show jin_glasses at right2
    voice audio.yoshi_v_relief1
    yo "We’ve got you settled in at last, Jin… Today’s been such a long day!"

    show jin laugh3 at right2
    voice audio.jin_v_yeah4a
    j "You said it! I can’t remember the last time I was this active! "
    j "I was so nervous that I’d screw up dealing with so many new people. But you really made me feel warm and welcome from the get-go!"

    show jin smile2 at right2
    voice audio.jin_v_thanks4b
    j "Thank you so much for being such a great host, Yoshinori!"

    show yoshi comp5 at left2
    voice audio.yoshi_v_response5
    yo "It’s my pleasure, Jin! That really means a lot coming from you!"
    yo "Now please get some rest, you can take the top bunk on the right side! "

    show jin talk2 at right2
    voice audio.jin_v_response2a1
    j "Oh, right! You did say earlier we’d be sharing the room with others. Where are they? "

    show yoshi_sleep at p7_6
    show yoshi comp5 at p7_6
    show jin_sleep at p7_7
    show jin talk2 at p7_7
    show jin_glasses at p7_7
    with move

    show darius_autumn at p7_1
    show darius norm1 at p7_1
    show lloyd_autumn at p7_2
    show lloyd talk2 at p7_2
    show aiden_autumn at p7_3
    show aiden norm1 at p7_3
    with dissolve

    voice audio.lloyd_v_aiden2c
    l "I gotta tell you, Aiden, you’re such a Gemini! Very adaptable, a multitasker, and quite the charmer!"

    show lloyd sigh3 at p7_2
    voice audio.lloyd_v_sigh2a
    l "*sigh* You must be popular with everyone! Life is so unfair! Why am I such an Aries?!"

    hide aiden_autumn
    hide aiden norm1
    show aiden2_autumn at p7_3
    show aiden2 confused5 at p7_3
    voice audio.aiden_v_lloyd5a
    a "Where do you even learn all these things, Lloyd? "

    show darius tease4 at p7_1
    voice audio.darius_v_laugh1
    d "From fiction."

    show lloyd angry2 at p7_2
    voice audio.lloyd_v_greet2c2
    l "Horoscopes are not fiction! How do you explain why everything is so accurate, huh?!"

    show yoshi happy2 at p7_6
    voice audio.yoshi_v_goodpm2
    yo "Good evening, you guys! "

    show darius_autumn at p5_1
    show darius tease4 at p5_1
    show lloyd_autumn at p5_2
    show lloyd angry2 at p5_2
    show aiden2_autumn at p5_3
    show aiden2 confused5 at p5_3
    show yoshi_sleep at p5_4
    show yoshi comp5 at p5_4
    show jin_sleep at p5_5
    show jin talk2 at p5_5
    show jin_glasses at p5_5
    with move

    hide aiden2_autumn
    hide aiden2 confused5
    show aiden_autumn
    show aiden shock3
    voice audio.aiden_v_shock1d2
    a "Whoa! Don’t tell me Jin’s our roommate too?!"

    show yoshi happy1 at p5_4
    voice audio.yoshi_v_yeah2
    yo "Yeah! He’ll be taking the last bunk in here!"

    show darius happy2 at p5_1
    voice audio.darius_v_excited1a3
    d "Nice."

    show lloyd laugh1 at p5_2
    voice audio.lloyd_v_laugh1a1
    l "The more, the merrier, right?"

    show jin think4 at p5_5
    voice audio.jin_v_comp8a2
    j "I-I did notice that there are only four beds, so I can sleep on the couch…! "

    show yoshi comp2 at p5_4
    voice audio.yoshi_v_oh1
    yo "Oh, I’m not letting you do that, Jin! You can use mine!"

    show lloyd talk2 at p5_2
    voice audio.lloyd_v_rush1a2
    l "Oh, come on, you guys! No one’s sleeping on the couch. Dar and I can just share one bed!"

    show jin confused3 at p5_5
    voice audio.jin_v_question1a1
    j "A-Are you sure…?"

    show darius comp5 at p5_1
    voice audio.darius_v_agree2a
    d "Yeah."

    show aiden laugh1 at p5_3
    voice audio.aiden_v_laugh2a1
    a "Haha, it feels like we’re all in a big sleepover or something, am I right?"

    show lloyd happy1 at p5_2
    voice audio.lloyd_v_conj1a3
    l "Well, I’m not sleeping just yet! I still have to brew up my nightly detox!"

    show jin think5 at p5_5
    voice audio.jin_v_conj1c3
    j "A-Actually, I need to make some coffee too."

    show yoshi confused2 at p5_4
    voice audio.yoshi_v_huh1
    yo "Coffee? This late at night?"

    show jin talk1 at p5_5
    voice audio.jin_v_yeah1b
    j "Yeah… I have some stuff I wanted to work on still."

    hide aiden_autumn
    hide aiden laugh1
    show aiden2_autumn at p5_3
    show aiden2 tease4 at p5_3
    voice audio.aiden_v_sheesh1b
    a "Sheesh, Yoshi. Look what you’ve done to Jin in just a day."

    show jin comp3 at p5_5
    voice audio.jin_v_no2c
    j "A-Ah, n-no, Aiden. It’s really just a habit of mine…"

    show yoshi comp3 at p5_4
    voice audio.yoshi_v_alright1
    yo "Just don’t stay up too late, alright, Jin?"

    show jin comp6 at p5_5
    voice audio.jin_v_agree1d1
    j "S-Sure…"

    show darius tired1 at p5_1
    voice audio.darius_v_goodpm2
    d "Good night. I’m going to sleep."

    hide aiden2_autumn
    hide aiden2 tease4
    show aiden_autumn at p5_3
    show aiden happy1 at p5_3
    voice audio.aiden_v_goodeve1a1
    a "I’m hitting the hay too! Got another long day coming up tomorrow!"

    show yoshi happy1 at p5_4
    voice audio.yoshi_v_goodpm4
    yo "Good night, guys!"

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black with fade

    yo "{i}Sharing the cabin with everyone made me feel like I was a scout again.{/i}"
    yo "{i}It’s only been a few days, and so much has changed already!{/i}"

    scene cg black
    hide screen location
    hide screen timeline
    hide screen quick_menu
    $quick_menu = False
    with fade
    play sound sleeping_time
    $ time_transition_night_to_day_fall()
    $ renpy.pause (2.0, hard=True)
    $persistent.profile_unlock.append("hyunjin")
    jump day5
