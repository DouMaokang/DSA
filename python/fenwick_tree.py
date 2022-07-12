class FenwickTree:
    def __init__(self, nums):
        self.N = len(nums)
        self.tree = [0] * self.N
        for idx, delta in enumerate(nums):
            self.add(idx, delta)

    def add(self, idx: int, delta):
        while idx < self.N:
            self.tree[idx] += delta
            idx = self._h(idx)

    def get_prefix_sum(self, idx: int):
        """
        Sum of elements in range [0, idx]
        """
        result = 0
        while idx >= 0:
            result += self.tree[idx]
            idx = self._g(idx) - 1
        return result

    def get_range_sum(self, start: int, end: int):
        return self.get_prefix_sum(end) - self.get_prefix_sum(start - 1)

    def _g(self, i: int):
        """
        Get lower bound g(i) of range [g(i), i]. T[i] = sum of A in [g(i), i].
        """
        return i & (i + 1)

    def _h(self, i: int):
        """
        Get upper bound j of the range covered by T[j] that contains element A[i].
        """
        return i | (i + 1)


if __name__ == '__main__':
    nums = [0, 1, 2, 3, 4]
    ft = FenwickTree(nums)
    assert ft.get_prefix_sum(4) == 10
    assert ft.get_prefix_sum(3) == 6
    assert ft.get_prefix_sum(2) == 3
    assert ft.get_prefix_sum(1) == 1
    assert ft.get_prefix_sum(0) == 0

    assert ft.get_range_sum(0, 4) == 10
    assert ft.get_range_sum(1, 4) == 10
    assert ft.get_range_sum(2, 4) == 9
    assert ft.get_range_sum(2, 3) == 5
    assert ft.get_range_sum(4, 4) == 4

    nums = [0, 1, -2, 3, 4]
    ft = FenwickTree(nums)
    assert ft.get_range_sum(0, 4) == 6
    assert ft.get_range_sum(2, 4) == 5
    assert ft.get_range_sum(2, 2) == -2

