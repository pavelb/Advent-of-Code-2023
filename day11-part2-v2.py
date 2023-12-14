with open('day11-input.txt', 'r') as input:
  map = [line.rstrip() for line in input]
  rowDelta = [1 if '#' in row else 1000000 for row in map]
  rowDelta = [sum(rowDelta[:i]) for i in range(len(rowDelta))]
  colDelta = [1 if any(row[x] == '#' for row in map) else 1000000 for x in range(len(map[0]))]
  colDelta = [sum(colDelta[:i]) for i in range(len(colDelta))]
  galaxies = [(x, y) for y, row in enumerate(map) for x, c in enumerate(row) if c == '#']
  total = 0
  for i, (x1, y1) in enumerate(galaxies):
    for j in range(i + 1, len(galaxies)):
      x2, y2 = galaxies[j]
      dist = colDelta[max(x1, x2)] - colDelta[min(x1, x2)]
      dist += rowDelta[max(y1, y2)] - rowDelta[min(y1, y2)]
      total += dist
  print(total)
