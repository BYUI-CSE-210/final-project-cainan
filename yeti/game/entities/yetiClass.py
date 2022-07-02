from yeti.game.entities.entity import Entity
from yeti.game.shared.point import Point
import pyray as pr
from pyray import Vector2



class Yeti(Entity):
    def __init__(self,_keyboard_service,_audio_service) -> None:
        super().__init__(_keyboard_service,_audio_service)
        self.center = Point()
        self.x = self.center.x
        self.y = self.center.y
        self.frameHeight = float
        self.frameWidth = float
        self.position = Vector2()
        self.rectangle = pr.Rectangle()

    def draw(self):
        self.yetiSprite = pr.load_texture("yeti/game/entities/images/yeti.png")
        self.frameWidth = float(self.yetiSprite/8)
        self.frameHeight = float(self.yetiSprite/6)
        self.maxFrames = int(self.yetiSprite.width/self.frameWidth)
        self.position = Vector2(self.x,self.y)
        self.rectangle = pr.Rectangle(self.frameWidth * self.frame,0,self.frameWidth,self.frameHeight)
        self.picFrame = pr.draw_texture_rec(self.yetiSprite,self.rectangle,self.position,pr.BLUE)

    def advance(self):
        self.timer = float(0.0)
        self.frame = 0

if __name__ == "__main__":

    pr.init_window(900,750,"YetiQuest")
    pr.set_target_fps(60)

    while not pr.window_should_close():
        yeti = Yeti()
        pr.begin_drawing()
        pr.clear_background(pr.RAYWHITE)

        yeti.timer += pr.get_frame_time()

        if yeti.timer >= 0.2:
            yeti.timer = 0.0
            yeti.frame += 1
        
        yeti.frame = yeti.frame % yeti.maxFrames 

        yeti.draw()

        pr.end_drawing()


