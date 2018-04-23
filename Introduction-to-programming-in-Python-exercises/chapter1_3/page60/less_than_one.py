import sys

a = float(sys.argv[1])
b = float(sys.argv[2])

if a <= 1.0 and a >= 0:
    if b <= 1.0 and b >= 0:
        print('True')
    else:
        print('False')
else:
    print('False')