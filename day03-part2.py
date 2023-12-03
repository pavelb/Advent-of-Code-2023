import re
from collections import defaultdict

mem = defaultdict(list)
with open('day03-input.txt', 'r') as input:
  lines = list(line.rstrip() for line in input)
  for i, line in enumerate(lines):
    for m in re.finditer(r'\d+', line):
      touchingSymbol = False
      for j in range(max(0, i - 1), min(len(lines), i + 2)):
        checkLine = lines[j]
        for k in range(max(0, m.start() - 1), min(len(line), m.end() + 1)):
          if checkLine[k] == '*':
            mem[(j, k)].append(int(m.group()))

total = 0
for nums in mem.values():
  if len(nums) == 2:
    total += nums[0] * nums[1]
print(total)