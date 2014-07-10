class HashTable(object):

    def __init__(self, size):
        self.size = size
        self.hash_table = [[] for i in range(self.size)]

    def hash(self, key):
        sum = 0
        for letter in key:
            sum += ord(letter)

        if self.size & (self.size - 1) == 0:
            sum = sum & (self.size - 1)
        else:
            sum = sum % self.size
        return sum

    def set(self, key, value):
        key_index = self.hash(key)
        self.hash_table[key_index].append(value)

    def get(self, key):
        return self.hash_table[self.hash(key)]


