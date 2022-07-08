from pyray import Rectangle
from game.entities.entity import Entity
from game.shared.point import Point
import pyray as pr
from pyray import Vector2

class Enemy(Entity):
    def __init__(self) -> None:
        super().__init__()

        self.center = Point()
        self.x = self.center.x
        self.y = self.center.y
        self.image = None
        
    def draw(self):
        x = self.center.x
        y = self.center.y
        self.image = pr.load_texture("game/entities/images/lumberjack.png")
        # self.rect = Rectangle (0,0,int(self.image.width/7),int(self.image.height/2))
        # pr.draw_texture_rec(self.image,self.rect,Vector2(15,40),pr.WHITE)
        self.frameWidth = self.image.width/7
        self.frameHeight = self.image.height/2
        self.source = Rectangle(0,0,self.frameWidth,self.frameHeight)
        self.destination = Rectangle(140,140,self.frameWidth/2,self.frameHeight/2)
        self.origin = Vector2(self.frameWidth/4,self.frameHeight/4)
        pr.draw_texture_pro(self.image,self.source,self.destination,self.origin,0,pr.RAYWHITE)

    def advance(self,_keyboard_service):
        

if __name__ == "__main__":
    pr.init_window(800,600,"ENEMY")
    enemy = Enemy()
    enemy.position = Vector2(350.0, 280.0)
    current_frame = 0
    frames_counter = 0
    frame_speed = 8
    pr.set_target_fps(60)
    while not pr.window_should_close():
        frames_counter += 1
        if frames_counter >= (60/frame_speed):
            frames_counter = 0
            current_frame += 1
            if current_frame >5:
                current_frame = 0
                enemy.source.x = current_frame * enemy.image.width/7
        pr.begin_drawing()
        pr.clear_background(pr.RAYWHITE)
        enemy.draw()
        pr.end_drawing()
    pr.unload_texture(enemy)
    pr.close_window()