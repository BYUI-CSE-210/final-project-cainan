from platform import platform
from game.deeds.deed import Deed
from game.entities.orange_slime import OrangeSlime
from game.entities.platform import Platform


class OrangeSlimeWalkDeed(Deed):
    def __init__(self, orange_slime:OrangeSlime, platform:Platform, service_manager=None, debug=False) -> None:
        super().__init__(service_manager, debug)
        self.platform = platform
        self.orange_slime = orange_slime
        self.direction = -1

    def jump(self):
        if self.orange_slime._pace_count % 5:
            dy = 20
            self.orange_slime.position.y += dy
            self.orange_slime.is_on_solid_ground = False
            if self.orange_slime.position.y > self.platform.position.y:
                self.orange_slime.position.y = self.platform.position.y
                self.orange_slime.is_on_solid_ground = True
        

    def execute(self):
        # return super().execute()
        if self.orange_slime.position.x <= self.platform.position.x + 10 or self.orange_slime.position.x >= self.platform.position.x + self.platform.get_width() - self.orange_slime.frameWidth/4 - 10:
            self.direction *= -1
        if self._debug:
            print("orange_slime Walk - orange_slime position: ", self.orange_slime.position.x, self.orange_slime.position.y )
        self.orange_slime.advance(self.direction,0)
        self.orange_slime.draw()
