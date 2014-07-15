import pytest
import timeit
from insertion import insertion_sort
from random import randint

@pytest.fixture(scope='session')
def random_list():
    return [randint(1, 50) for _ in range(10)]


def test_insertion_sort():
    for _ in range(20):
        test = [randint(1, 50) for _ in range(1000)]
        assert insertion_sort(test) == test.sort()


def test_empty_insertion_sort():
    lst = []
    assert insertion_sort(lst) == lst