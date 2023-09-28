#!/usr/bin/python3

def find_peak(list_of_integers):
    """
    Find a peak in an unsorted list of integers using a binary search approach.

    Args:
        list_of_integers (list): The list of unsorted
        integers in which to find a peak.

    Returns:
        int: The value of one of the peaks in the list.
    """
    low = 0
    high = len(list_of_integers) - 1

    while low < high:
        mid = (low + high) // 2

        if list_of_integers[mid] < list_of_integers[mid + 1]:
            low = mid + 1
        else:
            high = mid

    return list_of_integers[low]
