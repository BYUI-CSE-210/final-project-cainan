from game.deeds.deed import Deed
from game.entities.platform import Platform
from game.entities.boss import GoblinBoss


class BossWalkDeed(Deed):
    def __init__(self, boss:GoblinBoss, platform:Platform, service_manager=None, debug=False) -> None:
        super().__init__(service_manager, debug)
        self._platform = platform
        self._boss = boss
        self._frame_timer = 0
        self._pace_count = 0 
        self._direction = -1


    def execute(self):
        self._frame_timer += self.video_service.get_frame_time()
        if self._pace_count > 3:
            self._direction *= -1
            self._pace_count = 0

        if self._frame_timer > 1:
            self._frame_timer = 0
            self._pace_count += 1
        elif self._frame_timer > .5:
            self._boss.advance(self._direction,0)
        else:
            self._boss.advance(0,0)
        
        
