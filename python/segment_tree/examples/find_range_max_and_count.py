"""
Finding the maximum and the number of times it appears in [l, r]
"""

from segment_tree.segment_tree import TreeNode


class SegmentTree:
    def __init__(self, nums):
        self.nums = nums
        self.N = len(nums)
        self.root = self.build(0, self.N - 1)

    def build(self, l: int, r: int):
        if l == r:
            return TreeNode(l, r, {'val': float('-inf'), 'count': 0})
        else:
            mid = (l + r) // 2
            left_child = self.build()
