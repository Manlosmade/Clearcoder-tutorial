import pygame
from sys import exit
pygame.init()
screen = pygame.display.set_mode((1200,600))
pygame.display.set_caption("PYGAME RUNNER")
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    # draw all out elements and update everything
    pygame.display.update()
    clock.tick(60)