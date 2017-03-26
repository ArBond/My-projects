import pygame
pygame.font.init()
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


class Chips:

    def __init__(self, xpos, ypos, filename):
        self.x = xpos
        self.y = ypos
        self.bitmap = pygame.image.load(filename)
        self.bitmap.set_colorkey((0, 0, 0))

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


def determineCardPrice(sum, card, countA):
    if card == 'J' or card == 'Q' or card == 'K' or card == '10':
        return 10, countA
    elif card == 'A' and sum < 11:
        return 11, 1
    elif card == 'A' and sum >= 11:
        return 1, countA
    else:
        return int(card), countA





'''   Игровое окно       Игровое окно       Игровое окно       Игровое окно       Игровое окно       Игровое окно   '''


gameScreen = pygame.Surface((800, 600))

depozitText = pygame.font.SysFont("Consolas", 16, True)
betText = pygame.font.SysFont("Consolas", 16, True)

deal = Buttons(375, 495, "Images\Buttons\deal.png")
dealActive = Buttons(375, 495, "Images\Buttons\deal active.png")

chip1 = Chips(32, 447, "Images\Chips\\1.png")
chip5 = Chips(73, 466, "Images\Chips\\5.png")
chip25 = Chips(114, 481, "Images\Chips\\25.png")
chip100 = Chips(155, 494, "Images\Chips\\100.png")
chip1Active = Chips(32, 447, "Images\Chips\\1 active.png")
chip5Active = Chips(73, 466, "Images\Chips\\5 active.png")
chip25Active = Chips(114, 481, "Images\Chips\\25 active.png")
chip100Active = Chips(155, 494, "Images\Chips\\100 active.png")

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
chipsCount = 0
chipName = 'none'
doublesRender = False
lightGamerA = 0
lightDealerA = 0

gamerDepozit = 100
gamerBet = 0

