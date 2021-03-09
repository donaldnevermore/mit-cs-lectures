from math import acos, sin, cos, degrees, radians
import sys

x1 = float(sys.argv[1])
y1 = float(sys.argv[2])
x2 = float(sys.argv[3])
y2 = float(sys.argv[4])

# python use radians
dx1 = radians(x1)
dy1 = radians(y1)
dx2 = radians(x2)
dy2 = radians(y2)

# the formula use degrees
distance = 60*degrees(acos(sin(dx1)*sin(dx2)+cos(dx1)*cos(dx2)*cos(dy1-dy2)))

print(f'{distance} nautical miles')
