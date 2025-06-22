import math

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def __str__(self):
        return f"Rectangle (length={self.length}, width={self.width})"


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * (self.radius ** 2)
    
    def __str__(self):
        return f"Circle (radius={self.radius})"


def print_area(shape):
    print(f"{shape} has area: {shape.area():.2f}")
