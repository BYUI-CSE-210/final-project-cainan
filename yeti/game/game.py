from game.services.service_manager import ServiceManager
from game.entities.yeti import Yeti
from game.entities.platform import Platform
from game.deeds.deed import Deed
from game.deeds.start_services_deed import StartServicesDeed
from game.deeds.world_draw_background_deed import DrawBackgroundDeed
from game.deeds.world_move_camera_deed import MoveCameraDeed
from game.deeds.world_apply_gravity_deed import ApplyGravityDeed
from game.deeds.world_draw_platforms_deed import DrawPlatformsDeed
from game.deeds.world_detect_platform_collisions_deed import DetectPlatformCollisionsDeed
from game.deeds.player_action_deed import PlayerActionDeed
from game.deeds.player_move_deed import PlayerMoveDeed
from game.deeds.player_draw_deed import PlayerDrawDeed


class Game:
    def __init__(self, debug=False) -> None:
        self._debug = debug
    
    def start_game(self):
        # game initialization
        service_manager: ServiceManager
        service_manager = StartServicesDeed().execute()
        yeti = Yeti()
        yeti.center.x = 100
        yeti.center.y = 100
        platform = Platform(200, 20, service_manager=service_manager)
        platform.position.x = 200
        platform.position.y = 200

        if self._debug:
            service_manager.show_all_services()
        video_service = service_manager.video_serivce
        audio_service = service_manager.audio_service
        keyboard_service = service_manager.keyboard_service
        deeds_service = service_manager.deeds_service

        
        # action deeds 
        world_draw_background_deed = DrawBackgroundDeed(service_manager)
        world_move_camera_deed = MoveCameraDeed(service_manager, yeti)
        #TODO create a list of Entities to be passed to the apply gravity deed. 
        world_apply_gravity_deed = ApplyGravityDeed([yeti], service_manager)
        world_draw_platforms_deed = DrawPlatformsDeed([platform], service_manager)
        world_detect_platform_collisions_deed = DetectPlatformCollisionsDeed([platform], yeti)
        player_action_deed = PlayerActionDeed(service_manager, yeti)
        player_move_deed = PlayerMoveDeed(service_manager, yeti)
        player_draw_deed = PlayerDrawDeed(yeti)



        # deed registration
        deeds_service.register_deed(world_draw_background_deed, "action")
        deeds_service.register_deed(world_move_camera_deed, "action")
        deeds_service.register_deed(world_apply_gravity_deed, "action")
        deeds_service.register_deed(world_draw_platforms_deed, "action")
        deeds_service.register_deed(player_action_deed, "action")
        deeds_service.register_deed(player_move_deed, "action")
        deeds_service.register_deed(player_draw_deed, "action")
        deeds_service.register_deed(world_detect_platform_collisions_deed, "action")

        # game loop 
        while video_service.is_window_open():
            video_service.start_buffer()
            deed: Deed
            for deed in deeds_service.get_all_deeds(exclude_groups=['init']):
                deed.execute()
            video_service.end_buffer()
        service_manager.stop_all_services()
        
        

