#! /usr/bin/python

class Node(object):
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)

class LinkedList(object):
    def __init__(self, head=None, tail=None, length=0):
        self.head = head
        self.length = length

    def __repr__(self):
        node = self.head
        disp = ''
        while node:
            if node.next:
                disp += '{}, '.format(node)
            else:
                disp += '{}'.format(node)
            node = node.next
        return u'({})'.format(disp)

    def insert(self, val):
        """ Insert val at the head of the list """
        val.next = self.head
        self.head = val
        self.length += 1

    def pop(self):
        """ return the first value from the list raises a LookupError on empty lists """
        if self.head:
            return self.head
        else:
            print('Cannot pop from empty list')
            raise LookupError()

    def size(self):
        """ Returns the number of items in a list """
        return self.length

    def search(self, val):
        """ Returns val if it's in the list otherwise returns None """
        node = self.head
        while node:
            if node.value == val:
                return val
            node = node.next
        return node

    def remove(self, node):
        """ Removes given node from the list, node must be in list """
        element = self.head
        prev = None
        while element:
            if element is node:
                if element is self.head:
                    self.head = element.next
                if prev:
                    prev.next = element.next
                element.next = None
                self.length -= 1
                return
            prev = element
            element = element.next
        return u'Node not in list'

    def display(self):
        return self.__repr__()
