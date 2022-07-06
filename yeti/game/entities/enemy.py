from game.entities.entity import Entity
from game.shared.point import Point
import pyray as pr
from pyray import Vector2
from game.services.keyboard_service import KeyboardService
from game.services.audio_service import AudioService

class Enemy(Entity):
    def __init__(self) -> None:
        super().__init__()
        self.center = Point
        self.x = self.center.get_x()
        self.y = self.center.get_y()
        #use the video service here to register the textures, this will prevent it from registering the file every time there is a new Enemy
        #self.texture = self._video_service.register_texture("reference_name", "path/to/file.png" )
        #NOTE you need to add the service_manager parameter to the init of this and pass it to the super call. 
        self.image = pr.load_texture("yeti/game/entities/images/lumberjack.png")
        