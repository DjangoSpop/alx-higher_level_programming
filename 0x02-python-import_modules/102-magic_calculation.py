#!/usr/bin/python3
def magic_calculation(a, b):
    if a < b:
        add = __import__('magic_calculation_102').add
        sub = __import__('magic_calculation_102').sub
        return add(a, b)
    else:
        return sub(a, b)
