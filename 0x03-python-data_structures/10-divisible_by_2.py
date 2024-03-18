#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    Leng = len(my_list)
    list_new = []
    for a in range(Leng):
        if my_list[a] % 2 == 0:
            list_new.append(True)
        else:
            list_new.append(False)
    return list_new
