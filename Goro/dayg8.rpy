label day8_goro:
    $ day = "83"
    $ time = timeline_timeday
    $ location = location_quarters
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    $ working = True

    scene bg_quarters_winter_day with fade
    play music brand_new_day_winter loop
    play bgsound sfxloop_birds loop

    show aiden_sleep at left
    show aiden norm1 at left
    show jin_sleep at center
    show jin_glasses at center
    show jin norm1 at center
    show yoshi2_sleep at right
    show yoshi2 sleepy1 at right
    voice audio.yoshi_v_groan1a
    yo "Hngh…"

    show aiden happy2 at left
    voice audio.aiden_v_goodam1a1
    a "Oh, hey! Good morning, Yoshi!"

    show jin comp3 at center
    voice audio.jin_v_aww1a2
    j "Seems like you might’ve partied a bit too much last night...  "

    show yoshi2 sleepy6 at right
    voice audio.yoshi_v_yeah4
    yo "Y-Yeah, I’m a little groggy this morning… I’ve always been a lightweight when it comes to booze."

    show jin worry4 at center
    voice audio.jin_v_relief1a1
    j "Good thing I don’t drink alcohol. Hangovers are the worst…"

    show aiden shock3 at left
    voice audio.aiden_v_really3a
    a "Wait, really?! What did I see you chugging last night then?!"

    show jin relief2 at center
    voice audio.jin_v_conj1c1
    j "Th-That was iced-coffee… Yuri made it for me…"

    show aiden laugh2 at left
    voice audio.aiden_v_oh1a
    a "So that’s why you’re not dying like the rest of us this morning! Hahaha!"

    show jin comp2 at center
    voice audio.jin_v_conj2a1
    j "Well… I had just as much fun with everyone… Watching you all slowly get drunk was rather… interesting."

    show yoshi2 comp6 at right
    voice audio.yoshi_v_laugh6
    yo "Ahehe… It’s been a while since Yuri let us all drink at the camp."

    hide aiden_sleep
    hide aiden laugh2
    show aiden2_sleep at left
    show aiden2 comp3 at left
    voice audio.aiden_v_actually3a
    a "I kinda held back on the beers this time – don’t wanna wake up to our sponsorship getting cancelled ’cause I lost all my clothes again!  "

    show jin perv2 at center
    voice audio.jin_v_sigh1a
    j "I was hoping that’d happen… *cough* I-I don’t mean our project getting cancelled…!"

    hide aiden2_sleep
    hide aiden2 comp3
    show aiden_sleep at left
    show aiden laugh3 at left
    voice audio.aiden_v_laugh2b1
    a "Hahaha! "

    hide yoshi2_sleep
    hide yoshi2 comp6
    show yoshi_sleep at right
    show yoshi confused2 at right
    voice audio.yoshi_v_huh1
    yo "Where is everybody though? Did I wake up late again…?"

    show aiden talk4 at left
    voice audio.aiden_v_no2a1
    a "No, you didn’t! I actually woke up just a bit before you."
    a "Jin here was just catching me up on what we missed!"

    show jin think2 at center
    voice audio.jin_v_conj2c1
    j "W-Well… I’m just doing regular maintenance on our website."
    j "Lloyd and Darius are doing some minor repair work at the site before the workers arrive."

    show yoshi talk3 at right
    voice audio.yoshi_v_right6
    yo "Oh right, they should be showing up tomorrow."

    show aiden happy1 at left
    voice audio.aiden_v_anyway1a
    a "Meanwhile, Yuri and Emilia left a while ago to take the scouts back home."

    show yoshi awkward4 at right
    voice audio.yoshi_v_ah4
    yo "A-Ah, they didn’t have to do that! I was planning on driving them back today!"

    show aiden laugh2 at left
    voice audio.aiden_v_laugh2a1
    a "Haha, I think Yuri wanted to sneak in some more time with them for her usual questioning."
    a "She’s probably gonna be talking about ‘cracks’ and ‘ships’ the entire way, whatever that means."

    hide yoshi_sleep
    hide yoshi awkward4
    show yoshi2_sleep at right
    show yoshi2 comp6 at right
    voice audio.yoshi_v_laugh6
    yo "Ahehe, I wonder how Emilia will deal with that…"

    show aiden play2 at left
    voice audio.aiden_v_conj3a1
    a "Haha, with any luck, she’ll keep Yuri from going too crazy."

    hide yoshi2_sleep
    hide yoshi2 comp6
    show yoshi_sleep at right
    show yoshi confused3 at right
    voice audio.yoshi_v_think4
    yo "What about Goro though?"

    show jin confused5 at center
    voice audio.jin_v_think1a1
    j "I think he’s in his office with Mr. Clermont."

    show yoshi think2 at right
    voice audio.yoshi_v_really1
    yo "I’m surprised Mr. Clermont hasn’t left yet. "

    show aiden talk4 at left
    voice audio.aiden_v_response4a
    a "Same, actually. But I think he’s really enjoying his visit here."
    a "It’s like a vacation for him!"

    show yoshi happy2 at right
    voice audio.yoshi_v_well1
    yo "Well, it sounds like everyone is settling in again, at least. "

    hide aiden_sleep
    hide aiden talk4
    show aiden2_sleep at left
    show aiden2 sigh4 at left
    voice audio.aiden_v_hngh1b3
    a "Yeah, it’s time to get back to the grind, even though I’m dragging a little bit."

    show yoshi think2 at right
    voice audio.yoshi_v_yeah1
    yo "Me, too… Or maybe that’s just the hangover. "

    hide aiden2_sleep
    hide aiden2 sigh4
    show aiden_sleep at left
    show aiden happy1 at left
    voice audio.aiden_v_anyway1a
    a "Anyway, I should probably get to work and prep brunch!"

    show yoshi happy1 at right
    voice audio.yoshi_v_unsure3a
    yo "I guess I’ll get dressed too and see if there’s anything I can assist Goro with for Mr. Clermont."

    show aiden happy2 at left
    voice audio.aiden_v_jin5a
    a "What about you, Jin? Wanna come with me?"

    show jin talk4 at center
    voice audio.jin_v_comp8b1
    j "I-I’m fine staying here…"

    show aiden play2 at left
    voice audio.aiden_v_oho1a
    a "I’ll wear just an apron and let you watch, if you join~"

    hide jin_sleep
    hide jin_glasses
    hide jin talk4
    show jin2_sleep at center
    show jin2_glasses at center
    show jin2 scheme2 at center
    voice audio.jin_v_comp4a
    j "Call me Sous-chef Hyunjin Choi, then."

    hide yoshi_sleep
    hide yoshi happy1
    show yoshi2_sleep at right
    show yoshi2 comp6 at right
    voice audio.yoshi_v_laugh6
    yo "Ahehe… just try not to faint, Jin."

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
    scene bg_office_winter_day with fade
    play music buddy_oath_casual loop

    show goro_autumn at left2
    show goro norm3 at left2
    show william_autumn at right2
    show william talk3 at right2
    voice audio.william_v_conj6
    w "I’d really appreciate if you gave it more thought, Mr. Nomoru. I’d be thrilled to see Camp Buddy expand its horizons."
    w "There’s so much untapped potential here, and I would like to be a part of its future."

    show goro explain2 at left2
    voice audio.goro_v_thanks2b1
    g "Thank you for the offer, Mr. Clermont. I will definitely consider it."

    play sound sfx_doorknock
    $ renpy.pause (1.0, hard=True)
    show goro talk3 at left2
    voice audio.goro_v_greet2a2
    g "Come in."

    show goro_autumn at left
    show goro norm3 at left
    show william_autumn at center
    show william norm1 at center
    with move

    show yoshi_winter at right
    show yoshi talk3 at right
    with dissolve

    voice audio.yoshi_v_goodam1
    yo "O-Oh, good morning, gentlemen! I hope I didn’t interrupt anything!"

    show william happy1 at center
    voice audio.william_v_disagree1b
    w "Not at all! We just finished a little meeting and I’m about to take my leave."

    show goro happy2 at left
    voice audio.goro_v_thanks1a1
    g "Thanks again for staying with us, Mr. Clermont. We appreciate you taking the time out of your busy schedule to spend time with us yesterday."

    show william laugh1 at center
    voice audio.william_v_thanks1b
    w "I’m the one who should be thanking you! You’ve all been so hospitable to me!"

    show william happy3 at center
    voice audio.william_v_actually1
    w "And I must say, this is one of the best mini vacations I’ve taken in a long time!"
    w "With everything going on at work, I needed a bit of time away from the stress, and the rustic lifestyle was perfect for me."

    show yoshi laugh2 at right
    voice audio.yoshi_v_laugh1
    yo "Haha, we’re glad you enjoyed being here so much, sir. We wouldn’t have been able to clean up everything as quickly without your help, either. "

    show william comp4 at center
    voice audio.william_v_conj4
    w "Like I said, think nothing of it! It’s the least I could do. "
    w "I would like to extend my apologies again about what transpired with Ms. Komarova at the hotel, however. "

    show william sigh1 at center
    voice audio.william_v_sigh2
    w "I was not aware of the severity of her well-being at the time…  "

    show goro explain2 at left
    voice audio.goro_v_alright2b1
    g "It’s quite alright, sir. I don’t think any of us were aware, so you can’t be blamed."

    show william comp2 at center
    voice audio.william_v_conj6
    w "Regardless, I am glad that she is surrounded by supportive people."

    show goro relief2 at left
    voice audio.goro_v_comp2a1
    g "You can rest easy about her here."

    show william relief2 at center
    voice audio.william_v_amazed3
    w "Wonderful! Now, I believe it’s time for me to leave."

    show william comp2 at center
    voice audio.william_v_thanks1b
    w "Once again, thank you all for your hospitality! I hope that I didn’t put you out too much."

    show goro comp5 at left
    voice audio.goro_v_laugh2a
    g "Oh, not at all, Mr. Clermont! You’re welcome here at the camp anytime you want!"

    show yoshi happy2 at right
    voice audio.yoshi_v_right5
    yo "That’s right! Please feel free to come back and visit, sir!"

    show william laugh2 at center
    voice audio.william_v_thanks2
    w "Thank you, your kindness is greatly appreciated."

    show william happy3 at center
    voice audio.william_v_conj6
    w "Lastly, Mr. Nomoru, please let me know when you’ve come to a decision regarding my offer!"
    w "And feel free to consult with Mr. Nagira here as well!"

    hide goro_autumn
    hide goro comp5
    show goro2_autumn at left
    show goro2 disappoint3 at left
    voice audio.goro_v_yessir1c2
    g "I’ll keep that in mind, Mr. Clermont."

    show william happy2 at center
    voice audio.william_v_anyway1
    w "Anyway, you all need to start your day, so it’s best I be on my way."

    hide goro2_autumn
    hide goro2 disappoint3
    show goro_autumn at left
    show goro talk1 at left
    voice audio.goro_v_request5a1
    g "Please let me escort you out at least."

    show william laugh1 at center
    voice audio.william_v_dismiss1
    w "No need! I already know my way to the entrance and my driver should already be waiting."
    w "Thank you again, and I hope to see you all sometime soon!"

    show yoshi laugh2 at right
    voice audio.yoshi_v_bye1a
    yo "Take care, Mr. Clermont!"

    show william happy2 at center
    voice audio.william_v_bye1b
    w "Goodbye!"

    hide william_autumn
    hide william happy2
    with dissolve

    show goro_autumn at left2
    show goro talk1 at left2
    show yoshi_winter at right2
    show yoshi talk3 at right2
    with move

    voice audio.yoshi_v_amazed1c
    yo "Wow, I didn’t expect you and Mr. Clermont to jump into work stuff right away this morning."
    yo "Especially after how much we drank last night, hehe…"

    show goro confused2 at left2
    voice audio.goro_v_ah1b
    g "Ah, you mean the meeting? We were just having coffee and chatting, and the conversation moved in that direction."
    g "It turns out another reason he wanted to visit was to discuss it."

    show yoshi awkward4 at right2
    voice audio.yoshi_v_isee1
    yo "Oh, I see! I’m sorry I missed it… I wish I’d gotten up earlier to join in!"
    yo "What was it about, if you don’t mind me asking?"

    hide goro_autumn
    hide goro confused2
    show goro2_autumn at left2
    show goro2 explain2 at left2
    voice audio.goro_v_conj8a2
    g "To sum it up, he wants to expand Camp Buddy’s reach and asked if I was interested in reacquiring the previous branches that were shut down."
    g "He offered to provide all the funding needed to renovate them in exchange for becoming a full-fledged shareholder of the franchise."

    show yoshi amazed1 at right2
    voice audio.yoshi_v_really3
    yo "What?! Really?! That’s amazing news!"

    hide goro2_autumn
    hide goro2 explain2
    show goro_autumn at left2
    show goro talk1 at left2
    voice audio.goro_v_conj9a1
    g "I know, I couldn’t believe it either."
    g "Especially after getting a chance to talk to him about what happened back at the hotel."

    show goro sigh1 at left2
    voice audio.goro_v_but2a
    g "I expected him to be disappointed, but he was very understanding. And then following it up with yet another business opportunity…"

    show yoshi confused2 at right2
    voice audio.yoshi_v_why1
    yo "Did he tell you why he wanted to do it?"

    hide goro_autumn
    hide goro sigh1
    show goro2_autumn at left2
    show goro2 think3 at left2
    voice audio.goro_v_well1a
    g "Well, Mr. Clermont is an entrepreneur. His business has plenty of investments that he’s funded and earns passively from, and Camp Buddy has caught his attention."
    g "From what I understood, he thinks our camp is worth expanding to make it reach its full potential, both financially and performance-wise."

    show goro2 talk3 at left2
    voice audio.goro_v_think1a1
    g "He’s also a huge fan of the spirit of this place, and wants to allow more people to experience it."

    show yoshi think2 at right2
    voice audio.yoshi_v_isee1
    yo "I see… Mr. Clermont always does talk about how happy he is Felix got to experience this place, so that makes a lot of sense!"
    yo "Either way, this is exciting news! "

    show yoshi confused3 at right2
    voice audio.yoshi_v_so1a
    yo "Did you accept? It sounds like you didn’t give him an answer yet."

    show goro2 shy6 at left2
    voice audio.goro_v_yeah1c1
    g "Yeah, I didn’t want to decide on the spot. Especially with something so important."

    $ working = False
    $ shuffle_menu()
    menu():
        g "Yeah, I didn’t want to decide on the spot. Especially with something so important.{fast}"
        "The decision is obvious!":
            $ working = True
            $ score_goro -= 2
            show yoshi talk1 at right2
            voice audio.yoshi_v_but1
            yo "But I feel like the decision should be obvious, Goro!"
            yo "It sounds like it’d be great for the camp’s future!"

            show goro2 disappoint3 at left2
            voice audio.goro_v_think1a1
            g "Hmm, that may be so, but I’ve been down this road before."
        "We shouldn't miss the chance.":
            $ working = True
            $ score_goro -= 1
            show yoshi talk1 at right2
            voice audio.yoshi_v_but1
            yo "We shouldn’t miss this chance, Goro!"
            yo "It sounds like it’d be great for the camp’s future!"

            show goro2 disappoint3 at left2
            voice audio.goro_v_think1a1
            g "Hmm, that may be so, but I’ve been down this road before."
        "It means more responsibilities.":
            $ working = True
            $ score_goro += 1
            show yoshi explain2 at right2
            voice audio.yoshi_v_response1a
            yo "I understand. It would mean bigger responsibilities."

            show goro2 talk1 at left2
            voice audio.goro_v_agree4a1
            g "Exactly. As big of an opportunity as it is for the camp, it also means heavy changes for us involved in management."
        "It's a huge change.":
            $ working = True
            $ score_goro += 2
            show yoshi explain2 at right2
            voice audio.yoshi_v_response1a
            yo "I understand.  It would mean heavy changes for all of us here at camp."

            show goro2 talk1 at left2
            voice audio.goro_v_agree4a1
            g "Exactly. As big of an opportunity as it is for the camp, it also means bigger responsibilities that we may not be prepared for."

    show goro2_autumn at p4_1
    show goro2 norm3 at p4_1
    show yoshi_winter at p4_2
    show yoshi norm1 at p4_2
    with move

    show emilia_winter at p4_3
    show emilia annoy1 at p4_3
    show yuri_winter at p4_4
    show yuri annoy4 at p4_4
    with dissolve

    voice audio.yuri_v_ugh3a
    yu "Ugh… Why am I doing this with you again…?"

    show emilia irked3 at p4_3
    voice audio.emilia_v_question4a
    e "Excuse me? I came with you to bring the scouts home AND waited on you to finish browsing that book store for HOURS!"
    e "The least you could do is help me out!"

    show yuri irked2 at p4_4
    voice audio.yuri_v_agree5a1
    yu "Fine, Fine…"

    hide goro2_autumn
    hide goro2 norm3
    show goro_autumn at p4_1
    show goro talk3 at p4_1
    voice audio.goro_v_goodam1a1
    g "Oh, welcome back ladies. How was your drive?"

    show emilia angry5 at p4_3
    voice audio.emilia_v_worry3a
    e "Oh, don’t get me started! This pink thing was trying to get us killed with how reckless she is behind the wheel!"

    show yuri angry2 at p4_4
    voice audio.yuri_v_hey3a
    yu "Hey! It was fine until you started backseat driving!"

    show yoshi talk1 at p4_2
    voice audio.yoshi_v_comp7
    yo "Now, calm down both of you. Emilia, you’ve only just recovered."

    show yuri irked1 at p4_4
    voice audio.yuri_v_yeah1b1
    yu "Yeah! I kept telling her to stay behind and wait, but she insisted on coming along!"

    show emilia angry2 at p4_3
    voice audio.emilia_v_surprised1a
    e "I told you all, I’m fine already! I’m not helpless!"

    show yoshi worry2 at p4_2
    voice audio.yoshi_v_sorry2a
    yo "Sorry I didn’t wake up in time though, Yuri. I was supposed to take the scouts home today."

    show yuri comp2 at p4_4
    voice audio.yuri_v_alright2b1
    yu "It’s fine Yoshi! It’s been a while since I had some quality time with them anyway! Besides, Emilia wanted to get to know them too!"

    show emilia annoy5 at p4_3
    voice audio.emilia_v_tsun3a
    e "I-It’s not like that…!"

    show yuri play2 at p4_4
    voice audio.yuri_v_annoyed3a
    yu "Oh, don’t bother denying it! It’s okay to admit you like the scouts~"

    show emilia eyeroll4 at p4_3
    voice audio.emilia_v_hmph1a
    e "Hmph!"

    show yoshi laugh1 at p4_2
    voice audio.yoshi_v_praise1
    yo "Haha, it’s good to see you two getting along better."

    show goro confused2 at p4_1
    voice audio.goro_v_confused1a1
    g "What’s with all the empty boxes though? You girls packing something up?"

    show yuri talk2 at p4_4
    voice audio.yuri_v_well1a
    yu "Well, we just saw Mr. Clermont leave so we figured we could get some stuff out of the room now."

    show goro talk4 at p4_1
    voice audio.goro_v_oh1a
    g "Oh, right. Emilia stayed with you last night so Mr. Clermont could have a room."

    show yuri happy2 at p4_4
    voice audio.yuri_v_yeah1a1
    yu "Yeah, and she liked it so much she’s gonna bunk with me from now on!"

    show yoshi shock3 at p4_2
    voice audio.yoshi_v_wait2b
    yo "W-Wait, you and Emilia are gonna be permanent roommates?!"

    show yuri explain1 at p4_4
    voice audio.yuri_v_response2a2
    yu "Shocking, I know. But it was her decision."

    show emilia angry6 at p4_3
    voice audio.emilia_v_tsun2a
    e "Don’t make it sound like I begged you! It was a mutual agreement! "

    show yuri happy3 at p4_4
    voice audio.yuri_v_yeah1h1
    yu "Yeah, yeah, whatever you say! Either way, I’m not gonna lie, it’s nice to finally have a girl I can hang out with for once! "
    yu "It takes me back to when we had that other all-girls branch Dad left me in charge of…"

    show emilia eyeroll3 at p4_3
    voice audio.emilia_v_sarcastic2a
    e "Clearly, all this time with men affected your sense of fashion too. You barely have anything feminine in your wardrobe!"

    show yuri rage1 at p4_4
    voice audio.yuri_v_hey3a
    yu "Hey, speaking of that, you’re the messiest and sloppiest roommate ever! You dumped all my stuff on the floor!"

    show emilia angry5 at p4_3
    voice audio.emilia_v_question4c1
    e "Excuse me! I was trying to find the least drab outfit you own, turns out it was a hopeless cause!"

    show yuri angry5 at p4_4
    voice audio.yuri_v_hmph1a
    yu "You only got away with that because yesterday was a trial run."
    yu "Now that you’re officially moving in with me, there’s gonna be some house rules! Same goes for staying here at the camp!"

    show emilia sigh1 at p4_3
    voice audio.emilia_v_response1c
    e "*sigh* Fine…"

    show yuri talk2 at p4_4
    voice audio.yuri_v_anyway1a
    yu "Anyway, Dad! Now that Emilia is kicked out, you can use your room again~!"

    show emilia comp3 at p4_3
    voice audio.emilia_v_thanks2
    e "Thank you for letting me use it over the last few months, sir."

    show goro awkward4 at p4_1
    voice audio.goro_v_ah1a
    g "Ah, you’re welcome…"

    show yuri comp2 at p4_4
    voice audio.yuri_v_alright2b1
    yu "I would understand if you wanted to stay in the cabin with the boys for a while longer, though."
    yu "You seem to be having fun with the them, so—"

    hide goro_autumn
    hide goro awkward4
    show goro2_autumn at p4_1
    show goro2 think2 at p4_1
    voice audio.goro_v_think1a1
    g "Hmm… I do think it’s a good idea to move back in. "

    show yuri shock3 at p4_4
    voice audio.yuri_v_really1a
    yu "Wait, really?"

    show goro2 talk1 at p4_1
    voice audio.goro_v_yeah1a1
    g "Yeah."

    show yoshi comp2 at p4_2
    voice audio.yoshi_v_gratitude2
    yo "It was really nice having you in the scoutmaster’s quarters for a while."

    show goro2 play2 at p4_1
    voice audio.goro_v_well1a
    g "Well, I’m not going alone. You’re coming with me."

    show yoshi shock1 at p4_2
    yo "...!"

    hide goro2_autumn
    hide goro2 play2
    show goro_autumn at p4_1
    show goro explain3 at p4_1
    voice audio.goro_v_conj2a1
    g "The bed in my room is big enough for two people anyway."
    g "Not only that, but we’re just one door away from the office. It’ll be more convenient for work."

    show goro relief2 at p4_1
    voice audio.goro_v_conj7a
    g "And besides, the cabin is pretty cramped with six people sharing a room. They could use the extra space."
    g "Plus, it’d be nice to have some privacy again."

    show emilia evil5 at p4_3
    voice audio.emilia_v_agree1a1
    e "Right~ With Yoshinori."

    hide goro_autumn
    hide goro relief2
    show goro2_autumn at p4_1
    show goro2 disappoint2 at p4_1
    voice audio.goro_v_ehem1a
    g "*ehem* Like I said, it’s to be more efficient."

    show emilia wink2 at p4_3
    voice audio.emilia_v_response2a
    e "Okay, if you say so~"

    show yuri happy1 at p4_4
    voice audio.yuri_v_well1a
    yu "Well, if you’re gonna move back in, Dad, then I’ll go tidy up the room for you!"

    show emilia explain2 at p4_3
    voice audio.emilia_v_think1
    e "I suppose I’ll help as well. It IS my stuff after all."

    hide goro2_autumn
    hide goro2 disappoint2
    show goro_autumn at p4_1
    show goro happy2 at p4_1
    voice audio.goro_v_yoshi2a
    g "I guess that gives us something to do today, Yoshinori."

    show yoshi happy1 at p4_2
    voice audio.yoshi_v_yeah1
    yo "Yeah, I’ll need to pack up my stuff as well!"

    show goro happy3 at p4_1
    voice audio.goro_v_rush1d1
    g "Let’s go tell the others, then?"

    show yoshi happy2 at p4_2
    voice audio.yoshi_v_alright1
    yo "Alright, Goro!"

    hide goro_autumn
    hide goro happy3
    hide yoshi_winter
    hide yoshi happy2
    with dissolve

    show emilia play3 at p4_3
    voice audio.emilia_v_laugh1b
    e "Hehe, I didn’t know they were ‘that’ close."

    show yuri confused3 at p4_4
    voice audio.yuri_v_confused2b1
    yu "Huh?? What do you mean?  "

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

    $ location = location_quarters
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_quarters_winter_day with fade
    play music sunset_stroll_winter loop

    show aiden_autumn at p6_1
    show aiden comp1 at p6_1
    show lloyd_winter at p6_2
    show lloyd worry3 at p6_2
    show darius_winter at p6_3
    show darius comp1 at p6_3
    show goro_autumn at p6_5
    show goro comp1 at p6_5
    show jin_autumn at p6_4
    show jin_glasses at p6_4
    show jin worry1 at p6_4
    show yoshi_autumn at p6_6
    show yoshi comp1 at p6_6
    voice audio.lloyd_v_aww1a2
    l "Aww… I will miss having you around, sir… Do you really have to leave us?"
    l "Our nightly shenanigans won’t be the same without you!"

    show jin awkward6 at p6_4
    voice audio.jin_v_aww1a1
    j "I-I have grown really attached to Sir Goro over the months… It’s nice having a daddy— I mean, father figure…"

    show lloyd worry2 at p6_2
    voice audio.lloyd_v_agree5a
    l "I know right?! I never got the chance to get to know Sir Goro this well when we were scouts!"

    show aiden comp2 at p6_1
    voice audio.aiden_v_comeon1b1
    a "Come on, guys. It’s not like Gramps is dying or anything!"

    show lloyd angry5 at p6_2
    voice audio.lloyd_v_response2c1
    l "I know, I know! We just won’t spend as much time together if we aren’t roomies!"

    show darius talk2 at p6_3
    voice audio.darius_v_lloyd2
    d "Sir Goro wasn’t supposed to be bunking with us in the first place, Lloyd."

    show lloyd worry3 at p6_2
    voice audio.lloyd_v_yoshi4a
    l "What about Yoshi…? Do you really have to go too?"

    hide yoshi_autumn
    hide yoshi comp1
    show yoshi2_autumn at p6_6
    show yoshi2 comp3 at p6_6
    voice audio.yoshi_v_sorry4a
    yo "Haha, yeah, sorry guys. "

    show aiden talk4 at p6_1
    voice audio.aiden_v_actually1a
    a "It’s not too surprising, though! Yoshi’s been helping Gramps with all the management stuff, so it’ll be easier if they stay together!"

    show aiden wink2 at p6_1
    voice audio.aiden_v_laugh1b2
    a "Isn’t that right, Yoshi? *wink*"

    hide yoshi2_autumn
    hide yoshi2 comp3
    show yoshi_autumn at p6_6
    show yoshi shy6 at p6_6
    voice audio.yoshi_v_right5
    yo "Th-That’s right! It’ll be much more productive for both of us to stay close to the office! All the records are stored there after all!"

    show goro comp2 at p6_5
    voice audio.goro_v_comp2a1
    g "Don’t worry, everyone. We’ll still drop by here every now and then to hang out with you all. "
    g "We’re both still going to be with you for meals and breaks too. The only change is where we’re sleeping."

    show lloyd sigh4 at p6_2
    voice audio.lloyd_v_sigh2a
    l "*sigh* I guess there’s no stopping you then… "
    l "Huhuhu… No more fortune-telling sessions and crystal healings in the morning either…"

    show darius bored5 at p6_3
    voice audio.darius_v_question2c
    d "They’re literally next door, Lloyd."

    show lloyd angry2 at p6_2
    voice audio.lloyd_v_response1d1
    l "Fine! But don’t be surprised when we crash the office whenever we want!"

    show goro comp6 at p6_5
    voice audio.goro_v_response3a1
    g "I don’t mind. It can get dull and quiet there easily."

    show lloyd bold2 at p6_2
    voice audio.lloyd_v_amazed2a1
    l "Yay! Hear that, guys? We can bug them all the time now!"

    show darius play2 at p6_3
    voice audio.darius_v_rush2
    d "You missed the whole point, Lloyd. They’re trying NOT to get distracted."

    show jin comp3 at p6_4
    voice audio.jin_v_yeah2a
    j "Y-Yeah, I wouldn’t want to bother you guys while you’re working, after all.  "

    hide yoshi_autumn
    hide yoshi shy6
    show yoshi2_autumn at p6_6
    show yoshi2 comp6 at p6_6
    voice audio.yoshi_v_laugh6
    yo "Ahehe, don’t worry guys. We’ll make sure to balance out our time."

    show aiden talk3 at p6_1
    voice audio.aiden_v_anyway1a
    a "Anyway, I think that should be all you guys’ stuff, right? "

    show goro talk3 at p6_5
    voice audio.goro_v_agree2a1
    g "Ah, yes. Thank you for helping us pack. I still have most of my personal stuff stored in the shed, though."
    g "There wasn’t enough room in here, and I didn’t want to have Emilia share storage space with me in the room."

    show aiden happy2 at p6_1
    voice audio.aiden_v_encourage2a
    a "Let us carry all this back to your room, Gramps! You can head over to the shed for your stuff!"

    show goro happy2 at p6_5
    voice audio.goro_v_amazed2a1
    g "Ah, that’s perfect. I appreciate all the help."

    show aiden laugh1 at p6_1
    voice audio.aiden_v_response1a
    a "No problem, Gramps!"

    show goro happy1 at p6_5
    voice audio.goro_v_rush3a1
    g "Come with me, Yoshinori."

    hide yoshi2_autumn
    hide yoshi2 comp6
    show yoshi_autumn at p6_6
    show yoshi happy1 at p6_6
    voice audio.yoshi_v_right2
    yo "Right behind you!"

    hide goro_autumn
    hide goro happy1
    hide yoshi_autumn
    hide yoshi happy1
    with dissolve

    show aiden_autumn at p4_1
    show aiden comp1 at p4_1
    show lloyd_winter at p4_2
    show lloyd sad4 at p4_2
    show darius_winter at p4_3
    show darius norm3 at p4_3
    show jin_autumn at p4_4
    show jin_glasses at p4_4
    show jin comp1 at p4_4
    with move

    voice audio.lloyd_v_sad1a1
    l "Huhuhu… I miss them already!"

    show darius bored6 at p4_3
    voice audio.darius_v_lloyd2
    d "It’s only been three seconds, Lloyd."

    show jin confused2 at p4_4
    voice audio.jin_v_unsure1a2
    j "I don’t know if it’s just me, but… Doesn’t Sir Goro seem a bit closer to Yoshinori than everybody else…?"

    show lloyd talk4 at p4_2
    voice audio.lloyd_v_agree2b1
    l "Of course! They worked together the whole project, and they’ve always been a pair since we were scouts."

    show jin confuseddn2 at p4_4
    voice audio.jin_v_no2a
    j "N-No, I mean… It’s different even compared to when I first joined."
    j "Sir Goro’s behavior completely changes around Yoshinori… He’s a lot more… I don’t know… personal?"

    show darius think2 at p4_3
    voice audio.darius_v_agree1a
    d "Yes, I did notice that. When Yoshinori became his assistant, when we were on a vacation, and even more now."

    show lloyd confused5 at p4_2
    voice audio.lloyd_v_confused1c1
    l "Huh… he does seem pretty clingy, huh?"

    show aiden comp3 at p4_1
    voice audio.aiden_v_laugh1b2
    a "Hehe, you guys are just overthinking it~"
    a "Now come on, these boxes won’t move themselves!"

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

    $ location = location_shed
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_shed_day with fade
    play music old_familiar_home loop

    play sound sfx_boxesdrop
    show yoshi_winter2 at left2
    show yoshi norm1 at left2
    show goro_winter2 at right2
    show goro happy2 at right2
    voice audio.goro_vsg19_line1
    g "That should be all of it!"

    show yoshi shock2 at left2
    voice audio.yoshi_vsg19_line1
    yo "That’s… a lot of stuff, Goro… All of this came from your room…?"

    show goro explain2 at right2
    voice audio.goro_vsg19_line2
    g "Well, some of it’s already been stored in here for a couple years now. I figured it was time to bring it all back inside."

    voice audio.goro_vsg19_line3
    g "Actually, that’s one of the reasons I dragged you with me, I wanted to show you something."

    show yoshi confused2 at left2
    voice audio.yoshi_vsg19_line2
    yo "Oh, now I’m curious! What’s in these boxes, anyway?"

    hide goro_winter2
    hide goro explain2
    show goro2_winter2 at right2
    show goro2 think5 at right2
    voice audio.goro_vsg19_line4
    g "Hmm, it’s mostly stuff from my past that I stopped looking back at."

    hide yoshi_winter2
    hide yoshi confused2
    show yoshi2_winter2 at left2
    show yoshi2 worry3 at left2
    voice audio.yoshi_vsg19_line3
    yo "Oh…"

    hide goro2_winter2
    hide goro2 think5
    show goro_winter2 at right2
    show goro confused2 at right2
    voice audio.goro_vsg19_line5
    g "I can’t remember the last time I opened this one. "

    hide yoshi2_winter2
    hide yoshi2 worry3
    show yoshi_winter2 at left2
    show yoshi confused3 at left2
    voice audio.yoshi_vsg19_line4
    yo "Yeah… It looks like it’s collected a lot of dust! "

    show goro happy3 at right2
    voice audio.goro_vsg19_line6
    g "Ah, here they are!"

    show cg_fade at truecenter
    show fxg7 1 at fx_pos with dissolve
    voice audio.yoshi_vsg19_line5
    yo "Oh, these are pictures from way back…!"

    voice audio.goro_vsg19_line7
    g "Yes, and this one in particular is the first time I took Yuri camping."

    voice audio.yoshi_vsg19_line6
    yo "You both look so happy here!"

    voice audio.goro_vsg19_line8
    g "We were, but things weren’t so great before this moment…"

    voice audio.yoshi_vsg19_line7
    yo "What do you mean, sir…?"

    voice audio.goro_vsg19_line9
    g "When Yuri was growing up, she didn’t have the best environment at home…"

    voice audio.goro_vsg19_line10
    g "As the family’s breadwinner, I was often away from home, leaving Yuri to spend time with her mother."

    voice audio.goro_vsg19_line11
    g "She and her mother didn’t get along, and all Yuri saw when we were together was her parents arguing…"

    voice audio.goro_vsg19_line12
    g "It started affecting her studies… and even her overall demeanor changed thanks to all the pent-up frustrations…"

    voice audio.goro_vsg19_line13
    g "I realized that I had to take over and find a way to give Yuri the childhood she deserved."

    voice audio.goro_vsg19_line14
    g "And that’s when I started making more time for her as a father."

    voice audio.goro_vsg19_line15
    g "When I first took her out camping with me, she was so thrilled, and everything about her lit up like I hadn’t seen in years."

    voice audio.goro_vsg19_line16
    g "We both had a passion for adventure and loved the idea of doing those same activities together with the people we loved."

    voice audio.goro_vsg19_line17
    g "Now that we had something in common, I continued taking her out more and more, until I realized…"

    voice audio.goro_vsg19_line18
    g "I wanted it to last forever… not only for her, but for the both of us."

    hide cg_fade
    hide fxg7 1
    with dissolve

    show goro happy1 at right2
    voice audio.goro_vsg19_line19
    g "That’s when I started working harder… I wanted to save enough money to make that dream a reality. "

    show yoshi shock2 at left2
    voice audio.yoshi_vsg19_line8
    yo "Wait… Do you mean that—"

    show goro laugh3 at right2
    voice audio.goro_vsg19_line20
    g "Yes, that’s how Camp Buddy was born."

    show yoshi comp2 at left2
    voice audio.yoshi_vsg19_line9
    yo "Wow… That’s really heartwarming…"

    show goro comp2 at right2
    voice audio.goro_vsg19_line21
    g "The road to get there wasn’t easy at all, and it was only possible because Yuri was with me every step of the way."

    voice audio.goro_vsg19_line22
    g "You can imagine just how happy we both were to launch the very first term and finally get to share our dream with everyone else. With you."

    show yoshi comp5 at left2
    voice audio.yoshi_vsg19_line10
    yo "I can’t believe that’s how everything really started…"

    show goro laugh1 at right2
    voice audio.goro_vsg19_line23
    g "Haha, now you know the real history."

    voice audio.goro_vsg19_line24
    g "This place’s legacy is something that I want you to carry into the future, and share with others, too."

    show yoshi bold2 at left2
    voice audio.yoshi_vsg19_line11
    yo "It’s an honor to be a part of all this… I’ll try my hardest to make Camp Buddy the best it can be."

    show goro comp2 at right2
    voice audio.goro_vsg19_line25
    g "I know you will… But that’s not all I wanted to show you… "

    show cg_fade at truecenter
    show fxg8 1 at fx_pos with dissolve
    voice audio.yoshi_vsg19_line12
    yo "Oh my god… Is that who I think it is?! "

    voice audio.goro_vsg19_line26
    g "Yeah, that’s me, Vera, and a very tiny Yuri."

    voice audio.goro_vsg19_line27
    g "Yuri really takes after her mother, doesn't she?"

    voice audio.yoshi_vsg19_line13
    yo "Yeah… Although I barely recognized you, Goro…"

    voice audio.goro_vsg19_line28
    g "Well, Yuri was only two here. That makes me twenty-two around this time… "

    voice audio.yoshi_vsg19_line14
    yo "I-It’s not just that you look young, sir… even the way you dressed seems so out of character."

    voice audio.goro_vsg19_line29
    g "Well, having a child changed my life forever. I was striving for the perfect family and did my best to be an ideal father and husband."

    voice audio.goro_vsg19_line30
    g "Looking back, I really thought everything would go the way I imagined as long as I kept doing things the 'proper’ way."

    voice audio.goro_vsg19_line31
    g "Eventually, I realized that I was raising my daughter on my own, and that Vera and I lacked the foundation to be a proper couple."

    voice audio.goro_vsg19_line32
    g "I honestly can’t believe I managed it; we were both so young for all that responsibility. "

    voice audio.goro_vsg19_line33
    g "Most people that age were focused on taking care of themselves, and I don’t blame Vera for it. But I had to step up for Yuri’s sake."

    $ working = False
    $ shuffle_menu()
    menu():
        g "Most people that age were focused on taking care of themselves, and I don’t blame Vera for it. But I had to step up for Yuri’s sake.{fast}"
        "You deserved better.":
            $ working = True
            $ score_goro -= 2
            voice audio.yoshi_vsg19_line15a
            yo "You really deserved better…"

            voice audio.goro_vsg19_line34a
            g "That’s not the point."

            voice audio.goro_vsg19_line35ab
            g "Regardless of my past, I’m happy where I am today."
        "It must've been so difficult.":
            $ working = True
            $ score_goro -= 1
            voice audio.yoshi_vsg19_line15b
            yo "It must’ve been so difficult to make all those sacrifices."

            voice audio.goro_vsg19_line34b
            g "It was. But I don’t regret them."

            voice audio.goro_vsg19_line35ab
            g "Regardless of my past, I’m happy where I am today."
        "You're in a good place now.":
            $ working = True
            $ score_goro += 1
            voice audio.yoshi_vsg19_line15c
            yo "You’re in a good place now thanks to all the sacrifices you’ve made."

            voice audio.goro_vsg19_line34c
            g "Yes. I’m happy where I am in life. My past made me who I am today."
        "It made you who you are today.":
            $ working = True
            $ score_goro += 2
            voice audio.yoshi_vsg19_line15d
            yo "The past made you who you are today."

            voice audio.goro_vsg19_line34d
            g "Yes. And I’m thankful for it. I can finally say I’m happy where I am in life."
    hide cg_fade
    hide fxg8 1
    with dissolve

    show yoshi think2 at left2
    voice audio.yoshi_vsg19_line16
    yo "Even though I’ve known you for so long, there’s still so many things I’m learning about you…"

    hide goro_winter2
    hide goro comp2
    show goro2_winter2 at right2
    show goro2 play3 at right2
    voice audio.goro_vsg19_line36
    g "Heh, speaking of… I still want to show you one last picture."

    show cg_fade at truecenter
    show fxg9 1 at fx_pos with dissolve
    voice audio.yoshi_vsg19_line17
    yo "Whoa…! "

    voice audio.goro_vsg19_line37
    g "I know I told you I’d only talk about this once, but…"

    voice audio.goro_vsg19_line38
    g "I figured I’d show you what I looked like during my biker days rather than just leaving it to your imagination."

    voice audio.yoshi_vsg19_line18
    yo "This looks even better than what I imagined…!"

    voice audio.yoshi_vsg19_line19
    yo "That outfit and the bike behind you… You look so handsome, sir!"

    voice audio.goro_vsg19_line39
    g "Haha, I thought I looked so cool and tough wearing all that grunge and leather."

    voice audio.yoshi_vsg19_line20
    yo "But you really were, sir! How long ago was this?"

    voice audio.goro_vsg19_line40
    g "This was way before I had my family, even before I met my wife."

    voice audio.goro_vsg19_line41
    g "Heh… I remember I’d spend all my time and money customizing my bike, then showing it off to the gang."

    voice audio.goro_vsg19_line42
    g "It’s crazy how different my priorities were back then."

    voice audio.yoshi_vsg19_line21
    yo "But you really look like you’re having fun here, sir!"

    hide cg_fade
    hide fxg9 1
    with dissolve

    show yoshi confused2 at left2
    voice audio.yoshi_v_goro7
    yo "Where’s your bike now, Goro?"

    show goro2 think2 at right2
    voice audio.goro_v_think2a1
    g "I gave it to a friend, when I had Yuri. But I still have the original keys with me."
    g "In fact, I still have all my outfit and old stuff in the other boxes."

    $working = False
    $shuffle_menu()
    menu():
        g "In fact, I still have all my outfit and old stuff in the other boxes.{fast}"
        "It was time to move on.":
            $working = True
            $score_goro -= 2
            hide yoshi_winter2
            hide yoshi confused2
            show yoshi2_winter2 at left2
            show yoshi2 think3 at left2
            voice audio.yoshi_v_unsure3b
            yo "I guess that makes sense… It was time to move on then."
            yo "But don’t you miss having it?"

            show goro2 disappoint2 at right2
            voice audio.goro_v_agree3a2
            g "Of course, I do. Maybe one day I’ll get it back, if he still has it. "
        "Giving it up must've been hard.":
            $working = True
            $score_goro -= 1
            hide yoshi_winter2
            hide yoshi confused2
            show yoshi2_winter2 at left2
            show yoshi2 worry2 at left2
            voice audio.yoshi_v_aww1
            yo "Giving it up must’ve been hard…"

            show goro2 disappoint2 at right2
            voice audio.goro_v_but2a
            g "It was, but it was the right thing to do."
            g "Maybe one day I’ll be able to get it back though, if he still has it."
        "I want to see you wear it again.":
            $working = True
            $score_goro += 1
            show yoshi happy2 at left2
            voice audio.yoshi_v_oh2
            yo "Oh, I’d love to see you wear the outfit!"

            show goro2 play2 at right2
            voice audio.goro_v_heh1a
            g "I won’t deny, I would love to put it on and go for a ride again."

            show yoshi bold2 at left2
            voice audio.yoshi_v_laugh1
            yo "Maybe you could go get it back from that friend!"

            show goro2 laugh1 at right2
            voice audio.goro_v_laugh2a
            g "Haha, one day, perhaps!"
        "Take me on a ride one day.":
            $working = True
            $score_goro += 2
            show yoshi bold2 at left2
            voice audio.yoshi_v_oh2
            yo "Maybe one day you can get the bike back… and take me on a ride!"

            show goro2 laugh1 at right2
            voice audio.goro_v_laugh2a
            g "Hahaha! That eager to make me relive my glory days, huh?"
            g "I won’t deny I would love to ride again - one day, perhaps!"

    hide yoshi_winter2
    hide yoshi bold2
    show yoshi2_winter2 at left2
    show yoshi2 sigh4 at left2
    voice audio.yoshi_v_sigh3a
    yo "Man, you were doing all these cool things, and I was learning how to knit patches when I was that age… I feel so lame all of a sudden."
    yo "I can’t believe how we lived such opposite lives, Goro…"

    hide goro2_winter2
    hide goro2 laugh1
    hide goro2 disappoint2
    show goro_winter2 at right2
    show goro happy1 at right2
    voice audio.goro_v_conj1a1
    g "And yet here we are. Going against all odds."

    hide yoshi2_winter2
    hide yoshi2 sigh4
    show yoshi_winter2 at left2
    show yoshi confused2 at left2
    voice audio.yoshi_v_think3
    yo "After everything I’ve learned…  Can I ask why you wanted to show me all this, Goro?"

    show goro explain2 at right2
    voice audio.goro_v_well1a
    g "For the longest time, I kept all of these memories locked away, thinking it was what I needed in order to change…"
    g "Back then, I wouldn’t even dare to look at this myself, let alone show it to someone else."

    show goro comp2 at right2
    voice audio.goro_v_conj3a1
    g "But now it just feels liberating… it’s making me realize how far I’ve come."
    g "After what happened back at the hotel, I realized that I don’t need to bury my past anymore."

    show goro comp3 at right2
    voice audio.goro_v_glad1a
    g "I may have given up a lot of things, but I’ve also earned more than I ever hoped for."
    g "Camp Buddy… This family we built… And you."

    show yoshi comp2 at left2
    voice audio.yoshi_v_goro4
    yo "Goro…"

    show goro explain3 at right2
    voice audio.goro_v_conj4a
    g "Not only that, but my delinquent days were also a joyful time of my life… They’re a genuine part of who I am."

    show goro comp2 at right2
    voice audio.goro_v_thanks2b1
    g "I know I’ve said this a lot already, but thank you for encouraging me to not be ashamed of my past and…"
    g "Teaching me to be myself again… "

    show yoshi bold2 at left2
    voice audio.yoshi_v_but2
    yo "But you did that yourself...! You were the one who’s opened up to me on your own."
    yo "I was only able to help because you let me…"

    hide goro_winter2
    hide goro comp2
    show goro2_winter2 at right2
    show goro2 explain1 at right2
    voice audio.goro_v_ehem1a
    g "*ehem* I didn’t mean for this to get so cheesy."
    g "Anyway, that’s all of the interesting stuff for now, I can show you the other pictures after we carry all this to our room."

    show yoshi laugh1 at left2
    voice audio.yoshi_v_alright2
    yo "Haha, alright! I want to see more photos of you with your bike!"

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black with fade
    yo "{i}Goro and I carried everything into our room and spent the rest of the day unpacking and chatting casually about his things.{/i}"
    yo "{i}Goro has come such a long way to be able to be so open with me… It’s like the floodgates have opened and he’s so excited to tell me all about his life.{/i}"
    yo "{i}I’m so happy I get to be a part of it!{/i}"

    scene cg black
    hide screen location
    hide screen timeline
    hide screen quick_menu
    $quick_menu = False
    with fade
    $ time_transition_day_to_sunset_winter2()
    $ renpy.pause (2.0, hard=True)

    $ location = location_messhall
    $ time = timeline_timesunset
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_messhall_winter_sunset with fade
    play music here_they_come loop

    show yoichi_autumn at p10_1
    show yoichi normal1 at p10_1
    show taiga_autumn at p10_2
    show taiga normal1 at p10_2
    show emilia_winter3 at p10_3
    show emilia norm1 at p10_3
    show aiden_autumn at p10_5
    show aiden amazed2 at p10_5
    show yuri_autumn at p10_4
    show yuri norm1 at p10_4
    show darius_winter at p10_7
    show darius norm1 at p10_7
    show goro_autumn at p10_9
    show goro shock1 at p10_9
    show yoshi_autumn at p10_10
    show yoshi shock1 at p10_10
    show lloyd_winter at p10_6
    show lloyd norm1 at p10_6
    show jin_autumn at p10_8
    show jin_glasses at p10_8
    show jin norm1 at p10_8
    voice audio.aiden_v_hey1b3
    a "Eyyy! The guests of honor are finally here!"

    show yoshi shock2 at p10_10
    voice audio.yoshi_v_what2
    yo "Wh-What?"

    hide goro_autumn
    hide goro shock1
    show goro2_autumn at p10_9
    show goro2 confused2 at p10_9
    hide jin_autumn
    hide jin_glasses
    hide jin norm1
    show jin_autumn at p10_8
    show jin_glasses at p10_8
    show jin norm1 at p10_8
    voice audio.goro_v_confused1a1
    g "Huh? What’s going on here?"

    show yuri happy2 at p10_4
    voice audio.yuri_v_rush1a3
    yu "Come here, Dad! Sit with us~!"

    show goro2_autumn at p10_6
    show goro2 confused3 at p10_6
    show yoshi_autumn at p10_7
    show yoshi shock1 at p10_7
    show lloyd_winter at p10_8
    show lloyd norm1 at p10_8
    show darius_winter at p10_9
    show darius norm1 at p10_9
    show jin_autumn at p10_10
    show jin_glasses at p10_10
    show jin norm1 at p10_10
    with move

    hide goro2_autumn
    hide goro2 confused3
    show goro_autumn at p10_6
    show goro confused3 at p10_6
    voice audio.goro_v_so1b
    g "So, what’s with the sudden party? "

    show lloyd bold2 at p10_8
    voice audio.lloyd_v_conj1a3
    l "Well, since it’s you two’s last day in our cabin, we thought we should take the chance to send you off with a bang!"
    l "We’ll really miss you guys! Boo hoo!"

    hide yoshi_autumn
    hide yoshi shock1
    show yoshi2_autumn at p10_7
    show yoshi2 shy5 at p10_7
    hide lloyd_winter
    hide lloyd bold2
    show lloyd_winter at p10_8
    show lloyd bold2 at p10_8
    voice audio.yoshi_v_uh1a
    yo "Is that really the reason…?"

    hide goro_autumn
    hide goro confused3
    show goro2_autumn at p10_6
    show goro2 annoy2 at p10_6
    voice audio.goro_v_really4a
    g "Didn’t we just have a party last night? This seems like an excuse to have another one. "

    show darius happy1 at p10_9
    voice audio.darius_v_conj1a1
    d "It is. But Lloyd and I also finished up the repairs today, so we wanted to celebrate."

    show lloyd excited3 at p10_8
    voice audio.lloyd_v_agree2b1
    l "Yeah! Let’s get in one last hurrah together before the workers get back!"

    show aiden comp6 at p10_5
    voice audio.aiden_v_laugh1b2
    a "Hehe~ It’s nothing too fancy, just a little drinking session to make us all feel warm and fuzzy inside!"

    hide yoshi2_autumn
    hide yoshi2 shy5
    show yoshi_autumn at p10_7
    show yoshi shock3 at p10_7
    hide lloyd_winter
    hide lloyd excited3
    show lloyd_winter at p10_8
    show lloyd excited3 at p10_8
    voice audio.yoshi_v_what4
    yo "What?! There’s more alcohol?!"

    hide goro2_autumn
    hide goro2 annoy2
    show goro_autumn at p10_6
    show goro bored2 at p10_6
    voice audio.goro_v_yuri6a
    g "I’m surprised you let everyone drink again, Yuri… Even the scouts…"

    show taiga annoyed2 at p10_2
    voice audio.taiga2_v_hey1f
    t "Hey! We’re not scouts right now, we work here just like y’all!"

    show yoichi excited1 at p10_1
    voice audio.yoichi_v_agree1d1
    yi "YEAH! Pass over the booze already!"

    hide yoshi_autumn
    hide yoshi shock3
    show yoshi2_autumn at p10_7
    show yoshi2 sigh1 at p10_7
    hide lloyd_winter
    hide lloyd excited3
    show lloyd_winter at p10_8
    show lloyd excited3 at p10_8
    voice audio.yoshi_v_sigh3a
    yo "*sigh* I guess it wouldn’t hurt to hang out together one more time…"

    hide goro_autumn
    hide goro bored2
    show goro2_autumn at p10_6
    show goro2 tease2 at p10_6
    voice audio.goro_v_yoshi14a
    yo "Well, I’m down. Yoshinori, you’re getting drunk tonight."

    hide yoshi2_autumn
    hide yoshi2 sigh1
    show yoshi_autumn at p10_7
    show yoshi panic3 at p10_7
    hide lloyd_winter
    hide lloyd excited3
    show lloyd_winter at p10_8
    show lloyd excited3 at p10_8
    voice audio.yoshi_v_shock3
    yo "Gah! I can’t afford to have a hangover tomorrow!"

    show goro2 tease5 at p10_6
    voice audio.goro_v_heh1a
    g "Heh, better work on your tolerance then. "

    show jin thinkdn3 at p10_10
    voice audio.jin_v_conj1b1
    j "Now that I think about it… I don’t think I’ve ever heard of a workplace that parties this much together…"

    play sound sfx_shotglass
    show emilia angry5 at p10_3
    voice audio.emilia_v_ugh1
    e "Ugh! I know right?! It’s like we’re not in the middle of a project!"

    show lloyd tease2 at p10_8
    voice audio.lloyd_v_laugh1a1
    l "You say that as you gulp down that shot."

    show emilia eyeroll3 at p10_3
    voice audio.emilia_v_hmph1a
    e "Hmph, I’m just trying to fit in with the group. "

    show yuri pout1 at p10_4
    voice audio.yuri_v_angry4a1
    yu "Jeez, where was this Emilia back at the hotel?"

    show emilia irked2 at p10_3
    voice audio.emilia_v_question2a1
    e "Really? We’re going through this again?"

    show aiden excited3 at p10_5
    voice audio.aiden_v_anyway1a
    a "Anywayyyy since it’s a party, let’s play a game while we drink!"

    show lloyd excited4 at p10_8
    voice audio.lloyd_v_shock1b1
    l "Oooh! Party games! Me likey! "

    show emilia confused2 at p10_3
    voice audio.emilia_v_question1b2
    e "Party games? Like musical chairs? What are we, five?"

    show aiden play3 at p10_5
    voice audio.aiden_v_conj1
    a "Obviously Emilia here hasn’t gotten a taste of how we do things at Camp Buddy."
    a "Things get spicy when you’re tipsy~"

    show yuri tease2 at p10_4
    voice audio.yuri_v_laugh1b1
    yu "Hihihi~ I like where you’re going with this, Aiden~"

    show emilia angry5 at p10_3
    voice audio.emilia_v_disagree2a1
    e "*sigh* Count me out."

    hide jin_autumn
    hide jin_glasses
    hide jin thinkdn3
    show jin2_autumn at p10_10
    show jin2_glasses at p10_10
    show jin2 fudan2 at p10_10
    voice audio.jin_v_really2a
    j "S-Spicy you say…?!"

    show aiden bold5 at p10_5
    voice audio.aiden_v_conj4a
    a "Now, since Yoshi and Gramps are our special guests, why don’t we give ’em the honor of picking what game we play?"

    hide goro2_autumn
    hide goro2 tease5
    show goro_autumn at p10_6
    show goro happy2 at p10_6
    voice audio.goro_v_yoshi2a
    g "It’s your choice, Yoshinori."

    $ working = False
    $ shuffle_menu()
    menu():
        g "It’s your choice, Yoshinori.{fast}"
        "Never have I ever.":
            $working = True
            jump day8_goro_lloyd
        "Truth or dare.":
            $working = True
            jump day8_goro_jin
        "Rock-Paper-Scissors.":
            $working = True
            jump day8_goro_aiden
        "Picture Charades.":
            $working = True
            jump day8_goro_yuri

