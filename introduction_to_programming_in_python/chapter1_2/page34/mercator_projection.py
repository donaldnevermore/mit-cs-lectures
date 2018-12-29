import sys
import math

lam = float(sys.argv[1])
lat = float(sys.argv[2])
lng = float(sys.argv[3])

x = lng - lam
minus = (1 + math.sin(lat)) / (1 - math.sin(lat))
y = 1 / 2 * math.log(minus)

result = (x, y)
print(result)
