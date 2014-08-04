#! usr/bin/python


class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __repr__(self):
        return str(self.value)


class DoubleLinkedList(object):
    def __init__(self, *nodes):
        if nodes:
            for node in nodes:
                self.append(node)
        else:
            self.head = None
            self.tail = None
            self._size = 0

    def insert(self, val):
        """ Insert the value ``val`` at the head of the list. """
        if self.head:
            new_head, new_head.next = Node(val), self.head
            self.head.next, self.head = self.head, new_head
        else:
            self.head = self.tail = Node(val)
        self._size += 1

    def append(self, val):
        """ Append the value ``val`` at the tail of the list. """
        if self.head:
            new_tail, new_tail.prev = Node(val), self.tail
            self.tail.next = new_tail
            self.tail = new_tail
        else:
            self.head = self.tail = Node(val)
        self._size += 1

    def pop(self):
        """ Pop the first value off the head of the list and return it. """
        if self.head:
            new_head = self.head.next
            self.head.next = None
            result = self.head.value
            self.head = new_head
            self._size -= 1
            return result
        else:
            raise LookupError

    def shift(self):
        """ Remove the last value from the tail of the list and return it. """
        if self.head:
            new_tail = self.tail.prev
            self.tail.next = None
            result = self.tail.value
            self.tail = new_tail
            self._size -= 1
            return result
        else:
            raise LookupError

    def remove(self, val):
        """ 
        Remove the first instance of 'val' found in the list, starting from
        the head. If 'val' is not present, it will raise a LookupError
        """
        if self.head:
            node = self.head
            while node:
                if node.value == val:
                    node.prev.next, node.next.prev = node.next, node.prev
                    self._size -= 1
                    return True
                node = node.next
            raise LookupError
        else:
            raise LookupError

    def size(self):
        return self._size