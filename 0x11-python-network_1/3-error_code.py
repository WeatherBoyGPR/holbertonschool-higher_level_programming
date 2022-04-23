#!/usr/bin/python3
""" will send request to specified url, shows body of response"""

from sys import argv
from urllib.error import HTTPError
from urllib.request import urlopen, Request
from urllib import parse

if __name__ == "__main__":
    url = argv[1]
    try:
        with urlopen(url) as res:
            print(res.read().decode('utf-8'))
    except HTTPError as e:
        print("Error code: {}".format(e.cpde))
