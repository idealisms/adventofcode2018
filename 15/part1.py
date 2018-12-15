board = open('input').read().split('\n')

# board = [
# '#######',
# '#G..#E#',
# '#E#E.E#',
# '#G.##.#',
# '#...#E#',
# '#...E.#',
# '#######',
# ]
# board = [
# '#######',
# '#E..EG#',
# '#.#G.E#',
# '#E.##E#',
# '#G..#.#',
# '#..E#.#',
# '#######',
# ]
# board = [
# '#######',
# '#E.G#.#',
# '#.#G..#',
# '#G.#.G#',
# '#G..#.#',
# '#...E.#',
# '#######',
# ]
# board = [
# '#######',
# '#.E...#',
# '#.#..G#',
# '#.###.#',
# '#E#G#G#',
# '#...#G#',
# '#######',
# ]
# board = [
# '#########',
# '#G......#',
# '#.E.#...#',
# '#..##..G#',
# '#...##..#',
# '#...#...#',
# '#.G...G.#',
# '#.....G.#',
# '#########',
# ]
# board = [
#   '########',
#   '#......#',
#   '#...G.E#',
#   '#...E..#',
#   '########',
# ]
# board = [
# '#########',
# '#G..G..G#',
# '#.......#',
# '#.......#',
# '#G..E..G#',
# '#.......#',
# '#.......#',
# '#G..G..G#',
# '#########',
# ]
# board = [
# '#######',
# '#.G...#',
# '#...EG#',
# '#.#.#G#',
# '#..G#E#',
# '#.....#',
# '#######',
# ]
# (row, col) -> (type, hitpoints)
units = {}
for row, line in enumerate(board):
  for col, c in enumerate(line):
    if c in 'EG':
      units[(row, col)] = [c, 200, True]

OTHER_UNIT = {
  'E': 'G',
  'G': 'E'
}

def find_unit_to_attack(row, col, unit_type):
  possible = ((row-1, col), (row, col-1), (row, col+1), (row+1, col))
  unit_to_attack = None
  for target in possible:
    if target in units and units[target][0] == OTHER_UNIT[unit_type]:
      if unit_to_attack is None:
        unit_to_attack = target
      else:
        # Tie breaker for multiple units to attack.
        if units[target][1] < units[unit_to_attack][1]:
          unit_to_attack = target
  return unit_to_attack

def search_move(row, col, unit_type, positions):
  visited = set()
  positions_to_search = [(row - 1, col, 1), (row, col - 1, 1), (row, col + 1, 1), (row + 1, col, 1)]
  while len(positions_to_search) > 0:
    r, c, distance = positions_to_search.pop(0)
    if (r, c) in positions:
      continue
    if board[r][c] == '.':
      target = find_unit_to_attack(r, c, unit_type)
      positions[(r, c)] = (distance, target)
      if not target:
        positions_to_search.append((r - 1, c, distance + 1))
        positions_to_search.append((r, c - 1, distance + 1))
        positions_to_search.append((r, c + 1, distance + 1))
        positions_to_search.append((r + 1, c, distance + 1))
  #print '{} @ {},{}'.format(unit_type, row, col)
  #for key, value in positions.iteritems():
  #  distance, target = value
  #  if target:
  #    print '  ', key

def find_closest_position(positions):
  move_to = None
  for key, value in positions.iteritems():
    row, col = key
    distance, target = value
    #print row, col, distance, target
    if target:
      if move_to is None:
        move_to = (row, col, distance)
      elif distance < move_to[2]:
        move_to = (row, col, distance)
      elif distance == move_to[2]:
        #print '  equidistant:', move_to[:2], (row, col)
        if row < move_to[0]:
          move_to = (row, col, distance)
        elif row == move_to[0] and col < move_to[1]:
          #print '    same col'
          move_to = (row, col, distance)
        #print '  picked:', move_to

  return move_to

def print_board():
  for r, row in enumerate(board):
    print row, r

def print_units():
  keys = sorted(units.keys())
  for key in keys:
    print '{} @ {},{} ({})'.format(units[key][0], key[0], key[1], units[key][1])

