class Point:
    def __init__ (self, x = 0, y = 0):
        self.x = x
        self.y = y

    def set_XY (self, x, y):
        self.x = x
        self.y =y

    def get_XY (self):
        return self.x, self.y

    def __str__(self):
        return f"({self.x}, {self.y})"