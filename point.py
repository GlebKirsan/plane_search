class Point:

    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self) -> str:
        return f'Point(x={self.x}, y={self.y}, z={self.z})'
