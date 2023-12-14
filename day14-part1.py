from itertools import count

def slideUp(mem, x, y):
  while mem.get((x, y - 1)) == '.':
    mem[(x, y)], mem[(x, y - 1)] = mem[(x, y - 1)], mem[(x, y)]
    y -= 1

with open('day14-input.txt', 'r') as input:
  mem = {(x, y): c for y, row in enumerate(input) for x, c in enumerate(row.rstrip())}
  for (x, y), c in mem.items():
    if c == 'O':
      slideUp(mem, x, y)
  Y = max(y for (x, y) in mem.keys())
  total = 0
  for (x, y), c in mem.items():
    if c == 'O':
      total += Y - y + 1
  print(total)
