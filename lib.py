class Node(object):
  value = None
  left = None
  right = None
  def __init__(self, value):
    self.value = value

def Add(node, range):
  rangeStart, rangeEnd, rangeMetadata = range
  if rangeStart > rangeEnd:
    return node
  if not node:
    return Node(range)
  start, end, metadata = node.value

  if rangeEnd < start:
    node.left = Add(node.left, range)
    return node
  if rangeStart > end:
    node.right = Add(node.right, range)
    return node

  if rangeStart < start:
    node.left = Add(node.left, (rangeStart, start - 1, rangeMetadata))
    if rangeEnd < end:
      node.value = (start, rangeEnd, metadata + rangeMetadata)
      node.right = Add(node.right, (rangeEnd + 1, end, metadata))
    else:
      node.value = (start, end, metadata + rangeMetadata)
      node.right = Add(node.right, (end + 1, rangeEnd, rangeMetadata))
  else:
    node.left = Add(node.left, (start, rangeStart - 1, metadata))
    if rangeEnd < end:
      node.value = (rangeStart, rangeEnd, metadata + rangeMetadata)
      node.right = Add(node.right, (rangeEnd + 1, end, metadata))
    else:
      node.value = (rangeStart, end, metadata + rangeMetadata)
      node.right = Add(node.right, (end + 1, rangeEnd, rangeMetadata))

  return node

def Walk(node):
  if node.left:
    yield from Walk(node.left)
  yield node.value
  if node.right:
    yield from Walk(node.right)

# takes list of possibly-overlapping (start, end, list-of-metadata)
# returns sorted list of non-overlapping (start, end, list-of-metadata)
#   with overlaps as separate ranges unioning the metadata of overlapping ranges
def flattenRanges(ranges):
  head = None
  for range in ranges:
    head = Add(head, range)
  yield from Walk(head)
