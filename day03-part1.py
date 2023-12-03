import re

DIGIT = {'.': True}
for n in range(10):
  DIGIT[str(n)] = True

total = 0
with open('day03-input.txt', 'r') as input:
  lines = list(line.rstrip() for line in input)
  for i, line in enumerate(lines):
    for m in re.finditer(r'\d+', line):
      touchingSymbol = False
      for j in range(max(0, i - 1), min(len(lines), i + 2)):
        checkLine = lines[j]
        for k in range(max(0, m.start() - 1), min(len(line), m.end() + 1)):
          if checkLine[k] not in DIGIT:
            touchingSymbol = True
      if touchingSymbol:
        total += int(m.group())
print(total)