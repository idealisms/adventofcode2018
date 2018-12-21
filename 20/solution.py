# Room is ((x, y), [n, e, s, w])
rooms = {}
rooms[(0, 0)] = ((0, 0), [False] * 4)
INPUT = open('input').read()
# INPUT = '^WNE$'
# INPUT = '^ENWWW(NEEE|SSE(EE|N))$'  # 16 rooms, 10 doors
# INPUT = '^ENNWSWW(NEWS|)SSSEEN(WNSE|)EE(SWEN|)NNN$'  # 25 rooms, 18 doors
#                  1         2         3         4         5
#        012345678901234567890123456789012345678901234567890
# INPUT = '^ESSWWN(E|NNENN(EESS(WNSE|)SSS|WWWSSSSE(SW|NNNE)))$'  # 36 rooms, 23 doors
#        0123456789
# INPUT = '^E(S|N)$'
# INPUT = '^E(S|(N|)|)E$'
# INPUT = '^E(S|N|)E$' # ESE, ENE, EE -> 7 rooms
# INPUT = '^W|N$'

# returns next_i and list of end positions
def expr(i, x, y):
  # print '{} {},{}'.format(i, x, y)

  if INPUT[i] == '$':
    raise Exception('parse error $')
  if INPUT[i] in '|)':
    return i, [(x,y)]

  if INPUT[i] in 'NESW':
    while INPUT[i] in 'NESW':
      if INPUT[i] == 'N':
        rooms[(x, y)][1][0] = True
        y -= 1
      elif INPUT[i] == 'E':
        rooms[(x, y)][1][1] = True
        x += 1
      elif INPUT[i] == 'S':
        rooms[(x, y)][1][2] = True
        y += 1
      elif INPUT[i] == 'W':
        rooms[(x, y)][1][3] = True
        x -= 1
      room = rooms.setdefault((x, y), ((x, y), [False] * 4))
      if INPUT[i] == 'N':
        room[1][2] = True
      elif INPUT[i] == 'E':
        room[1][3] = True
      elif INPUT[i] == 'S':
        room[1][0] = True
      elif INPUT[i] == 'W':
        room[1][1] = True
      i += 1
    if INPUT[i] == '(':
      return expr(i, x, y)
    if INPUT[i] in '|)$':
      return i, [(x, y)]
    raise Exception('parse error, unexpected token after letters')

  if INPUT[i] in '^(':
    # print '{} {}'.format(i, INPUT[i])
    next_i, next_rooms = expr(i+1, x, y)
    while INPUT[next_i] not in ')$':
      next_i, more_rooms = expr(next_i+1, x, y)
      next_rooms.extend(more_rooms)
    if INPUT[next_i] == '$':
      if INPUT[i] != '^':
        raise Exception('parse error, expected $ to match ^')
      return # We're done

    # Consume the close paren.
    next_i += 1

    if INPUT[next_i] == '$':
      return next_i, []

    next_rooms = set(next_rooms)
    print INPUT[i:next_i]
    print '  next_rooms: {}'.format(str(next_rooms))
    ret_rooms = []
    ret_i = None
    for room in next_rooms:
      ret_i, more_rooms = expr(next_i, room[0], room[1])
      # print '  ret_i:', ret_i
      ret_rooms.extend(more_rooms)
    return ret_i, ret_rooms
  raise Exception('unexpected token: ' + INPUT[i])

expr(0, 0, 0)

print 'rooms:', len(rooms.keys())
print rooms.keys()

seen = set()
# x, y, distance
queue = [(0, 0, 0)]
max_doors = 0
more_than_1000 = 0
while len(queue) > 0:
  x, y, dist = queue.pop(0)
  if (x, y) in seen:
    continue
  seen.add((x, y))
  if dist > max_doors:
    # print '{} to {},{}'.format(dist, x, y)
    max_doors = dist
  if dist >= 1000:
    more_than_1000 += 1
  coord, doors = rooms[(x, y)]
  if doors[0]:
    queue.append((x, y-1, dist+1))
  if doors[1]:
    queue.append((x+1, y, dist+1))
  if doors[2]:
    queue.append((x, y+1, dist+1))
  if doors[3]:
    queue.append((x-1, y, dist+1))

print 'rooms seen:', len(seen)
print 'part1:', max_doors
print 'part2:', more_than_1000
