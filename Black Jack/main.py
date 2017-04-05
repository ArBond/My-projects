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
        self.bitmap.set_colorkey((0, 0, 0))

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


'''     Инво окно          Инво окно          Инво окно          Инво окно          Инво окно          Инво окно    '''

def infoScree():
    print("Инфо")





'''   Стартовое окно        Стартовое окно         Стартовое окно         Стартовое окно         Стартовое окно  '''


def startScreen():

    startScreen = pygame.Surface((800, 600))

    stringWelcome = pygame.font.SysFont("Consolas", 50, True)
    infoButton = pygame.font.SysFont("Consolas", 24, True)
    gameButton = pygame.font.SysFont("Consolas", 35, True)

    blueOfStringToContinue = 0

    depositString = ""
    enteringDeposit = pygame.font.SysFont("Arial", 40)

    redOfRect = 0
    greenOfRect = 255
    windowForInter = 'none'
    widthOfWindowLine = 2

    while True:

        startScreen.blit(pygame.image.load("Images\Backgrounds\Start screen.png"), (0, 0))

        startScreen.blit(stringWelcome.render("Добро пожаловать!", 1, (255, 255, 255)), (170, 30))

        pygame.draw.rect(startScreen, (255, 255, 255), [325, 220, 160, 50])
        pygame.draw.rect(startScreen, (redOfRect, greenOfRect, 0), [325, 220, 160, 50], widthOfWindowLine)
        startScreen.blit(enteringDeposit.render(depositString, 1, (0, 0, 0)), (330, 220))

        startScreen.blit(gameButton.render("Начать", 1, (255, 255, blueOfStringToContinue)), (350, 360))

        startScreen.blit(infoButton.render("Описание", 1, (255, 255, 255)), (340, 560))

        for i in pygame.event.get():

            if i.type == pygame.QUIT:
                sys.exit()

            if i.type == pygame.KEYDOWN and windowForInter == 'center':
                if (i.key >= pygame.K_0 and i.key <= pygame.K_9 or i.key >= pygame.K_KP0 and i.key <= pygame.K_KP9) \
                        and len(depositString) < 8:
                    depositString += i.unicode
                elif i.key == pygame.K_BACKSPACE:
                    depositString = depositString[:-1]

            mousePos = pygame.mouse.get_pos()

            if mousePos[0] > 325 and mousePos[0] < 485 and mousePos[1] > 220 and mousePos[1] < 275 and \
                            i.type == pygame.MOUSEBUTTONDOWN and i.button == 1:
                windowForInter = 'center'
                widthOfWindowLine = 4
                redOfRect = 0
                greenOfRect = 255
                depositString = ""

            if mousePos[0] > 350 and mousePos[0] < 470 and mousePos[1] > 365 and mousePos[1] < 390:
                blueOfStringToContinue = 0
                if i.type == pygame.MOUSEBUTTONDOWN and i.button == 1:
                    if depositString != '' and int(str(''.join(depositString))) != 0:
                        return int(str(''.join(depositString)))
                    else:
                        redOfRect = 200
                        greenOfRect = 0
                        widthOfWindowLine = 4
            else:
                blueOfStringToContinue = 150

        window.blit(startScreen, (0, 0))
        pygame.display.flip()




'''     Закончились деньги           Закончились деньги           Закончились деньги         Закончились деньги    '''


def whenMoneyIOut():

    whenMoneyIOutScreen = pygame.Surface((800, 600))

    animation1 = pygame.image.load("Images\Backgrounds\start screen.png"), (0, 0)





'''   Игровое окно       Игровое окно       Игровое окно       Игровое окно       Игровое окно       Игровое окно   '''


gameScreen = pygame.Surface((800, 600))

backCard = Cards(800, 0, "Images\Cards\\Back.png")

depozitText = pygame.font.SysFont("Consolas", 16, True)
betText = pygame.font.SysFont("Consolas", 16, True)

gamerSumText = pygame.font.SysFont("Consolas", 16)
dealerSumText = pygame.font.SysFont("Consolas", 16)

whoWinText = pygame.font.SysFont("Consolas", 30, True)

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

canFinish = True
needFinish = True
dealerSum = 0
gamerSum = 0
gamerCardCount = 0
finishDelayCounter = 0
cardCount = 0

gamerDepozit = -1
gamerBet = 0

