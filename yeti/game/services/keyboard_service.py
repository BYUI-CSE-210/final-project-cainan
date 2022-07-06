import pyray as pr
from game.services.service import Service
from game.shared.point import Point


class KeyboardService(Service):
    '''Service to interact with the keyboard. Default keys are the arrow keys.'''
    def __init__(self) -> None:
        super().__init__()
        self.LEFT_KEY = None
        self.RIGHT_KEY = None
        self.UP_KEY = None
        self.DOWN_KEY = None
        self.ACTION_ONE = None
        self.ACTION_TWO = None
        self._is_started = False
        
    def start_service(self):
        if not self.LEFT_KEY:
            print("***********Using Default keys! This could conflict if you have more than one keyboard service!!***********")
            self.LEFT_KEY = pr.KEY_LEFT
            self.RIGHT_KEY = pr.KEY_RIGHT
            self.UP_KEY = pr.KEY_UP
            self.DOWN_KEY = pr.KEY_DOWN
            self.ACTION_ONE = pr.KEY_SPACE
            self.ACTION_TWO = pr.KEY_ENTER
            self.ACTION_THREE = pr.KEY_LEFT_SHIFT
            self.ACTION_FOUR = pr.KEY_LEFT_CONTROL
        self._is_started = True
        return self._is_started
    
    def stop_service(self):
        self._is_started = False

    def get_direction(self, single_press = False):
        '''
        Gets the direction being pressed.  Returns a Point() object.

        The returned point object will be between the range of (-1,-1) and (1,1)
        '''
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
    
    def get_action(self, single_press = False):
        '''
        returns the number of the action button pressed. Eg. return 1 if ACTION_ONE button is pressed.
        '''

        if not self._is_started:
            raise ValueError("Keyboard Service not started.")
        method = pr.is_key_down
        if single_press:
            method = pr.is_key_pressed
        
        if method(self.ACTION_ONE):
            return 1
        if method(self.ACTION_TWO):
            return 2
        if method(self.ACTION_THREE):
            return 3
        if method(self.ACTION_FOUR):
            return 4


   

    
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

