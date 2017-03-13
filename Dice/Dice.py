# Name: Dice
# Version 4.0
# Release date: 14.03.2017
# Developer: ArBond



import pygame, sys
import time
import random
from pygame.locals import *
pygame.font.init()


window = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Dice 4.0")



'''  Инфо по игре       Инфо по игре       Инфо по игре       Инфо по игре       Инфо по игре       Инфо по игре  '''


def infoScreen():

    class SpritesOnInfoScreen:
        def __init__(self, xpos, ypos, filename):
            self.x = xpos
            self.y = ypos
            self.bitmap = pygame.image.load(filename)
            self.bitmap.set_colorkey((255, 255, 255))

        def render(self):
            infoScreen.blit(self.bitmap, (self.x, self.y))

    infoScreen = pygame.Surface((640, 480))

    arrowUp = SpritesOnInfoScreen(540, 50, "Images\Sprites\Arrow up.bmp")
    arrowUpActive = SpritesOnInfoScreen(540, 50, "Images\Sprites\Arrow up active.bmp")
    arrowDown = SpritesOnInfoScreen(540, 390, "Images\Sprites\Arrow down.bmp")
    arrowDownActive = SpritesOnInfoScreen(540, 390, "Images\Sprites\Arrow down active.bmp")

    stringDescription = pygame.font.SysFont("Consolas", 30, True)
    section = pygame.font.SysFont("Consolas", 22, True)
    text = pygame.font.SysFont("Consolas", 16)
    listNumber = pygame.font.SysFont("Consolas", 22, True)
    buttonExit = pygame.font.SysFont("Consolas", 22, True)

    line1In1 = "В данной версии доступен только режим"
    line2In1 = '"Играть одному!"'
    line3In1 = "Вы ставите ставку на число и бросаете"
    line4In1 = "кубики. Игра продолжается до тех пор, пока"
    line5In1 = "вы не захотите уйти. Если все деньги проиграны,"
    line6In1 = "есть возможнось пополнить их или взять кредит."
    line7In1 = "В игре присутствуют персонажи которые не оставят"
    line8In1 = "вас разочарованным."

    line1In2 = "Управление в игре осуществляется только"
    line2In2 = "нажатием кнопки мыши. Ввод данных производится"
    line3In2 = "с клавиатуры набором цифр от 0 до 9. Выбранное"
    line4In2 = "окно ввода выделяется зеленым жирным"
    line5In2 = "прямоугольником(мигающий курсор не поддерживается)."
    line6In2 = "Если введенные данные не удовлетворяют текущему"
    line7In2 = "условию игры, то поле выделяется красным"
    line8In2 = "прямоугольником."

    line1In3 = "Имя:  Dice"
    line2In3 = "Версия:  4.0"
    line3In3 = "Дата выхода:  14.03.2017"
    line4In3 = "Разработчик:  ArBond"
    line5In3 = 'Системные требования:  "Не бзди - потянет!"'

    redOfExitButton = 100
    greenOfEsitButton = 50

    list = 1

    while True:

        infoScreen.blit(pygame.image.load("Images\Backgrounds\Info screen.bmp"), (0, 0))

        infoScreen.blit(stringDescription.render("Описание", 1, (150, 0, 0)), (250, 20))

        mousePos = pygame.mouse.get_pos()
        if list > 1:
            if mousePos[0] > 540 and mousePos[0] < 593 and mousePos[1] > 50 and mousePos[1] < 105:
                arrowUpActive.render()
            else:
                arrowUp.render()
        if list < 3:
            if mousePos[0] > 540 and mousePos[0] < 593 and mousePos[1] > 390 and mousePos[1] < 447:
                arrowDownActive.render()
            else:
                arrowDown.render()

        infoScreen.blit(listNumber.render(str(list), 1, (0, 0, 0)), (35, 430))
        if list == 1:
            infoScreen.blit(section.render("Процесс игры:", 1, (0, 0, 0)), (70, 70))
            infoScreen.blit(text.render(line1In1, 1, (0, 0, 0)), (30, 130))
            infoScreen.blit(text.render(line2In1, 1, (0, 0, 0)), (30, 160))
            infoScreen.blit(text.render(line3In1, 1, (0, 0, 0)), (30, 190))
            infoScreen.blit(text.render(line4In1, 1, (0, 0, 0)), (30, 220))
            infoScreen.blit(text.render(line5In1, 1, (0, 0, 0)), (30, 250))
            infoScreen.blit(text.render(line6In1, 1, (0, 0, 0)), (30, 280))
            infoScreen.blit(text.render(line7In1, 1, (0, 0, 0)), (30, 310))
            infoScreen.blit(text.render(line8In1, 1, (0, 0, 0)), (30, 340))
        elif list == 2:
            infoScreen.blit(section.render("Управление в игре:", 1, (0, 0, 0)), (70, 70))
            infoScreen.blit(text.render(line1In2, 1, (0, 0, 0)), (30, 130))
            infoScreen.blit(text.render(line2In2, 1, (0, 0, 0)), (30, 160))
            infoScreen.blit(text.render(line3In2, 1, (0, 0, 0)), (30, 190))
            infoScreen.blit(text.render(line4In2, 1, (0, 0, 0)), (30, 220))
            infoScreen.blit(text.render(line5In2, 1, (0, 0, 0)), (30, 250))
            infoScreen.blit(text.render(line6In2, 1, (0, 0, 0)), (30, 280))
            infoScreen.blit(text.render(line7In2, 1, (0, 0, 0)), (30, 310))
            infoScreen.blit(text.render(line8In2, 1, (0, 0, 0)), (30, 340))
        else:
            infoScreen.blit(section.render("Общее:", 1, (0, 0, 0)), (70, 70))
            infoScreen.blit(text.render(line1In3, 1, (0, 0, 0)), (30, 130))
            infoScreen.blit(text.render(line2In3, 1, (0, 0, 0)), (30, 160))
            infoScreen.blit(text.render(line3In3, 1, (0, 0, 0)), (30, 190))
            infoScreen.blit(text.render(line4In3, 1, (0, 0, 0)), (30, 220))
            infoScreen.blit(text.render(line5In3, 1, (0, 0, 0)), (30, 250))

        if list == 3:
            infoScreen.blit(buttonExit.render("Выход", 1, (redOfExitButton, greenOfEsitButton, 0)), (290, 430))

        for i in pygame.event.get():

            if i.type == pygame.QUIT:
                sys.exit()

            if mousePos[0] > 540 and mousePos[0] < 593 and mousePos[1] > 50 and mousePos[1] < 105 and \
                i.type == pygame.MOUSEBUTTONDOWN and i.button == 1 and list > 1:
                list -= 1
            if mousePos[0] > 540 and mousePos[0] < 593 and mousePos[1] > 390 and mousePos[1] < 447 and \
                i.type == pygame.MOUSEBUTTONDOWN and i.button == 1 and list < 3:
                list += 1
            if mousePos[0] > 285 and mousePos[0] < 353 and mousePos[1] > 430 and mousePos[1] < 452:
                redOfExitButton = 250
                greenOfEsitButton = 0
                if i.type == pygame.MOUSEBUTTONDOWN and i.button == 1 and list > 1:
                    return
            else:
                redOfExitButton = 100
                greenOfEsitButton = 50

        window.blit(infoScreen, (0, 0))
        pygame.display.flip()




