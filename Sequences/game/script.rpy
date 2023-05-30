# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define p = Character(_('Паяц'), color="#00ffff")
define cm = Character(_('Сеньор Молтисанти'), color="#8e4c32")
define k1 = Character(_('"Бита"'), color="#ff6600")
define k2 = Character(_('Некто за углом'), color="#ff00ff")
define c = Character(_('Шэрон Фалько'), color="#a3c15f")

# Музыка и звуки
define audio.mus1 = "music/imp#4.ogg"
define audio.mus2 = "music/emptychair.ogg"
define audio.mus3 = "music/raindrops.ogg"
define audio.mus4 = "music/noisegeneratedambient.ogg"
define audio.mus5 = "music/Slow Rush.ogg"
define audio.mus6 = "music/untitled32.ogg"
define audio.mus7 = "music/untitled37.ogg"
define audio.mus8 = "music/untitled17.ogg"
define audio.mus9 = "music/Oyasumi.ogg"


# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.
image bg Jesters = "bg/Jesters.png"
image bg MCday = "bg/MC's aparts day.png"
image bg MCnight = "bg/MC's aparts night.png"
image bg Streetday = "bg/Street view day.png"
image bg Streetnight = "bg/Street view night.png"
image bg Incar1 = "bg/Incar1.png"
image bg Incar2 = "bg/Incar2.png"
image bg GA1 = "bg/Gang aparts 1.png"
image bg GA2 = "bg/Gang aparts 2.png"
image bg GA2b = "bg/Gang aparts 2 blurred.png"
image bg MHday = "bg/Moltisanti's house day.png"
image bg MHnight = "bg/Moltisanti's house night.png"
image bg Hell1 = "bg/Hell1.png"
image bg Hell2 = "bg/Hell2.png"
image bg Hell3 = "bg/Hell3.png"
image bg Hell4 = "bg/Hell4.png"

image Jester1 = "char/Jester1.png"
image Jester2 = "char/Jester2.png"
image Jester3 = "char/Jester3.png"
image Jester4 = "char/Jester4.png"
image Jester5 = "char/Jester5.png"
image Jester6 = "char/Jester6.png"
image Bat1 = "char/Bat1.png"
image Sharon1 = "char/Sharon1.png"
image Sharon2 = "char/Sharon2.png"
image Sharon3 = "char/Sharon3.png"

image Hell_anim:
    "bg/Hell1.png"
    pause 2.0
    "bg/Hell2.png"
    pause 1.0
    "bg/Hell3.png"
    pause 2.0
    "bg/Hell4.png"
    pause 1.0
    repeat

image black = "#000"

