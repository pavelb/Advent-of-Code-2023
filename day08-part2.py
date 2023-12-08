import math

with open('day08-input.txt', 'r') as input:
  lines = [line.rstrip() for line in input]
  map = {}
  for line in lines[2:]:
    node, path = line.split(" = ")
    path = path[1:-1]
    left, right = path.split(", ")
    map[node] = {'L': left, 'R': right}

  directions = lines[0]

  multiples = []
  for node in map.keys():
    if node[-1] != 'A':
      continue
    current = node
    i = 0
    while current[-1] != 'Z':
      direction = directions[i % len(directions)]
      current = map[current][direction]
      i += 1
    multiples.append(i)

  print(math.lcm(*multiples))

