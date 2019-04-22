#!python

from linkedlist import LinkedList


# Implement LinkedQueue below, then change the assignment at the bottom
# to use this Queue implementation to verify it passes all tests
class LinkedQueue(object):

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue."""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise."""
        return self.list.size == 0

    def length(self):
        """Return the number of items in this queue."""
        return self.list.size

    def enqueue(self, item):
        """Insert the given item at the back of this queue.
        Running time: O(1)"""
        # TODO: Insert given item
        self.list.append(item)

    def front(self):
        """Return the item at the front of this queue without removing it,
        or None if this queue is empty."""
        if(self.is_empty()):
            print("Queue is empty!")
            return None

        return self.list.head.data

    def dequeue(self):
        """Remove and return the item at the front of this queue,
        or raise ValueError if this queue is empty.
        Running time: O(1)"""
        if(self.is_empty()):
            raise ValueError("Queue is empty!")

        to_return = self.list.head.data
        self.list.head = self.list.head.next
        self.list.size -= 1
        return to_return


#Better dynamic array implementation using wrapping and an frontIndex
class WrapArrayQueue(object):

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any."""
        # Initialize a new list (dynamic array) to store the items
        self.frontIndex = 0
        self.lastIndex = 0
        self.size = 0
        self.list = [None] * 8
        if iterable is not None:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue."""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise."""
        return self.size == 0

    def length(self):
        """Return the number of items in this queue."""
        # TODO: Count number of items
        '''if(self.frontIndex > self.lastIndex):
            return len(self.list) - self.frontIndex + self.lastIndex
        else:
            return self.lastIndex - self.frontIndex'''
        return self.size


    def enqueue(self, item):
        """Insert the given item at the back of this queue.
        Running time: O(1)"""
        # TODO: Insert given item

        self.list[self.lastIndex] = item
        self.size += 1
        #if(self.lastIndex == self.frontIndex - 1):
        if(self.size == len(self.list)):
            self.resize()
        else:
            self.lastIndex += 1
            self.lastIndex = self.lastIndex%len(self.list)

    def front(self):
        """Return the item at the front of this queue without removing it,
        or None if this queue is empty."""
        # TODO: Return front item, if any
        if(self.is_empty()):
            print("Queue is empty!")
            return None

        return self.list[self.frontIndex]

    def dequeue(self):
        """Remove and return the item at the front of this queue,
        or raise ValueError if this queue is empty.
        Running time: O(n) as it must shift all elements in list down 1 index"""
        # TODO: Remove and return front item, if any
        if(self.is_empty()):
            raise ValueError("Queue is empty!")

        self.frontIndex += 1
        self.size -= 1
        return self.list[self.frontIndex - 1]

    def resize(self):

        new_list = [None] * (len(self.list) * 2)
        for i in range(len(self.list)):

            new_list[i] = self.list[(i+self.frontIndex)%len(self.list)]

        self.list = new_list
        self.frontIndex = 0
        self.lastIndex = self.size


class ArrayQueue(object):

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any."""
        # Initialize a new list (dynamic array) to store the items
        self.list = list()
        if iterable is not None:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue."""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise."""
        return len(self.list) == 0

    def length(self):
        """Return the number of items in this queue."""
        # TODO: Count number of items
        return len(self.list)

    def enqueue(self, item):
        """Insert the given item at the back of this queue.
        Running time: O(1)"""
        # TODO: Insert given item
        self.list.append(item)

    def front(self):
        """Return the item at the front of this queue without removing it,
        or None if this queue is empty."""
        # TODO: Return front item, if any
        if(self.is_empty()):
            print("Queue is empty!")
            return None

        return self.list[0]

    def dequeue(self):
        """Remove and return the item at the front of this queue,
        or raise ValueError if this queue is empty.
        Running time: O(n) as it must shift all elements in list down 1 index"""
        # TODO: Remove and return front item, if any
        if(self.is_empty()):
            raise ValueError("Queue is empty!")

        return self.list.pop(0)


# Implement LinkedQueue and ArrayQueue above, then change the assignment below
# to use each of your Queue implementations to verify they each pass all tests
# Queue = LinkedQueue
Queue = WrapArrayQueue
