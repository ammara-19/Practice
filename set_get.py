class Car:
    def __init__(self):
        self.brand = ""
        self.color = ""

    def set_brand(self, brand): 
        self.brand = brand
    def set_color(self, color):
        self.color = color

    def get_brand(self):
        return self.brand
    def get_color(self):
        return self.color

car1 = Car() #object
car1.set_brand("Toyota")
car1.set_color("Red")

print("Brand:", car1.get_brand())
print("Color:", car1.get_color())