'''  Начальное меню      Начальное меню     Начальное меню     Начальное меню     Начальное меню     Начальное меню  '''


def goToStartScreen():

    startScreen = pygame.Surface((640, 480))

    stringWelcome = pygame.font.SysFont("Consolas", 50, True)

    buttonPlayWithCopmuter = pygame.font.SysFont("Consolas", 40)
    buttonPlayWithFriend = pygame.font.SysFont("Consolas", 40)
    buttonPlayOne = pygame.font.SysFont("Consolas", 40)
    buttonExit = pygame.font.SysFont("Consolas", 40)
    buttonDescription = pygame.font.SysFont("Consolas", 20, True)

    greenOfButtonPlayOne = 100
    greenOfButtonPlayWithCopmuter = 100
    greenOfButtonPlayWithFriend = 100
    greenOfButtonExit = 100

    blueOfButtonDescription = 100

    while True:

        startScreen.blit(pygame.image.load("Images\Backgrounds\Start screen.bmp"), (0, 0))

        startScreen.blit(stringWelcome.render("Добро пожаловать!", 1, (255, 0, 0)), (100, 30))
        startScreen.blit(buttonPlayWithCopmuter.render("Играть c компьютером", 1,
                                                       (255, greenOfButtonPlayWithCopmuter, 255)), (167, 150))
        startScreen.blit(buttonPlayWithFriend.render("Играть с другом", 1,
                                                       (255, greenOfButtonPlayWithFriend, 255)), (275, 205))
        startScreen.blit(buttonPlayOne.render("Играть одному", 1, (255, greenOfButtonPlayOne, 255)), (320, 260))
        startScreen.blit(buttonExit.render("Выйти", 1,(255, greenOfButtonExit, 255)), (495, 335))

        startScreen.blit(buttonDescription.render("Описание игры", 1, (200, 200, blueOfButtonDescription)), (240, 435))

        for i in pygame.event.get():

            if i.type == pygame.QUIT:
                sys.exit()

            mousePos = pygame.mouse.get_pos()

            '''обработка кнопки играть против компьютера'''
            if mousePos[0] > 165 and mousePos[0] < 615 and mousePos[1] > 150 and mousePos[1] < 190:
                greenOfButtonPlayWithCopmuter = 255
                if i.type == pygame.MOUSEBUTTONDOWN and i.button == 1:
                    print("В разработке")
            else:
                greenOfButtonPlayWithCopmuter = 100

            '''обработка кнопки играть с другом'''
            if mousePos[0] > 270 and mousePos[0] < 615 and mousePos[1] > 205 and mousePos[1] < 245:
                greenOfButtonPlayWithFriend = 255
                if i.type == pygame.MOUSEBUTTONDOWN and i.button == 1:
                    print("В разработке")
            else:
                greenOfButtonPlayWithFriend = 100

            '''обработка кнопки играть одному'''
            if mousePos[0] > 320 and mousePos[0] < 615 and mousePos[1] > 260 and mousePos[1] < 300:
                greenOfButtonPlayOne = 255
                if i.type == pygame.MOUSEBUTTONDOWN and i.button == 1:
                    time.sleep(0.3)
                    return 1
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
                    infoScreen()
            else:
                blueOfButtonDescription = 100

            window.blit(startScreen, (0, 0))
            pygame.display.flip()






