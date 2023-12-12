def satisfy(condition, springs):
  if len(condition) < sum(springs):
    return 0

  out = 0
  if condition[0] != '#':
    out += satisfy(condition[1:], springs)
  n = springs[0]
  if '.' not in condition[:n]:
    if len(springs) == 1:
      out += 1 if '#' not in condition[n:] else 0
    elif len(condition) > n and condition[n] != '#':
      out += satisfy(condition[n + 1:], springs[1:])
  return out

with open('day12-input.txt', 'r') as input:
  total = 0
  for line in input:
    line = line.rstrip()
    condition, springs = line.split(" ")
    springs = tuple(map(int, springs.split(",")))
    total += satisfy(condition, springs)
  print(total)
