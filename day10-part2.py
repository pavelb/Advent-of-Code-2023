from collections import defaultdict

NORTH = (0, -1)
SOUTH = (0, 1)
EAST = (1, 0)
WEST = (-1, 0)
DIRS = [NORTH, EAST, SOUTH, WEST]
MAP = {
  '|': {NORTH: NORTH, SOUTH: SOUTH},
  '-': {EAST: EAST, WEST: WEST},
  'L': {SOUTH: EAST, WEST: NORTH},
  'J': {SOUTH: WEST, EAST: NORTH},
  '7': {NORTH: WEST, EAST: SOUTH},
  'F': {NORTH: EAST, WEST: SOUTH},
  'S': {NORTH: NORTH, SOUTH: SOUTH, EAST: EAST, WEST: WEST},
}
WIND = {
  (NORTH, WEST): -1,
  (NORTH, NORTH): 0,
  (NORTH, EAST): 1,
  (EAST, NORTH): -1,
  (EAST, EAST): 0,
  (EAST, SOUTH): 1,
  (SOUTH, EAST): -1,
  (SOUTH, SOUTH): 0,
  (SOUTH, WEST): 1,
  (WEST, SOUTH): -1,
  (WEST, WEST): 0,
  (WEST, NORTH): 1
}

def outside(c, dir, wind):
  cw = wind > 0
  return {
    ('|', NORTH, True): [EAST],
    ('|', NORTH, False): [WEST],
    ('|', SOUTH, True): [WEST],
    ('|', SOUTH, False): [EAST],

    ('-', EAST, True): [SOUTH],
    ('-', EAST, False): [NORTH],
    ('-', WEST, True): [NORTH],
    ('-', WEST, False): [SOUTH],

    ('L', SOUTH, True): [SOUTH, WEST],
    ('L', SOUTH, False): [],
    ('L', WEST, True): [],
    ('L', WEST, False): [SOUTH, WEST],

    ('J', SOUTH, True): [],
    ('J', SOUTH, False): [SOUTH, EAST],
    ('J', EAST, True): [EAST, SOUTH],
    ('J', EAST, False): [],

    ('7', NORTH, True): [NORTH, EAST],
    ('7', NORTH, False): [],
    ('7', EAST, True): [],
    ('7', EAST, False): [NORTH, EAST],

    ('F', NORTH, True): [],
    ('F', NORTH, False): [NORTH, WEST],
    ('F', WEST, True): [NORTH, WEST],
    ('F', WEST, False): [],

    ('S', NORTH, True): [EAST],
    ('S', NORTH, False): [WEST],
    ('S', SOUTH, True): [WEST],
    ('S', SOUTH, False): [EAST],
    ('S', EAST, True): [SOUTH],
    ('S', EAST, False): [NORTH],
    ('S', WEST, True): [NORTH],
    ('S', WEST, False): [SOUTH],
  }[c, dir, cw]

with open('day10-input.txt', 'r') as input:
  mem = [list(line.rstrip()) for line in input]

  def cells():
    for y, row in enumerate(mem):
      for x, c in enumerate(row):
        yield (x, y), c

  start = next(pos for (pos, c) in cells() if c == 'S')

  def walkLoop(start, dir):
    x, y = start
    path = []
    wind = 0
    while True:
      path.append(((x, y), dir))
      c = mem[y][x]
      if c not in MAP or dir not in MAP[c]:
        return [], wind
      dx, dy = MAP[c][dir]
      nx = x + dx
      ny = y + dy
      wind += WIND[dir, (dx, dy)]
      if (nx, ny) == start:
        return path, wind
      if 0 <= ny < len(mem) and 0 <= nx < len(mem[ny]):
        x, y = nx, ny
        dir = (dx, dy)
      else:
        return [], wind
  
  pipe = defaultdict(bool)
  path = []
  wind = None
  for dir in DIRS:
    path, wind = walkLoop(start, dir)
    for pos, _ in path:
      pipe[pos] = True
    if path:
      break
  
  inside = set()
  for (x, y), dir in path:
    c = mem[y][x]
    for dx, dy in outside(c, dir, wind):
      nx = x + dx
      ny = y + dy
      if not pipe[nx, ny]:
        inside.add((nx, ny))

  seen = defaultdict(bool)
  n = 0
  while inside:
    n += 1
    x, y = inside.pop()
    seen[x, y] = True
    for dx, dy in DIRS:
      nx = x + dx
      ny = y + dy
      if not pipe[nx, ny] and not seen[nx, ny]:
        inside.add((nx, ny))
  print(n)