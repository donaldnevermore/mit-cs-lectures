"""随机移动问题"""

import math
import random
import pylab


class Location:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def move(self, xc, yc):
        return Location(self.x + float(xc), self.y + float(yc))

    def get_coords(self):
        return self.x, self.y

    def get_dist(self, other):
        ox, oy = other.get_coords()
        x_dist = self.x - ox
        y_dist = self.y - oy
        return math.sqrt(x_dist ** 2 + y_dist ** 2)


class CompassPt:
    possibles = ('N', 'S', 'E', 'W')

    def __init__(self, pt):
        if pt in self.possibles:
            self.pt = pt
        else:
            raise ValueError("inCompassPt.__init__")

    def move(self, dist):
        if self.pt == 'N':
            return 0, dist
        elif self.pt == 'S':
            return 0, -dist
        elif self.pt == 'E':
            return dist, 0
        elif self.pt == 'W':
            return -dist, 0
        else:
            raise ValueError("in  CompassPt.move")


class Field:
    def __init__(self, drunk, loc):
        self.drunk = drunk
        self.loc = loc

    def move(self, cp, dist):
        old_loc = self.loc
        xc, yc = cp.move(dist)
        self.loc = old_loc.move(xc, yc)

    def get_loc(self):
        return self.loc

    def get_drunk(self):
        return self.drunk


class Drunk:
    def __init__(self, name):
        self.name = name

    def move(self, field, time=1):
        if field.get_drunk() != self:
            raise ValueError("Drunk.move called with drunk not in field")
        for i in range(time):
            pt = CompassPt(random.choice(CompassPt.possibles))
            field.move(pt, 1)  # Drunk moves a step


def perform_trial(time, f):
    start = f.get_loc()
    distances = [0.0]
    for t in range(1, time + 1):
        f.get_drunk().move(f)
        new_loc = f.get_loc()
        distance = new_loc.get_dist(start)
        distances.append(distance)
    return distances


drunk = Drunk("Homer Simpson")
for i in range(3):
    f = Field(drunk, Location(0, 0))
    distances = perform_trial(500, f)
    pylab.plot(distances)
pylab.title("Homer\'s Random Walk")
pylab.xlabel("Time")
pylab.ylabel("Distance from Origin")


def perform_sim(time, num_trials):
    dist_lists = []
    for trial in range(num_trials):
        d = Drunk("Drunk" + str(trial))
        f = Field(d, Location(0, 0))
        distances = perform_trial(time, f)
        dist_lists.append(distances)
    return dist_lists


def ans_quest(max_time, num_trials):
    means = []
    dist_lists = perform_sim(max_time, num_trials)
    for t in range(max_time + 1):
        tot = 0.0
        for dist_l in dist_lists:
            tot += dist_l[t]
        means.append(tot / len(dist_lists))
    pylab.figure()
    pylab.plot(means)
    pylab.xlabel("distance")
    pylab.ylabel("time")
    pylab.title("Average Distance  vs. Time (" + str(len(dist_lists)) +
                "trials)")


ans_quest(500, 300)
pylab.show()
