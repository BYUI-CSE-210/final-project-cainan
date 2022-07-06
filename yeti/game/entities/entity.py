from abc import ABC, abstractmethod
from game.shared.point import Point

class Entity(ABC):

    def __init__(self) -> None:
        super().__init__()
        self.position = Point()
        self._weight = 0

    @abstractmethod
    def advance(self):
        pass

    @abstractmethod
    def draw(self):
        pass

    @property
    def weight(self):
        '''
        Weight of an entity is used to apply gravity to the entity. 
        
        See the world_apply_gravity_deed.py:
        Something that has 2 weight is twice as heavy as something with 1.'''
        return self._weight
    
    @weight.setter
    def set_weight(self, weight):
        self._weight = weight

