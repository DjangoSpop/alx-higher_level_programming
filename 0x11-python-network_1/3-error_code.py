#!/usr/bin/python3
import urrlib.request, urlib.error
import sys




try:
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.read().decode('utf-8'))
except urllib.error.HTTPError as e:
    print('Error code:', e.code)
