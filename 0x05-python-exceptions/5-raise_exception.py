#!/usr/bin/python
def raise_exception():
    raise TypeError("This is a custom type exception")

# Example usage:
try:
    raise_exception()
except TypeError as e:
    print("Caught an exception:", e)
