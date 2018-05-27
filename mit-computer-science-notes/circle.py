from turtle import *
import math


class Circle():
    def __init__(self, origin, radius):
        self.origin = origin
        self.radius = radius

    def moveOrigin(self, newOrigin, dist=1):
        dist = math.sqrt((origin.x - newOrigin.x)**2 +
                         (origin.y - newOrigin.y)**2)  # 计算两点距离
        xDist = origin.x - newOrigin.x  # 水平距离
        yDist = origin.y - newOrigin.y  # 垂直距离
        ratio = dist / distance
        xMove = abs(xDist) * ratio
        yMove = abs(yDist) * ratio
        if xDist > 0:
            newX = origin.x - xMove
        else:
            newX = origin.x + xMove
        if yDist > 0:
            newY = origin.y - yMove
        else:
            newY = origin.y + yMove
        return (newX, newY)


class Field:
    def __init__(self, long):
        pass


class Point:
    def __init__(self, x, y):
        self.loction = (x, y)

    def move(self, newX, newY):
        self.loction = (newX, newY)
