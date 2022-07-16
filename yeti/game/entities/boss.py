from game.entities.entity import Entity
import pyray as pr
from game.shared.point import Point
from game.deeds.start_services_deed import StartServicesDeed
from game.deeds.boss_create_axe_deed import BossCreateAxeDeed

class GoblinBoss(Entity):
    """
    Create a GoblinBoss enemy for use in 
    the game. args:
    max_hp, speed
    """
    def __init__(self, axes_list, service_manager, max_hp = 5, speed = 7,  debug=None) -> None:
        super().__init__(service_manager, debug)
        self.weight = 0
        self.is_on_solid_ground = True
        
        self.max_hp = max_hp
        self.speed = speed
        self._service_manager = service_manager
        self._is_alive = True
        self.position = Point()
        self.direction = 1
        self.animation_list = []
        # self._action = 0 #0 idle, 1 attack, 2 hurt, 3 dying
        self._action = 'blink-idle'
        self.frameCount = 0
        self._frame_timer = self._video_service.get_frame_time()
        self.is_idle = False
        self.is_attacking = False
        self.is_hurt = False
        self._is_moving = False
        self.is_dying = False
               #Tom's load images code
        self._actions = ['blink-idle', 'attack', 'hurt', 'dying', 'run']
        for action_type in self._actions:
            for i in range(8):
                texture = self._video_service.register_texture(f'goblin_{action_type}_{i}', f'yeti/game/entities/images/goblin/{action_type}/{i}.png')
        self.frameHeight = texture.height - 126 - 65
        self.frameWidth = texture.width
        self._axes_list = axes_list
    def draw(self):
        """
        function to display the boss sprite
        on screen.
        """
        if not self._is_alive:
            self._action = self._actions[3]
        elif self.is_attacking:
            self._action = self._actions[1]
        elif self.is_hurt:
            self._action = self._actions[2]
        elif self._is_moving:
            self._action = self._actions[4]
        else:
            self._action = self._actions[0]
        self._texture = self._video_service.get_texture(f"goblin_{self._action}_{self.frameCount}")
        x = self.position.x
        y = self.position.y
        self.frameWidth = self._texture.width
        self.frameHeight = self._texture.height
        if self._debug:
            print("Goblin Size*****",self.frameHeight,self.frameWidth)
        source_x = self.frameWidth
        source_y = 0
        self.source = pr.Rectangle(source_x, source_y+65, self.frameWidth * self.direction, self.frameHeight)
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
    def advance(self,x_direction,y_direction):
        self._is_moving = abs(x_direction)
        self._frame_timer += self._video_service.get_frame_time()

        if self._frame_timer > .12:
            self.frameCount += 1
            self._frame_timer = 0
        if self.frameCount >=7:
            if self.is_alive:
                self.frameCount = 0
                self.is_attacking = False
                self.is_hurt = False
                
            else:
                self.frameCount = 7
        self.position.x += x_direction * self.speed

    def get_hitbox(self):
        # return super().get_hitbox()
        """
        return a rectangle for hit detection
        """
        return self._destination
    def got_hit(self):
        # return super().got_hit()
        self.max_hp -= 1
        if self.max_hp == 0:
            self._is_alive = False
            
    """Set action button being pressed to true"""
    def do_action(self, action):
       
        if action == 2:
            self.frameCount = 0
            self.is_attacking = True
            for i in range(3):
                create_axe = BossCreateAxeDeed(self,self._axes_list,self._service_manager,debug=False)
                create_axe.execute()
            if self._debug:
                print("Throwing Boss' axe!")
        if action == 3:
            self.frameCount = 0
            self.is_hurt = True
            
        if action == 4:
            self.is_dying = True
            self.frameCount = 7
            
        else:
            
            
            self.is_idle = True



