import re
fabric = []
for i in range(1000):
  fabric.append([0 for _ in range(1000)])

overlapping = set()
RE_SPLIT = re.compile('[# ,: x]')
for line in open('input').read().split('\n'):
  if not line:
    continue
  _, claim, _, left, top, _, width, height = re.split(RE_SPLIT, line)
  claim = int(claim)
  for x in range(int(left), int(left) + int(width)):
    for y in range(int(top), int(top) + int(height)):
      if fabric[x][y] != 0:
        overlapping.add(fabric[x][y])
        overlapping.add(claim)
      fabric[x][y] = claim

for i in range(len(overlapping) + 1):
  if i + 1 not in overlapping:
    print i + 1
