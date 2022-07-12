from game.entities.entity import Entity
import pyray as pr
from game.deeds.start_services_deed import StartServicesDeed
from game.shared.color import Color


class BabyYeti(Entity):
    def __init__(self, service_manager=None, debug=None) -> None:
        super().__init__(service_manager, debug)
        self._texture = self._video_service.register_texture("Baby Yeti","yeti/game/entities/images/yeti.png")
        self._is_saved = False
        self._frameCount = 0
        self.x = self.position.x
        self.y = self.position.y

        self._frame_width = self._texture.width / 8
        self.direction = -1
        self._frame_height = self._texture.height / 6
        self._frame_timer = 0
        self.height = self._frame_height
        self.width = self._frame_width
        self._destination = pr.Rectangle()


    def draw(self): 
        baby_color = Color(255,180,145).get_tuple()
        x = self.position.x
        y = self.position.y
        source_x = self._frameCount * self._frame_width
        source_y = 0

        if self._is_saved:
            source_y = 5 * self._frame_height


        self.source = pr.Rectangle(source_x, source_y, self._frame_width * self.direction, self._frame_height)
        self._destination = pr.Rectangle(x, y, self._frame_width/1.5, self._frame_height/1.5)
        self.origin = pr.Vector2(0, 0)
        pr.draw_texture_pro(self._texture, self.source, self._destination, self.origin, 0, baby_color)

    def advance(self):
        self._frame_timer += self._video_service.get_frame_time()
        if self._frame_timer > .14:
            self._frameCount += 1
            self._frame_timer = 0
        if (self._frameCount < 4 and self._is_saved) or (self._is_saved and self._frameCount > 7):
            print(self._frameCount)
            self._frameCount = 4

    def get_hitbox(self):
        return self._destination


if __name__ == "__main__":
    service_manager = StartServicesDeed().execute()
    _vs = service_manager.video_service
    _ks = service_manager.keyboard_service
    baby_yeti = BabyYeti(service_manager)
    baby_yeti._is_saved = False
    baby_yeti.position = pr.Vector2(200,200)
    pr.set_target_fps(50)
    while _vs.is_window_open():
        _vs.start_buffer()
        baby_yeti.advance()
        baby_yeti.draw()
        _vs.end_buffer()
    service_manager.stop_all_services()
        