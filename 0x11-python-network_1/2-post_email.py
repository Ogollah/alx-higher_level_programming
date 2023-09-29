#!/usr/bin/python3
"""Script that takes in a URL and an email"""

import urllib.request
import sys


if __name__ == '__main__':
    with urllib.request.urlopen(sys.argv[1],
                                b'email=' + sys.argv[2].encode()) as req:
        print(req.read().decode('UTF-8'))
