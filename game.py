import pygame
import random
import os

pygame.init()
pygame.mixer.init()

game_display = pygame.display.set_mode((600, 500))
pygame.display.set_caption('This is my game')
font = pygame.font.SysFont(None, 40)

bg = pygame.image.load("snakes.jpg")
bg = pygame.transform.scale(bg,(600,500)).convert_alpha()
bg2 = pygame.image.load("welcomescreen.png")
bg2 = pygame.transform.scale(bg2,(600,500)).convert_alpha()
bg3 = pygame.image.load("game over.jpg")
bg3 = pygame.transform.scale(bg3,(600,500)).convert_alpha()

def txt_screen(text, color , x ,y):
    screen_text = font.render(text, True, color)
    game_display.blit(screen_text, [x,y])

def plot_snake(game_display, black, snk_list , snake_size_x):
    for x,y in snk_list:
        pygame.draw.rect(game_display, black, [x,y, snake_size_x, snake_size_x])

def welcome():
    working = True
    while working:
        game_display.blit(bg2,(0,0))
        txt_screen("Welcome to snakes", [255, 0, 0], 150,200 )
        txt_screen("Press Space to Start", [255, 0, 0], 150,250)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                working = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load("game.mp3")
                    pygame.mixer.music.play()
                    game_loop()

        pygame.display.update()
        clock.tick(30)

clock = pygame.time.Clock()
def game_loop():
    fps = 40
    working = True
    snk_list = []
    snk_length = 1
    red = [255, 0, 0]
    black = [0, 0, 0]
    white = [255, 255, 255]
    snake_x = 290
    snake_y = 250
    snake_size_x = 15
    vel_x = 0
    vel_y = 0
    food_x = random.randint(0, 500)
    food_y = random.randint(0, 400)
    score = 0
    game_over = False

    if(not os.path.exists("hiscore.txt")):
        with open("hiscore.txt","w") as f:
            f.write("0")
    with open ("hiscore.txt", "r")as f:
        high_score = f.read()


    while working:
        if game_over:
            with open("hiscore.txt", "w")as f:
                f.write(str(high_score))

            game_display.blit(bg3, (0, 0))
            txt_screen("GAME OVER , PRESS ENTER TO CONTINUE", white ,5,250)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    working = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    working = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:

                        vel_x = 4
                        vel_y = 0
                    if event.key == pygame.K_LEFT:
                        vel_x = -4
                        vel_y = 0

                    if event.key == pygame.K_UP:
                        vel_y = -4
                        vel_x = 0

                    if event.key == pygame.K_DOWN:
                        vel_y = +4
                        vel_x = 0

            snake_x += vel_x
            snake_y += vel_y

            game_display.blit(bg,(0,0))

            if abs(snake_x-food_x)<10 and abs(snake_y-food_y)<10:
                score +=1
                food_x = random.randint(0, 600)
                food_y = random.randint(0, 500)
                snk_length+=4
                if score>int(high_score):
                    high_score = score
            txt_screen("Score:" + str(score) +"   High score:" +str(high_score), black, 5, 4)

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            pygame.draw.rect(game_display, red, [food_x, food_y, 15, 15])
            plot_snake(game_display, black, snk_list, snake_size_x)

            if len(snk_list)>snk_length:
                del snk_list[0]
            if snake_x<0 or snake_y<0 or snake_x>600 or snake_y>500:
                game_over = True
                pygame.mixer.music.load("game2.mp3")
                pygame.mixer.music.play()
            if head in snk_list[:-1]:
                game_over = True
                pygame.mixer.music.load("game2.mp3")
                pygame.mixer.music.play()
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
welcome()