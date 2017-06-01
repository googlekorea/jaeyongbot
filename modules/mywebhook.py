'''
slack webhook module
under development
'''

class Message:
    '''
    incoming webhook
    '''
    __incoming_message = {}
    def add_attr(self, key, value):
        '''
        add json attribute
        '''
        self.__incoming_message[key] = value
    def get_json(self):
        '''
        get json dictionary
        '''
        return self.__incoming_message
