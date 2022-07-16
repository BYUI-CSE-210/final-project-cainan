from matplotlib.pyplot import cla
import pyray as pr
from game.deeds.deed import Deed

class EnemyDetectProjectileCollisionDeed(Deed):
    def __init__(self, enemies, projectiles, remove_dead_units=True, service_manager=None, debug=False) -> None:
        super().__init__(service_manager, debug)
        self._enemies = enemies
        self._projectiles = projectiles
        self._remove_dead = remove_dead_units

    def execute(self):
        for enemy in self._enemies:
            enemy_hitbox = enemy.get_hitbox()
            for projectile in self._projectiles:
                projectile_hitbox = projectile.get_hitbox()
                colliding = pr.check_collision_recs(enemy_hitbox, projectile_hitbox)
                if colliding:
                    enemy.got_hit()
                    projectile.got_hit()
                    if not enemy.is_alive() and self._remove_dead:
                        self._enemies.remove(enemy)
                    self._projectiles.remove(projectile)
