class RangeSum:
    def __init__(self, nums):
        self.nums = nums
        self.N = len(self.nums)
        self.tree = [0] * self.N * 4  # TODO: [think] why 4n?
        self._build(1, 0, self.N - 1)

    def _build(self, node: int, l: int, r: int):
        if l == r:
            self.tree[node] = self.nums[l]
        else:
            mid = (l + r) // 2
            self._build(node * 2, l, mid)  # left
            self._build(node * 2 + 1, mid + 1, r)  # right
            self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1]

    def _query(self, node: int, tl: int, tr: int, l: int, r: int):
        if l > r:
            return 0

        if tl == l and tr == r:
            return self.tree[node]

        mid = (tl + tr) // 2  # mid of tree interval
        return self._query(node * 2, tl, mid, l, min(mid, r)) + self._query(node * 2 + 1, mid + 1, tr, max(mid + 1, l), r)

    def _update(self, node, tl, tr, idx: int, val: int):
        if tl == tr:
            self.tree[node] = val
        else:
            mid = (tl + tr) // 2
            if idx <= mid:
                # left
                self._update(node * 2, tl, mid, idx, val)
            else:
                self._update(node * 2 + 1, mid + 1, tr, idx, val)
            self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1]

    def query(self, l: int, r: int):
        return self._query(1, 0, self.N - 1, l, r)

    def update(self, idx: int, val: int):
        self._update(1, 0, self.N - 1, idx, val)


class RangeMin:
    def __init__(self, nums):
        self.nums = nums
        self.N = len(nums)
        self.tree = [0] * 4 * self.N
        self._build(1, 0, self.N - 1)

    def _build(self, node: int, tl: int, tr: int):
        if tl == tr:
            self.tree[node] = self.nums[tl]
        else:
            mid = (tl + tr) // 2
            self._build(node * 2, tl, mid)
            self._build(node * 2 + 1, mid + 1, tr)
            self.tree[node] = min(self.tree[node * 2], self.tree[node * 2 + 1])

    def _query(self, node: int, tl: int, tr: int, l: int, r: int):
        if l > r:
            return float('inf')

        if tl == l and tr == r:
            return self.tree[node]

        mid = (tl + tr) // 2
        return min(self._query(node * 2, tl, mid, l, min(mid, r)), self._query(node * 2 + 1, mid + 1, tr, max(mid + 1, l), r))

    def _update(self, node: int, tl: int, tr: int, idx: int, val: int):
        if tl == tr:
            self.tree[node] = val
        else:
            mid = (tl + tr) // 2
            if idx <= mid:
                self._update(node * 2, tl, mid, idx, val)
            else:
                self._update(node * 2 + 1, mid + 1, tr, idx, val)
            self.tree[node] = min(self.tree[node * 2], self.tree[node * 2 + 1])

    def query(self, l: int, r: int):
        return self._query(1, 0, self.N - 1, l, r)

    def update(self, idx: int, val: int):
        self._update(1, 0, self.N - 1, idx, val)


class TreeNode:
    def __init__(self, start: int, end: int, val, left: 'TreeNode' = None, right: 'TreeNode' = None):
        """
        Segment tree node.
        :param start: interval start (inclusive)
        :param end: interval end (inclusive)
        :param val: value store in the node
        :param left: left child
        :param right: right child
        """
        self.start = start
        self.end = end
        self.val = val
        self.left = left
        self.right = right

    def mid(self):
        return (self.start + self.end) // 2


class SegmentTree:
    def __init__(self, nums):
        self.root = self.build(nums, 0, len(nums) - 1)

    def build(self, nums, l, r):
        if l == r:
            return TreeNode(l, r, nums[l])
        else:
            mid = (l + r) // 2
            left_child = self.build(nums, l, mid)
            right_child = self.build(nums, mid + 1, r)
            return TreeNode(l, r, left_child.val + right_child.val, left_child, right_child)

    def update(self, node, idx, val):
        if node.start == node.end:
            node.val = val
        else:
            mid = node.get_mid()
            if idx <= mid:
                self.update(node.left, idx, val)
            else:
                self.update(node.right, idx, val)
            node.val = node.left.val + node.right.val

    def query(self, node, l, r):
        if l > r:
            return 0

        if node.start == l and node.end == r:
            return node.val
        mid = node.get_mid()
        return self.query(node.left, l, min(mid, r)) + self.query(node.right, max(mid + 1, l), r)


if __name__ == '__main__':
    rs = RangeSum([0, 9, 5, 7, 3])
    print(rs.query(4, 4))
    print(rs.query(2, 4))
    print(rs.query(1, 1))
    rs.update(0, 3)
    print(rs.query(0, 1))
    rs.update(1, -3)
    print(rs.query(0, 1))

    rmin = RangeMin([1, 2, -1, 4, 5])
    print(rmin.query(0, 0))
    rmin.update(4, -5)
    print(rmin.query(0, 3))

    st = SegmentTree([9, -8, 7])
    print(st.query(st.root, 0, 2))
    st.update(st.root, 1, 1)
    print(st.query(st.root, 0, 2))
