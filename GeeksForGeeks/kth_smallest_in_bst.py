def inorder_traversel(item):
    stack = [node]
    counter = 0
    left_node = stack.left
    while left_node
        stack.append(left_node)
        left_node = left_node.left


    while stack:
        node = stack.pop(-1)
        counter += 1
        if counter == K: return node
        right_node = node.right
        while right_node:
            stack.append(right_node)
            right_node = right_node.left
