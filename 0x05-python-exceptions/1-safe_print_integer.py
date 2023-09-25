#!/usr/bin/python
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False

# Example usage:
result1 = safe_print_integer(42)
print("Result 1:", result1)  # Should print True

result2 = safe_print_integer("Hello")
print("Result 2:", result2)  # Should print False
