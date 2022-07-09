from game.entities.axe import Axe
from game.deeds.deed import Deed

class RemoveOldAxesDeed(Deed):
    def __init__(self, axes:list, service_manager=None, debug=False) -> None:
        super().__init__(service_manager, debug)
        self._axes = axes

    def execute(self):
        axe: Axe
        for axe in self._axes:
            if axe._alive_time > axe._max_alive_time:
                self._axes.remove(axe)