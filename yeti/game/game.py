from game.services.service_manager import ServiceManager
from game.entities.yeti import Yeti
from game.entities.platform import Platform
from game.deeds.deed import Deed
from game.deeds.start_services_deed import StartServicesDeed
from game.deeds.world_draw_background_deed import DrawBackgroundDeed
from game.deeds.world_move_camera_deed import MoveCameraDeed
from game.deeds.world_apply_gravity_deed import ApplyGravityDeed
from game.deeds.world_draw_platforms_deed import DrawPlatformsDeed
from game.deeds.world_create_platforms_deed import CreatePlatformsDeed
from game.deeds.world_detect_platform_collisions_deed import DetectPlatformCollisionsDeed
from game.deeds.player_action_deed import PlayerActionDeed
from game.deeds.player_move_deed import PlayerMoveDeed
from game.deeds.player_draw_deed import PlayerDrawDeed
from game.deeds.enemy_create_axeman import CreateAxemanDeed
from game.deeds.create_slime_deed import CreateSlimeDeed
from game.deeds.enemy_axeman_walk_deed import AxemanWalkDeed
from game.deeds.slime_walk_deed import OrangeSlimeWalkDeed
from game.deeds.enemy_move_axes_deed import MoveAxesDeed
from game.deeds.enemy_remove_old_axes_deed import RemoveOldAxesDeed
from game.deeds.create_bird_deed import CreateBirdDeed
from game.deeds.move_birds_deed import MoveBirdsDeed
from game.deeds.player_detect_enemy_collisions_deed import PlayerDetectEnemyCollisionsDeed
from game.deeds.slime_platform_collision_deed import SlimePlatformCollisionsDeed
from game.entities.healer import Healer
from game.deeds.world_draw_hud_deed import DrawHudDeed
from game.deeds.world_create_healers_deed import CreateHealersDeed
from game.deeds.world_detect_healer_collisions_deed import DetectHealerCollisionsDeed



class Game:
    def __init__(self, debug=False) -> None:
        self._debug = debug
    
    def start_game(self):
        # game initialization
        service_manager: ServiceManager
        service_manager = StartServicesDeed().execute()
        video_service = service_manager.video_service
        audio_service = service_manager.audio_service
        keyboard_service = service_manager.keyboard_service
        deeds_service = service_manager.deeds_service
        yeti = Yeti(service_manager)
        yeti.position.x = 100
        yeti.position.y = video_service.get_height() - 300


        #TODO move to world_create_platform_deed
        platforms = []
        axemen = []
        slimes=[]
        axes = []
        birds = []
        healers = []


        CreatePlatformsDeed(platforms, service_manager).execute()

        if self._debug:
            service_manager.show_all_services()
        world_draw_background_deed = DrawBackgroundDeed(service_manager)
        deeds_service.register_deed(world_draw_background_deed, "action")
        for i in range(60):
            platform = platforms[i]
            if not i % 12 and not i ==0:
                bird = CreateBirdDeed(service_manager).execute()
                birds.append(bird)
                axeman = CreateAxemanDeed(platform, service_manager).execute()
                axemen.append(axeman)
                print("AXEMAN ******", axeman)
                deeds_service.register_deed(AxemanWalkDeed(axeman, platform, service_manager), "action")
            if not i % 5:
                slime = CreateSlimeDeed(platform,service_manager).execute()
                slimes.append(slime)
                deeds_service.register_deed(OrangeSlimeWalkDeed(slime,platform,service_manager,debug=False),"action")
                slime_platform_collsions_deed = DetectPlatformCollisionsDeed(platforms,slime)
                deeds_service.register_deed(slime_platform_collsions_deed,"action")



        
        # action deeds 
        world_move_camera_deed = MoveCameraDeed(service_manager, yeti)
        #TODO create a list of Entities to be passed to the apply gravity deed. 
        yeti_apply_gravity_deed = ApplyGravityDeed([yeti], service_manager)
        axes_apply_gravity_deed = ApplyGravityDeed(axes, service_manager)
        slime_apply_gravity_deed = ApplyGravityDeed(slimes,service_manager)
        world_draw_platforms_deed = DrawPlatformsDeed(platforms, service_manager)
        world_detect_platform_collisions_deed = DetectPlatformCollisionsDeed(platforms, yeti)
        player_action_deed = PlayerActionDeed(service_manager, yeti)
        player_move_deed = PlayerMoveDeed(service_manager, yeti)
        player_draw_deed = PlayerDrawDeed(yeti)
        move_axes_deed = MoveAxesDeed(axes,service_manager)
        remove_old_axes_deed = RemoveOldAxesDeed(axes, service_manager)
        move_birds_deed = MoveBirdsDeed(birds,service_manager)
        player_detect_enemy_collisions_deed = PlayerDetectEnemyCollisionsDeed(yeti, axes, axemen, birds, slimes, service_manager,debug=True)
        draw_hud_deed = DrawHudDeed(yeti, service_manager)
        world_create_healers = CreateHealersDeed(healers, service_manager)
        world_detect_healer_collisions_deed = DetectHealerCollisionsDeed(yeti, healers)
    


        # deed registration
        deeds_service.register_deed(world_move_camera_deed, "action")
        deeds_service.register_deed(yeti_apply_gravity_deed, "action")
        deeds_service.register_deed(axes_apply_gravity_deed, "action")
        deeds_service.register_deed(slime_apply_gravity_deed,"action")
        deeds_service.register_deed(world_draw_platforms_deed, "action")
        deeds_service.register_deed(player_action_deed, "action")
        deeds_service.register_deed(player_move_deed, "action")
        deeds_service.register_deed(world_create_healers, "action")
        deeds_service.register_deed(player_draw_deed, "action")
        deeds_service.register_deed(world_detect_platform_collisions_deed, "action")
        deeds_service.register_deed(move_axes_deed,"action")
        deeds_service.register_deed(remove_old_axes_deed, "action")
        deeds_service.register_deed(move_birds_deed,"action")
        deeds_service.register_deed(player_detect_enemy_collisions_deed, "action")
        deeds_service.register_deed(draw_hud_deed, "action")
        deeds_service.register_deed(world_detect_healer_collisions_deed, "action")

        # game loop 
        frame_time_counter = 0
        while video_service.is_window_open():
            video_service.start_buffer()
            deed: Deed
            for deed in deeds_service.get_all_deeds(exclude_groups=['init']):
                deed.execute()
            
            frame_time_counter += video_service.get_frame_time()
            if frame_time_counter > 2:
                for axeman in axemen:
                    axeman.do_action(1, axes)
                for slime in slimes:
                    slime.do_action(1)
                frame_time_counter = 0
            video_service.end_buffer()
        service_manager.stop_all_services()
        
        