'''    окно ввода денег       окно ввода денег     окно ввода денег       окно ввода денег       окно ввода денег   '''


def goToEnterMoneyScreen(callCode):
    enterMoneyScreen = pygame.Surface((640, 480))
    stringInfoAboutDepozit = pygame.font.SysFont("Consolas", 35, True)
    toContinue = pygame.font.SysFont("Consolas", 24, True)

    redOfStringToContinue = 120
    blueOfStringToContinue = 50

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

        enterMoneyScreen.blit(toContinue.render("Продолжить", 1, (redOfStringToContinue, 50, blueOfStringToContinue)),
                              (250, 420))

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
                widthOfWindowLine = 4
                redOfRect = 0
                greenOfRect = 255
                depositString = ""

            if mousePos[0] > 260 and mousePos[0] < 380 and mousePos[1] > 420 and mousePos[1] < 445:
                blueOfStringToContinue = 0
                redOfStringToContinue = 250
                if i.type == pygame.MOUSEBUTTONDOWN and i.button == 1:
                    if depositString != '' and int(str(''.join(depositString))) != 0:
                        return int(str(''.join(depositString)))
                    else:
                        redOfRect = 200
                        greenOfRect = 0
                        widthOfWindowLine = 4
            else:
                blueOfStringToContinue = 50
                redOfStringToContinue = 120

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
    x1Step = random.randint(20, 60)
    x2Step = random.randint(30, 60)

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
    toContinue = pygame.font.SysFont("Consolas", 22, True)
    buttons = pygame.font.SysFont("Consolas", 26, True)

    redOfStringToContinue = 120
    blueOfStringToContinue = 50

    creditString = ""
    enteringCredit = pygame.font.SysFont("Arial", 40)

    redOfRect = 0
    greenOfRect = 255
    windowForInter = 'none'
    widthOfWindowLine = 2

    redOfYesButton = 120
    redOfNoButton = 120
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
            takeCreditScreen.blit(toContinue.render("Продолжить", 1, (redOfStringToContinue, 0, blueOfStringToContinue))
                                  , (260, 420))

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
                    redOfStringToContinue = 220
                    if i.type == pygame.MOUSEBUTTONDOWN and i.button == 1:
                        if creditString != '' and int(str(''.join(creditString))) > 19:
                            credit = int(str(''.join(creditString)))
                            creditEntered = True
                        else:
                            redOfRect = 255
                            greenOfRect = 0
                            widthOfWindowLine = 4
                else:
                    blueOfStringToContinue = 50
                    redOfStringToContinue = 120

            ''' Обработка подтверждения кредита '''
            if creditEntered == True:

                if mousePos[0] > 80 and mousePos[0] < 195 and mousePos[1] > 420 and mousePos[1] < 445:
                    redOfYesButton = 255
                    blueOfYesButton = 0
                    if i.type == pygame.MOUSEBUTTONDOWN and i.button == 1:
                        return credit
                else:
                    redOfYesButton = 120
                    blueOfYesButton = 70

                if mousePos[0] > 400 and mousePos[0] < 555 and mousePos[1] > 420 and mousePos[1] < 445:
                    redOfNoButton = 255
                    blueOfNoButton = 0
                    if i.type == pygame.MOUSEBUTTONDOWN and i.button == 1:
                        return 0
                else:
                    redOfNoButton = 120
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

    greenOfStringAddMoney = 110
    greenOfStringTakeALoan = 110
    greenOfStringEnd = 110

    man = 2

    while True:

        refillDepositScreen.blit(pygame.image.load("Images\Backgrounds\Money screen.bmp"), (0, 0))

        refillDepositScreen.blit(stringMoneyIsEnded.render("У вас закончились деньги!", 1, (0, 0, 100)), (45, 45))

        refillDepositScreen.blit(stringAddMoney.render("Пополнить депозит", 1, (50, greenOfStringAddMoney, 200)),
                                 (50, 160))
        refillDepositScreen.blit(stringTakeALoan.render("Взять кредит", 1, (50, greenOfStringTakeALoan, 200)),
                                 (50, 240))
        refillDepositScreen.blit(stringEnd.render("Закончить", 1, (50, greenOfStringEnd, 200)), (50, 320))

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
                greenOfStringAddMoney = 110

            '''обработка кнопки взять кредит'''
            if mousePos[0] > 50 and mousePos[0] < 315 and mousePos[1] > 240 and mousePos[1] < 275:
                greenOfStringTakeALoan = 0
                man = 2
                if i.type == pygame.MOUSEBUTTONDOWN and i.button == 1:
                    gamerDeposit = goToTakeCreditScreen()
                    if gamerDeposit != 0:
                        return gamerDeposit, 11, int(gamerDeposit * 1.3)
            else:
                greenOfStringTakeALoan = 110

            '''обработка кнопки Закончить'''
            if mousePos[0] > 50 and mousePos[0] < 250 and mousePos[1] > 320 and mousePos[1] < 355:
                greenOfStringEnd = 0
                man = 3
                if i.type == pygame.MOUSEBUTTONDOWN and i.button == 1:
                    return 0, 0, 0
            else:
                greenOfStringEnd = 110

        window.blit(refillDepositScreen, (0, 0))
        pygame.display.flip()






