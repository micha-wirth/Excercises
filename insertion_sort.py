#! /usr/bin/env python3

def insertion_sort(my_list=list()):
    ''' Implementation of insertion sort algorithm.

    # Empty list.
    >>> insertion_sort([])
    []

    # Missing list (no parameter).
    >>> insertion_sort()
    []

    # List with only 1 element.
    >>> insertion_sort([0])
    [0]

    # List with even number of elements.
    >>> insertion_sort([2, -1, 3, 0])
    [-1, 0, 2, 3]

    # List with an uneven number of elements.
    >>> insertion_sort([2, 1, 0])
    [0, 1, 2]

    # No list (parameter has wrong type).
    >>> insertion_sort('no list')
    Traceback (most recent call last):
        ...
    TypeError: my_list must be a list.

    # At least one element is not a numeric type.
    # >>> insertion_sort([0, -1, 2, 'a'])
    # Traceback (most recent call last):
    #     ...
    # TypeError: wrong type of element in list.
    '''

    # Check given parameter data type.
    if not isinstance(my_list, (list)):
        raise TypeError('my_list must be a list.')

    # Option #1
    # for i in range(len(my_list)-1):
    #     for j in range(i+1, 0, -1):
    #         if (isinstance(my_list[j-1], (int, float))
    #                 and isinstance(my_list[j], (int, float))):
    #             if my_list[j-1] > my_list[j]:
    #                 my_list[j], my_list[j-1] = my_list[j-1], my_list[j]
    #         else:
    #             raise TypeError('wrong type of element in list.')

    # Option #2.
    # for index, item in enumerate(my_list):
    #     while index > 0 and item < my_list[index - 1]:
    #         my_list[index] = my_list[index - 1]
    #         index -= 1
    #     my_list[index] = item

    # Option #3.
    # for index, item in enumerate(my_list[1:]):
    #     for x in range(index + 1, -1, -1):
    #         if item < my_list[x -1]:
    #             my_list[x] = my_list[x -1 ]
    #         else:
    #             break
    #     my_list[x] = item

    # Option #3:
    for index1, item1 in enumerate(my_list[:-1]):
        for index2, item2 in enumerate(my_list[1:index1]):
            if item1 < item2:
                my_list[index2 + 1] = item2
            else:
                break
        my_list[index2] = item1
    return my_list




if __name__ == "__main__":
    import doctest

    doctest.testmod()


if __name__ == "__main__":
    import doctest

    doctest.testmod()
