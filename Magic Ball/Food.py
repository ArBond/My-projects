import pygame
import random
import datetime
import os

class Dish():
    def __init__(self, score, image, snake, dishes, weight, height, time=0):
        self.score = score
        self.image = image
        self.time = time
        self.added_time = datetime.datetime.now()
        self.coordinates = self.RandomCoordinates(snake, dishes, weight, height)

    def RandomCoordinates(self, snake, dishes, weight, height):
        coordinates = []
        rand = True
        while rand:
            x, y = random.randint(0, (weight - 20) / 20) * 20, random.randint(0, (height - 20) / 20) * 20

            rand = False

            if snake.head_x == x and snake.head_y == y:
                rand = True
                continue

            for dish in dishes:
                if dish.coordinates[0] == x and dish.coordinates[1] == y:
                    rand = True

            for part in snake.tail:
                if part.x == x and part.y == y:
                    rand = True

        coordinates.append(x)
        coordinates.append(y)
        return coordinates

    def Draw(self, screen, time=0):
        screen.blit(self.image, self.coordinates)

class Food():
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height
        self.iterator = 0
        self.dishes = []
        self.simple_images = [pygame.image.load('images\\food\\food1.png'), pygame.image.load('images\\food\\food2.png'), pygame.image.load('images\\food\\food3.png'), \
                              pygame.image.load('images\\food\\food4.png'), pygame.image.load('images\\food\\food5.png'), pygame.image.load('images\\food\\food6.png')]
        self.bonus_images = [pygame.image.load('images\\food\\bonus1.png'), pygame.image.load('images\\food\\bonus2.png'), pygame.image.load('images\\food\\bonus3.png'), \
                              pygame.image.load('images\\food\\bonus4.png'), pygame.image.load('images\\food\\bonus5.png')]
        self.sounds = self.GetOggFiles("sounds\\food")


    def Update(self, screen, snake):
        if len(self.dishes) == 0 or (len(self.dishes) == 1 and self.dishes[0].time != 0):
            self.AddDish(snake)

        x = 0
        while x <= len(self.dishes) - 1:
            if self.dishes[x].time != 0:
                if (datetime.datetime.now() - self.dishes[x].added_time).seconds >= self.dishes[x].time:
                    self.dishes.pop(x)
                    continue
            x += 1

        self.Draw(screen)

    def AddDish(self, snake):
        dish_rand = random.randint(0, 5)

        self.dishes.append(Dish(dish_rand + 1, self.simple_images[dish_rand], snake, self.dishes, self.weight, self.height))

        if self.iterator % 5 == 0 and self.iterator != 0:
            dish_rand = random.randint(0, 4)
            self.dishes.append(Dish((dish_rand + 1) * 100, self.bonus_images[dish_rand], snake, self.dishes, self.weight, self.height, 7 - dish_rand))

        self.iterator += 1


    def Eat(self, index):
        if self.dishes[index].time == 0:
            score = self.dishes[index].score
        else:
            dif = (datetime.datetime.now() - self.dishes[index].added_time).microseconds
            dif = self.dishes[index].time * 1000000 - dif

            score = dif * self.dishes[index].score // (self.dishes[index].time * 1000000)

        self.dishes.pop(index)
        self.PlayEat()
        return score

    def PlayEat(self):
        if len(self.sounds) == 0:
            return

        sound = pygame.mixer.Sound(self.sounds[random.randint(0, len(self.sounds) - 1)])
        sound.set_volume(1.0)
        sound.play()

    def Draw(self, screen):
        for dish in self.dishes:
            dish.Draw(screen, dish.time)

    def GetOggFiles(self, path):
        list = []
        for file in os.listdir(path):
            if file.endswith(".ogg"):
                list.append(os.path.join(path, file))
        return list