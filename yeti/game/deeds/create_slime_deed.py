from game.deeds.deed import Deed
from game.entities.orange_slime import OrangeSlime
from game.entities.platform import Platform
from game.shared.point import Point

class CreateSlimeDeed(Deed):
    def __init__(self, platform:Platform, service_manager=None, debug=False) -> None:
        super().__init__(service_manager, debug)
        self.platform = platform

    def execute(self):
        # return super().execute()
        slime = OrangeSlime(self.service_manager, debug=False)
        starting_pos = Point(self.platform.position.x + self.platform.get_width() - slime.frameWidth/4-11, self.platform.position.y -3)
        slime.position = starting_pos
        if self._debug:
            print("***Slime Starting position: ", starting_pos.x, starting_pos.y)
        return slime