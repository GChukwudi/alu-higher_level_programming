#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    total_weight = 0
    weighed_sum = 0
    for score, weight in my_list:
        total_weight += weight
        weighed_sum += score * weight
    return (weighed_sum / total_weight)
