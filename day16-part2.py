from itertools import chain

UP = (0, -1)
DOWN = (0, 1)
RIGHT = (1, 0)
LEFT = (-1, 0)

def adjust(pos, dir):
  return pos[0] + dir[0], pos[1] + dir[1]

def move(pos, dir):
  return adjust(pos, dir), dir

def energize(board, start):
  beams = [start]
  mem = set()
  while beams:
    beam = beams.pop()
    if beam in mem:
      continue
    pos, dir = beam
    x, y = pos
    if not (0 <= y < len(board) and 0 <= x < len(board[y])):
      continue
    mem.add(beam)
    c = board[y][x]
    if c == '.':
      beams.append(move(pos, dir))
    elif c == '-':
      if dir == RIGHT or dir == LEFT:
        beams.append(move(pos, dir))
      else:
        beams.append(move(pos, LEFT))
        beams.append(move(pos, RIGHT))
    elif c == '|':
      if dir == UP or dir == DOWN:
        beams.append(move(pos, dir))
      else:
        beams.append(move(pos, UP))
        beams.append(move(pos, DOWN))
    elif c == '\\':
      beams.append(move(pos, LEFT if dir == UP else RIGHT if dir == DOWN else UP if dir == LEFT else DOWN))
    elif c == '/':
      beams.append(move(pos, RIGHT if dir == UP else LEFT if dir == DOWN else DOWN if dir == LEFT else UP))
  return len(set(pos for pos, _ in mem))

with open('day16-input.txt', 'r') as input:
  board = [line.rstrip() for line in input]
  top = (((x, 0), DOWN) for x in range(len(board[0])))
  bottom = (((x, len(board) - 1), UP) for x in range(len(board[0])))
  left = (((0, y), RIGHT) for y in range(len(board)))
  right = (((len(board[0]) - 1, y), LEFT) for y in range(len(board)))
  print(max(energize(board, start) for start in chain(top, bottom, left, right)))
