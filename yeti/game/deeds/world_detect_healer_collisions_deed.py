import pyray as pr
from game.deeds.deed import Deed


class DetectHealerCollisionsDeed(Deed):
    def __init__(self, player, healers_list, service_manager=None, debug=False) -> None:
        super().__init__(service_manager, debug)
        self._healers = healers_list
        self._player = player
    
    def execute(self):
        player_hitbox = self._player.get_hitbox()
        for healer in self._healers:
            healer_hitbox = healer.get_hitbox()
            colliding = pr.check_collision_recs(player_hitbox, healer_hitbox)
            if colliding:
                self._player.increase_health(3)
                healer.do_action(1)
                break
            
            