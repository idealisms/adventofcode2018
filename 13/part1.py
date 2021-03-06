import sys
tracks = []
# car = (row, col, direction, num turns)
cars = []
for row, line in enumerate(open('input').read().split('\n')):
  track = ''
  for col, c in enumerate(line):
    if c == '<':
      cars.append((row, col, '<', 0))
      track += '-'
    elif c == '>':
      cars.append((row, col, '>', 0))
      track += '-'
    elif c == '^':
      cars.append((row, col, '^', 0))
      track += '|'
    elif c == 'v':
      cars.append((row, col, 'v', 0))
      track += '|'
    else:
      track += c
  tracks.append(track)

LEFT_TURN = '<v>^<'
RIGHT_TURN = '<^>v<'
def turn_car(direction, turns):
  if turns % 3 == 0:
    return LEFT_TURN[LEFT_TURN.index(direction) + 1]
  if turns % 3 == 1:
    return direction
  if turns % 3 == 2:
    return RIGHT_TURN[RIGHT_TURN.index(direction) + 1]

def is_collision(ccars, row, col):
  for car in ccars:
    if car[0] == row and car[1] == col:
      return True
  return False

for t in range(1000):
  cars.sort()
  new_cars = []
  for c, car in enumerate(cars):
    row, col, direction, turns = car
    if direction == '<':
      col -= 1
    elif direction == '>':
      col += 1
    elif direction == '^':
      row -= 1
    elif direction == 'v':
      row += 1
    if is_collision(new_cars, row, col) or is_collision(cars[c+1:], row, col):
      print t, 'location of the crash is {},{}'.format(col, row)
      sys.exit(0)
    if tracks[row][col] == '+':
      direction = turn_car(direction, turns)
      turns += 1
    elif tracks[row][col] == '/':
      if direction == '<':
        direction = 'v'
      elif direction == 'v':
        direction = '<'
      elif direction == '>':
        direction = '^'
      elif direction == '^':
        direction = '>'
    elif tracks[row][col] == '\\':
      if direction == '<':
        direction = '^'
      elif direction == 'v':
        direction = '>'
      elif direction == '>':
        direction = 'v'
      elif direction == '^':
        direction = '<'
    new_cars.append((row, col, direction, turns))
  cars = new_cars
