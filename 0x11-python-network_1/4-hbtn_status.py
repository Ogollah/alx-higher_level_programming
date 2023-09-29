#!/usr/bin/python3
"""script that fetches https://alx-intranet.hbtn.io/status"""

import requests

url = 'https://alx-intranet.hbtn.io/status'


if __name__ == '__main__':
    req = requests.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(req.text)))
    print("\t- content: {}".format(req.text))
