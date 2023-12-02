import re
from collections import defaultdict

# r12, g13, b14

total = 0
with open('day02-input.txt', 'r') as input:
  for line in input:
    line = line.rstrip()
    game, line = line.split(": ", 1)
    _, id = game.split(" ")
    impossible = False
    for round in line.split('; '):
      mem = defaultdict(int)
      for cube in round.split(', '):
          num, color = cube.split(' ')
          mem[color] += int(num)
      if mem['red'] > 12 or mem['green'] > 13 or mem['blue'] > 14:
         impossible = True
    if not impossible:
      total += int(id)
print(total)