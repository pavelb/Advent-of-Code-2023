def applyRule(rule, part):
  if ":" in rule:
    cond, goto = rule.split(":")
    if ">" in cond:
      p, v = cond.split(">")
      return goto if part[p] > int(v) else None
    else:
      p, v = cond.split("<")
      return goto if part[p] < int(v) else None
  else:
    return rule

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

  work = {}
  for workflow in workflows:
    name, rulesStr = workflow.split("{")
    work[name] = rulesStr[:-1].split(",")
  
  def testPart(part):
    workflow = 'in'
    while True:
      for rule in work[workflow]:
        workflow = applyRule(rule, part)
        if workflow == 'A':
          return True
        if workflow == 'R':
          return False
        if workflow is not None:
          break
  
  parts = []
  for partStr in partStrs:
    part = {}
    for prop in partStr[1:-1].split(","):
      p, v = prop.split("=")
      part[p] = int(v)
    parts.append(part)
  
  total = 0
  for part in parts:
    if testPart(part):
      total += sum(part.values())
  print(total)
