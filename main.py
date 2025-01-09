import sys
import pygame
from pygame.locals import *
from time import sleep
 
# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()
 
# create the display surface object
# of specific dimension.
window = pygame.display.set_mode((600, 400))

p1_y = 175
p2_y = 175

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
        p1_y -= 10
    if keys[pygame.K_d]:
        p1_y += 10
    if keys[pygame.K_RIGHT]:
        p2_y += 10
    if keys[pygame.K_LEFT]:
        p2_y -= 10
    
    # Using draw.rect module of
    # pygame to draw the outlined rectangle
    player1 = pygame.draw.rect(window, (255, 255, 255), 
                            [10, p1_y, 10, 50], 2)
    player2 = pygame.draw.rect(window, (255, 255, 255), 
                            [580, p2_y, 10, 50], 2)

    ball = pygame.draw.circle(window, (255, 255, 255),
                            [300, 200], 6, 2)

    # Draws the surface object to the screen.
    pygame.display.update()
    sleep(1/50)
    