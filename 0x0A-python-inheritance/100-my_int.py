#!/usr/bin/python3
"""
MyInt class.
"""


class MyInt(int):
    """
    A rebel MyInt class that inverts the == and != operators.
    """

    def __eq__(self, other):
        """
        Inverted equality operator.

        Args:
            other (any): The object to compare with.

        Returns:
            bool: True if the values are not equal, False otherwise.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Inverted inequality operator.

        Args:
            other (any): The object to compare with.

        Returns:
            bool: True if the values are equal, False otherwise.
        """
        return super().__eq__(other)
