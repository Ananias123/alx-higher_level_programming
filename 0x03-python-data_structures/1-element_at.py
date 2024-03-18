# A function that retrieve an element at particular index
#!/usr/bin/python3
def element_at(my_list, idx): # A function that retrieve tha element at agiven index in a list
    if idx < 0:
        return (None)
    if idx > len(my_list) - 1:
        return (None)
    return my_list[idx]