#Понг
init python:

    class PongDisplayable(renpy.Displayable):

        def __init__(self):

            renpy.Displayable.__init__(self)

            # The sizes of some of the images.
            self.PADDLE_WIDTH = 12
            self.PADDLE_HEIGHT = 95
            self.PADDLE_X = 240
            self.BALL_WIDTH = 15
            self.BALL_HEIGHT = 15
            self.COURT_TOP = 190
            self.COURT_BOTTOM = 975

            # Some displayables we use.
            self.paddle = Solid("#ffffff", xsize=self.PADDLE_WIDTH, ysize=self.PADDLE_HEIGHT)
            self.ball = Solid("#ffffff", xsize=self.BALL_WIDTH, ysize=self.BALL_HEIGHT)

            # If the ball is stuck to the paddle.
            self.stuck = True

            # The positions of the two paddles.
            self.playery = (self.COURT_BOTTOM - self.COURT_TOP) / 2
            self.computery = self.playery

            # The speed of the computer.
            self.computerspeed = 380.0

            # The position, delta-position, and the speed of the
            # ball.
            self.bx = self.PADDLE_X + self.PADDLE_WIDTH + 10
            self.by = self.playery
            self.bdx = .5
            self.bdy = .5
            self.bspeed = 350.0

            # The time of the past render-frame.
            self.oldst = None

            # The winner.
            self.winner = None

        def visit(self):
            return [ self.paddle, self.ball ]

        # Recomputes the position of the ball, handles bounces, and
        # draws the screen.
        def render(self, width, height, st, at):

            # The Render object we'll be drawing into.
            r = renpy.Render(width, height)

            # Figure out the time elapsed since the previous frame.
            if self.oldst is None:
                self.oldst = st

            dtime = st - self.oldst
            self.oldst = st

            # Figure out where we want to move the ball to.
            speed = dtime * self.bspeed
            oldbx = self.bx

            if self.stuck:
                self.by = self.playery
            else:
                self.bx += self.bdx * speed
                self.by += self.bdy * speed

            # Move the computer's paddle. It wants to go to self.by, but
            # may be limited by it's speed limit.
            cspeed = self.computerspeed * dtime
            if abs(self.by - self.computery) <= cspeed:
                self.computery = self.by
            else:
                self.computery += cspeed * (self.by - self.computery) / abs(self.by - self.computery)

            # Handle bounces.

            # Bounce off of top.
            ball_top = self.COURT_TOP + self.BALL_HEIGHT / 2
            if self.by < ball_top:
                self.by = ball_top + (ball_top - self.by)
                self.bdy = -self.bdy

                if not self.stuck:
                    renpy.sound.play("music/minigames/pong_beep.opus", channel=0)

            # Bounce off bottom.
            ball_bot = self.COURT_BOTTOM - self.BALL_HEIGHT / 2
            if self.by > ball_bot:
                self.by = ball_bot - (self.by - ball_bot)
                self.bdy = -self.bdy

                if not self.stuck:
                    renpy.sound.play("music/minigames/pong_beep.opus", channel=0)

            # This draws a paddle, and checks for bounces.
            def paddle(px, py, hotside):

                # Render the paddle image. We give it an 800x600 area
                # to render into, knowing that images will render smaller.
                # (This isn't the case with all displayables. Solid, Frame,
                # and Fixed will expand to fill the space allotted.)
                # We also pass in st and at.
                pi = renpy.render(self.paddle, width, height, st, at)

                # renpy.render returns a Render object, which we can
                # blit to the Render we're making.
                r.blit(pi, (int(px), int(py - self.PADDLE_HEIGHT / 2)))

                if py - self.PADDLE_HEIGHT / 2 <= self.by <= py + self.PADDLE_HEIGHT / 2:

                    hit = False

                    if oldbx >= hotside >= self.bx:
                        self.bx = hotside + (hotside - self.bx)
                        self.bdx = -self.bdx
                        hit = True

                    elif oldbx <= hotside <= self.bx:
                        self.bx = hotside - (self.bx - hotside)
                        self.bdx = -self.bdx
                        hit = True

                    if hit:
                        renpy.sound.play("music/minigames/pong_boop.opus", channel=1)
                        self.bspeed *= 1.10

            # Draw the two paddles.
            paddle(self.PADDLE_X, self.playery, self.PADDLE_X + self.PADDLE_WIDTH)
            paddle(width - self.PADDLE_X - self.PADDLE_WIDTH, self.computery, width - self.PADDLE_X - self.PADDLE_WIDTH)

            # Draw the ball.
            ball = renpy.render(self.ball, width, height, st, at)
            r.blit(ball, (int(self.bx - self.BALL_WIDTH / 2), int(self.by - self.BALL_HEIGHT / 2)))

            # Check for a winner.
            if self.bx < -50:
                self.winner = "AIwon"

                # Needed to ensure that event is called, noticing
                # the winner.
                renpy.timeout(0)

            elif self.bx > width + 50:
                self.winner = "player"
                renpy.timeout(0)

            # Ask that we be re-rendered ASAP, so we can show the next
            # frame.
            renpy.redraw(self, 0)

            # Return the Render object.
            return r

        # Handles events.
        def event(self, ev, x, y, st):

            import pygame

            # Mousebutton down == start the game by setting stuck to
            # false.
            if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                self.stuck = False

                # Ensure the pong screen updates.
                renpy.restart_interaction()

            # Set the position of the player's paddle.
            y = max(y, self.COURT_TOP)
            y = min(y, self.COURT_BOTTOM)
            self.playery = y

            # If we have a winner, return him or her. Otherwise, ignore
            # the current event.
            if self.winner:
                return self.winner
            else:
                raise renpy.IgnoreEvent()

screen pong():

    default pong = PongDisplayable()

    add "minigames/bgpongfield.png" zoom 1.5

    add pong

    text "Player":
        xpos 240
        xanchor 0.5
        ypos 25
        size 40

    text "AI":
        xpos (1920 - 240)
        xanchor 0.5
        ypos 25
        size 40

    if pong.stuck:
        text "Click to begin.":
            xalign 0.5
            ypos 50
            size 40

label play_pong:

    window hide  # Hide the window and quick menu while in pong
    $ quick_menu = False

    call screen pong

    $ quick_menu = True
    window show

if _return == "AIwon":

    "Я проиграл..."

else:

    "Победа!"
jump pong_selection

label pong_selection:
    menu:
        "Хотите сыграть снова?"

        "Да":
            jump play_pong

        "Нет":
            jump after_game

