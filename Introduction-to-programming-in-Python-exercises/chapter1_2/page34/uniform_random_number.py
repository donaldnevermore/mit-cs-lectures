import random
import math
from functools import reduce

n = 5
numbers = [random.random() for _ in range(n)]
average = reduce(lambda x, y: x + y, numbers) / n
small = min(numbers)
big = max(numbers)

print(numbers)
print(average, small, big)
