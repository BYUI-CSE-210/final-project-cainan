from game.entities.axe import Axe
from game.deeds.deed import Deed

class MoveAxesDeed(Deed):
    def __init__(self,axes:list, service_manager=None, debug=False) -> None:
        super().__init__(service_manager, debug)
        self.axes = axes
        
    def execute(self):
        # return super().execute()
        if self._debug:
            print("Move Axes Deed - Axes list: ",self.axes)
        for axe in self.axes:
            axe:Axe
            axe.advance()
            axe.draw()

