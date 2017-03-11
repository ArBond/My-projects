# Name: Dice
# Version 4.0
# Release date: --.03.2017
# Developer: ArBond



import pygame, sys
import time
import random
from pygame.locals import *
pygame.font.init()


window = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Dice 4.0")





'''  Начальное меню      Начальное меню     Начальное меню     Начальное меню     Начальное меню     Начальное меню  '''


def goToStartScreen():

    startScreen = pygame.Surface((640, 480))

    stringWelcome = pygame.font.SysFont("Consolas", 50, True)

    buttonPlayWithCopmuter = pygame.font.SysFont("Consolas", 40)
    buttonPlayWithFriend = pygame.font.SysFont("Consolas", 40)
    buttonPlayOne = pygame.font.SysFont("Consolas", 40)
    buttonExit = pygame.font.SysFont("Consolas", 40)
    buttonDescription = pygame.font.SysFont("Consolas", 20)

    greenOfButtonPlayOne = 100
    greenOfButtonPlayWithCopmuter = 100
    greenOfButtonPlayWithFriend = 100
    greenOfButtonExit = 100

    blueOfButtonDescription = 100

    while True:

        startScreen.blit(pygame.image.load("Images\Backgrounds\Start Screen.bmp"), (0, 0))

        startScreen.blit(stringWelcome.render("Добро пожаловать!", 1, (255, 0, 0)), (100, 30))
        startScreen.blit(buttonPlayWithCopmuter.render("Играть c компьютером", 1,
                                                       (255, greenOfButtonPlayWithCopmuter, 255)), (167, 150))
        startScreen.blit(buttonPlayWithFriend.render("Играть с другом", 1,
                                                       (255, greenOfButtonPlayWithFriend, 255)), (275, 205))
        startScreen.blit(buttonPlayOne.render("Играть одному", 1, (255, greenOfButtonPlayOne, 255)), (320, 260))
        startScreen.blit(buttonExit.render("Выйти", 1,(255, greenOfButtonExit, 255)), (495, 335))

        startScreen.blit(buttonDescription.render("Описание игры", 1, (180, 180, blueOfButtonDescription)), (240, 435))

        for i in pygame.event.get():

            if i.type == pygame.QUIT:
                sys.exit()

            mousePos = pygame.mouse.get_pos()

            '''обработка кнопки играть против компьютера'''
            if mousePos[0] > 165 and mousePos[0] < 615 and mousePos[1] > 150 and mousePos[1] < 190:
                greenOfButtonPlayWithCopmuter = 255
                if i.type == pygame.MOUSEBUTTONDOWN and i.button == 1:
                    time.sleep(0.3)
                    return 1
            else:
                greenOfButtonPlayWithCopmuter = 100

            '''обработка кнопки играть с другом'''
            if mousePos[0] > 270 and mousePos[0] < 615 and mousePos[1] > 205 and mousePos[1] < 245:
                greenOfButtonPlayWithFriend = 255
                if i.type == pygame.MOUSEBUTTONDOWN and i.button == 1:
                    print("В разработке...")
            else:
                greenOfButtonPlayWithFriend = 100

            '''обработка кнопки играть одному'''
            if mousePos[0] > 320 and mousePos[0] < 615 and mousePos[1] > 260 and mousePos[1] < 300:
                greenOfButtonPlayOne = 255
                if i.type == pygame.MOUSEBUTTONDOWN and i.button == 1:
                    print("В разработке...")
            else:
                greenOfButtonPlayOne = 100

            '''обработка кнопки Выйти'''
            if mousePos[0] > 490 and mousePos[0] < 615 and mousePos[1] > 333 and mousePos[1] < 373:
                greenOfButtonExit = 255
                if i.type == pygame.MOUSEBUTTONDOWN and i.button == 1:
                    time.sleep(0.3)
                    sys.exit()
            else:
                greenOfButtonExit = 100

            ''' Обработка копки Описание '''
            if mousePos[0] > 240 and mousePos[0] < 385 and mousePos[1] > 435 and mousePos[1] < 455:
                blueOfButtonDescription = 0
                if i.type == pygame.MOUSEBUTTONDOWN and i.button == 1:
                    print("Описание")
            else:
                blueOfButtonDescription = 100

            window.blit(startScreen, (0, 0))
            pygame.display.flip()






'''    окно ввода денег       окно ввода денег     окно ввода денег       окно ввода денег       окно ввода денег   '''


