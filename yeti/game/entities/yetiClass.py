from atexit import register
from re import X
import pyray as pr
from pyray import Vector2
from game.entities.entity import Entity
from game.shared.point import Point
from game.shared.color import Color
from game.services.keyboard_service import KeyboardService
from game.services.audio_service import AudioService
from game.services.video_service import VideoService



class Yeti(Entity):
    def __init__(self, x, y):
        #TODO: add weight property to Yeti
        #TODO: pass in a service_manager object to Yeti
        #TODO: call super from Yeti init.
        #TODO: rename this file to yeti.py instead of yetiClass.py
        self.x = x
        self.y = y
        self.speed = 1
        self._tint = Color().get_tuple()
        self.is_moving = False
        self._video_service = VideoService(20)
        self._texture = self._video_service.register_texture("yeti", f"game/entities/images/yeti.png")

    def draw(self):
        pr.draw_texture(self._texture, int(self.x), int(self.y), self._tint)

    def advance(self, x_direction, y_direction):
        self.x += x_direction * self.speed
        self.y += y_direction * self.speed
        if x_direction != 0 or y_direction != 0:
            self.is_moving = True


if __name__ == "__main__":
    pr.init_window(800,600,"Yeti Test")
    pr.set_target_fps(20)
    c = Yeti(int(pr.get_screen_width() // 2), int(pr.get_screen_height() // 2), )
    while not pr.window_should_close():
        pr.begin_drawing()
        pr.clear_background(pr.BLACK)
        x_direction = 0
        y_direction = 0
        if pr.is_key_down(pr.KEY_RIGHT):
            x_direction = 1
        if pr.is_key_down(pr.KEY_UP):
            y_direction = -1
        if pr.is_key_down(pr.KEY_LEFT):
            x_direction = -1
        if pr.is_key_down(pr.KEY_DOWN):
            y_direction = 1
        if pr.is_key_down(pr.KEY_ESCAPE):
            pr.window_should_close()
        c.advance(x_direction,y_direction)
        c.draw()
        pr.end_drawing()
    print(pr.get_screen_height())
    print(pr.get_screen_width())