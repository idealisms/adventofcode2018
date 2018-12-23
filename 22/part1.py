# TARGET = (10, 10)
# DEPTH = 510
TARGET = (11,722)
DEPTH = 10689

import numpy as np

# Erosion levels
grid = np.zeros((TARGET[0] + 1, TARGET[1] + 1), np.int32)

for x in xrange(TARGET[0] + 1):
  for y in xrange(TARGET[1] + 1):
    gi = 0
    if (x == 0 and y == 0) or (x == TARGET[0] and y == TARGET[1]):
      gi = 0
    elif x == 0:
      gi = y * 48271
    elif y == 0:
      gi = x * 16807
    else:
      gi = grid[x-1][y] * grid[x][y-1]
    grid[x][y] = (gi + DEPTH) % 20183

risk = 0
for x in range(0, TARGET[0] + 1):
  for y in range(0, TARGET[1] + 1):
    risk += grid[x][y] % 3

print 'part1:', risk