from Snake import *
from Food import *
import os
import pygame

class App():
    def __init__(self):
        pygame.init()
        self.width = 500
        self.height = 500
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Snake")
        pygame.display.set_icon(pygame.image.load('images\icon.png'))
        self.font = pygame.font.SysFont('Comic Sans MS', 20)
        self.screen = pygame.display.set_mode([self.width, self.height])
        self.snake = Snake(self.width, self.height)
        self.food = Food(self.width, self.height)
        self.fail_sounds = self.GetOggFiles("sounds\\fail")

    def Run(self):
        clock = pygame.time.Clock()
        self.StartMusic()
        self.DrawWelcome(clock)
        while True:
            tmp_direction = None
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    if (event.key == pygame.K_LEFT and self.snake.direction != pygame.K_RIGHT) or\
                            (event.key == pygame.K_RIGHT and self.snake.direction != pygame.K_LEFT) or\
                            (event.key == pygame.K_UP and self.snake.direction != pygame.K_DOWN) or\
                            (event.key == pygame.K_DOWN and self.snake.direction != pygame.K_UP):
                        tmp_direction = event.key

            if tmp_direction != None:
                self.snake.direction = tmp_direction

            self.screen.fill((255, 255, 255))
            self.snake.Update(self.screen, self.food)
            self.food.Update(self.screen, self.snake)

            self.DrawGrid()
            if not self.snake.is_dead:
                self.DrawText(self.food)
            else:
                self.GameOver(clock)
                return

            pygame.display.update()

            if not pygame.mixer.music.get_busy():
                self.StartMusic()

            clock.tick(10)

    def DrawText(self, food):
        self.DrawPoints()
        self.DrawBonus(food)

    def DrawBonus(self, food):
        for dish in food.dishes:
            if dish.time != 0:
                text = self.font.render('Bonus: ' + str((dish.time - (datetime.datetime.now() - dish.added_time).seconds)), True, (255, 0, 0))
                self.screen.blit(text, (0, self.height - text.get_height()))

    def DrawPoints(self):
        points = self.font.render("Score: " + str(self.snake.points), True, (0, 0, 0))
        self.screen.blit(points, (0, 0))

    def DrawGrid(self):
        for x in range(self.width // 20):
            pygame.draw.aaline(self.screen, (230, 230, 230), (x * 20, 0), (x * 20, self.height))
        for y in range(self.width // 20):
            pygame.draw.aaline(self.screen, (230, 230, 230), (0, y * 20), (self.width, y * 20))

    def GameOver(self, clock):
        pygame.mixer.music.stop()

        font = pygame.font.SysFont('Comic Sans MS', 40)

        text = font.render('GAME OVER ', True, (255, 0, 0))
        self.screen.blit(text, (self.width / 2 - text.get_width() / 2, self.height / 2 - text.get_height() * 2))

        text = font.render('YOUR SCORE : ' + str(self.snake.points), True, (255, 0, 0))
        self.screen.blit(text, (self.width / 2 - text.get_width() / 2, self.height / 2 - text.get_height()))

        text = font.render('ESC/SPACE', True, (255, 0, 0))
        self.screen.blit(text, (self.width / 2 - text.get_width() / 2, self.height / 2 + text.get_height()))


        pygame.display.update()
        self.PlayGameOver()

        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        exit()
                    elif event.key == pygame.K_SPACE:
                        done = True

            clock.tick(20)

    def PlayGameOver(self):
        if len(self.fail_sounds) == 0:
            return

        sound = pygame.mixer.Sound(self.fail_sounds[random.randint(0, len(self.fail_sounds) - 1)])
        sound.set_volume(1.0)
        sound.play()

    def DrawWelcome(self, clock):
        font = pygame.font.SysFont('Comic Sans MS', 14)
        press_color = (255, 0, 0)
        next_color = 'G'

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    return

            self.screen.fill((255, 255, 255))

            text = self.font.render("POINTS", True, press_color)
            self.screen.blit(text, (self.width / 2 - text.get_width() / 2, 0))
            pygame.draw.aaline(self.screen, press_color, (0, text.get_height()), (self.width, text.get_height()))

            text = font.render(" - 1", True, (0, 0, 0))
            self.screen.blit(self.food.simple_images[0], (self.width / 4 - text.get_width() / 2, text.get_height() * 2))
            self.screen.blit(text, (self.width / 4 - text.get_width() / 2 + 20, text.get_height() * 2))

            text = font.render(" - 2", True, (0, 0, 0))
            self.screen.blit(self.food.simple_images[1], (self.width / 4 - text.get_width() / 2, text.get_height() * 4))
            self.screen.blit(text, (self.width / 4 - text.get_width() / 2 + 20, text.get_height() * 4))

            text = font.render(" - 3", True, (0, 0, 0))
            self.screen.blit(self.food.simple_images[2], (self.width / 4 - text.get_width() / 2, text.get_height() * 6))
            self.screen.blit(text, (self.width / 4 - text.get_width() / 2 + 20, text.get_height() * 6))

            text = font.render(" - 4", True, (0, 0, 0))
            self.screen.blit(self.food.simple_images[3], (self.width / 4 - text.get_width() / 2, text.get_height() * 8))
            self.screen.blit(text, (self.width / 4 - text.get_width() / 2 + 20, text.get_height() * 8))

            text = font.render(" - 5", True, (0, 0, 0))
            self.screen.blit(self.food.simple_images[4],
                             (self.width / 4 - text.get_width() / 2, text.get_height() * 10))
            self.screen.blit(text, (self.width / 4 - text.get_width() / 2 + 20, text.get_height() * 10))

            text = font.render(" - 6", True, (0, 0, 0))
            self.screen.blit(self.food.simple_images[5],
                             (self.width / 4 - text.get_width() / 2, text.get_height() * 12))
            self.screen.blit(text, (self.width / 4 - text.get_width() / 2 + 20, text.get_height() * 12))

            text = font.render(" - до 100", True, (0, 0, 0))
            self.screen.blit(self.food.bonus_images[0],
                             (self.width * 3 / 4 - text.get_width() / 2, text.get_height() * 3))
            self.screen.blit(text, (self.width * 3 / 4 - text.get_width() / 2 + 20, text.get_height() * 3))

            text = font.render(" - до 200", True, (0, 0, 0))
            self.screen.blit(self.food.bonus_images[1],
                             (self.width * 3 / 4 - text.get_width() / 2, text.get_height() * 5))
            self.screen.blit(text, (self.width * 3 / 4 - text.get_width() / 2 + 20, text.get_height() * 5))

            text = font.render(" - до 300", True, (0, 0, 0))
            self.screen.blit(self.food.bonus_images[2],
                             (self.width * 3 / 4 - text.get_width() / 2, text.get_height() * 7))
            self.screen.blit(text, (self.width * 3 / 4 - text.get_width() / 2 + 20, text.get_height() * 7))

            text = font.render(" - до 400", True, (0, 0, 0))
            self.screen.blit(self.food.bonus_images[3],
                             (self.width * 3 / 4 - text.get_width() / 2, text.get_height() * 9))
            self.screen.blit(text, (self.width * 3 / 4 - text.get_width() / 2 + 20, text.get_height() * 9))

            text = font.render(" - до 400", True, (0, 0, 0))
            self.screen.blit(self.food.bonus_images[4],
                             (self.width * 3 / 4 - text.get_width() / 2, text.get_height() * 11))
            self.screen.blit(text, (self.width * 3 / 4 - text.get_width() / 2 + 20, text.get_height() * 11))
            pygame.draw.aaline(self.screen, press_color, (0, text.get_height() * 14), (self.width, text.get_height() * 14))

            text = self.font.render("Нажмите любую клавишу", True, press_color)
            self.screen.blit(text, (self.width / 2 - text.get_width() / 2, text.get_height() * 15))
            pygame.display.update()

            lst = list(press_color)
            if next_color == 'R':
                lst[0] += 15
                lst[2] -= 15
            elif next_color == 'G':
                lst[0] -= 15
                lst[1] += 15
            elif next_color == 'B':
                lst[1] -= 15
                lst[2] += 15

            if lst[0] == 255:
                next_color = 'G'
            if lst[1] == 255:
                next_color = 'B'
            if lst[2] == 255:
                next_color = 'R'

            press_color = tuple(lst)

            if not pygame.mixer.music.get_busy():
                self.StartMusic()

            clock.tick(20)

    _music_list = []
    def StartMusic(self):
        if len(self._music_list) == 0:
            self._music_list = self.GetOggFiles("music")

        if len(self._music_list) == 0:
            return

        pygame.mixer.music.load(self._music_list[random.randint(0, len(self._music_list) - 1)])
        pygame.mixer.music.set_volume(0.4)
        pygame.mixer.music.play()

    def GetOggFiles(self, path):
        list = []
        for file in os.listdir(path):
            if file.endswith(".ogg"):
                list.append(os.path.join(path, file))
        return list

while True:
    app = App()
    app.Run()
