import pygame
import random
import os

# Initialize pygame
pygame.init()

# Set up display
screenwidth = 900
screenheight = 600
gamewindow = pygame.display.set_mode((screenwidth, screenheight))
pygame.display.set_caption("Snake Game by Pranay")

# Fonts and Colors
font = pygame.font.SysFont(None, 55)
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

# Load Sounds
snake_music = pygame.mixer.Sound('webcluster/snake_music.mp3')
hiss = pygame.mixer.Sound('webcluster/hiss3-103123.mp3')
game_over_music = pygame.mixer.Sound('webcluster/mixkit-arcade-fast-game-over-233.wav')

# Function to display text on screen
def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gamewindow.blit(screen_text, [x, y])

# Function to draw snake
def plot_snake(gameWindow, color, snake_list, snake_size):
    for x, y in snake_list:
        pygame.draw.circle(gameWindow, (0, 150, 0), (x, y), 13, 0)

# Welcome screen function
def welcome():
    exit_game = False
    while not exit_game:
        gamewindow.fill(white)
        text_screen("Welcome to Snake Game", (100, 100, 100), 200, 250)
        text_screen("Press Enter to Play", (0, 0, 255), 250, 300)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    gameloop()

# Main game loop
def gameloop():
    # Play background music
    snake_music.play()

    # Game variables
    if not os.path.exists("hiscore.txt"):
        with open("hiscore.txt", "w") as f:
            f.write("0")
    with open("hiscore.txt", "r") as f:
        hiscore = int(f.read())

    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    init_velocity = 5
    food_x = random.randint(20, screenwidth // 2)
    food_y = random.randint(20, screenheight // 2)
    score = 0
    snake_size = 30
    fps = 60
    snake_list = []
    snake_length = 1

    while not exit_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    velocity_x = init_velocity
                    velocity_y = 0
                if event.key == pygame.K_LEFT:
                    velocity_x = -init_velocity
                    velocity_y = 0
                if event.key == pygame.K_UP:
                    velocity_y = -init_velocity
                    velocity_x = 0
                if event.key == pygame.K_DOWN:
                    velocity_y = init_velocity
                    velocity_x = 0

        snake_x += velocity_x
        snake_y += velocity_y

        if abs(snake_x - food_x) < 30 and abs(snake_y - food_y) < 30:
            score += 10
            food_x = random.randint(20, screenwidth // 2)
            food_y = random.randint(20, screenheight // 2)
            snake_length += 5

        gamewindow.fill((0, 50, 0))
        text_screen("Score: " + str(score), red, 5, 5)
        text_screen("High Score: " + str(hiscore), (0, 0, 255), 250, 5)
        pygame.draw.circle(gamewindow, (255, 255, 255), (food_x, food_y), 13, 0)

        head = []
        head.append(snake_x)
        head.append(snake_y)
        snake_list.append(head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        if head in snake_list[:-1]:
            game_over = True

        if snake_x < 0 or snake_x > screenwidth or snake_y < 0 or snake_y > screenheight:
            game_over = True

        plot_snake(gamewindow, (0, 100, 0), snake_list, snake_size)

        pygame.display.update()
        clock.tick(fps)

    # Game over screen
    game_over_music.play()
    text_screen("Game Over!", red, 300, 200)
    text_screen("Press Enter to Continue", (40, 50, 60), 200, 300)
    pygame.display.update()

    while game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
                game_over = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    gameloop()

    pygame.quit()
    quit()