import re

total = 0
with open('day04-input.txt', 'r') as input:
  for line in input:
    line = line.rstrip()
    _, card = line.split(": ")
    winning, have = card.split(" | ")
    winning = re.split(r'\s+', winning.strip())
    have = re.split(r'\s+', have.strip())
    num = sum(1 for h in have if h in winning)
    if num > 0:
      total += pow(2, num - 1)
           
print(total)