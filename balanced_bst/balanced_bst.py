class Node(object):
    def __init__(self, value, l_child=None, r_child=None, parent=None):
        self.value = value
        self.l_child = l_child
        self.r_child = r_child
        self.parent = parent
        self.balance_factor = 0

    def __repr__(self):
        return '<value: {node.value}>'.format(node=self)

    def _find_min(self):
        current_node = self
        while current_node.l_child:
            current_node = current_node.l_child
        return current_node

    def _replace_parent(self, new_value=None):
        if self.parent:
            if self == self.parent.l_child:
                self.parent.l_child = new_value
            else:
                self.parent.r_child = new_value
        if new_value:
            new_value.parent = self.parent

    def _delete_node(self, val):
        if self.l_child and self.r_child:
            successor = self.r_child._find_min()
            self.value = successor.value
            successor._delete_node(successor.value)
        elif self.l_child:
            self._replace_parent(self.l_child)
        elif self.r_child:
            self._replace_parent(self.r_child)
        else:
            self._replace_parent(None)


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
                self.update_balance(node.l_child)
        else:
            if node is self.root:
                self.r_size += 1
            if node.r_child:
                self._insert(val, node.r_child)
            else:
                node.r_child = Node(val, parent=node)
                self.update_balance(node.r_child)

    def update_balance(self, node):

        if node.balance_factor < -1 or node.balance_factor > 1:
            self.rebalance(node)
            return
        if node.parent != None:
            if node.parent.l_child == node:
                node.parent.balance_factor += 1
            elif node.parent.r_child == node:
                node.parent.balance_factor += -1
            if node.parent.balance_factor != 0:
                self.update_balance(node.parent)

    def rotate_left(self, rotation_node):
        new_rotation_node = rotation_node.r_child
        rotation_node.r_child = new_rotation_node.l_child

        if new_rotation_node.l_child != None:
            new_rotation_node.l_child = rotation_node

        new_rotation_node.parent = rotation_node.parent

        if self.root == rotation_node:
            self.root = new_rotation_node
        else:
            if rotation_node.parent.l_child == rotation_node:
                rotation_node.parent.l_child = new_rotation_node
            else:
                rotation_node.r_child = new_rotation_node

        new_rotation_node.l_child = rotation_node
        rotation_node.parent = new_rotation_node

        rotation_node.balance_factor = rotation_node.balance_factor + 1 - min(new_rotation_node.balance_factor, 0)
        new_rotation_node.balance_factor = new_rotation_node.balance_factor + 1 + max(rotation_node.balance_factor, 0)

    def rotate_right(self, rotation_node):
        new_rotation_node = rotation_node.l_child
        rotation_node.l_child = new_rotation_node.r_child

        if new_rotation_node.r_child != None:
            new_rotation_node.r_child = rotation_node

        new_rotation_node.parent = rotation_node.parent

        if self.root == rotation_node:
            self.root = new_rotation_node
        else:
            if rotation_node.parent.r_child == rotation_node:
                rotation_node.parent.r_child = new_rotation_node
            else:
                rotation_node.l_child = new_rotation_node

        new_rotation_node.r_child = rotation_node
        rotation_node.parent = new_rotation_node

        rotation_node.balance_factor = rotation_node.balance_factor + 1 - min(new_rotation_node.balance_factor, 0)
        new_rotation_node.balance_factor = new_rotation_node.balance_factor + 1 + max(rotation_node.balance_factor, 0)

    def rebalance(self, node):
        if node.balance_factor < 0:
            if node.r_child.balance_factor > 0:
                self.rotate_right(node.r_child)
                self.rotate_left(node)
            else:
                self.rotate_left(node)
        elif node.balance_factor > 0:
            if node.l_child.balance_factor < 0:
                self.rotate_left(node.l_child)
                self.rotate_right(node)
            else:
                self.rotate_right(node)

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

    def delete_node(self, val):
        if not self.root:
            return None
        key = self.root
        while key.value != val:
            if val < key.value:
                key = key.l_child
            else:
                key = key.r_child
        key._delete_node(key)