label day8_goro_lloyd:
    $lloyd_ending = True
    show yoshi think2 at p10_7
    voice audio.yoshi_v_unsure3a
    yo "I guess let’s try ‘Never Have I Ever.’ How does it work again exactly?"

    show yuri bold2 at p10_4
    voice audio.yuri_v_oh1a
    yu "Oh, it’s easy! You go around the room and take turns saying something you’ve never done!"
    yu "If anyone else has done it, they lose a point, and if they lose three points then they’re out!"

    show goro talk2 at p10_6
    voice audio.goro_v_think1a1
    g "Sounds simple enough."

    show yuri happy1 at p10_4
    voice audio.yuri_v_alright1a2
    yu "Alright! Let’s start then!"

    show aiden talk3 at p10_5
    voice audio.aiden_v_sorry1a1
    a "You’ll have to count me out of this one, Yuri! I gotta make some snacks for us real quick!"
    a "Plus, I think I’d probably lose pretty quickly, hehe."

    show yuri pout1 at p10_4
    voice audio.yuri_v_aww2a
    yu "Aww, come on, Aiden! I have some theories I wanted to test on you!"

    show emilia eyeroll4 at p10_3
    voice audio.emilia_v_ugh1
    e "Eugh, on that note, I’m coming with you, Aiden."

    hide aiden_autumn
    hide aiden talk3
    show aiden2_autumn at p10_5
    show aiden2 shock2 at p10_5
    voice audio.aiden_v_confused1a2
    a "Eh?! What for?"

    show emilia explain3 at p10_3
    voice audio.emilia_v_well1
    e "You need somebody to help with the snacks, and it IS my job now, after all."

    hide aiden2_autumn
    hide aiden2 shock2
    show aiden_autumn at p10_5
    show aiden happy2 at p10_5
    voice audio.aiden_v_alright1a1
    a "Haha, alright then! We’ll be right back!"

    hide aiden_autumn
    hide aiden happy2
    hide emilia_winter3
    hide emilia explain3
    with dissolve

    show yoichi_autumn at p8_1
    show yoichi normal1 at p8_1
    show taiga_autumn at p8_2
    show taiga normal1 at p8_2
    show yuri_autumn at p8_3
    show yuri rage1 at p8_3
    show goro_autumn at p8_4
    show goro norm1 at p8_4
    show yoshi_autumn at p8_5
    show yoshi norm1 at p8_5
    show lloyd_winter at p8_6
    show lloyd norm1 at p8_6
    show darius_winter at p8_7
    show darius norm1 at p8_7
    show jin2_autumn at p8_8
    show jin2_glasses at p8_8
    show jin2 perv1 at p8_8
    with move

    hide yuri_autumn
    hide yuri rage1
    show yuri_autumn at p8_3
    show yuri rage1 at p8_3
    voice audio.yuri_v_what5a
    yu "WHAT?! That’s two out already, no fair!"

    show yoshi comp5 at p8_5
    voice audio.yoshi_v_comp4
    yo "Haha, don’t worry, Yuri, the rest of us will play with you."

    show yuri think3 at p8_3
    voice audio.yuri_v_think1a1
    yu "Hmmm… alright. I guess I can still get some good info out of all of you."
    yu "I’ll start! Never have I ever had sex!"

    show jin2 comic2 at p8_8
    voice audio.jin_v_laugh7a
    j "Pfft…!"

    show yoshi shock2 at p8_5
    voice audio.yoshi_v_yuri7
    yo "Y-Yuri!"

    show goro sigh2 at p8_4
    voice audio.goro_v_sigh2a
    g "*sigh* I should’ve guessed that’d be her first question."

    show taiga angry2 at p8_2
    voice audio.taiga2_v_denial3a
    t "I’m not answering that!"

    show yoichi talking3 at p8_1
    voice audio.yoichi_v_hmph1a
    yi "I lost a point."

    show darius play2 at p8_7
    voice audio.darius_v_agree4
    d "Same. And so did Lloyd."

    show lloyd angry2 at p8_6
    voice audio.lloyd_v_darius8b
    l "D-Dar! Don’t throw me under the bus like that!"

    show yuri play2 at p8_3
    voice audio.yuri_v_rush1b1
    yu "Interestiiiing~ So that answers that for Yoichi, Darius and Lloyd. The rest of you, speak up!"

    hide jin2_autumn
    hide jin2_glasses
    hide jin2 comic2
    show jin_autumn at p8_8
    show jin_glasses at p8_8
    show jin awkward6 at p8_8
    voice audio.jin_v_aww1a1
    j "I-I still keep my points…"

    show yuri comp2 at p8_3
    voice audio.yuri_v_aww1a
    yu "Aww, Jin! Don’t worry, there’s still a few months of the project left to get some action~"

    hide jin_autumn
    hide jin_glasses
    hide jin awkward6
    show jin2_autumn at p8_8
    show jin2_glasses at p8_8
    show jin2 fudan2 at p8_8
    voice audio.jin_v_gulp1a
    j "*gulp* W-With who…?"

    hide goro_autumn
    hide goro sigh2
    show goro2_autumn at p8_4
    show goro2 play2 at p8_4
    voice audio.goro_v_heh1a
    g "Yoshinori and I lose a point."

    show yoshi panic3 at p8_5
    voice audio.yoshi_v_shock4
    yo "G-Gah! "

    show yuri confused2 at p8_3
    voice audio.yuri_v_really1b
    yu "Oh, really? I guess I wouldn’t exist if Dad didn’t. Who was yours with, Yoshi?"

    show yoichi annoyed1 at p8_1
    voice audio.yoichi_v_sarcastic1a
    yi "Duh! It’s with the old—"

    hide yoshi_autumn
    hide yoshi panic3
    show yoshi2_autumn at p8_5
    show yoshi2 explain2 at p8_5
    voice audio.yoshi_v_ehem1a
    yo "*ehem* I-I don’t think that was the question, Yuri."

    show yuri pout1 at p8_3
    voice audio.yuri_v_hmph1a
    yu "Hmph, fine. Last one is you, Taiga! Speak up."

    show taiga angry5 at p8_2
    voice audio.taiga2_v_disagree1b
    t "Nope. This game’s already too weird, I’m out."

    hide taiga_autumn
    hide taiga angry5
    with dissolve

    show yoichi angry1 at p8_1
    voice audio.yoichi_v_greet1d1
    yi "HEY! No backing out, you pussycat! Tell ’em who you’re fucking!"

    voice audio.taiga_v_sarcastic1
    t "Not telling!"

    show yoichi angry6 at p8_1
    voice audio.yoichi_v_insult1a
    yi "Yes, you are! Get back here!"

    hide yoichi_autumn
    hide yoichi angry6
    with dissolve

    show yuri_autumn at p6_1
    show yuri irked2 at p6_1
    show goro2_autumn at p6_2
    show goro2 tease1 at p6_2
    show yoshi2_autumn at p6_3
    show yoshi2 awkward1 at p6_3
    show lloyd_winter at p6_4
    show lloyd pout1 at p6_4
    show darius_winter at p6_5
    show darius norm1 at p6_5
    show jin2_autumn at p6_6
    show jin2_glasses at p6_6
    show jin2 perv1 at p6_6
    with move

    voice audio.yuri_v_ugh3a
    yu "Ugh, there goes two more of my players."

    show yoshi2 awkward3 at p6_3
    voice audio.yoshi_v_well3
    yo "W-Well, what did you expect starting with that kind of question?"

    show yuri pout4 at p6_1
    voice audio.yuri_v_agree5a1
    yu "Hmph. Fine, then it’s your go next, Yoshi."

    hide yoshi2_autumn
    hide yoshi2 awkward3
    show yoshi_autumn at p6_3
    show yoshi think2 at p6_3
    voice audio.yoshi_v_oh2
    yo "O-Oh, alright! Hmmm… Let me think."
    yo "Never have I ever… Been on vacation with someone here!"

    hide jin2_autumn
    hide jin2_glasses
    hide jin2 perv1
    show jin_autumn at p6_6
    show jin_glasses at p6_6
    show jin awkward1 at p6_6
    show darius bored1 at p6_5
    show lloyd bored5 at p6_4
    hide goro2_autumn
    hide goro2 tease1
    show goro_autumn at p6_2
    show goro annoy1 at p6_2
    show yuri annoy1 at p6_1
    all "..."

    show yuri annoy4 at p6_1
    voice audio.yuri_v_rush1b1
    yu "Come on, Yoshi! Do better than that!"

    show yoshi shock2 at p6_3
    voice audio.yoshi_v_why3
    yo "E-Eh, why?"

    hide goro_autumn
    hide goro annoy1
    show goro2_autumn at p6_2
    show goro2 bored1 at p6_2
    voice audio.goro_v_really4a
    g "We literally all just went on a vacation together, Yoshinori…"

    hide yoshi_autumn
    hide yoshi shock2
    show yoshi2_autumn at p6_3
    show yoshi2 comp6 at p6_3
    voice audio.yoshi_v_right4
    yo "O-Oh, right… Oops."

    show goro2 play3 at p6_2
    voice audio.goro_v_confident1a
    g "I’ll try next. I have the perfect one."
    g "Hehe… Never have I ever had a crush on someone during the first term."

    show yuri tease2 at p6_1
    voice audio.yuri_v_laugh1b1
    yu "Not me~ "

    show jin thinkdn4 at p6_6
    voice audio.jin_v_think1a1
    j "I-I wasn’t even here the first term…"

    show lloyd pout2 at p6_4
    voice audio.lloyd_v_groan2b3
    l "This is no fair! It’s like you guys are targeting me and Dar!"

    show darius shy5 at p6_5
    voice audio.darius_v_think2a1
    d "You just outed me."

    hide yuri_autumn
    hide yuri tease2
    show yuri2_autumn at p6_1
    show yuri2 fangirl2 at p6_1
    voice audio.yuri_v_kyaa1a
    yu "KYAAAA! You two are so cuuuute~! "

    show yoshi2 shy5 at p6_3
    voice audio.yoshi_v_well1
    yo "Well, I… lost a point, too"

    hide yuri2_autumn
    hide yuri2 fangirl2
    show yuri_autumn at p6_1
    show yuri play2 at p6_1
    voice audio.yuri_v_think1a1
    yu "Hmmm… Is this the same person you had sex with, Yoshi~?"

    hide yoshi2_autumn
    hide yoshi2 shy5
    show yoshi_autumn at p6_3
    show yoshi irked1 at p6_3
    voice audio.yoshi_v_ehem1a
    yo "Again, that’s not the game, Yuri."

    show yuri explain3 at p6_1
    voice audio.yuri_v_well1a
    yu "Well, it looks like Yoshi, Lloyd, and Darius only have only one point left now, so they might lose!"

    show lloyd annoy2 at p6_4
    voice audio.lloyd_v_denial2a1
    l "It’s your turn, Jin, and you better not bully us!"

    show jin talk3 at p6_6
    voice audio.jin_v_conj2b2
    j "I-I do have something I’ve been dying to know."

    show yuri excited2 at p6_1
    voice audio.yuri_v_laugh1b1
    yu "Hihi, this one ought to be good~"

    show jin explain3 at p6_6
    voice audio.jin_v_think1b1
    j "Never have I ever had sex..."

    show lloyd rage3 at p6_4
    voice audio.lloyd_v_question1b1
    l "That’s the same thing Yuri said!"

    hide jin_autumn
    hide jin_glasses
    hide jin explain3
    show jin2_autumn at p6_6
    show jin2_glasses at p6_6
    show jin2 fudan2 at p6_6
    voice audio.jin_v_fudan1b1
    j "...in the scoutmaster cabin while others were around."

    hide yuri_autumn
    hide yuri excited2
    show yuri2_autumn at p6_1
    show yuri2 fangirl2 at p6_1
    voice audio.yuri_v_kyaa1a
    yu "KYAA! Perfect question for our departures theme tonight~!"
    yu "Obviously I don’t stay with you guys, so, no! Alright, speak up, all of you!"

    hide goro2_autumn
    hide goro2 play3
    show goro_autumn at p6_2
    show goro disappoint2 at p6_2
    voice audio.goro_v_no1a1
    g "Not me."

    show yoshi awkward4 at p6_3
    voice audio.yoshi_v_no1
    yo "Me neither…!"

    show yuri2 excited3 at p6_1
    voice audio.yuri_v_so2a
    yu "How about you, Lloyd and Darius?! "

    show lloyd pout5 at p6_4
    l "..."

    show darius explain2 at p6_5
    voice audio.darius_v_think1a1
    d "We’re both out."

    show jin2 scheme2 at p6_6
    voice audio.jin_v_fudan4a1
    j "So that was you two I heard last night…"

    show yuri2 drool2 at p6_1
    voice audio.yuri_v_what5a
    yu "WHAT?! TELL ME THE DETAILS!"

    show lloyd rage3 at p6_4
    voice audio.lloyd_v_geez1b1
    l "No fair! You guys already know how Dar and I are, so you picked those questions on purpose! "

    hide yoshi_autumn
    hide yoshi awkward4
    show yoshi2_autumn at p6_3
    show yoshi2 worry2 at p6_3
    voice audio.yoshi_v_disagree2
    yo "I-I don’t think that was our intent, Lloyd…"

    show lloyd rage4 at p6_4
    voice audio.lloyd_v_agree4c1
    l "Oh yeah?! Then how do you explain the rest of you having so many points left?!"

    show darius comp2 at p6_5
    voice audio.darius_v_comp1a2
    d "Relax, Lloyd. It’s not serious."

    hide yuri2_autumn
    hide yuri2 drool2
    show yuri_autumn at p6_1
    show yuri shock1 at p6_1
    hide jin2_autumn
    hide jin2_glasses
    hide jin2 scheme2
    show jin_autumn at p6_6
    show jin_glasses at p6_6
    show jin shock1 at p6_6
    show goro shock1 at p6_2
    show lloyd angry2 at p6_4
    voice audio.lloyd_v_question1b1
    l "What?! What do you mean ‘Not serious’?!"

    show darius play2 at p6_5
    voice audio.darius_v_laugh2a
    d "‘Sirius’, hehe."

    show lloyd disappoint3 at p6_4
    voice audio.lloyd_v_rush1a2
    l "I’m not joking! What’s wrong with you, Dar?!"

    show darius worry2 at p6_5
    voice audio.darius_v_worry1a
    d "Oh no. What did I say…?"

    show lloyd angry2 at p6_4
    voice audio.lloyd_v_groan2c1
    l "It’s what you didn’t say! "

    show darius confused2 at p6_5
    voice audio.darius_v_think2b1
    d "Uhh…"

    show lloyd rage3 at p6_4
    voice audio.lloyd_v_request1a
    l "We’ve been together long enough, haven’t we? I take this relationship seriously!"

    show darius worry4 at p6_5
    voice audio.darius_v_think2a2
    d "I think you misunderstood…"

    show lloyd pain5 at p6_4
    voice audio.lloyd_v_shock4a1
    l "Gah! Nevermind! I’m just going to get some snacks!"

    hide lloyd_winter
    hide lloyd pain5
    with dissolve

    show darius worry3 at p6_5
    voice audio.darius_v_wait1b
    d "Hold on. Let’s talk!"

    hide darius_winter
    hide darius worry3
    with dissolve

    show yuri_autumn at p4_1
    show yuri shock1 at p4_1
    show goro_autumn at p4_2
    show goro norm3 at p4_2
    show yoshi2_autumn at p4_3
    show yoshi2 confused2 at p4_3
    show jin_autumn at p4_4
    show jin_glasses at p4_4
    show jin worry1 at p4_4
    with move

    voice audio.yoshi_v_confused1a
    yo "Wh-What was that about?"

    show yuri comp4 at p4_1
    voice audio.yuri_v_laugh1b1
    yu "Hehe, looks like a lover’s quarrel~"

    show jin worry4 at p4_4
    voice audio.jin_v_hngh1a
    j "Hngh… Now I feel bad…"

    hide goro_autumn
    hide goro norm3
    show goro2_autumn at p4_2
    show goro2 confused5 at p4_2
    voice audio.goro_v_think1a1
    g "Hmmm, I wonder if they’re struggling to find a label."

    hide yoshi2_autumn
    hide yoshi2 confused2
    show yoshi_autumn at p4_3
    show yoshi shock2 at p4_3
    voice audio.yoshi_v_what3
    yo "Wh-What?! Where are you guys getting all that?!"

    show yuri irked1 at p4_1
    voice audio.yuri_v_conj1b1
    yu "Seriously, Yoshi? Read the room!"

    show jin confuseddn3 at p4_4
    voice audio.jin_v_think2a1
    j "I-It was pretty obvious…"

    show yuri bold2 at p4_1
    voice audio.yuri_v_rush1b1
    yu "Now, come on! Yoshi has one point left, and I’m gonna make the most of it! It’s my turn again!"

    hide yoshi_autumn
    hide yoshi shock2
    show yoshi2_autumn at p4_3
    show yoshi2 sigh4 at p4_3
    voice audio.yoshi_v_sigh3a
    yo ""

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black with fade
    yo "{i}We finished the round, and eventually Lloyd and Darius came back.{/i}"
    yo "{i}We were glad that they seem to have calmed down, and rejoined the game.{/i}"
    yo "{i}Eventually, Aiden and Emilia came back with snacks, and we all kept partying for the rest of the evening!{/i}"

    jump day8_goro_aftersq

