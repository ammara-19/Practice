from Point import Point
from Circle import Circle

center = Point()
center.set_XY (3,4)

circle = Circle (center, 5)
print ("Original Circle:")
print (circle)

c, r = circle.get_circle()

print (f"Area: {circle.area(): .2f}")
print (f"Circumference: {circle.circumference(): .2f}")

c.set_XY (6,8)
new_radius = 10
circle.set_circle(c, new_radius)

print ("\nUpdated Circle")
print (circle)
print (f"Area: {circle.area(): .2f}")
print (f"Circumference: {circle.circumference(): .2f}")