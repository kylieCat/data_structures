import pytest
from bst import BST


@pytest.fixtures(scope=function)
def make_bst():
    bst = BST()
    return bst


def test_insert(self, val):
    pass

def test_contains(self, val):
    pass

def test_size(self):
    pass

def test_depth(self):
    pass

def test_balance(self):
    pass