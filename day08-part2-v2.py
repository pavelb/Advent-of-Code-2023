import math

with open('day08-input.txt', 'r') as input:
  lines = [line.rstrip() for line in input]
  directions = lines[0]
  N = len(directions)
  map = {}
  for line in lines[2:]:
    node, path = line.split(" = ")
    path = path[1:-1]
    left, right = path.split(", ")
    map[node] = {'L': left, 'R': right}

  def cycle(node):
    little = node
    n = 0
    big = node
    m = 0
    while True:
      little = map[little][directions[n]]
      n = (n + 1) % N
      big = map[big][directions[m]]
      m = (m + 1) % N
      big = map[big][directions[m]]
      m = (m + 1) % N
      if little == big and n % N == m % N:
        break
    current = node
    start = 0
    while current != little:
      current = map[current][directions[start % N]]
      start += 1
    current = little
    i = start
    while True:
      current = map[current][directions[i % N]]
      i += 1
      if current == little:
        break
    return start, i - start

  work = []
  for node in map.keys():
    if node[-1] != 'A':
      continue
    start, length = cycle(node)
    work.append((length, start % length))

  length, a = work[0]
  for length2, start2 in work[1:]:
    while a % length2 != start2:
      a += length
    length = math.lcm(length, length2)
  print(length + a)
