# TARGET = (10, 10)
# DEPTH = 510
TARGET = (11,722)
DEPTH = 10689
SIZE = (TARGET[0] * 10, TARGET[1] + 78)


import numpy as np

# Erosion levels
grid = np.zeros((SIZE[0], SIZE[1]), np.int32)
regions = np.zeros((SIZE[0], SIZE[1]), np.int32)

for x in xrange(SIZE[0]):
  for y in xrange(SIZE[1]):
    gi = 0
    if (x == 0 and y == 0) or (x == TARGET[0] and y == TARGET[1]):
      gi = 0
    elif x == 0:
      gi = y * 48271
    elif y == 0:
      gi = x * 16807
    else:
      gi = grid[x-1][y] * grid[x][y-1]
    grid[x][y] = (gi + DEPTH) % 20183
    regions[x][y] = grid[x][y] % 3

# 0, 1, 2= nothing, torch, climbing gear
# 0, 1, 2 = rocky, wet, narrow
CAN_USE = {
  0: (1, 2),
  1: (0, 2),
  2: (0, 1),
}

# From https://gist.github.com/potpath/b1cc6383e1116e895ac2ec891f666888
import heapq
from collections import defaultdict

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def set_nodes(self, nodes):
        self.nodes = set(nodes)

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.distances[from_node, to_node] = distance


def dijkstra(graph, initial, target):
    visited = {initial: 0}
    h = [(0, initial)]
    path = {}

    nodes = set(graph.nodes)

    while nodes and h:
        current_weight, min_node = heapq.heappop(h)
        try:
            while min_node not in nodes:
                current_weight, min_node = heapq.heappop(h)
        except IndexError:
            break

        print min_node
        if min_node == target:
          print 'part2:', visited[min_node]
          break
        nodes.remove(min_node)

        for v in graph.edges[min_node]:
            weight = current_weight + graph.distances[min_node, v]
            if v not in visited or weight < visited[v]:
                visited[v] = weight
                heapq.heappush(h, (weight, v))
                path[v] = min_node

    return visited, path

g = Graph()
nodes = []

for x in xrange(SIZE[0]):
  for y in xrange(SIZE[1]):
    t1, t2 = CAN_USE[regions[x][y]]
    nodes.append((x, y, t1))
    nodes.append((x, y, t2))
    g.add_edge((x,y,t1), (x, y, t2), 7)
    g.add_edge((x,y,t2), (x, y, t1), 7)

    for t in (t1, t2):
      for target in ((x-1, y), (x+1, y), (x, y-1), (x, y+1)):
        tx, ty = target
        if tx < 0 or tx >= SIZE[0] or ty < 0 or ty >= SIZE[1]:
          continue
        if t not in CAN_USE[regions[tx][ty]]:
          continue
        g.add_edge((x,y,t), (tx, ty, t), 1)

g.set_nodes(nodes)
print 'graph built ({} nodes); solving'.format(len(nodes))
dijkstra(g, (0, 0, 1), (TARGET[0], TARGET[1], 1))
