import stddraw

stddraw.setXscale(-1.0, 1.0)
stddraw.setYscale(-1.0, 1.0)

DT = 20.0
RADIUS = 0.05
rx = 0.480
ry = 0.860
vx = 0.015
vy = 0.023

while True:
    # 更新小球的位置，并画出来
    if abs(rx + vx) + RADIUS > 1.0:
        vx = -vx

    if abs(ry + vy) + RADIUS > 1.0:
        vy = -vy

    rx = rx + vx
    ry = ry + vy

    stddraw.clear(stddraw.GRAY)
    stddraw.filledCircle(rx, ry, RADIUS)
    stddraw.show(DT)
