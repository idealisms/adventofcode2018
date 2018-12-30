import re

#  0           1     2      3           4      5            6           7
# [initiative, team, units, hit points, power, attack type, weaknesses, immunities]
INIT, TEAM, UNITS, HP, POWER, ATTACK, WEAK, IMMUNE = range(8)
units = []

team = None
for line in open('input').read().split('\n'):
  if not line:
    continue
  if line == 'Immune System:':
    team = 'immune'
    continue
  if line == 'Infection:':
    team = 'infection'
    continue

  m = re.match(r'^(\d+) units each with (\d+) hit points ([(](.+)[)] )?with an attack that does (\d+) (\w+) damage at initiative (\d+)', line)
  if not m:
    raise Exception('Unable to parse line: ' + line)
  tokens = m.groups()
  weak = set()
  immune = set()
  if tokens[3]:
    for s in tokens[3].split('; '):
      if s.startswith('weak to '):
        weak = set(s[8:].split(', '))
      elif s.startswith('immune to '):
        immune = set(s[10:].split(', '))
  units.append([
    int(tokens[6]),
    team,
    int(tokens[0]),
    int(tokens[1]),
    int(tokens[4]),
    tokens[5],
    weak,
    immune,
  ])

for t in range(100000):
  print 'turn', t
  # target selection
  units.sort(key=lambda u: (u[UNITS] * u[POWER], u[INIT]), reverse=True)
  targets = []
  for attacker in units:
    target = -1
    target_damage_amount = -1
    target_effective_power = -1
    target_initiative = -1
    for d, defender in enumerate(units):
      if attacker[TEAM] == defender[TEAM] or defender[UNITS] <= 0:
        continue
      if attacker[ATTACK] in defender[IMMUNE]:
        continue
      if d in targets:  # Already being targeted.
        continue
      damage_amount = attacker[UNITS] * attacker[POWER] * (2 if attacker[ATTACK] in defender[WEAK] else 1)
      print attacker, 'would deal', damage_amount, 'to', defender
      if damage_amount < target_damage_amount:
        continue
      if damage_amount == target_damage_amount:
        if defender[UNITS] * defender[POWER] < target_effective_power:
          continue
        if (defender[UNITS] * defender[POWER] == target_effective_power and
            target_initiative > defender[INIT]):
          continue
      target = d
      target_damage_amount = damage_amount
      target_effective_power = defender[UNITS] * defender[POWER]
      target_initiative = defender[INIT]
    targets.append(target)

  print
  for i, unit in enumerate(units):
    print unit, 'targets', units[targets[i]] if i != -1 else 'nobody'
  print

  attack_order = [(unit[INIT], i) for i, unit in enumerate(units)]
  attack_order.sort(reverse=True)

  for _, i in attack_order:
    if targets[i] == -1:
      continue
    defender = units[targets[i]]
    if defender[UNITS] <= 0:
      continue
    attacker = units[i]
    if attacker[UNITS] == 0:
      continue
    damage_amount = attacker[UNITS] * attacker[POWER] * (2 if attacker[ATTACK] in defender[WEAK] else 1)
    units_killed = min(int(damage_amount / defender[HP]), defender[UNITS])
    print attacker, 'deals', damage_amount, 'to', defender, 'killing', units_killed, 'units'
    defender[UNITS] -= units_killed

  # Check to see if we're done.
  immune_units = 0
  infection_units = 0
  for unit in units:
    if unit[TEAM] == 'immune':
      immune_units += unit[UNITS]
    else:
      infection_units += unit[UNITS]
  if immune_units == 0:
    print 'Infection wins: {} units left.'.format(infection_units)
    break
  elif infection_units == 0:
    print 'Immune wins: {} units left.'.format(immune_units)
    break
