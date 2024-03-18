#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    Leng = len(my_list)
    List_1 = []
    for a in range(Leng):
        if my_list[a] % 2 == 0:
            List_1.append(True)
        else:
            List_1.append(False)
    return List_1

