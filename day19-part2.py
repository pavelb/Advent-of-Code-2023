from math import prod
from lib import flattenRanges

def split(range1, range2):
  first = []
  both = []
  second = []
  for (min, max, m) in flattenRanges([[*range1, [True]], [*range2, [False]]]):
    range = (min, max)
    if len(m) == 2:
      both.append(range)
    elif m[0]:
      first.append(range)
    else:
      second.append(range)
  return first, both, second

def simplifyParts(parts):
  for i, part1 in enumerate(parts):
    for j in range(i + 1, len(parts)):
      part2 = parts[j]
      splits = {c: split(part1[c], part2[c]) for c in 'xmas'}
      if all(v[1] for v in splits.values()):
        parts.remove(part1)
        parts.remove(part2)
        inter = {c: v[1][0] for c, v in splits.items()}
        parts.append(inter)
        for c in 'xmas':
          for i, v in enumerate(splits[c]):
            if i != 1 and v:
              part = dict(inter)
              part[c] = v[0]
              parts.append(part)
        return True
  return False

with open('day19-input.txt', 'r') as input:
  workflows = []
  partStrs = []
  seenBlank = False
  for line in input:
    line = line.strip()
    if line == '':
      seenBlank = True
    elif seenBlank:
      partStrs.append(line)
    else:
      workflows.append(line)

  rules = {}
  for workflow in workflows:
    name, rulesStr = workflow.split("{")
    rules[name] = rulesStr[:-1].split(",")

  work = [('in', {'x': (1, 4000), 'm': (1, 4000), 'a': (1, 4000), 's': (1, 4000)})]
  parts = []
  while work:
    workflow, part = work.pop()
    if workflow == 'A':
      parts.append(part)
      continue
    if workflow == 'R':
      continue
    for rule in rules[workflow]:
      if ":" in rule:
        cond, goto = rule.split(":")
        if ">" in cond:
          p, v = cond.split(">")
          v = int(v)
          min, max = part[p]

          if v + 1 <= max:
            partYes = dict(part)
            partYes[p] = (v + 1, max)
            work.append((goto, partYes))
          
          if min <= v:
            part[p] = (min, v)
          else:
            break
        else:
          p, v = cond.split("<")
          v = int(v)
          min, max = part[p]

          if min <= v - 1:
            partYes = dict(part)
            partYes[p] = (min, v - 1)
            work.append((goto, partYes))

          if v <= max:
            part[p] = (v, max)
          else:
            break
      else:
        work.append((rule, part))
  
  while simplifyParts(parts):
    continue

  total = 0
  for part in parts:
    total += prod((max - min + 1) for (min, max) in part.values())
  print(total)
