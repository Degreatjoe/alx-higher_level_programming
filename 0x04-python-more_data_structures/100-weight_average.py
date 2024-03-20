#!/usr/bin/python3
def weight_average(my_list=[]):
    # Check if the list is empty
    if not my_list:
        return 0

    # Calculate the weighted sum and total weight
    weighted_sum = 0
    total_weight = 0
    for score, weight in my_list:
        weighted_sum += score * weight
        total_weight += weight

    # Calculate the weighted average
    weighted_avg = weighted_sum / total_weight
    return weighted_avg
