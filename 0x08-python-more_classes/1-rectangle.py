#!/usr/bin/python3

""" Class defining a Rectangle. """


class Rectangle:
    """Defining a rectangle class """

    def __init__(self, width=0, height=0):
        """ Initialize the width and the heigth of the rectangle. """
        self._width = 0
        self._height = 0
        self._height = height
        self._width = width

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def heigh(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._height = value
