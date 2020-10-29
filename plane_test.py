import unittest
from plane import Plane
from vector import Vector
from point import Point


class PlaneTest(unittest.TestCase):

    def test_plane_by_norm_and_point(self):
        n = Vector.by_coords(3, 7, -5)
        point = Point(-1, 2, -3)
        expected = Plane(3, 7, -5, -26)
        self.assertEqual(Plane.by_norm_vector_and_point(n, point), expected)
