#!/usr/bin/python3
import urllib, urllib.request
import sys
"""
we are her takeing to arguments and posting it to the website decodeing
the email from asci to utf 8 
 Python script that takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response (decoded in utf-8)
"""

url = sys.argv[1]
email = {'email': sys.argv[2]}



data = urllib.parse.urlencode(email)
data = data.encode('ascii')

with urllib.request.urlopen(url, data) as response:
    print(response.read().decode('utf-8'))
