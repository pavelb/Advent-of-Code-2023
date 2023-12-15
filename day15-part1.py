def hash(str):
  h = 0
  for c in str:
    h += ord(c)
    h *= 17
    h %= 256
  return h

with open('day15-input.txt', 'r') as input:
  strings = "".join(input).replace("\n", "").split(",")
  total = 0
  for s in strings:
    total += hash(s)
  print(total)