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

deskSize = 52
cardDesk = []
suit = ['c', 'd', 'h', 's']
suitNumber = 0
cardNumber = 2

for i in range(deskSize):

    if cardNumber < 11:
        cardDesk.append([str(cardNumber)])
    elif cardNumber == 11:
        cardDesk.append(['J'])
    elif cardNumber == 12:
        cardDesk.append(['O'])
    elif cardNumber == 13:
        cardDesk.append(['K'])
    else:
        cardDesk.append(['A'])

    cardDesk[i].append(suit[suitNumber])
    cardNumber += 1

    if cardNumber == 15:
        suitNumber += 1
        cardNumber = 2

cardDesk *= 6
deskSize *= 6

i = 0
cardName = cardDesk[i][0] + cardDesk[i][1] + '.png'
print(cardName)
cardName = 'Button.png'
print(cardName)

gamerCard1 = Cards(100, 100, "Images\Buttons\\" + cardName)

while True:

    gameScreen.blit(pygame.image.load("Images\Backgrounds\game screen.png"), (0, 0))
    gamerCard1.render()

    for i in pygame.event.get():

        if i.type == pygame.QUIT:
            sys.exit()

        window.blit(gameScreen, (0, 0))
        pygame.display.flip()