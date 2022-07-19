from game.deeds.deed import Deed
from game.services.keyboard_service import KeyboardService
from game.entities.yeti import Yeti

class PlayerActionDeed(Deed):
    def __init__(self, service_manager, player, debug=False) -> None:
        super().__init__(service_manager, debug)
        self._keyboard_service: KeyboardService
        self._keyboard_service = service_manager.keyboard_service
        self._player: Yeti
        self._player = player
    
    def execute(self):
        action = self._keyboard_service.get_action(single_press=True)
        if self._debug:
            print(action)
        self._player.do_action(action)
        
