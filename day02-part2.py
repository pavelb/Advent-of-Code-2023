import re
from collections import defaultdict

# r12, g13, b14

total = 0
with open('day02-input.txt', 'r') as input:
  for line in input:
    line = line.rstrip()
    game, line = line.split(": ", 1)
    _, id = game.split(" ")
    mem = defaultdict(int)
    for round in line.split('; '):
      for cube in round.split(', '):
          num, color = cube.split(' ')
          mem[color] = max(int(num), mem[color])
    total += mem['red'] * mem['green'] * mem['blue']
print(total)