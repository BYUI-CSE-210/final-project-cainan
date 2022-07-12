import pyray as pr
from game.deeds.deed import Deed
from game.shared.point import Point
from game.shared.color import Color
from game.entities.yeti import Yeti

class DrawHudDeed(Deed):
    def __init__(self, player, service_manager=None, debug=False) -> None:
        super().__init__(service_manager, debug)
        self._player: Yeti
        self._player = player
        self._health_bar_position = Point(20,20)
        self._health_bar_position_offset = Point(20,20)
        self._text_color = Color(255).get_tuple()
        self._font_size = 20
        
    
    def execute(self):
        target = pr.Vector2(self._player.position.x, 0)

        if target.x < self.video_service.get_width()/2:
            self.health_bar_position = self._health_bar_position_offset
        elif target.x > (self.video_service.get_game_width() - self.video_service.get_width()/2): 
            self.health_bar_position = Point(self.video_service.get_game_width() - self.video_service.get_width() + self._health_bar_position_offset.x, self._health_bar_position_offset.y)
        else:
            
            self.health_bar_position = Point(target.x - (self.video_service.get_width()/2) + self._health_bar_position_offset.x, self._health_bar_position_offset.y)

        pr.draw_text(str(f"HP: {self._player.get_health()}"), int(self.health_bar_position.x), int(self.health_bar_position.y), self._font_size, self._text_color)