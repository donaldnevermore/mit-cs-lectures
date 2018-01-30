import sys

t=float(sys.argv[1])
v=float(sys.argv[2])

assert t<50,'公式不成立'
assert v<120 and v>3,'公式不成立'
wind_chill=35.74+0.6215*t+(0.4275*t-35.75)*(v**0.16)

print(wind_chill)