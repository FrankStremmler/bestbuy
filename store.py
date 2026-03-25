'''
Description for the File
'''

class Store():
    '''
    Represents a store with a name and inventory management.
    '''
    name: str

    def __init__(self, name: str):
        self.name = name

    def get_name(self) -> str:
        '''Return the store name.'''
        return self.name

    def set_name(self, name: str) -> None:
        '''Set the store name.'''
        self.name = name



if __name__ == '__main':
    pass
