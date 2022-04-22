#!/usr/bin/python3
""" Will fetch https://intranet.hbtn.io/status using urllib """

from urllib import parse
from urllib.request import urlopen

if __name__ == "__main__":

    url = 'https://intranet.hbtn.io/status'
    with urlopen(url) as res:
        data = res.read()
        print("Body response:")
        print("\t- type: {}".format(type(data)))
        print("\t- content: {}".format(data))
        print("\t- uf8 content:{}".format(data.decode('utf')))