label day8_goro_jin:
    $sq_jin += 1
    show yoshi happy2 at p10_7
    voice audio.yoshi_v_think4
    yo "Let’s play Truth or Dare! It really takes me back to our scout days, haha!"

    hide yuri_autumn
    hide yuri tease2
    show yuri2_autumn at p10_4
    show yuri2 fangirl1 at p10_4
    voice audio.yuri_v_kyaa1a
    yu "KYAAA! That’s a great idea, Yoshi! I can’t wait to ‘dare’ everyone!"

    show aiden talk3 at p10_5
    voice audio.aiden_v_sorry1a1
    a "You’ll have to count me out of this one, Yuri! I gotta make some snacks for us real quick!"
    a "Plus, I think I’d probably lose pretty quickly, hehe."

    hide yuri2_autumn
    hide yuri2 fangirl1
    show yuri_autumn at p10_4
    show yuri pout1 at p10_4
    voice audio.yuri_v_aww2a
    yu "Aww, come on, Aiden! I have some theories I wanted to test on you!"

    show emilia eyeroll4 at p10_3
    voice audio.emilia_v_ugh1
    e "Eugh, on that note, I’m coming with you, Aiden."

    hide aiden_autumn
    hide aiden talk3
    show aiden2_autumn at p10_5
    show aiden2 shock2 at p10_5
    voice audio.aiden_v_confused1a2
    a "Eh?! What for?"

    show emilia explain3 at p10_3
    voice audio.emilia_v_well1
    e "You need somebody to help with the snacks, and it IS my job now, after all."

    hide aiden2_autumn
    hide aiden2 shock2
    show aiden_autumn at p10_5
    show aiden happy2 at p10_5
    voice audio.aiden_v_alright1a1
    a "Haha, alright then! We’ll be right back!"

    hide aiden_autumn
    hide aiden happy2
    hide emilia_winter3
    hide emilia explain3
    with dissolve

    show yoichi_autumn at p8_1
    show yoichi normal1 at p8_1
    show taiga_autumn at p8_2
    show taiga normal1 at p8_2
    show yuri_autumn at p8_3
    show yuri rage1 at p8_3
    show goro_autumn at p8_4
    show goro norm1 at p8_4
    show yoshi_autumn at p8_5
    show yoshi norm1 at p8_5
    show lloyd_winter at p8_6
    show lloyd norm1 at p8_6
    show darius_winter at p8_7
    show darius norm1 at p8_7
    show jin2_autumn at p8_8
    show jin2_glasses at p8_8
    show jin2 perv1 at p8_8
    with move

    voice audio.yuri_v_what5a
    yu "WHAT?! That’s two out already, no fair!"

    show yoshi comp5 at p8_5
    voice audio.yoshi_v_comp4
    yo "Haha, don’t worry, Yuri, the rest of us will play with you."

    show lloyd tease3 at p8_6
    voice audio.lloyd_v_laugh1a1
    l "We’re game too! It’s called Truth or DAR after all, ehhhhhhhhh?"

    show darius bored5 at p8_7
    voice audio.darius_v_cringe1a
    d "That was lame."

    show yuri think3 at p8_3
    voice audio.yuri_v_think1a1
    yu "Hmmm… alright. I guess I can still get some good info out of all of you."
    yu "I’ll start! Yoichi, truth or dare!"

    show yoichi confident3 at p8_1
    voice audio.yoichi_v_sarcastic1a
    yi "Dare, duh! What else would it be?"

    hide yuri_autumn
    hide yuri think3
    show yuri2_autumn at p8_3
    show yuri2 fangirl1 at p8_3
    voice audio.yuri_v_kyaa1a
    yu "KYAAA! Yes, I knew you would say that! Now, I have this box in the shed—"

    hide goro_autumn
    hide goro norm1
    show goro2_autumn at p8_4
    show goro2 annoy2 at p8_4
    voice audio.goro_v_yuri5b
    g "Nothing inappropriate, Yuri."

    hide yuri2_autumn
    hide yuri2 fangirl1
    show yuri_autumn at p8_3
    show yuri rage1 at p8_3
    voice audio.yuri_v_what2a
    yu "Whaaaaat?! That takes out all the fun!"

    show yoichi playful1 at p8_1
    voice audio.yoichi_v_rush2b2
    yi "Bring it on! I’m not scared of anything this crazy lady throws at me! "

    hide yuri_autumn
    hide yuri rage1
    show yuri2_autumn at p8_3
    show yuri2 fangirl2 at p8_3
    voice audio.yuri_v_conj2d1
    yu "See, Dad?! Yoichi doesn’t mind! Now get out of those clothes—"

    show yoichi talking3 at p8_1
    voice audio.yoichi_v_agree2b1
    yi "Done."

    hide yoichi_autumn
    hide yoichi playful1
    show yoichi_undie at p8_1
    show yoichi normal1 at p8_1
    with dissolve

    show jin2 fudan3 at p8_8
    voice audio.jin_v_laugh7b
    j "*splutters* SO FAST!"

    show yuri2 drool3 at p8_3
    voice audio.yuri_v_kyaa1a
    yu "KYAAA! SO LITTLE SHAME!"

    show lloyd confused3 at p8_6
    voice audio.lloyd_v_sigh2a
    l "Seriously. How does everyone here strip so fast?"

    show darius play2 at p8_7
    voice audio.darius_v_laugh1
    d "Plenty of practice."

    show yoshi angry3 at p8_5
    voice audio.yoshi_v_yoichi1
    yo "Yoichi! Put your pants back on!"

    show yoichi annoyed1 at p8_1
    voice audio.yoichi_v_question1a3
    yi "What? That was the dare. I ain’t no chicken!"

    show taiga sigh2 at p8_2
    voice audio.taiga_v_sigh1
    t "I’m just glad you kept your undies on, no one wants to see your overgrown bush…"

    show jin2 comic2 at p8_8
    voice audio.jin_v_laugh8a
    j "PFFFFT!! *spits out drink*"

    show yoichi confident3 at p8_1
    voice audio.yoichi_v_hmph1a
    yi "You’re just jealous ’cause I’m bigger than you!"

    show taiga annoyed4 at p8_2
    voice audio.taiga2_v_disagree1b
    t "No, you’re not."

    show yoichi excited1 at p8_1
    voice audio.yoichi_v_taiga3a
    yi "Then it’s your turn, Dynamite! I dare you to get naked! "

    show taiga angry2 at p8_2
    voice audio.taiga_v_wtf3
    t "Wh-What the fuck?! That’s not how the game works! "

    show yuri2 ahegao1 at p8_3
    voice audio.yuri_v_fujo4a
    yu "DOESN’T MATTER! DO IT, TAIGA! SHOW US YOU’RE A REAL MAN!" with vpunch

    show jin2 comic4 at p8_8
    voice audio.jin_v_yes6a
    j "YES, PLEASE DO! LET ME SEE THE GARDEN OF EDEN!"

    show yoshi irked1 at p8_5
    voice audio.yoshi_v_comp7
    yo "C-Calm down, all of you! And Yoichi, let Taiga pick truth or dare!"

    show yoichi pout1 at p8_1
    voice audio.yoichi_v_agree4a2
    yi "Hmph, fine! Truth or dare, Dynamite!"

    show taiga annoyed2 at p8_2
    voice audio.taiga2_v_sarcastic1a
    t "Knowing what you’re gonna dare, truth, duh."

    show yoichi angry1 at p8_1
    voice audio.yoichi_v_denial2a1
    yi "That’s bullshit! Quit being a pussycat!"

    show taiga angry5 at p8_2
    voice audio.taiga_v_denial2b
    t "No way! Just ask a question, you dumb dog!"

    show yoichi annoyed5 at p8_1
    voice audio.yoichi_v_groan1c2
    yi "Ugh, fine! Are you a top or a bottom?"

    show jin2 perv2 at p8_8
    voice audio.jin_v_please3a
    j "P-Please say both…"

    show taiga talking2 at p8_2
    voice audio.taiga_v_response1a
    t "Both. I don’t really care which, either feels good."

    show jin2 fudan2 at p8_8
    voice audio.jin_v_hngh4a
    j "HNNNG I KNEW IT! "

    show yoichi playful1 at p8_1
    voice audio.yoichi_v_response3a
    yi "Pfft, liar. You’re a total bottom."

    show taiga angry2 at p8_2
    voice audio.taiga_v_sarcastic1
    t "Am not! I can top whoever I want, even you!"

    show yoichi angry1 at p8_1
    voice audio.yoichi_v_rush2b2
    yi "Try me! "

    show goro2 disappoint3 at p8_4
    voice audio.goro_v_sigh2a
    g "*sigh* How did we end up in this conversation…?"

    show jin2 daydream4 at p8_8
    voice audio.jin_v_laugh1a
    j "I-It’s literally one of my top ten fantasies…"

    show yuri2 fangirl1 at p8_3
    voice audio.yuri_v_response2a1
    yu "Right?! The fanfics are writing themselves!"

    show lloyd angry2 at p8_6
    voice audio.lloyd_v_rush1a1
    l "Come on! Enough distractions, back to the game you two!"

    show taiga talking2 at p8_2
    voice audio.taiga2_v_surprised1c
    t "Oh right. Then your turn, Lloyd. Truth or dare?"

    show lloyd excited3 at p8_6
    voice audio.lloyd_v_shock1b1
    l "Oh, oh! I wanna pick dare!"

    show darius tease2 at p8_7
    voice audio.darius_v_laugh2a
    d "Someone’s brave."

    show taiga playful2 at p8_2
    voice audio.taiga2_v_laugh2a
    t "Hehe, you sure? You know I was the mean one last term, right?"

    show yoichi angry3 at p8_1
    voice audio.yoichi_v_response1b1
    yi "I was more badass than you!"

    show lloyd bold2 at p8_6
    voice audio.lloyd_v_agree4a1
    l "Bring it on! I bet you can’t make me blush!"

    show taiga playful2 at p8_2
    voice audio.taiga2_v_agree2a
    t "Okay. Make out with Darius."

    show lloyd_blush1 at p8_6
    show lloyd panic1 at p8_6
    l "..!"

    show jin2 fudan3 at p8_8
    show yuri2 drool3 at p8_3
    yuj "*screaming*" with vpunch #jey

    show yoshi panic3 at p8_5
    voice audio.yoshi_v_taiga5
    yo "T-Taiga! Why are you asking these things too?! They don’t have to—"

    show darius tease4 at p8_7
    voice audio.darius_v_encourage1a
    d "I’m down. Lloyd?"

    hide lloyd_blush1
    show lloyd_blush2 at p8_6
    show lloyd pout4 at p8_6
    l "..."

    show lloyd_winter at p8_7
    show lloyd_blush2 at p8_7
    show lloyd blep3 at p8_7
    with move

    l "*smooches Darius*"

    show lloyd_winter at p8_6
    show lloyd_blush2 at p8_6
    show lloyd pout4 at p8_6
    with move

    voice audio.lloyd_v_annoyed1b1
    l "Th-There! That’s all you're getting!"

    show darius bold4 at p8_7
    l "*licks lips*"

    show taiga angry2 at p8_2
    voice audio.taiga2_v_hey1f
    t "Hey! You didn’t even use your tongues!"

    show goro2 play2 at p8_4
    voice audio.goro_v_heh1a
    g "Looks like the alcohol’s certainly doing the trick, huh…?"

    show jin2 dizzy2 at p8_8
    voice audio.jin_v_pant2a
    j "*huff, huff* I-I think I need a toilet break…"

    hide lloyd_blush2
    show lloyd rage3 at p8_6
    voice audio.lloyd_v_disagree1a1
    l "Oh no, you don’t! It’s your turn, Jin!"

    show jin2 shock4 at p8_8
    voice audio.jin_v_wah2a
    j "G-Gah! Why me?!"

    show lloyd disappoint2 at p8_6
    voice audio.lloyd_v_annoyed1b3
    l "Because I’m tired of you getting to just react over there! It’s your turn!"
    l "Truth or dare! Better think carefully!"

    show yuri2 fangirl1 at p8_3
    voice audio.yuri_v_jin1b
    yu "Go with the dare, Jin!! Your heart wants it too!!"

    show jin2 fudan2 at p8_8
    voice audio.jin_v_gulp1a
    j "*gulp* A-Although I’m curious about the dare, I’ll go with truth…"

    show lloyd play3 at p8_6
    voice audio.lloyd_v_laugh1a1
    l "Good choice. If you’d said dare, I’d have had you sitting on Yoshi’s lap!"

    show jin2 fudan3 at p8_8
    voice audio.jin_v_laugh7a
    j "*splutters* WHAAAAAT?!"
    j "I TAKE IT BACK! LET ME OVER THERE!"

    show goro2 angry2 at p8_4
    voice audio.goro_v_no3a1
    g "Off limits! Private property!"
    g "And you already said truth, so no takebacks."

    hide yoshi_autumn
    hide yoshi panic3
    show yoshi2_autumn at p8_5
    show yoshi2 explain2 at p8_5
    voice audio.yoshi_v_ehem1a
    yo "*clears throat* What was your question, Lloyd?"

    show lloyd talk2 at p8_6
    voice audio.lloyd_v_agree3a3
    l "Alright, Jin! Have you ever ACTUALLY been with another guy?! You’re always going on and on about all these fantasies, but you gotta have experienced at least one, right!"

    hide jin2_autumn
    hide jin2_glasses
    hide jin2 fudan3
    show jin_autumn at p8_8
    show jin_glasses at p8_8
    show jin shock2 at p8_8
    voice audio.jin_v_oh4a
    j "O-Oh, well…"

    show jin shy6 at p8_8
    j "..."

    hide yoshi2_autumn
    hide yoshi2 explain2
    show yoshi_autumn at p8_5
    show yoshi awkward4 at p8_5
    voice audio.yoshi_v_ah2
    yo "A-Ah, you don’t have to answer if you don’t want to, Jin!"

    show darius play2 at p8_7
    voice audio.darius_v_naughty1a
    d "Bad boy, Lloyd."

    show lloyd shock3 at p8_6
    voice audio.lloyd_v_question1b1
    l "WHAT?! I didn’t mean it like that! I just wanted to know!"

    show jin awkward4 at p8_8
    voice audio.jin_v_comp1b1
    j "N-No, it’s alright…! It’s a fair question."
    j "B-But the answer is no… I haven’t."

    hide goro2_autumn
    hide goro2 angry2
    show goro_autumn at p8_4
    show goro confused2 at p8_4
    voice audio.goro_v_really1a
    g "Really? I’m a bit surprised, Jin. You’re a really handsome guy, after all."

    show lloyd talk3 at p8_6
    voice audio.lloyd_v_agree2b1
    l "Yeah! Surely you could’ve scored if you wanted to!"

    show jin sigh3 at p8_8
    voice audio.jin_v_conj2c1
    j "W-Well… You guys know I have a lot of social anxiety… And I like to have my fantasies in my games and novels…"
    j "It’s not that I don’t want to, but more of I’m not confident at all…"

    hide yuri2_autumn
    hide yuri2 fangirl1
    show yuri_autumn at p8_3
    show yuri comp2 at p8_3
    voice audio.yuri_v_aww1a
    yu "Aww, Jin! It’s alright, I’m sure you’ll find someone!"

    show yoshi comp2 at p8_5
    voice audio.yoshi_v_yeah2
    yo "Yeah! You’re already getting more confident just being with us here!"

    show jin comp3 at p8_8
    voice audio.jin_v_unsure1b1
    j "I-I guess you guys are right… Maybe there is still hope for me soon."

    show yoichi annoyed4 at p8_1
    voice audio.yoichi_v_well1a
    yi "Well, you lame-o’s know how to ruin the mood!"
    yi "Stutters! I’ve just got the thing for you!"

    show jin confused3 at p8_8
    voice audio.jin_v_what3a
    j "D-Did you just call me Stutters…?"

    show yoichi playful1 at p8_1
    voice audio.yoichi_v_idea1a
    yi "Dynamite here just said he’s a switch, go for him!"

    show taiga panic1 at p8_2
    voice audio.taiga2_v_hey1h
    t "H-Hey! You’re not my pimp!"

    hide jin_autumn
    hide jin_glasses
    hide jin confused3
    show jin2_autumn at p8_8
    show jin2_glasses at p8_8
    show jin2 fudan2 at p8_8
    voice audio.jin_v_hngh1b
    j "Hng...! "

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black with fade
    yo "{i}After Jin settled down, we got back to game, getting drunker with each round.{/i}"
    yo "{i}Eventually, Aiden and Emilia came back with snacks, and we all kept partying for the rest of the evening!{/i}"

    jump day8_goro_aftersq

