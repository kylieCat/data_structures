import os
import pytest
from data_structures.hash_table.hashtable import HashTable


@pytest.fixture(scope='session')
def make_hash_table():
    ht = HashTable(256)
    return ht


def get_words():
    with open(os.path.join(os.path.dirname(__file__), 'words.txt')) as words:
        for line in words:
            yield line.strip()


def test_hash_table(make_hash_table):
    ht = make_hash_table
    assert isinstance(ht, HashTable)


def test_get_set(make_hash_table):
    ht = make_hash_table
    for word in get_words():
        ht.set(word, word)
    for word in get_words():
        assert ht.get(word) == word


def test_hash(make_hash_table):
    bt = make_hash_table
    assert bt.hash('abc') == 38
    assert bt.hash('def') == 47