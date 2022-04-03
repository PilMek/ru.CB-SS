label day6_aiden:
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

    show yoshi2_winter at left2
    show yoshi2 norm1 at left2
    show aiden_winter at right2
    show aiden happy1 at right2
    voice audio.aiden_v_alright1a1
    a "Alright, we’re really going home today!"
    a "I know I’ve said this like a thousand times already, but I’m so ready to be back at the camp!"

    show yoshi2 talk2 at left2
    voice audio.yoshi_v_excited1
    yo "Yeah, it looks like the sky is clear, and I can see cars moving around outside so everything must’ve been resolved."

    show aiden relief4 at right2
    voice audio.aiden_v_excited1a
    a "Believe it or not, I’m excited to get back to work too! I’ll be sure to cook up something nice as soon as we arrive! "
    a "Who knows, maybe I’ll try and recreate the stuff that we had in that fancy dinner!"

    show yoshi2 think2 at left2
    voice audio.yoshi_v_sure3
    yo "Sure, that sounds exciting, Aiden."

    hide aiden_winter
    hide aiden relief4
    show aiden2_winter at right2
    show aiden2 worry2 at right2
    voice audio.aiden_v_sheesh1a
    a "Sheesh… You don’t sound that excited, Yoshi. "

    show yoshi2 worry2 at left2
    voice audio.yoshi_v_ah2
    yo "Ah… I’m sorry. I kinda had trouble sleeping thinking about what happened yesterday with Emilia."
    yo "There were a couple of times I wanted to get up and check on her. "

    show yoshi2 sad4 at left2
    voice audio.yoshi_v_sigh3a
    yo "I really think the way I brought everything up with her just went wrong. "

    show aiden2 awkward5 at right2
    voice audio.aiden_v_confused1c2
    a "Ehhh… Come on, Yoshi. Don’t beat yourself up so much about it!"
    a "You had good intentions, and it’s not your fault if Emilia can’t see that."

    show aiden2 awkward6 at right2
    voice audio.aiden_v_unsure1b
    a "Although I guess it’s gonna be an awkward trip back home… if she even wants to come with us."

    show yoshi2 upset1 at left2
    yo "..."

    show yoshi2_winter at p5_1
    show yoshi2 upset1 at p5_1
    show aiden2_winter at p5_2
    show aiden2 awkward6 at p5_2
    with move

    show darius_winter at p5_4
    show darius happy1 at p5_4
    show jin_winter at p5_5
    show jin_glasses at p5_5
    show jin sigh3 at p5_5
    show lloyd_winter at p5_3
    show lloyd happy1 at p5_3
    with dissolve

    hide yoshi2_winter
    hide yoshi2 upset1
    show yoshi2_winter at p5_1
    show yoshi2 upset1 at p5_1
    voice audio.lloyd_v_relief2a1
    l "Hey, guys, good morning! For real, this time!"

    show darius happy1 at p5_4
    voice audio.darius_v_agree2a
    d "It’s pretty sunny outside. Almost like the blizzard didn’t happen."

    show jin sigh3 at p5_5
    voice audio.jin_v_relief1a1
    j "I’m just glad we can finally go home now…  "

    show yoshi2_winter at p7_3
    show yoshi2 upset1 at p7_3
    show aiden2_winter at p7_4
    show aiden2 awkward6 at p7_4
    show lloyd_winter at p7_5
    show lloyd happy1 at p7_5
    show darius_winter at p7_6
    show darius happy1 at p7_6
    show jin_winter at p7_7
    show jin_glasses at p7_7
    show jin sigh3 at p7_7
    with move

    show goro_winter at p7_2
    show goro talk1 at p7_2
    show yuri_winter at p7_1
    show yuri norm1 at p7_1
    with dissolve

    voice audio.goro_v_goodam1a1
    g "Ah, it looks like you’re all ready to go. The workers are gathered as well and the shuttle should arrive in a few minutes."

    show yuri serious4 at p7_1
    voice audio.yuri_v_wait1c1
    yu "W-Wait! Emilia’s not here yet!"

    show goro confused2 at p7_2
    voice audio.goro_v_confused1a1
    g "I sent everyone a message to make sure they are prepared to go, including Emilia…"

    show jin talk2 at p7_7
    voice audio.jin_v_yeah1a
    j "Yeah, we saw it and came down right away…"

    hide aiden2_winter
    hide aiden2 awkward6
    show aiden_winter at p7_4
    show aiden worry5 at p7_4
    voice audio.aiden_v_wait1a1
    a "Wait, Yoshi... You told me last night Emilia wanted to quit… Do you think she was serious about that…?"

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

    hide goro_winter
    hide goro confused2
    show goro2_winter at p7_2
    show goro2 sigh2 at p7_2
    voice audio.goro_v_sigh1a
    g "*sigh* I’ve been hearing her go on about this all morning…"
    g "I thought we could at least wait to get back to camp before we talked about this…"

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
    voice audio.yoshi_v_well3
    yo "W-Well… She did at first. But since we had enough proof, she had no choice but to admit to everything…"

    show yoshi2 sad6 at p7_3
    yo "She was really caught off guard that we found out about her secret, though… that really pushed her over her limit…"

    show jin scared2 at p7_7
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

    hide goro2_winter
    hide goro2 sigh2
    show goro_winter at p7_2
    show goro talk1 at p7_2
    hide yuri_winter
    hide yuri angry6
    show yuri_winter at p7_1
    show yuri angry6 at p7_1
    voice audio.goro_v_conj5a
    g "Regardless, if she really is planning on quitting, that must be settled back at camp."

    hide aiden_winter
    hide aiden worry5
    show aiden2_winter at p7_4
    show aiden2 talk1 at p7_4
    hide yoshi2_winter
    hide yoshi2 sigh1
    show yoshi2_winter at p7_3
    show yoshi2 sigh1 at p7_3
    voice audio.aiden_v_yeah1a1
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
    play music heracleum_musicbox_a

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

    hide aiden2_winter
    hide aiden2 worry1
    show aiden_winter at p7_6
    show aiden talk5 at p7_6
    voice audio.aiden_v_confident1a
    a "Leave that to me, doc! I’ll keep an eye on her!"
    ol "I hear you’re all scheduled to leave today. There’s no need to admit her to a hospital right now."
    ol "She should be able to handle your trip back. Our shuttle’s seats can be laid back so she can properly rest."

    show goro worry3 at p7_7
    voice audio.goro_v_thanks1b1
    g "Thanks for the help, doctor. "
    ol "Alright. I’ll leave Ms. Komarova in your care now. Please take care of her."

    hide aiden_winter
    hide aiden talk5
    show aiden2_winter at p7_6
    show aiden2 worry5 at p7_6
    hide yoshi2_winter
    hide yoshi2 sad4
    show yoshi2_winter at p7_5
    show yoshi2 sad4 at p7_5
    hide yuri_winter
    hide yuri sigh3
    show yuri_winter at p7_4
    show yuri sigh3 at p7_4
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
    show aiden2 sad4 at p7_6
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

    hide aiden2 sad1
    hide yoshi2 sad1

    show jin sad2 at p7_1
    show darius talk1 at p7_2
    show lloyd talk2 at p7_3
    show aiden2 talk1 at p7_6
    show yoshi2 worry2 at p7_5
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

    show aiden talk2 at p4_2
    voice audio.aiden_v_yuri2a
    a "I’ll take her from here, Yuri! "

    hide aiden_winter2
    hide aiden talk2
    with moveoutleft

    show yuri serious4 at p4_1
    voice audio.yuri_v_alright1c1
    yu "Alright, I’ll go and heat up all of our cabins!"

    show yuri_winter2 at p4_2
    show yuri serious4 at p4_2
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

    voice audio.lloyd_v_shock2a1
    l "Oh no!! This isn’t looking good, Dar! We have to check on the site!"

    show darius worry3 at p4_2
    voice audio.darius_v_unsure1a
    d "Cross your fingers."

    hide lloyd_winter2
    hide lloyd shock3
    hide darius_winter2
    hide darius worry3
    with dissolve

    show yoshi worry2 at p4_3
    voice audio.yoshi_v_think1a
    yo "It looks like Lloyd and Darius are in a rush to check the expansion site."

    show goro2 sigh1 at p4_4
    voice audio.goro_v_think1a1
    g "I have a bad feeling the blizzard has something to do with it. Let’s catch up with them."

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

    show lloyd_winter2 at left2
    show lloyd panic3 at left2
    show darius_winter2 at right2
    show darius panic1 at right2
    voice audio.lloyd_v_swear1b1
    l "Noooooo!!!! It’s worse than I expected! Everything is buried in snow…!!"

    show darius disappoint5 at right2
    voice audio.darius_v_ugh1
    d "This is bad…"

    show lloyd_winter2 at p4_1
    show lloyd panic3 at p4_1
    show darius_winter2 at p4_2
    show darius panic1 at p4_2
    with move

    show yoshi_winter2 at p4_3
    show yoshi talk1 at p4_3
    show goro_winter2 at p4_4
    show goro norm3 at p4_4
    with dissolve

    voice audio.yoshi_v_worry3a
    yo "Is everything alright h—"

    show yoshi shock6 at p4_3
    voice audio.yoshi_v_shock1a
    yo "WHOA!" with vpunch

    hide goro_winter2
    hide goro norm3
    show goro2_winter2 at p4_4
    show goro2 disappoint5 at p4_4
    voice audio.goro_v_annoyed1a1
    g "Tsk… I knew it…"

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

    show goro2 sad2 at p4_4
    voice audio.goro_v_actually1b
    g "This was actually what I was afraid of when we were scheduling work around the winter time…"
    g "While snowstorms happen here at least once a year, this year’s was an extreme exception."

    hide goro2_winter2
    hide goro2 sad2
    show goro_winter2 at p4_4
    show goro sigh1 at p4_4
    voice audio.goro_v_glad1b
    g "Thankfully, we were away from camp when this happened. It would’ve been really dangerous for everyone."

    show lloyd sad4 at p4_1
    voice audio.lloyd_v_agree2c3
    l "Yeah… Despite these damages, it was the right call for us to a take that break. "

    show yoshi worry2 at p4_3
    voice audio.yoshi_v_unsure2a
    yo "Does that mean we’ll have to wait until spring to resume work?"

    show lloyd upset3 at p4_1
    voice audio.lloyd_v_disagree1a2
    l "No, unfortunately. Waiting that long and letting these damages endure the cold would only make it worse. "

    show darius sad2 at p4_2
    voice audio.darius_v_agree1b
    d "Yes. Without further weatherproofing, the materials will deteriorate at a rapid rate until they’re unsalvageable."

    hide goro_winter2
    hide goro sigh1
    show goro2_winter2 at p4_4
    show goro2 sigh4 at p4_4
    voice audio.goro_v_sigh1a
    g "Something like that would make us miss our targeted deadline for sure…"

    show lloyd sigh1 at p4_1
    voice audio.lloyd_v_sorry1b2
    l "*sigh* I’m really sorry… This is my department… I should’ve taken more precautions…"
    l "I didn’t consider that there would be a freak snowstorm we’d be dealing with…"

    hide goro2_winter2
    hide goro2 sigh4
    show goro_winter2 at p4_4
    show goro talk1 at p4_4
    voice audio.goro_v_alright2c1
    g "This isn’t anyone’s fault. None of us could’ve anticipated a storm like this."

    show lloyd worry2 at p4_1
    voice audio.lloyd_v_sigh2a
    l "But still… If only I had more experience working with site conditions like this, we would’ve been able to prevent it…"

    show darius sad3 at p4_2
    voice audio.darius_v_comp3a
    d "You did what you could. Let’s just get to work and do what we can to fix this."

    show yoshi awkward4 at p4_3
    voice audio.yoshi_v_wait4
    yo "Wait… You two aren’t planning on working right now, are you?"

    show darius talk2 at p4_2
    voice audio.darius_v_conj2a
    d "We have to at least clear the snow away from the paths and structures so we can assess the damages."

    show lloyd sad1 at p4_1
    voice audio.lloyd_v_agree2a2
    l "Yeah, we can’t really plan out the repairs without getting a clearer view."

    hide goro_winter2
    hide goro talk1
    show goro2_winter2 at p4_4
    show goro2 think1 at p4_4
    voice audio.goro_v_think1a1
    g "Hmm… The weather forecast did say the next couple days would be a lot clearer.  So, it’s not entirely impossible to work, as long as safety measures are taken."

    show lloyd talk2 at p4_1
    voice audio.lloyd_v_comp1b3
    l "You guys don’t have to worry, though! We’re just gonna shovel some snow away! "

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
    hide goro2_winter2
    hide goro2 think1
    show goro_winter2 at p4_4
    show goro talk1 at p4_4
    voice audio.goro_v_agree7a
    g "I will help as well."

    show lloyd excited2 at p4_1
    voice audio.lloyd_v_sir3a
    l "You too, sir…? Are you guys sure?!"

    show goro happy1 at p4_4
    voice audio.goro_v_agree3a1
    g "Of course. We do this every year anyway."

    show yoshi comp2 at p4_3
    voice audio.yoshi_v_well1
    yo "It looks like all the snow is still loose, so it shouldn’t be too hard to manually pile it up elsewhere."

    show darius think5 at p4_2
    voice audio.darius_v_think1a2
    d "I estimate with the four of us… we could clear at least the important parts of the site by the day the workers return."

    show lloyd excited3 at p4_1
    voice audio.lloyd_v_praise2c
    l "That’s good enough! Better than waiting for ice to melt!"

    show goro talk3 at p4_4
    voice audio.goro_v_alright1b2
    g "Alright then. Since Ms. Komarova is out of commission for the moment, I’ll take over and personally report the situation to Mr. Clermont first."
    g "Due to the circumstances, we have to take matters into our own hands and do as much as we can to get back on track."

    show lloyd bold2 at p4_1
    show darius talk1 at p4_2
    show yoshi talk1 at p4_3
    all "Yes, sir!"

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
    show yoshi talk1 at left2
    show goro_winter2 at right2
    show goro talk3 at right2
    with move

    show goro sigh1 at right2
    voice audio.goro_v_confused1a1
    g "This whole endeavor is really testing us, don’t you think?"

    hide yoshi_winter2
    hide yoshi talk1
    show yoshi2_winter2 at left2
    show yoshi2 sigh4 at left2
    voice audio.yoshi_v_yeah4
    yo "Yeah… The problems just keep piling on top of each other."

    hide goro_winter2
    hide goro sigh1
    show goro2_winter2 at right2
    show goro2 confused6 at right2
    voice audio.goro_v_think1a1
    g "It will be very complicated to explain everything to Mr. Clermont."
    g "He made us go on that trip hoping to improve our relationship with Ms. Komarova, and we know how that went…"

    show goro2 sigh4 at right2
    voice audio.goro_v_sigh1a
    g "And now, the first thing he’ll hear from us is another setback on the project."

    hide yoshi2_winter2
    hide yoshi2 sigh4
    show yoshi_winter2 at left2
    show yoshi comp2 at left2
    voice audio.yoshi_v_comp4
    yo "Don’t worry, sir. We’ve overcome so many challenges before, and this won’t be any different."

    hide goro2_winter2
    hide goro2 sigh4
    show goro_winter2 at right2
    show goro talk1 at right2
    voice audio.goro_v_agree6a2
    g "You’re right, Yoshinori. Predicaments were bound to happen the moment we decided to accept the sponsorship."

    show yoshi comp6 at left2
    voice audio.yoshi_v_sir1
    yo "I’m sure it’ll all be worth in the end, sir!"

    show goro talk3 at right2
    voice audio.goro_v_agree7a
    g "I think so too."
    g "The best we can do for now is keep things under control and regain our momentum one step at a time."

    show goro explain2 at right2
    voice audio.goro_v_think1a1
    g "As for Ms. Komarova, I believe we’ve all agreed to focus on her recovery before we address her situation with Mr. Clermont."

    show yoshi comp2 at left2
    voice audio.yoshi_v_comp2
    yo "I’m sure with Aiden taking care of her, she’ll get well in no time."

    show goro talk1 at right2
    voice audio.goro_v_actually1a
    g "It actually surprised me that Aiden, out of all people, would take it upon himself to watch over Emilia."
    g "Especially after how she mistreated him at the hotel… Or over the entire project, for that matter."

    show yoshi comp1 at left2
    voice audio.yoshi_v_aiden4
    yo "Aiden has always been a kind and caring person. I’ve never seen him stay angry or hold grudges."

    show goro comp2 at right2
    voice audio.goro_v_amazed1a1
    g "He’s a good sport, you know. Very steadfast and perseverant no matter what’s thrown at him."
    g "But I was surprised, even after all these years, I’ve never seen him open up and trust everyone with his feelings like he did back at the hotel.   "

    show goro comp3 at right2
    voice audio.goro_v_heh1a
    g "And I think you’ve played a huge part in that regard."

    show yoshi awkward4 at left2
    voice audio.yoshi_v_what3
    yo "Wh-What…? Me?"

    show goro happy2 at right2
    voice audio.goro_v_agree1a1
    g "Yes. This has been something I’ve been wanting to talk to you about, but never had the chance to."
    g "The impact you have on Aiden is what’s led him to become the great man he is today."

    show goro relief2 at right2
    voice audio.goro_v_conj3a1
    g "I was there from that very first term when you two became close friends – it was something I’ve always observed and admired."
    g "Aiden comes from a very different background, and you welcomed him with open arms, always making sure he felt included."

    hide yoshi_winter2
    hide yoshi awkward4
    show yoshi2_winter2 at left2
    show yoshi2 talk3 at left2
    voice audio.yoshi_v_sir4
    yo "I-I didn’t know you were watching over us like that, sir…"

    hide goro_winter2
    hide goro relief2
    show goro2_winter2 at right2
    show goro2 explain3 at right2
    voice audio.goro_v_ehem1a
    g "*ehem* D-Don’t get me wrong. I was your scoutmaster then and it was my duty to do so."

    show yoshi2 comp6 at left2
    voice audio.yoshi_v_laugh6
    yo "Ahehe…"

    hide goro2_winter2
    hide goro2 explain3
    show goro_winter2 at right2
    show goro happy1 at right2
    voice audio.goro_v_but1a
    g "But even so, after we were all separated and then reunited, we’ve all been so carried away with our responsibilities these past few years."
    g "It was as if those times from the past froze, and never thawed until recently."

    show goro comp2 at right2
    voice audio.goro_v_laugh2a
    g "Despite all of us being so busy working on this project, I could see from Aiden’s eyes that he was having the time of his life."
    g "Call it sappy, but the way Aiden smiles whenever he’s with you is truly something special."

    show yoshi2 shy3 at left2
    voice audio.yoshi_v_ah2
    yo "Ah…"

    show goro comp3 at right2
    voice audio.goro_v_glad1a
    g "You two finally grew a deeper bond. Something more than what you two had back then."

    $working = False
    $shuffle_menu()
    menu():
        g "You two finally grew a deeper bond. Something more than what you two had back then.{fast}"
        "We have room for one more.":
            $ working = True
            $ score_goro += 5
            $ score_aiden -= 5
            hide yoshi2_winter2
            hide yoshi2 shy3
            show yoshi_winter2 at left2
            show yoshi play3 at left2
            voice audio.yoshi_v_well1
            yo "Well, we have room for one more, sir!"

            show goro laugh5 at right2
            voice audio.goro_v_laugh2a
            g "HAHAHA!"
            g "You youngsters really like to blur the lines, don’t you?"

            show yoshi laugh2 at left2
            voice audio.yoshi_v_laugh1
            yo "Haha…! I was just joking, sir!"
            yo "I guess Aiden has started to rub off on me!"

            show goro talk1 at right2
            voice audio.goro_v_anyway2
            g "Anyway, it’s not my business to pry."
            g "Let’s just get to work, shall we?"
        "You're just seeing things.":
            $ working = True
            $ score_aiden -= 2
            show yoshi2 awkward3 at left2
            voice audio.yoshi_v_no5
            yo "Y-You’re just seeing things, sir…!"

            hide goro_winter2
            hide goro comp3
            show goro2_winter2 at right2
            show goro2 sigh1 at right2
            voice audio.goro_v_sigh1a
            g "*sigh* Yoshinori, at my age and experience, I know what a relationship looks like."

            hide goro2_winter2
            hide goro2 sigh1
            show goro_winter2 at right2
            show goro talk1 at right2
            voice audio.goro_v_anyway2
            g "Anyway, it’s not my business to pry."
            g "Let’s just get to work, shall we?"
        "I won't deny it.":
            $ working = True
            $ score_aiden += 1
            show yoshi2 sigh1 at left2
            voice audio.yoshi_v_but2
            yo "I don’t know what to say, sir… but I won’t deny it."

            hide goro_winter2
            hide goro comp3
            show goro2_winter2 at right2
            show goro2 sigh1 at right2
            voice audio.goro_v_sigh1a
            g "Yoshinori, at my age, I know what a relationship looks like."

            show yoshi2 comp6 at left2
            voice audio.yoshi_v_laugh6
            yo "Ahehe…"

            show goro2 tease2 at right2
            voice audio.goro_v_heh1a
            g "Heh, Yuri will go nuts once she finds out."

            show yoshi2 comp3 at left2
            voice audio.yoshi_v_actually1a
            yo "I-I’m sure she already knows… In fact, she probably would have been first one to notice."

            hide goro2_winter2
            hide goro2 tease2
            show goro_winter2 at right2
            show goro laugh2 at right2
            voice audio.goro_v_laugh2a
            g "Hahaha! It’s about time! I was getting worried I was going to die before you confessed!"

            hide yoshi2_winter2
            hide yoshi2 comp3
            show yoshi_winter2 at left2
            show yoshi shock2 at left2
            voice audio.yoshi_v_ah4
            yo "A-Ah…! "

            show goro play3 at right2
            voice audio.goro_v_comp4a
            g "You may be close to your thirties, but you still have a long way to go with this kind of stuff, late-bloomer!"

            hide yoshi_winter2
            hide yoshi shock2
            show yoshi2_winter2 at left2
            show yoshi2 sigh4 at left2
            voice audio.yoshi_v_sigh3a
            yo "*sigh* "
        "We're together now.":
            $ working = True
            $ score_aiden += 2
            show yoshi2 sigh1 at left2
            voice audio.yoshi_v_sir3
            yo "It’s embarrassing that we were that noticeable, sir."

            hide goro_winter2
            hide goro comp3
            show goro2_winter2 at right2
            show goro2 sigh1 at right2
            voice audio.goro_v_sigh1a
            g "Took you both ages to make it official. *sigh* Youngsters these days…"

            show yoshi2 comp6 at left2
            voice audio.yoshi_v_laugh6
            yo "Ahehe…"

            show goro2 tease2 at right2
            voice audio.goro_v_heh1a
            g "Heh, Yuri will go nuts once she finds out."

            show yoshi2 comp3 at left2
            voice audio.yoshi_v_actually1a
            yo "I-I’m sure she already knows… In fact, she probably would have been first one to notice."

            hide goro2_winter2
            hide goro2 tease2
            show goro_winter2 at right2
            show goro laugh2 at right2
            voice audio.goro_v_laugh2a
            g "Hahaha! It’s about time! I was getting worried I was going to die before you confessed!"

            hide yoshi2_winter2
            hide yoshi2 comp3
            show yoshi_winter2 at left2
            show yoshi shock2 at left2
            voice audio.yoshi_v_ah4
            yo "A-Ah…! "

            show goro play3 at right2
            voice audio.goro_v_comp4a
            g "You may be close to your thirties, but you still have a long way to go with this kind of stuff, late-bloomer!"

            hide yoshi_winter2
            hide yoshi shock2
            show yoshi2_winter2 at left2
            show yoshi2 sigh4 at left2
            voice audio.yoshi_v_sigh3a
            yo "*sigh* "

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black with fade
    yo "{i}After Sir Goro and I talked, he headed off to the office to report to Mr. Clermont, while I got started shoveling with Lloyd and Darius.{/i}"

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
    play music buddy_oath_aiden_sad loop

    show emilia_sleep at center
    show emilia sleepy4 at center
    voice audio.emilia_v_ugh2
    e "Nnn…"

    show emilia confused2 at center
    voice audio.emilia_v_think1
    e "H-Huh…? "

    show emilia shock2 at center
    voice audio.emilia_v_gasp1
    e "*gasp* Wh-Where am I?"

    show emilia_sleep at left2
    show emilia shock2 at left2
    with move

    show aiden_autumn at right2
    show aiden talk4 at right2
    with dissolve

    voice audio.aiden_v_emilia4a
    a "Oh, you’re finally awake, Emilia…! We’re back at camp!"

    show emilia awkward1 at left2
    e "..."

    hide aiden_autumn
    hide aiden talk4
    show aiden2_autumn at right2
    show aiden2 worry2 at right2
    voice audio.aiden_v_hey1e1
    a "H-How are you feeling?"

    show emilia upset4 at left2
    e "..."

    show emilia sad2 at left2
    voice audio.emilia_v_question1a
    e "H-Have you… been taking care of me?"

    show aiden2 awkward5 at right2
    voice audio.aiden_v_yeah1g1
    a "Y-Yeah, kinda… "

    show emilia upset5 at left2
    e "..."

    hide aiden2_autumn
    hide aiden2 awkward5
    show aiden_autumn at right2
    show aiden worry5 at right2
    voice audio.aiden_v_glad1a
    a "You gave us quite the scare back there… Good thing Yoshi found you… "

    show emilia sad2 at left2
    voice audio.emilia_v_oh4b
    e "I see…"

    show aiden comp2 at right2
    voice audio.aiden_v_well1c1
    a "W-Well, we’re home now! Everyone’s been worried about you, you know…"

    show emilia panic3 at left2
    voice audio.emilia_v_wait1b3
    e "Everyone…? But I was— Wait…"
    e "N-No! I… I shouldn’t be here anymore…! "

    show emilia_sleep at p5_1
    show emilia pain4 at p5_1
    with move

    show aiden_autumn at p5_2
    show aiden comp2 at p5_2
    with move

    voice audio.emilia_v_ugh1
    e "U-Ugh…! "

    show aiden panic2 at p5_2
    voice audio.aiden_v_shock1a1
    a "W-Whoa! Take it easy, Emilia…! You’re not well yet!"
    a "Here, I made you some soup. You haven’t eaten anything the whole day, and you need this before you take your medicine."

    show emilia_sleep at left2
    show emilia upset2 at left2
    show aiden_autumn at right2
    show aiden comp2 at right2
    with move

    voice audio.emilia_v_question1b1
    e "Wh-Why are you doing this…? "

    show aiden confused2 at right2
    voice audio.aiden_v_what1a
    a "Doing what? "

    show emilia upset6 at left2
    voice audio.emilia_v_think1
    e "Being nice to me. After everything I did…"

    show aiden comp3 at right2
    voice audio.aiden_v_confused1a2
    a "Eh… All’s good, you can forget about it and just focus on getting better."

    show emilia upset3 at left2
    voice audio.emilia_v_disagree4a
    e "I don’t understand… How can you forgive me just like that?"

    hide aiden_autumn
    hide aiden comp3
    show aiden2_autumn at right2
    show aiden2 awkward5 at right2
    voice audio.aiden_v_well1a1
    a "Well… I don’t know the whole story from your point of view."
    a "I just thought… It’s up to me to how I take it, and I decided I don’t wanna hold anything against you."

    show emilia upset4 at left2
    e "..."

    show emilia sad2 at left2
    voice audio.emilia_v_conj4a
    e "I… really need to leave. I don’t belong here…"

    hide aiden2_autumn
    hide aiden2 awkward5
    show aiden_autumn at right2
    show aiden awkward6 at right2
    voice audio.aiden_v_so2
    a "Where will you go…?"

    show emilia sigh3 at left2
    voice audio.emilia_v_sigh1b
    e "I-It’s over for me…"

    hide aiden_autumn
    hide aiden awkward6
    show aiden2_autumn at right2
    show aiden2 sigh1 at right2
    voice audio.aiden_v_sigh1a
    a "*sigh*"

    show emilia panic3 at left2
    voice audio.emilia_v_what2
    e "Wh-What...?"

    show aiden2 sad4 at right2
    voice audio.aiden_v_think1a1
    a "I’m sure you remember back then how I had nothing too… "

    show emilia upset6 at left2
    voice audio.emilia_v_agree2c
    e "Y-Yes… "

    show aiden2 comp2 at right2
    voice audio.aiden_v_actually5a
    a "Thanks to everyone and Camp Buddy, for once I had something to hope for."

    show aiden2 sad5 at right2
    voice audio.aiden_v_but1a1
    a "But believe it or not… I still ended up in the same position as you now…"
    a "Thinking that I’d lost everything…. I was ready to give up too."

    show emilia upset3 at left2
    voice audio.emilia_v_question2b
    e "H-How did you get back up…?"

    show aiden2 upset6 at right2
    voice audio.aiden_v_i1b2
    a "I… tried to look back… to find something worth fighting for."

    show emilia upset1 at left2
    e "..."

    show aiden2 explain2 at right2
    voice audio.aiden_v_unsure1a
    a "I guess what I’m saying is that running away won’t solve anything… "
    a "I know life can really suck sometimes, but you can still make something out of it if you give it another shot…!"

    show emilia upset4 at left2
    e "..."

    hide aiden2_autumn
    hide aiden2 explain2
    show aiden_autumn at right2
    show aiden talk5 at right2
    voice audio.aiden_v_conj4a
    a "Now, eat up before this soup gets cold."

    play sound sfx_doorknock
    show emilia_sleep at p4_1
    show emilia upset4 at p4_1
    show aiden_autumn at p4_2
    show aiden talk5 at p4_2
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
    show aiden_autumn at p4_3
    show aiden talk5 at p4_3
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

    hide aiden_autumn
    hide aiden talk5
    show aiden2_autumn at p4_3
    show aiden2 worry2 at p4_3
    voice audio.aiden_v_sheesh1a
    a "Sheesh, Yuri… You’re gonna give me a heart attack… I thought you were gonna smack Emilia there for a second."

    show emilia sad2 at p4_1
    voice audio.emilia_v_conj1a
    e "I’m just feeling a little light-headed from too much sleep… But I’m fine now, really…"

    show yoshi_winter at p4_3
    show yoshi worry3 at p4_3
    show aiden2_autumn at p4_4
    show aiden2 worry2 at p4_4
    with move

    hide aiden2_autumn
    hide aiden2 worry2
    show aiden_autumn at p4_4
    show aiden talk5 at p4_4
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
    #voice audio.emilia_vs11_line1
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

    hide aiden_autumn
    hide aiden talk5
    show aiden2_autumn at p4_4
    show aiden2 scared2 at p4_4
    voice audio.aiden_v_yuri6a
    a "H-Hey, come on, Yuri! Don’t work her up too much, she’s still recovering!"

    show emilia cry3 at p4_1
    voice audio.emilia_v_aiden2
    e "*sniff* I-I owe you an apology the most, Aiden…"
    e "It was so unfair that I projected all my insecurities towards you… You didn’t deserve to be treated like that..."

    show emilia cry2 at p4_1
    voice audio.emilia_v_yoshi2
    e "Just like Yoshinori, you’ve always been kind to me, and I exploited that to feel better about myself…"
    e "Yoshinori was right to condemn me all those times he defended you, because everything I’ve been saying to and about you was just cruel and untrue…"

    show emilia cry3 at p4_1
    voice audio.emilia_v_sorry2
    e "So, I’m really sorry…"

    show aiden2 comp2 at p4_4
    voice audio.aiden_v_hey1e1
    a "H-Hey, like I told you a while ago, I’m over it!"
    a "You’ll just stress yourself out if you keep worrying about that too."

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

    hide aiden2_autumn
    hide aiden2 comp2
    show aiden_autumn at p4_4
    show aiden comp5 at p4_4
    voice audio.aiden_v_yeah1a1
    a "Yeah, I already think of everyone here as my own, you know!"

    show emilia sad1 at p4_1
    e "..."

    show emilia sad2 at p4_1
    voice audio.emilia_v_think1
    e "I really don’t deserve all this kindness…"
    e "I’ve used up all my chances and now I’m being given another one… I don’t know if I can trust myself to not make another mistake…"

    show yoshi worry2 at p4_3
    voice audio.yoshi_v_encourage1
    yo "You can’t give up now, Emilia… It’s not too late to make things right. "
    yo "There’s obviously changes that need to be made, and we can only do so much to help you."

    show yoshi explain2 at p4_3
    voice audio.yoshi_v_but2
    yo "The change has to come from you… I’m sure you’re tired of living in your old ways too."

    show emilia sad4 at p4_1
    voice audio.emilia_v_regret2b
    e "I am. I don’t want to live like that anymore."

    show yoshi talk1 at p4_3
    voice audio.yoshi_v_conj3a
    yo "You can do something about it, especially now that you have people to support you."
    yo "I know you’re a fighter, Emilia. And fighters don’t go down easily, no matter what! "

    show yoshi bold2 at p4_3
    voice audio.yoshi_v_encourage3
    yo "Just keep moving forward and never give up!"

    show yuri irked2 at p4_2
    voice audio.yuri_v_shock1b1
    yu "Oh my, here we go again… Yoshi… *facepalm*"

    hide aiden_autumn
    hide aiden comp5
    show aiden2_autumn at p4_4
    show aiden2 comp6 at p4_4
    voice audio.aiden_v_laugh1b1
    a "Ahehe…"

    hide aiden2_autumn
    hide aiden2 comp6
    show aiden_autumn at p4_4
    show aiden shock1 at p4_4
    show yuri shock1 at p4_2
    show emilia angry2 at p4_1
    voice audio.emilia_v_agree2c
    e "That’s right! I am fierce! I won’t let this keep me down!"
    e "I do want to turn my life around! And I’m not going to waste this chance!"

    show aiden shock2 at p4_4
    voice audio.aiden_v_shock1d1
    a "Whoa… I can’t believe that worked…"

    show yuri shock2 at p4_2
    voice audio.yuri_v_response2b2
    yu "Tell me about it…"

    show emilia angry3 at p4_1
    voice audio.emilia_v_comp1b
    e "I will make up for everything, mark my words! And I—"

    show aiden comp2 at p4_4
    voice audio.aiden_v_yeah1a1
    a "Alright, hold your horses, you gotta recover first!"

    show yuri comp2 at p4_2
    voice audio.yuri_v_yeah1a1
    yu "Yeah. Try and rest for now, Emilia. "
    yu "And if you need us to get you some professional help, just tell us, alright?"

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

    show yoshi happy2 at p4_3
    voice audio.yoshi_v_bye1b
    yo "Alright then! I’ll see you two tomorrow!"

    show yoshi_winter at p8_7
    show yoshi happy2 at p8_7
    show aiden_autumn at p8_8
    show aiden play2 at p8_8
    with move

    voice audio.aiden_v_laugh1b2
    a "Hehe. I guess some people don’t find your chivalrous speeches cringey, huh Yoshi?"

    show yoshi panic2 at p8_7
    voice audio.yoshi_v_hey4
    yo "H-Hey! Was it really cringey…?!"

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black with fade
    yo "{i}It seems like finally, after everything we’ve been through the last few months, we were able to have an honest talk with Emilia…{/i}"
    yo "{i}I’m so glad she opened up to us, allowing us to finally understand her side, and is willing to give it another chance…{/i}"
    $ renpy.pause (1.0, hard=True)
    yo "{i}Since the sun was still up for a little while longer, Aiden and I went back to shoveling with everyone else before it got dark.{/i}"

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
    show darius_winter2 at p6_4
    show darius norm3 at p6_4
    show jin_winter at p6_1
    show jin_glasses at p6_1
    show jin pain3 at p6_1
    show lloyd_winter2 at p6_3
    show lloyd norm3 at p6_3
    show goro_winter2 at p6_5
    show goro norm3 at p6_5
    show yoshi_winter2 at p6_6
    show yoshi norm3 at p6_6
    voice audio.jin_v_oof3a
    j "A-Achooo!! *Sniff*"

    hide aiden_winter2
    hide aiden worry1
    show aiden2_winter2 at p6_2
    show aiden2 worry2 at p6_2
    voice audio.aiden_v_jin6b
    a "Uhh… Jin? You should really go back to the cabin. You’re gonna catch a cold at this rate."

    show goro worry3 at p6_5
    voice audio.goro_v_comp2a1
    g "Yes, you’ve been shoveling for quite a while now. You can leave this kind of work to us."

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

    hide goro_winter2
    hide goro worry3
    show goro2_winter2 at p6_5
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

    show goro_autumn at p6_1
    show goro talk1 at p6_1
    show darius_winter at p6_3
    show darius norm1 at p6_3
    show lloyd_winter at p6_2
    show lloyd norm3 at p6_2
    show aiden_autumn at p6_5
    show aiden norm1 at p6_5
    show jin_autumn at p6_4
    show jin_glasses at p6_4
    show jin norm3 at p6_4
    show yoshi_autumn at p6_6
    show yoshi norm1 at p6_6

    voice audio.goro_v_ah2b
    g "Ah, there he is."

    show aiden happy2 at p6_5
    voice audio.aiden_v_yoshi1b
    a "Hey, Yoshi! Come over here, I saved you a plate!"

    show yoshi happy1 at p6_6
    voice audio.yoshi_v_greet1a1
    yo "Hello, everyone! Sorry for the delay!"

    show goro talk3 at p6_1
    voice audio.goro_v_response2a1
    g "It’s no problem. Aiden was just getting us caught up a little on Ms. Komarova’s condition, but he said that you and Yuri talked to her more than he did."

    show jin worry2 at p6_4
    voice audio.jin_v_yeah2a
    j "Y-Yeah, we were worried things could’ve gone sour again…"

    show yoshi explain2 at p6_6
    voice audio.yoshi_v_actually1a
    yo "Actually, it was the opposite. She was really remorseful over the way she acted, and grateful over how we were taking care of her."

    show lloyd shock2 at p6_2
    voice audio.lloyd_v_amazed1b1
    l "Wow, that’s not what I expected to happen."

    show aiden talk1 at p6_5
    voice audio.aiden_v_yeah1c1
    a "Yeah, and believe it or not, she even apologized to me for how she’s treated me."

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

    show goro explain2 at p6_1
    voice audio.goro_v_conj4a
    g "Either way, I’m just glad we can try and move past it. It’s possible we could get along with Ms. Komarova now after all."

    show jin worry2 at p6_4
    voice audio.jin_v_think2b1
    j "U-Umm…"

    show aiden confused2 at p6_5
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
    show goro2_autumn at p6_1
    show goro2 sad2 at p6_1
    voice audio.goro_v_no1a1
    g "No. Mr. Clermont is our sponsor, and he deserves to know the truth at some point."
    g "If he found out later that we’d been hiding such a thing from him, I’m sure it would be much worse."

    hide goro2_autumn
    hide goro2 sad2
    show goro_autumn at p6_1
    show goro worry3 at p6_1
    voice audio.goro_v_but1a
    g "But l believe we can all agree that can wait for a while, to buy some time and allow Ms. Komarova to regain her health."

    show yoshi talk1 at p6_6
    voice audio.yoshi_v_yes1
    yo "Yes, that is our priority right now."

    hide aiden_autumn
    hide aiden confused2
    show aiden2_autumn at p6_5
    show aiden2 sad5 at p6_5
    voice audio.aiden_v_but1a1
    a "But I get what Jin is saying… Whether we wait or not, it doesn’t change the fact that she’d have nowhere to go."
    a "She’d be left out to dry… again. "

    show jin sad1 at p6_4
    show lloyd upset1 at p6_2
    show darius worry1 at p6_3
    show aiden2 upset1 at p6_5
    hide goro_autumn
    hide goro worry3
    show goro2_autumn at p6_1
    show goro2 sad1 at p6_1
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

    show goro2 confused2 at p6_1
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

    show goro2 think1 at p6_1
    voice audio.goro_v_think1a1
    g "Hmm… Clearly, our camp is understaffed. And every little bit of help counts at this point."

    show jin thinkdn2 at p6_4
    voice audio.jin_v_conj3b1
    j "A-And taking into account that she’s had a change of heart, that would solve the one problem we had with her… "

    show yoshi think3 at p6_6
    voice audio.yoshi_v_anyway1a
    yo "It’s not up for just me to decide, though…"

    show aiden2 sad5 at p6_5
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
    show goro_autumn at p6_1
    show goro talk3 at p6_1
    voice audio.goro_v_agree7a
    g "Hearing all of this, I’m sure we can all agree that we are willing to give Emilia another chance."
    g "I’ll make sure to consider what everyone has said."

    show goro explain2 at p6_1
    voice audio.goro_v_conj5a
    g "Regardless, I’ll have to report to Mr. Clermont on both the camp’s situation and Emilia being sick."

    show yoshi talk1 at p6_6
    voice audio.yoshi_v_agree1a
    yo "Of course, sir. That makes sense."

    hide aiden2_autumn
    hide aiden2 sad5
    show aiden_autumn at p6_5
    show aiden sigh1 at p6_5
    voice audio.aiden_v_relief1a1
    a "Phew… There’s still so much to consider on top of being exhausted from shoveling all day…"

    show lloyd sigh1 at p6_2
    voice audio.lloyd_v_sigh2a
    l "Yeah… Can’t I have my chicken noodle soup in peace? I need to dispel all this tension…"

    show darius comp2 at p6_3
    voice audio.darius_v_amazed2
    d "Try my cocoa."

    show jin talk1 at p6_4
    voice audio.jin_v_conj2c1
    j "W-Well, I have my laptop here with me… And if you guys want, we could work on the journal project some more…! "
    j "Aiden and Yoshi always seem to have fun with me when we do that."

    show lloyd confused2 at p6_2
    voice audio.lloyd_v_confused1a1
    l "Huh? There’s a journal project?"

    show darius confused3 at p6_3
    voice audio.darius_v_confused1a
    d "Never heard of it."

    show goro confused3 at p6_1
    voice audio.goro_v_oh1a
    g "Oh, is this what you were telling me about when Jin first arrived, Yoshinori?"

    show yoshi happy1 at p6_6
    voice audio.yoshi_v_yessir2
    yo "Yes, sir! We’re trying to log down all of our memories from the very first camp term up until now!"
    yo "They’re all going to appear on the website as a blog for interested scouts to read and find out what kind of experiences they’ll have here at Camp Buddy!"

    show lloyd excited3 at p6_2
    voice audio.lloyd_v_shock1b1
    l "Oooh, that sounds exciting!"

    show darius relief2 at p6_3
    voice audio.darius_v_aww1c1
    d "Nostalgic."

    show goro happy1 at p6_1
    voice audio.goro_v_alright1b1
    g "Sure, I’d be happy to help some."

    show yoshi happy2 at p6_6
    voice audio.yoshi_v_okay2
    yo "Okay, great! Let’s get started!"

    # JMA4
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
    $ minigame_id = 'jmA5'
    $ renpy.call(minigame_id, 'night')

