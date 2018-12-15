recipes = [3, 7, 1, 0]
elves = [0, 1]

target = [8, 4, 6, 6, 0, 1]

while True:
  total = 0
  for elf in elves:
    total += recipes[elf]
  new_digits = []
  if total == 0:
    new_digits = [0]
  else:
    while total > 0:
      new_digits.append(total % 10)
      total = int(total / 10)
  recipes.extend(reversed(new_digits))
  for e, elf in enumerate(elves):
    elves[e] = (elf + recipes[elf] + 1) % len(recipes)
  if recipes[len(recipes) - len(target):] == target:
    print len(recipes) - len(target)
    break
  elif recipes[len(recipes) - len(target) - 1:-1] == target:
    print len(recipes) - len(target) - 1
    break

