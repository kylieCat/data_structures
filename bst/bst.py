class Node(object):
    def __init__(self, value, l_child=None, r_child=None, parent=None):
        self.value = value
        self.l_child = l_child
        self.r_child = r_child
        self.parent = parent


class BST(object):
    def __init__(self):
        self.root = None
        self._size = 0

    def insert(self, val):
        pass

    def contains(self, val):
        pass

    def size(self):
        pass

    def depth(self):
        pass

    def balance(self):
        pass