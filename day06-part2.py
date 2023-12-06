with open('day06-input.txt', 'r') as input:
  lines = list(input)
  t = int(lines[0].split(" ", 1)[1].replace(' ', ''))
  d = int(lines[1].split(" ", 1)[1].replace(' ', ''))
  w1 = (t - (t*t - 4 * d) ** .5) // 2
  w2 = (t + (t*t - 4 * d) ** .5) // 2
  print(int(w2 - w1))
