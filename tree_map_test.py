import unittest
from tree_map import TreeMap
# Python 2 and 3 compatibility: unittest module renamed this assertion method
if not hasattr(unittest.TestCase, 'assertCountEqual'):
    unittest.TestCase.assertCountEqual = unittest.TestCase.assertItemsEqual


class TreeMapTest(unittest.TestCase):

    def test_init(self):
        ht = TreeMap()
        assert ht.size == 0

    def test_keys(self):
        ht = TreeMap()
        assert ht.keys() == []
        ht.set('I', 1)
        assert ht.keys() == ['I']
        ht.set('V', 5)
        self.assertCountEqual(ht.keys(), ['I', 'V'])  # Ignore item order
        ht.set('X', 10)
        self.assertCountEqual(ht.keys(), ['I', 'V', 'X'])  # Ignore item order

    def test_values(self):
        ht = TreeMap()
        assert ht.values() == []
        ht.set('I', 1)
        assert ht.values() == [1]
        ht.set('V', 5)
        self.assertCountEqual(ht.values(), [1, 5])  # Ignore item order
        ht.set('X', 10)
        self.assertCountEqual(ht.values(), [1, 5, 10])  # Ignore item order

    def test_items(self):
        ht = TreeMap()
        assert ht.items() == []
        ht.set('I', 1)
        assert ht.items() == [('I', 1)]
        ht.set('V', 5)
        self.assertCountEqual(ht.items(), [('I', 1), ('V', 5)])
        ht.set('X', 10)
        self.assertCountEqual(ht.items(), [('I', 1), ('V', 5), ('X', 10)])

    def test_size(self):
        ht = TreeMap()
        assert ht.size == 0
        ht.set('I', 1)
        assert ht.size == 1
        ht.set('V', 5)
        assert ht.size == 2
        ht.set('X', 10)
        assert ht.size == 3

    def test_contains(self):
        ht = TreeMap()
        ht.set('I', 1)
        ht.set('V', 5)
        ht.set('X', 10)
        assert ht.contains('I') is True
        assert ht.contains('V') is True
        assert ht.contains('X') is True
        assert ht.contains('A') is False

    def test_set_and_get(self):
        ht = TreeMap()
        ht.set('I', 1)
        ht.set('V', 5)
        ht.set('X', 10)
        assert ht.get('I') == 1
        assert ht.get('V') == 5
        assert ht.get('X') == 10
        assert ht.size == 3
        with self.assertRaises(KeyError):
            ht.get('A')  # Key does not exist

    def test_set_twice_and_get(self):
        ht = TreeMap()
        ht.set('I', 1)
        ht.set('V', 4)
        ht.set('X', 9)
        assert ht.size == 3
        ht.set('V', 5)  # Update value
        ht.set('X', 10)  # Update value
        assert ht.get('I') == 1
        assert ht.get('V') == 5
        assert ht.get('X') == 10
        assert ht.size == 3  # Check size is not overcounting

    '''def test_delete(self):
        ht = TreeMap(4)
        ht.set('I', 1)
        ht.set('V', 5)
        ht.set('X', 10)
        assert ht.load == 4
        assert ht.length() == 3
        assert ht.size == 3
        ht.delete('I')
        ht.delete('X')
        assert ht.length() == 1
        assert ht.size == 1
        with self.assertRaises(KeyError):
            ht.delete('X')  # Key no longer exists
        with self.assertRaises(KeyError):
            ht.delete('A')  # Key does not exist
        ht.set('I', 1)
        ht.set('V', 5)
        ht.set('X', 10)
        ht.set('II', 2)
        ht.set('IV', 4)
        ht.set('XI', 11)
        assert ht.length() == 6
        assert ht.size == 6'''



if __name__ == '__main__':
    unittest.main()
