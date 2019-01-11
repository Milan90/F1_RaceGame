import pygame
import time
import random

pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
obstacle_color = (11, 22, 33)

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("F1 Race Game")

clock = pygame.time.Clock()

carImg = pygame.image.load('racecar.png')

car_width = 73


def obstacles(obstacleX, obstacleY, obstacleW, obstacleH, color):
    pygame.draw.rect(gameDisplay, color, [obstacleX, obstacleY, obstacleW, obstacleH])


def car(x, y):
    gameDisplay.blit(carImg, (x, y))


def text_objects(text, font):
    textSurface = font.render(text, True, red)
    return textSurface, textSurface.get_rect()


def obstacles_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: " + str(count), True, red)
    gameDisplay.blit(text, (0, 0))


def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 100)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()


def crash():
    message_display('You crashed')


def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.75)
    x_change = 0

    obstacle_startx = random.randrange(0, display_width)
    obstacle_starty = -100
    obstacle_speed = 7
    obstacle_width = 100
    obstacle_heigth = 100
    dodged = 0
    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -15
                elif event.key == pygame.K_RIGHT:
                    x_change = 15

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or pygame.K_LEFT:
                    x_change = 0

        x += x_change

        gameDisplay.fill(white)

        obstacles(obstacle_startx, obstacle_starty, obstacle_width, obstacle_heigth, obstacle_color)
        obstacle_starty += obstacle_speed
        car(x, y)
        obstacles_dodged(dodged)

        if x > display_width - car_width or x < 0:
            crash()

        if obstacle_starty > display_height:
            obstacle_starty = 0 - obstacle_heigth
            obstacle_startx = random.randrange(0, display_width)
            dodged += 1
            obstacle_speed += 1
            obstacle_width += (dodged * 1.1)

        if y < obstacle_starty + obstacle_heigth:

            if x > obstacle_startx and x < obstacle_startx + obstacle_width \
                    or x + car_width > obstacle_startx \
                    and x + car_width < obstacle_startx + obstacle_width:
                crash()

        pygame.display.update()
        clock.tick(60)


game_loop()
pygame.quit()
quit()