'''  Пора погасить долг     Пора погасить долг     Пора погасить долг     Пора погасить долг     Пора погасить долг '''


def timeToPayCredit(gamerDeposit, needToPay):

    payCreditScreen = pygame.Surface((640, 480))

    stringTimeToPayCredit = pygame.font.SysFont("Consolas", 40, True)
    stringNeedToPay = pygame.font.SysFont("Consolas", 24, True)
    buttons = pygame.font.SysFont("Consolas", 26, True)
    stringInfoForPay = pygame.font.SysFont("Consolas", 22)

    redOfYesButton = 120
    blueOfYesButton = 70
    redOfNoButton = 120
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
                redOfYesButton = 220
                blueOfYesButton = 0
                if i.type == pygame.MOUSEBUTTONDOWN and i.button == 1:
                    if gamerDeposit < needToPay:
                        needToPay -= gamerDeposit
                        gamerDeposit = 0
                    else:
                        gamerDeposit -= needToPay
                        return gamerDeposit, 'paid'
            else:
                redOfYesButton = 120
                blueOfYesButton = 70

            if mousePos[0] > 410 and mousePos[0] < 510 and mousePos[1] > 380 and mousePos[1] < 403:
                redOfNoButton = 220
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
                redOfNoButton = 120
                blueOfNoButton = 70

        window.blit(payCreditScreen, (0, 0))
        pygame.display.flip()





'''Закончились деньги и не оплачен долг   Закончились деньги и не оплачен долг   Закончились деньги и не оплачен долг'''


