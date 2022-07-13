from game.entities.entity import Entity
import pyray as pr
from game.shared.point import Point
from game.deeds.start_services_deed import StartServicesDeed

class GoblinBoss(Entity):
    """
    Create a GoblinBoss enemy for use in 
    the game. args:
    max_hp, speed
    """
    def __init__(self, service_manager, max_hp = 5, speed = 15,  debug=None) -> None:
        super().__init__(service_manager, debug)
        self.max_hp = max_hp
        self.speed = speed
        self._service_manager = service_manager
        self._is_alive = True
        self.position = Point()
        self._direction = 1
        self.animation_list = []
        # self._action = 0 #0 idle, 1 attack, 2 hurt, 3 dying
        self._action = 'blink-idle'
        self.frameCount = 0
        self._frame_timer = self._video_service.get_frame_time()
        self.is_idle = True
        self.is_attacking = False
        self.is_hurt = False
        self.is_dying = False
               #Tom's load images code
        self._actions = ['blink-idle', 'attack', 'hurt', 'dying']
        for action_type in self._actions:
            for i in range(8):
                self._video_service.register_texture(f'goblin_{action_type}_{i}', f'game/entities/images/goblin/{action_type}/{i}.png')

    def draw(self):
        """
        function to display the boss sprite
        on screen.
        """
        # return super().draw()
        for list in self.animation_list:
            print("printing list...",list)
            for item in list:
                print("printing item...",item)
        
        self._texture = self._video_service.get_texture(f"goblin_{self._action}_{self.frameCount}")
        x = self.position.x
        y = self.position.y
        self.frameWidth = self._texture.width
        self.frameHeight = self._texture.height
        source_x = self.frameWidth
        source_y = 0
        self.source = pr.Rectangle(source_x, source_y, self.frameWidth * self._direction, self.frameHeight)
        self._destination = pr.Rectangle(x, y, self.frameWidth, self.frameHeight)
        self.origin = pr.Vector2(0, 0)
        pr.draw_texture_pro(self._texture, self.source, self._destination, self.origin, 0, pr.RAYWHITE)
        if self._debug:
            pr.draw_rectangle(int(self._destination.x),int(self._destination.y),int(self._destination.width),int(self._destination.height),pr.RED)
    """
    Advance function that changes the 
    state of the boss between idle,
    attacking, hurt and dying
    """
    def advance(self):
        self._frame_timer += self._video_service.get_frame_time()
        if self.is_idle:
            self.is_attacking = False
            self.is_hurt = False
            self.is_dying = False
            self._action = self._actions[0]
        if self.is_attacking:
            self.is_idle = False
            self.is_hurt = False
            self.is_dying = False
            self._action = self._actions[1]
        if self.is_hurt:
            self.is_idle = False
            self.is_attacking = False
            self.is_dying = False
            self._action = self._actions[2]
        if self.is_dying:
            self.is_idle = False
            self.is_attacking = False
            self.is_hurt = False
            self._action = self._actions[3]

        if self._frame_timer > .12:
            self.frameCount += 1
            self._frame_timer = 0
        if self.frameCount >=7:
            self.frameCount = 0

    def get_hitbox(self):
        # return super().get_hitbox()
        """
        return a rectangle for hit detection
        """
        return self._destination


if __name__ == "__main__":
    service_manager = StartServicesDeed().execute()
    _vs = service_manager.video_service
    _ks = service_manager.keyboard_service
    boss = GoblinBoss(service_manager)
    boss.position = Point(200,200)
    boss.is_idle = False
    boss.is_attacking = True
    pr.set_target_fps(50)
    while _vs.is_window_open():
        _vs.start_buffer()
        boss.advance()
        boss.draw()
        _vs.end_buffer()
    service_manager.stop_all_services()
