from game.deeds.deed import Deed
from game.entities.axe import Axe
import pyray as pr
from random import randint

class BossCreateAxeDeed(Deed):
    def __init__(self, boss ,axes:list, service_manager=None, debug=False) -> None:
        super().__init__(service_manager, debug)
        self.axes = axes
        self.boss = boss

    def execute(self):
        rand_num = randint(1,3)
        for i in range(3):
            axe = Axe(self.service_manager,pr.Vector2(self.boss.position.x, self.boss.position.y + self.boss.frameHeight/rand_num),-1)
        self.axes.append(axe)
        if self._debug:
            print(self.axes)