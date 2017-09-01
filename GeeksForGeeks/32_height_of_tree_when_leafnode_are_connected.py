class Node:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None



root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right.left = Node(4)
root.right.right = Node(5)
root.right.right.right = Node(6)

# root.right.right.right.left = root.right.left
# root.right.right.right.right = root.left

# root.right.left.right = root.right.right.right
# root.right.left.left = root.left

# root.left.left = root.right.right.right
# root.left.right = rroot.right.left




path = [root]
max_height = 0
leaf_linkedlist = set()

while len(path) > 0:
	max_height = max(max_height, len(path))
	node = path[-1]
	if node.left or node.right:
		while node.left:
			node = node.left
			path.append(node)
		if node.right:
			path.append(node.right)
	else:
		path.pop(-1)


# while True:
# 	node = path[-1].left:
# 	if not node or node in leaf_linkedlist:
# 		break
#  	if node in path:
#  		path.index(node)
#  		leaf_linkedlist.update(path[index:])
#  		path = path[:index + 1]
#  	else :
#  		path.append(node.left)
# max_height = max(max_height, len(path))

# while len(path) > 0:
# 	if path[-1] is not in leaf_linkedlist:
# 		if path[]





