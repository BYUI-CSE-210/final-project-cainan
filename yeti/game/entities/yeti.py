from game.entities.entity import Entity
from game.services.video_service import VideoService
from game.shared.point import Point
from game.shared.color import Color

import pyray as pr
from pyray import Vector2
from pyray import Rectangle

#TODO: Add projectile yeti can throw
#TODO: Stretch Goal: Make double jump

class Yeti(Entity):
    def __init__(self, service_manager=None, debug=None) -> None:
        super().__init__(service_manager, debug)
        #TODO decide how much health is good. 
        self._max_health = 5
        self._health = 5
        self.weight = 4
        self.speed = 5
        self._texture = self._video_service.register_texture("Yeti", "yeti/game/entities/images/yeti.png")
        
        self.x = self.position.x
        self.y = self.position.y
        self.direction = 1

        self.frame_width = self._texture.width / 8
        self.frame_height = self._texture.height / 6
        self.frameCount = 0
        self._frame_timer = 0

        self.is_moving = False
        self.is_running = False
        self.is_jumping = False
        self.double_jump = False
        self.is_falling = False
        self.is_throwing = False
        self.is_taunting = False
        self.is_stunned = False
        
        self.jump_height = 25
        self._fall_distance = 0
        self._stun_timer = 0
        self._animation_timer = 0 
        self._jump_timer = 0

    def draw(self):
        x = self.position.x
        y = self.position.y
        source_x = self.frameCount * self.frame_width
        source_y = 0

        if self.is_moving:
            source_y = 1 * self.frame_height
        if self.is_running:
            source_y = 2 * self.frame_height
        if self.is_jumping:
            if self._jump_timer < 10:
                source_y = 3 * self.frame_height
        if self.is_falling:
            if self._fall_distance < 101:
                source_y = 3 * self.frame_height
            else:
                source_y = 4 * self.frame_height
        if self.is_stunned:
            source_y = 4 * self.frame_height
        if self.is_throwing or self.is_taunting:
            source_y = 5 * self.frame_height

        self.source = Rectangle(source_x, source_y, self.frame_width * self.direction, self.frame_height)
        self.destination = Rectangle(x, y, self.frame_width, self.frame_height)
        self.origin = Vector2(0, 0)
        pr.draw_texture_pro(self._texture, self.source, self.destination, self.origin, 0, pr.RAYWHITE)
        if self._debug:
            if self.is_stunned:
                color = Color(green=0, blue=0).get_tuple()
            else:
                color = Color(red=0, blue=0).get_tuple()

            pr.draw_rectangle(int(self.destination.x), int(self.destination.y), int(self.destination.width), int(self.destination.height), color)

    def advance(self, x_direction, y_direction):
        if not self.is_moving or self.is_jumping or self.is_falling:
            self.is_running = False
        if self.is_stunned:
            self.is_moving = False
            self.is_running = False
            self.is_throwing = False
            self.is_taunting = False
        if self.is_moving or self.is_running or self.is_jumping or self.is_falling:
            self.is_taunting = False
            self.is_throwing = False
        if self.is_taunting or self.is_throwing:
            self.is_moving = False
            self.is_running = False
            self.is_jumping = False
        
        if self.is_running:
            self.speed = 10
        else:
            self.speed = 5

        self._frame_timer += self._video_service.get_frame_time()
        if self._frame_timer > .14:
            self.frameCount += 1
            self._frame_timer = 0

        if not self.is_stunned:
            self.position.x += x_direction * self.speed
            self.position.y += y_direction * self.speed

            if not self.is_on_solid_ground:
                self.is_falling = True
                self._fall_distance += 1
                if self.is_jumping and self._jump_timer < 25:
                    if self.frameCount > 5 or self._jump_timer == 0:
                        self.frameCount = 0
                else:
                    if (self.frameCount < 6 and self._fall_distance < 100) or self.frameCount > 7:
                        self.frameCount = 6
                    if self.frameCount > 1 and self.is_falling and self._fall_distance > 100:
                        self.frameCount = 0
            elif self.is_falling:
                self.is_falling = False
                if self._fall_distance > 101:
                    self.is_stunned = True
                self._fall_distance = 0


            if (self.frameCount < 4 and self.is_taunting) or (self.is_taunting and self.frameCount > 7):
                self.frameCount = 4
            if self.frameCount > 7 or (self.frameCount > 3 and self.is_throwing):
                self.frameCount = 0

            if x_direction != 0 or y_direction != 0:
                self.is_moving = True
                self.direction = x_direction or 1
            else:
                self.is_moving = False
        else:
            self._stun_timer += self._video_service.get_frame_time()
            if (self.frameCount < 2 or self.frameCount > 7):
                self.frameCount = 2
                
            if self._stun_timer > 2:
                self.is_stunned = False
                self._stun_timer = 0


    def get_hitbox(self):
        return self.destination
    
    def got_hit(self):
        self.is_stunned = True
        self._health -= 1
    
    def do_action(self, action):
        self.is_running = False
        if action == 1:
            self.is_jumping = True
            self.jump()
        if action == 2:
            self.is_taunting = True
        if action == 3:
            self.is_running = True
        if action == 4:
            self.is_throwing = True
        
        
        if (self.is_throwing and self._animation_timer < 15) or (self.is_taunting and self._animation_timer < 60):
            self._animation_timer += 1
        else:
            self.is_taunting = False
            self.is_throwing = False
            self._animation_timer = 0
        
    def jump(self):
        if self.is_stunned or self.is_taunting or self.is_throwing:
            self.is_jumping = False
            self._jump_timer = 0
        elif (self._jump_timer < self.jump_height) and self.is_jumping:
            self.position.y -= 10
            self._jump_timer += 1
        elif self.is_on_solid_ground:
            self.is_jumping = False
            self._jump_timer = 0

    def get_hitbox(self):
        return self.destination
    
    def increase_health(self, hp):
        if self._health < self._max_health - hp:
            self._health += hp
        else:
            self._health = self._max_health
    
    def get_health(self):
        return self._health

if __name__ == "__main__":
    pr.init_window(800,600,"YETI")
    yeti = Yeti()
    yeti.position = Vector2(350.0, 280.0)
    current_frame = 0
    frames_counter = 0
    frame_speed = 8
    pr.set_target_fps(15)
    while not pr.window_should_close():
        pr.begin_drawing()
        pr.clear_background(pr.RAYWHITE)
        x_direction = 0
        y_direction = 0
        if pr.is_key_down(pr.KEY_RIGHT):
            x_direction = 1
        if pr.is_key_down(pr.KEY_UP):
            y_direction = -1
        if pr.is_key_down(pr.KEY_LEFT):
            x_direction = -1
        if pr.is_key_down(pr.KEY_DOWN):
            y_direction = 1
        if pr.is_key_down(pr.KEY_ESCAPE):
            pr.window_should_close()
        if pr.is_key_down(pr.KEY_LEFT_SHIFT):
            yeti.is_running = True
        if pr.is_key_released(pr.KEY_LEFT_SHIFT):
            yeti.is_running = False
        if pr.is_key_pressed(pr.KEY_SPACE):
            yeti.is_jumping = True

        yeti.advance(x_direction,y_direction)
        yeti.draw()
        pr.end_drawing()
    pr.unload_texture(yeti)
    pr.close_window()