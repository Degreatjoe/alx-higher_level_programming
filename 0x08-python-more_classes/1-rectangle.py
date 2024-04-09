#!/usr/bin/python3
'''defines a rectangle'''


class Rectangle:
    '''Represent a new Rectangle'''
    def __init__(self, width=0, height=0):
        '''Initializing a new instance
        Args:
            width (init): the width of the rectaangle
            height (init): The height of the Rectangle
            '''
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be interger")
        if value < 0:
            raise ValueError("value must be >= 0")
        self.__height = value
