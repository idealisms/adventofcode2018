PADDING = 2000
state = ('.' * PADDING) + '###.......##....#.#.#..###.##..##.....#....#.#.....##.###...###.#...###.###.#.###...#.####.##.#....#' + ('.' * PADDING)

patterns = {}
for line in open('input').read().split('\n')[2:]:
  pattern, result = line.split(' => ')
  patterns[pattern] = result

last_total = 0
cycle = []
for i in range(500):
  new_state = ''
  for start in range(len(state) - 4):
    pattern = state[start:start+5]
    new_state += patterns[pattern]
  state = '..' + new_state + '..'

  total = 0
  for j, c in enumerate(state):
    if c == '#':
      total += j - PADDING
  delta = total - last_total
  print (i+1), total, delta #, state
  if i > 0:
    cycle.append(delta)
  last_total = total
print state

# We hit steady state after 131 cycles.
print (50000000000 - 500) * 52 + last_total