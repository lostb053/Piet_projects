from typing import Union

class Shape:
    """Calculates the area of a given shape in cm^2"""
    def __init__(self, name: str) -> None:
        self.name = name

    def area(self) -> int:
        return 0


class Rectangle(Shape):
    """Calculates the area of a rectangle in cm^2"""
    def __init__(self, name, length: int = 0, width: int = 0) -> None:
        self.name = name
        self.length = length
        self.width = width

    def area(self) -> int:
        return round(self.length*self.width, 3)


class Circle(Shape):
    """Calculates the area of a circle in cm^2"""
    def __init__(self, name, radius: int = 0) -> None:
        self.name = name
        self.radius = radius

    def area(self) -> int:
        return round(3.14 * (self.radius ** 2), 3)


def total_area(area: list[int]) -> int:
    """Calculate total area from list of shape areas"""
    totalArea = 0
    for i in area:
         totalArea = totalArea + i.area()
    return totalArea
