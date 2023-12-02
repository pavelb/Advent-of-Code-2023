import re

total = 0
with open('day01-input.txt', 'r') as input:
  for line in input:
        line = line.rstrip()
        m = re.findall('(\d)', line)
        value = int(m[0] + m[-1])
        total += value
print(total)