# Write a class Shape with an abstract method area(). Create two subclasses Circle and 
# Square that override the area() method. Instantiate both and print their areas.

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base shape with an area() contract."""

    @abstractmethod
    def area(self) -> float:
        """Return the area of the shape."""
        raise NotImplementedError


class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return math.pi * (self.radius ** 2)


class Square(Shape):
    def __init__(self, side: float):
        self.side = side

    def area(self) -> float:
        return self.side ** 2


if __name__ == "__main__":
    c = Circle(3)
    s = Square(4)

    print(f"Circle with radius 3 area: {c.area():.6f}")
    print(f"Square with side 4 area: {s.area():.6f}")