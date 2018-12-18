GRID_SIZE = 50 # 10
grid = [['x'] * (GRID_SIZE + 2)]
for line in open('input').read().split('\n'):
  grid.append(['x'] + [_ for _ in line] + ['x'])
grid.append(['x'] * (GRID_SIZE + 2))

def count_symbols(row, col, symbol):
  count = 0
  for r in range(row-1, row+2):
    for c in range(col-1, col+2):
      if r == row and c == col:
        continue
      if grid[r][c] == symbol:
        count += 1
  return count

def mutate(r, c):
  if grid[r][c] == '.':
    if count_symbols(r,c, '|') >= 3:
      return '|'
    else:
      return '.'
  if grid[r][c] == '|':
    if count_symbols(r,c, '#') >= 3:
      return '#'
    else:
      return '|'
  if grid[r][c] == '#':
    if count_symbols(r,c, '#') >= 1 and count_symbols(r,c,'|'):
      return '#'
    else:
      return '.'

def print_grid():
  for line in grid:
    print ''.join(line)

def res_value():
  trees = 0
  lumberyards = 0
  for r in range(1, GRID_SIZE + 1):
    for c in range(1, GRID_SIZE + 1):
      if grid[r][c] == '|':
        trees += 1
      if grid[r][c] == '#':
        lumberyards += 1

  return trees * lumberyards

seen = {}
for t in range(1, 10001):
  after = []
  for r in range(1, GRID_SIZE + 1):
    row = []
    after.append(row)
    for c in range(1, GRID_SIZE + 1):
      row.append(mutate(r, c))

  for r in range(1, GRID_SIZE + 1):
    grid[r] = ['x'] + after[r-1] + ['x']

  if t == 10:
    print 'part1:', res_value()

  key = ''.join([''.join(row) for row in grid])

  if key in seen:
    print 'duplicate {} and {}'.format(t, seen[key])
    cycle_size = t - seen[key]
    more_cycles = (1000000000 - t) % cycle_size
    equivalent = seen[key] + more_cycles
    print cycle_size, more_cycles, equivalent
    for key, value in seen.iteritems():
      if value == equivalent:
        trees = 0
        lumberyards = 0
        for c in key:
          if c == '|':
            trees += 1
          if c == '#':
            lumberyards += 1
        print 'part2:', trees * lumberyards
        break
    break
  else:
    seen[key] = t
