import sys

first = int(sys.argv[1])
second = int(sys.argv[2])
third = int(sys.argv[3])

if first == second and second == third:
    print('equal')
else:
    print('not equal')