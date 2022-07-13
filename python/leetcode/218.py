class Node:
    def __init__(self, start: int, end: int, val, left=None, right=None):
        """
        Segment tree node.
        :param start: lower bound of interval
        :param end: upper bound of interval
        :param val:
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
        val = max(left_child.val, right_child.val)
        return Node(l, r, val, left_child, right_child)

    def _query(self, node: Node, left: int, right: int):
        if left > right:
            return 0

        if node.start == left and node.end == right:
            return node.val

        mid = node.get_mid()
        return max(
            self._query(node.left, left, min(mid, right)),
            self._query(node.right, max(mid + 1, left), right)
        )

    def query(self, left: int, right: int):
        return self._query(self.root, left, right)

    def _update(self, node: Node, idx: int, val: int):
        if node.start == node.end:
            # only update if the new val is greater
            node.val = max(node.val, val)
        else:
            mid = node.get_mid()
            if idx <= mid:
                self._update(node.left, idx, val)
            else:
                self._update(node.right, idx, val)
            node.val = max(node.left.val, node.right.val)

    def update(self, idx: int, val: int):
        self._update(self.root, idx, val)

    def update_range(self, left: int, right: int, val: int):
        for i in range(left, right + 1):
            self.update(i, val)


def test_segment_tree():
    tree = SegmentTree(10)
    tree.update_range(0, 4, 1)
    assert tree.query(0, 0) == 1
    tree.update_range(2, 5, -1)
    assert tree.query(2, 2) == 1
    assert tree.query(2, 4) == 1
    tree.update_range(3, 6, 2)
    assert tree.query(2, 2) == 1
    assert tree.query(2, 4) == 2


def get_skyline(buildings: list[list]):
    points = []
    for building in buildings:
        points.append(building[0])
        points.append(building[1])

    sorted_unique_points = sorted(set(points))
    ranks = {val: rank for rank, val in enumerate(sorted_unique_points)}
    tree = SegmentTree(len(sorted_unique_points))

    for building in buildings:
        left, right, val = ranks[building[0]], ranks[building[1]], building[2]
        tree.update_range(left, right - 1, val)

    result = []
    for i in range(len(sorted_unique_points) - 1):
        result.append([sorted_unique_points[i], tree.query(i, i + 1)])

    print(result)


if __name__ == '__main__':
    test_segment_tree()
    get_skyline([[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]])
