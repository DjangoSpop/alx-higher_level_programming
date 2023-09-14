#!/usr/bin/python3
def best_score(a_dictionary):
    # Initialize variables to keep track of the best score and corresponding key
    best_key = None
    best_value = None

    # Iterate through the key-value pairs in the input dictionary
    for key, value in a_dictionary.items():
        # Check if the current value is greater than the best_value
        if best_value is None or value > best_value:
            best_key = key
            best_value = value

    return best_key

# Example usage:
student_scores = {"Alice": 90, "Bob": 85, "Charlie": 95, "David": 88}

best_student = best_score(student_scores)
print(best_student)

