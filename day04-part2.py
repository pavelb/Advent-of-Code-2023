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

count = [0] * len(mem)
for i in reversed(range(len(mem))):
  num = mem[i]
  count[i] = 1 + sum(count[i + 1: i + 1 + num])
print(sum(count))