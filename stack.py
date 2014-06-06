#! /usr/bin/python
class EmptyStack(Exception):
    def __init__(self):
        self.message = 'Stack is empty'
        
    def __str__(self):
        return str(self.message)

class Node(object):
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next
        
    def __repr__(self):
        return str(self.value)
  

class Stack(object):
    def __init__(self, head = None):
        self.head = head
    
    def push(self, data):
        """
        Adds a data element to the stack
        The parameter is the data element to add to the stack.
        """
        data.next = self.head
        self.head = data
    
    def pop(self):
        """
        Removes a data element from the stack and returns the value of that data element.
        """
        if self.head:
            result = self.head.value
            self.head, self.head.next = self.head.next, None
            return result
        else:
            raise EmptyStack()
            
            
            
            
            
            
            
            
            