import pygame
from game.utils.constants import FONT_STYLE

class Counter:
    def __init__(self):
        # Inicializa el contador en cero
        self.count = 0

    def update(self):
        # Incrementa el contador en uno
        self.count += 1

    def draw(self, screen):
        # Dibuja el contador en la pantalla
        font = pygame.font.Font(FONT_STYLE, 30)
        text = font.render(f'Score: {self.count}', True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (1000, 50)
        screen.blit(text, text_rect)
    
    def reset(self):
        # Reinicia el contador a cero
        self.count = 0

    def set_count(self, value):
        # Establece el valor del contador
        self.count = value