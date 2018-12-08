import datetime

# str(guard_num) -> array of minutes asleep
sleep_data = {}
current_guard = None
fell_asleep_minute = -1
for line in open('input.sorted').read().split('\n'):
  if not line:
    continue
  timestamp, command = line.split('] ')
  if command.startswith('Guard'):
    _, guard_num, _, _ = command.split(' ')
    current_guard = guard_num[1:]
  elif command.startswith('falls asleep'):
    asleep_timestamp = datetime.datetime.strptime(timestamp[1:], '%Y-%m-%d %H:%M')
    fell_asleep_minute = asleep_timestamp.minute
  elif command.startswith('wakes up'):
    wakeup_timestamp = datetime.datetime.strptime(timestamp[1:], '%Y-%m-%d %H:%M')
    wakeup_minute = wakeup_timestamp.minute
    minutes = sleep_data.setdefault(current_guard, [0 for _ in range(60)])
    for minute in range(fell_asleep_minute, wakeup_minute):
      minutes[minute] += 1
  else:
    print 'unknown command', command

# Compute most time asleep
time_asleep = -1
sleepiest_guard_num = ''
for guard_num, minutes in sleep_data.iteritems():
  if sum(minutes) > time_asleep:
    time_asleep = sum(minutes)
    sleepiest_guard_num = guard_num

print sleepiest_guard_num, sleep_data[sleepiest_guard_num]

most_asleep_min = sleep_data[sleepiest_guard_num].index(max(sleep_data[sleepiest_guard_num]))
print sleepiest_guard_num, '*', most_asleep_min, '=', int(sleepiest_guard_num) * most_asleep_min
