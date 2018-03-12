#! /usr/bin/env python3

"""
Exercise #14: Implementation of edit distance via recursion.
"""

import sys

def compute_ed_recursively(x, y):
    """
    Compute edit distance from x to y recursively.

    :param x: string x
    :param y: string y
    :return: min. value for edit distance

    # Doctest(s):
    >>> compute_ed_recursively('', '')
    0
    >>> compute_ed_recursively('abc', '')
    3
    >>> compute_ed_recursively('', 'abc')
    3
    >>> compute_ed_recursively('donald','ronaldo')
    2
    """
    m = len(x)
    n = len(y)

    if m == 0:
        return n
    if n == 0:
        return m

    # Insert case.
    ed1 = compute_ed_recursively(x, y[:-1]) + 1

    # Delete case.
    ed2 = compute_ed_recursively(x[:-1], y) + 1

    # Replace case.
    ed3 = compute_ed_recursively(x[:-1], y[:-1])

    # If the last character do not match, add replace costs.
    if x[-1] != y[-1]:
        ed3 += 1

    return min(ed1, ed2, ed3)

def compute_ed_via_table(x, y):
    """ TODO
    Compute edit distance via dynamic programming table.

    :param x:
    :param y:
    :return:

    # Doctest(s):
    >>> compute_ed_via_table('', '')
    0
    >>> compute_ed_recursively('abc', '')
    3
    >>> compute_ed_via_table('', 'abc')
    3
    >>> compute_ed_via_table('donald', 'ronaldo')
    2
    """
    m = len(x)
    n = len(y)
    num_rows = m + 1
    num_columns = n + 1

    # Initialize M x N matrix as a list of lists.
    matrix = [[0] * num_columns for x in range(num_rows)]

    # Add costs for empty word alignments.
    for row in range(1, num_rows):
        matrix[row][0] = matrix[row-1][0] + 1
    for column in range(1, num_columns):
        matrix[0][column] = matrix[0][column-1] + 1

    # Compute matrix.
    for row in range(1, num_rows):
        for column in range(1, num_columns):
            if x[row-1] != y[column-1]:
                delete_costs = matrix[row-1][column] + 1
                insert_costs = matrix[row][column-1] + 1
                replace_costs = matrix[row-1][column-1] + 1
                matrix[row][column] = min(delete_costs,
                                          insert_costs,
                                          replace_costs)
            else:
                matrix[row][column] = matrix[row-1][column-1]
    # Last matrix entry = min(ED(x, y)).
    return matrix[num_rows-1][num_columns-1]


def main():
    """ 
    Main function.
    """
    # Read in two string from the command line.
    num_args = len(sys.argv)

    if not num_args == 3:
        raise Exception('Script excepts two input strings')

    x = sys.argv[1]
    y = sys.argv[2]

    print('x = ' + x)
    print('y = ' + y)

    ed = compute_ed_recursively(x, y)
    print('Edit distance (x->y): ' + str(ed))



if __name__ == '__main__':
    """ 
    Executes only if it is run as a script.
    """
    import doctest

    doctest.testmod()

    main()
