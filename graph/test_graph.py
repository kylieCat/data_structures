# coding=utf-8
import pytest
from graph import Graph, Node


@pytest.fixture(scope="function")
def make_nodes():
    nodes = []
    for i range(10):
        nodes.append(Node(i))
    return nodes

def test_add_node():
    _graph = Graph()
    _graph.add_node(Node(4))
    assert _graph.graph == {'Node 0': [4, []]}


def test_add_edge():
    _graph = Graph()
    _node1 = Node(4)
    _node2 = Node(5)
    _graph.add_edges(_node1, _node2)
    assert _graph.graph == {'Node 0': [4, ['Node 1']],
                            'Node 1': [5, ['Node 0']]}


def test_del_node():
    _graph = Graph()
    _node1 = Node(4)
    _node2 = Node(5)
    _graph.add_edges(_node1, _node2)
    _graph.del_node(_node2)
    assert _graph.graph == {'Node 0': [4, []]}
    _node3 = Node(6)
    _node4 = Node(7)
    _graph.add_edges(_node1, _node2)
    _graph.add_edges(_node3, _node4)
    _graph.add_edges(_node2, _node4)
    _graph.del_node(_node4)
    assert _graph.graph == {'Node 0' : [4, ['Node 1']],
                            'Node 1' : [5, ['Node 0']],
                            'Node 3' : [6, []]}


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
    assert _graph.graph == {'Node 0' : [4, ['Node 1']], 
                            'Node 1' : [5, ['Node 0']], 
                            'Node 2' : [6, ['Node 3']], 
                            'Node 3' : [7, ['Node 2']]}



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
    assert _graph.neighbours(_node2) == [[4, ['Node 1']], [7, ['Node 2', 'Node 1']]]


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
    
def test_depth_traversal():
    g = Graph()
    for i in range(10):
        g.add_node(Node(i))