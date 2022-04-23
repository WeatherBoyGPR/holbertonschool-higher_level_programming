#!/usr/bin/python3
""" fetches https://intranet.hbtn.io/status """

import requests

if __name__ == "__main__":
    url = 'https://intranet.hbtn.io/status'
    form = """Body response:
    \t- type: {}
    \t- content: {}"""

    r = requests.get(url)
    print(form.format(type(r.text), r.text))
