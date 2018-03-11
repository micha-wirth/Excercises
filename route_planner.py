#! /usr/bin/env python3

"""
Exercise #13: Implementation of Dijkstra's algorithm.
"""

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

    def read_graph_from_file(self, file_name, directed=True):
        """
        Read in graph from *.graph file.

        Specification of *.graph file format:
            1st line: number of nodes
            2nd line: number of arcs
            3-column lines with node information:
                node_id latitude longitude
            4-column lines with edge information:
                tail_node_id head_node_id distance[m] max_speed[km/h]
        Comment lines (^#) are ignored.

        :param file_name:
        :return: None

        # Test
        >>> graph = Graph()
        >>> graph.read_graph_from_file('graph_13/test.graph')
        >>> graph
        [0->1(30), 0->2(70), 1->2(20), 2->3(50), 3->1(40), 4->3(20)]
        """

        column_lines = 0
        with open(file_name, 'rt') as graph_file:
            for line in graph_file:
                columns = line.strip().split(' ')
                # Skip comment lines.
                if re.search('^#', columns[0]):
                    continue
                column_lines += 1
                if column_lines == 1:
                    if self._num_nodes != 0:
                        raise Exception('Graph is already read in')
                    # Number of nodes.
                    self._num_nodes = int(columns[0])
                elif column_lines == 2:
                    # Number of arcs.
                    self._num_arcs = int(columns[0])
                elif column_lines <= self._num_nodes + 2:
                    # All node info lines.
                    if not len(columns) == 3:
                        raise Exception('Node info line with != 3 columns')
                    node = Node(int(columns[0]), float(columns[1]),
                                float(columns[2]))
                    # Append node to list.
                    self._nodes.append(node)
                    # Append empty adjacency list for node.
                    self._adjacency_lists.append([])
                else:
                    # All arc info lines.
                    if not len(columns) == 4:
                        raise Exception('Arc info line with != 4 columns')
                    tail_node_id = int(columns[0])
                    arc = Arc(tail_node_id, int(columns[1]), int(columns[2]),
                              int(columns[3]))

                    # Create undirected graph.
                    if not directed:
                        self._adjacency_lists[arc.head_node_id].append(Arc(arc.head_node_id,
                                                                            arc.tail_node_id,
                                                                            arc.distance,
                                                                            arc.max_speed))
                    # Append arc to tail node's adjacency list.
                    self._adjacency_lists[tail_node_id].append(arc)
        # graph_file.close()
        if not graph_file.closed:
            raise Exception('File *.graph was not closed')

        return None

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
        >>> graph.compute_reachable_nodes(0)[0]
        4
        >>> graph.compute_reachable_nodes(4)[0]
        6
        >>> graph.compute_reachable_nodes(6)[0]
        1
        """

        # List of nodes to visit currently.
        current_level = [node_id]
        # Create a list of marked nodes. Reachable nodes are marked with 1.
        marked_nodes = [0] * self._num_nodes
        # Mark start node as reachable node.
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
        # return num_marked_nodes
        # TODO
        return (num_marked_nodes, marked_nodes)

    def set_arc_costs_to_travel_time(self, max_vehicle_speed):
        """
        Set arc costs to travel time in whole seconds.

        :param self:
        :param max_vehicle_speed: [km/h]
        :return: None

        # Doctest(s):
        >>> graph = Graph()
        >>> graph.read_graph_from_file('graph_13/test.graph')
        >>> graph
        [0->1(30), 0->2(70), 1->2(20), 2->3(50), 3->1(40), 4->3(20)]
        >>> graph.set_arc_costs_to_travel_time(100)
        >>> graph
        [0->1(4), 0->2(8), 1->2(2), 2->3(6), 3->1(5), 4->3(2)]
        """

        for i in range(self._num_nodes):
            for arc in self._adjacency_lists[i]:
                # Compute max. possible speed for this arc.
                max_speed = min(arc.max_speed, int(max_vehicle_speed))
                # Compute travel time in whole seconds.
                travel_time_sec = '{0:.0f}'.format(arc.distance / (max_speed / 3.6))
                # Set costs to travel time in whole seconds.
                arc.costs = int(travel_time_sec)

        return None

    def set_arc_costs_to_distance(self):
        """
        Set arc costs to distance.

        :return: None

        # Doctest(s):
        >>> graph = Graph()
        >>> graph.read_graph_from_file(('graph_13/test.graph'))
        >>> graph
        [0->1(30), 0->2(70), 1->2(20), 2->3(50), 3->1(40), 4->3(20)]
        >>> graph.set_arc_costs_to_travel_time(100)
        >>> graph.set_arc_costs_to_distance()
        >>> graph
        [0->1(30), 0->2(70), 1->2(20), 2->3(50), 3->1(40), 4->3(20)]
        """

        for i in range(self._num_nodes):
            for arc in self._adjacency_lists[i]:
                arc.costs = arc.distance

        return None

    def compute_lcc(self):
        """ TODO
        Mark all nodes in the largest connected component.

        :param marked_nodes:
        :return: longest connected component.

        # Doctest(s):
        >>> graph = Graph()
        >>> graph.read_graph_from_file('graph_13/test.graph')
        >>> graph
        [0->1(30), 0->2(70), 1->2(20), 2->3(50), 3->1(40), 4->3(20)]
        >>> graph.compute_lcc()
        (4, [4, 1, 2, 3])
        >>> graph2 = Graph()
        >>> graph2.read_graph_from_file('graph_13/test2.graph')
        >>> graph2.compute_lcc()
        (6, [5, 1, 2, 3, 4])
        """
        # Shallow copy of all nodes.
        unvisited_nodes = self._nodes[:]
        lcc = (0, None)

        # Visit all nodes which are in no connected component.
        # while len(unvisited_nodes) > 0:
        while unvisited_nodes:
            # Remove one node in each iteration.
            node = unvisited_nodes.pop()
            # node = unvisited_nodes[0]

            (num_marked_nodes, marked_nodes) = self.compute_reachable_nodes(node_id=node._id)

            # Create a list with all visited nodes in this lcc.
            marked_indices = [node._id]
            # marked_indices = []
            for marked_node, marked in enumerate(marked_nodes):
                if marked == 1 and self._nodes[marked_node] in unvisited_nodes:
                    marked_indices.append(marked_node)
                    # Remove from unvisited list.
                    unvisited_nodes.remove(self._nodes[marked_node])

            # Have we already found a larger component?
            if num_marked_nodes > lcc[0]:
                lcc = (num_marked_nodes, marked_indices)

        return lcc


    def compute_shortest_paths(self, start_node_id):
        """ TODO
        Compute the shortest paths for a given start node.
        To solve this problem the Dijkstra's algorithm is used.
        :param start_node_id: identifier of start node
        :return: None

        # Doctest(s):
        >>> graph = Graph()
        >>> graph.read_graph_from_file('graph_13/test.graph')
        >>> graph
        [0->1(30), 0->2(70), 1->2(20), 2->3(50), 3->1(40), 4->3(20)]
        >>> start_id = 1
        >>> graph.compute_shortest_paths(start_id)
        >>> ['{0}->{1}({2})'.format(start_id, node._id, node._distance) for node in graph._nodes]
        ['1->0(-1)', '1->1(0)', '1->2(20)', '1->3(70)', '1->4(-1)']
        """
        # Distance from start node to itself is 0.
        self._nodes[start_node_id]._distance = 0

        # Priority queue for shortest path storage.
        active_nodes = queue.PriorityQueue()
        # Put start node into priority queue as first element.
        active_nodes.put(self._nodes[start_node_id])

        while not active_nodes.empty():
        # while active_nodes.qsize():
            node = active_nodes.get()
            if node._settled:
                # Node has already been settled.
                continue
            # Settle active node.
            node._settled = True

            # Update all connected nodes.
            for arc in self._adjacency_lists[node._id]:
                new_node = self._nodes[arc.head_node_id]
                new_distance = node._distance + arc.costs

                # Update tentative distance if a new distance is smaller.
                if not new_node._settled and (
                        new_node._distance < 0 or
                        new_distance < new_node._distance):
                    new_node._distance = new_distance
                    new_node._traceback_arc = arc
                    active_nodes.put(new_node)

        return None

    def __repr__(self):
        """
        Define object's string representation.

        :return: object represented as string.

        >>> graph = Graph()
        >>> graph.read_graph_from_file('graph_13/test.graph')
        >>> graph
        [0->1(30), 0->2(70), 1->2(20), 2->3(50), 3->1(40), 4->3(20)]
        """

        obj_str_repr = ''
        for idx in range(self._num_nodes):
           for arc in self._adjacency_lists[idx]:
                obj_str_repr += repr(arc) + ', '
        if obj_str_repr:
            return '[' + obj_str_repr[:-2] + ']'
        else:
            return '[]'


class Node:

    def __init__(self, node_id, latitude, longitude, traceback_arc=None):
        self._id = node_id
        self._latitude = latitude
        self._longitude = longitude
        # Especially needed for Dijkstra's algorithm.
        self._traceback_arc = traceback_arc
        self._settled = False
        self._distance = -1

    def __repr__(self):
        return '{0}'.format(self._id)

    def __lt__(self, other):
        """ Defines the operator '<' (less than) for priority queue. """
        return self._distance < other._distance


class Arc:

    def __init__(self, tail_id, head_id, distance, max_speed):
        self.tail_node_id = tail_id
        self.head_node_id = head_id
        self.distance = distance
        self.max_speed = max_speed
        # Set default costs to distance.
        self.costs = distance

    def __repr__(self):
        return '{0}->{1}({2})'.format(self.tail_node_id, self.head_node_id,
                                      self.costs)

def travel_to(graph, end_node, max_speed):
    """ Compute distance and travel time of the selected path. """
    node = graph._nodes[end_node]
    # Time in hours [h].
    time = 0
    # Distance in kilometers [km]
    distance = 0

    while True:
        arc = node._traceback_arc
        if not arc:
            break

        distance += arc.distance / 1000.0

        # v = s / t => t = s / v
        time += arc.distance / 1000.0 / min(arc.max_speed, max_speed)

        # Follow to previous node.
        node = graph._nodes[arc.tail_node_id]

    return (distance, time_to_string(time))

def time_to_string(time):
    """ Convert time [h] to string format. """
    hh = int(time)
    mm = int((time - hh) * 60)

    return '{0} hour(s) and {1} minute(s)'.format(hh, mm)

def reset_graph(graph):
    """ Resets the graph and it's fields. """
    for node in graph._nodes:
        node._traceback_arc = None
        node._settled = False
        node._distance = -1

