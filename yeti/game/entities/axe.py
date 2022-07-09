import pyray as pr
from game.entities.entity import Entity


class Axe(Entity):
    def __init__(self, service_manager,starting_pos:pr.Vector2,direction) -> None:
        super().__init__(service_manager)
        self.position.x = starting_pos.x
        self.position.y = starting_pos.y
        self.direction = direction
        self.speed = 25
        self._weight = 3
        self.texture = self._video_service.register_texture("flyingAxe","yeti/game/entities/images/axe.png")
        self._angle = int()
        self._spin = 20
        self._alive_time = 0 
        self._max_alive_time = 3
        self._axe_weight_coefficient = 5

    def draw(self):
        x = self.position.x
        y = self.position.y
        frameWidth = self.texture.width
        frameHeight = self.texture.height
        source = pr.Rectangle(0,0,frameWidth,frameHeight)
        destination = pr.Rectangle(x,y - frameHeight/4,frameWidth/6,frameHeight/6)
        origin = pr.Vector2(frameWidth/12,frameHeight/12)
        pr.draw_texture_pro(self.texture,source,destination,origin,self._angle,pr.WHITE)

    def advance(self):
        # return super().advance()
        self.position.x += self.direction * self.speed
        self._angle += self._spin * self.direction
        self._alive_time += self._video_service.get_frame_time()

    def get_hitbox(self):
        return super().get_hitbox()

    @property
    def weight(self):
        return self._weight * (self._axe_weight_coefficient * self._alive_time)