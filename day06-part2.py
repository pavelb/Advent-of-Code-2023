from math import sqrt, ceil, floor

with open('day06-input.txt', 'r') as input:
  lines = list(input)
  t = int(lines[0].split(" ", 1)[1].replace(' ', ''))
  d = int(lines[1].split(" ", 1)[1].replace(' ', ''))
  w1 = ceil((t - sqrt(t*t - 4 * d)) / 2)
  w2 = floor((t + sqrt(t*t - 4 * d)) / 2)
  print(w2 - w1 + 1)
