#!/usr/bin/python
def raise_exception_msg(message=""):
    raise NameError(message)

# Example usage:
try:
    raise_exception_msg("This is a custom name exception")
except NameError as e:
    print("Caught an exception:", e)
