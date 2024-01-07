#!/usr/bin/python3
import urllib.request
import sys

def fetch_x_request_id(url):
    """
    Fetches the value of the 'X-Request-Id' variable from the header of the response to a given URL.

    Args:
    - url (str): The URL to send the request to.

    Returns:
    - str: The value of the 'X-Request-Id' variable in the response headers, or a message if not found.
    """
    try:
        with urllib.request.urlopen(url) as response:
            x_request_id = response.headers.get('X-Request-Id')
            if x_request_id:
                return x_request_id
            else:
                return "X-Request-Id not found in the response headers."
    except urllib.error.URLError as e:
        return f"Error: {e.reason}"

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    result = fetch_x_request_id(url)
    print(result)
