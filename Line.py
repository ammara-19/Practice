from Point import Point
class Line:
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end

    def set_points (self, start: Point, end: Point):
        self.start = start
        self.end = end

    def get_points(self):
        return self.start, self.end
    
    def length(self):
        dx = self.end.x - self.start.x
        dy = self.end.y - self.start.y
        return (dx ** 2 + dy ** 2) ** 0.5 #distance formula
    
    def __str__(self):
        return f"Line from {self.start} to {self.end}, Length = {self.length():.2f}"