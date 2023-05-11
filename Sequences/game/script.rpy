﻿# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define p = Character('Паяц', color="#c8ffc8")
define cm = Character('Сеньор Молтисанти', color="#c8ffc8")
define k1 = Character('Идиот 1', color="#c8ffc8")
define k2 = Character('Идиот 2', color="#c8ffc8")
define c = Character('Шэрон Фалько', color="#c8ffc8")

# Музыка и звуки
define audio.mus1 = "music/imp#4.ogg"
define audio.mus2 = "music/emptychair.ogg"


# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:

    scene подвал Паяца 1

    play music mus1 fadein 10

    show Паяц

    "Что это?"
    p "Чип это, чувак. Его нужно доставить."
    "За этим ты меня сегодня выдернул?"
    p "Чел, ты всё равно сейчас ничем толком не занят, вот я и подумал, почему бы не подкинуть тебе работку."
    "Может быть, лучше нанять профессионала. Я никогда курьером не работал, ты это знаешь."
    p "Никогда не поздно начать, чувак, никогда не поздно..."
    "Допустим, я соглашусь, но..."
    p "Угу?"
    "С делом ведь наверняка что-то нечисто."
    p "Предположим."
    "В таком случае, мне бы хотелось хотя бы знать кто заказчик."
    p "Ничего не могу сказать, клиент настоял на анонимности."
    "Это тогда просто какой-то анекдот получается. Ты уговариваешь меня подписаться на дело, которое не просто сигнализирует, а орёт о том, что ни под каким предлогом в него не стоит влезать."
    p "Ага. А оплаченный аванс, случаем, не сигнализирует тебе о том, что сомнения излишни?"
    "Большие деньги, конечно, часто сопряжены с немалым риском, но здесь риск слишком велик."
    p "С каких пор это стало для тебя проблемой? Кончай набивать себе цену."
    "Ладно, давай чип этот."
    p "Во! Это уже другой разговор."
    "Но мне всё один вопрос покоя не даёт."
    p "Какой вопрос?"
    "Почему из всего разнообразия он выбрал меня? Как он вообще на меня вышел? Почему он поручил это мне?"
    p "Ты лис, старый лис, может поэтому? Мало тех, кто бы мог так просто уходить от неприятностей. Уж не знаю, что за импланты у тебя стоят, но я ни о чём подобном больше не слышал. Кстати, про импланты, кошмары всё ещё мучают?"
    "Порой."
    p "Странно, наномашины должны это подавлять."
    "Ну..."
    p "Давай я тогда это поправлю."
    "Не надо."
    p "Даже на халяву? Приятнее жить с кошмарами? Чел, тебя это не доконало?"
    "Есть в этом что-то притягательное."
    p "Да, чувак... Жесть ты приколист."
    "..."
    p "Это, анекдот хочешь?"
    "Ну?"
    p "Сидят две древние хтонические сущности, погребённые в океане времени..."
    "Слышал уже, не надо."

    stop music fadeout 1

    scene апартаменты ГГ 2

    play music mus2 fadein 1

    "После того, как всё полилось на голову Хартовской команде, статус кво изменился на 360, потом ещё на 360, а потом на 180, и всех Хартовских \"пацанов\" окатило помоями, как из ведра."
    "Кто-то из них было пытался выгрести и уцепиться за какую-нибудь дощечку, кто-то просто вероломно, в панике, бежал с корабля, но бо́льшая часть вела себя как коты, вынюхавшие пол тазика котовника и выжравшие аналогичную порцию валиума."
    "Складывалось ощущение, что бо́льшей части команды было плевать на то, что будет дальше, они настолько привыкли контролировать всё, что, потеряв точку опоры, начали биться в конвульсиях и вгрызаться друг другу в глотки."
    "В какой-то момент, очевидно, им всем предложили пойти на сделку. И что вы думаете?"
    "Не прошло и секунды, как они стали закладывать друг друга, они запели так, будто от этого зависит судьба всего мира, а не их жалкое положение в обществе таких же свиней, как и они сами."
    "Люди Харта строили всю его предвыборную кампанию на сладостных речах про единство и веру в ближнего, а в итоге немедля сами друг друга же и позакладывали, лживые лицемеры."
    "Единственной хорошей новостью из Денвера было сообщение о списке всех подозреваемых участников этого дела... Меня в этом списке не было... Я испарился в очередной раз."

    "Вдруг мне вспомнились строчки Леонарда Коэна:"
    "When they poured across the border"
    "I was cautioned to surrender"
    "This I could not do;"
    "I took my gun and vanished"
    "I have changed my name so often..."
    "Не помню, что там было дальше, да и вряд ли следующие строчки относятся ко мне. Было очевидно, что \"война\" проиграна и я \"перешёл границу\" снова."
    "Система имеет слепые зоны, и кто я такой, чтобы этим не пользоваться. Мне совсем не нужно быть испачканным в политическом скандале."
    "Я этого не хочу, тем более сам скандал не мал, хоть и не ужасен — о нём вскоре забудут."
    "Этот скандал, достаточно большой, чтобы его обсуждала вся страна, но недостаточно, чтобы этим заинтересовалась PANGAEA, лишь способ растормошить народ."
    "Говорят, что сегодня ночью Бюро собирается обнародовать восстановленные с Фаррелловского компьютера данные."
    "Бедный Исак Фаррелл, хоть стоит признать, что он был хорошим бухгалтером, не знал, что данные недостаточно просто \"удалить\"."
    "Их нужно было снести напрочь, а так он сделал большой подарок Бюро, которое дополнительно навесило на него статью за сокрытие улик."
    "Хотя, вряд ли ему сейчас вообще есть до этого дело — мёртвые не нервничают."
    "К утру коридоры конгресса будут залиты кровью — это неизбежно, такие дела не остаются безнаказанными и в миг бесследно не забываются."
    "Впрочем, к чёрту политику, меня сейчас интересует другое: чип, переданный Паяцем. Что это вообще и зачем он нужен? На себе я его испытать не могу ввиду отсутствия у самого наномашин, значит придется как-то догадываться самому."
    "Вдруг я ненароком поднёс чип к виску."
    "Что произошло после этого?"
    "Я увидел АД."

    stop music fadeout 1

    jump cycle1
    return

