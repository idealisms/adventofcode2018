import re
fout_points = open('input.points.js', 'w')
fout_deltas = open('input.deltas.js', 'w')
fout_points.write('let points = [\n')
fout_deltas.write('let deltas = [\n')
for line in open('input').read().split('\n'):
  _, x, y, _, dx, dy, _ = re.split('[,<>]', line)

  fout_points.write('[{}, {}],\n'.format(x.strip(), y.strip()))
  fout_deltas.write('[{}, {}],\n'.format(dx.strip(), dy.strip()))

fout_points.write(']\n')
fout_deltas.write(']\n')
fout_points.close()
fout_deltas.close()

