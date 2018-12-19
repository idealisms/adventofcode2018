import math

def op(code, a, b, c, regs_in):
  #regs = regs_in[:]
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


lines = open('input').read().split('\n')
ip_s = int(lines[0][-1])
cmds = []
for line in lines[1:]:
  tokens = line.split(' ')
  cmds.append([tokens[0]] + map(int, tokens[1:]))

TARGET = 10551345  # This is the value of reg[5]
factors = []
for i in range(1, int(math.sqrt(TARGET)) + 1):
  if TARGET % i == 0:
    factors.append(i)
    factors.append(TARGET / i)
factors.sort()
print factors
print sum(factors)  # This is the solution to part 2.

jump_values = {}
SAFE_OFFSET = 2
for i, factor in enumerate(factors):
  if factor > 21:
    jump_values[factors[i-1] + SAFE_OFFSET] = factors[i] - SAFE_OFFSET
jump_values[factors[-1] + SAFE_OFFSET] = 10551340
print jump_values

ip = 0
regs = [0] * 6
regs[0] = 1
try:
  for t in xrange(10000000):
    if t % 10000 == 0:
      print t
    if ip == 8 and regs[2] in jump_values:
      regs[2] = jump_values[regs[2]]
    if ip == 12 and regs[1] in jump_values:
      regs[1] = jump_values[regs[1]]
    regs[ip_s] = ip
    print '{} ip={} {}'.format(t, ip, str(regs))
    code, a, b, c = cmds[ip]
    regs = op(code, a, b, c, regs)
    print '  command: {} {}'.format(str(cmds[ip]), str(regs))
    ip = regs[ip_s] + 1
except IndexError:
  print 'out of range'
  print regs

# incorrect: 10612210, 10612401
# 19354944
