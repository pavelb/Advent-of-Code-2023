with open('day09-input.txt', 'r') as input:
  total = 0
  for line in input:
    line = line.rstrip()
    nums = list(map(int, line.split(" ")))
    n = 0
    while any(n != 0 for n in nums):
      n += nums[-1]
      nums = [nums[i + 1] - nums[i] for i in range(len(nums) - 1)]
    total += n
  print(total)

