#! /usr/bin/env python3

"""
Exercise #10: Binary Search Tree.
"""

import random
import timeit


class BinarySearchTree:
    """
    Implementation of a binary search tree.
    """
    class Node:
        """
        A node containing a key-value pair.
        The node might have two children as well as a parent.
        """
        def __init__(self, key, value, parent_node):
            """
            Creates a new node with three parameters.
            Both children are initialized with None.
            """
            self._key = key
            self._value = value
            self._parent_node = parent_node
            self._left_child = None
            self._right_child = None

    def __init__(self):
        """
        Creates an empty binary search tree.

        # New instance must be empty.
        >>> tree = BinarySearchTree()
        >>> tree.depth() == 0 and tree.size() == 0
        True

        """
        self._root_node = None
        self._depth = 0
        self._item_count = 0

    def insert(self, key, value):
        """
        Inserts a new node into an existing search tree.

        :param key:
        :param value:
        :return:

        >>> tree = BinarySearchTree()
        >>> tree.insert(10, 'ten')
        >>> tree.depth() == 1 and tree.size() == 1
        True
        >>> tree.insert(15, 'fifteen')
        >>> tree.depth() == 2 and tree.size() == 2
        True
        >>> tree.insert(5, 'five')
        >>> tree.depth() == 2 and tree.size() == 3
        True
        """
        if self._root_node:
            # Tree is not empty.
            depth = 1
            current_node = self._root_node
            while True:
                # Represents actual search level.
                depth += 1

                if key == current_node._key:
                    # Replace of an existing entry.
                    # current._key = key
                    current_node._value = value
                    # self._depth = self._depth
                    # self._count = self._count
                    return
                elif key < current_node._key:
                    # Search on the left side.
                    if current_node._left_child:
                        # Search on next level.
                        current_node = current_node._left_child
                        continue
                    else:
                        # Insert new left node.
                        current_node._left_child = self.Node(key, value,
                                                             current_node)
                        self._depth = max(self._depth, depth)
                        self._item_count += 1
                        return
                else:
                    # Search on the right side.
                    if current_node._right_child:
                        # Search on next level.
                        current_node = current_node._right_child
                        continue
                    else:
                        # Insert new right node.
                        current_node._right_child = self.Node(key, value,
                                                              current_node)
                        self._depth = max(self._depth, depth)
                        self._item_count += 1
                        return
        else:
            # Tree is empty.
            self._root_node = self.Node(key, value, None)
            self._depth = 1
            self._item_count += 1
            return

    def lookup(self, key):
        """
        Search for a given key in the tree. Due to its search result the
        corresponding item as key-value pair or None will be returned.

        :param key: search for a given key
        :return: item (key-value pair) or None

        >>> tree = BinarySearchTree()
        >>> tree.lookup(5) is None
        True
        >>> tree.insert(10, 'ten')
        >>> tree.lookup(5) is None
        True
        >>> tree.lookup(10) == (10, 'ten')
        True
        >>> tree.insert(5, 'five')
        >>> tree.lookup(5) == (5, 'five')
        True

        """
        if self._root_node:
            # Tree is not empty.
            current_node = self._root_node
            while True:
                if key == current_node._key:
                    # Key is found.
                    return key, current_node._value
                elif key < current_node._key:
                    # Key might be on the left side.
                    if current_node._left_child:
                        # Look on the next level.
                        current_node = current_node._left_child
                        continue
                    else:
                        # Key is not in tree.
                        return None
                else:
                    # Key might be on the right side.
                    if current_node._right_child:
                        # Look on the next level in next iteration.
                        current_node = current_node._right_child
                        continue
                    else:
                        # Key is not in tree.
                        return None
        else:
            # Tree is empty.
            return None

    def depth(self):
        """
        Returns the tree depth.
        :return: max. depth
        """
        return self._depth

    def size(self):
        """
        Return the tree size.
        :return: count of items
        """
        return self._item_count

    def is_empty(self):
        """
        Check if tree is empty.
        :return: boolean value
        """
        return self._item_count == 0

    def to_string(self):
        """
        Generate a string representation of the binary tree.
        :return: binary tree represented as string
        """


def main():
    """ Main function.
    """

    def insert(tree, keys):
        for key in keys:
            tree.insert(key, None)

    def ordered_keys(size):
        return [key for key in range(size)]

    def random_keys(size):
        return random.sample(range(size), size)

    def ordered_insert(size, result):
        tree = BinarySearchTree()
        keys = ordered_keys(size)
        result[2] = timeit.timeit(stmt=lambda: insert(tree, keys), number=1)
        result[1] = tree.depth()
        result[0] = size

    def random_insert(size, result):
        tree = BinarySearchTree()
        keys = random_keys(size)
        result[2] = timeit.timeit(stmt=lambda: insert(tree, keys), number=1)
        result[1] = tree.depth()
        result[0] = size

    start_size = 2**10
    end_size = 2**20
    step_size = 2**10

    print("{0:<15}\t{1:<15}\t{2:<15}\t{3:<15}\t{4:<15}\t{5:<15}".format(
        "ordered size:", "ordered depth:", "ordered time",
        "random size:", "random depth:", "random time"))

    for size in range(start_size, end_size+1, step_size):
        print()
        ordered_result = [None, None, None]
        random_result = [None, None, None]

        ordered_insert(size, ordered_result)
        random_insert(size, random_result)

        print("{0:<15}\t{1:<15}\t{2:<15.5}\t{3:<15}\t{4:<15}\t{5:<15.5}".format(
            ordered_result[0], ordered_result[1], ordered_result[2],
            random_result[0], random_result[1], random_result[2]))


if __name__ == '__main__':
    """ 
    Executes only if it is run as a script.
    """
    import doctest

    doctest.testmod()

    main()
