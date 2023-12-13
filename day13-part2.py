total = 0
puzzles = []
puzzle = []

def countRows(puzzle):
  rows = 0
  for i in range(1, len(puzzle)):
    n = min(i, len(puzzle) - i)
    top = "".join(puzzle[i - n:i])
    bottom = "".join(reversed(puzzle[i:i + n]))
    if sum(a != b for a, b in zip(top, bottom)) == 1:
      rows += i
  return rows

with open('day13-input.txt', 'r') as input:
  for line in input:
    line = line.rstrip()
    if line:
      puzzle.append(line)
    else:
      puzzles.append(puzzle)
      puzzle = []
  if puzzle:
    puzzles.append(puzzle)

total = 0
for puzzle in puzzles:
  rows = countRows(puzzle)
  puzzle2 = ["".join(row[i] for row in puzzle) for i in range(len(puzzle[0]))]
  cols = countRows(puzzle2)
  total += rows * 100 + cols
print(total)