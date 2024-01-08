#!/usr/bin/python
def safe_print_list(my_list=[], x=0):
    count = 0  # Initialize a count to keep track of printed elements
    
    try:
        for i in range(x):
            print(my_list[i], end='')  # Print the element without a newline
            count += 1  # Increment the count of printed elements
    except IndexError:
        pass  # Catch the IndexError if it occurs (list index out of range)

    print()  # Print a newline to separate the output
    return count  # Return the count of printed elements

# Example usage:
my_list = [1, 2, 3, 4, 5]
x = 3
printed_elements = safe_print_list(my_list, x)
print("Number of elements printed:", printed_elements)
