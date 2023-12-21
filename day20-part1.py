from collections import defaultdict

class Dummy(object):
  name = 'dummy'
  def pulse(self, high, source):
    return []

modules = defaultdict(Dummy)
sources = defaultdict(list)

class Broadcaster(object):
  def __init__(self, name, modules):
    self.name = name
    self.modules = modules

  def pulse(self, high, source):
    for module in self.modules:
      yield self.name, high, module

class FlipFlop(object):
  def __init__(self, name, modules):
    self.name = name
    self.on = False
    self.modules = modules

  def pulse(self, high, source):
    if high:
      return []
    self.on = not self.on
    high = self.on
    for module in self.modules:
      yield self.name, high, module

class Conjunction(object):
  def __init__(self, name, modules):
    self.name = name
    self.mem = defaultdict(bool)
    self.modules = modules

  def pulse(self, high, source):
    self.mem[source] = high
    high = not all(self.mem[module] for module in sources[self.name])
    for module in self.modules:
      yield self.name, high, module

with open('day20-input.txt', 'r') as input:
  for line in input:
    a, b = line.rstrip().split(" -> ")
    moduleNames = b.split(", ")
    module = None
    if a == 'broadcaster':
      module = Broadcaster(a, moduleNames)
    elif a[0] == '%':
      module = FlipFlop(a[1:], moduleNames)
    elif a[0] == '&':
      module = Conjunction(a[1:], moduleNames)
    for m in moduleNames:
      sources[m].append(module.name)
    modules[module.name] = module
  
  count = [0, 0]
  for _ in range(1000):
    work = [('button', False, 'broadcaster')]
    while work:
      source, high, dest = work.pop(0)
      # print(source + ' -' + ('high' if high else 'low') + '-> ' + dest)
      count[high] += 1
      work.extend(modules[dest].pulse(high, source))
  print(count[0] * count[1])