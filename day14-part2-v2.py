from itertools import count, product

def slide(board, dx, dy):
  rx = range(len(board[0]))
  if dx > 0:
    rx = reversed(rx)
  ry = range(len(board))
  if dy > 0:
    ry = reversed(ry)
  for x, y in product(rx, ry):
    if board[y][x] == 'O':
      while 0 <= y + dy < len(board) and 0 <= x + dx < len(board[y]) and board[y + dy][x + dx] == '.':
        board[y][x] = '.'
        x += dx
        y += dy
        board[y][x] = 'O'

def getKey(board):
  return tuple(map(tuple, board))

def loopSize(mem, key):
  k = key
  for n in count(1):
    k = getKey(mem[k])
    if k == key:
      return n

with open('day14-input.txt', 'r') as input:
  board = [list(line.rstrip()) for line in input]
  
  mem = dict()
  looped = False
  n = 1_000_000_000
  while n > 0:
    if not looped:
      key = getKey(board)
      if key in mem:
        looped = True
        n %= loopSize(mem, key)
        continue
    n -= 1
    slide(board, 0, -1)
    slide(board, -1, 0)
    slide(board, 0, 1)
    slide(board, 1, 0)
    if not looped:
      mem[key] = list(map(list, board))

  total = 0
  for y, row in enumerate(board):
    for c in row:
      if c == 'O':
        total += len(board) - y
  print(total)
