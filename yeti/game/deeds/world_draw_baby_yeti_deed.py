from game.deeds.deed import Deed
from game.entities.baby_yeti import BabyYeti

class DrawBabyYetiDeed(Deed):
    def __init__(self, babies_list:list, service_manager=None, debug=False) -> None:
        super().__init__(service_manager, debug)
        self._babies = babies_list
    def execute(self):
        for baby in self._babies:
            baby:BabyYeti
            baby.advance()
            baby.draw()