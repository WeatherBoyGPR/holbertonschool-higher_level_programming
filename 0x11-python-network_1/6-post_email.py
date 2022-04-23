#!/usr/bin/python3
""" Will send post request to url """

from sys import argv
import requests

if __name__ == "__main__":
    url = argv[1]
    email = argv[2]

    r = requests.post(url, data={'email': email})
    print(r.text)
