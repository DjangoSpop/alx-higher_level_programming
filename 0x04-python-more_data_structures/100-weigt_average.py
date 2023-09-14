#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    total_score = 0
    total_weight = 0

    for score, weight in my_list:
        total_score += score * weight
        total_weight += weight

    return total_score / total_weight

# Example usage:
scores_and_weights = [(80, 3), (90, 2), (75, 4)]
result = weight_average(scores_and_weights)
print(result)

