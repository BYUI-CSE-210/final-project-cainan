from game.entities.entity import Entity
import pyray as pr
from pyray import Vector2,Rectangle
from game.shared.point import Point
from game.deeds.start_services_deed import StartServicesDeed

class OrangeSlime(Entity):
    def __init__(self, service_manager=None, speed=3,_turn_after = 20, debug=False) -> None:
        super().__init__(service_manager, debug)
        self.texture = self._video_service.register_texture("OrangeSlime","yeti/game/entities/images/OrangeSlimeSimp.png")
        self._weight = 1
        self._slime_weight_coefficient = 3
        self._jump_height = 128
        self.speed = speed
        self._pace_count = 0
        self.direction = -1
        self._turn_after = _turn_after
        self.frameCount = 1
        self.frameWidth = self.texture.width/3.05
        self.scaled_frameWidth = self.frameWidth * 2
        self.frameHeight = self.texture.height
        self.scaled_frameHeight = self.frameHeight * 2
        self.is_on_solid_ground = True
        self._frame_timer = 0
        self._jump_timer = 0
        self.is_jumping = False

    def draw(self):
        self._texture = self._video_service.get_texture("OrangeSlime")
        x = self.position.x
        y = self.position.y
        source_x = self.frameCount * self.frameWidth
        source_y = 0
        self.source = Rectangle(source_x,source_y,self.frameWidth * self.direction, self.frameHeight)
        self._destination = Rectangle(x,y - self.scaled_frameHeight,self.scaled_frameWidth,self.scaled_frameHeight)
        self.origin = Vector2(0,0)
        pr.draw_texture_pro(self._texture, self.source,self._destination,self.origin,0,pr.RAYWHITE)
        if self._debug:
            pr.draw_rectangle(int(self._destination.x),int(self._destination.y),int(self._destination.width),int(self._destination.height),pr.WHITE)

           
            

    def advance(self,x_direction,y_direction):
        self._frame_timer += self._video_service.get_frame_time()
        # print(f"frame-time: {self._frame_timer}")
        dy = 8
        if self._frame_timer > 0.04:
            if self._jump_timer < self._jump_height and self.is_jumping:
                self.position.y -= dy
                self._jump_timer +=16
                # print(f"Jump Timer********: {self._jump_timer}")
            else:
                self.is_jumping = False
                self._jump_timer = 0
                # print(f"Jumping switching to False!")

        if self._frame_timer > .15:
            self.frameCount += 1
            self._frame_timer = 0
        if self.frameCount > 3:
            self.frameCount = 1
        if x_direction != 0:
            self.direction = x_direction * -1
        self._pace_count += 1
        self.position.x += x_direction * self.speed
        self.position.y += y_direction * self.speed

    def get_hitbox(self):
        return self._destination
    
    def got_hit(self):
        self._is_alive = False

    def jump(self):
        self.is_jumping = True

    def do_action(self,action):
        dy = 10
        if action == 1:
            self.jump()

    @property
    def weight(self):
        if self._jump_timer <= self._jump_height and self.is_jumping:
            return 0
        return 2
        # return self._weight * (self._slime_weight_coefficient / self._jump_timer)



if __name__ == "__main__":
    service_manager = StartServicesDeed().execute()
    _vs = service_manager.video_service
    _ks = service_manager.keyboard_service
    slime = OrangeSlime(service_manager)
    slime.position = Point(200,200)
    pr.set_target_fps(50)
    while _vs.is_window_open():
        _vs.start_buffer()
        slime.advance(_ks.get_direction().x,_ks.get_direction().y)
        slime.draw()
        _vs.end_buffer()
    service_manager.stop_all_services()