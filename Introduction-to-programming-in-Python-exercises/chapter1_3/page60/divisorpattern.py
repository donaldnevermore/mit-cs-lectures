import sys

# n = int(sys.argv[1])
n = 25

i = 1
while i < n:
    j = 1
    while j < n:
        if (i % j == 0) or (j % i == 0):
            print('* ', end='')
        else:
            print('  ', end='')
        j += 1
    i += 1
    print(i)
