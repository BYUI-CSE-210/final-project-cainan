import pyray as pr
from game.entities.entity import Entity
from game.shared.point import Point
from game.shared.color import Color

class Platform(Entity):
    def __init__(self, width=0, height=0, solid = True, fading_type=False, service_manager=None, debug=None) -> None:
        super().__init__(service_manager, debug)
        self._width = width
        self._height = height
        self.position = Point(0,0)
        self.solid = solid
        self._texture = self._video_service.register_texture("platform_snow", "yeti/game/entities/images/platform_snowy_interior.png")
        self._destination = pr.Rectangle()
        self._frame_time_counter = 0
        self._fade_delay = 0
        self._color: Color
        self._color = Color()
        self._fading_out = True
        self._fading_type = fading_type
        if self._debug:
            print("Platform: ", self.position.x, self.position.y)
    
    def draw(self):
        x = self.position.x
        y = self.position.y
        width = self._width
        height = self._height
        # pr.draw_rectangle(x,y,width,height,pr.RED)
        source = pr.Rectangle(0, 0, 32, 32)
        self._destination = pr.Rectangle(x, y, width, height)
        pr.draw_texture_tiled(self._texture, source, self._destination, pr.Vector2(0,0), 0, 1, self._color.get_tuple() )
    
    def advance(self):
        if not self._video_service.is_on_screen(self.position):
            return
        self._frame_time_counter += self._video_service.get_frame_time()
        alpha = self._color.get_tuple()[3]


        
      

        self._fade_delay += self._video_service.get_frame_time()
        if self._fade_delay > 10:
            if self._frame_time_counter > .12 and self._fading_type:
                if alpha < 1:
                    self._fading_out = False
                    self._fade_delay = 0
                elif alpha > 254:
                    self._fading_out = True
                    self._fade_delay = 0
                if self._fading_out:
                    alpha -= 1
                    self.solid = (alpha > 150)
                    
                else:
                    alpha += 1
                    self.solid = (alpha > 150)
                    
            
                self._color = Color(alpha=alpha)
                self._frame_time_counter = 0

    def get_width(self):
        return self._width

    def get_hitbox(self):
        # return pr.Rectangle(self.position.x, self.position.y, self._width, self._height)
        return self._destination