def whenMoneyIsOutAndYouHaveACredit(needToPay):

    hanaScreen = pygame.Surface((640, 480))

    stringAllIsBad = pygame.font.SysFont("Consolas", 40, True)
    button = pygame.font.SysFont("Consolas", 30, True)
    stringNeedToPay = pygame.font.SysFont("Consolas", 30, True)

    redOfButton = 120
    blueOfButton = 70

    while True:

        hanaScreen.blit(pygame.image.load("Images\Backgrounds\Money screen.bmp"), (0, 0))

        hanaScreen.blit(stringAllIsBad.render("У вас закончились деньги.", 1, (0, 0, 100)), (55, 50))
        hanaScreen.blit(stringAllIsBad.render("И на вас еще висит долг!", 1, (0, 0, 100)), (60, 120))
        hanaScreen.blit(stringNeedToPay.render("(" + str(needToPay) + "$)", 1, (0, 0, 100)), (270, 180))

        hanaScreen.blit(button.render("Сбежать", 1, (redOfButton, 0, blueOfButton)), (260, 400))

        for i in pygame.event.get():

            if i.type == pygame.QUIT:
                sys.exit()

            mousePos = pygame.mouse.get_pos()
            ''' Обработка кнопки сбежать'''
            if mousePos[0] > 260 and mousePos[0] < 380 and mousePos[1] > 400 and mousePos[1] < 430:
                redOfButton = 220
                blueOfButton = 0
                if i.type == pygame.MOUSEBUTTONDOWN and i.button == 1:
                    action = random.randint(0, 2)
                    if action == 1:
                        return 'canRunOut'
                    else:
                        return 'canNotRunOut'
            else:
                redOfButton = 120
                blueOfButton = 70

        window.blit(hanaScreen, (0, 0))
        pygame.display.flip()




'''  Нельзя уйти - есть долг       Нельзя уйти - есть долг      Нельзя уйти - есть долг      Нельзя уйти - есть долг '''


