import pygame

from game.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT, FONT_STYLE


class Menu:
    HALF_SCREEN_WIDTH = SCREEN_WIDTH // 2
    HALF_SCREEN_HEIGHT = SCREEN_HEIGHT // 2

    def __init__(self, message, screen):
        # Inicializa la clase Menu con un mensaje y la pantalla del juego
        screen.fill((255,255,255))  # Limpia la pantalla con un color blanco
        self.font = pygame.font.Font(FONT_STYLE, 30)  # Crea una fuente para el mensaje
        self.text = self.font.render(message, True, (0,0,0))  # Renderiza el mensaje en una superficie de texto
        self.text_rect = self.text.get_rect()  # Obtiene el rectángulo que rodea el mensaje
        self.text_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT)  # Centra el mensaje en la pantalla

    def handle_events_to_menu(self,game):
        # Maneja los eventos de teclado y de cierre de ventana
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.running = False
                game.playing = False
            if event.type == pygame.KEYDOWN:
                game.run()
    
    def update(self,game):
        # Actualiza la pantalla del juego y maneja los eventos
        pygame.display.update()
        self.handle_events_to_menu(game)
    
    def draw(self,screen):
        # Dibuja el mensaje en la pantalla
        screen.blit(self.text, self.text_rect)

    def update_message(self, message):
        # Actualiza el mensaje que se muestra en la pantalla

        lines = message.split('\n')  # Separar el mensaje en líneas usando saltos de línea

        rendered_lines = []
        line_heights = []
        max_line_width = 0

        for line in lines:
            rendered_line = self.font.render(line, True, (0, 0, 0))  # Renderiza cada línea del mensaje
            rendered_lines.append(rendered_line)

            line_width, line_height = rendered_line.get_size()  # Obtiene el ancho y alto de la línea renderizada
            line_heights.append(line_height)  # Almacena la altura de cada línea
            max_line_width = max(max_line_width, line_width)  # Actualiza el ancho máximo de línea

        total_height = sum(line_heights)  # Calcula la altura total del mensaje sumando las alturas de cada línea

        self.text = pygame.Surface((max_line_width, total_height), pygame.SRCALPHA)  # Crea una superficie para el mensaje
        y = 0

        for i, rendered_line in enumerate(rendered_lines):
            line_width, line_height = rendered_line.get_size()
            x = (max_line_width - line_width) // 2  # Calcula la posición x para centrar cada línea
            self.text.blit(rendered_line, (x, y))  # Dibuja la línea en la superficie del mensaje
            y += line_height

        self.text_rect = self.text.get_rect()  # Obtiene el rectángulo del mensaje
        self.text_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT + 50)  # Centra el mensaje en la pantalla con un desplazamiento hacia abajo

    def reset_screen_collor(self,screen):
        # Cambia el color de fondo de la pantalla a blanco
        screen.fill((255,255,255))