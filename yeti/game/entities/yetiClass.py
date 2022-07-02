from game.entities.entity import Entity
from game.shared.point import Point
import pyray as pr
from pyray import Vector2
from game.services.keyboard_service import KeyboardService
from game.services.audio_service import AudioService



class Yeti(Entity):
    def __init__(self,_keyboard_service,_audio_service) -> None:
        super().__init__()
        self.yetiSprite = pr.load_texture("game/entities/images/yeti.png")
        self.center = Point()
        self.x = self.center.x
        self.y = self.center.y
        self.timer = 0.0
        self.frame = int()
        self.frameWidth = int(self.yetiSprite.width/8)
        self.frameHeight = self.yetiSprite.height/6
        self.maxFrames = 8
        self.position = Vector2()
        self.rectangle = pr.Rectangle()

    def draw(self):
        self.position = Vector2(self.x,self.y)
        self.rectangle = pr.Rectangle(self.frameWidth * self.frame,0,self.frameWidth,self.frameHeight)
        self.picFrame = pr.draw_texture_rec(self.yetiSprite,self.rectangle,self.position,pr.WHITE)

    def advance(self):
        self.timer = float(0.0)
        self.frame = 0

if __name__ == "__main__":

    pr.init_window(900,750,"YetiQuest")
    pr.set_target_fps(60)
    _aud_serv = AudioService()
    _ks = KeyboardService()


    while not pr.window_should_close():
        yeti = Yeti(_ks,_aud_serv)
        pr.begin_drawing()
        pr.clear_background(pr.RAYWHITE)

        yeti.timer += pr.get_frame_time()

        if yeti.timer >= 0.2:
            yeti.timer = 0.0
            yeti.frame += 1
            print(f"frame: {yeti.frame}")
        
        yeti.frame = yeti.frame % yeti.maxFrames 

        yeti.draw()

        pr.end_drawing()


