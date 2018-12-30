verticies = []
for line in open('input').read().split('\n'):
  verticies.append(map(int, line.split(',')))

def distance(v1, v2):
  return sum(map(lambda x: abs(x[0] - x[1]), zip(v1, v2)))

edges = []
for i, v1 in enumerate(verticies):
  e = set()
  edges.append(e)
  for j, v2 in enumerate(verticies):
    if i == j:
      continue
    if distance(v1, v2) <= 3:
      e.add(j)

def mark_seen(v, seen):
  if v in seen:
    return
  seen.add(v)
  for edge in edges[v]:
    mark_seen(edge, seen)

# Count constellations.
seen = set()
count = 0
for v in xrange(len(verticies)):
  if v in seen:
    continue
  count += 1
  mark_seen(v, seen)
print count