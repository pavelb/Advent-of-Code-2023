with open('day11-input.txt', 'r') as input:
  map = []
  for line in input:
    hasGalaxy = False
    row = []
    for c in line.rstrip():
      row.append(c)
      if c == '#':
        hasGalaxy = True
    map.append(row)
    if not hasGalaxy:
      map.append(row)
  for x in reversed(range(len(map[0]))):
    if all(row[x] == '.' for row in map):
      for y in range(len(map)):
        map[y] = map[y][:x] + ['.'] + map[y][x:]
  galaxies = []
  for y, row in enumerate(map):
    for x, c in enumerate(row):
      if c == '#':
        galaxies.append((x, y))
  total = 0
  for i, (x1, y1) in enumerate(galaxies):
    for j in range(i + 1, len(galaxies)):
      x2, y2 = galaxies[j]
      dist = abs(x1 - x2) + abs(y1 - y2)
      total += dist
  print(total)
