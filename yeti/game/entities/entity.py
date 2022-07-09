from abc import ABC, abstractmethod
from game.shared.point import Point
from game.services.video_service import VideoService
from game.services.audio_service import AudioService
from game.services.keyboard_service import KeyboardService
from game.services.service_manager import ServiceManager
from game.services.deeds_service import DeedsService
class Entity(ABC):

    def __init__(self, service_manager = None, debug = None) -> None:
        super().__init__()
        self.position = Point()
        self._weight = 0
        self.is_on_solid_ground = False
        self._debug = debug
        self._service_manager: ServiceManager
        self._service_manager = service_manager
        if service_manager:
            self._video_service = self._service_manager.get_first_service(VideoService)
            self._audio_service = self._service_manager.get_first_service(AudioService)
            self._keyboard_service = self._service_manager.get_first_service(KeyboardService)
            self._deeds_service = self._service_manager.get_first_service(DeedsService)
            
    @abstractmethod
    def advance(self):
        pass

    @abstractmethod
    def draw(self):
        pass
    
    @abstractmethod
    def get_hitbox(self):
        pass

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, weight):
        self._weight = weight
