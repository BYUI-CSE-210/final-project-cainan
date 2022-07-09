import pyray as pr
from game.deeds.deed import Deed
from game.entities.yeti import Yeti

class DetectPlatformCollisionsDeed(Deed):
    def __init__(self, platforms: list, player, service_manager=None, debug=False) -> None:
        super().__init__(service_manager, debug)
        self._platforms = platforms
        self._player: Yeti
        self._player = player

    def execute(self):
        player_hitbox = self._player.get_hitbox()
        feet_line_start = pr.Vector2(player_hitbox.x, player_hitbox.y + player_hitbox.height)
        feet_line_end = pr.Vector2(player_hitbox.x + player_hitbox.width, player_hitbox.y + player_hitbox.height)
        pr.draw_line(int(feet_line_start.x), int(feet_line_start.y), int(feet_line_end.x), int(feet_line_end.y), pr.BLUE)
        for platform in self._platforms:
            platform_hitbox = platform.get_hitbox()
            platform_line_start = pr.Vector2(platform_hitbox.x, platform_hitbox.y)
            platform_line_end = pr.Vector2(platform_hitbox.x + platform_hitbox.width, platform_hitbox.y)
            # colliding = pr.check_collision_recs(platform_hitbox, player_hitbox)
            cp = pr.Vector2(0,0)
            pr.draw_line(int(platform_line_start.x), int(platform_line_start.y), int(platform_line_end.x), int(platform_line_end.y), pr.GREEN)
            colliding = pr.check_collision_lines(feet_line_start, feet_line_end, platform_line_start, platform_line_end, cp)
            print(cp.x)
            if colliding and platform.solid:
                self._player.is_on_solid_ground = True
                break
            else:
                self._player.is_on_solid_ground = False
            platform.advance()
            
