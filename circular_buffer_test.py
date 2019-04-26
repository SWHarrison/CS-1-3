#!python

from circular_buffer import CircularBuffer
import unittest


class CircularBufferTest(unittest.TestCase):

    def test_init(self):
        q = CircularBuffer()
        assert q.front() is None
        assert q.length() == 0
        assert q.is_empty() is True

    def test_init_with_list(self):
        q = CircularBuffer(max_size = 3,iterable = ['A', 'B', 'C'])
        assert q.front() == 'A'
        assert q.length() == 3
        assert q.is_full() is True
        assert q.is_empty() is False

    def test_length(self):
        q = CircularBuffer(max_size = 2)
        assert q.length() == 0
        q.enqueue('A')
        assert q.length() == 1
        q.enqueue('B')
        assert q.length() == 2
        assert q.is_full() is True
        q.dequeue()
        assert q.front() == 'B'
        assert q.length() == 1
        q.dequeue()
        assert q.front() == None
        assert q.length() == 0

    def test_enqueue(self):
        q = CircularBuffer()
        q.enqueue('A')
        assert q.front() == 'A'
        assert q.length() == 1
        q.enqueue('B')
        assert q.front() == 'A'
        assert q.length() == 2
        q.enqueue('C')
        assert q.front() == 'A'
        assert q.length() == 3
        assert q.is_empty() is False

    def test_front(self):
        q = CircularBuffer()
        assert q.front() is None
        q.enqueue('A')
        assert q.front() == 'A'
        q.enqueue('B')
        assert q.front() == 'A'
        q.dequeue()
        assert q.front() == 'B'
        q.dequeue()
        assert q.front() is None

    def test_dequeue(self):
        q = CircularBuffer(iterable = ['A', 'B', 'C'])
        assert q.dequeue() == 'A'
        assert q.length() == 2
        assert q.dequeue() == 'B'
        assert q.length() == 1
        assert q.dequeue() == 'C'
        assert q.length() == 0
        assert q.is_empty() is True
        with self.assertRaises(ValueError):
            q.dequeue()

    def test_enqueue_full(self):
        q = CircularBuffer(iterable = ['A', 'B', 'C', 'D', 'E', 'F', 'G'])
        assert q.length() == 7
        assert q.enqueue('H') == None
        assert q.length() == 8
        assert q.is_full() is True
        assert q.enqueue('I') == 'A'
        assert q.length() == 8
        assert q.is_full() is True

    def test_dequeue_full(test):
        q = CircularBuffer(iterable = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'])
        assert q.length() == 8
        assert q.is_full() is True
        assert q.dequeue() == 'A'
        assert q.length() == 7
        assert q.is_empty() is False
        assert q.is_full() is False
        assert q.dequeue() == 'B'
        assert q.length() == 6
        assert q.is_empty() is False
        assert q.is_full() is False
        assert q.dequeue() == 'C'
        assert q.length() == 5
        assert q.is_empty() is False
        assert q.is_full() is False
        assert q.dequeue() == 'D'
        assert q.length() == 4
        assert q.is_empty() is False
        assert q.is_full() is False
        assert q.dequeue() == 'E'
        assert q.length() == 3
        assert q.is_empty() is False
        assert q.is_full() is False
        assert q.dequeue() == 'F'
        assert q.length() == 2
        assert q.is_empty() is False
        assert q.is_full() is False
        assert q.dequeue() == 'G'
        assert q.length() == 1
        assert q.is_empty() is False
        assert q.is_full() is False
        assert q.dequeue() == 'H'
        assert q.length() == 0
        assert q.is_empty() is True
        assert q.is_full() is False

    def test_init_max_size_greater_than_iterable(test):
        q = CircularBuffer(max_size = 4,iterable = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'])
        assert q.length() == 4
        assert q.is_empty() is False
        assert q.is_full() is True
        assert q.front() == 'E'

    def test_multiple_enqueue_dequeue(test):
        q = CircularBuffer(max_size = 4,iterable = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'])
        assert q.is_empty() is False
        assert q.is_full() is True
        assert q.dequeue() == 'E'
        assert q.length() == 3
        assert q.is_empty() is False
        assert q.is_full() is False
        assert q.dequeue() == 'F'
        assert q.length() == 2
        assert q.is_empty() is False
        assert q.is_full() is False
        assert q.dequeue() == 'G'
        assert q.length() == 1
        assert q.is_empty() is False
        assert q.is_full() is False
        assert q.dequeue() == 'H'
        assert q.length() == 0
        assert q.is_empty() is True
        assert q.is_full() is False
        assert q.enqueue('I') == None
        q.enqueue('J')
        q.enqueue('K')
        q.enqueue('L')
        assert q.enqueue('M') == 'I'


if __name__ == '__main__':
    unittest.main()
