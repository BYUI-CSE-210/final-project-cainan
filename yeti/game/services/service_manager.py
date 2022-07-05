from time import perf_counter
from game.services.service import Service


class ServiceManager:
    '''
    ServiceManager class maintains a collection of services.
    '''

    def __init__(self, debug = False) -> None:
        self._services = {}
        self._debug = debug

    @property
    def video_serivce(self):
        return self.get_first_service(VideoService)

    @property
    def audio_service(self):
        return self.get_first_service(AudioService)
     
    @property
    def keyboard_service(self):
        return self.get_first_service(KeyboardService)

    def register_service(self, service, group):
        '''
        Register a service to a group in the ServiceManager.

        service - Service Object 
        group - String
        '''
        if group not in self._services.keys():
            self._services[group] = []
        self._services[group].append(service)
    
    def get_services(self, group):
        '''
        Returns all services in the group.

        group - String
        '''
        return self._services[group]

    def get_first_service(self, item_type):
        '''
        Returns the first service of item_type. 

        item_type - The class type of the service you want back. Example:  KeyboardService
        '''

        for group in self._services.keys():
            if self._debug:
                print(f"Looking in {group} for {item_type}.")
            for service in self._services[group]:
                if self._debug:
                    print(f"Is {type(service)} an instance of {item_type}? {isinstance(service, item_type)}")
                if isinstance(service, item_type):
                    return service
        
    def start_all_services(self):
        '''
        Triggers the start_service() method for all services that have been registered.
        '''

        if self._debug:
            print("Services dictionary", self._services)
        for group in self._services:
            if self._debug:
                print("Starting Group: ", group)
            service: Service
            for service in self._services[group]:
                if self._debug:
                    print("Starting Service: ", service)
                service.start_service()
                
    def stop_all_services(self):
        '''
        Triggers the stop_service() method for all services that have been registered.
        '''

        if self._debug:
            print("Services dictionary", self._services)
        for group in self._services:
            if self._debug:
                print("Stopping Group: ", group)
            service: Service
            for service in self._services[group]:
                if self._debug:
                    print("Stopping Service: ", service)
                service.stop_service()

    def show_all_services(self):
        '''
        Shows all services that have been registered and their current state (running or not).
        '''


        for group in self._services:
            service: Service
            for service in self._services[group]:
                print(f"Service {service} is running: {bool(service)}")


if __name__ == "__main__":
    from game.services.deeds_service import DeedsService
    from game.services.keyboard_service import KeyboardService
    from game.services.audio_service import AudioService
    from game.services.video_service import VideoService

    service_manager = ServiceManager()
    keyboard_service1 = KeyboardService()
    audio_service = AudioService()
    video_service = VideoService(20)
    deed_service = DeedsService()

    service_manager.register_service(keyboard_service1, "input")
    service_manager.register_service(audio_service, "output")
    service_manager.register_service(video_service, "output")
    service_manager.register_service(deed_service, "control")

    service_manager.start_all_services()
    service_manager.show_all_services()

    print("Audio service: ", service_manager.get_first_service(AudioService))
