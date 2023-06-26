#!/usr/bin/python3

def safe_print_list(my_list=None, x=0):

    if my_list is None:
        my_list = []
    
    printed_elements = 0
    for index, element in enumerate(my_list):
        if index >= x:
            break
        print("{}".format(element), end="")
        printed_elements += 1
    return printed_elements
