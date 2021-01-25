n = 555
s = ''

while n > 0:
    s = str(n % 10) + s
    n //= 10

print(s, type(s))
