from pyray import Rectangle
from game.entities.entity import Entity
from game.deeds.start_services_deed import StartServicesDeed
import pyray as pr
from pyray import Vector2

class Axe(Entity):
    def __init__(self, service_manager) -> None:
        super().__init__(service_manager)
        self._service_manager = StartServicesDeed.execute()
        self.speed = 20
        self.weight = 1
        self.image = self._video_service.register_texture("flyingAxe","")

class Enemy(Entity):
    def __init__(self, service_manager=None) -> None:
        super().__init__(service_manager)
        self.speed = 10
        self.weight = 3
        self.image = pr.load_texture("game/entities/images/lumberjack_walk.png")
        # self.rect = Rectangle (0,0,int(self.image.width/7),int(self.image.height/2))
        # pr.draw_texture_rec(self.image,self.rect,Vector2(15,40),pr.WHITE)
        self.frameWidth = self.image.width/5
        self.frameHeight = self.image.height
        self.frameCount = 1
        self.direction = self.frameWidth
        
    def draw(self):
        x = self.position.x
        y = self.position.y
        source_x = int(self.frameCount * self.frameWidth)
        source_y = 0

        print("***********Frame: ", self.frameCount)
        print(f"Frame size: width:  {self.frameWidth}, height: {self.frameHeight}")
        print(source_x,source_y, "source starting point")
        print(source_x + self.frameWidth, source_y + self.frameHeight, 'source ending point')
        print("destination starting point", x, y)
        print('destination ending point', x+self.frameWidth, y+ self.frameHeight)
        self.source = pr.Rectangle(source_x,source_y,self.direction,self.frameHeight)
        self.destination = pr.Rectangle(x,y, self.frameWidth/4, self.frameHeight/4)
        self.origin = Vector2(x/2,y/2)
        pr.draw_texture_pro(self.image,self.source,self.destination,self.origin,0,pr.RAYWHITE)
        print("End frame*****************")

    def advance(self,x_direction,y_direction):
        self.position.x += x_direction * self.speed
        self.position.y += y_direction * self.speed
        if x_direction != 0 or y_direction != 0:
            self.is_moving = True
            self.direction = self.frameWidth * x_direction
            self.frameCount += 1
            if self.frameCount > 5:
                self.frameCount = 1


if __name__ == "__main__":
    from game.entities.enemy import Enemy
    pr.init_window(800,600,"ENEMY")
    
    enemy = Enemy()
    pr.set_target_fps(10)
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
        enemy.advance(x_direction,y_direction)
        enemy.draw()
        pr.end_drawing()
    pr.unload_texture(enemy)
    pr.close_window()