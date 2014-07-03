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
    bst = BST()
    bst.insert(5)
    assert bst.depth(node=bst.root) == 1
    bst.insert(3)
    bst.insert(4)
    bst.insert(6)
    assert bst.depth(node=bst.root) == 3

def test_depth_all_right():
    bst = BST()
    for i in range(10,110,10):
        bst.insert(i)
    assert bst.depth(bst.root) == 10

def test_depth_all_left():
    bst = BST()
    for i in range(110,10,-10):
        bst.insert(i)
    assert bst.depth(bst.root) == 10

def test_depth_collatz():
    bst = BST()
    for i in range(1,11):
        if not i % 2:
            i /= 2
        else:
            i = i * 3 + 1
        print('i = {}'.format(i))
        bst.insert(i)
    assert bst.depth(bst.root) == 5

def test_left_balance():
    bst = BST()
    bst.insert(5)
    assert bst.balance() == 0
    bst.insert(4)
    bst.insert(3)
    assert bst.balance() == 2

def test_right_balance():
    bst = BST()
    bst.insert(5)
    assert bst.balance() == 0
    bst.insert(6)
    bst.insert(7)
    assert bst.balance() == -2

def test_balanced():
    bst = BST()
    bst.insert(5)
    assert bst.balance() == 0
    bst.insert(4)
    bst.insert(7)
    assert bst.balance() == 0
    bst.insert(3)
    bst.insert(8)
    assert bst.balance() == 0