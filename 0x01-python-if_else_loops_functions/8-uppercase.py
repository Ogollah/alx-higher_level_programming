#!/usr/bin/python3
def uppercase(str):
    for char in str:
        num = 32 if ord(char) > 96 and ord(char) < 123 else 0
        print("{:c}".format(ord(char) - num), end='')
    print()
