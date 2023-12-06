from lib import flattenRanges, mergeRanges

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
      dest, start, n = map(int, line.split(" "))
      maps[-1].append((start, start + n - 1, [(MAP, dest - start)]))

  _, seeds = lines[0].split(": ")
  seeds = list(map(int, seeds.split(" ")))
  sources = [(start, start + n - 1, [(SOURCE, 0)]) for start, n in zip(seeds[::2], seeds[1::2])]

  for map in maps:
    newSources = []
    for start, end, metadata in flattenRanges(map + sources):
      output = False
      for type, delta in metadata:
        if type == SOURCE:
          output = True
        elif type == MAP:
          start += delta
          end += delta
      if output:
        newSources.append((start, end, [(SOURCE, 0)]))
    sources = mergeRanges(newSources, lambda m1, m2: m1[2] if m1[2] == m2[2] else None)
  
  print(sources[0][0])
