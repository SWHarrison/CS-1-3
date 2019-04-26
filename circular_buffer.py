class CircularBuffer(object):

    def __init__(self, max_size = 8, iterable = None):
        """Initialize this queue and enqueue the given items, if any."""
        # Initialize a new list (dynamic array) to store the items
        self.frontIndex = 0
        self.lastIndex = 0
        self.size = 0
        self.list = [None] * max_size
        print(max_size)
        print(iterable)
        if iterable is not None:
            for item in iterable:
                print("This is being enqueued",item)
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue."""
        return 'Circular Buffer({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise."""
        return self.size == 0

    def is_full(self):
        """Return True if this queue is empty, or False otherwise."""
        return self.size == len(self.list)

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

        to_return = None
        if(self.is_full()):
            to_return = self.dequeue()

        self.list[self.lastIndex] = item
        self.lastIndex += 1
        self.lastIndex = self.lastIndex%len(self.list)
        self.size += 1
        return to_return

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
        self.frontIndex = self.frontIndex % len(self.list)
        self.size -= 1
        return self.list[self.frontIndex - 1]


if __name__ == '__main__':

    q = CircularBuffer(iterable = ['A','B'])
    print(q)
