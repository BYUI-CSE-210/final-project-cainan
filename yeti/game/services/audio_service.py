import pyray as pr
from game.services.service import Service

class AudioService(Service):
    '''
    Class used to interface with the PyRay audio module.
    '''
    def __init__(self, debug = False) -> None:
        self._sounds = {}
        self._debug = debug
       
    def start_service(self):
        '''Initiates the sounds device using PyRay's audio interface.  Open the VideoService Window before you do this. Do this before you register sounds.'''
        pr.init_audio_device()
        pr.set_master_volume(.2)
        self._is_started = True
    
    def stop_service(self):
        '''Closes the sound device.'''
        pr.close_audio_device()
        self._is_started = False


    def register_sound(self, name, path, replace = False):
        '''
        Register a sound file with the AudioService. Giving it a name that can be called later. 
        This method returns the results of pyray.load_sound() which is a sound object
        parameters:
        name - The name used to reference the sound later
        path - The file path of the sound file to load
        replace - Tells the method to replace the sound at the given name.
        '''
        if name not in self._sounds:
            self._sounds[name] = pr.load_sound(path)
        if replace:
            self._sounds[name] = pr.load_sound(path)
        return self._sounds[name]

    def play_sound(self, name, stop_other_sounds = False):
        '''
        Uses the AudioService to play the sound by name. 
        parameters: 
        name - The name of the sound that was registered that you want to play
        stop_other_sounds - True causes the AudioService to stop all other playing sounds
        '''
        if name in self._sounds:
            if self._debug:
                print("playing sound: ", name, self._sounds[name], "stop others: ", stop_other_sounds)
            if stop_other_sounds:
                pr.stop_sound_multi()
                for s_name in self._sounds:
                    pr.stop_sound(self._sounds[s_name])
                pr.play_sound(self._sounds[name])
                return True    
            pr.play_sound_multi(self._sounds[name])
            if self._debug:
                print("Number of sounds playing: ", pr.get_sounds_playing())
            return True
        return False

    def get_sound(self, sound:str):
        if sound not in self._sounds.keys():
            return False
        return self._sounds[sound]
    
    def is_sound_playing(self, sound=None):
        '''Returns True if there is a sound playing in the multichanell buffer. False otherwise.'''
        if sound:
            sound_object = self.get_sound(sound) 
            if sound_object:
                return pr.is_sound_playing(sound_object)
            return False
        if pr.get_sounds_playing() > 0:
            return True
        return False

    def number_of_sounds_playing(self) -> int:
        '''Returns an int() number of sounds currently playing. '''
        return pr.get_sounds_playing()

if __name__ == "__main__":
    from game.services.video_service import VideoService
    from game.services.keyboard_service import KeyboardService
    audio_service = AudioService(True)
    kbd = KeyboardService()
    kbd.DOWN_KEY = pr.KEY_DOWN
    kbd.UP_KEY = pr.KEY_UP
    kbd.LEFT_KEY = pr.KEY_LEFT
    kbd.RIGHT_KEY = pr.KEY_RIGHT
    vs = VideoService(20)
    vs.start_service()
    kbd.start_service()
    audio_service.start_service()
    while not pr.is_audio_device_ready():
        print("Waiting for sound device")
    audio_service.register_sound("sound1", "game/entities/sounds/sound1.wav")
    audio_service.register_sound("player_error", "game/entities/sounds/player_error.wav")
    audio_service.register_sound("bg1", "game/entities/sounds/background1.mp3")
    audio_service.play_sound("bg1")
    while vs.is_window_open():
        vs.start_buffer()
        pr.draw_text("""
        You should be hearing background music.
        Press UP to test the player error sounds.
        Press RIGHT to trigger the laZers repeatedly.
        Press DOWN to trigger the LaZerS once.""", 10 , int(vs.get_height()/2), 20, pr.WHITE)
        if kbd.get_direction().x > 0:
            audio_service.play_sound("sound1")
        if kbd.get_direction(single_press=True).y > 0:
            audio_service.play_sound("sound1")
        if kbd.get_direction().y < 0:
            audio_service.play_sound("player_error")
        
        vs.end_buffer()
        if not vs.is_window_open():
            vs.stop_service()


  
    audio_service.stop_service()
    vs.stop_service()