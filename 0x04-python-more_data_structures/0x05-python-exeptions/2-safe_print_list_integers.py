def safe_print_list_integers(my_list=[], x=0):
    count = 0  # Initialize a count to keep track of printed integers
    
    try:
        for i in range(x):
            # Try to convert the element to an integer
            try:
                value = int(my_list[i])
            except (ValueError, TypeError):
                pass  # Skip non-integer values
            
            # Check if the value is an integer
            if isinstance(value, int):
                print("{:d}".format(value), end=' ')  # Print the integer
                count += 1  # Increment the count of printed integers
    
    except IndexError:
        pass  # Catch the IndexError if it occurs (list index out of range)

    print()  # Print a newline to separate the output
    return count  # Return the count of printed integers

# Example usage:
my_list = [1, "2", 3, "4", "hello", 5]
x = 4
printed_integers = safe_print_list_integers(my_list, x)
print("Number of integers printed:", printed_integers)