label day8_goro_aiden:
    $sq_aiden += 1
    show yoshi happy2 at p10_7
    voice audio.yoshi_v_think4
    yo "Oh, how about rock paper scissors? That’s nice and easy!"

    show yuri angry2 at p10_4
    voice audio.yuri_v_what2a
    yu "Whaaaat?! That’s not spicy at all!"

    show emilia disgust3 at p10_3
    voice audio.emilia_v_tsun2a
    e "For once, I agree with her. It’s a little childish don’t you think?"

    show aiden comp5 at p10_5
    voice audio.aiden_v_aww2a
    a "Aww, come on! It sounds fun! "

    show goro talk4 at p10_6
    voice audio.goro_v_alright2a2
    g "It’s alright. The rest of us will play."

    show taiga playful2 at p10_2
    voice audio.taiga_v_insult2a
    t "I’ll totally kick Yoichi’s ass."

    show yoichi angry1 at p10_1
    voice audio.yoichi_v_denial2a1
    yi "Like you could!"

    show yuri irked2 at p10_4
    voice audio.yuri_v_agree5a1
    yu "Ugh, fine! You boys have fun then, I’ll go and get some more snacks in the kitchen! Come help me out, Emilia!"

    show emilia explain2 at p10_3
    voice audio.emilia_v_response1a
    e "Fine, I’d rather do that anyway."

    hide emilia_winter3
    hide emilia explain2
    hide yuri_autumn
    hide yuri irked2
    with dissolve

    show yoichi_autumn at p8_1
    show yoichi normal1 at p8_1
    show taiga_autumn at p8_2
    show taiga normal1 at p8_2
    show aiden_autumn at p8_3
    show aiden play2 at p8_3
    show goro_autumn at p8_4
    show goro norm1 at p8_4
    show yoshi_autumn at p8_5
    show yoshi norm1 at p8_5
    show lloyd_winter at p8_6
    show lloyd norm1 at p8_6
    show darius_winter at p8_7
    show darius norm1 at p8_7
    show jin2_autumn at p8_8
    show jin2_glasses at p8_8
    show jin2 perv1 at p8_8
    with move

    voice audio.aiden_v_alright1a1
    a "Alriiight! Now that they’re gone, we can make this way more ‘interesting.’"

    hide yoshi_autumn
    hide yoshi norm1
    show yoshi2_autumn at p8_5
    show yoshi2 sigh4 at p8_5
    voice audio.yoshi_v_sigh3a
    yo "*sigh* I already know where this is going. You’re going to say we could make it into—"

    hide yoshi2_autumn
    hide yoshi2 sigh4
    show yoshi_autumn at p8_5
    show yoshi annoy3 at p8_5
    show aiden bold2 at p8_3
    yoa "A strip show!"

    show aiden shock3 at p8_3
    voice audio.aiden_v_shock1a2
    a "Whoa! How’d you know, Yoshi?!"

    show darius bored5 at p8_7
    voice audio.darius_v_aiden2
    d "You’re predictable, Aiden."

    show taiga angry4 at p8_2
    voice audio.taiga_v_what8
    t "What?! Why would I wanna do that? Count me out!"

    show yoichi playful1 at p8_1
    voice audio.yoichi_v_agree3c1
    yi "Heh, thought you said you were gonna kick my ass. "
    yi "Guess you realized you never could."

    show taiga angry5 at p8_2
    voice audio.taiga_v_agree3b
    t "Tch. Fine! You’ll be bare-ass naked in the snow by the end of the game!"

    show lloyd disappoint2 at p8_6
    voice audio.lloyd_v_denial1a2
    l "Count Dar and I out! We aren’t stripping when it’s this cold out!"

    show darius happy1 at p8_7
    voice audio.darius_v_comp3a
    d "We’ll just watch."

    show aiden laugh1 at p8_3
    voice audio.aiden_v_alright2a
    a "Haha, okay, okay, fair enough! You two can have a pass this time."

    show jin2 perv5 at p8_8
    voice audio.jin_v_laugh3c
    j "I-I think I’ll just be the observer too…"

    show aiden play3 at p8_3
    voice audio.aiden_v_no1a1
    a "Oh, no you don’t Jin! You’re in too, and we’re gonna see that twink bod of yours again!"

    show jin2 shock2 at p8_8
    voice audio.jin_v_hngh1a
    j "Hngh!"

    show aiden bold2 at p8_3
    voice audio.aiden_v_okay1a
    a "The rules are simple! Three rounds per person, each round you lose, you strip a piece of clothing! If you’re naked, you’re out!"
    a "First round, Yoshi and me! Let’s go!"

    hide yoshi_autumn
    hide yoshi annoy3
    show yoshi2_autumn at p8_5
    show yoshi2 awkward4 at p8_5
    voice audio.yoshi_v_aiden5
    yo "A-Aiden, I’m not sure if—"

    hide goro_autumn
    hide goro norm1
    show goro2_autumn at p8_4
    show goro2 annoy1 at p8_4
    show aiden tease1 at p8_3
    voice audio.aiden_v_rush1b1
    a "Come on, Yoshi! Don’t be a party pooper, or I’ll strip you myself!"

    hide yoshi2_autumn
    hide yoshi2 awkward4
    show yoshi_autumn at p8_5
    show yoshi irked3 at p8_5
    voice audio.yoshi_v_agree2b1
    yo "F-Fine! Let’s just go!"

    show yoshi_autumn at p8_4
    show yoshi irked3 at p8_4
    show goro2_autumn at p8_5
    show goro2 annoy1 at p8_5
    with move

    show aiden bold2 at p8_3
    voice audio.aiden_v_alright1a1
    a "Alright! Rock, paper, scissors… Shoot!"

    show yoshi talk1 at p8_4
    voice audio.yoshi_v_okay2
    yo "Rock!"

    show aiden laugh2 at p8_3
    voice audio.aiden_v_laugh1d1
    a "And that’s scissors for me! Seeya, shirt!"

    hide aiden_autumn
    hide aiden laugh2
    show aiden_shirtless at p8_3
    show aiden play2 at p8_3
    with dissolve

    voice audio.aiden_v_here1a
    a "Here Jin, catch!"
    a "*tosses shirt at Jin*"

    show jin2 perv6 at p8_8
    voice audio.jin_v_fudan4a1
    j "*sniff* So manly… "

    show aiden bold2 at p8_3
    voice audio.aiden_v_alright1a1
    a "Alright! Round two… Rock, paper, scissors… Shoot!"

    show yoshi talk2 at p8_4
    voice audio.yoshi_v_okay2
    yo "Paper!"

    show aiden excited3 at p8_3
    voice audio.aiden_v_oops3a
    a "Sci—I mean rock!"

    hide yoshi_autumn
    hide yoshi talk2
    show yoshi2_autumn at p8_4
    show yoshi2 confused2 at p8_4
    voice audio.yoshi_v_huh3c
    yo "H-Huh? But didn’t you—"

    show aiden laugh2 at p8_3
    voice audio.aiden_v_oops2b
    a "Looks like I lose again! Here goes the pants!"

    hide aiden_shirtless
    hide aiden laugh2
    show aiden_undie at p8_3
    show aiden play1 at p8_3
    with dissolve

    show jin2 fudan3 at p8_8
    voice audio.jin_v_laugh7a
    j "*splutters* FULL MOON!"

    show goro2 disappoint3 at p8_5
    voice audio.goro_v_hmph1a
    g "At least he’s wearing underwear…"

    show taiga talking4 at p8_2
    voice audio.taiga_v_aiden7
    t "Nice jockstrap, Aiden. "

    show aiden play2 at p8_3
    voice audio.aiden_v_laugh1d1
    a "Looks like I’m only a tiny piece away from baring it all~ You got what it takes, Yoshi?"

    show yoshi2 think2 at p8_4
    voice audio.yoshi_v_but3
    yo "B-But it seems like you’re just losing on purpose…"

    show aiden tease1 at p8_3
    voice audio.aiden_v_oho1a
    a "No way! I would never~ Or would I?"

    show aiden_undie at p8_1
    show aiden shock1 at p8_1
    show yoichi_autumn at p8_3
    show yoichi angry1 at p8_3
    with move

    voice audio.yoichi_v_annoyed2b1
    yi "I’ve had enough of your talking! It’s mine and Dynamite’s turn!"

    show taiga confused1 at p8_2
    voice audio.taiga2_v_confused1a
    t "Huh? But they only have one round left!"

    show aiden laugh1 at p8_1
    voice audio.aiden_v_alright3d
    a "Haha, it’s alright~ I’ll let you two take the spotlight for a minute! "
    a "Besides, the less clothes in the room, the better~"

    show yoichi talking2 at p8_3
    voice audio.yoichi_v_rush1a1
    yi "Somebody, count us off!"

    hide yoshi2_autumn
    hide yoshi2 think2
    show yoshi_autumn at p8_4
    show yoshi awkward3 at p8_4
    voice audio.yoshi_v_alright3
    yo "A-Alright… Rock, paper, scissors… shoot!"

    show yoichi excited1 at p8_3
    voice audio.yoichi_v_agree1d3
    yi "Rock! "

    show taiga angry5 at p8_2
    voice audio.taiga_v_pain1
    t "Dammit… Scissors."

    show yoichi laugh1 at p8_3
    voice audio.yoichi_v_laugh1c1
    yi "Hah! Get your shirt off, Dynamite!"

    show taiga angry6 at p8_2
    voice audio.taiga_v_annoyed4a
    t "Tch, fine."

    hide taiga_autumn
    hide taiga angry6
    show taiga_winter2 at p8_2
    show taiga angry1 at p8_2
    with dissolve

    show jin2 perv5 at p8_8
    voice audio.jin_v_please2a
    j "Toss your shirt over here too…?"

    show aiden excited1 at p8_1
    voice audio.aiden_v_amazed1b1
    a "Yeah, way to go, dude! You’re a lean, mean, twinky machine!"

    show taiga annoyed2 at p8_2
    voice audio.taiga_v_disagree2
    t "S-Shut up. Just count us off again, so I can beat this dumbass!"

    show yoichi angry1 at p8_3
    voice audio.yoichi_v_denial2a3
    yi "Like hell you will!"

    show yoshi talk1 at p8_4
    show aiden excited3 at p8_1
    hide goro2_autumn
    hide goro2 disappoint3
    show goro_autumn at p8_5
    show goro talk1 at p8_5
    hide lloyd_winter
    hide lloyd disappoint2
    show lloyd_winter at p8_6
    show lloyd talk2 at p8_6
    show darius talk2 at p8_7
    all "Rock, paper, scissors… shoot!"

    show yoichi talking2 at p8_3
    voice audio.yoichi_v_agree1d2
    yi "Paper!"

    show taiga playful1 at p8_2
    voice audio.taiga2_v_boastful1a
    t "Scissors! Hah! Got you!"

    show yoichi rage2 at p8_3
    voice audio.yoichi_v_swear2a1
    yi "FUCK! "

    hide yoichi_autumn
    hide yoichi rage2
    show yoichi_winter2 at p8_3
    show yoichi angry4 at p8_3
    with dissolve

    show jin2 dizzy2 at p8_8
    voice audio.jin_v_fudan1a1
    j "M-Mini-bara… "

    show yoichi angry1 at p8_3
    voice audio.yoichi_v_rush2c1
    yi "Last round! Loser bares all!"

    show taiga playful2 at p8_2
    voice audio.taiga_v_rush2a
    t "You’re on! "

    show jin2 dizzy3 at p8_8
    voice audio.jin_v_really2b
    j "C-Could this really be happening?!"

    show yoshi confused3 at p8_4
    voice audio.yoshi_v_uh1a
    yo "Uhh… okay… Rock, paper, scissors… Shoot?"

    show taiga talking2 at p8_2
    show yoichi angry1 at p8_3
    yt "Pape—"

    show taiga_winter2 at p8_1
    show taiga surprised1 at p8_1
    show yoichi_winter2 at p8_2
    show yoichi shock1 at p8_2
    show aiden_undie at p8_3
    show aiden laugh3 at p8_3
    with move

    voice audio.aiden_v_laugh2c1
    a "Rock! Oh no, looks like I lose! "

    show yoshi angry2 at p8_4
    voice audio.yoshi_v_aiden6
    yo "A-Aiden! You weren’t even playing!"

    hide goro_autumn
    hide goro talk1
    show goro2_autumn at p8_5
    show goro2 annoy3 at p8_5
    voice audio.goro_v_shy1a
    g "He’s just looking for an excuse to get naked."

    show aiden tease1 at p8_3
    voice audio.aiden_v_unsure5b1
    a "Maybe so, but Jin won’t mind, will you~?"

    show jin2 fudan3 at p8_8
    voice audio.jin_v_yes6c
    j "Hng! YES! PLEASE DO!"

    show lloyd confused3 at p8_6
    voice audio.lloyd_v_confused1a2
    l "Why are we acting like we don’t see Aiden naked all the time…? "

    show darius play2 at p8_7
    voice audio.darius_v_laugh1
    d "Freshly baked buns every day."

    show aiden wink3 at p8_3
    voice audio.aiden_v_well1a3
    a "Weeell… Maybe if you play one more round… with me!"
    a "Only if I win, you bare it all instead!"

    show jin2 shock2 at p8_8
    voice audio.jin_v_what4a
    j "Wh-What!?"

    show aiden bold2 at p8_3
    voice audio.aiden_v_perv1
    a "You heard me! You want the prize, you gotta risk it all!"

    show jin2 fudan1 at p8_8
    j "..."

    show jin2 fudan2 at p8_8
    voice audio.jin_v_yes5a
    j "I’ll do it. "

    show jin2_autumn at p8_4
    show jin2_glasses at p8_4
    show jin2 fudan1 at p8_4
    show yoshi_autumn at p8_5
    show yoshi awkward1 at p8_5
    show goro2_autumn at p8_6
    show goro2 annoy1 at p8_6
    show lloyd_winter at p8_7
    show lloyd confused1 at p8_7
    show darius_winter at p8_8
    show darius play1 at p8_8
    with move

    show aiden excited1 at p8_3
    voice audio.aiden_v_alright1a1
    a "Alright! Count us off then, Yoshi!"

    hide yoshi_autumn
    hide yoshi awkward1
    show yoshi2_autumn at p8_5
    show yoshi2 sigh4 at p8_5
    voice audio.yoshi_v_sigh3a
    yo "*sigh* This has totally gone off the rails…"

    hide yoshi2_autumn
    hide yoshi2 sigh4
    show yoshi_autumn at p8_5
    show yoshi talk1 at p8_5
    show goro2 talk2 at p8_6
    show lloyd talk1 at p8_7
    show darius talk2 at p8_8
    show taiga talking4 at p8_1
    show yoichi talking2 at p8_2
    all "Rock… Paper… Scissors…"

    show jin2 dizzy5 at p8_4
    voice audio.jin_v_please1b
    j "Please by the divine grace let me win…"

    show yoshi talk2 at p8_5
    show goro2 talk1 at p8_6
    show lloyd talk2 at p8_7
    show darius talk1 at p8_8
    show taiga talking5 at p8_1
    show yoichi angry1 at p8_2
    all "…Shoot!"

    show jin2 fudan3 at p8_4
    voice audio.jin_v_hngh1b
    j "S-Scissors!"

    show aiden laugh3 at p8_3
    voice audio.aiden_v_laugh1d1
    a "And mine’s rock! Looks like I win~"

    show jin2 comic1 at p8_4
    voice audio.jin_v_what4a
    j "NOOOOO! What cruel fate is this?!"

    show aiden play2 at p8_3
    voice audio.aiden_v_oho1a
    a "Time to collect my reward~"

    show jin2 shock1 at p8_4
    j "...!"

    show aiden_undie at p8_4
    show aiden play1 at p8_4
    with move

    hide jin2_autumn
    hide jin2_glasses
    hide jin2 shock1
    show jin2_undie at p8_4
    show jin2_glasses at p8_4
    show jin2 shock1 at p8_4
    with dissolve

    show aiden_undie at p8_3
    show aiden play1 at p8_3
    with move

    voice audio.aiden_v_excited2a
    a "There! That’s more like it!"

    show jin2 fudan3 at p8_4
    voice audio.jin_v_shock2c
    j "GAHHH! I’M EXPOSED!"

    show aiden play3 at p8_3
    voice audio.aiden_v_amazed3a
    a "Hey, not bad, Jin! You may not have a lot of muscle, but that slender frame is good to look at~"

    show yoichi playful1 at p8_2
    voice audio.yoichi_v_unsure1a1
    yi "Should I call him Slenderman now?"

    show jin2 sigh6 at p8_4
    voice audio.jin_v_worry1c1
    j "Huhuhu… To think I was the one stripped…"

    show goro2 sigh4 at p8_6
    voice audio.goro_v_sigh2a
    g "*sigh* This got out of hand way too quickly…"

    show aiden laugh1 at p8_3
    voice audio.aiden_v_laugh2b1
    a "Hahaha! Come on, Gramps! Nothing wrong with a bunch of dudes stripping down together! Speaking of…"
    a "*grabs his underwear*"

    show taiga_winter2 at p10_3
    show taiga surprised1 at p10_3
    show yoichi_winter2 at p10_4
    show yoichi shock1 at p10_4
    show aiden_undie at p10_5
    show aiden play1 at p10_5
    show jin2_undie at p10_6
    show jin2_glasses at p10_6
    show jin2 shock1 at p10_6
    show yoshi_autumn at p10_7
    show yoshi shock1 at p10_7
    show goro2_autumn at p10_8
    show goro2 shock1 at p10_8
    show lloyd_winter at p10_9
    show lloyd shock1 at p10_9
    show darius_winter at p10_10
    show darius shock1 at p10_10
    with move

    show emilia_winter3 at p10_1
    show emilia disgust1 at p10_1
    show yuri2_autumn at p10_2
    show yuri2 fangirl2 at p10_2
    with dissolve

    voice audio.yuri_v_kyaa1a
    yu "KYAAAA! WHAT HAPPENED HERE?!"

    show emilia eyeroll6 at p10_1
    voice audio.emilia_v_ugh1
    e "Eugh. Why am I not surprised?"

    show yuri2 fangirl4 at p10_2
    voice audio.yuri_v_fujo4a
    yu "AIDEN, JIN, TAIGA AND YOICHI ALL NEAR-NAKED?! WHAT IS THIS SCENE UNFOLDING IN FRONT OF ME?!"

    show yoshi panic3 at p10_7
    voice audio.yoshi_v_shock3
    yo "Gah! Yuri it’s not what it looks like!"

    show taiga sigh1 at p10_3
    voice audio.taiga2_v_disagree1a
    t "No, it pretty much is exactly what it looks like."

    show aiden excited1 at p10_5
    voice audio.aiden_v_oh1b
    a "Oh, just in time Yuri. Jin and I were about to lose the undies!"

    show jin2 fudan3 at p10_6
    voice audio.jin_v_what4a
    j "WHAT?!"

    show yuri2 fangirl3 at p10_2
    voice audio.yuri_v_agree1c1
    yu "YES! LET ME GRAB MY CAMERA!"

    hide goro2_autumn
    hide goro2 shock1
    show goro_autumn at p10_8
    show goro comic2 at p10_8
    voice audio.goro_v_annoyed3b1
    g "Y-Yuri! Stop that!"

    hide yoshi_autumn
    hide yoshi panic3
    show yoshi2_autumn at p10_7
    show yoshi2 sigh1 at p10_7
    voice audio.yoshi_v_sigh3a
    yo "*sigh*"

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black with fade
    yo "{i}We shut down the game before it got too out of hand and switched to something else.{/i}"
    yo "{i}We kept drinking and partying for the rest of the evening!{/i}"

    jump day8_goro_aftersq

