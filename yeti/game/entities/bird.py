from game.entities.entity import Entity
import pyray as pr
from pyray import Rectangle,Vector2
from game.deeds.start_services_deed import StartServicesDeed
from game.shared.point import Point
class Bird(Entity):
    def __init__(self, service_manager=None, debug=None) -> None:
        super().__init__(service_manager, debug)
    # def __init__(self,service_manager) -> None:
    #     super().__init__(service_manager)
        self._texture = self._video_service.register_texture("bird1","yeti/game/entities/images/bird-1.png")
        self._video_service.register_texture("bird2","yeti/game/entities/images/bird-2.png")
        self._video_service.register_texture("bird3","yeti/game/entities/images/bird-3.png")
        self._video_service.register_texture("bird4","yeti/game/entities/images/bird-4.png")
        self.frameCount = 1
        self.frameWidth = self._texture.width
        self.frameHeight = self._texture.height
        self.direction = -1
        self.speed = 15
        self.timeCounter = 0


    def advance(self):
        # return super().advance()
        self.timeCounter += 1
        self.frameCount += 1
        if self.frameCount >= 4:
            self.frameCount = 1
        if self.timeCounter >= 30:
            self.direction *= -1
            self.timeCounter= 0
        self.position.x += self.direction * self.speed
        

    def draw(self):
        # return super().draw()
        self._texture = self._video_service.get_texture(f"bird{self.frameCount}")
        x = self.position.x
        y = self.position.y
        source_x = self.frameCount * self.frameWidth
        source_y = 0
        self.source = Rectangle(source_x, source_y, self.frameWidth * self.direction, self.frameHeight)
        self.destination = Rectangle(x, y, self.frameWidth/12, self.frameHeight/12)
        self.origin = Vector2(0, 0)
        pr.draw_texture_pro(self._texture, self.source, self.destination, self.origin, 0, pr.RAYWHITE)
        # pr.draw_rectangle(int(self.destination.x),int(self.destination.y),int(self.destination.width),int(self.destination.height),pr.RED)


    def get_hitbox(self):
        return self.destination


if __name__ == "__main__":
    service_manager = StartServicesDeed().execute()
    _vs = service_manager.video_service
    _ks = service_manager.keyboard_service
    bird = Bird(service_manager)
    bird.position = Point(200,200)
    while _vs.is_window_open():
        _vs.start_buffer()
        bird.advance()
        bird.draw()
        _vs.end_buffer()
    service_manager.stop_all_services()