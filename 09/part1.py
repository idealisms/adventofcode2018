NUM_PLAYERS = 428

LAST_MARBLE = 72061

marbles = [0, 1]
scores = [0] * NUM_PLAYERS

current_player = 0
current_marble = 1
for m in range(2, LAST_MARBLE + 1):
  current_player = (current_player + 1) % NUM_PLAYERS
  if m % 23 == 0:
    scores[current_player] += m
    pos = current_marble - 7
    if pos < 0:
      pos += len(marbles)
    scores[current_player] += marbles.pop(pos)
    current_marble = pos % len(marbles)
  else:
    pos = (current_marble + 2) % len(marbles)
    marbles.insert(pos, m)
    current_marble = pos
print max(scores)