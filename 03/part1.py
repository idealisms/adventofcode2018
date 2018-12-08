import re
fabric = []
for i in range(1000):
  fabric.append([0 for _ in range(1000)])

RE_SPLIT = re.compile('[ ,: x]')
for line in open('input').read().split('\n'):
  if not line:
    continue
  _, _, left, top, _, width, height = re.split(RE_SPLIT, line)
  for x in range(int(left), int(left) + int(width)):
    for y in range(int(top), int(top) + int(height)):
      fabric[x][y] += 1

multiple_claims = 0
for x in range(1000):
  for y in range(1000):
    if fabric[x][y] >= 2:
      multiple_claims += 1

print multiple_claims
