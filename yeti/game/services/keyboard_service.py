import pyray as pr
from game.services.service import Service
from game.shared.point import Point


class KeyboardService(Service):

    def __init__(self) -> None:
        super().__init__()
        self.LEFT_KEY = None
        self.RIGHT_KEY = None
        self.UP_KEY = None
        self.DOWN_KEY = None
        self._is_started = False
        
    def start_service(self):
        if not self.LEFT_KEY:
            print("***********Using Default keys! This could conflict if you have more than one keyboard service!!***********")
            self.LEFT_KEY = pr.KEY_LEFT
            self.RIGHT_KEY = pr.KEY_RIGHT
            self.UP_KEY = pr.KEY_UP
            self.DOWN_KEY = pr.KEY_DOWN
        self._is_started = True
        return self._is_started
    
    def stop_service(self):
        self._is_started = False

    def get_direction(self, single_press = False):
        if not self._is_started:
            raise ValueError("Keyboard Service not started.")
        method = pr.is_key_down
        if single_press:
            method = pr.is_key_pressed
        p = Point(0,0)
        if method(self.UP_KEY):
            p.y = -1
        elif method(self.RIGHT_KEY):
            p.x = 1
        elif method(self.LEFT_KEY):
            p.x = -1
        elif method(self.DOWN_KEY):
            p.y = 1
        return p

    def _get_character_input(self):
        return pr.get_char_pressed()
    
    def _get_key_input(self):
        return pr.get_key_pressed()
    
    def get_character(self):
        character = self._get_key_input()
        if character == 257:
            return False
        return self._get_character_input()
   

    
if __name__ == "__main__":
    pr.init_window(800, 600, "Keyboard Test")
    pr.set_target_fps(20)
    kbd = KeyboardService()
    kbd.DOWN_KEY = pr.KEY_DOWN
    kbd.UP_KEY = pr.KEY_UP
    kbd.LEFT_KEY = pr.KEY_LEFT
    kbd.RIGHT_KEY = pr.KEY_RIGHT

    kbd2 = KeyboardService()
    kbd2.DOWN_KEY = pr.KEY_S
    kbd2.UP_KEY = pr.KEY_W
    kbd2.LEFT_KEY = pr.KEY_A
    kbd2.RIGHT_KEY = pr.KEY_D

    keyboards = [kbd, kbd2]

    while not pr.window_should_close():
        pr.begin_drawing()
        pr.clear_background(pr.BLACK)
        y_position = 150
        pr.draw_text("Use the Arrows Keys.", 200, y_position, 20, pr.WHITE)
        for keyboard in keyboards:
            y_position += 50
            d = keyboard.get_direction()
            text = f"The direction is ({d.x}, {d.y})"
            pr.draw_text(text,200,y_position,20,pr.WHITE)
    
        pr.end_drawing()
    pr.close_window()

