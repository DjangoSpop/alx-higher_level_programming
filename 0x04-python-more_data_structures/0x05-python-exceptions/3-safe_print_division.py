#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {:.1f}".format(result))
        return result

# Example usage:
a = 10
b = 2
division_result = safe_print_division(a, b)
