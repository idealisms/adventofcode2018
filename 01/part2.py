import itertools

values = map(int, open('input').read().split())
seen = {}
current = 0
for n in itertools.cycle(values):
  current += n
  if current in seen:
    print current
    print str.format('Values seen: {}', len(seen))
    break
  seen[current] = True