label day8_goro_yuri:
    $sq_yuri += 1
    show yoshi happy2 at p10_7
    voice audio.yoshi_v_think4
    yo "Oh, how about we play picture charades? "

    hide goro_autumn
    hide goro happy2
    show goro2_autumn at p10_6
    show goro2 play3 at p10_6
    voice audio.goro_v_laugh1b2
    g "Hehe, I think you’ll enjoy this one, dear."

    hide jin2_autumn
    hide jin2_glasses
    hide jin2 fudan3
    show jin_autumn at p10_10
    show jin_glasses at p10_10
    show jin norm1 at p10_10
    show yuri excited2 at p10_4
    voice audio.yuri_v_oh1c
    yu "Oooh, artsy! Yes, that’s my thing~!"

    show emilia happy2 at p10_3
    voice audio.emilia_v_conj1a
    e "Actually, I don’t mind either. I did take a few painting classes growing up~"

    show taiga talking5 at p10_2
    voice audio.taiga2_v_agree2b
    t "I’ll join, it sounds fun."

    show yoichi angry3 at p10_1
    voice audio.yoichi_v_disagree1a1
    yi "Count me out! Arts and crafts are for nerds!"
    yi "I’m going to get more snacks!"

    hide yoichi_autumn
    hide yoichi angry3
    with dissolve

    show taiga annoyed2 at p10_2
    voice audio.taiga_v_ugh1
    t "Ugh, what a turd."

    hide aiden_autumn
    hide aiden bold5
    show aiden2_autumn at p10_5
    show aiden2 comp3 at p10_5
    hide yuri_autumn
    hide yuri excited2
    show yuri_autumn at p10_4
    show yuri excited2 at p10_4
    voice audio.aiden_v_laugh1a2
    a "Ahehehe, I’d better go after him, otherwise he might destroy the kitchen. Plus, it looks like we need some more food anyway."

    show lloyd talk3 at p10_8
    voice audio.lloyd_v_shock1a1
    l "Oh, Dar and I will come help you, Aiden! Drawing pretty much reminds us of work!"

    show darius tease2 at p10_9
    voice audio.darius_v_conj1a2
    d "Lloyd’s actually bad at drawing."

    show lloyd angry2 at p10_8
    voice audio.lloyd_v_darius8b
    l "D-Dar! You’re damaging my reputation as an architect!"

    hide aiden2_autumn
    hide aiden2 comp3
    show aiden_autumn at p10_5
    show aiden happy1 at p10_5
    voice audio.aiden_v_rush1a1
    a "Haha, alright! Let’s go, you two! The rest of you, have fun!"

    hide aiden_autumn
    hide aiden happy1
    hide lloyd_winter
    hide lloyd angry2
    hide darius_winter
    hide darius tease2
    with dissolve

    show taiga_autumn at p6_1
    show taiga normal1 at p6_1
    show emilia_winter3 at p6_2
    show emilia norm1 at p6_2
    show yuri_autumn at p6_3
    show yuri happy3 at p6_3
    show goro2_autumn at p6_4
    show goro2 norm1 at p6_4
    show yoshi_autumn at p6_5
    show yoshi norm1 at p6_5
    show jin_autumn at p6_6
    show jin_glasses at p6_6
    show jin norm1 at p6_6
    with move

    voice audio.yuri_v_alright1a1
    yu "Alright! Let’s split into pairs! Emilia and I will be one!"

    show emilia explain5 at p6_2
    voice audio.emilia_v_response2a
    e "Oh, very well, but don’t drag me down!"

    show goro2 happy2 at p6_4
    voice audio.goro_v_alright1a1
    g "Yoshinori and I are a pair."

    show yoshi comp2 at p6_5
    voice audio.yoshi_v_yeah2
    yo "Y-Yeah!"

    show emilia_winter3 at p6_1
    show emilia norm1 at p6_1
    show yuri_autumn at p6_2
    show yuri happy3 at p6_2
    show goro2_autumn at p6_3
    show goro2 norm1 at p6_3
    show yoshi_autumn at p6_4
    show yoshi norm1 at p6_4
    show taiga_autumn at p6_5
    show taiga talking1 at p6_5
    show jin_autumn at p6_6
    show jin_glasses at p6_6
    show jin norm1 at p6_6
    with move

    voice audio.taiga2_v_thinking2a
    t "Guess that leaves me and Jin."

    hide jin_autumn
    hide jin_glasses
    hide jin norm1
    show jin2_autumn at p6_6
    show jin2_glasses at p6_6
    show jin2 daydream2 at p6_6
    voice audio.jin_v_taiga4a
    j "F-Feel free to have your way with me, Taiga…"

    show yoshi happy1 at p6_4
    voice audio.yoshi_v_so1a
    yo "So, who wants to go first?"

    hide goro2_autumn
    hide goro2 norm1
    show goro_autumn at p6_3
    show goro bold2 at p6_3
    voice audio.goro_v_confident1a
    g "We can start, Yoshinori. I’ll draw."

    hide yoshi_autumn
    hide yoshi happy1
    show yoshi2_autumn at p6_4
    show yoshi2 comp3 at p6_4
    voice audio.yoshi_v_really5
    yo "R-Really? "

    hide goro_autumn
    hide goro bold2
    show goro2_autumn at p6_3
    show goro2 bold5 at p6_3
    voice audio.goro_v_agree3a1
    g "Of course. Where did you think Yuri’s artistic skills came from?"
    g "Now how does this work?"

    hide yoshi2_autumn
    hide yoshi2 comp3
    show yoshi_autumn at p6_4
    show yoshi happy2 at p6_4
    voice audio.yoshi_v_oh2
    yo "Oh, you just pick a card and try and draw what’s on it! "
    yo "After you’re done, I’ll guess and see if I can get it right!"

    hide goro2_autumn
    hide goro2 bold5
    show goro_autumn at p6_3
    show goro happy3 at p6_3
    voice audio.goro_v_think2b1
    g "Sure, simple enough. Let’s see."

    hide goro_autumn
    hide goro happy3
    show goro2_autumn at p6_3
    show goro2 confused4 at p6_3
    g "..."

    hide goro2_autumn
    hide goro2 confused4
    show goro_autumn at p6_3
    show goro bold2 at p6_3
    voice audio.goro_v_alright1a1
    g "Alright. Here we go…"

    hide goro_autumn
    hide goro bold2
    show goro2_autumn at p6_3
    show goro2 think4 at p6_3
    g "*scribbling*"

    hide goro2_autumn
    hide goro2 think4
    show goro_autumn at p6_3
    show goro happy2 at p6_3
    voice audio.goro_v_here1a
    g "Alright. Here you go, Yoshinori."

    show cg_fade at truecenter
    show fxsq_yuri 1 at fx_pos
    with dissolve

    voice audio.yoshi_v_oh3
    yo "O-Oh…"

    voice audio.jin_v_laugh7a
    j "P-Pfft…"

    voice audio.yuri_v_aww1b
    yu "Aww, Dad…"

    voice audio.emilia_v_surprised1b1
    e "That is honestly disturbing."

    voice audio.taiga2_v_laugh1a
    t "Right? I guess that’s not one of his talents."

    voice audio.goro_v_ehem1a
    g "EHEM, let Yoshinori think, all of you! Your comments aren’t necessary!"

    voice audio.yoshi_v_uh1a
    yo "Umm…"

    voice audio.goro_v_yoshi6
    g "Alright, Yoshinori. What is it?"

    voice audio.yoshi_v_think1a
    yo "I-Is it a… cat?"

    voice audio.goro_v_rush2b1
    g "No, come on. You can do it, Yoshinori."

    voice audio.yoshi_v_unsure1b
    yo "M-Maybe a tiger…?"

    voice audio.goro_v_no1a1
    g "You’re getting warmer…"

    voice audio.taiga_v_laugh1a
    t "HAHAHA! There’s no way he’d get it!"

    voice audio.yoshi_v_huh1
    yo "I-I don’t know, are those legs or arms? And why are there an uneven number of fingers??"

    voice audio.yuri_v_sorry1a1
    yu "Time’s up!"

    hide cg_fade
    hide fxsq_yuri 1
    with dissolve

    show goro comic2 at p6_3
    voice audio.goro_v_angry1b1
    g "Grah, it was a bear! "

    hide yoshi_autumn
    hide yoshi happy2
    show yoshi2_autumn at p6_4
    show yoshi2 confused3 at p6_4
    voice audio.yoshi_v_oh3
    yo "O-Oh… I had no idea…"

    show jin2 perv2 at p6_6
    voice audio.jin_v_daddy1a
    j "You should have just drawn yourself, sir…"

    show yuri play2 at p6_2
    voice audio.yuri_v_laugh1b1
    yu "Hihi, Dad’s never been a great artist~"

    hide goro_autumn
    hide goro comic2
    show goro2_autumn at p6_3
    show goro2 annoy2 at p6_3
    voice audio.goro_v_annoyed1a1
    g "Tch. Fine, then you all show me what you can do!"

    show taiga talking4 at p6_5
    voice audio.taiga2_v_agree1a
    t "Alright! I’ll go next!"

    show taiga confused2 at p6_5
    t "..."

    show taiga laugh1 at p6_5
    voice audio.taiga2_v_boastful1a
    t "Ha! This is super easy – no way Jin can mess this up!"

    show taiga confident3 at p6_5
    t "*scribbling*"

    show taiga excited1 at p6_5
    voice audio.taiga2_v_agree1b
    t "Alright! It’s done – check it out!"

    show cg_fade at truecenter
    show fxsq_yuri 2 at fx_pos with dissolve

    voice audio.jin_v_oh2a
    j "A dildo!"

    voice audio.taiga_v_wtf3
    t "What the fuck?!"

    voice audio.yuri_v_laugh3a1
    yu "Pffttttt!"

    voice audio.emilia_v_disgust1
    e "How scandalous. To think cards like that are in the deck."

    voice audio.taiga2_v_denial1a
    t "N-No, it’s not! "

    voice audio.jin_v_think2a1
    j "Is it a monster cock?"

    voice audio.taiga2_v_rush1a
    t "It’s a vegetable!"

    voice audio.jin_v_wait3a
    j "Wait… Is this your penis? I didn’t know you had limp dick…"

    voice audio.taiga_v_whatthe1b
    t "What the hell?! Why do you keep making it about penises…?! Think of something else!"

    voice audio.jin_v_oh2b
    j "Ooh! A bad dragon! A big bad dragon!"

    voice audio.taiga_v_rage3
    t "Holy shit, Jin, you’re hopeless!"

    voice audio.yuri_v_taiga2b
    yu "Taiga! Give him a hint he can understand maybe?"

    voice audio.taiga_v_insult4a
    t "What else is there to guess?! It looks like literally what it is!"

    voice audio.yuri_v_unsure1c1
    yu "Oh, I dunno, maybe like… a famous pop-culture scientist turned into this one episode!"

    voice audio.jin_v_conj2c1
    j "I-I’m a programmer…"

    voice audio.taiga_v_insult3a
    t "It’s a pickle, for fuck’s sake!"

    hide cg_fade
    hide fxsq_yuri 2
    with dissolve

    show taiga angry1 at p6_5
    show goro2 tease2 at p6_3
    voice audio.goro_v_heh1a
    g "Heh. Suddenly my drawing doesn’t look so bad."

    hide jin2_autumn
    hide jin2_glasses
    hide jin2 perv2
    show jin_autumn at p6_6
    show jin_glasses at p6_6
    show jin awkward5 at p6_6
    voice audio.jin_v_wah1b
    j "W-Wah… I still don’t see it…"

    show yoshi2 confused2 at p6_4
    voice audio.yoshi_v_conj4a
    yo "T-To be fair, even I thought it was inappropriate…"

    show taiga angry5 at p6_5
    voice audio.taiga_v_annoyed3c
    t "Whatever! You do it then, Yuri!"

    show yuri bold4 at p6_2
    voice audio.yuri_v_laugh1b1
    yu "Hihi, don’t mind if I do! I’ll show you all how it’s done~"

    show emilia annoy2 at p6_1
    voice audio.emilia_v_ugh1
    e "Just nothing lewd, please? I’d really rather not deal with that."

    show yuri confused3 at p6_2
    voice audio.yuri_v_isee1a
    yu "Let’s see…"

    show yuri think1 at p6_2
    yu "..."

    show yuri excited2 at p6_2
    voice audio.yuri_v_oh1a
    yu "Oh! This is perfect! You and I are winning for sure, Emilia!"

    show emilia bold5 at p6_1
    voice audio.emilia_v_sarcastic1
    e "Obviously."

    show yuri bold1 at p6_2
    yu "*scribbling*"

    show yuri bold2 at p6_2
    voice audio.yuri_v_here1a
    yu "Here! "

    show cg_fade at truecenter
    show fxsq_yuri 3 at fx_pos with dissolve

    voice audio.yoshi_v_shock1b
    yo "Whoa! That’s incredibly detailed for what it is, Yuri!"

    voice audio.goro_v_amazed1a1
    g "I’m impressed, dear."

    voice audio.taiga_v_annoyed2a
    t "Tch. Damn, she has me beat."

    voice audio.jin_v_yuri4a
    j "I didn’t know you were so talented, Yuri…"

    voice audio.yuri_v_laugh1b1
    yu "Hihi~ Thank you! Emilia’s lucky, ’cause this is a giveaway!"

    voice audio.emilia_v_question4b
    e "I-I don’t get it… What are you all seeing?!"
    e "I have no idea what that is!"

    voice audio.yuri_v_what5a
    yu "WHAT?! It’s so easy though!"

    voice audio.yoshi_v_emilia6
    yo "I-It is pretty obvious, Emilia… Just take a guess!"

    voice audio.emilia_v_disagree3b
    e "You’re all messing with me! She just drew something random, didn’t she?"

    voice audio.goro_v_no1a1
    g "No, it’s very real. And well-drawn too."

    voice audio.yuri_v_emilia8a
    yu "EMILIA! Don’t you mess this up!"

    voice audio.emilia_v_request2a
    e "Be quiet you! I’m thinking...!"
    e "..."

    voice audio.emilia_v_sad1
    e "I…"
    e "…have no idea."

    voice audio.yuri_v_angry3b
    yu "GRAHHH! ARE YOU SERIOUS?! IT’S  A TOILET PLUNGER!"

    hide cg_fade
    hide fxsq_yuri 3
    with dissolve

    show emilia angry3 at p6_1
    voice audio.emilia_v_question1c
    e "Wh-Why would I have known that?! I’ve never even heard of it before!"

    show yoshi2 comp6 at p6_4
    voice audio.yoshi_v_laugh6
    yo "Ahehe, I guess Emilia DID have quite the different upbringing from us…"

    show goro2 tease5 at p6_3
    voice audio.goro_v_laugh1b2
    g "Better luck next time, dear."

    show yuri rage1 at p6_2
    voice audio.yuri_v_angry3a
    yu "Grrrrr…! No way am I accepting this! We’re doing another round!"
    yu "And Emilia, you better get it this time, or else!"

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black with fade
    yo "{i}We played a few more rounds, while continuing to drink and have fun.{/i}"
    yo "{i}Surprisingly, none of us could guess anyone’s drawing, making Yuri more and more frustrated.{/i}"
    yo "{i}Eventually, Aiden and the others came back with snacks, and we all kept partying for the rest of the evening!{/i}"

    jump day8_goro_aftersq

