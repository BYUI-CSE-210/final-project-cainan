from game.services.service_manager import ServiceManager
from game.entities.yeti import Yeti
from game.deeds.deed import Deed
from game.deeds.start_services_deed import StartServicesDeed
from game.deeds.world_draw_background_deed import DrawBackgroundDeed
from game.deeds.world_move_camera_deed import MoveCameraDeed
from game.deeds.world_apply_gravity_deed import ApplyGravityDeed


class Game:
    def __init__(self, debug=False) -> None:
        self._debug = debug
    
    def start_game(self):
        # game initialization
        service_manager: ServiceManager
        service_manager = StartServicesDeed().execute()
        yeti = Yeti()

        if self._debug:
            service_manager.show_all_services()
        video_service = service_manager.video_serivce
        audio_service = service_manager.audio_service
        keyboard_service = service_manager.keyboard_service
        deeds_service = service_manager.deeds_service

        
        # action deeds 
        world_draw_background_deed = DrawBackgroundDeed(service_manager)
        world_move_camera_deed = MoveCameraDeed(service_manager, yeti)
        world_apply_gravity_deed = ApplyGravityDeed([yeti], service_manager)

        # deed registration
        deeds_service.register_deed(world_draw_background_deed, "action")
        deeds_service.register_deed(world_move_camera_deed, "action")
        deeds_service.register_deed(world_apply_gravity_deed, "action")

        # game loop 
        while video_service.is_window_open():
            video_service.start_buffer()
            deed: Deed
            for deed in deeds_service.get_all_deeds(exclude_groups=['init']):
                deed.execute()
            video_service.end_buffer()
        service_manager.stop_all_services()
        
        

