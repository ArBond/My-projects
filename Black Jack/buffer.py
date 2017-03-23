'''
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
'''


import pygame
import sys
import random
import time

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
clickedButton = 'none'
insuranceIsActive = False

while True:

    gameScreen.blit(pygame.image.load("Images\Backgrounds\game screen.png"), (0, 0))
    mousePos = pygame.mouse.get_pos()

    if gamerSum > 21 or dealerSum > 21:
        if gamerSum > 21:
            print("you LOOSER!", dealerSum)
        elif dealerSum > 21:
            print("you WINNER!", dealerSum)
        time.sleep(2)
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
        clickedButton = 'none'
        insuranceIsActive = False

    if clickedButton == 'dealerGetCards':
        clickedButton = 'none'
        if gamerSum == 21 and dealerSum != 21:
            print("Black Jack. you WINNER!")
        elif dealerSum == 21 and gamerSum != 21:
            if insuranceIsActive == True:
                print("Insuranse")
            else:
                print("you LOOSER!")
        elif gamerSum > dealerSum:
            print("you WINNER!", dealerSum)
        elif gamerSum < dealerSum:
            print("you LOOSER!", dealerSum)
        else:
            print("draw!", dealerSum)
        time.sleep(2)
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
        clickedButton = 'none'
        insuranceIsActive = False

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

        gamerCardCount = 2
        dealerCardCount = 2
        cardCount += 4

    if clickedButton == 'Hit':
        clickedButton = 'none'
        if gamerCardCount == 3:
            gamerCard3 = Cards(410, 280, "Images\Cards\\" + cardDesk[cardCount][0] + cardDesk[cardCount][1] + ".png")
            valueOfGamerCard3 = cardDesk[cardCount][0]
            priceOfGamerCard3 = determineCardPrice(gamerSum, cardDesk[cardCount][0])
            gamerSum += priceOfGamerCard3
        elif gamerCardCount == 4:
            gamerCard4 = Cards(430, 280, "Images\Cards\\" + cardDesk[cardCount][0] + cardDesk[cardCount][1] + ".png")
            valueOfGamerCard4 = cardDesk[cardCount][0]
            priceOfGamerCard4 = determineCardPrice(gamerSum, cardDesk[cardCount][0])
            gamerSum += priceOfGamerCard4
        elif gamerCardCount == 5:
            gamerCard5 = Cards(450, 280, "Images\Cards\\" + cardDesk[cardCount][0] + cardDesk[cardCount][1] + ".png")
            valueOfGamerCard5 = cardDesk[cardCount][0]
            priceOfGamerCard5 = determineCardPrice(gamerSum, cardDesk[cardCount][0])
            gamerSum += priceOfGamerCard5
        elif gamerCardCount == 6:
            gamerCard6 = Cards(470, 280, "Images\Cards\\" + cardDesk[cardCount][0] + cardDesk[cardCount][1] + ".png")
            valueOfGamerCard6 = cardDesk[cardCount][0]
            priceOfGamerCard6 = determineCardPrice(gamerSum, cardDesk[cardCount][0])
            gamerSum += priceOfGamerCard6
        elif gamerCardCount == 7:
            gamerCard7 = Cards(490, 280, "Images\Cards\\" + cardDesk[cardCount][0] + cardDesk[cardCount][1] + ".png")
            valueOfGamerCard7 = cardDesk[cardCount][0]
            priceOfGamerCard7 = determineCardPrice(gamerSum, cardDesk[cardCount][0])
            gamerSum += priceOfGamerCard7
        elif gamerCardCount == 8:
            gamerCard8 = Cards(510, 280, "Images\Cards\\" + cardDesk[cardCount][0] + cardDesk[cardCount][1] + ".png")
            valueOfGamerCard8 = cardDesk[cardCount][0]
            priceOfGamerCard8 = determineCardPrice(gamerSum, cardDesk[cardCount][0])
            gamerSum += priceOfGamerCard8

    if clickedButton == 'Stand':
        clickedButton = 'dealerGetCards'
        while dealerSum < 17:
            dealerCardCount += 1
            cardCount += 1
            if dealerCardCount == 3:
                dealerCard3 = Cards(450, 100, "Images\Cards\\" + cardDesk[cardCount][0] + cardDesk[cardCount][1] + ".png")
                valueOfDealerCard3 = cardDesk[cardCount][0]
                priceOfDealerCard3 = determineCardPrice(dealerSum, cardDesk[cardCount][0])
                dealerSum += priceOfDealerCard3
            elif dealerCardCount == 4:
                dealerCard4 = Cards(470, 100, "Images\Cards\\" + cardDesk[cardCount][0] + cardDesk[cardCount][1] + ".png")
                valueOfDealerCard4 = cardDesk[cardCount][0]
                priceOfDealerCard4 = determineCardPrice(dealerSum, cardDesk[cardCount][0])
                dealerSum += priceOfDealerCard4
            elif dealerCardCount == 5:
                dealerCard5 = Cards(490, 100, "Images\Cards\\" + cardDesk[cardCount][0] + cardDesk[cardCount][1] + ".png")
                valueOfDealerCard5 = cardDesk[cardCount][0]
                priceOfDealerCard5 = determineCardPrice(dealerSum, cardDesk[cardCount][0])
                dealerSum += priceOfDealerCard5
            elif dealerCardCount == 6:
                dealerCard6 = Cards(510, 100, "Images\Cards\\" + cardDesk[cardCount][0] + cardDesk[cardCount][1] + ".png")
                valueOfDealerCard6 = cardDesk[cardCount][0]
                priceOfDealerCard6 = determineCardPrice(dealerSum, cardDesk[cardCount][0])
                dealerSum += priceOfDealerCard6
            elif dealerCardCount == 7:
                dealerCard7 = Cards(530, 100, "Images\Cards\\" + cardDesk[cardCount][0] + cardDesk[cardCount][1] + ".png")
                valueOfDealerCard7 = cardDesk[cardCount][0]
                priceOfDealerCard7 = determineCardPrice(dealerSum, cardDesk[cardCount][0])
                dealerSum += priceOfDealerCard7
            elif dealerCardCount == 8:
                dealerCard8 = Cards(450, 100, "Images\Cards\\" + cardDesk[cardCount][0] + cardDesk[cardCount][1] + ".png")
                valueOfDealerCard8 = cardDesk[cardCount][0]
                priceOfDealerCard8 = determineCardPrice(dealerSum, cardDesk[cardCount][0])
                dealerSum += priceOfDealerCard8

    if clickedButton == 'Double':
        clickedButton = 'Stand'
        gamerCard3 = Cards(410, 280, "Images\Cards\\" + cardDesk[cardCount][0] + cardDesk[cardCount][1] + ".png")
        valueOfGamerCard3 = cardDesk[cardCount][0]
        priceOfGamerCard3 = determineCardPrice(gamerSum, cardDesk[cardCount][0])
        gamerSum += priceOfGamerCard3

    if clickedButton == 'Insurance':
        insuranceIsActive = True
        clickedButton = 'none'

    if gamerCardCount > 0:
        gamerCard1.render()
        gamerCard2.render()
        if gamerCardCount > 2:
            gamerCard3.render()
            if gamerCardCount > 3:
                gamerCard4.render()
                if gamerCardCount > 4:
                    gamerCard5.render()
                    if gamerCardCount > 5:
                        gamerCard6.render()
                        if gamerCardCount > 6:
                            gamerCard7.render()
                            if gamerCardCount > 7:
                                gamerCard8.render()

    if dealerCardCount > 0:
        dealerCard1.render()
        dealerCard2.render()
        if dealerCardCount > 2:
            dealerCard3.render()
            if dealerCardCount > 3:
                dealerCard4.render()
                if dealerCardCount > 4:
                    dealerCard5.render()
                    if dealerCardCount > 5:
                        dealerCard6.render()
                        if dealerCardCount > 6:
                            dealerCard7.render()
                            if dealerCardCount > 7:
                                dealerCard8.render()

    if buttonQuantity == 0:
        buttonQuantity = 3

        if gamerCardCount == 2 and dealerCardCount == 2:
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
                        gamerCardCount == 2 and mousePos[1] > 495 and mousePos[1] < 555:
            thirdButtonActive.render()
        elif gamerCardCount == 2:
            thirdButton.render()

        if buttonQuantity == 4 and mousePos[0] > xPosOfFourthButtons and mousePos[0] < xPosOfFourthButtons + 60 and \
                        mousePos[1] > 495 and mousePos[1] < 555 and insuranceIsActive == False:
            fourthButtonActive.render()
        elif buttonQuantity == 4 and insuranceIsActive == False:
            fourthButton.render()

        if buttonQuantity == 5 and mousePos[0] > xPosOfFivethButtons and mousePos[0] < xPosOfFivethButtons + 60 and \
                        mousePos[1] > 495 and mousePos[1] < 555 and insuranceIsActive == False:
            fivethButtonActive.render()
        elif buttonQuantity == 5 and insuranceIsActive == False:
            fivethButton.render()

    for i in pygame.event.get():

        if i.type == pygame.QUIT:
            sys.exit()

        if mousePos[0] > xPosOfFirstButtons and mousePos[0] < xPosOfFirstButtons + 60 and buttonQuantity > 0 and \
                        mousePos[1] > 495 and mousePos[1] < 555 and i.type == pygame.MOUSEBUTTONDOWN and i.button == 1:
            clickedButton = 'Hit'
            buttonQuantity = 0
            xPosOfFirstButtons = 375
            xPosOfSecondButtons = 375
            xPosOfThirdButtons = 375
            gamerCardCount += 1
            cardCount += 1

        if mousePos[0] > xPosOfSecondButtons and mousePos[0] < xPosOfSecondButtons + 60 and buttonQuantity > 0 and \
                        mousePos[1] > 495 and mousePos[1] < 555 and i.type == pygame.MOUSEBUTTONDOWN and i.button == 1:
            clickedButton = 'Stand'
            buttonQuantity = -1

        if mousePos[0] > xPosOfThirdButtons and mousePos[0] < xPosOfThirdButtons + 60 and gamerCardCount == 2 and \
                        mousePos[1] > 495 and mousePos[1] < 555 and i.type == pygame.MOUSEBUTTONDOWN and i.button == 1:
            clickedButton = 'Double'
            buttonQuantity = -1
            gamerCardCount += 1
            cardCount += 1

        if buttonQuantity == 4 and mousePos[0] > xPosOfFourthButtons and mousePos[0] < xPosOfFourthButtons + 60 and \
                        mousePos[1] > 495 and mousePos[1] < 555 and valueOfDealerCard1 == 'A' and \
                        i.type == pygame.MOUSEBUTTONDOWN and i.button == 1:
            clickedButton = 'Insurance'

        elif buttonQuantity == 4 and mousePos[0] > xPosOfFourthButtons and mousePos[0] < xPosOfFourthButtons + 60 and \
                        mousePos[1] > 495 and mousePos[1] < 555 and i.type == pygame.MOUSEBUTTONDOWN and i.button == 1:
            clickedButton = 'Split'

        if buttonQuantity == 5 and mousePos[0] > xPosOfFivethButtons and mousePos[0] < xPosOfFivethButtons + 60 and \
                        mousePos[1] > 495 and mousePos[1] < 555 and i.type == pygame.MOUSEBUTTONDOWN and i.button == 1:
            clickedButton = 'Insurance'

        if takeABet == False and i.type == pygame.MOUSEBUTTONDOWN and i.button == 1 and\
                        mousePos[0] > 375 and mousePos[0] < 435 and mousePos[1] > 495 and mousePos[1] < 555:
            clickedButton = 'Dill'
            takeABet = True
            gamerCardCount = 0
            dealerCardCount = 0
            buttonQuantity = 0

    window.blit(gameScreen, (0, 0))
    pygame.display.flip()
