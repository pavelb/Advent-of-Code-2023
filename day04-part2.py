import re
from functools import cache

mem = []
with open('day04-input.txt', 'r') as input:
  for line in input:
    line = line.rstrip()
    name, card = line.split(": ")
    _, cardNumber = re.split(r'\s+', name)
    winning, have = card.split(" | ")
    winning = re.split(r'\s+', winning.strip())
    have = re.split(r'\s+', have.strip())
    num = sum(1 for h in have if h in winning)
    mem.append(num)

@cache
def total(i):
  if i >= len(mem):
    return 0
  num = mem[i]
  return 1 + sum(total(i + 1 + j) for j in range(num))

print(sum(total(i) for i in range(len(mem))))