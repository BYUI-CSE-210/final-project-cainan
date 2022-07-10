from game.entities.bird import Bird
from game.deeds.deed import Deed

class MoveBirdsDeed(Deed):
    def __init__(self,birds:list, service_manager=None, debug=False) -> None:
        super().__init__(service_manager, debug)
        self.birds = birds
        
    def execute(self):
        if self._debug:
            print("Move Birds Deed - Birds list: ",self.birds)
        for bird in self.birds:
            bird:Bird
            bird.advance()
            bird.draw()
