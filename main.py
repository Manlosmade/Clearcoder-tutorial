import pygame
from sys import exit
pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("PYGAME RUNNER")
clock = pygame.time.Clock()
font = pygame.font.Font('font/Pixeltype.ttf', 50)


skySurface = pygame.image.load('graphics/Sky.png').convert_alpha()
groundSurface = pygame.image.load('graphics/Ground.png').convert_alpha()
scoreSurface = font.render('Score: ', False, 'Black').convert_alpha()


snailSurface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
playerSurface = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()

playerCollision = playerSurface.get_rect(midbottom = (80,300))
snailCollision = snailSurface.get_rect(midbottom = (700, 300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    
    screen.blit(skySurface,(0,0))
    screen.blit(groundSurface,(0,300))
    screen.blit(scoreSurface,(300,50))
    screen.blit(snailSurface, snailCollision)
    screen.blit(playerSurface, playerCollision)
    
    snailCollision.x -= 1
    if snailCollision.right <= 0:
        snailCollision.left = 800
    pygame.display.update()
    clock.tick(120)