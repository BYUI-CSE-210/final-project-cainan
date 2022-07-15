from game.deeds.deed import Deed
from game.entities.boss import GoblinBoss

class BossActionsDeed(Deed):
    def __init__(self, boss:GoblinBoss, service_manager=None, debug=False) -> None:
        super().__init__(service_manager, debug)
        self._frame_timer = 0
        self._boss = boss

    def execute(self):
        self._frame_timer += self.video_service.get_frame_time()
        if self._frame_timer > 2:
            self._boss.do_action(2)
            self._frame_timer = 0