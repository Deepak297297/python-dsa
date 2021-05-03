
class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def find_depth(root):
    d = 0 
    while root:
        d += 1
        root = root.left
    return d


def check_perfect(root, d, level=0):
    if not root:
        return True

    if root.left is None and root.right is None:
        return d == (level + 1)

    if root.left is None or root.right is None:
        return False

    return check_perfect(root.left, d, level+1) and check_perfect(root.right, d, level+1)


def is_perfect(root):
    d = find_depth(root)
    return check_perfect(root, d)
