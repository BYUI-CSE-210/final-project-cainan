from game.deeds.deed import Deed
from game.entities.enemy import *
from game.entities.platform import Platform


class AxemanWalkDeed(Deed):
    def __init__(self, axeman:Axeman, platform:Platform, service_manager=None, debug=False) -> None:
        super().__init__(service_manager, debug)
        self.platform = platform
        self.axeman = axeman
        self.direction = -1

    def execute(self):
        # return super().execute()
        if self.axeman.position.x <= self.platform.position.x + 10 or self.axeman.position.x >= self.platform.position.x + self.platform.get_width() - self.axeman.frameWidth/4 - 10:
            self.direction *= -1
        if self._debug:
            print("Axeman Walk - Axeman position: ", self.axeman.position.x, self.axeman.position.y )
        if self.axeman._is_alive:
            self.axeman.advance(self.direction,0)
            self.axeman.draw()

