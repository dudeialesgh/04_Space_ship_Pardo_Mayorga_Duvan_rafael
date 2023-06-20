import pygame

from game.components.enemies.enemy_weak.enemy import Enemy
from game.utils.constants import SHIELD_TYPE, SOUND_2

class BulletManager:
    def __init__(self):
        # Inicializa las listas de balas
        self.bullets = []
        self.enemy_bullets = []
        # Crea un objeto Sound de Pygame para reproducir sonidos
        self.Sound = pygame.mixer.Sound(SOUND_2)

    def update(self, game):
        # Actualiza las balas de los enemigos
        for bullet in self.enemy_bullets:
            bullet.update(self.enemy_bullets)
            # Comprueba si la bala colisiona con el jugador
            if bullet.rect.colliderect(game.player.rect) and bullet.owner == 'enemy':
                # Elimina la bala si colisiona con el jugador
                self.enemy_bullets.remove(bullet)
                # Si el jugador no tiene escudo, detiene el juego y muestra una pantalla de muerte
                if game.player.power_up_type != SHIELD_TYPE:
                    game.playing = False
                    pygame.time.delay(1000)
                    game.death_count.update()
                break
        
        # Actualiza las balas del jugador
        for bullet in self.bullets:
            bullet.update(self.bullets)
            # Comprueba si la bala colisiona con un enemigo
            for enemy in game.enemy_manager.enemies:
                if bullet.rect.colliderect(enemy.rect) and bullet.owner == 'player':
                    # Elimina el enemigo y la bala si colisionan
                    game.enemy_manager.enemies.remove(enemy)
                    self.bullets.remove(bullet)
                    # Actualiza la puntuación del jugador
                    game.score.update()
                    
                    

    def draw(self, screen):
        # Dibuja las balas de los enemigos
        for bullet in self.enemy_bullets:
            bullet.draw(screen)
        # Dibuja las balas del jugador
        for bullet in self.bullets:
            bullet.draw(screen)

    def add_bullet(self, bullet):
        # Agrega la bala a la lista correspondiente
        if bullet.owner == 'enemy' and len(self.enemy_bullets) < 1:
            self.enemy_bullets.append(bullet)
        elif bullet.owner == 'player' and len(self.bullets) < 2:
            self.bullets.append(bullet)
            # Reproduce un sonido al agregar la bala del jugador
            self.Sound.play(1)

    def reset(self):
        # Reinicia las listas de balas
        self.bullets = []
        self.enemy_bullets = []