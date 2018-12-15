recipes = [3, 7, 1, 0]
elves = [0, 1]

target = 846601
#target = 2018

while True:
  total = 0
  for elf in elves:
    total += recipes[elf]
  new_digits = []
  if total == 0:
    recipes.append(0)
  else:
    while total > 0:
      new_digits.append(total % 10)
      total = int(total / 10)
    recipes.extend(reversed(new_digits))
  for e, elf in enumerate(elves):
    elves[e] = (elf + recipes[elf] + 1) % len(recipes)
  if len(recipes) >= target + 10:
    break

print ''.join(map(str, recipes[target:target+10]))