import sys
import math

x=float(sys.argv[1])
y=float(sys.argv[2])

p=math.sqrt(x*x+y*y)
s=math.atan2(y,x)

polar=(p,s)
print(polar)