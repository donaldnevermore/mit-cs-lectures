class Stack:
    _a: list

    def __init__(self):
        self._a = []

    def is_empty(self):
        return len(self._a) == 0

    def __len__(self):
        return len(self._a)

    def push(self, item):
        self._a += [item]

    def pop(self):
        return self._a.pop()
