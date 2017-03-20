import pygame
import random
import sys

window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Black Jack")




class Cards:

    def __init__(self, xpos, ypos, filename):
        self.x = xpos
        self.y = ypos
        self.bitmap = pygame.image.load(filename)

    def render(self):
        gameScreen.blit(self.bitmap, (self.x, self.y))





'''     Инициализация заполнение и перемешивание колоды        Инициализация заполнение и перемешивание колоды      '''

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

random.shuffle(cardDesk)
random.shuffle(cardDesk)
random.shuffle(cardDesk)






''' Присваивание карты     Присваивание карты     Присваивание карты     Присваивание карты     Присваивание карты '''

def cardInitialize(card, position):

    xPos = 0
    yPos = 0
    if position == 'g1':
        xPos = 370
        yPos = 280
    elif position == 'g2':
        xPos = 390
        yPos = 280
    elif position == 'd1':
        xPos = 350
        yPos = 100
    elif position == 'd2':
        xPos = 410
        yPos = 100

    if card[0] == '2':
        if card[1] == 'c':
            card = Cards(xPos, yPos, "Images\Cards\\2c.png")
        elif card[1] == 'd':
            card = Cards(xPos, yPos, "Images\Cards\\2d.png")
        elif card[1] == 'h':
            card = Cards(xPos, yPos, "Images\Cards\\2h.png")
        else:
            card = Cards(xPos, yPos, "Images\Cards\\2s.png")
    elif card[0] == '3':
        if card[1] == 'c':
            card = Cards(xPos, yPos, "Images\Cards\\3c.png")
        elif card[1] == 'd':
            card = Cards(xPos, yPos, "Images\Cards\\3d.png")
        elif card[1] == 'h':
            card = Cards(xPos, yPos, "Images\Cards\\3h.png")
        else:
            card = Cards(xPos, yPos, "Images\Cards\\3s.png")
    elif card[0] == '4':
        if card[1] == 'c':
            card = Cards(xPos, yPos, "Images\Cards\\4c.png")
        elif card[1] == 'd':
            card = Cards(xPos, yPos, "Images\Cards\\4d.png")
        elif card[1] == 'h':
            card = Cards(xPos, yPos, "Images\Cards\\4h.png")
        else:
            card = Cards(xPos, yPos, "Images\Cards\\4s.png")
    elif card[0] == '5':
        if card[1] == 'c':
            card = Cards(xPos, yPos, "Images\Cards\\5c.png")
        elif card[1] == 'd':
            card = Cards(xPos, yPos, "Images\Cards\\5d.png")
        elif card[1] == 'h':
            card = Cards(xPos, yPos, "Images\Cards\\5h.png")
        else:
            card = Cards(xPos, yPos, "Images\Cards\\5s.png")
    elif card[0] == '6':
        if card[1] == 'c':
            card = Cards(xPos, yPos, "Images\Cards\\6c.png")
        elif card[1] == 'd':
            card = Cards(xPos, yPos, "Images\Cards\\6d.png")
        elif card[1] == 'h':
            card = Cards(xPos, yPos, "Images\Cards\\6h.png")
        else:
            card = Cards(xPos, yPos, "Images\Cards\\6s.png")
    elif card[0] == '7':
        if card[1] == 'c':
            card = Cards(xPos, yPos, "Images\Cards\\7c.png")
        elif card[1] == 'd':
            card = Cards(xPos, yPos, "Images\Cards\\7d.png")
        elif card[1] == 'h':
            card = Cards(xPos, yPos, "Images\Cards\\7h.png")
        else:
            card = Cards(xPos, yPos, "Images\Cards\\7s.png")
    elif card[0] == '8':
        if card[1] == 'c':
            card = Cards(xPos, yPos, "Images\Cards\\8c.png")
        elif card[1] == 'd':
            card = Cards(xPos, yPos, "Images\Cards\\8d.png")
        elif card[1] == 'h':
            card = Cards(xPos, yPos, "Images\Cards\\8h.png")
        else:
            card = Cards(xPos, yPos, "Images\Cards\\8s.png")
    elif card[0] == '9':
        if card[1] == 'c':
            card = Cards(xPos, yPos, "Images\Cards\\9c.png")
        elif card[1] == 'd':
            card = Cards(xPos, yPos, "Images\Cards\\9d.png")
        elif card[1] == 'h':
            card = Cards(xPos, yPos, "Images\Cards\\9h.png")
        else:
            card = Cards(xPos, yPos, "Images\Cards\\9s.png")
    elif card[0] == '10':
        if card[1] == 'c':
            card = Cards(xPos, yPos, "Images\Cards\\10c.png")
        elif card[1] == 'd':
            card = Cards(xPos, yPos, "Images\Cards\\10d.png")
        elif card[1] == 'h':
            card = Cards(xPos, yPos, "Images\Cards\\10h.png")
        else:
            card = Cards(xPos, yPos, "Images\Cards\\10s.png")
    elif card[0] == 'J':
        if card[1] == 'c':
            card = Cards(xPos, yPos, "Images\Cards\\Jc.png")
        elif card[1] == 'd':
            card = Cards(xPos, yPos, "Images\Cards\\Jd.png")
        elif card[1] == 'h':
            card = Cards(xPos, yPos, "Images\Cards\\Jh.png")
        else:
            card = Cards(xPos, yPos, "Images\Cards\\Js.png")
    elif card[0] == 'Q':
        if card[1] == 'c':
            card = Cards(xPos, yPos, "Images\Cards\\Qc.png")
        elif card[1] == 'd':
            card = Cards(xPos, yPos, "Images\Cards\\Qd.png")
        elif card[1] == 'h':
            card = Cards(xPos, yPos, "Images\Cards\\Qh.png")
        else:
            card = Cards(xPos, yPos, "Images\Cards\\Qs.png")
    elif card[0] == 'K':
        if card[1] == 'c':
            card = Cards(xPos, yPos, "Images\Cards\\Kc.png")
        elif card[1] == 'd':
            card = Cards(xPos, yPos, "Images\Cards\\Kd.png")
        elif card[1] == 'h':
            card = Cards(xPos, yPos, "Images\Cards\\Kh.png")
        else:
            card = Cards(xPos, yPos, "Images\Cards\\Ks.png")
    else:
        if card[1] == 'c':
            card = Cards(xPos, yPos, "Images\Cards\\Ac.png")
        elif card[1] == 'd':
            card = Cards(xPos, yPos, "Images\Cards\\Ad.png")
        elif card[1] == 'h':
            card = Cards(xPos, yPos, "Images\Cards\\Ah.png")
        else:
            card = Cards(xPos, yPos, "Images\Cards\\As.png")

    return card








