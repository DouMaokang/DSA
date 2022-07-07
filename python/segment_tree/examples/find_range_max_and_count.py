"""
Finding the maximum and the number of times it appears in [l, r]
"""

from segment_tree.segment_tree import TreeNode


class SegmentTree:
    _MIN_VALUE = {'max': float('-inf'), 'count': 0}

    def __init__(self, nums):
        self.nums = nums
        self.N = len(nums)
        self.root = self.build(0, self.N - 1)

    def _compare(self, a, b):
        val = {}
        if a['max'] > b['max']:
            val = a
        elif a['max'] < b['max']:
            val = b
        else:
            val['max'] = a['max']
            val['count'] = a['count'] + b['count']
        return val

    def build(self, l: int, r: int):
        if l == r:
            return TreeNode(l, r, {'max': self.nums[l], 'count': 1})
        else:
            mid = (l + r) // 2
            left_child = self.build(l, mid)
            right_child = self.build(mid + 1, r)
            val = self._compare(left_child.val, right_child.val)
            return TreeNode(l, r, val, left_child, right_child)

    def _query(self, node: TreeNode, l: int, r: int):
        if l > r:
            return self._MIN_VALUE
        if node.start == l and node.end == r:
            return node.val

        mid = node.mid()
        return self._compare(self._query(node.left, l, min(mid, r)),
                             self._query(node.right, max(mid + 1, l), r))

    def query(self, l: int, r: int):
        return self._query(self.root, l, r)


    def _update(self, node: TreeNode, idx: int, val):
        if node.start == node.end:
            node.val['max'] = val
        else:
            mid = node.mid()
            if idx <= mid:
                self._update(node.left, idx, val)
            else:
                self._update(node.right, idx, val)
            node.val = self._compare(node.left.val, node.right.val)

    def update(self, idx: int, val):
        self._update(self.root, idx, val)


if __name__ == "__main__":
    nums = [1, 1, 2, 8, 6, 4, 4, 8, 8]
    st = SegmentTree(nums)
    assert st.query(0, 8) == {'max': 8, 'count': 3}
    assert st.query(0, 7) == {'max': 8, 'count': 2}
    assert st.query(0, 6) == {'max': 8, 'count': 1}
    assert st.query(0, 1) == {'max': 1, 'count': 2}
    assert st.query(5, 6) == {'max': 4, 'count': 2}