import sys
from stdlib_python import stdio

E = 1e-15

n = int(sys.argv[1])
k = int(sys.argv[2])

t = n
while abs(t - n / t**(k - 1)) > (t**(k - 1) * E):
    t = (n / t**(k - 1) + t) / 2.0

stdio.writeln(t)
