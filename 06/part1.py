GRID_SIZE = 1000
OFFSET = 300

points = []
for line in open('input').read().split('\n'):
  pt = map(int, line.split(', '))
  pt[0] += OFFSET
  pt[1] += OFFSET
  points.append(pt)

def distance(pt1, pt2):
  return abs(pt1[0] - pt2[0]) + abs(pt1[1] - pt2[1])

grid = [[-1] * GRID_SIZE for _ in range(GRID_SIZE)]
for i in range(len(grid)):
  for j in range(len(grid[i])):
    if j == 0 and i % 100 == 0:
      print i
    grid_pt = (i, j)
    min_dist = GRID_SIZE * 2
    closest_pts = []
    for p, point in enumerate(points):
      d = distance(point, grid_pt)
      if d < min_dist:
        min_dist = d
        closest_pts = [p]
      elif d == min_dist:
        closest_pts.append(p)
    if len(closest_pts) == 1:
      grid[i][j] = closest_pts[0]
    elif len(closest_pts) > 1:
      grid[i][j] = -1

#print grid
infinites = set()
for i in range(GRID_SIZE):
  infinites.add(grid[0][i])
  infinites.add(grid[GRID_SIZE - 1][i])
  infinites.add(grid[i][0])
  infinites.add(grid[i][GRID_SIZE - 1])

sizes = [0 for _ in range(len(points))]
for i in range(GRID_SIZE):
  for j in range(GRID_SIZE):
    pt = grid[i][j]
    if pt == -1 or pt in infinites:
      continue
    sizes[pt] += 1
print max(sizes)
print sizes