def youCanNotExit(needToPay):

    youCanNotExitScreen = pygame.Surface((640, 480))

    stringYouCanNotExit = pygame.font.SysFont("Consolas", 40, True)
    stringNeedToPay = pygame.font.SysFont("Consolas", 30, True)
    buttons = pygame.font.SysFont("Consolas", 30, True)

    redOfContinueButton = 140
    blueOfContinueButton = 70
    redOfRunOutButton = 140
    blueOfRunOutButton = 70

    while True:

        youCanNotExitScreen.blit(pygame.image.load("Images\Backgrounds\Money screen.bmp"), (0, 0))

        youCanNotExitScreen.blit(stringYouCanNotExit.render("Вы не можете уйти", 1, (0, 0, 100)), (130, 50))
        youCanNotExitScreen.blit(stringYouCanNotExit.render("т. к. на вас висит долг!", 1, (0, 0, 100)), (60, 120))
        youCanNotExitScreen.blit(stringNeedToPay.render("(" + str(needToPay) + "$)", 1, (0, 0, 100)), (270, 180))

        youCanNotExitScreen.blit(buttons.render("Продолжить играть", 1, (redOfContinueButton, 0, blueOfContinueButton)),
                                 (180, 290))
        youCanNotExitScreen.blit(buttons.render("Сбежать", 1, (redOfRunOutButton, 0, blueOfRunOutButton)), (260, 370))

        for i in pygame.event.get():

            if i.type == pygame.QUIT:
                sys.exit()

            mousePos = pygame.mouse.get_pos()
            ''' Обработка кнопки продолжить играть'''
            if mousePos[0] > 180 and mousePos[0] < 470 and mousePos[1] > 290 and mousePos[1] < 320:
                redOfContinueButton = 220
                blueOfContinueButton = 0
                if i.type == pygame.MOUSEBUTTONDOWN and i.button == 1:
                    return 'continue'
            else:
                redOfContinueButton = 140
                blueOfContinueButton = 70

            ''' Обработка кнопки сбежать'''
            if mousePos[0] > 260 and mousePos[0] < 380 and mousePos[1] > 370 and mousePos[1] < 400:
                redOfRunOutButton = 220
                blueOfRunOutButton = 0
                if i.type == pygame.MOUSEBUTTONDOWN and i.button == 1:
                    userAction = random.randint(0, 2)
                    if userAction == 1:
                        return 'canRunOut'
                    else:
                        return 'canNotRunOut'
            else:
                redOfRunOutButton = 140
                blueOfRunOutButton = 70

        window.blit(youCanNotExitScreen, (0, 0))
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
    stringOperationsInfo = pygame.font.SysFont("Consolas", 22)
    buttonPayCredit = pygame.font.SysFont("Consolas", 22)
    buttonExit = pygame.font.SysFont("Consolas", 26, True)


    spriteDice1 = SpritesOnGameScreen(70, 50, "Images\Dices\One.bmp")
    spriteDice2 = SpritesOnGameScreen(250, 50, "Images\Dices\One.bmp")
    throwButton = SpritesOnGameScreen(460, 75, "Images\Sprites\Throw dices button.bmp")
    throwButtonActive = SpritesOnGameScreen(460, 75, "Images\Sprites\Throw dices button(active).bmp")

    betString = ""
    numberString = ""
    enteringBet = pygame.font.SysFont("Consolas", 25)
    enteringNumber = pygame.font.SysFont("Consolas", 25)

    windowForInter = 'none'

    blueOfPaycreditButton = 0

    blueOfButtonExit = 0
    redOfLeftRect = 255
    greenOfLeftRect = 255
    redOfRightRect = 255
    greenOfRightRect = 255
    lineWidthOfLeftRect = 1
    lineWidthOfRightRect = 1

    needToPay = 0
    timeCredit = 0
    sum = -1

    throwDice = False
    timer = 0

    while True:

        gameInfoScreen.fill((50, 50, 100))
        gameScreen.blit(pygame.image.load("Images\Backgrounds\Game screen.bmp"), (0, 0))

        gameInfoScreen.blit(stringGamerDepositInfo.render("Ваш депозит:" + str(gamerDeposit) + "$", 1, (255, 255, 255)),
                            (8, 8))
        if needToPay != 0:
            gameInfoScreen.blit(stringCreditInfo.render("Долг:" + str(needToPay) + "$", 1, (255, 255, 255)), (270, 8))
            gameInfoScreen.blit(stringTimeKreditInfo.render("Осталось ходов для выплаты:" + str(timeCredit - 1), 1,
                                                        (255, 255, 255)),(390, 8))
        if needToPay <= gamerDeposit and timeCredit > 1:
            gameScreen.blit(buttonPayCredit.render("Погасить долг", 1, (200, 200, blueOfPaycreditButton)), (450, 20))

        if throwDice == True and sum > 1:
            gameScreen.blit(stringDiceSumInfo.render("В ы п а л о : " + str(sum), 1, (255, 255, 0)), (110, 190))
            if gamerNumber != sum:
                gameScreen.blit(stringStavkaSygrala.render("Ставка не сыграла.", 1, (250, 250, 250)), (50, 290))
                gameScreen.blit(stringProigrysh.render("Списано: "+ str(gamerBet)+ "$", 1, (250, 250, 250)), (280, 290))
            else:
                gameScreen.blit(stringStavkaSygrala.render("Ставка сыграла!", 1, (250, 250, 250)), (45, 290))
                gameScreen.blit(stringVyigrysh.render("Вы выиграли: " + str(gamerBet * 6) + "$", 1, (250, 250, 250)),
                                (250, 290))
        if sum == 1:
            gameScreen.blit(stringOperationsInfo.render("Деньги добавлены.", 1, (250, 250, 250)), (50, 290))
        if sum == 0:
            gameScreen.blit(stringOperationsInfo.render("Долг погашен.", 1, (250, 250, 250)), (50, 290))

        pygame.draw.rect(gameScreen, (255, 200, 200), [490, 375, 80, 25])
        gameScreen.blit(buttonExit.render("Выйти", 1, (0, 0, blueOfButtonExit)), (495, 375))

        spriteDice1.render()
        spriteDice2.render()

        mousePos = pygame.mouse.get_pos()
        if mousePos[0] > 460 and mousePos[0] < 540 and mousePos[1] > 105 and mousePos[1] < 185:
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

            ''' обработка кнопки погасить долг'''
            if needToPay <= gamerDeposit and timeCredit > 1:
                if mousePos[0] > 450 and mousePos[0] < 615 and mousePos[1] > 50 and mousePos[1] < 73:
                    blueOfPaycreditButton = 255
                    if i.type == pygame.MOUSEBUTTONDOWN and i.button == 1:
                        gamerDeposit -= needToPay
                        timeCredit = 0
                        needToPay = 0
                        sum = 0
                else:
                    blueOfPaycreditButton = 0

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

            ''' Обработка кнопки выйти'''
            if mousePos[0] > 490 and mousePos[0] < 570 and mousePos[1] > 405 and mousePos[1] < 430:
                blueOfButtonExit = 200
                if i.type == pygame.MOUSEBUTTONDOWN and i.button == 1:
                    if needToPay == 0:
                        return
                    else:
                        action = youCanNotExit(needToPay)
                        if action != 'continue':
                            return action
            else:
                blueOfButtonExit = 0


            ''' Обработка кнопки бросить кубики'''
            if mousePos[0] > 460 and mousePos[0] < 540 and mousePos[1] > 105 and mousePos[1] < 185 and \
                            i.type == pygame.MOUSEBUTTONDOWN and i.button == 1:
                if numberString != '' and betString != '':
                    gamerNumber = int(str(''.join(numberString)))
                    gamerBet = int(str(''.join(betString)))

                    if gamerNumber > 1 and gamerNumber < 13 and gamerBet != 0 and gamerBet <= gamerDeposit:
                        if timeCredit != 0:
                            timeCredit -= 1
                        throwDice = True
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
                        throwDice = False
                        if gamerBet == 0 or gamerBet > gamerDeposit:
                            redOfLeftRect = 255
                            greenOfLeftRect = 0
                            lineWidthOfLeftRect = 3
                        if gamerNumber < 2 or gamerNumber > 12:
                            redOfRightRect = 255
                            greenOfRightRect = 0
                            lineWidthOfRightRect = 3
                else:
                    throwDice = False
                    if betString == '':
                        redOfLeftRect = 255
                        greenOfLeftRect = 0
                        lineWidthOfLeftRect = 3
                    if numberString == '':
                        redOfRightRect = 255
                        greenOfRightRect = 0
                        lineWidthOfRightRect = 3

        if gamerDeposit == 0:
            timer += 1
            if timer == 200:
                timer = 0
                if timeCredit == 0:
                    gamerDeposit, timeCredit, needToPay = whenMoneyIsOut()
                    sum = 1
                    if gamerDeposit == 0:
                        break
                else:
                    return whenMoneyIsOutAndYouHaveACredit(needToPay)

        if timeCredit == 1:
            timer += 1
            if timer == 200:
                timer = 0
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

    redOfButton = 150
    blueOfButton = 70

    while True:

        ripScreen.blit(pygame.image.load("Images\Backgrounds\R.I.P. Screen.bmp"), (0, 0))

        ripScreen.blit(button.render("Продолжить", 1, (redOfButton, 0, blueOfButton)), (235, 110))

        for i in pygame.event.get():

            if i.type == pygame.QUIT:
                sys.exit()

            mousePos = pygame.mouse.get_pos()
            if mousePos[0] > 230 and mousePos[0] < 410 and mousePos[1] > 110 and mousePos[1] < 140:
                redOfButton = 240
                blueOfButton = 0
                if i.type == pygame.MOUSEBUTTONDOWN and i.button == 1:
                    return
            else:
                redOfButton = 140
                blueOfButton = 70

        window.blit(ripScreen, (0, 0))
        pygame.display.flip()






