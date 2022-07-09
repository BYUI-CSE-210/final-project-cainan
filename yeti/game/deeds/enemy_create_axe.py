from game.deeds.deed import Deed
from game.entities.enemy import Axe

class AxeCreateDeed(Deed):
    def __init__(self, axeman,axes:list, service_manager=None, debug=False) -> None:
        super().__init__(service_manager, debug)
        self.axes = axes
        self.axeman = axeman

    def execute(self):
        axe = Axe(self.service_manager,self.axeman.position,self.axeman.direction)
        self.axes.append(axe)

        
        


