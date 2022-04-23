#!/usr/bin/python3
""" Will list commits from repository owned by specified user """

from sys import argv
from requests.auth import HTTPBasicAuth
import requests

if __name__ == "__main__":
    url = "https://api.github.com/repos"
    repo = '/' + argv[2]
    owner = '/' + argv[1]
    url = url + owner + repo + '/commits'

    headers = {'page': '1'}

    r = requests.get(url, headers=headers)
    try:
        res = r.json()
        for i in range(0, 10):
            sha = res[i].get('sha')
            author = res[i].get('commit').get('author').get('name')
            print("{}: {}".format(sha, author))
    except IndexError:
        pass
