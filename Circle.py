from Point import Point
import math

class Circle:
    def __init__ (self, center: Point, radius: float):
        self.center = center
        self.radius = radius

    def set_circle (self, center: Point, radius: float):
        self.center = center
        self.radius = radius

    def get_circle (self):
        return self.center, self.radius
    
    def area (self):
        return math.pi * self.radius ** 2
    def circumference (self):
        return 2 * math.pi * self.radius
    
    def __str__ (self):
        return f"Circle with center at {self.center} and radius {self.radius}"