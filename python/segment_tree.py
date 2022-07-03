class RangeSum:
    def __init__(self, nums):
        self.nums = nums
        self.N = len(self.nums)
        self.tree = [0] * self.N * 4
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

        mid = (tl + tr) // 2
        return self._query(node * 2, tl, mid, l, min(mid, r)) + self._query(node * 2 + 1, mid + 1, tr, max(mid + 1, l), r)

    def query(self, l: int, r: int):
        return self._query(1, 0, self.N - 1, l, r)


if __name__ == '__main__':
    rs = RangeSum([1, 2, 3, 4, 5])
    print(rs.query(0, 4))
