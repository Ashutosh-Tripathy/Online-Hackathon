class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None

def inorder(root):
    stack = [root]
    while stack[0].left:
        stack.insert(0, stack[0].left)
    result = []
    while len(stack) > 0:
        right = stack[0].right
        result.append(stack.pop(0).data)
        if right:
            stack.insert(0, right)
    return result

def is_tree_identical(root1, root2):
    list1, list2 = inorder(root1), inorder(root2)
    result = True if list1 == list2 else False
    return result
    # while len(list1) > 0:
    #     item1 = list1.pop(0)
    #     item2 = list2.pop(0)
    #     if item or item1.data != item2.data:
    #         return False

    #     if item1.left:
    #         list1.append(item1.left)
    #     if item2.left:
    #         list2.append(item2.left)
    #     if item1.right:
    #         list1.append(item1.right)
    #     if item2.right:
    #         list2.append(item2.right)

    # if len(list2) > 0:
    #     return False
    # return True


root1 = Node(1)
root2 = Node(1)

root1.left = Node(2)
root2.left = Node(2)

root1.left.left = Node(3)
root2.left.left = Node(3)

root1.right = Node(4)
root2.right = Node(5)

message = "Same" if is_tree_identical(root1, root2) else "Not same"
print(message)