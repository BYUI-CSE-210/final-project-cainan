from game.deeds.deed import Deed

class DrawHealersDeed(Deed):
    def __init__(self, healers_list:list, service_manager=None, debug=False) -> None:
        super().__init__(service_manager, debug)
        self._healers = healers_list
    def execute(self):
        for healer in self._healers:
            healer.advance()
            healer.draw()
        
