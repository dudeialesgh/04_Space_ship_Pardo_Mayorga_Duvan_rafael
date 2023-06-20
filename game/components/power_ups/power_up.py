import random
from pygame.sprite import Sprite
from game.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT


class PowerUp(Sprite):
    def __init__(self, image, type):
        # Inicializa el power-up con la imagen y el tipo correspondiente
        self.image = image
        self.type = type
        # Establece la posición inicial del power-up de forma aleatoria
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(120, SCREEN_WIDTH - 120)
        self.rect.y = 0
        # Establece el tiempo de inicio del power-up
        self.start_time = 0

    def update(self, game_speed, power_ups, ):
        # Actualiza la posición del power-up en función de la velocidad del juego
        self.rect.y += game_speed
        # Si el power-up sale de la pantalla, se elimina de la lista de power-ups
        if self.rect.y < 0 or self.rect.y >= SCREEN_HEIGHT:
            power_ups.remove(self)

    def draw(self, screen):
        # Dibuja el power-up en la pantalla
        screen.blit(self.image, self.rect)