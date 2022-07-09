import pyray as pr
from game.entities.entity import Entity
from game.shared.point import Point

class Platform(Entity):
    def __init__(self, width=0, height=0, solid = True, service_manager=None, debug=None) -> None:
        super().__init__(service_manager, debug)
        self._width = width
        self._height = height
        self.position = Point(0,0)
        self.solid = solid
    
    def draw(self):
        x = self.position.x
        y = self.position.y
        width = self._width
        height = self._height
        pr.draw_rectangle(x,y,width,height,pr.RED)
    
    def advance(self):
        direction = self._keyboard_service.get_direction()
        if direction.y > 0:
            self.solid = False
        else:
            self.solid = True

    def get_hitbox(self):
        return pr.Rectangle(self.position.x, self.position.y, self._width, self._height)