from lib import flattenRanges

MAP = 0
SOURCE = 1

with open('day05-input.txt', 'r') as input:
  lines = [line.rstrip() for line in input]
  maps = []
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
        [(MAP, destFirst - sourceFirst)]
      ))

  _, seeds = lines[0].split(": ")
  seeds = list(map(int, seeds.split(" ")))
  sources = [(seedFirst, seedFirst + seedLength - 1, [(SOURCE, 0)]) for seedFirst, seedLength in zip(seeds[::2], seeds[1::2])]

  smallest = float('inf')
  for map in maps:
    ranges = flattenRanges(map + sources)
    sources = []
    for start, end, metadata in ranges:
      output = False
      for type, delta in metadata:
        if type == SOURCE:
          output = True
        elif type == MAP:
          start += delta
          end += delta
      if output:
        sources.append((start, end, [(SOURCE, 0)]))
    sources = sorted(sources)
  print(sources[0][0])
