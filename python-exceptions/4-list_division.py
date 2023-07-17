#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new = []

    try:
        for i in range(list_length):
            try:
                value_1 = my_list_1[i]
                value_2 = my_list_2[i]
                result = value_1 / value_2
            except IndexError:
                print("out of range")
                result = 0
            except ZeroDivisionError:
                print("division by 0")
                result = 0
            except (TypeError, ValueError):
                print("wrong type")
                result = 0
            finally:
                new.append(result)
    finally:
        return new
