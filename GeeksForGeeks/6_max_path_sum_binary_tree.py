class Node():
    """docstring for Node"""
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

node = Node(10)
node.left = Node(2)
node.right = Node(10)

node.left.left = Node(20)
node.left.right = Node(1)

node.right.right = Node(-25)
node.right.right.left = Node(3)
node.right.right.right = Node(4)

max_path = -float('inf')
def max_path_sum(node):
    global max_path
    if not node:
        return -float('inf')
    value = node.val
    left = max_path_sum(node.left) + value
    right = max_path_sum(node.right) + value
    cmax = max(value, left, right)
    max_path = max(max_path, cmax, left + right - value)
    return cmax

max_path_sum(node)
print(max_path)