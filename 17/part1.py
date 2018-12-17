grid = [['.' for _ in range(620)] for _ in range(1900)]

x_max, y_min, y_max = 0, 1000, 0
for line in open('input').read().split('\n'):
  first, second = line.split(', ')
  if first[0] == 'x':
    x = int(first[2:])
    y1, y2 = map(int, second[2:].split('..'))
    for y in range(y1, y2 + 1):
      grid[y][x] = '#'
    x_max = max(x_max, x)
    y_min = min(y_min, y1)
    y_max = max(y_max, y2)
  elif first[0] == 'y':
    y = int(first[2:])
    x1, x2 = map(int, second[2:].split('..'))
    for x in range(x1, x2 + 1):
      grid[y][x] = '#'
    x_max = max(x_max, x2)
    y_min = min(y_min, y)
    y_max = max(y_max, y)

print x_max, y_min, y_max

def write_grid(filename='grid', y=None):
  # if y and y > 1860:
  #   _ = raw_input('enter')
  # else:
  #   return
  f = open(filename, 'w')
  for row in grid:
    f.write(''.join(row))
    f.write('\n')
  f.close()

def fill(y, x, falling):
  print 'fill y={},x={}'.format(y, x)
  if grid[y][x] not in 'w.':
    write_grid()
    raise Exception('Should be water or clay y={},x={}'.format(y, x))

  count = 0

  if grid[y][x] == '.':
    grid[y][x] = 'w'
    count += 1
  right_wall = None
  for nx in range(x+1, x_max+1):
    if grid[y][nx] == 'w':
      if grid[y+1][nx - 1] == '#' and grid[y+1][nx-2] == 'w' and grid[y][nx+1] == '.':
        break
      continue
    if grid[y][nx] == '.':
      grid[y][nx] = 'w'
      count += 1
    elif grid[y][nx] == '#':
      right_wall = nx
      break
    if grid[y+1][nx] == '.':
      falling.append((nx, y+1))
      break
  left_wall = None
  for nx in range(x - 1, -1, -1):
    if grid[y][nx] == 'w':
      if grid[y+1][nx + 1] == '#' and grid[y+1][nx+2] == 'w' and grid[y][nx-1] == '.':
        break
      continue
    if grid[y][nx] == '.':
      grid[y][nx] = 'w'
      count += 1
      if grid[y+1][nx] == '.':
        falling.append((nx, y+1))
        break
    if grid[y][nx] == '#':
      left_wall = nx
      break
  # write_grid(y=y)

  if left_wall and right_wall:
    count += fill(y - 1, x, falling)

  # print left_wall, right_wall
  # write_grid()
  # raise Exception()

  return count

falling = [(500, 0)]
count = 0
while len(falling) > 0:
  x, y = falling.pop(0)
  if y > y_max:
    continue
  if grid[y][x] == 'w':
    falling.append((x, y+1))
    continue
  print 'falling y={},x={}'.format(y, x)
  # write_grid(y=y)

  if grid[y][x] == '.':
    if y_min <= y <= y_max:
      grid[y][x] = 'w'
      count += 1
    falling.append((x, y+1))
  elif grid[y][x] == '#':
    count += fill(y-1, x, falling)

print count
write_grid()