def goToEnterMoneyScreen(callCode):

    enterMoneyScreen = pygame.Surface((640, 480))
    stringInfoAboutDepozit = pygame.font.SysFont("Consolas", 35, True)
    toContinue = pygame.font.SysFont("Consolas", 24, True)

    blueOfStringToContinue = 100

    depositString = ""
    enteringDeposit = pygame.font.SysFont("Arial", 40)

    redOfRect = 0
    greenOfRect = 255
    windowForInter = 'none'
    widthOfWindowLine = 2

    while True:

        enterMoneyScreen.blit(pygame.image.load("Images\Backgrounds\Money screen.bmp"), (0, 0))

        if callCode == 0:
            enterMoneyScreen.blit(stringInfoAboutDepozit.render("Для начала игры вам нужно", 1, (0, 0, 100)), (75, 50))
            enterMoneyScreen.blit(stringInfoAboutDepozit.render("ввести ваш депозит($)", 1, (0, 0, 100)), (130, 100))
        elif callCode == 1:
            enterMoneyScreen.blit(stringInfoAboutDepozit.render("Введите сумму ($)", 1, (0, 0, 100)), (160, 80))

        pygame.draw.rect(enterMoneyScreen, (255, 255, 255), [235, 220, 160, 50])
        pygame.draw.rect(enterMoneyScreen, (redOfRect, greenOfRect, 0), [235, 220, 160, 50], widthOfWindowLine)

        enterMoneyScreen.blit(toContinue.render("Продолжить", 1, (70, 70, blueOfStringToContinue)), (250, 420))

        enterMoneyScreen.blit(enteringDeposit.render(depositString, 1, (0, 0, 0)), (240, 220))

        for i in pygame.event.get():

            if i.type == pygame.QUIT:
                sys.exit()

            '''  Обработка ввода депозита  '''
            if i.type == pygame.KEYDOWN and windowForInter == 'center':
                if (i.key >= pygame.K_0 and i.key <= pygame.K_9 or i.key >= pygame.K_KP0 and i.key <= pygame.K_KP9) \
                        and len(depositString) < 8:
                    depositString += i.unicode
                elif i.key == pygame.K_BACKSPACE:
                    depositString = depositString[:-1]

            '''  Обработка кнопки продолжить'''
            mousePos = pygame.mouse.get_pos()

            if mousePos[0] > 228 and mousePos[0] < 400 and mousePos[1] > 220 and mousePos[1] < 275 and \
                            i.type == pygame.MOUSEBUTTONDOWN and i.button == 1:
                windowForInter = 'center'
                widthOfWindowLine = 3
                redOfRect = 0
                greenOfRect = 255
                depositString = ""

            if mousePos[0] > 260 and mousePos[0] < 380 and mousePos[1] > 420 and mousePos[1] < 445:
                blueOfStringToContinue = 0
                if i.type == pygame.MOUSEBUTTONDOWN and i.button == 1:
                    if depositString != '' and int(str(''.join(depositString))) != 0:
                        return int(str(''.join(depositString)))
                    else:
                        redOfRect = 255
                        greenOfRect = 0
                        widthOfWindowLine = 4
            else:
              blueOfStringToContinue = 100

        window.blit(enterMoneyScreen, (0, 0))
        pygame.display.flip()







'''  Анимация броска     Анимация броска    Анимация броска     Анимация броска    Анимация броска   Анимация броска '''


def throwAnimation(gamerDeposit, needToPay, timeCredit):

    class SpritesOnGameScreen:
        def __init__(self, xpos, ypos, filename):
            self.x = xpos
            self.y = ypos
            self.bitmap = pygame.image.load(filename)
            self.bitmap.set_colorkey((0, 0, 0))

        def render(self):
            gameScreen.blit(self.bitmap, (self.x, self.y))

    gameInfoScreen = pygame.Surface((640, 30))
    gameScreen = pygame.Surface((640, 450))

    stringGamerDepositInfo = pygame.font.SysFont("Consolas", 15)
    stringCreditInfo = pygame.font.SysFont("Consolas", 15)
    stringTimeKreditInfo = pygame.font.SysFont("Consolas", 15)

    delay = 0.05

    x1 = 450
    x2 = 450
    x1Step = random.randint(25, 60)
    x2Step = random.randint(25, 60)

    while delay < 0.5:

        gameInfoScreen.fill((50, 50, 100))
        gameScreen.blit(pygame.image.load("Images\Backgrounds\Game screen.bmp"), (0, 0))

        gameInfoScreen.blit(stringGamerDepositInfo.render("Ваш депозит:" + str(gamerDeposit) + "$", 1, (255, 255, 255)),
                            (8, 8))
        if needToPay != 0:
            gameInfoScreen.blit(stringCreditInfo.render("Долг:" + str(needToPay) + "$", 1, (255, 255, 255)), (270, 8))
            gameInfoScreen.blit(stringTimeKreditInfo.render("Осталось ходов для выплаты:" + str(timeCredit), 1,
                                                        (255, 255, 255)),(390, 8))

        dice1 = random.randint(1, 6)
        if dice1 == 1:
            spriteDice1 = SpritesOnGameScreen(x1, 80, "Images\Dices\One.bmp")
        elif dice1 == 2:
            spriteDice1 = SpritesOnGameScreen(x1, 80, "Images\Dices\Two.bmp")
        elif dice1 == 3:
            spriteDice1 = SpritesOnGameScreen(x1, 80, "Images\Dices\Three.bmp")
        elif dice1 == 4:
            spriteDice1 = SpritesOnGameScreen(x1, 80, "Images\Dices\Four.bmp")
        elif dice1 == 5:
            spriteDice1 = SpritesOnGameScreen(x1, 80, "Images\Dices\Five.bmp")
        else:
            spriteDice1 = SpritesOnGameScreen(x1, 80, "Images\Dices\Six.bmp")
        dice2 = random.randint(1, 6)
        if dice2 == 1:
            spriteDice2 = SpritesOnGameScreen(x2, 250, "Images\Dices\One.bmp")
        elif dice2 == 2:
            spriteDice2 = SpritesOnGameScreen(x2, 250, "Images\Dices\Two.bmp")
        elif dice2 == 3:
            spriteDice2 = SpritesOnGameScreen(x2, 250, "Images\Dices\Three.bmp")
        elif dice2 == 4:
            spriteDice2 = SpritesOnGameScreen(x2, 250, "Images\Dices\Four.bmp")
        elif dice2 == 5:
            spriteDice2 = SpritesOnGameScreen(x2, 250, "Images\Dices\Five.bmp")
        else:
            spriteDice2 = SpritesOnGameScreen(x2, 250, "Images\Dices\Six.bmp")

        x1 -= x1Step
        x2 -= x2Step
        if x1Step > 0:
            x1Step -= random.randint(2, 4)
        if x2Step > 0:
            x2Step -= random.randint(2, 4)

        spriteDice1.render()
        spriteDice2.render()

        time.sleep(delay)
        delay += 0.05

        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                sys.exit()

        window.blit(gameInfoScreen, (0, 0))
        window.blit(gameScreen, (0, 30))
        pygame.display.flip()






