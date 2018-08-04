import pygame
import random
import time
#1 Initialize
pygame.init()
pygame.display.set_caption("Pong Game")
#2 Set up game window
def game(a, b):
    sentences = ["Hay l¾m gi¸o s­. Quit mÑ game ®i ",
                 "GG noob 3k trash.",
                 "Putang inamo, cyka blyat.",
                 "Giê sao!!!"]
    index_sentecnces = random.randint(0,3)
    SIZE = (600, 600)

    BG_COLOR = (1, 1, 1) # google color picker
    label_color = (255,255,255)

    canvas = pygame.display.set_mode(SIZE) # to giay ve

    clock = pygame.time.Clock()

    paddle_image = pygame.image.load("assets/paddle.png") # load anh
    ball_image = pygame.image.load("assets/ball.png")

    loop = True

    x1 = 0
    x2 = 570

    ball_x = random.randint(275,325)
    ball_y = random.randint(275,325)

    xn = random.choice([-1, 1])
    yn = random.choice([-1, 1])

    vx = random.randint(4,7)
    vy = random.randint(2,5)
    v = (vx ** 2 + vy ** 2)

    while  (vx ** 2 + vy ** 2) <= 33 and (vx ** 2 + vy ** 2) >= 40 :
        vx = random.randint(4,7)
        vy = random.randint(2,5)

    ball_v_x = xn * vx
    ball_v_y = yn * vy

    y1 = ball_y + ball_v_y * 50
    y2 = ball_y + ball_v_y * 50

    l_score = a
    r_score = b

    w_pressed = False
    s_pressed = False
    up_pressed = False
    down_pressed = False

    display_text = True

    while loop:
        # pooling, check xem nguoi dung lam gi
        events = pygame.event.get() # lay ra hanh dong nguoi dung, de vao list
        for e in events: # duyet tung phan tu trong event

            if e.type == pygame.QUIT:
                loop = False # action = thoat game


            elif e.type == pygame.KEYDOWN: # nhan xuong ( keyup nha ra)
                if e.key == pygame.K_w: # chu y toa do x, y
                    w_pressed = True
                elif e.key == pygame.K_s:
                    s_pressed = True

                if e.key == pygame.K_UP:  # chu y toa do x, y
                    up_pressed = True
                elif e.key == pygame.K_DOWN:
                    down_pressed = True


            elif e.type == pygame.KEYUP:
                if e.key == pygame.K_w:
                    w_pressed = False
                elif e.key == pygame.K_s:
                    s_pressed = False

                if e.key == pygame.K_UP:
                    up_pressed = False
                elif e.key == pygame.K_DOWN:
                    down_pressed = False

        if w_pressed:
            if v >= 35:
                y1 -= 10
            else:
                y1 -= 5
            if y1 < 0:
                y1 = 0
        if s_pressed:
            if v >= 35:
                y1 += 10
            else:
                y1 += 5
            if y1 > 480:
                y1 = 480

        if up_pressed:
            if v >= 35:
                y2 -= 10
            else:
                y2 -= 5
            if y2 < 0:
                y2 = 0
        if down_pressed:
            if v >= 35:
                y2 += 10
            else:
                y2 += 5
            if y2 > 480:
                y2 = 480

        ball_x += ball_v_x
        ball_y += ball_v_y
        #cong thuc event action
        # if ball_x >= 580 or ball_x <= 0:
        #     ball_v_x = - ball_v_x
        if ball_y >= 580 or ball_y <= 0:

            ball_v_y = - ball_v_y

        if ((x2 -20 - ball_v_x) <= ball_x <= (x2 - 20  + ball_v_x )) and (y2 - 20 <= ball_y <= (y2 + 20 +120)):

            ball_v_x = - ball_v_x


        if ((x1 + 30 - 3) <= ball_x <= (x1 + 30 + 3)) and (y1 - 20 <= ball_y <= (y1 + 20 + 120)):
            ball_v_x = - ball_v_x

        if (ball_x >= 600 ):
            loop  = False
            a += 1
            game(a, b)

        if (ball_x <= 0):
            loop  = False
            b += 1
            game(a, b)
            #doi chieu v


        canvas.fill(BG_COLOR)

        canvas.blit(paddle_image, (x1, y1))
        canvas.blit(paddle_image, (x2, y2))
        canvas.blit(ball_image, (ball_x, ball_y))

        myfont1 = pygame.font.SysFont("Comic Sans MS", 20)

        label1 = myfont1.render("Score " + str(l_score), 1, (255, 255, 255))
        canvas.blit(label1, (50, 20))

        label2 = myfont1.render("Score " + str(r_score), 1, (255, 255, 255))
        canvas.blit(label2, (470, 20))

        myfont3 = pygame.font.SysFont("Vn.Arial", 40)
        label3 = myfont3.render(sentences[index_sentecnces],1, label_color)
        start_time = int(time.strftime("%S"))
        canvas.blit(label3, (50, 300))
        while display_text:

            if not display_text:
                display_text = True
                start_time = int(time.strftime("%S"))

            else:
                if int(time.strftime("%S")) - start_time > 0.5:
                    display_text = False



        clock.tick(120)

        pygame.display.flip()

game(0, 0)
