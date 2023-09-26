#!/usr/bin/python
import sys

def safe_function(fct, *args):
    try:
        result = fct(*args)  # Execute the given function with provided arguments
        return result
    except Exception as e:
        # If an exception occurs, print the error message to stderr with "Exception:" prefix
        print("Exception:", e, file=sys.stderr)
        return None

# Example usage:
def divide(a, b):
    return a / b

result1 = safe_function(divide, 10, 2)
print("Result 1:", result1)  # Should print 5.0

result2 = safe_function(divide, 10, 0)
print("Result 2:", result2)  # Should print None and print an error message to stderr
