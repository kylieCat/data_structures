import pytest
from data_structures.queue import Queue


def test_queue():
    q = Queue()
    assert q is not None


def test_enqueue():
    q = Queue()
    q.enqueue(1)
    assert q.head.value == 1
    assert q.head.next is None
    assert q.tail.value == 1
    q.enqueue(2)
    assert q.head.value == 1
    assert q.head.next.value == 2
    assert q.tail.value == 2
    q.enqueue(3)
    assert q.head.value == 1
    assert q.head.next.value == 2
    assert q.tail.value == 3


def test_dequeue_empty():
    with pytest.raises(LookupError):
        Queue().dequeue()


def test_dequeue():
    q = Queue()
    for i in range(1, 4):
        q.enqueue(i)
    assert q.dequeue() == 1
    assert q.dequeue() == 2
    assert q.dequeue() == 3


def test_size():
    q = Queue()
    assert q.size() == 0
    for i in range(1, 4):
        q.enqueue(i)
    assert q.size() == 3
    q.dequeue()
    assert q.size() == 2
    q.dequeue()
    assert q.size() == 1