'''  Не убежали       Не убежали       Не убежали      Не убежали       Не убежали       Не убежали      Не убежали  '''


def youCanNotRunOut():

    class SpritesOnCanNotRunOutScreen:
        def __init__(self, xpos, ypos, filename):
            self.x = xpos
            self.y = ypos
            self.bitmap = pygame.image.load(filename)
            self.bitmap.set_colorkey((255, 255, 255))

        def render(self):
            сanNotRunOutScreen.blit(self.bitmap, (self.x, self.y))

    сanNotRunOutScreen = pygame.Surface((640, 480))

    stringYouCanNotRunOut = pygame.font.SysFont("Consolas", 40, True)
    button = pygame.font.SysFont("Consolas", 26, True)
    stirngAboutKuvalda = pygame.font.SysFont("Consolas", 35, True)

    xPosOfMen1 = -170
    xPosOfMen2 = 600

    yPosOfKuvalda = -350
    kuvaldaStep = 2

    blueOfKuvaldaButton = 120

    sptiteBigBoss = SpritesOnCanNotRunOutScreen(110, 100, "Images\Sprites\Big Boss.bmp")
    speaking = SpritesOnCanNotRunOutScreen(320, 5, "Images\Sprites\Speaking.bmp")

    helpButtonIsClicked = False

    timer = 0

    while True:

        сanNotRunOutScreen.blit(pygame.image.load("Images\Backgrounds\Run out screen.bmp"), (0, 0))
        SpritesOnCanNotRunOutScreen(0, 383, "Images\Sprites\Table.bmp").render()

        SpritesOnCanNotRunOutScreen(xPosOfMen1, 33, "Images\Sprites\Security man left.bmp").render()
        SpritesOnCanNotRunOutScreen(xPosOfMen2, 33, "Images\Sprites\Security man right.bmp").render()

        SpritesOnCanNotRunOutScreen(140, yPosOfKuvalda, "Images\Sprites\Kuvalda.bmp").render()

        if helpButtonIsClicked == False:
            сanNotRunOutScreen.blit(stringYouCanNotRunOut.render("Вас догнали!", 1, (255, 255, 255)), (200, 40))
            сanNotRunOutScreen.blit(button.render("Последний звонок", 1, (255, 255, blueOfKuvaldaButton)), (220, 435))
            sptiteBigBoss.render()
            if xPosOfMen1 < 0:
                xPosOfMen1 += 2
                xPosOfMen2 -= 2

        elif kuvaldaIsHelp == 1 or kuvaldaIsHelp == 2:
            сanNotRunOutScreen.blit(stirngAboutKuvalda.render("Кувалда спас!", 1, (255, 255, 255)), (200, 420))
            if yPosOfKuvalda < 25:
                yPosOfKuvalda += kuvaldaStep
                kuvaldaStep += 0.3
            if xPosOfMen1 > -190:
                xPosOfMen1 -= 2.5
                xPosOfMen2 += 2.5
            else:
                speaking.render()
                timer += 1
                if timer > 400:
                    return 'easyGotOff'

        else:
            sptiteBigBoss.render()
            сanNotRunOutScreen.blit(stirngAboutKuvalda.render("Кувалда очень занят", 1, (255, 255, 255)), (150, 420))
            timer += 1
            if timer > 300:
                return 'bye'

        for i in pygame.event.get():

            if i.type == pygame.QUIT:
                sys.exit()

            mousePos = pygame.mouse.get_pos()

            '''  обработка кнопки посдений звонок'''
            if mousePos[0] > 220 and mousePos[0] < 450 and mousePos[1] > 435 and mousePos[1] < 460 and helpButtonIsClicked == False:
                blueOfKuvaldaButton = 0
                if i.type == pygame.MOUSEBUTTONDOWN and i.button == 1:
                    helpButtonIsClicked = True
                    kuvaldaIsHelp = random.randint(0, 2)
            else:
                blueOfKuvaldaButton = 120

        window.blit(сanNotRunOutScreen, (0, 0))
        pygame.display.flip()






