import unittest
from vector import Vector


class VectorTest(unittest.TestCase):

    def test_multiplication_same_vectors(self):
        a = Vector.by_coords(0, 0, 0)
        b = Vector.by_coords(0, 0, 0)
        expected = Vector.by_coords(0, 0, 0)
        self.assertEqual(a * b, expected)

    def test_multiplication_diff_simple_vectors(self):
        a = Vector.by_coords(1, 0, 0)
        b = Vector.by_coords(0, 1, 0)
        expected = Vector.by_coords(0, 0, 1)
        self.assertEqual(a * b, expected)

    def test_multiplication_diff_vectors(self):
        a = Vector.by_coords(1, 1, 0)
        b = Vector.by_coords(2, -3, 6)
        expected = Vector.by_coords(6, -6, -5)
        self.assertEqual(a * b, expected)
