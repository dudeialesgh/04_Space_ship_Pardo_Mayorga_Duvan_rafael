import pygame
import random

from pygame.sprite import Sprite
from game.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT, ENEMY_1

class Enemy(Sprite):
    Y_POS = 20
    X_POS_LIST = [50, 150, 250, 350, 450, 550, 300, 100, 258, 400]
    SPEED_X = 5
    SPEED_Y = 1
    MOD_X = {0:'left', 1:'right'}

    def __init__(self):
        self.image = ENEMY_1
        self.image = pygame.transform.scale(self.image, (40, 60))
        self.rect = self.image.get_rect()
        self.rect.x = random.choice(self.X_POS_LIST)
        self.rect.y = self.Y_POS
        self.type = 'enemy'

        self.mod_x = random.choice(self.MOD_X)
        self.speed_x = self.SPEED_X
        self.speed_y = self.SPEED_Y
        self.move_x_for = random.randint(30, 100)
        self.index = 0
        self.shooting_time = random.randint(30, 50)

    def change_movemet_in_x(self):
        self.index += 1
        if(self.index >= self.move_x_for and self.mod_x == 'right') or (self.rect.x >= SCREEN_WIDTH - 40 ):
            self.mod_x = 'left'
        elif(self.index >= self.move_x_for and self.mod_x == 'left') or (self.rect.x <= 10):
            self.mod_x = 'right'
        if(self.index >= self.move_x_for):
            self.index = 0

    def update(self, ships):
        self.rect.y += self.speed_y

        if self.mod_x == 'left':
            self.rect.x -= self.speed_x
            self.change_movemet_in_x()
        elif self.mod_x == 'right':
            self.rect.x += self.speed_x
            self.change_movemet_in_x()
        
        if self.rect.y >= SCREEN_HEIGHT:
            ships.remove(self)

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))