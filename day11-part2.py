with open('day11-input.txt', 'r') as input:
  map = [line.rstrip() for line in input]
  rowDelta = [1 if '#' in row else 1000000 for row in map]
  colDelta = [1 if any(row[x] == '#' for row in map) else 1000000 for x in range(len(map[0]))]
  galaxies = [(x, y) for y, row in enumerate(map) for x, c in enumerate(row) if c == '#']
  total = 0
  for i, (x1, y1) in enumerate(galaxies):
    for j in range(i + 1, len(galaxies)):
      x2, y2 = galaxies[j]
      dist = sum(colDelta[x] for x in range(min(x1, x2), max(x1, x2)))
      dist += sum(rowDelta[y] for y in range(min(y1, y2), max(y1, y2)))
      total += dist
  print(total)
