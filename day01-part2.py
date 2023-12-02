import re

MAP = {
  '1': 1,
  '2': 2,
  '3': 3,
  '4': 4,
  '5': 5,
  '6': 6,
  '7': 7,
  '8': 8,
  '9': 9,
  'one': 1,
  'two': 2,
  'three': 3,
  'four': 4,
  'five': 5,
  'six': 6,
  'seven': 7,
  'eight': 8,
  'nine': 9,
}
RE = '|'.join(MAP.keys())

total = 0
with open('day01-input.txt', 'r') as input:
  for line in input:
    first = re.search(RE, line).group(0)
    last = re.search(RE[::-1], line[::-1]).group(0)[::-1]
    total += MAP[first] * 10 + MAP[last]
print(total)