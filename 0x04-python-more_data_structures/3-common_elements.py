#!/usr/bin/python3
def common_elements(set_1, set_2):
    # Use the intersection method of sets to find common elements
    common_set = set_1.intersection(set_2)

    return common_set

# Example usage:
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

result = common_elements(set1, set2)
print(result)

