from vector import Vector
from point import Point


class Plane:

    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    @classmethod
    def by_norm_vector_and_point(cls, n: Vector, p: Point):
        d = -(n.x * p.x + n.y * p.y + n.z * p.z)
        return cls(n.x, n.y, n.z, d)

    def __repr__(self):
        return f'Plane(a={self.a}, b={self.b}, c={self.c}, d={self.d})'

    def __iter__(self):
        return (i for i in (self.a, self.b, self.c, self.d))

    def __eq__(self, other: 'Plane'):
        return tuple(self) == tuple(other)
