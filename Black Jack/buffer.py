import pygame
import sys

window = pygame.display.set_mode((800, 600))

gameScreen = pygame.Surface((800, 600))

class Cards:
    def __init__(self, xpos, ypos, filename):
        self.x = xpos
        self.y = ypos
        self.bitmap = pygame.image.load(filename)
        self.bitmap.set_colorkey((255, 255, 255))

    def render(self):
        gameScreen.blit(self.bitmap, (self.x, self.y))

gamerCard1 = Cards(100, 100, "Images\Cards\clear.bmp")

while True:

    gameScreen.blit(pygame.image.load("Images\Backgrounds\game screen.png"), (0, 0))
    gamerCard1.render()

    for i in pygame.event.get():

        if i.type == pygame.QUIT:
            sys.exit()

        window.blit(gameScreen, (0, 0))
        pygame.display.flip()