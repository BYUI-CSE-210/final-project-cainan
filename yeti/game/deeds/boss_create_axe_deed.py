from game.deeds.deed import Deed
from game.entities.axe import Axe

class BossCreateAxeDeed(Deed):
    def __init__(self, boss ,axes:list, service_manager=None, debug=False) -> None:
        super().__init__(service_manager, debug)
        self.axes = axes
        self.boss = boss

    def execute(self):
        axe = Axe(self.service_manager,self.boss.position,-1)
        self.axes.append(axe)
        if self._debug:
            print(self.axes)