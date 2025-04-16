import pygame
import time
import sys

background_colour = (255,255,255)
(width, height) = (500, 500)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Asteroids")
screen.fill(background_colour)

pygame.display.flip()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

class Character:
    def _init_(self, image, x, y):
        self.image = pygame.image.load(image)
        self.x = x
        self.y = y
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    