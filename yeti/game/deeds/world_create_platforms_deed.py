from pyray import play_audio_stream
from game.deeds.deed import Deed
from game.entities.platform import Platform
from random import randint, choice

class CreatePlatformsDeed(Deed):
    def __init__(self, platforms_list:list, service_manager=None, debug=False) -> None:
        super().__init__(service_manager, debug)
        self._platforms = platforms_list

    def execute(self):
        platforms = self._platforms
        # boss platform
        floor_platform = Platform(4048, 20, service_manager=self.service_manager)
        floor_platform.position.x = 16192
        floor_platform.position.y = self.video_service.get_height()-20
        platforms.append(floor_platform)
        # create floor platforms.
        for p in range(4):
            floor_platform = Platform(4048*2/3, 20, service_manager=self.service_manager)
            floor_platform.position.x = 4048*p
            floor_platform.position.y = self.video_service.get_height()-20
            platforms.append(floor_platform)

        # create random floating platforms within jump range of eachother
        platform_x = 50
        platform_y = self.video_service.get_height() - 150
        last_platform = None
        for i in range(60):
            platform_height = 20
            platform_width = 200
            
            if last_platform:
                platform_x += randint(200, 350)
                if last_platform.position.y < 200:
                    platform_y = last_platform.position.y + 150
                elif last_platform.position.y > self.video_service.get_height()-300:
                    platform_y = last_platform.position.y - 150
                else:
                    platform_y = choice([last_platform.position.y + 150, last_platform.position.y - 150])
            
            
                
            platform = Platform(platform_width, platform_height, service_manager=self.service_manager)
            platform.position.x = platform_x
            platform.position.y = platform_y
            self._platforms.append(platform)
            last_platform = platform
            
            

