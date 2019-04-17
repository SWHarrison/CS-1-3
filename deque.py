
from doublelinkedlist import DoubleLinkedList


# Implement LinkedQueue below, then change the assignment at the bottom
# to use this deque implementation to verify it passes all tests
class Deque(object):

    def __init__(self, iterable=None):
        """Initialize this deque and enqueue the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = DoubleLinkedList()
        if iterable is not None:
            for item in iterable:
                self.push_back(item)

    def __repr__(self):
        """Return a string representation of this deque."""
        return 'deque({} items, front={} back ={})'.format(self.length(), self.front(), self.back())

    def is_empty(self):
        """Return True if this deque is empty, or False otherwise."""
        return self.list.size == 0

    def length(self):
        """Return the number of items in this deque."""
        return self.list.size

    def push_back(self, item):
        """Insert the given item at the back of this deque.
        Running time: O(1)"""
        # TODO: Insert given item
        self.list.append(item)

    def push_front(self, item):
        """Insert the given item at the front of this deque.
        Running time: O(1)"""
        # TODO: Insert given item
        self.list.prepend(item)

    def front(self):
        """Return the item at the front of this deque without removing it,
        or None if this deque is empty."""
        if(self.is_empty()):
            print("deque is empty!")
            return None

        return self.list.head.data

    def back(self):
        """Return the item at the front of this deque without removing it,
        or None if this deque is empty."""
        if(self.is_empty()):
            print("deque is empty!")
            return None

        return self.list.tail.data

    def pop_front(self):
        """Remove and return the item at the front of this deque,
        or raise ValueError if this deque is empty.
        Running time: O(1)"""
        if(self.is_empty()):
            raise ValueError("deque is empty!")

        to_return = self.list.head.data
        self.list.head = self.list.head.next
        self.list.size -= 1
        return to_return

    def pop_back(self):
        """Remove and return the item at the back of this deque,
        or raise ValueError if this deque is empty.
        Running time: O(1)"""
        if(self.is_empty()):
            raise ValueError("deque is empty!")

        to_return = self.list.tail.data
        self.list.tail = self.list.tail.previous
        self.list.size -= 1
        return to_return
