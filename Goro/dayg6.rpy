label day6_goro:
    $ day = "81"
    $ time = timeline_timeday
    $ location = location_hotellobby
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    $ working = True

    scene bg_hotel_lobby_day with fade
    play music close_distance loop

    show yoshi_winter at left2
    show yoshi talk1 at left2
    show goro_winter at right2
    show goro norm3 at right2
    voice audio.yoshi_v_think1a
    yo "Looks like the cleanup outside is done, the sky’s clear and I can see shuttles arriving, – we can finally go home."

    show goro talk2 at right2
    voice audio.goro_v_yeah1a1
    g "Yeah, some groups are already checking out."

    show yoshi explain2 at left2
    voice audio.yoshi_v_conj4a
    yo "I’m a little surprised, from the sound of things yesterday I thought we’d be here longer, but it did have to end eventually."
    yo "And either way, I did enjoy our trip here! W-Well… at least the first parts of it."

    hide goro_winter
    hide goro talk2
    show goro2_winter at right2
    show goro2 explain2 at right2
    voice audio.goro_v_conj10a1
    g "The last two nights were pretty rough. Hopefully they didn’t spoil the whole getaway for you."

    hide yoshi_winter
    hide yoshi explain2
    show yoshi2_winter at left2
    show yoshi2 worry2 at left2
    voice audio.yoshi_v_ah2
    yo "I’m going to be honest… I had a bit of trouble sleeping last night thinking about what happened yesterday with Emilia…"

    show yoshi2 sad4 at left2
    voice audio.yoshi_v_sigh3a
    yo "There were a couple of times I wanted to get up and check on her… but it was really late."
    yo "I really think the way I brought everything up to her went wrong at some point.  "

    hide goro2_winter
    hide goro2 explain2
    show goro_winter at right2
    show goro worry2 at right2
    voice audio.goro_v_comp5a
    g "I did notice you tossing and turning last night… but try not to worry so much, Yoshinori."
    g "We can resolve everything once we get back to the camp."

    show goro sigh2 at right2
    voice audio.goro_v_sigh2a
    g "After everything that’s happened at the hotel, I think it’s best if we try and handle it away from here… but I do expect it to be an awkward bus ride back."
    g "Just bear with it a little longer, alright?"

    show yoshi2_winter at p5_1
    show yoshi2 worry1 at p5_1
    show goro_winter at p5_2
    show goro norm3 at p5_2
    with move

    show lloyd_winter at p5_3
    show lloyd happy1 at p5_3
    show darius_winter at p5_4
    show darius happy1 at p5_4
    show aiden_winter at p5_5
    show aiden norm1 at p5_5
    with dissolve

    voice audio.lloyd_v_goodam1a1
    l "Hey, guys, good morning!"

    show darius happy1 at p5_4
    voice audio.darius_v_agree2a
    d "It’s pretty sunny outside. Almost like the blizzard didn’t happen."

    show aiden relief2 at p5_5
    voice audio.aiden_v_relief1a1
    a "Phew… I’m just glad we can finally go home now…"
    a "Believe it or not, I’m excited to get back to work! Fancy living is nice, but ehh... I don’t think it’s for me."

    show yoshi2_winter at p7_3
    show yoshi2 worry1 at p7_3
    show goro_winter at p7_4
    show goro norm3 at p7_4
    show lloyd_winter at p7_5
    show lloyd norm1 at p7_5
    show darius_winter at p7_6
    show darius norm1 at p7_6
    show aiden_winter at p7_7
    show aiden norm1 at p7_7
    with move

    show yuri_winter at p7_1
    show yuri happy1 at p7_1
    show jin_winter at p7_2
    show jin_glasses at p7_2
    show jin norm1 at p7_2
    with dissolve

    voice audio.yuri_v_greet2a
    yu "Hey, guys! Looks like you’re all ready to go!"
    yu "The workers are gathered as well and the shuttle should arrive in a few minutes!"

    show jin worry2 at p7_2
    voice audio.jin_v_think2b1
    j "U-Umm… Ms. Emilia isn’t here yet, though..."

    show goro confused2 at p7_4
    voice audio.goro_v_confused1a1
    g "I sent everyone a message to make sure they are prepared to go, including Emilia…"

    show jin talk2 at p7_2
    voice audio.jin_v_yeah1a
    j "Yeah, we saw it and came down right away…"

    show goro confused3 at p7_4
    voice audio.goro_v_wait2a1
    g "Wait, Yoshinori... You told me last night Emilia wanted to quit… Do you think she was serious about that…?"

    show yuri rage1 at p7_1
    voice audio.yuri_v_what5a
    yu "What?! Quitting?!"

    show yoshi2 sad6 at p7_3
    voice audio.yoshi_v_ah2
    yo "Ah… At some point during our talk last night, she did say that… But I didn’t think she meant like this…"

    show lloyd annoy5 at p7_5
    voice audio.lloyd_v_annoyed1b1
    l "Maybe she doesn’t want to show her face after being exposed as a liar."

    show darius annoy2 at p7_6
    voice audio.darius_v_ugh1
    d "Sounds about right."

    show yuri rage4 at p7_1
    voice audio.yuri_v_angry4a1
    yu "I can’t believe she’s just gonna run away after everything she did! "
    yu "If that’s what she wants, then good riddance to her!"

    hide yoshi2_winter
    hide yoshi2 sad6
    show yoshi_winter at p7_3
    show yoshi worry4 at p7_3
    voice audio.yoshi_v_yuri6
    yo "C-Calm down, Yuri… I don’t think she said that just to spite us…"

    show aiden sigh4 at p7_7
    voice audio.aiden_v_aww1a
    a "Man, I was hoping we coulda waited ’til we got back to camp to talk about this drama…  "

    show lloyd think2 at p7_5
    voice audio.lloyd_v_yoshi4a
    l "I am really curious, though… How did she react when you confronted her, Yoshi?"

    show darius disgust2 at p7_6
    voice audio.darius_v_think1a1
    d "I bet she denied everything."

    hide yoshi_winter
    hide yoshi worry4
    show yoshi2_winter at p7_3
    show yoshi2 upset6 at p7_3
    hide jin_glasses
    hide jin_winter
    hide jin talk2
    show jin_winter at p7_2
    show jin_glasses at p7_2
    show jin talk2 at p7_2
    voice audio.yoshi_v_well3
    yo "W-Well… She did at first. But since we had enough proof, she had no choice but to admit to everything…"

    show yoshi2 sad6 at p7_3
    yo "She was really caught off guard that we found out about her secret, though… that really pushed her over her limit…"

    show jin scared2 at p7_2
    voice audio.jin_v_worry1a3
    j "I-I can only imagine how scary she must’ve been…"

    show yuri angry3 at p7_1
    voice audio.yuri_v_angry5a
    yu "She really has the nerve to be the angry one?! "

    show lloyd upset3 at p7_5
    voice audio.lloyd_v_agree2c1
    l "Y-Yeah… The least she could do is apologize to all of us for treating us so crappily…"

    show darius disappoint2 at p7_6
    voice audio.darius_v_denial1a2
    d "Don’t expect that from her. You’ll just be disappointed."

    show yuri rage1 at p7_1
    voice audio.yuri_v_angry6b
    yu "It’s been so unfair this whole time, not only for us, but for the project too!"
    yu "We were all working on something serious and she risked that for her personal gain…!"

    show yuri angry6 at p7_1
    voice audio.yuri_v_angry3e
    yu "Not only that, everyone tried so hard to deal with her attitude! Especially you, Yoshi!"
    yu "I thought she would listen to you at least… "

    show yoshi2 sigh1 at p7_3
    voice audio.yoshi_v_actually2a
    yo "I really tried, but I don’t think she was ready at all to talk through and fix things…"

    show goro talk1 at p7_4
    voice audio.goro_v_conj5a
    g "Regardless, if she really is planning on quitting, that must be settled back at camp."

    hide aiden_winter
    hide aiden sigh4
    show aiden2_winter at p7_7
    show aiden2 talk1 at p7_7
    hide darius_winter
    hide darius disappoint2
    show darius_winter at p7_6
    show darius disappoint2 at p7_6
    voice audio.aiden_v_yeah1d2
    a "Yeah… Plus if she really is broke, there’s no way she can afford to stay another night…"

    hide yoshi2_winter
    hide yoshi2 sigh1
    show yoshi_winter at p7_3
    show yoshi talk1 at p7_3
    voice audio.yoshi_v_right5
    yo "That’s right. We can’t just leave her behind."
    yo "I’ll go to her room and fetch her! I’ll be right back!"

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
    scene cg black with fade
    play sound sfx_doorknock
    $ renpy.pause (1.0, hard=True)
    voice audio.yoshi_v_emilia5
    yo "Emilia? Are you up? "
    yo "It’s time for our trip back to camp, do you need help with your bags?"
    yo "..."

    voice audio.yoshi_v_but2
    yo "I-I know you said you quit… But can you at least come back with us to camp? "
    yo "I’m sure I can help you with your situation, if you’d just let me…"

    voice audio.yoshi_v_uh1a
    yo "Emilia…?"

    play music where_am_i loop
    play sound sfx_dooropen
    scene bg_hotel_room3_day_mess with fade
    show yoshi_winter at p5_5
    show yoshi confused2 at p5_5
    voice audio.yoshi_v_huh2
    yo "H-huh…? The door is open…"

    show yoshi shock1 at p5_5
    yo "...!"

    show yoshi shock2 at p5_5
    voice audio.yoshi_v_what4
    yo "W-What happened to this place?!"

    show yoshi scared2 at p5_5
    voice audio.yoshi_v_worry3
    yo "Emilia?! Where are you?!"

    show yoshi_winter at center
    show yoshi panic4 at center
    with move

    voice audio.yoshi_v_emilia8
    yo "Emilia?!"

    show yoshi_winter at left
    show yoshi panic3 at left
    with move

    voice audio.yoshi_v_shock3
    yo "*gasp*"

    show cg fade at truecenter
    show fx6 1 at fx_pos
    with dissolve

    voice audio.yoshi_vs10_line1
    yo "Emilia!! What happened?!"

    show fx6 2 at fx_pos
    with dissolve

    voice audio.yoshi_vs10_line2
    yo "A-Ah…! First Aid…!"

    voice audio.yoshi_vs10_line3
    yo "Airway, check... "

    voice audio.yoshi_vs10_line4
    yo "Pulse…"

    voice audio.yoshi_vs10_line5
    yo "Check."

    voice audio.yoshi_vs10_line6
    yo "Phew… Thank goodness, you’re still breathing…"

    voice audio.yoshi_vs10_line7
    yo "Wait… T-There’s pills all over the floor… Emilia, what did you do…?!"

    voice audio.yoshi_vs10_line8
    yo "I need to get help!"

    voice audio.yoshi_vs10_line9
    yo "Hang in there, Emilia…!"

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black with fade
    yo "{i}After moving Emilia to her bed, I immediately used the phone in her room to call for medical help.{/i}"
    yo "{i}Everyone else arrived as soon as they heard what happened… {/i}"

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
    scene bg_hotel_room3_day_mess with fade
    play music heracleum_musicbox_a loop

    show darius_winter at p6_2
    show darius worry1 at p6_2
    show jin_winter at p6_1
    show jin_glasses at p6_1
    show jin worry1 at p6_1
    show lloyd_winter at p6_3
    show lloyd sad1 at p6_3
    show aiden2_winter at p6_6
    show aiden2 worry1 at p6_6
    show yoshi2_winter at p6_5
    show yoshi2 sad2 at p6_5
    show yuri_winter at p6_4
    show yuri sad5 at p6_4
    voice audio.yuri_v_i1a
    yu "I… I can’t believe that Emilia would do something like this… "

    show aiden2 sad4 at p6_6
    voice audio.aiden_v_sigh1a
    a "Me either…"

    show jin worry2 at p6_1
    voice audio.jin_v_worry2c
    j "I-Is Ms. Emilia going to be okay here…? D-Don’t we need to bring her to a hospital?"

    show darius think5 at p6_2
    voice audio.darius_v_think1a1
    d "The roads to the nearest one are still being cleared of snow…"

    show lloyd worry3 at p6_3
    voice audio.lloyd_v_relief2b2
    l "It’s a good thing this hotel had an in-house doctor available to help."

    show yoshi2 sad5 at p6_5
    voice audio.yoshi_v_unsure1b
    yo "She wasn’t injured or struggling to breathe when I found her… So, let’s just hope everything is ok…"

    show jin_winter at p7_1
    show jin_glasses at p7_1
    show jin worry2 at p7_1
    show darius_winter at p7_2
    show darius think5 at p7_2
    show lloyd_winter at p7_3
    show lloyd worry3 at p7_3
    show yuri_winter at p7_4
    show yuri sad5 at p7_4
    show yoshi2_winter at p7_5
    show yoshi2 sad2 at p7_5
    show aiden2_winter at p7_6
    show aiden2 worry1 at p7_6
    with move

    show goro_winter at p7_7
    show goro worry1 at p7_7
    with dissolve

    show yuri worry5 at p7_4
    voice audio.yuri_v_goro9c
    yu "Dad…!! H-How’s Emilia?! What’s her status?"

    show goro sad2 at p7_7
    voice audio.goro_v_scold1a1
    g "Calm down, Yuri. Let the doctor explain everything. "
    ol "*ehem* It appears what happened to Ms. Komarova is a mild overdose, specifically from sleeping pills."
    ol "Thankfully, it wasn’t anywhere near a lethal dose, and I was able to administer medicine that reverses the sedating effects."
    ol "She’s fortunate that someone found her, or it could have been much worse."

    show yuri worry4 at p7_4
    voice audio.yuri_v_worry1c
    yu "I-Is she gonna be okay…?"
    ol "Right now, she’s in a very deep sleep due to the pills. "
    ol "She might experience some lethargy when she regains her consciousness but overall, she’ll be fine."

    show yuri sigh3 at p7_4
    voice audio.yuri_v_relief3b1
    yu "Phew… Th-That’s a relief…"
    ol "I do have to address some concerns related to Ms. Komarova’s overall well-being."
    ol "Mr. Nomoru described her behavior and the situation prior to this incident that could’ve potentially led to this."
    ol "The pills appear to be prescribed to Ms. Komarova for sleep deprivation, and it appears she takes these pills regularly, but today she took more than she should.    "
    ol "Some individuals might misuse medications like these when they are subjected to emotional distress."
    ol "I advise that you all be cautious in how you deal with her when she wakes up, and it may be beneficial for her to seek additional help after this."

    show yoshi2 sad4 at p7_5
    voice audio.yoshi_v_response1c
    yo "We understand…"
    ol "Here’s a prescription for her medicine. "
    ol "Make sure she takes these and refrains from sleeping pills for now."

    show goro talk1 at p7_7
    voice audio.goro_v_comp1a1
    g "You can leave it to me. I’ll keep an eye on her."
    ol "I hear you’re all scheduled to leave today. There’s no need to admit her to a hospital right now."
    ol "She should be able to handle your trip back. Our shuttle’s seats can be laid back so she can properly rest."

    show goro worry3 at p7_7
    voice audio.goro_v_thanks1b1
    g "Thanks for the help, doctor. "
    ol "Alright. I’ll leave Ms. Komarova in your care now. Please take care of her."

    show aiden2 worry5 at p7_6
    voice audio.aiden_v_so1
    a "S-So what’s our plan now…? Are we still going home?"

    show goro talk3 at p7_7
    voice audio.goro_v_well1a
    g "We’re proceeding as planned. The doctor said it’s safe for Emilia to travel."

    hide yoshi2_winter
    hide yoshi2 sad4
    show yoshi_winter at p7_5
    show yoshi worry2 at p7_5
    hide yuri_winter
    hide yuri sigh3
    show yuri_winter at p7_4
    show yuri sigh3 at p7_4
    voice audio.yoshi_v_yeah1
    yo "Yeah, and I believe we can take care of her better at camp."

    show lloyd sad5 at p7_3
    voice audio.lloyd_v_sigh1c
    l "Luckily, the workers aren’t scheduled to return for a few more days too."

    show darius talk1 at p7_2
    voice audio.darius_v_agree2a
    d "It’ll be much quieter, and we won’t be busy at all."

    show yuri worry2 at p7_4
    voice audio.yuri_v_goro4a
    yu "D-Did you tell Mr. Clermont about this yet, Dad…?"

    hide goro_winter
    hide goro talk3
    show goro2_winter at p7_7
    show goro2 worry1 at p7_7
    voice audio.goro_v_think1a1
    g "I was planning on doing that when we got home… I really don’t want him to extend our stay here any longer, especially after what just happened."
    g "But once he finds out about Emilia’s lies… I’m sure he won’t hesitate to fire her…"

    show yuri sad4 at p7_4
    voice audio.yuri_v_unsure1a2
    yu "I’m not sure how Emilia will handle that when she wakes up…"

    show jin upset6 at p7_1
    voice audio.jin_v_sorry1c3
    j "Now I feel really guilty I urged everyone to look into her… I didn’t expect it to spiral into all this…"

    show darius sad2 at p7_2
    voice audio.darius_v_think1b1
    d "It was only a matter of time until we found out about it. "

    show lloyd upset6 at p7_3
    voice audio.lloyd_v_conj1b2
    l "And we were only trying to find out the truth for the sake of our project…"
    l "Don’t get me wrong, I feel just as bad that it came to this…"

    show yuri sad5 at p7_4
    voice audio.yuri_v_sigh2a
    yu "I didn’t know things seemed so hopeless for her if she were to lose her job at Camp Buddy…"

    hide yoshi_winter
    hide yoshi worry2
    show yoshi2_winter at p7_5
    show yoshi2 sad6 at p7_5
    hide yuri_winter
    hide yuri sad5
    show yuri_winter at p7_4
    show yuri sad5 at p7_4
    voice audio.yoshi_v_oops2
    yo "She really did lose everything she had, just like we found out in our search…"
    yo "And from what I understand, she’s really been struggling ever since she began fending for herself."

    show yoshi2 sigh4 at p7_5
    voice audio.yoshi_v_sigh3a
    yo "To her, Camp Buddy was the only choice she had left."
    yo "She lied her way back out of desperation not only for her survival but also to regain her pride…"

    show yuri sad3 at p7_4
    voice audio.yuri_v_sad3a
    yu "I just can’t understand why that was enough for her to go this far…"

    show yoshi2 upset5 at p7_5
    voice audio.yoshi_v_but2
    yo "I… think the way I talked to her last night is what really pushed her over the edge…"

    show aiden2 sad4 at p7_6
    voice audio.aiden_v_yoshi4a
    a "Yoshi…"

    show yoshi2 upset4 at p7_5
    voice audio.yoshi_v_emilia4
    yo "Emilia’s been fighting alone all this time… And coming back here was almost a cry for help that I didn’t realize…"
    yo "To her, I was still the only friend she made back then, and the fact that she couldn’t rely on me at her lowest point hurt her the most…"

    show yoshi2 sad2 at p7_5
    voice audio.yoshi_v_sad1
    yo "It’s almost as if I led her to do this…"

    show yuri worry3 at p7_4
    voice audio.yuri_v_yoshi4a
    yu "N-No, Yoshi…! I played just as much role in this too…!"
    yu "I was the one who went against her from the start, even up until this morning…"

    show yuri sigh3 at p7_4
    voice audio.yuri_v_sad2a
    yu "I know I had good reasons to be upset, but I still took it too far sometimes with what I said and how I acted…"

    show aiden2 worry4 at p7_6
    voice audio.aiden_v_guys6a
    a "Yoshi, Yuri… Please don’t blame yourselves like that…"

    hide goro2_winter
    hide goro2 worry1
    show goro_winter at p7_7
    show goro talk1 at p7_7
    voice audio.goro_v_alright2c1
    g "It was out of our control. None of us could’ve predicted this would happen."
    g "I’m sure we all played a role in this, but it won’t help Emilia, or any of us for that matter, if we keep focusing on what went wrong."

    show aiden2 worry2 at p7_6
    voice audio.aiden_v_yeah1g1
    a "Y-Yeah… The best thing we can do for now is to help her get better."

    show jin sad1 at p7_1
    show darius sad1 at p7_2
    show lloyd upset1 at p7_3
    show aiden2 worry1 at p7_6
    show yoshi2 sad1 at p7_5
    show yuri sad1 at p7_4
    all "..."

    show goro explain1 at p7_7
    voice audio.goro_v_rush4b2
    g "For now, let’s head back to camp. We’ll figure out what to do next when we’re all settled in."
    g "I’ll carry Emilia to the shuttle and get her situated."

    show goro talk3 at p7_7
    voice audio.goro_v_rush1c1
    g "Lloyd, Darius, gather the workers and have them board the shuttle as well."

    show goro talk4 at p7_7
    voice audio.goro_v_request2a1
    g "Yoshinori and the rest, kindly pack Emilia’s belongings and make sure we don’t leave anything behind."

    hide aiden2 worry1
    hide aiden2_winter
    hide yoshi2_winter
    show aiden_winter at p7_6
    show yoshi_winter at p7_5
    hide yoshi2 sad1

    show jin sad2 at p7_1
    show darius talk1 at p7_2
    show lloyd talk2 at p7_3
    show aiden talk1 at p7_6
    show yoshi worry2 at p7_5
    show yuri worry2 at p7_4
    all "Yes, sir!"

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black with fade
    yo "{i}Everyone was in a somber mood the entire drive home… We couldn’t help but worry about Emilia…{/i}"
    yo "{i}We all took turns checking on her, but she was still sleeping peacefully even when we arrived back at the camp…{/i}"

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
    play music brand_new_day_winter loop

    show aiden_winter2 at left
    show aiden relief2 at left
    show yoshi_winter2 at center
    show yoshi norm4 at center
    show goro_winter2 at right
    show goro norm3 at right
    voice audio.aiden_v_relief1a1
    a "Ahhh~ Home sweet home! Camp Buddy, I missed you!"
    a "Brrr… It’s so cold out here…! So much for ‘summer’ camp!"

    show yoshi talk2 at center
    voice audio.yoshi_v_shock1d
    yo "I’ve never seen this much snow here before."

    hide goro_winter2
    hide goro norm3
    show goro2_winter2 at right
    show goro2 worry4 at right
    voice audio.goro_v_sigh1a
    g "It looks like the snowstorm hit harder here than expected while we were away… "

    show aiden_winter2 at p4_2
    show aiden relief2 at p4_2
    show yoshi_winter2 at p4_3
    show yoshi norm4 at p4_3
    show goro2_winter2 at p4_4
    show goro2 worry4 at p4_4
    with move

    show yuri_winter2 at p4_1
    show yuri talk3 at p4_1
    with dissolve

    voice audio.yuri_v_guys1a
    yu "Uhh, guys? We need to bring Emilia to her room right away. She’s still asleep, but I’m worried she might catch a cold out here."

    hide goro2_winter2
    hide goro2 worry4
    show goro_winter2 at p4_4
    show goro talk3 at p4_4
    voice audio.goro_v_here1a
    g "I’ll take her from here, dear."

    hide goro_winter2
    hide goro talk3
    with dissolve

    show yuri serious4 at p4_1
    voice audio.yuri_v_alright1c1
    yu "Alright, I’ll go and heat up all of our cabins!"

    show yuri_winter2 at p4_2
    show yuri serious4 at p4_2
    show aiden_winter2 at p4_3
    show aiden shock1 at p4_3
    show yoshi_winter2 at p4_4
    show yoshi shock1 at p4_4
    with move

    show jin_winter at p4_1
    show jin_glasses at p4_1
    show jin sleepy4 at p4_1
    with dissolve

    voice audio.jin_v_hngh1c
    j "*hurl*"

    show yuri worry3 at p4_2
    voice audio.yuri_v_worry3a
    yu "Oh dear…!"

    show jin sleepy5 at p4_1
    voice audio.jin_v_sorry1a3
    j "I-I’m sorry, I thought I could handle the bus ride this time around…"

    show yuri worry4 at p4_2
    voice audio.yuri_v_here1a
    yu "Here, come with me and let’s get you some rest too."

    hide yuri_winter2
    hide yuri worry4
    hide jin_winter
    hide jin_glasses
    hide jin sleepy5
    with dissolve

    show lloyd_winter2 at p4_1
    show lloyd shock3 at p4_1
    show darius_winter2 at p4_2
    show darius shock4 at p4_2
    with dissolve

    voice audio.lloyd_v_shock2b1
    l "Oh no!! This isn’t looking good, Dar! We have to check on the site!"

    show darius worry3 at p4_2
    voice audio.darius_v_unsure1a
    d "Cross your fingers."

    hide lloyd_winter2
    hide lloyd shock3
    hide darius_winter2
    hide darius worry3
    with dissolve

    show yoshi worry2 at p4_4
    voice audio.yoshi_v_think1a
    yo "It looks like Lloyd and Darius are in a rush to check the expansion site."

    hide aiden_winter2
    hide aiden shock1
    show aiden2_winter2 at p4_3
    show aiden2 worry2 at p4_3
    voice audio.aiden_v_yeah1d2
    a "Yeah, Lloyd was freaking out the whole ride home about the storm…"

    show yoshi talk1 at p4_4
    voice audio.yoshi_v_rush5
    yo "Let’s catch up with them."

    hide aiden2_winter2
    hide aiden2 worry2
    show aiden_winter2 at p4_3
    show aiden talk2 at p4_3
    voice audio.aiden_v_agree2e1
    a "Right behind ya!"

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
    scene bg_site3_winter_day with fade
    play music where_am_i loop
    play bgsound sfxloop_windy loop

    show lloyd_winter2 at left
    show lloyd panic3 at left
    show darius_winter2 at right
    show darius panic1 at right
    voice audio.lloyd_v_swear1b1
    l "Noooooo!!!! It’s worse than I expected! Everything is buried in snow…!!"

    show darius disappoint5 at right
    voice audio.darius_v_ugh1
    d "This is bad…"

    show lloyd_winter2 at p4_1
    show lloyd panic3 at p4_1
    show darius_winter2 at p4_2
    show darius panic1 at p4_2
    with move

    show yoshi_winter2 at p4_3
    show yoshi talk1 at p4_3
    show aiden_winter2 at p4_4
    show aiden norm3 at p4_4
    with dissolve

    voice audio.yoshi_v_worry3a
    yo "Is everything alright h—"

    show yoshi shock6 at p4_3
    voice audio.yoshi_v_shock1a
    yo "WHOA!" with vpunch

    hide aiden_winter2
    hide aiden norm3
    show aiden2_winter2 at p4_4
    show aiden2 pain1 at p4_4
    voice audio.aiden_v_sheesh2a
    a "Sheesh… That doesn’t look good…"

    show darius upset2 at p4_2
    voice audio.darius_v_sorry2b
    d "We have bad news. It seems that some of the foundations and roofing framework collapsed from the snow buildup."

    show lloyd upset3 at p4_1
    voice audio.lloyd_v_swear3c3
    l "Even all the tarps I covered the materials with got blown away by the storm…"

    show darius disappoint3 at p4_2
    voice audio.darius_v_ah1c3
    d "This is what happens when you leave the work halfway done…"

    show lloyd tired5 at p4_1
    voice audio.lloyd_v_sad1a1
    l "I knowwww… Huhuhu… You didn’t have to say that again, Dar…"
    l "This will push us back a few more weeks… or even months! "

    hide yoshi_winter2
    hide yoshi shock6
    show yoshi2_winter2 at p4_3
    show yoshi2 worry2 at p4_3
    voice audio.yoshi_v_oops2
    yo "This was actually what Sir Goro was afraid of when we were scheduling work around the winter time…"
    yo "Snowstorms happen here at least once a year, but this was way worse than usual…"

    hide yoshi2_winter2
    hide yoshi2 worry2
    show yoshi_winter2 at p4_3
    show yoshi sigh1 at p4_3
    voice audio.yoshi_v_relief4
    yo "Thank goodness, we were away from camp when this happened. It would’ve been really dangerous for everyone."

    show lloyd sad4 at p4_1
    voice audio.lloyd_v_agree2c3
    l "Yeah… Despite these damages, it was the right call for us to a take that break. "

    show aiden2 worry2 at p4_4
    voice audio.aiden_v_sad1a
    a "Does that mean we gotta wait ’til spring to work again?"

    show lloyd upset3 at p4_1
    voice audio.lloyd_v_disagree1d1
    l "No, unfortunately. Waiting that long and letting these damages endure the cold would only make it worse. "

    show darius sad2 at p4_2
    voice audio.darius_v_agree1b
    d "Yes. Without further weatherproofing, the materials will deteriorate at a rapid rate until they’re unsalvageable."

    hide yoshi_winter2
    hide yoshi sigh1
    show yoshi2_winter2 at p4_3
    show yoshi2 sad4 at p4_3
    voice audio.yoshi_v_think1a
    yo "Something like that would make us miss our target for sure…"

    show lloyd sigh1 at p4_1
    voice audio.lloyd_v_sorry1b2
    l "*sigh* I’m really sorry… This is my department… I should’ve taken more precautions…"
    l "I didn’t consider that there would be a freak snowstorm we’d be dealing with…"

    hide yoshi2_winter2
    hide yoshi2 sad4
    show yoshi_winter2 at p4_3
    show yoshi worry2 at p4_3
    voice audio.yoshi_v_comp3
    yo "This isn’t anyone’s fault. None of us could’ve anticipated a storm like this."

    show lloyd worry2 at p4_1
    voice audio.lloyd_v_sigh2a
    l "But still… If only I had more experience working with site conditions like this, we would’ve been able to prevent it…"

    show darius sad3 at p4_2
    voice audio.darius_v_comp3a
    d "You did what you could. Let’s just get to work and do what we can to fix this."

    hide aiden2_winter2
    hide aiden2 worry2
    show aiden_winter2 at p4_4
    show aiden shock2 at p4_4
    voice audio.aiden_v_wait1a1
    a "Wait… You two aren’t planning on working right now, are you?"

    show darius talk2 at p4_2
    voice audio.darius_v_conj2a
    d "We have to at least clear the snow away from the paths and structures so we can assess the damages."

    show lloyd sad1 at p4_1
    voice audio.lloyd_v_agree2a2
    l "Yeah, we can’t really plan out the repairs without getting a clearer view."

    hide aiden_winter2
    hide aiden shock2
    show aiden2_winter2 at p4_4
    show aiden2 worry5 at p4_4
    voice audio.aiden_v_think1a1
    a "It’s tough to even move around in this mess… "

    show lloyd sigh4 at p4_1
    voice audio.lloyd_v_sad1a2
    l "Huhuhu… This makes me wanna cry… "

    show darius sad3 at p4_2
    voice audio.darius_v_aww1b1
    d "Your crystals lied to you about having a good day today, Lloyd."

    show yoshi think2 at p4_3
    voice audio.yoshi_v_well3
    yo "Well… The news did say we’d have clear weather for the next few days. Maybe we can work, as long as we’re careful?"

    show lloyd worry2 at p4_1
    voice audio.lloyd_v_think1a1
    l "You think if we start shoveling now, we can clear it all up?"
    l "I mean, it’s just some snow after all… how hard can it be?  "

    show darius confused2 at p4_2
    voice audio.darius_v_think2b3
    d "Some snow? There’s at least eight inches covering an entire two acres, Lloyd."

    show lloyd sigh3 at p4_1
    voice audio.lloyd_v_aww1a2
    l "Aww, shucks… I forgot we don’t have the workers… They won’t be coming back for a few more days…"
    l "Ughhh… Why is everything going wrong suddenly?!"

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    show yoshi talk3 at p4_3
    voice audio.yoshi_v_confident2
    yo "I could help out! At least that's more manpower…!"

    show lloyd shock3 at p4_1
    show darius shock1 at p4_2
    voice audio.lloyd_v_shock3a2
    l "Wah, really…?"

    play music brand_new_day_winter loop
    hide aiden2_winter2
    hide aiden2 worry5
    show aiden_winter2 at p4_4
    show aiden bold2 at p4_4
    voice audio.aiden_v_hey1a2
    a "Hey, count me in as well~! I wouldn’t mind getting my hands dirty, especially after all that pampering from our vacation!"

    show lloyd worry3 at p4_1
    voice audio.lloyd_v_wait1c1
    l "Are you guys sure?! This isn’t your job, so you don’t have to…"

    show yoshi comp2 at p4_3
    voice audio.yoshi_v_agree1a
    yo "Of course. We do this every year anyways. "
    yo "Besides, it looks like all the snow here is still loose, so it shouldn’t be too hard to pile it up somewhere else."

    show darius think5 at p4_2
    voice audio.darius_v_think1a2
    d "I estimate with the four of us… we could clear at least the important parts of the site by the day the workers return."

    show lloyd excited3 at p4_1
    voice audio.lloyd_v_praise2c
    l "That’s good enough! Better than waiting for ice to melt!"

    show lloyd laugh2 at p4_1
    voice audio.lloyd_v_laugh1a1
    l "I’ll go get the shovels!"

    hide lloyd_winter2
    hide lloyd laugh2
    with moveoutleft

    show darius shock3 at p4_2
    voice audio.darius_v_ah1d1
    d "H-Hey…! Don’t run or you’ll slip…!"

    hide darius_winter2
    hide darius shock1
    with moveoutleft

    show yoshi_winter2 at left2
    show yoshi norm3 at left2
    show aiden_winter2 at right2
    show aiden sigh5 at right2
    with move

    hide aiden_winter2
    hide aiden sigh5
    show aiden2_winter2 at right2
    show aiden2 sigh5 at right2
    voice audio.aiden_v_sheesh2a
    a "Sheesh… All of a sudden, our work piled in like a storm… Literally…"

    hide yoshi_winter2
    hide yoshi norm3
    show yoshi2_winter2 at left2
    show yoshi2 sigh2 at left2
    voice audio.yoshi_v_yeah3
    yo "Yeah… The problems just keep coming one on top of another…   "

    show aiden2 confused5 at right2
    voice audio.aiden_v_unsure2a
    a "Not sure how Mr. Clermont will react to all of this…"

    show aiden2 sigh3 at right2
    voice audio.aiden_v_sigh1a
    a "First that whole dinner fiasco, then the situation with Emilia, and now this…"
    a "If I were him, I’d be really disappointed. "

    hide yoshi2_winter2
    hide yoshi2 sigh2
    show yoshi_winter2 at left2
    show yoshi bold2 at left2
    voice audio.yoshi_v_comp5
    yo "Don’t worry, Aiden. We’ve overcome so many challenges before, and this won’t be any different."

    hide aiden2_winter2
    hide aiden2 sigh3
    show aiden_winter2 at right2
    show aiden talk1 at right2
    voice audio.aiden_v_yeah1b2
    a "Yeah, I guess you’re right, Yoshi. This is just another hurdle for us to jump over!"
    a "Either way, I’ll always be right behind you and Gramps!"

    show yoshi comp3 at left2
    voice audio.yoshi_v_thanks4
    yo "Thanks, Aiden. I’m sure it’ll all be worth it in the end."
    yo "We just have to do our best to keep things under control and get our momentum back."

    show yoshi explain2 at left2
    voice audio.yoshi_v_conj5b
    yo "For now, I trust Goro’s judgment on how to handle the situation with Mr. Clermont."

    hide aiden_winter2
    hide aiden talk1
    show aiden2_winter2 at right2
    show aiden2 confused2 at right2
    voice audio.aiden_v_yeah2a1
    a "Oh yeah… Gramps’s the one who’s gonna have to explain all this… Did he talk to him yet?"

    show yoshi confused2 at left2
    voice audio.yoshi_v_think1a
    yo "Hmmm… I know the hotel staff informed him about us being stuck at the hotel, but I think that’s all he knows so far."
    yo "I’m sure he’ll want to report about the site condition once he finds out at least."

    show aiden2 awkward5 at right2
    voice audio.aiden_v_think2a
    a "What about the stuff with Emilia..?"

    hide yoshi_winter2
    hide yoshi confused2
    show yoshi2_winter2 at left2
    show yoshi2 explain2 at left2
    voice audio.yoshi_v_conj3a
    yo "Goro told me on our way back he’ll let Emilia recover first before we address the situation with her."

    hide aiden2_winter2
    hide aiden2 awkward5
    show aiden_winter2 at right2
    show aiden sigh1 at right2
    voice audio.aiden_v_response2b2
    a "Yeah, that makes sense… I’m really glad Gramps is taking it easy on Emilia... And even more so that he’s taking care of her right now!"
    a "Especially after things got so personal back at the hotel… "

    show aiden comp3 at right2
    voice audio.aiden_v_unsure1b
    a "I guess he really has softened up these past few months, huh? "

    hide yoshi2_winter2
    hide yoshi2 explain2
    show yoshi_winter2 at left2
    show yoshi comp2 at left2
    voice audio.yoshi_v_yeah3
    yo "Yeah… He’s been trying to be more understanding and forgiving than he was before."

    show aiden comp2 at right2
    voice audio.aiden_v_agree4b
    a "I can tell. He’s always been the kinda guy who doesn’t show any emotion and bottles everything up."
    a "It shocked me seeing him open up like that yesterday, letting everyone ask stuff I never guessed he’d wanna answer."

    show aiden comp5 at right2
    voice audio.aiden_v_aww2a
    a "I can really see that he wants to be closer to everyone, just like how he was when he was our scoutmaster…"

    show yoshi comp5 at left2
    voice audio.yoshi_v_gratitude2
    yo "I’m glad you noticed his efforts, Aiden. He’s had a hard time trying to adjust to all of this at once."

    show aiden relief2 at right2
    voice audio.aiden_v_well1a1
    a "Well, it was only possible because of you."

    hide yoshi_winter2
    hide yoshi comp5
    show yoshi2_winter2 at left2
    show yoshi2 confused2 at left2
    voice audio.yoshi_v_huh1
    yo "Huh? What do you mean?  "

    hide aiden_winter2
    hide aiden relief2
    show aiden2_winter2 at right2
    show aiden2 confused6 at right2
    voice audio.aiden_v_think1a1
    a "Hmm…. There’s just something in Gramps’ eyes whenever I see him with you, and that goes way back to when you were still a scout."
    a "He’s a lot more carefree, and always smiling. "

    hide aiden2_winter2
    hide aiden2 confused6
    show aiden_winter2 at right2
    show aiden comp5 at right2
    voice audio.aiden_v_glad1b
    a "You’re his comfort zone where he can be a person too, and not just a leader or dad that always has to be responsible for everything."

    show yoshi2 awkward3 at left2
    voice audio.yoshi_v_ah2
    yo "Ah… "

    show aiden worry2 at right2
    voice audio.aiden_v_sigh1a
    a "I know that side of him was gone for the last few years, after we went our separate ways and came back."

    show aiden comp2 at right2
    voice audio.aiden_v_but1a1
    a "But seeing that he’s still got that part inside of him… I think you’ve been really bringing it out of him."
    a "Seeing you guys together, it’s like there’s some new spark in him… From the way he talks to you, to the tiniest gestures."

    show aiden happy2 at right2
    voice audio.aiden_v_laugh2a1
    a "There’s no denying how much he enjoys your company… and it seems like he’s been wanting it for a really long time now, too."
    a "So, yeah! Congrats to you two!  "

    show yoshi2 shy5 at left2
    voice audio.yoshi_v_what2
    yo "Wh-What are you trying to say, Aiden…?"

    show aiden play2 at right2
    voice audio.aiden_v_comeon1b1
    a "Come on. You think I haven’t noticed how you’re calling him by just his name now?"

    $ working = False
    $ shuffle_menu()
    menu():
        a "Come on. You think I haven’t noticed how you’re calling him by just his name now?{fast}"
        "You could too.":
            $ working = True
            $ score_goro -= 5
            $ score_aiden += 5
            hide yoshi2_winter2
            hide yoshi2 shy5
            show yoshi_winter2 at left2
            show yoshi happy1 at left2
            voice audio.yoshi_v_well1
            yo "Well, you could call him Goro too, if you wanted. "

            show aiden tease1 at right2
            voice audio.aiden_v_oho1a
            a "Oho~? You guys got room for one more?"

            hide yoshi_winter2
            hide yoshi happy1
            show yoshi2_winter2 at left2
            show yoshi2 comp6 at left2
            voice audio.yoshi_v_unsure1b
            yo "I-I’m not sure if he’d like that though."

            show aiden laugh3 at right2
            voice audio.aiden_v_laugh2b1
            a "HAHAHA! You crack me up, Yoshi!"
            a "Can’t imagine myself calling him anything other than Gramps! Well, maybe ‘Daddy’ fits better!"

            show yoshi2 sigh4 at left2
            voice audio.yoshi_v_sigh3a
            yo "*sigh* I don’t know where we’re going with this…"

            show aiden tease1 at right2
            voice audio.aiden_v_laugh2b1
            a "Hehehe… Classic Yoshi."
        "Don't get the wrong idea.":
            $ working = True
            $ score_goro -= 2
            show yoshi2 awkward3 at left2
            voice audio.yoshi_v_uh1a
            yo "D-Don’t get the wrong idea, Aiden… I’m not trying to be disrespectful to him, he’s still our camp president!"

            show aiden comp2 at right2
            voice audio.aiden_v_laugh1b1
            a "That’s not what I meant at all, silly!"

            show yoshi2 sigh4 at left2
            voice audio.yoshi_v_sigh3a
            yo "*sigh* I don’t know where we’re going with this…"

            show aiden tease1 at right2
            voice audio.aiden_v_laugh2b1
            a "Hehehe… Classic Yoshi."
        "Okay, you got me.":
            $ working = True
            $ score_goro += 1
            show yoshi2 sigh1 at left2
            voice audio.yoshi_v_okay4
            yo "Okay… you got me…"

            show aiden bold2 at right2
            voice audio.aiden_v_laugh2a1
            a "Ha! I knew it! "

            show yoshi2 comp6 at left2
            voice audio.yoshi_v_laugh6
            yo "Ahehe…"

            show aiden play2 at right2
            voice audio.aiden_v_oho1a
            a "Yuri will go nuts once she finds out!"

            show yoshi2 shy6 at left2
            voice audio.yoshi_v_ah2
            yo "Ahh… I’m not sure how she’ll take that… Surprisingly, it doesn’t look like she’s noticed anything at all…"

            show aiden tease1 at right2
            voice audio.aiden_v_shock1d1
            a "That’s wild… Can you believe you’re going to be her stepdad now, Yoshi?!"

            hide yoshi2_winter2
            hide yoshi2 shy6
            show yoshi_winter2 at left2
            show yoshi panic4 at left2
            voice audio.yoshi_v_shock4
            yo "G-Gah…! Don’t say something like that!"

            show aiden laugh1 at right2
            voice audio.aiden_v_well1a1
            a "Well, all I can say is just keep it up, whatever you two have going on!"
            a "That big ol’ teddy bear is like a dad to me already! You better not screw up and make him go back to being scary and grumpy, you got that?!"

            hide yoshi_winter2
            hide yoshi panic4
            show yoshi2_winter2 at left2
            show yoshi2 comp3 at left2
            voice audio.yoshi_v_sure1
            yo "S-Sure, Aiden…"
        "He likes it that way.":
            $ working = True
            $ score_goro += 2
            show yoshi2 awkward3 at left2
            voice audio.yoshi_v_well1
            yo "H-He likes it that way, Aiden…"

            show aiden bold2 at right2
            voice audio.aiden_v_laugh2a1
            a "Hahaha! You’re not even denying it!"
            a "Maaaan, you guys are so lucky."

            show yoshi2 comp6 at left2
            voice audio.yoshi_v_laugh6
            yo "Ahehe…"

            show aiden play2 at right2
            voice audio.aiden_v_oho1a
            a "Yuri will go nuts once she finds out!"

            show yoshi2 shy6 at left2
            voice audio.yoshi_v_ah2
            yo "Ahh… I’m not sure how she’ll take that… Surprisingly, it doesn’t look like she’s noticed anything at all…"

            show aiden tease1 at right2
            voice audio.aiden_v_shock1d1
            a "That’s wild… Can you believe you’re going to be her stepdad now, Yoshi?!"

            hide yoshi2_winter2
            hide yoshi2 shy6
            show yoshi_winter2 at left2
            show yoshi panic4 at left2
            voice audio.yoshi_v_shock4
            yo "G-Gah…! Don’t say something like that!"

            show aiden laugh1 at right2
            voice audio.aiden_v_well1a1
            a "Well, all I can say is just keep it up, whatever you two have going on!"
            a "That big ol’ teddy bear is like a dad to me already! You better not screw up and make him go back to being scary and grumpy, you got that?!"

            hide yoshi_winter2
            hide yoshi panic4
            show yoshi2_winter2 at left2
            show yoshi2 comp3 at left2
            voice audio.yoshi_v_sure1
            yo "S-Sure, Aiden…"

    show aiden happy1 at right2
    voice audio.aiden_v_anyway1a
    a "Now, where’s Lloyd and Darius?! "
    a "I bet they don’t know where the shovels are! Stay right here, Yoshi!"

    hide yoshi2_winter2
    hide yoshi2 comp3
    hide yoshi2 sigh4
    show yoshi_winter2 at left2
    show yoshi comp6 at left2
    voice audio.yoshi_v_alright1
    yo "Alright, Aiden."

    hide aiden_winter2
    hide aiden happy1
    with dissolve

    show yoshi comp1 at left2
    yo "..."

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black with fade
    yo "{i}After a while, Aiden and the others came back with the shovels and we started to clear the snow.{/i}"

    scene cg black
    hide screen location
    hide screen timeline
    hide screen quick_menu
    $quick_menu = False
    with fade
    $time_transition_day_to_sunset_winter2()
    $ renpy.pause (2.0, hard=True)

    $ location = location_gororoom
    $ time = timeline_timesunset
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_gororoom_winter_sunset with fade
    play music buddy_oath_goro_sad loop

    show emilia_sleep at center
    show emilia sleepy4 at center
    voice audio.emilia_v_ugh2
    e "Nnn…"

    show emilia confused2 at center
    voice audio.emilia_v_think1
    e "H-Huh…? "

    show emilia_sleep at left2
    show emilia shock1 at left2
    with move

    show goro_autumn at right2
    show goro talk3 at right2
    with dissolve

    voice audio.goro_v_emilia4a
    g "Ah, Emilia… You’re awake."

    show emilia shock2 at left2
    voice audio.emilia_v_gasp1
    e "*gasp* Wh-Where am I?"

    hide goro_autumn
    hide goro talk3
    show goro2_autumn at right2
    show goro2 explain2 at right2
    voice audio.goro_v_think1a1
    g "We’re back at Camp Buddy. You were passed out for the whole day."

    show emilia awkward1 at left2
    e "..."

    hide goro2_autumn
    hide goro2 explain2
    show goro_autumn at right2
    show goro worry2 at right2
    voice audio.goro_v_alright3a
    g "How are you feeling…?"

    show emilia upset4 at left2
    e "..."

    show emilia sad2 at left2
    voice audio.emilia_v_question1a
    e "H-Have you… been taking care of me?"

    show goro explain5 at right2
    voice audio.goro_v_no1a1
    g "No, I’m only watching over you. Yuri’s been the one nursing you all day…  She just went out to fetch your medicine."

    show emilia upset6 at left2
    voice audio.emilia_v_oh4b
    e "Y-Yuri…? I see…"

    hide goro_autumn
    hide goro explain5
    show goro2_autumn at right2
    show goro2 sad2 at right2
    voice audio.goro_v_sigh2a
    g "You gave us quite the scare back there… It’s a good thing Yoshinori found you just in time."
    g "You would’ve been in a worse state if it were a little later."

    show emilia upset4 at left2
    e "..."

    hide goro2_autumn
    hide goro2 sad2
    show goro_autumn at right2
    show goro explain2 at right2
    voice audio.goro_v_well1a
    g "Well, what matters is that you’re home now. Everyone was quite worried about you."

    show emilia panic3 at left2
    voice audio.emilia_v_wait1b3
    e "Everyone…? But I was— Wait…"
    e "N-No! I… I shouldn’t be here anymore…! "

    show emilia_sleep at p5_1
    show emilia pain4 at p5_1
    with move

    show goro_autumn at p5_2
    show goro worry1 at p5_2
    with move

    voice audio.emilia_v_ugh1
    e "U-Ugh…! "

    show goro panic2 at p5_2
    voice audio.goro_v_wait3a1
    g "Take it easy, Emilia… You’re not well. "
    g "You need to stay put and recover."

    show emilia_sleep at left2
    show emilia irked2 at left2
    show goro_autumn at right2
    show goro worry1 at right2
    with move

    voice audio.emilia_v_question1b1
    e "Wh-Why are you doing this…? "
    e "…I thought you didn’t want me here anymore. "

    show goro shock1 at right2
    g "..."

    show goro shy6 at right2
    voice audio.goro_v_but2a
    g "I know we have our differences… But, I won’t let a disagreement get in the way of your well-being."
    g "What I said to you and how I acted… I want you to know that I regret them."

    show goro sigh4 at right2
    voice audio.goro_v_sorry1b1
    g "You don’t need to accept it but… I apologize for everything."

    show emilia upset3 at left2
    voice audio.emilia_v_disagree4a
    e "I don’t understand… Why would you apologize just like that…?"
    e "Even after everything I did…"

    show goro talk1 at right2
    voice audio.goro_v_sigh2a
    g "Because no matter how you look at it, I did something wrong. And neither of us can move forward if we don’t come to an understanding."
    g "And, after thinking about it, I know why you ended saying everything you did…"

    show goro explain2 at right2
    voice audio.goro_v_conj3a1
    g "I believe you and I share a common trait when it comes to managing our emotions."
    g "When we keep things to ourselves, it just boils up inside until it explodes…"

    show goro worry2 at right2
    voice audio.goro_v_conj10a1
    g "And in those moments, we end up losing sight of what’s right…"

    show emilia upset4 at left2
    e "..."

    show goro sad3 at right2
    voice audio.goro_v_sorry1b2
    g "I just want you to know that I don’t have anything personal against you. We all have our own struggles, and I apologize for not attempting to learn yours."

    show emilia sad2 at left2
    voice audio.emilia_v_conj4a
    e "I… really need to leave. I don’t belong here…"

    hide goro_autumn
    hide goro sad3
    show goro2_autumn at right2
    show goro2 confused2 at right2
    voice audio.goro_v_oh3a
    g "Where will you go…?"

    show emilia sigh3 at left2
    voice audio.emilia_v_sigh1b
    e "Nowhere… I-It’s over for me…"

    show goro2 talk1 at right2
    voice audio.goro_v_no1a1
    g "No, it’s not. You still have Camp Buddy."
    g "I might not know the full story… But you’ve gone through so much and now’s not the time to give up."

    show emilia angry2 at left2
    voice audio.emilia_v_disagree2b
    e "D-don’t pity me! I… I don’t need sympathy…"

    show goro2 explain2 at right2
    voice audio.goro_v_conj5a
    g "Look… I know how important it is to you to be independent and tough… As a leader, I bear that responsibility as well."

    hide goro2_autumn
    hide goro2 explain2
    show goro_autumn at right2
    show goro talk3 at right2
    voice audio.goro_v_but2a
    g "But sometimes, it’s alright to show vulnerability… It helps others to understand you better and find ways to help you."
    g "Whatever happened to you before caused you plenty of pain, frustration and anger, and you’ve been battling it alone… so it’s no wonder things turned out this way…"

    show emilia sad1 at left2
    e "..."

    show goro sad3 at right2
    voice audio.goro_v_conj10a1
    g "Back when my wife and I separated… I thought I could handle it all myself, but I couldn’t."
    g "I started taking what I had left for granted, not realizing how much people around me cared."

    show goro comp2 at right2
    voice audio.goro_v_comp5a
    g "I’m sure if you stop and look around as well, you can find something worth fighting for too."

    show emilia cry1 at left2
    e "..."

    hide goro_autumn
    hide goro comp2
    show goro2_autumn at right2
    show goro2 shy2 at right2
    voice audio.goro_v_ah1a
    g "A-Ah, I apologize… I didn’t mean to get carried away. I only wanted to let you know that I can sympathize with where you are right now."
    g "In any case, I’m sure you need to rest… So please, take it easy and we can talk when—"

    play sound sfx_doorknock
    show emilia_sleep at p4_1
    show emilia upset4 at p4_1
    show goro2_autumn at p4_2
    show goro2 shock1 at p4_2
    with move

    show yuri_winter at p4_3
    show yuri talk3 at p4_3
    show yoshi_winter at p4_4
    show yoshi talk1 at p4_4
    with dissolve

    voice audio.yoshi_v_greet1a1
    yo "We’re here. How’s Em—"

    show yuri shock4 at p4_3
    voice audio.yuri_v_shock2a
    yu "*gasp* "

    show yuri_winter at p4_2
    show yuri shock4 at p4_2
    show goro2_autumn at p4_3
    show goro2 shock1 at p4_3
    with move

    show emilia panic3 at p4_1
    voice audio.emilia_v_ah2b
    e "A-Ah…!!"

    show yuri worry5 at p4_2
    voice audio.yuri_v_relief2b1
    yu "Thank goodness, you’re awake now…! I was so worried!"

    show emilia panic1 at p4_1
    e "...!"

    show yuri worry4 at p4_2
    voice audio.yuri_v_worry2a
    yu "A-Are you feeling alright…? If you need us to bring you to the hospital, just tell us right away…!"

    show emilia sad2 at p4_1
    voice audio.emilia_v_conj1a
    e "I’m just feeling a little light-headed from too much sleep… But I’m fine now, really…"

    show yoshi_winter at p4_3
    show yoshi worry3 at p4_3
    show goro2_autumn at p4_4
    show goro2 shock1 at p4_4
    with move

    voice audio.yoshi_v_emilia4
    yo "Emilia, I apologize for pushing you to talk last night… "
    yo "What I said really upset you… And you were right about not being able to count on me as your friend."

    hide yoshi_winter
    hide yoshi worry3
    show yoshi2_winter at p4_3
    show yoshi2 sad4 at p4_3
    voice audio.yoshi_v_sad1
    yo "This wouldn’t have happened if I had approached things in a better way…"

    show emilia upset3 at p4_1
    voice audio.emilia_v_question1a
    e "W-Why are you apologizing…?"

    show yuri upset2 at p4_2
    voice audio.yuri_v_emilia4a
    yu "I-I’m sorry too, Emilia… I know we never had a great relationship, even back when we were scouts."
    yu "And I admit that when you came back, I was still pretty biased, which made things worse between us."

    show yuri sad3 at p4_2
    voice audio.yuri_v_sorry1c1
    yu "I really regret being closed-minded this whole time, and I never considered that you had reasons for your actions…"

    show emilia upset6 at p4_1
    voice audio.emilia_v_disagree4a
    e "I don’t understand… "
    e "You were all supposed to hate me for everything I’ve done… but instead you’re treating me like this…"

    show emilia sad4 at p4_1
    voice audio.emilia_v_regret4
    e "If anything, I should be the one apologizing… not only for my lies but also for causing you all trouble…"

    hide yoshi2_winter
    hide yoshi2 sad4
    show yoshi_winter at p4_3
    show yoshi sad6 at p4_3
    voice audio.yoshi_v_but2
    yo "But we really understand now why you ended up doing those things..."

    show yuri worry2 at p4_2
    voice audio.yuri_v_agree1b2
    yu "Yes, we can put that all in the past now… What’s important is what we do from here on."

    show emilia sigh1 at p4_1
    voice audio.emilia_v_sigh1b
    e "I really can’t fathom how you could all let that go so easily, when I’ve done nothing but let my bitterness consume me…"
    e "The expectations I had were so unreasonable, acting so entitled and then being so loathsome when things didn’t go my way…"

    show emilia sad4 at p4_1
    voice audio.emilia_v_regret3
    e "In a sense, I thought to myself that this place allowed me to return to what I used to be. But then, what I used to be was a horrible person to begin with…"
    e "There’s just no excuse… I was so, so wrong…"

    show emilia cry2 at p4_1
    voice audio.emilia_v_sorry1a
    e "I… I’m really sorry…"

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    show emilia cry4 at p4_1
    voice audio.emilia_v_sigh2a
    e "*cries*"

    show yuri_winter at left
    show yuri worry2 at left
    with move
    play music heracleum_musicbox_b loop
    show cg fade at truecenter
    show fx7 1 at fx_pos
    with dissolve

    e "...!!"

    voice audio.yuri_vs11_line1
    yu "I forgive you… And I’m sure the rest of us feel the same way…"

    voice audio.yuri_vs11_line2
    yu "I hope you can forgive us too for not understanding sooner."

    show fx7 2 at fx_pos with Dissolve(0.25)
    #voice audio.emilia_vs11_line1 #jey
    e "*sniff*"

    voice audio.yuri_vs11_line3
    yu "Just please remember you have people to count on now…"

    show fx7 3 at fx_pos with Dissolve(0.25)
    voice audio.yuri_vs11_line4
    yu "You don’t have to be alone anymore. We’ll all be here for you."

    #voice audio.emilia_vs11_line2
    e "*cries*"

    hide cg fade
    hide fx7 3
    with dissolve

    show yuri_winter at p4_2
    show yuri comp1 at p4_2
    with move

    hide goro2_autumn
    hide goro2 shock1
    show goro_autumn at p4_4
    show goro awkward4 at p4_4
    voice audio.goro_v_yuri5b
    g "Hey, Yuri… Don’t work her up too much, she’s still recovering…"

    show emilia cry3 at p4_1
    voice audio.emilia_v_goro2
    e "*sniff* I-I owe you an apology the most, Sir Goro…"
    e "You were only doing your job as the leader of the camp, and all I did was let my prejudice take over – intentionally pushing your buttons every chance I got…"

    show emilia cry2 at p4_1
    voice audio.emilia_v_yoshi2
    e "Just like Yoshinori, you’ve been as tolerant as possible with my behavior, given how I deliberately tested everyone’s patience…"
    e "Even when I was a scout here, you always handled me with compassion regardless of my immaturity…"
    e "That’s all I wanted from my parents, and I see now that I took it for granted even here…"

    show emilia cry3 at p4_1
    voice audio.emilia_v_sorry2
    e "So, I’m really sorry…"

    show goro comp2 at p4_4
    voice audio.goro_v_request5a1
    g "I’m really humbled by your acknowledgement, Emilia… But please, save your tears… "

    show emilia upset4 at p4_1
    voice audio.emilia_v_regret1
    e "I’m just really ashamed… because what I just did earlier today made things a lot worse…"
    e "And I don’t want you all to think that any of it is your fault…"

    show yuri worry4 at p4_2
    voice audio.yuri_v_worry1b
    yu "What was going through your mind before that, Emilia…?"

    show emilia sad4 at p4_1
    voice audio.emilia_v_sigh1b
    e "I couldn’t sleep last night… I was just thinking about everything that happened and what I’d done."
    e "I felt like it was tearing me apart, and I panicked and took a lot of my sleeping pills, hoping they would calm me down…"

    show emilia upset4 at p4_1
    voice audio.emilia_v_think1
    e "I couldn’t remember anything much after that… "

    show yuri sad5 at p4_2
    voice audio.yuri_v_emilia4a
    yu "Th-That could’ve gone worse for you, Emilia…"

    show emilia sigh2 at p4_1
    voice audio.emilia_v_regret3
    e "I knew it was wrong… But at that moment, everything was dark and I felt like there was no way out for me…"
    e "I was desperate to get out of the hole I was left in by my parents. "

    show emilia sad2 at p4_1
    voice audio.emilia_v_conj4a
    e "I have no money, I have no home, and I could barely survive… I don’t even have a family to rely on."
    e "I have nothing left outside of Camp Buddy… This really was the last chance I had, yet I took it for granted by being so greedy and arrogant…"

    show emilia sigh1 at p4_1
    voice audio.emilia_v_sigh1b
    e "I thought if I held myself to a high standard, that I’d be able to fit in and be someone important again."

    show yuri sad4 at p4_2
    voice audio.yuri_v_emilia4b
    yu "Emilia, you don’t have to try to be something that you aren’t with us..."

    show emilia sad2 at p4_1
    voice audio.emilia_v_regret3
    e "I know… I realize now that I let the wrong things define who I was, and it was my main drive for acting the way I did."

    hide yoshi_winter
    hide yoshi sad6
    show yoshi2_winter at p4_3
    show yoshi2 worry2 at p4_3
    voice audio.yoshi_v_sorry2b
    yo "Emilia… I’m really sorry to hear all that…"
    yo "This really is the first time we’ve seen you let your walls down, and I’m glad you trusted us enough to tell us how you honestly feel…"

    hide yoshi2_winter
    hide yoshi2 worry2
    show yoshi_winter at p4_3
    show yoshi comp2 at p4_3
    voice audio.yoshi_v_confident2
    yo "And it’s just like Yuri said, we’re here to help you out. Our doors were open to you then and they still are now."

    show yuri comp2 at p4_2
    voice audio.yuri_v_response2e1
    yu "We may never compare to what you had, but we can be your family too. "

    show goro worry3 at p4_4
    voice audio.goro_v_comp2a1
    g "You were once a part of Camp Buddy… So, don’t let anything change that."

    show emilia sad1 at p4_1
    e "..."

    show emilia sad2 at p4_1
    voice audio.emilia_v_think1
    e "I really don’t deserve all this kindness…"
    e "I’ve used up all my chances and now I’m being given another one… I don’t know if I can trust myself to not make another mistake…"

    show goro talk1 at p4_4
    voice audio.goro_v_comp2a1
    g "You can’t give up now, Emilia… It’s not too late to make things right. "
    g "There’s obviously change that needs to happen, and we can only do so much to help you."

    show goro explain2 at p4_4
    voice audio.goro_v_but2a
    g "It has to come from you… I’m sure you’re tired of living in your old ways too."

    show emilia sad4 at p4_1
    voice audio.emilia_v_regret2b
    e "I am. I don’t want to live like that anymore."

    show goro talk3 at p4_4
    voice audio.goro_v_encourage2a
    g "You can do something about it, especially now that you have people to support you."
    g "I know you’re a fighter, Emilia. We both are… And fighters don’t go down easily, no matter what! "

    show goro happy3 at p4_4
    voice audio.goro_v_encourage1a
    g "Just keep moving forward and never give up!"

    show yuri shock4 at p4_2
    voice audio.yuri_v_shock1a1
    yu "Oh my… That sounded like a Yoshi speech, so I guess we know where he got it from…"

    hide goro_autumn
    hide goro happy3
    show goro2_autumn at p4_4
    show goro2 disappoint2 at p4_4
    voice audio.goro_v_ehem1a
    g "*ehem* "

    show yoshi shock1 at p4_3
    show yuri shock1 at p4_2
    show emilia angry2 at p4_1
    voice audio.emilia_v_agree2c
    e "That’s right! I am fierce! I won’t let this keep me down!"
    e "I do want to turn my life around! And I’m not going to waste this chance!"

    hide yoshi_winter
    hide yoshi shock1
    show yoshi2_winter at p4_3
    show yoshi2 shock2 at p4_3
    voice audio.yoshi_v_amazed2b
    yo "I-I can’t believe that worked… "

    show yuri shock2 at p4_2
    voice audio.yuri_v_response2b2
    yu "Yeah, the scouts always ignore you when you do it."

    show emilia angry3 at p4_1
    voice audio.emilia_v_comp1b
    e "I will make up for everything, mark my words! And I—"

    show yuri worry3 at p4_2
    voice audio.yuri_v_wait2b1
    yu "Slow down, Emilia… It’s a little early for you to be moving around…"

    hide yoshi2_winter
    hide yoshi2 shock2
    show yoshi_winter at p4_3
    show yoshi comp3 at p4_3
    voice audio.yoshi_v_yeah1
    yo "Yeah. Try and rest for now, Emilia. "
    yo "And if you feel like you need professional help, just tell us, alright?"

    show emilia comp2 at p4_1
    voice audio.emilia_v_thanks2
    e "Thank you…"
    e "Not only for taking care of me, but also for all the advice and understanding…"

    show yoshi comp2 at p4_3
    voice audio.yoshi_v_gratitude2
    yo "I’m really glad we were able to resolve things on a positive note, Emilia."
    yo "It’s a huge step for you, I’m sure. But I’m really proud that you’re off to a great start."

    show emilia comp1 at p4_1
    e "..."

    show yoshi comp3 at p4_3
    voice audio.yoshi_v_alright1
    yo "Now, I think we’ve bothered you enough! You keep resting and we’ll check on you again tomorrow, alright?"

    show emilia relief3 at p4_1
    voice audio.emilia_v_agree1b2
    e "I will. Thank you again."

    show yuri happy1 at p4_2
    voice audio.yuri_v_actually1a
    yu "Actually, I’ll stay here and keep Emilia company for the night!"

    show emilia shock2 at p4_1
    voice audio.emilia_v_what2
    e "H-Huh? Y-You don’t have to…!"

    show yuri bold2 at p4_2
    voice audio.yuri_v_sarcastic2a
    yu "Ah-ah-ah! You don’t have a choice!"

    show emilia sigh1 at p4_1
    voice audio.emilia_v_sigh1b
    e "*sigh*"

    hide goro2_autumn
    hide goro2 disappoint2
    show goro_autumn at p4_4
    show goro happy2 at p4_4
    voice audio.goro_v_alright1a1
    g "Alright then. I’ll see you two tomorrow."

    show yoshi_winter at p8_7
    show yoshi bold2 at p8_7
    show goro_autumn at p8_8
    show goro norm3 at p8_8
    with move

    voice audio.yoshi_v_amazed3
    yo "That was a really amazing speech you gave there, Goro!"

    show goro sigh2 at p8_8
    voice audio.goro_v_sigh2a
    g "*sigh* I blame you for rubbing off on me."

    hide yoshi_winter
    hide yoshi bold2
    show yoshi2_winter at p8_7
    show yoshi2 worry4 at p8_7
    voice audio.yoshi_v_hey4
    yo "H-Hey…! That’s not a bad thing, is it…?!"

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black with fade
    yo "{i}It seems like finally, after everything we’ve been through the last few months, we were able to have an honest talk with Emilia…{/i}"
    yo "{i}I’m so glad she opened up to us, allowing us to finally understand her side, and is willing to give it another chance…{/i}"
    $ renpy.pause (1.0, hard=True)
    yo "{i}Since the sun was still up for a little while longer, Goro and I headed back to join everyone and continue shoveling before it got dark.{/i}"

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
    scene bg_site4_winter_sunset with fade
    play music sunset_stroll_winter loop
    play bgsound sfxloop_windy loop

    show aiden_winter2 at p6_2
    show aiden worry1 at p6_2
    show jin_winter at p6_1
    show jin_glasses at p6_1
    show jin pain3 at p6_1
    show darius_winter2 at p6_4
    show darius norm3 at p6_4
    show lloyd_winter2 at p6_3
    show lloyd norm3 at p6_3
    show goro_winter2 at p6_5
    show goro norm3 at p6_5
    show yoshi_winter2 at p6_6
    show yoshi norm3 at p6_6
    voice audio.jin_v_oof3a
    j "A-Achooo!! *Sniff*"

    hide goro_winter2
    hide goro norm3
    show goro2_winter2 at p6_5
    show goro2 confused5 at p6_5
    voice audio.goro_v_think3
    g "Uhh… Jin? You should really go back to the cabin. You may catch a cold at this rate."

    hide aiden_winter2
    hide aiden worry1
    show aiden2_winter2 at p6_2
    show aiden2 comp3 at p6_2
    hide jin_winter
    hide jin_glasses
    hide jin pain3
    show jin_winter at p6_1
    show jin_glasses at p6_1
    show jin pain3 at p6_1
    voice audio.aiden_v_yeah1d1
    a "Yeaaahh… you’ve been shoveling for a while now. Leave this work to the big guys!"

    show jin comp3 at p6_1
    voice audio.jin_v_comp8b1
    j "I-I’m fine! It’s just a little sneeze!"
    j "I know we need as many hands as possible… So, I really don’t mind the work, even though I’m slow."

    show lloyd sigh5 at p6_3
    voice audio.lloyd_v_sad1b1
    l "Huhuhu… Even with all of us shoveling here, we didn’t even clear it halfway…"

    show darius think4 at p6_4
    voice audio.darius_v_think1a1
    d "Do I need to use two shovels?"

    show aiden2 sigh4 at p6_2
    voice audio.aiden_v_sigh1a
    a "At this point, I think we’ll die of hypothermia before we finish all of this. "

    show goro2 think5 at p6_5
    voice audio.goro_v_think1a1
    g "This seems to be a bigger problem than I anticipated… I think we should stop for now.  It will only get colder since the sun has just set too."
    g "Let’s continue tomorrow. Hopefully we can make more progress."

    show jin thinkdn2 at p6_1
    voice audio.jin_v_sigh1a
    j "We really need more people to clear this snow…"

    hide goro2_winter2
    hide goro2 think5
    show goro_winter2 at p6_5
    show goro sigh1 at p6_5
    voice audio.goro_v_sigh1a
    g "Sadly, the workers won’t arrive till next week… I don’t think we have much of a choice but to do it ourselves."

    hide yoshi_winter2
    hide yoshi norm3
    show yoshi2_winter2 at p6_6
    show yoshi2 think4 at p6_6
    yo "..."

    hide aiden2_winter2
    hide aiden2 sigh4
    show aiden_winter2 at p6_2
    show aiden talk1 at p6_2
    voice audio.aiden_v_yeah1c1
    a "Either way, I agree with Gramps… We should go inside and call it for now. "
    a "You know what they say, “leave today’s problems to tomorrow’s me!”"

    hide goro_winter2
    hide goro sigh1
    show goro2_winter2 at p6_5
    show goro2 bored1 at p6_5
    voice audio.goro_v_aiden2b
    g "I don’t think that’s a very productive motto, Aiden…"

    play sound sfx_stomachgrowl
    show lloyd hungry1 at p6_3
    l "*stomach growls*"

    show lloyd hungry2 at p6_3
    voice audio.lloyd_v_groan1c2
    l "Oof… Man, I’m hungry… Did you cook anything yet, Aiden…?"

    show aiden bold5 at p6_2
    voice audio.aiden_v_orderup1a
    a "Is that a real question? Of course I did! I made chicken noodle soup, and there’s cocoa too! All fresh and steaming hot!   "

    show lloyd hungry4 at p6_3
    voice audio.lloyd_v_amazed1a1
    l "Wow! That sounds so gooood! "

    show darius excited1 at p6_4
    voice audio.darius_v_excited1a1
    d "Cocoa. Yum."

    show lloyd amazed3 at p6_3
    voice audio.lloyd_v_rush1a1
    l "Come on, Dar! I wanna get filled up!"

    show darius bold2 at p6_4
    voice audio.darius_v_rush1
    d "I’ll come inside."

    hide darius_winter2
    hide darius bold2
    hide lloyd_winter2
    hide lloyd amazed3
    with dissolve

    show jin_winter at p4_1
    show jin_glasses at p4_1
    show jin thinkdn2 at p4_1
    show aiden_winter2 at p4_2
    show aiden bold5 at p4_2
    show goro2_winter2 at p4_3
    show goro2 think4 at p4_3
    show yoshi2_winter2 at p4_4
    show yoshi2 think4 at p4_4
    with move

    voice audio.goro_v_think1a1
    g "Hmm… Can I request some sausage and eggs…? I’m really craving them for some reason."

    show aiden excited3 at p4_2
    voice audio.aiden_v_oho1a
    a "Ooh, breakfast for dinner? I can whip a big one out for you, no problem, Gramps!"

    show jin daydream2 at p4_1
    voice audio.jin_v_unsure2a3
    j "Maybe I’m just tired and I’m hearing everything wrong…. "

    hide goro2_winter2
    hide goro2 think4
    show goro_winter2 at p4_3
    show goro talk1 at p4_3
    voice audio.goro_v_comp2a1
    g "You’re already drooling. I’ll share my sausage and give you a mouthful."

    show jin dizzy1 at p4_1
    j "..."

    hide jin_winter
    hide jin_glasses
    hide jin dizzy1
    hide goro_winter2
    hide goro talk1
    with dissolve

    show aiden_winter2 at left2
    show aiden laugh1 at left2
    show yoshi2_winter2 at right2
    show yoshi2 think4 at right2
    with move

    voice audio.aiden_v_laugh2a1
    a "Now that was just dirty. Hahaha!"

    hide yoshi2_winter2
    hide yoshi2 think4
    show yoshi_winter2 at right2
    show yoshi talk3 at right2
    voice audio.yoshi_v_greet2a1
    yo "You can go ahead too, Aiden. I just need to get something! I’ll catch up!"

    show aiden happy1 at left2
    voice audio.aiden_v_alright1a2
    a "Alright~"

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black
    hide screen location
    hide screen timeline
    hide screen quick_menu
    $quick_menu = False
    with fade
    $ time_transition_sunset_to_night_winter2()
    $ renpy.pause (2.0, hard=True)

    $ location = location_messhall
    $ time = timeline_timenight
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_messhall_winter_night with fade
    play music ready_for_tomorrow_winter loop

    show goro_autumn at p6_5
    show goro talk1 at p6_5
    show darius_winter at p6_3
    show darius norm1 at p6_3
    show jin_autumn at p6_4
    show jin_glasses at p6_4
    show jin norm3 at p6_4
    show aiden_autumn at p6_1
    show aiden talk2 at p6_1
    show lloyd_winter at p6_2
    show lloyd norm3 at p6_2
    show yoshi_autumn at p8_8
    show yoshi norm1 at p8_8
    voice audio.aiden_v_oh1a
    a "Oh, there he is!"

    show goro talk3 at p6_5
    voice audio.goro_v_yoshi1a
    g "Over here, Yoshinori. I saved you a plate."

    show yoshi_autumn at p6_6
    show yoshi happy1 at p6_6
    with move

    voice audio.yoshi_v_greet1a1
    yo "Hello, sorry for the delay!"

    show aiden happy2 at p6_1
    voice audio.aiden_v_response1a
    a "No problem! Gramps was just getting us caught up a little on Emilia’s condition, but he said that you and Yuri talked to her more than he did."

    show jin worry2 at p6_4
    voice audio.jin_v_yeah2a
    j "Y-Yeah, we were worried things could’ve gone sour again…"

    show yoshi explain2 at p6_6
    voice audio.yoshi_v_actually1a
    yo "Actually, it was the opposite. She was really remorseful over the way she acted, and grateful over how we were taking care of her."

    show lloyd shock2 at p6_2
    voice audio.lloyd_v_amazed1b1
    l "Wow, that’s not what I expected to happen."

    hide goro_autumn
    hide goro talk3
    show goro2_autumn at p6_5
    show goro2 talk1 at p6_5
    voice audio.goro_v_conj3a1
    g "She finally realized she had made her fair share of mistakes, in fact. I am glad she’s beginning to take accountability for her actions."

    show darius shock2 at p6_3
    voice audio.darius_v_shock1a
    d "That’s even more surprising."

    show jin sad3 at p6_4
    voice audio.jin_v_think1a1
    j "I-I guess now that we know what happened to her, all of her attitude and behavior makes sense…"

    show lloyd worry3 at p6_2
    voice audio.lloyd_v_agree2a1
    l "Yeah, it really was just her defense mechanism… "

    show darius disappoint2 at p6_3
    voice audio.darius_v_think1a1
    d "We’re not excusing the wrong things she’s done, but this really helped us understand her better."

    hide goro2_autumn
    hide goro2 talk1
    show goro_autumn at p6_5
    show goro explain2 at p6_5
    voice audio.goro_v_conj4a
    g "Either way, I’m just glad we can try and move past it. It’s possible we could get along with Emilia now after all."

    show jin worry2 at p6_4
    voice audio.jin_v_think2b1
    j "U-Umm…"

    show aiden confused2 at p6_1
    voice audio.aiden_v_greet1a
    a "What’s up, Jin?"

    show jin worry4 at p6_4
    voice audio.jin_v_conj2c1
    j "I-I’m just wondering… Does this change what happens to Ms. Emilia after all this…?"

    show darius sad2 at p6_3
    voice audio.darius_v_goro1
    d "Like Sir Goro told us earlier, there’s no doubt she’s getting fired as soon as Mr. Clermont finds out everything "

    show lloyd sad5 at p6_2
    voice audio.lloyd_v_think2a2
    l "Does that mean we won’t tell on her then…?"

    hide goro_autumn
    hide goro explain2
    show goro2_autumn at p6_5
    show goro2 sad2 at p6_5
    voice audio.goro_v_no1a1
    g "No. Mr. Clermont is our sponsor, and he deserves to know the truth at some point."
    g "If he found out later that we’d been hiding such a thing from him, I’m sure it would be much worse."

    hide goro2_autumn
    hide goro2 sad2
    show goro_autumn at p6_5
    show goro worry3 at p6_5
    voice audio.goro_v_but1a
    g "But l believe we can all agree that can wait for a while, to buy some time and allow Emilia to recover."

    show yoshi talk1 at p6_6
    voice audio.yoshi_v_yes1
    yo "Yes, that is our priority right now."

    hide aiden_autumn
    hide aiden confused2
    show aiden2_autumn at p6_1
    show aiden2 sad5 at p6_1
    voice audio.aiden_v_but1a1
    a "But I get what Jin is saying… Whether we wait or not, it doesn’t change the fact that she’d have nowhere to go."
    a "She’d be left out to dry… again. "

    show jin sad1 at p6_4
    show lloyd upset1 at p6_2
    show darius worry1 at p6_3
    show aiden2 upset1 at p6_1
    hide goro_autumn
    hide goro worry3
    show goro2_autumn at p6_5
    show goro2 sad1 at p6_5
    hide yoshi_autumn
    hide yoshi talk1
    show yoshi2_autumn at p6_6
    show yoshi2 sad1 at p6_6
    all "..."

    hide yoshi2_autumn
    hide yoshi2 sad1
    show yoshi_autumn at p6_6
    show yoshi think2 at p6_6
    voice audio.yoshi_v_well1
    yo "Well… What if we let her stay?"

    show goro2 confused2 at p6_5
    voice audio.goro_v_question2a1
    g "What do you mean, Yoshinori?"

    show yoshi talk2 at p6_6
    voice audio.yoshi_v_confident2
    yo "We’re taking care of her until she gets back on her feet, but I think there’s more we can do to help."
    yo "Hear me out on this… I know her true credentials don’t fit her original position, but maybe we can find something for her to work on."

    show yoshi talk1 at p6_6
    voice audio.yoshi_v_think1a
    yo "She doesn’t have to be a scoutmaster to be able to help the camp out."

    show lloyd sigh4 at p6_2
    voice audio.lloyd_v_agree2c1
    l "Yeah… Whether we like it or not, she filled the role of inspector despite not being qualified for the job."

    show darius think2 at p6_3
    voice audio.darius_v_agree2a
    d "We reached our initial target working with her."

    show goro2 think1 at p6_5
    voice audio.goro_v_think1a1
    g "Hmm… Clearly, our camp is understaffed. And every little bit of help counts at this point."

    show jin thinkdn2 at p6_4
    voice audio.jin_v_conj3b1
    j "A-And taking into account that she’s had a change of heart, that would solve the one problem we had with her… "

    show yoshi think3 at p6_6
    voice audio.yoshi_v_anyway1a
    yo "It’s not up for just me to decide, though…"

    show aiden2 sad5 at p6_1
    voice audio.aiden_v_unsure5b1
    a "Yeah… But I kinda get what you’re saying, Yoshi."

    show darius talk2 at p6_3
    voice audio.darius_v_conj2a
    d "We’re not even sure if Emilia would want that. "

    show lloyd think5 at p6_2
    voice audio.lloyd_v_think1a1
    l "But we’d at least have a way to help if things don’t work out for her."

    show yoshi talk2 at p6_6
    voice audio.yoshi_v_right1
    yo "Exactly."

    hide goro2_autumn
    hide goro2 think1
    show goro_autumn at p6_5
    show goro talk3 at p6_5
    voice audio.goro_v_agree7a
    g "So it seems we’re all willing to give Emilia another chance."
    g "I’ll make sure to consider what everyone has said."

    show goro explain2 at p6_5
    voice audio.goro_v_conj5a
    g "Regardless, I’ll have to report to Mr. Clermont on both the camp’s situation and Emilia being sick."

    show yoshi talk1 at p6_6
    voice audio.yoshi_v_agree1a
    yo "Of course, Goro. That makes sense."

    show goro happy1 at p6_5
    voice audio.goro_v_conj4a
    g "Either way, I’m impressed, Yoshinori. Every day you’re becoming more of a leader."
    g "I’ve said it before, but you’ll do a fine job leading this place one day."

    show aiden2 confused3 at p6_1
    voice audio.aiden_v_sheesh1a
    a "Sheesh Gramps, do we need to get your memory checked? I think you’ve said that line every day the past few months!"

    hide goro_autumn
    hide goro happy1
    show goro2_autumn at p6_5
    show goro2 explain1 at p6_5
    voice audio.goro_v_ehem1a
    g "*ehem* I-I just thought it was appropriate to give proper praise."

    show yoshi comp6 at p6_6
    voice audio.yoshi_v_thanks3
    yo "Th-Thank you, Goro…"

    show aiden2 tired5 at p6_1
    voice audio.aiden_v_anyway1a
    a "Anyway, I dunno about you guys but I’m beat! Today has been crazy draining!"

    hide aiden2_autumn
    hide aiden2 tired5
    show aiden_autumn at p6_1
    show aiden sigh1 at p6_1
    voice audio.aiden_v_relief1a1
    a "There’s so much drama on top of being exhausted from shoveling all day…"

    show lloyd sigh1 at p6_2
    voice audio.lloyd_v_sigh2a
    l "Yeah… Can’t I have my chicken noodle soup in peace? I need to dispel all this tension…"

    show darius comp2 at p6_3
    voice audio.darius_v_amazed2
    d "Try my cocoa."

    show jin talk1 at p6_4
    voice audio.jin_v_conj2c1
    j "W-Well, I have my laptop here with me… And if you guys want, we could work on the journal project some more…! "
    j "Sir Goro and Yoshi always seem to have fun with me when we do that."

    show lloyd confused2 at p6_2
    voice audio.lloyd_v_confused1a1
    l "Huh? There’s a journal project?"

    show darius confused3 at p6_3
    voice audio.darius_v_confused1a
    d "Never heard of it."

    show aiden excited3 at p6_1
    voice audio.aiden_v_oh3a
    a "Oh, oh, is this that online thingie where Jin’s been posting raw pics of you and Gramps? "

    hide yoshi_autumn
    hide yoshi comp6
    show yoshi2_autumn at p6_6
    show yoshi2 shy5 at p6_6
    voice audio.yoshi_v_uh1a
    yo "Th-The way you say it…"

    show goro2 shy6 at p6_5
    voice audio.goro_v_actually1a
    g "*ehem* Actually, Yoshinori and Jin here are trying to log down all the memories in Yuri’s journal, from the camp’s first term and up until now."

    hide yoshi2_autumn
    hide yoshi2 shy5
    show yoshi_autumn at p6_6
    show yoshi happy1 at p6_6
    voice audio.yoshi_v_yeah2
    yo "Yeah! And they’re all going to appear on the website as a blog that interested scouts can read and find out what sorts of experiences they’ll have here at Camp Buddy!"

    show lloyd excited3 at p6_2
    voice audio.lloyd_v_shock1b1
    l "Oooh, that sounds exciting!"

    show darius relief2 at p6_3
    voice audio.darius_v_aww1c1
    d "Nostalgic."

    show yoshi happy2 at p6_6
    voice audio.yoshi_v_okay2
    yo "Okay, great! Let’s get started!"

    # JMA4
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
    $ minigame_id = 'jmG5'
    $ renpy.call(minigame_id)

