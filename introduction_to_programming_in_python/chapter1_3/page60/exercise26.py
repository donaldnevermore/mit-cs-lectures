import sys
import stdio

n = 3757208

factor = 2
while factor <= n:
    # 从2开始找因子
    while n % factor == 0:
        n //= factor
        stdio.write(str(factor) + ' ')
    factor += 1

if n > 1:
    stdio.write(n)
stdio.writeln()
