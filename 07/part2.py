# I had an off by one error when computing the time
# (i.e., I was pausing 1 sec before starting new jobs).

# Letter to array of letters
tree = {}
reverse = {}
for line in open('input').read().split('\n'):
  arr = line.split(' ')
  children = tree.setdefault(arr[1], [])
  children.append(arr[7])

  parents = reverse.setdefault(arr[7], [])
  parents.append(arr[1])

workers = [None] * 5
todo = list('BFKEGNOVATIHXYZRMCJDLSUPWQ')
done = []

def next_job():
  for key in todo:
    all_done = True
    for parent in reverse.get(key, []):
      if parent not in done:
        all_done = False
        break
    if all_done:
      return key

def assign_work(time):
  for w, worker in enumerate(workers):
    if worker is None:
      key = next_job()
      if not key:
        return
      print time, 'assign', key, 'to worker', w
      workers[w] = [key, ord(key) - 5]
      todo.remove(key)


time = 0

while len(done) < 26:
  if None in workers:
    assign_work(time)

  time += 1
  for w, worker in enumerate(workers):
    if worker is None:
      continue
    if worker[1] > 0:
      worker[1] -= 1
    else:
      print time, 'finished', worker[0]
      done.append(worker[0])
      workers[w] = None

print workers
print time
