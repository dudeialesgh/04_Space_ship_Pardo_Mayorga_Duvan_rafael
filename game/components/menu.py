import pygame

from game.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT, FONT_STYLE


class Menu:
    HALF_SCREEN_WIDTH = SCREEN_WIDTH // 2
    HALF_SCREEN_WIDTH = SCREEN_HEIGHT // 2

    def __init__(self, message,screen):
        screen.fill((255,255,255))
        self.font = pygame.font.Font(FONT_STYLE, 30)
        self.text = self.font.render(message, True, (0,0,0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_WIDTH)

    def handle_events_to_menu(self,game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.running = False
                game.playing = False
            if event.type == pygame.KEYDOWN:
                game.run()
    
    def update(self,game):
        pygame.display.update()
        self.handle_events_to_menu(game)
    
    def draw(self,screen):
        screen.blit(self.text, self.text_rect)

    def update_message(self,message):
        self.text = self.font.render(message, True, (0,0,0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_WIDTH)

    def reset_screen_collor(self,screen):
        screen.fill((255,255,255))
    
