from pyray import Rectangle
from game.entities.entity import Entity
from game.shared.point import Point
from game.deeds.start_services_deed import StartServicesDeed
import pyray as pr
from pyray import Vector2

class Enemy(Entity):
    def __init__(self) -> None:
        super().__init__()
        self.speed = 10
        self.weight = 3
        #TODO: inherit point from Entity and correct methods accordingly
        self.center = Point()
        self.x = self.center.x
        self.y = self.center.y
        self.image = pr.load_texture("game/entities/images/lumberjack_walk.png")
        # self.rect = Rectangle (0,0,int(self.image.width/7),int(self.image.height/2))
        # pr.draw_texture_rec(self.image,self.rect,Vector2(15,40),pr.WHITE)
        self.frameWidth = self.image.width/7
        self.frameHeight = self.image.height/2
        self.frameCount = 0
        
    def draw(self):
        x = self.center.x
        y = self.center.y
        source_x = self.frameCount * self.frameWidth
        source_y = 0
        print(f"height: {self.frameHeight}, width:  {self.frameWidth}")
        print(source_x,source_y)
        print(source_x + self.frameWidth, source_y + self.frameHeight)
        self.source = Rectangle(source_x,source_y,source_x + self.frameWidth,source_y + self.frameHeight)
        self.destination = Rectangle(x,y,x + self.frameWidth,y + self.frameHeight)
        self.origin = Vector2(source_x,source_y)
        pr.draw_texture_pro(self.image,self.source,self.destination,self.origin,0,pr.RAYWHITE)

    def advance(self,x_direction,y_direction):
        self.center.x += x_direction * self.speed
        self.center.y += y_direction * self.speed
        if x_direction != 0 or y_direction != 0:
            self.is_moving = True
        self.frameCount += 1
        if self.frameCount > 6:
            self.frameCount = 0

if __name__ == "__main__":
    pr.init_window(800,600,"ENEMY")
    enemy = Enemy()
    enemy.position = Vector2(350.0, 280.0)
    current_frame = 0
    frames_counter = 0
    frame_speed = 8
    pr.set_target_fps(5)
    while not pr.window_should_close():
        pr.begin_drawing()
        pr.clear_background(pr.RAYWHITE)
        x_direction = 0
        y_direction = 0
        if pr.is_key_down(pr.KEY_RIGHT):
            x_direction = -1
        if pr.is_key_down(pr.KEY_UP):
            y_direction = 1
        if pr.is_key_down(pr.KEY_LEFT):
            x_direction = 1
        if pr.is_key_down(pr.KEY_DOWN):
            y_direction = -1
        if pr.is_key_down(pr.KEY_ESCAPE):
            pr.window_should_close()
        enemy.advance(x_direction,y_direction)
        enemy.draw()
        pr.end_drawing()
    pr.unload_texture(enemy)
    pr.close_window()