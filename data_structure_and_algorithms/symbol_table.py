class SymbolTable:
    def __init__(self):
        self.keys = []
        self.vals = []

    def __getitem__(self, key):
        for i in range(len(self.keys)):
            if self.keys[i] == key:
                return self.vals[i]

        raise KeyError

    def __setitem__(self, key, val):
        for i in range(len(self.keys)):
            if self.keys[i] == key:
                self.vals[i] == val
                return

        self.keys += [key]
        self.vals += [val]