'''   Окно берем в долг      Окно берем в долг      Окно берем в долг     Окно берем в долг     Окно берем в долг   '''


def goToTakeCreditScreen():
    takeCreditScreen = pygame.Surface((640, 480))
    stringInfoAboutCredit = pygame.font.SysFont("Consolas", 35, True)
    stringInfoAboutMinCredit = pygame.font.SysFont("Consolas", 28, True)
    stringNeedToPay = pygame.font.SysFont("Consolas", 18, True)
    toContinue = pygame.font.SysFont("Consolas", 20)
    buttons = pygame.font.SysFont("Consolas", 26, True)

    blueOfStringToContinue = 100

    creditString = ""
    enteringCredit = pygame.font.SysFont("Arial", 40)

    redOfRect = 0
    greenOfRect = 255
    windowForInter = 'none'
    widthOfWindowLine = 2

    redOfYesButton = 200
    redOfNoButton = 200
    blueOfYesButton = 70
    blueOfNoButton = 70

    creditEntered = False
    credit = 0

    while True:

        takeCreditScreen.blit(pygame.image.load("Images\Backgrounds\Money screen.bmp"), (0, 0))

        takeCreditScreen.blit(stringInfoAboutCredit.render("Какую сумму хотите взять", 1, (0, 0, 100)), (90, 40))
        takeCreditScreen.blit(stringInfoAboutMinCredit.render("минимум 20($)", 1, (0, 0, 100)), (220, 85))

        pygame.draw.rect(takeCreditScreen, (255, 255, 255), [235, 220, 160, 50])
        pygame.draw.rect(takeCreditScreen, (redOfRect, greenOfRect, 0), [235, 220, 160, 50], widthOfWindowLine)

        if creditEntered == False:
            takeCreditScreen.blit(toContinue.render("Продолжить", 1, (50, 50, blueOfStringToContinue)), (260, 420))

        if creditEntered == True:
            takeCreditScreen.blit(stringNeedToPay.render("Вам нужно будет выплатить " + str(int(credit * 1.3)) +
                                                         "$ не позднее,", 1, (0, 0, 0)), (115, 310))
            takeCreditScreen.blit(stringNeedToPay.render("чем через 10 ходов.", 1, (0, 0, 0)), (215, 340))
            takeCreditScreen.blit(buttons.render("Согласен", 1, (redOfYesButton, 0, blueOfYesButton)), (80, 420))
            takeCreditScreen.blit(buttons.render("Не согласен", 1, (redOfNoButton, 0, blueOfNoButton)), (400, 420))

        takeCreditScreen.blit(enteringCredit.render(creditString, 1, (0, 0, 0)), (240, 220))

        for i in pygame.event.get():

            if i.type == pygame.QUIT:
                sys.exit()

            mousePos = pygame.mouse.get_pos()
            if mousePos[0] > 228 and mousePos[0] < 400 and mousePos[1] > 220 and mousePos[1] < 275 and \
                            i.type == pygame.MOUSEBUTTONDOWN and i.button == 1 and creditEntered == False:
                windowForInter = 'center'
                widthOfWindowLine = 3
                redOfRect = 0
                greenOfRect = 255
                creditString = ""

            '''  Обработка ввода кредита  '''
            if i.type == pygame.KEYDOWN and windowForInter == 'center' and creditEntered == False:
                if (i.key >= pygame.K_0 and i.key <= pygame.K_9 or i.key >= pygame.K_KP0 and i.key <= pygame.K_KP9) \
                        and len(creditString) < 8:
                    creditString += i.unicode
                elif i.key == pygame.K_BACKSPACE:
                    creditString = creditString[:-1]

            '''  Обработка кнопки продолжить '''
            if creditEntered == False:
                if mousePos[0] > 260 and mousePos[0] < 380 and mousePos[1] > 420 and mousePos[1] < 445:
                    blueOfStringToContinue = 0
                    if i.type == pygame.MOUSEBUTTONDOWN and i.button == 1:
                        if creditString != '' and int(str(''.join(creditString))) > 19:
                            credit = int(str(''.join(creditString)))
                            creditEntered = True
                        else:
                            redOfRect = 255
                            greenOfRect = 0
                            widthOfWindowLine = 4
                else:
                    blueOfStringToContinue = 100

            ''' Обработка подтверждения кредита '''
            if creditEntered == True:

                if mousePos[0] > 80 and mousePos[0] < 195 and mousePos[1] > 420 and mousePos[1] < 445:
                    redOfYesButton = 255
                    blueOfYesButton = 0
                    if i.type == pygame.MOUSEBUTTONDOWN and i.button == 1:
                        return credit
                else:
                    redOfYesButton = 200
                    blueOfYesButton = 70

                if mousePos[0] > 400 and mousePos[0] < 555 and mousePos[1] > 420 and mousePos[1] < 445:
                    redOfNoButton = 255
                    blueOfNoButton = 0
                    if i.type == pygame.MOUSEBUTTONDOWN and i.button == 1:
                        return 0
                else:
                    redOfNoButton = 200
                    blueOfNoButton = 70

        window.blit(takeCreditScreen, (0, 0))
        pygame.display.flip()






