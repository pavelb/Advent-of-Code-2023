from collections import defaultdict

NORTH = (0, -1)
SOUTH = (0, 1)
EAST = (1, 0)
WEST = (-1, 0)
DIRS = [NORTH, EAST, SOUTH, WEST]

# For each pipe piece store incoming direction mapped to
#   outgoing direction
#   clock-wise/counter-clockwise wind number of the turn
#   adjacent cells right of the pipe in travel direction
#   adjacent cells left of the pipe in travel direction
MAP = {
  '|': {
    NORTH: (NORTH, 0, [EAST], [WEST]),
    SOUTH: (SOUTH, 0, [WEST], [EAST])
  },
  '-': {
    EAST: (EAST, 0, [SOUTH], [NORTH]),
    WEST: (WEST, 0, [NORTH], [SOUTH])
  },
  'L': {
    SOUTH: (EAST, -1, [SOUTH, WEST], []),
    WEST: (NORTH, 1, [], [SOUTH, WEST])
  },
  'J': {
    SOUTH: (WEST, 1, [], [SOUTH, EAST]),
    EAST: (NORTH, -1, [SOUTH, EAST], [])
  },
  '7': {
    NORTH: (WEST, -1, [NORTH, EAST], []),
    EAST: (SOUTH, 1, [], [NORTH, EAST])
  },
  'F': {
    NORTH: (EAST, 1, [], [NORTH, WEST]),
    WEST: (SOUTH, -1, [NORTH, WEST], [])
  },
  'S': {
    NORTH: (NORTH, 0, [EAST], [WEST]),
    SOUTH: (SOUTH, 0, [WEST], [EAST]),
    EAST: (EAST, 0, [SOUTH], [NORTH]),
    WEST: (WEST, 0, [NORTH], [SOUTH])
  }
}

with open('day10-input.txt', 'r') as input:
  mem = {(x, y): c for y, row in enumerate(input) for x, c in enumerate(row.rstrip())}

  def walk(start, dir):
    path = []
    wind = 0
    pos = start
    while True:
      try:
        dir, w, right, left = MAP[mem[pos]][dir]
      except:
        return [], 0
      path.append((pos, right, left))
      wind += w
      pos = (pos[0] + dir[0], pos[1] + dir[1])
      if pos == start:
        return path, wind
  
  start = next(pos for pos, c in mem.items() if c == 'S')
  path, wind = next(filter(lambda x: x[0], (walk(start, dir) for dir in DIRS)))
  seen = defaultdict(bool)
  work = set()
  for (x, y), right, left in path:
    seen[x, y] = True
    work.update((x + dx, y + dy) for dx, dy in (right if wind > 0 else left))
  n = 0
  while work:
    x, y = work.pop()
    if seen[x, y]:
      continue
    seen[x, y] = True
    n += 1
    work.update((x + dx, y + dy) for dx, dy in DIRS)
  print(n)
