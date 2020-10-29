import unittest

from point import Point
from plane import Plane

from main import get_plane_coefficients_by_three_points


class MainTest(unittest.TestCase):

    def test_get_plane(self):
        points_set = [[Point(-3, 2, -1), Point(-1, 2, 4), Point(3, 3, -1)],
                      [Point(5, -8, -2), Point(1, -2, 0), Point(-1, 1, 1)]]
        expected_set = [Plane(-5, 30, 2, -73),
                        Plane(0, 0, 0, 0)]
        for i in range(len(points_set)):
            a = points_set[i][0]
            b = points_set[i][1]
            c = points_set[i][2]
            expected = expected_set[i]
            with self.subTest(a=a, b=b, c=c, expected=expected):
                self.assertEqual(
                    get_plane_coefficients_by_three_points(a, b, c),
                    expected)
