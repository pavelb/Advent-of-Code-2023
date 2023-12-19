with open('day18-input.txt', 'r') as input:
  x, y = (0, 0)
  total = 0
  for line in input:
    _, _, color = line.rstrip().split(" ")
    dx, dy = {'0': (1, 0), '1': (0, 1), '2': (-1, 0), '3': (0, -1)}[color[-2]]
    m = int(color[2:-2], 16)
    nx, ny = x + dx * m, y + dy * m
    total += m + x * ny - nx * y
    x, y = nx, ny
  print(1 + abs(total) // 2)