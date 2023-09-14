#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    # Use the symmetric_difference method of sets to find elements present in only one set
    diff_set = set_1.symmetric_difference(set_2)

    return diff_set

# Example usage:
set1 = {"Python", "C", "Javascript"}
set2 = {"Bash", "C", "Ruby", "Perl"}

result = only_diff_elements(set1, set2)
print(sorted(list(result)))

