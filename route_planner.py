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
        >>> graph.read_graph_from_file('graph_13/test.graph')
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
                    if self._num_nodes != 0:
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

    def get_num_nodes(self):
        """
        :return: number of nodes in graph.
        """
        return self._num_nodes

    def get_num_arcs(self):
        """
        :return: number of arcs in graph.
        """
        return self._num_arcs

    def compute_reachable_nodes(self, node_id):
        """
        Mark all reachable nodes from a given node.
        Implemented as breadth first search (BFS).

        :param node_id: identifier of a given node.
        :return: number of reachable start nodes (incl. start node).

        >>> graph = Graph()
        >>> graph.read_graph_from_file('graph_13/test2.graph')
        >>> graph.compute_reachable_nodes(0)
        4
        >>> graph.compute_reachable_nodes(4)
        6
        >>> graph.compute_reachable_nodes(6)
        1
        """

        # List of currently visited nodes.
        current_level = [node_id]
        # Create a list of marked nodes. Reachable nodes are marked with 1.
        marked_nodes = [0] * self._num_nodes
        # Mark start node as reachable.
        marked_nodes[node_id] = 1
        # Store number of reachable nodes.
        num_marked_nodes = 1
        # Visit all nodes.
        while len(current_level) > 0:
            # Store nodes which are connected to current_level nodes.
            next_level = []
            # Go through all nodes of current_level.
            for curr_node_id in current_level:
                # Go through arcs of current node:
                for arc in self._adjacency_lists[curr_node_id]:
                    # If had_id has not been marked yet.
                    if not marked_nodes[arc.head_node_id]:
                        marked_nodes[arc.head_node_id] = 1
                        num_marked_nodes += 1
                        # Add head_id to the new current level nodes.
                        next_level.append(arc.head_node_id)
            current_level = next_level
        return num_marked_nodes

    def set_arc_costs_to_travel_time(self, max_vehicle_speed):
        """
        Set arc costs to travel time in whole seconds.

        :param self:
        :param max_vehicle_speed: [km/h]
        :return: None

        >>> graph = Graph()
        >>> graph.read_graph_from_file('graph_13/test.graph')
        >>> graph
        [0->1(30), 0->2(70), 1->2(20), 2->3(50), 3->1(40), 4->3(20)]
        """

        for i in range(self._num_nodes):
            for arc in self._adjacency_lists[i]:
                arc.costs = arc.distance

    def compute_lcc(self, marked_nodes):
        """
        Mark all nodes in the largest connected component.
        :param marked_nodes:
        :return:
        """

    def compute_shortest_paths(self, start_node_id):
        """
        Compute the shortest paths for a given start node.
        To solve this problem the Dijkstra's algorithm is used.
        :param start_node_id:
        :return:
        """

    def __repr__(self):
        """
        Define object's string representation.

        :return: object represented as string.

        >>> graph = Graph()
        >>> graph.read_graph_from_file('graph_13/test.graph')
        >>> graph
        [0->1(30), 0->2(70), 1->2(20), 2->3(50), 3->1(40), 4->3(20)]
        """

        obj_str_repr = ""
        for i in range(self._num_nodes):
            for arc in self._adjacency_lists[i]:
                obj_str_repr += repr(arc) + ", "
            if obj_str_repr:
                return "[" + obj_str_repr[:-2] + "]"
            else:
                return "[]"


class Node:
    def __init__(self, node_id, latitude, longitude):
        self._id = node_id
        self._latitude = latitude
        self._longitude = longitude

    def __repr__(self):
        return "{0}".format(self._id)


class Arc:
    def __init__(self, tail_id, head_id, distance, max_speed):
        self.tail_node_id = tail_id
        self.head__node_id = head_id
        self.distance = distance
        self.max_speed = max_speed
        self.costs = distance

    def __repr__(self):
        return "{0}->{1}({2}".format(self.tail_node_id, self.head__node_id,
                                     self.costs)


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
