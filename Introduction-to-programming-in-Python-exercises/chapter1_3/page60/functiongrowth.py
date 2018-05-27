import math

for i in range(1, 12):
    n = 2 ** i
    print(
        f'{n}\t{math.log2(n)}\t{n}\t{n * math.log(n)}\t{n * n}\t{n * n * n}\t{2**n}'
    )
