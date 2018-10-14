def gcd(x: int, y: int):
    if x % y == 0:
        return y
    else:
        return gcd(y, x % y)


print(gcd(12, 8))
