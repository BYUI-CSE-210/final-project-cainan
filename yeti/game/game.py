from email.mime import audio
from mimetypes import init
from game.deeds.deed import Deed
from game.deeds.start_services_deed import StartServicesDeed
from game.services.service_manager import ServiceManager



class Game:
    def __init__(self, debug=False) -> None:
        self._debug = debug
    
    def start_game(self):
        service_manager: ServiceManager
        service_manager = StartServicesDeed().execute()
        if self._debug:
            service_manager.show_all_services()
        video_service = service_manager.video_serivce
        audio_service = service_manager.audio_service
        keyboard_service = service_manager.keyboard_service
        deeds_service = service_manager.deeds_service

        # initialization deeds 

        # action deeds 

        # deed registration

        # game loop 
        while video_service.is_window_open():
            video_service.start_buffer()
            deed: Deed
            for deed in deeds_service.get_all_deeds(exclude_groups=['init']):
                deed.execute()
            video_service.end_buffer()
        service_manager.stop_all_services()
        
        

