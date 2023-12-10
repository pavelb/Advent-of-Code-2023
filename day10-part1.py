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
  '.': {},
  'S': {NORTH: NORTH, SOUTH: SOUTH, EAST: EAST, WEST: WEST},
}

with open('day10-input.txt', 'r') as input:
  mem = [list(line.rstrip()) for line in input]
  start = None
  for y, row in enumerate(mem):
    for x, c in enumerate(row):
      if c == 'S':
        start = (x, y)
  dist = defaultdict(lambda: float('inf'))
  dist[start] = 0

  def walk(start, dir):
    x, y = start
    while True:
      c = mem[y][x]
      if dir not in MAP[c]:
        break
      dx, dy = MAP[c][dir]
      nx = x + dx
      ny = y + dy
      if (nx, ny) != start and 0 <= ny < len(mem) and 0 <= nx < len(mem[ny]) and mem[ny][nx] != '.':
        dist[nx, ny] = min(dist[nx, ny], dist[x, y] + 1)
        x, y = nx, ny
        dir = (dx, dy)
      else:
        break
  
  walk(start, NORTH)
  walk(start, SOUTH)
  walk(start, EAST)
  walk(start, WEST)
  print(max(dist.values()))