import pygame

from game.components.enemies.enemy_weak.enemy import Enemy

class BulletManager:
    def __init__(self):
        self.bullets = []
        self.enemy_bullets = []
        self.ally_bullets = []

    def update(self, game):
        for bullet in self.enemy_bullets:
            bullet.update(self.enemy_bullets)

            if bullet.rect.colliderect(game.player.rect) and bullet.owner == 'enemy':
                self.bullets.remove(bullet)
                game.playing = False
                pygame.time.delay(1000)
                break
        
        for bullet in self.ally_bullets:
            bullet.update(self.ally_bullets)
            # condicional para verificar que el bullet colisione con el enemigo
            for enemy in game.enemy_manager.enemies:
                if bullet.rect.colliderect(enemy.rect) and bullet.owner == 'player':
                    self.ally_bullets.remove(bullet)
                    game.enemy_manager.enemies.remove(enemy)
                    break


    def draw(self, screen):
        for bullet in self.enemy_bullets:
            bullet.draw(screen)
        for bullet in self.ally_bullets:
            bullet.draw(screen)

    def add_bullet(self, bullet):
        if bullet.owner == 'enemy' and len(self.enemy_bullets) < 1:
            self.enemy_bullets.append(bullet)
        elif bullet.owner == 'player' and len(self.ally_bullets) < 1:
            self.ally_bullets.append(bullet)
