PADDING = 50
state = ('.' * PADDING) + '###.......##....#.#.#..###.##..##.....#....#.#.....##.###...###.#...###.###.#.###...#.####.##.#....#' + ('.' * PADDING)

patterns = {}
for line in open('input').read().split('\n')[2:]:
  pattern, result = line.split(' => ')
  patterns[pattern] = result

for i in range(20):
  print state
  new_state = ''
  for start in range(len(state) - 4):
    pattern = state[start:start+5]
    new_state += patterns[pattern]
  state = '..' + new_state + '..'
  print state
  print

total = 0
for i, c in enumerate(state):
  if c == '#':
    total += i - 50
print total
