s = open('input').read()
s = s.strip()

while True:
  reacted = False
  for i in range(len(s) - 1):
    if i >= len(s) - 1:
      break
    c1 = s[i]
    c2 = s[i+1]
    if ((c1.islower() and not c2.islower()) or
        (c2.islower() and not c1.islower())) and (
          c1.lower() == c2.lower()
        ):
      s = s[:i] + s[i+2:]
      i -= 1
      reacted = True
  if not reacted:
    break

print s
print len(s)
