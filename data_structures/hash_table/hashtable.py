class HashTable(object):
    def __init__(self, size):
        self.size = size
        self.hash_table = [[] for _ in range(self.size)]

    def hash(self, key):
        total = 0
        for letter in key:
            total += ord(letter)
        if not self.size & self.size - 1:
            total &= self.size - 1
        else:
            total = total % self.size
        return total

    def set(self, key, value):
        key_index = self.hash(key)
        self.hash_table[key_index].append((key, value))

    def get(self, key):
        for item in self.hash_table[self.hash(key)]:
            if item[0] == key:
                return item[1]
        raise KeyError
