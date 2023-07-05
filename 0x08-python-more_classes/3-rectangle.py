#!/usr/bin/python3

""" Rectangle class. """


class Rectangle:
    """Defining a rectangle class """

    def __init__(self, width=0, height=0):
        """ Initialize the width and the heigth of the rectangle. """

        self._width = 0
        self._height = 0
        self.width = width
        self.height = height

    def __str__(self):
        """String representation of the rectangle."""
        if self._height == 0 or self._width == 0:
            return ""
        str_rectangle = (self.__width * str(self.print_symbol) + "\n") * (self.__height - 1)
        str_rectangle += self.__width * str(self.print_symbol)
        return str_rectangle

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
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def area(self):
        """Area of a Rectangle"""

        return self._width * self._height

    def perimeter(self):
        """Perimeter"""

        if self._width == 0 or self._height == 0:
            return
        return 2 * (self._width + self._height)
