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
    g.add_edges(nodes[0],nodes[1], 1)
    g.add_edges(nodes[0],nodes[6], 1)
    g.add_edges(nodes[0],nodes[7], 1)
    g.add_edges(nodes[1],nodes[2], 1)
    g.add_edges(nodes[1],nodes[5], 1)
    g.add_edges(nodes[2],nodes[3], 1)
    g.add_edges(nodes[2],nodes[4], 1)
    g.add_edges(nodes[7],nodes[8], 1)
    g.add_edges(nodes[8],nodes[9], 1)
    return g

@pytest.fixture(scope="function")
def make_weighted_graph(make_nodes):
    nodes = make_nodes[:6]
    g = Graph(nodes)
    g.add_edges(nodes[0],nodes[1], 7)
    g.add_edges(nodes[0],nodes[2], 9)
    g.add_edges(nodes[0],nodes[5], 14)
    g.add_edges(nodes[1],nodes[2], 10)
    g.add_edges(nodes[1],nodes[3], 15)
    g.add_edges(nodes[2],nodes[3], 11)
    g.add_edges(nodes[2],nodes[5], 2)
    g.add_edges(nodes[3],nodes[4], 6)
    g.add_edges(nodes[4],nodes[5], 9)
    return g


def test_add_node():
    _graph = Graph()
    _graph.add_node(Node(4))
    assert _graph.graph == {'n0': {}}


def test_add_edge():
    _graph = Graph()
    _node1 = Node(4)
    _node2 = Node(5)
    _graph.add_edges(_node1, _node2, 1)
    assert _graph.graph == {'n0': {'n1': 1},
                            'n1': {'n0': 1}}


def test_del_node():
    _graph = Graph()
    _node1 = Node(4)
    _node2 = Node(5)
    _graph.add_edges(_node1, _node2, 1)
    _graph.del_node(_node2)
    assert _graph.graph == {'n0': {}}
    _node3 = Node(6)
    _node4 = Node(7)
    _graph.add_edges(_node1, _node2, 1)
    _graph.add_edges(_node3, _node4, 1)
    _graph.add_edges(_node2, _node4, 1)
    _graph.del_node(_node4)
    assert _graph.graph == {'n0': {'n1': 1},
                            'n1': {'n0': 1},
                            'n3': {}}


def test_del_edge():
    _graph = Graph()
    _node1 = Node(4)
    _node2 = Node(5)
    _node3 = Node(6)
    _node4 = Node(7)
    _graph.add_edges(_node1, _node2, 1)
    _graph.add_edges(_node3, _node4, 1)
    _graph.add_edges(_node2, _node4, 1)
    _graph.del_edge(_node2, _node4)
    assert _graph.graph == {
                            'n0': {'n1': 1},
                            'n1': {'n0': 1},
                            'n2': {'n3': 1},
                            'n3': {'n2': 1}}
    assert _graph.graph == {'n0': {'n1': 1}, 'n1': {'n0': 1}, 'n2': {'n3': 1}, 'n3': {'n2': 1}}


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
    _graph.add_edges(_node1, _node2, 1)
    _graph.add_edges(_node3, _node4, 1)
    _graph.add_edges(_node2, _node4, 1)
    _graph.add_edges(_node1, _node2, 2)
    _graph.add_edges(_node3, _node4, 2)
    _graph.add_edges(_node2, _node4, 2)
    assert _graph.neighbours(_node2) == ['n0', 'n3']



def test_adjacent():
    _graph = Graph()
    _node1 = Node(4)
    _node2 = Node(5)
    _node3 = Node(6)
    _node4 = Node(7)
    _graph.add_edges(_node1, _node2, 1)
    _graph.add_edges(_node3, _node4, 1)
    _graph.add_edges(_node2, _node4, 1)
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


def test_dijekstra(make_weighted_graph):
    g = make_weighted_graph
    visited, path = g.dijekstra('n0', 'n4')
    print('visited: {}\npath: {}'.format(visited, path))
    expected_visits = {'n0': 0, 'n1': 7, 'n2': 9, 'n3': 20, 'n4': 20, 'n5': 11}
    expected_path = ['n0', 'n1', 'n2', 'n5', 'n4']
    assert expected_visits, expected_path == g.dijekstra('n0', 'n4')
    assert {'n0' : 0}, ['n0'] == g.dijekstra('n0', 'n0')

def test_floyd_warshall(make_weighted_graph):

    graph_obj = Graph()
    graph_obj.name_counter = 1

    n1 = Node('n1',{'n2':2, 'n3':4})
    n2 = Node('n2',{'n1':2, 'n3':1, 'n4':5})
    n3 = Node('n3',{'n1':4, 'n2':1, 'n4':3})
    n4 = Node('n4',{'n2':5, 'n3':3})

    graph_obj.add_node(n1)
    graph_obj.add_node(n2)
    graph_obj.add_node(n3)
    graph_obj.add_node(n4)

    graph = graph_obj.graph


    inf = float('inf')
    adj_matrix_of_graph = {'n1': {'n1': 0, 'n2': 2, 'n3': 4, 'n4': inf},
                           'n2': {'n1': 2, 'n2': 0, 'n3': 1, 'n4': 5},
                           'n3': {'n1': 4, 'n2': 1, 'n3': 0, 'n4': 3},
                           'n4': {'n1': inf, 'n2': 5, 'n3': 3, 'n4': 0}}

    adj_matrix_of_graph_with_shortest_path = {'n1': {'n1': 0, 'n2': 2, 'n3': 3, 'n4': 6},
                                              'n2': {'n1': 2, 'n2': 0, 'n3': 1, 'n4': 4},
                                              'n3': {'n1': 3, 'n2': 1, 'n3': 0, 'n4': 3},
                                              'n4': {'n1': 6, 'n2': 4, 'n3': 3, 'n4': 0}}


    t = graph_obj.floyd_warshall(graph)
    print graph
    print t[0]
    print t[1]
    assert t[0] == adj_matrix_of_graph
    assert t[1] == adj_matrix_of_graph_with_shortest_path