label day6_aiden_postmg:

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
    scene bg_messhall_past_day with fade
    play music go_with_the_flow loop
    play bgsound sfxloop_messhall loop

    show ydarius_camp at p5_1
    show ydarius norm1 at p5_1
    show ylloyd_camp at p5_2
    show ylloyd norm1 at p5_2
    show yyoshi_camp at p5_3
    show yyoshi happy2 at p5_3
    show ygoro_camp at p5_5
    show ygoro norm1 at p5_5
    show yyuri_camp at p5_4
    show yyuri norm1 at p5_4
    voice audio.yyoshi_v_sir2
    yo "Glad you’re joining us for lunch today, sir!"

    show yyuri irked1 at p5_4
    voice audio.yyuri_v_goro9c
    yu "Yeah, Dad! We never get to hang out, cause all you do is work!"

    show ygoro explain2 at p5_5
    voice audio.ygoro_v_well1
    g "Well, being camp president can be a lot of work, dear. Thankfully the other staff can handle some of the tasks for now."
    g "You all look like you had fun with this morning’s activity, though!"

    show ylloyd tired1 at p5_2
    voice audio.ylloyd_v_groan2c1
    l "Ugh… It was pretty crazy, and now I’m starving!"

    show ydarius confused2 at p5_1
    voice audio.ydarius_v_confused1a3
    d "Wonder what’s for lunch."

    show yyoshi think2 at p5_3
    voice audio.yyoshi_v_think1a
    yo "Hmm… It smells like Aiden’s cooking…"
    yo "Speaking of which, I don’t think I’ve seen him all morning."

    show ygoro talk3 at p5_5
    voice audio.ygoro_v_shock1a
    g "Ah, Andre did tell me Aiden was taking over lunch duty since he wasn’t feeling well."

    show yyuri worry2 at p5_4
    voice audio.yyuri_v_think1a1
    yu "But I wonder if Aiden’s alright in the kitchen by himself… He’s usually clumsy."

    show yyoshi talk3 at p5_3
    voice audio.yyoshi_v_oh2
    yo "I’ll go check on him! Maybe I can help him finish up too!"

    show ylloyd talk2 at p5_2
    voice audio.ylloyd_v_agree2d5
    l "Yeahhhh! Do that and get back quick so we can eat!"

    show yyoshi happy1 at p5_3
    voice audio.yyoshi_v_bye4a
    yo "Alright, I’ll be right back!"

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

    show yyoshi_camp at right2
    show yyoshi talk1 at right2
    voice audio.yyoshi_v_aiden2
    yo "Hey there, Aiden! I came to h—"

    show yaiden_apron at left2
    show yaiden happy1 at left2
    with dissolve

    voice audio.yaiden_v_yoshi3a
    a "Oh hey, Yoshi!"

    show yyoshi panic3 at right2
    voice audio.yyoshi_v_shock1a
    yo "WHOA, AIDEN! What the heck are you wearing?!" with vpunch

    show yaiden confused2 at left2
    voice audio.yaiden_v_think3a
    a "Uhh… An apron?"

    show yyoshi awkward4 at right2
    voice audio.yyoshi_v_ah4
    yo "J-Just an apron, you mean…!"

    show yaiden comp6 at left2
    voice audio.yaiden_v_laugh1b1
    a "Ehehe, sorry, it gets really hot in here, so it’s easier to strip down while working!"

    show yyoshi worry2 at right2
    voice audio.yyoshi_v_sigh2
    yo "What if you get caught…? You know what happened last time Yuri found you."

    show yaiden tease2 at left2
    voice audio.yaiden_v_comeon1a2
    a "Relaaaax! Nobody ever comes in here besides me and my dad! And you won’t tell on me, will you?"

    show yyoshi worry5 at right2
    voice audio.yyoshi_v_but2a
    yo "Well, I won’t. But still…"

    show yaiden talk2 at left2
    voice audio.yaiden_v_well1a1
    a "If you came here to help me cook, you’re a bit late cause I just finished up!"
    a "But you can still help me serve this out there! Here, let me grab some trays."

    show yaiden_apron at center
    show yaiden talk2 at center
    with move

    show yyoshi panic3 at right2
    voice audio.yyoshi_v_worry1c1
    yo "Aiden, your apron is untied. Be careful not to f—"

    play sound sfx_crash
    show yaiden shock3 at center
    voice audio.yaiden_v_shock1c1
    a "WH-WHOA!" with vpunch

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    hide yaiden_apron
    hide yaiden shock3
    with moveoutbottom

    scene sxma3 1 with fade
    play music on_the_edge loop
    voice audio.yaiden_vsxma3_line1
    a "Oh crap, that was close…! I almost crashed into all the food…"
    yo "...!"

    show sxma3 2 with Dissolve(0.25)
    yo "{i}(Aiden’s apron had come completely undone, and from where I was standing, I had a clear, full view of his backside…){/i}"

    voice audio.yaiden_vsxma3_line2
    a "Aww… The first batch is totally wasted."

    show sxma3 3 with Dissolve(0.25)
    yo "{i}(My eyes were locked on Aiden’s lower body… His butt looked firm, yet bouncy, and just past it… his cute, soft dick was hanging too…){/i}"

    show sxma3 4 with Dissolve(0.25)
    voice audio.yaiden_vsxma3_line3
    a "Um, Yoshi? I need a hand here~"

    show sxma3 5 with Dissolve(0.25)
    voice audio.yyoshi_vsxma3_line1
    yo "S-Sorry, Aiden…! Are you okay?"

    voice audio.yaiden_vsxma3_line4
    a "Mm-hm~ "
    yo "{i}(I tried to help Aiden get back up, holding and gently pulling on his lean body, but then—){/i}"

    show sxma3 6 with Dissolve(0.25)
    voice audio.yaiden_vsxma3_line5
    a "*giggles*"
    yo "{i}(Aiden’s hips suddenly started squirming, grinding his bare butt against my crotch.){/i}"

    show sxma3 7 with Dissolve(0.25)
    voice audio.yaiden_vsxma3_line6
    a "You were enjoying the view, weren’t you Yoshi?"

    voice audio.yyoshi_vsxma3_line2
    yo "Mmhh…"
    yo "{i}(Aiden kept teasing me while continuing his naughty motions… His playful shaking was working me up…){/i}"

    voice audio.yaiden_vsxma3_line7
    a "Hehe, it’s pretty easy to get you hard~ "

    show sxma3 8 with Dissolve(0.25)
    voice audio.yyoshi_vsxma3_line3
    yo "S-Sorry, I can’t help it…"

    voice audio.yaiden_vsxma3_line8
    a "Not that I’m complaining~ You know I’m always down for some fun!"
    yo "{i}(I don’t know how the two of us got to this point… When I first met Aiden, he seemed really polite and even somewhat shy…){/i}"
    yo "{i}(But as we hung out more and spent time together, we started doing this kind of stuff with each other.){/i}"

    voice audio.yyoshi_vsxma3_line4
    yo "I promise I’ll make it quick…"

    voice audio.yaiden_vsxma3_line9
    a "I’m not in a hurry~"

    show sxma3 9 with Dissolve(0.25)
    voice audio.yaiden_vsxma3_line10
    a "Ooohhh~"
    yo "{i}(Ever since Aiden moved into our cabin, we spent a lot of time cuddling, and I knew most of his favorite spots…){/i}"
    yo "{i}(First… His nipples are extra sensitive – they stiffen up at the slightest touch… And every time I pinch them, it makes him shiver…){/i}"

    show sxma3 10 with Dissolve(0.25)
    voice audio.yaiden_vsxma3_line11
    a "A-Ahehe…!"
    yo "{i}(Second… His armpits are also a quick way to turn him on… One day, when we were wrestling, he instantly got a boner from me tickling him there…){/i}"

    show sxma3 11 with Dissolve(0.25)
    voice audio.yaiden_vsxma3_line12
    a "Uwaahh…"
    yo "{i}(And last but not least, he really likes it when I go straight for the prize… Stroking his dick slowly with a light grip makes it twitch with excitement.){/i}"

    show sxma3 12 with Dissolve(0.25)
    voice audio.yaiden_vsxma3_line13
    a "Ooooh… You’re gonna make me cum, Yoshiiii…"
    yo "{i}(Every time we’ve fooled around, Aiden and I have tried something new…){/i}"
    yo "{i}(Even though I knew he’d reach his limit soon, I wanted to take things further than usual…){/i}"

    show sxma3 13 with Dissolve(0.25)
    voice audio.yaiden_vsxma3_line14
    a "E-Eehh…?"
    yo "{i}(Wetting my finger, I poked it into Aiden’s hole… if I wanted to do more, then I needed to get him ready…){/i}"

    show sxma3 14 with Dissolve(0.25)
    voice audio.yaiden_vsxma3_line15
    a "Hnnghh…!"
    yo "{i}(With a gentle push, I shoved it all the way in… Aiden’s insides were warm and trembling from the new sensation…){/i}"

    show sxma3 15 with Dissolve(0.25)
    voice audio.yaiden_vsxma3_line16
    a "Nggaaahh… I-It feels weird, Yoshi…"

    voice audio.yyoshi_vsxma3_line5
    yo "Tell me if I need to stop, Aiden…"

    voice audio.yaiden_vsxma3_line17
    a "N-No… K-Keep going…!"
    yo "{i}(I kept digging my finger into his ass trying to find something…){/i}"

    show sxma3 16 with Dissolve(0.25)
    voice audio.yaiden_vsxma3_line18
    a "Euughhhh~~!!"
    yo "{i}(Bending my knuckles up, I finally found it! Aiden’s pleasure spot! ){/i}"

    show sxma3 17 with Dissolve(0.25)
    voice audio.yaiden_vsxma3_line19
    a "Hnggghh~~! Yoshii~~~"
    yo "{i}(All of a sudden Aiden’s insides were in a frenzy, pulsing around my buried digit.){/i}"
    yo "{i}(At that point I knew he was ready for me…){/i}"

    show sxma3 18 with Dissolve(0.25)
    voice audio.yyoshi_vsxma3_line6
    yo "I’m going in, Aiden…"

    show sxma3 19 with Dissolve(0.25)
    voice audio.yaiden_vsxma3_line20
    a "NNGHH...!!!"
    yo "{i}(As carefully as possible, I nudged my dick into Aiden’s hole, and felt his insides slowly adjusting to every inch I pushed in.){/i}"

    show sxma3 20 with Dissolve(0.25)
    voice audio.yaiden_vsxma3_line21
    a "Haaaaahhh…!"
    yo "{i}(Finally, I was all the way in, with the tip of my cock prodding right against the spot I found before…){/i}"
    yo "{i}(Aiden was getting overwhelmed, and I knew I had to do something to ease him up.){/i}"

    show sxma3 21 with Dissolve(0.25)
    voice audio.yaiden_vsxma3_line22
    a "Waahhh…"
    yo "{i}(I fondled his chest again, hoping to release some of the tension in his body…){/i}"

    show sxma3 22 with Dissolve(0.25)
    voice audio.yaiden_vsxma3_line23
    a "Mnnghhh~ "
    yo "{i}(Moving my hands back to his pits, Aiden began to moan excitedly, and his insides began to loosen up again…){/i}"

    show sxma3 23 with Dissolve(0.25)
    voice audio.yyoshi_vsxma3_line7
    yo "D-Does it feel good, Aiden…?"

    voice audio.yaiden_vsxma3_line24
    a "Y-Yeaaahh… S-So good…"

    voice audio.yyoshi_vsxma3_line8
    yo "I’ll start moving now, alright…?"

    voice audio.yaiden_vsxma3_line25
    a "Okay, I-I can take it…!"

    show sxma3 24 with Dissolve(0.25)
    voice audio.yaiden_vsxma3_line26
    a "Ngghh…! Hnghh…!"
    yo "{i}(I began thrusting, sliding my shaft back and forth into Aiden…){/i}"

    show sxma3 25 with Dissolve(0.25)
    voice audio.yaiden_vsxma3_line27
    a "Aaahh!! Haaah! Ahh!"
    yo "{i}(I couldn’t believe what Aiden and I were doing right now… It felt way better than anything else we’d ever done before…){/i}"
    yo "{i}(We were both so into it, I could feel myself leaking inside him, making my thrusts quicker… Aiden must’ve been too, dripping precum onto the floor.){/i}"

    show sxma3 26 with Dissolve(0.25)
    voice audio.yaiden_vsxma3_line28
    a "Y-Yoshi, I can’t… a-anymore…!"
    yo "{i}(After all the teasing at the start, and now finally having me inside him made Aiden ready for a release… I knew I couldn’t last much longer either… ){/i}"

    voice audio.yyoshi_vsxma3_line9
    yo "M-Me too, Aiden…!!"

    show sxma3 27 with Dissolve(0.25)
    voice audio.yyoshiaiden_vsxma3_line1
    yoa "*cums*"

    show sxma3 28 with Dissolve(0.25)
    voice audio.yaiden_vsxma3_line29
    a "Whew… Ooohhh~…"

    show sxma3 29 with Dissolve(0.25)
    yo "{i}(Aiden tried to catch his breath, and glancing down I could see his dick softening up after such an intense release… ){/i}"

    voice audio.yaiden_vsxma3_line30
    a "You came inside me, Yoshi… It feels so warm…"

    voice audio.yyoshi_vsxma3_line10
    yo "A-Ahh… I didn’t mean to… "

    show sxma3 30 with Dissolve(0.25)
    voice audio.yaiden_vsxma3_line31
    a "That’s a first for me…"

    voice audio.yyoshi_vsxma3_line11
    yo "Me too… "

    voice audio.yaiden_vsxma3_line32
    a "It better not be the last, okay…?"

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black with fade
    yo "{i}After Aiden and I had recovered, we quickly cleaned up the mess we had made... We were lucky nobody else had come in while we were doing that!{/i}"

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

    show yaiden_apron at left2
    show yaiden norm1 at left2
    show yyoshi_camp at right2
    show yyoshi happy1 at right2
    voice audio.yyoshi_v_aiden2
    yo "Okay, Aiden! I think that's the last of it ready to go!"

    show yaiden relief4 at left2
    voice audio.yaiden_v_relief1a1
    a "Whew... Thanks, Yoshi! I dunno what I'd have done without you after spilling all that."

    show yyoshi comp6 at right2
    voice audio.yyoshi_v_yeah3
    yo "Hehe, yeah... We really did make a mess. "

    show yaiden tease1 at left2
    voice audio.yaiden_v_laugh1c1
    a "In a couple ways, yeah~"

    show yyoshi shy4 at right2
    voice audio.yyoshi_v_ah3
    yo "A-Ah..."

    show yaiden happy1 at left2
    voice audio.yaiden_v_rush1a1
    a "Anyway, come on! Let's go serve lunch!"

    hide yaiden_apron
    hide yaiden happy1
    with moveoutleft

    show yyoshi shock3 at right2
    voice audio.yyoshi_v_wait3
    yo "W-Wait, Aiden! You're not dressed yet!"

    hide yyoshi_camp
    hide yyoshi shock3
    with moveoutleft

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
    scene bg_messhall_past_day with fade
    play music here_they_come loop

    show ygoro_camp at p7_6
    show ygoro norm3 at p7_6
    show ydarius_camp at p7_4
    show ydarius norm1 at p7_4
    show ylloyd_camp at p7_5
    show ylloyd norm1 at p7_5
    show yyuri_camp at p7_7
    show yyuri norm1 at p7_7

    show yaiden_apron at p7_1
    show yaiden bold2 at p7_1
    with dissolve

    show ydarius shock1 at p7_4
    show ylloyd shock1 at p7_5
    show ygoro shock1 at p7_6
    show yyuri shock4 at p7_7
    voice audio.yaiden_v_orderup1a
    a "Order up!"

    show yaiden_apron at p7_2
    show yaiden bold2 at p7_2
    with move

    show yyoshi_camp at p7_1
    show yyoshi panic4 at p7_1
    with dissolve

    voice audio.yyoshi_v_aiden6
    yo "A-Aiden, get back there! "

    show yaiden happy4 at p7_2
    voice audio.yaiden_v_oh1a
    a "Ah! There they are!"

    show yaiden_apron at p7_3
    show yaiden happy4 at p7_3
    with move

    voice audio.yaiden_v_todayspecial1a
    a "Sorry for the wait, everyone! Today’s special is creamy potato soup!"

    show yyuri fangirl2 at p7_7
    voice audio.yyuri_v_kyaa1
    yu "KYAAAAAA!!!!!" with vpunch

    show yyoshi_camp at p7_2
    show yyoshi panic4 at p7_2
    with move

    show yyoshi_camp at p7_1
    show yyoshi panic4 at p7_1
    show yaiden_apron at p7_2
    show yaiden happy4 at p7_2
    with move

    show yyoshi panic3 at p7_1
    voice audio.yyoshi_v_shock4
    yo "G-Gah! Everyone, don’t look!"

    show ygoro sigh1 at p7_6
    voice audio.ygoro_v_sigh2a
    g "*sigh* Not again…"

    show ylloyd amazed1 at p7_5
    #jey
    voice audio.ylloyd_v_excited4a
    l "Ooooh~ That looks yummy!"

    show ydarius confused2 at p7_4
    voice audio.ydarius_v_think2a2
    d "You’ve got something dripping down there."

    show yyuri drool1 at p7_7
    voice audio.yyuri_v_fujo4a
    yu "Oh my god!!! Could it be?!"

    show yyoshi_camp at p7_2
    show yyoshi panic3 at p7_2
    show yaiden_apron at p7_1
    show yaiden scared3 at p7_1
    with move

    voice audio.yyoshi_v_noway1
    yo "T-T-That’s definitely just c-crum, I mean CREAM…! I-It got pretty messy in the kitchen!" with vpunch

    show yyuri drool4 at p7_7
    voice audio.yyuri_v_kyaa1
    yu "KYAAAAAA~!"

    show yyuri drool5 at p7_7
    yu "*faints*"

    hide yyuri_camp
    hide yyuri drool5
    with moveoutbottom

    show yaiden shock3 at p7_1
    voice audio.yaiden_v_yuri8a
    a "Wah! Yuri!"

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

    jump day6_aiden_postfb

