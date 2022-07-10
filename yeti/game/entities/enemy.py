from random import randint
from pyray import Rectangle
from game.entities.entity import Entity
from game.deeds.start_services_deed import StartServicesDeed
from game.deeds.enemy_create_axe import AxeCreateDeed
import pyray as pr
from pyray import Vector2

class Axeman(Entity):
    def __init__(self, service_manager=None, speed=5,_turn_after = 20, debug=False) -> None:
        super().__init__(service_manager, debug)
        self.texture = self._video_service.register_texture("Axeman","yeti/game/entities/images/lumberjack_walk.png")
        self.weight = 3
        self.speed = speed
        self._pace_count = 0
        self.direction = -1
        self._turn_after = _turn_after
        self.frameCount = 1
        self.frameWidth = self.texture.width/5
        self.scaled_frameWidth = self.frameWidth/4
        self.frameHeight = self.texture.height
        self.scaled_frameHeight = self.frameHeight/4
        self.is_on_solid_ground = True
        self._frame_timer = 0

        
    def draw(self):
        self._texture = self._video_service.get_texture("Axeman")
        x = self.position.x
        y = self.position.y
        source_x = self.frameCount * self.frameWidth
        source_y = 0
        self.source = pr.Rectangle(source_x,source_y,self.frameWidth * self.direction, self.frameHeight)
        self.destination = pr.Rectangle(x,y - self.scaled_frameHeight,self.frameWidth/4,self.frameHeight/4)
        self.origin = Vector2(0,0)
        pr.draw_texture_pro(self._texture, self.source,self.destination,self.origin,0,pr.RAYWHITE)
        if self._debug:
            pr.draw_rectangle(int(self.destination.x),int(self.destination.y),int(self.destination.width),int(self.destination.height),pr.WHITE)

    def advance(self,x_direction,y_direction):
        # return super().advance()
        self._frame_timer += self._video_service.get_frame_time()
        if self._frame_timer > .12:
            self.frameCount += 1
            self._frame_timer = 0
        if (self.frameCount < 3):
            self.frameCount = 2
        if self.frameCount > 3:
            self.frameCount = 0
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

    def do_action(self,action,axes:list):
        if action == 1:
            create_axe = AxeCreateDeed(self,axes,self._service_manager,debug=False)
            create_axe.execute()
            if self._debug:
                print("Throwing axe!")

    def get_hitbox(self):
        return self.destination

    


