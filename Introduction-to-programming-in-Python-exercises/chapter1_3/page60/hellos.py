import sys

lines = int(sys.argv[1])

a = lines % 100 % 10
if a == 1:
    print(str(lines) + 'st Hello!')
elif a == 2:
    print(str(lines) + 'nd Hello!')
elif a == 3:
    print(str(lines) + 'rd Hello!')
else:
    print(str(lines) + 'th Hello!')
