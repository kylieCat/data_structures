class Node(object):
    def __init__(self, value, l_child=None, r_child=None, parent=None):
        self.value = value
        self.l_child = l_child
        self.r_child = r_child
        self.parent = parent

    def __repr__(self):
        return '<value: {node.value} - parent: {node.parent} - l_child: {node.l_child} - r_child: {node.r_child}>'.format(node=self)


class BST(object):
    def __init__(self):
        self.root = None
        self._size = 0

    def insert(self, val):
        if self.contains(val):
            return
        if self.root is None:
            self.root = Node(val)
        else:
            self._insert(val, self.root)
        self._size += 1

    def _insert(self, val, current_node):
        node = current_node
        if val < node.value:
            if node.l_child:
                self._insert(val, node.l_child)
            else:
                node.l_child = Node(val, parent=node)
        else:
            if node.r_child:
                self._insert(val, node.r_child)
            else:
                node.r_child = Node(val, parent=node)


    def contains(self, val):
        node = self.root
        while node:
            if node.value == val:
                return True
            if val < node.value:
                node = node.l_child
            else:
                node = node.r_child
        return False


    def size(self):
        return self._size

    def depth(self):
        pass

    def balance(self):
        pass