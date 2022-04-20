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
    yo "{i}(Эх, снова наступил этот период?){/i}"

    voice audio.yoshi_vs1_line2
    yo "{i}(Летняя смена в Лагере Друзей завершилась и началась осень...){/i}"

    voice audio.yoshi_vs1_line3
    yo "{i}(Не самое мое любимое время года, но и оно когда-то должно было наступить… Видя лагерь таким тихим и пустым, начинаешь ощущать себя одиноким...){/i}"

    voice audio.yoshi_vs1_line4
    yo "{i}(Во всем лагере нет ни одного скаута... А значит и  мероприятий никаких организовывать не нужно...){/i}"

    voice audio.yoshi_vs1_line5
    yo "{i}(Но… на этот раз все совсем не так, как было в прошлые годы.){/i}"

    show cg2 newbeginning2 with Dissolve(0.25)
    voice audio.yoshi_vs1_line6
    yo "{i}(Теперь, когда лагерь стал успешеым и популярным, следующая смена будет куда более насыщенной чем все предыдущие!){/i}"

    voice audio.yoshi_vs1_line7
    yo "{i}(Это именно то чего я так долго ждал! Как же я счастлив, что Лагерь Друзей снова на пике популярности!){/i}"

    voice audio.yuri_vs1_line1
    yu "Эй!"

    show cg2 newbeginning3 with Dissolve(0.25)
    voice audio.yoshi_vs1_line8
    yo "Чт-Что?!"

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
    yu "Не могу поверить, что ты пропустил мимо ушей все, что я говорила, Йоши."

    hide yoshi_autumn
    hide yoshi shock1
    show yoshi2_autumn at left2
    show yoshi2 awkward3 at left2
    voice audio.yoshi_vs1_line9
    yo "П-прости! Я просто задумался!"

    show yuri confused2 at right2
    voice audio.yuri_vs1_line3
    yu "Боже, ты все еще продолжаешь разговаривать сам с собой? Я думала, что с этой привычкой покончено!"

    voice audio.yuri_vs1_line4
    yu "Некоторые вещи никогда не изменятся, так ведь? Ты все такой же сентиментальный, ну прямо как пенсионер"

    hide yoshi2_autumn
    hide yoshi2 awkward3
    show yoshi_autumn at left2
    show yoshi annoy5 at left2
    voice audio.yoshi_vs1_line10
    yo "Нуу… Я не настолько старый… И вообще, между нами всего год разницы!"

    show yuri tease2 at right2
    voice audio.yuri_vs1_line5
    yu "Хи-хи, говоря так, ты напоминаешь мне моего отца."

    hide yoshi_autumn
    hide yoshi annoy5
    show yoshi2_autumn at left2
    show yoshi2 sigh1 at left2
    voice audio.yoshi_vs1_line11
    yo "*вздох* сэр Горо тоже еще не старик..."

    show yuri explain2 at right2
    voice audio.yuri_vs1_line6
    yu "В любом случае, раз ты меня не слушал, я повторю вопрос: Когда ты закончишь тут убираться?"

    voice audio.yuri_vs1_line7
    yu "Становится прохладно и мне нужны дрова для нашего офиса."

    hide yoshi2_autumn
    hide yoshi2 sigh1
    show yoshi_autumn at left2
    show yoshi talk3 at left2
    voice audio.yoshi_vs1_line12
    yo "О! я как раз только что закончил, так что могу заняться их заготовкой прямо сейчас!"

    voice audio.yoshi_vs1_line13
    yo "Давай я найду Эйдена, думаю вдвоем мы справимся быстрее!"

    show yuri confused4 at right2
    voice audio.yuri_vs1_line8
    yu "Сомневаюсь, что Эйден сможет помочь тебе в ближайшее время. Просто я видела, как он был занят другими делами, и не стала просить его."

    voice audio.yuri_vs1_line9
    yu "Если хочешь, я могу помочь тебе вместо него. Я ведь тоже умею размахивать топром~"

    show yoshi laugh1 at left2
    voice audio.yoshi_vs1_line14
    yo "Ха-Ха, не беспокойся Юри, я справлюсь!"

    voice audio.yoshi_vs1_line15
    yo "Кроме того, разве у вас с сэром Горо нет других дел?"

    show yuri sigh4 at right2
    voice audio.yuri_vs1_line10
    yu "*вздох* Не напоминай… Я не понимаю, как папа может работать в своем кабинете целыми днями напролет - так он сведет меня с ума!"

    voice audio.yuri_vs1_line11
    yu "И если быть честной, то идея прийти к тебе с просьбой - это всего лишь повод чтобы прогуляться и подышать свежим воздухом."

    show yoshi comp3 at left2
    voice audio.yoshi_vs1_line16
    yo "Юри, тут ничего не поделаешь. После последней смены сэру Горо пришлось разгребать кучу документов."

    voice audio.yoshi_vs1_line17
    yo "Предстоит многое сделать, что бы лагерь нормально функционировал без скаутов и при малом количестве обслуживающего персонала."

    show yuri talk2 at right2
    voice audio.yuri_vs1_line12
    yu "Ты об этом только что грезил?"

    show yoshi think2 at left2
    voice audio.yoshi_vs1_line18
    yo "Да, я как раз размышлял о том как сильно изменился Лагерь Друзей в последнее годы…"

    show yuri comp2 at right2
    voice audio.yuri_vs1_line13
    yu "Похоже на американские горки, правда...?"

    show yoshi comp3 at left2
    voice audio.yoshi_vs1_line19
    yo "Да… В этот раз у меня была возможность полноценно пообщаться скаутами… Похоже, это лучшая смена, которая у меня когда либо была."

    voice audio.yoshi_vs1_line20
    yo "И этот факт заставляет меня задуматься сколько из них вернется в следующем году."

    show yuri comp4 at right2
    voice audio.yuri_vs1_line14
    yu "Оу, ты действительно так скучаешь по ним?"

    voice audio.yuri_vs1_line15
    yu "Уверена многие из них вернутся. А если и нет, то ничего страшного."

    hide yoshi_autumn
    hide yoshi comp3
    show yoshi2_autumn at left2
    show yoshi2 sad4 at left2
    voice audio.yoshi_vs1_line21
    yo "Да, но если быть честным… Я сильно расстроюсь, если не увижу некторых из них снова."

    show yuri play2 at right2
    voice audio.yuri_vs1_line16
    yu "Послушай, тебе надо расслабиться. Я думала, что теперь, когда у нас все хорошо, ты будешь меньше переживать."

    voice audio.yuri_vs1_line17
    yu "До следующей смены еще несколько месяцев и всякое может случится за это время в их жизни."

    show yuri happy1 at right2
    voice audio.yuri_vs1_line18
    yu "Ты выполнил свою задачу прошлым летом, и теперь вернуться они или нет зависит только от самих скаутов."

    voice audio.yuri_vs1_line19
    yu "Но одно можно сказать абсолютно точно. У нас всех остались самые яркие воспоминания о прошлой смене, проведенной здесь в Лагере Друзей… "

    show yuri comp4 at right2
    voice audio.yuri_vs1_line20
    yu "И они навсегда останутся в наших сердцах!"

    hide yoshi2_autumn
    hide yoshi2 sad4
    show yoshi_autumn at left2
    show yoshi comp6 at left2
    voice audio.yoshi_vs1_line22
    yo "Ахаха… ну и кто тут сентиментальный?"

    show yuri_autumn at left2
    show yuri pout1 at left2
    with move

    show yuri_autumn at right2
    show yuri pout1 at right2
    with move

    yu "*дергает Йоши за ухо*"

    show yoshi pain3 at left2
    voice audio.yoshi_vs1_line23
    yo "Ауч!"

    show yuri irked2 at right2
    voice audio.yuri_vs1_line21
    yu "Пфф! Я просто хотела сказать, что можно долго вспоминать о прошлом, но лучше кинуть свой взгляд в будущее!"

    show yoshi comp2 at left2
    voice audio.yoshi_vs1_line24
    yo "Ты права, Юри."

    show yuri happy1 at right2
    voice audio.yuri_vs1_line22
    yu "В любом случае, Йоши, эти бревна сами себя не расколят. Мне бы хотелось увидеть кучу свежих дровишек к закату!"

    voice audio.yuri_vs1_line23
    yu "Если я тебе понадоблюсь, я буду около сарая~!"

    hide yuri_autumn
    hide yuri happy1
    with moveoutright

    show yoshi_autumn at center
    show yoshi shock3 at center
    with move

    voice audio.yoshi_vs1_line25
    yo "Э-эй! Я думал ты помогаешь своему отцу…!"

    voice audio.yuri_vs1_line24
    yu "О, не перживай, какое-то время он справится и без меня! Хи-хи-хи~!"

    show yoshi relief5 at center
    voice audio.yoshi_vs1_line26
    yo "*вздох*"

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
    yo "Брр… И правда становится довольно холодно… Думаю лучше поторопиться."

    play sound sfx_woodchop
    show yoshi confused2 at center
    voice audio.yoshi_v_huh2
    yo "Эм…? Тут уже кто-то есть?"

    scene cg aiden1_1 with fade
    play music go_with_the_flow loop
    voice audio.yoshi_vsa1_line1
    yo "О, Эйден…!"

    voice audio.aiden_vsa1_line1
    a "Здорово, Йоши!"

    voice audio.aiden_vsa1_line2
    a "Я тут решил наколоть дров. Тебе что-то нужно?"

    voice audio.yoshi_vsa1_line2
    yo "Я как раз сам собирался заняться ими, чтобы отнести в офис."

    voice audio.aiden_vsa1_line3
    a "Так забирай и неси. Я их уже много наколол."

    voice audio.aiden_vsa1_line4
    a "Я просто подумал, что теперь, когда стало холоднее, дровишек нам потребуется намного больше чем раньше."

    voice audio.aiden_vsa1_line5
    a "И я был уверен, что Юри попросит тебя ими заняться, вот и решил, подкорректировать твой список дел!"

    voice audio.yoshi_vsa1_line3
    yo "Эйден… Ты не обязан был делать все это. "

    voice audio.aiden_vsa1_line6
    a "Забей! Все в норме! Мне всегда в радость покрушить несколько деревяшек и подкачать мышцы!"

    voice audio.yoshi_vsa1_line4
    yo "Нда, я хотел обратиться к тебе за помощью, но Юри сказала, что у ты занят другими делами."

    show cg aiden1_2 with Dissolve(0.25)
    voice audio.aiden_vsa1_line7
    a "Да я был занят, но уже закончил с готовкой и поставил наш ужин в духовку."

    voice audio.aiden_vsa1_line8
    a "И обнаружил, что израсходовал все дрова, которые были на кухне, так что мне все равно нужно было пойти их наколоть!"

    voice audio.yoshi_vsa1_line5
    yo "Ахха, наш пострел везде поспел?"

    show cg aiden1_3 with Dissolve(0.25)
    voice audio.aiden_vsa1_line9
    a "Именно! Ты же знаешь, что всегда можешь на меня рассчитывать!"

    voice audio.yoshi_vsa1_line6
    yo "Эйден, тебе нужно отдыхать, хотя бы изредка. Я имею в виду... Ты не перестал заниматься хозяйственными делами даже, когда смена завершилась."

    show cg aiden1_2 with Dissolve(0.25)
    voice audio.aiden_vsa1_line10
    a "Не волнуйся, в между сменами работы гораздо меньше. Мне всего-то нужно прокормить, сколько там... шесть человек?"

    voice audio.aiden_vsa1_line11
    a "Кроме того, это обычная лагерная рутина, ничего такого с чем бы я не справился!"

    voice audio.yoshi_vsa1_line7
    yo "Ха, другого я и не ожидал. В конце концов, сколько я себя помню, ты всегда заботился обо всех жителях лагеря."

    show cg aiden1_4 with Dissolve(0.25)
    voice audio.aiden_vsa1_line12
    a "Без проблем, Йоши! Я всегда к твоим услугам!"

    scene bg_forest_autumn_day with fade
    show aiden_work at left2
    show aiden norm1 at left2
    show yoshi_autumn at right2
    show yoshi think1 at right2
    voice audio.yoshi_v_think1a
    yo "Как бы я не был тебе благодарен, за готовсть прийти на помощь, но на следующий год нам потребуется больше работников."
    yo "Особенно, учитывая ожидаемое большое количество заявок. Не хотелось бы, чтобы ты погряз в работе, как в последние смены!"

    show aiden laugh1 at left2
    voice audio.aiden_v_response1a
    a "Как по мне это не сильно большая проблема! Это же всего лишь рутина!"

    show yoshi happy2 at right2
    voice audio.yoshi_v_well1
    yo "Ну раз ты теперь как и я - скаутмастер, то думаю тебе не помешала бы рука помощи."

    hide aiden_work
    hide aiden laugh1
    show aiden2_work at left2
    show aiden2 awkward5 at left2
    voice audio.aiden_v_well1c1
    a "Ну... Если ты так считаешь, я не против."

    show yoshi happy1 at right2
    voice audio.yoshi_v_conj2a
    yo "Кстати об этом, почему бы мне помочь тебе закончить тут с дровами? Раз уж я все равно пришел сюда с топором."

    hide aiden2_work
    hide aiden2 awkward5
    show aiden_work at left2
    show aiden happy1 at left2
    voice audio.aiden_v_laugh2b1
    a "Ха. Я бы не отказался от компании~! Уверен, что физическая работа будет тебе в кайф, после той нудятины, которой ты занимался."

    hide yoshi_autumn
    hide yoshi happy1
    show yoshi2_autumn at right2
    show yoshi2 shy5 at right2
    voice audio.yoshi_v_right4
    yo "В-возможно... А почему ты без рубашки? Разве тебе не холодно?"

    show aiden tease1 at left2
    voice audio.aiden_v_oho1a
    a "Хе~ Ты, что глазеешь на мое тело?"

    hide yoshi2_autumn
    hide yoshi2 shy5
    show yoshi_autumn at right2
    show yoshi awkward6 at right2
    show yoshi_blush1 at right2
    yo "...!"

    show aiden laugh3 at left2
    voice audio.aiden_v_laugh2b1
    a "Ха-Ха! Ты покраснел, как рак, Йоши!"
    a "Успокойся, я думал, что ты привык, что я почти всегда хожу полуголый."

    hide yoshi_autumn
    hide yoshi awkward6
    hide yoshi_blush1
    show yoshi2_autumn at right2
    show yoshi2 comp3 at right2
    voice audio.yoshi_v_unsure3c
    yo "Я-я думаю ты прав, хахаха…"

    show aiden excited1 at left2
    voice audio.aiden_v_rush1a2
    a "А теперь давай приступим к работе!"

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
    yo "Извините, что вошел без стука, сэр! Я принес дрова э—"

    scene cg goro1_1 with fade
    play music old_familiar_home loop
    voice audio.yoshi_vsg1_line1
    yo "Ой…! Надеюсь, я не побеспокил вас, Сэр Горо!"

    voice audio.goro_vsg1_line1
    g "Нет, все в порядке, Йошинори."

    voice audio.yoshi_vsg1_line2
    yo "Я только сложу дрова у камина и сразу уйду!"

    voice audio.goro_vsg1_line2
    g "Спасибо Йошинори. Все в порядке, можешь не торопиться."

    show cg goro1_2 with Dissolve(0.25)
    yo "{i}(Сэр Горо как всегда выглядит занятым… Представить себе не могу, сколько важных дел необходимо сделать, будучи главой лагеря.){/i}"

    show cg goro1_1 with Dissolve(0.25)
    voice audio.goro_vsg1_line3
    g "Полагаю, тебя прислала Юри?"

    voice audio.yoshi_vsg1_line3
    yo "Да, сэр! Так же она упомянула, что ей нужно поработать в сарае."

    show cg goro1_3 with Dissolve(0.25)
    voice audio.goro_vsg1_line4
    g "*вздох* Я вижу она опять, пытается отлынивать от решения административных задач."

    voice audio.yoshi_vsg1_line4
    yo "Может я могу вам чем-нибудь помочь, сэр?"

    show cg goro1_4 with Dissolve(0.25)
    voice audio.goro_vsg1_line5
    g "Не беспокойся,Йошинори. Я сам все решу."

    voice audio.goro_vsg1_line6
    g "Вообще-то я надеялся, что смогу помочь вам с работой по лагерю вместо всей этой бюрократии."

    voice audio.yoshi_vsg1_line5
    yo "После последней смены, вы целыми днями занимались бумажной работой. Я думал, что могу помочь вам с ней."

    voice audio.goro_vsg1_line7
    g "Что ж, сейчас я пытаюсь убедиться, что мы с мистерм Клермонтом решили все вопросы. Это меньшее, что я могу сделать, учитывая его спонсорскую поддержку."

    voice audio.goro_vsg1_line8
    g "Управляя жизнью лагеря, ты делаешь неоценимый вклад. И меня греет мысль, что именно ты будешь тем, кто заменит меня, когда придет время."

    voice audio.yoshi_vsg1_line6
    yo "Это честь услышать от вас такие слова, сэр…!"

    show cg goro1_5 with Dissolve(0.25)
    voice audio.goro_vsg1_line9
    g "Но… Мне очень хочется наверстать упущенное за все то время, когда я, будучи главой Лагеря Друзей, полноценно не управлял им."

    voice audio.goro_vsg1_line10
    g "Я изо всех сил старюсь предемонстрировать, что могу работать так же усердно, как и вы, что эта работа не являеется для меня пустой формальностью."

    voice audio.yoshi_vsg1_line7
    yo "Я понимаю, сэр!"

    show cg goro1_6 with Dissolve(0.25)
    voice audio.goro_vsg1_line11
    g "Йошинори, расслабься. Нет смысла быть со мной настолько  формальным."

    voice audio.yoshi_vsg1_line8
    yo "Ох-х…!"

    voice audio.goro_vsg1_line12
    g "Хотя вас всех можно понять. Последние пару лет я был настолько срогим и замкнутым, что весь персонал был просто напуган..."

    # voice audio.goro_vsg1_line13 #jey missing audio
    g "Я искренне сожалею, что заставил вас испытать такое."

    show cg goro1_7 with Dissolve(0.25)
    voice audio.goro_vsg1_line14
    g "И поэтому я благодарю судьбу, за то что прошлым летом мы провели много времени вместе и смогли понять друг друга."

    voice audio.goro_vsg1_line15
    g "Ты и скауты из прошлой смены заставили меня вспомнить все о чем мы мечтали когда создавали этот лагерь."

    scene bg_office_autumn_day with fade
    show goro_autumn2 at left2
    show goro norm2 at left2
    show yoshi_autumn at right2
    show yoshi comp1 at right2
    yo "..."

    show goro play3 at left2
    voice audio.goro_v_ehem1a
    g "*хмм* Возможно стоит сделать небольшой перерыв, пока я не превратился в мумию в этом кресле."

    show yoshi awkward3 at right2
    voice audio.yoshi_v_what7
    yo "Ч-что..."

    show goro laugh1 at left2
    voice audio.goro_v_laugh2c2
    g "Ахаа! Я тут подумал, что Эйден и Юри правы. С годами я не становлюсь моложе, так что мне эта шутка показалась удачной. А ты как считаешь?"

    show yoshi angry2 at right2
    voice audio.yoshi_v_disagree1a
    yo "Я не согласен, сэр! Вы не выглядите старым, особенно для меня."

    hide goro_autumn2
    hide goro laugh1
    show goro2_autumn2 at left2
    show goro2 annoy3 at left2
    voice audio.goro_v_really4a
    g "Если это попытка подлизаться ко мне, чтобы занять должность главы лагеря, то она провалилась."

    show yoshi shock6 at right2
    voice audio.yoshi_v_sir4
    yo "Н-нет, сэр...! Я действительно так думаю!"

    hide goro2_autumn2
    hide goro2 annoy3
    show goro_autumn2 at left2
    show goro happy2 at left2
    voice audio.goro_v_comp2a2
    g "Я же шучу, Йошинори! Будь проще!"

    show yoshi comp6 at right2
    voice audio.yoshi_v_unsure3c
    yo "Я... Наверное все дело в том, что я отвык от ваших шуток и давно не видел вас в таком хорошем расположении духа."

    show goro play2 at left2
    voice audio.goro_v_heh1a
    g "Прямо как в старые добрые времена?"

    show yoshi laugh1 at right2
    voice audio.yoshi_v_laugh1
    yo "Ха, именно так, сэр! И это замечательно!"

    show goro happy2 at left2
    voice audio.goro_v_well1a
    g "Сказать по правде, я изо всех сил стараюсь поменьше ворчать. Мне хочется, что бы вы все поняли, как приятно мне находится тут в лагере вместе с вами."

    show yoshi play2 at right2
    voice audio.yoshi_v_encourage3
    yo "Мы рады, что старый сэр Горо снова с нами, сэр!"

    hide goro_autumn2
    hide goro happy2
    show goro2_autumn2 at left2
    show goro2 explain2 at left2
    voice audio.goro_v_okay4a
    g "Так, я беру свои слова обратно. Непривычно слышать от тебя слово старый."

    show yoshi laugh2 at right2
    voice audio.yoshi_v_laugh1
    yo "Ха-ха-ха!"

    hide goro2_autumn2
    hide goro2 explain2
    show goro_autumn2 at left2
    show goro talk3 at left2
    voice audio.goro_v_anyway2
    g "В любом случае, думаю нам стоит пойти в сарай и помочь Юри с ее делами."

    show yoshi confused2 at right2
    voice audio.yoshi_v_unsure2b
    yo "В-вы уверены сэр? У вас же сейчас очень много своих дел."

    show goro happy2 at left2
    voice audio.goro_v_alright2a2
    g "Все нормально. Я хочу, чтобы к приезду мистера Клермонта в лагере все сияло."

    show yoshi talk2 at right2
    voice audio.yoshi_v_alright2
    yo "Сарай уже давно забит, так наверно стоит пойти и глянуть, что стоит оставить, а что необходимо выкинуть."

    show goro talk4 at left2
    voice audio.goro_v_agree4a1
    g "Именно так. Давно пора было сделать генральную уборку и избавится от гор по всюду разброшенных вещей."
    g "Этот хлам опасен, особенно учитывая, что в новом году скаутов будет больше и уследить за ними будет сложнее."

    show yoshi talk1 at right2
    voice audio.yoshi_v_response1b
    yo "Я понял, сэр!"

    show goro talk3 at left2
    voice audio.goro_v_anyway2
    g "В общем, еще раз спасибо за беспокойство, Йошинори. Но не пора ли нам выдвинуться на помощь к Юри?"

    show yoshi happy1 at right2
    voice audio.yoshi_v_yessir2
    yo "Да, сэр!"

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
    yu "Мннннннггххххххххх...!"

    play sound sfx_boxesdrop
    show yuri tired2 at center
    voice audio.yuri_v_relief1a1
    yu "Фух! И это только один ящик из тридцати..." with vpunch

    show yuri_autumn at left
    show yuri tired2 at left
    with move

    show aiden_autumn at right
    show aiden shock3 at right
    with dissolve

    voice audio.aiden_v_shock1e1
    a "Хей, полегче. Что ты пытаешься тут сделать, Юри?"

    show yuri talk2 at left
    voice audio.yuri_v_oh1a
    yu "Эм.. ну видишь ли, я хотела убраться в сарае, так как слышала, как папа говорил по телефону, что ему нужно место по склад."

    hide aiden_autumn
    hide aiden shock3
    show aiden2_autumn at right
    show aiden2 worry2 at right
    voice audio.aiden_v_confused2a2
    a "Почему ты не попросила никого из нас помочь? Я имею в виду.. Понимаешь для одного человека это непосильная работа."

    show yuri irked1 at left
    voice audio.yuri_v_hmph1a
    yu "Пфф! Эйден, я сильнее чем кажется."
    yu "Ну и плюс к этому, у вас, парней, и так дел по горло."

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
    a "Так. Я ни за что не позволю тебе таскать все эти ящики самой.Ты можешь пораниться!"

    show yuri sigh2 at left2
    voice audio.yuri_v_sigh1a
    yu "*вздох* Ладно. Я всего лишь хотела, чтобы ты немного отдохнул."

    show aiden laugh2 at right2
    voice audio.aiden_v_laugh2a1
    a "Ха! не переживай за меня -  в конце концов это меньшее, что я могу сделать для тебя."
    a "Йоши и Дедуля делают огромную работу, для того, что бы лагерь функционировал, так что я не против быть на подхвате и браться за мелкие поручения."

    show yuri talk3 at left2
    voice audio.yuri_v_conj5a
    yu "Да ты делаешь больше работы чем мы все вместе взятые, и не имеет значения, мелкая задача или нет. Рутинные дела тоже важны!"
    yu "Эйден, поверь в себя! Ты ведь такой скаутмастер как и мы!"

    hide aiden_autumn
    hide aiden laugh2
    show aiden2_autumn at right2
    show aiden2 sad4 at right2
    voice audio.aiden_v_conj5a1
    a "Я просто.. Понимаешь меня не покидает мысль о том, что все кроме меня изменились в лучшую сторону"
    a "Я имею в виду... после последней смены Дедуля наконец расслабился, а Йоши стал меньше дергаться по поводу  и без."

    show yuri serious3 at left2
    voice audio.yuri_v_no2a1
    yu "Ты не прав, Эйден. В последнее время мой отец все время сидит в своем кресле в офисе, не удивлюсь если его задница была просто к нему приклеена!"
    yu "А Йоши? Когда я подошла к нему, он смотрел на небо и опять был погружен в свои мысли!"

    show yuri comp2 at left2
    voice audio.yuri_v_encourage2a
    yu "Я считаю, что ты слишком строг к себе! Все что ты наговорил, всего лишь твои домыслы!"

    show aiden2 comp3 at right2
    voice audio.aiden_v_laugh1a1
    a "Хе,кажется мои разговоры мрачноваты?"

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
    yo "Юри, мы пришли!"

    show yoshi shock2 at p4_2
    voice audio.yoshi_v_oh2
    yo "...Оу! Эйден ты тоже здесь!"

    hide aiden2_autumn
    hide aiden2 norm2
    show aiden_autumn at p4_4
    show aiden happy2 at p4_4
    voice audio.aiden_v_hey2a2
    a "Йоши, Дедуля - приветы! Я просто проходил мимо и увидел, как Юри сама пытается разобрать в сарае."

    show yuri irked2 at p4_3
    voice audio.yuri_v_ugh3a
    yu "Нда, здорово... Теперь тут вся толпа."

    show goro worry2 at p4_1
    voice audio.goro_v_yuridear1b
    g "Юри-деточка, ты должна была подождать, чтобы мы помоголи тебе."

    show aiden talk2 at p4_4
    voice audio.aiden_v_goro3b
    a "Перво-наперво, я удивлен, что ты не в офисе дедуля. Я думал, что ты по уши завален всякой ерундой для Клермонта"

    show goro confused3 at p4_1
    voice audio.goro_v_well1a
    g "Эйден, а ты сам не перетрудился?"

    show aiden bold5 at p4_4
    voice audio.aiden_v_psh1a
    a "Пффф. Я в порядке!"

    show goro talk3 at p4_1
    voice audio.goro_v_anyway2
    g "В общем почему бы не оставить всю эту работу мне? Это будет неплохой тренировкой после сидячего дня."

    show yoshi happy2 at p4_2
    voice audio.yoshi_v_think4
    yo "Сэр, раз уж мы все собрались тут, то почему бы не не заняться этим вместе?"

    show yuri comp4 at p4_3
    voice audio.yuri_v_aww2a
    yu "Оууу~ Все заботятся друг о друге, прямо как в старе добрые времена~"

    show goro happy1 at p4_1
    voice audio.goro_v_ehem1a
    g "Хм.. Тогда давайте начнем пока не село солнце. После заката бедет невыносимо холодно."

    show yoshi happy1 at p4_2
    show yuri bold2 at p4_3
    show aiden bold2 at p4_4
    all "Да, сэр!"

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
    yo "Блин, Юри, что в этих ящиках? Они весят под тонну!"

    show yuri comp4 at right2
    voice audio.yuri_v_laugh1a1
    yu "Ну... просто некоторые безделушки без которых мне не обойтись~ХиХи~"

    show yoshi think2 at left2
    voice audio.yoshi_v_think1a
    yo "Я и не знал, что большая часть вещей в сарае твои. Я думал там полно какого-нибудь хозяственного инвентаря или чего-то подобного..."

    show yuri tease2 at right2
    voice audio.yuri_v_well4a
    yu "Ну... это инвентарь... в каком-то смысле."

    show yoshi_autumn at left
    show yoshi think2 at left
    show yuri_autumn at center
    show yuri tease2 at center
    with move

    show goro_autumn at right
    show goro confused2 at right
    with dissolve

    voice audio.goro_v_think3
    g "Хм.. Я тут нашел маленькую коробочку с надписью \“Не трогать\”..."

    show yuri_autumn at right
    show yuri irked2 at right
    with move

    show yuri_autumn at center
    show yuri irked2 at center
    with move

    voice audio.yuri_v_thanks1a
    yu "Так и не трогай ее, заранее спасибо!"

    show goro annoy2 at right
    voice audio.goro_v_think3
    g "Хм.. Что в ней? Ты держишь опасные предметы в лагере?"

    show yuri excited2
    voice audio.yuri_v_laugh2a1
    yu "Это зависит от того, как ты будешь их использовать~!"

    show goro awkward3 at right
    voice audio.goro_v_sigh1b
    g "Я-я даже пробовать не буду... Чую я зря спросил об этом."

    show yoshi talk1 at left
    voice audio.yoshi_v_huh5
    yo "Мне кажется, что в большинстве ящиков в которые мы заглянули просто случайный набор предметов."

    show goro think2 at right
    voice audio.goro_v_think1a1
    g "Когда Юри была маленькой, ее сложно было оторвать от того, что ей было интересно. Всякий раз когда у нее появлялось новое увлечение, она была буквально одержима им."

    show yuri angry3 at center
    voice audio.yuri_v_angry2a1
    yu "Что что? Ты последний человек, от которого я ожидала это услышать!"
    yu "Ведь именно ты никак не можешь расстаться со старыми вещами!"

    show goro laugh3 at right
    voice audio.goro_v_laugh2c2
    g "Ха, я думаю ты права. В моей коллекции много книг и произведений искусства"

    show yoshi confused2 at left
    voice audio.yoshi_v_why2
    yo "Зачем ты держишь все эти вещи в сарае? почему бы не хранить их у себя в комнате?"

    show yuri explain2 at center
    voice audio.yuri_v_think1a1
    yu "Моя комната переполнена... Но нужно же было куда-нибудь их убрать..."

    show yoshi awkward4 at left
    voice audio.yoshi_v_oh3
    yo "Оу..."

    show yuri irked1 at center
    voice audio.yuri_v_what1a
    yu "Почему вы двое так на меня смотрите?"
    yu "Именно по этому я пыталась разобрать их сама!"

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
    a "Так, Юри! Это последняя коробка на которой стоит твое имя."
    a "А еще я подмел в сарае. Никогда бы не подумал, что в нем так просторно!"

    show yuri happy2 at p4_3
    voice audio.yuri_v_thanks1b
    yu "Больше спасибо за помошь парни! Я это очень ценю."
    yu "Я заберу все отсюда и решу что из этого я хочу сохранить."

    show aiden happy3 at p4_1
    voice audio.aiden_v_alright1a3
    a "Отлично! Если вы двое не против, я могу использовать свои мега-мышцы, чтобы разобраться со всем, что тут осталось"
    a "Тут несколько инструментов, которые необходимо починить, а также куча сломанного ржавого инвентаря, от которого нужно избавится"

    show yoshi happy1 at p4_2
    voice audio.yoshi_v_sure2
    yo "Конечно, Эйден!"

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
    yu "Хмм, так посмотрим..."

    show yuri shock5 at p5_5
    voice audio.yuri_v_shock2a
    yu "*задыхается*"

    hide yuri_autumn
    hide yuri shock5
    show yuri2_autumn at p5_5
    show yuri2 fangirl2 at p5_5
    voice audio.yuri_v_omg1a
    yu "О БОЖЕ!!!" with vpunch

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
    g "Что случилось?"

    show yuri2 laugh3 at p4_4
    voice audio.yuri_v_excited1a
    yu "Парни вы не поверите, что я сейчас нашла!!"

    show cg fade at truecenter
    show fx1 at fx_pos
    with dissolve

    voice audio.goro_v_yuri7a
    g "Юри... ты доведешь меня до инфаркта. Я думал ты поранилась или что похуже.."

    voice audio.yuri_v_rush1d1
    yu "Вы не понимаете! Я искала его целую вечность! Не могу поверить, что все это время он был в сарае!"

    voice audio.aiden_v_confused2a2
    a "Что это вообще такое...? Похоже на древнюю книгу, в которую ведьмы записывают свои заклинания."

    voice audio.yuri_v_aiden8a
    yu "Эйден! Я не могу поверить, что ты не знаешь что это! Мы делали записи в этой книге, когда были младше, вспомнил?"

    voice audio.yoshi_v_oh2
    yo "ОО!!! Я узнал его!"

    voice audio.yoshi_v_yuri5
    yo "Это же твой дневник, Юри?"

    voice audio.yuri_v_agree1c1
    yu "Да! Я так рада, что хоть ты помнишь, Йоши!"

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
    a "блииин... Я вообще забыл о его существовании... Насколько помню последний раз я видел этот дневник, когда мы были скаутами!"
    a "Он выглядит несколько потертым... Это что пятна от воды?"
    yu "Да... коробка в которой он был немного намокла... но все равно большая часть читаема!!!"

    hide goro_autumn
    hide goro confused1
    show goro2_autumn at p4_3
    show goro2 confused3 at p4_3
    voice audio.goro_v_think1b1
    g "Я вроде не видел твой дневник раньше..."

    show yuri explain1 at p4_4
    voice audio.yuri_v_goro1a
    yu "Да, потому что был вечно занятым скаутмастером."
    yu "В нем я хранила все свои любимые воспоминания о вас парни! Было очень весело описывать все то, чем мы занимались."

    show yuri talk3 at p4_4
    voice audio.yuri_v_aww1b
    yu "Мне очень хотелось показать его скаутам из прошлой смены и рассказать об истории этого лагеря..."
    yu "Но я не смогла, потому что думала, что этот дневник потерян навсегда."

    show yoshi confused2 at p4_2
    voice audio.yoshi_v_think1a
    yo "Ты поэтому выдала такие же дневники некоторым новоприбывшим скаутам?"

    show yuri happy1 at p4_4
    voice audio.yuri_v_yeah1b1
    yu "Да~! Записывать свои воспоминания было так здорово, что мне зателось, чтобы они тоже смогли испытать эти чувства! "
    yu "Понимаете, я всегда любила писать, даже когда была совсем юной. Ну и я подумала, что было бы здорово научить этому скаутов, что бы в будущем они с любовью смогли оглянуться на свое прошлое."

    show yuri laugh1 at p4_4
    voice audio.yuri_v_laugh1a1
    yu "И я ввела свою личную традицию предлагать вести дневник скаутам полным вдохновения, таким как мистер Акатора и мистер Нагаме!"

    show aiden tease2 at p4_1
    voice audio.aiden_v_comeon2a
    a "Ой да ладно. Ты просто посмотрела в личных анкетах, кто в графе хобби написал “сочинительство”"

    show yuri pout2 at p4_4
    voice audio.yuri_v_hmph1b
    yu "Пфф, Эйден, вовсе нет!"

    show goro2 happy2 at p4_3
    voice audio.goro_v_actually1a
    g "Теперь мне самому стало интересно каким был лагерь глазами скаута..."

    show yuri excited2 at p4_4
    voice audio.yuri_v_alright1d1
    yu "Тогда предлагаю посмотреть. Вы не против?"

    show cg fade at truecenter
    show fx2 2 at fx_pos
    with dissolve

    voice audio.yuri_v_kyaa1b
    yu "Ийййаааяяя!!! Посмотрите на это! Это вы парни~!!"

    yo "{i}(Это… наша первая совместная фотография!){/i}"
    yo "{i}(Это пробуждает во мне воспоминания о том что произошло в тот день…){/i}"

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
    yu "Давайте парни!  Поторопитесь! В такой замечательный день как этот, мы просто обязаны сделать снимок!"

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
    a "Ю-Юри! Т-ты не могла бы хоть немного подвинуться?!  Ты наступила мне на ногу!"

    show yyuri excited2 at left3
    voice audio.yyuri_v_andre1a
    yu "Мистер Андрэ, я думаю было замечательно, если вы сфотографировались с нами!"
    yu "В конце концов, это же первый день Эйдена в качестве помощника по лагерю!"

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
    u "Ничего страшного! Лучше я вас сфотографирую, это все же момент вашей жизни!"

    show yyuri_camp2 at p4_4
    show yyuri excited1 at p4_4
    show yyoshi_camp at p4_3
    show yyoshi happy1 at p4_3
    with move

    voice audio.yyoshi_v_congrats1
    yo "Эйден, поздравляю тебя! Ты наконец, стал частью Лагеря Друзей!"
    yo "Я бы хотел, что бы ты был скаутом, но и этот вариант тоже неплох. Мы же все равно можем тусить и общаться друг с другом!"

    show yaiden laugh1 at p4_2
    voice audio.yaiden_v_laugh1a1
    a "Хе, это все благодаря тебе, Йоши! Ты с самого первого дня рекомендовал меня!"

    show yyoshi comp5 at p4_3
    voice audio.yyoshi_v_disagree1a
    yo "Неее, ты сам проявил себя во всей красе, помогая по лагерю!"

    show yaiden happy1 at p4_2
    voice audio.yaiden_v_well1a1
    a "И все же этого бы не случилось, если бы ты не указывал сэру Горо, на каждую мелочь, которой я занимался!"

    show yyoshi laugh1 at p4_3
    voice audio.yyoshi_v_laugh1
    yo "Ахха! Я думаю это просто командная работа!"

    show yyuri angry2 at p4_4
    voice audio.yyuri_v_goro9c
    yu "Папа!! Мама!! Вы чего так долго?!" with vpunch

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
    g "Ой... Идем, деточка!"

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
    g "Вера, давай все решим позже, хорошо?"

    show vera annoy2 at p6_6
    #voice audio.vera_v_
    v "Хмпф. Ладно"

    show ygoro talk1 at p6_5
    voice audio.ygoro_v_rush2b1
    g "Давай, присоединяйся к нашей фото—"

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
    yu "Забей на нее, папа! Просто иди уже к нам!"

    show ygoro comp2 at p5_4
    voice audio.ygoro_v_sorry2a
    g "Ах, да, конечно"

    show yyoshi confused1 at p5_3
    voice audio.yyoshi_v_sirgoro7
    yo "Сэр Горо, все хорошо?"

    show ygoro comp5 at p5_4
    voice audio.ygoro_v_oh2
    g "Ха! Все в норме! Моя супруга просто немного устала!"

    show yyuri happy1 at p5_5
    voice audio.yyuri_v_alright1a1
    yu "Так, мистер Андре! Мы готовы!"

    show andre happy3 at p5_1
    voice audio.andre_v_camera1b
    u "Супер, 3… 2… 1… Улыбочку!"

    play sound sfx_camerashot
    show yyuri laugh3 at p5_5
    show yaiden grin1 at p5_2
    show yyoshi grin2 at p5_3
    show ygoro grin3 at p5_4
    with flash

    show andre laugh3 at p5_1
    voice audio.andre_v_amazed1b1
    u "Вау, вы только посмотрите! Фото уже печатается! Это нереально круто!"

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
    yu "Можно глянуть? Можно? Можно?"

    show yyuri laugh3 at p5_2
    voice audio.yyuri_v_kyaa1c
    yu "Йиия! Мы так мило выглядим на этой фотке!!" with vpunch

    show ygoro happy1 at p5_5
    voice audio.ygoro_v_yuri2
    g "Если хочешь, Юри, я могу поместить ее в рамку, чтобы ты могла повесить ее у себя."

    show yyuri bold2 at p5_2
    voice audio.yyuri_v_no2a1
    yu "Ни за что! Она должна быть в моем альбоме!"

    show ygoro laugh1 at p5_5
    voice audio.ygoro_v_laugh1b
    g "Хаха, ну конечно же."

    voice audio.ygoro_v_anyway1
    g "В любом случае, это замечательный день стоит отпраздновать! Я купил для вас, ваше любимое Неаполитанское мороженое!"

    show yyoshi excited1 at p5_4
    voice audio.yyoshi_v_amazed1c
    yo "Вау! Вкусняшки!!"

    show yaiden confused2 at p5_3
    voice audio.yaiden_v_confused2a1
    a "Неаполитанское? Это еще что за мороженое?"

    show yyuri happy1 at p5_2
    voice audio.yyuri_v_aiden3a
    yu "Эйден, это мороженое с тремя разными вкусами. Оно всегда выручает папу, когда мы не можем договориться какое мороженое брать!"
    yu "Да и цвета в нем отлично нам подходит! Клубника для меня, ваниль для папы и шоколад для Йоши!"

    show yyoshi comp5 at p5_4
    voice audio.yyoshi_v_laugh3
    yo "Так, посколько Эйден, теперь тоже часть нашей команды, то в следующий раз нам придется добавить еще один вкус!"

    show yaiden excited3 at p5_3
    voice audio.yaiden_v_oh1a
    a "Оу! Это было бы круто!"

    show yyuri bold2 at p5_2
    voice audio.yyuri_v_laugh1a2
    yu "И это обязательно, должно быть что-то зеленое! Это абсолютно точно твой цвет!"

    show yyoshi annoy3 at p5_4
    voice audio.yyoshi_v_yuri9a
    yo "Юри, зачем ты все ограничила цветом? Эйден сам должен выбрать то, что ему нравится!"

    show yaiden comp5 at p5_3
    voice audio.yaiden_v_alright3a
    a "Йоши, все в норме! Мне редко удается поесть мороженое, и я пока так и не решил, какое мне нравится больше всего!"

    show ygoro play2 at p5_5
    voice audio.ygoro_v_well1
    g "Эм, может вы все-таки его съедите пока оно не растаяло."

    show andre relief2 at p5_1
    voice audio.andre_v_service1a
    u "Я выдам вам его в столовой! За мной!"

    hide andre_camp
    hide andre relief2
    with dissolve

    show yyuri_camp2 at left3
    show yyuri excited2 at left3
    with move
    voice audio.yyuri_v_rush1c1
    yu "Вперед, Эйден! двай для начала все попробуем!"

    show yaiden panic3 at p5_3
    voice audio.yaiden_v_hey1d
    a "Э-ээй, Ю-Юри...!"

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
    yo "Вы не пойдете с нами, сэр Горо?"

    show ygoro comp2 at right2
    voice audio.ygoro_v_yoshi2
    g "Я присоединюсь к вам после телефонного звонка. Начинайте без меня, Йошинори."

    show yyoshi comp5 at left2
    voice audio.yyoshi_v_sir2
    yo "Я оставлю вам ванильного мороженого, сэр!"

    show ygoro laugh2 at right2
    voice audio.ygoro_v_laugh1b
    g "Ахха, спасибо!"

    show yyoshi laugh2 at left2
    voice audio.yyoshi_v_bye5
    yo "Увидимся!"

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
    yu "Вау... мы тут выглядим совсем по-другому..."

    voice audio.goro_v_think1a1
    g "хм... Напомни, когда эта фотография была снята?"

    voice audio.yuri_v_goro2b
    yu "Примерно в то время, когда ты подарил мне новую камеру, папа~! Почти десять лет назад, еще во время первой смены лагеря друзей!"

    voice audio.aiden_v_sheesh1b
    a "Блин, я себя совсем не узнаю. не ужели это было так давно...?"

    voice audio.goro_v_satisfied2a
    g "Этоа фотография вызывает у меня ностальгию... Она возвращает меня..."

    voice audio.aiden_v_laugh1d1
    a "ХиХиХи~ Дедуля, а как твои волосы умудрились поседеть всего за десять лет?"

    voice audio.goro_v_hmph1a
    g "Хмпф, на себя посмотри, Эйден. Кто бы подумал, что такоф дрищ как ты, так вымахает всего за пару лет."

    voice audio.aiden_v_oho1a
    a "Ты о моей божественной красоте? Я приму это как комплимент."

    voice audio.yuri_v_aww2a
    yu "Эхх, вы с Йоши выглядили такими юными с вашими стройными телами! Нет, нет, не подумай у меня нет претензий к вашим мышцам~"

    hide cg fade
    hide fx2 2
    with dissolve

    hide yoshi_autumn
    hide yoshi norm3
    show yoshi2_autumn at p4_2
    show yoshi2 think5 at p4_2
    voice audio.yoshi_v_sigh3a
    yo "Время летит незаметно, вы согласны?"

    show yuri comp4 at p4_4
    voice audio.yuri_v_laugh1a1
    yu "Да, я скучаю по тем временам, когда я была скаутом. Это было лучшее время в моей жизни!"

    show goro talk3 at p4_3
    voice audio.goro_v_ehem1a
    g "*Кхм* И тем не менее, Юри-деточка, почему бы нам не закончить с работой, пока ты не слишком увлеклась?"

    show yuri happy2 at p4_4
    voice audio.yuri_v_actually1a
    yu "Ну... я забрала из сарая все, что мне было нужно. Так что оставляю уборку вам парни~!"

    show aiden confused2 at p4_1
    voice audio.aiden_v_confused1a1
    a "Эй! Ты куда?"

    show yuri angry2 at p4_4
    voice audio.yuri_v_hmph1a
    yu "Я не видела свой дневник несколько лет! Дайте мне насладиться этим моментом!"
    yu "Конечно потребуется время чтобы прочесть все, что тут написано... Я обязательно расскажу вам, если прочту что-то интересное!"

    show yuri excited3 at p4_4
    voice audio.yuri_v_bye1a1
    yu "Пооокаа~!"

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
    g "*вздох* Ее действительно нельзя остановить, если он за что-то уцепится."

    show aiden laugh1 at left
    voice audio.aiden_v_laugh2b1
    a "Ахха, и какие еще есть новости?"

    voice audio.aiden_v_anyway1b
    a "В общем, нам нужно вынести весь этот хлам, и мы здесь закончили!"

    show aiden happy1 at left
    a "Парни помогите мне тут, а с меня тогда пиво."

    show goro happy1 at right
    voice audio.goro_v_agree7a
    g "Звучит неплохо. Мне непомешало бы немного расслабиться после сегодняшнео трудного дня. Что скажешь Йошинори?"

    hide yoshi2_autumn
    hide yoshi2 think5
    show yoshi_autumn at center
    show yoshi shock3 at center
    voice audio.yoshi_v_ah3
    yo "Д-да! Буду рад присоединиться!"

    show aiden happy3 at left
    voice audio.aiden_v_amazed3b
    a "Отлично! Давайте покончим с этим!"

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
    a "Еще раз спасибо что помогаете мне по хозйственным делам, парни."

    show goro laugh3 at left
    voice audio.goro_vs2_line1
    g "Без проблем, Эйден. У меня рядко выпадает возможность помочь тебе."

    voice audio.goro_vs2_line2
    g "Наш лагерь существует несколько лет, во многом благодаря твоим стараниям"

    show aiden comp5 at right
    voice audio.aiden_vs2_line2
    a "Оу, Дедуля... Всегда приятно услышать от тебя комплимент."

    hide goro_autumn
    hide goro laugh3
    show goro2_autumn at left
    show goro2 disappoint3 at left
    voice audio.goro_vs2_line3
    g "Эммм, я всегда их говорю... когда это оправдано."

    show aiden laugh1 at right
    voice audio.aiden_vs2_line3
    a "Ха-ха, это так, но тебе трудно угодить. Ты хвалишь нас раз в сто лет!"

    hide goro2_autumn
    hide goro2 disappoint3
    show goro_autumn at left
    show goro talk1 at left
    voice audio.goro_vs2_line4
    g "Нуу, как я уже говорил сегодня утром  Йошинори, я стараюсь быть более открытым... особенно учитывая мое поведение последние несколько лет."

    show aiden relief2 at right
    voice audio.aiden_vs2_line4
    a "Не парься Дедуля. Мы прекрасно понимаем, что сегодня ты весь день разгребал важные бумажные дела"

    show goro happy1 at left
    voice audio.goro_vs2_line5
    g "Пока я еще тут хочу сказть спасибо за приглашение выпить. Я давно не пил такого вкусного пива."

    hide aiden_autumn
    hide aiden relief2
    show aiden2_autumn at right
    show aiden2 scared2 at right
    voice audio.aiden_vs2_line5
    a "Тсс! Дедуля, не пались! Мы ведь не должны пить при всех!"

    show goro panic4 at left
    voice audio.goro_vs2_line6
    g "Чего?! Я всегда выпивал на улице! Почему я вдруг должен поменять свои привычки?"

    show aiden2 annoy6 at right
    voice audio.aiden_vs2_line6
    a "Да ну?! Я думал, кто-кто, а уж ты то должен знать местные правила лучше всех!"

    hide aiden2_autumn
    hide aiden2 annoy6
    show aiden_autumn at right
    show aiden confused2 at right
    voice audio.aiden_vs2_line7
    a "Ты ведь, тоже их знаешь, Йоши? Ты ведь бухал со мной раньше!"

    show yoshi2 explain1 at center
    yo "..."

    hide goro_autumn
    hide goro panic4
    show goro2_autumn at left
    show goro2 confused2 at left
    voice audio.goro_vs2_line7
    g "Йошинори?"

    hide yoshi2_autumn
    hide yoshi2 explain1
    show yoshi_autumn at center
    show yoshi shock2 at center
    voice audio.yoshi_vs2_line1
    yo "Агхм! Извините, парни, о чем вы тут говорили?"

    show goro2 worry3 at left
    voice audio.goro_vs2_line8
    g "С тобой все впорядке, Йошинори? Ты опять задумался?"

    show yoshi worry2 at center
    voice audio.yoshi_vs2_line2
    yo "Ээм, нет сэр! Я в норме..!"

    show aiden talk5 at right
    voice audio.aiden_vs2_line8
    a "Ну же, что с тобой творится? С того момента, как Юри показала нам ту фотографию, ты не проронил ни слова!"

    hide goro2_autumn
    hide goro2 worry3
    show goro_autumn at left
    show goro talk3 at left
    voice audio.goro_vs2_line9
    g "Действительно. Это фото вызвало у тебя какие-то плохие воспоминания?"

    hide yoshi_autumn
    hide yoshi worry2
    show yoshi2_autumn at center
    show yoshi2 comp3 at center
    voice audio.yoshi_vs2_line3
    yo "Н-нет, наоборот! Увидев это фото, где мы все вместе, я задумался о событиях прошлого."

    hide aiden_autumn
    hide aiden talk5
    show aiden2_autumn at right
    show aiden2 think6 at right
    voice audio.aiden_vs2_line9
    a "Эмм? О чем ты?"

    show yoshi2 explain2 at center
    voice audio.yoshi_vs2_line4
    yo "Ну.. в то время сэр Горо был нашим скаутмастером, и мы проводили в этом лагере прекрасное лето."

    voice audio.yoshi_vs2_line5
    yo "... думая о том, насколько это было здорово, мне захотелось вновь пережить все эти моменты нашей жизни."

    show goro comp2 at left
    voice audio.goro_vs2_line10
    g "Я тоже вспоминаю эти дни с особой любовью. Такие скауты, как вы, да еще и в первой смене, разжигали во мне желание больше отдавать себя работе в Лагере Друзей."

    hide aiden2_autumn
    hide aiden2 think6
    show aiden_autumn at right
    show aiden play5 at right
    voice audio.aiden_vs2_line10
    a "Хех, ну в конце концов это и правда были наши лучшие совместные воспоминания."

    show yoshi2 talk1 at center
    voice audio.yoshi_vs2_line6
    yo "Да, так и есть... Но проблема в том, я похоже совсем забыл, каково это - получать удовольствие, ни о чем не беспокоясь."

    voice audio.yoshi_vs2_line7
    yo "Я осознал, что с тех пор как я стал скаутмастером, я был сконцентрирован лишь на настоящем и будущем Лагеря Друзей..."

    hide goro_autumn
    hide goro comp2
    show goro2_autumn at left
    show goro2 talk2 at left
    voice audio.goro_vs2_line11
    g "Думаю, это частично моя вина. На какое-то время я оставил тебя одного, без надлежащей поддержки, и это стало для тебя тяжелой ношей."

    hide yoshi2_autumn
    hide yoshi2 talk1
    show yoshi_autumn at center
    show yoshi worry4 at center
    voice audio.yoshi_vs2_line8
    yo "ЭЭэ, я вовсе не об этом, сэр!"

    voice audio.yoshi_vs2_line9
    yo "Моя мечта была, стать скаутмастером. И теперь, когда я достиг своей цели, я оглядываюсь назад и пытаюсь понять, почему я так сидьно желал этого."

    hide goro2_autumn
    hide goro2 talk2
    show goro_autumn at left
    show goro comp2 at left
    voice audio.goro_vs2_line12
    g "Знаешь, Йошинори, ты всегда был таким активным и заботливым скаутом, что всегда вдохнавлял меня, работать на благо Лагеря Друзей все больше и больше."

    voice audio.goro_vs2_line13
    g "Так что надеюсь, я смогу вернуть тебе долг и помочь расслабиться да и просто приятно провести время в лагере."

    show yoshi comp2 at center
    voice audio.yoshi_vs2_line10
    yo "Сэр Горо.."

    show aiden talk1 at right
    voice audio.aiden_vs2_line11
    a "Да, я тоже скучаю по старому, Йоши! Ты был таким веселыми беззаботым в те времена, а теперь ты почти все время проводишь в раздумьях и переживаниях!"

    voice audio.aiden_vs2_line12
    a "Мы просто-напросто должны заставить тебя перестать думать обо всем это, хе-хе~"

    hide yoshi_autumn
    hide yoshi comp2
    show yoshi2_autumn at center
    show yoshi2 think6 at center
    voice audio.yoshi_vs2_line11
    yo "Ну... Мне кажется, меня стали посещать такие мысли, потому что сейчас, между сменами, у меня больше свободного времени."

    voice audio.yoshi_vs2_line12
    yo "Ведь обычно мой мозг занят придумыванием новых видов деятельности для скаутов, и мыслями о том, как сделать, там чтобы скаутам в лагере жилось лучше."

    show yoshi2 think5 at center
    voice audio.yoshi_vs2_line13
    yo "По окончании смены, обязанностей у меня становится гораздо меньше... и у меня появляется достаточно времнеи, чтобы,  хоть немного, подумать о себе."

    hide yoshi2_autumn
    hide yoshi2 think5
    show yoshi_autumn at center
    show yoshi worry2 at center
    voice audio.yoshi_vs2_line14
    yo "Эм... Извините, что вам двоим приходится все это выслушивать!"

    show aiden comp2 at right
    voice audio.aiden_vs2_line13
    a "Нет нет, Йоши, все в норме. ты же знаешь, что мы всегда готовы выслушать тебя и помочь, по мере наших сил!"

    show goro happy1 at left
    voice audio.goro_vs2_line14
    g "Именно так. Ты всегда можешь на нас расчитывать, Йошинори."

    show yoshi comp2 at center
    voice audio.yoshi_vs2_line15
    yo "С-спасибо, огромное вам двоим."

    show aiden comp5 at right
    voice audio.aiden_vs2_line14
    a "Без проблем, Йоши~ Но довольно этих дурацких разговоров! Пора немного выпить и расслабиться!"

    hide goro_autumn
    hide goro happy1
    show goro2_autumn at left
    show goro2 worry2 at left
    voice audio.goro_vs2_line15
    g "Честно говоря, меня немного бескоит тот факт, что официальные лица могут увидеть нас тут с пивом."

    show aiden wink2 at right
    voice audio.aiden_vs2_line15
    a "Ой да ладно тебе, Дедуля! Жизнь коротка! Да и что это вообще за жизнь, если хоть иногда не нарушать правила?"

    show yoshi laugh2 at center
    voice audio.yoshi_vs2_line16
    yo "Аххаа! Вот теперь это ДЕЙСТВИТЕЛЬНО похоже на старые добрые времена. Ты всегда был зачинщиком всех беспорядков, Эйден"

    show aiden play3 at right
    voice audio.aiden_vs2_line16
    a "Эй, но это никогда не приводило к серьезным последствиям! Ведь так, Дедуля?"

    show goro2 sigh1 at left
    voice audio.goro_vs2_line16
    g "*вздох* Я начинаю беспокоится о тебе , как о скаутмастере, Эйден."

    show aiden annoy3 at right
    voice audio.aiden_vs2_line17
    a "Ой только не стройте из себя невинных овечек! Вспомните только, сколько мы втроем выпили за прошлое лето!"

    hide goro2_autumn
    hide goro2 sigh1
    show goro_autumn at left
    show goro think2 at left
    voice audio.goro_vs2_line17
    g "С большим притоком новых скаутов, думаю, нам придется это прекратить. Кто-нибудь из них может нас застукать."

    show yoshi happy1 at center
    voice audio.yoshi_vs2_line17
    yo "Ха! Юри была бы счастлива, если бы это прекратилось. Он ругается каждый раз, когда мы выпиваем."

    show goro sigh3 at left
    voice audio.goro_vs2_line18
    g "*вздох* Да сложно расслабиться, выпивая, когда понимаешь, что она расстраивается и-за этого."

    show aiden tease1 at right
    voice audio.aiden_vs2_line18
    a "Хе, выпей еще пару кружек и ты будешь достаточно \"расслабленным\", чтобы просто ее игнорировать!"

    hide goro_autumn
    hide goro sigh3
    show goro2_autumn at left
    show goro2 annoy2 at left
    voice audio.goro_vs2_line19
    g "Хмф, ты думаешь этого хватит, чтобы меня отключить? Я, знаешь ли, обычно пью гораздо более крепкие вещи."

    show aiden talk2 at right
    voice audio.aiden_vs2_line19
    a "Да точно! Я видел, как много ты мог выпить раньше! Думаю не последню роль в этом играют, эти накачанные мышцы~"

    voice audio.aiden_vs2_line20
    a "Твое крепкое тело, выдержит горааздо больше чем несколько бутылок пива!"

    show goro2 play3 at left
    voice audio.goro_vs2_line20
    g "Твое и Йошинори тоже. Как я уже говорил ранее, я удивлен как вы двое подкачались за последние годы."

    voice audio.goro_vs2_line21
    g "Я могу понять, как этого добился Эйден. Он тренируется без устали каждый день. Но я не подозревал, что ты тоже тренируешься, Йошинори."

    show yoshi laugh1 at center
    voice audio.yoshi_vs2_line18
    yo "Ха-ха, я всего пару раз присоединялся к Эйдену на тренировках. Но стараюсь держать себя в форме, чтобы не возникало проблем при выполнении работы."

    voice audio.yoshi_vs2_line19
    yo "У нас лагерь под открытым небом, в конце-концов!"

    show aiden pout1 at right
    voice audio.aiden_vs2_line21
    a "Так, так твои мысли опять возвращаются к работе, Йоши! Давай выпей еще и расслабься уже наконец! "

    hide yoshi_autumn
    hide yoshi laugh1
    show yoshi2_autumn at center
    show yoshi2 awkward4 at center
    voice audio.yoshi_vs2_line20
    yo "О-ох..."

    hide goro2_autumn
    hide goro2 play3
    show goro_autumn at left
    show goro happy2 at left
    voice audio.goro_vs2_line22
    g "Эйден прав. Да и плюс ко всему у нас не часто выпадает шанс вот так посидеть вместе."

    hide yoshi2_autumn
    hide yoshi2 awkward4
    show yoshi_autumn at center
    show yoshi comp3 at center
    voice audio.yoshi_vs2_line21
    yo "Да, парни, вы правы...!"

    show aiden happy1 at right
    voice audio.aiden_vs2_line22
    a "Нам нужно собираться так почаще! Возможно пока не началась новая смена, мне удасться увидеть пьяного Дедулю!"

    show yoshi think2 at center
    voice audio.yoshi_vs2_line22
    yo "Раз уж ты об это заговорил, то я сам видел сэра Горо пьяным, за все время только один раз."

    show goro talk2 at left
    voice audio.goro_vs2_line23
    g "*Экхм* Это секретная информация, Йошинори."

    show aiden tease2 at right
    voice audio.aiden_vs2_line23
    a "Я знаю, что Йоши сносит крышу, когда он напьется!"

    show yoshi panic3 at center
    voice audio.yoshi_vs2_line23
    yo "Э-Эйден...!"

    show aiden comp5 at right
    voice audio.aiden_vs2_line24
    a "Хе-хе~ Я же шучу, Йоши~"

    show yoshi comp2 at center
    voice audio.yoshi_vs2_line24
    yo "В любом случае спасибо вам обоим, что даете мне возможность посмотреть на этот переиод между сменами другими глазами."

    voice audio.yoshi_vs2_line25
    yo "Теперь я понимаю, что мне есть чем заняться, даже когда в лагере нет скаутов..."

    $working = False
    $shuffle_menu()
    menu():
        yo "Мне есть, чего ждать, о чем мечтать, когда в лагере нет скаутов... {fast}"
        "Испытывать вместе новые ощущения.":
            $working = True
            $score_aiden += 1
            show yoshi happy1 at center
            voice audio.yoshi_vs2_line26a
            yo "Я хочу испытать новые ощущения вместе с людьми, которые мне действительно не безразличны!"

            show aiden excited1 at right
            voice audio.aiden_vs2_line25a
            a "Вот и я об этом! Пришло время вернуть тебя, Йоши!"

            voice audio.aiden_vs2_line26a
            a "Если мы дарим нашим скаутам незабываемые воспоминания об этом лагере, то почему мы не можем подарить их себе!"

            show yoshi excited1 at center
            voice audio.yoshi_vs2_line27a
            yo "Ты прав, Эйден! Никогда не поздно узнать, что готовит нам будущее!"

            voice audio.yoshi_vs2_line28a
            yo "И нет никого, с кем бы я хотел испытать эти новые эмоции, кроме вас парни!"
        "Пусть узы связывающие нас станут еще крепче.":
            $working = True
            $score_aiden += 1
            show yoshi happy1 at center
            voice audio.yoshi_vs2_line26b
            yo "Мое желание, сделать эти узы крепче, сильнее чем когда-либо раньше."

            show aiden excited1 at right
            voice audio.aiden_vs2_line25b
            a "Вот теперь, я стобой полностью соглаен!"

            voice audio.aiden_vs2_line26b
            a "Мы не должны упустить эту возможность провести как можно больше времени друг с другом!"

            show yoshi excited1 at center
            voice audio.yoshi_vs2_line27b
            yo "Ты прав, Эйден! Мы всегда достаточно близки, но это не значит, что мы не можем сблизиться еще больше!"
        "Ценить каждое мгновение, проведнное всо своей семьей в лагере.":
            $working = True
            $score_goro += 1
            show yoshi happy1 at center
            voice audio.yoshi_vs2_line26c
            yo "Я всегда смотрел далеко в будущее, и не видел, того что находится прямо передо мной - мою семью в Лагере Друзей."

            show goro comp2 at left
            voice audio.goro_vs2_line24a
            g "Я хочу того же."

            voice audio.goro_vs2_line25a
            g "Время проведенное прошлым летом, было хорошим напоминанием о прошлых годах, но теперь у нас есть возможность снова получше узнать друг друга."

            show yoshi relief2 at center
            voice audio.yoshi_vs2_line27c
            yo "Я согласен, сэр...! Для меня нет никого важнее всех вас!"
        "Я заново осознаю, что это место значит для меня.":
            $working = True
            $score_goro += 1
            show yoshi happy1 at center
            voice audio.yoshi_vs2_line26d
            yo "Я хочу заново понять, что на самом деле значит Лагерь Друзей для меня!"

            show goro comp2 at left
            voice audio.goro_vs2_line24b
            g "Это отличная цель, Йошинори. Оглядываясь назад и вспоминая путь по которому мы шли, мы заново осознаем причины, которые направили на на этот путь."

            voice audio.goro_vs2_line25b
            g "Рассчитывай на меня в любой момент на пути к своей цели."

            show yoshi relief2 at center
            voice audio.yoshi_vs2_line27d
            yo "Спасибо, сэр..! Я знаю, что прошлое помогает нам сделать себя лучше в будущем!"

            voice audio.yoshi_vs2_line28d
            yo "И имея таких союзников, как вы парни, я уверен, что достигну своей цели несмотря, ни на что!"
    show aiden tease1 at right
    voice audio.aiden_vs2_line27
    a "Отлично, теперь я убежден что пиво, наконец, ударило тебе в голову."

    voice audio.aiden_vs2_line28
    a "Ты всегда был сентиментальным пьянчугой, Йоши!"

    show yoshi angry2 at center
    voice audio.yoshi_vs2_line29
    yo "Это не так! Я не такой!"

    show goro laugh3 at left
    voice audio.goro_vs2_line26
    g "Ахха, ты слегка покраснел, Йошинори."

    $ renpy.music.stop(channel='music', fadeout = 2.0)
    show yoshi panic3 at center
    voice audio.yoshi_vs2_line30
    yo "Ч-что? Вы тоже так думаете обо мне, сэр Горо?"

    $location = location_entrance
    scene cg3 starrynight with fade
    play music buddy_oath_acoustic loop
    play bgsound sfxloop_night loop
    voice audio.yoshi_vs3_line1
    yo "{i}(Возвращаясь обратно в Лагерь Друзей с Эйденом и сэром Горо, глядя на ночное небо, я вспоминал, связанные с ними приятные воспоминания, о временах, когда я был скаутом.){/i}"

    voice audio.yoshi_vs3_line2
    yo "{i}(Все мы остались в лагере и делали все что могли для его развития по одной и той же причине, но пришло время нам продолжить наши собственные истории.){/i}"

    voice audio.yoshi_vs3_line3
    yo "{i}(Теперь у нас появился еще один замечательный шанс, набраться столько же восхитительных впечатлений, сколько мы уже успели получить раньше!){/i}"

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
