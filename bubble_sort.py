#! /usr/bin/env python3


from itertools import islice


def bubble_sort(lst=list()):
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

    #
    >>> bubble_sort([3, 2, -1, 1, 0])
    [-1, 0, 1, 2, 3]
    """

    # # Option #1.
    # if len(lst) > 0:
    #     for i in range(len(lst) - 1):
    #         for j in range(len(lst) - 1):
    #             if lst[j] > lst[j + 1]:
    #                 lst[j], lst[j + 1] = lst[j + 1], lst[j]
    #
    # # Option #2.
    # if len(lst) > 0:
    #     for x in range(len(lst) - 1):
    #         for index, item in enumerate(lst[:-1]):
    #             if item > lst[index + 1]:
    #                 lst[index], lst[index + 1] = lst[index + 1], lst[index]
    #
    # # Option #3.
    # if len(lst) > 0:
    #     for x in lst[:-1]:
    #         for index, item in enumerate(lst[:-1]):
    #             if item > lst[index + 1]:
    #                 lst[index], lst[index + 1] = lst[index + 1], lst[index]

    # # Option #4.
    # for x in lst[1:]:
    #     for index, item in enumerate(lst[:-1]):
    #         if item > lst[index+1]:
    #             lst[index], lst[index+1] = lst[index+1], lst[index]

    # # Option #5.
    # for j, y in enumerate(lst[1:], 1):
    #     for i, x in enumerate(lst[:-1]):
    #         if x > lst[j]:
    #             lst[i], lst[j] = lst[j], x

    # # Option #6.
    # if lst:
    #     for j, y in enumerate(islice(lst, len(lst)-1)):
    #         for i, x in enumerate(islice(lst, 1, len(lst)), 1):
    #             if x < lst[i-1]:
    #                 lst[i], lst[i-1] = lst[i-1], x

    # # Option #7:
    # if lst:
    #     for n in range(len(lst)-1):
    #         for i, x in enumerate(lst[-1:0:-1]):
    #             idx = len(lst)-1-i
    #             if x < lst[idx-1]:
    #                 lst[idx], lst[idx-1] = lst[idx-1], lst[idx]

    # Option #8:
    for n in range(len(lst)-1):
        for x in range(len(lst)-1):
            if lst[x] > lst[x+1]:
                lst[x], lst[x+1] = lst[x+1], lst[x]

    return lst


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    lst = [3, 2, -1, 1, 0]
    bubble_sort(lst)
    print(lst)
