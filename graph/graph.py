# coding=utf-8
class Node(object):
    def __init__(self, value, neighbours= None):
        self.value = value
        self.name = "n{}"
        if neighbours:
            self.neighbours = neighbours
        else:
            self.neighbours = {}


class Graph(object):
    def __init__(self, sequence=None):
        self.name_counter = 0
        self.graph = {}
        if sequence:
            for node in sequence:
                self.add_node(node)


    def add_node(self, node):
        node.name = node.name.format(self.name_counter)
        self.name_counter += 1
        self.graph[node.name] = node.neighbours


    def add_edges(self, node1, node2):
        if node1.name not in self.graph.keys():
            self.add_node(node1)
        if node2.name not in self.graph.keys():
            self.add_node(node2)
        node1.neighbours.update({node2.name: 2})
        node2.neighbours.update({node1.name: 2})


    def del_node(self, node):
        if node.name not in self.graph.keys():
            raise KeyError
        else:
            node_neighbour = node.neighbours
            for neighbour in node_neighbour.keys():
                del self.graph[neighbour][node.name]
            node.neighbours = {}
            del self.graph[node.name]


    def del_edge(self, node1, node2):
        if node1.name in node2.neighbours and node2.name in node1.neighbours:
            del node1.neighbours[node2.name]
            del node2.neighbours[node1.name]
        else:
            raise LookupError


    def had_node(self, node):
        return node.name in self.graph.keys()


    def neighbours(self, node):
        if node.name not in self.graph.keys():
            raise KeyError
        else:
            return [name for name in node.neighbours.keys()]


    def adjacent(self, node1, node2):
        if node1.name not in self.graph.keys() or node2.name not in self.graph.keys():
            raise KeyError
        else:
            return node2.name in node1.neighbours


    def breadth_first_traversal(self, start):
        visited, stack = [], [start]
        while stack:
            node = stack.pop(0)
            if node not in visited:
                visited.append(node)
                stack.extend([n for n in self.graph[node] if n not in visited])
        return visited


    def depth_first_traversal(self, start):
        visited, stack = [], [start]
        while stack:
            node = stack.pop(0)
            if node not in visited:
                visited.append(node)
                stack[0:0] = [n for n in self.graph[node] if n not in visited]
                # import pdb; pdb.set_trace()
                while len(self.graph[node]) > 1:
                    if node == start:
                        break
                    else:
                        stack[0:0] = self.graph[node]
                        node = [i for i in self.graph[node].keys() if i not in visited][0]
                        visited.append(node)
        return visited