import re
from collections import defaultdict

maps = []
with open('day05-input.txt', 'r') as input:
  lines = [line.rstrip() for line in input]

  for line in lines:
    if len(line) == 0:
      pass
    elif ":" in line:
      maps.append([])
    else:
      destRangeStart, sourceRangeStart, rangeLength = line.split(" ")
      maps[-1].append((int(sourceRangeStart), int(destRangeStart), int(rangeLength)))
  
  _, seeds = lines[0].split(": ")
  locs = []
  for seed in seeds.split(" "):
    source = int(seed)
    for ranges in maps:
      for sourceRangeStart, destRangeStart, rangeLength in sorted(ranges):
        offset = source - sourceRangeStart
        if 0 <= offset < rangeLength:
          source = destRangeStart + offset
          break
    locs.append(source)

  print(min(locs))
