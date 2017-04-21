class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

#             25
#         15              35
#     10     20       30          45
# 5     12  17 21    28 33   40       50

root = Node(25)
root.left = Node(15)
root.right = Node(35)

root.left.left = Node(10)
root.left.right = Node(20)

root.left.left.left = Node(5)
root.left.left.right = Node(12)

root.left.right.left = Node(17)
root.left.right.right = Node(21)

root.right.left = Node(30)
root.right.right = Node(45)

root.right.left.left = Node(28)
root.right.left.right = Node(33)

root.right.right.left = Node(40)
root.right.right.right = Node(50)


def get_top_view(node):
    stack = [node]

    while node.left:
        stack.append(node.left)
        node = node.left

    while len(stack) != 1:
        print(stack.pop(-1).value)

    node = stack.pop(-1)
    print(node.value)

    while node.right:
        print(node.right.value)
        node = node.right

get_top_view(root)









