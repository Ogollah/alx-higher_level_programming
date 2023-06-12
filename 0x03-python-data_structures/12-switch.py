#!/usr/bin/python3
a = 89
b = 10
a, b = (10, 89) if a == 89 else (89, 10)
print("a={:d} - b={:d}".format(a, b))
