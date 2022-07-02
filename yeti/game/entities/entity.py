from abc import ABC, abstractmethod
from game.shared.point import Point

class Entity(ABC):

    def __init__(self) -> None:
        super().__init__()
        self.position = Point()

    @abstractmethod
    def advance(self):
        pass

    @abstractmethod
    def draw(self):
        pass

