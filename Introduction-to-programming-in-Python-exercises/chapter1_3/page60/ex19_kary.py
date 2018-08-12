import sys
import stdio


def hex_num(num: int) -> str:
    """
    换成十六进制的数字写法
    :param num: int
    :return: str
    """
    num_to_hex = {
        11: 'A',
        12: 'B',
        13: 'C',
        14: 'D',
        15: 'E',
        16: 'F',
    }
    return num_to_hex[num]


i = int(sys.argv[1])
k = int(sys.argv[2])

assert 16 >= k >= 2, 'k为2到16之间的整数'
v = 1
# 找出小于i的最大k幂级数
while v <= i // k:
    v *= k

while v > 0:
    if i < v:
        stdio.write(i % v)
    else:
        remain = i // v
        if remain >= 11:
            stdio.write(hex_num(remain))
        else:
            stdio.write(remain)
        i -= v * remain
    v //= k
stdio.writeln()
