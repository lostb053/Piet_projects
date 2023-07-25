from typing import Union

class Shape:
    """Calculates the area of a given shape in cm^2"""
    def __init__(self, name: str) -> None:
        self.name = name

    def area(self) -> int:
        return 0


class Rectangle(Shape):
    """Calculates the area of a rectangle in cm^2"""
    def area(self, length: int = 0, width: int = 0) -> int:
        return length*width


class Circle(Shape):
    """Calculates the area of a circle in cm^2"""
    def area(self, radius: int = 0) -> int:
        return 3.14 * (radius ** 2)


def total_area(area: list[int]) -> int:
    """Calculate total area from list of shape areas"""
    totalArea = 0
    for i in area:
         totalArea = totalArea + i
    return totalArea
