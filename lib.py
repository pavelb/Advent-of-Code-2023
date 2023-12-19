import heapq

class Node(object):
  value = None
  left = None
  right = None
  def __init__(self, value):
    self.value = value
  def values(self):
    if self.left:
      yield from self.left.values()
    yield self.value
    if self.right:
      yield from self.right.values()

# range = (start, end, list-of-metadata)
def AddRange(node, range):
  rangeStart, rangeEnd, rangeMetadata = range
  if rangeStart > rangeEnd:
    return node
  if not node:
    return Node(range)
  start, end, metadata = node.value

  if rangeEnd < start:
    node.left = AddRange(node.left, range)
    return node
  if rangeStart > end:
    node.right = AddRange(node.right, range)
    return node

  if rangeStart < start:
    node.left = AddRange(node.left, (rangeStart, start - 1, rangeMetadata))
    if rangeEnd < end:
      node.value = (start, rangeEnd, metadata + rangeMetadata)
      node.right = AddRange(node.right, (rangeEnd + 1, end, metadata))
    else:
      node.value = (start, end, metadata + rangeMetadata)
      node.right = AddRange(node.right, (end + 1, rangeEnd, rangeMetadata))
  else:
    node.left = AddRange(node.left, (start, rangeStart - 1, metadata))
    if rangeEnd < end:
      node.value = (rangeStart, rangeEnd, metadata + rangeMetadata)
      node.right = AddRange(node.right, (rangeEnd + 1, end, metadata))
    else:
      node.value = (rangeStart, end, metadata + rangeMetadata)
      node.right = AddRange(node.right, (end + 1, rangeEnd, rangeMetadata))

  return node

# takes list of possibly-overlapping (start, end, list-of-metadata)
# returns sorted list of non-overlapping (start, end, list-of-metadata)
#   with overlaps as separate ranges unioning the metadata of overlapping ranges
def flattenRanges(ranges):
  head = None
  for range in ranges:
    head = AddRange(head, range)
  yield from head.values()

# takes list of possibly-overlapping (start, end, list-of-metadata)
#   and a function that returns list-of-metadata for merge-eligible ranges
# returns sorted list of merged non-overlapping (start, end, list-of-metadata)
#   where the merge function returned some metadata.
def mergeRanges(ranges, meta=None):
  ranges = sorted(ranges)
  i = 0
  while i < len(ranges) - 1:
    start1, end1, metadata1 = ranges[i]
    start2, end2, metadata2 = ranges[i + 1]
    if end1 + 1 == start2:
      m = meta(ranges[i], ranges[i + 1]) if meta else True
      if m:
        ranges.pop(i)
        ranges[i] = (start1, end2, m)
        continue
    i += 1
  return ranges

class PriorityQueue:
  def __init__(self):
    self.heap = []
    self.entry_finder = {}

  def update(self, item, priority):
    self.remove(item)
    entry = [priority, item, False]
    self.entry_finder[item] = entry
    heapq.heappush(self.heap, entry)

  def remove(self, item):
    if item in self.entry_finder:
      entry = self.entry_finder.pop(item)
      entry[-1] = True

  def pop(self):
    while self.heap:
      entry = heapq.heappop(self.heap)
      priority, item, deleted = entry
      if not deleted:
        return item
    return None