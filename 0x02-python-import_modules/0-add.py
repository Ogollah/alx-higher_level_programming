#!/usr/bin/python3i
from add_0 import add

def main():

    a,b = 1, 2

    sum = add(a, b)

    print("{:d} + {:d} = {:d}".format(a, b, sum))

if __name__ == '__main__':
    main()