label cycle1:

    "Проснувшись утром, я заметил множественные следствия проникновения в мои апартаменты: разбросанные вещи, разбитую технику и так далее."
    "В целом, всё было ясно, ночью ко мне вломился какой-то идиот. Зачем? Видимо, с целью украсть чип. Готов поставить на то, что чип сейчас либо у него, либо в ближайшем к нему ломбарде."
    "Посмотрев затем зорким глазом видео с камер, я заметил, что идиот, а идиот он оттого, что его стиль работы явно любительский и даже не предполагает планирование, "
    "влез ко мне не в одиночку, он был в компании своих друзей-идиотов. Все они были в масках, но какой от них толк, если ты идиот и даже не допускаешь возможность того, что на тебя смогут выйти через имплант."

    "Для этого мне нужен Паяц."

    scene подвал Паяца 1
    show Паяц

    p"	Опять ты, чувак?	"
    "	Хочешь услышать анекдот?	"
    p"	А он смешной?	"
    "	Обоссышься...	"
    p"	...	"
    "	Чип украли.	"
    p"	Что-то мне не смешно.	"
    "	А я и не говорил, что будет смешно.	"
    p"	Если груз не будет доставлен, то нам конец.	"
    "	Выкрутимся.	"
    p"	Нет, ты меня немного неправильно понял: конец это тот, который с большой буквы П.	"
    "	А...	"
    p"	Что \"А\"? Думай, давай.	"
    "	А... А, я просто думаю, как ты так ловко сумел мне всё обосрать.	"
    p"	Всё должно было пройти проще, более гладко и более быстро: ты должен был взять чип, отдать его и получить деньги в этот же день, одна нога здесь, другая там. План был прост.	"
    "	Только какой толк от его простоты? Да, план элементарен и что? Будто от этого он становится надёжным?	"
    p"	Так точно. План прост, потому и красив. Если план слишком сложен, то всё может пойти наперекосяк.	"
    "	Так, чёрт побери, всё и пошло наперекосяк, Паяц, с этим твоим простым планом! Уверен, что всё правильно спланировал?! А?!"
    "  К тому же, \"Одна нога здесь, другая там\" знаешь когда такое бывает?"
    "Когда кто-то наступает на мину и на ней подрывается, а мы сейчас вступили огромную в кучу дерьма, которая вот-вот рванёт, да не просто вступили, а залезли в неё по уши."
    "Как тебе такое положение, Паяц, нравится?	"
    p"	Так или иначе, я не мог отказаться от этого предложения.	"
    "	Вот значит, как...	"
    p"	Ко мне пришёл некто, от него несло смертью. Он положил чип на стол и сказал передать Частицу Бога, так он назвал чип, некоему мистеру Молтисанти."
    p"Сам не знаю, почему он выбрал тебя в качестве курьера.	"
    "	Зато я, кажется, догадываюсь почему.	"
    p"	Расскажи...	"
    "	Во мне нет имплантов.	"
    p"	Ладно-ладно, достал меня порядком твой надменный сарказм.	"
    "	Я серьёзно. Наномашин в моей крови тоже нет.	"
    p"	Этого быть не может. Не верю.	"
    "	Я уколов боюсь... Наномашины вводились всем через иглу, вместе с медикаментами, так?"
    "А я всегда от инъекций косил. Ты не представляешь, насколько изобретательным нужно быть, насколько нужно напрягать мозг, чтобы каждый раз находить отмазки.	"
    p"	То-есть ты хочешь сказать, что ты полностью невидим для системы из-за боязни уколов? Почему ты раньше об этом не говорил?	"
    "	Не видел в этом смысла.	"
    p"	А теперь видишь?	"
    "	А теперь мы в жопе, Паяц, и я активно ищу из неё выход.	"
    p"	...	"
    "	Насчёт \"мистера Молтисанти\": он имел ввиду Серхио Молтисанти. Итало-мексиканец, участвует в предвыборной компании, вероятно хочет воспользоваться подвернувшимся ему шансом."
    "Хотя, кто после такого масштабного скандала не хочет? Харт отлетел и больше к нам не вернётся, самое время рвать, пока не проснулись остальные.	"
    p"	Окей, но, чувак, чем ему может быть полезен чип в предвыборной гонке?	"
    "	Хрен его знает. Предположу, что это следствие того, что Серхио предельно религиозный политик. Может быть, он и вправду верит во всю эту байду, что несёт с трибун, кто знает?"
    "Так или иначе, вряд ли ему по какой-то другой причине понадобилось нечто, названное Частицей Бога.	"
    p"	...	"
    "	Давай к делу, пробей этих взломщиков-любителей, пока нам трындец не наступил.	"
    p"	Уже, чувак.	"
    "	Рассказывай тогда. Кто они? Уличная банда?	"
    p"	Ага, \"Карапузы\".	"
    "	Лажа какая-то, не пойму... Это они так сами себя назвали?	"
    p"	Наверное. Только, ты, чувак, на их название не смотри, они тебя в два счета размотают, имплантов-то у тебя совсем нет, как оказалось."
    p"Что ты с ними делать будешь?	"
    "	С этим я уж как-нибудь разберусь.	"

    scene улица 3

    "Что делать? Я же ведь совсем не хочу, чтобы из моего языка сделали колумбийский галстук."
    "Самой обсуждаемой новостью сегодня было сообщение об аварии, в которую попал Харт. Бюро обнародовало переписки, чеки и всю чёрную бухгалтерию Фаррелла."
    "Там даже для меня нашлись сюрпризы, я вот, например, не знал, что Харт в течении двадцати лет продвигал в разные компании своих людей."
    "Что происходило дальше, думаю, объяснять не имеет смысла, больше этих компаний нет."
    "Видимо, осознавая неотвратимость надвигающейся лавины, Харт употребил весь свой арсенал стимуляторов, и, пожалуй, алкоголь был из них самым безобидным."
    "Когда эффект от применения стимуляторов ударил ему в голову, он въехал в столб"
    "Вскоре Харт уйдет с президентского поста. Да, он сделал немало хорошего в течение своего срока."
    "Но запомнят его именно за это, даже не за Денвергейт, так журналисты назвали этот скандал, а за этот нелепый случай пьяного вождения"
    "Пока я размышлял, чёрный автомобиль перегородил мне дорогу. Открылась дверь, а за ней виднелась рука."

    scene машина 7

    cm"Присаживайтесь."
    "Я сейчас сильно занят, не могу."
    cm"Я настаиваю."
    "Ладно."
    cm"Меня интересует статус груза, посылки, которую вы мне должны доставить. Она у вас?"
    "Прямо сейчас — нет..."
    cm"..."
    "Но мне её уже передали."
    cm"Доставите посылку сегодня. До вечера."

    scene улица 3

    "Визит заказчика меня не обрадовал."
    "Ещё больше самого факта визита меня тревожила его заинтересованность в получении чипа, это уже не похоже на влияние только религиозности, за его намерениями кроется что-то ещё."
    "Позвонив одному своему знакомому, я выяснил, что Молтисанти снял свою кандидатуру и решил не принимать участие в выборах."
    "Знание этого натолкнуло меня на тревожные мысли. Я знал, что Молтисанти раньше работал на PANGAEA, знал, что у него есть множество друзей в Африке, а также много денег, и, что самое главное, доступ к оружию."
    "После 2045-го он занимался \"коллекционированием\" оружия. Когда война закончилась и PANGAEA всех разом прижала, развитые страны начали сливать оружие буквально за копейки."
    "Этим и воспользовался Серхио, затарив всё, что плохо лежало, себе на многочисленные склады, которые он арендовал прямо у PANGAEA."
    "В PANGAEA либо не замечали этого, либо предпочитали закрывать на это глаза, ссылаясь на то, что Серхио, простой мексиканский спекулянт, который скупает оружие по всему миру и продаёт Африке."
    "До дня сегодняшнего я тоже так думал."
    "Боюсь, я был неправ."

    scene апартаменты банды 4

    "Дверь в апартаменты была открыта, даже взламывать не пришлось. Апартаменты пусть и нельзя было назвать притоном, всё же впечатление жилья представителей среднего класса они не вызывали."
    "Место дурное и пахло здесь противно, мне хотелось поскорее уйти..."
    "Но вдруг я обнаружил труп, труп совсем недавно был главарём банды идиотов, то-есть Карапузов, если я правильно понял, а рядом с трупом лежал чип. Тот самый чип."
    "Ничего не понимаю... Это цирк какой-то..."

    k1"Опача, ты кто, мужик? Кем будешь?"
    "...а вот и клоуны."
    "Я, детки, потерпевший."
    k2"Гы, терпила, значит. Чё надо?"
    "Да так, мне бы просто чип забрать."
    k2"Ты не обнаглел часом?"
    "Я просто чип заберу. Хорошо? Не будте гнидами."
    k2"Да я тя щас замочу, дядь!"
    "Я всё же рискнул взять чип, за неимением альтернатив."
    "Выражение лиц клоунов сменилось в моменте с агрессивно-угрожающего на растерянно-нелепое."
    k1"С-стой, мужик. Давай без обид, л-ладно?"
    "Что?"
    "И тут я понял, почему труп стал трупом."
    "Видимо, когда главарь банды идиотов дотронулся голыми руками до чипа — его конвертировало в кадавра, зажмурило, убило короче."
    "И вот теперь они выпученными глазами наблюдают за тем, как я держу чип. Не знаю, о чём они сейчас думают, но явно не о том, как его отобрать."
    "Всё складывается замечательно."

    "Зачем чип украли?"
    k1"Мы, это, подумали: \"Раз лежит, то почему бы не взять\". В металлолом, типа, его сдать хотели."
    "Ну, пацаны, я смотрю, вы умны не по годам. Вас, кстати, в детстве арматурой по голове били?"
    k1"Чё? Какой арматурой?"
    "Да вот, просто смотрю на вас и понимаю, что естественный отбор больше не работает."
    k1"..."
    "Я пойду?"
    k1"Да-да, и-иди-иди."
    "Чип при мне, моя главная задача на данный момент — не посеять его."

    scene Торговая улица 5

    "Мне назначили встречу на поздний вечер, именно тогда я должен буду передать чип."
    "Ничего сложного: передам чип — получу деньги, а затем смоюсь куда подальше, мне всё это надоело."
    "Молтисанти определённо использует этот чип в своих интересах, несмотря на возможные ужасные последствия, но я не собираюсь в это вмешиваться, не моё это дело"
    "Я просто курьер, меня наняли для того, чтобы я выполнил работу."
    "Время ожидания будет тянуться невыносимо долго, нужно себя занять чем-нибудь на ближайшие часы, чтобы дурные мысли не напрягали. К счастью, я сейчас в наиболее подходящем для убийства времени месте."
    "*Тут должна быть возможность сыграть в мини-игру*"

    scene дом заказчика 7

    "Чудом я умудрился не потерять чип. Теперь дело за малым — отдать устройство заказчику и забыть этот день как страшный сон."
    "Здравствуйте, мне нужно к мистеру Молтисанти, для него есть посылка. Вы, наверное, его экономка..."
    c"Секретарша."
    "Вы бы не могли проводить меня к нему или хотя бы сообщить о моем прибытии?"
    c"Увы, но это невозможно. Господин Молтисанти... скончался прямо перед вашим приходом."
    "Интересно. Неужели это значит, что с меня снимается обязательство по доставке чипа?"
    c"Вы что-то говорили про посылку. Это ценная вещь?"

    "*Сюда можно вставить варианты выбора*"

    "Да нет, просто мелочёвка, расходники."
    c"Вы уверены, что при вас нет ничего ценного? Может вам чего-то не сказали?"
    "Больно она подозрительная."
    "Нет, это просто расходники."
    c"..."
    "Посылка должна вручаться лично заказчику. Но поскольку заказчик скончался, как вы сказали, посылку придется отправить обратно. Еще раз, соболезную."
    "Ну, умер и умер, нет — так нет. Видно, не судьба отдать чип, тогда оставлю его себе, а дальше как-нибудь решу, что с ним делать."
    "Раз заказчик мертв, то никто не будет меня преследовать из-за этого долбанного чипа. Нет обязательств, можно спать спокойно"

    scene апартаменты ГГ 2

    "Секретарша вела себя подозрительно, но, с другой стороны, Молтисанти был немолод, это должно было когда-нибудь случиться. Так или иначе, это не моё дело, я не должен об этом беспокоиться."
    "Сообщив Паяцу о намерениях уехать ненадолго, я начал собирать немногочисленные вещи, которые хотел перевезти в Европу."
    "Да, у меня есть квартира в восточной Европе, её я когда-то давно выиграл в споре у одного румына, не совсем честно выиграл, но тем не менее."
    "Составляя план досуга, я просидел до ночи, а затем провалился в сон."

    "Конец первого цикла"

    return
