import sys

x = float(sys.argv[1])
y = float(sys.argv[2])
z = float(sys.argv[3])

if x < y < z or x > y > z:
    print(True)
else:
    print(False)
