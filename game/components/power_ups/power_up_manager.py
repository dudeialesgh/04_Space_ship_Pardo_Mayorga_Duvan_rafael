import pygame
import random

from game.components.power_ups.shield import Shield
from game.components.power_ups.speed_power_up import SpeedPowerUp
from game.utils.constants import SHIELD_TYPE, SHIELD, SPACESHIP_SHIELD, THUNDER_TYPE, SPACESHIP

class PowerUpManager:
    def __init__(self):
        # Inicializa la lista de power-ups y establece el tiempo de aparición y duración de los mismos
        self.power_ups = []
        self.when_appears = random.randint(5000,10000)
        self.duration = random.randint(3,5)

    def generate_power_up(self):
        # Genera un power-up aleatorio (escudo o aumento de velocidad)
        power_up_type = random.choice([Shield, SpeedPowerUp])
        power_up = power_up_type()
        # Establece el tiempo de aparición del siguiente power-up
        self.when_appears += random.randint(5000, 10000)
        # Agrega el power-up a la lista
        self.power_ups.append(power_up)
    
    def update(self, game):
        # Captura el tiempo actual
        current_time = pygame.time.get_ticks()
        # Genera un power-up si la lista está vacía y ha pasado el tiempo de aparición
        if len(self.power_ups) == 0 and current_time >= self.when_appears:
            self.generate_power_up()

        # Actualiza cada power-up en la lista
        for power_up in self.power_ups:
            current_time = pygame.time.get_ticks()
            # Genera un power-up si la lista está vacía y ha pasado el tiempo de aparición
            if len(self.power_ups) == 0 and current_time >= self.when_appears:
                self.generate_power_up()

            # Actualiza el power-up
            power_up.update(game.game_speed, self.power_ups)

            # Verifica si el jugador ha colisionado con el power-up
            if game.player.rect.colliderect(power_up):
                # Establece el tiempo de inicio del power-up
                power_up.start_time = pygame.time.get_ticks()

                # Aplica el power-up correspondiente al jugador
                if isinstance(power_up, Shield):
                    game.player.power_up_type = SHIELD_TYPE
                    game.player.set_image((65, 75), SPACESHIP_SHIELD)
                elif isinstance(power_up, SpeedPowerUp):
                    game.player.power_up_type = THUNDER_TYPE
                    game.player.apply_speed_boost()
                    game.player.set_image((20, 30), SPACESHIP)

                # Establece el tiempo de finalización del power-up
                game.player.power_time_up = power_up.start_time + (self.duration * 1000)
                # Elimina el power-up de la lista
                self.power_ups.remove(power_up)
                # Establece la bandera de power-up activo en el jugador
                game.player.has_power_up = True

    def draw(self, screen):
        # Dibuja cada power-up en la lista
        for power_up in self.power_ups:
            power_up.draw(screen)
        
    def reset(self):
        # Captura el tiempo actual
        now = pygame.time.get_ticks()
        # Limpia la lista de power-ups
        self.power_ups = []
        # Genera el tiempo de aparición del siguiente power-up
        self.when_appears =  random.randint(5000,10000)