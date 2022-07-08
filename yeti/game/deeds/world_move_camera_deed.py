from game.deeds.deed import Deed

class MoveCameraDeed(Deed):
    def __init__(self, service_manager, debug=False) -> None:
        super().__init__(service_manager, debug)
