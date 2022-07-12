import pyray as pr
from game.deeds.deed import Deed
from game.entities.baby_yeti import BabyYeti
from game.entities.yeti import Yeti

class PlayerDetectBabyCollisionsDeed(Deed):
    def __init__(self, player,babies:list, service_manager=None, debug=False) -> None:
        super().__init__(service_manager, debug)
        self._babies = babies
        self._player: Yeti
        self._player = player
    
    def execute(self):
        player_hitbox = self._player.get_hitbox()
        for baby in self._babies:
            baby: BabyYeti
            baby_hitbox = baby.get_hitbox()
            colliding = pr.check_collision_recs(player_hitbox, baby_hitbox)
            if colliding:
                baby._is_saved = True
                break

            