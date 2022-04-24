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

    i = 0
    for res in r.json():
        sha = res.get('sha')
        author = res.get('commit').get('author').get('name')
        print("{}: {}".format(sha, author))
        if i == 9:
            break
        i += 1
