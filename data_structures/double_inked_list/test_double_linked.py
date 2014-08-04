import pytest
from double_linked import Node, DoubleLinkedList

def test_node():
    """ Test node creation """
    node = Node(1)
    assert node.value == 1
    assert node.prev == None
    assert node.next == None

def test_double_linked_list():
    """ Test list creation and insert method """
    l = DoubleLinkedList()
    assert l.head == None
    assert l.tail == None
    assert l._size == 0
    for element in [1,2]:
        l.append(element)
    print('Value: {}, Type: {}'.format(l.head.value, type(l.head.value)))
    assert l.head.value == 1
    assert l.tail.value == 2
    assert l._size == 2
    assert l.head.next.value == 2
    assert l.tail.next == None
    
def test_append():
    """ Test append method """
    l = DoubleLinkedList()
    l.append(1)
    assert l.tail.value == 1
    assert l.tail.next == None
    assert l.head.value == 1
    assert l._size == 1
    l.append(2)
    assert l.tail.value == 2
    assert l.tail.next == None
    assert l.head.value == 1
    assert l.head.next.value == 2
    assert l._size == 2
    
def test_pop():
    """ Test the pop method """
    l = DoubleLinkedList()
    with pytest.raises(LookupError):
        l.pop()
    for i in range(1,4):
        l.append(i)
    assert l._size == 3
    assert l.pop() == 1
    assert l.head.value == 2
    assert l.tail.value == 3
    assert l._size == 2
    assert l.pop() == 2
    assert l.head.value == 3
    assert l.tail.value == 3
    assert l._size == 1
    
def test_shift():
    """ Test shift """
    l = DoubleLinkedList()
    with pytest.raises(LookupError):
        l.shift()
    for i in range(1,4):
        l.append(i)
    assert l._size == 3
    assert l.shift() == 3
    assert l.head.value == 1
    assert l.tail.value == 2
    assert l._size == 2
    assert l.shift() == 2
    assert l.head.value == 1
    assert l.tail.value == 1
    assert l._size == 1
    
    
def test_remove():
    """ Test remove """
    l = DoubleLinkedList()
    with pytest.raises(LookupError):
        l.remove(1)
    for i in range(1,4):
        l.append(i)
    assert l.remove(2)
    assert l.head.value == 1
    assert l.head.next.value == 3
    assert l.tail.value == 3
    assert l._size == 2
    
    
    
    
    
    
    
    
    
    