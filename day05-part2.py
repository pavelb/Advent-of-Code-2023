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
      destFirst, sourceFirst, rangeLength = map(int, line.split(" "))
      maps[-1].append((
        sourceFirst,
        sourceFirst + rangeLength - 1,
        destFirst - sourceFirst
      ))

  def translate(first, last, i):
    if first > last:
      return
    if i >= len(maps):
      yield (first, last)
      return
    
    for sourceFirst, sourceLast, delta in sorted(maps[i]):
      # [source] [range]
      if sourceLast < first:
        continue
      # [range] [source]
      if sourceFirst > last:
        yield from translate(first, last, i + 1)
        return
      # [range [sou]rce] or [range [source]]
      if sourceFirst > first:
        yield from translate(first, sourceFirst - 1, i + 1)
        first = sourceFirst
      # [source [range]]
      if sourceLast >= last:
        yield from translate(first + delta, last + delta, i + 1)
        return
      # [source [ran]ge]
      yield from translate(first + delta, sourceLast + delta, i + 1)
      first = sourceLast + 1
    
    # translate remaining range
    yield from translate(first, last, i + 1)

  _, seeds = lines[0].split(": ")
  seeds = list(map(int, seeds.split(" ")))
  smallest = float('inf')
  for seedFirst, seedLength in zip(seeds[::2], seeds[1::2]):
    for first, last in translate(seedFirst, seedFirst + seedLength - 1, 0):
      smallest = min(smallest, first)
  print(smallest)
