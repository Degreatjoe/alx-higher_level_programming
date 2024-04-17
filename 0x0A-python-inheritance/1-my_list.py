class MyList(list):
    '''MyList inherits from list '''
    ERR_MSG = "'<' not supported between instances of 'str' and 'int'"

    def __init__(self, *args):
        '''Initializes the list and checks if all elements are integers'''
        super().__init__(*args)
        if not all(isinstance(x, int) for x in self):
            raise TypeError(MyList.ERR_MSG)

    def print_sorted(self):
        '''Prints the sorted list'''
        sorted_list = sorted(self)
        print(sorted_list)
