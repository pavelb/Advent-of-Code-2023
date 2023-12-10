from collections import defaultdict

NORTH = (0, -1)
SOUTH = (0, 1)
EAST = (1, 0)
WEST = (-1, 0)
MAP = {
  '|': {NORTH: NORTH, SOUTH: SOUTH},
  '-': {EAST: EAST, WEST: WEST},
  'L': {SOUTH: EAST, WEST: NORTH},
  'J': {SOUTH: WEST, EAST: NORTH},
  '7': {NORTH: WEST, EAST: SOUTH},
  'F': {NORTH: EAST, WEST: SOUTH},
  'S': {NORTH: NORTH, SOUTH: SOUTH, EAST: EAST, WEST: WEST},
}

with open('day10-input.txt', 'r') as input:
  mem = {(x, y): c for y, row in enumerate(input) for x, c in enumerate(row.rstrip())}

  def walk(start, dir):
    path = []
    pos = start
    while True:
      try:
        dir = MAP[mem[pos]][dir]
      except:
        return []
      path.append(pos)
      pos = (pos[0] + dir[0], pos[1] + dir[1])
      if pos == start:
        return path
  
  start = next(pos for pos, c in mem.items() if c == 'S')
  dist = defaultdict(lambda: float('inf'))
  for dir in [NORTH, EAST, SOUTH, WEST]:
    for d, (x, y) in enumerate(walk(start, dir)):
      dist[x, y] = min(dist[x, y], d)
  print(max(dist.values()))
