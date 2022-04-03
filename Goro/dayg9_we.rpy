label day9_goro_we:
    hide yoshi2_biker
    hide yoshi2 sad4
    show yoshi_biker at left2
    show yoshi worry2 at left2
    voice audio.yoshi_vsg24_line1
    yo "What was the reason then…?"

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    show goro disappoint3 at right2
    voice audio.goro_vsg24c_line1
    g "I… I’ve had enough…"

    voice audio.goro_vsg24c_line2
    g "Our journey with Camp Buddy has gone as far as it could…"

    show goro talk1 at right2
    voice audio.goro_vsg24_line3
    g "To start, we’ve received so many amazing chances already and regained what we nearly lost the previous term…"

    voice audio.goro_vsg24_line4
    g "Now we’ve made it even bigger in such a short period of time… and to receive yet another opportunity was just so unexpected... "

    show goro explain2 at right2
    voice audio.goro_vsg24_line5
    g "And honestly... It’s something I don’t aspire for anymore…  "

    hide yoshi_biker
    hide yoshi worry2
    show yoshi2_biker at left2
    show yoshi2 worry4 at left2
    voice audio.yoshi_vsg24b_line3
    yo "Wh-What are you trying to say…?"

    show goro worry3 at right2
    voice audio.goro_vsg24c_line3
    g "I’ve been holding on to this place for so long, sacrificing myself for the camp and everyone else this whole time, but never really pursued my own happiness…"

    voice audio.goro_vsg24b_line6
    g "I just want to move on to a new chapter… And I want you in it…"

    show goro sad3 at right2
    voice audio.goro_vsg24c_line4
    g "I want us to leave the camp…  "

    play music buddy_oath_goro_tragic loop
    show goro worry5 at right2
    voice audio.goro_vsg24b_line8
    g "We’ve both done so much for a such long time. This is our chance to be happy together…!"

    hide yoshi2_biker
    hide yoshi2 worry4
    show yoshi_biker at left2
    show yoshi angry3 at left2
    voice audio.yoshi_vsg24c_line1
    yo "There’s no reason why we can’t be together and still stay at the camp!"

    show goro angry4 at right2
    voice audio.goro_vsg24c_line5
    g "But it’s not just about the camp, Yoshinori…! I thought you’d understand…"

    show yoshi angry2 at left2
    voice audio.yoshi_vsg24c_line2
    yo "How can I understand?! It’s one thing to turn away from a huge opportunity, but now you even want us just to leave everything behind?!"

    hide goro_biker
    hide goro angry4
    show goro2_biker at right2
    show goro2 angry2 at right2
    voice audio.goro_vsg24c_line6
    g "Is that place really your only dream?! Is that the only thing that’ll make you happy?!"

    show yoshi worry4 at left2
    voice audio.yoshi_vsg24c_line3
    yo "I thought it’s what we’ve been fighting for this entire time…!  "

    voice audio.yoshi_vsg24c_line4
    yo "Why are you giving up all of a sudden? That would make everything we’ve been through pointless!"

    hide goro2_biker
    hide goro2 angry2
    show goro_biker at right2
    show goro panic1 at right2
    g "...!"

    show goro upset5 at right2
    voice audio.goro_vsg24c_line7
    g "We… don’t share the same views anymore…"

    voice audio.goro_vsg24c_line8
    g "This was a mistake all along… We can’t spend our futures together… "

    hide yoshi_biker
    hide yoshi worry4
    show yoshi2_biker at left2
    show yoshi2 panic2 at left2
    voice audio.yoshi_vsg24c_line5
    yo "Wh-What…?"

    hide goro_biker
    hide goro upset5
    show goro2_biker at right2
    show goro2 disappoint5 at right2
    voice audio.goro_vsg24c_line9
    g "Being partners was never meant for us…"

    show yoshi2 panic4 at left2
    voice audio.yoshi_vsg24c_line6
    yo "W-Wait, you can’t be serious… "

    show goro2 disappoint3 at right2
    voice audio.goro_vsg24c_line10
    g "We’ve had all these experiences together... all these chances... and we still ended up in the same place as before…"

    show yoshi2 worry5 at left2
    voice audio.yoshi_vsg24c_line7
    yo "Y-You’re letting go of me too…?"

    hide goro2_biker
    hide goro2 disappoint3
    show goro_biker at right2
    show goro angry3 at right2
    voice audio.goro_vsg24c_line11
    g "I’m making this choice for myself… I need to prove that I can find happiness on my own without attaching it to the camp… attaching it to you…"

    voice audio.goro_vsg24c_line12
    g "I’ve spent my whole life giving up everything until there was nothing left to give."

    hide goro_biker
    hide goro angry3
    show goro2_biker at right2
    show goro2 disappoint3 at right2
    voice audio.goro_vsg24c_line13
    g "It’s over."

    show yoshi2 sad4 at left2
    yo "..."

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    play sound sfx_harleydepart
    scene cg black with fade
    yo "{i}I was at loss for words as Goro drove us both home in silence…{/i}"
    yo "{i}I can’t believe that I never saw how he was losing heart for the camp… and for our relationship…{/i}"

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
    play sound sfx_harleyarrive
    scene bg_entrance_winter_night with fade
    play bgsound sfxloop_windy loop

    show goro2_biker at left2
    show goro2 upset1 at left2
    show yoshi2_biker at right2
    show yoshi2 worry2 at right2
    voice audio.yoshi_vsg24c_line8
    yo "Aren’t you coming in…?"

    show goro2 upset3 at left2
    voice audio.goro_vsg24c_line14
    g "I need time… and space..."

    voice audio.goro_vsg24c_line15
    g "I trust you with the camp."

    show yoshi2 panic2 at right2
    voice audio.yoshi_vsg24c_line9
    yo "You can’t leave just like this…"

    hide goro2_biker
    hide goro2 upset3
    show goro_biker at left2
    show goro upset4 at left2
    g "..."

    show yoshi2 panic4 at right2
    voice audio.yoshi_vsg24c_line10
    yo "We can still talk this out. Don’t let everything end this way…"

    play sound sfx_harleystart
    show goro disappoint1 at left2
    g "..."

    show yoshi2 panic3 at right2
    voice audio.yoshi_vsg24c_line11
    yo "Goro…!"

    play sound sfx_harleydeparthard
    hide goro_biker
    hide goro disappoint1
    with dissolve
    show yoshi2 panic1 at right2
    yo "...!"

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black
    hide screen location
    hide screen timeline
    hide screen quick_menu
    $quick_menu = False
    with fade
    $ renpy.pause (3.0, hard=True)
    $ time_transition_night_to_day_winter2()
    $ renpy.pause (2.0, hard=True)
    jump day10_goro_we
