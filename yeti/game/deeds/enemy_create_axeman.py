from game.deeds.deed import Deed
from game.entities.enemy import *
from game.entities.platform import Platform
from game.shared.point import Point  

class CreateAxemanDeed(Deed):
    def __init__(self, platform:Platform, service_manager=None, debug=False) -> None:
        super().__init__(service_manager, debug)
        self.platform = platform

    def execute(self):
        # return super().execute()
        axeman = Axeman()
        starting_pos = Point(self.platform.position.x + self.platform.get_width() -11, self.platform.position.y)
        axeman.position = starting_pos
