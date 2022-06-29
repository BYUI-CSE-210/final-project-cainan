from typing import List
from game.services.service import Service

class ActionsService(Service):
    '''
    The actions service allows for "deeds" or "actions" to be registered to groups. Then returns the groups when called.

    It requires no parameters.
    '''

    def __init__(self) -> None:
        super().__init__()
        self._actions = {}

   
    def start_service(self):
        self._is_started = True
    
    def stop_service(self):
        self._is_started = False

    def register_action(self, action, group):
        '''
        Register and action or deed to a group. 

        Parameters:
        action - an instance of the Action class or it's children (deeds)
        group - a string specifying the group name the action should be in
        '''
        if group not in self._actions.keys():
            self._actions[group] = []
        if action not in self._actions[group]:
            self._actions[group].append(action)

    def get_actions(self, group):
        '''
        Returns all actions in the specified group
        
        group - string 
        '''

        return self._actions[group]

    def get_all_actions(self, exclude_groups = []):
        '''
        Returns all actions in a dictionary with group names as keys.
        '''
        actions = []
        for group in self._actions.keys():
            if group not in exclude_groups:
                for action in self._actions[group]:
                    actions.append(action)
        return actions

    

    def get_first_action(self, group):
        '''
        Returns the first action in the group

        group - string
        '''
        return self._actions[group][0]

    def get_last_action(self, group):
        '''
        Returns the last action in the group.

        group - string
        '''
        group = self._actions[group]
        return group[-1]