import pyray as pr
from game.deeds.deed import Deed


class MoveCameraDeed(Deed):
    '''
    Moves camera to Vector2() target.
    
    Param: target can be any object with a .x and .y property. 
    '''
    def __init__(self, service_manager, target, debug=False ) -> None:
        super().__init__(service_manager, debug)
        #TODO if yeti starts using position instead of center we need to update the next line. 
        #The camera won't follow the yeti.
        self._target = target.center
        assert isinstance(self._target.x, float) or isinstance(self._target.x, int), "Target of MoveCameraDeed needs to have an x property, it must be a float/int. Eg: target.x"
        assert isinstance(self._target.y, float) or isinstance(self._target.y, int), "Target of MoveCameraDeed needs to have a y property, it must be a float/int. Eg: target.y"
        

    def execute(self):
        target = pr.Vector2(self._target.x, 0)

        if target.x < self.video_service.get_width()/2:
            self.video_service.set_camera_target(pr.Vector2(self.video_service.get_width()/2,0))
        elif target.x > ((4048 * 2) - self.video_service.get_width()/2): 
            self.video_service.set_camera_target(pr.Vector2((4048 * 2 - self.video_service.get_width()/2), 0))
        else:
            self.video_service.set_camera_target(pr.Vector2(target.x, 0))


        