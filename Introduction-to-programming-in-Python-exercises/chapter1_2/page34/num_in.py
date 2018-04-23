'''
取a,b两数之间的随机整数
a,b相减，+1就包含上限
取0~1的随机小数差值相乘，加上a,b最小那个
'''
__revision__ = '0.1'

import random
import math
import sys

a=int(sys.argv[1])
b=int(sys.argv[2])

diff= (b+1) - a

for i in range(20):
    rd = math.floor(random.random() * diff + a)  
    print(rd)
