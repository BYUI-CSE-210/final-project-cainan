import pyray as pr
from game.entities.entity import Entity

class Healer(Entity):
    def __init__(self, service_manager=None, debug=None) -> None:
        super().__init__(service_manager, debug)
        self._texture = self._video_service.register_texture("Healer", "yeti/game/entities/images/healer.png")
        self._frame_width = self._texture.width/3
        self._frame_height = self._texture.height/4
        self._destination = pr.Rectangle()
        self.height = self._frame_height
        self.width = self._frame_width

    def get_hitbox(self):
        return self._destination
    
    def advance(self):
        return super().advance()
    
    def do_action(self):
        pass

    def draw(self):
        source = pr.Rectangle(0, 0, self._frame_width, self._frame_height)
        self._destination = pr.Rectangle(self.position.x,self.position.y, self._frame_width, self._frame_height)
        pr.draw_texture_pro(self._texture, source, self._destination, pr.Vector2(0,0), 0, pr.WHITE)
        if self._debug:
            pr.draw_rectangle(int(self._destination.x), int(self._destination.y), int(self._destination.width), int(self._destination.height), pr.RED)

