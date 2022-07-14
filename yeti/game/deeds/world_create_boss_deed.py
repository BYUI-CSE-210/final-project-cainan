from game.deeds.deed import Deed
from game.entities.boss import GoblinBoss
from game.entities.platform import Platform
from game.shared.point import Point  

class CreateBossDeed(Deed):
    def __init__(self, platform:Platform, service_manager=None, debug=False) -> None:
        super().__init__(service_manager, debug)
        self.platform = platform

    def execute(self):
        # return super().execute()
        boss = GoblinBoss(self.service_manager)
        # starting_pos = Point(0,0)
        starting_pos = Point(self.platform.position.x, self.video_service.get_height()- boss.frameHeight)
        boss.position = starting_pos
        if self._debug:
            print("***GoblinBoss Starting position (CreateBossDeed):************************************* ", starting_pos.x, starting_pos.y)
            print("Boss FrameHeight (CreateBossDeed)",boss.frameHeight)
        return boss