label day8_goro_aftersq:
    scene cg black
    $quick_menu = False
    hide screen location
    hide screen timeline
    hide screen quick_menu
    with fade
    $ time_transition_sunset_to_night_winter2()
    $ renpy.pause (2.0, hard=True)

    $ location = location_gororoom
    $ time = timeline_timenight
    $quick_menu = True
    show screen location
    show screen timeline
    show screen quick_menu
    scene bg_gororoom_winter_night with fade
    play music old_familiar_home loop

    play sound sfx_dooropen
    show yoshi_autumn at p5_4
    show yoshi_blush1 at p5_4
    show yoshi drunk5 at p5_4
    show goro_autumn at p5_5
    show goro norm1 at p5_5
    voice audio.yoshi_v_laugh5a
    yo "*hic*"

    show goro talk1 at p5_5
    voice audio.goro_v_wait3a1
    g "We’re almost to the bed, Yoshinori."

    show yoshi_autumn at left2
    show yoshi_blush1 at left2
    show yoshi drunk1 at left2
    show goro_autumn at right2
    show goro relief2 at right2
    with move

    voice audio.goro_v_here1a
    g "There you go."

    hide yoshi_autumn
    hide yoshi_blush1
    hide yoshi drunk1
    show yoshi2_autumn at left2
    show yoshi2_blush1 at left2
    show yoshi2 tired3 at left2
    voice audio.yoshi_v_ah6
    yo "Ahh… Crap… I had too much to drink… again."

    hide goro_autumn
    hide goro relief2
    show goro2_autumn at right2
    show goro2 play3 at right2
    voice audio.goro_v_rush2c1
    g "Come on, Yoshinori. it wasn’t even that much…"

    show yoshi2 upset5 at left2
    voice audio.yoshi_v_groan1a
    yo "Hngh… My first night in your room and I’m like this…"

    show goro2 tease5 at right2
    voice audio.goro_v_heh1a
    g "Heh… Even when you’re drunk, you’re still worried about that…?"

    show yoshi2 worry5 at left2
    voice audio.yoshi_v_sorry2a
    yo "I can’t help it… I don’t wanna make a mess…"

    hide goro2_autumn
    hide goro2 tease5
    show goro_autumn at right2
    show goro play2 at right2
    voice audio.goro_v_rush1d1
    g "Let’s get you comfortable, then."

    show goro_autumn at center
    show goro play1 at center
    with move

    hide yoshi2_autumn
    hide yoshi2_blush1
    hide yoshi2 worry5
    show yoshi_autumn at left2
    show yoshi_blush1 at left2
    show yoshi panic3 at left2
    voice audio.yoshi_v_shock4
    yo "W-Wah...! What are you doing…?"

    hide yoshi_autumn
    hide yoshi_blush1
    hide yoshi panic3
    show yoshi2_undie2 at left2
    show yoshi2_blush1 at left2
    show yoshi2 panic1 at left2
    with dissolve

    show goro_autumn at right2
    show goro play3 at right2
    with move

    voice audio.goro_v_laugh1b2
    g "Getting you settled in. "

    show yoshi2 angry5 at left2
    voice audio.yoshi_v_groan1a
    yo "Nnn… I could’ve taken my clothes off myself, you know."

    hide goro_autumn
    hide goro play3
    show goro2_autumn at right2
    show goro2 tease3 at right2
    voice audio.goro_v_yeah1d1
    g "Oh yeah? You could barely walk on the way back here."

    show yoshi2 sigh4 at left2
    voice audio.yoshi_v_sigh3a
    yo "*sigh* This is so embarrassing…"

    hide goro2_autumn
    hide goro2 tease3
    show goro_autumn at right2
    show goro relief2 at right2
    voice audio.goro_v_glad1a
    g "Good thing I lit the fireplace before we went to that party. You should be pretty cozy in here."

    hide yoshi2_undie2
    hide yoshi2_blush1
    hide yoshi2 sigh4
    show yoshi_undie2 at left2
    show yoshi_blush1 at left2
    show yoshi drunk6 at left2
    voice audio.yoshi_v_yeah4
    yo "Y-Yeah… It’s nice and snug…"

    show goro happy2 at right2
    voice audio.goro_v_well1a
    g "Well, I’m going to take a shower before bed. Want me to wash you up, too?"

    show yoshi awkward4 at left2
    voice audio.yoshi_v_ah2
    yo "A-Ah…! You don’t have to…! I’ll shower first thing in the morning…"

    show goro talk3 at right2
    voice audio.goro_v_alright1a1
    g "Alright then. Just give me a few minutes, I’ll be right back."

    show yoshi drunk2 at left2
    voice audio.yoshi_v_okay4
    yo "O-Okay, Goro…"

    hide goro_autumn
    hide goro talk3
    with dissolve

    show yoshi drunk1 at left2
    yo "..."

    show yoshi drunk5 at left2
    voice audio.yoshi_v_amazed2b
    yo "I can’t believe I’m really staying in the same room as Goro from now on…"
    yo "Back when I was a scout, I only got to come here to bring him his coffee…"
    yo "Then when he became my boss, I don’t think I ever let myself in here much. "

    hide yoshi_blush1
    show yoshi_blush2 at left2
    show yoshi drunk6 at left2
    voice audio.yoshi_v_think1a
    yo "And now that we’re officially together… We’re even sharing one bed… and unlike the vacation, now it’s permanent…"

    show yoshi panic3 at left2
    voice audio.yoshi_v_shock4
    yo "G-Gah! Why am I getting so flustered about this…?! This shouldn’t be any different from sleeping in the same tent or something…!"

    hide yoshi_blush2
    hide yoshi_undie2
    hide yoshi panic3
    show yoshi2_undie2 at left2
    show yoshi2_blush1 at left2
    show yoshi2 sigh4 at left2
    voice audio.yoshi_v_sigh3a
    yo "*sigh* I better get used to it before I make things awkward…"
    yo "Let me just scoot over here to make space for him…"

    show yoshi2_undie2 at center
    show yoshi2_blush1 at center
    show yoshi2 confused2 at center
    with move

    hide yoshi2_undie2
    hide yoshi2_blush1
    hide yoshi2 confused2
    show yoshi_undie2 at center
    show yoshi_blush1 at center
    show yoshi confused2 at center
    voice audio.yoshi_v_huh1
    yo "Huh? What’s this…? A box?"

    show cg_fade at truecenter
    show fxg10 1 at fx_pos with dissolve
    voice audio.yoshi_vsg20_line1
    yo "That’s weird… I thought we unboxed everything earlier today."

    voice audio.yoshi_vsg20_line2
    yo "I might as well empty it before Goro comes out of—"

    voice audio.yoshi_vsg20_line3
    yo "Oh, wait…"

    voice audio.yoshi_vsg20_line4
    yo "Something’s sticking out of the box… What is that?"

    show fxg10 2 at fx_pos with Dissolve(0.25)
    voice audio.yoshi_vsg20_line5
    yo "This looks familiar…"

    voice audio.goro_vsg20_line1
    g "Yoshinori."

    hide cg_fade
    hide fxg10 2
    show yoshi panic3 at center
    show goro_towel at right
    show goro norm4 at right
    voice audio.yoshi_v_shock4
    yo "G-GAH...!!" with vpunch
    yo "S-Sorry, Goro! I didn’t mean to go through your stuff without asking…!"

    show goro talk4 at right
    voice audio.goro_v_response3a1
    g "It’s fine."

    show yoshi_undie2 at left2
    show yoshi_blush1 at left2
    show yoshi shock1 at left2
    show goro_towel at right2
    show goro confused2 at right2
    with move

    voice audio.goro_v_confused1a2
    g "Looks like you found my stash of biking gear, huh?"

    hide yoshi_undie2
    hide yoshi shock1
    hide yoshi_blush1
    show yoshi2_undie2 at left2
    show yoshi2_blush1 at left2
    show yoshi2 shy5 at left2
    voice audio.yoshi_v_ah2
    yo "A-Ah, well…"

    show goro play2 at right2
    voice audio.goro_v_alright2a1
    g "I don’t mind showing you."

    hide yoshi2_undie2
    hide yoshi2_blush1
    hide yoshi2 shy5
    show yoshi_undie2 at left2
    show yoshi_blush1 at left2
    show yoshi confused3 at left2
    voice audio.yoshi_v_think3
    yo "Is this the same jacket from the picture you showed me earlier, Goro…?"

    show goro explain3 at right2
    voice audio.goro_v_agree1a1
    g "Yes, you have a sharp memory."

    show yoshi happy2 at left2
    voice audio.yoshi_v_amazed1a
    yo "It looks a lot cooler in person…!"

    hide goro_towel
    hide goro explain3
    show goro2_towel at right2
    show goro2 play3 at right2
    voice audio.goro_v_heh1a
    g "Heh, I’m surprised it’s still in good condition."

    show yoshi drunk2 at left2
    voice audio.yoshi_v_think1a
    yo "I wonder if it still fits you, though…?"

    hide goro2_towel
    hide goro2 play3
    show goro_towel at right2
    show goro think3 at right2
    voice audio.goro_v_think1a1
    g "The clothes, probably not anymore. They’re already too small for me, since I bulked up a lot over the years."
    g "Although, I think they’d fit your body… I was around your build the last time I wore them."

    hide goro_towel
    hide goro think3
    show goro2_towel at right2
    show goro2 happy1 at right2
    voice audio.goro_v_rush4b2
    g "Go on, try the jacket out."

    show yoshi confused3 at left2
    voice audio.yoshi_v_really2
    yo "R-Right now?"

    show goro2 play3 at right2
    voice audio.goro_v_yeah1a2
    g "Yeah. I’d like to see you in it."

    show yoshi drunk5 at left2
    voice audio.yoshi_v_okay2
    yo "Okay…!"

    hide yoshi_undie2
    hide yoshi_blush1
    hide yoshi drunk5
    show yoshi_biker2 at left2
    show yoshi_blush1 at left2
    show yoshi shock2 at left2
    with dissolve

    voice audio.yoshi_v_shock1a
    yo "Whoa…! It does fit me!"

    show goro2 laugh4 at right2
    voice audio.goro_v_laugh1b2
    g "Hehe, it looks perfect on you. I have to say, leather suits you very well."
    g "In fact, I’d like you to have it."

    show yoshi shock3 at left2
    voice audio.yoshi_v_what4
    yo "Wh-What?! Are you sure? Isn’t this really important to you, Goro?"

    hide goro2_towel
    hide goro2 laugh4
    show goro_towel at right2
    show goro comp2 at right2
    voice audio.goro_v_conj7a
    g "All the more reason I want you to have it. And besides, I’d really enjoy seeing you in it regularly."

    show yoshi comp2 at left2
    voice audio.yoshi_v_thanks2
    yo "Th-Thank you, Goro! I’ll definitely take care of it!"

    show goro happy2 at right2
    voice audio.goro_v_think2b1
    g "Let’s see what else I have in here."

    show cg_fade at truecenter
    show fxg10 3 at fx_pos with dissolve
    voice audio.yoshi_vsg20_line6
    yo "WAH! A-Are these…?!"

    voice audio.goro_vsg20_line2
    g "*ehem* I forgot I put these in the same box."

    voice audio.yoshi_vsg20_line7
    yo "Th-That’s a lot of belts… And some of them look like… *gulp*"

    voice audio.goro_vsg20_line3
    g "Well, I’ve always liked leather… including ‘intimate’ accessories."

    voice audio.goro_vsg20_line4
    g "I’d be lying if I said it’s not a kink of mine…"

    $ working = False
    $ shuffle_menu()
    menu():
        g "I’d be lying if I said it’s not a kink of mine…{fast}"
        "Tight.":
            $ working = True
            $ score_top += 1
            $ bond_top = True
            voice audio.yoshi_vsg20_line8a
            yo "These look really tight…"

            voice audio.goro_vsg20_line5a
            g "You’d be surprised how nice they actually feel…"

            voice audio.yoshi_vsg20_line9a
            yo "I’m not sure if this is the alcohol talking but… C-Can you try them on…?"
        "Pointy.":
            $ working = True
            $ score_bot += 1
            $ bond_top = False
            voice audio.yoshi_vsg20_line8b
            yo "Some of these looks painful to wear though…"

            voice audio.goro_vsg20_line5a
            g "You’d be surprised how nice they actually feel…"

            voice audio.yoshi_vsg20_line9b
            yo "I’m not sure if this is the alcohol talking but… C-Can I try them on…?"
        "Leather Daddy.":
            $ working = True
            $ score_bot += 2
            $ bond_top = False
            voice audio.yoshi_vsg20_line8c
            yo "I’m not sure if this is the alcohol talking but… I want to see you as a leather daddy…"

            voice audio.yoshi_vsg20_line9cd
            yo "*cough* I can’t believe I just said that."
        "Strap me up.":
            $ working = True
            $ score_top += 2
            $ bond_top = True
            voice audio.yoshi_vsg20_line8d
            yo "I’m not sure if this is the alcohol talking but… strap me up!"

            voice audio.yoshi_vsg20_line9cd
            yo "*cough* I can’t believe I just said that."

    hide cg_fade
    hide fxg10 3
    with dissolve

    hide goro_towel
    hide goro happy2
    show goro2_towel at right2
    show goro2 tease2 at right2
    voice audio.goro_v_laugh2b1
    g "Hehe… We were thinking the same thing…"
    g "Seeing you in my leather jacket really gets me going…"

    if bond_top == True:
        show goro2 tease5 at right2
        voice audio.goro_v_conj9a2
        g "And believe it or not… It’s always been my fantasy to see you in them too…"

        show yoshi drunk2 at left2
        voice audio.yoshi_v_really2
        yo "R-Really…? W-Well, I can make that a reality for you, Goro…"
        yo "L-Let’s put them on…"
    else:
        show goro2 tease5 at right2
        voice audio.goro_v_conj9a2
        g "And believe it or not… It’s always been my fantasy to see you in them…"

        show yoshi drunk6 at left2
        voice audio.yoshi_v_well2
        yo "I-I’m not wearing them unless you do too, Goro…"

        show goro2 tease3 at right2
        voice audio.goro_v_heh1a
        g "Heh, don’t mind if I do."

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black
    $quick_menu = False
    hide screen location
    hide screen timeline
    hide screen quick_menu
    with fade
    play sound sfx_leather
    $ renpy.pause (2.0, hard=True)

    $ location = location_gororoom
    $ quick_menu = True
    show screen location
    show screen timeline
    show screen quick_menu
    scene bg_gororoom_winter_night with fade
    play music on_the_edge loop

    show yoshi_bondage at left2
    show yoshi pain1 at left2
    show goro_bondage at right2
    show goro tease1 at right2
    show goro_shades at right2
    voice audio.yoshi_v_groan1a
    yo "Hngh… it’s quite tight… I’m not sure if I’m wearing this right…"

    show goro tease2 at right2
    voice audio.goro_v_response3a1
    g "You’re fine, Yoshinori. You look sexy as hell…"

    show yoshi comp3 at left2
    voice audio.yoshi_v_yeah4
    yo "Y-You too…"

    show goro tease3 at right2
    voice audio.goro_v_heh1a
    g "Heh, it’s been a while since I wore something like this…"
    g "Believe it or not, I used to wear it underneath my everyday clothes…"

    show yoshi play3 at left2
    voice audio.yoshi_v_really2
    yo "R-Really…?!"

    show goro tease5 at right2
    voice audio.goro_v_yeah1a2
    g "Yeah. But I always made sure no one noticed. "

    show yoshi play2 at left2
    voice audio.yoshi_v_amazed1b
    yo "Just thinking about you wearing something like this underneath your camp uniform… makes me squirm a little…"

    show goro tease2 at right2
    voice audio.goro_v_laugh1b2
    g "Hehe… Who knew you’d be into this too?"

    # if score_aiden >= 20:
    #     play sound sfx_doorslam
    #     show goro_bondage at center
    #     show goro shock1 at center
    #     show goro_shades at center
    #     show yoshi_bondage at left
    #     show yoshi shock1 at left
    #     show aiden_undie at right
    #     show aiden_blush2 at right
    #     show aiden laugh3 at right
    #     voice audio.aiden_v_drunk4a
    #     a "PARTYYYYYYY~!!" with vpunch
    #
    #     show yoshi panic3 at left
    #     voice audio.yoshi_v_shock3
    #     yo "GAH!! AIDEN?!"
    #
    #     show goro angry4 at center
    #     voice audio.goro_v_insult1a1
    #     g "Wh-Who said you could come in here?!"
    #
    #     hide aiden_undie
    #     hide aiden_blush2
    #     hide aiden laugh3
    #     show aiden2_undie at right
    #     show aiden2_blush2 at right
    #     show aiden2 drunk3 at right
    #     voice audio.aiden_v_drunk5a
    #     a "Wait, this isn’t our cabin…! Oh, right! You two moved out so you could get some fuckin’ without me! *hic*"
    #
    #     show yoshi angry3 at left
    #     voice audio.yoshi_v_aiden6
    #     yo "A-Aiden, you’re seriously drunk!! And did you walk around camp with just your underwear on?!"
    #
    #     hide aiden2_undie
    #     hide aiden2_blush2
    #     hide aiden2 drunk3
    #     show aiden_undie at right
    #     show aiden_blush2 at right
    #     show aiden drunk5 at right
    #     voice audio.aiden_v_hey1b1
    #     a "Hey! Speak for yourselves! You guys are wearing full-on kinky shit!"
    #
    #     show yoshi scared2 at left
    #     voice audio.yoshi_v_groan1a
    #     yo "Hngh… Just when I thought this couldn’t get more embarrassing than it already is…."
    #
    #     show goro disappoint3 at center
    #     voice audio.goro_v_sigh2a
    #     g "*sigh* Should we wrap up?"
    #
    #     $ working = False
    #     $ shuffle_menu()
    #     menu():
    #         g "*sigh* Should we wrap up?{fast}"
    #         "Let's bring Aiden back.":
    #             $ working = True
    #             $ score_top -= 1
    #             show yoshi sigh4 at left
    #             voice audio.yoshi_v_unsure3a
    #             yo "I guess let’s bring Aiden back to his quarters…"
    #
    #             hide aiden_undie
    #             hide aiden_blush2
    #             hide aiden drunk5
    #             show aiden2_undie at right
    #             show aiden2_blush2 at right
    #             show aiden2 pout5 at right
    #             voice audio.aiden_v_aww1a
    #             a "Aww… I wanna join in the fun too."
    #
    #             show goro annoy3 at center
    #             voice audio.goro_v_insult2a1
    #             g "No, clearly you’ve had enough, cockblocker."
    #
    #             show aiden2 sigh5 at right
    #             voice audio.aiden_v_sheesh2a
    #             a "Sheeeessshh, you sound so pissed, Grampss…."
    #
    #             $crack_sx = False
    #             jump day8_goro_aftersx
    #         "Let's call it a night.":
    #             $ working = True
    #             $ score_bot -= 1
    #             show yoshi sigh4 at left
    #             voice audio.yoshi_v_yeah4
    #             yo "Y-Yeah, let’s call it a night…"
    #
    #             hide aiden_undie
    #             hide aiden_blush2
    #             hide aiden drunk5
    #             show aiden2_undie at right
    #             show aiden2_blush2 at right
    #             show aiden2 pout5 at right
    #             voice audio.aiden_v_aww1a
    #             a "Aww… I wanna join in the fun too."
    #
    #             show goro annoy3 at center
    #             voice audio.goro_v_insult2a1
    #             g "No, clearly you’ve had enough, cockblocker."
    #
    #             show aiden2 sigh5 at right
    #             voice audio.aiden_v_sheesh2a
    #             a "Sheeeessshh, you sound so pissed, Grampss…."
    #
    #             $crack_sx = False
    #             jump day8_goro_aftersx
    #         "Three is better than two.":
    #             $ working = True
    #             $ score_top += 1
    #             show yoshi relief2 at left
    #             voice audio.yoshi_v_well1
    #             yo "W-Well, I still want to have some fun… Three is better than two?"
    #
    #             show goro play2 at center
    #             voice audio.goro_v_confused1a1
    #             g "Huh, so this is what you’re really into, Yoshinori?"
    #
    #             show yoshi awkward2 at left
    #             voice audio.yoshi_v_gulp1a
    #             yo "*gulp*"
    #
    #             show goro play5 at center
    #             voice audio.goro_v_alright1a1
    #             g "If you want it so much, then sure. I don’t mind sharing."
    #
    #             show goro_bondage at left
    #             show goro play1 at left
    #             show goro_shades at left
    #             show yoshi_bondage at center
    #             show yoshi awkward2 at center
    #             with move
    #
    #             show aiden drunk2 at right
    #             voice audio.aiden_v_celebrate1a1
    #             a "Finally~! I get to join in the fun~"
    #
    #             show goro annoy2 at left
    #             voice audio.goro_v_taunt2a
    #             g "Don’t get the wrong idea here, boy. I’m only agreeing once."
    #
    #             show aiden tease1 at right
    #             voice audio.aiden_v_yeah2b1
    #             a "Why? Afraid I can make Yoshi feel better than you can, Gramps?"
    #
    #             show goro play2 at left
    #             voice audio.goro_v_heh1a
    #             g "Heh… You have no idea just how much I make Yoshinori cum from just his ass."
    #
    #             show yoshi panic2 at center
    #             voice audio.yoshi_v_goro6
    #             yo "G-Goro…!"
    #
    #             show aiden bold5 at right
    #             voice audio.aiden_v_perv1
    #             a "Well, I can do that too! Maybe even better than you~ "
    #
    #             show goro angry2 at left
    #             voice audio.goro_v_really4a
    #             g "Are you challenging me again, kiddo?"
    #
    #             show aiden drunk6 at right
    #             voice audio.aiden_v_whistle2a
    #             a "I’m just sayin’ I won’t believe it til’ I see it~"
    #
    #             show goro angry3 at left
    #             voice audio.goro_v_taunt1a
    #             g "Looks like we’ve got some unfinished business."
    #
    #             show aiden drunk3 at right
    #             voice audio.aiden_v_rush1b1
    #             a "Then let’s settle this for good! First one to make Yoshi cum, wins!"
    #
    #             show yoshi panic3 at center
    #             voice audio.yoshi_v_what4
    #             yo "W-Wait, what…?!"
    #
    #             jump day8_goro_crackgoro
    #         "Maybe he can join?":
    #             $ working = True
    #             $ score_bot += 1
    #             show yoshi relief2 at left
    #             voice audio.yoshi_v_actually1a
    #             yo "M-Maybe Aiden can join us too…?"
    #
    #             show goro play2 at center
    #             voice audio.goro_v_confused1a1
    #             g "Huh, so this is what you’re really into, Yoshinori?"
    #
    #             show yoshi awkward2 at left
    #             voice audio.yoshi_v_gulp1a
    #             yo "*gulp*"
    #
    #             show goro play5 at center
    #             voice audio.goro_v_alright1a1
    #             g "If you want it so much, then sure. I don’t mind sharing."
    #
    #             show goro_bondage at left
    #             show goro play1 at left
    #             show goro_shades at left
    #             show yoshi_bondage at center
    #             show yoshi awkward2 at center
    #             with move
    #
    #             show aiden drunk2 at right
    #             voice audio.aiden_v_celebrate1a1
    #             a "Finally~! I get to join in the fun~"
    #
    #             show goro annoy2 at left
    #             voice audio.goro_v_taunt2a
    #             g "Don’t get the wrong idea here, boy. I’m only agreeing once."
    #
    #             show aiden tease1 at right
    #             voice audio.aiden_v_yeah2b1
    #             a "Why? Afraid I can make Yoshi feel better than you can, Gramps?"
    #
    #             show goro play2 at left
    #             voice audio.goro_v_heh1a
    #             g "Heh… You have no idea just how much I make Yoshinori cum from just his ass."
    #
    #             show yoshi panic2 at center
    #             voice audio.yoshi_v_goro6
    #             yo "G-Goro…!"
    #
    #             show aiden bold5 at right
    #             voice audio.aiden_v_perv1
    #             a "Well, I can do that too! Maybe even better than you~ "
    #
    #             show goro angry2 at left
    #             voice audio.goro_v_really4a
    #             g "Are you challenging me again, kiddo?"
    #
    #             show aiden drunk6 at right
    #             voice audio.aiden_v_whistle2a
    #             a "I’m just sayin’ I won’t believe it til’ I see it~"
    #
    #             show goro angry3 at left
    #             voice audio.goro_v_taunt1a
    #             g "Looks like we’ve got some unfinished business."
    #
    #             show aiden drunk3 at right
    #             voice audio.aiden_v_rush1b1
    #             a "Then let’s settle this for good! First one to make Yoshi cum, wins!"
    #
    #             show yoshi panic3 at center
    #             voice audio.yoshi_v_what4
    #             yo "W-Wait, what…?!"
    #
    #             jump day8_goro_crackgoro
    # else:
    if score_top > score_bot:
        show yoshi relief2 at left2
        voice audio.yoshi_v_well1
        yo "I’d be into anything as long as it’s with you…"

        show goro tease5 at right2
        voice audio.goro_v_heh1a
        g "Heh, Yoshinori…"

        jump day8_goro_6s
    elif score_bot > score_top:
        show goro tease5 at right2
        voice audio.goro_v_rush4b1
        g "Now… Why don’t we put these things to good use?"

        show yoshi shock1 at left2
        voice audio.yoshi_v_groan1a
        yo "Hngh…"

        jump day8_goro_6d
    else:
        $ position = renpy.random.randint(1,2)
        if position == 1:
            show yoshi relief2 at left2
            voice audio.yoshi_v_well1
            yo "I’d be into anything as long as it’s with you…"

            show goro tease5 at right2
            voice audio.goro_v_heh1a
            g "Heh, Yoshinori…"

            jump day8_goro_6s
        else:
            show goro tease5 at right2
            voice audio.goro_v_rush4b1
            g "Now… Why don’t we put these things to good use?"

            show yoshi shock1 at left2
            voice audio.yoshi_v_groan1a
            yo "Hngh…"

            jump day8_goro_6d

label day8_goro_aftersx:
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
    $ time_transition_night_to_day_winter2()
    $ renpy.pause (2.0, hard=True)
    jump day9_goro
