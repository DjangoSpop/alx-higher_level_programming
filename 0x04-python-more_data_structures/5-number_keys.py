#!/usr/bin/python3
def number_keys(a_dictionary):
    # Use the len() function to count the keys in the dictionary
    num_keys = len(a_dictionary)

    return num_keys

# Example usage:
my_dict = {"name": "John", "age": 30, "city": "New York"}

result = number_keys(my_dict)
print(result)

