from random import randint
from pyray import Rectangle
from game.entities.entity import Entity
from game.deeds.start_services_deed import StartServicesDeed
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


class Axeman(Entity):
    def __init__(self, service_manager=None, speed=10,_turn_after = 20, debug=False) -> None:
        super().__init__(service_manager, debug)
        self.texture = self._video_service.register_texture("Axeman","yeti/game/entities/images/lumberjack_walk.png")
        # self.axes = []
        self.weight = 3
        self.speed = speed
        self._pace_count = 0
        self.direction = -1
        self._turn_after = _turn_after
        self.frameCount = 1
        self.frameWidth = self.texture.width/5
        self.frameHeight = self.texture.height
        self.is_on_solid_ground = True

    def draw(self):
        # return super().draw()
        x = self.position.x
        y = self.position.y
        source_x = int(self.frameCount * self.frameWidth)
        source_y = 0
        self.source = pr.Rectangle(source_x,source_y,self.frameWidth * self.direction,self.frameHeight)
        self.destination = pr.Rectangle(x,y, self.frameWidth/4, self.frameHeight/4)
        self.origin = Vector2(x/2,y/2)
        pr.draw_texture_pro(self.texture,self.source,self.destination,self.origin,0,pr.RAYWHITE)
        if self._debug:
            pr.draw_rectangle(int(x),int(y),int(self.frameWidth),int(self.frameHeight),pr.GREEN)
            print("Drawing axeman at: ", x, y)

    def advance(self,x_direction,y_direction):
        # return super().advance()
        self._pace_count += 1
        if x_direction != 0:
            self.direction = x_direction
        self.frameCount += 1
        if self.frameCount >5:
            self.frameCount = 0
        self.position.x += x_direction * self.speed
        self.position.y += y_direction * self.speed
        # if self._pace_count >= self._turn_after:
        #     self.direction *= -1
        #     self._pace_count = 0
        #     self.axes.append(Axe)
        # if self.position.x <=0:
        #     self.direction = 0
        #     self._pace_count = 0
        #     self.axes.append(Axe)
        # if self.position.x >= pr.get_screen_width():
        #     self.direction = -1
        #     self._pace_count = 0
        #     self.axes.append(Axe)

    def do_action(self,action,entities:list):
        if action == 1:
            entities.append(axe)
            for axe in entities:
                axe = Axe()
                axe.draw()
                axe.advance()
        if action ==2:
            return

    def get_hitbox(self):
        return super().get_hitbox()


if __name__ == "__main__":
    _service_manager = StartServicesDeed().execute()
    _vs = _service_manager.video_service
    _ks = _service_manager.keyboard_service
    axeman = Axeman(_service_manager)
    entities=[]
    axe = Axe(_service_manager,Vector2(300,300),1)
    axeman.position.x = 140
    axeman.position.y = 140
    pr.set_target_fps(10)
    while _vs.is_window_open():
        _vs.start_buffer()
        input = _ks.get_direction()
        axeman.advance(input.x,input.y)
        axe.advance()
        axe.draw()
        axeman.draw()
        _vs.end_buffer()
    _service_manager.stop_all_services()