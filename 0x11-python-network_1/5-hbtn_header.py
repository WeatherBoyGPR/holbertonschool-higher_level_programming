#!/usr/bin/python3
""" Will take in URL, sends request and displays value """

from sys import argv
import requests

if __name__ == "__main__":
    url = argv[1]

    r = requests.get(url)
    print(r.headers['X-Request-Id'])
