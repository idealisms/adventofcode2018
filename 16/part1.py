samples = []
for sample in open('input.samples').read().split('\n\n'):
  #print sample
  before, command, after = sample.split('\n')
  before = map(int, before[9:-1].split(', '))
  command = map(int, command.split(' '))
  after = map(int, after[9:-1].split(', '))
  samples.append([before, command, after])

CODES = [
  'addr',
  'addi',
  'mulr',
  'muli',
  'banr',
  'bani',
  'borr',
  'bori',
  'setr',
  'seti',
  'gtir',
  'gtri',
  'gtrr',
  'eqir',
  'eqri',
  'eqrr',
]

def op(code, a, b, c, regs_in):
  regs = regs_in[:]
  if code == 'addr':
    regs[c] = regs[a] + regs[b]
  elif code == 'addi':
    regs[c] = regs[a] + b
  elif code == 'mulr':
    regs[c] = regs[a] * regs[b]
  elif code == 'muli':
    regs[c] = regs[a] * b
  elif code == 'banr':
    regs[c] = regs[a] & regs[b]
  elif code == 'bani':
    regs[c] = regs[a] & b
  elif code == 'borr':
    regs[c] = regs[a] | regs[b]
  elif code == 'bori':
    regs[c] = regs[a] | b
  elif code == 'setr':
    regs[c] = regs[a]
  elif code == 'seti':
    regs[c] = a
  elif code == 'gtir':
    regs[c] = 1 if a > regs[b] else 0
  elif code == 'gtri':
    regs[c] = 1 if regs[a] > b else 0
  elif code == 'gtrr':
    regs[c] = 1 if regs[a] > regs[b] else 0
  elif code == 'eqir':
    regs[c] = 1 if a == regs[b] else 0
  elif code == 'eqri':
    regs[c] = 1 if regs[a] == b else 0
  elif code == 'eqrr':
    regs[c] = 1 if regs[a] == regs[b] else 0
  else:
    raise Exception('unknown code: ' + code)
  return regs

# samples = [
#   [[3,2,1,1],
#    [9,2,1,2],
#    [3,2,2,1]],
# ]

part1_count = 0
for sample in samples:
  print sample
  before, command, after = sample
  count = 0
  for code in CODES:
    res = op(code, command[1], command[2], command[3], before)
    if after == res:
      print code
      count += 1
  if count >= 3:
    part1_count += 1
  print

print part1_count, len(samples)
