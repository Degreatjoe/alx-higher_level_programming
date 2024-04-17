#!/usr/bin/python3
'''Rectangle class that inherits base geometry'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''Rectangle class that calculate rectangles'''
    def __init__(self, width, height):
        '''An instantiation of the Rectangle class
        Args:
            width (init): the width of the rectangle
            height (init): the height of the rectangle
            '''
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
