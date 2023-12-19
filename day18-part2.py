from collections import defaultdict

UP = (0, -1)
DOWN = (0, 1)
RIGHT = (1, 0)
LEFT = (-1, 0)
DIR_MAP = {'0': RIGHT, '1': DOWN, '2': LEFT, '3': UP}

def reverse(dir):
  return {UP: DOWN, DOWN: UP, LEFT: RIGHT, RIGHT: LEFT}[dir]

def mult2D(dir, m):
  return dir[0] * m, dir[1] * m

def add2D(pos, dir):
  return pos[0] + dir[0], pos[1] + dir[1]

class Node(object):
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.next = defaultdict(lambda: None)
  def __str__(self):
    dirs = "".join(sorted({UP: 'U', DOWN: 'D', LEFT: 'L', RIGHT: 'R'}[k] for k, v in self.next.items() if v))
    return "{pos: " + str((self.x, self.y)) + ", next: " + str(dirs) + "}"
  def __repr__(self):
    return self.__str__()

def connect(node1, node2, dir):
  node1.next[dir] = node2
  node2.next[reverse(dir)] = node1

def getNodes():
  with open('day18-input.txt', 'r') as input:
    x, y = (0, 0)
    nodes = [Node(x, y)]
    for line in input:
      _, _, color = line.rstrip().split(" ")
      dir = DIR_MAP[color[-2]]
      meters = int(color[2:-2], 16)
      x, y = add2D((x, y), mult2D(dir, meters))
      if (x, y) == (0, 0):
        connect(nodes[-1], nodes[0], dir)
        break
      node = Node(x, y)
      connect(nodes[-1], node, dir)
      nodes.append(node)
    return nodes

def toBox(node):
  if not node:
    return '.'
  U = node.next[UP]
  D = node.next[DOWN]
  L = node.next[LEFT]
  R = node.next[RIGHT]
  if sum(not not d for d in [U, D, L, R]) != 2:
    raise 'X'
  return '-' if L and R else '│' if U and D else '┐' if L and D else '┘' if L and U else '└' if U and R else '┌' if D and R else '?'

def printRange(top, mid, bottom):
  print(toBox(top.next[LEFT]) + toBox(top))
  for node in mid:
    print("│", end="")
    print(toBox(node))
  print(toBox(bottom.next[LEFT]) + toBox(bottom))

nodes = getNodes()
total = 0
while nodes:
  left = min(node.x for node in nodes)
  right = min(node.x for node in nodes if node.x > left)

  for node in sorted(nodes, key=lambda node: node.y):
    if node.x == left:
      print(toBox(node) + toBox(node.next[RIGHT]))
  for node in sorted(nodes, key=lambda node: node.y):
    if node.x == right:
      print(toBox(node.next[LEFT]) + toBox(node))
  
  for node in reversed(nodes):
    if node.x == left:
      nodes.remove(node)
      rightNode = node.next[RIGHT]
      if rightNode and rightNode.x > right:  # add horizontal bisectors
        newNode = Node(right, node.y)
        connect(node, newNode, RIGHT)
        connect(newNode, rightNode, RIGHT)
        nodes.append(newNode)
  
  cut = sorted([node for node in nodes if node.x == right], key=lambda node: node.y)
  ranges = []
  open = False
  for node in cut:
    if node.next[LEFT]:
      if not open:
        ranges.append([])
      open = not open
      ranges[-1].append(node)
    elif open:
      ranges[-1].append(node)

  for range in ranges:
    top = range.pop(0)
    bottom = range.pop()
    printRange(top, range, bottom)

    if top.next[DOWN] == bottom:  # rectangle
      total += (right - left + 1) * (bottom.y - top.y + 1)
      nodes.remove(top)
      nodes.remove(bottom)
    else:
      if top.next[DOWN]:
        newTop = top.next[DOWN]
        total += (right - left + 1) * (newTop.y - top.y)
        nodes.remove(top)
        del newTop.next[UP]
        node = Node(left, newTop.y)
        connect(node, newTop, RIGHT)
        connect(node, bottom.next[LEFT], DOWN)
        top = newTop
        range.pop(0)
        printRange(top, range, bottom)
      if bottom.next[UP]:
        newBottom = bottom.next[UP]
        total += (right - left + 1) * (bottom.y - newBottom.y)
        nodes.remove(bottom)
        del newBottom.next[DOWN]
        node = Node(left, newBottom.y)
        connect(node, newBottom, RIGHT)
        connect(node, top.next[LEFT], UP)
        bottom = newBottom
        range.pop()
        printRange(top, range, bottom)

      total += (right - left) * (bottom.y - top.y + 1)
      del top.next[LEFT]
      del bottom.next[LEFT]
      curTop = top
      for (a, b) in zip(range[::2], range[1::2]):
        total += b.y - a.y - 1
        connect(curTop, a, DOWN)
        del a.next[DOWN]
        del b.next[UP]
        curTop = b
      connect(curTop, bottom, DOWN)
      printRange(top, range, bottom)

  for node in reversed(nodes):  # remove vertical bisectors
    up = node.next[UP]
    down = node.next[DOWN]
    if up and down:
      connect(up, down, DOWN)
      nodes.remove(node)

print(total)
