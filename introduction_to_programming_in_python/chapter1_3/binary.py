import sys
import stdio

n = int(sys.argv[1])

v = 1
# 找到小于n的最大的2的幂级数
while v <= n // 2:
    v *= 2

while v > 0:
    if n < v:
        # 余下0
        stdio.write(0)
    # n >= v 就是换成二进制的最高位的数字
    else:
        # 余下1
        stdio.write(1)
        # n - v之后继续找最高位的数字
        n -= v * 1
    # 继续找次高位的数字，然后递归
    v //= 2
stdio.writeln()
