from point import Point
from vector import Vector
from plane import Plane


def get_plane_coefficients_by_three_points(a: Point, b: Point, c: Point) \
        -> Plane:
    ab = Vector(a, b)
    ac = Vector(a, c)
    n = ab * ac
    return Plane.by_norm_vector_and_point(n, a)
