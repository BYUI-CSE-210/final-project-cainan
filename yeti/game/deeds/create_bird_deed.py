from game.deeds.deed import Deed
from game.entities.bird import Bird
from game.shared.point import Point  
from random import randint
import pyray as pr

class CreateBirdDeed(Deed):
    def __init__(self, service_manager=None, debug=True) -> None:
        super().__init__(service_manager, debug)

    def execute(self):
        # return super().execute()
        starting_pos = Point(randint(1000,8000),randint(40,512))
        bird = Bird(self.service_manager)
        bird.position = starting_pos
        if self._debug:
            print("***Bird Starting position: ", starting_pos.x, starting_pos.y)  
        return bird

