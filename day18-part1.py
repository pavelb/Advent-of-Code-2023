from collections import defaultdict

NORTH = (0, -1)
SOUTH = (0, 1)
EAST = (1, 0)
WEST = (-1, 0)
DIRS = [NORTH, EAST, SOUTH, WEST]

UP = (0, -1)
DOWN = (0, 1)
RIGHT = (1, 0)
LEFT = (-1, 0)
DIR_MAP = {'U': UP, 'D': DOWN, 'L': LEFT, 'R': RIGHT}

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

def adjust(pos, dir):
  return pos[0] + dir[0], pos[1] + dir[1]

with open('day18-input.txt', 'r') as input:
  pos = (0, 0)
  mem = {}
  lastDir = None
  perimLen = 0
  for line in input:
    dir, meters, color = line.rstrip().split(" ")
    dir = DIR_MAP[dir]
    for _ in range(int(meters)):
      perimLen += 1
      if lastDir:
        if lastDir == LEFT and dir == LEFT or lastDir == RIGHT and dir == RIGHT:
          mem[pos] = '-'
        elif lastDir == UP and dir == UP or lastDir == DOWN and dir == DOWN:
          mem[pos] = '|'
        elif lastDir == UP and dir == RIGHT or lastDir == LEFT and dir == DOWN:
          mem[pos] = 'F'
        elif lastDir == DOWN and dir == RIGHT or lastDir == LEFT and dir == UP:
          mem[pos] = 'L'
        elif lastDir == RIGHT and dir == DOWN or lastDir == UP and dir == LEFT:
          mem[pos] = '7'
        elif lastDir == DOWN and dir == LEFT or lastDir == RIGHT and dir == UP:
          mem[pos] = 'J'
      pos = adjust(pos, dir)
      lastDir = dir
  mem[0, 0] = 'S'

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
  print(perimLen + n)
