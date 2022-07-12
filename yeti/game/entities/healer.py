from email.mime import audio
import pyray as pr
from game.entities.entity import Entity

class Healer(Entity):
    def __init__(self, service_manager=None, debug=None) -> None:
        super().__init__(service_manager, debug)
        self._texture = self._video_service.register_texture("Healer", "yeti/game/entities/images/healer.png")
        self._audio_service.register_sound("heal", "yeti/game/entities/sounds/heal.mp3")
        self._frame_width = self._texture.width/3
        self._frame_height = self._texture.height/4
        self._destination = pr.Rectangle()
        self.height = self._frame_height
        self.width = self._frame_width
        self._is_healing = False
        self._frame_count = 0
        self._frame_time_counter = 0

    def get_hitbox(self):
        return self._destination
    
    def advance(self):
        if self._is_healing:
            
            self._frame_time_counter += self._video_service.get_frame_time()
            if self._frame_time_counter > .3 :
                self._frame_count +=1
                self._frame_time_counter = 0
                if self._frame_count > 2:
                    self._frame_count = 0
                    self._is_healing = False


    
    def do_action(self, action):
        if action == 1:
            self._is_healing = True
            
            if not self._audio_service.is_sound_playing("heal"):
                self._audio_service.play_sound("heal")

    def draw(self):
        source = pr.Rectangle(self._frame_count*self._frame_width, 0, self._frame_width, self._frame_height)
        self._destination = pr.Rectangle(self.position.x,self.position.y, self._frame_width, self._frame_height)
        pr.draw_texture_pro(self._texture, source, self._destination, pr.Vector2(0,0), 0, pr.WHITE)
        if self._debug:
            pr.draw_rectangle(int(self._destination.x), int(self._destination.y), int(self._destination.width), int(self._destination.height), pr.RED)

