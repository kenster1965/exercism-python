"""Simple Linked List"""
class EmptyListException(Exception):
    """Empty List Exception"""

class Node:
    """Node class"""
    def __init__(self, value, next_node=None):
        """Node
            value: value of the node
            next_node: next node
        """
        self._value = value
        self._next = next_node

    def value(self):
        """Return the value of the node"""
        return self._value

    def next(self):
        """Return the next node"""
        return self._next

    def __str__(self):
        """Return the string representation of the node"""
        return f'Node({self._value}, {self._next})'

    def __repr__(self):
        """Return the string representation of the node"""
        return f'Node({self._value}, {self._next})'


class LinkedList:
    """Linked List"""
    def __init__(self, values=None):
        """Linked List
            values: list of values
        """
        self._head = None
        self._len = 0
        if values:
            for value in values:
                self.push(value)

    def __iter__(self):
        """Return the iterator of the linked list"""
        while self._head:
            yield self.pop()

    def __len__(self):
        """Return the length of the linked list"""
        return self._len

    def head(self):
        """Return the head of the linked list"""
        if self._head:
            return self._head
        else:
            raise EmptyListException('The list is empty.')

    def push(self, value):
        """Push a value to the linked list"""
        node = Node(value, self._head)
        self._head = node
        self._len += 1

    def pop(self):
        """Pop a value from the linked list"""
        current_head = self._head
        self._head = self.head().next()
        self._len -= 1
        return current_head.value()

    def reversed(self):
        """Return the reversed linked list"""
        values = list(self)
        values.reverse()
        return values
