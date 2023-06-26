class Rectangle:
    """Calculate area and perimeter, and check if it's a square"""
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width
    
    def get_area(self) -> int:
        area = self.length*self.width
        return area

    def get_perimeter(self) -> int:
        perimeter = 2*(self.length+self.width)
        return perimeter

    def is_square(self) -> bool:
        if self.length == self.width:
            return True
        else:
            return False