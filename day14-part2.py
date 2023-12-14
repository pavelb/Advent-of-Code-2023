from itertools import count

def slide(mem, dx, dy):
  for (x, y), c in sorted(mem.items(), key = (lambda i: i[0][1]) if dy else (lambda i: i), reverse = dx > 0 or dy > 0):
    if c == 'O':
      while mem.get((x + dx, y + dy)) == '.':
        mem[(x, y)], mem[(x + dx, y + dy)] = mem[(x + dx, y + dy)], mem[(x, y)]
        x += dx
        y += dy

def getKey(mem):
  return tuple(sorted(mem.items()))

def loopSize(meta, key):
  m = 0
  k = key
  while True:
    m += 1
    v = meta[k]
    k = getKey(v)
    if k == key:
      break
  return m

with open('day14-input.txt', 'r') as input:
  mem = {(x, y): c for y, row in enumerate(input) for x, c in enumerate(row.rstrip())}

  meta = dict()
  for i in range(1000000000):
    key = getKey(mem)
    if key in meta:
      for _ in range((1000000000 - i) % loopSize(meta, key)):
        slide(mem, 0, -1)
        slide(mem, -1, 0)
        slide(mem, 0, 1)
        slide(mem, 1, 0)
      break
    slide(mem, 0, -1)
    slide(mem, -1, 0)
    slide(mem, 0, 1)
    slide(mem, 1, 0)
    meta[key] = dict(mem)

  Y = max(y for (x, y) in mem.keys())
  total = 0
  for (x, y), c in mem.items():
    if c == 'O':
      total += Y - y + 1
  print(total)
