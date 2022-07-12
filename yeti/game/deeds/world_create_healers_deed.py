from game.deeds.deed import Deed
from game.entities.healer import Healer
from game.shared.point import Point

class CreateHealersDeed(Deed):
    def __init__(self, healers_list:list, service_manager=None, debug=False) -> None:
        super().__init__(service_manager, debug)
        self._healers = healers_list

    def execute(self):
        for i in range(0, 3):
            healer = Healer(self.service_manager)
            healer.position = Point(i*4048 + 500, self.video_service.get_height()- healer.height - 20)
            self._healers.append(healer)
            healer.draw()
