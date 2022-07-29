# class Node:
#     def __init__(self, start: int, end: int, val: bool, marked: bool = False, left: "Node" = None,
#                  right: "Node" = None):
#         self.start = start
#         self.end = end
#         self.val = val
#         self.marked = marked
#         self.left = left
#         self.right = right
#
#     def get_mid(self):
#         return (self.start + self.end) // 2
#
#
# class SegmentTree:
#     def __init__(self):
#         self.root = Node(1, 4, False)
#
#     def push(self, node: Node):
#
#         if node.marked:
#             if node.start != node.end:
#                 mid = node.get_mid()
#                 if not node.left:
#                     node.left = Node(node.start, mid, False)
#                 if not node.right:
#                     node.right = Node(mid + 1, node.end, False)
#                 node.left.val = node.right.val = node.val
#                 node.left.marked = node.right.marked = True
#             node.marked = False
#
#     def add_range(self, node: Node, l: int, r: int):
#         if l > r:
#             return
#
#         if node.start == l and node.end == r:
#             node.val = True
#             # need to recursively change all child nodes
#             node.marked = True
#         else:
#             mid = node.get_mid()
#             if not node.left:
#                 node.left = Node(node.start, mid, False)
#             if not node.right:
#                 node.right = Node(mid + 1, node.end, False)
#
#             self.push(node)
#             self.add_range(node.left, l, min(r, mid))
#             self.add_range(node.right, max(l, mid + 1), r)
#             node.val = node.left.val and node.right.val
#
#     def remove_range(self, node: Node, l: int, r: int):
#         if l > r:
#             return
#
#         if node.start == l and node.end == r:
#             node.val = False
#             # need to recursively change all child nodes
#             node.marked = True
#         else:
#             mid = node.get_mid()
#             if not node.left:
#                 node.left = Node(node.start, mid, False)
#             if not node.right:
#                 node.right = Node(mid + 1, node.end, False)
#
#             self.push(node)
#             self.remove_range(node.left, l, min(r, mid))
#             self.remove_range(node.right, max(l, mid + 1), r)
#             node.val = node.left.val and node.right.val
#
#     def query(self, node: Node, l: int, r: int):
#         if not node:
#             return False
#
#         if node.start == l and node.end == r:
#             return node.val
#
#         self.push(node)
#         mid = node.get_mid()
#         if r <= mid:
#             return self.query(node.left, l, min(r, mid))
#         elif l > mid:
#             return self.query(node.right, max(l, mid + 1), r)
#         else:
#             return self.query(node.left, l, min(r, mid)) and self.query(node.right, max(l, mid + 1), r)
#

class Node:
    def __init__(self, start: int, end: int, val: bool, marked: bool = False, left: "Node" = None,
                 right: "Node" = None):
        self.start = start
        self.end = end
        self.val = val
        self.marked = marked
        self.left = left
        self.right = right

    def get_mid(self):
        return (self.start + self.end) // 2


class SegmentTree:
    def __init__(self):
        self.root = Node(1, 1 << 9, False)

    def add_range(self, node: Node, l: int, r: int):
        if l > r:
            return

        if node.start == l and node.end == r:
            node.val = True
            node.left = node.right = None
        else:
            mid = node.get_mid()
            if not node.left:
                node.left = Node(node.start, mid, False)
            if not node.right:
                node.right = Node(mid + 1, node.end, False)

            self.add_range(node.left, l, min(r, mid))
            self.add_range(node.right, max(l, mid + 1), r)
            node.val = node.left.val and node.right.val

    def remove_range(self, node: Node, l: int, r: int):
        if l > r:
            return

        if node.start == l and node.end == r:
            node.val = False
            node.left = node.right = None
        else:
            mid = node.get_mid()
            if not node.left:
                node.left = Node(node.start, mid, False)
            if not node.right:
                node.right = Node(mid + 1, node.end, False)

            self.remove_range(node.left, l, min(r, mid))
            self.remove_range(node.right, max(l, mid + 1), r)
            node.val = node.left.val and node.right.val

    def query(self, node: Node, l: int, r: int):
        if l > r:
            return True

        if (node.start == l and node.end == r) or (not node.left and not node.right):
            return node.val

        mid = node.get_mid()
        return self.query(node.left, l, min(r, mid)) and self.query(node.right, max(l, mid + 1), r)


if __name__ == '__main__':
    tree = SegmentTree()
    tree.add_range(tree.root, 1, 4)
    tree.remove_range(tree.root, 2, 3)
    print(tree.query(tree.root, 4, 4))
    print(tree.query(tree.root, 1, 1))

