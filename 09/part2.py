import collections
NUM_PLAYERS = 428

LAST_MARBLE = 72061 * 100

marbles = collections.deque()
marbles.append(0)
scores = [0] * NUM_PLAYERS

current_player = 0
for m in range(1, LAST_MARBLE + 1):
  current_player = (current_player + 1) % NUM_PLAYERS
  if m % 23 == 0:
    scores[current_player] += m
    marbles.rotate(7)
    scores[current_player] += marbles.popleft()
  else:
    marbles.rotate(-2)
    marbles.appendleft(m)
print max(scores)