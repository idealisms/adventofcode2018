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

code_numbers = [set(CODES) for i in range(len(CODES))]

for sample in samples:
  before, command, after = sample
  possible = []
  for code in CODES:
    res = op(code, command[1], command[2], command[3], before)
    if after == res:
      possible.append(code)
  code_numbers[command[0]] = code_numbers[command[0]].intersection(possible)
  print

#print code_numbers
for _ in range(20):
  for i, possible in enumerate(code_numbers):
    if len(possible) == 1:
      for j, target in enumerate(code_numbers):
        if j == i:
          continue
        target.difference_update(possible)
print code_numbers

registers = [0, 0, 0, 0]
for line in open('input.program').read().split('\n'):
  code_num, a, b, c = map(int, line.split(' '))
  code = list(code_numbers[code_num])[0]
  registers = op(code, a, b, c, registers)

print registers
