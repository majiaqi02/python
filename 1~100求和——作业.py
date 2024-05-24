from functools import reduce

total = reduce(lambda x, y: x + y, range(1, 101))
print(total)