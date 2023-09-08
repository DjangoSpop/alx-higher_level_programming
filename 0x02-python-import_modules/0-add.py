#!/usr/bin/python3
if __name__ == "__main__":
# Define variables a and b
a = 1
b = 2

# Import the add function from add_0.py
from add_0 import add

# Calculate the result of add(a, b)
result = add(a, b)

# Print the result with string formatting
print(f"{a} + {b} = {result}")

