#! /usr/bin/env python3

"""
Implementation of graph.
"""


class Graph:
    def __init__(self):
        self.vertices = []
        self.edges = []

    def add_vertex(self, vertex):
        # Append vertex (node) to the list of vertices.
        self.vertices.append(vertex)

    def add_edge(self, from_vertex, to_vertex, cost):
        # Append edge (arc) as tuple to the list of edges.
        self.edges.append((from_vertex, to_vertex, cost))

    def to_string(self):
        return '{' \
            + ', '.join([str(len(self.vertices)), str(len(self.edges))] \
            + [" (%s) " % tup for tup in self.edges]) \
            + '}'


def main():
    """
    Main function.
    """
    g = Graph()
    g.add_vertex(0)
    g.add_vertex(1)
    g.add_edge(0, 1, 3)
    g.to_string()

    pass


if __name__ == '__main__':
    """ 
    Executes only if it is run as a script.
    """
    import doctest

    doctest.testmod()

    main()
