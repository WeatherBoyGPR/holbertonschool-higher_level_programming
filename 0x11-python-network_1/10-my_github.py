#!/usr/bin/python3
""" displays github api """

from sys import argv
from requests.auth import HTTPBasicAuth
import requests

if __name__ == "__main__":
    url = "https://api.github.com/user"
    usr = argv[1]
    passwd = argv[2]

    r = requests.get(url, auth=HTTPBasicAuth(usr, passwd))
    print(r.json()['id'])
