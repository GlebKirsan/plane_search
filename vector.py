from point import Point


class Vector:

    def __init__(self, a: Point, b: Point):
        self.x = b.x - a.x
        self.y = b.y - a.y
        self.z = b.z - a.z

    @classmethod
    def by_coords(cls, x: float, y: float, z: float):
        return cls(Point(0, 0, 0), Point(x, y, z))

    def __repr__(self):
        return f'Vector(x={self.x}, y={self.y}, z={self.z})'

    def __iter__(self):
        return (i for i in (self.x, self.y, self.z))

    def __eq__(self, other: 'Vector'):
        return tuple(self) == tuple(other)

    def __mul__(self, other) -> 'Vector':
        if not isinstance(other, Vector):
            raise ValueError

        return self.by_coords(self.y * other.z - self.z * other.y,
                              self.z * other.x - self.x * other.z,
                              self.x * other.y - self.y * other.x)
