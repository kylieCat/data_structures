import pytest
from bst import BST, Node


@pytest.fixture(scope='function')
def make_bst():
    bst = BST()
    return bst

def test_bst():
    assert BST() is not None

def test_node():
    node = Node(2)
    assert node.value == 2
    assert node.l_child == None
    assert node.r_child == None
    assert node.parent == None

def test_insert():
    bst = BST()
    bst.insert(3)
    assert bst.root.value == 3
    bst.insert(5)
    assert bst.root.r_child.value == 5
    assert bst.root.r_child.parent is bst.root
    bst.insert(2)
    assert bst.root.l_child.value == 2
    assert bst.root.l_child.parent is bst.root

def test_contains():
    bst = BST()
    for i in range(1,11):
        bst.insert(i)
    assert bst.contains(1)
    assert bst.contains(5)
    assert not bst.contains(15)

def test_size():
    bst = BST()
    assert bst.size() == 0
    bst.insert(5)
    assert bst.size() == 1
    bst.insert(5)
    assert bst.size() == 1

def test_depth():
    pass

def test_balance():
    pass