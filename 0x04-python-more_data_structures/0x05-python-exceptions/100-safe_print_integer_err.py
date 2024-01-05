#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    try:
        integer_value = int(value)
        print("{:d}".format(integer_value))
        return True
    except ValueError:
        # If the conversion to int fails, print the error message to stderr
        print("Exception: Cannot print as integer", file=sys.stderr)
        return False

# Example usage:
result1 = safe_print_integer_err(42)
print("Result 1:", result1)  # Should print True

result2 = safe_print_integer_err("Hello")
print("Result 2:", result2)  # Should print False and print an error message to stderr
