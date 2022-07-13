from game.entities.entity import Entity
import pyray as pr
from game.shared.point import Point
from game.deeds.start_services_deed import StartServicesDeed

class GoblinBoss(Entity):
    def __init__(self, service_manager, max_hp = 5, speed = 15,  debug=None) -> None:
        super().__init__(service_manager, debug)
        self.max_hp = max_hp
        self.speed = speed
        self._service_manager = service_manager
        self._is_alive = True
        self.position = Point()
        self._direction = 1
        self.animation_list = []
        self._action = 0 #0 idle, 1 attack, 2 hurt, 3 dying
        self.frameCount = 0
        self._frame_timer = self._video_service.get_frame_time()
        self.is_idle = True
        self.is_attacking = False
        self.is_hurt = False
        self.is_dying = False
        #load idle images
        temp_list = []
        image_num = 0
        for i in range(8):
            img = self._video_service.register_texture(f"Goblin{image_num}",f"game/entities/images/goblin/blink-idle/{image_num}.png")
            image_num += 1
            temp_list.append(img)
        self.animation_list.append(temp_list)
        #load attack images
        temp_list = []
        image_num = 0
        for i in range(8):
            img = self._video_service.register_texture(f"Goblin{image_num}",f"game/entities/images/goblin/attack/{image_num}.png")
            image_num += 1
            temp_list.append(img)
        self.animation_list.append(temp_list)
        #load hurt images
        temp_list = []
        image_num = 0
        for i in range(8):
            img = self._video_service.register_texture(f"Goblin{image_num}",f"game/entities/images/goblin/hurt/{image_num}.png")
            image_num += 1
            temp_list.append(img)
        self.animation_list.append(temp_list)
        #load attack images
        temp_list = []
        image_num = 0
        for i in range(8):
            img = self._video_service.register_texture(f"Goblin{image_num}",f"game/entities/images/goblin/dying/{image_num}.png")
            temp_list.append(img)
        self.animation_list.append(temp_list)
        self.image = self.animation_list[self._action][self.frameCount]

    def draw(self):
        # return super().draw()
        for list in self.animation_list:
            print("printing list...",list)
            for item in list:
                print("printing item...",item)
        
        self._texture = self.animation_list[self._action][self.frameCount]
        print("printing texture...",self.animation_list[self._action][self.frameCount])
        x = self.position.x
        y = self.position.y
        self.frameWidth = self._texture.width
        self.frameHeight = self._texture.height
        source_x = self.frameWidth
        source_y = 0
        self.source = pr.Rectangle(source_x, source_y, self.frameWidth * self._direction, self.frameHeight)
        self.destination = pr.Rectangle(x, y, self.frameWidth, self.frameHeight)
        self.origin = pr.Vector2(0, 0)
        pr.draw_texture_pro(self._texture, self.source, self.destination, self.origin, 0, pr.RAYWHITE)
        if self._debug:
            pr.draw_rectangle(int(self.destination.x),int(self.destination.y),int(self.destination.width),int(self.destination.height),pr.RED)

    def advance(self):
        self._frame_timer += self._video_service.get_frame_time()
        # print(f"frame-time: {self._frame_timer}")
        if self.is_idle:
            self.is_attacking = False
            self.is_hurt = False
            self.is_dying = False
            self._action = 0
        if self.is_attacking:
            self.is_idle = False
            self.is_hurt = False
            self.is_dying = False
            self._action = 1
        if self.is_hurt:
            self.is_idle = False
            self.is_attacking = False
            self.is_dying = False
            self._action = 2
        if self.is_dying:
            self.is_idle = False
            self.is_attacking = False
            self.is_hurt = False
            self._action = 3

        if self._frame_timer > .25:
            self.frameCount += 1
            self._frame_timer = 0
        if self.frameCount >=7:
            self.frameCount = 1

    def get_hitbox(self):
        return super().get_hitbox()


if __name__ == "__main__":
    service_manager = StartServicesDeed().execute()
    _vs = service_manager.video_service
    _ks = service_manager.keyboard_service
    boss = GoblinBoss(service_manager)
    boss.position = Point(200,200)
    boss.is_attacking = True
    pr.set_target_fps(50)
    while _vs.is_window_open():
        _vs.start_buffer()
        boss.advance()
        boss.draw()
        _vs.end_buffer()
    service_manager.stop_all_services()

