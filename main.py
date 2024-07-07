import pygame
import random
import os
import pygame.mixer
from pygame.locals import *
x=pygame.init()
pygame.mixer.init()
clock=pygame.time.Clock()
music=pygame.mixer.Sound('snake_music.mp3')
hiss=pygame.mixer.Sound('hiss3-103123.mp3')
gom=pygame.mixer.Sound('mixkit-arcade-fast-game-over-233.wav')
#colors
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)
font=pygame.font.SysFont(None,55)

# creating window
screenwidth=900
screenheight=600
gamewindow=pygame.display.set_mode((screenwidth,screenheight))
pygame.display.set_caption("snake game by pranay")

def text_screen(text,color,x,y):
    screen_text=font.render(text,True,color)
    gamewindow.blit(screen_text,[x,y])

def plot_snake(gameWindow,color,snake_list,snake_size):
    for x,y in snake_list:
        # pygame.draw.rect(gameWindow,color,[x,y,snake_size,snake_size])
        pygame.draw.circle(gamewindow,(0,150,0),(x,y),13,0)
def welcome():
    exit_game=False
    while not exit_game:
        gamewindow.fill(white)
        gamewindow.fill((150,200,156))
        text_screen("welcome to snake game",(100,100,100),200,250)
        text_screen("press enter to play ",(0,0,255),250,300)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit_game=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RETURN:
                    gameloop()
        pygame.display.update()
        clock.tick(60)
#creating a game loop
def gameloop():
    pygame.mixer.music.load('snake_music.mp3')
    pygame.mixer.music.play()
# creating game specific variables
    if (not os.path.exists("hiscore.txt")):
        with open("hiscore.txt","w") as f:
            f.write("0")
    with open("hiscore.txt","r") as f:
        hiscore=f.read()
    exit_game=False
    game_over=False
    snake_x=45
    snake_y=55
    velocity_x=0
    velocity_y=0
    init_velocity=5
    food_x=random.randint(20,screenwidth//2)
    food_y=random.randint(20,screenheight//2)
    score=0
    snake_size=30
    fps=60
    snake_list=[]
    snake_length=1
    while not exit_game:
        if score>int(hiscore):
                hiscore=score
        if game_over:
            with open("hiscore.txt","w") as f:
                f.write(str(hiscore))
            gamewindow.fill((55,155,255))
            text_screen("Game over!",red,300,200)
            pygame.mixer.music.load('mixkit-arcade-fast-game-over-233.wav')
            pygame.mixer.music.play()
            text_screen(" Press enter to continue",(40,50,60),200,300)

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        gameloop()
                        # gameloop()
        else:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT:
                        velocity_x=init_velocity
                        velocity_y=0
                    if event.key==pygame.K_LEFT:
                        velocity_x=-init_velocity
                        velocity_y=0
                    if event.key==pygame.K_UP:
                        velocity_y=-init_velocity
                        velocity_x=0
                    if event.key==pygame.K_DOWN:
                        velocity_y=init_velocity
                        velocity_x=0

            snake_x=snake_x+velocity_x
            snake_y=snake_y+velocity_y

            if abs(snake_x-food_x) < 30 and abs(snake_y-food_y) <30 :
                pygame.mixer.Sound.play(hiss)
                score+=10
                food_x=random.randint(20,screenwidth//2)
                food_y=random.randint(20,screenheight//2)
                snake_length+=5
                
            

            gamewindow.fill((0,50,0))
            text_screen("score "+str(score),red,5,5)
            text_screen("Hiscore"+str(hiscore),(0,0,255),250,5)
            pygame.draw.circle(gamewindow,(255,255,255),(food_x,food_y,),13,0)

            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if len(snake_list)>snake_length:
                del snake_list[0]
            
            if head in snake_list[:-1]:
                game_over=True
                pygame.mixer.Sound.play(gom)
            if snake_x<0 or snake_x>screenwidth or snake_y<0 or snake_y>screenheight:
                pygame.mixer.music.load('mixkit-arcade-fast-game-over-233.wav')
                pygame.mixer.music.play()
                game_over=True
            # pygame.draw.rect(gamewindow,(0,100,0),[snake_x,snake_y,snake_size,snake_size])
            pygame.draw.circle(gamewindow,(255,255,255),(food_x,food_y,),1,0)
            
            plot_snake(gamewindow,(0,100,0),snake_list,snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
welcome()
