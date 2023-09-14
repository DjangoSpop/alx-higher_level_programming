#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    # Create a list to store keys to be deleted
    keys_to_delete = []

    # Iterate through the dictionary to find keys with the specified value
    for key, val in a_dictionary.items():
        if val == value:
            keys_to_delete.append(key)

    # Delete the keys with the specified value
    for key in keys_to_delete:
        del a_dictionary[key]

# Example usage:
my_dict = {"a": 1, "b": 2, "c": 3, "d": 2}

complex_delete(my_dict, 2)
print(my_dict)

