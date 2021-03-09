import sys

a = float(sys.argv[1])
b = float(sys.argv[2])

if 1.0 >= a >= 0:
    if 1.0 >= b >= 0:
        print('True')
    else:
        print('False')
else:
    print('False')