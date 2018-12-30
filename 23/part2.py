import math
import numpy as np

# (r, x, y, z)
points = []
for line in open('input').read().split('\n'):
  pos_equal, r_equal = line.split(', ')
  x, y, z = map(int, pos_equal[5:-1].split(','))
  r = int(r_equal[2:])
  points.append((r, x, y, z))

def distance(p1, p2):
  return int(abs(p1[1] - p2[1]) + abs(p1[2] - p2[2]) + abs(p1[3] - p2[3]))

def in_range(x, y, z):
  count = 0
  for point in points:
    if distance((0, x, y, z), point) <= point[0]:
      count += 1
  return count

points.sort()

STEP_SIZE = 1000000
def scale_point(p):
  return map(lambda x: x/STEP_SIZE, p)

orig_points = points[:]
points = map(scale_point, points)

mins = map(min, zip(*points))
maxes = map(max, zip(*points))
print mins, maxes

def million():
  grid = np.zeros((maxes[1] - mins[1] + 1, maxes[2] - mins[2] + 1, maxes[3] - mins[3] + 1), np.int32)

  for t, point in enumerate(points):
    print 'm', t
    r, x, y, z, = point
    for i, rx in enumerate(xrange(max(x - r, mins[1]), min(x + r, maxes[1]) + 1)):
      dx = abs(rx - x)
      for j, dy in enumerate(xrange(-(r - dx), r - dx + 1)):
        ry = y + dy
        if ry < mins[2] or ry > maxes[2]:
          continue

        dz = r - abs(dy) - abs(dx)
        for k, rz in enumerate(xrange(z - dz, z + dz + 1)):
          if rz < mins[3] or rz > maxes[3]:
            continue
          grid[rx - mins[1]][ry - mins[2]][rz - mins[3]] += 1

  max_count = grid.max()
  print '--'
  print max_count
  shape = grid.shape
  for x in range(shape[0]):
    for y in range(shape[1]):
      for z in range(shape[2]):
        if grid[x][y][z] == max_count:
          print '{}, {}, {}'.format(x + mins[1], y + mins[2], z + mins[3])

# million()
# max_count = 880
# grid_pos = 55 40 44
points = orig_points[:]
estimate = map(lambda x: x * STEP_SIZE, (55, 40, 44))
# print in_range(*estimate)
# print in_range(54100000, 41000000, 43600000)

max_count = 0
s = STEP_SIZE
while s > 1:
  max_count = 0
  best_pos = None
  print s, estimate
  for x in xrange(estimate[0] - s, estimate[0] + s + 1, s / 10):
    for y in xrange(estimate[1] - s, estimate[1] + s + 1, s / 10):
      for z in xrange(estimate[2] - s, estimate[2] + s + 1, s / 10):
        c = in_range(x,y,z)
        if c > max_count:
          max_count = c
          best_pos = [x, y, z]
        elif c == max_count:
          if x + y + z < sum(best_pos):
            best_pos = [x, y, z]
  print max_count
  estimate = best_pos
  print
  s /= 10
print estimate
print sum(estimate)