label day6_goro_postmg:

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

    $ location = location_office
    $ day = "??"
    $ time = timeline_timeday
    $ season = season_summer
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_office_past_day with fade
    play music old_familiar_home loop
    play bgsound sfxloop_birds loop

    play sound sfx_doorknock
    $ renpy.pause (1.0, hard=True)
    show yyoshi_camp at right
    show yyoshi happy1 at right
    voice audio.yyoshi_v_goodam2
    yo "Good morning, sir! "
    yo "I brought you your morning coffee before we started work today! I figured-"

    show yyoshi_camp at center
    show yyoshi confused2 at center
    with move

    voice audio.yyoshi_v_huh1
    yo "Huh? "

    show yyoshi think5 at center
    voice audio.yyoshi_v_think1b
    yo "Hmmm… That’s odd. Sir Goro is always awake this time of day. I wonder if he overslept?"

    show yyoshi play2 at center
    voice audio.yyoshi_v_laugh1
    yo "Hehe… Maybe I can catch him snoring… Yuri always mentions he’s a heavy sleeper."

    show yyoshi_camp at left
    show yyoshi shock2 at left
    with move

    voice audio.yyoshi_v_oh2
    yo "Oh! His door is even unlocked."

    play sound sfx_thud
    show yyoshi confused2 at left
    voice audio.yyoshi_v_huh1
    yo "Huh?"

    jump day6_goro_mg3

