label day1:
    $ day = "01"
    $ time = timeline_timeday
    $ season = season_autumn
    $ location = location_entrance
    $ working = True

    scene cg white with fade
    play music buddy_oath_casual loop
    play bgsound sfxloop_windy loop
    show cg intro:
        yalign 0.0 xalign 0.5
    show leaves
    with Dissolve(2.0)
    $ renpy.pause(2.0, hard=True)
    show cg intro:
        yalign 0.0 xalign 0.5
        linear 5 yalign 1.0
    $ renpy.pause(6.0, hard=True)

    hide leaves
    scene cg2 newbeginning1 with dissolve
    show screen location()
    show screen timeline()
    show screen quick_menu()
    $quick_menu = True
    play bgsound2 sfxloop_leaves loop
    voice audio.yoshi_vs1_line1
    yo "{i}(It’s that time of the year again, huh?){/i}"

    voice audio.yoshi_vs1_line2
    yo "{i}(Camp Buddy’s off-season…){/i}"

    voice audio.yoshi_vs1_line3
    yo "{i}(It’s not really my favorite part of the year, but it has to happen eventually… It’s always so lonely to see the camp so quiet and empty…){/i}"

    voice audio.yoshi_vs1_line4
    yo "{i}(There's no campers around like there used to be… And that means no activities either…){/i}"

    voice audio.yoshi_vs1_line5
    yo "{i}(But… this time is different than the previous years.){/i}"

    show cg2 newbeginning2 with Dissolve(0.25)
    voice audio.yoshi_vs1_line6
    yo "{i}(Now that the camp has become successful and popular, the next term will be busier than ever!){/i}"

    voice audio.yoshi_vs1_line7
    yo "{i}(I guess that’s something I can look forward to! I’m happy that Camp Buddy is back at its peak!){/i}"

    voice audio.yuri_vs1_line1
    yu "Hey!"

    show cg2 newbeginning3 with Dissolve(0.25)
    voice audio.yoshi_vs1_line8
    yo "Wh-Wha—?!"

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black
    hide screen location
    hide screen timeline
    hide screen quick_menu
    with fade
    $quick_menu = False

    $ location = location_entrance
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_entrance_autumn_day with fade
    play music buddy_oath_casual loop
    play bgsound sfxloop_windy loop
    play bgsound2 sfxloop_leaves loop

    show yoshi_autumn at left2
    show yoshi shock1 at left2
    show yuri_autumn at right2
    show yuri irked1 at right2
    voice audio.yuri_vs1_line2
    yu "I can’t believe you were ignoring everything I was saying, Yoshi."

    hide yoshi_autumn
    hide yoshi shock1
    show yoshi2_autumn at left2
    show yoshi2 awkward3 at left2
    voice audio.yoshi_vs1_line9
    yo "S-Sorry! I just had something on my mind!"

    show yuri confused2 at right2
    voice audio.yuri_vs1_line3
    yu "Jeez, you still talk to yourself this much? I thought you were over that habit!"

    voice audio.yuri_vs1_line4
    yu "Some things never really change, huh? You’re always so sentimental, just like a retired person!"

    hide yoshi2_autumn
    hide yoshi2 awkward3
    show yoshi_autumn at left2
    show yoshi annoy5 at left2
    voice audio.yoshi_vs1_line10
    yo "H-Hey… I’m not that old… And we’re only a year apart!"

    show yuri tease2 at right2
    voice audio.yuri_vs1_line5
    yu "Hehe, hearing you say that makes you sound like my dad. "

    hide yoshi_autumn
    hide yoshi annoy5
    show yoshi2_autumn at left2
    show yoshi2 sigh1 at left2
    voice audio.yoshi_vs1_line11
    yo "*sigh* Sir Goro’s not that old either…"

    show yuri explain2 at right2
    voice audio.yuri_vs1_line6
    yu "Anyway, since you weren’t listening to me, I was asking when you’ll be done cleaning up here? "

    voice audio.yuri_vs1_line7
    yu "I need some firewood for the office since the air is getting a little chilly now."

    hide yoshi2_autumn
    hide yoshi2 sigh1
    show yoshi_autumn at left2
    show yoshi talk3 at left2
    voice audio.yoshi_vs1_line12
    yo "Oh, I just finished here, so I can chop some right away!"

    voice audio.yoshi_vs1_line13
    yo "Let me go find Aiden and we'll get it done for you faster!"

    show yuri confused4 at right2
    voice audio.yuri_vs1_line8
    yu "I doubt he’ll be able to help anytime soon. I just saw Aiden busy with some other chores, so I didn’t bother asking him."

    voice audio.yuri_vs1_line9
    yu "If you want, I can help you instead! I know how to swing an axe around too, after all~"

    show yoshi laugh1 at left2
    voice audio.yoshi_vs1_line14
    yo "Haha, it’s alright, Yuri. I can manage!"

    voice audio.yoshi_vs1_line15
    yo "Besides, don’t you have work to do with Sir Goro as well?"

    show yuri sigh4 at right2
    voice audio.yuri_vs1_line10
    yu "*sigh* Don't remind me… I don't know how Dad can stand to keep working  in his office like that all day long – it drives me crazy!"

    voice audio.yuri_vs1_line11
    yu "Honestly, coming out here to check on you was just an excuse to stretch my legs and get some fresh air!"

    show yoshi comp3 at left2
    voice audio.yoshi_vs1_line16
    yo "I guess it can't be helped, Yuri. There's been a ton of legal paperwork for Sir Goro to work on ever since the last term ended."

    voice audio.yoshi_vs1_line17
    yo "There's so much stuff to do just to keep the place running with only the few of us and almost all the scouts gone."

    show yuri talk2 at right2
    voice audio.yuri_vs1_line12
    yu "Is that what you were daydreaming about before? "

    show yoshi think2 at left2
    voice audio.yoshi_vs1_line18
    yo "I was just thinking about how much Camp Buddy has changed over the years…"

    show yuri comp2 at right2
    voice audio.yuri_vs1_line13
    yu "It’s been a roller-coaster ride, huh…?"

    show yoshi comp3 at left2
    voice audio.yoshi_vs1_line19
    yo "Yeah… I really got the chance to connect with the campers as well… It's probably the greatest term I've ever had."

    voice audio.yoshi_vs1_line20
    yo "It does make me wonder how many of them will come back next year."

    show yuri comp4 at right2
    voice audio.yuri_vs1_line14
    yu "Aww, you really do miss them a lot, don't you?"

    voice audio.yuri_vs1_line15
    yu "I’m sure a lot of them will come back! And if not, that’s okay too!"

    hide yoshi_autumn
    hide yoshi comp3
    show yoshi2_autumn at left2
    show yoshi2 sad4 at left2
    voice audio.yoshi_vs1_line21
    yo "Yeah, but I have to be honest… It'll be really sad if I never see some of those campers again."

    show yuri play2 at right2
    voice audio.yuri_vs1_line16
    yu "Hey, lighten up a bit, will you? I expected you to be less of a worrywart now that everything is going well."

    voice audio.yuri_vs1_line17
    yu "The next term is still months away and a lot can happen in their personal lives."

    show yuri happy1 at right2
    voice audio.yuri_vs1_line18
    yu "You did your job last summer, and whether they come back or not is up to them."

    voice audio.yuri_vs1_line19
    yu "But one thing is certain, we all had some of our greatest memories here at Camp Buddy last term… "

    show yuri comp4 at right2
    voice audio.yuri_vs1_line20
    yu "And that’s something that will forever stay in our hearts!"

    hide yoshi2_autumn
    hide yoshi2 sad4
    show yoshi_autumn at left2
    show yoshi comp6 at left2
    voice audio.yoshi_vs1_line22
    yo "Haha… Now who’s the sentimental one?"

    show yuri_autumn at left2
    show yuri pout1 at left2
    with move

    show yuri_autumn at right2
    show yuri pout1 at right2
    with move

    yu "*pulls Yoshinori’s ear*"

    show yoshi pain3 at left2
    voice audio.yoshi_vs1_line23
    yo "O-Ow!"

    show yuri irked2 at right2
    voice audio.yuri_vs1_line21
    yu "Hmph! All I’m saying is, you can cherish the past, but it’s best to focus on what’s ahead!"

    show yoshi comp2 at left2
    voice audio.yoshi_vs1_line24
    yo "You’re right, Yuri."

    show yuri happy1 at right2
    voice audio.yuri_vs1_line22
    yu "Anyways! Those logs aren’t gonna split themselves, Yoshi! I better see a fresh pile of wood chopped by sundown!"

    voice audio.yuri_vs1_line23
    yu "I’ll be around the shed if you need me~!"

    hide yuri_autumn
    hide yuri happy1
    with moveoutright

    show yoshi_autumn at center
    show yoshi shock3 at center
    with move

    voice audio.yoshi_vs1_line25
    yo "H-Hey! I thought you were helping your dad…!"

    voice audio.yuri_vs1_line24
    yu "Oh, he’ll be fine without me for a while! Hihihi~!"

    show yoshi relief5 at center
    voice audio.yoshi_vs1_line26
    yo "*sigh*"

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

    $ location = location_forest
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_forest_autumn_day with fade
    play bgsound sfxloop_leaves loop

    show yoshi_autumn at center
    show yoshi scared2 at center
    voice audio.yoshi_v_relief2
    yo "Brr… It’s really cold out here… I better get moving."

    play sound sfx_woodchop
    show yoshi confused2 at center
    voice audio.yoshi_v_huh2
    yo "H-Huh…? Is someone already here?"

    scene cg aiden1_1 with fade
    play music go_with_the_flow loop
    voice audio.yoshi_vsa1_line1
    yo "Oh, Aiden…!"

    voice audio.aiden_vsa1_line1
    a "Hey there, Yoshi! "

    voice audio.aiden_vsa1_line2
    a "I was just chopping some wood over here. You need anything?"

    voice audio.yoshi_vsa1_line2
    yo "Ah, I was about to gather some myself to bring to the office. "

    voice audio.aiden_vsa1_line3
    a "Here, come and get some! I made plenty!"

    voice audio.aiden_vsa1_line4
    a "I figured we would be using a lot more now that the weather's getting colder."

    voice audio.aiden_vsa1_line5
    a "And I knew Yuri was gonna ask you to do it, so I thought I'd take it off your list!"

    voice audio.yoshi_vsa1_line3
    yo "Aiden… You didn’t have to do that. "

    voice audio.aiden_vsa1_line6
    a "Oh, come on! It’s fine! I always like to smack some wood and work my muscles up!"

    voice audio.yoshi_vsa1_line4
    yo "Well, I was going to ask for your help anyway, but Yuri told me you were busy with other chores."

    show cg aiden1_2 with Dissolve(0.25)
    voice audio.aiden_vsa1_line7
    a "I was, but I already prepped everything and left our dinner cooking in the oven."

    voice audio.aiden_vsa1_line8
    a "And I used up all the firewood in the kitchen, so I needed to make some more anyways! "

    voice audio.yoshi_vsa1_line5
    yo "Haha, it looks like you've got everything covered, huh?"

    show cg aiden1_3 with Dissolve(0.25)
    voice audio.aiden_vsa1_line9
    a "Yup! You know you can always count on me!"

    voice audio.yoshi_vsa1_line6
    yo "You should give yourself a break sometimes though, Aiden. I mean… you really haven't stopped doing chores even after the summer term ended."

    show cg aiden1_2 with Dissolve(0.25)
    voice audio.aiden_vsa1_line10
    a "Don't worry, there's not that much stuff to do now that it's off-season. I only have to feed what, like... six people?"

    voice audio.aiden_vsa1_line11
    a "Other than that, it’s just the usual stuff around the camp too, nothing I can’t handle!"

    voice audio.yoshi_vsa1_line7
    yo "Haha, I guess I shouldn't have expected any different. You've been taking care of everyone here for as long as I can remember, after all."

    show cg aiden1_4 with Dissolve(0.25)
    voice audio.aiden_vsa1_line12
    a "It’s my pleasure, Yoshi! Always at your service!"

    scene bg_forest_autumn_day with fade
    show aiden_work at left2
    show aiden norm1 at left2
    show yoshi_autumn at right2
    show yoshi think1 at right2
    voice audio.yoshi_v_think1a
    yo "Hmm… As grateful as I am that you're always so willing to help, we should really get more staff around here for next year's term."
    yo "Especially since we're expecting so many new recruits. We don't want you getting swamped with work like the past few terms!"

    show aiden laugh1 at left2
    voice audio.aiden_v_response1a
    a "It’s really not that big of a deal! They’re just chores after all!"

    show yoshi happy2 at right2
    voice audio.yoshi_v_well1
    yo "Well, now that you're a scoutmaster just like me, I'm sure you could use a helping hand!"

    hide aiden_work
    hide aiden laugh1
    show aiden2_work at left2
    show aiden2 awkward5 at left2
    voice audio.aiden_v_well1c1
    a "W-Well, if you put it that way, I guess so."

    show yoshi happy1 at right2
    voice audio.yoshi_v_conj2a
    yo "Speaking of which, why don't you let me help you finish up here? I brought an axe with me anyway!"

    hide aiden2_work
    hide aiden2 awkward5
    show aiden_work at left2
    show aiden happy1 at left2
    voice audio.aiden_v_laugh2b1
    a "Haha, I wouldn't say no to some company~! You'll probably enjoy working up a sweat after all those boring tasks you've been doing!"

    hide yoshi_autumn
    hide yoshi happy1
    show yoshi2_autumn at right2
    show yoshi2 shy5 at right2
    voice audio.yoshi_v_right4
    yo "R-Right… Is that why you don’t have a shirt on? Aren't you cold?"

    show aiden tease1 at left2
    voice audio.aiden_v_oho1a
    a "Oho~ Distracted by my bod, are you?"

    hide yoshi2_autumn
    hide yoshi2 shy5
    show yoshi_autumn at right2
    show yoshi awkward6 at right2
    show yoshi_blush1 at right2
    yo "...!"

    show aiden laugh3 at left2
    voice audio.aiden_v_laugh2b1
    a "Hahaha! You’re red as a tomato, Yoshi!"
    a "Come on, you should be used to me being half naked most of the time by now!"

    hide yoshi_autumn
    hide yoshi awkward6
    hide yoshi_blush1
    show yoshi2_autumn at right2
    show yoshi2 comp3 at right2
    voice audio.yoshi_v_unsure3c
    yo "I-I guess you’re right, hahaha…"

    show aiden excited1 at left2
    voice audio.aiden_v_rush1a2
    a "Now let’s get to work!"

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black
    hide screen location
    hide screen timeline
    hide screen quick_menu
    $quick_menu = False
    with fade
    play sound sfx_woodchop
    $ renpy.pause (2.0, hard=True)

    $ location = location_office
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_office_autumn_day with fade

    show yoshi_autumn at center
    show yoshi talk1 at center
    voice audio.yoshi_v_greet2a1
    yo "Excuse me for coming in without knocking, sir! I have the firewood right h—"

    scene cg goro1_1 with fade
    play music old_familiar_home loop
    voice audio.yoshi_vsg1_line1
    yo "Ah…! I hope I'm not disturbing you, Sir Goro!"

    voice audio.goro_vsg1_line1
    g "No, not at all, Yoshinori."

    voice audio.yoshi_vsg1_line2
    yo "Let me put these by the fireplace and I'll head out!"

    voice audio.goro_vsg1_line2
    g "Ah, thank you, Yoshinori. Take your time though, it’s really alright."

    show cg goro1_2 with Dissolve(0.25)
    yo "{i}(Sir Goro looks busy as always… I can't imagine how stressful it must be to have so many responsibilities as the camp president.){/i}"

    show cg goro1_1 with Dissolve(0.25)
    voice audio.goro_vsg1_line3
    g "I assume Yuri fetched you?"

    voice audio.yoshi_vsg1_line3
    yo "Yes, sir! She also mentioned having work to do in the shed."

    show cg goro1_3 with Dissolve(0.25)
    voice audio.goro_vsg1_line4
    g "*sigh* She’s trying to avoid all the admin tasks again, I see."

    voice audio.yoshi_vsg1_line4
    yo "Is there anything I can help with, sir?"

    show cg goro1_4 with Dissolve(0.25)
    voice audio.goro_vsg1_line5
    g "It’s fine, Yoshinori. I can handle it."

    voice audio.goro_vsg1_line6
    g "Actually, I was hoping to help you three with chores around the camp instead of all this legal work."

    voice audio.yoshi_vsg1_line5
    yo "You have been working nonstop on paperwork since the last term ended. I was hoping to be able to assist you with it some."

    voice audio.goro_vsg1_line7
    g "Well, I'm trying to make sure we have everything arranged properly with Mr. Clermont. It's the least I could do, considering his company is sponsoring our camp."

    voice audio.goro_vsg1_line8
    g "You're already doing a great deal just by managing the camp anyway. It makes me relieved to know that you'll be the one to take my place here when the time comes."

    voice audio.yoshi_vsg1_line6
    yo "That’s an honor to hear from you, sir…!"

    show cg goro1_5 with Dissolve(0.25)
    voice audio.goro_vsg1_line9
    g "But… I also want to make up for all the previous years when I didn't manage Camp Buddy properly as its president."

    voice audio.goro_vsg1_line10
    g "I’m trying my best to show you all that I can work just as hard and that this is much more than a job to me."

    voice audio.yoshi_vsg1_line7
    yo "I understand, sir!"

    show cg goro1_6 with Dissolve(0.25)
    voice audio.goro_vsg1_line11
    g "Come on, Yoshinori. You don’t have to be so stiff and formal around me. "

    voice audio.yoshi_vsg1_line8
    yo "A-Ah…!"

    voice audio.goro_vsg1_line12
    g "Although, I can understand why you and everyone else were intimidated by me, given how strict and uptight I'd been over the last couple of years…"

    # voice audio.goro_vsg1_line13 #jey missing audio
    g "I truly regret that my actions led you all to feel that way."

    show cg goro1_7 with Dissolve(0.25)
    voice audio.goro_vsg1_line14
    g "That's why I'm so grateful that we got to spend so much time together and catch up with one another last summer."

    voice audio.goro_vsg1_line15
    g "You and the scouts from the previous term were the reason I got my passion back and remembered what we all dreamed for this place to be."

    scene bg_office_autumn_day with fade
    show goro_autumn2 at left2
    show goro norm2 at left2
    show yoshi_autumn at right2
    show yoshi comp1 at right2
    yo "..."

    show goro play3 at left2
    voice audio.goro_v_ehem1a
    g "*ehem* Maybe I should take a break before I start turning to dust here in the office."

    show yoshi awkward3 at right2
    voice audio.yoshi_v_what7
    yo "Wh-Wha…"

    show goro laugh1 at left2
    voice audio.goro_v_laugh2c2
    g "Hahaha! I figured Yuri and Aiden were right that I’m not getting any younger. Might as well laugh about it, don't you think?"

    show yoshi angry2 at right2
    voice audio.yoshi_v_disagree1a
    yo "I disagree, sir! You don't look old at all, especially not to me!"

    hide goro_autumn2
    hide goro laugh1
    show goro2_autumn2 at left2
    show goro2 annoy3 at left2
    voice audio.goro_v_really4a
    g "If you're trying to kiss up to me so that you'll be promoted to camp president, you'll have to try harder than that."

    show yoshi shock6 at right2
    voice audio.yoshi_v_sir4
    yo "I-I’m not, sir…! I really meant it!"

    hide goro2_autumn2
    hide goro2 annoy3
    show goro_autumn2 at left2
    show goro happy2 at left2
    voice audio.goro_v_comp2a2
    g "I’m just kidding, Yoshinori! Take it easy!"

    show yoshi comp6 at right2
    voice audio.yoshi_v_unsure3c
    yo "I… I guess it’s just unusual for me to see you making jokes again, sir. It’s been so long since I’ve seen you this cheerful."

    show goro play2 at left2
    voice audio.goro_v_heh1a
    g "Just like back in the “old” days, you mean?"

    show yoshi laugh1 at right2
    voice audio.yoshi_v_laugh1
    yo "Hahaha, exactly, sir! It’s a good thing though!"

    show goro happy2 at left2
    voice audio.goro_v_well1a
    g "Well, I'm trying my best to not be such a grump. I want to show how much I enjoy being here at camp with you all."

    show yoshi play2 at right2
    voice audio.yoshi_v_encourage3
    yo "We’re glad to have the “old” you back as well, sir!"

    hide goro_autumn2
    hide goro happy2
    show goro2_autumn2 at left2
    show goro2 explain2 at left2
    voice audio.goro_v_okay4a
    g "Okay, I take it back. It does sound weird if you’re the one calling me old."

    show yoshi laugh2 at right2
    voice audio.yoshi_v_laugh1
    yo "Hahaha!"

    hide goro2_autumn2
    hide goro2 explain2
    show goro_autumn2 at left2
    show goro talk3 at left2
    voice audio.goro_v_anyway2
    g "Anyway, why don’t we go over to the shed and help Yuri with whatever she’s doing?"

    show yoshi confused2 at right2
    voice audio.yoshi_v_unsure2b
    yo "A-Are you sure, sir? You already have plenty on your hands right now."

    show goro happy2 at left2
    voice audio.goro_v_alright2a2
    g "It's alright. I want us to get rid of a lot of clutter before Mr. Clermont's ocular visit. "

    show yoshi talk2 at right2
    voice audio.yoshi_v_alright2
    yo "The shed has been overflowing for a while, so it's probably best we go through it and see what's worth keeping."

    show goro talk4 at left2
    voice audio.goro_v_agree4a1
    g "Exactly. A general cleanup has been long overdue. There's a lot of things scattered all over the place."
    g "And with plenty of new campers next year, it will be hard to monitor them all. The excess junk could be a hazard."

    show yoshi talk1 at right2
    voice audio.yoshi_v_response1b
    yo "I understand, sir!"

    show goro talk3 at left2
    voice audio.goro_v_anyway2
    g "Anyway, thank you again for your concern, Yoshinori. Why don’t we go and join Yuri?"

    show yoshi happy1 at right2
    voice audio.yoshi_v_yessir2
    yo "Yes, sir!"

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black
    hide screen location
    hide screen timeline
    hide screen quick_menu
    $quick_menu = False
    with fade
    $ renpy.pause (1.0, hard=True)

    $ location = location_shed
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_outshed_autumn_day with fade
    play bgsound sfxloop_leaves loop
    play music buddy_oath_casual loop

    show yuri_autumn at center
    show yuri pain3 at center
    voice audio.yuri_v_hngh1b1
    yu "Hnnnnnnghhh…!!"

    play sound sfx_boxesdrop
    show yuri tired2 at center
    voice audio.yuri_v_relief1a1
    yu "Whew! That’s one crate out of thirty…" with vpunch

    show yuri_autumn at left
    show yuri tired2 at left
    with move

    show aiden_autumn at right
    show aiden shock3 at right
    with dissolve

    voice audio.aiden_v_shock1e1
    a "Whoa, whoa, whoa. What are you trying to do here, Yuri?"

    show yuri talk2 at left
    voice audio.yuri_v_oh1a
    yu "Oh, umm… Well, you see, I figured I'd work on clearing out the shed since I overheard Dad on the phone talking about needing storage space."

    hide aiden_autumn
    hide aiden shock3
    show aiden2_autumn at right
    show aiden2 worry2 at right
    voice audio.aiden_v_confused2a2
    a "Why didn’t you ask any of us for help? I mean… that's a lot of lifting for just one person, you know. "

    show yuri irked1 at left
    voice audio.yuri_v_hmph1a
    yu "Hmph! I’m a lot stronger than I look, Aiden. "
    yu "Besides, you guys are all so busy already. "

    show yuri_autumn at left2
    show yuri irked1 at left2
    show aiden2_autumn at right2
    show aiden2 worry2 at right2
    with move

    hide aiden2_autumn
    hide aiden2 worry2
    show aiden_autumn at right2
    show aiden comp2 at right2
    voice audio.aiden_v_well1a2
    a "Well, there's no way I'll let you lift all these crates by yourself. You could get hurt!"

    show yuri sigh2 at left2
    voice audio.yuri_v_sigh1a
    yu "*sigh* Fine. I was just trying to cut you some slack, you know. "

    show aiden laugh2 at right2
    voice audio.aiden_v_laugh2a1
    a "Haha, don't worry about me – this is really the least I can do after all."
    a "Yoshi and Gramps are doing the big, important work to actually help the camp, so I don't mind taking on the simple tasks."

    show yuri talk3 at left2
    voice audio.yuri_v_conj5a
    yu "You practically do the most work out of all of us! And whether they're simple or not doesn't matter, they're just as important!"
    yu "Give yourself a little more credit, Aiden! You’re a scoutmaster too, just like us!"

    hide aiden_autumn
    hide aiden laugh2
    show aiden2_autumn at right2
    show aiden2 sad4 at right2
    voice audio.aiden_v_conj5a1
    a "It’s just… I can’t help but think everyone else has changed for the better except me, you know?"
    a "I mean… Gramps has loosened up a lot ever since the last term, and Yoshi isn’t such a worrywart anymore."

    show yuri serious3 at left2
    voice audio.yuri_v_no2a1
    yu "That’s not true, Aiden. You’ve seen my dad lately – he’s been in his office chair so much. I wouldn’t be surprised if his butt was glued to it! "
    yu "And Yoshi? I walked up to him staring up at the sky earlier, lost in his thoughts again!"

    show yuri comp2 at left2
    voice audio.yuri_v_encourage2a
    yu "My point is, don’t be so hard on yourself! It’s so not you to be thinking like this!"

    show aiden2 comp3 at right2
    voice audio.aiden_v_laugh1a1
    a "Ahehe, I guess I do sound a bit sulky saying all that, eh?"

    show yuri_autumn at p4_3
    show yuri norm3 at p4_3
    show aiden2_autumn at p4_4
    show aiden2 norm2 at p4_4
    with move

    show goro_autumn at p4_1
    show goro norm1 at p4_1
    show yoshi_autumn at p4_2
    show yoshi happy2 at p4_2
    with dissolve

    voice audio.yoshi_v_yuri1
    yo "We’re here, Yuri!"

    show yoshi shock2 at p4_2
    voice audio.yoshi_v_oh2
    yo "…Oh! Aiden, you’re here too!"

    hide aiden2_autumn
    hide aiden2 norm2
    show aiden_autumn at p4_4
    show aiden happy2 at p4_4
    voice audio.aiden_v_hey2a2
    a "Hey there, Yoshi and Gramps! I just happened to walk by and saw Yuri trying to empty the shed all by herself."

    show yuri irked2 at p4_3
    voice audio.yuri_v_ugh3a
    yu "Ugh, great… Now everyone’s here."

    show goro worry2 at p4_1
    voice audio.goro_v_yuridear1b
    g "Yuri-dear, you should’ve waited for us so we could help."

    show aiden talk2 at p4_4
    voice audio.aiden_v_goro3b
    a "I’m pretty surprised to see you out of the office to begin with, Gramps. Thought you were swamped with Clermont mumbo-jumbo?"

    show goro confused3 at p4_1
    voice audio.goro_v_well1a
    g "Well, aren’t you overworked yourself, Aiden? "

    show aiden bold5 at p4_4
    voice audio.aiden_v_psh1a
    a "Psshhh. I’m fine! "

    show goro talk3 at p4_1
    voice audio.goro_v_anyway2
    g "Anyway, why don’t you all leave this to me? I could use a workout after sitting all day."

    show yoshi happy2 at p4_2
    voice audio.yoshi_v_think4
    yo "Since we’re all here, why don’t we work on it together, sir?"

    show yuri comp4 at p4_3
    voice audio.yuri_v_aww2a
    yu "Aww~ Everyone’s looking out for each other, just like the good ol’ days~"

    show goro happy1 at p4_1
    voice audio.goro_v_ehem1a
    g "*ehem* Should we get started while there’s still a little bit of sun? It’ll be unbearably cold later."

    show yoshi happy1 at p4_2
    show yuri bold2 at p4_3
    show aiden bold2 at p4_4
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
    play sound sfx_boxesdrop
    $ renpy.pause (1.0, hard=True)
    play sound sfx_sweep
    $ time_transition_day_to_sunset_fall()
    $ renpy.pause (2.0, hard=True)

    $ location = location_shed
    $ time = timeline_timesunset
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_outshed_autumn_sunset_crates with fade
    play bgsound sfxloop_leaves loop
    play music buddy_oath_casual loop

    play sound sfx_boxesdrop
    show yoshi_autumn at left2
    show yoshi confused2 at left2
    show yuri_autumn at right2
    show yuri norm1 at right2
    voice audio.yoshi_v_amazed1d
    yo "Gee, Yuri, what is in all of these boxes?! They weigh a ton!"

    show yuri comp4 at right2
    voice audio.yuri_v_laugh1a1
    yu "I-It’s just some stuff I like to keep around~ Hihi~"

    show yoshi think2 at left2
    voice audio.yoshi_v_think1a
    yo "I didn’t realize that most of the stuff in the shed belonged to you… I thought it was full of tools or something…"

    show yuri tease2 at right2
    voice audio.yuri_v_well4a
    yu "W-Well… they are tools… in a way."

    show yoshi_autumn at left
    show yoshi think2 at left
    show yuri_autumn at center
    show yuri tease2 at center
    with move

    show goro_autumn at right
    show goro confused2 at right
    with dissolve

    voice audio.goro_v_think3
    g "Uhh… I have a small box here that says \“Don’t Touch\”…?"

    show yuri_autumn at right
    show yuri irked2 at right
    with move

    show yuri_autumn at center
    show yuri irked2 at center
    with move

    voice audio.yuri_v_thanks1a
    yu "So, don’t touch it, thank you!"

    show goro annoy2 at right
    voice audio.goro_v_think3
    g "Uhh… What was in there? Are you keeping dangerous items at camp?"

    show yuri excited2
    voice audio.yuri_v_laugh2a1
    yu "Well, it depends on how you use them~!"

    show goro awkward3 at right
    voice audio.goro_v_sigh1b
    g "I-I’m not going to pry further… I feel like I’ll regret asking."

    show yoshi talk1 at left
    voice audio.yoshi_v_huh5
    yo "It seems like most of the boxes we opened out here so far just have random items in them."

    show goro think2 at right
    voice audio.goro_v_think1a1
    g "Growing up, Yuri did have a hard time letting go of stuff she found interesting. Whenever she started a hobby, she would obsess over it."

    show yuri angry3 at center
    voice audio.yuri_v_angry2a1
    yu "Excuse me?! You’re the last person I wanna hear that from! Hmph! "
    yu "You’re the one who never lets go of stuff!"

    show goro laugh3 at right
    voice audio.goro_v_laugh2c2
    g "Hahaha, I guess that’s true. I do have quite a lot of  art and literature in my collection."

    show yoshi confused2 at left
    voice audio.yoshi_v_why2
    yo "Why are you keeping all of this in the shed anyway? Why not in your room or something?"

    show yuri explain2 at center
    voice audio.yuri_v_think1a1
    yu "My room is kinda full… so I had to put them somewhere…"

    show yoshi awkward4 at left
    voice audio.yoshi_v_oh3
    yo "Oh… "

    show yuri irked1 at center
    voice audio.yuri_v_what1a
    yu "Now why are you two giving me that look?!"
    yu "Hmph! This is why I was trying to do this on my own!"

    show yoshi_autumn at p4_2
    show yoshi norm2 at p4_2
    show yuri_autumn at p4_3
    show yuri irked1 at p4_3
    show goro_autumn at p4_4
    show goro norm1 at p4_4
    with move

    play sound sfx_boxesdrop
    show aiden_autumn at p4_1
    show aiden happy1 at p4_1
    with move

    voice audio.aiden_v_okay1a
    a "Okay, Yuri! This is the last box with your name on it in there."
    a "I swept the shed spotless too. Never realized there was so much space in there without all this stuff!"

    show yuri happy2 at p4_3
    voice audio.yuri_v_thanks1b
    yu "Thank you guys for your hard work! I really appreciate it."
    yu "I can take it from here and sort out the things I want to keep."

    show aiden happy3 at p4_1
    voice audio.aiden_v_alright1a3
    a "Alright! Then if you two don't mind, I could use some big muscles to sort the other stuff. "
    a "There's a few old tools that sorely need replacing, and we have some rusted and broken stuff we need to dispose of too."

    show yoshi happy1 at p4_2
    voice audio.yoshi_v_sure2
    yo "Sure, Aiden!"

    show aiden_autumn at p5_1
    show aiden norm1 at p5_1
    show yoshi_autumn at p5_2
    show yoshi norm1 at p5_2
    show goro_autumn at p5_3
    show goro norm1 at p5_3
    show yuri_autumn at p5_5
    show yuri confused2 at p5_5
    with move

    voice audio.yuri_v_think1a1
    yu "Hmm, okay, let’s see…"

    show yuri shock5 at p5_5
    voice audio.yuri_v_shock2a
    yu "*gasp*"

    hide yuri_autumn
    hide yuri shock5
    show yuri2_autumn at p5_5
    show yuri2 fangirl2 at p5_5
    voice audio.yuri_v_omg1a
    yu "OMG!!!!" with vpunch

    show aiden_autumn at p4_1
    show aiden panic1 at p4_1
    show yoshi_autumn at p4_2
    show yoshi panic1 at p4_2
    show goro_autumn at p4_3
    show goro panic4 at p4_3
    show yuri2_autumn at p4_4
    show yuri2 fangirl2 at p4_4
    with move

    voice audio.goro_v_worry3a2
    g "What happened?!"

    show yuri2 laugh3 at p4_4
    voice audio.yuri_v_excited1a
    yu "You guys won’t believe what I just found!!"

    show cg fade at truecenter
    show fx1 at fx_pos
    with dissolve

    voice audio.goro_v_yuri7a
    g "Yuri… You’re going to give me a heart attack. I thought you hurt yourself or something…"

    voice audio.yuri_v_rush1d1
    yu "You don’t understand! I’ve been looking for this old thing for ages! I can’t believe it was in the shed all these years!"

    voice audio.aiden_v_confused2a2
    a "What is it anyways…? Kinda looks like an ancient book witches use to cast spells."

    voice audio.yuri_v_aiden8a
    yu "Aiden! I can’t believe you don’t know what this is! We used to write in this book when we were younger, remember?"

    voice audio.yoshi_v_oh2
    yo "OH! I recognize that book!"

    voice audio.yoshi_v_yuri5
    yo "Isn’t that your journal, Yuri?!"

    voice audio.yuri_v_agree1c1
    yu "Yes! Oh, I’m so glad you remember it, Yoshi."

    hide cg fade
    hide fx1
    with dissolve

    show aiden comp3 at p4_1
    show yoshi norm3 at p4_2
    show goro confused1 at p4_3
    hide yuri2_autumn
    hide yuri2 fangirl2
    show yuri_autumn at p4_4
    show yuri excited3 at p4_4
    voice audio.aiden_v_sheesh1b
    a "Sheesh… I honestly forgot that thing existed… I think the last time I saw it was when we were still scouts!"
    a "It’s looking a little rough, too… Are those water stains all over it?"
    yu "Yeah… the box it was in must have gotten wet somehow… But it’s still readable for the most part!!"

    hide goro_autumn
    hide goro confused1
    show goro2_autumn at p4_3
    show goro2 confused3 at p4_3
    voice audio.goro_v_think1b1
    g "I don’t think I’ve seen this journal of yours before…"

    show yuri explain1 at p4_4
    voice audio.yuri_v_goro1a
    yu "Yeah, because you were a busy scoutmaster back then. "
    yu "This is where I used to put all my favorite memories with you guys! It was so much fun to write about what we were up to."

    show yuri talk3 at p4_4
    voice audio.yuri_v_aww1b
    yu "I really, really wanted to show this to last year’s scouts and give them a little history of the camp…"
    yu "But I couldn’t because I thought this thing was lost forever."

    show yoshi confused2 at p4_2
    voice audio.yoshi_v_think1a
    yo "Is that why you gave a journal just like this to some of the scouts when they first arrived at camp?"

    show yuri happy1 at p4_4
    voice audio.yuri_v_yeah1b1
    yu "Yeah~! It was so wonderful to be able to write down memories, and I wanted them to be able to experience that as well!"
    yu "You guys know I've always had a passion for writing, even when I was younger. I thought it would be great to share that with the scouts, so they'd be able to look fondly back on their experiences here one day!"

    show yuri laugh1 at p4_4
    voice audio.yuri_v_laugh1a1
    yu "I made it my personal tradition to offer a journal when I see scouts full of inspiration, such as Mr. Akatora and Mr. Nagame!"

    show aiden tease2 at p4_1
    voice audio.aiden_v_comeon2a
    a "Oh, come on, you just look at their application forms and see who wrote “writing” as their hobbies."

    show yuri pout2 at p4_4
    voice audio.yuri_v_hmph1b
    yu "Hmph, not at all, Aiden! "

    show goro2 happy2 at p4_3
    voice audio.goro_v_actually1a
    g "Now I’m actually curious what the camp was like back then from the eyes of a scout…"

    show yuri excited2 at p4_4
    voice audio.yuri_v_alright1d1
    yu "Alright, let’s take a peek then, shall we?"

    show cg fade at truecenter
    show fx2 2 at fx_pos
    with dissolve

    voice audio.yuri_v_kyaa1b
    yu "Kyaaaa!!! Look at this, you guys~!!"

    yo "{i}(This is… our first picture together!){/i}"
    yo "{i}(Seeing it makes me remember what happened on that day so clearly…){/i}"

    hide screen location
    hide screen timeline
    hide screen quick_menu
    $quick_menu = False
    scene cg white with Dissolve(2.0)
    $past_scene = True

    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    voice audio.yyuri_v_rush3b
    yu "Come on, guys! Hurry up! We have to take a picture on a special day like this!"

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
    $ day = "??"
    $ time = timeline_timeday
    $ season = season_summer
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_campgrounds_past_day with fade
    play music camping_time loop

    show yaiden_casual at left
    show yaiden pain3 at left
    show yyuri_camp2 at left3
    show yyuri excited1 at left3
    show yyoshi_camp at right
    show yyoshi comp3 at right
    voice audio.yaiden_v_yuri7
    a "Y-Yuri! C-Can you move a little?! You’re stepping on my foot!"

    show yyuri excited2 at left3
    voice audio.yyuri_v_andre1a
    yu "Mr. Andre, I think it would be better if you were in the shot too!"
    yu "After all, this is Aiden’s first official day as a helper here! "

    show yaiden_casual at p4_2
    show yaiden norm1 at p4_2
    show yyuri_camp2 at p4_3
    show yyuri excited1 at p4_3
    show yyoshi_camp at p4_4
    show yyoshi comp3 at p4_4
    with move

    show andre_camp at p4_1
    show andre comp2 at p4_1
    with dissolve

    voice audio.andre_v_response2a2
    u "It’s fine! I’ll take the picture; this is your moment after all!"

    show yyuri_camp2 at p4_4
    show yyuri excited1 at p4_4
    show yyoshi_camp at p4_3
    show yyoshi happy1 at p4_3
    with move

    voice audio.yyoshi_v_congrats1
    yo "Congratulations on finally being a part of Camp Buddy, Aiden!"
    yo "I wish you were a scout too, but this works just as well! As long as we get to hang out and have fun together!"

    show yaiden laugh1 at p4_2
    voice audio.yaiden_v_laugh1a1
    a "Hehe, it’s all thanks to you, Yoshi! You’ve been vouching for me since day one! "

    show yyoshi comp5 at p4_3
    voice audio.yyoshi_v_disagree1a
    yo "Nah, you’re the one who proved yourself here! You’ve been super helpful around the camp!"

    show yaiden happy1 at p4_2
    voice audio.yaiden_v_well1a1
    a "Still, it wouldn’t have happened if you hadn’t been showing Sir Goro every little thing I was working on! "

    show yyoshi laugh1 at p4_3
    voice audio.yyoshi_v_laugh1
    yo "Haha, I guess it’s a team effort then!"

    show yyuri angry2 at p4_4
    voice audio.yyuri_v_goro9c
    yu "Dad!!! Mom!!! What’s taking you so long?!" with vpunch

    show andre_camp at p5_1
    show andre norm1 at p5_1
    show yyuri_camp2 at p5_4
    show yyuri angry2 at p5_4
    show yyoshi_camp at p5_3
    show yyoshi laugh1 at p5_3
    show yaiden_casual at p5_2
    show yaiden happy1 at p5_2
    with move

    show ygoro_camp at p5_5
    show ygoro shock2 at p5_5
    with dissolve

    hide yyuri_camp2
    hide yyuri angry2
    show yyuri_camp2 at p5_4
    show yyuri angry2 at p5_4
    voice audio.ygoro_v_shock1a
    g "A-Ah… Coming, dear! "

    show andre_camp at p6_1
    show andre norm1 at p6_1
    show yyuri_camp2 at p6_4
    show yyuri angry2 at p6_4
    show yyoshi_camp at p6_3
    show yyoshi laugh1 at p6_3
    show yaiden_casual at p6_2
    show yaiden happy1 at p6_2
    show ygoro_camp at p6_5
    show ygoro shock2 at p6_5
    with move

    show vera_casual at p6_6
    show vera annoy1 at p6_6
    with dissolve

    show ygoro disappoint2 at p6_5
    voice audio.ygoro_v_vera5
    g "Vera, let’s settle this later, alright?"

    show vera annoy2 at p6_6
    #voice audio.vera_v_
    v "Hmph. Fine."

    show ygoro talk1 at p6_5
    voice audio.ygoro_v_rush2b1
    g "Come on, join us in the pic—"

    hide vera_casual
    hide vera annoy2
    with dissolve

    show andre_camp at p5_1
    show andre norm1 at p5_1
    show yyuri_camp2 at p5_4
    show yyuri angry2 at p5_4
    show yyoshi_camp at p5_3
    show yyoshi laugh1 at p5_3
    show yaiden_casual at p5_2
    show yaiden happy1 at p5_2
    show ygoro_camp at p5_5
    show ygoro sad1 at p5_5
    with move

    g "..."

    show yyuri_camp2 at p5_5
    show yyuri angry3 at p5_5
    with move

    show ygoro_camp at p5_4
    show ygoro norm3 at p5_4
    show yyuri_camp2 at p5_5
    show yyuri angry3 at p5_5
    with move

    hide yyoshi_camp
    hide yyoshi laugh1
    show yyoshi_camp at p5_3
    show yyoshi laugh1 at p5_3
    voice audio.yyuri_v_rush1d2
    yu "Let her be, Dad! Just come here already!"

    show ygoro comp2 at p5_4
    voice audio.ygoro_v_sorry2a
    g "A-Ah, yes, of course"

    show yyoshi confused1 at p5_3
    voice audio.yyoshi_v_sirgoro7
    yo "Is everything alright, Sir Goro?"

    show ygoro comp5 at p5_4
    voice audio.ygoro_v_oh2
    g "Oh, haha! It’s nothing! My wife’s just a little tired, is all!"

    show yyuri happy1 at p5_5
    voice audio.yyuri_v_alright1a1
    yu "Alright, Mr. Andre! We’re ready!"

    show andre happy3 at p5_1
    voice audio.andre_v_camera1b
    u "Okay, 3… 2… 1… Cheese!"

    play sound sfx_camerashot
    show yyuri laugh3 at p5_5
    show yaiden grin1 at p5_2
    show yyoshi grin2 at p5_3
    show ygoro grin3 at p5_4
    with flash

    show andre laugh3 at p5_1
    voice audio.andre_v_amazed1b1
    u "Wow, would you look at that! It’s already printing! That’s really cool."

    show yyuri_camp2 at p5_2
    show yyuri excited3 at p5_2
    show yaiden_casual at p5_3
    show yaiden norm1 at p5_3
    show yyoshi_camp at p5_4
    show yyoshi norm1 at p5_4
    show ygoro_camp at p5_5
    show ygoro norm1 at p5_5
    with move

    voice audio.yyuri_v_request1a
    yu "Can I see? Can I see?!"

    show yyuri laugh3 at p5_2
    voice audio.yyuri_v_kyaa1c
    yu "Kyaa!! We look so cute here!" with vpunch

    show ygoro happy1 at p5_5
    voice audio.ygoro_v_yuri2
    g "If you want, I can frame it for you to hang inside the office, Yuri."

    show yyuri bold2 at p5_2
    voice audio.yyuri_v_no2a1
    yu "No way! This is gonna be in my album!"

    show ygoro laugh1 at p5_5
    voice audio.ygoro_v_laugh1b
    g "Hahaha, of course."

    voice audio.ygoro_v_anyway1
    g "Anyway, a special day like this is worth a treat! I bought you guys your favorite Neapolitan ice cream!"

    show yyoshi excited1 at p5_4
    voice audio.yyoshi_v_amazed1c
    yo "Oh wow! Score!"

    show yaiden confused2 at p5_3
    voice audio.yaiden_v_confused2a1
    a "Neapolitan? What’s that?"

    show yyuri happy1 at p5_2
    voice audio.yyuri_v_aiden3a
    yu "It’s three ice-cream flavors in one, Aiden! Dad always gets this one since we can’t agree on just one! "
    yu "And besides, the colors match us too! Strawberry for me, vanilla for Dad and chocolate for Yoshi!"

    show yyoshi comp5 at p5_4
    voice audio.yyoshi_v_laugh3
    yo "Hehe, since Aiden is an official part of our squad now, we should add one more flavor next time!"

    show yaiden excited3 at p5_3
    voice audio.yaiden_v_oh1a
    a "Oh! That’d be nice! "

    show yyuri bold2 at p5_2
    voice audio.yyuri_v_laugh1a2
    yu "It should definitely be something green! That’s totally your color! "

    show yyoshi annoy3 at p5_4
    voice audio.yyoshi_v_yuri9a
    yo "Yuri, did you really have to narrow it down like that? You should let Aiden pick whatever he likes!"

    show yaiden comp5 at p5_3
    voice audio.yaiden_v_alright3a
    a "It’s okay, Yoshi! I rarely have the chance to eat ice cream, so I don’t know what my favorite flavor is yet!"

    show ygoro play2 at p5_5
    voice audio.ygoro_v_well1
    g "Well, you all might want to eat up before it melts."

    show andre relief2 at p5_1
    voice audio.andre_v_service1a
    u "I’ll serve some up at the mess hall! Just follow me!"

    hide andre_camp
    hide andre relief2
    with dissolve

    show yyuri_camp2 at left3
    show yyuri excited2 at left3
    with move
    voice audio.yyuri_v_rush1c1
    yu "Come on, Aiden! Let’s have you try all the flavors first!"

    show yaiden panic3 at p5_3
    voice audio.yaiden_v_hey1d
    a "H-Hey, Y-Yuri…!"

    hide yyuri_camp2
    hide yyuri excited2
    hide yaiden_casual
    hide yaiden panic3
    with moveoutleft

    show yyoshi_camp at left2
    show yyoshi happy2 at left2
    show ygoro_camp at right2
    show ygoro norm1 at right2
    with move

    voice audio.yyoshi_v_sirgoro7
    yo "Aren’t you coming, Sir Goro?"

    show ygoro comp2 at right2
    voice audio.ygoro_v_yoshi2
    g "I’ll catch up after a phone call. Please go ahead, Yoshinori."

    show yyoshi comp5 at left2
    voice audio.yyoshi_v_sir2
    yo "I’ll save the vanilla flavor for you, sir!"

    show ygoro laugh2 at right2
    voice audio.ygoro_v_laugh1b
    g "Hahaha, thank you!"

    show yyoshi laugh2 at left2
    voice audio.yyoshi_v_bye5
    yo "Seeya!"

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

    $ location = location_shed
    $ day = "01"
    $ time = timeline_timesunset
    $ season = season_autumn
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_outshed_autumn_sunset_crates with fade
    play bgsound sfxloop_leaves loop
    play music buddy_oath_casual loop

    show aiden_autumn at p4_1
    show aiden norm1 at p4_1
    show yoshi_autumn at p4_2
    show yoshi norm3 at p4_2
    show goro_autumn at p4_3
    show goro norm1 at p4_3
    show yuri_autumn at p4_4
    show yuri excited1 at p4_4

    show cg fade at truecenter
    show fx2 2 at fx_pos

    voice audio.yuri_v_amazed1c
    yu "Wow… We all look so different here…"

    voice audio.goro_v_think1a1
    g "Hmm… When was this taken again?"

    voice audio.yuri_v_goro2b
    yu "It’s around the time you got me my first camera, Dad~! Almost a decade ago, during Camp Buddy's first-ever term! "

    voice audio.aiden_v_sheesh1b
    a "Sheesh, I barely recognize myself there. Has it really been that long…?"

    voice audio.goro_v_satisfied2a
    g "Seeing us like this feels so nostalgic… It really takes me back…"

    voice audio.aiden_v_laugh1d1
    a "Hehehe~ How’d all your hair turn gray in less than a decade, Gramps?"

    voice audio.goro_v_hmph1a
    g "Hmph. Speak for yourself, Aiden. It’s hard to believe that a twig like you would bulk up in a couple years."

    voice audio.aiden_v_oho1a
    a "Talking about my glow-up, eh? I’ll take that as a compliment."

    voice audio.yuri_v_aww2a
    yu "Aww, but you and Yoshi looked so youthful with your skinny, twinky bodies! Not that I have complaints about your muscles now~"

    hide cg fade
    hide fx2 2
    with dissolve

    hide yoshi_autumn
    hide yoshi norm3
    show yoshi2_autumn at p4_2
    show yoshi2 think5 at p4_2
    voice audio.yoshi_v_sigh3a
    yo "Time sure has flown by, hasn’t it?"

    show yuri comp4 at p4_4
    voice audio.yuri_v_laugh1a1
    yu "Yeah, I miss being a scout – it was the happiest time of my life!  "

    show goro talk3 at p4_3
    voice audio.goro_v_ehem1a
    g "*ehem* Anyway, why don’t we finish up here before you get too carried away, Yuri-dear? "

    show yuri happy2 at p4_4
    voice audio.yuri_v_actually1a
    yu "Actually… I got all the things I need from the shed. I’ll leave the cleanup to you guys~! "

    show aiden confused2 at p4_1
    voice audio.aiden_v_confused1a1
    a "Eh? Where are you going?"

    show yuri angry2 at p4_4
    voice audio.yuri_v_hmph1a
    yu "I haven’t seen my journal in years! Let me have my moment! "
    yu "Though it’ll probably take me a while to read through all the entries…  I’ll let you guys know if there’s some cool stuff in here!"

    show yuri excited3 at p4_4
    voice audio.yuri_v_bye1a1
    yu "Byeeee~!"

    hide yuri_autumn
    hide yuri excited3
    with moveoutright

    show aiden_autumn at left
    show aiden confused2 at left
    show yoshi2_autumn at center
    show yoshi2 think5 at center
    show goro_autumn at right
    show goro sigh1 at right
    with move

    voice audio.goro_v_sigh1b
    g "*sigh* You really can’t stop her when she starts obsessing over something."

    show aiden laugh1 at left
    voice audio.aiden_v_laugh2b1
    a "Hahaha, what else is new?"

    voice audio.aiden_v_anyway1b
    a "Anyways, I think all we need to do is take the trash out, then we’re done here!"

    show aiden happy1 at left
    a "Why don’t you guys give me a hand, and I’ll treat you both to a beer?"

    show goro happy1 at right
    voice audio.goro_v_agree7a
    g "Sounds good to me. I could use a little stress relief after today. What do you say, Yoshinori?"

    hide yoshi2_autumn
    hide yoshi2 think5
    show yoshi_autumn at center
    show yoshi shock3 at center
    voice audio.yoshi_v_ah3
    yo "A-Ah, yes! I’d be happy to join!"

    show aiden happy3 at left
    voice audio.aiden_v_amazed3b
    a "Great! Let’s go then!"

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black
    hide screen location
    hide screen timeline
    hide screen quick_menu
    $quick_menu = False
    with fade
    play sound sfx_boxesdrop
    $ renpy.pause (2.0, hard=True)
    $ time_transition_sunset_to_night_fall()

    $ location = location_alley
    $ time = timeline_timenight
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_alley_autumn_night with fade
    play bgsound sfxloop_night loop
    play music buddy_oath_acoustic loop

    show goro_autumn at left
    show goro norm2 at left
    show yoshi2_autumn at center
    show yoshi2 think1 at center
    show aiden_autumn at right
    show aiden happy2 at right
    voice audio.aiden_vs2_line1
    a "Thanks again for helping me with the chores, guys. "

    show goro laugh3 at left
    voice audio.goro_vs2_line1
    g "It’s no problem, Aiden. I rarely get the chance to help."

    voice audio.goro_vs2_line2
    g "You’ve pretty much kept our camp running over the years."

    show aiden comp5 at right
    voice audio.aiden_vs2_line2
    a "Aww, Gramps… It’s always so nice to hear a compliment from you."

    hide goro_autumn
    hide goro laugh3
    show goro2_autumn at left
    show goro2 disappoint3 at left
    voice audio.goro_vs2_line3
    g "H-Hey, I always give them out… when they’re due."

    show aiden laugh1 at right
    voice audio.aiden_vs2_line3
    a "Hahaha, that's true, but it's hard to please you, Gramps! You only praise us once in a blue moon!"

    hide goro2_autumn
    hide goro2 disappoint3
    show goro_autumn at left
    show goro talk1 at left
    voice audio.goro_vs2_line4
    g "Well, I was telling Yoshinori earlier today how I’ve been trying to be more easygoing around you guys… especially after how I was the past few years."

    show aiden relief2 at right
    voice audio.aiden_vs2_line4
    a "Don’t sweat it, Gramps. We know you just had plenty of management matters to deal with."

    show goro happy1 at left
    voice audio.goro_vs2_line5
    g "While I’m at it, thanks again for treating us to these nice cold drinks. It’s been a while since I’ve had a beer like this."

    hide aiden_autumn
    hide aiden relief2
    show aiden2_autumn at right
    show aiden2 scared2 at right
    voice audio.aiden_vs2_line5
    a "Shh, Gramps! Don’t be so obvious about it! We’re not supposed to have them in public!"

    show goro panic4 at left
    voice audio.goro_vs2_line6
    g "What?! I used to drink these outside all the time! When did that change?"

    show aiden2 annoy6 at right
    voice audio.aiden_vs2_line6
    a "Sheesh, seriously? I thought you of all people would know the local rules!"

    hide aiden2_autumn
    hide aiden2 annoy6
    show aiden_autumn at right
    show aiden confused2 at right
    voice audio.aiden_vs2_line7
    a "You knew about that too, right, Yoshi? You’ve been out drinking with me before!"

    show yoshi2 explain1 at center
    yo "..."

    hide goro_autumn
    hide goro panic4
    show goro2_autumn at left
    show goro2 confused2 at left
    voice audio.goro_vs2_line7
    g "Yoshinori?"

    hide yoshi2_autumn
    hide yoshi2 explain1
    show yoshi_autumn at center
    show yoshi shock2 at center
    voice audio.yoshi_vs2_line1
    yo "A-Ah! Sorry, what were you guys talking about?"

    show goro2 worry3 at left
    voice audio.goro_vs2_line8
    g "Are you alright, Yoshinori? You seem to be spacing out again."

    show yoshi worry2 at center
    voice audio.yoshi_vs2_line2
    yo "O-Oh, no, sir! I’m fine…!"

    show aiden talk5 at right
    voice audio.aiden_vs2_line8
    a "Come on, something’s definitely up! You’ve barely said anything ever since Yuri showed us that picture!"

    hide goro2_autumn
    hide goro2 worry3
    show goro_autumn at left
    show goro talk3 at left
    voice audio.goro_vs2_line9
    g "That’s true. Did it bring up a bad memory or something?"

    hide yoshi_autumn
    hide yoshi worry2
    show yoshi2_autumn at center
    show yoshi2 comp3 at center
    voice audio.yoshi_vs2_line3
    yo "N-No, the opposite, actually! Seeing us all together back then made me think about all the things that happened in the past. "

    hide aiden_autumn
    hide aiden talk5
    show aiden2_autumn at right
    show aiden2 think6 at right
    voice audio.aiden_vs2_line9
    a "Hmm? What do you mean exactly?"

    show yoshi2 explain2 at center
    voice audio.yoshi_vs2_line4
    yo "Well… back then, Sir Goro was our scoutmaster, and we were the ones having a great summer at camp."

    voice audio.yoshi_vs2_line5
    yo "…Thinking about how fun it was, it really made me want to relive those moments again."

    show goro comp2 at left
    voice audio.goro_vs2_line10
    g "I look back on those days fondly as well. Having scouts like you in the very first term really helped solidify my passion for Camp Buddy."

    hide aiden2_autumn
    hide aiden2 think6
    show aiden_autumn at right
    show aiden play5 at right
    voice audio.aiden_vs2_line10
    a "Hehe, those were some of our best memories together, after all."

    show yoshi2 talk1 at center
    voice audio.yoshi_vs2_line6
    yo "Yeah… but the thing is, I feel like I’ve forgotten what it’s like to enjoy myself without worrying about everything else."

    voice audio.yoshi_vs2_line7
    yo "It made me realize that ever since I became a scoutmaster, I’ve been so single-mindedly focused on the present and future of Camp Buddy…"

    hide goro_autumn
    hide goro comp2
    show goro2_autumn at left
    show goro2 talk2 at left
    voice audio.goro_vs2_line11
    g "I think I’m partly to blame for that. The time I left you in charge on your own without proper guidance caused a far greater burden on you."

    hide yoshi2_autumn
    hide yoshi2 talk1
    show yoshi_autumn at center
    show yoshi worry4 at center
    voice audio.yoshi_vs2_line8
    yo "A-Ah, that’s not what I meant, sir!"

    voice audio.yoshi_vs2_line9
    yo "Becoming a scoutmaster there has always been my dream. And now that I've achieved that goal, it makes me look back at why I wanted it in the first place."

    hide goro2_autumn
    hide goro2 talk2
    show goro_autumn at left
    show goro comp2 at left
    voice audio.goro_vs2_line12
    g "You know, Yoshinori, you were such a passionate and caring scout that you constantly inspired me to keep fighting for Camp Buddy. "

    voice audio.goro_vs2_line13
    g "I hope I can return the favor and help you enjoy your time at camp again."

    show yoshi comp2 at center
    voice audio.yoshi_vs2_line10
    yo "Sir Goro…"

    show aiden talk1 at right
    voice audio.aiden_vs2_line11
    a "Yeah, I miss the old Yoshi too! You were so cheerful and carefree back then, and now you spend so much of your time worrying!  "

    voice audio.aiden_vs2_line12
    a "We just gotta get you to stop overthinking things, hehe~"

    hide yoshi_autumn
    hide yoshi comp2
    show yoshi2_autumn at center
    show yoshi2 think6 at center
    voice audio.yoshi_vs2_line11
    yo "Well… I guess it’s mostly because I’ve been far less busy now that we’re in the off-season."

    voice audio.yoshi_vs2_line12
    yo "Normally, I’d use my time to think about what activities we’d be doing next, or how to improve everyone’s experiences at camp."

    show yoshi2 think5 at center
    voice audio.yoshi_vs2_line13
    yo "With the scouts gone, I don’t have as many responsibilities… and I guess that’s given me a lot of time to think about myself for once."

    hide yoshi2_autumn
    hide yoshi2 think5
    show yoshi_autumn at center
    show yoshi worry2 at center
    voice audio.yoshi_vs2_line14
    yo "Ah, I’m sorry you two have to hear me ramble about all this!"

    show aiden comp2 at right
    voice audio.aiden_vs2_line13
    a "No, no, it’s fine, Yoshi. You know we’re always here to listen and help you with whatever’s going through your head!"

    show goro happy1 at left
    voice audio.goro_vs2_line14
    g "Exactly. We all have your back here, Yoshinori."

    show yoshi comp2 at center
    voice audio.yoshi_vs2_line15
    yo "Th-Thank you both, really."

    show aiden comp5 at right
    voice audio.aiden_vs2_line14
    a "No problem, Yoshi~ But I think that’s enough of that cheesy talk! We’re having a drink to relax and have fun!"

    hide goro_autumn
    hide goro happy1
    show goro2_autumn at left
    show goro2 worry2 at left
    voice audio.goro_vs2_line15
    g "To be honest, I'm a little concerned about the authorities seeing us with these beers now."

    show aiden wink2 at right
    voice audio.aiden_vs2_line15
    a "Aww, come on, Gramps, live a little! What’s life if you don’t break the rules every once in a while?"

    show yoshi laugh2 at center
    voice audio.yoshi_vs2_line16
    yo "Hahaha! Now this DOES feel like old times! You used to be such a troublemaker, Aiden."

    show aiden play3 at right
    voice audio.aiden_vs2_line16
    a "Hey, I don’t think we ever got ourselves into anything serious! Right, Gramps?"

    show goro2 sigh1 at left
    voice audio.goro_vs2_line16
    g "*sigh* I’m suddenly starting to worry about you as a scoutmaster, Aiden."

    show aiden annoy3 at right
    voice audio.aiden_vs2_line17
    a "Don’t start acting like you two are so innocent! The three of us drank plenty during last summer term!"

    hide goro2_autumn
    hide goro2 sigh1
    show goro_autumn at left
    show goro think2 at left
    voice audio.goro_vs2_line17
    g "With all the new scouts coming in next year, we’ll probably have to stop that. We don’t want a camper catching us, after all."

    show yoshi happy1 at center
    voice audio.yoshi_vs2_line17
    yo "Haha, Yuri would be glad if we stopped. She’s always scolding us for drinking anyway. "

    show goro sigh3 at left
    voice audio.goro_vs2_line18
    g "*sigh* It is difficult to relax for a drink when she’s upset with us."

    show aiden tease1 at right
    voice audio.aiden_vs2_line18
    a "Hehe, have a couple more of those, and you'll be too \"relaxed\" to let her bug you!"

    hide goro_autumn
    hide goro sigh3
    show goro2_autumn at left
    show goro2 annoy2 at left
    voice audio.goro_vs2_line19
    g "Hmph, you think something like this is enough to affect me? I drink much stronger alcohol, you know. "

    show aiden talk2 at right
    voice audio.aiden_vs2_line19
    a "That’s true! I’ve seen how much you were able to put down before! I think those muscles play a big role in it, also~"

    voice audio.aiden_vs2_line20
    a "Your jacked bod is way tougher than a few beers!"

    show goro2 play3 at left
    voice audio.goro_vs2_line20
    g "You and Yoshinori as well. I mentioned it earlier, but it’s amazing to see how much the two of you have bulked up over the recent years."

    voice audio.goro_vs2_line21
    g "I understand how Aiden did it, since I see him working out pretty regularly. But I wasn’t aware that you trained as well, Yoshinori."

    show yoshi laugh1 at center
    voice audio.yoshi_vs2_line18
    yo "Haha, I have joined Aiden for a few of his workout sessions. But I do try and keep myself in the best shape possible so that I have no issues with our activities!"

    voice audio.yoshi_vs2_line19
    yo "We are an outdoor-themed camp, after all!"

    show aiden pout1 at right
    voice audio.aiden_vs2_line21
    a "Tsk, tsk, there you go, bringing it back to work, Yoshi! Come on, let the beers loosen you up too!"

    hide yoshi_autumn
    hide yoshi laugh1
    show yoshi2_autumn at center
    show yoshi2 awkward4 at center
    voice audio.yoshi_vs2_line20
    yo "A-Ah…"

    hide goro2_autumn
    hide goro2 play3
    show goro_autumn at left
    show goro happy2 at left
    voice audio.goro_vs2_line22
    g "Aiden's right. Besides, it's not often we get to hang out together like this."

    hide yoshi2_autumn
    hide yoshi2 awkward4
    show yoshi_autumn at center
    show yoshi comp3 at center
    voice audio.yoshi_vs2_line21
    yo "Yeah, you guys are right…! "

    show aiden happy1 at right
    voice audio.aiden_vs2_line22
    a "We should do this more often while it’s still off-season! Who knows, maybe one of these days I'll get to see what kind of drunk Gramps is!"

    show yoshi think2 at center
    voice audio.yoshi_vs2_line22
    yo "Now that you mention it, I’ve only ever seen Sir Goro drunk once."

    show goro talk2 at left
    voice audio.goro_vs2_line23
    g "*ehem* That’s classified information, Yoshinori."

    show aiden tease2 at right
    voice audio.aiden_vs2_line23
    a "I know Yoshi gets really crazy when he's had too much to drink!"

    show yoshi panic3 at center
    voice audio.yoshi_vs2_line23
    yo "A-Aiden…!"

    show aiden comp5 at right
    voice audio.aiden_vs2_line24
    a "Hehe~ I’m just kidding, Yoshi~"

    show yoshi comp2 at center
    voice audio.yoshi_vs2_line24
    yo "But really, thank you both for giving me a different perspective about this off-season."

    voice audio.yoshi_vs2_line25
    yo "Now I have something to look forward to while the scouts aren’t here…"

    $working = False
    $shuffle_menu()
    menu():
        yo "Now I have something to look forward to while the scouts aren’t here…{fast}"
        "Experiencing new things together.":
            $working = True
            $score_aiden += 1
            show yoshi happy1 at center
            voice audio.yoshi_vs2_line26a
            yo "I want to experience new things together – with the people I truly care about!"

            show aiden excited1 at right
            voice audio.aiden_vs2_line25a
            a "Now that’s what I’m talking about! It’s about time we got you back, Yoshi!"

            voice audio.aiden_vs2_line26a
            a "If we can give the scouts unforgettable memories at camp, there’s no reason we can’t do that for ourselves too!"

            show yoshi excited1 at center
            voice audio.yoshi_vs2_line27a
            yo "That’s right, Aiden! It’s never too late to explore what the future has in store for us!"

            voice audio.yoshi_vs2_line28a
            yo "And there’s no one I’d rather share it with than you guys!"
        "Strengthen our bonds even more than before.":
            $working = True
            $score_aiden += 1
            show yoshi happy1 at center
            voice audio.yoshi_vs2_line26b
            yo "I want to strengthen the bonds between us all, even more than before."

            show aiden excited1 at right
            voice audio.aiden_vs2_line25b
            a "Now that’s something I’m totally on board with!"

            voice audio.aiden_vs2_line26b
            a "We shouldn’t miss this chance to spend as much time as we can together!"

            show yoshi excited1 at center
            voice audio.yoshi_vs2_line27b
            yo "You’re right, Aiden! We were all close before, but that doesn't mean there's not room for more!"
        "Cherishing every moment with my family at camp.":
            $working = True
            $score_goro += 1
            show yoshi happy1 at center
            voice audio.yoshi_vs2_line26c
            yo "I’ve been looking far ahead into the future instead of cherishing what’s right in front of me – my family at Camp Buddy."

            show goro comp2 at left
            voice audio.goro_vs2_line24a
            g "That is something I desire as well. "

            voice audio.goro_vs2_line25a
            g "Our time together last summer was a nice reminder of what it was once like, but now is an even better opportunity to get to know one another again."

            show yoshi relief2 at center
            voice audio.yoshi_vs2_line27c
            yo "I agree, sir…! Nothing is more important to me than all of you!"
        "Rediscovering what this place means to me.":
            $working = True
            $score_goro += 1
            show yoshi happy1 at center
            voice audio.yoshi_vs2_line26d
            yo "I want to rediscover what Camp Buddy really means to me!"

            show goro comp2 at left
            voice audio.goro_vs2_line24b
            g "That’s an admirable goal, Yoshinori. Looking back where we came from is a reminder of why we pursued this path."

            voice audio.goro_vs2_line25b
            g "You can count on me to do my best and be there every step of the way."

            show yoshi relief2 at center
            voice audio.yoshi_vs2_line27d
            yo "Thank you, sir…! I know the past will help guide us to a better version of ourselves for the future!"

            voice audio.yoshi_vs2_line28d
            yo "And with you guys by my side, I’m sure I can take on the challenge, no matter what!"
    show aiden tease1 at right
    voice audio.aiden_vs2_line27
    a "Okay, now I’m convinced the drinks really are going to your head."

    voice audio.aiden_vs2_line28
    a "You always were a sappy drunk, Yoshi! "

    show yoshi angry2 at center
    voice audio.yoshi_vs2_line29
    yo "They are not! And I am not!"

    show goro laugh3 at left
    voice audio.goro_vs2_line26
    g "Haha, you do look a tad red, Yoshinori. "

    $ renpy.music.stop(channel='music', fadeout = 2.0)
    show yoshi panic3 at center
    voice audio.yoshi_vs2_line30
    yo "Wh-What? You think so too, Sir Goro?!"

    $location = location_entrance
    scene cg3 starrynight with fade
    play music buddy_oath_acoustic loop
    play bgsound sfxloop_night loop
    voice audio.yoshi_vs3_line1
    yo "{i}(Walking back to Camp Buddy with Aiden and Sir Goro under the starry night sky made me remember some of the fond memories I had with them from back when I was a scout.){/i}"

    voice audio.yoshi_vs3_line2
    yo "{i}(We’ve all stayed here and done the best we could for the same reason, but the time has come to continue where our own stories left off.){/i}"

    voice audio.yoshi_vs3_line3
    yo "{i}(This season marks another chance for us to make just as many amazing memories as we had before!){/i}"

    $ renpy.music.stop(channel='music', fadeout = 5.0)
    scene cg white with Dissolve(5.0)
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
    jump day2
