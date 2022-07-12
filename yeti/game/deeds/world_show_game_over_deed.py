import pyray as pr
from game.deeds.deed import Deed
from game.shared.color import Color
from game.shared.point import Point

class ShowGameOverDeed(Deed):
    def __init__(self, player, service_manager=None, debug=False) -> None:
        super().__init__(service_manager, debug)
        self._position = player.position
    
    def execute(self):
        if self._position.x < self.video_service.get_width()/2:
            center = Point(int(self.video_service.get_width()/2), int(self.video_service.get_height()/2))
        elif self._position.x > self.video_service.get_game_width() - self.video_service.get_width()/2:
            #TODO confirm this by falling off the "boss" end of the screen
            center = Point(int(self.video_service.get_game_width()-self.video_service.get_width()/2), self.video_service.get_height())
        else:
            center = Point(int(self._position.x), int(self.video_service.get_height()/2))
        pr.draw_rectangle_gradient_v(int(center.x - self.video_service.get_width()/2), 0, self.video_service.get_width(), 
            self.video_service.get_height(), Color(255,0,0).get_tuple(), Color(0,0,0,255).get_tuple())
        pr.draw_text("GAME OVER", center.x, center.y, 50, pr.WHITE)
        pr.draw_text("Press esc to close the window.", center.x, center.y + 55, 30, pr.WHITE)