# coding=utf-8
import pytest
from graph import Graph, Node


@pytest.fixture(scope="function")
def make_nodes():
    nodes = []
    for i in range(10):
        nodes.append(Node(i))
    return nodes


@pytest.fixture(scope="function")
def make_graph(make_nodes):
    nodes = make_nodes
    g = Graph(nodes)
    g.add_edges(nodes[0],nodes[1])
    g.add_edges(nodes[0],nodes[6])
    g.add_edges(nodes[0],nodes[7])
    g.add_edges(nodes[1],nodes[2])
    g.add_edges(nodes[1],nodes[5])
    g.add_edges(nodes[2],nodes[3])
    g.add_edges(nodes[2],nodes[4])
    g.add_edges(nodes[7],nodes[8])
    g.add_edges(nodes[8],nodes[9])
    return g


def test_add_node():
    _graph = Graph()
    _graph.add_node(Node(4))
    assert _graph.graph == {'n0': []}


def test_add_edge():
    _graph = Graph()
    _node1 = Node(4)
    _node2 = Node(5)
    _graph.add_edges(_node1, _node2)
    assert _graph.graph == {'n0': ['n1'],
                            'n1': ['n0']}


def test_del_node():
    _graph = Graph()
    _node1 = Node(4)
    _node2 = Node(5)
    _graph.add_edges(_node1, _node2)
    _graph.del_node(_node2)
    assert _graph.graph == {'n0': []}
    _node3 = Node(6)
    _node4 = Node(7)
    _graph.add_edges(_node1, _node2)
    _graph.add_edges(_node3, _node4)
    _graph.add_edges(_node2, _node4)
    _graph.del_node(_node4)
    assert _graph.graph == {'n0' : {'n1': 2},
                            'n1' : ['n0'],
                            'n3' : []}


def test_del_edge():
    _graph = Graph()
    _node1 = Node(4)
    _node2 = Node(5)
    _node3 = Node(6)
    _node4 = Node(7)
    _graph.add_edges(_node1, _node2)
    _graph.add_edges(_node3, _node4)
    _graph.add_edges(_node2, _node4)
    _graph.del_edge(_node2, _node4)
    assert _graph.graph == {'n0' : ['n1'],
                            'n1' : ['n0'],
                            'n2' : ['n3'],
                            'n3' : ['n2']}


def test_has_node():
    _graph = Graph()
    _node1 = Node(4)
    _node2 = Node(5)
    _graph.add_node(_node1)
    assert _graph.had_node(_node1) == True
    assert _graph.had_node(_node2) == False


def test_neighbours():
    _graph = Graph()
    _node1 = Node(4)
    _node2 = Node(5)
    _node3 = Node(6)
    _node4 = Node(7)
    _graph.add_edges(_node1, _node2)
    _graph.add_edges(_node3, _node4)
    _graph.add_edges(_node2, _node4)
    assert _graph.neighbours(_node2) == [['n1'], ['n2', 'n1']]


def test_adjacent():
    _graph = Graph()
    _node1 = Node(4)
    _node2 = Node(5)
    _node3 = Node(6)
    _node4 = Node(7)
    _graph.add_edges(_node1, _node2)
    _graph.add_edges(_node3, _node4)
    _graph.add_edges(_node2, _node4)
    assert _graph.adjacent(_node1, _node2) == True
    assert _graph.adjacent(_node3, _node4) == True
    assert _graph.adjacent(_node2, _node4) == True
    assert _graph.adjacent(_node1, _node4) == False


def test_breadth_traversal(make_graph):
    g = make_graph
    assert g.breadth_first_traversal('n0') == ['n0', 'n1', 'n6', 'n7', 'n2', 'n5', 'n8', 'n3', 'n4', 'n9']


def test_depth_traversal(make_graph):
    g = make_graph
    assert g.depth_first_traversal('n0') == ['n{}'.format(i) for i in range(10)]