label day6_goro_aftersx:
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
    $ day = "81"
    $ time = timeline_timenight
    $ season = season_winter
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_campgrounds_past_day with fade
    play music old_familiar_home loop
    play bgsound sfxloop_birds loop

    show yyoshi_camp at center
    show yyoshi tired3 at center
    voice audio.yyoshi_v_pant1
    yo "*huff* *huff* I-I can’t believe I did that…"
    yo "My shirt is all sticky too… I didn’t have a chance to-"

    show yyoshi panic4 at center
    voice audio.yyoshi_v_oops1
    yo "Oh no! I-It got all over the door!"
    yo "I have to go back there and clean it quick-"

    show yyoshi_camp at left2
    show yyoshi panic1 at left2
    with move

    show ygoro_sleep at right2
    show ygoro talk2 at right2
    with dissolve

    voice audio.ygoro_v_yoshi2
    g "Yoshinori!"

    show yyoshi_blush1 at left2
    show yyoshi panic4 at left2
    voice audio.yyoshi_v_shock3
    yo "GAH! Sir Goro!"

    show ygoro confused2 at right2
    voice audio.ygoro_v_think1a1
    g "W-Were you just in my office…?"

    show yyoshi panic2 at left2
    voice audio.yyoshi_v_no4
    yo "N-No sir! Not at all! I-I was just heading to get you for our chores…"

    show ygoro think2 at right2
    voice audio.ygoro_v_unsure1b1
    g "Are you sure…? I swear I heard-"

    show yyoshi scared3 at left2
    voice audio.yyoshi_v_no5
    yo "NO! I just got here!"

    show ygoro confused3 at right2
    g "..."

    show ygoro confused2 at right2
    voice audio.ygoro_v_think2a1
    g "What’s that on your…?"

    show yyoshi awkward4 at left2
    voice audio.yyoshi_v_oh2
    yo "OH! I just remembered, I promised Aiden I’d help him in the garden this morning!  "
    yo "Sorry sir, I’ll come back again- I mean, I gotta go!"

    hide yyoshi_camp
    hide yyoshi_blush1
    hide yyoshi awkward4
    with moveoutleft

    show ygoro awkward3 at right2
    voice audio.ygoro_v_wait2b1
    g "Wait, Yoshinori…!"

    show ygoro awkward1 at right2
    g "..."

    show ygoro think1 at right2
    voice audio.ygoro_v_think1a1
    g "Hmmm… Maybe I’m just imagining things, but…"

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

