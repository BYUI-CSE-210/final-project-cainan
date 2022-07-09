from random import randint
from pyray import Rectangle
from game.entities.entity import Entity
import pyray as pr
from pyray import Vector2

class Axe(Entity):
    def __init__(self, service_manager,starting_pos:Vector2,direction) -> None:
        super().__init__(service_manager)
        self.position.x = starting_pos.x
        self.position.y = starting_pos.y
        self.direction = direction
        self.speed = 25
        self.weight = 1
        self.texture = self._video_service.register_texture("flyingAxe","game/entities/images/Axe.png")
        self._angle = int()
        self._spin = 20

    def draw(self):
        x = self.position.x
        y = self.position.y
        frameWidth = self.texture.width
        frameHeight = self.texture.height
        source = Rectangle(0,0,frameWidth,frameHeight)
        destination = Rectangle(x,y,frameWidth/6,frameHeight/6)
        origin = Vector2(frameWidth/12,frameHeight/12)
        pr.draw_texture_pro(self.texture,source,destination,origin,self._angle,pr.WHITE)

    def advance(self):
        # return super().advance()
        self.position.x += self.direction * self.speed
        self._angle += self._spin * self.direction

    def get_hitbox(self):
        return super().get_hitbox()
