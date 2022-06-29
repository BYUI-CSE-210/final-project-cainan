from abc import ABC, abstractmethod

class Service(ABC):

    def __init__(self) -> None:
        super().__init__()
        self._is_started = False
    
    def __bool__(self):
        return self._is_started

    @abstractmethod
    def start_service(self):
        '''
        Runs all the needed methods to get the service ready to use.
        '''
        pass

    @abstractmethod
    def stop_service(self):
        '''
        Shutsdown the service.
        '''
        pass
    