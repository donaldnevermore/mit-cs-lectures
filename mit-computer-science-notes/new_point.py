class newPoint:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return '(' + str(self.x) + ',' + str(self.y) + ')'

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == self.y)

    def __add__(self, other):
        return newPoint(self.x + other.x, self.y + other.y)



p1 = newPoint(3.0, 4.0)
p2 = newPoint(2.0,3.0)
print(p1==p2)


