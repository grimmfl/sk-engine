import maths
from errors import SkTypeError


class Quaternion:
    def __init__(self, scalar: float, vector: maths.Vector):
        self.scalar: float = scalar
        self.vector: maths.Vector = vector

    def __eq__(self, other) -> bool:
        if isinstance(other, Quaternion):
            return self.scalar == other.scalar and self.vector == other.vector
        return False

    def __str__(self) -> str:
        return f"Quaternion({self.scalar}, {self.vector})"

    def __add__(self, other) -> "Quaternion":
        if isinstance(other, Quaternion):
            return Quaternion(self.scalar + other.scalar, self.vector + other.vector)
        raise SkTypeError(self, other, "+")

    def __iadd__(self, other) -> "Quaternion":
        if isinstance(other, Quaternion):
            self.scalar += other.scalar
            self.vector += other.vector
            return self
        raise SkTypeError(self, other, "+=")

    def __sub__(self, other) -> "Quaternion":
        if isinstance(other, Quaternion):
            return Quaternion(self.scalar - other.scalar, self.vector - other.vector)
        raise SkTypeError(self, other, "-")

    def __isub__(self, other) -> "Quaternion":
        if isinstance(other, Quaternion):
            self.scalar -= other.scalar
            self.vector -= other.vector
            return self
        raise SkTypeError(self, other, "-=")


if __name__ == "__main__":
    q = Quaternion(90, maths.Vector(1, 1, 1))
    print(q)