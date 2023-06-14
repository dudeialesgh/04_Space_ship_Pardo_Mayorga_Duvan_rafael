from game.components.enemies.enemy_weak.enemy import Enemy

class EnemyManager:
    def __init__(self):
        self.enemies = []

    def update(self):
        self.add_enemy()
        for enemy in self.enemies:
            enemy.update(self.enemies)

    def add_enemy(self):
        if len(self.enemies) < 20:
            enemy = Enemy()
            self.enemies.append(enemy)

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)