import pyray as pr
from game.deeds.deed import Deed
from game.entities.orange_slime import OrangeSlime
from game.entities.platform import Platform

class SlimePlatformCollisionsDeed(Deed):
    def __init__(self, platforms: list, slime, service_manager=None, debug=False) -> None:
        super().__init__(service_manager, debug)
        self._platforms = platforms
        self._slime = slime
        self._slime: OrangeSlime
        self._debug = debug

    def execute(self):
        slime_hitbox = self._slime.get_hitbox()
        print(slime_hitbox.x,slime_hitbox.y,slime_hitbox.width,slime_hitbox.height)
        slime_hit_rectangle = pr.Rectangle(slime_hitbox.x,slime_hitbox.y,slime_hitbox.width,slime_hitbox.height)
        if self._debug:
            pr.draw_rectangle(int(slime_hit_rectangle.x), int(slime_hit_rectangle.y), int(slime_hit_rectangle.width), int(slime_hit_rectangle.height), pr.RED)
        
        

        for platform in self._platforms:
            platform: Platform
            platform_hitbox = platform.get_hitbox()
            platform_hit_rectangle = pr.Rectangle(platform_hitbox.x, platform_hitbox.y, platform_hitbox.width, 2)
            if self._debug:
                pr.draw_rectangle(int(platform_hit_rectangle.x), int(platform_hit_rectangle.y), int(platform_hit_rectangle.width), int(platform_hit_rectangle.height), pr.GREEN)
            colliding = pr.check_collision_recs(platform_hit_rectangle, slime_hit_rectangle)
            # print(f"checking slime collsion:{slime_hitbox}")
            # print(self._slime.is_on_solid_ground)
            # print(colliding)
            if colliding:
                self._slime.is_on_solid_ground = True
                break
            else:
                self._slime.is_on_solid_ground = False
            platform.advance()
            
