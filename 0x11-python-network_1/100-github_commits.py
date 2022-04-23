#!/usr/bin/python3
""" Will list commits from repository owned by specified user """

from sys import argv
import requests

if __name__ == "__main__":
    url = "https://api.github.com/repos"
    repo = '/' + argv[2]
    owner = '/' + argv[1]

    url = url + owner + repo + '/commits'

    r = requests.get(url)
    try:
        res = r.json()
        for i in range(0, 10):
            sha = res[i].get('sha')
            author = res[i].get('commit').get('author').get('name')
            print("{}: {}".format(sha, author))
    except IndexError:
        pass
