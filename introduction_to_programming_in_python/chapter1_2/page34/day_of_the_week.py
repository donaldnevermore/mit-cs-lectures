import sys

week_day = ['星期日', '星期一', '星期二', '星期三', '星期四', '星期五', '星期六']

y = int(sys.argv[1])
m = int(sys.argv[2])
d = int(sys.argv[3])

y0 = y - (14 - m) // 12
x = y0 + y0 // 4 - y0 // 100 + y0 // 400
m0 = m + 12 * ((14 - m) // 12) - 2
d0 = (d + x + (31 * m0) // 12) % 7

print(f'这一天是{week_day[d0]}')
