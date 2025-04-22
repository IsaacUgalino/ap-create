import pygame
import time
import sys

background_colour = (0,0,0)
(width, height) = (500, 500)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Asteroids")
screen.fill(background_colour)

pygame.display.flip()

#player icon
player_image = pygame.image.load("spaceship.png").convert_alpha() #convert alpha makes image transparent 
player_rect = player_image.get_rect() #gets rectangle area of image
player_rect.center = (width // 2, height // 2) #centers box on screen
player_speed = 6

clock = pygame.time.Clock()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #Key controls
    keys = pygame.get_pressed()
    if keys[pygame.K_w]: #move up
        player_rect.w -= player_speed
    if keys[pygame.K_s]:
        [player_rect.s] += player_speed
    if keys[pygame.K_a]:
        player_rect.a -= player_speed
    if keys[pygame.K_d]:
        player_rect.d += player_speed