label day6_goro_postfb:
    $ location = location_messhall
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_messhall_winter_night with fade
    play music ready_for_tomorrow_winter loop

    show goro2_autumn at p6_5
    show goro2 shy1 at p6_5
    show lloyd_winter at p6_2
    show lloyd annoy2 at p6_2
    show darius_winter at p6_3
    show darius play1 at p6_3
    show jin2_autumn at p6_4
    show jin2_blush at p6_4
    show jin2_nosebleed at p6_4
    show jin2_glasses at p6_4
    show jin2 dizzy2 at p6_4
    show aiden_autumn at p6_1
    show aiden play1 at p6_1
    show yoshi2_autumn at p6_6
    show yoshi2 shy3 at p6_6
    voice audio.lloyd_v_wait1b1
    l "Waiiiit… Is that why you came back to the room in a panic that day?!"

    show darius play2 at p6_3
    voice audio.darius_v_laugh1
    d "You hopped in the shower before any of us could question you."

    show aiden laugh3 at p6_1
    voice audio.aiden_v_laugh2a1
    a "Hahaha! I can’t believe you spied on Gramps like that, Yoshi!"

    show yoshi2 awkward4 at p6_6
    voice audio.yoshi_v_guys3
    yo "G-Guys, that sounds a lot worse than it was…"

    show jin2 scheme2 at p6_4
    voice audio.jin_v_really3a
    j "S-So all I had to do this whole time was sneak up on Sir Goro while he’s sleeping…"

    show goro2 annoy2 at p6_5
    voice audio.goro_v_ehem1a
    g "*ehem* Don’t get carried away, Jin."

    show jin2 perv5 at p6_4
    voice audio.jin_v_fudan1a1
    j "To think that Yoshi was brave enough to spy like that too… How unexpected."

    show aiden tease1 at p6_1
    voice audio.aiden_v_yoshi13a
    a "So, who else have you been snooping on, Yoshi~? Been spying on my buns while I’m not looking~?"

    hide yoshi2_autumn
    hide yoshi2 awkward4
    show yoshi_autumn at p6_6
    show yoshi awkward3 at p6_6
    voice audio.yoshi_v_rush5
    yo "I-I’m sure Jin has enough story for now, so let’s go to bed!"

    show lloyd tease2 at p6_2
    voice audio.lloyd_v_laugh1a1
    l "Don’t forget to put your blankets on, guys. Or Yoshi might sneak a peek~"

    show darius tease4 at p6_3
    voice audio.darius_v_naughty1a
    d "Peeping Tom. "

    show yoshi_blush1 at p6_6
    show yoshi panic3 at p6_6
    voice audio.yoshi_v_shock4
    yo "G-Gah! Come on, guys! That’s enough!"

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
    jump day7_goro
