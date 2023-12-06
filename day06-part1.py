import re

with open('day06-input.txt', 'r') as input:
  lines = list(input)
  times = map(int, re.split("\s+", lines[0].split(" ", 1)[1].strip()))
  distances = map(int, re.split("\s+", lines[1].split(" ", 1)[1].strip()))

  total = 1
  for t, d in zip(times, distances):
    n = 0
    for w in range(t):
      if w * (t - w) > d:
        n += 1
    total *= n
  print(total)
