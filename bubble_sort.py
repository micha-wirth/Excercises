#! /usr/bin/env python3


def bubble_sort(my_list=list()):
    """ Implementation of bubble sort algorithm.

    # No parameter (no list) to function call.
    >>> bubble_sort()
    []

    # Empty list to function call.
    >>> bubble_sort([])
    []

    # List with single item to function call.
    >>> bubble_sort([1])
    [1]

    # List with even number of items to function call.
    >>> bubble_sort([2, -1, 1, 0])
    [-1, 0, 1, 2]

    # List with uneven number of items to function call.
    >>> bubble_sort([2, 1, 0])
    [0, 1, 2]
    """

    # Option #1.
    # if len(my_list) > 0:
    #     for i in range(len(my_list) - 1):
    #         for j in range(len(my_list) - 1):
    #             if my_list[j] > my_list[j + 1]:
    #                 my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]

    # Option #2.
    # if len(my_list) > 0:
    #     for x in range(len(my_list) - 1):
    #         for index, item in enumerate(my_list[:-1]):
    #             if item > my_list[index + 1]:
    #                 my_list[index], my_list[index + 1] = my_list[index + 1], my_list[index]

    # Option #3.
    # if len(my_list) > 0:
    #     for x in my_list[:-1]:
    #         for index, item in enumerate(my_list[:-1]):
    #             if item > my_list[index + 1]:
    #                 my_list[index], my_list[index + 1] = my_list[index + 1], my_list[index]

    # Option #4.
    # for x in my_list[1:]:
    #     for index, item in enumerate(my_list[:-1]):
    #         if item > my_list[index + 1]:
    #             my_list[index], my_list[index + 1] = my_list[index + 1], my_list[index]

    # Option #5.
    for j, y in enumerate(my_list[1:], 1):
        for i, x in enumerate(my_list[:-1]):
            if x > y:
                my_list[i], my_list[j] = my_list[j], my_list[i]
    return  my_list


if __name__ == "__main__":
    import doctest

    doctest.testmod()