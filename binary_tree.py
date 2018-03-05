#! /usr/bin/env python3

class BinaryTree():
    class Node():
        def __init__(self, key, parent_node=None, left_child=None, right_child=None):
            self.key = key
            self.value = None
            self.parent_node = parent_node
            self.left_child = left_child
            self.right_child = right_child

    def __init__(self):
        self.node0 = self.Node(4)
        self.node1 = self.Node(2)
        self.node2 = self.Node(6)
        self.node3 = self.Node(1)
        self.node4 = self.Node(3)
        self.node5 = self.Node(5)
        self.node6 = self.Node(7)

        self.node0.left_child = self.node1
        self.node0.right_child = self.node2

        self.node1.left_child = self.node3
        self.node1.right_child = self.node4

        self.node2.left_child = self.node5
        self.node2.right_child = self.node6

    def print_all_keys(self, node):
        if node:
            # Print keys in descending order.
            self.print_all_keys(node.right_child)
            print(node.key)
            self.print_all_keys(node.left_child)

            # # Print keys in ascending order.
            # self.print_all_keys(node.left_child)
            # print(node.key)
            # self.print_all_keys(node.right_child)
        else:
            return None


def main():
    """ 
    Main function.
    """
    tree = BinaryTree()
    tree.print_all_keys(tree.node0)
    pass


if __name__ == '__main__':
    """ 
    Executes only if it is run as a script.
    """
    import doctest

    doctest.testmod()

    main()
