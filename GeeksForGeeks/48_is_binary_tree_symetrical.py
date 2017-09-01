class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


root = Node(10)

root.left = Node(5)
root.right = Node(5)

root.left.left = Node(1)
root.left.right = Node(8)

root.right.left = Node(8)
# root.right.right = Node(1)


def is_tree_symetrical(node1, node2):
    queue1 = [node1]
    queue2 = [node2]

    while True:
        if len(queue1) != len(queue2):
            return False
        if len(queue1) == 0:
            return True
        item1, item2 = queue1.pop(0), queue2.pop(0)
        if item1.value != item2.value:
            return False
        if item1.left is not None:
            queue1.append(item1.left)
        if item2.right is not None:
            queue2.append(item2.right)
        if item1.right is not None:
            queue1.append(item1.right)
        if item2.left is not None:
            queue2.append(item2.left)
        
        


print(is_tree_symetrical(root.left, root.right))
