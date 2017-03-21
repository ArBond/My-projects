import pygame
import sys
import random

window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Black Jack")


class Cards:

    def __init__(self, xpos, ypos, filename):
        self.x = xpos
        self.y = ypos
        self.bitmap = pygame.image.load(filename)

    def render(self):
        gameScreen.blit(self.bitmap, (self.x, self.y))


class Buttons:

    def __init__(self, xpos, ypos, filename):
        self.x = xpos
        self.y = ypos
        self.bitmap = pygame.image.load(filename)

    def render(self):
        gameScreen.blit(self.bitmap, (self.x, self.y))





'''    Инициализация, заполнение и перемешивание колоды        Инициализация, заполнение и перемешивание колоды     '''


deskSize = 52
deckQuantity = 6
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
        cardDesk.append(['Q'])
    elif cardNumber == 13:
        cardDesk.append(['K'])
    else:
        cardDesk.append(['A'])

    cardDesk[i].append(suit[suitNumber])
    cardNumber += 1

    if cardNumber == 15:
        suitNumber += 1
        cardNumber = 2

cardDesk *= deckQuantity
deskSize *= deckQuantity

random.shuffle(cardDesk)






'''  Определяем цену карты        Определяем цену карты        Определяем цену карты        Определяем цену карты   '''


def determineCardPrice(sum, card):
    if card == 'J' or card == 'Q' or card == 'K' or card == '10':
        return 10
    elif card == 'A' and sum < 11:
        return 11
    elif card == 'A' and sum >= 11:
        return 1
    else:
        return int(card)





'''   Игровое окно       Игровое окно       Игровое окно       Игровое окно       Игровое окно       Игровое окно   '''


gameScreen = pygame.Surface((800, 600))

deal = Buttons(375, 495, "Images\Buttons\deal.png")
dealActive = Buttons(375, 495, "Images\Buttons\deal active.png")


cardCount = 0
gamerCardCount = -1
dealerCardCount = -1
gamerSum = 0
dealerSum = 0
takeABet = False
buttonQuantity = -1
xPosOfFirstButtons = 375
xPosOfSecondButtons = 375
xPosOfThirdButtons = 375
xPosOfFourthButtons = 375
xPosOfFivethButtons = 375

