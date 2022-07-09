from abc import ABC, abstractmethod
from game.shared.point import Point
from game.services.video_service import VideoService
from game.services.audio_service import AudioService
from game.services.keyboard_service import KeyboardService
from game.services.service_manager import ServiceManager
from game.services.deeds_service import DeedsService
class Entity(ABC):

    def __init__(self, service_manager = None) -> None:
        super().__init__()
        self.position = Point()
        self.weight = 0
        self.is_on_solid_ground = False
        if service_manager:
            self._video_service: VideoService
            self._video_service = service_manager.video_service
            self._audio_service: AudioService
            self._audio_service = service_manager.audio_service
            self._keyboard_service: KeyboardService
            self._keyboard_service = service_manager.keyboard_service
            self._deeds_service: DeedsService
            self._deeds_service = service_manager.deeds_service
            
    @abstractmethod
    def advance(self):
        pass

    @abstractmethod
    def draw(self):
        pass


