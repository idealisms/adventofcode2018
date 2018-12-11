# I overwrote part 1, sorry!

import numpy as np
SERIAL_NUMBER = 6303
grid = [[None for _ in range(300)] for _ in range(300)]

print 'compute grid'
for x in range(1, 301):
  for y in range(1, 301):
    rack_id = x + 10
    power = rack_id * y
    power += SERIAL_NUMBER
    power *= rack_id
    power = (int(power / 100) % 10) - 5
    grid[x-1][y-1] = power

print 'v_powers'
v_powers = np.zeros((300, 300, 301), np.int32)
for x in range(300):
  for y in range(300):
    p = 0
    for le in range(1, 300 - y + 1):
      p += grid[x][y+le-1]
      v_powers[x][y][le] = p

print 'h_powers'
h_powers = np.zeros((300, 300, 301), np.int32)
for y in range(300):
  for x in range(300):
    p = 0
    for le in range(1, 300 - x + 1):
      p += grid[x+le-1][y]
      h_powers[x][y][le] = p

# x, y, size
print 'compute squares'
max_power = 0
max_cell = None
powers = np.zeros((300, 300, 301), np.int32)
for x in range(300):
  for y in range(300):
    for size in range(1, 300 - max(x, y) + 1):
      if size == 1:
        powers[x][y][size] = grid[x][y]
      else:
        power = (
          powers[x][y][size - 1] +
          h_powers[x][y+size-1][size-1]+
          v_powers[x+size-1][y][size-1]+
          grid[x+size-1][y+size-1])
        powers[x][y][size] = power
        if power > max_power:
          max_power = power
          max_cell = (x + 1, y + 1, size)

#print powers[89][268][16]
print max_power
print '{},{},{}'.format(max_cell[0], max_cell[1], max_cell[2])