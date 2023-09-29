#!/usr/bin/python3
"""
Script that takes in a letter and sends a
POST request to http://0.0.0.0:5000/search_user
"""

import requests
import sys
url = "http://0.0.0.0:5000/search_user"


if __name__ == '__main__':
    if len(sys.argv) < 2:
        search = {'q': '""'}
    else:
        search = {'q': sys.argv[1]}
    request = requests.post(url, search)
    try:
        search = request.json()
    except ValueError:
        print("Not a valid JSON")
    else:
        if hasattr(search, '__contains__') and len(search) < 1:
            print('No result')
        else:
            print('[{}] {}'.format(search['id'], search['name']))
