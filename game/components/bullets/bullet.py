import pygame

from pygame.sprite import Sprite

from game.utils.constants import BULLET, BULLET_ENEMY, SCREEN_HEIGHT, SCREEN_WIDTH


class Bullet(Sprite):
    # Posición inicial de la bala
    X_POS = 80
    Y_POS = 310
    # Velocidad de la bala
    SPEED = 20
    # Tamaño de la bala del jugador y del enemigo
    BULLET_SIZE = pygame.transform.scale(BULLET, (10, 20))
    BULLET_SIZE_ENEMY = pygame.transform.scale(BULLET_ENEMY, (9, 32))
    # Diccionario que contiene los tamaños de las balas
    BULLETS = {'player': BULLET_SIZE, 'enemy': BULLET_SIZE_ENEMY}
    
    def __init__(self, spaceship):
        # Inicializa la bala con el tamaño correspondiente
        self.image = self.BULLETS[spaceship.type]
        self.rect = self.image.get_rect()
        # Establece la posición inicial de la bala en el centro de la nave
        self.rect.center = spaceship.rect.center
        # Establece el propietario de la bala (jugador o enemigo)
        self.owner =  spaceship.type

    def events(self):
        # Este método no se utiliza en la clase Bullet
        pass

    def update(self, bullets):
        # Actualiza la posición de la bala en función de su propietario
        if self.owner == 'enemy':
            self.rect.y += self.SPEED
        elif self.owner == 'player':
            self.rect.y -= self.SPEED
        # Si la bala sale de la pantalla, se elimina de la lista de balas
        if self.rect.y >= SCREEN_HEIGHT or self.rect.y < 0:
            bullets.remove(self)

    def draw(self, screen):
        # Dibuja la bala en la pantalla
        screen.blit(self.image, (self.rect.x, self.rect.y))