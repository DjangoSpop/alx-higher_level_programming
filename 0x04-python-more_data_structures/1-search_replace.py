#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # Create a new list to store the modified elements
    new_list = []

    # Iterate through the elements of the input list
    for item in my_list:
        # If the element is equal to the search element, replace it with the replacement element
        if item == search:
            new_list.append(replace)
        else:
            new_list.append(item)

    return new_list

# Example usage:
original_list = [1, 2, 3, 4, 2, 5, 2]
search_element = 2
replacement_element = 6

result = search_replace(original_list, search_element, replacement_element)
print(result)

