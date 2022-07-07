from segment_tree.segment_tree import TreeNode


class SegmentTree:
    def __init__(self, nums):
        self.nums = nums
        self.N = len(nums)
        self.root = self.build(0, self.N - 1)

    def build(self, l, r):
        if l == r:
            return TreeNode(l, r, self.nums[l])
        else:
            mid = (l + r) // 2
            left_child = self.build(l, mid)
            right_child = self.build(mid + 1, r)
            return TreeNode(l, r, max(left_child.val, right_child.val), left_child, right_child)

    def _update(self, node: TreeNode, idx, val):
        if node.start == node.end:
            node.val = val
        else:
            mid = node.mid()
            if idx <= mid:
                self._update(node.left, idx, val)
            else:
                self._update(node.right, idx, val)
            node.val = max(node.left.val, node.right.val)

    def update(self, idx: int, val):
        self._update(self.root, idx, val)

    def _query(self, node: TreeNode, l: int, r: int):
        if l > r:
            return float('-inf')

        if node.start == l and node.end == r:
            return node.val

        mid = node.mid()
        return max(self._query(node.left, l, min(r, mid)),
                   self._query(node.right, max(l, mid + 1), r))

    def query(self, l: int, r: int):
        return self._query(self.root, l, r)


if __name__ == '__main__':
    nums = [1, 8, 4, 6, -2, 6, 2]
    st = SegmentTree(nums)
    assert st.query(0, 6) == 8
    assert st.query(0, 4) == 8
    assert st.query(2, 6) == 6
    assert st.query(4, 4) == -2
    st.update(1, -5)
    assert st.query(0, 6) == 6
    assert st.query(1, 2) == 4
