import pyray as pr
from game.deeds.deed import Deed
from game.entities.baby_yeti import BabyYeti
from game.entities.yeti import Yeti

class PlayerDetectEnemyCollisionsDeed(Deed):
    def __init__(self, player,baby_yeti, service_manager=None, debug=False) -> None:
        super().__init__(service_manager, debug)
        self._baby_yeti: BabyYeti
        self._baby_yeti = baby_yeti
        self._player: Yeti
        self._player = player
    
    def execute(self):
        if pr.check_collision_recs(self._player.get_hitbox(), self._baby_yeti.get_hitbox()):
            self._baby_yeti._is_saved = True
            