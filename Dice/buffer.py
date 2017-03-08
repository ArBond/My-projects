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
    cuvaldaButton = pygame.font.SysFont("Consolas", 28, True)
    stringInfoForPay = pygame.font.SysFont("Consolas", 22)

    redOfYesButton = 200
    blueOfYesButton = 70
    redOfNoButton = 200
    blueOfNoButton = 70
    redOfCuvaldaButton = 200
    blueOfCuvaldaButton = 70

    escape = False

    while True:

        payCreditScreen.fill((255, 225, 160))

        payCreditScreen.blit(stringTimeToPayCredit.render("Пора оплатить долг!", 1, (0, 0, 255)), (120, 40))

        payCreditScreen.blit(stringNeedToPay.render("Ваш депозит: "+ str(gamerDeposit) + "$", 1, (0, 0, 0)), (200, 140))
        payCreditScreen.blit(stringNeedToPay.render("Нужно оплатить: " + str(needToPay) + "$", 1, (0, 0, 0)), (180, 190))

        if gamerDeposit == 0 and needToPay != 0:
            payCreditScreen.blit(stringInfoForPay.render("Вам не хватает денег чтобы оплатить долг!", 1, (255, 0, 0)),
                                 (80, 285))
        elif gamerDeposit > needToPay and escape == True:
            payCreditScreen.blit(stringInfoForPay.render("Вам хватает денег чтобы оплатить долг!", 1, (255, 0, 0)),
                                 (95, 285))

        payCreditScreen.blit(buttons.render("Оплатить", 1, (redOfYesButton, 0, blueOfYesButton)), (110, 380))
        payCreditScreen.blit(buttons.render("Убежать", 1, (redOfNoButton, 0, blueOfNoButton)), (410, 380))
        if gamerDeposit == 0:
            payCreditScreen.blit(cuvaldaButton.render("Позвать КУВАЛДИНА!", 1,
                                                      (redOfCuvaldaButton, 0, blueOfCuvaldaButton)), (187, 430))

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
                        needToPay = 0
                        print("Оплатил!")
            else:
                redOfYesButton = 200
                blueOfYesButton = 70

            if mousePos[0] > 410 and mousePos[0] < 510 and mousePos[1] > 380 and mousePos[1] < 403:
                redOfNoButton = 255
                blueOfNoButton = 0
                if i.type == pygame.MOUSEBUTTONDOWN and i.button == 1:
                    if escape == True:
                        print("Сбежал!")
                    escape = True
            else:
                redOfNoButton = 200
                blueOfNoButton = 70

            if mousePos[0] > 187 and mousePos[0] < 455 and mousePos[1] > 430 and mousePos[1] < 455 and gamerDeposit == 0:
                redOfCuvaldaButton = 255
                blueOfCuvaldaButton = 0
                if i.type == pygame.MOUSEBUTTONDOWN and i.button == 1:
                    print("Кувалда спас!")
            else:
                redOfCuvaldaButton = 200
                blueOfCuvaldaButton = 70

        window.blit(payCreditScreen, (0, 0))
        pygame.display.flip()

timeToPayCredit(100, 200)