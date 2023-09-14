#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    # Check if the key exists in the dictionary
    if key in a_dictionary:
        # Delete the key from the dictionary
        del a_dictionary[key]

# Example usage:
my_dict = {"name": "John", "age": 30, "city": "New York"}

# Delete a key that exists in the dictionary
simple_delete(my_dict, "age")

# Attempt to delete a key that doesn't exist in the dictionary
simple_delete(my_dict, "country")

print(my_dict)

