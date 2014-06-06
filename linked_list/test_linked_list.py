import pytest
from linked_list import Node, LinkedList


def create_nodes():
    """ Creates 3 nodes to use for testing, returns a 3 element tuple """
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    return n1, n2, n3
    
def populate_list(nodes):
    """ Accepts a sequence of nodes and inserts them into a new LinkedList, returns the list """
    l = LinkedList()
    for node in nodes:
        l.insert(node)
    return l

def test_node_creation():
    n1 = Node(1)
    assert n1.value == 1
    assert n1.next == None
    
def test_list_insert():
    n1, n2, n3 = create_nodes()
    l = populate_list((n1,n2,n3))
    assert l.head is n3
    assert l.length == 3
    assert n3.next is n2 and n2.next is n1

def test_pop():
    l = LinkedList()
    with pytest.raises(LookupError):
        l.pop()
    l = populate_list(create_nodes())
    assert l.pop().value == 3
    l.remove(l.head)
    assert l.pop().value == 2
    
def test_size():
    l = populate_list(create_nodes())
    assert l.size() == 3
    l.remove(l.head)
    assert l.size() == 2
    
def test_search():
    assert populate_list(create_nodes()).search(2) == 2
    assert populate_list(create_nodes()).search(4) is None
    
def test_remove():
    n1, n2, n3 = create_nodes()
    l = populate_list((n1,n2,n3))
    l.remove(n2)
    sz = l.size()
    assert n3.next is n1
    assert n2.next is None
    l.remove(n3)
    assert l.head is n1
    assert l.size() == sz - 1
    