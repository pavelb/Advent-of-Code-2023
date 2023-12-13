def countRows(puzzle):
  rows = 0
  for i in range(1, len(puzzle)):
    n = min(i, len(puzzle) - i)
    top = "".join(puzzle[i - n:i])
    bottom = "".join(reversed(puzzle[i:i + n]))
    if top == bottom:
      rows += i
  return rows

with open('day13-input.txt', 'r') as input:
  puzzles = [s.split("\n") for s in "".join(input).split("\n\n")]
  total = 0
  for puzzle in puzzles:
    rows = countRows(puzzle)
    puzzle2 = ["".join(row[i] for row in puzzle) for i in range(len(puzzle[0]))]
    cols = countRows(puzzle2)
    total += rows * 100 + cols
  print(total)