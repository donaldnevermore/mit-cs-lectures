import sys
from enum import Enum

class Weekday(Enum):
    星期日=0
    星期一=1
    星期二=2
    星期三=3
    星期四=4
    星期五=5
    星期六=6

y=int(sys.argv[1])
m=int(sys.argv[2])
d=int(sys.argv[3])

y0=y-(14-m)//12
x=y0+y0//4-y0//100+y0//400
m0=m+12*((14-m)//12)-2
d0=(d+x+(31*m0)//12)%7

print('这一天是{}'.format(Weekday(d0).name))
