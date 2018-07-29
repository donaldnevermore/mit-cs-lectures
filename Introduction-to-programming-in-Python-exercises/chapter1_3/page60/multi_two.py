import sys

n = int(sys.argv[1])
if n >= 0:
    for i in range(n + 1):
        pow = 2 ** i
        if pow <= n:
            print(pow)
