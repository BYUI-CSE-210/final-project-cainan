from game.deeds.deed import Deed
from game.entities.entity import Entity

class PlayerDrawDeed(Deed):
    def __init__(self, player, service_manager=None, debug=False) -> None:
        self._player: Entity
        self._player = player

    def execute(self):
        self._player.draw()