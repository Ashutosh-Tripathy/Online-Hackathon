class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


root = Node(10)
root.right = Node(6)
root.left = Node(-2)

root.left.right = Node(-4)
root.left.left = Node(8)

root.right.right = Node(5)
root.right.left = Node(7)

def convert_into_sumtree(node):
    # temp1, temp2 = 0, 0
    # if node.left is None and node.right is None:
    #     return 0        
    
    # if node.left is not None:
    #     temp1 = node.left.value
    #     node.left.value = convert_into_sumtree(node.left)

    # if node.right is not None:
    #     temp2 = node.right.value
    #     node.right.value = convert_into_sumtree(node.right)
    #     # sum += temp
    # return node.left.value + node.right.value + temp1 + temp2
    if node is None:
        return 0
    temp = node.value
    node.value = convert_into_sumtree(node.left) + convert_into_sumtree(node.right)
    return node.value + temp

convert_into_sumtree(root)