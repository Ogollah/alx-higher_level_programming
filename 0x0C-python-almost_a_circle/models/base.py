#!/usr/bin/python3

"""
The Base class.
"""


class Base:
    """
     is the foundation for all other
    classes in the project and provides a mechanism for managing the 'id'
    attribute of instances.
    """
    __nb_objects = 0  # Private class attribute

    def __init__(self, id=None):
        """
        Constructor for the Base class.

        Args:
            id (int, optional): An optional parameter
            representing the ID of the instance. If provided, the 'id'
            attribute of the instance will be set to this value.
            If not provided, a new ID will be generated and
            assigned to the instance by incrementing the
            '__nb_objects' class attribute.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
