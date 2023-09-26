#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []  # Initialize an empty list to store division results

    try:
        for i in range(list_length):
            try:
                # Try to convert elements to float and perform division
                num1 = float(my_list_1[i])
                num2 = float(my_list_2[i])

                if num2 == 0:
                    # Check for division by zero
                    result.append(0)
                    print("division by 0")
                else:
                    result.append(num1 / num2)
            except (ValueError, TypeError):
                # Handle invalid types
                result.append(0)
                print("wrong type")
            except IndexError:
                # Handle list length issues
                result.append(0)
                print("out of range")
    except ZeroDivisionError:
        # Handle unexpected division by zero errors
        pass
    finally:
        return result

# Example usage:
list1 = [1, 2, "3", 4]
list2 = [2, 0, 5, "6"]
length = 4

result_list = list_division(list1, list2, length)
print(result_list)
