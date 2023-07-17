#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    temp_dic = {}
    for key, val in a_dictionary.items():
        temp_dic[key] = val * 2
    return temp_dic
