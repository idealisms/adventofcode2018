# This took me forever to finish because I didn't realize that
# the lexical sort was across all nodes, not just children of
# current node.

# Letter to array of letters
tree = {}
reverse = {}
for line in open('input').read().split('\n'):
  arr = line.split(' ')
  children = tree.setdefault(arr[1], [])
  children.append(arr[7])

  parents = reverse.setdefault(arr[7], [])
  parents.append(arr[1])


order = []
def traverse(key):
  if key in order:
    print 'already added', key
    return
  print key, '<-', reverse.get(key, [])
  all_done = True
  for parent in reverse.get(key, []):
    if parent not in order:
      all_done = False
      break
  if not all_done:
    return
  print 'adding', key
  order.append(key)
  children = sorted(tree.get(key, []))
  print key, '->', children
  for child in children:
    available.append(child)

available = []
for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
  if c not in reverse.keys():
    available.append(c)

while len(available):
  print 'available', sorted(available)
  key = sorted(available)[0]
  traverse(key)
  available.remove(key)

print ''.join(order)
