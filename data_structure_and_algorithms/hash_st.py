import stdio
import stdarray


class SymboTable:
    def __init__(self, m=1024):
        self.m = m
        self.keys = stdarray.create2D(m, 0)
        self.vals = stdarray.create2D(m, 0)

    def __getitem__(self, key):
        i = hash(key) % self.m

        for j in range(len(self.keys[i])):
            if self.keys[i][j] == key:
                return self.vals[i][j]

        raise KeyError

    def __setitem__(self, key, val):
        i = hash(key) % self.m

        for j in range(len(self.keys[i])):
            if self.keys[i][j] == key:
                self.vals[i][j] = val
                return

        self.keys[i] += [key]
        self.vals[i] += [val]
