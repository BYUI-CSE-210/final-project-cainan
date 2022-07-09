from game.deeds.deed import Deed

class DrawPlatformsDeed(Deed):
    def __init__(self, platforms:list, service_manager=None, debug=False) -> None:
        super().__init__(service_manager, debug)
        self._platforms = platforms

    def execute(self):
        for platform in self._platforms:
            platform.draw()