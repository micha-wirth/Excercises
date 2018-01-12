#! /usr/bin/env python3


def heap_sort(array):
    """ Implementation of the heap sort algorithm.

    # List with an even number ob items to function call.
    >>> heap_sort([0, -1, 5, -2])
    [-2, -1, 0, 5]

    # List with an uneven number of items to function call.
    >>> heap_sort([3, 2, 0, 4, 1])
    [0, 1, 2, 3, 4]

    # List with only one element to function call.
    >>> heap_sort([0])
    [0]

    # Empty list to function call.
    >>> heap_sort([])
    []

    :param arr:
    :return:
    """
    root_parent_index = 0
    # initial heapify operation.
    heapify(array)
    #
    for child_index in range(len(array) - 1, root_parent_index, -1):
        # Swap the last item with the first item.
        array[root_parent_index], array[child_index] = array[child_index], array[root_parent_index]
        # Repair heap from bottom up.
        repair_heap(array, root_parent_index, child_index - 1)

    return array


def heapify(array):
    """

    :param array:
    :return:
    """

    last_child_index = len(array) - 1
    last_parent_index = (last_child_index - 1) // 2

    for parent_index in range(last_parent_index, -1, -1):
        repair_heap(array, parent_index, last_child_index)

    return array


def repair_heap(array, parent_index, last_child_index):
    """ Repair the heap.

    :param array:
    :param parent_index:
    :param last_child_index:
    :return:

    >>> invalid_heap = [3, 2, 0, 4, 1]
    >>> repair_heap(invalid_heap, 1, 4)
    [3, 4, 0, 2, 1]
    >>> repair_heap(invalid_heap, 0, 4)
    [4, 3, 0, 2, 1]

    """
    current_parent_index = parent_index
    heap_size = last_child_index + 1

    while current_parent_index < heap_size:
        left_child_index = 2 * current_parent_index + 1
        right_child_index = left_child_index + 1
        max_child_index = left_child_index
        if left_child_index > last_child_index:
            break
        if right_child_index < heap_size and array[right_child_index] > array[left_child_index]:
            max_child_index = right_child_index
        if array[max_child_index] > array[current_parent_index]:
            array[max_child_index], array[current_parent_index] = array[current_parent_index], array[max_child_index]
            current_parent_index = max_child_index
        else:
            break

    return array




if __name__ == "__main__":
    import doctest

    doctest.testmod()
