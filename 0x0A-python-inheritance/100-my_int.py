#!/usr/bin/python3
'''Define myint'''


class MyInt(int):
    '''my int class
    Args:
        int: Base class
        '''
    def __eq__(self, other):
        '''eq definition
        Args:
            other: the other
            '''
        return super().__ne__(other)

    def __ne__(self, other):
        '''ne definition
        Args:
            other: the other
            '''
        return super().__eq__(other)
