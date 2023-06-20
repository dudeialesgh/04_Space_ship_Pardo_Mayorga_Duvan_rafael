from game.components.enemies.enemy_weak.enemy import Enemy

class EnemyManager:
    def __init__(self):
        # Inicializa la lista de enemigos
        self.enemies = []

    def update(self, game):
        # Agrega un enemigo si no hay ninguno en la lista
        self.add_enemy()
        # Actualiza cada enemigo en la lista
        for enemy in self.enemies:
            enemy.update(self.enemies, game)


    def add_enemy(self):
        # Agrega un enemigo a la lista si no hay ninguno
        if len(self.enemies) < 3:
            enemy = Enemy()
            self.enemies.append(enemy)

    def draw(self, screen):
        # Dibuja cada enemigo en la lista
        for enemy in self.enemies:
            enemy.draw(screen)
    
    def reset(self):
        # Reinicia la lista de enemigos
        self.enemies = []