#Змейка
init python:

    import random
    import pygame

    FPS = 20
    clock = pygame.time.Clock()
    clock.tick(FPS)

    class SnakeDisplayable(renpy.Displayable):

        def __init__(self):

            renpy.Displayable.__init__(self)

            # Set game values
            self.SNAKE_SIZE = 60

            self.score = 0

            # Some displayables we use
            self.snake = Solid("#009933", xsize=self.SNAKE_SIZE, ysize=self.SNAKE_SIZE)
            self.snake_body = Solid("#004d1a", xsize=self.SNAKE_SIZE, ysize=self.SNAKE_SIZE)
            self.apple = Solid("#cc0000", xsize=self.SNAKE_SIZE, ysize=self.SNAKE_SIZE)

            # The positions of the displayables
            self.shx = 1920/2
            self.shy = 1080/2
            self.shdx = 0
            self.shdy = 0
            self.shxmin = 0
            self.shxmax = 1920
            self.shymin = 0
            self.shymax = 1080
            self.key_pressed = False
            self.direction = None

            self.sbxy = []

            self.ax = random.randint(0, 1920 - self.SNAKE_SIZE)
            self.ay = random.randint(0, 1080 - self.SNAKE_SIZE)

            # The time of the past render-frame
            self.oldst = None

            self.lose = False

            return

        # Draws the screen
        def render(self, width, height, st, at):

            # The Render object we'll be drawing into
            r = renpy.Render(width, height)

            # Figure out the time elapsed since the previous frame.
            if self.oldst is None:
                self.oldst = st

            dtime = st - self.oldst
            self.oldst = st

            # This draws the snake
            def snake(shx, shy):

                # Render the snake image
                snake = renpy.render(self.snake, width, height, st, at)

                # renpy.render returns a Render object, which we can
                # blit to the Render we're making
                r.blit(snake, (int(shx), int(shy)))
            
            # This draws the apple
            def snake_body(sbxy):

                # Render the snake body image
                snake_body = renpy.render(self.snake_body, width, height, st, at)

                # renpy.render returns a Render object, which we can
                # blit to the Render we're making
                for body in sbxy:
                    r.blit(snake_body, (int(body[0]), int(body[1])))

            # This draws the apple
            def apple(ax, ay):

                # Render the apple image
                apple = renpy.render(self.apple, width, height, st, at)

                # renpy.render returns a Render object, which we can
                # blit to the Render we're making
                r.blit(apple, (int(ax), int(ay)))

            snake(self.shx, self.shy)
            snake_body(self.sbxy)
            apple(self.ax, self.ay)

            if self.direction == "up":
                self.shdx = 0
                self.shdy = -1 * self.SNAKE_SIZE
            elif self.direction == "down":
                self.shdx = 0
                self.shdy = self.SNAKE_SIZE
            elif self.direction == "left":
                self.shdx = -1 * self.SNAKE_SIZE
                self.shdy = 0
            elif self.direction == "right":
                self.shdx = self.SNAKE_SIZE
                self.shdy = 0

            self.sbxy.insert(0, (self.shx, self.shy))
            self.sbxy.pop()

            # Update the x, y position of the snake's head and make a new coordinate
            self.shx += self.shdx
            self.shy += self.shdy

            # Check for collisions
            def is_colliding(snake, apple):
                return (
                    self.shx <= self.ax + self.SNAKE_SIZE and
                    self.shx + self.SNAKE_SIZE >= self.ax and
                    self.shy <= self.ay + self.SNAKE_SIZE and
                    self.shy + self.SNAKE_SIZE >= self.ay
                )
            
            if is_colliding(snake, apple):
                self.score += 1
                renpy.sound.play("music/minigames/pong_beep.opus")
                self.ax = random.randint(0, 1920 - self.SNAKE_SIZE)
                self.ay = random.randint(0, 1080 - self.SNAKE_SIZE)
                self.sbxy.append((self.shx, self.shy))

            if self.shx < self.shxmin or self.shx + self.SNAKE_SIZE > self.shxmax :

                self.lose = True

                renpy.timeout(0)

            if self.shy < self.shymin or self.shy + self.SNAKE_SIZE > self.shymax:

                self.lose = True

                renpy.timeout(0)
            
            if self.key_pressed and (self.shx, self.shy) in self.sbxy:

                self.lose = True

                renpy.timeout(0)

            # Ask that we be re-rendered ASAP, so we can show the next
            # frame.
            renpy.redraw(self, 0.05)

            # Return the Render object.
            return r

        # Handles events.
        def event(self, ev, x, y, st):
            
            import pygame

            if renpy.map_event(ev, "focus_up") and (self.direction != "down" or self.sbxy == []):
                self.key_pressed = True
                self.direction = "up"
            elif renpy.map_event(ev, "focus_down") and (self.direction != "up" or self.sbxy == []):
                self.key_pressed = True
                self.direction = "down"
            elif renpy.map_event(ev, "focus_left") and (self.direction != "right" or self.sbxy == []):
                self.key_pressed = True
                self.direction = "left"
            elif renpy.map_event(ev, "focus_right") and (self.direction != "left" or self.sbxy == []):
                self.key_pressed = True
                self.direction = "right"
            else:
                self.key_pressed = False

            # Ensure the screen updates.
            renpy.restart_interaction()

            # If the player loses, return it.
            if self.lose:
                return self.lose
            else:
                raise renpy.IgnoreEvent()

    def display_s_score(st, at):
        return Text (_("Score: ") + "%d" % snake.score, size=90, color="#cc0000", outlines=[ (4, "#800000", 0, 0) ]), .1

