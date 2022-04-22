#!/usr/bin/python3
""" Will print header variable X-Request-Id from response to request """

from sys import argv
from urllib.request import urlopen

if __name__ == "__main__":

    url = argv[1]
    with urlopen(url) as res:
        print(res.info()['X-Request-Id'])
