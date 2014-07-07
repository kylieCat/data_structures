import pytest
from bst import BST, Node


@pytest.fixture(scope='function')
def make_bst():
    bst = BST()
    return bst

@pytest.fixture(scope='function')
def make_nodes(make_bst):
    bst = make_bst
    bst.insert(10)
    bst.insert(2)
    bst.insert(1)
    bst.insert(4)
    bst.insert(3)
    bst.insert(5)
    bst.insert(11)
    bst.insert(13)
    bst.insert(12)
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
    bst.insert(4)
    bst.insert(3)
    bst.insert(6)
    assert bst.balance() == 1

def test_right_balance():
    bst = BST()
    bst.insert(5)
    bst.insert(6)
    bst.insert(7)
    bst.insert(3)
    assert bst.balance() == -1

def test_balanced():
    bst = BST()
    bst.insert(5)
    bst.insert(4)
    bst.insert(6)
    assert bst.balance() == 0

def test_in_order(make_nodes):
    bst = make_nodes
    pre = bst.in_order()
    expected = [1,2,3,4,5,10,11,12,13]
    actual = []
    for num in pre:
        actual.append(num.value)
    print('actual: {}'.format(actual))
    assert actual == expected

def test_empty_in_order(make_bst):
    bst = make_bst
    pre = bst.in_order()
    expected = []
    actual = []
    for num in pre:
        actual.append(num)
    print('actual: {}'.format(actual))
    assert actual == expected

def test_pre_order(make_nodes):
    bst = make_nodes
    pre = bst.pre_order()
    expected = [10,2,1,4,3,5,11,13,12]
    actual = []
    for num in pre:
        actual.append(num.value)
    print('actual: {}'.format(actual))
    assert actual == expected

def test_empty_pre_order(make_bst):
    bst = make_bst
    pre = bst.pre_order()
    expected = []
    actual = []
    for num in pre:
        actual.append(num)
    print('actual: {}'.format(actual))
    assert actual == expected

def test_post_order(make_nodes):
    bst = make_nodes
    pre = bst.post_order()
    expected = [1,3,5,4,2,12,13,11,10]
    actual = []
    for num in pre:
        actual.append(num.value)
    print('actual: {}'.format(actual))
    assert actual == expected

def test_empty_post_order(make_bst):
    bst = make_bst
    pre = bst.in_order()
    expected = []
    actual = []
    for num in pre:
        actual.append(num)
    print('actual: {}'.format(actual))
    assert actual == expected

def test_level_order(make_nodes):
    bst = make_nodes
    pre = bst.level_order()
    expected = [10,2,11,1,4,13,3,5,12]
    actual = []
    for num in pre:
        actual.append(num.value)
    print('actual: {}'.format(actual))
    assert actual == expected

def test_empty_level_order(make_bst):
    bst = make_bst
    pre = bst.level_order()
    expected = []
    actual = []
    for num in pre:
        actual.append(num)
    print('actual: {}'.format(actual))
    assert actual == expected