while True:

    gameScreen.blit(pygame.image.load("Images\Backgrounds\game screen.png"), (0, 0))

    mousePos = pygame.mouse.get_pos()

    if cardCount > deskSize * deckQuantity / 1.5 and gamerCardCount == -1:
        random.shuffle(cardDesk)
        cardCount = 0

    if takeABet == False:
        if mousePos[0] > 375 and mousePos[0] < 435 and mousePos[1] > 495 and mousePos[1] < 555:
            dealActive.render()
        else:
            deal.render()

    if gamerCardCount == 0:

        gamerCard1 = Cards(370, 280, "Images\Cards\\" + cardDesk[cardCount][0] + cardDesk[cardCount][1] + ".png")
        valueOfGamerCard1 = cardDesk[cardCount][0]
        priceOfGamerCard1 = determineCardPrice(gamerSum, cardDesk[cardCount][0])
        gamerSum += priceOfGamerCard1

        dealerCard1 = Cards(350, 100, "Images\Cards\\" + cardDesk[cardCount + 1][0] + cardDesk[cardCount + 1][1] + ".png")
        valueOfDealerCard1 = cardDesk[cardCount + 1][0]
        priceOfDealerCard1 = determineCardPrice(dealerSum, cardDesk[cardCount + 1][0])
        dealerSum += priceOfDealerCard1

        gamerCard2 = Cards(390, 280, "Images\Cards\\" + cardDesk[cardCount + 2][0] + cardDesk[cardCount + 2][1] + ".png")
        valueOfGamerCard2 = cardDesk[cardCount + 2][0]
        priceOfGamerCard2 = determineCardPrice(gamerSum, cardDesk[cardCount + 2][0])
        gamerSum += priceOfGamerCard2

        dealerCard2 = Cards(410, 100, "Images\Cards\\" + cardDesk[cardCount + 3][0] + cardDesk[cardCount + 3][1] + ".png")
        valueOfDealerCard2 = cardDesk[cardCount + 3][0]
        priceOfDealerCard2 = determineCardPrice(dealerSum, cardDesk[cardCount + 3][0])
        dealerSum += priceOfDealerCard2

        print(gamerSum, dealerSum)

        gamerCardCount = 2
        dealerCardCount = 2
        cardCount += 4

    if buttonQuantity == 0:

        buttonQuantity = 3
        if valueOfGamerCard1 == valueOfGamerCard2 and valueOfDealerCard1 == 'A':
            buttonQuantity += 2
        elif valueOfGamerCard1 == valueOfGamerCard2 or valueOfDealerCard1 == 'A':
            buttonQuantity += 1

        if buttonQuantity == 3:
            xPosOfFirstButtons -= 70
            xPosOfThirdButtons += 70
        elif buttonQuantity == 4:
            xPosOfFirstButtons -= 105
            xPosOfSecondButtons -=35
            xPosOfThirdButtons += 35
            xPosOfFourthButtons += 105
        else:
            xPosOfFirstButtons -= 140
            xPosOfSecondButtons -= 70
            xPosOfFourthButtons += 70
            xPosOfFivethButtons += 140

        firstButton = Buttons(xPosOfFirstButtons, 495, "Images\Buttons\Hit.png")
        firstButtonActive = Buttons(xPosOfFirstButtons, 495, "Images\Buttons\Hit active.png")
        secondButton = Buttons(xPosOfSecondButtons, 495, "Images\Buttons\Stand.png")
        secondButtonActive = Buttons(xPosOfSecondButtons, 495, "Images\Buttons\Stand active.png")
        thirdButton = Buttons(xPosOfThirdButtons, 495, "Images\Buttons\Double.png")
        thirdButtonActive = Buttons(xPosOfThirdButtons, 495, "Images\Buttons\Double active.png")
        if buttonQuantity == 4 and valueOfDealerCard1 == 'A':
            fourthButton = Buttons(xPosOfFourthButtons, 495, "Images\Buttons\Yes.png")
            fourthButtonActive = Buttons(xPosOfFourthButtons, 495, "Images\Buttons\Yes active.png")
        else:
            fourthButton = Buttons(xPosOfFourthButtons, 495, "Images\Buttons\Split.png")
            fourthButtonActive = Buttons(xPosOfFourthButtons, 495, "Images\Buttons\Split active.png")
        fivethButton = Buttons(xPosOfFivethButtons, 495, "Images\Buttons\Yes.png")
        fivethButtonActive = Buttons(xPosOfFivethButtons, 495, "Images\Buttons\Yes active.png")

    if buttonQuantity > 0:
        if mousePos[0] > xPosOfFirstButtons and mousePos[0] < xPosOfFirstButtons + 60 and \
                        mousePos[1] > 495 and mousePos[1] < 555:
            firstButtonActive.render()
        else:
            firstButton.render()

        if mousePos[0] > xPosOfSecondButtons and mousePos[0] < xPosOfSecondButtons + 60 and \
                        mousePos[1] > 495 and mousePos[1] < 555:
            secondButtonActive.render()
        else:
            secondButton.render()

        if mousePos[0] > xPosOfThirdButtons and mousePos[0] < xPosOfThirdButtons + 60 and \
                        mousePos[1] > 495 and mousePos[1] < 555:
            thirdButtonActive.render()
        else:
            thirdButton.render()

        if buttonQuantity == 4 and mousePos[0] > xPosOfFourthButtons and mousePos[0] < xPosOfFourthButtons + 60 and \
                        mousePos[1] > 495 and mousePos[1] < 555:
            fourthButtonActive.render()
        elif buttonQuantity == 4:
            fourthButton.render()

        if buttonQuantity == 5 and mousePos[0] > xPosOfFivethButtons and mousePos[0] < xPosOfFivethButtons + 60 and \
                        mousePos[1] > 495 and mousePos[1] < 555:
            fivethButtonActive.render()
        elif buttonQuantity == 5:
            fivethButton.render()

    if gamerCardCount > 0:

        gamerCard1.render()
        dealerCard1.render()
        gamerCard2.render()
        dealerCard2.render()

    for i in pygame.event.get():

        if i.type == pygame.QUIT:
            sys.exit()

        if mousePos[0] > xPosOfFirstButtons and mousePos[0] < xPosOfFirstButtons + 60 and buttonQuantity > 0 and \
                        mousePos[1] > 495 and mousePos[1] < 555 and i.type == pygame.MOUSEBUTTONDOWN and i.button == 1:
            print("Hit")

        if mousePos[0] > xPosOfSecondButtons and mousePos[0] < xPosOfSecondButtons + 60 and buttonQuantity > 0 and \
                        mousePos[1] > 495 and mousePos[1] < 555 and i.type == pygame.MOUSEBUTTONDOWN and i.button == 1:
            print("Stand")

        if mousePos[0] > xPosOfThirdButtons and mousePos[0] < xPosOfThirdButtons + 60 and buttonQuantity > 0 and \
                        mousePos[1] > 495 and mousePos[1] < 555 and i.type == pygame.MOUSEBUTTONDOWN and i.button == 1:
            print("Double")

        if buttonQuantity == 4 and mousePos[0] > xPosOfFourthButtons and mousePos[0] < xPosOfFourthButtons + 60 and \
                        mousePos[1] > 495 and mousePos[1] < 555 and valueOfDealerCard1 == 'A' and \
                        i.type == pygame.MOUSEBUTTONDOWN and i.button == 1:
            print("Insurance")

        elif buttonQuantity == 4 and mousePos[0] > xPosOfFourthButtons and mousePos[0] < xPosOfFourthButtons + 60 and \
                        mousePos[1] > 495 and mousePos[1] < 555 and i.type == pygame.MOUSEBUTTONDOWN and i.button == 1:
            print("Split")

        if buttonQuantity == 5 and mousePos[0] > xPosOfFivethButtons and mousePos[0] < xPosOfFivethButtons + 60 and \
                        mousePos[1] > 495 and mousePos[1] < 555 and i.type == pygame.MOUSEBUTTONDOWN and i.button == 1:
            print("Insurance")

        if takeABet == False and i.type == pygame.MOUSEBUTTONDOWN and i.button == 1 and\
                        mousePos[0] > 375 and mousePos[0] < 435 and mousePos[1] > 495 and mousePos[1] < 555:
            takeABet = True
            gamerCardCount = 0
            dealerCardCount = 0
            buttonQuantity = 0
            break

    window.blit(gameScreen, (0, 0))
    pygame.display.flip()