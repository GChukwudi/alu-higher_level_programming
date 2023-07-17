#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for i in range(0, len(a_dictionary)):
        for key, value1 in a_dictionary.items():
            if value == value:
                del a_dictionary[key]
                break
    return a_dictionary
