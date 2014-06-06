import pytest
from stack import Node, Stack, EmptyStack

@pytest.fixture(scope='session')
def create_nodes():
    n1, n2, n3 = Node(1), Node(2), Node('a')
    return n1, n2, n3

@pytest.fixture(scope='session')
def create_stack():
    s = Stack()
    return s

def test_node(create_nodes):
    """ Test node creation """
    n1, n2, n3 = create_nodes
    assert n1.value == 1
    assert n1.next == None

def test_stack():
    s = Stack()
    assert s is not None
    assert s.head == None
    
def test_push(create_nodes, create_stack):
    n1, n2, n3 = create_nodes
    s = create_stack
    s.push(n1)
    assert s.head is n1
    assert s is not None
    s.push(n2)
    assert s.head is n2
    assert n2.next is n1
    s.push(n3)
    assert s.head is n3
    assert n3.next is n2
    assert n2.next is n1
    
def test_pop(create_nodes, create_stack):
    n1, n2, n3 = Node(1), Node(2), Node(3)
    s = Stack()
    with pytest.raises(EmptyStack):
        s.pop()
    for ele in (n1,n2,n3):
        s.push(ele)
    assert s.head.next is n2
    assert s.pop() == n3.value
    assert s.head is n2
    assert s.head.next is n1
    assert n3.next is None
    
    
    
    
    
    
    
    
    
    