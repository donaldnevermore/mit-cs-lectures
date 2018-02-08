import sys

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

arr = None
minimum = min(a, b)
maximum = max(a, b)
if c <= minimum:
    arr = (c, minimum, maximum)
elif c > minimum and c < maximum:
    arr = (minimum, c, maximum)
else:
    arr = (minimum, maximum, c)


print(arr)
