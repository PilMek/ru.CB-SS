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
    yo "Хн-н…"

    play sound sfx_truckbeep
    show yoshi2 sleepy2 at center
    yo "..."

    play sound sfx_bang
    show yoshi2 awkward4 at center
    voice audio.yoshi_v_worry3a
    yo "Ч-что…? Что происходит?" with vpunch

    show yoshi2_sleep at right
    show yoshi2 shock2 at right
    with move

    voice audio.yoshi_v_what2
    yo "Ч-чего?! Только не говорите мне, что группа строителей уже здесь?! Я думал, они должны были приехать позже?!"

    hide yoshi2_sleep
    hide yoshi2 shock2
    show yoshi2_sleep at right
    show yoshi2 shy4 at right
    yo "Если бы я знал, встал бы пораньше! "

    hide yoshi2_sleep
    hide yoshi2 shy4
    show yoshi_sleep at right
    show yoshi awkward3 at right
    voice audio.yoshi_v_ah4
    yo "Нужно быстрее переодеваться!"

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
    a "О, проснулся, Йоши!"

    show yuri tease2 at left
    voice audio.yuri_v_laugh1a1
    yu "Хи-хи~ Наконец, не ты один теперь первым встал!"

    show yoshi worry2 at right
    voice audio.yoshi_v_why1
    yo "Почему вы меня не разбудили? Я же не знал, что работники так рано приезжают."

    show yuri talk2 at left
    voice audio.yuri_v_oh1a
    yu "Ой, так это не работники, Йоши! Они тут просто доставить строительные материалы!"
    yu "Предполагалось, что они прибыли бы вместе с работниками, но вышло так, что они явились раньше запланированного. "

    show aiden comp5 at center
    voice audio.aiden_v_yeah1a1
    a "Ага, хорошо, что в такую рань я уже не спал, когда они приехали, иначе бы никто не впустил их внутрь! "

    show yoshi sigh1 at right
    voice audio.yoshi_v_relief4
    yo "О, какое облегчение… На секунду я решил, что опоздаю на первый день ремонта."

    show yuri laugh1 at left
    voice audio.yuri_v_yeah1a1
    yu "Если бы не шум снаружи, я бы тоже не проснулась."

    show yoshi talk1 at right
    voice audio.yoshi_v_think1b
    yo "Похоже, что с этих пор нам придётся быть более готовыми к неожиданностям. "

    show yuri talk2 at left
    voice audio.yuri_v_anyway1b
    yu "Кстати говоря, мистер Клермонт дал нам подробные детали на сегодняшнюю повестку дня. Папа попросил меня передать информацию и вам двоим!"

    hide aiden_autumn
    hide aiden comp5
    show aiden2_autumn at center
    show aiden2 confused5 at center
    voice audio.aiden_v_goro5a
    a "А где Дедуля? Не ему бы следовало вводить нас в курс дела?"

    show yuri confused2 at left
    voice audio.yuri_v_think1a1
    yu "Папа уехал супер рано… Сказал, что по делам… хоть и не объяснил, по каким…"

    show yoshi think2 at right
    voice audio.yoshi_v_conj3b
    yo "Судя по вчерашней встрече, думаю, он отправился за разрешениями в мэрию. "
    yo "Но как бы там ни было, мы сможем справиться и сами! "

    show yuri happy1 at left
    voice audio.yuri_v_agree1b1
    yu "Да! Папа назначил выполнить всего два задания – сравнить поставки со списком материалов и подготовиться к приезду рабочих."

    show yoshi talk1 at right
    voice audio.yoshi_v_confident3
    yo "Позволь мне заняться поставкой, Юри. Ты можешь пока подготовить домики, в которых остановятся рабочие. "

    show yuri excited2 at left
    voice audio.yuri_v_oh1a
    yu "Ой, так я уже! Вчера я засиделась после полуночи, протирая полы и раскладывая постельное бельё."
    yu "К тому же, думаю, мне понравится работать с поставками. Учитывая, что всё, что нужно делать - наблюдать за этими… ох… мускулистыми… вспотевшими…  и возможно даже полуголыми мальчиками из доставки… Хи-хи-хи~"

    hide yoshi_autumn
    hide yoshi think2
    show yoshi2_autumn at right
    show yoshi2 awkward3 at right
    voice audio.yoshi_v_yuri6
    yo "Ю-Юри… Тебя снова уже заносит… Убедись, что полностью посчитала количество материалов правильно и всё проверила."

    hide aiden2_autumn
    hide aiden2 confused5
    show aiden_autumn at center
    show aiden tease1 at center
    voice audio.aiden_v_laugh1c1
    a "Хе, зная Юри, она всё-всё проверит~ "

    show yuri relief2 at left
    voice audio.yuri_v_fujo1b1
    yu "Ах… Быть благословлённой смотреть столь чудное шоу для меня одной~ Как же я обожаю свою работу!"

    show yoshi2 angry5 at right
    voice audio.yoshi_v_ehem1a
    yo "*кхем* Ладно, информация о том, сколько работников приезжает сегодня уже пришла?"

    show yuri talk2 at left
    voice audio.yuri_v_agree1a3
    yu "А, да, ожидается, что первая группа будет где-то из тридцати человек."

    hide aiden_autumn
    hide aiden tease1
    show aiden2_autumn at center
    show aiden2 panic4 at center
    voice audio.aiden_v_shock2a1
    a "Блин блинский! Хочешь сказать, что стольких мне придётся накормить?! Я вчера только половину приготовил…!"

    $working = False
    $shuffle_menu()
    menu():
        a "Блин блинский! Хочешь сказать, что стольких мне придётся накормить?! Я вчера только половину приготовил…!{fast}"
        "Успеешь закончить вовремя?":
            $working = True
            $score_aiden -= 1
            show yoshi2 worry2 at right
            voice audio.yoshi_v_worry2
            yo "Успеешь приготовить всё вовремя, Эйден? Похоже, работы много…"

            show aiden2 sigh4 at center
            voice audio.aiden_v_yeah1a1
            a "Ага, мне бы не помешала помощь. "
            a "если ты не слишком занят, может, поможешь мне, Йоши?"

            show yoshi2 worry5 at right
            voice audio.yoshi_v_unsure2a
            yo "Уверен? Я мало что смыслю в готовке… "

            hide aiden2_autumn
            hide aiden2 sigh4
            show aiden_autumn at center
            show aiden talk4 at center
            voice audio.aiden_v_no1a1
            a "Ну что ты! На худой край, поможешь мне хотя бы нарезать ингридиенты!"

            hide yoshi2_autumn
            hide yoshi2 worry5
            show yoshi_autumn at right
            show yoshi happy1 at right
            voice audio.yoshi_v_alright2
            yo "Хорошо, если это поможет!"

            show aiden laugh2 at center
            voice audio.aiden_v_praise1a
            a "Супер! Пойдём тогда!"
        "У меня нет никаких планов.":
            $working = True
            show yoshi2 think5 at right
            voice audio.yoshi_v_worry2
            yo "У меня нет никаких планов до приезда работников, и раз Юри займётся поставкой…"

            hide aiden2_autumn
            hide aiden2 laugh2
            show aiden_autumn at center
            show aiden amazed2 at center
            voice audio.aiden_v_oh1a
            a "О! Может, тогда пойдёшь со мной?"

            hide yoshi2_autumn
            hide yoshi2 think5
            show yoshi_autumn at right
            show yoshi happy1 at right
            voice audio.yoshi_v_sure2
            yo "Конечно, я не против!"

            show aiden laugh2 at center
            voice audio.aiden_v_praise1a
            a "Супер! Пойдём тогда!"
        "Может, мне помочь тебе?":
            $working = True
            $score_aiden += 1
            hide yoshi2_autumn
            hide yoshi2 angry5
            show yoshi_autumn at right
            show yoshi happy1 at right
            voice audio.yoshi_v_worry2
            yo "Может, мне помочь тебе, Эйден? Уверен, так ты быстрее закончишь!"

            hide aiden2_autumn
            hide aiden2 panic4
            show aiden_autumn at center
            show aiden amazed2 at center
            voice audio.aiden_v_thanks1a1
            a "Ты мой спаситель, Йоши! Самому, я думаю, мне не удастся успеть вовремя!"

            show yoshi laugh1 at right
            voice audio.yoshi_v_laugh1
            yo "Ха-ха, я видал, как ты и не с такими дедлайнами справлялся. Но я рад, что смогу облегчить тебе работу сегодня!"

            show aiden laugh2 at center
            voice audio.aiden_v_comeon1a1
            a "Спасибо, Йоши! Ну же, пойдём!"
        "Я помогу тебе с готовкой.":
            $working = True
            $score_aiden += 2
            hide yoshi2_autumn
            hide yoshi2 angry5
            show yoshi_autumn at right
            show yoshi bold2 at right
            voice audio.yoshi_v_worry2
            yo "Я помогу тебе с готовкой, Эйден! Тебе бы пригодился помощник шефа!"
            yo "Я могу помочь подготовить и нарезать ингредиенты, чтобы сэкономить время!"

            hide aiden2_autumn
            hide aiden2 panic4
            show aiden_autumn at center
            show aiden amazed2 at center
            voice audio.aiden_v_thanks1a1
            a "Звучит здорово, Йоши! Буду только рад видеть тебя на кухне со мной!"

            show yoshi happy1 at right
            voice audio.yoshi_v_rush5
            yo "Тогда пойдём!"

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
    yu "Хе-хе… Ну-ка, куда я положила свою камеру~?"
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
    a "Эй, уверен, что будешь работать одетым? "

    show yoshi comp3 at right2
    voice audio.yoshi_v_comp2
    yo "А-а… Всё в порядке, Эйден! А тебе не холодно?"

    show aiden explain3 at left2
    voice audio.aiden_v_no2a1
    a "Не! Здесь будет жарко, только мы начнём готовить!"

    show yoshi bold2 at right2
    voice audio.yoshi_v_so2
    yo "Т-так, что готовим сегодня, и как я могу помочь тебе?"

    hide aiden_apron2
    hide aiden explain3
    show aiden2_apron2 at left2
    show aiden2 think4 at left2
    voice audio.aiden_v_think1b
    a "Хм-м-м… Раз уж я готовлю для группы энергичных парней, предполагаю, что аппетит у них сыграется не на шутку!"

    hide aiden2_apron2
    hide aiden2 think4
    show aiden_apron2 at left2
    show aiden bold2 at left2
    voice audio.aiden_v_excited2b
    a "Сытная еда, насыщенная протеином и питательными веществами сойдёт, чтобы восстановить в них энергию после долгого дня!"
    a "Как удачно сложилось, ведь это та же категория блюд, которые любят скауты, а значит, мы можем использовать ранее мной подготовленное меню!"

    show yoshi shock2 at right2
    voice audio.yoshi_v_amazed1d
    yo "Ого… Похоже, много всего надо приготовить… ещё и тридцать порций всего этого?!"

    show aiden laugh1 at left2
    voice audio.aiden_v_yeah1a2
    a "Ха-ха, именно! Добро пожаловать в мой мир! Поэтому мой младший шеф, Хиро, оказывал мне большую услугу, помогая тогда летом!"

    show aiden excited1 at left2
    voice audio.aiden_v_actually1a
    a "Хотя, если быть честным, Я так взволнолван! Как давно я не готовил для большой группы, ха-ха! "
    a "А с твоей помощью, всё пройдёт как по маслу! Будешь моим су шефом! "

    show yoshi comp5 at right2
    voice audio.yoshi_v_unsure1b
    yo "И правда, давно я не помогал на кухне. Надеюсь, успеем вовремя."

    show aiden laugh2 at left2
    voice audio.aiden_v_laugh2a1
    a "Ха-ха, ага, здесь как в скороварке, особенно когда в столовую начинают заходить люди!"
    a "Кстати говоря, надень фартук и давай начнём уже готовить ингредиенты!"

    show yoshi happy1 at right2
    voice audio.yoshi_v_right3
    yo "Хорошо!"

    hide yoshi_autumn
    hide yoshi happy1
    show yoshi_autumn3 at right2
    show yoshi happy1 at right2
    with dissolve

    scene cga2 1 with fade
    play bgsound sfxloop_chopping loop
    voice audio.aiden_vsa3_line1
    a "Хе-хе, какая ностальгия видеть тебя на кухне вновь, Йоши."

    voice audio.aiden_vsa3_line2
    a "С тех самыр пор, как ты стал полноценным скаутмастером, у тебя едва ли появлялась возможность помочь мне с готовкой! "

    voice audio.yoshi_vsa3_line1
    yo "А-а…"

    show cga2 2 with Dissolve(0.25)
    voice audio.aiden_vsa3_line3
    a "Но я тебя не виню. У тебя и так теперь есть дела поважнее."

    voice audio.yoshi_vsa3_line2
    yo "Ч-что ж, я всё ещё стараюсь помогать тебя время от времени, когда моё расписание не занято."

    voice audio.aiden_vsa3_line4
    a "Ага, один или два раза в сезон! "

    voice audio.yoshi_vsa3_line3
    yo "Не уверен, что я вообще помогаю… Я не так хорошо готовлю, как ты. "

    show cga2 3 with Dissolve(0.25)
    voice audio.aiden_vsa3_line5
    a "Дело не в навыках, а в простой компании! А еда, приготовленная с ЛБВ, лучше всех! "

    voice audio.yoshi_vsa3_line4
    yo "Это означает с латуком, булочками и ветчиной, да…? Не знал, что мы собираемся готовить бутерброды."

    show cga2 4 with Dissolve(0.25)
    voice audio.aiden_vsa3_line6
    a "Я имел ввиду с любовью, ну даёшь! Божечки…"

    voice audio.aiden_vsa3_line7
    a "Если готовить с кем-то или кому-то, блюдо обязательно станет особенным."

    voice audio.yoshi_vsa3_line5
    yo "Думаю, в этом ты прав… Ну то есть, мне куда веселее на работе в лагере, когда вокруг много скаутов. "

    show cga2 5 with Dissolve(0.25)
    voice audio.aiden_vsa3_line8
    a "Ага, ты всегда так взволнован тем, какие мероприятния для них устроишь."

    voice audio.aiden_vsa3_line9
    a "Прям когда сам в них учавствовал! Ты всегда хотел быть самым первым, лучшим во всём!"

    voice audio.aiden_vsa3_line10
    a "Напоминает мне о том, как ты был заинтересован в готовке очень очень давно – мы тогда так много времени проводили вместе на кухне!"

    voice audio.yoshi_vsa3_line6
    yo "А, точно… Я помню! Ты тогда помогал мне получить нашивку за готовку."

    show cga2 6 with Dissolve(0.25)
    voice audio.aiden_vsa3_line11
    a "Угх… Эта проклятущая нашивка. Только ты получил её, как сразу перестал интересоваться готовкой."

    $working = False
    $shuffle_menu()
    menu():
        a "Угх… Эта проклятущая нашивка. Только ты получил её, как сразу перестал интересоваться готовкой.{fast}"
        "В ней всегда лучше был ты.":
            $working = True
            $score_aiden -= 2
            show cga2 7a with Dissolve(0.25)
            voice audio.yoshi_vsa3_line7a
            yo "Что ж, в ней ты всегда был лучше меня. "

            voice audio.yoshi_vsa3_line8ab
            yo "Ты видел, что я тогда наготовил, оно было едва ли съедобно. Потому я и решил, что готовка это совершенно не моё."

            show cga2 8ab with Dissolve(0.25)
            voice audio.aiden_vsa3_line12ab
            a "Хорошо, что в конце ты всё-таки научился готовить лучше! "
        "Готовить не мой конёк.":
            $working = True
            $score_aiden -= 1
            show cga2 7b with Dissolve(0.25)
            voice audio.yoshi_vsa3_line7b
            yo "Н-ну, не то, чтобы я больше не был в ней заинтересован. Я просто подумал, что готовить не мой конёк."

            voice audio.yoshi_vsa3_line8ab
            yo "Ты видел, что я тогда наготовил, оно было едва ли съедобно. Потому я и решил, что готовка это совершенно не моё."

            show cga2 8ab with Dissolve(0.25)
            voice audio.aiden_vsa3_line12ab
            a "Хорошо, что в конце ты всё-таки научился готовить лучше! "
        "Я предпочитаю твою готовку.":
            $working = True
            $score_aiden += 1
            show cga2 7cd with Dissolve(0.25)
            voice audio.yoshi_vsa3_line7c
            yo "Я бы предпочёл твою готовку своей!"

            voice audio.yoshi_vsa3_line8c
            yo "ты всегда был в этом так хорош, что для смысла становиться лучше не было."

            show cga2 8c with Dissolve(0.25)
            voice audio.aiden_vsa3_line12c
            a "Хе-хе, если ты так говоришь."

            voice audio.aiden_vsa3_line13cd
            a "В конце концов, я видел и даже попробовал, что ты приготовил тогда, и должен сказать – никогда бы не подумал, что увижу мясо и шоколад в одной тарелке вместе…"

            show cga2 9cd with Dissolve(0.25)
            voice audio.yoshi_vsa3_line9cd
            yo "Г-гах! Клянусь, я не хотел! "

            show cga2 10cd with Dissolve(0.25)
            voice audio.aiden_vsa3_line14cd
            a "Ха-ха-ха! И такой вид был у тебя всегда, каждый раз, как ты оплошал, даже после моих уроков!"
        "Ты всегда приготовишь для меня.":
            $working = True
            $score_aiden += 2
            show cga2 7cd with Dissolve(0.25)
            voice audio.yoshi_vsa3_line7d
            yo "ха-ха, зачем вообще, если ты всегда приготовишь для меня~?"

            voice audio.yoshi_vsa3_line8d
            yo "Твоё готовка и так лучшая, так что и соревноваться не с кем!"

            show cga2 8d with Dissolve(0.25)
            voice audio.aiden_vsa3_line12d
            a "Хм, что ж, раз уж ты решил пофлиртовать, думаю, ты прощён~ "

            show cga2 8c with Dissolve(0.25)
            voice audio.aiden_vsa3_line13cd
            a "В конце концов, я видел и даже попробовал, что ты приготовил тогда, и должен сказать – никогда бы не подумал, что увижу мясо и шоколад в одной тарелке вместе…"

            show cga2 9cd with Dissolve(0.25)
            voice audio.yoshi_vsa3_line9cd
            yo "Г-гах! Клянусь, я не хотел! "

            show cga2 10cd with Dissolve(0.25)
            voice audio.aiden_vsa3_line14cd
            a "Ха-ха-ха! И такой вид был у тебя всегда, каждый раз, как ты оплошал, даже после моих уроков!"

    show cga2 11 with Dissolve(0.25)
    voice audio.yoshi_vsa3_line10
    yo "Да уж, эта нашивка и правда далась мне с трудом… но мне было так весело с тобой тогда!"

    voice audio.aiden_vsa3_line15
    a "Знаешь, я даже благодарен той нашивке – если бы не она, я бы может и не повстречал тебя."

    voice audio.aiden_vsa3_line16
    a "Она стала причиной того, почему я вообще остался в Лагере Друзей!"

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
    u "Итак, Эйден, Я понимаю, что общела позаботиться о тебе сегодня, но нам назначили срочное собрание…"
    u "Мне не разрешено брать с собой посетителей из-за политики лагеря, но к счастью сэр Горо сделал исключение для тебя и позволил подождать здесь в связи с обстоятельствами… "

    show andre talk2 at right2
    voice audio.andre_v_question1a
    u "Мне нужно, чтобы ты остался тут и подождал, пока не закончится собрание. Обещаю, я не на долго, поэтому не проказничай тут сильно, хорошо?"

    show yaiden talk3 at left2
    voice audio.yaiden_v_okay3b
    a "Хорошо, пап. Я могу подождать."

    show andre happy1 at right2
    voice audio.andre_v_agree1a3
    u "Отлично! Я скоро буду, Эйден!"

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
    yo "ну же, Юри! Мне очень нужна эта нашивка! Иди попробуй, что я сделал! "

    show yyuri sigh1 at p5_5
    voice audio.yyuri_v_yoshi11a
    yu "Йоши… Ты заставил меня попробовать уже пять жутких блюд за сегодня! А чем это отличается от остальных?!"

    show yyoshi bold2 at p5_4
    voice audio.yyoshi_v_confident4
    yo "Уверен, это я приправил как надо! Вот увидишь!"

    show yaiden_casual at left
    show yaiden norm3 at left
    show yyoshi_camp at center
    show yyoshi talk3 at center
    show yyuri_camp at right
    show yyuri sigh1 at right
    with move

    voice audio.yyoshi_v_oh2
    yo "О! "

    show yaiden awkward1 at left
    a "...!"

    show yyoshi happy2 at center
    voice audio.yyoshi_v_greet1a
    yo "Привет! Не видел тебя раньше, ты новенький?"

    show yaiden awkward2 at left
    voice audio.yaiden_v_think3a
    a "Я… Э-э… Нет—"

    show yyuri talk5 at right
    voice audio.yyuri_v_wait1a1
    yu "Погоди, я знаю тебя! Я видела, как ты пришёл с мистером Андре! Ты его сын?"

    show yaiden awkward3 at left
    voice audio.yaiden_v_yeah1c1
    a "А-ага…"

    show yyoshi comp5 at center
    voice audio.yyoshi_v_well1
    yo "Ну, друг мистера Андре и наш друг! Меня зовут Йошинори! "

    show yyuri happy1 at right
    voice audio.yyuri_v_intro1a
    yu "А я Юри! "

    show yyoshi happy2 at center
    voice audio.yyoshi_v_greet3a
    yo "Добро пожаловать в Лагерь Друзей! Как тебя зовут? "

    show yaiden talk3 at left
    voice audio.yaiden_v_intro1
    a "Эйден… "

    show yyoshi laugh1 at center
    voice audio.yyoshi_v_greet5a
    yo "Приятно познакомиться, Эйден! А что ты тут делаешь один?  "

    show yaiden explain3 at left
    voice audio.yaiden_v_oh1d
    a "О, я просто жду, когда папа вернётся с собрания… Он попросил побыть тут и подождать…"

    show yyoshi talk3 at center
    voice audio.yyoshi_v_isee1
    yo "Оу, вот как… Что ж, это точно займёт какое-то время! Если хочешь, можешь помочь мне с получением нашивок!"
    yo "Сегодня я пытаюсь получить нашивку за готовку, мне бы пригодился ещё человек, который бы попробовал блюдо, что я приготовил!"

    show yyoshi bold2 at center
    voice audio.yyoshi_v_think2
    yo "Раз твой папа работает здесь шефом, ты и сам наверное знаешь вещицу-две про готовку, верно?"

    show yaiden awkward2 at left
    voice audio.yaiden_v_unsure5a1
    a "Наверное… Да, я немного знаю о ней…"

    show yyuri laugh1 at right
    voice audio.yyuri_v_praise2a
    yu "Что за чудная идея, Йоши! Значит, я больше не понадоблюсь тебе в дегустации!"

    show yyoshi angry3 at center
    voice audio.yyoshi_v_hey3
    yo "Э-эй! Ты пока не свободна! Эйден ещё даже не согласился!"

    show yyuri rage3 at right
    voice audio.yyuri_v_ugh2a
    yu "УГХ-Х-Х…"

    show yyoshi norm1 at center
    show yaiden worry2 at left
    voice audio.yaiden_v_think3a
    a "Ну не знаю… Папа сказал мне побыть тут и—"

    show yyuri comp6 at right
    voice audio.yyuri_v_no1b1
    yu "Нет-нет! Всё будет в порядке! Эти собрания ЧАСАМИ длятся! Он даже и не узнает, что ты вышел! Просто скажи уже да!!"

    show yaiden worry5 at left
    voice audio.yaiden_v_think1a
    a "Уверена, что я не попаду от этого в неприятности…?"

    show yyuri play2 at right
    voice audio.yyuri_v_hey1a
    yu "Мой папа президент лагеря! Мы из любой передряги выберемся!"

    show yaiden shock2 at left
    voice audio.yaiden_v_really1a
    a "Вау, правда что ли?"

    show yyuri angry6 at right
    voice audio.yyuri_v_agree1b1
    yu "Да, правда! Поэтому, прошу, УМОЛЯЮ, спаси меня от очередного несварения за сегодня, Эйден!!"

    show yyoshi awkward4 at center
    voice audio.yyoshi_v_aiden2
    yo "Н-не слушай её, Эйден, на кухне я приготовил очень вкусную пиццу! Если пойдёшь со мной, я тебе хоть всю отдам!"

    play sound sfx_stomachgrowl
    show yaiden hungry3 at left
    voice audio.yaiden_v_amazed2b1
    a "Пицца?! *урчит живот*"

    show yyoshi excited1 at center
    voice audio.yyoshi_v_laugh1
    yo "Звучит так, словно тебе и правда не помешает пицца! Я только согрею её и будет супер тянучая и с сыром!"

    show yaiden hungry2 at left
    voice audio.yaiden_v_oh1a
    a "Ах… звучит вкусно!  Думаю… от перекуса ничего не будет."

    show yyuri amazed3 at right
    voice audio.yyuri_v_celebrate3a
    yu "Ура! Ты просто спаситель, Эйден! Думаю, мы станем очень хорошими друзьями! *шёпотом* Разумеется, если выживешь после его пиццы…"

    show yyoshi play3 at center
    voice audio.yyoshi_v_unsure2a
    yo "Ты точно не хочешь пойти с нами, Юри? Я могу приготовить для тебя другу, если хочешь!"

    show yyuri play2 at right
    voice audio.yyuri_v_nothankyou1a
    yu "Нетушки, спаси-и-и-ибо~~"
    yu "О, и Эйден, скажешь Йоши всё, что ты ПРАВДА думаешь о его готовке, ладно?!"

    show yaiden talk4 at left
    voice audio.yaiden_v_alright2a
    a "Л-ладно…!"

    show yyuri tease2 at right
    voice audio.yyuri_v_tease2a
    yu "Повеселись на свидании с этим милым мальчиком, Йоши~! "

    hide yyuri_camp
    hide yyuri tease2
    with dissolve

    show yyoshi angry2 at center
    voice audio.yyoshi_v_no2
    yo "Это н-не свидание!! "

    show yyoshi explain2 at center
    voice audio.yyoshi_v_anyway2
    yo "*кхем* Не важно, еда ждёт на кухне! Пошли!"

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
    yo "Так, маленькое предупреждение, опыта в готовке у меня нет, поэтому не жди многого, пожалуйста!"
    yo "Но я сильно посторался готовя это! Я следовал рецепту, но и добавил кое что от себя, и—"

    show yyoshi confused2 at left2
    voice audio.yyoshi_v_aiden7b
    yo "Эйден…? Ты слушаешь?"

    show yaiden shock2 at right2
    voice audio.yaiden_v_sorry1c1
    a "О-ой! Прости, Йошинори…! Я просто… Я просто никогда раньше не был в такой роскошной кухне раньше…"

    show yaiden excited3 at right2
    voice audio.yaiden_v_amazed2b2
    a "Двухстворчатый холодильник, встроенная духовка, и ещё кухонная плита даже с вытяжкой…"
    a "У нас дома такого совсем нет… "

    show yyoshi shock2 at left2
    voice audio.yyoshi_v_really1
    yo "Что, правда? Я даже удивлён, учитывая как вкусно мистер Андре готовит!"

    play sound sfx_microwavebeep
    show yyoshi happy2 at left2
    voice audio.yyoshi_v_ah4
    yo "Ах! Готово!"

    show yyoshi_camp at p5_1
    show yyoshi play2 at p5_1
    with move

    show yyoshi_camp at left2
    show yyoshi play2 at left2
    with move

    voice audio.yyoshi_v_here1
    yo "А вот и пицца, что я сделал! С пылу, с жару из микроволновки!"

    show yaiden confused2 at right2
    voice audio.yaiden_v_wait1a1
    a "Ты приготовил пиццу… в микроволновке?"

    show yyoshi bold2 at left2
    voice audio.yyoshi_v_yeah2
    yo "Ага! Ну же, попробуй!"

    show yaiden awkward3 at right2
    voice audio.yaiden_v_alright2b
    a "Ладно… "

    show yaiden munch1 at right2
    a "*жуёт*"

    show yyoshi talk4 at left2
    voice audio.yyoshi_v_so3
    yo "Ну-у, и как? Неплохо, да?"

    show yaiden comp3 at right2
    voice audio.yaiden_v_yeah1c1
    a "Эм… Д-да…?"

    show yyoshi confused3 at left2
    voice audio.yyoshi_v_think1a
    yo "Чую нотки сомнения… не стесняйся, можешь сказать, если что-то не так!"

    show yaiden think2 at right2
    voice audio.yaiden_v_unsure5b1
    a "М-может она недопеклась… Я укусил за сырое тесто внизу."

    show yyoshi worry2 at left2
    voice audio.yyoshi_v_aww1
    yo "О-о, правда? Что я сделал не так…? Я точно следовал рецепту."

    show yaiden explain2 at right2
    voice audio.yaiden_v_think1a
    a "Думаю, было бы лучше, если бы использовал духовку и готовил подольше, раз уж тесто у тебя вышло немного толстоватым."

    show yyoshi think5 at left2
    voice audio.yyoshi_v_actually1
    yo "Вообще я использовал уже покупное тесто их морозилки, сам я не умею его делать… и как пользоваться духовкой тоже…"

    show yyoshi talk3 at left2
    voice audio.yyoshi_v_think1b
    yo "К-как хоть на вкус? С этим-то я не напортачил, верно? Это же пицца!"

    show yaiden awkward2 at right2
    voice audio.yaiden_v_well1c1
    a "Н-ну… вкус очень… интересный… Ты точно следовал рецепту?"

    show yyoshi comp6 at left2
    voice audio.yyoshi_v_unsure4
    yo "Типа того… Некоторых ингредиентов не было, поэтому я их немного поменял…"
    yo "Я использовал кетчуп вместо соуса, он ведь сделан из помидоров, а ещё я нашёл немного сыра блю в морозилке, подумал, так будет приличнее!"

    show yaiden comp3 at right2
    voice audio.yaiden_v_laugh1b1
    a "Хе-хе-хе… Это так не работает, Йоши…"

    show yyoshi sigh1 at left2
    voice audio.yyoshi_v_sigh2
    yo "*вздох* Ну, блин… А я-то думал, что в этот раз точно получится! "

    show yaiden comp2 at right2
    voice audio.yaiden_v_alright3a
    a "Всё хорошо! Ты хотя бы попытался! Я всё равно наелся, так что это в любом из вариантов победа!"

    show yyoshi comp2 at left2
    voice audio.yyoshi_v_thanks4
    yo "Спасибо, что бы честен и дал пару советов, Эйден. ты и правда хороший парень!"

    show yaiden comp5 at right2
    voice audio.yaiden_v_thanks2b1
    a "А тебе спасибо, что дал перекусить, Йошинори!"

    show yyoshi laugh2 at left2
    voice audio.yyoshi_v_response6a
    yo "Пожалуйста! Раз уж мы теперь друзья, зови меня просто Йоши!"

    show yaiden talk3 at right2
    voice audio.yaiden_v_alright2a
    a "Х-хорошо, Йоши!"

    show yyoshi sigh4 at left2
    voice audio.yyoshi_v_sigh2
    yo "Что ж, похоже, мне нужно больше практиковаться в готовке… *вздох* так много за простую нашивку…"

    show yaiden comp3 at right2
    voice audio.yaiden_v_unsure5a1
    a "Если хочешь, может, я спосмотрю в этот раз за тобой и если что дам пару указаний…?"

    show yyoshi excited1 at left2
    voice audio.yyoshi_v_idea1
    yo "О! У меня есть идея получше! Как насчёт того, что ты сам покажешь мне? Может, трак я быстрее научусь!"

    show yaiden shock2 at right2
    voice audio.yaiden_v_what4a
    a "Ч-что? Прямо сейчас? Но я же не скаут… Ничего не будет? "

    show yyoshi comp5 at left2
    voice audio.yyoshi_v_confident3
    yo "Мы не что-то против правил затеваем, так что всё должно быть хорошо, Эйден! Доверься мне!"
    yo "К тому же, разве ты не хочешь попользоваться такой кухней?"

    show yaiden amazed2 at right2
    voice audio.yaiden_v_amazed3a
    a "Ва-ах… Х-хочу…!"

    show yyoshi bold2 at left2
    voice audio.yyoshi_v_praise2
    yo "Супер, тогда покажи, как всё делается, и получим наконец эту нашивку! "

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
    a "О, готово!"

    show yyoshi tasty1 at right2
    voice audio.yyoshi_v_mmm1
    yo "М-м-м… Пахнет вкусно!"

    show yaiden happy3 at left2
    voice audio.yaiden_v_here1a
    a "хе-хе, сейчас достану из духовки!"

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
    a "Та-да! Вот так я и готовлю пиццу! "

    voice audio.yyoshi_v_amazed1a
    yo "Ва-а-а-ау!!! От одного взгляда слюнки текут! "

    voice audio.yaiden_v_sorry1a1
    a "Извини, готовилось подольше, раз мне пришлось делать и тесто и соус с нуля."

    voice audio.yyoshi_v_amazed2a
    yo "Шутишь что ли? Я поверить не могу, что ты её за меньше часа приготовил! Я со своей всю ночь просидел, ха-ха-ха!"

    voice audio.yaiden_v_well1a1
    a "Ну, к счастью, в кухне было всё, чтобы получилось побыстрее. Я впервые пользуюсь кухонным комбайном, миксером, и даже духовкой!"

    voice audio.yyoshi_v_amazed3
    yo "Но готовил как профессионал! Было супер круто!"

    voice audio.yaiden_v_laugh1b1
    a "ой, хе-хе… Честно говоря, прежде чем разобрался, я с ними просто возился – но, оказывается, всё было предельно просто. "

    voice audio.yaiden_v_anyway1a
    a "Но не важно, ну же, попробуй пока горячее!"

    voice audio.yyoshi_v_alright4
    yo "I thought you’d never ask!"

    hide cg fade
    hide fxa1
    with dissolve

    show yyoshi tasty2 at right2
    yo "*чавк*"

    show yaiden worry2 at left2
    voice audio.yaiden_v_think3a
    a "Н-ну и как?"

    show yyoshi amazed1 at right2
    voice audio.yyoshi_v_amazed1c
    yo "ВКУСНОТИЩА!!! Эта лучшая пицца, что я пробовал в своей жизни!" with vpunch

    show yaiden comp3 at left2
    voice audio.yaiden_v_ah1a
    a "А-а… Да ты преувеличиваешь…"

    show yyoshi excited1 at right2
    voice audio.yyoshi_v_noway1
    yo "Вовсе нет! Никогда бы не подумал, что понравятся ананасы в пицце!"

    show yaiden comp5 at left2
    voice audio.yaiden_v_aww2a
    a "О-о… Ну, я рад, что тебе понравилось, Йоши! "

    show yaiden_casual at center
    show yaiden comp5 at center
    show yyoshi_camp at right
    show yyoshi excited1 at right
    with move

    show andre_camp at left
    show andre shock3 at left
    with dissolve

    voice audio.andre_v_aiden4b
    u "В-вот ты где, Эйден! Я обыскался тебя! "

    show yaiden shock3 at center
    voice audio.yaiden_v_dad5a
    a "П-пап…! "

    show andre sigh1 at left
    voice audio.andre_v_sigh1a
    u "*вздох* Разве я не просил остаться в столовой?"

    show yyoshi worry2 at right
    voice audio.yyoshi_v_sorry2a
    yo "Ой, за это простите, мистер Андре…! Это я пригласил Эйдена помочь мне с получением нашивки!"

    show andre sigh2 at left
    voice audio.andre_v_relief2a
    u "Фух… Хорого, что он встретился с тобой. Я волновался, что он убежал куда-то за пределы Лагеря Друзей…"

    show yyoshi talk1 at right
    voice audio.yyoshi_v_andre2
    yo "О, мистер Андре! Как так вышло, что вы никогда не приводили сюда Эйдена? Он хороший парень, и готовит великолепно, прям как вы!"

    show andre talk1 at left
    voice audio.andre_v_conj3b2
    u "Он был дома один с тех пор, как я сюда устроился на работу, потому я спросил сэра Горо об услуге, позволить привести его сегодня в лагерь. "

    show yyoshi happy1 at right
    voice audio.yyoshi_v_laugh1
    yo "Приводите почаще тогда! Я был бы рад проводить сним хоть весь день!"

    show andre worry2 at left
    voice audio.andre_v_ah1b1
    u "Ах, вообще-то, нам не разрешено приводить посетителей в лагерь… Сегодня - лишь исключение, поскольку у нас было собрание, и потому что я сегодня буду работать допоздна."

    show yyoshi excited1 at right
    voice audio.yyoshi_v_idea1
    yo "О, а может он вступит к нам в лагерь? Будет так весело!! Правда же, Эйден?!"

    show yaiden excited3 at center
    voice audio.yaiden_v_oh1a
    a "О…!"

    show yyoshi amazed1 at right
    voice audio.yyoshi_v_excited1
    yo "Мы бы вместе во всех мероприятиях учавствовали! Мы бы и гуляли, и на рыбалку ходили, или он бы мог бы учить меня готовить, пока я не получу нашивку!"

    show andre worry3 at left
    voice audio.andre_v_yoshi3c
    u "Э-эм, ну, Йошинори… Не думаю, что это возможно…"

    show yaiden sad1 at center
    show yyoshi worry3 at right
    voice audio.yyoshi_v_oh3
    yo "О-оу…"

    show andre sad4 at left
    voice audio.andre_v_unsure2b
    u "Я бы хотел, чтобы он со мной чаще приходил, но сэр Горо и так сделал достаточно для меня, я не хотел бы напрягать его большим. "

    show yyoshi sad4 at right
    voice audio.yyoshi_v_isee2
    yo "I see… That’s a shame…"

    show yaiden comp1 at center
    yo "Но Эйден такой талантливый повар прямо как вы, мистер Андре! Посмотрите, какую вкусную пиццу он сделал! "

    show andre comp4 at left
    voice audio.andre_v_laugh1a2
    u "А, ха-ха… Я был бы удивлён, да только, готовка была любимым хобби Эйдена ещё когда он был маленьким! "
    u "Я понимаю, что ты чувствуешь. Жаль, что Эйден не сможет стать частью лагеря."

    $working = False
    $shuffle_menu()
    menu():
        u "Я понимаю, что ты чувствуешь. Жаль, что Эйден не сможет стать частью лагеря.{fast}"
        "И правда жаль.":
            $working = True
            $score_aiden -= 1
            show yyoshi upset6 at right
            voice audio.yyoshi_v_sad2
            yo "И правда жаль, что он не сможет остаться… Он мог бы многое изменить в лагере."

            show yaiden sad2 at center
            a "..."

            show andre sad3 at left
            voice audio.andre_v_unsure1a
            u "Как бы я хотел такого… Но не знаю, как это сделать…"
        "Хотел бы я, чтобы он остался.":
            $working = True
            show yyoshi upset6 at right
            voice audio.yyoshi_v_sad3
            yo "Вот бы был какой то способ, чтобы Эйден остался…"

            show andre sad3 at left
            voice audio.andre_v_unsure1a
            u "Как бы я хотел такого… Но не знаю, как это сделать…"
        "Из Эйдена вышел бы хороший повар.":
            $working = True
            $score_aiden += 1
            show yyoshi think2 at right
            voice audio.yyoshi_v_sad3
            yo "Должен быть способ, чтобы Эйден остался в лагере. Я уверен, он бы стал, к примеру, лучшим шефом!"

            show yaiden shock1 at center
            a "...!"

            show andre worry2 at left
            voice audio.andre_v_ah1b1
            u "Ах…"
        "Нам бы было весело вместе.":
            $working = True
            $score_aiden += 2
            show yyoshi think2 at right
            voice audio.yyoshi_v_unsure1b
            yo "Должен быть способ, чтобы Эйден остался в лагере. Так ему бы не пришлось больше сидеть дома одному, нам было бы так весело!"

            show yaiden shock1 at center
            a "...!"

            show andre worry2 at left
            voice audio.andre_v_ah1b1
            u "Ах…"

    show yaiden talk1 at center
    voice audio.yaiden_v_unsure5b1
    a "М-может быть, я бы мог помочь тебе с обязанностями, пап?"

    show andre confused3 at left
    voice audio.andre_v_wait2a
    u "Имеешь ввиду… что хочешь поработать со мной, Эйден?"

    show yaiden happy2 at center
    voice audio.yaiden_v_yeah1a3
    a "Ага…! Я могу помочь тебе подзаработать, тогда тебе не придётся волноваться о том, что я буду сидеть дома один, мы будем всё время вместе!"

    show andre worry2 at left
    voice audio.andre_v_aiden1a
    u "Эйден…"

    $ renpy.pause (1.0, hard=True)
    show andre comp2 at left
    voice audio.andre_v_agree1a2
    u "Ну хорошо. Думаю, я могу поговорить с сэром Горо насчёт этого."

    show yyoshi amazed1 at right
    show yaiden amazed2 at center
    voice audio.yaiden_v_amazed3a
    a "Ва…! Правда?!"

    show andre comp4 at left
    voice audio.andre_v_compassion1a1
    u "Не обещаю, что сработает, но я обещаю, что попробую его убедить, хорошо?"

    show yyoshi bold2 at right
    voice audio.yyoshi_v_confident2
    yo "О, давайте я помогу, мистер Андре! Уверен, сэру Горо понравится Эйден! Дайте я только позову Юри, и пойдёмте спросим его сразу же!"

    hide yyoshi_camp
    hide yyoshi bold2
    with moveoutright

    show andre shock3 at left
    voice audio.andre_v_yoshi2b
    u "П-погоди, Йошинори…!"

    show andre_camp at left2
    show andre sigh1 at left2
    show yaiden_casual at right2
    show yaiden amazed2 at right2
    with move

    voice audio.andre_v_sigh1a
    u "*вздох* Гиперактивный как и всегда… "
    u "Покорил его своей стрепнёй, а, Эйден?"

    show yaiden comp3 at right2
    voice audio.yaiden_v_ah1a
    a "Э-эм… Ну…"

    show andre laugh1 at left2
    voice audio.andre_v_conj1a3
    u "Ну ладно, я рад, что ты завёл нового друга! А теперь, пойдём, догоним его!"

    show yaiden laugh1 at right2
    voice audio.yaiden_v_yeah1a2
    a "Ага!"

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
    a "Думая об этом сейчас, трудно поверить в то, чем всё закончилось.  "

    voice audio.aiden_vsa3_line18
    a "Я рос, многого мы не имели, был только отец и я сам."

    voice audio.aiden_vsa3_line19
    a "Готовка нас объединяла, но и именно она привела меня к тебе…"

    voice audio.aiden_vsa3_line20
    a "И тогда, благодаря твоей решимости, я стал работать здесь!"

    show cga2 13 with Dissolve(0.25)
    voice audio.yoshi_vsa3_line11
    yo "Оно стоило того! Целые годы у меня выдалась возможность есть твои кулинарные шедевры, и они всё ещё лучшие в мире! "

    voice audio.aiden_vsa3_line21
    a "Ой, посмотрите на него, мистер Обольститель! Будешь дальше слать такие комплименты, и я могу обслужить тебя по-особенному, если понимаешь, о чём я~"

    show cga2 14 with Dissolve(0.25)
    voice audio.yoshi_vsa3_line12
    yo "Э-Эйден…! "

    voice audio.aiden_vsa3_line22
    a "Гляди, красный как помидор! Всё тот же скаут-балбес, ха-ха-ха!"

    voice audio.yoshi_vsa3_line13
    yo "Д-давай уже закончим с готовкой! Нам ещё нужно успеть до приезда рабочих, а мы тут отвлекаемся!"

    voice audio.aiden_vsa3_line23
    a "Ладно-ладно! Ха-ха-ха!"

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black with fade
    yo "{i}Такая ностальгия вновь работать на кухне с Эйденом… Не удивительно, что она стал вспоминать прошлое.{/i}"
    yo "{i}Не часто он о таком разговаривает, и я рад, что мы можем так вспоминаь прошлое и снова проводить время вместе, как и раньше.{/i}"

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
    a "Фух! Картофельное пюре, есть! Зелень, есть! Ещё две кастрюли рагу на медленном огне и запечённые рёбрышки в духовке, которые будут готовы через пару минут! "

    show yoshi bold2 at right2
    voice audio.yoshi_v_praise1
    yo "отлично, Эйден! Уверен, рабочие с ума посходят с твой готовки! От одного запаха чувствуешь, как вкусно! "

    hide aiden_apron2
    hide aiden bold5
    show aiden_apron2 at left2
    show aiden wink2 at left2
    voice audio.aiden_v_well1b2
    a "Что ж, спасибо моего ассистенту шефа на сегодня! Если бы не ты, я бы возможно сейчас продолжал возиться, пытаясь успеть все пригтовить."

    show yoshi comp1 at right2
    voice audio.yoshi_v_response3b
    yo "Без проблем! Рад, что мы успели все закончить дол приезда рабочих!"

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
    t "Эй, Йоши! Юри попросила нас привести тебя, работники приехали!"

    show yoshi happy1 at p4_2
    voice audio.yoshi_v_ah1
    yo "О, кстати говоря, вот и мой выход!"

    show yoichi annoyed5 at p4_4
    voice audio.yoichi_v_wait2b
    yi "Погоди, чего?! Ты говорил, что мы сюда за маршмеллоу?!"

    show taiga playful2 at p4_3
    voice audio.taiga_v_conjunction2c
    t "Ну, Я знал, что со мной ты не пойдёшь, потому и сделал предлог сходить за закусками. "
    t "А ещё чтобы не позволить тебе облаять навоприбывших и распугать там всех."

    show yoichi_autumn at p5_4
    show yoichi rage2 at p5_4
    with move

    voice audio.yoichi_v_angry2b1
    yi "ГРАХ!!! Сейчас получишь, кошатник!"

    show taiga panic1 at p4_3
    voice audio.taiga_v_surprised4b
    t "ВАХ! А ну слезь с меня, псина! Кыш!!"

    hide yoshi_autumn3
    hide yoshi rage2
    show yoshi2_autumn3 at p4_2
    show yoshi2 comp5 at p4_2
    voice audio.yoshi_v_laugh1
    yo "Ха-ха-ха… Может, и правда хорошо, что вы тут остались…"

    show aiden happy3 at p4_1
    voice audio.aiden_v_comp1a2
    a "Ага, можешь оставить их на меня! Обещаю, что они не наведут смуту, а-ха-ха!"

    hide yoshi2_autumn3
    hide yoshi2 comp5
    show yoshi_autumn3 at p4_2
    show yoshi happy2 at p4_2
    voice audio.yoshi_v_thanks4
    yo "Спасибо, Эйден! Я прниведу их ближе к обеду, чтобы и ты с ними встретился!"

    show aiden excited3 at p4_1
    voice audio.aiden_v_praise1a
    a "О, хорошо! Очень хочу с ними встретиться!"

    hide yoshi_autumn3
    hide yoshi happy2
    show yoshi2_autumn3 at p4_2
    show yoshi2 comp6 at p4_2
    voice audio.yoshi_v_sigh3a
    yo "…Просто, не забудь надеть что нибудь, ладно?"

    show aiden laugh3 at p4_1
    voice audio.aiden_v_laugh2a1
    a "Ха-ха-ха! Ладно-ладно! Но только потому что ты мне помог сегодня!"
    a "Иди! Они уже ждут наверное!"

    hide yoshi2_autumn3
    hide yoshi2 comp6
    show yoshi_autumn3 at p4_2
    show yoshi happy1 at p4_2
    voice audio.yoshi_v_alright2
    yo "Хорошо!"

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
    yo "Воу…! А они не шутили, когда говорили, что отправят тридцать людей…"

    show yoshi_autumn at left2
    show yoshi shock3 at left2
    with move

    show yuri_autumn at right2
    show yuri talk3 at right2
    with dissolve

    voice audio.yuri_v_greet1a
    yu "А, вот ты где, Йоши! Работники только приехали и разобрали багаж. Мне уже немного невмоготу всем помогать."

    show yoshi talk1 at left2
    voice audio.yoshi_v_worry2
    yo "Как мне помочь, Юри?"

    show yuri confused4 at right2
    voice audio.yuri_v_oh1a
    yu "О, мне нужно, чтобы ты поговорил с бригадирами. Уверена, в этих формальных беседах ты разбираешься получше меня."

    show yoshi happy1 at left2
    voice audio.yoshi_v_alright2
    yo "Хорошо, Юри. Я этим займусь!"

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
    yo "Здравствуйте! Добро пожаловать в Лагерь Друзей! Моё имя Йошинори Нагира, я здесь во главе заселения! А это Юри Номору, моя подруга скаутмастер. "

    show lloyd talk1 at p4_3
    voice audio.lloyd_v_ah1a1
    ar "А, мы раньше встречались. Приятно видеть тебя снова, Йошинори! "

    hide yoshi_autumn
    hide yoshi happy2
    show yoshi2_autumn at p4_2
    show yoshi2 confused1 at p4_2
    yo "{i}(А? Что значит… \"снова\"?){/i}"

    show lloyd happy1 at p4_3
    voice audio.lloyd_v_conj6a2
    ar "Меня звать Архитектором Сириусом, а это Мастер Наджар."

    show darius talk1 at p4_4
    voice audio.darius_v_greet1a1
    fo "Привет."

    show lloyd bold2 at p4_3
    voice audio.lloyd_v_william2c
    ar "Люди позади меня - команда строителей. Как, я уверен, вы уже знаете, мы были наняты Clermont Inc. для реконструкции и дизайна зданий вместе с благоустройством согласно официальному плану!"
    ar "Можете ожидать от нашей группы наилучшего результата! Я специалист как в архитектурных, так и в структурных аспектах проекта!"

    show lloyd laugh1 at p4_3
    voice audio.lloyd_v_conj6a2
    ar "Если вам нужны какие-либо чётко выполненные плотницкие работы или укладка, мой напарник - мастер в обоих ремёслах!"

    show darius talk2 at p4_4
    voice audio.darius_v_agree1a
    fo "Ага. "

    hide yoshi2_autumn
    hide yoshi2 confused1
    show yoshi_autumn at p4_2
    show yoshi amazed1 at p4_2
    voice audio.yoshi_v_amazed3
    yo "Великолепно! Мы с нетерпением ждём возможности поработать с вами!"

    show lloyd happy2 at p4_3
    voice audio.lloyd_v_gratitude2a2
    ar "Как и мы! Большая привелегия быть здесь!"

    show yoshi happy1 at p4_2
    voice audio.yoshi_v_conj6a
    yo "Прежде чем мы приступим к бизнесу, нам бы хотелось пригласить вас к обеду. Вы должно быть все истощены долгой поездкой."

    show lloyd grin1 at p4_3
    voice audio.lloyd_v_praise3a
    ar "Отлично! "

    show yoshi bold2 at p4_2
    voice audio.yoshi_v_alright2
    yo "Чудно! Юри и я поможем вам добраться до домиков, дабы разложить ваш багаж в первую очередь!"
    yo "Мы подготовили жилые комнаты в неиспользованных домиках для работников, а вы двое може еостаться с нами в скаутмастерской части, согласны?"

    show lloyd happy1 at p4_3
    voice audio.lloyd_v_agree2b1
    ar "Конечно! Звучит как отличная возможность наверстать упущенное!"

    show yuri happy1 at p4_1
    voice audio.yuri_v_rush4a
    yu "Отлично, прошу за мной!"

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black with fade

    yo "{i}Юри и я отвели бригадиров и команды рабочих по их домикам и дали им время разобраться с багажом.{/i}"
    yo "{i}Всё то время, пока с ними нахожусь, никак не могу отделаться от чувства, словно раньше уже встречались… Но где и когда я не помню.{/i}"
    yo "{i}Разберусь с этим позже! В данный момент, я обязан оказать тёплый приём и выдать все инструкции!{/i}"

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
    yu "Еда уже на подходе! Я уведомила повара, что все уже здесь!"

    show lloyd hungry2 at p4_2
    voice audio.lloyd_v_gratitude3a
    ar "Благодарю за гостеприимство! Я весь изголодался!"
    ar "Кстати, спасибо за помощь с заселением! А здесь едва ли что-то изменилось, а?"

    show yoshi happy1 at p4_3
    voice audio.yoshi_v_yes1
    yo "Да! Мы старались держать здесь всё без изменений на протяжение нескольких лет, дабы сохранить классический стиль. Знал, что вы оцените это как архитектор!"

    show lloyd explain1 at p4_2
    voice audio.lloyd_v_conj1a3
    ar "Вообще, я имел ввиду чувство ностальгии!"

    show yoshi talk3 at p4_3
    voice audio.yoshi_v_right7
    yo "Ах, вот как…!"
    yo "Знаете, должен сказать, вы наверное гений, раз уже архитектор в таком юном возрасте, мистер Сириус!"

    show lloyd angry3 at p4_2
    voice audio.lloyd_v_greet2c2
    ar "Юном?! Мы почти одного возраста!"

    hide yoshi_autumn
    hide yoshi talk3
    show yoshi2_autumn at p4_3
    show yoshi2 confused2 at p4_3
    voice audio.yoshi_v_really5
    yo "Погодите… Правда? Я думал—"

    show lloyd rage3 at p4_2
    voice audio.lloyd_v_ignored1c3
    ar "Это из-за моего низкого роста?!"

    show darius bored5 at p4_1
    voice audio.darius_v_comp1a1
    fo "Спокойно."

    show lloyd pout4 at p4_2
    voice audio.lloyd_v_annoyed1b3
    ar "Хмпф!"

    show darius shy5 at p4_1
    voice audio.darius_v_sorry3
    fo "Прошу прощения. Темы касательно его роста злят его."

    show yoshi2 panic4 at p4_3
    voice audio.yoshi_v_sorry1a1
    yo "Ах, извиняюсь, я не это имел ввиду…!"

    show yuri sigh3 at p4_4
    voice audio.yuri_v_sigh2a
    yu "*вздох* Йоши, ты чего…"

    show lloyd angry5 at p4_2
    voice audio.lloyd_v_conj1a2
    ar "Что ж, я прощу такое, но лишь раз, в память о старых добрых временах."

    show lloyd happy1 at p4_2
    voice audio.lloyd_v_conj2b1
    ar "Не так важно, есть ещё кое что, что не изменилось - здесь пахнет так же вкусно, как я помню!"

    show yuri laugh1 at p4_4
    voice audio.yuri_v_laugh1a1
    yu "Ты наверное давно хотел побывать тут, зная как вкусно здесь готовят!"

    show yoshi2 confused1 at p4_3
    yo "{i}(Что происходит…? Я что-то пропустил? ){/i}"

    show darius talk1 at p4_1
    voice audio.darius_v_shock1a
    fo "О, а вот и еда."

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
    a "Ваш заказ! Четыре порции барбекю с гарниром!"

    hide aiden_apron3
    hide aiden bold2
    show aiden2_apron3 at p5_1
    show aiden2 shock3 at p5_1
    voice audio.aiden_v_wait2b2
    a "Одну минутку… Эй, ты же…"

    hide yoshi2_autumn
    hide yoshi2 confused1
    hide aiden2_apron3
    hide aiden2 bold2
    show yoshi_autumn at p5_4
    show yoshi shock1 at p5_4
    show aiden_apron3 at p5_1
    show aiden excited1 at p5_1
    voice audio.aiden_v_shock3a2
    a "Да ни в жизнь! Дариус, ты что ли?!" with vpunch

    show darius happy2 at p5_2
    voice audio.darius_v_aiden3
    d "Эйден. "

    show aiden amazed1 at p5_1
    voice audio.aiden_v_greet1c
    a "Как жизнь, чувак?! Сколько лет, сколько зим!"

    show darius happy3 at p5_2
    voice audio.darius_v_response2b
    d "Всё путём. Не знал, что ты тут тоже работаешь…"

    show aiden excited3 at p5_1
    voice audio.aiden_v_swear2a1
    a "ЧЁРТ ВОЗЬМИ! Да ты вырос, прям, на пару метров! Я тебя едва узнаю!"

    show darius tease2 at p5_2
    voice audio.darius_v_thanks1a1
    d "И я тоже. Занимался мускулами?"

    show aiden laugh3 at p5_1
    voice audio.aiden_v_flex1a
    a "Ага, чтобы было за что подержаться, а?!"
    a "Как здорово видеть тебя спустя столько лет! Я уж думал, что никогда тебя не увижу!"

    show darius comp5 at p5_2
    voice audio.darius_v_agree4
    d "И я."

    show aiden excited3 at p5_1
    voice audio.aiden_v_wait1a2
    a "Погоди… Только не говори мне, что ты ещё и из команды рабочих?!"

    show darius happy1 at p5_2
    voice audio.darius_v_agree2a
    d "Оттуда."

    show aiden amazed2 at p5_1
    voice audio.aiden_v_amazed3b
    a "БАЛДЁЖ! Мы чудно проведём время, как в старые добрые! "

    show lloyd confused2 at p5_3
    voice audio.lloyd_v_darius4a
    ar "Дар, ты с ним знаком?"

    show darius confused2 at p5_2
    voice audio.darius_v_rush2
    d "Сын повара. Не помнишь его?"

    show aiden shock3 at p5_1
    voice audio.aiden_v_what2b
    a "А что за малыш кстати? Погоди— У тебя уже сын появился?! Господи, неужели прошло столько времени?!"

    show lloyd rage3 at p5_3
    voice audio.lloyd_v_question1b1
    ar "ЧЕГО?!"

    show aiden laugh2 at p5_1
    voice audio.aiden_v_amazed1a1
    a "Ты просто обязан записать его в лагерь! Лагерь Друзей будет на пике своего совершенства— "

    show lloyd rage4 at p5_3
    voice audio.lloyd_v_conj3b1
    ar "ПО-ПЕРВЫХ, Я НИКАКОЙ НЕ МАЛЫШ! И уж точно НЕ ЕГО СЫН!"

    show darius explain2 at p5_2
    voice audio.darius_v_lloyd2
    d "Это Ллойд, мой бизнес партнёр. Эйден, он старше меня."

    hide aiden_apron3
    hide aiden laugh2
    show aiden2_apron3 at p5_1
    show aiden2 comp3 at p5_1
    voice audio.aiden_v_laugh1b1
    a "Ой… Хе-хе… Извиняй, маленький паренёк!"

    show lloyd annoy4 at p5_3
    voice audio.lloyd_v_groan1d3
    l "ГГХХХ!! МАЛЕНЬКИЙ?! Да как ты смеешь!"

    show yuri tease2 at p5_5
    voice audio.yuri_v_laugh1b2
    yu "Хи-хи-хи, так и продыху не дают."

    show lloyd pout1 at p5_3
    voice audio.lloyd_v_annoyed1b3
    l "Хмпф! Я уже начинаю жалеть, что вернулся!"

    show yuri angry1 at p5_5
    voice audio.yuri_v_aiden1a
    yu "Эйден, прекращай дразнить главного архитектора! Он и Дариус помогут нам с ремонтом!"

    show aiden2 kiss1 at p5_1
    voice audio.aiden_v_whistle1a
    a "*свист* Ха, архитектор значит? Вау, виноват, что пропустил такое! Ты просто выглядишь таким-м-м—"

    show lloyd rage1 at p5_3
    l "*пялится*"

    show aiden2 comp3 at p5_1
    voice audio.aiden_v_think2b
    a "…м-молодым?? "

    show lloyd laugh2 at p5_3
    voice audio.lloyd_v_laugh1a1
    l "Люди часто мне такое говорят, ха-ха!"

    show darius tease4 at p5_2
    voice audio.darius_v_excited1a1
    d "Неплохо выкрутился."

    hide aiden2_apron3
    hide aiden2 comp3
    show aiden_apron3 at p5_1
    show aiden excited1 at p5_1
    voice audio.aiden_v_amazed1a2
    a "Это ведь супер круто! С вами проект станет таким захватывающим!"

    show yuri laugh2 at p5_5
    voice audio.yuri_v_yeah1b2
    yu "Ага, словно звёзды сошлись, и вот мы снова вместе, правда?"

    show lloyd excited1 at p5_3
    voice audio.lloyd_v_shock1a3
    l "Ой, и не говори! Мой гороскоп на этот месяц гласил, что я \"встречу знакомые лица на своём пути.\""
    l "…И вот он я, вновь с вами, ребята! Совпадение? А я так не думаю!"

    hide aiden_apron3
    hide aiden excited1
    show aiden2_apron3 at p5_1
    show aiden2 confused2 at p5_1
    voice audio.aiden_v_confused2a2
    a "Ты про те предсказания, что ещё на бумашке в печеньках…?"

    hide yoshi_autumn
    hide yoshi shock1
    show yoshi2_autumn at p5_4
    show yoshi2 confused5 at p5_4
    voice audio.yoshi_v_uh1b
    yo "Э-эм… Мне ужасно жаль, но, я немного озадачен… Откуда вы друг друга знаете?"
    yo "Не хочу показаться грубым, но… Ещё с первой встречи я подумал, что вы выглядите до боли знакомыми…"

    show yuri shock4 at p5_5
    voice audio.yuri_v_wait1a1
    yu "Погоди… То есть, ты всё это время не знал, Йоши?! "
    yu "Мы с ними всё утро болтали – ты должен был хотя бы догадаться!"

    hide yoshi2_autumn
    hide yoshi2 confused1
    show yoshi_autumn at p5_4
    show yoshi panic5 at p5_4
    voice audio.yoshi_v_shock3
    yo "ГАХ! М-мне правда жаль…!"

    show yuri confused4 at p5_5
    voice audio.yuri_v_request3a
    yu "Это Ллойд Сириус и Дариус Наджар! Выпускники Лагеря Друзей! "
    yu "Как ты мог забыть?! Они же были в той же группе, что и мы!"

    hide yoshi_autumn
    hide yoshi panic5
    show yoshi2_autumn at p5_4
    show yoshi2 worry5 at p5_4
    voice audio.yoshi_v_think1b
    yo "Эм…"

    show yuri irked2 at p5_5
    voice audio.yuri_v_ugh3a
    yu "Угх… Ну ты даёшь, Йоши! "
    yu "*с шлепком кладёт книгу на стол*"

    show yuri bold2 at p5_5
    voice audio.yuri_v_here1b
    yu "Вот! К счастью у меня остались фотографии в старом дневнике!"

    show aiden2 awkward2 at p5_1
    voice audio.aiden_v_confused1a1
    a "Т-ты везде его с собой носишь…?"

    show cg fade at truecenter
    show fx4 at fx_pos
    with dissolve

    yo "..."

    voice audio.yoshi_vs4_line1
    yo "О-О!!! Теперь-то я вспомнил! Малыш Ллойд и Дариус Серьёзность из первого сезона?!"

    voice audio.yuri_vs4_line1
    yu "Да! Боже мой, так вот почему ты так странно себя вёл!!!"

    voice audio.lloyd_vs4_line1
    l "Господи… Долго ты соображал…"

    voice audio.darius_vs4_line1
    d "Забавно."

    voice audio.yuri_vs4_line2
    yu "Похоже, стареет не один мой папа."

    voice audio.lloyd_vs4_line2
    l "А я-то думал, что это он как и в прошлом, словно паинька старается вести себя серьёзно ради бизнеса."

    hide cg fade
    hide fx4
    with dissolve

    hide yoshi2_autumn
    hide yoshi2 worry5
    show yoshi_autumn at p5_4
    show yoshi amazed2 at p5_4
    voice audio.yoshi_v_amazed2a
    yo "Посмотрите только… Малыш Ллойд… не могу поверить, что это правда ты!"

    show lloyd annoy2 at p5_3
    voice audio.lloyd_v_groan2a3
    l "Угх. Может уже хватит погонял?! Мы уже давно их забросили, ещё когда были в лагере!"

    hide yoshi_autumn
    hide yoshi amazed2
    show yoshi2_autumn at p5_4
    show yoshi2 think6 at p5_4
    voice audio.yoshi_v_actually2b
    yo "Если так подумать… Ты совсем не вырос с тех пор… Но не то, чтобы это плохо! "

    show lloyd rage3 at p5_3
    voice audio.lloyd_v_greet2d1
    l "ЭЙ, А ВОТ И НЕ ПРАВДА!! Скажи им, Дар! Я всё точно измерил, да?"

    show darius bored5 at p5_2
    voice audio.darius_v_agree2a
    d "Около 160 сантиметров, да. Учитывая обувь. "
    d "Ты вырос на один сантиметр, с тех пор как мы виделись в последний раз."

    show lloyd confused3 at p5_3
    voice audio.lloyd_v_aiden2c
    l "Должен признать, мне тоже жаль, что я кое кого забылe. Не думаю, что вообще тебя помню, Эйден."

    hide aiden2_apron3
    hide aiden2 awkward2
    show aiden_apron3 at p5_1
    show aiden comp6 at p5_1
    voice audio.aiden_v_alright3b2
    a "Хе-хе, всё в порядке! Я тогда не был скаутом, наверное поэтому ты  не узнал меня."
    a "Но Йоши нет прощения… До сих пор не могу поверить, что ты их не узнал, особенно Дариуса!"

    show yoshi2 awkward4 at p5_4
    voice audio.yoshi_v_ah2
    yo "А-а-а… Как же стыдно… М-мне жаль, Дариус. Просто, ты просто выглядишь совсем другим, нежели как я помню, я даже и не подумал, что ты один и тот же человек."

    show darius comp5 at p5_2
    voice audio.darius_v_comp3a
    d "Всё хорошо. "
    d "Всё так говорят."

    show aiden amazed1 at p5_1
    voice audio.aiden_v_oho1a
    a "Ага, кто бы знал, что ты превратишься в такого качка!"

    show yuri tease2 at p5_5
    voice audio.yuri_v_agree2a1
    yu "И не говори, Эйден~ Что за привлекательный джентельмен со столь загадочным глубоким голосом и диким взглядом~"

    show lloyd rage3 at p5_3
    voice audio.lloyd_v_question1d2
    l "Ка-а-акого чёрта?! Все хорошие комплименты, так саруз Дар, а как я, так один шутки про рост?!"
    l "Несправедливо!"

    show aiden laugh2 at p5_1
    voice audio.aiden_v_comp3b
    a "как и сказал Йоши, мы не в плохом смысле! В том, чтобы быть низеньким, есть свои плюсы!"

    show lloyd annoy2 at p5_3
    voice audio.lloyd_v_annoyed1a3
    l "Ага? Например?"

    hide aiden_apron3
    hide aiden laugh2
    show aiden2_apron3 at p5_1
    show aiden2 think4 at p5_1
    a "..."

    show aiden2 think6 at p5_1
    voice audio.aiden_v_think2a
    a "Эм… Больше места для ног в транспорте…?"

    show lloyd think4 at p5_3
    l "..."

    show yuri comp2 at p5_5
    voice audio.yuri_v_praise4a
    yu "А я думаю, что ты супер милый и просто очаровашка, Ллойд! В твоих венах течёт благословение вечной юности! "
    yu "Вечно Молодой, Вечно Пьяный, я права?!"

    show lloyd angry2 at p5_3
    voice audio.lloyd_v_request2c
    l "Может уже прекратим о моём росте?! Не могу понять, как мы постоянно возвращаемся к этой теме! "

    show yoshi2 shy5 at p5_4
    voice audio.yoshi_v_sorry5b
    yo "П-прости за это, Ллойд! В любом случае, так приятно видеть, как прошлые участники Лагеря Друзей снова здесь и делятся друг с другом опытом!"

    show lloyd talk2 at p5_3
    voice audio.lloyd_v_agree2a3
    l "Ага. Я даже не удивлён, что ты стал скаутмастером, Йошинори. Ты всегда был прирождённым скаутом."

    hide yoshi2_autumn
    hide yoshi2 awkward4
    show yoshi_autumn at p5_4
    show yoshi happy1 at p5_4
    voice audio.yoshi_v_actually1a
    yo "Так странно, что мы все прошли целый круг и снова вернулись к общей цели! "

    show yuri confused2 at p5_5
    voice audio.yuri_v_conj6a
    yu "А мне любопытно, как так вышло, что вы были наняты на работы в Лагерь Друзей? По воле ли судьбы? "

    show lloyd talk4 at p5_3
    voice audio.lloyd_v_shock1a1
    l "О, Clermont Inc. вообще обращалось во многие строительные компании относительно проекта."
    l "Когда Дар и я увидели, что заявка была о Лагере Друзей, мы были так взволнованы, что мигом отправили форму."

    show lloyd happy1 at p5_3
    voice audio.lloyd_v_laugh1a1
    l "Мы были лучшими по критериям мистера Клермонта, а как только он услышал, что мы ещё и прошлые скауты Лагеря Друзей, он тут же дал нам одобрение."
    l "Всё сложилось хорошо – поскльку я много времени провёл в этом лагере, мой архитектурный стиль стал сильнее сфокусирован на более простых и уютных дизайнах!"

    show yoshi talk1 at p5_4
    voice audio.yoshi_v_so1a
    yo "Значит, домики будут главной задачей для вас?"

    show lloyd explain1 at p5_3
    voice audio.lloyd_v_conj1a3
    l "Ну, из того что я знаю, это самая трудоёмкая часть, но есть и другие цели в том числе."
    l "Мы также займёмся строительством зала для мероприятий, лазарета, и нескольких гостевых помещений около озера."

    show yoshi talk3 at p5_4
    voice audio.yoshi_v_really5
    yo "Много всего… А всё это построить в столь короткий срок реально?"

    show lloyd happy2 at p5_3
    voice audio.lloyd_v_darius2b
    l "Что ж, потому здесь и Дар! Когда дело доходит до строительства, он творит чудеса!"

    hide aiden2_apron3
    hide aiden2 think6
    show aiden_apron3 at p5_1
    show aiden happy1 at p5_1
    voice audio.aiden_v_darius3a
    a "Дариус всегда был изобретательным парнем, ещё когда мы были скаутами! Он даже дал мне первый урок как плотника, и у меня до сих пор остались эти навыки!  "
    a "Благодаря ним я смог помочь Йоши в строительстве некоторых проектов за прошедшие несколько лет. Прошлым летом мы работали с некоторыми скаутами и отремонтировали хиленькие домики!"

    show aiden happy3 at p5_1
    voice audio.aiden_v_oh1b
    a "А ещё мы построили огроменную полосу препятствий! "

    show lloyd shock3 at p5_3
    voice audio.lloyd_v_amazed3a1
    l "Воу! Ты про те, как в игровых шоу по телевизору?!"

    show yoshi happy1 at p5_4
    voice audio.yoshi_v_yes2
    yo "Ага! это был мой самый первый проект, с тех пор как я устроился на работу!"

    show lloyd shock3 at p5_3
    voice audio.lloyd_v_amazed2a1
    l "И всей работой занимались лишь вы двое?!"

    show yoshi comp3 at p5_4
    voice audio.yoshi_v_yeah2
    yo "По большей части, да…! Правда, заняло это дело пару лет."

    show lloyd excited1 at p5_3
    voice audio.lloyd_v_laugh1a1
    l "Вы просто обязаны показать нам всё в округе! Хочу увидеть весь лагерь спустя столько лет. "
    l "Прогулка дала бы мне пару идей о том, с чем мы имеем дело в проекте."

    show yoshi happy2 at p5_4
    voice audio.yoshi_v_agree1b2
    yo "Разумеется! У нас назначен целый тур по лагерю после обеда!"

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black with fade
    yo "{i}А дальше мы впятером провели ещё немного времени в столовой, доедая обед и вспоминая старые времена, но вскоре пришло время возвращаться к работе.{/i}"
    yo "{i}Юри отвела других рабочих обратно в их домики, чтобы помочь им устроиться, в то время как Эйден потащил Йоичи и Тайгу помочь ему с уборкой кухни. {/i}"
    yo "{i}Тем временем я повел Дариуса и Ллойда на экскурсию по лагерю, показав им все изменения и более подробно обсудив работу, которую они будут выполнять… {/i}"

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
    yo "И на этом всё! Вы увидели всё, что хотели? "

    show lloyd happy1 at right
    voice audio.lloyd_v_agree2b2
    l "Да, думаю, у меня и Дариуса была хорошая возможность осмотреть местность. Даже провёл несколько необходимых измерений."
    l "Я уже набросал большую часть материала до того, как попал сюда, но после осмотра местности придётся внести некоторые коррективы."

    show lloyd talk1 at right
    voice audio.lloyd_v_conj6a2
    l "Завтра первым же делом мы начнём подготавливать площадку. Наши цели: очистить территорию от деревьев и мусора, выровнять землю, а затем переместить туда все строительные материалы к концу недели."

    show yoshi talk1 at left
    voice audio.yoshi_v_response1a
    yo "Понял. Я буду рядом, если понадобится моё руководство."

    show lloyd talk2 at right
    voice audio.lloyd_v_conj2b1
    l "А теперь, с вашего разрешения, я пойду вносить поправки в план!"

    show yoshi happy2 at left
    voice audio.yoshi_v_alright2
    yo "Хорошо. Если что-то нужно, ты знаешь, где меня найти."

    show lloyd happy2 at right
    voice audio.lloyd_v_response2a1
    l "Конечно. Я буду в нашем домике. Увидимся завтра! "

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
    yo "Эм… Дариус? А ты не пойдёшь с Ллойдом? "

    show darius shy4 at right2
    voice audio.darius_v_no1a
    d "Нет. Ллойду нравится работать одному, чтобы его не беспокоили."

    show yoshi2 think6 at left2
    voice audio.yoshi_v_isee2
    yo "О… Вот как…"

    show darius shy1 at right2
    d "..."

    show yoshi2 shy3 at left2
    yo "{i}(Неловко вышло… Дариус просто стоит, смотрит на меня… Может мне уйти, или лучше остаться—){/i}"

    show yoshi2_autumn at center
    show yoshi2 shy3 at center
    show darius_autumn at right
    show darius shy1 at right
    with move

    show aiden_autumn at left
    show aiden happy2 at left
    with dissolve

    voice audio.aiden_v_hey2a2
    a "Эй там!"

    hide yoshi2_autumn
    hide yoshi2 shy3
    show yoshi_autumn at center
    show yoshi awkward4 at center
    voice audio.yoshi_v_hey3
    yo "О-о! Привет, Эйден! "

    hide aiden_autumn
    hide aiden happy2
    show aiden2_autumn at left
    show aiden2 shock2 at left
    voice audio.aiden_v_confused1a1
    a "А? А чего это вы тут стоите, смотрите друг на друга?"

    show yoshi explain2 at center
    voice audio.yoshi_v_ah3
    yo "Э-эм, ну, я как раз закончил с экскурсией для Ллойда и Дариуса. Ллойд отправился в наш домик работать."

    hide aiden2_autumn
    hide aiden2 shock2
    show aiden_autumn at left
    show aiden amazed2 at left
    voice audio.aiden_v_shock3a2
    a "Быть не может, они ещё и останутся у нас?! "
    a "Здорово! Мы будем соседями по комнате, Дар!"

    show darius happy2 at right
    voice audio.darius_v_excited1a1
    d "Круто."

    show aiden happy1 at left
    voice audio.aiden_v_actually1a
    a "С кухней на сегодня покончено. Похоже, у вас тоже перерыв!"

    show yoshi comp2 at center
    voice audio.yoshi_v_unsure3a
    yo "Можно и так сказать… Сегодня был трудный день."

    show aiden happy3 at left
    voice audio.aiden_v_anyway1a
    a "Кстати, Дариус! Нам так и не выдалось возможности поговорить! Как ты, парниша~?"

    show darius happy1 at right
    voice audio.darius_v_response2a
    d "В порядке. И жду не дождусь работать."

    hide aiden_autumn
    hide aiden happy3
    show aiden2_autumn at left
    show aiden2 kiss2 at left
    voice audio.aiden_v_sheesh1a
    a "Да уж, а так и не скажешь. Ну же, расскажи нам больше! Чем занимался все эти годы?"

    hide yoshi_autumn
    hide yoshi comp2
    show yoshi2_autumn at center
    show yoshi2 awkward3 at center
    voice audio.yoshi_v_aiden13
    yo "Эйден… Не надо заставлять его говорить…"

    show darius sad2 at right
    voice audio.darius_v_no1a
    d "Нет, он прав."
    d "Иногда я просто не знаю, что мне сказать."

    hide aiden2_autumn
    hide aiden2 kiss2
    show aiden_autumn at left
    show aiden laugh2 at left
    voice audio.aiden_v_laugh2a1
    a "Ха-ха! Ты всегда был тихим, хотя я и думал, что тебе удастся это перебороть за столько лет! "

    show darius awkward1 at right
    d "..."

    show aiden happy1 at left
    voice audio.aiden_v_conj2a3
    a "Понимаешь, Дариус был мне как братом ещё когда мы были скаутами, Йоши."
    a "У него не было много друзей из-за того, что скауты легко его пугались."

    show darius sigh1 at right
    voice audio.darius_v_confident1
    d "Всё так."

    hide yoshi2_autumn
    hide yoshi2 awkward3
    show yoshi_autumn at center
    show yoshi think2 at center
    voice audio.yoshi_v_think1a
    yo "Я помню, как пару раз видел его с тобой, когда проходил мимо столовой."

    show aiden grin1 at left
    voice audio.aiden_v_yeah1b1
    a "Да! Обычно он проводил время там, когда не был со своим соседом."

    hide yoshi_autumn
    hide yoshi think2
    show yoshi2_autumn at center
    show yoshi2 shy5 at center
    voice audio.yoshi_v_unsure3c
    yo "Я т-тогда просто не знал, как сблизиться с ним, с тех пор как его стали называть Дариус Серьёзность… Я подумал, может, это из-за того, что он был забиякой…"

    show aiden bold2 at left
    voice audio.aiden_v_bro1b
    a "Бро, поэтому-то тебе и стоит чаще говорить, так люди вроде Йоши не будут тебя бояться."

    show darius sad3 at right
    voice audio.darius_v_sorry2b
    d "Прости, если я страшный."

    hide yoshi2_autumn
    hide yoshi2 shy5
    show yoshi_autumn at center
    show yoshi comp2 at center
    voice audio.yoshi_v_no5
    yo "В-всё не так, Дариус! Я понимаю, что ты просто по натуре такой тихий – это я был не прав в том, что и не пытался сблизиться с тобой."

    show darius talk2 at right
    voice audio.darius_v_conj1b1
    d "Я хочу со всеми ладить. Но в отличие от Ллойда, я не умею поддерживать беседу."

    show aiden relief2 at left
    voice audio.aiden_v_comp1a1
    a "Не думай сильно об этом и просто старайся двигаться по течению!"

    show darius comp2 at right
    voice audio.darius_v_thanks1a1
    d "Спасибо, приму к сведению. "
    d "Просто обычно Ллойд говорит всё за меня. "

    show aiden comp3 at left
    voice audio.aiden_v_unsure1b
    a "Справедливо, каждому тихому человеку нужен свой общительный, чтобы сохранять баланс."

    show darius explain2 at right
    voice audio.darius_v_agree3
    d "Согласен. Удобно, что мне не приходится ничего говорить, когда рядом Ллойд."
    d "Пускай некоторые и находят его грубым и надоедливым, потому что со стороны выглядит, словно он меня перебивает."

    show darius comp2 at right
    voice audio.darius_v_conj5b
    d "Но… Но если честно, всё совсем наоборот. Мне нравится, как он выражает свои мысли. Хотелось бы мне быть таким же."

    show aiden tease1 at left
    voice audio.aiden_v_oho1b
    a "Посмотрите на него, мистер \"я-не-умею-поддерживать-беседу\"~"

    show darius shock5 at right
    voice audio.darius_v_ah1d3
    d "Э-эм… "

    show yoshi awkward3 at center
    voice audio.yoshi_v_aiden6
    yo "Эйден! Не надо его дразнить!"

    show darius comp5 at right
    voice audio.darius_v_comp3a
    d "Всё хорошо. Я привык к шуткам Эйдена."
    d "Я так с ним впервые и познакомился."

    show aiden laugh1 at left
    voice audio.aiden_v_laugh2a1
    a "Ха-ха! Йоши знает меня уже целую вечность, а до сих пор не привык!"

    show yoshi annoy3 at center
    voice audio.yoshi_v_well3
    yo "В-вообще-то, привык! Но не когда дело касается других!"

    show darius tease2 at right
    voice audio.darius_v_question1c
    d "Завидуешь?"

    hide yoshi_autumn
    hide yoshi annoy3
    show yoshi2_autumn at center
    show yoshi2 awkward4 at center
    voice audio.yoshi_v_what4
    yo "Ч-что…?"

    show aiden laugh4 at left
    voice audio.aiden_v_laugh2c1
    a "Ха-ха-ха-ха! Жжёшь, бро!"

    hide yoshi2_autumn
    hide yoshi2 awkward4
    show yoshi_autumn at center
    show yoshi comp3 at center
    voice audio.yoshi_v_anyway3a
    yo "В-в любом случае, я лишь хотел сказать, что рад был бы узнать тебя получше, Дариус!"
    yo "Надеюсь, мы оба хорошо проведём время в лагере! В конце концов, никогда не поздно стать друзьями. "

    show darius comp2 at right
    voice audio.darius_v_thanks2a1
    d "Спасибо. Ты очень дружелюблный."

    hide darius_autumn
    hide darius comp2
    with dissolve

    hide yoshi_autumn
    hide yoshi comp3
    show yoshi2_autumn at center
    show yoshi2 panic2 at center
    voice audio.yoshi_v_ah3
    yo "А-ах… Я что-то не так сказал…?"

    show aiden comp5 at left
    voice audio.aiden_v_no2a1
    a "Ха-ха-ха! Не думаю, мне кажетсся, Дариус просто решил, что беседа окончена."

    show aiden comp5 at left2
    show aiden_autumn at left2
    show yoshi2_autumn at right2
    show yoshi2 confused5 at right2
    with move

    voice audio.yoshi_v_isee1
    yo "О… Вот как… А Дариус интересный парень, а?"

    show aiden comp2 at left2
    voice audio.aiden_v_well1b2
    a "Ты просто не привык иметь дело с непоколебимыми людьми, Йоши. Ты скорее водишься с более общительными."
    a "Ну то есть, я живое тому доказательство! "

    hide yoshi2_autumn
    hide yoshi2 confused5
    show yoshi_autumn at right2
    show yoshi comp3 at right2
    voice audio.yoshi_v_right9
    yo "Ха-ха, думаю, тут ты прав, Эйден."

    show aiden happy1 at left2
    voice audio.aiden_v_anyway1a
    a "Ну ладно, раз со всем на сегодня покончено, может вернёмся и отдохнём немного?"

    show yoshi explain2 at right2
    voice audio.yoshi_v_well1
    yo "Вообще-то, мне ещё нужно написать отчёт сэру Горо о произошедшем за сегодня."

    hide aiden_autumn
    hide aiden happy1
    show aiden2_autumn at left2
    show aiden2 sleepy2 at left2
    voice audio.aiden_v_amazed2a1
    a "Вау… Как увлекательно."

    show yoshi talk2 at right2
    voice audio.yoshi_v_hey1
    yo "Эй, кто-то должен этим заняться."

    hide aiden2_autumn
    hide aiden2 sleepy2
    show aiden_autumn at left2
    show aiden explain1 at left2
    voice audio.aiden_v_agree5b
    a "Знаю-знаю. Твоя работа очень важная, все дела~ "

    hide aiden_autumn
    hide aiden explain1
    show aiden2_autumn at left2
    show aiden2 sigh1 at left2
    voice audio.aiden_v_unsure1b
    a "В какой-то степени я даже понимаю Дариуса. "
    a "Мне повезло, что у меня есть ты, потому что ты можешь столько всего крутого, чего я и в миллион лет не смогу добиться!"

    show yoshi comp2 at right2
    voice audio.yoshi_v_disagree2
    yo "Неправда, Эйден. Если бы ты попытался, и сам бы смог тоже!"

    hide aiden2_autumn
    hide aiden2 sigh1
    show aiden_autumn at left2
    show aiden happy1 at left2
    voice audio.aiden_v_no2a1
    a "Да не нужно, с тобой рядом я в стопроцентной защите! "
    a "…прям как в презервативе."

    show yoshi awkward3 at right2
    voice audio.yoshi_v_aiden10
    yo "Эйден!!!"

    show aiden laugh2 at left2
    voice audio.aiden_v_laugh2c1
    a "Ха-ха-ха! Ладно уж, я пойду с тобой~ Могу просто полежать в кресле, пока ты работаешь!"

    show yoshi happy2 at right2
    voice audio.yoshi_v_gratitude1
    yo "Спасибо, Эйден. буду рад твоей компании."

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
    yu "Угх-х… Я та-а-ак устала…"

    show yoshi happy1 at left
    voice audio.yoshi_v_yuri2
    yo "и тебе привет, Юри! Как прошёл онакомительный тур?"

    show yuri worry4 at right
    voice audio.yuri_v_no3a1
    yu "Я думала, что приветствовать тридцать человек будет весело, а на деле вышло куда больше работы, чем я предполагала."

    show yoshi comp3 at left
    voice audio.yoshi_v_well3
    yo "Н-ну… Тебе пришлось и обучать их правилам лагеря, и помочь им расположиться в домиках… не удивительно, что ты так устала."

    show yuri think4 at right
    voice audio.yuri_v_yeah1d2
    yu "Да-а-а уж… Мне пришлось ссмотреть за тем,чтобы всем было удобно, поэтому я посматривала за ними время от времени."
    yu "Это сильно отличается от того, когда я заботилась о скаутах. У больших парней большие запросы, если вы понимаете, о чём я?"

    show aiden talk2 at center
    voice audio.aiden_v_response2b3
    a "Понимаю. Давно я не готовил и убирал за стольким количеством людей!"

    show yoshi bold2 at left
    voice audio.yoshi_v_excited1
    yo "Но разве не волнительно В последнее время здесь было так тихо, а шум и суета как раз кстати для разнообразия!"

    show yuri confused3 at right
    voice audio.yuri_v_conj4a
    yu "А разве у тебя не перерыв? Я видела как ты проходил по лагерю с Ллойдом и Дариусом весь день."

    show yoshi talk1 at left
    voice audio.yoshi_v_sigh3a
    yo "Честно сказать, я измотан… но ещё нужно закончить отчёт для сэра Горо о проделанной работе."

    show aiden confused3 at center
    voice audio.aiden_v_yeah2a1
    a "О да, кстати о Дедуле, не пора ли ему уже вернуться?"

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
    g "*вздох*"

    show yuri talk2 at p4_4
    voice audio.yuri_v_goro1b
    yu "О, помяни чёрта! С возвращением, пап!"

    show goro talk1 at p4_1
    voice audio.goro_v_goodpm2a1
    g "А, добрый вечер, всем вам. "
    g "Всё прошло согласно плану?"

    show yoshi happy1 at p4_2
    voice audio.yoshi_v_yessir1
    yo "Да, сэр! Юри занялась поставкой, работниками и подгтоовила все жилищные условия, а Эйден всех накормил."

    show yoshi bold5 at p4_2
    voice audio.yoshi_v_conj5b
    yo "Тем временем я разобрался c бригадирами и провёл им экскурсию, обсудив их планы на следующие несколько дней."
    yo "Я выписал полный отчёт для вас обо всех планах, она у вас на столе, как у вас появится возможность просмотреть его!"

    show goro happy1 at p4_1
    voice audio.goro_v_thanks2a1
    g "Благодарю, Йошинори. Отлично."

    show aiden excited3 at p4_3
    voice audio.aiden_v_goro1b
    a "О, и, угадай что, Дедуль? Бригадирами оказались два наших бывших скаута, Дариус и Ллойд! помнишь их?"

    hide goro_autumn
    hide goro happy1
    show goro2_autumn at p4_1
    show goro2 play2 at p4_1
    voice audio.goro_v_really2a
    g "Серьёзно? Какое облегчение – они точно знают место получше остальных."
    g "Интересно, нанял ли их мистер Клермонт нарочно…"

    show yoshi happy1 at p4_2
    voice audio.yoshi_v_actually1a
    yo "Вообще, когда мы обсуждали это с ними, оба сказали, что записал сразу после того, как увидели заявку от Лагеря Друзей."
    yo "Должно быть они были сильно взволнованы тем, что смогут вернуться в лагерь и помочь здесь после тех хороших времён в прошлом! "

    hide goro2_autumn
    hide goro2 play2
    show goro_autumn at p4_1
    show goro comp2 at p4_1
    voice audio.goro_v_glad1a
    g "Рад слышать это. звучит так, словно мы можем расчитывать на их поддержку. Отлично поработали, все трое."

    show yuri talk1 at p4_4
    voice audio.yuri_v_goro5a
    yu "А как у тебя с делами, папа? Чем занимался всё это время?"

    show goro talk3 at p4_1
    voice audio.goro_v_oh1a
    g "О, я оформлял разрешения работы необходимые мистеру Клермонту в мэрии. "
    g "Нам стоит быть готовыми ко всей работе, что будет проходить следующие дни."

    show yoshi excited1 at p4_2
    voice audio.yoshi_v_praise1
    yo "Прекрасно, сэр! Хотелось бы отметить, я так нервничал, наблюдая, как много прибыло людей, но похоже теперь мы обо всём позаботились."

    hide goro_autumn
    hide goro talk3
    show goro2_autumn at p4_1
    show goro2 explain2 at p4_1
    voice audio.goro_v_no1a1
    g "Не совсем, Йошинори. Я также пересматривал документы переданные мистером Клермонтом, так что мы вполне можем ожидать новую партию специалистов с застрашнего дня."

    hide goro2_autumn
    hide goro2 explain2
    show goro_autumn at p4_1
    show goro talk2 at p4_1
    voice audio.goro_v_yoshi2a
    g "Йошинори, мне нужно, чтобы ты позаботился и о них, как сегодня с Дариусом и Ллойдом. Всё понятно?"

    show yoshi bold2 at p4_2
    voice audio.yoshi_v_confident1
    yo "Да, сэр! расчитывайте на меня!"

    show goro talk1 at p4_1
    voice audio.goro_v_think1a1
    g "Похоже, сегодня мы коснулись лишь вершины айберга работы, которую предстоит сделать, и нашим первым большим испытанием будет проверка через неделю."
    g "Нам придется хорошенько потрудиться, дабы подготовить всё к тому моменту, так что я ожидаю от вас полной гтовности ко всему."

    show goro talk4 at p4_1
    voice audio.goro_v_request2a1
    g "Всё понятно?"

    show yoshi happy1 at p4_2
    show aiden happy1 at p4_3
    show yuri happy1 at p4_4
    all "Есть, сэр!"

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
