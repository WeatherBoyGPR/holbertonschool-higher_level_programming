#!/usr/bin/python3
""" Will take in letter as input and send post request """

from sys import argv
import requests

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    val = ""
    if len(argv) >= 2:
        val = argv[1]
    r = requests.post(url, data={'q': val})

    try:
        res = r.json()
    except Error:
        print("Not a valid JSON")
    else:
        if len(res) == 0:
            print("No result")
        else:
            print("[{}] {}".format(res['id'], res['name']))
