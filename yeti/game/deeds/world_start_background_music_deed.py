from game.deeds.deed import Deed

class StartBackgroundMusicDeed(Deed):
    def __init__(self, service_manager=None, debug=False) -> None:
        super().__init__(service_manager, debug)
        self.audio_service.register_sound("bg1", "yeti/game/entities/sounds/80sTech.wav" )

    
    def execute(self):
        self.audio_service.play_sound("bg1")