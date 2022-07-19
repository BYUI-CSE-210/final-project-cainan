from game.deeds.deed import Deed
from game.entities.baby_yeti import BabyYeti
from game.shared.point import Point

class CreateBabyYetiDeed(Deed):
    def __init__(self, babies_list:list, service_manager=None, debug=False) -> None:
        super().__init__(service_manager, debug)
        self._babies = babies_list

    def execute(self):
        for i in range(1):
            baby = BabyYeti(self.service_manager)
            baby.position = Point(self.video_service.get_game_width() - 130, self.video_service.get_height() - baby.height)
            self._babies.append(baby)

