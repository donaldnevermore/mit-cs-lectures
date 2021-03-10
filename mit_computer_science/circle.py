import math


class Circle:
    def __init__(self, origin, radius):
        self.origin = origin
        self.radius = radius

    def move_origin(self, location, distance=1):
        # Calculate the distance.
        dist = math.sqrt(
            (self.origin.x - location.x) ** 2 + (self.origin.y - location.y) ** 2
        )
        x_dist = self.origin.x - location.x  # 水平距离
        y_dist = self.origin.y - location.y  # 垂直距离
        ratio = dist / distance
        x_move = abs(x_dist) * ratio
        y_move = abs(y_dist) * ratio
        if x_dist > 0:
            new_x = self.origin.x - x_move
        else:
            new_x = self.origin.x + x_move
        if y_dist > 0:
            new_y = self.origin.y - y_move
        else:
            new_y = self.origin.y + y_move
        return (new_x, new_y)


class Field:
    def __init__(self, long):
        pass


class Point:
    def __init__(self, x, y):
        self.location = (x, y)

    def move(self, new_x, new_y):
        self.location = (new_x, new_y)
