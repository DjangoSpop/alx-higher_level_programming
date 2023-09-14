#!/usr/bin/python3
def uniq_add(my_list=[]):
    # Create a set to store unique integers
    unique_integers = set()

    # Iterate through the elements of the input list
    for item in my_list:
        if isinstance(item, int):
            unique_integers.add(item)

    # Calculate the sum of unique integers
    result = sum(unique_integers)

    return result

# Example usage:
my_list = [1, 2, 2, 3, 4, 4, 5, 5, 6]
result = uniq_add(my_list)
print(result)

