from game.entities.entity import Entity
from game.services.video_service import VideoService
from game.shared.point import Point

import pyray as pr
from pyray import Vector2
from pyray import Rectangle

#TODO: Make sure yeti cant sprint while standing still 
#TODO: Animation for yeti crashing into the ground
#TODO: Add projectile yeti can throw
#TODO: Make sure animations reset when they first start

class Yeti(Entity):
    def __init__(self, service_manager=None, debug=None) -> None:
        super().__init__(service_manager, debug)
        
        self.weight = 3
        self.speed = 5
        self._texture = self._video_service.register_texture("Yeti", "yeti/game/entities/images/yeti.png")
        
        self.x = self.position.x
        self.y = self.position.y

        self.frameWidth = self._texture.width / 8
        self.frameHeight = self._texture.height / 6
        self.frameCount = 0
        self._frame_timer = 0

        self.is_moving = False
        self.is_running = False
        self.is_jumping = False
        self.is_falling = False
        self.is_throwing = False
        self.is_taunting = False
        self.direction = 1
        self._fall_distance = 0


    def draw(self):
        x = self.position.x
        y = self.position.y
        source_x = self.frameCount * self.frameWidth
        source_y = 0

        if self.is_moving:
            source_y = 1 * self.frameHeight
        if self.is_running:
            source_y = 2 * self.frameHeight
        if self.is_jumping:
            source_y = 3 * self.frameHeight
        if self.is_falling:
            if self._fall_distance < 51:
                source_y = 3 * self.frameHeight
            else:
                source_y = 4 * self.frameHeight
        if self.is_throwing or self.is_taunting:
            source_y = 5 * self.frameHeight

        self.source = Rectangle(source_x, source_y, self.frameWidth * self.direction, self.frameHeight)
        self.destination = Rectangle(x, y, self.frameWidth, self.frameHeight)
        self.origin = Vector2(0, 0)
        pr.draw_texture_pro(self._texture, self.source, self.destination, self.origin, 0, pr.RAYWHITE)

    def advance(self, x_direction, y_direction):
        if self.is_running:
            self.speed = 10
        else:
            self.speed = 5

        self.position.x += x_direction * self.speed
        self.position.y += y_direction * self.speed

        self._frame_timer += self._video_service.get_frame_time()
        if self._frame_timer > .12:
            self.frameCount += 1
            self._frame_timer = 0

        if not self.is_on_solid_ground:
            self.is_falling = True
            self._fall_distance += 1
        else:
            self.is_falling = False
            self._fall_distance = 0
        if (self.frameCount < 6 and self.is_falling and self._fall_distance < 50) or (self.is_falling and self.frameCount > 7):
           self.frameCount = 6
        if self.frameCount > 1 and self.is_falling and self._fall_distance > 50:
           self.frameCount = 0
        
        if (self.frameCount < 4 and self.is_taunting) or (self.is_taunting and self.frameCount > 7):
            self.frameCount = 4
        if self.frameCount > 7 or (self.frameCount > 4 and self.is_throwing):
            self.frameCount = 0

        if x_direction != 0 or y_direction != 0:
            self.is_moving = True
            self.direction = x_direction or 1
        else:
            self.is_moving = False

    def get_hitbox(self):
        return self.destination
    
    def do_action(self, action):
        self.is_running = False
        self.is_jumping = False
        self.is_throwing = False
        self.is_taunting = False
        if action == 1:
            self.is_jumping = True
        if action == 2:
            self.is_taunting = True
        if action == 3:
            self.is_running = True
        if action == 4:
            self.is_throwing = True
        
    def get_hitbox(self):
        return self.destination
        

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