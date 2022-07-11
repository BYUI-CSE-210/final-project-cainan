import pyray as pr
from game.deeds.deed import Deed
from game.entities.entity import Entity

class DetectPlatformCollisionsDeed(Deed):
    def __init__(self, platforms: list, player, service_manager=None, debug=False) -> None:
        super().__init__(service_manager, debug)
        self._platforms = platforms
        self._player: Entity
        self._player = player

    def execute(self):
        player_hitbox = self._player.get_hitbox()
        player_hit_rectangle = pr.Rectangle(player_hitbox.x + (player_hitbox.width/4), player_hitbox.y + (player_hitbox.height-2), player_hitbox.width/1.5, 3)
        if self._debug:
            pr.draw_rectangle(int(player_hit_rectangle.x), int(player_hit_rectangle.y), int(player_hit_rectangle.width), int(player_hit_rectangle.height), pr.BLUE)
        
        

        for platform in self._platforms:
            platform_hitbox = platform.get_hitbox()
            platform_hit_rectangle = pr.Rectangle(platform_hitbox.x, platform_hitbox.y, platform_hitbox.width, 2)
            if self._debug:
                pr.draw_rectangle(int(platform_hit_rectangle.x), int(platform_hit_rectangle.y), int(platform_hit_rectangle.width), int(player_hit_rectangle.height), pr.GREEN)
            colliding = pr.check_collision_recs(platform_hit_rectangle, player_hit_rectangle)
            if colliding and platform.solid:
                self._player.is_on_solid_ground = True
                break
            else:
                self._player.is_on_solid_ground = False
            platform.advance()
            
