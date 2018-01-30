import sys
import math

t=int(sys.argv[1])
p=float(sys.argv[2])
r=float(sys.argv[3])

interest=p*(math.e**(r*t))

print(interest)