while True:

    gameScreen.blit(pygame.image.load("Images\Backgrounds\game screen.png"), (0, 0))

    mousePos = pygame.mouse.get_pos()

    if gamerSum > 21 or dealerSum > 21:
        if gamerSum > 21:
            print("you LOOSER!")
        elif dealerSum > 21:
            print("you WINNER!")
            gamerDepozit += gamerBet * 2
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
        chipsCount = 0
        doublesRender = False
        lightGamerA = 0
        lightDealerA = 0

        gamerBet = 0

    if clickedButton == 'dealerGetCards':
        clickedButton = 'none'
        if gamerSum == 21 and dealerSum != 21 and gamerCardCount == 2:
            print("Black Jack. you WINNER!")
            gamerDepozit += gamerBet * 3
        elif dealerSum == 21 and gamerSum != 21:
            if insuranceIsActive == True and dealerCardCount == 2:
                print("Insuranse")
                gamerDepozit += gamerBet
            else:
                print("you LOOSER!")
        elif gamerSum > dealerSum:
            print("you WINNER!")
            gamerDepozit += gamerBet * 2
        elif gamerSum < dealerSum:
            print("you LOOSER!")
        else:
            print("draw!")
            gamerDepozit += gamerBet
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
        chipsCount = 0
        doublesRender = False
        lightGamerA = 0
        lightDealerA = 0

        gamerBet = 0

    if cardCount > deskSize * deckQuantity / 1.5 and gamerCardCount == -1:
        random.shuffle(cardDesk)
        cardCount = 0

    if takeABet == False:

        if mousePos[0] > 32 and mousePos[0] < 70 and mousePos[1] > 447 and mousePos[1] < 478:
            chip1Active.render()
        else:
            chip1.render()

        if mousePos[0] > 73 and mousePos[0] < 110 and mousePos[1] > 466 and mousePos[1] < 498:
            chip5Active.render()
        else:
            chip5.render()

        if mousePos[0] > 114 and mousePos[0] < 150 and mousePos[1] > 481 and mousePos[1] < 514:
            chip25Active.render()
        else:
            chip25.render()

        if mousePos[0] > 155 and mousePos[0] < 190 and mousePos[1] > 494 and mousePos[1] < 527:
            chip100Active.render()
        else:
            chip100.render()

        if mousePos[0] > 375 and mousePos[0] < 435 and mousePos[1] > 495 and mousePos[1] < 555 and gamerBet != 0:
            dealActive.render()
        else:
            deal.render()

        if chipName != 'none':
            if chipsCount == 1:
                rendersChip1 = Chips(389, 400, "Images\Chips\\" + chipName + ".png")
                valueOfChip1 = int(chipName)
                doubles1Chip1 = Chips(369, 400, "Images\Chips\\" + chipName + ".png")
                doubles2Chip1 = Chips(409, 400, "Images\Chips\\" + chipName + ".png")
            elif chipsCount == 2:
                rendersChip2 = Chips(389, 395, "Images\Chips\\" + chipName + ".png")
                valueOfChip2 = int(chipName)
                doubles1Chip2 = Chips(369, 395, "Images\Chips\\" + chipName + ".png")
                doubles2Chip2 = Chips(409, 395, "Images\Chips\\" + chipName + ".png")
            elif chipsCount == 3:
                rendersChip3 = Chips(389, 390, "Images\Chips\\" + chipName + ".png")
                valueOfChip3 = int(chipName)
                doubles1Chip3 = Chips(369, 390, "Images\Chips\\" + chipName + ".png")
                doubles2Chip3 = Chips(409, 390, "Images\Chips\\" + chipName + ".png")
            elif chipsCount == 4:
                rendersChip4 = Chips(389, 385, "Images\Chips\\" + chipName + ".png")
                valueOfChip4 = int(chipName)
                doubles1Chip4 = Chips(369, 385, "Images\Chips\\" + chipName + ".png")
                doubles2Chip4 = Chips(409, 385, "Images\Chips\\" + chipName + ".png")
            elif chipsCount == 5:
                rendersChip5 = Chips(389, 380, "Images\Chips\\" + chipName + ".png")
                valueOfChip5 = int(chipName)
                doubles1Chip5 = Chips(369, 380, "Images\Chips\\" + chipName + ".png")
                doubles2Chip5 = Chips(409, 380, "Images\Chips\\" + chipName + ".png")
            chipName = 'none'

        if chipsCount > 0:
            rendersChip1.render()
            gamerBet = valueOfChip1
            if chipsCount > 1:
                rendersChip2.render()
                gamerBet = valueOfChip1 + valueOfChip2
                if chipsCount > 2:
                    rendersChip3.render()
                    gamerBet = valueOfChip1 + valueOfChip2 + valueOfChip3
                    if chipsCount > 3:
                        rendersChip4.render()
                        gamerBet = valueOfChip1 + valueOfChip2 + valueOfChip3 + valueOfChip4
                        if chipsCount > 4:
                            rendersChip5.render()
                            gamerBet = valueOfChip1 + valueOfChip2 + valueOfChip3 + valueOfChip4 + valueOfChip5
        else:
            gamerBet = 0

    elif chipsCount > 0 and doublesRender == False:
            rendersChip1.render()
            if chipsCount > 1:
                rendersChip2.render()
                if chipsCount > 2:
                    rendersChip3.render()
                    if chipsCount > 3:
                        rendersChip4.render()
                        if chipsCount > 4:
                            rendersChip5.render()

    if gamerCardCount == 0:

        gamerCard1 = Cards(370, 280, "Images\Cards\\" + cardDesk[cardCount][0] + cardDesk[cardCount][1] + ".png")
        valueOfGamerCard1 = cardDesk[cardCount][0]
        priceOfGamerCard1, lightGamerA = determineCardPrice(gamerSum, cardDesk[cardCount][0], lightGamerA)
        gamerSum += priceOfGamerCard1

        dealerCard1 = Cards(350, 100, "Images\Cards\\" + cardDesk[cardCount + 1][0] + cardDesk[cardCount + 1][1] + ".png")
        valueOfDealerCard1 = cardDesk[cardCount + 1][0]
        priceOfDealerCard1, lightDealerA = determineCardPrice(dealerSum, cardDesk[cardCount + 1][0], lightDealerA)
        dealerSum += priceOfDealerCard1

        gamerCard2 = Cards(390, 280, "Images\Cards\\" + cardDesk[cardCount + 2][0] + cardDesk[cardCount + 2][1] + ".png")
        valueOfGamerCard2 = cardDesk[cardCount + 2][0]
        priceOfGamerCard2, lightGamerA = determineCardPrice(gamerSum, cardDesk[cardCount + 2][0], lightGamerA)
        gamerSum += priceOfGamerCard2

        dealerCard2 = Cards(410, 100, "Images\Cards\\" + cardDesk[cardCount + 3][0] + cardDesk[cardCount + 3][1] + ".png")
        valueOfDealerCard2 = cardDesk[cardCount + 3][0]
        priceOfDealerCard2, lightDealerA = determineCardPrice(dealerSum, cardDesk[cardCount + 3][0], lightDealerA)
        dealerSum += priceOfDealerCard2

        gamerCardCount = 2
        dealerCardCount = 2
        cardCount += 4

    if clickedButton == 'Hit':
        clickedButton = 'none'
        if gamerCardCount == 3:
            gamerCard3 = Cards(410, 280, "Images\Cards\\" + cardDesk[cardCount][0] + cardDesk[cardCount][1] + ".png")
            valueOfGamerCard3 = cardDesk[cardCount][0]
            priceOfGamerCard3, lightGamerA = determineCardPrice(gamerSum, cardDesk[cardCount][0], lightGamerA)
            gamerSum += priceOfGamerCard3
            if gamerSum > 21 and lightGamerA == 1:
                gamerSum -= 10
                lightGamerA = 0
        elif gamerCardCount == 4:
            gamerCard4 = Cards(430, 280, "Images\Cards\\" + cardDesk[cardCount][0] + cardDesk[cardCount][1] + ".png")
            valueOfGamerCard4 = cardDesk[cardCount][0]
            priceOfGamerCard4, lightGamerA = determineCardPrice(gamerSum, cardDesk[cardCount][0], lightGamerA)
            gamerSum += priceOfGamerCard4
            if gamerSum > 21 and lightGamerA == 1:
                gamerSum -= 10
                lightGamerA = 0
        elif gamerCardCount == 5:
            gamerCard5 = Cards(450, 280, "Images\Cards\\" + cardDesk[cardCount][0] + cardDesk[cardCount][1] + ".png")
            valueOfGamerCard5 = cardDesk[cardCount][0]
            priceOfGamerCard5, lightGamerA = determineCardPrice(gamerSum, cardDesk[cardCount][0], lightGamerA)
            gamerSum += priceOfGamerCard5
            if gamerSum > 21 and lightGamerA == 1:
                gamerSum -= 10
                lightGamerA = 0
        elif gamerCardCount == 6:
            gamerCard6 = Cards(470, 280, "Images\Cards\\" + cardDesk[cardCount][0] + cardDesk[cardCount][1] + ".png")
            valueOfGamerCard6 = cardDesk[cardCount][0]
            priceOfGamerCard6, lightGamerA = determineCardPrice(gamerSum, cardDesk[cardCount][0], lightGamerA)
            gamerSum += priceOfGamerCard6
            if gamerSum > 21 and lightGamerA == 1:
                gamerSum -= 10
                lightGamerA = 0
        elif gamerCardCount == 7:
            gamerCard7 = Cards(490, 280, "Images\Cards\\" + cardDesk[cardCount][0] + cardDesk[cardCount][1] + ".png")
            valueOfGamerCard7 = cardDesk[cardCount][0]
            priceOfGamerCard7, lightGamerA = determineCardPrice(gamerSum, cardDesk[cardCount][0], lightGamerA)
            gamerSum += priceOfGamerCard7
            if gamerSum > 21 and lightGamerA == 1:
                gamerSum -= 10
                lightGamerA = 0
        elif gamerCardCount == 8:
            gamerCard8 = Cards(510, 280, "Images\Cards\\" + cardDesk[cardCount][0] + cardDesk[cardCount][1] + ".png")
            valueOfGamerCard8 = cardDesk[cardCount][0]
            priceOfGamerCard8, lightGamerA = determineCardPrice(gamerSum, cardDesk[cardCount][0], lightGamerA)
            gamerSum += priceOfGamerCard8
            if gamerSum > 21 and lightGamerA == 1:
                gamerSum -= 10
                lightGamerA = 0

    if clickedButton == 'Stand':
        clickedButton = 'dealerGetCards'
        while dealerSum < 17:
            dealerCardCount += 1
            cardCount += 1
            if dealerCardCount == 3:
                dealerCard3 = Cards(430, 100, "Images\Cards\\" + cardDesk[cardCount][0] + cardDesk[cardCount][1] + ".png")
                valueOfDealerCard3 = cardDesk[cardCount][0]
                priceOfDealerCard3, lightDealerA = determineCardPrice(dealerSum, cardDesk[cardCount][0], lightDealerA)
                dealerSum += priceOfDealerCard3
                if dealerSum > 21 and lightDealerA == 1:
                    dealerSum -= 10
                    lightDealerA = 0
            elif dealerCardCount == 4:
                dealerCard4 = Cards(450, 100, "Images\Cards\\" + cardDesk[cardCount][0] + cardDesk[cardCount][1] + ".png")
                valueOfDealerCard4 = cardDesk[cardCount][0]
                priceOfDealerCard4, lightDealerA = determineCardPrice(dealerSum, cardDesk[cardCount][0], lightDealerA)
                dealerSum += priceOfDealerCard4
                if dealerSum > 21 and lightDealerA == 1:
                    dealerSum -= 10
                    lightDealerA = 0
            elif dealerCardCount == 5:
                dealerCard5 = Cards(470, 100, "Images\Cards\\" + cardDesk[cardCount][0] + cardDesk[cardCount][1] + ".png")
                valueOfDealerCard5 = cardDesk[cardCount][0]
                priceOfDealerCard5, lightDealerA = determineCardPrice(dealerSum, cardDesk[cardCount][0], lightDealerA)
                dealerSum += priceOfDealerCard5
                if dealerSum > 21 and lightDealerA == 1:
                    dealerSum -= 10
                    lightDealerA = 0
            elif dealerCardCount == 6:
                dealerCard6 = Cards(490, 100, "Images\Cards\\" + cardDesk[cardCount][0] + cardDesk[cardCount][1] + ".png")
                valueOfDealerCard6 = cardDesk[cardCount][0]
                priceOfDealerCard6, lightDealerA = determineCardPrice(dealerSum, cardDesk[cardCount][0], lightDealerA)
                dealerSum += priceOfDealerCard6
                if dealerSum > 21 and lightDealerA == 1:
                    dealerSum -= 10
                    lightDealerA = 0
            elif dealerCardCount == 7:
                dealerCard7 = Cards(510, 100, "Images\Cards\\" + cardDesk[cardCount][0] + cardDesk[cardCount][1] + ".png")
                valueOfDealerCard7 = cardDesk[cardCount][0]
                priceOfDealerCard7, lightDealerA = determineCardPrice(dealerSum, cardDesk[cardCount][0], lightDealerA)
                dealerSum += priceOfDealerCard7
                if dealerSum > 21 and lightDealerA == 1:
                    dealerSum -= 10
                    lightDealerA = 0
            elif dealerCardCount == 8:
                dealerCard8 = Cards(530, 100, "Images\Cards\\" + cardDesk[cardCount][0] + cardDesk[cardCount][1] + ".png")
                valueOfDealerCard8 = cardDesk[cardCount][0]
                priceOfDealerCard8, lightDealerA = determineCardPrice(dealerSum, cardDesk[cardCount][0], lightDealerA)
                dealerSum += priceOfDealerCard8
                if dealerSum > 21 and lightDealerA == 1:
                    dealerSum -= 10
                    lightDealerA = 0

    if clickedButton == 'Double':
        doublesRender = True

        gamerCard3 = Cards(410, 280, "Images\Cards\\" + cardDesk[cardCount][0] + cardDesk[cardCount][1] + ".png")
        valueOfGamerCard3 = cardDesk[cardCount][0]
        priceOfGamerCard3, lightGamerA = determineCardPrice(gamerSum, cardDesk[cardCount][0], lightGamerA)
        gamerSum += priceOfGamerCard3
        if gamerSum > 21 and lightGamerA == 1:
            gamerSum -= 10
            lightGamerA = 0

        clickedButton = 'Stand'

    if doublesRender == True:
        doubles1Chip1.render()
        doubles2Chip1.render()
        if chipsCount > 1:
            doubles1Chip2.render()
            doubles2Chip2.render()
            if chipsCount > 2:
                doubles1Chip3.render()
                doubles2Chip3.render()
                if chipsCount > 3:
                    doubles1Chip4.render()
                    doubles2Chip4.render()
                    if chipsCount > 4:
                        doubles1Chip5.render()
                        doubles2Chip5.render()

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
                        gamerCardCount == 2 and mousePos[1] > 495 and mousePos[1] < 555 and gamerDepozit >= gamerBet:
            thirdButtonActive.render()
        elif gamerCardCount == 2 and gamerDepozit >= gamerBet:
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

    gameScreen.blit(depozitText.render("Money: "+ str(gamerDepozit) + " $", 1, (255, 255, 255)), (30, 576))
    if takeABet == True:
        gameScreen.blit(betText.render("Bet: " + str(gamerBet) + " $", 1, (255, 255, 255)), (350, 576))

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
                        mousePos[1] > 495 and mousePos[1] < 555 and gamerDepozit >= gamerBet  and \
                        i.type == pygame.MOUSEBUTTONDOWN and i.button == 1:
            clickedButton = 'Double'
            gamerDepozit -= gamerBet
            gamerBet *= 2
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

        if takeABet == False:

            if mousePos[0] > 375 and mousePos[0] < 435 and mousePos[1] > 495 and mousePos[1] < 555 and \
                            gamerBet != 0 and i.type == pygame.MOUSEBUTTONDOWN and i.button == 1:
                clickedButton = 'Dill'
                takeABet = True
                gamerDepozit -= gamerBet
                gamerCardCount = 0
                dealerCardCount = 0
                buttonQuantity = 0

            if mousePos[0] > 32 and mousePos[0] < 70 and mousePos[1] > 447 and mousePos[1] < 478 and \
                            i.type == pygame.MOUSEBUTTONDOWN:
                if i.button == 1 and chipsCount < 5 and gamerDepozit >= gamerBet + 1:
                    chipName = "1"
                    chipsCount += 1
                elif i.button == 3 and chipsCount > 0:
                    chipsCount -= 1

            if mousePos[0] > 73 and mousePos[0] < 110 and mousePos[1] > 466 and mousePos[1] < 498 and \
                            i.type == pygame.MOUSEBUTTONDOWN:
                if i.button == 1 and chipsCount < 5 and gamerDepozit >= gamerBet + 5:
                    chipName = "5"
                    chipsCount += 1
                elif i.button == 3 and chipsCount > 0:
                    chipsCount -= 1

            if mousePos[0] > 114 and mousePos[0] < 150 and mousePos[1] > 481 and mousePos[1] < 514 and \
                            i.type == pygame.MOUSEBUTTONDOWN:
                if i.button == 1 and chipsCount < 5 and gamerDepozit >= gamerBet + 25:
                    chipName = "25"
                    chipsCount += 1
                elif i.button == 3 and chipsCount > 0:
                    chipsCount -= 1

            if mousePos[0] > 155 and mousePos[0] < 190 and mousePos[1] > 494 and mousePos[1] < 527 and \
                            i.type == pygame.MOUSEBUTTONDOWN:
                if i.button == 1 and chipsCount < 5 and gamerDepozit >= gamerBet + 100:
                    chipName = "100"
                    chipsCount += 1
                elif i.button == 3 and chipsCount > 0:
                    chipsCount -= 1

    window.blit(gameScreen, (0, 0))
    pygame.display.flip()