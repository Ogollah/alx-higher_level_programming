#!/usr/bin/python3

"""
Print statistics
"""


import sys


def print_statistics(total_size, status_count):

    """
    Print the statistics including the total file size and
    the number of lines by status code.

    Args:
        total_size (int): The total file size.
        status_count (dict): A dictionary containing
        the count of lines for each status code.

    Returns:
        None

    """
    print("File size: {}".format(total_size))
    sorted_statuses = sorted(status_count.keys())
    for status in sorted_statuses:
        count = status_count[status]
        print("{}: {}".format(status, count))


def compute_metrics():

    """
    Read stdin line by line, compute metrics, and print statistics.

    Returns:
        None

    """
    count = 0
    total_size = 0
    status_count = {}

    try:
        for line in sys.stdin:
            count += 1
            parts = line.split()
            if len(parts) >= 7:
                status = parts[-2]
                size = parts[-1]
                total_size += int(size)
                if status in status_count:
                    status_count[status] += 1
                else:
                    status_count[status] = 1

            if count % 10 == 0:
                print_statistics(total_size, status_count)

    except KeyboardInterrupt:
        print_statistics(total_size, status_count)
        raise


compute_metrics()
