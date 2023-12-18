from collections import defaultdict
import heapq

class PriorityQueue:
  def __init__(self):
    self.heap = []
    self.entry_finder = {}

  def update(self, item, priority):
    self.remove(item)
    entry = [priority, item, False]
    self.entry_finder[item] = entry
    heapq.heappush(self.heap, entry)

  def remove(self, item):
    if item in self.entry_finder:
      entry = self.entry_finder.pop(item)
      entry[-1] = True

  def pop(self):
    while self.heap:
      entry = heapq.heappop(self.heap)
      priority, item, deleted = entry
      if not deleted:
        return item
    return None

UP = (0, -1)
DOWN = (0, 1)
RIGHT = (1, 0)
LEFT = (-1, 0)

def adjust(pos, dir):
  return pos[0] + dir[0], pos[1] + dir[1]

def turnLeft(dir):
  return {
    UP: LEFT,
    LEFT: DOWN,
    DOWN: RIGHT,
    RIGHT: UP
  }[dir]

def turnRight(dir):
  return {
    UP: RIGHT,
    RIGHT: DOWN,
    DOWN: LEFT,
    LEFT: UP
  }[dir]

with open('day17-input.txt', 'r') as input:
  board = [line.rstrip() for line in input]
  heatlossMem = defaultdict(lambda: float('inf'))
  seen = set()
  work = PriorityQueue()
  prev = {}
  for start in [((0, 0), RIGHT, 0), ((0, 0), DOWN, 0)]:
    heatlossMem[start] = 0
    work.update(start, 0)

  def update(w, dir, straights):
    pos = adjust(w[0], dir)
    nw = pos, dir, straights
    x, y = pos
    if not (0 <= y < len(board) and 0 <= x < len(board[y])):
      return
    heatloss = heatlossMem[w] + int(board[y][x])
    if heatloss < heatlossMem[nw]:
      heatlossMem[nw] = heatloss
      prev[nw] = w
      work.update(nw, heatlossMem[nw])

  while True:
    w = work.pop()
    if w is None:
      break
    if w in seen:
      continue
    seen.add(w)
    pos, dir, straights = w
    if straights < 9:
      update(w, dir, straights + 1)
    if straights >= 3:
      update(w, turnLeft(dir), 0)
      update(w, turnRight(dir), 0)
  finish = (len(board[0]) - 1, len(board) - 1)

  # Pretty print
  board = list(map(list, board))
  _, w = min((heatloss, w) for w, heatloss in heatlossMem.items() if w[0] == finish and w[2] >= 4)
  pmem = set()
  while w not in pmem:
    pmem.add(w)
    (x, y), _, _ = w
    board[y][x] = '*'
    if w not in prev:
      break
    w = prev[w]
  for row in board:
    print("".join(row))

  print(min(heatloss for (pos, _, _), heatloss in heatlossMem.items() if pos == finish))