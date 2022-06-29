class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self,other):
        x = self.x + other.get_x()
        y = self.y + other.get_y()

    def equals(self,other):
        return self.x == other.get_x() and self.y == other.get_y()

    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y

    def reverse(self):
        new_x = self.x * -1
        new_y = self.y * -1
        return Point(new_x,new_y)

    def scale(self,factor):
        return Point(self.x * factor ,self.y * factor)