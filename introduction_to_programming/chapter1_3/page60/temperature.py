import sys

t = float(sys.argv[1])
v = float(sys.argv[2])

if t >= 50 or v > 120 or t < 3:
    print('公式不成立！')
else:
    wind_chill = 35.74 + 0.6215 * t + (0.4275 * t - 35.75) * (v**0.16)
    print(wind_chill)