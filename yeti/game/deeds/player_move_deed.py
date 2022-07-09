from game.deeds.deed import Deed
from game.services.keyboard_service import KeyboardService
from game.entities.yeti import Yeti

class PlayerMoveDeed(Deed):
    def __init__(self, service_manager, player, debug=False) -> None:
        super().__init__(service_manager, debug)
        self._keyboard_service: KeyboardService
        self._keyboard_service = service_manager.keyboard_service
        self._player: Yeti
        self._player = player
    
    def execute(self):
        direction = self._keyboard_service.get_direction()
        self._player.advance(direction.x, direction.y)
        
