#! /usr/bin/env python3


"""
Exercise #14: output optimal alignments.
"""

import sys

def compute_dp_table(x, y):
    """
    Compute dynamic programming table.

    :param x: input string x
    :param y: output string y
    :return: table containing edit distances

    # Doctest(s):
    >>> compute_dp_table('ja', 'ja')
    [[0, 1, 2], [1, 0, 1], [2, 1, 0]]
    >>> compute_dp_table('ja', 'ne')
    [[0, 1, 2], [1, 1, 2], [2, 2, 2]]
    >>> compute_dp_table('', '')
    [[0]]
    >>> compute_dp_table('e', '')
    [[0], [1]]
    >>> compute_dp_table('', 'e')
    [[0, 1]]
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
                insert_costs = matrix[row][column-1] + 1
                delete_costs = matrix[row-1][column] + 1
                replace_costs = matrix[row-1][column-1] + 1
                matrix[row][column] = min(delete_costs,
                                          insert_costs,
                                          replace_costs)
            else:
                matrix[row][column] = matrix[row-1][column-1]

    # Last matrix entry = min(ED(x, y)).
    return matrix

def extract_optimal_paths(x, y):
    """
    Extract optimal paths from edit distance table.

    :param x: input string x
    :param y: output string y
    :return: all optimal paths

    # Doctest(s):
    >>> paths = extract_optimal_paths('ma', 'maa')
    >>> paths[0]
    [(2, 3, '-'), (2, 2, 'i'), (1, 1, 'm'), (0, 0, 'm')]
    >>> paths[1]
    [(2, 3, '-'), (1, 2, 'm'), (1, 1, 'i'), (0, 0, 'm')]
    >>> extract_optimal_paths('', '')
    []
    >>> extract_optimal_paths('', 'e')
    [[(0, 1, '-'), (0, 0, 'i')]]
    >>> extract_optimal_paths('e', '')
    [[(1, 0, '-'), (0, 0, 'd')]]
    """
    table = compute_dp_table(x, y)
    num_rows = len(table)
    num_cols = len(table[0])

    ed = table[num_rows-1][num_cols-1]

    paths = list()

    if (x, y) == ('', ''):
        return []



    row = num_rows - 1
    col = num_cols -1
    min_ed = table[row][col]
    max_s = 0


    for row in range(num_rows-1, 0, -1):
        for col in range(num_cols-1, 0, -1):
            ed = table[row][col]
            if ed - table[row][col-1] >= 0:
                paths.append()


    ed = table[row][col]
    if ed - table[row][col-1] >= 0:
        paths.append([])
    if ed - table[row-1][col] >= 0:
        paths.append([])
    if ed - table[row-1][col-1] >= 0:
        paths.append([])

    if len(paths) >= 1:
        paths[0].append((num_rows-1, num_cols-1, '-'))
        while row > 0 or col > 0:
            ed = table[row][col]
            if ed - table[row][col-1] >= 0 and col-1 >= 0 and max_s <= min_ed:
                # Insert operation.
                max_s += 1
                row, col = row, col-1
                paths[0].append((row, col, 'i'))
                continue
            if ed - table[row-1][col] >= 0 and row-1 >= 0 and max_s <= min_ed:
                # Delete operation.
                max_s += 1
                row, col = row-1, col
                paths[0].append((row, col, 'd'))
                continue
            if ed - table[row-1][col-1] >= 0 and row-1 >= 0 and col-1 >= 0:
                # Replace operation.
                row, col = row-1, col-1
                paths[0].append((row, col, 'm'))
                continue

    if len(paths) >= 2:
        row = num_rows - 1
        col = num_cols -1
        paths[1].append((num_rows-1, num_cols-1, '-'))
        while row > 0 or col > 0:
            ed = table[row][col]
            if ed - table[row-1][col] >= 0 and row-1 >= 0 and max_s <= min_ed:
                # Delete operation.
                max_s += 1
                row, col = row-1, col
                paths[1].append((row, col, 'd'))
                continue
            if ed - table[row-1][col-1] >= 0 and row-1 >= 0 and col-1 >= 0:
                # Replace operation.
                row, col = row-1, col-1
                paths[1].append((row, col, 'm'))
                continue
            if ed - table[row][col-1] >= 0 and col-1 >= 0 and max_s <= min_ed:
                # Insert operation.
                max_s += 1
                row, col = row, col-1
                paths[1].append((row, col, 'i'))
                continue


    if len(paths) >= 3:
        row = num_rows - 1
        col = num_cols -1
        paths[1].append((num_rows-1, num_cols-1, '-'))
        while row > 0 or col > 0:
            ed = table[row][col]
            if ed - table[row-1][col-1] >= 0 and row-1 >= 0 and col-1 >= 0:
                # Replace operation.
                row, col = row-1, col-1
                paths[2].append((row, col, 'm'))
                continue
            if ed - table[row-1][col] >= 0 and row-1 >= 0:
                # Delete operation.
                row, col = row-1, col
                paths[2].append((row, col, 'd'))
                continue
            if ed - table[row][col-1] >= 0 and col-1 >= 0:
                # Insert operation.
                row, col = row, col-1
                paths[2].append((row, col, 'i'))
                continue


    return paths









def main():
    """ 
    Main function.
    """
    pass


if __name__ == '__main__':
    """ 
    Executes only if it is run as a script.
    """
    import doctest

    doctest.testmod()

    main()
