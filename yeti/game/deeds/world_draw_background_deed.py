import pyray as pr
from game.deeds.deed import Deed
from game.shared.point import Point
class DrawBackgroundDeed(Deed):

    def __init__(self, service_manager) -> None:
        super().__init__(service_manager)
        self._background = self.video_service.register_texture("background", "game/entities/images/background.png")
        
    def execute(self):
        background_width = 4048
        background_height = 1024        
        source_rect = pr.Rectangle(0, 0, background_width, background_height)
        dest_rect = pr.Rectangle(0, 0, background_width, self.video_service.get_height())
        origin = pr.Vector2(0,0)

        pr.draw_texture_pro(self._background, source_rect, dest_rect, origin, 0, pr.WHITE )
        dest_rect = pr.Rectangle(background_width, 0, background_width*2, self.video_service.get_height())
        pr.draw_texture_pro(self._background, source_rect, dest_rect, origin, 0, pr.WHITE )
        


#  This is just to test the deed to make sure it works
if __name__ == "__main__":

    class Player:
        def __init__(self) -> None:
            self.x = 0
            self.y = 0
    
    from game.deeds.start_services_deed import StartServicesDeed
    from game.services.video_service import VideoService
    service_manager = StartServicesDeed().execute()
    service_manager.show_all_services()
    video_service = service_manager.get_first_service(VideoService)
    keyboards = service_manager.get_services("input")
    kbd = keyboards[0]
    player = Player()
    x = 300
    y = 1000
    camera = pr.Camera2D( pr.Vector2(video_service.get_width()/2,0), pr.Vector2(player.x, player.y), 0, 1)

    from game.deeds.world_draw_background_deed import DrawBackgroundDeed
    draw_background_deed = DrawBackgroundDeed(service_manager)

    while video_service.is_window_open():
        video_service.start_buffer()
        pr.begin_mode_2d(camera)
        
        draw_background_deed.execute()
        

        # get input deed
        direction = kbd.get_direction()

        # move deed
        x = (x + direction.x * 10) 
        y = (y + direction.y * 10) 
        player.x = x
        player.y = y
        if player.x < video_service.get_width()/2:
            camera.target = pr.Vector2(video_service.get_width()/2,0)
        elif player.x > ((4048 * 2) - video_service.get_width()/2): 
            camera.target = pr.Vector2((4048 * 2 - video_service.get_width()/2), 0)
        else:
            camera.target = pr.Vector2(player.x, 0)
        # draw text deed
        pr.draw_text(f"Current position is: ({x}, {y})", 20, 20, 20, pr.WHITE)
        pr.draw_text(f"Current position is: ({x}, {y})", 4000, 20, 20, pr.WHITE)
        pr.draw_text(f"Current position is: ({x}, {y})", 7000, 20, 20, pr.WHITE)
        # draw text deed
        pr.draw_text(f"The max width and height should be: {video_service.get_width()} by {video_service.get_height()}. The square is 10x10.", 20, 50, 20, pr.WHITE )
        pr.draw_text(f"The max width and height should be: {video_service.get_width()} by {video_service.get_height()}. The square is 10x10.", 4000, 50, 20, pr.WHITE )
        pr.draw_text(f"The max width and height should be: {video_service.get_width()} by {video_service.get_height()}. The square is 10x10.", 7000, 50, 20, pr.WHITE )

        # draw rect deed
        pr.draw_rectangle(x,y,10,10,pr.RED)
        pr.end_mode_2d(camera)
        video_service.end_buffer()

    service_manager.stop_all_services()
    service_manager.show_all_services()