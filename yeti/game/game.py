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
from game.deeds.enemy_create_axeman import CreateAxemanDeed
from game.deeds.enemy_axeman_walk_deed import AxemanWalkDeed
from game.deeds.enemy_move_axes_deed import MoveAxesDeed


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


        #TODO move to world_create_platform_deed
        from random import randint
        platforms = []
        axemen = []
        axes = []
        platform_x = 50

        if self._debug:
            service_manager.show_all_services()
        video_service = service_manager.video_service
        audio_service = service_manager.audio_service
        keyboard_service = service_manager.keyboard_service
        deeds_service = service_manager.deeds_service
        world_draw_background_deed = DrawBackgroundDeed(service_manager)
        deeds_service.register_deed(world_draw_background_deed, "action")
        for i in range(60):
            platform = Platform(200, 20, service_manager=service_manager)
            platform.position.x = platform_x
            platform.position.y = randint(200, 800)
            platforms.append(platform)
            if i == 0:
                axeman = CreateAxemanDeed(platform, service_manager, debug=True).execute()
                axemen.append(axeman)
                print("AXEMAN ******", axeman)
                deeds_service.register_deed(AxemanWalkDeed(axeman, platform, service_manager, debug=True), "action")
            platform_x += randint(100,400)

        
        # action deeds 
        world_move_camera_deed = MoveCameraDeed(service_manager, yeti)
        #TODO create a list of Entities to be passed to the apply gravity deed. 
        world_apply_gravity_deed = ApplyGravityDeed([yeti], service_manager)
        world_draw_platforms_deed = DrawPlatformsDeed(platforms, service_manager)
        world_detect_platform_collisions_deed = DetectPlatformCollisionsDeed(platforms, yeti)
        player_action_deed = PlayerActionDeed(service_manager, yeti)
        player_move_deed = PlayerMoveDeed(service_manager, yeti)
        player_draw_deed = PlayerDrawDeed(yeti)
        move_axes_deed = MoveAxesDeed(axes,service_manager)
    


        # deed registration
        deeds_service.register_deed(world_move_camera_deed, "action")
        deeds_service.register_deed(world_apply_gravity_deed, "action")
        deeds_service.register_deed(world_draw_platforms_deed, "action")
        deeds_service.register_deed(player_action_deed, "action")
        deeds_service.register_deed(player_move_deed, "action")
        deeds_service.register_deed(player_draw_deed, "action")
        deeds_service.register_deed(world_detect_platform_collisions_deed, "action")
        deeds_service.register_deed(move_axes_deed,"action")

        # game loop 
        while video_service.is_window_open():
            video_service.start_buffer()
            deed: Deed
            for deed in deeds_service.get_all_deeds(exclude_groups=['init']):
                deed.execute()
            video_service.end_buffer()
        service_manager.stop_all_services()
        
        

