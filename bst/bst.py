class Node(object):
    def __init__(self, value, l_child=None, r_child=None, parent=None):
        self.value = value
        self.l_child = l_child
        self.r_child = r_child
        self.parent = parent

    def __repr__(self):
        return '<value: {node.value}>'.format(node=self)


class BST(object):
    def __init__(self):
        self.root = None
        self.r_size = 0
        self.l_size = 0
        self.l_depth = 0
        self.r_depth = 0
        self._size = self.l_size + self.r_size

    def insert(self, val):
        if self.contains(val):
            return
        if self.root is None:
            self.root = Node(val)
            self._size += 1
        else:
            self._insert(val, self.root)

    def _insert(self, val, current_node):
        node = current_node
        if val < node.value:
            if node is self.root:
                self.l_size += 1
            if node.l_child:
                self._insert(val, node.l_child)
            else:
                node.l_child = Node(val, parent=node)
        else:
            if node is self.root:
                self.r_size += 1
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

    def depth(self, node, max_depth=0):
        if node is None:
            return max_depth
        return max(self.depth(node.l_child, max_depth+1), self.depth(node.r_child, max_depth+1))

    def balance(self):
        return self.depth(self.root.l_child, max_depth=1) - self.depth(self.root.r_child, max_depth=1)

    def in_order(self):
        parent_stack = []
        node = self.root
        while parent_stack or node is not None:
            if node is not None:
                parent_stack.insert(0, node)
                node = node.l_child
            else:
                node = parent_stack.pop(0)
                yield node
                node = node.r_child

    def pre_order(self):
        parent_stack = []
        top = self.root
        while top:
            try:
                yield top
                if top.r_child is not None:
                    parent_stack.insert(0, top.r_child)
                if top.l_child is not None:
                    parent_stack.insert(0, top.l_child)
                top = parent_stack.pop(0)
            except IndexError:
                raise StopIteration

    def post_order(self):
        parent_stack = []
        last_node = None
        node = self.root
        while parent_stack or node is not None:
            if node is not None:
                parent_stack.insert(0, node)
                node = node.l_child
            else:
                peek_node = parent_stack[0]
                if peek_node.r_child is not None and last_node is not peek_node.r_child:
                    node = peek_node.r_child
                else:
                    parent_stack.pop(0)
                    yield peek_node
                    last_node = peek_node

    def level_order(self):
        q = []
        if self.root:
            q.append(self.root)
        else:
            return
        while q:
            node = q.pop(0)
            yield node
            if node.l_child is not None:
                q.append(node.l_child)
            if node.r_child is not None:
                q.append(node.r_child)
