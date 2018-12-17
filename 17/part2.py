import re

grid = []
for line in open('grid').read().split('\n'):
  grid.append(line)

def repl_water(m):
  return m.string[m.start():m.end()].replace('w', '|')

for i, line in enumerate(grid):
  line = re.sub('[.](w+)#', repl_water, line)
  line = re.sub('[.](w+)[.]', repl_water, line)
  line = re.sub('[.](w+)[.]', repl_water, line)
  line = re.sub('[.](w+)[.]', repl_water, line)
  line = re.sub('#(w+)[.]', repl_water, line)
  # line = re.sub('[.]w', '.|', line)
  # line = re.sub('w[.]', '|.', line)
  grid[i] = line

f = open('grid2', 'w')
for line in grid:
  f.write(line)
  f.write('\n')
f.close()

part2 = 0
for line in grid:
  for c in line:
    if c == 'w':
      part2 += 1

print part2