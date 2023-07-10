#!/usr/bin/python3
"""
Add attribute.
"""


def add_attribute(obj, attribute, value):
    """
    Adds a new attribute to an object if it's possible.

    Args:
        obj (object): The object to which the attribute should be added.
        attribute (str): The name of the attribute to be added.
        value (any): The value to be assigned to the attribute.

    Raises:
        TypeError: If the object can't have a new attribute.

    Returns:
        None
    """
    if not hasattr(obj, '__dict__') and not hasattr(obj, '__slots__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)