'''   Когда закончили деньги      Когда закончили деньги       Когда закончили деньги       Когда закончили деньги   '''


def whenMoneyIsOut():

    class SpritesOnRefillDepositScreen:
        def __init__(self, xpos, ypos, filename):
            self.x = xpos
            self.y = ypos
            self.bitmap = pygame.image.load(filename)
            self.bitmap.set_colorkey((255, 255, 255))

        def render(self):
            refillDepositScreen.blit(self.bitmap, (self.x, self.y))

    refillDepositScreen = pygame.Surface((640, 480))

    stringMoneyIsEnded = pygame.font.SysFont("Consolas", 40, True)
    stringAddMoney = pygame.font.SysFont("Consolas", 40)
    stringTakeALoan = pygame.font.SysFont("Consolas", 40)
    stringEnd = pygame.font.SysFont("Consolas", 40)

    man1 = SpritesOnRefillDepositScreen(430, 120, "Images\Sprites\Man without money 1.bmp")
    man2 = SpritesOnRefillDepositScreen(430, 120, "Images\Sprites\Man without money 2.bmp")
    man3 = SpritesOnRefillDepositScreen(430, 120, "Images\Sprites\Man without money 3.bmp")

    greenOfStringAddMoney = 100
    greenOfStringTakeALoan = 100
    greenOfStringEnd = 100

    man = 2

    while True:

        refillDepositScreen.blit(pygame.image.load("Images\Backgrounds\Money screen.bmp"), (0, 0))

        refillDepositScreen.blit(stringMoneyIsEnded.render("У вас закончились деньги!", 1, (0, 50, 200)), (45, 45))

        refillDepositScreen.blit(stringAddMoney.render("Пополнить депозит", 1, (100, greenOfStringAddMoney, 255)),
                                 (50, 160))
        refillDepositScreen.blit(stringTakeALoan.render("Взять кредит", 1, (100, greenOfStringTakeALoan, 255)),
                                 (50, 240))
        refillDepositScreen.blit(stringEnd.render("Закончить", 1, (100, greenOfStringEnd, 255)), (50, 320))

        if man == 1:
            man1.render()
        elif man == 2:
            man2.render()
        else:
            man3.render()

        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                sys.exit()

            mousePos = pygame.mouse.get_pos()
            '''обработка кнопки пополнить депозит'''
            if mousePos[0] > 50 and mousePos[0] < 430 and mousePos[1] > 160 and mousePos[1] < 195:
                greenOfStringAddMoney = 0
                man = 1
                if i.type == pygame.MOUSEBUTTONDOWN and i.button == 1:
                    return goToEnterMoneyScreen(1), 0, 0
            else:
                greenOfStringAddMoney = 100

            '''обработка кнопки взять кредит'''
            if mousePos[0] > 50 and mousePos[0] < 315 and mousePos[1] > 240 and mousePos[1] < 275:
                greenOfStringTakeALoan = 0
                man = 2
                if i.type == pygame.MOUSEBUTTONDOWN and i.button == 1:
                    gamerDeposit = goToTakeCreditScreen()
                    if gamerDeposit != 0:
                        return gamerDeposit, 11, int(gamerDeposit * 1.3)
            else:
                greenOfStringTakeALoan = 100

            '''обработка кнопки Закончить'''
            if mousePos[0] > 50 and mousePos[0] < 250 and mousePos[1] > 320 and mousePos[1] < 355:
                greenOfStringEnd = 0
                man = 3
                if i.type == pygame.MOUSEBUTTONDOWN and i.button == 1:
                    return 0, 0, 0
            else:
                greenOfStringEnd = 100

            window.blit(refillDepositScreen, (0, 0))
            pygame.display.flip()






