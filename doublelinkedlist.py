class Node():

    def __init__(self, data):
        self.next = None
        self.previous = None
        self.data = data

    def update(self, new_data):
        self.data = new_data

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)

class DoubleLinkedList():

    def __init__(self, items = None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        self.iter = None
        self.size = 0
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format('<- -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def append(self, data):
        # O(1) time as it does not depend on size of list.
        #Adds a new value, commented out chunk does not use tail of list
        '''if(self.length < 1):
            self.head = Node(data)
            self.length += 1
            return

        current = self.head

        while(current.next != None):
            current = current.next

        current.next = Node(data)
        self.length += 1'''

        new_node = Node(data)

        if(self.size == 0):
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node

        self.size += 1

    def prepend(self, data):
        # O(1) time as it does not depend on size of list.

        new_head = Node(data)
        old_head = self.head
        new_head.next = old_head
        self.head = new_head
        self.size += 1

        if(self.size == 1):
            self.tail = self.head
        else:
            old_head.previous = self.head

    def get_at_index(self, index):
        """Return the item at the given index in this linked list, or
        raise ValueError if the given index is out of range of the list size.
        Best case running time: ??? under what conditions? [TODO]
        Worst case running time: ??? under what conditions? [TODO]"""
        # Check if the given index is out of range and if so raise an error
        if not (0 <= index < self.size):
            raise ValueError('List index out of range: {}'.format(index))
        # Find the node at the given index and return its data

        current = self.head
        for i in range(index):
            current = current.next

        return current.data

    def insert_at_index(self, index, item):
        """Insert the given item at the given index in this linked list, or
        raise ValueError if the given index is out of range of the list size.
        Best case running time: ??? under what conditions? [TODO]
        Worst case running time: ??? under what conditions? [TODO]"""

        if(index == 0):
            self.prepend(item)
            return

        if(index == self.size):
            self.append(item)
            return

        # Check if the given index is out of range and if so raise an error
        if not (0 <= index <= self.size):
            raise ValueError('List index out of range: {}'.format(index))
        # TODO: Find the node before the given index and insert item after it

        current = self.head
        for i in range(index-1):
            current = current.next

        current_next = current.next
        new_node = Node(item)
        new_node.next = current_next
        new_node.previous = current
        if(current_next != None):
            current_next.previous = new_node
        current.next = new_node
        self.size += 1

    def find(self, quality):
        # O(n) time as it needs to go through the list

        '''current = self.head

        while(current != None):
            if(current.data == data):
                return current
            current = current.next

        return None'''
        node = self.head
        while node is not None:
            print(node.data)
            if quality(node.data):
                return node.data
            node = node.next
        return None

    def _find_node(self, quality): # Returns node, unlike above which returns data
        # O(n) time as it needs to go through the list
        node = self.head
        while node is not None:
            if quality(node.data):
                return node
            node = node.next
        return None

    def replace(self, old_data, new_data):
        # O(n) time as it needs to go through the list

        print("Replacing " + str(old_data) + " with " + str(new_data))
        node = self._find_node(lambda data : data == old_data)

        if(node != None):
            node.data = new_data
        else:
            raise(ValueError)

    def find_by_index(self, index_to_find):
        # O(n) time as it needs to go through the list

        if(index_to_find > self.size-1):
            print("Index out of Range!")
            return None

        current = self.head
        for i in range(index_to_find):
            current = current.next

        return current

    def print_list(self):
        # O(n) time as it needs to go through the list

        print("Length: " + str(self.size))
        current = self.head
        while(current != None):
            print(current.data)
            current = current.next

    def length(self):
        # O(1) time as it does not depend on size of list.
        return self.size

    def delete(self, data):
        # O(n) time as it needs to go through the list

        #Returns error if empty list
        if(self.size == 0):
            raise(ValueError)

        current = self.head

        #If head is the node to delete
        if(current.data == data):
            if(self.size == 1):
                self.head = None
                self.tail = None
            else:
                self.head = current.next
                current.next = None
                self.head.previous = None
            self.size -= 1
            return

        #Parses through list, and removes the node if it matches data
        while(current != None):
            if(current.data == data):
                current.previous.next = current.next
                if(current != self.tail):
                    current.next.previous = current.previous
                else:
                    self.tail = current.previous
                current.next = None
                current.previous = None
                self.size -= 1
                return

            current = current.next

        raise(ValueError)


    def __iter__(self):
        self.iter = self.head
        return self

    def __next__(self):
        if(self.iter != None):
            data = self.iter
            self.iter = self.iter.next
            return data
        else:
            raise StopIteration

def test_linked_list():
    ll = DoubleLinkedList()
    print(ll)

    print('Appending items:')
    ll.append('A')
    print(ll)
    ll.append('B')
    print(ll)
    ll.append('C')
    print(ll)
    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('size: {}'.format(ll.size))
    print('length: {}'.format(ll.length()))

    print('Getting items by index:')
    for index in range(ll.size):
        item = ll.get_at_index(index)
        print('get_at_index({}): {!r}'.format(index, item))

    print("******")
    for node in ll:
        print("Previous Node is " + str(node.previous))
        print(node)
        print("Next Node is " + str(node.next))
    ll.replace('A', 'D')

    for node in ll:
        print("Previous Node is " + str(node.previous))
        print(node)
        print("Next Node is " + str(node.next))

    print('Deleting items:')
    ll.delete('B')
    print(ll)
    ll.delete('C')
    print(ll)
    ll.delete('D')
    print(ll)
    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('size: {}'.format(ll.size))
    print('length: {}'.format(ll.length()))

    ll.insert_at_index(0,'B')
    for node in ll:
        print("Previous Node is " + str(node.previous))
        print(node)
        print("Next Node is " + str(node.next))
    ll.insert_at_index(0,'A')
    for node in ll:
        print("Previous Node is " + str(node.previous))
        print(node)
        print("Next Node is " + str(node.next))
    ll.insert_at_index(2,'D')
    for node in ll:
        print("Previous Node is " + str(node.previous))
        print(node)
        print("Next Node is " + str(node.next))
    ll.insert_at_index(2,'C')
    for node in ll:
        print("Previous Node is " + str(node.previous))
        print(node)
        print("Next Node is " + str(node.next))

    print(ll)


if __name__ == '__main__':
    test_linked_list()
