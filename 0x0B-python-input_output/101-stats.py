#!/usr/bin/python3
import signal
import sys

def print_stats(size, status_codes):
    """Print accumulated metrics"""
    print("File size: {}".format(size))
    for code in sorted(status_codes):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))

def signal_handler(sig, frame):
    """Handle Ctrl+C"""
    print_stats(size, status_codes)
    sys.exit(0)

# Register the Ctrl+C signal handler
signal.signal(signal.SIGINT, signal_handler)

size = 0
status_codes = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}
count = 0

try:
    for line in sys.stdin:
        if count == 10:
            print_stats(size, status_codes)
            count = 0
        else:
            count += 1

        parts = line.split()
        if len(parts) >= 9:
            try:
                size += int(parts[-1])
                status_code = parts[-2]
                if status_code in status_codes:
                    status_codes[status_code] += 1
            except (ValueError, KeyError):
                pass

    print_stats(size, status_codes)

except KeyboardInterrupt:
    print_stats(size, status_codes)
    sys.exit(0)
