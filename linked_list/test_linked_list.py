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
    
def test_list_creation():
    l = LinkedList()
    assert l is not None
    
def test_list_insert():
    l = populate_list((1,2,3))
    assert l.head.value is 3
    assert l.length == 3
    assert l.head.next.value == 2 and l.head.next.next.value is 1

def test_pop():
    l = LinkedList()
    with pytest.raises(LookupError):
        l.pop()
    l = populate_list((1,2,3))
    assert l.pop() == 3
    l.remove(l.head.value)
    assert l.pop() == 2
    
def test_size():
    l = populate_list(create_nodes())
    assert l.size() == 3
    l.remove(l.head.value)
    assert l.size() == 2
    
def test_search():
    assert populate_list((1,2,3)).search(2) == 2
    assert populate_list((1,2,3)).search(4) is None
    
def test_remove():
    l = populate_list((1,2,3))
    # vars to hold nodes for testing after they are removed from list
    n3 = l.head
    n2 = l.head.next
    n1 = l.head.next.next
    l.remove(l.head.next.value)
    sz = l.size()
    assert n3.next is n1
    assert n2.next is None
    l.remove(l.head.value)
    assert l.head is n1
    assert l.size() == sz - 1
    