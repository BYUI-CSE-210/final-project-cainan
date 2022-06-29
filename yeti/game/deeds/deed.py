from abc import ABC, abstractmethod
from game.services.video_service import VideoService
from game.services.audio_service import AudioService
from game.services.keyboard_service import KeyboardService
from game.services.service_manager import ServiceManager

class Deed(ABC):

    def __init__(self, service_manager = None, debug = False) -> None:
        super().__init__()
        self.service_manager: ServiceManager
        self.service_manager = service_manager
        if self.service_manager:
            self.video_service = self.service_manager.get_first_service(VideoService)
            self.audio_service = self.service_manager.get_first_service(AudioService)
            self.keyboard_service = self.service_manager.get_first_service(KeyboardService)
        self._debug = debug

    @abstractmethod
    def execute(self):
        pass
