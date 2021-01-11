#!/usr/bin/python3
""" sends a POST request to the passed URL with the email as a parameter, and
displays the body of the response (decoded in utf-8)"""

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = {"email": sys.argv[2]}

    data = urllib.parse.urlencode(email)
    data = data.encode('utf8')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
