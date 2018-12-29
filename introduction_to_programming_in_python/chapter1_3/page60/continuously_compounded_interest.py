import sys
import math
# 投资年数
t = int(sys.argv[1])
# 本金
p = float(sys.argv[2])
# 年利率
r = float(sys.argv[3])

interest = p * (math.e**(r * t))

print(interest)

for i in range(1, 13):
    interest = p * math.e**(r * (i / 12))
    print(f'第{i}个月：\t{interest}')
