import math
import sys
from stdlib_python import stdio

a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])
if a == 0:
    stdio.writeln('a不能为0！')
else:
    discriminant = b * b - 4.0 * a * c
    if discriminant < 0:
        stdio.writeln('方程没有解！')
    else:
        d = math.sqrt(discriminant)
        stdio.writeln((-b + d) / (a * 2.0))
        stdio.writeln((-b - d) / (a * 2.0))
