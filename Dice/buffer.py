import pygame, sys
import time
import random
from pygame.locals import *
pygame.font.init()

window = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Buffer")




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



timeToPayCredit(300, 200)