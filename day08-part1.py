with open('day08-input.txt', 'r') as input:
  lines = [line.rstrip() for line in input]
  map = {}
  for line in lines[2:]:
    node, path = line.split(" = ")
    path = path[1:-1]
    left, right = path.split(", ")
    map[node] = {'L': left, 'R': right}

  directions = lines[0]
  i = 0
  current = 'AAA'
  while current != 'ZZZ':
    direction = directions[i % len(directions)]
    if current in map:
      current = map[current][direction]
    i += 1
  print(i)
    

