from collections import defaultdict
from itertools import count
import math

modules = {}
sources = defaultdict(list)
dests = defaultdict(list)

class Broadcaster(object):
  def __init__(self, name):
    self.type = 'broadcaster'
    self.name = name

  def pulse(self, state, high, source):
    for module in dests[self.name]:
      yield self.name, high, module
  
  def state(self):
    return None

class FlipFlop(object):
  def __init__(self, name):
    self.type = '%'
    self.name = name
  
  def __repr__(self):
    return self.type + self.name

  def pulse(self, state, high, source):
    if high:
      return []
    state[self.name] = not state[self.name]
    high = state[self.name]
    for module in dests[self.name]:
      yield self.name, high, module

class Conjunction(object):
  def __init__(self, name):
    self.type = '&'
    self.name = name
  
  def __repr__(self):
    return self.type + self.name

  def pulse(self, state, high, source):
    s = list(state[self.name])
    s[sources[self.name].index(source)] = high
    state[self.name] = tuple(s)
    high = not all(state[self.name])
    for module in dests[self.name]:
      yield self.name, high, module

def upstream(name):
  mem = set()
  work = [name]
  while work:
    name = work.pop()
    if name not in mem:
      mem.add(name)
      work.extend(sources[name])
  return mem

def getCycle(name, sourceModules, initState):
  state = dict(initState)
  mem = []
  stateToN = {}

  key = tuple((m, state.get(m, ())) for m in sourceModules)
  stateToN[key] = 0
  mem = [(0, 0, False)]

  for n in count(1):
    work = [('button', False, 'broadcaster')]
    good = False
    while work:
      source, high, dest = work.pop(0)
      if source == name and high:
        good = True
      work.extend(modules[dest].pulse(state, high, source))

    key = tuple((m, state.get(m, ())) for m in sourceModules)
    if key in stateToN:
      return stateToN[key], n - stateToN[key], mem
    stateToN[key] = n

    if not mem:
      mem.append((n, n, good))
    else:
      L, H, g = mem[-1]
      if g == good:
        mem[-1] = (L, H + 1, g)
      else:
        mem.append((n, n, good))

with open('day20-input.txt', 'r') as input:
  for line in input:
    a, b = line.rstrip().split(" -> ")
    moduleNames = b.split(", ")
    module = None
    if a == 'broadcaster':
      module = Broadcaster(a)
    elif a[0] == '%':
      module = FlipFlop(a[1:])
    elif a[0] == '&':
      module = Conjunction(a[1:])
    for m in moduleNames:
      dests[module.name].append(m)
      sources[m].append(module.name)
    modules[module.name] = module
  modules['rx'] = Conjunction('rx')

  state = {}
  for module in modules.values():
    if module.type == '&':
      state[module.name] = tuple(False for _ in sources[module.name])
    elif module.type == '%':
      state[module.name] = False
  
  keyOutputs = []
  work = [('rx', True)]
  while work:
    name, high = work.pop(0)
    type = modules[name].type
    if not all(len(dests[m]) == 1 for m in sources[name]):
      keyOutputs.append((name, high))
    elif type == '&':
      if high:
        if len(sources[name]) == 1:
          work.append((sources[name][0], False))
        else:
          keyOutputs.append((name, high))
      else:
        work.extend((m, True) for m in sources[name])
    elif type == '%':
      keyOutputs.append((name, high))

  wtf = []
  for name, high in keyOutputs:
    sourceModules = upstream(name)
    cycleStart, cycleLen, cycle = getCycle(name, sourceModules, dict(state))
    print(cycleStart, cycleLen, cycle)
    wtf.append(cycleLen)  # This makes no sense to do in general
  print(math.lcm(*wtf))  # This makes no sense to do in general