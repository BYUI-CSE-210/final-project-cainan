import pyray as pr
from game.shared.color import Color
from game.services.service import Service


class VideoService(Service):

    def __init__(self, framerate, width = 0, height = 0, caption = "Cycles", bg_color = None) -> None:
        super().__init__()
        self._width = width
        self._height = height
        self._caption = caption
        self._framerate = framerate
        self._textures = {}
        if not bg_color:
            bg_color = Color(0,0,0,255)    
        self._background_color = bg_color.get_tuple()
    
    def start_service(self):
        width = 0 
        height = 0 
        pr.init_window(width, height, self._caption)
        pr.set_target_fps(self._framerate)
        screen = pr.get_current_monitor()
        self._width = pr.get_monitor_width(screen)
        self._height = pr.get_monitor_height(screen)
        if self._height > 1200:
            self._height = 950
            self._width = 1750
            pr.set_window_size(self._width,self._height)
        else:
            pr.toggle_fullscreen()
        self._is_started = True
    
    def stop_service(self):
        pr.close_window()
        self._is_started = False
    
    def start_buffer(self):
        pr.begin_drawing()
        pr.clear_background(self._background_color)

    def end_buffer(self):
        pr.end_drawing(self)
    
    def is_window_open(self):
        return not pr.window_should_close()
       
    def get_width(self):
        '''Returns the width of the window'''
        return self._width
    
    def get_height(self):
        '''Returns the height of the window'''
        return self._height

    def register_texture(self, name, path):
        '''
        Registers a texture to use at a later date. Returns the results of pr.load_texture(path)
        Parameters:
        name - the reference name to use later when calling get_texture()
        path - the file path to the resource
        
        '''
        if name not in self._textures:
            print(f"Loaded textures: {self._textures}")
            texture = pr.load_texture(path)
            self._textures[name] = texture
        return self._textures[name]

    def get_texture(self, name):
        '''
        Returns a texture if one has been registered with the "name" parameter passed in. 
        Returns False if no texture has been registered with that name. 
        Parameters:
        name - the reference name used when a texture was registerd. 
        '''
        if name in self._textures:
            return self._textures[name]
        return False


if __name__ == "__main__":
    from game.deeds.start_services_deed import StartServicesDeed
    from game.services.video_service import VideoService
    start_services_deed = StartServicesDeed()
    service_manager = start_services_deed.execute()
    service_manager.show_all_services()
    video_service = service_manager.get_first_service(VideoService)
    keyboards = service_manager.get_services("input")
    kbd = keyboards[0]

    x = 0
    y = 0

    while video_service.is_window_open():
        video_service.start_buffer()
        pr.draw_text("Use the arrow keys.",200, 200, 20, Color().get_tuple())
        direction = kbd.get_direction()
        x = (x + direction.x * 10) % video_service.get_width()
        y = (y + direction.y * 10) % video_service.get_height()
        pr.draw_text(f"Current position is: ({x}, {y})", 20, 20, 20, pr.WHITE)
        pr.draw_text(f"The max width and height should be: {video_service.get_width()} by {video_service.get_height()}. The square is 10x10.", 20, 50, 20, pr.WHITE )
        pr.draw_rectangle(x,y,10,10,pr.WHITE)
        video_service.end_buffer()

    video_service.stop_service()