def determine_step(start_row, start_col, end_row, end_col):
  #print '  from {},{} to {} @ {},{}'.format(start_row, start_col, board[end_row][end_col], end_row, end_col)
  positions_to_search = [(start_row, start_col, 1)]

  possible_steps = []
  visited = set()
  while len(positions_to_search) > 0:
    r, c, distance = positions_to_search.pop(0)
    if (r, c) in visited:
      continue
    if board[r][c] == '.':
      is_adjacent_to_end = (
        (r - 1 == end_row and c == end_col) or
        (r == end_row and c - 1 == end_col) or
        (r == end_row and c + 1 == end_col) or
        (r + 1 == end_row and c == end_col))
      if is_adjacent_to_end:
        possible_steps.append((distance, r, c))
      visited.add((r, c))
      if not is_adjacent_to_end:
        positions_to_search.append((r - 1, c, distance + 1))
        positions_to_search.append((r, c - 1, distance + 1))
        positions_to_search.append((r, c + 1, distance + 1))
        positions_to_search.append((r + 1, c, distance + 1))

  possible_steps.sort()
  best_step = possible_steps[0]
  #if len(possible_steps) > 1:
  #  print '  possible steps:', possible_steps
  #  print '  ', best_step
  return (best_step[1], best_step[2])

for t in range(500):
  units_to_act = sorted(units.keys())
  for value in units.values():
    value[2] = False
  for current in units_to_act:
    if current not in units:
      continue

    # Check for attacks first.
    row, col = current
    c, hitpts, has_acted = units[current]
    if has_acted:
      continue
    has_acted = True
    units[current][2] = has_acted
    #print ' {} @ {},{}'.format(c, row, col)
    unit_to_attack = find_unit_to_attack(row, col, c)
    if unit_to_attack:
      units[unit_to_attack][1] -= 3
      #print '{}: {} @ {},{} attacks {},{} ({})'.format(
      #    t, c, row, col, unit_to_attack[0], unit_to_attack[1], units[unit_to_attack][1])
      if units[unit_to_attack][1] <= 0:
        #print '  unit died, removing from board'
        del units[unit_to_attack]
        r = map(lambda x: x, board[unit_to_attack[0]])
        r[unit_to_attack[1]] = '.'
        board[unit_to_attack[0]] = ''.join(r)
        print_board()
      continue

    # Now try to move using a BFS
    positions = {}  # row, col -> (distance, target)
    search_move(row, col, c, positions)
    # r, c, distance
    move_to = find_closest_position(positions)
    if not move_to:
      #print '{} @ {},{} is unable to move'.format(c, row, col)
      continue
    print '{} @ {},{} moves to {},{}'.format(c, row, col, move_to[0], move_to[1])

    positions = {}  # row, col -> distance
    new_row, new_col = determine_step(move_to[0], move_to[1], row, col)
    #print '{} @ {},{} is moving to {},{}'.format(c, row, col, new_row, new_col)
    units[(new_row, new_col)] = [c, hitpts, has_acted]
    del units[current]

    # Ugh, move a piece.
    r = map(lambda x: x, board[new_row])
    r[new_col] = board[row][col]
    board[new_row] = ''.join(r)
    r = map(lambda x: x, board[row])
    r[col] = '.'
    board[row] = ''.join(r)

    # We can also attack after moving.
    row, col = new_row, new_col
    unit_to_attack = find_unit_to_attack(row, col, c)
    if unit_to_attack:
      units[unit_to_attack][1] -= 3
      #print '{}: {} @ {},{} attacks {},{} ({})'.format(
      #    t, c, row, col, unit_to_attack[0], unit_to_attack[1], units[unit_to_attack][1])
      if units[unit_to_attack][1] <= 0:
        #print '  unit died, removing from board'
        del units[unit_to_attack]
        r = map(lambda x: x, board[unit_to_attack[0]])
        r[unit_to_attack[1]] = '.'
        board[unit_to_attack[0]] = ''.join(r)
      continue

  #print t+1
  #print_board()
  #print

  # TODO: Check to see if we are done.
  elf_hitpts = 0
  goblin_hitpts = 0
  for value in units.values():
    c, hitpts, _ = value
    if c == 'E':
      elf_hitpts += hitpts
    elif c == 'G':
      goblin_hitpts += hitpts
  if elf_hitpts == 0:
    print_units()
    print 'Combat ends after {} full rounds.'.format(t)
    print 'Goblins win with {} hit pts lefts.'.format(goblin_hitpts)
    print 'Outcome: {}'.format((t) * goblin_hitpts)
    break
  elif goblin_hitpts == 0:
    print_units()
    print 'Combat ends after {} full rounds.'.format(t)
    print 'Elves win with {} hit pts lefts.'.format(elf_hitpts)
    print 'Outcome: {}'.format((t) * elf_hitpts)
    break