default snake = SnakeDisplayable()

screen snake():

    add "minigames/bgsnake.png"

    text _("Змейка"):
        xpos 240
        xanchor 0.5
        ypos 25
        size 90
        color "#cc0000"
        outlines [ (4, "#800000", 0, 0) ]
        #font "gui/font/Gallagher.ttf"

    add DynamicDisplayable(display_s_score) xpos (1920 - 240) xanchor 0.5 ypos 25

    add snake

label play_snake:

    window hide  # Hide the window and quick menu while in Feed the Dragon
    $ quick_menu = False
    #hide screen buttons_ui

    #play music "audio/minigames/04.mp3"

    $ snake.lose = False
    $ snake.key_pressed = False
    $ snake.direction = None
    $ snake.score = 0
    $ snake.shx = 1920/2
    $ snake.shy = 1080/2
    $ snake.shdx = 0
    $ snake.shdy = 0
    $ snake.sbxy = []

    call screen snake

    #play music amusement

    #show screen buttons_ui()
    $ quick_menu = True
    window auto

label snake_done:
    "Счёт: [snake.score]"

label snake_selection:
    menu:
        "Хотите сыграть снова?"

        "Да":
            jump play_snake

        "Нет":
            jump after_game

# Игра начинается здесь:
label start:

    scene bg Jesters
    with Dissolve(1.0)

    play music mus1 fadein 10

    show Jester4
    with Dissolve(1.0)

    "Что это?"
    hide Jester4
    show Jester5
    p "Чип это, чувак. Его нужно доставить."
    "За этим ты меня сегодня выдернул?"
    hide Jester5
    show Jester6
    p "Чел, ты всё равно сейчас ничем толком не занят, вот я и подумал, почему бы не подкинуть тебе работку."
    "Может быть, лучше нанять профессионала? Я никогда курьером не работал, ты это знаешь."
    p "Никогда не поздно начать, чувак, никогда не поздно..."
    "Допустим, я соглашусь, но..."
    p "Угу?"
    "С делом ведь наверняка что-то нечисто."
    hide Jester6
    show Jester4
    p "Предположим."
    "В таком случае, мне бы хотелось хотя бы знать кто заказчик."
    p "Ничего не могу сказать, клиент настоял на анонимности."
    "Это тогда просто какой-то анекдот получается. Ты уговариваешь меня подписаться на дело, которое не просто сигнализирует, а орёт о том, что ни под каким предлогом в него не стоит влезать."
    p "Ага. А оплаченный аванс, случаем, не сигнализирует тебе о том, что сомнения излишни?"
    "Большие деньги, конечно, часто сопряжены с немалым риском, но здесь риск слишком велик."
    p "С каких пор это стало для тебя проблемой? Кончай набивать себе цену."
    "Ладно, давай чип этот."
    hide Jester4
    show Jester6
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
    hide Jester6
    show Jester5
    p "Даже на халяву? Приятнее жить с кошмарами? Чел, тебя это не доконало?"
    "Есть в этом что-то притягательное."
    p "Да, чувак... Жесть ты приколист."
    "..."
    hide Jester5
    show Jester6
    p "Это, анекдот хочешь?"
    "Ну?"
    p "Сидят две древние хтонические сущности, погребённые в океане времени..."
    "Слышал уже, не надо."
    hide Jester6
    stop music fadeout 1

    scene bg MCnight
    with dissolve

    play music mus2 fadein 1

    "{color=#888888}{i} После того, как всё полилось на голову Хартовской команде, статус кво изменился на 360, потом ещё на 360, а потом на 180, и всех Хартовских \"пацанов\" окатило помоями, как из ведра.{/i}{/color}"
    "{color=#888888}{i}Кто-то из них было пытался выгрести и уцепиться за какую-нибудь дощечку, кто-то просто вероломно, в панике, бежал с корабля, {/i}{/color}"
    "{color=#888888}{i}но бо́льшая часть вела себя как коты, вынюхавшие пол тазика котовника и выжравшие аналогичную порцию валиума.{/i}{/color}"
    "{color=#888888}{i}Складывалось ощущение, что бо́льшей части команды было плевать на то, что будет дальше, они настолько привыкли контролировать всё, что, потеряв точку опоры, начали биться в конвульсиях и вгрызаться друг другу в глотки.{/i}{/color}"
    "{color=#888888}{i}В какой-то момент, очевидно, им всем предложили пойти на сделку. И что вы думаете?{/i}{/color}"
    "{color=#888888}{i}Не прошло и секунды, как они стали закладывать друг друга, они запели так, будто от этого зависит судьба всего мира, а не их жалкое положение в обществе таких же свиней, как и они сами.{/i}{/color}"
    "{color=#888888}{i}Люди Харта строили всю его предвыборную кампанию на сладостных речах про единство и веру в ближнего, а в итоге немедля сами друг друга же и позакладывали, лживые лицемеры.{/i}{/color}"
    "{color=#888888}{i}Единственной хорошей новостью из Денвера было сообщение о списке всех подозреваемых участников этого дела...{/i}{/color}"
    "{color=#888888}{i}Меня в этом списке не было...{/i}{/color}"
    "{color=#888888}{i}Я испарился в очередной раз.{/i}{/color}"

    "{color=#888888}{i} Вдруг мне вспомнились строчки Леонарда Коэна:{/i}{/color}"
    "{color=#888888}{i}When they poured across the border{/i}{/color}"
    "{color=#888888}{i}I was cautioned to surrender{/i}{/color}"
    "{color=#888888}{i}This I could not do;{/i}{/color}"
    "{color=#888888}{i}I took my gun and vanished{/i}{/color}"
    "{color=#888888}{i}I have changed my name so often...{/i}{/color}"
    "{color=#888888}{i}Не помню, что там было дальше, да и вряд ли следующие строчки относятся ко мне. Было очевидно, что \"война\" проиграна и я \"перешёл границу\" снова.{/i}{/color}"
    "{color=#888888}{i}Система имеет слепые зоны, и кто я такой, чтобы этим не пользоваться. Мне совсем не нужно быть испачканным в политическом скандале.{/i}{/color}"
    "{color=#888888}{i}Я этого не хочу, тем более сам скандал не мал, хоть и не ужасен — о нём вскоре забудут.{/i}{/color}"
    "{color=#888888}{i}Этот скандал, достаточно большой, чтобы его обсуждала вся страна, но недостаточно, чтобы этим заинтересовалась PANGAEA, лишь способ растормошить народ.{/i}{/color}"
    "{color=#888888}{i}Говорят, что сегодня ночью Бюро собирается обнародовать восстановленные с Фаррелловского компьютера данные.{/i}{/color}"
    "{color=#888888}{i}Бедный Исак Фаррелл, хоть стоит признать, что он был хорошим бухгалтером, не знал, что данные недостаточно просто \"удалить\".{/i}{/color}"
    "{color=#888888}{i}Их нужно было снести напрочь, а так он сделал большой подарок Бюро, которое дополнительно навесило на него статью за сокрытие улик.{/i}{/color}"
    "{color=#888888}{i}Хотя, вряд ли ему сейчас вообще есть до этого дело — мёртвые не нервничают.{/i}{/color}"
    "{color=#888888}{i}К утру коридоры конгресса будут залиты кровью — это неизбежно, такие дела не остаются безнаказанными и в миг бесследно не забываются.{/i}{/color}"
    "{color=#888888}{i}Впрочем, к чёрту политику, меня сейчас интересует другое: чип, переданный Паяцем. Что это вообще и зачем он нужен? На себе я его испытать не могу ввиду отсутствия у самого наномашин, значит придется как-то догадываться самому.{/i}{/color}"
    "{color=#888888}{i}Вдруг я ненароком поднёс чип к виску.{/i}{/color}"
    scene black
    with Dissolve(1.0)
    "{color=#888888}{i}Что произошло после этого?{/i}{/color}"
    
    show Hell_anim
    play sound "music/sfx2.ogg" fadein 2.0
    with Dissolve(15.0)
    "{size=+100}{color=#888888}{i}Я увидел АД.{/i}{/color}"
    stop sound
    stop music
    hide Hell_anim

    jump cycle1
    return

