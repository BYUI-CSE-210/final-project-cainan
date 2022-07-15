import pyray as pr
from game.deeds.deed import Deed
from game.entities.entity import Entity
from game.entities.yeti import Yeti
from yeti.game.entities.orange_slime import OrangeSlime

class PlayerDetectEnemyCollisionsDeed(Deed):
    def __init__(self, player, axes, enemies, birds, slimes, service_manager=None, debug=False) -> None:
        super().__init__(service_manager, debug)
        self._entities = [axes, enemies, birds, slimes]
        self._player: Yeti
        self._player = player
    
    def execute(self):
        entity:Entity
        for entity_list in self._entities:
            for entity in entity_list:
                if pr.check_collision_recs(self._player.get_hitbox(), entity.get_hitbox()):
                    if isinstance(entity, OrangeSlime):
                        self._player.add_ammo()
                    else:
                        self._player.got_hit()
                        entity.got_hit()
                    entity_list.remove(entity)
                