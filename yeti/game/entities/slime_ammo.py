from game.entities.axe import Axe
import pyray as pr
from game.deeds.start_services_deed import StartServicesDeed

class SlimeAmmo(Axe):
    def __init__(self, service_manager, starting_pos: pr.Vector2, direction, debug=False) -> None:
        super().__init__(service_manager, starting_pos, direction, debug)
        self.texture = self._video_service.register_texture("slime-ammo","yeti/game/entities/images/orange_guy.png")
        self._audio_service.register_sound("ammo-splat", "yeti/game/entities/sounds/splat.wav" )
        self.dest_divisor = 4
        self.origin_divisor = 56
        self.frame_divisor = 28
        self.destination = pr.Rectangle()

    def play_sound(self):
        self._audio_service.play_sound("ammo-splat")

    def draw(self):
        x = self.position.x
        y = self.position.y
        frameWidth = self.texture.width
        frameHeight = self.texture.height
        source = pr.Rectangle(0,0,frameWidth,frameHeight)
        self.destination = pr.Rectangle(x,y+frameHeight/self.frame_divisor/2,frameWidth/self.frame_divisor ,frameHeight/self.frame_divisor )
        origin = pr.Vector2(frameWidth/self.origin_divisor,frameHeight/self.origin_divisor)
        pr.draw_texture_pro(self.texture,source,self.destination,origin,self._angle,pr.WHITE)
        if self._video_service.is_on_screen(self.position):
            self.play_sound()
        if self._debug:
            pr.draw_rectangle(int(self.destination.x), int(self.destination.y), int(self.destination.width), int(self.destination.height), pr.GREEN)


if __name__ == "__main__":
    service_manager = StartServicesDeed().execute()
    _vs = service_manager.video_service
    _ks = service_manager.keyboard_service
    ammo = SlimeAmmo(service_manager,pr.Vector2(500,500),1)
    pr.set_target_fps(50)
    print("Frame size",ammo.texture.width, ammo.texture.height)
    while _vs.is_window_open():
        _vs.start_buffer()
        # ammo.advance()
        # print("drawing slime")
        ammo.draw()
        print("Destination size:", ammo.destination.x,ammo.destination.y,ammo.destination.width,ammo.destination.height)
        _vs.end_buffer()
    service_manager.stop_all_services()