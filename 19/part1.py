
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

ip = 0
regs = [0] * 6
try:
  for t in range(10000000):
    if t % 1000 == 0:
      print t
    regs[ip_s] = ip
    #print '{} ip={} {}'.format(t, ip, str(regs))
    code, a, b, c = cmds[ip]
    regs = op(code, a, b, c, regs)
    #print '  command: {} {}'.format(str(cmds[ip]), str(regs))
    ip = regs[ip_s] + 1
except IndexError:
  print 'out of range'
  print regs
