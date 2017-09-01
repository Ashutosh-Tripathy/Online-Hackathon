class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


root = Node(10)
root.right = Node(15)
root.left = Node(5)

root.left.right = Node(8)
root.left.left = Node(1)

root.right.right = Node(20)
root.right.left = Node(12)

def get_kth_smallest_element(node, k):
    queue = []
    counter = 0
    while node is not None:
        queue.append(node)
        node = node.left

    while len(queue) > 0:
        node = queue.pop()
        counter += 1
        if counter == k:
            print(node.value)
            break
        if node.right:
            node = node.right
            while node is not None:
                queue.append(node)
                node = node.left        

get_kth_smallest_element(root, 4)