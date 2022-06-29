from game.services.service import Service

class DeedsService(Service):
    '''
    The deeds service allows for "deeds" or "deeds" to be registered to groups. Then returns the groups when called.

    It requires no parameters.
    '''

    def __init__(self) -> None:
        super().__init__()
        self._deeds = {}

   
    def start_service(self):
        self._is_started = True
    
    def stop_service(self):
        self._is_started = False

    def register_deed(self, deed, group):
        '''
        Register and deed or deed to a group. 

        Parameters:
        deed - an instance of the deed class or it's children (deeds)
        group - a string specifying the group name the deed should be in
        '''
        if group not in self._deeds.keys():
            self._deeds[group] = []
        if deed not in self._deeds[group]:
            self._deeds[group].append(deed)

    def get_deeds(self, group):
        '''
        Returns all deeds in the specified group
        
        group - string 
        '''

        return self._deeds[group]

    def get_all_deeds(self, exclude_groups = []):
        '''
        Returns all deeds in a dictionary with group names as keys.
        '''
        deeds = []
        for group in self._deeds.keys():
            if group not in exclude_groups:
                for deed in self._deeds[group]:
                    deeds.append(deed)
        return deeds

    

    def get_first_deed(self, group):
        '''
        Returns the first deed in the group

        group - string
        '''
        return self._deeds[group][0]

    def get_last_deed(self, group):
        '''
        Returns the last deed in the group.

        group - string
        '''
        group = self._deeds[group]
        return group[-1]