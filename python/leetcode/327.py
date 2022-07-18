class Node:
    def __init__(self, start: int, end: int, val: int, left=None, right=None):
        """
        Segment tree node.
        :param start: lower bound of interval
        :param end: upper bound of interval
        :param val: int
        :param left: left child
        :param right: right child
        """
        self.start = start
        self.end = end
        self.val = val
        self.left = left
        self.right = right

    def get_mid(self):
        return (self.start + self.end) // 2


class SegmentTree:
    def __init__(self, n):
        self.N = n
        self.root = self.build(0, self.N - 1)

    def build(self, l: int, r: int):
        if l == r:
            return Node(l, r, 0)
        mid = (l + r) // 2
        left_child = self.build(l, mid)
        right_child = self.build(mid + 1, r)
        val = left_child.val + right_child.val
        return Node(l, r, val, left_child, right_child)

    def _query(self, node: Node, left: int, right: int):
        if left > right:
            return 0

        if node.start == left and node.end == right:
            return node.val

        mid = node.get_mid()
        return self._query(node.left, left, min(mid, right)) + self._query(node.right, max(mid + 1, left), right)

    def query(self, left: int, right: int):
        return self._query(self.root, left, right)

    def _update(self, node: Node, idx: int):
        if node.start == node.end:
            node.val += 1
        else:
            mid = node.get_mid()
            if idx <= mid:
                self._update(node.left, idx)
            else:
                self._update(node.right, idx)
            node.val = node.left.val + node.right.val

    def update(self, idx: int):
        self._update(self.root, idx)


def count_range_sum(self, nums: list[int], lower: int, upper: int) -> int:
    # lower <= tree[j] - x <= upper
    # find x where (tree[j] - upper <= x <= tree[j] - lower)

    n = len(nums)
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + nums[i]

    all_nums = set()
    for x in prefix_sum:
        all_nums.add(x)
        all_nums.add(x - lower)
        all_nums.add(x - upper)

    all_nums = sorted(all_nums)
    ranks = {num: rank for rank, num in enumerate(all_nums)}

    tree = SegmentTree(len(all_nums))
    result = 0
    for x in prefix_sum:
        result += tree.query(ranks[x - upper], ranks[x - lower])
        tree.update(ranks[x])
    return result


class DynamicSegmentTree:
    """
    Segment tree with dynamic node insertion.
    """

    def __init__(self, lo: int, hi: int):
        """
        :param lo: lower bound of all possible values
        :param hi: higher bound of allpossible values
        """
        self.root = Node(lo, hi, 0)

    def _insert(self, node: Node, val: int):
        if node.start == node.end:
            node.val += 1
        else:
            mid = node.get_mid()
            if not node.left:  # TODO: why do we have to place this here?
                node.left = Node(node.start, mid, 0)
            if not node.right:
                node.right = Node(mid + 1, node.end, 0)

            if val <= mid:
                self._insert(node.left, val)
            else:
                self._insert(node.right, val)
            if node.left:
                node.val = node.left.val
            if node.right:
                node.val += node.right.val

    def insert(self, val: int):
        self._insert(self.root, val)

    def _query(self, node: Node, left: int, right: int):
        if not node or left > right:
            return 0

        if node.start == left and node.end == right:
            return node.val

        mid = node.get_mid()
        return self._query(node.left, left, min(mid, right)) + self._query(node.right, max(mid + 1, left), right)

    def query(self, left: int, right: int):
        return self._query(self.root, left, right)


def count_range_sum_1(self, nums: list[int], lower: int, upper: int) -> int:
    n = len(nums)
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + nums[i]

    all_nums = set()
    for x in prefix_sum:
        all_nums.add(x)
        all_nums.add(x - lower)
        all_nums.add(x - upper)

    tree = DynamicSegmentTree(min(all_nums), max(all_nums))
    result = 0
    for x in prefix_sum:
        result += tree.query(x - upper, x - lower)
        tree.insert(x)
    return result
