#!/usr/bin/python3
import urlib.request, urlib.parse
import sys


url = sys.argv[1]
email = {'email': sys.argv[2]}



data = urlib.parse.urlencode(email)
data = data.encode('ascii')

with urllib.request.urlopen(url, data) as response:
    print(response.read().decode('utf-8))
