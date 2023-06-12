#!/usr/bin/python3
a = 89
b = 10
a = b
b = 89 if a == 10 else b
print("a={:d} - b={:d}".format(a, b))
