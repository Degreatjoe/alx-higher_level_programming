#!/usr/bin/python3
'''Defining my list class that inherits from list'''


class MyList(list):
    '''myList inherits from list '''

    def print_sorted(self):
        '''Prints the sorted list'''
        sorted_list = sorted(self)
        print(sorted_list)
