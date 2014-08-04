import pytest
from data_structures.binary_heap.binary_heap import BinaryHeap


@pytest.fixture(scope='function')
def populated_heap():
    heap = BinaryHeap()
    for val in [2, 20, -12, 223, 12, -2]:
        heap.push(val)
    return heap


def test_empty_binary_heap():
    heap = BinaryHeap()
    with pytest.raises(IndexError):
        heap.pop()


def test_binary_heap_push():
    heap = BinaryHeap()
    for val in [2, 20, -12, 223, 12, -2]:
        heap.push(val)
    assert heap.values == [223, 20, -2, 2, 12, -12]


def test_binary_heap_pop(populated_heap):
    heap = populated_heap
    heap.pop()
    heap.pop()
    assert heap.values == [12, 2, -2, -12]