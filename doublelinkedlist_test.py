#!python

from doublelinkedlist import DoubleLinkedList, Node
import unittest


class NodeTest(unittest.TestCase):

    def test_init(self):
        data = 'ABC'
        node = Node(data)
        assert node.data is data
        assert node.next is None


class DoubleLinkedListTest(unittest.TestCase):

    def test_init(self):
        ll = DoubleLinkedList()
        assert ll.head is None
        assert ll.tail is None
        assert ll.size == 0

    def test_init_with_list(self):
        ll = DoubleLinkedList(['A', 'B', 'C'])
        assert ll.head.data == 'A'  # first item
        assert ll.tail.data == 'C'  # last item
        assert ll.size == 3

    def test_items(self):
        ll = DoubleLinkedList()
        assert ll.items() == []
        ll.append('B')
        assert ll.items() == ['B']
        ll.prepend('A')
        assert ll.items() == ['A', 'B']
        ll.append('C')
        assert ll.items() == ['A', 'B', 'C']

    def test_length(self):
        ll = DoubleLinkedList()
        assert ll.length() == 0
        # append and prepend operations increase length
        ll.append('B')
        assert ll.head.previous == None
        assert ll.head.next == None
        assert ll.tail.previous == None
        assert ll.tail.next == None
        assert ll.length() == 1
        ll.prepend('A')
        assert ll.head.previous == None
        assert ll.head.next.data == 'B'
        assert ll.tail.previous.data == 'A'
        assert ll.tail.next == None
        assert ll.length() == 2
        ll.append('C')
        assert ll.head.previous == None
        assert ll.head.next.data == 'B'
        assert ll.tail.previous.data == 'B'
        assert ll.tail.next == None
        assert ll.length() == 3
        # delete operations decrease length
        ll.delete('B')
        assert ll.head.previous == None
        assert ll.head.next.data == 'C'
        assert ll.tail.previous.data == 'A'
        assert ll.tail.next == None
        assert ll.length() == 2
        ll.delete('C')
        assert ll.head.previous == None
        assert ll.head.next == None
        assert ll.tail.previous== None
        assert ll.tail.next == None
        assert ll.length() == 1
        ll.delete('A')
        assert ll.head == None
        assert ll.head == None
        assert ll.length() == 0

    def test_size(self):
        ll = DoubleLinkedList()
        assert ll.size == 0
        # append and prepend operations increment size
        ll.append('B')
        assert ll.size == 1
        ll.prepend('A')
        assert ll.size == 2
        ll.append('C')
        assert ll.size == 3
        # delete operations decrement size
        ll.delete('B')
        assert ll.size == 2
        ll.delete('C')
        assert ll.size == 1
        ll.delete('A')
        assert ll.size == 0

    def test_get_at_index(self):
        ll = DoubleLinkedList(['A', 'B', 'C'])
        assert ll.get_at_index(0) == 'A'  # head item
        assert ll.get_at_index(1) == 'B'  # middle item
        assert ll.get_at_index(2) == 'C'  # tail item
        with self.assertRaises(ValueError):
            ll.get_at_index(3)  # index too high
        with self.assertRaises(ValueError):
            ll.get_at_index(-1)  # index too low

    def test_insert_at_index(self):
        ll = DoubleLinkedList()
        ll.insert_at_index(0, 'B')  # append('B')
        assert ll.head.data == 'B'  # new head (at index 0)
        assert ll.tail.data == 'B'  # new tail (at index 0)
        assert ll.size == 1
        ll.insert_at_index(0, 'A')  # prepend('A')
        assert ll.head.data == 'A'  # new head (at index 0)
        assert ll.tail.data == 'B'  # unchanged (now at index 1)
        assert ll.size == 2
        assert ll.head.next.data  == 'B'
        assert ll.tail.previous.data  == 'A'
        ll.insert_at_index(2, 'D')  # append('D')
        assert ll.head.data == 'A'  # unchanged (at index 0)
        assert ll.tail.data == 'D'  # new tail (now at index 2)
        assert ll.size == 3
        assert ll.head.next.data  == 'B'
        assert ll.tail.previous.data  == 'B'
        ll.insert_at_index(2, 'C')  # insert 'C' between 'B' and 'D'
        assert ll.head.data == 'A'  # unchanged (at index 0)
        assert ll.tail.data == 'D'  # unchanged (now at index 3)
        assert ll.size == 4
        assert ll.head.next.data  == 'B'
        assert ll.tail.previous.data  == 'C'
        with self.assertRaises(ValueError):
            ll.insert_at_index(5, 'X')  # index too high
        with self.assertRaises(ValueError):
            ll.insert_at_index(-1, 'Y')  # index too low

    def test_append(self):
        ll = DoubleLinkedList()
        ll.append('A')
        assert ll.head.data == 'A'  # new head
        assert ll.tail.data == 'A'  # new tail
        assert ll.size == 1
        ll.append('B')
        assert ll.head.data == 'A'  # unchanged
        assert ll.tail.data == 'B'  # new tail
        assert ll.size == 2
        assert ll.head.next.data  == 'B'
        assert ll.tail.previous.data  == 'A'
        ll.append('C')
        assert ll.head.data == 'A'  # unchanged
        assert ll.tail.data == 'C'  # new tail
        assert ll.size == 3
        assert ll.head.next.data  == 'B'
        assert ll.tail.previous.data  == 'B'

    def test_prepend(self):
        ll = DoubleLinkedList()
        ll.prepend('C')
        assert ll.head.data == 'C'  # new head
        assert ll.tail.data == 'C'  # new head
        assert ll.size == 1
        ll.prepend('B')
        assert ll.head.data == 'B'  # new head
        assert ll.tail.data == 'C'  # unchanged
        assert ll.size == 2
        assert ll.head.next.data  == 'C'
        assert ll.tail.previous.data  == 'B'
        ll.prepend('A')
        assert ll.head.data == 'A'  # new head
        assert ll.tail.data == 'C'  # unchanged
        assert ll.size == 3
        assert ll.head.next.data  == 'B'
        assert ll.tail.previous.data  == 'B'

    def test_find(self):
        ll = DoubleLinkedList(['A', 'B', 'C'])
        assert ll.find(lambda item: item == 'B') == 'B'
        assert ll.find(lambda item: item < 'B') == 'A'
        assert ll.find(lambda item: item > 'B') == 'C'
        assert ll.find(lambda item: item == 'X') is None

    def test_replace(self):
        ll = DoubleLinkedList(['A', 'B', 'C'])
        ll.replace('A', 'D')
        assert ll.head.data == 'D'  # new head
        assert ll.tail.data == 'C'  # unchanged
        assert ll.size == 3
        ll.replace('B', 'E')
        assert ll.head.data == 'D'  # unchanged
        assert ll.tail.data == 'C'  # unchanged
        assert ll.size == 3
        ll.replace('C', 'F')
        assert ll.head.data == 'D'  # unchanged
        assert ll.tail.data == 'F'  # new tail
        assert ll.size == 3
        with self.assertRaises(ValueError):
            ll.replace('X', 'Y')  # item not in list

    def test_delete(self):
        ll = DoubleLinkedList(['A', 'B', 'C'])
        ll.delete('A')
        assert ll.head.data == 'B'  # new head
        assert ll.tail.data == 'C'  # unchanged
        assert ll.size == 2
        ll.delete('C')
        assert ll.head.data == 'B'  # unchanged
        assert ll.tail.data == 'B'  # new tail
        assert ll.size == 1
        ll.delete('B')
        assert ll.head is None  # new head
        assert ll.tail is None  # new head
        assert ll.size == 0
        with self.assertRaises(ValueError):
            ll.delete('X')  # item not in list


if __name__ == '__main__':
    unittest.main()
