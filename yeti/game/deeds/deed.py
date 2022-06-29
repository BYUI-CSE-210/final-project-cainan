from abc import ABC, abstractmethod

class Deed(ABC):

    def __init__(self, service_manager = None, video_service = None, audio_service = None, keyboard_service = None, debug = False) -> None:
        super().__init__()
        self.service_manager = service_manager
        self.video_service = video_service
        self.audio_service = audio_service
        self.keyboard_service = keyboard_service
        self._debug = debug

    @abstractmethod
    def execute(self):
        pass