'''  Пора погасить долг     Пора погасить долг     Пора погасить долг     Пора погасить долг     Пора погасить долг '''


def timeToPayCredit(gamerDeposit, needToPay):

    payCreditScreen = pygame.Surface((640, 480))

    stringTimeToPayCredit = pygame.font.SysFont("Consolas", 40, True)
    stringNeedToPay = pygame.font.SysFont("Consolas", 26)
    buttons = pygame.font.SysFont("Consolas", 26, True)
    stringInfoForPay = pygame.font.SysFont("Consolas", 22)

    redOfYesButton = 200
    blueOfYesButton = 70
    redOfNoButton = 200
    blueOfNoButton = 70

    clickRunOut = False

    while True:

        payCreditScreen.blit(pygame.image.load("Images\Backgrounds\Money screen.bmp"), (0, 0))

        payCreditScreen.blit(stringTimeToPayCredit.render("Пора оплатить долг!", 1, (0, 0, 100)), (120, 40))

        payCreditScreen.blit(stringNeedToPay.render("Ваш депозит: " + str(gamerDeposit) + "$", 1, (0, 0, 0)),
                             (200, 140))
        payCreditScreen.blit(stringNeedToPay.render("Нужно оплатить: " + str(needToPay) + "$", 1, (0, 0, 0)),
                             (180, 190))

        if gamerDeposit == 0 and needToPay != 0:
            payCreditScreen.blit(stringInfoForPay.render("Вам не хватает денег чтобы оплатить долг!", 1, (255, 0, 0)),
                                 (80, 285))
        elif gamerDeposit > needToPay and clickRunOut == True:
            payCreditScreen.blit(stringInfoForPay.render("Вам хватает денег чтобы оплатить долг!", 1, (255, 0, 0)),
                                 (95, 285))

        payCreditScreen.blit(buttons.render("Оплатить", 1, (redOfYesButton, 0, blueOfYesButton)), (110, 380))
        payCreditScreen.blit(buttons.render("Убежать", 1, (redOfNoButton, 0, blueOfNoButton)), (410, 380))

        for i in pygame.event.get():

            if i.type == pygame.QUIT:
                sys.exit()

            mousePos = pygame.mouse.get_pos()
            if mousePos[0] > 110 and mousePos[0] < 225 and mousePos[1] > 380 and mousePos[1] < 403:
                redOfYesButton = 255
                blueOfYesButton = 0
                if i.type == pygame.MOUSEBUTTONDOWN and i.button == 1:
                    if gamerDeposit < needToPay:
                        needToPay -= gamerDeposit
                        gamerDeposit = 0
                    else:
                        gamerDeposit -= needToPay
                        return gamerDeposit, 'paid'
            else:
                redOfYesButton = 200
                blueOfYesButton = 70

            if mousePos[0] > 410 and mousePos[0] < 510 and mousePos[1] > 380 and mousePos[1] < 403:
                redOfNoButton = 255
                blueOfNoButton = 0
                if i.type == pygame.MOUSEBUTTONDOWN and i.button == 1:
                    if clickRunOut == True or gamerDeposit < needToPay:
                        youIsRunner = random.randint(0, 1)
                        if youIsRunner == 1:
                            return gamerDeposit, 'canRunOut'
                        else:
                            return gamerDeposit, 'canNotRunOut'
                    clickRunOut = True
            else:
                redOfNoButton = 200
                blueOfNoButton = 70

        window.blit(payCreditScreen, (0, 0))
        pygame.display.flip()





'''Закончились деньги и не оплачен долг   Закончились деньги и не оплачен долг   Закончились деньги и не оплачен долг'''


