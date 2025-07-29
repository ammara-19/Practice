from Point import Point
from Line import Line

A = Point ()
A.set_XY (2,4)

B = Point()
B.set_XY (3,5)

line = Line(A, B)
print ("Original Line:")
print (line)

start, end = line.get_points()

start.set_XY (6,8)
end.set_XY (7,9)
line.set_points (start, end)

print ("\nUpdated Line")
print (line)

