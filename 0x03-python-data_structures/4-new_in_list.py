#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    var_temp = my_list[:]
    if idx < 0:
        return var_temp
    if idx > len(my_list) - 1:
        return var_temp
    var_temp[idx] = element
    return var_temp
