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
  mem = defaultdict(dict)
  for s in strings:
    add = '=' in s
    label, focal = s.split('=' if add else '-')
    hashmap = mem[hash(label)]
    if add:
      hashmap[label] = focal
    else:
      hashmap.pop(label, None)

  total = 0
  for box, hashmap in mem.items():
    for i, (label, focal) in enumerate(hashmap.items()):
      total += (1 + box) * (1 + i) * int(focal)
  print(total)