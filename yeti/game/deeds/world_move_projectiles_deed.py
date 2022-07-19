from game.entities.slime_ammo import SlimeAmmo
from game.deeds.deed import Deed

class MoveProjectilesDeed(Deed):
    def __init__(self,slimes:list, service_manager=None, debug=False) -> None:
        super().__init__(service_manager, debug)
        self._slimes_list = slimes
        
    def execute(self):
        # return super().execute()
        if self._debug:
            print("Move Projectiles Deed - Projectiles list: ",self.axes)
        for slime in self._slimes_list:
            slime:SlimeAmmo
            slime.advance()
            slime.draw()

