label day2:
    $ day = "02"
    $ time = timeline_timeday
    $ location = location_office
    $ working = True
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_office_autumn_day with fade
    play music buddy_oath_casual loop

    show goro_semiformal at center
    show goro explain2 at center
    voice audio.goro_v_alright1a2
    g "Ладно… Надо убедиться, что я ничего не забыл…"

    play sound sfx_doorknock
    $ renpy.pause (1.0, hard=True)
    show goro talk1 at center
    voice audio.goro_v_greet2a1
    g "Войдите."

    show yoshi_autumn at p5_5
    show yoshi happy1 at p5_5
    with dissolve

    voice audio.yoshi_v_goodam1
    yo "Доброе тро, сэр Горо!"

    show goro_semiformal at left2
    show goro talk1 at left2
    show yoshi_autumn at right2
    show yoshi happy1 at right2
    with move

    hide yoshi_autumn
    hide yoshi happy1
    show yoshi_autumn at right2
    show yoshi amazed1 at right2
    voice audio.yoshi_v_praise3
    yo "Вы как будто в спешке. Собираетесь куда-то?"

    show goro talk3 at left2
    voice audio.goro_v_agree2a1
    g "А, да, собираюсь. У меня назначена встреча с мистером Клермонтом. "

    hide yoshi amazed1
    show yoshi talk1 at right2
    voice audio.yoshi_v_oh1
    yo "Оу. А что на повестке дня, могу узнать?"

    show goro explain2 at left2
    voice audio.goro_v_comp2a1
    g "Всего лишь обычная встреча, нужно обсудить прогресс в спонсорстве. Подумал, что и упоминания не стоит."

    show yoshi comp6 at right2
    voice audio.yoshi_v_laugh3
    yo "Хе-хе, вы и правда любите секретничать касательно своей работы, сэр. "
    yo "Хотя, мне немного любопытно – вы не волнуетесь сегодняшней с ним встрече? "

    show goro confused3  at left2
    voice audio.goro_v_no2a1
    g "Нет, совсем нет. А почему ты спрашиваешь? "

    hide yoshi_autumn
    hide yoshi comp6
    show yoshi2_autumn at right2
    show yoshi2 comp2 at right2
    voice audio.yoshi_v_well3
    yo "Н-ну, прошлый раз, как мистер Клермонт был тут, вы вели себя весьма не как обычно. Я имею ввиду… Никогда раньше не видел вас таким взбалмошным."

    hide goro confused3
    show goro annoy2 at left2
    voice audio.goro_v_hey5a
    g "Эй, я вёл себя спокойно, пока показывал ему окресности… И постарался не показывать своё волнение до тех пора, пока он не уйдёт."
    g "В конце концов, мистер Клермонт это тот, на кого я долгое время ровнялся. Никогда бы и не подумал, что встречусь с ним лично, потому его визит и застал меня врасплох."

    hide goro annoy2
    show goro explain5 at left2
    voice audio.goro_v_think1a1
    g "Его работы вдохновили меня пересмотреть самого себя в прошлом. "

    show yoshi2 shy5 at right2
    voice audio.yoshi_v_right4
    yo "И правда…"

    show goro talk1 at left2
    voice audio.goro_v_anyway2
    g "Итак, Что привело тебя в офис, Йошинори?"

    hide yoshi2_autumn
    hide yoshi2 shy5
    show yoshi_autumn at right2
    show yoshi talk3 at right2
    voice audio.yoshi_v_actually1a
    yo "О… Вообще, я планировал спросить про мой еженедельный список задач, но с этим можно и подождать, учитывая что вы заняты!"
    yo "Пока что я могу провести пару задач по обслуживанию лагеря, чтобы подедрживать всё в приличном состоянии. "

    hide goro_semiformal
    hide goro talk1
    show goro_semiformal at left2
    show goro think2 at left2
    voice audio.goro_v_yoshi2a
    g "Кстати, Йошинори…"

    hide goro_semiformal
    hide goro think2
    show goro_semiformal at left2
    show goro talk2 at left2
    g "А не пойти ли тебе сегодня со мной?"

    show yoshi awkward4 at right2
    voice audio.yoshi_v_really1
    yo "С вами, сэр? Не хотелось бы путаться под ногами, особенно на такой важной встрече."

    show goro happy2 at left2
    voice audio.goro_v_dismiss2a
    g "Чепуха какая. Рано или поздно, тебе всё равно придётся посещать такие в будущем."
    g "Однако, тебе понадобится вид поформальней. У меня есть запасной костюм, можешь использовать его. Поношенный, но должен быть тебе в пору."

    show goro talk3 at left2
    voice audio.goro_v_response1b1
    g "Отправляемся сразу после того, как переоденешься."

    show yoshi happy2 at right2
    voice audio.yoshi_v_yessir1
    yo "Есть, сэр!"

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black
    play sound sfx_carstart
    hide screen location
    hide screen timeline
    hide screen quick_menu
    $quick_menu = False
    with fade
    $ renpy.pause (2.0, hard=True)

    $ location = location_car
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene cgg2 1 with fade
    play music old_familiar_home loop
    play bgsound sfxloop_carride loop

    yo "{i}(Не знаю почему, но, пускай мы и едем по деловым вопросам… Я так взволнован быть сегодня вместе с сэром Горо.){/i}"
    yo "{i}(Словно я вернулся к походам, которые раньше часто устраивали.){/i}"
    g "..."

    show cgg2 2 with Dissolve(0.25)
    yo "{i}(Довольно редкое зрелище видеть меня и сэра Горо в дороге, но мы едва ли даже разговаривали с тех пор, как выехали этим утром…){/i}"
    yo "{i}(Надо бы что-нибудь сказать, чтобы разбавить обстановку…){/i}"

    $working = False
    $shuffle_menu()
    menu():
        yo "{i}(Надо бы что-нибудь сказать, чтобы разбавить обстановку…){/i}{fast}"
        "Сидеть тихо.":
            $working = True
            $score_goro -= 1
            show cgg2 3a with Dissolve(0.25)
            yo "{i}(Не хочется, чтобы меня сочли несерьёзно относящимся к этой встрече, может быть, лучше просто посидеть тихо.){/i}"

            show cgg2 5 with Dissolve(0.25)
            voice audio.goro_vsg3_line2ab
            g "*кхем* Что же, Йошинори."

            voice audio.yoshi_vsg3_line2ab
            yo "О! Да, сэр?"

            voice audio.goro_vsg3_line3ab
            g "Не мог не заметить ту брошку, что ты закрепил на костюме."
        "Поговорить о погоде.":
            $working = True
            show cgg2 3b with Dissolve(0.25)
            voice audio.yoshi_vsg3_line1b
            yo "П-погода вот сегодня хорошая, да, сэр…?"

            show cgg2 4b with Dissolve(0.25)
            voice audio.goro_vsg3_line1b
            g "Да, хорошая."

            yo "{i}(Да уж, ничего не вышло… ){/i}"

            show cgg2 5 with Dissolve(0.25)
            voice audio.goro_vsg3_line2ab
            g "*кхем* Что же, Йошинори."

            voice audio.yoshi_vsg3_line2ab
            yo "О! Да, сэр?"

            voice audio.goro_vsg3_line3ab
            g "Не мог не заметить ту брошку, что ты закрепил на костюме."
        "Обсудить встречу.":
            $working = True
            $score_goro += 1
            show cgg2 3cd with Dissolve(0.25)
            voice audio.yoshi_vsg3_line1c
            yo "С-спасибо ещё раз, что позволили мне присоединиться к вам сегодня, сэр…!"

            voice audio.yoshi_vsg3_line2c
            yo "Не до конца уверен, как именно я смогу помочь, но я рад, что вы позволили мне увидить над, чем вы работали с мистером Клермонтом в последние пару недель."

            show cgg2 4c with Dissolve(0.25)
            voice audio.goro_vsg3_line1c
            g "Рад, что ты в предвкушении. Настолько, что так сильно прихорашивался в костюме."

            voice audio.yoshi_vsg3_line3c
            yo "А-ах…! А я и не знал, что так выглядел…!"

            show cgg2 5 with Dissolve(0.25)
            voice audio.goro_vsg3_line3cd
            g "И тем не менее… Не мог не заметить ту брошку, что ты закрепил на костюме."
        "Поговорить о костюме.":
            $working = True
            $score_goro += 2
            show cgg2 3cd with Dissolve(0.25)
            voice audio.yoshi_vsg3_line1d
            yo "С-спасибо ещё раз, что одолжили мне этот костюм, сэр…! Давно я не носил чего-то подобного!"

            show cgg2 4d with Dissolve(0.25)
            voice audio.goro_vsg3_line1d
            g "Ах, надеюсь, он не большиват для тебя. "

            voice audio.yoshi_vsg3_line2d
            yo "Совсем нет, сэр! Оно и для сезона как раз хороший вариант!"

            voice audio.goro_vsg3_line2d
            g "Вот и хорошо. Знал, что такой стиль и цвет тебе будет как раз…"

            show cgg2 5 with Dissolve(0.25)
            voice audio.goro_vsg3_line3cd
            g "И тем не менее… Не мог не заметить ту брошку, что ты закрепил на костюме."

    show cg fade at truecenter
    show fxg1 at fx_pos
    with dissolve

    voice audio.goro_vsg3_line4
    g "Эта ли не та, которую я подарил тебе, ещё когда ты был скаутом?"

    voice audio.yoshi_vsg3_line4
    yo "Да, она самая, сэр…!   "

    voice audio.goro_vsg3_line5
    g "Я не видел её столько лет. Удивлён, что ты до сих пор её хранишь."

    voice audio.yoshi_vsg3_line5
    yo "Ещё бы, она многое для меня значила, вот я и держал её в целости и сохранности."

    voice audio.yoshi_vsg3_line6
    yo "Подумал, может принесёт удачу на сегодня!"

    hide cg fade
    hide fxg1
    with dissolve

    show cgg2 6 with Dissolve(0.25)
    voice audio.goro_vsg3_line6
    g "Ха-ха-ха, а ты ещё думал, что это я волновался."

    voice audio.yoshi_vsg3_line7
    yo "А… Хе-хе-хе…"

    show cgg2 7 with Dissolve(0.25)
    voice audio.goro_vsg3_line7
    g "Знаешь, а Юри даже позавидовала, когда я дал тебе эту брошку."

    voice audio.goro_vsg3_line8
    g "Она даже обвинила меня в том, что у меня есть любимчики среди кэмперов."

    voice audio.goro_vsg3_line9
    g "Но по-другому и быть не могло… Ты был тем ещё хвастуном будучи скаутом."

    voice audio.yoshi_vsg3_line8
    yo "П-правда? С трудом помню, каким я тогда был…"

    show cgg2 8 with Dissolve(0.25)
    voice audio.goro_vsg3_line10
    g "Если говорить за себя, не многое изменилось… Ты всё тот же энергичный, бодрый скаут, которого я помню."

    voice audio.goro_vsg3_line11
    g "Ты и вправду сильно выделялся среди сверстников, особенно в тот первых поход."

    voice audio.goro_vsg3_line12
    g "Как факт, тогда я и подарил тебе эту брошку."

    show cgg2 9 with Dissolve(0.25)
    voice audio.yoshi_vsg3_line9
    yo "Да, я помню…"

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    hide screen location
    hide screen timeline
    hide screen quick_menu
    $quick_menu = False
    scene cg white with Dissolve(2.0)
    $past_scene = True

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

    show ygoro_camp at center
    show ygoro talk1 at center
    voice audio.ygoro_v_attention1a
    g "Внимание, скауты! Через несколько минут мы отправимся в поля!"

    show ygoro explain2 at center
    g "Я хочу, чтобы каждый вместе со своим партнёром перепроверили снаряжение каждого."

    show ygoro talk3 at center
    voice audio.ygoro_v_dismiss2b
    g "На этом всё! Отправляемся через пять минут!"

    hide ygoro_camp
    hide ygoro talk3
    with dissolve

    show yyoshi_camp at left2
    show yyoshi norm1 at left2
    show yyuri_camp2 at right2
    show yyuri annoy5 at right2
    with dissolve

    voice audio.yyuri_v_ugh3c
    yu "У-у-угх… Ещё пять минут? А не можем уже сейчас? Мы уже два часа как проснулись!"

    show yyoshi talk3 at left2
    voice audio.yyoshi_v_yuri9a
    yo "Ну же, Юри. Это время мы потратили на то, чтобы переодеться и позавтракать."
    yo "Что более важно, ты же знаешь, как много эти проверки значат."

    show yyuri angry3 at right2
    voice audio.yyuri_v_but1b
    yu "Но ты уже проверил наши вещи раз пять уже за это утро!"

    show yyoshi play2 at left2
    voice audio.yyoshi_v_laugh5
    yo "И если бы не проверил, то и не обнаружил бы, что ты не взяла ничего, кроме своих тетрадок."

    show yyuri pout3 at right2
    voice audio.yyuri_v_hmph1a
    yu "Это фанфики, хмпф!"

    show yyoshi_camp at left
    show yyoshi play2 at left
    show yyuri_camp2 at center
    show yyuri pout3 at center
    with move

    show ygoro_camp at right
    show ygoro comp3 at right
    with dissolve

    voice audio.ygoro_v_yuridear1
    g "Дорогая, поэтому я и поставил тебя в пару с Йошинори. Ха-ха-ха."

    show yyuri annoy4 at center
    voice audio.yyuri_v_question1b
    yu "Этот поход всего на ночь, зачем нам так много вещей?"

    show ygoro explain4 at right
    voice audio.ygoro_v_well1
    g "Ну, если бы ты была внимательней на наших уроках, ты бы знала, что брать главнее всего: а это средства навигации, соответствующую еду и воду, аптечку первой помощи и многое другое!"

    show yyoshi bold2 at left
    voice audio.yyoshi_v_sir2
    yo "Мы упаковали дополнительную одежду, спрей от насекомых, а также туалетные принадлежности, сэр!"

    show ygoro play3 at right
    voice audio.ygoro_v_see5a
    g "Видишь? Сразу видно, Йошинори всё подмечал!"

    show yyuri rage3 at center
    voice audio.yyuri_v_rush3b
    yu "Ну, твои пять минут вышли и мы все готовы, так пошли-и-и-и же!"

    show ygoro comp2 at right
    voice audio.ygoro_v_alright1a
    g "Ладно-ладно, я позову остальных."

    show yyoshi_camp at p6_1
    show yyoshi bold2 at p6_1
    show yyuri_camp2 at p6_2
    show yyuri rage3 at p6_2
    show ygoro_camp at center
    show ygoro comp2 at center
    with move

    show ygoro happy1 at center
    voice audio.ygoro_v_okay2a
    g "Итак, скауты! Выстроиться в линию и найти своего друга! Начинаем марш."

    show ygoro happy3 at center
    voice audio.ygoro_v_rush1b1
    g "За мной!"

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black
    hide screen location
    hide screen timeline
    hide screen quick_menu
    $quick_menu = False
    with fade
    play sound sfx_trekking
    $ renpy.pause (2.0, hard=True)

    $ location = location_forest
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_forest_past_day with fade
    play music adventure loop
    play bgsound sfxloop_birds loop

    show ygoro_camp at center
    show ygoro talk3 at center
    voice audio.ygoro_v_worry1a
    g "Как самочувствие у всех? "
    g "путь что я выбрал - кратчайший и безопаснейший, так чтобы каждый смог ознакомиться с местностью для следующих походов!"

    show ygoro talk4 at center
    voice audio.ygoro_v_comp2a1
    g "Просто старайтесь держаться вместе с вашим напарником и следовать за мной, хорошо, скауты?"
    all "Есть, сэр!"

    show ygoro explain2 at center
    voice audio.ygoro_v_rush4
    g "Итак, кто-то из вас может задуматься, зачем я разделили вас на пары. Причина тому - развить ваше чувство кооперации, оно особенно важно в экстренных ситуациях!"
    g "Если вы отстали от группы, важно оставаться в спокойствии и найти решение вместе с вашим партнёром!"

    show ygoro talk2 at center
    voice audio.ygoro_v_conj7a
    g "Вы можете воспользоваться инструментами навигации, чтобы вновь встать на верный путь и достичь места назначения, либо чтобы вернуться в лагерь."

    show ygoro explain5 at center
    voice audio.ygoro_v_comp2a1
    g "На случай, если вы совсем потерялись, не паникуйте, помните: важно сохранять свою энергию и оставаться на месте."
    g "Вы сможете воспользоваться вашими инструментами выживания, кремнем, фонариком и спальным мешком, чтобы соорудить временный лагерь."

    show ygoro talk2 at center
    voice audio.ygoro_v_conj2a1
    g "Развести огонь будет особенно полезным, так как дым сможет помочь команде спасения найти вас быстрее. "

    show ygoro bold2 at center
    voice audio.ygoro_v_request2a1
    g "Вместе со всеми этими инструментами и заниями из сегодняшнего урока, вы точно сможете справиться с экстренными ситуациями!"

    show ygoro_camp at p5_5
    show ygoro bold2 at p5_5
    with move

    show yyuri_camp2 at p5_1
    show yyuri fangirl1 at p5_1
    show yyoshi_camp at p5_2
    show yyoshi norm1 at p5_2
    with dissolve

    voice audio.yyuri_v_kyaa1
    yu "Кья-я-я! Не могу поверить, что наконец-то чем то займёмся!"
    yu "так наскучило постоянно сидеть в лагере весь день!"

    show yyoshi angry2 at p5_2
    voice audio.yyoshi_v_yuri9b
    yo "Юри, не говори так! Я уверен, у сэра горо были причины на то, чтобы держать нас внутри лагеря, и он делал всё возможное, чтобы здесь всё было интересно!"

    show yyuri angry6 at p5_1
    voice audio.yyuri_v_yeah1h1
    yu "Да-да, знаю я! Но неужели нам ПРАВДА нужно было ждать целых две недели, только чтобы начать поход?"

    show yyoshi explain2 at p5_2
    voice audio.yyoshi_v_conj1a
    yo "Уверен, такие вылазки требуют много планирования и подготовки, чтобы всё прошло идеально!"
    yo "К тому же, разве не здорово, что нам выдалась возможность узнать так много нового и крутого от сэра Горо? "

    show yyuri sigh1 at p5_1
    voice audio.yyuri_v_sigh1a
    yu "*вздох* Беда в том, что я уже всё это знаю…"

    show yyuri_camp2 at left
    show yyuri norm1 at left
    show yyoshi_camp at center
    show yyoshi norm1 at center
    show ygoro_camp at right
    show ygoro bold2 at right
    with move

    show ygoro disappoint2 at right
    voice audio.ygoro_v_ehem1a
    g "*кхем* Не у всех здесь была фора как у тебя, милая."

    show yyoshi shock2 at center
    voice audio.yyoshi_v_sirgoro10a
    yo "А-ах, сэр Горо…!"

    show ygoro happy2 at right
    voice audio.ygoro_v_well1
    g "Юри много интересовалась природой в прошлом, потому большинство того, чему я учу вас она уже знает."

    show yyuri happy1 at left
    voice audio.yyuri_v_yeah1b1
    yu "Да! Папа покупал мне много книг с уроками по выживанию и кэмпингу!"

    show ygoro explain3 at right
    voice audio.ygoro_v_conj6a1
    g "Но на практике всё по-другому! Как и ты, большинство скаутов ещё ни разу не были в настоящих походах на свежем воздухе. "

    show ygoro talk1 at right
    voice audio.ygoro_v_conj1a1
    g "Это мой долг как скаутмастера - подготовить всех путём наших уроков и упражнений к путешествию как это."
    g "Со всем, чему я учил всех, гарантирую, что каждому будет весело, а главное безопасно!"

    show yyuri sigh1 at left
    voice audio.yyuri_v_unsure3a
    yu "Думаю, тут ты прав…"

    show ygoro comp2 at right
    voice audio.ygoro_v_yuridear1
    g "Будь терпеливее, дорогая. Пользуйся моментом и поделись знаниями, которые ты обрела!"

    show yyuri talk3 at left
    voice audio.yyuri_v_but1a
    yu "Но Йоши вроде бы и так всё знает тоже."

    show yyoshi comp2 at center
    voice audio.yyoshi_v_oh2
    yo "О-оу! Я знаю всё из уроков сэра Горо…!"
    yo "Нам так повезло, что вы нас учите и направляете, сэр!"

    show yyuri tease2 at left
    voice audio.yyuri_v_laugh2b1
    yu "Хе-хе-хе… Только посмотрите, как он подлизывается к моему папе~"

    show yyoshi awkward4 at center
    voice audio.yyoshi_v_shock3
    yo "В-вах…! Я п-просто правду говорил!"
    yo "Все те мероприятия, которые для нас подготовил сэр Горо, особенно групповые, были отличной подготовкой для сегодняшнего дня!"

    show yyoshi happy2 at center
    voice audio.yyoshi_v_laugh1
    yo "Благодаря им нам удалось узнать друг друга поближе, а ещё мы узнали как работать сообща!"

    show ygoro bold2 at right
    voice audio.ygoro_v_laugh1a
    g "Тебе бы следовало понабраться энтузиазма у Йошинори, милая. Похоже, что он понимает суть уроков на ура!"

    show ygoro play2 at right
    voice audio.ygoro_v_rush4
    g "А теперь, продолжим поход? Мы почти на месте назначения!"

    play sound sfx_phonering
    show yyoshi shock1 at center
    show ygoro shock2 at right
    voice audio.ygoro_v_oh2
    g "О-ой…! А вообще, не нужно ответить на этот звонок."

    show ygoro_camp at p5_5
    show ygoro talk3 at p5_5
    show yyuri_camp2 at p5_1
    show yyuri pout1 at p5_1
    show yyoshi_camp at p5_2
    show yyoshi shock1 at p5_2
    with move

    voice audio.ygoro_v_ehem1a
    g "Внимание, скауты! Устроим небольшой перерыв! "
    g "Хорошенько воспользуйтесь этим временем, можете перекусить и попить. "

    show ygoro explain2 at p5_5
    voice audio.ygoro_v_bye4a
    g "Я скоро вернусь!"

    hide ygoro_camp
    hide ygoro explain2
    with dissolve

    show yyuri_camp2 at left2
    show yyuri  sigh1 at left2
    show yyoshi_camp at right2
    show yyoshi shock1 at right2
    with move

    voice audio.yyuri_v_sigh2a
    yu "*вздох* Только не снова… А я-то думала, что в этот раз всё будет хорошо."

    show yyoshi confused2 at right2
    voice audio.yyoshi_v_huh1
    yo "Х-ха? О чём ты, Юри?"

    show yyuri annoy4 at left2
    voice audio.yyuri_v_annoyed1a
    yu "Правда, не хочу об этом говорить. Мы всё равно ничего с этим поделать не сможем."

    show yyoshi worry2 at right2
    voice audio.yyoshi_v_unsure2a
    yo "Т-ты уверена? Может, есть что-то, чем мы сможем помочь сэру Го-"

    show yyuri_camp2 at center
    show yyuri annoy4 at center
    with move
    voice audio.yyuri_v_hmph2a
    yu "*ущипнула Йошинори*"

    show yyoshi pain3 at right2
    voice audio.yyoshi_v_oww1
    yo "А-ай! А это за что, Юри??"

    show yyuri angry2 at center
    voice audio.yyuri_v_annoyed3a
    yu "Я же сказала, это бессмысленно! Давай просто не лезть в это! "

    show yyoshi angry2 at right2
    voice audio.yyoshi_v_hmph1b
    yo "А щипать меня так сильно было необязательно…"

    show yyuri angry5 at center
    voice audio.yyuri_v_rush1b2
    yu "Пошли, раздадим всем немного закусок и воды, пока ждём!"

    show yyoshi talk3 at right2
    voice audio.yyoshi_v_right7
    yo "О… Хорошо."

    hide yyuri_camp2
    hide yyuri angry5
    with dissolve

    show yyoshi worry1 at right2
    yo "..."

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
    scene bg_forest_past_day with fade
    play music old_familiar_home_slow loop
    play bgsound sfxloop_birds loop

    show ygoro_camp at center
    show ygoro worry3 at center
    voice audio.ygoro_vsg4_line1
    g "…Что значит, ты не придёшь? Всё в порядке, даже если опоздаешь, мы можем подождать."

    show ygoro worry1 at center
    g "..."

    show ygoro angry3 at center
    voice audio.ygoro_vsg4_line2
    g "Как это у тебя нет времени?! Ты де знала, что я планировал эт омароприятие неделями, а—"

    show ygoro angry1 at center
    g "..."

    show ygoro angry4 at center
    voice audio.ygoro_vsg4_line3
    g "Юри так ждала сегодняшнего дня! Неужели ты не понимаешь, как важно для неё это? "

    show yyoshi_camp at p5_5
    show yyoshi worry1 at p5_5
    with dissolve

    yo "..."

    show ygoro disappoint4 at center
    voice audio.ygoro_vsg4_line4
    g "Тебя никогда нет рядом, Вера! Это единственный раз, когда я просил тебя побыть вместе, как семья!"

    voice audio.ygoro_vsg4_line5
    g "What are you even busy with?!"

    show ygoro panic1 at center
    g "..."

    show ygoro panic2 at center
    voice audio.ygoro_vsg4_line6
    g "Н-нет, я не пытаюсь обвинять тебя в чём-либо! "

    show ygoro worry4 at center
    voice audio.ygoro_vsg4_line7
    g "Знаю, заводить семью никогда не было нашим планом, но уже девятнадцать лет прошло! "

    voice audio.ygoro_vsg4_line8
    g "Прошу, приди, хотя бы ради Юри…"

    play sound sfx_phonebutton
    show ygoro worry2 at center
    voice audio.ygoro_vsg4_line9
    g "А-алло? "

    show ygoro sigh1 at center
    voice audio.ygoro_vsg4_line10
    g "*вздох*"

    show ygoro shock3 at center
    voice audio.ygoro_vsg4_line11
    g "А-ах! Йошинори…! "

    show ygoro_camp at left2
    show ygoro shock3 at left2
    show yyoshi_camp at right2
    show yyoshi worry2 at right2
    with move

    voice audio.yyoshi_vsg4_line1
    yo "Эм… Сэр? У вас всё хорошо…?"

    show ygoro awkward3 at left2
    voice audio.ygoro_vsg4_line12
    g "Д-да. Просто личные дела, ничего такого, о чём тебе стоит волноваться."

    voice audio.ygoro_vsg4_line13
    g "Что тебя сюда привело? "

    $working = False
    $shuffle_menu()
    menu():
        g "Что тебя сюда привело? {fast}"
        "Когда мы уже продолжим поход?":
            $working = True
            $score_goro -= 2
            show yyoshi talk1 at right2
            voice audio.yyoshi_vsg4_line2a
            yo "Просто хотел спросить, когда мы уже продолжим поход, сэр!"

            show ygoro explain2 at left2
            voice audio.ygoro_vsg4_line14a
            g "Вот как. Прошу прощения за задержку. Я мигом вернусь."

            show yyoshi explain2 at right2
            voice audio.yyoshi_vsg4_line4ab
            yo "В-вообще… Ещё я хотел спросить кое-что, если я могу как-то помочь, сэр…!"

            show ygoro confused3 at left2
            voice audio.ygoro_vsg4_line16ab
            g "О, в чём дело?"
        "Докладываю обстановку.":
            $working = True
            show yyoshi talk1 at right2
            voice audio.yyoshi_vsg4_line2b
            yo "Я здесь, чтобы доложить обстановку, сэр…!"

            show ygoro confused2 at left2
            voice audio.ygoro_vsg4_line14b
            g "Хм? У остальных всё хорошо?"

            show yyoshi talk2 at right2
            voice audio.yyoshi_vsg4_line3b
            g "Т-так точно, сэр! По факту, Юри и я раздали немного закусок и напитков между другими скаутами, пока ждали…!"

            show ygoro explain2 at left2
            voice audio.ygoro_vsg4_line15b
            g "А, хорошая работа, Йошинори. Я мигом вернусь и мы продолжим поход."

            show yyoshi explain2 at right2
            voice audio.yyoshi_vsg4_line4ab
            yo "В-вообще… Ещё я хотел спросить кое-что, если я могу как-то помочь, сэр…!"

            show ygoro confused3 at left2
            voice audio.ygoro_vsg4_line16ab
            g "О, в чём дело?"
        "Хотел проведать вас.":
            $working = True
            $score_goro += 1
            show yyoshi talk1 at right2
            voice audio.yyoshi_vsg4_line2c
            yo "Я п-просто хотел проведать вас, сэр…!"

            voice audio.yyoshi_vsg4_line3c
            yo "Юри и я раздавали немного закусок и напитков между другими скаутами, пока ждали."

            voice audio.yyoshi_vsg4_line4c
            yo "Вот я и подумал, что вам тоже немного полегчает от напитка, поэтому пошёл искать вас, как только мы закончили…!"

            show ygoro comp1 at left2
            g "..."

            show ygoro comp2 at left2
            voice audio.ygoro_vsg4_line14cd
            g "Спасибо за беспокойство, Йошинори. Я в порядке."

            show yyoshi worry2 at right2
            voice audio.yyoshi_vsg4_line4cd
            yo "П-простите за любопытство, но… если есть что-нибудь, что я могу для вас сделать, пожалуйста, позвольте вам помочь, сэр…"
        "Я заметил, что вы расстроены чем-то.":
            $working = True
            $score_goro += 2
            show yyoshi talk1 at right2
            voice audio.yyoshi_vsg4_line2d
            yo "Я заметил, что вы были расстроены когда вам позвонили… Вот я и подумал, что вам не помешает компания!"

            voice audio.yyoshi_vsg4_line3d
            yo "Можете не волноваться о других скаутах! Юри и я только закончили раздавать закуски и напитки!"

            show ygoro comp1 at left2
            g "..."

            show ygoro comp2 at left2
            voice audio.ygoro_vsg4_line14cd
            g "Спасибо за беспокойство, Йошинори. Я в порядке."

            show yyoshi worry2 at right2
            voice audio.yyoshi_vsg4_line4cd
            yo "П-простите за любопытство, но… если есть что-нибудь, что я могу для вас сделать, пожалуйста, позвольте вам помочь, сэр…

    show yyoshi comp2 at right2
    voice audio.yyoshi_vsg4_line5
    yo "Е-если хотите, я могу повести скаутов дальше в поход! Вам не стоит беспокиться за нас, карту я запомнил, так что не потеряемся!"

    voice audio.yyoshi_vsg4_line6
    yo "О-о, мы ещё можем заранее установить лагерь в полях, так у нас будет больше времени на занятия в остаток дня на открытом воздухе…!"

    show ygoro talk3 at left2
    voice audio.ygoro_vsg4_line17
    g "Я правда ценю твои намерения, Йошинори, но тебе необязательно брать всё в свои руки."

    show yyoshi worry3 at right2
    voice audio.yyoshi_vsg4_line7
    yo "Н-но, сэр…"

    show ygoro sigh1 at left2
    voice audio.ygoro_vsg4_line18
    g "*вздох* Я знал, что просто так ты не сдашься…"

    voice audio.ygoro_vsg4_line19
    show ygoro comp1 at left2
    g "Раз так, почему бы нам не повести скаутов вместе?"

    show yyoshi shock1 at right2
    yo "...!"

    show ygoro comp2 at left2
    voice audio.ygoro_vsg4_line20
    g "Я позволю тебе встать первым в строю, а я буду подле тебя наблюдать, чтобы всё следовали за тобой. Как тебе?"

    show ygoro comp1 at left2
    show yyoshi bold2 at right2
    voice audio.yyoshi_vsg4_line8
    yo "Буду почтён, сэр! Спасибо, что позволили помочь!"

    voice audio.yyoshi_vsg4_line9
    yo "Я мигом всех соберу…!"

    show yyoshi_camp at p6_6
    show yyoshi excited1 at p6_6
    with move

    show ygoro talk3 at left2
    voice audio.ygoro_vsg4_line21
    g "А, Йошинори… Ещё кое-что."

    show yyoshi_camp at right2
    show yyoshi talk3 at right2
    with move

    voice audio.yyoshi_vsg4_line10
    yo "Д-да, сэр…?"

    show ygoro comp2 at left2
    voice audio.ygoro_vsg4_line22
    g "Хочу, чтобы это было у тебя…"

    show ygoro_camp at center
    show ygoro comp2 at center
    with move

    show cg fade at truecenter
    show fxg1 at fx_pos
    with dissolve

    voice audio.ygoro_vsg4_line23
    g "Я сделал его ещё когда только готовился начинать Лагерь Друзей."

    voice audio.yyoshi_vsg4_line11
    yo "О, тот же символ, что везде в лагере и на наших костюмах…!"

    voice audio.ygoro_vsg4_line24
    g "Именно, эмблема олицетворяет саму суть этого лагеря."

    voice audio.ygoro_vsg4_line25
    g "Звезда, что всегда светит ярко, несмотря ни на что; как и тот, на кого ты всегда сможешь положиться в трудную минуту."

    voice audio.ygoro_vsg4_line26
    g "Возможно, сейчас эти слова не значат многого, но я уверяю тебя, однажды они обретут смысл."

    hide cg fade
    hide fxg1
    with dissolve

    show yyoshi comp2 at right2
    voice audio.yyoshi_vsg4_line12
    yo "С-спасибо огромное, сэр! Для меня честь получить такое…!"

    show ygoro comp5 at center
    voice audio.ygoro_vsg4_line27
    g "На здоровье, Йошинори. А теперь пойдём. Все уже наверное закончили перерыв."

    show yyoshi bold2 at right2
    voice audio.yyoshi_vsg4_line13
    yo "Есть, сэр!"

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

    $ location = location_car
    $ day = "02"
    $ time = timeline_timeday
    $ season = season_autumn
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene cgg2 10 with fade
    play music old_familiar_home loop
    play bgsound sfxloop_carride loop

    voice audio.yoshi_vsg3_line10
    yo "Т-теперь мне даже немного стыдно за то, как я себя тогда вёл… Я и не думал, что был таким занудой…"

    voice audio.goro_vsg3_line13
    g "Ну, не то, чтобы в этом было что-то плохое. Я понимал, что для тебя лагерь был таким волнительным."

    show cgg2 11 with Dissolve(0.25)
    voice audio.goro_vsg3_line14
    g "Если бы не это твоё качество, я бы, может, и не подарил тебе эту брошку."

    voice audio.yoshi_vsg3_line11
    yo "А-ах… Не уверен, следует ли мне считать это комплиментом, сэр. "

    show cgg2 12 with Dissolve(0.25)
    voice audio.goro_vsg3_line15
    g "Хм… Скажем так, я просто увидил в тебе что-то многообещающее, начиная с твоих поступков, заканчивая желанием вести за собой и нести ответственность."

    voice audio.goro_vsg3_line16
    g "Мне хотелось дать тебе что-то в знак признания этого."

    show cgg2 13 with Dissolve(0.25)
    voice audio.goro_vsg3_line17
    g "Хех, оказалось, я тоже был прав. Взгляни, как далеко ты зашёл. "

    voice audio.yoshi_vsg3_line12
    yo "С-спасибо вам, сэр. Я правда польщён тем, сколько надежды вы вкладываете в меня и мои способности."

    voice audio.yoshi_vsg3_line13
    yo "Хотя, должен признать, каждый раз, как вы мне говорите, что я - следующий на очереди, кто возьмёт вашу роль в Лагере Друзей, я всегда задумываюсь, справлюсь ли."

    show cgg2 14 with Dissolve(0.25)
    voice audio.goro_vsg3_line18
    g "Да ладно тебе, где же твой былой бескрайний энтузиазм? "

    voice audio.goro_vsg3_line19
    g "Скажи я молодому Йошинори, что он станет однажды во главе, он бы никогда не успокоился! "

    voice audio.goro_vsg3_line20
    g "К тому же, ты вёл за собой лагерь уже много лет. Пускай и были неудачи, твоё руководство в прошлом сезоне более чем доказывало, что в тебе есть всё то, чтобы продолжить эстафету."

    show cgg2 15 with Dissolve(0.25)
    voice audio.yoshi_vsg3_line14
    yo "Вы мне льстите, сэр…"

    voice audio.goro_vsg3_line21
    g "Знаешь, причина, по которой я дал тебе этот значок и по которой я привёл тебя с собой на эту встречу, она одна и та же."

    voice audio.goro_vsg3_line22
    g "Даже если я главнее тебя, я желаю вести Лагерь Друзей бок о бок, как и было прежде…"

    voice audio.goro_vsg3_line23
    g "Я понимаю, что твои намерения в правильном русле, и что идут они за пределы возможного, ради лагеря, прямо как и в тот день.  "

    voice audio.yoshi_vsg3_line15
    yo "Сэр Горо…"

    show cgg2 16 with Dissolve(0.25)
    voice audio.goro_vsg3_line24
    g "Что же, лучше будь внимательнее с этой встречей и поучись чему-то, а иначе я не возьму тебя в следующий раз!  "

    voice audio.yoshi_vsg3_line16
    yo "Есть, сэр! Сделаю всё возможное!"

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black with fade

    yo "{i}Сэр Горо делает всё возможное, чтобы открыться мне, вспоминая прошлое и непринужденно болтая.{/i}"
    yo "{i}Это правда облегчает - иметь возможность поговорить с ним на столь личном уровне, и не только о работе… {/i}"
    yo "{i}Я позабочусь о том, чтобы сэр Горо не ошибся, доверившись мне!{/i}"

    scene cg black
    hide screen location
    hide screen timeline
    hide screen quick_menu
    $quick_menu = False
    with fade
    $ renpy.pause (2.0, hard=True)

    $ location = location_clermont
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_clermontlobby_day with fade
    play music close_distance loop

    show goro_semiformal at left2
    show goro norm1 at left2
    show yoshi_semiformal at right2
    show yoshi shock3 at right2
    voice audio.yoshi_v_amazed1d
    yo "Вау… Значит, здесь работает мистер Клермонт…?"

    show goro play3 at left2
    voice audio.goro_v_heh1a
    g "Ага… Мило, не правда ли? Я тоде был удивлён, когда был тут впервые."

    show yoshi awkward4 at right2
    voice audio.yoshi_v_amazed2b
    yo "До сих пор не могу поверить, что кто-то вроде мистера Клермонта согласился на спонсорство Лагеря Друзей…"

    show goro comp2 at left2
    voice audio.goro_v_conj9a1
    g "За это нам стоит поблагодарить мистера Нагаме и его друзей… "
    g "Пускай мистер Клермонт и был поражён лагерем, я считаю, их рассказ был тем финальным убеждением, что заставило его поддержать нас."

    hide yoshi_semiformal
    hide yoshi awkward4
    show yoshi_semiformal at right2
    show yoshi norm3 at right2
    show goro shock1 at left2
    fd "Мистер Номору? Мистер Клермонт желает встретиться с вами сейчас!"

    show goro happy2 at left2
    voice audio.goro_v_rush1d1
    g "наша очередь. Пойдём!"

    hide yoshi_semiformal
    hide yoshi norm3
    show yoshi_semiformal at right2
    show yoshi shy2 at right2
    voice audio.yoshi_v_gulp1a
    yo "*глоть* Внезапно, я начинаю нервничать."

    hide goro_semiformal
    hide goro happy2
    show goro_semiformal at left2
    show goro bold2 at left2
    voice audio.goro_v_confident1a
    g "Всё будет хорошо, Йошинори. Просто наблюдай за мной."

    hide yoshi_semiformal
    hide yoshi shy2
    show yoshi_semiformal at right2
    show yoshi talk1 at right2
    voice audio.yoshi_v_right4
    yo "Л-ладно!"

    scene cg black
    hide screen location
    hide screen timeline
    hide screen quick_menu
    $quick_menu = False
    with fade
    $ renpy.pause (2.0, hard=True)

    $ location = location_clermont
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_clermontoffice_day with fade
    play music old_familiar_home loop

    show william_formal at left
    show william norm1 at left
    show goro_semiformal at center
    show goro happy1 at center
    show yoshi_semiformal at right
    show yoshi norm3 at right
    voice audio.goro_v_goodam2a2
    g "День добрый, мистер Клермонт."

    show william happy1 at left
    voice audio.william_v_surprised1b
    w "О! Давно не виделись, мистер Номору!"

    show goro happy2 at center
    voice audio.goro_v_request4a1
    g "Надеюсь, вы не против, что я привёл своего главного скаутмастера с собой сегодня – это Йошинори Нагира."
    g "Прошу прощения, что не проинформаировал заранее."

    show william comp4 at left
    voice audio.william_v_comp1b
    w "Никаких проблем! Я полагаю, мы уже встречались на моём визите в лагере, верно, мистер Нагира?"

    show yoshi happy2 at right
    voice audio.yoshi_v_yessir1
    yo "Да, сэр! Приятно видеть вас вновь, мистер Клермонт!"

    show william explain3 at left
    voice audio.william_v_request1
    w "И мы как раз вовремя, так перейдём же сразу к бизнесу, согласны?"

    show goro talk1 at center
    voice audio.goro_v_yessir1a1
    g "Да, сэр."

    show william happy2 at left
    voice audio.william_v_anyway1
    w "Итак, у меня есть для вас хорошие новости – как вы уже могли знать, та маленькая книжка /"лучшие Воспоминания/" которую мы опубликовали пробыла на полках и в онлайн магазинах уже больше месяца."
    w "Хотелось бы поздравить вас, так как это пока наш величайший релиз! Всё принесло гораздо больше продаж, чем мы ожидали!"

    show yoshi shock5 at right
    voice audio.yoshi_v_amazed1d
    yo "О-оу, вау… Это великолепно! "

    show william laugh2 at left
    voice audio.william_v_laugh1
    w "Похоже, публика оценила потенциал, что я увидел в вас и вашем лагере. Словно глоток чистого воздуха во всём рынке!"

    show william amazed3 at left
    voice audio.william_v_conj1a
    w "И, как говорится, /"куй железо пока горчячо/"; хорошая реклама, которую мы получаем от книги, -  отличная возможность углубиться в сам лагерь!"
    w "Поскольку наибольшая часть продаж направляется на улучшения в Лагере Друзей, мы сможем предложить полное спонсорство на долгие годы вперёд!"

    show goro comp5 at center
    voice audio.goro_v_thanks3a
    g "Благодрю вас ещё раз за то, что увидели потенциал в нашем лагере, мистер Клермонт. "

    show william happy2 at left
    voice audio.william_v_conj4
    w "Полагаю, здесь имеет дело быть и нечто другое, чем бизнес – дело ведь и в том, за что это место отвечает в современном поколении!"

    show goro happy1 at center
    voice audio.goro_v_glad1a
    g "Я рад, что мы на одной волне, сэр!"

    show william think2 at left
    voice audio.william_v_conj5
    w "Двигаемся дальше, обсудим планы улучшений."
    w "Полагаю, вы ведь знакомы с АНУС, Асоциацией Национально Установленных Скаутов?"

    show goro talk3 at center
    voice audio.goro_v_agree3a1
    g "Да, конечно, мы следуем их рекомендациям в большинстве наших лагерных мероприятий."

    show william talk1 at left
    voice audio.william_v_think1
    w "Я провел встречу с ассоциацией и попросил бизнес-консультацию о том, как улучшить лагерь."
    w "Полученные знания от профессионалов дали нам огромный объём потенциальных улучшений при том бюджете, который у нас есть."

    show william comp2 at left
    voice audio.william_v_agree1a
    w "Разумеется, с одобрения президента лагеря и по сигналу."

    show goro confused3 at center
    voice audio.goro_v_ah1b
    g "А… Могу ли я узнать, что именно за улучшения они посоветовали?"

    show william laugh1 at left
    voice audio.william_v_well1a
    w "Что же, мы бы могли просидеть тут весь день, обсуждая каждое из них."
    w "Но, как вводная часть, по большинству - всего лишь расширение лагеря! "

    show cg fade at truecenter
    show fx3 at fx_pos
    with dissolve

    voice audio.william_v_conj3a
    w "Мне сообщили, что пристройка рядом с лагерем предназначалась для улучшений. То была самая большая работа, которую они предложили."
    w "АНУС решила, что, раз мы ожидаем больше кэмперов в следующем сезоне, они бы хотели отсроить больше домиков и других объектов!"

    voice audio.goro_v_actually1a
    g "Мы это также предвидели. По факту, в качестве подготовки к следующему сезону мы уже начали ремонтировать старые, обветшалые домики."

    hide cg fade
    hide fx3
    with dissolve

    show william amazed2 at left
    voice audio.william_v_amazed2
    w "Отлично! Это послужит нам форой в самом большом объёме работы."
    w "Тем не менее, помимо этого есть и другие не менее важные предложения, такие как интеграция технологий, модернизация оборудования и новый курс, для обеспечения интересов безопасности."

    hide goro_semiformal
    hide goro confused3
    show goro_semiformal at center
    show goro shock2 at center
    voice audio.goro_v_oh2b
    g "О… Это даже за гранью того, что я ожидал…"

    show william happy2 at left
    voice audio.william_v_comp3
    w "Я отправлю вам электронным письмом все особенности по этой теме, так что вы сможете тщательно всё обдумать."

    hide goro_semiformal
    hide goro shock2
    show goro_semiformal at center
    show goro talk1 at center
    voice audio.goro_v_response1c2
    g "Понял. Я позабочусь о том, чтобы всё хорошенько изучить."
    g "Я ценю всю ту работу, что вы вкладываете в спонсорство нашего лагеря, мистер Клермонт. Я глубоко вам обязан."

    show yoshi comp2 at right
    voice audio.yoshi_v_thanks2
    yo "Да, мы даже не знаем как вас отблагодарить, мистер Клермонт!"

    show william comp4 at left
    voice audio.william_v_comp1a
    w "Как я и говорил ранее, я только счастлив быть частью вашего дела."

    show william talk1 at left
    voice audio.william_v_conj1a
    w "Итак, а теперь обсудим, к какому сроку проект должен быть завершён."
    w "Мы собираемся сохранить ту же цель по крайней мере за месяц до начала летнего сезона в следующем году."

    hide goro_semiformal
    hide goro talk1
    show goro_semiformal at center
    show goro think2 at center
    voice audio.goro_v_think1a1
    g "Хотелось бы выразить обеспокоенность по этому поводу, сэр."
    g "Что касается только ремонтных работ, не думаю, что наш нынешний персонал будет способен выполнить строительные работы через несколько месяцев."

    show william laugh1 at left
    voice audio.william_v_laugh3
    w "Кха-ха-ха-ха! Что вы, я бы не поставил вас в такую безвыходную ситуацию, мистер Номору!"
    w "Неразумно было бы просить вашу команду из четырех человек справиться со всем этим. "

    hide goro_semiformal
    hide goro think5
    show goro_semiformal at center
    show goro talk2 at center
    voice audio.goro_v_conj7a
    g "На этом прошу позволить выделить мне некоторое время, дабы нанять необходимую рабочую силу для выполнения работы."

    show william happy3 at left
    voice audio.william_v_comp3
    w "Я уже всё устроил – я заключил контракт с подрядчиком, который предоставит нам команду профессионалов с наилучшим опытом для выполнения этой работы."

    hide goro_semiformal
    hide goro talk2
    show goro_semiformal at center
    show goro shock2 at center
    voice audio.goro_v_unsure1a1
    g "О… Не много ли это, сэр? Я имею ввиду… Вы и так проспонсировали целое расширение."

    show william comp4 at left
    voice audio.william_v_impressed1a
    w "Считайте это частью нашего спонсорства. Всё, что от вас будет требоваться как от президента лагеря - это дать мне разрешение на предложенные нами планы модернизации."
    w "Это, и поручить одному из ваших сотрудников координировать действия с любыми представителями, которых я пошлю на место от моего имени. Итак, удобно ли это нам обоим?"

    hide goro_semiformal
    hide goro shock2
    show goro_semiformal at center
    show goro amazed2 at center
    voice audio.goro_v_thanks2a1
    g "Весьма, сэр. Премного благодарен за вашу щедрость."
    g "Могу я спросить, когда у нас официальная дата начала проекта?"

    show william talk2 at left
    voice audio.william_v_rush1a
    w "Я бы сказал, чем быстрее - тем лучше, поскольку поджимают сроки.  "
    w "На самом деле, я могу отправить команду уже завтра, чтобы дать им достаточно времени освоиться и ознакомиться с участком, если вы не против."

    hide yoshi_semiformal
    hide yoshi comp2
    show yoshi_semiformal at right
    show yoshi awkward4 at right
    voice audio.yoshi_v_what3
    yo "Ч-что…? Уже завтра?"

    show goro happy1 at center
    voice audio.goro_v_agree7a
    g "Согласен с вами, мистер Клермонт. Я подготовлю персонал к их прибытию. Мы выделим несколько свободных домиков для временного жилья на протяжение всего строительства."

    show william explain2 at left
    voice audio.william_v_think1
    w "Установим ежедневное расписание и отправим команды по их специальности до тех пор, пока в лагере не будет полностью мобилизована вся необходимая рабочая сила."
    w "Понимаю, это может быть ошеломляюще, но, предполагаю, работать с большим количеством людей над единой целью вам не в новинку."

    show goro bold2 at center
    voice audio.goro_v_agree6a2
    g "Всё верно. Уверен, что мы справимся."

    show william talk3 at left
    voice audio.william_v_conj7
    w "И последнее, нам нужно закрыть юридическую сторону проекта. Раз уж мы собираемся заселять всех завтра и незамедлительно начать, нам потребуются документации и разрешения."

    show goro talk1 at center
    voice audio.goro_v_conj6a1
    g "Насчёт этого, я уже работал с местной мэрией ещё с конца предыдущего сезона. Хорошие новости: всю необходимую документацию я уже оформил."
    g "Я внесу важные коррективы на основе обновленной области, что мы сегодня обсудили, завтра же отправлюсь туда, чтобы получить все разрешения."

    show william happy3 at left
    voice audio.william_v_impressed2b
    w "Великолепно! Вы действительно подготовились ко всему, мистер Номору."

    show goro comp2 at center
    voice audio.goro_v_response2a2
    g "Честно, это меньше что я могу сделать, сэр. "
    g "Можете расчитывать на наш персонал в выполнении своей части всего проекта. "

    show william laugh1 at left
    voice audio.william_v_laugh2
    w "Ха-ха-ха, превосходно. Итак, полагаю, на сегодня мы решили все вопросы?"

    show goro happy1 at center
    voice audio.goro_v_response1a2
    g "В самом деле. Не будем дальше занимать ваше время."

    show william happy1 at left
    voice audio.william_v_bye1b
    w "Тогда хорошо, собрание окончено! Увидемся на следующей неделе на новой встрече."

    show goro laugh3 at center
    voice audio.goro_v_thanks2a1
    g "Да, сэр. Благодарю."

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

    $ location = location_clermont
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_clermontlobby_day with fade
    play music close_distance loop

    show yoshi_semiformal at left2
    show yoshi sigh1 at left2
    show goro_semiformal at right2
    show goro norm1 at right2
    voice audio.yoshi_v_relief1
    yo "Фух…"

    show goro play3 at right2
    voice audio.goro_v_so3a
    g "Ну…? Как тебе твоя первая деловая встреча?"

    $working = False
    $shuffle_menu()
    menu():
        g "Ну…? Как тебе твоя первая деловая встреча?{fast}"
        "Было немного напряжённо.":
            $working = True
            $score_goro -= 1
            show yoshi worry2 at left2
            voice audio.yoshi_v_conj4a
            yo "Честно говоря, она меня немного напрягла. "

            show yoshi sigh1 at left2
            voice audio.yoshi_v_sigh2
            yo "Беседа так стремительно развивалась, что я понятия не имел когда мне вставить слово, или когда мне обдумать полученную информацию! "
            yo "В какой-то момент я почувствовал себя плохо из-за того, я так ничего и не внёс в обсуждение."

            show goro comp2 at right2
            voice audio.goro_v_comp2a2
            g "Не волуйся, я и не ожидал, что ты начнёшь активно участвовать. Я понимаю, всё это было вне зоны твоего комфорта."

            show goro explain3 at right2
            voice audio.goro_v_conj5a
            g "И тем не мнее, испытать такое - полезный опыт."
            g "Такой занятой человек, как мистер Клермонт может позволить нам лишь малую часть своего времени, потому так важно сразу переходить к делу и достичь наилучшего результата за каждую встречу."

            hide yoshi_semiformal
            hide yoshi sigh1
            show yoshi_semiformal at left2
            show yoshi talk1 at left2
            voice audio.yoshi_v_response1a
            yo "Я понимаю, сэр."
        "Сильно отличается, от тех, что в лагере.":
            $working = True
            $score_goro -= 1
            show yoshi worry2 at left2
            voice audio.yoshi_v_conj4a
            yo "Было очень… стрессово… Она сильно отличается от тех собраний, что мы обычно устраиваем в лагере."

            show yoshi sigh1 at left2
            voice audio.yoshi_v_sigh2
            yo "Беседа так стремительно развивалась, что я понятия не имел когда мне вставить слово, или когда мне обдумать полученную информацию! "
            yo "В какой-то момент я почувствовал себя плохо из-за того, я так ничего и не внёс в обсуждение."

            show goro comp2 at right2
            voice audio.goro_v_comp2a2
            g "Не волуйся, я и не ожидал, что ты начнёшь активно участвовать. Я понимаю, всё это было вне зоны твоего комфорта."

            show goro explain3 at right2
            voice audio.goro_v_conj5a
            g "И тем не мнее, испытать такое - полезный опыт."
            g "Такой занятой человек, как мистер Клермонт может позволить нам лишь малую часть своего времени, потому так важно сразу переходить к делу и достичь наилучшего результата за каждую встречу."

            hide yoshi_semiformal
            hide yoshi sigh1
            show yoshi_semiformal at left2
            show yoshi talk1 at left2
            voice audio.yoshi_v_response1a
            yo "Я понимаю, сэр."
        "Хорошо, что вы были там.":
            $working = True
            $score_goro += 1
            hide yoshi_semiformal
            hide yoshi sigh1
            show yoshi_semiformal at left2
            show yoshi comp2 at left2
            voice audio.yoshi_v_amazed3
            yo "Хорошо, что вы были там, сэр."
            yo "Мистер Клермонт приводил много чего, что требовало незамедлительных решений, и у вас получилось принять каждое из них."

            show yoshi sigh1 at left2
            voice audio.yoshi_v_sigh2
            yo "Я едва успевал на темпом дискуссии. Хотелось бы мне внести такой же вклад, как вы!"

            show goro comp2 at right2
            voice audio.goro_v_comp2a2
            g "Знания приходят с опытом. Такой занятой человек, как мистер Клермонт может позволить нам лишь малую часть своего времени, и нам следует уважать это. "
            g "Важно сразу переходить к делу и достичь наилучшего результата за каждую встречу."

            show goro comp5 at right2
            voice audio.goro_v_conj9a1
            g "Но, если честно, такие собрания не сильно отличаются от тех, что мы проводим в лагере."

            show yoshi happy1 at left2
            voice audio.yoshi_v_response1b
            yo "Я понимаю, сэр."
        "У вас всё было под контролем.":
            $working = True
            $score_goro += 2
            hide yoshi_semiformal
            hide yoshi sigh1
            show yoshi_semiformal at left2
            show yoshi bold2 at left2
            voice audio.yoshi_v_amazed3
            yo "У был поражён тем, как хорошо вы со всем управлялись, сэр!"
            yo "Даже когда беседа развивалась стремительно, вам удавалось поспевать за каждым вопросом приведённым мистером Клермонтом."

            show yoshi sigh1 at left2
            voice audio.yoshi_v_sigh2
            yo "У вас даже получилось незамедлительно решить каждый из них… Не уверен, что смог бы так сделать!"

            show goro comp2 at right2
            voice audio.goro_v_comp2a2
            g "Знания приходят с опытом. Такой занятой человек, как мистер Клермонт может позволить нам лишь малую часть своего времени, и нам следует уважать это. "
            g "Важно сразу переходить к делу и достичь наилучшего результата за каждую встречу."

            show goro comp5 at right2
            voice audio.goro_v_conj9a1
            g "Но, если честно, такие собрания не сильно отличаются от тех, что мы проводим в лагере

            show yoshi happy1 at left2
            voice audio.yoshi_v_response1b
            yo "Я понимаю, сэр."

    hide goro_semiformal
    hide goro play3
    show goro_semiformal at right2
    show goro tease5 at right2
    voice audio.goro_v_heh1a
    g "Хех, выдел бы ты своё лицо на протяжение всего собрания, Йошинори. Как у ребёнка, потерявшегося в супермаркете."

    show yoshi panic4 at left2
    voice audio.yoshi_v_shock4
    yo "Г-гах…! Было настолько плохо? Надеюсь, мистер Клермонт не заметил."

    hide goro_semiformal
    hide goro tease5
    show goro_semiformal at right2
    show goro laugh5 at right2
    voice audio.goro_v_laugh2b1
    g "Не похоже, что твой талисман принёс хоть каплю удачи. Ха-ха-ха!"

    hide yoshi_semiformal
    hide yoshi panic4
    show yoshi_semiformal at left2
    show yoshi sigh3 at left2
    voice audio.yoshi_v_sigh3a
    yo "*вздох* На понимаю, как вам это удаётся, сэр."

    show goro happy1 at right2
    voice audio.goro_v_comp4a
    g "Если повторяешь что-то раз за разом, однажды осознаешь, что всё не так сложно, как ты думал раньше."

    hide goro_semiformal
    hide goro happy1
    show goro_semiformal at right2
    show goro happy2 at right2
    voice audio.goro_v_conj3a1
    g "Хотя, стоит признать, мне понравилось быть в компании с тобой."
    g "В каком-то смысле, я почувствовал себя уверенней вместе с тобой."

    show goro tease2 at right2
    voice audio.goro_v_heh1a
    g "А ещё, наблюдать, как ты потеешь от нервов, было довольно забавно. "

    show yoshi shy6 at left2
    voice audio.yoshi_v_unsure1b
    yo "Теперь я даже не знаю, присоединяться ли мне в следующий раз…"

    hide goro_semiformal
    hide goro tease2
    show goro_semiformal at right2
    show goro laugh1 at right2
    voice audio.goro_v_laugh2b1
    g "Ха-ха-ха!"

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black with fade

    yo "{i}Во время поездки обратно сэр Горо всё продолжал дразнить меня и болтать… Но в самом деле, было даже весело видеть его таким расслабленным.{/i}"
    yo "{i}Время пролетело быстро, не успел я оглянуться, как мы уже были в Лагере Друзей.{/i}"
    yo "{i}Сэр Горо немедленно организовал встречу со всеми скаутмастерами, дабы подготовиться к завтрашнему прибытию рабочих.{/i}"

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
    play music ready_for_tomorrow loop

    show goro_semiformal at p4_1
    show goro talk1 at p4_1
    show yoshi_semiformal at p4_2
    show yoshi norm1 at p4_2
    show aiden_autumn at p4_3
    show aiden norm1 at p4_3
    show yuri_autumn at p4_4
    show yuri norm1 at p4_4
    voice audio.goro_v_so1a
    g "На этом всё. Я рассказал вам все детали о ремонте, выданные мне мистером Клермонтом, так чтобы всем всё было понятно."

    show aiden shock5 at p4_3
    voice audio.aiden_v_shock1b1
    a "Ого, а дело и правда не плёвое, Дедуль… Судя по всему, стоить это будет целое состояние!"

    show yuri explain2 at p4_4
    voice audio.yuri_v_well1a
    yu "Что ж, папа говорил, что вся реконструкция будет оплачена средствами из спонсорства."

    show yoshi talk1 at p4_2
    voice audio.yoshi_v_right5
    yo "Всё верно.  Единственное, что осталось решить - разные инструменты. Но этот вопрос может быть решён с помощью прошедшего сбора средств."

    show goro talk3 at p4_1
    voice audio.goro_v_anyway2
    g "Итак, всем понятны ваши обязанности?"

    show yuri happy1 at p4_4
    voice audio.yuri_v_agree1b1
    yu "Да! Я скоорденируюсь с подрядчиками завтрашним днём и проведу для них экскурсию по лагерю, предоставив жильё!"

    show aiden laugh1 at p4_3
    voice audio.aiden_v_agree1a1
    a "Угу, а я прослежу за тем, чтобы рабочие были сыты и поддерживали регулярное техническое обслуживание."

    show goro explain2 at p4_1
    voice audio.goro_v_yoshi2a
    g "А насчёт тебя, Йошинори. Я поставлю тебя во главе наблюдения за запланированным расписанием на эту неделю, тем временем я возьмусь за оставшуюся документацию."

    show yoshi happy1 at p4_2
    voice audio.yoshi_v_yessir2
    yo "Есть, сэр! Можете расчитывать на меня!"

    show goro happy1 at p4_1
    voice audio.goro_v_amazed2a1
    g "Отлично! Если всё понятно, собрание окончено."

    hide yuri_autumn
    hide yuri happy1
    show yuri2_autumn at p4_4
    show yuri2 excited3 at p4_4
    voice audio.yuri_v_kyaa1a
    yu "Кья-а-а~ Я так взволнована! Если всё продёт как по маслу, Лагерь Друзей будет на пике своег осовершенства! "
    yu "Представьте, сколько мероприятий я смогу устроить с таким большим бюджетом, хи-хи-хи…"

    show aiden tease1 at p4_3
    voice audio.aiden_v_laugh1a1
    a "Хе-хе, зная тебя, ты бы устроила очередную костюмированную вечеринку."

    hide yuri2_autumn
    hide yuri2 excited3
    show yuri_autumn at p4_4
    show yuri excited2 at p4_4
    voice audio.yuri_v_laugh2a4
    yu "То была лучшая из моих идей прошлым летом! Но у меня есть идеи и попривлекательнее, которыми все смогут /"насладиться/"~! Хи-хи-хи…"

    hide yoshi_semiformal
    hide yoshi happy1
    show yoshi_semiformal at p4_2
    show yoshi sigh4 at p4_2
    voice audio.yoshi_v_sigh3a
    yo "*вздох* Юри, ты же помнишь, что бюджет для улучшений…"

    hide goro_semiformal
    hide goro happy1
    show goro_semiformal at p4_1
    show goro disappoint2 at p4_1
    voice audio.goro_v_ehem1a
    g "*кхем* Йошинори прав. Давайте не будем перегибать палку, а придерживаться наших планов. "

    show yuri pout4 at p4_4
    voice audio.yuri_v_idea2a
    yu "Знаю-знаю я! А теперь, может вам уже пора снять ваши официальные прикиды и отдохнуть оставшуюся ночь? "

    show aiden play3 at p4_3
    voice audio.aiden_v_wait2b1
    a "Попридержи коней, они в них так стильно и элегантно в них выглядят! Может, сначала отпразнуем? "
    a "В духовке как раз сидит огромный жаренный цыплёнок, уверен, хорошо зайдёт с шампанским!"

    show aiden bold2 at p4_3
    voice audio.aiden_v_rush1a1
    a "У нас может не быть такой возможности в будущем, когда мы будем заняты! "

    show yuri angry2 at p4_4
    voice audio.yuri_v_what5a
    yu "Чего?! Снова выпивать собрались?! Ни за что! Особенно когда мы ждём новых людей завтрашним днём! "
    yu "Последнее, чего я хочу, это чтобы вы шаткими и пьяными угробили первое впечатление!"

    show goro sigh1 at p4_1
    voice audio.goro_v_sigh1a
    g "*взлох* Пускай мне и нравится идея выпить сегодня, чтобы отдахнуть… Юри права. "

    show yuri annoy2 at p4_4
    voice audio.yuri_v_alright1d1
    yu "Отпразнуем одним цыплёнком, пока что без алкоголя, идёт?!"

    show aiden wink1 at p4_3
    voice audio.aiden_v_alright2a
    a "Идёт-идёт. Никакого алкоголя на сегодня! Да, Йоши, Дедуль? *подмигивает*"

    show yuri pout1 at p4_4
    voice audio.yuri_v_hey3a
    yu "Эй, я всё видела!!"

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

    $ location = location_messhall
    $ time = timeline_timenight
    show screen location
    show screen timeline
    show screen quick_menu
    $quick_menu = True
    scene bg_messhall_autumn_night with fade
    play music sunset_stroll loop

    show taiga_autumn at p6_1
    show taiga normal3 at p6_1
    show yoichi_autumn at p6_2
    show yoichi angry6 at p6_2
    show yuri_autumn at p6_3
    show yuri norm1 at p6_3
    show aiden_autumn at p6_4
    show aiden norm1 at p6_4
    show yoshi_semiformal at p6_5
    show yoshi norm1 at p6_5
    show goro_semiformal at p6_6
    show goro norm1 at p6_6
    voice audio.yoichi_v_groan2c4
    yi "АГХ! НУ НАКОНЕЦ-ТО, старичьё здесь! Мы вас уже весь день ждём!"

    show taiga annoyed4 at p6_1
    voice audio.taiga_v_yoichi8
    t "Йоичи, прошло от силы десять минут. "

    show yoichi angry3 at p6_2
    voice audio.yoichi_v_shock3a7
    yi "Гах! Да плевать! Время идёт медленней, когда я голодный!"

    show yoshi comp2 at p6_5
    voice audio.yoshi_v_sorry5a
    yo "Просим прощение за задержку! У нас было собрание! "

    hide yoichi_autumn
    hide yoichi angry3
    show yoichi_autumn at p6_2
    show yoichi annoyed6 at p6_2
    voice audio.yoichi_v_angry1d
    yi "Тц. Всегда ведёте себя так занято, с тех пор как в лагере пусто.  "
    yi "Готов поспорить, что вы опять забыли про нас! Я ни одного из вас не видел со вчерашнего дня!"

    show taiga sigh2 at p6_1
    voice audio.taiga_v_ugh1
    t "Угх… Он всегда такой, когда время его кормёжки… Я говорил ему, что он может согреть в микроволновке что-нибудь из холодильника."

    hide yoichi_autumn
    hide yoichi annoyed6
    show yoichi_autumn at p6_2
    show yoichi annoyed4 at p6_2
    voice audio.yoichi_v_disagree1a5
    yi "Не хочу я снова есть объедки! К тому же, я чую, что они прячут что-то вкусное здесь! Этот нос не обманешь!"

    show yuri laugh1 at p6_3
    voice audio.yuri_v_yoichi7a
    yu "Что же, сегодня твой счастливый день, Йоичи~! эйден приготовил кое что особенное сегодня на ужин!"

    show aiden laugh1 at p6_4
    voice audio.aiden_v_laugh2a1
    a "Ха-ха! Я лучше пойду подготовлю кк подаче, пржде чем Йоичи с ума сойдёт! Скоро буду!"

    hide aiden_autumn
    hide aiden laugh1
    with dissolve

    show taiga_autumn at p5_1
    show taiga sigh2 at p5_1
    show yoichi_autumn at p5_2
    show yoichi annoyed4 at p5_2
    show yuri_autumn at p5_3
    show yuri laugh1 at p5_3
    show yoshi_semiformal at p5_4
    show yoshi comp2 at p5_4
    show goro_semiformal at p5_5
    show goro norm1 at p5_5
    with move

    show taiga_autumn at p5_1
    show taiga confused1 at p5_1
    voice audio.taiga_v_confused2a
    t "Ита-а-ак… Что за костюмы? Давно я не видел вас в чём-то столь формальном."

    show yoshi talk3 at p5_4
    voice audio.yoshi_v_ah1
    yo "А, у нас сегодня была встреча с мистером Клермонтом."

    show yoichi confused3 at p5_2
    voice audio.yoichi_v_confused1a4
    yi "И вы разоделись как два сутенёра ради какой-то скучной встречи?"

    show goro sigh3 at p5_5
    voice audio.goro_v_sigh1a
    g "*вздох* Подумать только, сильно потратился, лишь бы выглядеть вот так…"

    show yoichi talking2 at p5_2
    voice audio.yoichi_v_laugh1a5
    yi "Ну, знаешь ли, сутенёры тоже много зарабатывают."

    show yoshi angry2 at p5_4
    voice audio.yoshi_v_yoichi7
    yo "Йоичи! Никто из нас, особенно сэр Горо, никогда бы таким не занимались!"

    show yoichi talking4 at p5_2
    voice audio.yoichi_v_hmph1a
    yi "Ага, пресмыкайся и дальше, симп. "

    show yoshi sigh4 at p5_4
    voice audio.yoshi_v_sigh3a
    yo "*вздох*"

    show taiga confused3 at p5_1
    voice audio.taiga2_v_thinking2a
    t "А о чём была встреча? Должно быть что-то важное, раз вы так одеты."

    show yoshi happy1 at p5_4
    voice audio.yoshi_v_actually3a
    yo "Вообще, это и правда было важно… Благодаря тому, что книга Кейтаро имела большой успех на рынке, мистер Клермонт предложил нам ещё больший бюджет для улучшения лагеря."

    show goro talk2 at p5_5
    voice audio.goro_v_request2a2
    g "Со вступлением в силу спонсорства с этого момента всё будет очень напряжённо, и я ожидаю от вас, что вы сделаете всё возможное, чтобы помочь нам."

    show taiga excited1 at p5_1
    voice audio.taiga2_v_excited2a
    t "Не знаю насчёт Йоичи, но я уже давно ждал, над чем бы поработать! Время здесь и правда длится меленнее в межсезонье."

    show yoichi_autumn at p5_2
    show yoichi talking2 at p5_2
    voice audio.yoichi_v_greet1b1
    yi "Эй, а это куда лучше, чем помирать здесь со скуки. Этим мускулам бы тоже поработать не помешало."

    show yoshi bold2 at p5_4
    voice audio.yoshi_v_encourage3
    yo "Отличный настрой! Надеюсь, что вы сохраните этот позитивный настрой до завтра, когда прибудут новые работники и начнут работу!"

    show yoichi_autumn at p5_2
    show yoichi annoyed4 at p5_2
    voice audio.yoichi_v_groan2a1
    yi "Ага, круть… Новые лица. "

    hide yoshi_semiformal
    hide yoshi bold2
    show yoshi_semiformal at p5_4
    show yoshi comp3 at p5_4
    voice audio.yoshi_v_please1a
    yo "Пожалуйста, хотя бы попытайся подружиться с ними, Йоичи."

    show yoichi_autumn at p5_2
    show yoichi annoyed1 at p5_2
    voice audio.yoichi_v_well1b
    yi "Ну, может, новые лица тут - это и не плохо. Я всё равно уже стал видеть лицо и выслушивать нытьё Динамита день напролёт. "

    show taiga angry5 at p5_1
    voice audio.taiga_v_disagree1
    t "Кто бы говорил! Быть тут заточённым с тобой крайне утомительно – я уже скучаю по компании Ли и Эдуарда."

    show yoichi annoyed5 at p5_2
    voice audio.yoichi_v_angry1d
    yi "То же самое! Я бы лучше тусил с мистером Совершенством или Неженкой, или даже с тем раздражающим Факелоголовым!"

    show yuri comp2 at p5_3
    voice audio.yuri_v_aww2a
    yu "О-о~ Только посмотрите, так скучаете по друзьям! Это так мило! А вы с ними хотя бы общаетесь?"

    show taiga compassion5 at p5_1
    voice audio.taiga2_v_agree3a
    t "Да, общаемся! Пускай все заняты своими делами, мы всё равно находим время пообщаться.  "

    show yoichi playful1 at p5_2
    voice audio.yoichi_v_agree1a1
    yi "Ага, те групповые звонки были вполне весёлыми. Это лучше, чем слушать голос Динамита на постоянной основе."

    show taiga_autumn at p5_1
    show taiga angry6 at p5_1
    voice audio.taiga_v_ugh1
    t "Угх…"

    show yuri tease2 at p5_3
    voice audio.yuri_v_well1a
    yu "О, ну разве вы не чудно ладите~"

    show taiga_autumn at p6_1
    show taiga angry6 at p6_1
    show yoichi_autumn at p6_2
    show yoichi playful1 at p6_2
    show yuri_autumn at p6_3
    show yuri tease2 at p6_3
    show yoshi_semiformal at p6_4
    show yoshi comp3 at p6_4
    show goro_semiformal at p6_5
    show goro talk2 at p6_5
    with move

    show aiden_autumn at p6_6
    show aiden comp5 at p6_6
    with dissolve
    voice audio.aiden_v_sorry1a1
    a "Простите, что так долго! Пришлось сделать немного немного картофельного пюре! "

    show taiga_autumn at p6_1
    show taiga angry6 at p6_1
    show yuri_autumn at p6_2
    show yuri tease2 at p6_2
    show yoshi_semiformal at p6_3
    show yoshi comp3 at p6_3
    show goro_semiformal at p6_4
    show goro talk2 at p6_4
    show yoichi_autumn at p6_5
    show yoichi playful1 at p6_5
    with move

    voice audio.yoichi_v_groan2c2
    yi "УГХ, ОТЛИЧНО!!! Я голоден как волк!! "

    show yuri_autumn at p6_1
    show yuri tease2 at p6_1
    show yoshi_semiformal at p6_2
    show yoshi comp3 at p6_2
    show goro_semiformal at p6_3
    show goro talk2 at p6_3
    show taiga_autumn at p6_4
    show taiga angry6 at p6_4
    with move

    show taiga_autumn at p6_4
    show taiga angry2 at p6_4
    voice audio.taiga2_v_hey1h
    t "Э-эй! Хватит всё загребать! Оставь хоть бёдрышко мне! "

    show yoichi playful3 at p6_5
    voice audio.yoichi_v_bye2b
    yi "Кто успел, тот и съел! "

    show aiden comp3 at p6_6
    voice audio.aiden_v_conj4a
    a "Ну-ну, тут всем хватит! "

    show yuri excited2 at p6_1
    voice audio.yuri_v_bye3a
    yu "Я пойду поставлю стол!"

    hide yuri_autumn
    hide yuri excited2
    with dissolve

    show yoshi_semiformal at p6_1
    show yoshi comp3 at p6_1
    show goro_semiformal at p6_2
    show goro talk2 at p6_2
    with move

    hide yoshi_semiformal
    hide yoshi comp3
    show yoshi_semiformal at p6_1
    show yoshi comp1 at p6_1
    yo "..."

    hide goro_semiformal
    hide goro talk2
    show goro_semiformal at p6_2
    show goro play3 at p6_2
    voice audio.goro_v_laugh1a1
    g "Хе-хе… Говорил же, ты и так уже хорошо справлешься. Посмотри как сильно выросли эти двое."

    show yoshi comp2 at p6_1
    voice audio.yoshi_v_right9
    yo "Вы правы, сэр… Не смог бы гордиться меньше."

    hide goro_semiformal
    hide goro play3
    show goro_semiformal at p6_2
    show goro bold2 at p6_2
    voice audio.goro_v_rush2a1
    g "Почему бы нам не присоединиться? У нас был долгий день, думаю, мы заслужили хороший ужин."

    show yoshi happy1 at p6_1
    voice audio.yoshi_v_right2
    yo "К-конечно! "

    $ renpy.music.stop(channel='music', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound', fadeout = 1.0)
    $ renpy.music.stop(channel='bgsound2', fadeout = 1.0)
    scene cg black with fade
    yo "{i}После тяжёлого дня со всем лагерным бизнесом с сэром Горо, мы позаботились о том, чтобы приятно провести время вместе, вшестером. {/i}"
    yo "{i}Зная, какие большие перемены ждут нас завтра, я благодарен за те простые моменты, как этот, что я могу провести со всеми.{/i}"

    $persistent.profile_unlock.append("taiga")
    $persistent.profile_unlock.append("yoichi")
    $persistent.profile_unlock.append("william")
    scene cg black
    hide screen location
    hide screen timeline
    hide screen quick_menu
    $quick_menu = False
    with fade
    play sound sleeping_time
    $ time_transition_night_to_day_fall()
    $ renpy.pause (2.0, hard=True)
    jump day3
