import re
from collections import defaultdict

def hash(str):
  h = 0
  for c in str:
    h += ord(c)
    h *= 17
    h %= 256
  return h

with open('day15-input.txt', 'r') as input:
  strings = "".join(input).replace("\n", "").split(",")
  mem = defaultdict(list)
  for s in strings:
    add = '=' in s
    operation = s.split('=' if add else '-')
    label, focal = operation
    hashmap = mem[hash(label)]

    if add:
      added = False
      for i, (l, f) in enumerate(hashmap):
        if l == label:
          hashmap[i] = (label, focal)
          added = True
          break
      if not added:
        hashmap.append((label, focal))
    else:
      for i, entry in enumerate(hashmap):
        if entry[0] == label:
          hashmap.remove(entry)

  total = 0
  for box, hashmap in mem.items():
    for i, (label, focal) in enumerate(hashmap):
      total += (1 + box) * (1 + i) * int(focal)

  print(total)