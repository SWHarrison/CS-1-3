#!python

from recursion import factorial
from perm_of_n import permutation
import unittest


class RecursionTest(unittest.TestCase):
    def test_permutation_with_small_integers(self):
        assert permutation(1) == [[1]]
        assert permutation(2) == [[1,2],[2,1]]
        assert permutation(3) == [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

    def test_permutation_by_length_with_small_integers(self):
        assert len(permutation(5)) == factorial(5)
        assert len(permutation(6)) == factorial(6)
        assert len(permutation(7)) == factorial(7)

    def test_permutation_by_length_with_small_integers_pick_k(self):
        assert len(permutation(5,3)) == (factorial(5)/factorial(5-3))
        assert len(permutation(6,4)) == (factorial(6)/factorial(6-4))
        assert len(permutation(7,2)) == (factorial(7)/factorial(7-2))


    def test_permutation_with_small_integers_with_floating_point_numbers(self):
        # permutation should raise a ValueError for non-integer n
        with self.assertRaises(ValueError, msg='function undefined for float'):
            permutation(2.0)
            permutation(3.14159)

    def test_permutation_with_negative_integers(self):
        # permutation should raise a ValueError for n < 0
        with self.assertRaises(ValueError, msg='function undefined for n < 0'):
            permutation(-1)
            permutation(-5)



if __name__ == '__main__':
    unittest.main()
