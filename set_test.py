#!python

from set import Set
import unittest


class SetTest(unittest.TestCase):

    def test_init(self):
        s = Set()
        assert s.size() == 0

    def test_init_with_list(self):
        s = Set(['A', 'B', 'C'])
        assert s.size() == 3
        assert s.contains('A') is True

    def test_size(self):
        s = Set(['A', 'B', 'C'])
        assert s.size() == 3
        s.add('D')
        assert s.size() == 4
        s.add('E')
        assert s.size() == 5
        s.add('D')
        assert s.size() == 5
        s.remove('D')
        assert s.size() == 4

    def test_contains(self):
        s = Set(['A', 'B', 'C'])
        assert s.contains('A') is True
        assert s.contains('D') is False
        assert s.contains('E') is False
        s.add('D')
        assert s.contains('A') is True
        assert s.contains('D') is True
        assert s.contains('E') is False
        s.add('E')
        assert s.contains('A') is True
        assert s.contains('D') is True
        assert s.contains('E') is True
        s.remove('B')
        assert s.contains('A') is True
        assert s.contains('D') is True
        assert s.contains('E') is True
        assert s.contains('B') is False

    def test_add(self):
        s = Set()
        assert s.size() == 0
        assert s.contains('A') is False
        assert s.contains('D') is False
        assert s.contains('E') is False
        s.add('D')
        assert s.size() == 1
        assert s.contains('A') is False
        assert s.contains('D') is True
        assert s.contains('E') is False
        s.add('E')
        assert s.size() == 2
        assert s.contains('A') is False
        assert s.contains('D') is True
        assert s.contains('E') is True

    def test_remove(self):
        s = Set(['A', 'B', 'C'])
        assert s.contains('A') is True
        assert s.contains('B') is True
        assert s.contains('C') is True
        s.remove('A')
        assert s.contains('A') is False
        assert s.contains('B') is True
        assert s.contains('C') is True
        s.remove('B')
        assert s.contains('A') is False
        assert s.contains('B') is False
        assert s.contains('C') is True
        s.remove('C')
        assert s.contains('A') is False
        assert s.contains('B') is False
        assert s.contains('C') is False
        with self.assertRaises(KeyError):
            s.remove('A')

    def test_union(self):
        s1 = Set(['A', 'D', 'E'])
        s2 = Set(['A', 'B', 'C'])
        s3 = s1.union(s2)
        assert s3.contains('A') is True
        assert s3.contains('B') is True
        assert s3.contains('C') is True
        assert s3.contains('D') is True
        assert s3.contains('E') is True
        assert s3.size() == 5

    def test_intersection(self):
        s1 = Set(['A', 'D', 'E'])
        s2 = Set(['A', 'B', 'C'])
        s3 = s1.intersection(s2)
        assert s3.contains('A') is True
        assert s3.contains('B') is False
        assert s3.contains('C') is False
        assert s3.contains('D') is False
        assert s3.contains('E') is False
        assert s3.size() == 1

    def test_difference(self):
        s1 = Set(['A', 'D', 'E'])
        s2 = Set(['A', 'B', 'C'])
        s3 = s1.difference(s2)
        assert s3.contains('A') is False
        assert s3.contains('B') is False
        assert s3.contains('C') is False
        assert s3.contains('D') is True
        assert s3.contains('E') is True
        assert s3.size() == 2

    def test_is_subset(self):
        s1 = Set(['A', 'D', 'E'])
        s2 = Set(['A', 'B', 'C'])
        s3 = s1.union(s2)
        s4 = s1.intersection(s2)
        assert s1.is_subset(s2) is False
        assert s1.is_subset(s4) is True
        assert s2.is_subset(s4) is True
        assert s4.is_subset(s1) is False
        assert s4.is_subset(s2) is False
        assert s4.is_subset(s3) is False
        assert s3.is_subset(s3) is True
        assert s3.is_subset(s1) is True
        assert s3.is_subset(s2) is True
        assert s3.is_subset(s4) is True
