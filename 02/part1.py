two = 0
three = 0
for boxid in open('input').read().split():
  has_two = False
  has_three = False
  for letter in boxid:
    cnt = boxid.count(letter)
    if cnt == 2:
      has_two = True
    elif cnt == 3:
      has_three = True
  if has_two:
    two += 1
  if has_three:
    three += 1

print two, '*', three, '=', two * three



