#!/usr/bin/python3
""" Locked class """


class LockedClass:
    """ Prevets user not to instantiatte a new Locked Class"""

    __slots__ = ["first_name"]

    def __setattr__(self, attr, value):
        if attr != "first_name":
            raise AttributeError("Cannot only set attribute 'first_name'")
        super().__setattr__(attr, value)
