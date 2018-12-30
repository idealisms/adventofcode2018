import math
# (r, x, y, z)
points = []
for line in open('input').read().split('\n'):
  pos_equal, r_equal = line.split(', ')
  x, y, z = map(int, pos_equal[5:-1].split(','))
  r = int(r_equal[2:])
  points.append((r, x, y, z))

def distance(p1, p2):
  return int(abs(p1[1] - p2[1]) + abs(p1[2] - p2[2]) + abs(p1[3] - p2[3]))

points.sort()

in_range = 0
for pt in points:
  if distance(points[-1], pt) <= points[-1][0]:
    in_range += 1

print 'part1:', in_range