def whenMoneyIsOutAndYouHaveACredit():

    hanaScreen = pygame.Surface((640, 480))

    stringAllIsBad = pygame.font.SysFont("Consolas", 40, True)
    stringYouCantRunOut = pygame.font.SysFont("Consolas", 25)
    buttons = pygame.font.SysFont("Consolas", 35, True)
    cuvaldaButton = pygame.font.SysFont("Consolas", 28, True)

    redOfNoButton = 200
    blueOfNoButton = 70
    redOfCuvaldaButton = 200
    blueOfCuvaldaButton = 70

    canEscape = True

    while True:

        hanaScreen.fill((255, 225, 160))

        hanaScreen.blit(stringAllIsBad.render("У вас закончились деньги.", 1, (0, 0, 255)), (55, 40))
        hanaScreen.blit(stringAllIsBad.render("И на вас еще висит долг!", 1, (0, 0, 255)), (60, 90))

        if canEscape == True:
            hanaScreen.blit(buttons.render("Убежать", 1, (redOfNoButton, 0, blueOfNoButton)), (240, 300))
        else:
            hanaScreen.blit(stringYouCantRunOut.render("Вас догнали!", 1, (0, 0, 0)), (240, 360))
            hanaScreen.blit(cuvaldaButton.render("Позвать КУВАЛДИНА!", 1, (redOfCuvaldaButton, 0, blueOfCuvaldaButton)),
                            (187, 430))

        for i in pygame.event.get():

            if i.type == pygame.QUIT:
                sys.exit()

            mousePos = pygame.mouse.get_pos()

            if mousePos[0] > 240 and mousePos[0] < 375 and mousePos[1] > 300 and mousePos[
                1] < 333 and canEscape == True:
                redOfNoButton = 255
                blueOfNoButton = 0
                if i.type == pygame.MOUSEBUTTONDOWN and i.button == 1:
                    if canEscape == True:
                        canEscape = random.randint(0, 2)
                        if canEscape == 1:
                            return True
                        else:
                            canEscape = False
            else:
                redOfNoButton = 200
                blueOfNoButton = 70

            if mousePos[0] > 187 and mousePos[0] < 455 and mousePos[1] > 430 and mousePos[
                1] < 455 and canEscape == False:
                redOfCuvaldaButton = 255
                blueOfCuvaldaButton = 0
                if i.type == pygame.MOUSEBUTTONDOWN and i.button == 1:
                    canEscape = random.randint(0, 1)
                    if canEscape == 1:
                        return True
                    else:
                        return False
            else:
                redOfCuvaldaButton = 200
                blueOfCuvaldaButton = 70

        window.blit(hanaScreen, (0, 0))
        pygame.display.flip()







''' Игровое окно Играть одному   Игровое окно Играть одному   Игровое окно Играть одному  Игровое окно Играть одному '''


