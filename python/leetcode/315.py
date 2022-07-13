class FenwickTree:
    """
    Standard Fenwick Tree.
    """

    def __init__(self, n: int):
        """
        Initialize an empty tree of size n.
        """
        self.N = n
        self.tree = [0] * n

    def add(self, idx: int, delta: int):
        while idx < self.N:
            self.tree[idx] += delta
            idx = (idx | (idx + 1))

    def query(self, idx: int):
        result = 0
        while idx >= 0:
            result += self.tree[idx]
            idx = (idx & (idx + 1)) - 1
        return result

    def query_range(self, left: int, right: int):
        return self.query(right) - self.query(left - 1)


def count_smaller(nums: list):
    # discretization
    sorted_unique_nums = sorted(set(nums))
    ranks = {num: rank for rank, num in enumerate(sorted_unique_nums)}

    # use Fenwick Tree to efficiently query the count of smaller numbers on the right
    fenwick_tree = FenwickTree(len(sorted_unique_nums))

    # we process the array from right to left
    # for each number, add 1 to Fenwick Tree at index idx where idx is the rank of the current number
    # tree.query(idx - 1) is the count of smaller numbers added so far (i.e. to the right of the current number)
    n = len(nums)
    result = [0] * n
    for i in range(n - 1, -1, -1):
        rank = ranks[nums[i]]
        result[i] = fenwick_tree.query(rank - 1)
        fenwick_tree.add(rank, 1)
    return result


def count_larger(nums: list):
    sorted_unique_nums = sorted(set(nums))
    ranks = {num: rank for rank, num in enumerate(sorted_unique_nums)}

    fenwick_tree = FenwickTree(len(sorted_unique_nums))
    n = len(nums)
    result = [0] * n
    for i in range(n - 1, -1, -1):
        rank = ranks[nums[i]]
        result[i] = fenwick_tree.query_range(rank + 1, fenwick_tree.N - 1)
        fenwick_tree.add(rank, 1)
    return result


if __name__ == '__main__':
    nums = [5, 2, 6, 6]
    print(count_smaller(nums))
    print(count_larger(nums))
