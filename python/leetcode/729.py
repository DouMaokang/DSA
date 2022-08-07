"""
Segment tree model: dynamic, range update, range query, lazy propagation.
"""

class Node:
    def __init__(self, start: int, end: int, val: bool, left: 'Node' = None, right: 'Node' = None, delta: bool = False):
        self.start = start
        self.end = end
        self.val = val
        self.delta = delta
        self.left = left
        self.right = right

    def mid(self):
        return (self.start + self.end) // 2

class SegmentTree:
    def __init__(self, start, end):
        self.root = Node(start, end, False)

    def _push(self, node: Node):
        # create left and right child nodes
        mid = node.mid()
        if not node.left:
            node.left = Node(node.start, mid, False)
        if not node.right:
            node.right = Node(mid + 1, node.end, False)

        if node.delta:
            # must update child node val and delta
            node.left.val = node.right.val = node.val
            node.left.delta = node.right.delta = node.delta
            node.delta = False

    def add(self, node: Node, l: int, r: int):
        if l <= node.start and node.end <= r:
            # add delta to all elements in the range
            node.val = True
            node.delta = True
        else:
            self._push(node)
            mid = node.mid()
            if l <= mid:
                self.add(node.left, l, r)
            if r > mid:
                self.add(node.right, l, r)
            # update parent, interval cannot be booked if any child interval is booked
            node.val = node.left.val or node.right.val

    def query(self, node: Node, l: int, r: int):
        if l <= node.start and node.end <= r:
            return node.val
        self._push(node)
        mid = node.mid()
        result = False
        if l <= mid:
            result = self.query(node.left, l, r)
        if r > mid:
            result = result or self.query(node.right, l, r)
        return result