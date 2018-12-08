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

grid = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]
for i in range(len(grid)):
  for j in range(len(grid[i])):
    if j == 0 and i % 100 == 0:
      print i
    grid_pt = (i, j)
    total_distance = 0
    for point in points:
      total_distance += distance(point, grid_pt)
      if total_distance >= 10000:
        break
    if total_distance < 10000:
      grid[i][j] = 1

# Verify that the edges are not in the region
for i in range(GRID_SIZE):
  if (grid[0][i] == 1 or
      grid[GRID_SIZE - 1][i] == 1 or
      grid[i][0] == 1 or
      grid[i][GRID_SIZE - 1] == 1):
    print 'TOO SMALL'

region_size = 0
for i in range(GRID_SIZE):
  for j in range(GRID_SIZE):
    if grid[i][j]:
      region_size += 1

print region_size
