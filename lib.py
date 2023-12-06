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