while True:

    gameScreen.blit(pygame.image.load("Images\Backgrounds\game screen.png"), (0, 0))

    mousePos = pygame.mouse.get_pos()

    if gamerSum >= 21 and canFinish == True:
        needFinish = True

    if canFinish == True and needFinish == True:

        if gamerSum > 21:
            gameScreen.blit(whoWinText.render("you LOOSER!", 1, (255, 255, 0)), (280, 195))
        elif gamerSum == 21 and dealerSum != 21 and gamerCardCount == 2:
            gameScreen.blit(whoWinText.render("Black Jack. you WINNER!", 1, (255, 255, 0)), (280, 195))
            if finishDelayCounter == 0:
                gamerDepozit += gamerBet * 3
        elif dealerSum > 21:
            gameScreen.blit(whoWinText.render("you WINNER!", 1, (255, 255, 0)), (280, 195))
            if finishDelayCounter == 0:
                gamerDepozit += gamerBet * 2
        elif dealerSum == 21 and gamerSum != 21:
            if insuranceIsActive == True and dealerCardCount == 2:
                gameScreen.blit(whoWinText.render("Insuranse", 1, (255, 255, 0)), (280, 195))
                if finishDelayCounter == 0:
                    gamerDepozit += gamerBet * 2
            else:
                gameScreen.blit(whoWinText.render("you LOOSER!", 1, (255, 255, 0)), (280, 195))
        elif gamerSum > dealerSum and dealerSum >= 17:
            gameScreen.blit(whoWinText.render("you WINNER!", 1, (255, 255, 0)), (280, 195))
            if finishDelayCounter == 0:
                gamerDepozit += gamerBet * 2
        elif gamerSum < dealerSum and dealerSum >= 17:
            gameScreen.blit(whoWinText.render("you LOOSER!", 1, (255, 255, 0)), (280, 195))
        elif dealerSum >= 17:
            gameScreen.blit(whoWinText.render("draw!", 1, (255, 255, 0)), (280, 195))
            if finishDelayCounter == 0:
                gamerDepozit += gamerBet

        if gamerDepozit == -1:
            gamerDepozit = startScreen()
            finishDelayCounter = 49

        finishDelayCounter += 1

        if finishDelayCounter == 50:

            if gamerDepozit == 0:
                gamerDepozit = whenMoneyIOut()
                if gamerDepozit == 0:
                    startScreen()

            time.sleep(2)
            gamerCardCount = -1
            dealerCardCount = -1
            gamerSum = 0
            dealerSum = 0
            takeABet = False
            buttonQuantity = -1
            clickedButton = 'none'
            insuranceIsActive = False
            chipsCount = 0
            doublesRender = False
            lightGamerA = 0
            lightDealerA = 0
            gamerBet = 0
            canFinish = False
            needFinish = False
            finishDelayCounter = 0
            cardAnimationCount = 0
            chipName = 'none'

            gamerCard1IsRender = False
            gamerCard2IsRender = False
            gamerCard3IsRender = False
            gamerCard4IsRender = False
            gamerCard5IsRender = False
            gamerCard6IsRender = False
            gamerCard7IsRender = False
            gamerCard8IsRender = False

            dealerCard1IsRender = False
            dealerCard2IsRender = False
            dealerCard3IsRender = False
            dealerCard4IsRender = False
            dealerCard5IsRender = False
            dealerCard6IsRender = False
            dealerCard7IsRender = False
            dealerCard8IsRender = False

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
                doublesChip1 = Chips(150, 505, "Images\Chips\\" + chipName + ".png")
                insuranceChip1 = Chips(150, 505, "Images\Chips\\" + chipName + ".png")
            elif chipsCount == 2:
                rendersChip2 = Chips(389, 395, "Images\Chips\\" + chipName + ".png")
                valueOfChip2 = int(chipName)
                doublesChip2 = Chips(150, 500, "Images\Chips\\" + chipName + ".png")
                insuranceChip2 = Chips(150, 500, "Images\Chips\\" + chipName + ".png")
            elif chipsCount == 3:
                rendersChip3 = Chips(389, 390, "Images\Chips\\" + chipName + ".png")
                valueOfChip3 = int(chipName)
                doublesChip3 = Chips(150, 495, "Images\Chips\\" + chipName + ".png")
                insuranceChip3 = Chips(150, 495, "Images\Chips\\" + chipName + ".png")
            elif chipsCount == 4:
                rendersChip4 = Chips(389, 385, "Images\Chips\\" + chipName + ".png")
                valueOfChip4 = int(chipName)
                doublesChip4 = Chips(150, 490, "Images\Chips\\" + chipName + ".png")
                insuranceChip4 = Chips(150, 490, "Images\Chips\\" + chipName + ".png")
            elif chipsCount == 5:
                rendersChip5 = Chips(389, 380, "Images\Chips\\" + chipName + ".png")
                valueOfChip5 = int(chipName)
                doublesChip5 = Chips(150, 485, "Images\Chips\\" + chipName + ".png")
                insuranceChip5 = Chips(150, 485, "Images\Chips\\" + chipName + ".png")

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

    elif chipsCount > 0:
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

        gamerCard1 = Cards(370, 260, "Images\Cards\\" + cardDesk[cardCount][0] + cardDesk[cardCount][1] + ".png")
        valueOfGamerCard1 = cardDesk[cardCount][0]
        priceOfGamerCard1, lightGamerA = determineCardPrice(gamerSum, cardDesk[cardCount][0], lightGamerA)
        gamerSum += priceOfGamerCard1

        dealerCard1 = Cards(350, 80, "Images\Cards\\" + cardDesk[cardCount + 1][0] + cardDesk[cardCount + 1][1] + ".png")
        valueOfDealerCard1 = cardDesk[cardCount + 1][0]
        priceOfDealerCard1, lightDealerA = determineCardPrice(dealerSum, cardDesk[cardCount + 1][0], lightDealerA)
        dealerSum += priceOfDealerCard1

        gamerCard2 = Cards(390, 260, "Images\Cards\\" + cardDesk[cardCount + 2][0] + cardDesk[cardCount + 2][1] + ".png")
        valueOfGamerCard2 = cardDesk[cardCount + 2][0]
        priceOfGamerCard2, lightGamerA = determineCardPrice(gamerSum, cardDesk[cardCount + 2][0], lightGamerA)
        gamerSum += priceOfGamerCard2

        dealerCard2 = Cards(410, 80, "Images\Cards\\Back.png")
        realDealerCard2 = Cards(410, 80, "Images\Cards\\" + cardDesk[cardCount + 3][0] + cardDesk[cardCount + 3][1] + ".png")
        valueOfDealerCard2 = cardDesk[cardCount + 3][0]
        priceOfDealerCard2, lightDealerA = determineCardPrice(dealerSum, cardDesk[cardCount + 3][0], lightDealerA)

        gamerCardCount = 2
        dealerCardCount = 2
        cardCount += 4

    if clickedButton == 'Hit':
        clickedButton = 'none'
        if gamerCardCount == 3:
            gamerCard3 = Cards(410, 260, "Images\Cards\\" + cardDesk[cardCount][0] + cardDesk[cardCount][1] + ".png")
            priceOfGamerCard3, lightGamerA = determineCardPrice(gamerSum, cardDesk[cardCount][0], lightGamerA)
            gamerSum += priceOfGamerCard3
            if gamerSum > 21 and lightGamerA == 1:
                gamerSum -= 10
                lightGamerA = 0
        elif gamerCardCount == 4:
            gamerCard4 = Cards(430, 260, "Images\Cards\\" + cardDesk[cardCount][0] + cardDesk[cardCount][1] + ".png")
            priceOfGamerCard4, lightGamerA = determineCardPrice(gamerSum, cardDesk[cardCount][0], lightGamerA)
            gamerSum += priceOfGamerCard4
            if gamerSum > 21 and lightGamerA == 1:
                gamerSum -= 10
                lightGamerA = 0
        elif gamerCardCount == 5:
            gamerCard5 = Cards(450, 260, "Images\Cards\\" + cardDesk[cardCount][0] + cardDesk[cardCount][1] + ".png")
            priceOfGamerCard5, lightGamerA = determineCardPrice(gamerSum, cardDesk[cardCount][0], lightGamerA)
            gamerSum += priceOfGamerCard5
            if gamerSum > 21 and lightGamerA == 1:
                gamerSum -= 10
                lightGamerA = 0
        elif gamerCardCount == 6:
            gamerCard6 = Cards(470, 260, "Images\Cards\\" + cardDesk[cardCount][0] + cardDesk[cardCount][1] + ".png")
            priceOfGamerCard6, lightGamerA = determineCardPrice(gamerSum, cardDesk[cardCount][0], lightGamerA)
            gamerSum += priceOfGamerCard6
            if gamerSum > 21 and lightGamerA == 1:
                gamerSum -= 10
                lightGamerA = 0
        elif gamerCardCount == 7:
            gamerCard7 = Cards(490, 260, "Images\Cards\\" + cardDesk[cardCount][0] + cardDesk[cardCount][1] + ".png")
            priceOfGamerCard7, lightGamerA = determineCardPrice(gamerSum, cardDesk[cardCount][0], lightGamerA)
            gamerSum += priceOfGamerCard7
            if gamerSum > 21 and lightGamerA == 1:
                gamerSum -= 10
                lightGamerA = 0
        elif gamerCardCount == 8:
            gamerCard8 = Cards(510, 260, "Images\Cards\\" + cardDesk[cardCount][0] + cardDesk[cardCount][1] + ".png")
            priceOfGamerCard8, lightGamerA = determineCardPrice(gamerSum, cardDesk[cardCount][0], lightGamerA)
            gamerSum += priceOfGamerCard8
            if gamerSum > 21 and lightGamerA == 1:
                gamerSum -= 10
                lightGamerA = 0

    if clickedButton == 'Stand':
        cardAnimationCount += 1
        if cardAnimationCount == 1:
            dealerCard2 = Cards(410, 80, "Images\Cards\\Animation1.png")
        elif cardAnimationCount == 2:
            dealerCard2 = Cards(415, 80, "Images\Cards\\Animation2.png")
        elif cardAnimationCount == 3:
            dealerCard2 = Cards(425, 80, "Images\Cards\\Animation3.png")
        elif cardAnimationCount == 4:
            dealerCard2 = Cards(425, 80, "Images\Cards\\Animation4.png")
        elif cardAnimationCount == 5:
            dealerCard2 = Cards(420, 80, "Images\Cards\\Animation5.png")
        elif cardAnimationCount == 6:
            dealerCard2 = realDealerCard2
        elif cardAnimationCount == 9:
            dealerSum += priceOfDealerCard2
            while dealerSum < 17:
                dealerCardCount += 1
                cardCount += 1
                if dealerCardCount == 3:
                    dealerCard3 = Cards(430, 80,
                                        "Images\Cards\\" + cardDesk[cardCount][0] + cardDesk[cardCount][1] + ".png")
                    priceOfDealerCard3, lightDealerA = determineCardPrice(dealerSum, cardDesk[cardCount][0],
                                                                          lightDealerA)
                    dealerSum += priceOfDealerCard3
                    if dealerSum > 21 and lightDealerA == 1:
                        dealerSum -= 10
                        lightDealerA = 0
                elif dealerCardCount == 4:
                    dealerCard4 = Cards(450, 80,
                                        "Images\Cards\\" + cardDesk[cardCount][0] + cardDesk[cardCount][1] + ".png")
                    priceOfDealerCard4, lightDealerA = determineCardPrice(dealerSum, cardDesk[cardCount][0],
                                                                          lightDealerA)
                    dealerSum += priceOfDealerCard4
                    if dealerSum > 21 and lightDealerA == 1:
                        dealerSum -= 10
                        lightDealerA = 0
                elif dealerCardCount == 5:
                    dealerCard5 = Cards(470, 80,
                                        "Images\Cards\\" + cardDesk[cardCount][0] + cardDesk[cardCount][1] + ".png")
                    priceOfDealerCard5, lightDealerA = determineCardPrice(dealerSum, cardDesk[cardCount][0],
                                                                          lightDealerA)
                    dealerSum += priceOfDealerCard5
                    if dealerSum > 21 and lightDealerA == 1:
                        dealerSum -= 10
                        lightDealerA = 0
                elif dealerCardCount == 6:
                    dealerCard6 = Cards(490, 80,
                                        "Images\Cards\\" + cardDesk[cardCount][0] + cardDesk[cardCount][1] + ".png")
                    priceOfDealerCard6, lightDealerA = determineCardPrice(dealerSum, cardDesk[cardCount][0],
                                                                          lightDealerA)
                    dealerSum += priceOfDealerCard6
                    if dealerSum > 21 and lightDealerA == 1:
                        dealerSum -= 10
                        lightDealerA = 0
                elif dealerCardCount == 7:
                    dealerCard7 = Cards(510, 80,
                                        "Images\Cards\\" + cardDesk[cardCount][0] + cardDesk[cardCount][1] + ".png")
                    priceOfDealerCard7, lightDealerA = determineCardPrice(dealerSum, cardDesk[cardCount][0],
                                                                          lightDealerA)
                    dealerSum += priceOfDealerCard7
                    if dealerSum > 21 and lightDealerA == 1:
                        dealerSum -= 10
                        lightDealerA = 0
                elif dealerCardCount == 8:
                    dealerCard8 = Cards(530, 80,
                                        "Images\Cards\\" + cardDesk[cardCount][0] + cardDesk[cardCount][1] + ".png")
                    priceOfDealerCard8, lightDealerA = determineCardPrice(dealerSum, cardDesk[cardCount][0],
                                                                          lightDealerA)
                    dealerSum += priceOfDealerCard8
                    if dealerSum > 21 and lightDealerA == 1:
                        dealerSum -= 10
                        lightDealerA = 0
            if dealerCardCount == 2:
                canFinish = True
            clickedButton = 'none'
            needFinish = True

    if clickedButton == 'Double':

        rendersChip1.x += 20
        if chipsCount > 1:
            rendersChip2.x += 20
            if chipsCount > 2:
                rendersChip3.x += 20
                if chipsCount > 3:
                    rendersChip4.x += 20
                    if chipsCount > 4:
                        rendersChip5.x += 20

        gamerCard3 = Cards(410, 260, "Images\Cards\\" + cardDesk[cardCount][0] + cardDesk[cardCount][1] + ".png")
        valueOfGamerCard3 = cardDesk[cardCount][0]
        priceOfGamerCard3, lightGamerA = determineCardPrice(gamerSum, cardDesk[cardCount][0], lightGamerA)
        gamerSum += priceOfGamerCard3
        if gamerSum > 21 and lightGamerA == 1:
            gamerSum -= 10
            lightGamerA = 0

        doublesRender = True
        clickedButton = 'none'

    if doublesRender == True:
        if doublesChip1.x < 340:
            doublesChip1.x += 40
            doublesChip1.y -= 20
        else:
            doublesChip1.x = 369
            doublesChip1.y = 400
        doublesChip1.render()
        if chipsCount > 1:
            if doublesChip2.x < 340:
                doublesChip2.x += 40
                doublesChip2.y -= 20
            else:
                doublesChip2.x = 369
                doublesChip2.y = 395
            doublesChip2.render()
            if chipsCount > 2:
                if doublesChip3.x < 340:
                    doublesChip3.x += 40
                    doublesChip3.y -= 20
                else:
                    doublesChip3.x = 369
                    doublesChip3.y = 390
                doublesChip3.render()
                if chipsCount > 3:
                    if doublesChip4.x < 340:
                        doublesChip4.x += 40
                        doublesChip4.y -= 20
                    else:
                        doublesChip4.x = 369
                        doublesChip4.y = 385
                    doublesChip4.render()
                    if chipsCount > 4:
                        if doublesChip5.x < 340:
                            doublesChip5.x += 40
                            doublesChip5.y -= 20
                        else:
                            doublesChip5.x = 369
                            doublesChip5.y = 380
                        doublesChip5.render()

    if insuranceIsActive == True:
        if insuranceChip1.y > 150:
            insuranceChip1.x += 20
            insuranceChip1.y -= 70
        insuranceChip1.render()
        if chipsCount > 1:
            if insuranceChip2.y > 145:
                insuranceChip2.x += 20
                insuranceChip2.y -= 70
            insuranceChip2.render()
            if chipsCount > 2:
                if insuranceChip3.y > 140:
                    insuranceChip3.x += 20
                    insuranceChip3.y -= 70
                insuranceChip3.render()
                if chipsCount > 3:
                    if insuranceChip4.y > 135:
                        insuranceChip4.x += 20
                        insuranceChip4.y -= 70
                    insuranceChip4.render()
                    if chipsCount > 4:
                        if insuranceChip5.y > 130:
                            insuranceChip5.x += 20
                            insuranceChip5.y -= 70
                        insuranceChip5.render()

    if gamerCardCount > 0:

        if gamerCard1IsRender == False:
            if backCard.y < 280:
                backCard.x -= 60
                backCard.y += 40
                backCard.render()
            else:
                backCard.x = 800
                backCard.y = 0
                gamerCard1IsRender = True
        else:
            gamerCard1.render()

            if dealerCard1IsRender == True and gamerCard2IsRender == False:
                if backCard.y < 280:
                    backCard.x -= 60
                    backCard.y += 40
                    backCard.render()
                else:
                    backCard.x = 800
                    backCard.y = 0
                    gamerCard2IsRender = True
            elif dealerCard1IsRender == True:
                gamerCard2.render()

                if gamerCardCount > 2 and gamerCard3IsRender == False:
                    if backCard.y < 280:
                        backCard.x -= 60
                        backCard.y += 40
                        backCard.render()
                    else:
                        backCard.x = 800
                        backCard.y = 0
                        gamerCard3IsRender = True
                        gamerCard3.render()
                        canFinish = True
                        if doublesRender == True:
                            buttonQuantity = -1
                            if gamerSum <= 21:
                                clickedButton = 'Stand'
                                canFinish = False
                            else:
                                needFinish = True
                elif gamerCardCount > 2:
                    gamerCard3.render()

                    if gamerCardCount > 3 and gamerCard4IsRender == False:
                        if backCard.y < 280:
                            backCard.x -= 60
                            backCard.y += 40
                            backCard.render()
                        else:
                            backCard.x = 800
                            backCard.y = 0
                            gamerCard4IsRender = True
                            gamerCard4.render()
                            canFinish = True
                    elif gamerCardCount > 3:
                        gamerCard4.render()

                        if gamerCardCount > 4 and gamerCard5IsRender == False:
                            if backCard.y < 280:
                                backCard.x -= 60
                                backCard.y += 40
                                backCard.render()
                            else:
                                backCard.x = 800
                                backCard.y = 0
                                gamerCard5IsRender = True
                                gamerCard5.render()
                                canFinish = True
                        elif gamerCardCount > 4:
                            gamerCard5.render()

                            if gamerCardCount > 5 and gamerCard6IsRender == False:
                                if backCard.y < 280:
                                    backCard.x -= 60
                                    backCard.y += 40
                                    backCard.render()
                                else:
                                    backCard.x = 800
                                    backCard.y = 0
                                    gamerCard6IsRender = True
                                    gamerCard6.render()
                                    canFinish = True
                            elif gamerCardCount > 5:
                                gamerCard6.render()

                                if gamerCardCount > 6 and gamerCard7IsRender == False:
                                    if backCard.y < 280:
                                        backCard.x -= 60
                                        backCard.y += 40
                                        backCard.render()
                                    else:
                                        backCard.x = 800
                                        backCard.y = 0
                                        gamerCard7IsRender = True
                                        gamerCard7.render()
                                        canFinish = True
                                elif gamerCardCount > 6:
                                    gamerCard7.render()

                                    if gamerCardCount > 7 and gamerCard8IsRender == False:
                                        if backCard.y < 280:
                                            backCard.x -= 60
                                            backCard.y += 40
                                            backCard.render()
                                        else:
                                            backCard.x = 800
                                            backCard.y = 0
                                            gamerCard8IsRender = True
                                            gamerCard8.render()
                                            canFinish = True
                                    elif gamerCardCount > 7:
                                        gamerCard8.render()

    if dealerCardCount > 0:

        if gamerCard1IsRender == True and dealerCard1IsRender == False:
            if backCard.x > 500:
                backCard.x -= 60
                backCard.y += 10
                backCard.render()
            else:
                backCard.x = 800
                backCard.y = 0
                dealerCard1IsRender = True
        elif gamerCard1IsRender == True:
            dealerCard1.render()

            if gamerCard2IsRender == True and dealerCard2IsRender == False:
                if backCard.x > 500:
                    backCard.x -= 60
                    backCard.y += 10
                    backCard.render()
                else:
                    backCard.x = 800
                    backCard.y = 0
                    dealerCard2IsRender = True
                    canFinish = True
            elif gamerCard2IsRender == True:
                dealerCard2.render()

                if dealerCardCount > 2 and dealerCard3IsRender == False:
                    if backCard.x >500:
                        backCard.x -= 60
                        backCard.y += 10
                        backCard.render()
                    else:
                        backCard.x = 800
                        backCard.y = 0
                        dealerCard3IsRender = True
                        dealerCard3.render()
                        if dealerCardCount == 3:
                            canFinish = True
                elif dealerCardCount > 2:
                    dealerCard3.render()

                    if dealerCardCount > 3 and dealerCard4IsRender == False:
                        if backCard.x > 500:
                            backCard.x -= 60
                            backCard.y += 10
                            backCard.render()
                        else:
                            backCard.x = 800
                            backCard.y = 0
                            dealerCard4IsRender = True
                            dealerCard4.render()
                            if dealerCardCount == 4:
                                canFinish = True
                    elif dealerCardCount > 3:
                        dealerCard4.render()

                        if dealerCardCount > 4 and dealerCard5IsRender == False:
                            if backCard.x > 500:
                                backCard.x -= 60
                                backCard.y += 10
                                backCard.render()
                            else:
                                backCard.x = 800
                                backCard.y = 0
                                dealerCard5IsRender = True
                                dealerCard5.render()
                                if dealerCardCount == 5:
                                    canFinish = True
                        elif dealerCardCount > 4:
                            dealerCard5.render()

                            if dealerCardCount > 5 and dealerCard6IsRender == False:
                                if backCard.x > 500:
                                    backCard.x -= 60
                                    backCard.y += 10
                                    backCard.render()
                                else:
                                    backCard.x = 800
                                    backCard.y = 0
                                    dealerCard6IsRender = True
                                    dealerCard6.render()
                                    if dealerCardCount == 6:
                                        canFinish = True
                            elif dealerCardCount > 5:
                                dealerCard6.render()

                                if dealerCardCount > 6 and dealerCard7IsRender == False:
                                    if backCard.x > 500:
                                        backCard.x -= 60
                                        backCard.y += 10
                                        backCard.render()
                                    else:
                                        backCard.x = 800
                                        backCard.y = 0
                                        dealerCard7IsRender = True
                                        dealerCard7.render()
                                        if dealerCardCount == 7:
                                            canFinish = True
                                elif dealerCardCount > 6:
                                    dealerCard7.render()

                                    if dealerCardCount > 7 and dealerCard8IsRender == False:
                                        if backCard.x > 500:
                                            backCard.x -= 60
                                            backCard.y += 10
                                            backCard.render()
                                        else:
                                            backCard.x = 800
                                            backCard.y = 0
                                            dealerCard8IsRender = True
                                            dealerCard8.render()
                                            if dealerCardCount == 8:
                                                canFinish = True
                                    elif dealerCardCount > 7:
                                        dealerCard8.render()

    if buttonQuantity == 0:
        buttonQuantity = 3

        if gamerCardCount == 2 and dealerCardCount == 2:
            if valueOfGamerCard1 == valueOfGamerCard2 and valueOfDealerCard1 == 'A':
                buttonQuantity += 2
            elif valueOfGamerCard1 == valueOfGamerCard2 or valueOfDealerCard1 == 'A':
                buttonQuantity += 1

        firstButton = Buttons(245, 495, "Images\Buttons\Hit.png")
        firstButtonActive = Buttons(245, 495, "Images\Buttons\Hit active.png")
        secondButton = Buttons(310, 495, "Images\Buttons\Stand.png")
        secondButtonActive = Buttons(310, 495, "Images\Buttons\Stand active.png")
        thirdButton = Buttons(375, 495, "Images\Buttons\Double.png")
        thirdButtonActive = Buttons(375, 495, "Images\Buttons\Double active.png")
        if buttonQuantity == 4 and valueOfDealerCard1 == 'A':
            fourthButton = Buttons(440, 495, "Images\Buttons\Yes.png")
            fourthButtonActive = Buttons(440, 495, "Images\Buttons\Yes active.png")
        else:
            fourthButton = Buttons(440, 495, "Images\Buttons\Split.png")
            fourthButtonActive = Buttons(440, 495, "Images\Buttons\Split active.png")
        fivethButton = Buttons(505, 495, "Images\Buttons\Yes.png")
        fivethButtonActive = Buttons(505, 495, "Images\Buttons\Yes active.png")

    if buttonQuantity > 0:
        if mousePos[0] > 245 and mousePos[0] < 245 + 60 and \
                        mousePos[1] > 495 and mousePos[1] < 555:
            firstButtonActive.render()
        else:
            firstButton.render()

        if mousePos[0] > 310 and mousePos[0] < 310 + 60 and \
                        mousePos[1] > 495 and mousePos[1] < 555:
            secondButtonActive.render()
        else:
            secondButton.render()

        if mousePos[0] > 375 and mousePos[0] < 375 + 60 and \
                        gamerCardCount == 2 and mousePos[1] > 495 and mousePos[1] < 555 and gamerDepozit >= gamerBet:
            thirdButtonActive.render()
        elif gamerCardCount == 2 and gamerDepozit >= gamerBet:
            thirdButton.render()

        if buttonQuantity == 4 and mousePos[0] > 440 and mousePos[0] < 440 + 60 and \
                        mousePos[1] > 495 and mousePos[1] < 555 and insuranceIsActive == False:
            fourthButtonActive.render()
        elif buttonQuantity == 4 and insuranceIsActive == False:
            fourthButton.render()

        if buttonQuantity == 5 and mousePos[0] > 505 and mousePos[0] < 505 + 60 and \
                        mousePos[1] > 495 and mousePos[1] < 555 and insuranceIsActive == False:
            fivethButtonActive.render()
        elif buttonQuantity == 5 and insuranceIsActive == False:
            fivethButton.render()

    gameScreen.blit(depozitText.render("Money: "+ str(gamerDepozit) + " $", 1, (255, 255, 255)), (30, 576))
    if takeABet == True:
        gameScreen.blit(betText.render("Bet: " + str(gamerBet) + " $", 1, (255, 255, 255)), (350, 576))

    if dealerCard2IsRender == True:
        pygame.draw.rect(gameScreen, (255, 255, 255), [320, 80, 22, 16])
        if dealerSum < 10:
            xPosOfDealerSumText = 327
        else:
            xPosOfDealerSumText = 322
        gameScreen.blit(dealerSumText.render(str(dealerSum), 1, (0, 0, 0)), (xPosOfDealerSumText, 81))

        pygame.draw.rect(gameScreen, (255, 255, 255), [340, 260, 22, 16])
        if gamerSum < 10:
            xPosOfGamerSumText = 347
        else:
            xPosOfGamerSumText = 342
        gameScreen.blit(gamerSumText.render(str(gamerSum), 1, (0, 0, 0)), (xPosOfGamerSumText, 261))

    for i in pygame.event.get():

        if i.type == pygame.QUIT:
            sys.exit()

        if mousePos[0] > 245 and mousePos[0] < 245 + 60 and buttonQuantity > 0 and \
                        mousePos[1] > 495 and mousePos[1] < 555 and i.type == pygame.MOUSEBUTTONDOWN and i.button == 1:
            clickedButton = 'Hit'
            canFinish = False
            buttonQuantity = 0
            xPosOfFirstButtons = 375
            xPosOfSecondButtons = 375
            xPosOfThirdButtons = 375
            gamerCardCount += 1
            cardCount += 1

        if mousePos[0] > 310 and mousePos[0] < 310 + 60 and buttonQuantity > 0 and \
                        mousePos[1] > 495 and mousePos[1] < 555 and i.type == pygame.MOUSEBUTTONDOWN and i.button == 1:
            clickedButton = 'Stand'
            canFinish = False
            buttonQuantity = -1

        if mousePos[0] > 375 and mousePos[0] < 375 + 60 and gamerCardCount == 2 and \
                        mousePos[1] > 495 and mousePos[1] < 555 and gamerDepozit >= gamerBet  and \
                        i.type == pygame.MOUSEBUTTONDOWN and i.button == 1:
            clickedButton = 'Double'
            canFinish = False
            gamerDepozit -= gamerBet
            gamerBet *= 2
            buttonQuantity = -1
            gamerCardCount += 1
            cardCount += 1

        if buttonQuantity == 4 and mousePos[0] > 440 and mousePos[0] < 440 + 60 and \
                        mousePos[1] > 495 and mousePos[1] < 555 and valueOfDealerCard1 == 'A' and \
                        i.type == pygame.MOUSEBUTTONDOWN and i.button == 1:
            clickedButton = 'Insurance'
            insuranceIsActive = True

        elif buttonQuantity == 4 and mousePos[0] > 440 and mousePos[0] < 440 + 60 and \
                        mousePos[1] > 495 and mousePos[1] < 555 and i.type == pygame.MOUSEBUTTONDOWN and i.button == 1:
            clickedButton = 'Split'

        if buttonQuantity == 5 and mousePos[0] > 505 and mousePos[0] < 505 + 60 and \
                        mousePos[1] > 495 and mousePos[1] < 555 and i.type == pygame.MOUSEBUTTONDOWN and i.button == 1:
            clickedButton = 'Insurance'
            gamerDepozit -= gamerBet

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