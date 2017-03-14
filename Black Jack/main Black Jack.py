import pygame
import sys

window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Black Jack")

gameScreen = pygame.Surface((800, 600))

while True:

    gameScreen.blit(pygame.image.load("Images\Backgrounds\game screen.bmp"), (0, 0))

    for i in pygame.event.get():

        if i.type == pygame.QUIT:
            sys.exit()

    window.blit(gameScreen, (0, 0))
    pygame.display.flip()
