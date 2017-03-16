import pygame
import random
import sys

window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Black Jack")

deskSize = 52
cardDesk = []
suit = ['D', 'H', 'S', 'C']
suitNumber = 0
cardNumber = 2
for i in range(deskSize):
    cardDesk.append([cardNumber])
    cardDesk[i].append(suit[suitNumber])
    cardNumber += 1
    if cardNumber == 15:
        suitNumber += 1
        cardNumber = 2

cardDesk *= 3
deskSize *= 3

random.shuffle(cardDesk)

for i in range(deskSize):
    print(i + 1, cardDesk[i])

gameScreen = pygame.Surface((800, 600))

while True:

    gameScreen.blit(pygame.image.load("Images\Backgrounds\game screen.bmp"), (0, 0))

    for i in pygame.event.get():

        if i.type == pygame.QUIT:
            sys.exit()

    window.blit(gameScreen, (0, 0))
    pygame.display.flip()
