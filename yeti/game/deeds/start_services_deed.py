from game.deeds.deed import Deed
from game.services.deeds_service import DeedsService
from game.services.video_service import VideoService
from game.services.audio_service import AudioService
from game.services.keyboard_service import KeyboardService
from game.services.service_manager import ServiceManager

class StartServicesDeed(Deed):
    
    def execute(self):
        service_manager = ServiceManager(self._debug)
        keyboard_service = KeyboardService()

        audio_service = AudioService()
        video_service = VideoService(20)
        deed_service = DeedsService()

        service_manager.register_service(keyboard_service, "input")
        service_manager.register_service(audio_service, "output")
        service_manager.register_service(video_service, "output")
        service_manager.register_service(deed_service, "control")

        service_manager.start_all_services()
        return service_manager


if __name__ == "__main__":
    deed = StartServicesDeed()