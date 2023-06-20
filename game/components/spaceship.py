import pygame
import random
from pygame.sprite import Sprite
from game.utils.constants import SPACESHIP, SCREEN_WIDTH, SCREEN_HEIGHT, DEFAULT_TYPE, THUNDER

from game.components.bullets.bullet import Bullet


class Spaceship(Sprite):
    # Posición inicial de la nave
    X_POS = (SCREEN_WIDTH // 2) - 40
    Y_POS = 500

    def __init__(self):
        # Inicializa la nave con la imagen correspondiente y la posición inicial
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (40, 60))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.type = 'player'
        self.has_power_up = False
        self.power_time_up = 0
        self.power_up_type = DEFAULT_TYPE
        self.speed_boost = False

    def move_left(self):
        # Mueve la nave hacia la izquierda
        if self.rect.x > 0:
            if self.speed_boost == True:
                self.rect.x -= 20
            else:
                self.rect.x -= 10
        elif self.rect.x == 0:
            self.rect.x = SCREEN_WIDTH - 40
    
    def move_right(self):
        # Mueve la nave hacia la derecha
        if self.rect.x < SCREEN_WIDTH - 40:
            if self.speed_boost == True:
                self.rect.x += 20
            else:
                self.rect.x += 10
        elif self.rect.x == SCREEN_WIDTH - 40:
            self.rect.x = 0
    
    def move_up(self):
        # Mueve la nave hacia arriba
        if self.rect.y > SCREEN_HEIGHT // 2:
            if self.speed_boost == True:
                self.rect.y -= 20
            else:
                self.rect.y -= 10

    def move_down(self):
        # Mueve la nave hacia abajo
        if self.rect.y < SCREEN_HEIGHT - 70:
            if self.speed_boost == True:
                self.rect.y += 20
            else:
                self.rect.y += 10

    def update(self, user_input, game):
        # Actualiza la posición de la nave en función de la entrada del usuario
        if user_input[pygame.K_LEFT]:
            self.move_left()
        if user_input[pygame.K_RIGHT]:
            self.move_right()
        if user_input[pygame.K_UP]:
            self.move_up()
        if user_input[pygame.K_DOWN]:
            self.move_down()
        if user_input[pygame.K_SPACE]:
            self.shoot(game.bullet_manager)
        
    def shoot(self, bullet_manager):
        # Crea una bala y la añade al administrador de balas
        bullet = Bullet(self)
        bullet_manager.add_bullet(bullet)

    def draw(self, screen):
        # Dibuja la nave en la pantalla
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def reset(self):
        # Reinicia la posición de la nave y desactiva el impulso de velocidad
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.speed_boost = False

    def set_image(self, size=(40,60), image = SPACESHIP):
        # Actualiza la imagen de la nave y la escala
        self.image = image
        self.image = pygame.transform.scale(self.image, size)

    def apply_speed_boost(self):
        # Activa el impulso de velocidad
        self.speed_boost = True