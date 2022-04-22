#!/usr/bin/python3
""" Will send post request containing email to specified url """

from sys import argv
from urllib.request import urlopen, Request
from urllib import parse

if __name__ == "__main__":
    data = {'email': argv[2]}
    url = argv[1]

    data = parse.urlencode(data)
    data = data.encode('ascii')
    req = Request(url, data)
    with urlopen(req) as res:
        print(res.read().decode('utf=8'))
