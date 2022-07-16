from game.deeds.deed import Deed
from game.entities.boss import GoblinBoss
from game.entities.platform import Platform


class DrawBossDeed(Deed):
    def __init__(self, boss:GoblinBoss, platform:Platform, service_manager=None, debug=False) -> None:
        super().__init__(service_manager, debug)
        self.platform = platform
        self.boss = boss
        self.direction = -1

    def execute(self):
        if self._debug:
            print("GoblinBoss Walk (Draw Deed) - GoblinBoss position: ", self.boss.position.x, self.boss.position.y )
        # if self.boss._is_alive:
        self.boss.draw()