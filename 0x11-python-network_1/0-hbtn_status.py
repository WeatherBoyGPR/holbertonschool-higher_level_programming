#!/usr/bin/python3
""" Will fetch https://intranet.hbtn.io/status using urllib """

from urllib import parse
from urllib.request import urlopen

if __name__ == "__main__":

    url = 'https://intranet.hbtn.io/status'
    form = """Body response:
    - type: {}
    - content: {}
    - utf8 content: {}"""
    with urlopen(url) as res:
        data = res.read()
        typ = type(data)
        con = data
        utf = data.decode('utf')
        print(form.format(typ, con, utf))
