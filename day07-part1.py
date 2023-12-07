from collections import defaultdict

MAP = {
  '2': 2,
  '3': 3,
  '4': 4,
  '5': 5,
  '6': 6,
  '7': 7,
  '8': 8,
  '9': 9,
  'T': 10,
  'J': 11,
  'Q': 12,
  'K': 13,
  'A': 14,
}

with open('day07-input.txt', 'r') as input:
  hands = []
  for line in input:
    hand, bid = line.rstrip().split(" ")
    hand = [MAP[c] for c in hand]
    mem = defaultdict(int)
    for n in hand:
      mem[n] += 1
    numMatches = defaultdict(int)
    for v in mem.values():
      numMatches[v] += 1
    key = (numMatches[5], numMatches[4], numMatches[3], numMatches[2])
    
    hands.append((key, hand, int(bid)))
  hands = sorted(hands)

  print(sum((i + 1) * bid for i, (_, _, bid) in enumerate(hands)))
