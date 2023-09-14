#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    # Get the keys and sort them alphabetically
    sorted_keys = sorted(a_dictionary.keys())

    # Iterate through the sorted keys and print the key-value pairs
    for key in sorted_keys:
        value = a_dictionary[key]
        print(f"{key}: {value}")

# Example usage:
my_dict = {"name": "John", "age": 30, "city": "New York", "country": "USA"}

print_sorted_dictionary(my_dict)

