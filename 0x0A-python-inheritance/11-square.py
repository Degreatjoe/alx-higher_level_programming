#!/usr/bin/python3
'''Defining a square'''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''class representation of a square'''
    def __init__(self, size):
        '''An instantiation with size
        Args:
            size (init): the size of the square
            '''
        self.__size = 0
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

        def area(self):
            """Compute the area of the rectangle."""
            return self.__width * self.__height

        def __str__(self):
            """Return the string representation of the square."""
            return "[Square] {}/{}".format(self.__size, self.__size)