label cycle1:

    scene bg MCday
    play music mus3 fadein 5
    with Dissolve(5.0)

    "{color=#888888}{i} Проснувшись утром, я заметил множественные следствия проникновения в мои апартаменты: разбросанные вещи, разбитую технику и так далее."
    "{color=#888888}{i}В целом, всё было ясно, ночью ко мне вломился какой-то идиот. Зачем? Видимо, с целью украсть чип. Готов поставить на то, что чип сейчас либо у него, либо в ближайшем к нему ломбарде."
    "{color=#888888}{i}Посмотрев затем зорким глазом видео с камер, я заметил, что идиот, а идиот он оттого, что его стиль работы явно любительский и даже не предполагает планирование, "
    "{color=#888888}{i}влез ко мне не в одиночку, он был в компании своих друзей-идиотов. Все они были в масках, но какой от них толк, если ты идиот и даже не допускаешь возможность того, что на тебя смогут выйти через имплант."

    "{color=#888888}{i}Для этого мне нужен Паяц."
    stop music fadeout 1

    play music mus4 fadein 5
    scene bg Jesters
    show Jester2

    p"	Опять ты, чувак?	"
    "	Хочешь услышать анекдот?	"
    p"	А он смешной?	"
    "	Обоссышься...	"
    p"	...	"
    "	Чип украли.	"
    hide Jester2
    show Jester1
    p"	Что-то мне не смешно.	"
    "	А я и не говорил, что будет смешно.	"
    p"	Если груз не будет доставлен, то нам конец.	"
    "	Выкрутимся.	"
    p"	Нет, ты меня немного неправильно понял: конец это тот, который с большой буквы П.	"
    "	А...	"
    p"	Что \"А\"? Думай, давай.	"
    "	А... А, я просто думаю, как ты так ловко сумел мне всё обосрать.	"
    hide Jester1
    show Jester2
    p"	Всё должно было пройти проще, более гладко и более быстро: ты должен был взять чип, отдать его и получить деньги в этот же день, одна нога здесь, другая там. План был прост.	"
    "	Только какой толк от его простоты? Да, план элементарен и что? Будто от этого он становится надёжным?	"
    p"	Так точно. План прост, потому и красив. Если план слишком сложен, то всё может пойти наперекосяк.	"
    "	Так, чёрт побери, всё и пошло наперекосяк, Паяц, с этим твоим простым планом! Уверен, что всё правильно спланировал?! А?!"
    "  К тому же, \"Одна нога здесь, другая там\" знаешь когда такое бывает?"
    "Когда кто-то наступает на мину и на ней подрывается, а мы сейчас вступили огромную в кучу дерьма, которая вот-вот рванёт, да не просто вступили, а залезли в неё по уши."
    "Как тебе такое положение, Паяц, нравится?	"
    hide Jester2
    show Jester1
    p"	Так или иначе, я не мог отказаться от этого предложения.	"
    "	Вот значит, как...	"
    p"	Ко мне пришёл некто, от него несло смертью. Он положил чип на стол и сказал передать Частицу Бога, так он назвал чип, некоему мистеру Молтисанти."
    p"Сам не знаю, почему он выбрал тебя в качестве курьера.	"
    "	Зато я, кажется, догадываюсь почему.	"
    hide Jester2
    show Jester3
    p"	Расскажи...	"
    "	Во мне нет имплантов.	"
    hide Jester3
    show Jester2
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
    "	Насчёт \"мистера Молтисанти\": он имел ввиду Серхио Молтисанти. Итало-мексиканец, участвует в предвыборной гонке, вероятно хочет воспользоваться подвернувшимся ему шансом."
    "Хотя, кто после такого масштабного скандала не хочет? Харт отлетел и больше к нам не вернётся, самое время рвать, пока не проснулись остальные.	"
    p"	Окей, но, чувак, чем ему может быть полезен чип в предвыборной гонке?	"
    "	Хрен его знает. Предположу, что это следствие того, что Серхио предельно религиозный политик. Может быть, он и вправду верит во всю эту байду, что несёт с трибун, кто знает?"
    "Так или иначе, вряд ли ему по какой-то другой причине понадобилось нечто, названное Частицей Бога.	"
    p"	...	"
    "	Давай к делу, пробей этих взломщиков-любителей, пока нам трындец не наступил.	"
    hide Jester2
    show Jester3
    p"	Уже, чувак.	"
    "	Рассказывай тогда. Кто они? Уличная банда?	"
    p"	Ага, \"Карапузы\".	"
    "	Лажа какая-то, не пойму... Это они так сами себя назвали?	"
    hide Jester3
    show Jester2
    p"	Наверное. Только, ты, чувак, на их название не смотри, они тебя в два счета размотают, имплантов-то у тебя совсем нет, как оказалось."
    p"Что ты с ними делать будешь?	"
    "	С этим я уж как-нибудь разберусь.	"
    stop music fadeout 1

    scene black
    with Dissolve(1.0)
    "{color=#888888}{i} Что делать? Я же ведь совсем не хочу, чтобы из моего языка сделали колумбийский галстук."
    scene bg Streetday
    play music mus5 fadein 5
    with Dissolve(1.0)
    "{color=#888888}{i} Самой обсуждаемой новостью сегодня было сообщение об аварии, в которую попал Харт. Бюро обнародовало переписки, чеки и всю чёрную бухгалтерию Фаррелла."
    "{color=#888888}{i}Там даже для меня нашлись сюрпризы, я вот, например, не знал, что Харт в течении двадцати лет продвигал в разные компании своих людей."
    "{color=#888888}{i}Что происходило дальше, думаю, объяснять не имеет смысла, больше этих компаний нет."
    "{color=#888888}{i}Видимо, осознавая неотвратимость надвигающейся лавины, Харт употребил весь свой арсенал стимуляторов, и, пожалуй, алкоголь был из них самым безобидным."
    "{color=#888888}{i}Когда эффект от применения стимуляторов ударил ему в голову, он въехал в столб"
    "{color=#888888}{i}Вскоре Харт уйдет с президентского поста. Да, он сделал немало хорошего в течение своего срока."
    "{color=#888888}{i}Но запомнят его именно за это, даже не за Денвергейт, так журналисты назвали этот скандал, а за этот нелепый случай пьяного вождения"
    scene bg Incar1
    with Dissolve(1.0)
    "{color=#888888}{i} Пока я размышлял, чёрный автомобиль перегородил мне дорогу. Открылась дверь, а за ней виднелась рука."
    cm"Присаживайтесь."
    "Я сейчас сильно занят, не могу."
    cm"Я настаиваю."
    "Ладно."
    scene bg Incar2
    with Dissolve(1.0)
    cm"Меня интересует статус груза, посылки, которую вы мне должны доставить. Она у вас?"
    "Прямо сейчас — нет..."
    cm"..."
    "Но мне её уже передали."
    cm"Доставите посылку сегодня. До вечера."

    scene bg Streetday
    with Dissolve(1.0)

    "{color=#888888}{i} Визит заказчика меня не обрадовал."
    "{color=#888888}{i}Ещё больше самого факта визита меня тревожила его заинтересованность в получении чипа, это уже не похоже на влияние только религиозности, за его намерениями кроется что-то ещё."
    "{color=#888888}{i}Позвонив одному своему знакомому, я выяснил, что Молтисанти снял свою кандидатуру и решил не принимать участие в выборах."
    "{color=#888888}{i}Знание этого натолкнуло меня на тревожные мысли. Я знал, что Молтисанти раньше работал на PANGAEA, знал, что у него есть множество друзей в Африке, а также много денег, и, что самое главное, доступ к оружию."
    "{color=#888888}{i}После 2045-го он занимался \"коллекционированием\" оружия. Когда война закончилась и PANGAEA всех разом прижала, развитые страны начали сливать оружие буквально за копейки."
    "{color=#888888}{i}Этим и воспользовался Серхио, затарив всё, что плохо лежало, себе на многочисленные склады, которые он арендовал прямо у PANGAEA."
    "{color=#888888}{i}В PANGAEA либо не замечали этого, либо предпочитали закрывать на это глаза, ссылаясь на то, что Серхио, простой мексиканский спекулянт, который скупает оружие по всему миру и продаёт Африке."
    "{color=#888888}{i}До дня сегодняшнего я тоже так думал."
    "{color=#888888}{i}Боюсь, я был неправ."

    stop music fadeout 1
    scene bg GA1
    play music mus6 fadein 5
    with Dissolve(1.0)

    "{color=#888888}{i} Дверь в апартаменты была открыта, даже взламывать не пришлось. Апартаменты пусть и нельзя было назвать притоном, всё же впечатление жилья представителей среднего класса они не вызывали."
    "{color=#888888}{i}Место дурное и пахло здесь противно, мне хотелось поскорее уйти..."
    "{color=#888888}{i}Но вдруг я обнаружил труп, труп совсем недавно был главарём банды идиотов, то-есть Карапузов, если я правильно понял, а рядом с трупом лежал чип. Тот самый чип."
    "{color=#888888}{i}Ничего не понимаю... Это цирк какой-то..."

    scene bg GA2
    with Dissolve(1.0)

    k1"Опача, ты кто, мужик? Кем будешь?"
    show Bat1
    with Dissolve(1.0)
    "{i}...а вот и клоуны."
    "Я, детки, потерпевший."
    k2"Гы, терпила, значит. Чё надо?"
    "Да так, мне бы просто чип забрать."
    k1"Ты не обнаглел часом?"
    "Я просто чип заберу. Хорошо? Не будте гнидами."
    k1"Да я тя щас замочу, дядь!"
    "{color=#888888}{i} Я всё же рискнул взять чип, за неимением альтернатив."
    "{color=#888888}{i} Выражение лиц клоунов сменилось в моменте с агрессивно-угрожающего на растерянно-нелепое."
    k1"С-стой, мужик. Давай без обид, л-ладно?"
    "Что?"
    scene bg GA1
    with Dissolve(1.0)
    "{color=#888888}{i} И тут я понял, почему труп стал трупом."
    "{color=#888888}{i}Видимо, когда главарь банды идиотов дотронулся голыми руками до чипа — его конвертировало в кадавра, зажмурило, убило короче."
    "{color=#888888}{i}И вот теперь они выпученными глазами наблюдают за тем, как я держу чип. Не знаю, о чём они сейчас думают, но явно не о том, как его отобрать."
    "{color=#888888}{i} Всё складывается замечательно."

    scene bg GA2
    show Bat1
    with Dissolve(1.0)
    "Зачем чип украли?"
    k1"Мы, это, подумали: \"Раз лежит, то почему бы не взять\". В металлолом, типа, его сдать хотели."
    "Ну, пацаны, я смотрю, вы умны не по годам. Вас, кстати, в детстве арматурой по голове били?"
    k1"Чё? Какой арматурой?"
    "Да вот, просто смотрю на вас и понимаю, что естественный отбор больше не работает."
    k1"..."
    "Я пойду?"
    k1"Да-да, и-иди-иди."

    scene black
    stop music fadeout 1
    with Dissolve(1.0)
    "{color=#888888}{i} Чип при мне, моя главная задача на данный момент — не посеять его."

    scene bg Streetnight
    play music mus7 fadein 5
    with Dissolve(1.0)

    "{color=#888888}{i} Мне назначили встречу на поздний вечер, именно тогда я должен буду передать чип."
    "{color=#888888}{i}Ничего сложного: передам чип — получу деньги, а затем смоюсь куда подальше, мне всё это надоело."
    "{color=#888888}{i}Молтисанти определённо использует этот чип в своих интересах, несмотря на возможные ужасные последствия, но я не собираюсь в это вмешиваться, не моё это дело"
    "{color=#888888}{i}Я просто курьер, меня наняли для того, чтобы я выполнил работу."
    "{color=#888888}{i}Время ожидания будет тянуться невыносимо долго, нужно себя занять чем-нибудь на ближайшие часы, чтобы дурные мысли не напрягали. К счастью, я сейчас в наиболее подходящем для убийства времени месте."
    
    menu:
        "Во что хотите сыграть?"

        "Понг":
            jump play_pong
        "Змейка":
            jump play_snake
        "Не хочу играть":
            jump after_game

