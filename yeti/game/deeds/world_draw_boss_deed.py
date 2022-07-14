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
        # return super().execute()
        if self.boss.position.x <= self.platform.position.x + 10 or self.boss.position.x >= self.platform.position.x + self.platform.get_width() - self.boss.frameWidth/4 - 10:
            self.direction *= -1
        if self._debug:
            print("GoblinBoss Walk (Draw Deed) - GoblinBoss position: ", self.boss.position.x, self.boss.position.y )
        if self.boss._is_alive:
            self.boss.advance(self.direction,0)
            self.boss.draw()