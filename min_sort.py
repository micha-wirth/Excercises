#! /usr/bin/env python3


def min_sort(lst):
    """ Implementation of min sort algorithm.

    >>> min_sort([24, 6, 12, 32, 0, 18, -1])
    [-1, 0, 6, 12, 18, 24, 32]

    # Empty list as parameter to function call.
    >>> min_sort([])
    []

    # Wrong type of parameter (no list) to function call.
    >>> min_sort('no list')
    Traceback (most recent call last):
        ...
    TypeError: my_list must be a list.

    # # Wrong type(s) of elements in given list.
    # >>> min_sort([0, -1, '1', 2, 3])
    # Traceback (most recent call last):
    #     ...
    # TypeError: wrong type of element in given list.

    # Elements of type int and float in given list.
    >>> min_sort([0.0, 0, -1.5, 1, -2])
    [-2, -1.5, 0, 0.0, 1]
    """

    # Check type of given parameter to function call.
    if not isinstance(lst, list):
        raise TypeError('my_list must be a list.')

    # # Option #1.
    # for i in range(0, len(my_list) - 1):
    #     min_index = i
    #     for j in range(i + 1, len(my_list)):
    #         if not (isinstance(my_list[i], (int, float))
    #                 and isinstance(my_list[j], (int, float))):
    #             raise TypeError('wrong type of element in given list.')
    #         if my_list[min_index] > my_list[j]:
    #             min_index = j
    #
    #     if i != min_index:
    #         my_list[i], my_list[min_index] = my_list[min_index], my_list[i]

    # Option #2:
    for i, x in enumerate(lst[:-1]):
        min_index = i
        min_value = lst[min_index]  # min_value = x
        for j, y in enumerate(lst[i + 1:], i + 1):
            if min_value > y:
                min_index = j
                min_value = y
        if min_index != i:
            lst[i], lst[min_index] = lst[min_index], lst[i]

    return lst


if __name__ == "__main__":
    import doctest

    doctest.testmod()
