from game.deeds.deed import Deed
from game.entities.platform import Platform
from random import randint

class CreatePlatformsDeed(Deed):
    def __init__(self, platforms_list:list, service_manager=None, debug=False) -> None:
        super().__init__(service_manager, debug)
        self._platforms = platforms_list

    def execute(self):
        platform_x = 50
        platforms = self._platforms
        for i in range(60):
            platform = Platform(200, 20, service_manager=self.service_manager)
            platform.position.x = platform_x
            platform.position.y = randint(200, 800)
            platforms.append(platform)
            platform_x += randint(100,400)

