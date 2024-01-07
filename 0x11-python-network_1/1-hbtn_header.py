import urllib.request
import sys

url = sys.argv[1]

try:
    with urllib.request.urlopen(url) as response:
        x_request_id = response.headers.get('X-Request-Id')
        if x_request_id:
            print(x_request_id)
        else:
            print("X-Request-Id not found in the response headers.")
except urllib.error.URLError as e:
    print(f"Error: {e.reason}")
