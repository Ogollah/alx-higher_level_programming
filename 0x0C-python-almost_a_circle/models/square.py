#!/usr/bin/python3
"""
Class squire.
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    The Square class represents a square
    and inherits from the Rectangle class.

    Attributes (inherited from Rectangle):
        __width (int): The width of the square.
        __height (int): The height of the square (same as width).
        __x (int): The x-coordinate of the square's position.
        __y (int): The y-coordinate of the square's position.

    Methods:
        __init__(self, size, x=0, y=0, id=None):
            The constructor for the Square class.

            Args:
                size (int): The size of the square (width and height).
                x (int, optional): The x-coordinate
                of the square's position (default is 0).
                y (int, optional): The y-coordinate
                of the square's position (default is 0).
                id (int, optional): An optional
                parameter representing the ID of the square.

        update(self, *args, **kwargs):
            Assigns the provided key/value
            arguments to the corresponding attributes.

        __str__(self):
            Returns the string representation
            of the Square instance.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor for the Square class.

        Args:
            size (int): The size of the square (width and height).
            x (int, optional): The x-coordinate
            of the square's position (default is 0).
            y (int, optional): The y-coordinate
            of the square's position (default is 0).
            id (int, optional): An optional
            parameter representing the ID of the square.

        Raises:
            ValueError: If size is less than or equal to 0.
            TypeError: If any of the arguments
            (size, x, y) is not an integer.
        """
        super().__init__(size, size, x, y, id)

    def update(self, *args, **kwargs):
        """
        Assigns the provided key/value arguments
        to the corresponding attributes.

        Args:
            *args: Variable-length argument list.
            (Unused in this version of the method)
            **kwargs: Keyworded argument list
            representing attribute key/value pairs.
        """
        super().update(*args, **kwargs)

    def __str__(self):
        """
        Returns the string representation
        of the Square instance.

        Returns:
            str: The formatted string
            representing the Square instance.
        """
        rect_x = self._Rectangle__x
        rect_y = self._Rectangle__y
        return f"[Square] ({self.id}) {rect_x}/{rect_y} - {self.width}"
