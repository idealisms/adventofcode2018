s = open('input').read()
orig_input = s.strip()

def react(s):
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
  return len(s)

best = len(orig_input)
for i in range(ord('a'), ord('z') + 1):
  l = chr(i)
  u = l.upper()
  s = orig_input.replace(l, '').replace(u, '')
  best = min(best, react(s))

print best
