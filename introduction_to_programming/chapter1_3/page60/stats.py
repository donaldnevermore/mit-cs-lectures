import random
import math
import sys
from functools import reduce

n = int(sys.argv[1])
numbers = [random.random() for _ in range(n)]
average = reduce(lambda x, y: x + y, numbers) / n
small = min(numbers)
big = max(numbers)

print(numbers)
print(average, small, big)
