from pytest import fixture
from hashtable import HashTable


@fixture(scope='session')
def make_hash_table():
    ht = HashTable(256)
    return ht

@fixture(scope='session')
def get_words():
    with open('/usr/share/dict/words') as words:
        test_words = [line.strip() for line in words]
    return test_words[:255]

def test_hash_table(make_hash_table):
    ht = make_hash_table
    assert isinstance(ht, HashTable)

def test_get_set(make_hash_table, get_words):
    ht = make_hash_table
    for word in get_words:
        ht.set(word, word)
    for word in get_words:
        assert ht.get(word) == word


def test_hash(make_hash_table):
    bt = make_hash_table
    assert bt.hash('abc') == 38
    assert bt.hash('def') == 47