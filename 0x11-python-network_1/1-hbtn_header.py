#!/usr/bin/python3
#1. Response header value #0
import urllib.request
import sys

with urllib.request.urlopen(sys.argv[1]) as response:
    print(response.headers.get('X-Request-Id'))