'''   Легко отделался        Легко отделался        Легко отделался        Легко отделался        Легко отделался   '''


def easyGotOff():
    easyGotOffScreen = pygame.Surface((640, 480))

    stringEasyGotOff = pygame.font.SysFont("Consolas", 40, True)
    stirngInfo = pygame.font.SysFont("Consolas", 29)
    button = pygame.font.SysFont("Consolas", 26, True)

    blueOfButton = 100

    while True:

        easyGotOffScreen.blit(pygame.image.load("Images\Backgrounds\Run out screen.bmp"), (0, 0))

        easyGotOffScreen.blit(stringEasyGotOff.render("Вы легко отделались!", 1, (255, 255, 255)), (100, 45))
        easyGotOffScreen.blit(stirngInfo.render("Думаю, вам не стоит некоторое время", 1, (255, 255, 255)), (40, 160))
        easyGotOffScreen.blit(stirngInfo.render("посещать это казино", 1, (255, 255, 255)), (170, 200))
        easyGotOffScreen.blit(button.render("продолжить", 1, (255, 255, blueOfButton)), (250, 400))

        for i in pygame.event.get():

            if i.type == pygame.QUIT:
                sys.exit()

            mousePos = pygame.mouse.get_pos()

            '''  обработка кнопки продолжить '''
            if mousePos[0] > 250 and mousePos[0] < 390 and mousePos[1] > 400 and mousePos[1] < 425:
                blueOfButton = 0
                if i.type == pygame.MOUSEBUTTONDOWN and i.button == 1:
                    return
            else:
                blueOfButton = 100

        window.blit(easyGotOffScreen, (0, 0))
        pygame.display.flip()






'''   Н А Ч А Л О     Н А Ч А Л О     Н А Ч А Л О     Н А Ч А Л О     Н А Ч А Л О      Н А Ч А Л О     Н А Ч А Л О   '''


while True:
    selection = goToStartScreen()

    if selection == 1:
        gamerDeposit = goToEnterMoneyScreen(0)
        action = goToGameOneScreen(gamerDeposit)
        if action == 'canRunOut':
            easyGotOff()
        elif action == 'canNotRunOut':
            action = youCanNotRunOut()
            if action == 'easyGotOff':
                easyGotOff()
            else:
                ripScreen()
    elif selection == 2:
        print("В разработке...")
    else:
        print("В разработке...")