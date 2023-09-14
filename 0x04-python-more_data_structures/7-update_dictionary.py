#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    # Update the dictionary with the new key-value pair
    a_dictionary[key] = value

# Example usage:
my_dict = {"name": "John", "age": 30, "city": "New York"}

# Adding a new key-value pair
update_dictionary(my_dict, "country", "USA")

# Replacing the value of an existing key
update_dictionary(my_dict, "age", 31)

print(my_dict)