def get_furthest_node(graph):
    """ Returns the id fo the furthest node. """
    max_dist = (-1, None)

    for node in graph._nodes:
        if node._distance > max_dist[0]:
            max_dist = (node._distance, node._id)

    return max_dist[1]


def main():
    """ TODO
    Main function.
    """
    print("Read in file *.graph: START!")
    graph = Graph()
    graph.read_graph_from_file('bawue_bayern_13/bawue_bayern.graph')
    graph.set_arc_costs_to_distance()
    print("Read in file *.graph: END!")

    # Shortest and longest distance.
    print("\nShortest path:")
    graph.compute_shortest_paths(5508637)
    result1 = travel_to(graph, 4435496, sys.maxsize)
    print("Distance: {0:.3f} km\tTime: {1}".format(result1[0], result1[1]))
    print("\nLongest path:")
    max_dist_id1 = get_furthest_node(graph)
    result1 = travel_to(graph, max_dist_id1, sys.maxsize)
    print("Distance: {0:.3f} km\tTime: {1}".format(result1[0], result1[1]))

    # Shortest and longest time of travel with up to 130 km/h.
    print("\nShortest time of travel with max. speed up to 130 km/h:")
    reset_graph(graph)
    graph.set_arc_costs_to_travel_time(max_vehicle_speed=130)
    graph.compute_shortest_paths(5508637)
    result2 = travel_to(graph, 4435496, 130)
    print("Distance: {0:.3f} km\tTime: {1}".format(result2[0], result2[1]))
    print("\nLongest time of travel with max. speed up to 130 km/h:")
    max_dist_id2 = get_furthest_node(graph)
    result2 = travel_to(graph, max_dist_id2, 130)
    print("Distance: {0:.3f} km\tTime: {1}".format(result2[0], result2[1]))

    # Shortest and longest time of travel with up to 100 km/h.
    print("\nShortest time of travel with max. speed up to 100 km/h:")
    reset_graph(graph)
    graph.set_arc_costs_to_travel_time(max_vehicle_speed=100)
    graph.compute_shortest_paths(5508637)
    result3 = travel_to(graph, 4435496, 100)
    print("Distance: {0:.3f} km\tTime: {1}".format(result3[0], result3[1]))
    print("\nLongest time of travel with max. speed up to 100 km/h")
    max_dist_id3 = get_furthest_node(graph)
    result3 = travel_to(graph, max_dist_id3, 100)
    print("Distance: {0:.3f} km\tTime: {1}".format(result3[0], result3[1]))



    # graph = Graph()
    # graph.read_graph_from_file('graph_13/test.graph')
    # print(graph)
    # print(graph.get_num_nodes())
    # print(graph.get_num_arcs())
    # print(graph._adjacency_lists)


if __name__ == '__main__':
    """ 
    Executes only if it is run as a script.
    """
    import doctest

    doctest.testmod()

    main()
