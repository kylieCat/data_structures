import pytest
import timeit
from insertion import insertion_sort
from random import randint

@pytest.fixture(scope='session')
def random_list():
    return [randint(1, 50) for _ in range(10)]


def test_insertion_sort(random_list):
    pass