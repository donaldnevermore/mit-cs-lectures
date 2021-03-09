class Division:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def div(self):
        return True if self.a % self.b == 0 else False
