from game.entities.entity import Entity
from game.shared.point import Point

class Platform(Entity):
    def __init__(self, width=0, height=0, solid = True, service_manager=None, debug=None) -> None:
        super().__init__(service_manager, debug)
        self._width = width
        self._height = height
        self.position = Point(0,0)
        self._solid = solid

    def draw(self):
        return super().draw()
    
    def advance(self, player):
        return super().advance()