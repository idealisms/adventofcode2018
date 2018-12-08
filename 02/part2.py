import itertools
boxids = open('input').read().split()
for ida, idb in itertools.combinations(boxids, 2):
  different = 0
  newout = []
  for i, c in enumerate(ida):
    if c != idb[i]:
      different += 1
    else:
      newout.append(c)

  if different == 1:
    print ida, idb, ''.join(newout)
    break