def goToGameOneScreen(gamerDeposit):

    class SpritesOnGameScreen:
        def __init__(self, xpos, ypos, filename):
            self.x = xpos
            self.y = ypos
            self.bitmap = pygame.image.load(filename)
            self.bitmap.set_colorkey((0, 0, 0))

        def render(self):
            gameScreen.blit(self.bitmap, (self.x, self.y))

    gameInfoScreen = pygame.Surface((640, 30))
    gameScreen = pygame.Surface((640, 450))

    stringGamerDepositInfo = pygame.font.SysFont("Consolas", 15)
    stringCreditInfo = pygame.font.SysFont("Consolas", 15)
    stringTimeKreditInfo = pygame.font.SysFont("Consolas", 15)
    stringVashaStavka = pygame.font.SysFont("Consolas", 24)
    stringNaKakojeChisloStavite = pygame.font.SysFont("Consolas", 24)
    stringDiceSumInfo = pygame.font.SysFont("Consolas", 50, True)
    stringStavkaSygrala = pygame.font.SysFont("Consolas", 22)
    stringProigrysh = pygame.font.SysFont("Consolas", 22)
    stringVyigrysh = pygame.font.SysFont("Consolas", 22)
    operationsInfo = pygame.font.SysFont("Consolas", 22)

    spriteDice1 = SpritesOnGameScreen(70, 50, "Images\Dices\One.bmp")
    spriteDice2 = SpritesOnGameScreen(250, 50, "Images\Dices\One.bmp")
    throwButton = SpritesOnGameScreen(460, 65, "Images\Sprites\Throw dices button.bmp")
    throwButtonActive = SpritesOnGameScreen(460, 65, "Images\Sprites\Throw dices button(active).bmp")

    betString = ""
    numberString = ""
    enteringBet = pygame.font.SysFont("Consolas", 25)
    enteringNumber = pygame.font.SysFont("Consolas", 25)

    windowForInter = 'none'

    redOfLeftRect = 255
    greenOfLeftRect = 255
    redOfRightRect = 255
    greenOfRightRect = 255
    lineWidthOfLeftRect = 1
    lineWidthOfRightRect = 1

    needToPay = 0
    timeCredit = 0
    sum = -1

    while True:

        gameInfoScreen.fill((50, 50, 100))
        gameScreen.blit(pygame.image.load("Images\Backgrounds\Game screen.bmp"), (0, 0))

        gameInfoScreen.blit(stringGamerDepositInfo.render("Ваш депозит:" + str(gamerDeposit) + "$", 1, (255, 255, 255)),
                            (8, 8))
        if needToPay != 0:
            gameInfoScreen.blit(stringCreditInfo.render("Долг:" + str(needToPay) + "$", 1, (255, 255, 255)), (270, 8))
            gameInfoScreen.blit(stringTimeKreditInfo.render("Осталось ходов для выплаты:" + str(timeCredit - 1), 1,
                                                        (255, 255, 255)),(390, 8))

        if sum > 1:
            gameScreen.blit(stringDiceSumInfo.render("В ы п а л о : " + str(sum), 1, (255, 255, 0)), (110, 190))

            if gamerNumber != sum:
                gameScreen.blit(stringStavkaSygrala.render("Ставка не сыграла.", 1, (250, 250, 250)), (50, 290))
                gameScreen.blit(stringProigrysh.render("Списано: "+ str(gamerBet)+ "$", 1, (250, 250, 250)), (280, 290))
            else:
                gameScreen.blit(stringStavkaSygrala.render("Ставка сыграла!", 1, (250, 250, 250)), (45, 290))
                gameScreen.blit(stringVyigrysh.render("Вы выиграли: " + str(gamerBet * 6) + "$", 1, (250, 250, 250)),
                                (250, 290))
        if sum == 1:
            gameScreen.blit(operationsInfo.render("Деньги добавлены.", 1, (250, 250, 250)), (50, 290))
        if sum == 0:
            gameScreen.blit(operationsInfo.render("Долг погашен.", 1, (250, 250, 250)), (50, 290))

        spriteDice1.render()
        spriteDice2.render()

        mousePos = pygame.mouse.get_pos()
        if mousePos[0] > 460 and mousePos[0] < 540 and mousePos[1] > 95 and mousePos[1] < 175:
            throwButtonActive.render()
        else:
            throwButton.render()

        gameScreen.blit(stringNaKakojeChisloStavite.render("Сколько выпадет(2-12):", 1, (0, 0, 0)), (50, 360))
        pygame.draw.rect(gameScreen, (170, 255, 170), [356, 358, 40, 25])
        pygame.draw.rect(gameScreen, (redOfRightRect, greenOfRightRect, 0), [356, 358, 40, 25], lineWidthOfRightRect)
        gameScreen.blit(stringVashaStavka.render("Ваша ставка($):", 1, (0, 0, 0)), (50, 400))
        pygame.draw.rect(gameScreen, (170, 255, 170), [280, 398, 117, 25])
        pygame.draw.rect(gameScreen, (redOfLeftRect, greenOfLeftRect, 0), [280, 398, 117, 25], lineWidthOfLeftRect)

        gameScreen.blit(enteringNumber.render(numberString, 1, (0, 0, 0)), (361, 360))
        gameScreen.blit(enteringBet.render(betString, 1, (0, 0, 0)), (282, 400))

        for i in pygame.event.get():

            if i.type == pygame.QUIT:
                sys.exit()

            '''  Выбор окна ввода'''
            if mousePos[0] > 277 and mousePos[0] < 402 and mousePos[1] > 425 and mousePos[1] < 458 and \
                            i.type == pygame.MOUSEBUTTONDOWN and i.button == 1:
                windowForInter = 'Low'
                betString = ""
                lineWidthOfLeftRect = 3
                lineWidthOfRightRect = 1
                redOfLeftRect = 0
                redOfRightRect = 255
                greenOfLeftRect = 255

            elif mousePos[0] > 352 and mousePos[0] < 400 and mousePos[1] > 385 and mousePos[1] < 417 and \
                            i.type == pygame.MOUSEBUTTONDOWN and i.button == 1:
                windowForInter = 'Top'
                numberString = ""
                lineWidthOfLeftRect = 1
                lineWidthOfRightRect = 3
                redOfRightRect = 0
                redOfLeftRect = 255
                greenOfRightRect = 255

            '''  Обработка ввода ставки ($) '''
            if i.type == pygame.KEYDOWN and windowForInter == 'Low':
                if (i.key >= pygame.K_0 and i.key <= pygame.K_9 or i.key >= pygame.K_KP0 and i.key <= pygame.K_KP9) \
                        and len(betString) < 8:
                    betString += i.unicode
                elif i.key == pygame.K_BACKSPACE:
                    betString = betString[:-1]

            '''  Обработка ввода ставки на число (2-12) '''
            if i.type == pygame.KEYDOWN and windowForInter == 'Top':
                if (i.key >= pygame.K_0 and i.key <= pygame.K_9 or i.key >= pygame.K_KP0 and i.key <= pygame.K_KP9) \
                        and len(numberString) < 2:
                    numberString += i.unicode
                elif i.key == pygame.K_BACKSPACE:
                    numberString = numberString[:-1]

            ''' Обработка кнопки бросить кубики'''
            if mousePos[0] > 460 and mousePos[0] < 540 and mousePos[1] > 95 and mousePos[1] < 175 and \
                            i.type == pygame.MOUSEBUTTONDOWN and i.button == 1:
                if numberString != '' and betString != '':
                    gamerNumber = int(str(''.join(numberString)))
                    gamerBet = int(str(''.join(betString)))

                    if gamerNumber > 1 and gamerNumber < 13 and gamerBet != 0 and gamerBet <= gamerDeposit:
                        if timeCredit != 0:
                            timeCredit -= 1
                        throwAnimation(gamerDeposit, needToPay, timeCredit)
                        betString = ""
                        numberString = ""
                        dice1 = random.randint(1, 6)
                        if dice1 == 1:
                            spriteDice1 = SpritesOnGameScreen(70, 50, "Images\Dices\One.bmp")
                        elif dice1 == 2:
                            spriteDice1 = SpritesOnGameScreen(70, 50, "Images\Dices\Two.bmp")
                        elif dice1 == 3:
                            spriteDice1 = SpritesOnGameScreen(70, 50, "Images\Dices\Three.bmp")
                        elif dice1 == 4:
                            spriteDice1 = SpritesOnGameScreen(70, 50, "Images\Dices\Four.bmp")
                        elif dice1 == 5:
                            spriteDice1 = SpritesOnGameScreen(70, 50, "Images\Dices\Five.bmp")
                        else:
                            spriteDice1 = SpritesOnGameScreen(70, 50, "Images\Dices\Six.bmp")
                        dice2 = random.randint(1, 6)
                        if dice2 == 1:
                            spriteDice2 = SpritesOnGameScreen(250, 50, "Images\Dices\One.bmp")
                        elif dice2 == 2:
                            spriteDice2 = SpritesOnGameScreen(250, 50, "Images\Dices\Two.bmp")
                        elif dice2 == 3:
                            spriteDice2 = SpritesOnGameScreen(250, 50, "Images\Dices\Three.bmp")
                        elif dice2 == 4:
                            spriteDice2 = SpritesOnGameScreen(250, 50, "Images\Dices\Four.bmp")
                        elif dice2 == 5:
                            spriteDice2 = SpritesOnGameScreen(250, 50, "Images\Dices\Five.bmp")
                        else:
                            spriteDice2 = SpritesOnGameScreen(250, 50, "Images\Dices\Six.bmp")

                        sum = dice1 + dice2
                        if gamerNumber != sum:
                            gamerDeposit -= gamerBet
                        else:
                            gamerDeposit += gamerBet * 6

                    else:
                        if gamerBet == 0 or gamerBet > gamerDeposit:
                            redOfLeftRect = 255
                            greenOfLeftRect = 0
                            lineWidthOfLeftRect = 3
                        if gamerNumber < 2 or gamerNumber > 12:
                            redOfRightRect = 255
                            greenOfRightRect = 0
                            lineWidthOfRightRect = 3
                else:
                    if betString == '':
                        redOfLeftRect = 255
                        greenOfLeftRect = 0
                        lineWidthOfLeftRect = 3
                    if numberString == '':
                        redOfRightRect = 255
                        greenOfRightRect = 0
                        lineWidthOfRightRect = 3

        if gamerDeposit == 0:
            if timeCredit == 0:
                gamerDeposit, timeCredit, needToPay = whenMoneyIsOut()
                sum = 1
                if gamerDeposit == 0:
                    break
            else:
                return whenMoneyIsOutAndYouHaveACredit()


        if timeCredit == 1:

            gamerDeposit, action = timeToPayCredit(gamerDeposit, needToPay)
            if action == 'Paid':
                timeCredit = 0
                needToPay = 0
                sum = 0
            else:
                return action

        window.blit(gameInfoScreen, (0, 0))
        window.blit(gameScreen, (0, 30))
        pygame.display.flip()






