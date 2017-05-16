import pygame
import os

class Part():
    def __init__(self, pos):
        self.x = pos[0]
        self.y = pos[1]
        self.is_eat = False

    def Draw(self, screen, color):
        rect = pygame.Rect(self.x, self.y, 20, 20)
        pygame.draw.rect(screen, color, rect)

class Snake():
    def __init__(self, width, height):
        self.tail_color = (0, 255, 0)
        self.eat_color = (0, 0, 255)
        self.screen_width = width
        self.screen_height = height
        self.head_x = width - 60
        self.head_y = 0
        self.direction = pygame.K_LEFT
        self.step = 20
        self.points = 0
        self.is_dead = False
        self.eat = False

        self.head_images = [pygame.image.load('images\\heads\\red_l.png'), pygame.image.load('images\\heads\\red_r.png'), \
                            pygame.image.load('images\\heads\\red_u.png'), pygame.image.load('images\\heads\\red_d.png')]
        self.head_eat_images = [pygame.image.load('images\\heads\\blue_l.png'), pygame.image.load('images\\heads\\blue_r.png'), \
                                pygame.image.load('images\\heads\\blue_u.png'), pygame.image.load('images\\heads\\blue_d.png')]

        self.tail = [Part([self.head_x + 20, 0]), Part([self.head_x + 40, 0])]

    def Update(self, screen, food):
        self.UpdatePosition()
        self.Check(food)
        self.Draw(screen)

    def UpdatePosition(self):
        old_x = self.head_x
        old_y = self.head_y
        old_is_eat = self.eat

        if self.direction == pygame.K_LEFT:
            self.head_x -= 20
        elif self.direction == pygame.K_RIGHT:
            self.head_x += 20
        elif self.direction == pygame.K_UP:
            self.head_y -= 20
        elif self.direction == pygame.K_DOWN:
            self.head_y += 20

        if self.head_x < 0:
            self.head_x = self.screen_width + self.head_x
        if self.head_y < 0:
            self.head_y = self.screen_height + self.head_y
        if self.head_x >= self.screen_width:
            self.head_x = 0
        if self.head_y >= self.screen_height:
            self.head_y = 0

        self.eat = False
        if self.tail[len(self.tail) - 1].is_eat:
            self.tail[len(self.tail) - 1].is_eat = False
            self.tail.append(Part([0, 0]))

        for part in self.tail:
            part.x, old_x = old_x, part.x
            part.y, old_y = old_y, part.y
            part.is_eat, old_is_eat = old_is_eat, part.is_eat

    def Check(self, food):
        for part in self.tail:
            if self.head_x == part.x and self.head_y == part.y:
                self.eat = True
                self.is_dead = True
                return

        x = 0
        while x <= len(food.dishes) - 1:
            if self.head_x == food.dishes[x].coordinates[0] and self.head_y == food.dishes[x].coordinates[1]:
                self.points += food.Eat(x)
                self.eat = True
                continue
            x += 1


    def Draw(self, screen):
        if self.direction == pygame.K_LEFT:
            image = self.head_images[0] if not self.eat else self.head_eat_images[0]
        elif self.direction == pygame.K_RIGHT:
            image = self.head_images[1] if not self.eat else self.head_eat_images[1]
        elif self.direction == pygame.K_UP:
            image = self.head_images[2] if not self.eat else self.head_eat_images[2]
        elif self.direction == pygame.K_DOWN:
            image = self.head_images[3] if not self.eat else self.head_eat_images[3]

        for part in self.tail:
            if not part.is_eat:
                part.Draw(screen, self.tail_color)
            else:
                part.Draw(screen, self.eat_color)

        screen.blit(image, (self.head_x, self.head_y))

    def GetOggFiles(self, path):
        list = []
        for file in os.listdir(path):
            if file.endswith(".ogg"):
                list.append(os.path.join(path, file))
        return list