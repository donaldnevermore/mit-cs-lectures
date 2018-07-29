import sys
from stdlib_python import stdio

n = 3757208

factor = 2
factor_list = []
while factor * factor <= n:
    # 从2开始找因子
    while n % factor == 0:
        n //= factor
        if factor not in factor_list:
            factor_list.append(factor)
            stdio.write(str(factor) + ' ')
    factor += 1

if n > 1 and n not in factor_list:
    stdio.write(n)
stdio.writeln()
