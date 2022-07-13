from game.deeds.deed import Deed

class ApplyGravityDeed(Deed):
    '''
    Applies gravity to objects. 

    Parameter - Entities: Nested list, each item in the entities list is expected to be a list of entitles. 

    Method - Execute() if item is not on solid ground, apply gravity based on weight.
    '''

    #TODO fix this deed to use either a single list or a single object, then call the deed multiple times,
    # rather than a nested list of entities. EG: entities[0][0]
    def __init__(self, entities,  service_manager=None, debug=False) -> None:
        super().__init__(service_manager, debug)
        self._entities = entities

    def execute(self):
        if self._debug:
            print("Entities: ", self._entities)
        for entity in self._entities:
            if self._debug:
                print("Specific Entity: ", entity)
            if not entity.is_on_solid_ground:
                if self._debug:
                    print("Entity is not on solid ground. He should fall at a rate of: ", 1*entity.weight)
                entity.position.y += 1 * entity.weight
                



if __name__ == "__main__":
    from game.entities.entity import Entity
    from game.deeds.start_services_deed import StartServicesDeed
    from game.deeds.world_apply_gravity_deed import ApplyGravityDeed
    import pyray as pr
    
    class Rock(Entity):

        def __init__(self) -> None:
            super().__init__()
            self.position.x = 100
            self.position.y = 100
            self.is_on_solid_ground = False
            self.weight = 1
        
        def draw(self):
            pr.draw_text("Test", self.position.x, self.position.y, 20, pr.WHITE)
            pr.draw_text(f"({self.position.x},{self.position.y})", 30,30,20,pr.WHITE)
        
        def advance(self):
            pass
            

    service_manager = StartServicesDeed().execute()
    video_service = service_manager.video_serivce
    r = Rock()
    apply_gravity_deed = ApplyGravityDeed([r])
    apply_gravity_deed.execute()



    while video_service.is_window_open():
        video_service.start_buffer()
        apply_gravity_deed.execute()
        r.draw()
        video_service.end_buffer()
    
    service_manager.stop_all_services()


