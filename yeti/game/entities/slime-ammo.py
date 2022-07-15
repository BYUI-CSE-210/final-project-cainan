from game.entities.axe import Axe
import pyray as pr
from game.deeds.start_services_deed import StartServicesDeed

class SlimeAmmo(Axe):
    def __init__(self, service_manager, starting_pos: pr.Vector2, direction, debug=False) -> None:
        super().__init__(service_manager, starting_pos, direction, debug)
        self.texture = self._video_service.register_texture("slime-ammo","game/entities/images/orange_guy.png")
        self._audio_service.register_sound("ammo-splat", "game/entities/sounds/splat.wav" )
        self.dest_divisor = 4
        self.origin_divisor = 6
        self.frame_divisor = 28
        self.destination = pr.Rectangle()

    def play_sound(self):
        self._audio_service.play_sound("ammo-splat")

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