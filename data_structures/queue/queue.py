class Node(object):
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)


class Queue(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0
        
    def enqueue(self, value):
        if not self.head:
            self.head = Node(value)
            self.tail = self.head
        else:
            node = Node(value)
            self.tail.next, self.tail = node, node
        self._size += 1

    def dequeue(self):
        if not self.size():
            raise LookupError()
        else:
            old_head, self.head = self.head, self.head.next
            old_head.next = None
            self._size -= 1
            return old_head.value

    def size(self):
        return self._size
