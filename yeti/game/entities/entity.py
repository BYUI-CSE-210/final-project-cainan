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
        self._weight = 0
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

    @property
    def weight(self):
        '''
        Weight of an entity is used to apply gravity to the entity. 
        
        See the world_apply_gravity_deed.py:
        Something that has 2 weight is twice as heavy as something with 1.'''
        return self._weight
    
    @weight.setter
    def set_weight(self, weight):
        self._weight = weight

