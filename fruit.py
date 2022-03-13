import pygame
from random import randint

class Fruit():
    def __init__(self, screen, snake):
        self.screen = screen
        self.snake = snake
        self.coords = [10, 8]
        self.surface = pygame.image.load('graphics/fruit.png')
        self.rect = self.surface.get_rect(topleft = (self.coords[0] * 64, self.coords[1] * 64))
        self.score = 0
        self.goodLocation = False

    def move(self):
        while self.goodLocation == False:
            self.coords = [randint(1, 15), randint(1, 15)]
            self.goodLocation = True
            for part in self.snake.partsList.keys():
                if self.coords == self.snake.partsList[part]:
                    self.goodLocation = False
        self.rect = self.surface.get_rect(topleft = (self.coords[0] * 64, self.coords[1] * 64))

    def collision(self):
        self.goodLocation = False
        if self.snake.partsList['head'] == self.coords:
            self.score += 1
            self.move()


    def loop(self):
        self.collision()
        self.screen.blit(self.surface, self.rect)