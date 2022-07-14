from game.deeds.deed import Deed
from game.entities.axe import Axe
from game.shared.point import Point
class BossCreateAxeDeed(Deed):
    def __init__(self, boss ,axes:list, service_manager=None, debug=False) -> None:
        super().__init__(service_manager, debug)
        self.axes = axes
        self.boss = boss

    def execute(self):
        starting_point = Point(self.boss.position.x, self.boss.position.y + self.boss.frameHeight/2)
        axe = Axe(self.service_manager,starting_point,-1)
        self.axes.append(axe)
        if self._debug:
            print(self.axes)