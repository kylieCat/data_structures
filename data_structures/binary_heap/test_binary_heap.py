from pytest import raises
from data_structures.binary_heap.binary_heap import BinaryHeap


def test_binary_heap():
    _heap = BinaryHeap()
    
    with raises(IndexError):
        _heap.pop()
    
    _heap.push(2)
    _heap.push(20)
    _heap.push(-12)
    _heap.push(223)
    _heap.push(12)
    _heap.push(-2)
    sorted_list = _heap.values
    
    assert _heap.values == [223, 20, -2, 2, 12, -12]
    
    _heap.pop()
    _heap.pop()
    
    assert _heap.values == [12, 2, -2, -12]