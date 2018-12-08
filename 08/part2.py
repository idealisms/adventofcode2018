input = map(int, open('input').read().split(' '))

class Node(object):
  def __init__(self):
    self.children = []
    self.metadata = []

sum_metadata = 0
def parse(input):
  global sum_metadata
  node = Node()
  num_children = input.pop(0)
  metadata_size = input.pop(0)
  for i in range(num_children):
    node.children.append(parse(input))
  for i in range(metadata_size):
    metadata = input.pop(0)
    node.metadata.append(metadata)
    sum_metadata += metadata
  return node

tree = parse(input)

def value(node):
  if len(node.children) == 0:
    return sum(node.metadata)
  v = 0
  for m in node.metadata:
    if m - 1 < len(node.children):
      v += value(node.children[m-1])
  return v

print value(tree)
