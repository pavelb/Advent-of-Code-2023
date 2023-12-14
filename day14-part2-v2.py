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

with open('day14-input.txt', 'r') as input:
  board = [list(line.rstrip()) for line in input]
  cyclesToBoard = dict()
  boardToCycles = dict()
  for i in range(1_000_000_000):
    key = tuple(map(tuple, board))
    if key in boardToCycles:
      loopStart = boardToCycles[key]
      loopLen = i - loopStart
      board = cyclesToBoard[loopStart + (1_000_000_000 - loopStart) % loopLen]
      break
    cyclesToBoard[i] = key
    boardToCycles[key] = i
    slide(board, 0, -1)
    slide(board, -1, 0)
    slide(board, 0, 1)
    slide(board, 1, 0)

  total = 0
  for y, row in enumerate(board):
    for c in row:
      if c == 'O':
        total += len(board) - y
  print(total)
