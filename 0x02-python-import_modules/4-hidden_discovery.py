#!/usr/bin/python3
import dis
import types


def print_defined_names(module):
    names = []
    for const in module.co_consts:
        if isinstance(const, types.CodeType):
            names.extend(const.co_names)
    names = sorted(set(names))
    
    for name in names:
        if not name.startswith("__"):
            print(name)


module = __import__("hidden_4")


print_defined_names(module)