'''    RIP Screen          RIP Screen          RIP Screen         RIP Screen        RIP Screen         RIP Screen    '''


def ripScreen():

    ripScreen = pygame.Surface((640, 480))

    button = pygame.font.SysFont("Consolas", 30, True)

    redOfButton = 200
    blueOfButton = 70

    while True:

        ripScreen.blit(pygame.image.load("R.I.P. Screen.bmp"), (0, 0))

        ripScreen.blit(button.render("Продолжить", 1, (redOfButton, 0, blueOfButton)), (235, 110))

        for i in pygame.event.get():

            if i.type == pygame.QUIT:
                sys.exit()

            mousePos = pygame.mouse.get_pos()
            if mousePos[0] > 230 and mousePos[0] < 410 and mousePos[1] > 110 and mousePos[1] < 140:
                redOfButton = 255
                blueOfButton = 0
                if i.type == pygame.MOUSEBUTTONDOWN and i.button == 1:
                    return
            else:
                redOfButton = 200
                blueOfButton = 70

        window.blit(ripScreen, (0, 0))
        pygame.display.flip()






'''   Н А Ч А Л О     Н А Ч А Л О     Н А Ч А Л О     Н А Ч А Л О     Н А Ч А Л О      Н А Ч А Л О     Н А Ч А Л О   '''

while True:
    selection = goToStartScreen()

    if selection == 1:
        gamerDeposit = goToEnterMoneyScreen(0)
        acton = goToGameOneScreen(gamerDeposit)
        if acton == 'canRunOut':
            print("Легко отделался")
        else:
            print("Поймали")
    elif selection == 2:
        print("В разработке...")
    else:
        print("В разработке...")

# добавить досрочное погашение кредита
# поправить условие появление инфо о сыгравше/не сыгравшей ставке
# ну и доделать финишные скрины