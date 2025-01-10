import sys
import pygame
from pygame.locals import *
from time import sleep
from random import random, choice
import cmath
 
# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()
 
# create the display surface object
# of specific dimension.
window = pygame.display.set_mode((600, 400))

p1_y = 175
p2_y = 175

ball_x = 300
ball_y = 200
speed = cmath.rect(0.7, random() * 10 / 180 * cmath.pi * choice((-1, 1)))

running = True

while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            continue

    # Fill the scree with white color
    window.fill((0, 0, 0))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        p1_y -= 1
    if keys[pygame.K_d]:
        p1_y += 1
    if keys[pygame.K_RIGHT]:
        p2_y += 1
    if keys[pygame.K_LEFT]:
        p2_y -= 1
    
    # Using draw.rect module of
    # pygame to draw the outlined rectangle
    player1 = pygame.draw.rect(window, (255, 255, 255), 
                            [10, p1_y, 10, 50], 2)
    player2 = pygame.draw.rect(window, (255, 255, 255), 
                            [580, p2_y, 10, 50], 2)
    
    if 579 < ball_x < 581:
        if p2_y + 25 - 25 < ball_y < p2_y + 25 + 25:
            t = cmath.polar(speed)
            speed = cmath.rect(t[0], cmath.pi - t[1])
        else:
            #TODO Punkt Spieler 1
            pass
    if 19 < ball_x < 21:
        if p1_y + 25 - 25 < ball_y < p1_y + 25 + 25:
            t = cmath.polar(speed)
            speed = cmath.rect(t[0], cmath.pi - t[1])
        else:
            #TODO Punkt Spieler 1
            pass
    if ball_y < 10:
        t = cmath.polar(speed)
        speed = cmath.rect(t[0], -t[1])
    
    if ball_y > 590:
        t = cmath.polar(speed)
        speed = cmath.rect(t[0], -t[1])

    ball_x += speed.real
    ball_y += speed.imag
    ball = pygame.draw.circle(window, (255, 255, 255),
                            [ball_x, ball_y], 6, 2)

    # Draws the surface object to the screen.
    pygame.display.update()
    sleep(1/250)
    