label after_game:

    scene bg MHnight
    play music mus8 fadein 5
    with Dissolve(1.0)

    "{color=#888888}{i} Чудом я умудрился не потерять чип. Теперь дело за малым — отдать устройство заказчику и забыть этот день как страшный сон."
    
    show Sharon1
    with Dissolve(1.0)
    
    "Здравствуйте, мне нужно к мистеру Молтисанти, для него есть посылка. Вы, наверное, его экономка..."
    hide Sharon1
    show Sharon3
    c"Секретарша."
    hide Sharon3
    show Sharon1
    "Вы бы не могли проводить меня к нему или хотя бы сообщить о моем прибытии?"
    c"Увы, но это невозможно. Господин Молтисанти... скончался прямо перед вашим приходом."
    "{color=#888888}{i} Интересно. Неужели это значит, что с меня снимается обязательство по доставке чипа?"
    hide Sharon1
    show Sharon2
    c"Вы что-то говорили про посылку. Это ценная вещь?"

    menu:
        "Сказать правду":
            jump say1
        "Скрыть правду":
            jump say2
    
label say1:
    "Ага... чип."
    c"Вы  можете отдать его мне."
    "{color=#888888}{i} Больно она подозрительная."
    hide Sharon2
    show Sharon1
    "Извините, но нет."
    jump cycle1_ending

