import pytest
from balanced_bst import BST, Node


@pytest.fixture(scope='function')
def make_bst():
    b_bst = BST()
    return b_bst


@pytest.fixture(scope='function')
def make_right_tree(make_bst):
    b_bst = make_bst
    b_bst.insert(10)
    b_bst.insert(11)
    b_bst.insert(12)

    return b_bst

@pytest.fixture(scope='function')
def make_left_tree(make_bst):
    b_bst = make_bst
    b_bst.insert(10)
    b_bst.insert(9)
    b_bst.insert(8)

    return b_bst

@pytest.fixture(scope='function')
def make_unbalanced_tree(make_bst):
    b_bst = make_bst
    b_bst.insert(10)
    b_bst.insert(11)
    b_bst.insert(8)
    b_bst.insert(9)
    b_bst.insert(7)
    b_bst.insert(6)

    return b_bst

def test_right_balance(make_right_tree):
    b_bst = make_right_tree
    pre = b_bst.pre_order()
    expected = [11, 10, 12]
    actual = []
    for num in pre:
        actual.append(num.value)
    print('actual: {}'.format(actual))
    assert actual == expected


def test_left_balance(make_left_tree):
    b_bst = make_left_tree
    pre = b_bst.pre_order()
    expected = [9, 8, 10]
    actual = []
    for num in pre:
        actual.append(num.value)
    print('actual: {}'.format(actual))
    assert actual == expected


def test_tree_balance(make_unbalanced_tree):
    b_bst = make_unbalanced_tree
    pre = b_bst.pre_order()
    expected = [8, 7, 6, 10, 9, 11]
    actual = []
    for num in pre:
        actual.append(num.value)
    print('actual: {}'.format(actual))
    assert actual == expected