gameScreen = pygame.Surface((800, 600))

gamerCard1 = Cards(800, 600, "Images\Cards\Back.png")
gamerCard2 = Cards(800, 600, "Images\Cards\Back.png")
gamerCard3 = Cards(800, 600, "Images\Cards\Back.png")
gamerCard4 = Cards(800, 600, "Images\Cards\Back.png")
gamerCard5 = Cards(800, 600, "Images\Cards\Back.png")

dealerCard1 = Cards(800, 600, "Images\Cards\Back.png")
dealerCard2 = Cards(800, 600, "Images\Cards\Back.png")
dealerCard3 = Cards(800, 600, "Images\Cards\Back.png")
dealerCard4 = Cards(800, 600, "Images\Cards\Back.png")
dealerCard5 = Cards(800, 600, "Images\Cards\Back.png")

cardCount = 0
cardCountInParty = -1

while True:

    if cardCount > deskSize * 4 and cardCountInParty == -1:
        random.shuffle(cardDesk)
        random.shuffle(cardDesk)
        random.shuffle(cardDesk)
        cardCount = 0

    gameScreen.blit(pygame.image.load("Images\Backgrounds\game screen.png"), (0, 0))

    if cardCountInParty == 0:
        gamerCard1 = cardInitialize(cardDesk[cardCount], 'g1')
        cardCount += 1
        dealerCard1 = cardInitialize(cardDesk[cardCount], 'd1')
        cardCount += 1
        gamerCard2 = cardInitialize(cardDesk[cardCount], 'g2')
        cardCount += 1
        dealerCard2 = cardInitialize(cardDesk[cardCount], 'd2')
        cardCount += 1
        cardCountInParty = 4

    gamerCard1.render()
    dealerCard1.render()
    gamerCard2.render()
    dealerCard2.render()

    for i in pygame.event.get():

        if i.type == pygame.QUIT:
            sys.exit()

        if i.type == pygame.KEYDOWN and i.key == pygame.K_SPACE:
            cardCountInParty = 0

        if i.type == pygame.KEYDOWN and i.key == pygame.K_ESCAPE:
            cardCountInParty = -1

    window.blit(gameScreen, (0, 0))
    pygame.display.flip()
