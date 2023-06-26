#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):

    printed_integers = 0
    for i in range(x):
        try:
            value = my_list[i]
            if isinstance(value, int):
                print("{:d}".format(value), end=" ")
        except IndexError:
            break
        except TypeError:
            pass
        else:
            printed_integers += 1

    print()
    return printed_integers
