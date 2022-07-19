import pyray as pr
from game.deeds.deed import Deed
from game.shared.color import Color

class DrawBillboardsDeed(Deed):
    def __init__(self, service_manager=None, debug=False) -> None:
        super().__init__(service_manager, debug)
        self._height = int(self.video_service.get_height()*.15)
        self._text_color = Color().get_tuple()


    def execute(self):
        pr.draw_text("Good Luck!", 500, self._height, 50, self._text_color)
        pr.draw_text("Boss ahead!", self.video_service.get_game_width()-self.video_service._background_width, self._height, 50, self._text_color )