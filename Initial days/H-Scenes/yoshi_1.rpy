label day6_yoshi_1:
    play music on_the_edge loop
    scene sxy1 1 with fade
    voice audio.yoshi_vsxy1_line1
    yo "Khh… It’s really not calming down, huh…? I better get this over with…"

    voice audio.yoshi_vsxy1_line2
    yo "Hnghh…"
    yo "{i}(My body is all heated up, and I can’t stop thinking about him…){/i}"
    $ renpy.pause (2.0, hard=True)

    show sxy1 2 with Dissolve(0.25)
    voice audio.yoshi_vsxy1_line3
    yo "Mmmhh…"
    yo "{i}(If he were here… there’s so many naughty things I would do with him…){/i}"
    $ renpy.pause (2.0, hard=True)

    show sxy1 3 with Dissolve(0.25)
    voice audio.yoshi_vsxy1_line4
    yo "Mfff… Mmmghh…!"
    yo "{i}(I need you so badly…){/i}"

    show sxy1 4 with Dissolve(0.25)
    if d5_aiden == True:
        voice audio.yoshi_vsxy1_line5a
        yo "AIDEN…!!"
    elif d5_goro == True:
        voice audio.yoshi_vsxy1_line5b
        yo "SIR GORO…!!"

    show sxy1 5 with Dissolve(0.25)
    voice audio.yoshi_vsxy1_line6
    yo "Mhh… Hhh…"

    voice audio.yoshi_vsxy1_line7
    yo "Damn… I came so much… This is such a mess…"

    voice audio.yoshi_vsxy1_line8
    yo "It felt so good though… I guess I’ve been holding that in for so long…"

    voice audio.yoshi_vsxy1_line9
    yo "This should be enough for now…"

    jump day6_after
