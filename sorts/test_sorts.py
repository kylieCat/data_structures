import pytest
import sorts
from random import randint


@pytest.fixture(scope='session')
def random_list():
    return [randint(1, 50) for _ in range(10)]


def test_sorts_insertion():
    for _ in range(20):
        test = [randint(1, 100000) for _ in range(1000)]
        expected = sorted(test)
        sorts.insertion(test)
        assert test == expected


def test_empty_insertion():
    lst = []
    assert sorts.insertion(lst) == lst


def test_single_insertion():
    lst = [randint(1, 50)]
    assert sorts.insertion(lst) == lst


def test_sorts_merge():
    for _ in range(20):
        test = [randint(1, 100000) for _ in range(1000)]
        expected = sorted(test)
        actual = sorts.merge(test)
        assert actual == expected


def test_sorts_quick():
    for _ in range(20):
        test = [randint(1, 50) for _ in range(10)]
        print('test: {}'.format(test))
        expected = sorted(test)
        actual = sorts.quick(test)
        print('actual: {}'.format(actual))
        print('expected: {}'.format(expected))
        assert actual == expected