label day6_aiden_postfb:

    $ location = location_messhall
    $ day = "81"
    $ time = timeline_timenight
    $ season = season_winter
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_messhall_winter_night with fade
    play music ready_for_tomorrow loop

    show goro_autumn at p6_1
    show goro norm3 at p6_1
    show darius_winter at p6_3
    show darius norm1 at p6_3
    show lloyd_winter at p6_2
    show lloyd norm1 at p6_2
    show aiden_autumn at p6_5
    show aiden norm1 at p6_5
    show jin_autumn at p6_4
    show jin_glasses at p6_4
    show jin excited2 at p6_4
    show yoshi_autumn at p6_6
    show yoshi norm1 at p6_6
    voice audio.jin_v_whoa3b
    j "The origin of the blessed apron has been revealed…"

    show goro sigh1 at p6_1
    voice audio.goro_v_sigh1a
    g "*sigh* It always caused a ruckus with the campers even back then."

    show aiden play2 at p6_5
    voice audio.aiden_v_laugh1b2
    a "Hehe, but you never stopped me, Gramps. "

    show lloyd laugh2 at p6_2
    voice audio.lloyd_v_conj1a3
    l "Well, it did get everybody excited whenever it happened."

    show darius tease4 at p6_3
    voice audio.darius_v_naughty1a
    d "Yoshi would know."

    show yoshi shock2 at p6_6
    voice audio.yoshi_v_shock4
    yo "G-Gah! Don’t get the wrong idea, everyone…!"

    hide jin_autumn
    hide jin_glasses
    hide jin excited2
    show jin2_autumn at p6_4
    show jin2_glasses at p6_4
    show jin2 fudan2 at p6_4
    voice audio.jin_v_please3b
    j "W-Was Yuri right about what happened in the kitchen, though…?"

    show aiden wink3 at p6_5
    voice audio.aiden_v_unsure3a
    a "I dunno~ You tell them, Yoshi~"

    show yoshi awkward3 at p6_6
    voice audio.yoshi_v_rush6
    yo "I-I think we’re done here! We still got lots of work left to do tomorrow!"
    yo "G-Go to bed everyone!"

    show aiden laugh4 at p6_5
    voice audio.aiden_v_laugh2a1
    a "Hahaha!"

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
    jump day7_aiden
