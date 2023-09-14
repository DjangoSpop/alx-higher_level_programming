#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    # Create a new dictionary to store the modified values
    new_dictionary = {}

    # Iterate through the key-value pairs in the input dictionary
    for key, value in a_dictionary.items():
        # Multiply the value by 2 and add it to the new dictionary
        new_dictionary[key] = value * 2

    return new_dictionary

# Example usage:
my_dict = {"a": 1, "b": 2, "c": 3}

result = multiply_by_2(my_dict)
print(result)

