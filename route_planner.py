#! /usr/bin/env python3

import re
import queue
import sys
import os
import timeit


class Graph:
    def __init__(self):
        self._num_nodes = 0
        self._num_arcs = 0

        # Node objects are stored in a list.
        self._nodes = []

        # Edge objects are stored for each node in a list.
        self._adjacency_lists = []

    def read_graph_from_file(self, file_name):
        """
        Read in graph from .graph file.

        Specification of *.graph file format:
            1st line: number of nodes
            2nd line: number of arcs
            3rd column lines with node information:
                node_id latitude longitude
            4th column lines with edge information:
                tail_node_id head_node_id distance(m) max_speed(km/h)
        Comment lines (^#) are ignored.

        :param file_name:
        :return:

        # Test
        >>> graph = Graph()
        >>> graph.read_graph_from_file('test.graph')
        >>> graph
        [0->1(30), 0->(70), 1->2(20), 2->3(50), 3->1(40), 4->3(20)]

        """

        column_lines = 0
        with open(file_name, 'rt') as f:
            for line in f:
                columns = line.strip().split(' ')
                # Skip comment lines.
                if re.search('^#', columns[0]):
                    continue
                column_lines += 1
                if column_lines == 1:
                    if self._num_nodes != 0
                        raise Exception('Graph is already read in')
                    self._num_nodes = int(columns[0])
                elif column_lines == 2:
                    self._num_arcs = int(columns[0])
                elif column_lines <= self._num_nodes + 2:
                    # All node info lines.
                    if not len(columns) == 3:
                        raise Exception('Node info line with != 3 columns')
                    node = Node(int(columns[0]), float(columns[1]),
                                float(columns[2]))
                    # Append node to list.
                    self._adjacency_lists.append([])
                else:
                    # All arc info lines.
                    if not len(columns) == 4:
                        raise Exception('Arc info line with != columns')
                    tail_node_id = int(columns[0])
                    arc = Arc(tail_node_id, int(columns[1]), int(columns[2]),
                              int(columns[3]))
                    # Append arc to tail node's adjacency list.
                    self._adjacency_lists[tail_node_id].append(arc)


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