label say2:
    "Да нет, просто мелочёвка, расходники."
    hide Sharon2
    show Sharon1
    c"Вы уверены, что при вас нет ничего ценного? Может вам чего-то не сказали?"
    "{color=#888888}{i} Больно она подозрительная."
    "Нет, это просто расходники."
    c"..."
    jump cycle1_ending

label cycle1_ending:
    "Посылка должна вручаться лично заказчику. Но поскольку заказчик скончался, как вы сказали, посылку придется отправить обратно. Еще раз, соболезную."
    "{color=#888888}{i} Ну, умер и умер, нет — так нет. Видно, не судьба отдать чип, тогда оставлю его себе, а дальше как-нибудь решу, что с ним делать."
    "{color=#888888}{i}Раз заказчик мертв, то никто не будет меня преследовать из-за этого долбанного чипа. Нет обязательств, можно спать спокойно"

    scene bg MCnight
    play music mus9 fadein 5
    with Dissolve(1.0)

    "{color=#888888}{i} Секретарша вела себя подозрительно, но, с другой стороны, Молтисанти был немолод, это должно было когда-нибудь случиться. Так или иначе, это не моё дело, я не должен об этом беспокоиться."
    "{color=#888888}{i}Сообщив Паяцу о намерениях уехать ненадолго, я начал собирать немногочисленные вещи, которые хотел перевезти в Европу."
    "{color=#888888}{i}Да, у меня есть квартира в восточной Европе, её я когда-то давно выиграл в споре у одного румына, не совсем честно выиграл, но тем не менее."
    "{color=#888888}{i} Составляя план досуга, я просидел до ночи, а затем провалился в сон."


    return
