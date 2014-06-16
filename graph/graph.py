# coding=utf-8

class Node(object):

    def __init__(self, value, neighbours= None):
        self.value = value
        self.name = "Node {}"
        if neighbours:
            self.neighbours = neighbours
        else:
            self.neighbours = []


class Graph(object):

    def __init__(self, sequence=None):
        self.name_counter = 0

        if sequence:
            for node in sequence:
                self.add_node(node)
        else:
            self.graph = {}

    def add_node(self, node):

        node.name = node.name.format(self.name_counter)
        self.name_counter += 1

        self.graph[node.name] = [node.value, node.neighbours]

    def add_edges(self, node1, node2):

        if node1.name not in self.graph.keys():
            self.add_node(node1)
        if node2.name not in self.graph.keys():
            self.add_node(node2)

        node1.neighbours.append(node2.name)
        node2.neighbours.append(node1.name)

    def del_node(self, node):
        if node.name not in self.graph.keys():
            raise KeyError
        else:
            node_neighbour = node.neighbours
            for neighbour in node_neighbour:
                self.graph[neighbour][1].remove(node.name)

            node.neighbours = []
            del self.graph[node.name]

    def del_edge(self, node1, node2):

        if node1.name in node2.neighbours and node2.name in node1.neighbours:
            node1.neighbours.remove(node2.name)
            node2.neighbours.remove(node1.name)
        else:
            raise LookupError

    def had_node(self, node):

        return node.name in self.graph.keys()

    def neighbours(self, node):

        if node.name not in self.graph.keys():
            raise KeyError
        else:
            return [self.graph[name] for name in node.neighbours]


    def adjacent(self, node1, node2):

        if node1.name not in self.graph.keys() or node2.name not in self.graph.keys():
            raise KeyError
        else:
            return node2.name in node1.neighbours



