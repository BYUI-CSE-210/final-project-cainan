from game.deeds.deed import Deed
from game.entities.axe import Axe

class ProjectileCreateDeed(Deed):
    def __init__(self, entity, projectiles:list, service_manager=None, debug=False, object_type=None) -> None:
        super().__init__(service_manager, debug)
        self._projectiles_list = projectiles
        self.entity = entity
        self._object_type = object_type

    def execute(self):
        if self._object_type:
            projectile = self._object_type(self.service_manager, self.entity.position, self.entity.direction)
        else:
            projectile = Axe(self.service_manager,self.entity.position,self.entity.direction)
        self._projectiles_list.append(projectile)
        if self._debug:
            print(self._projectiles_list)

        
        


