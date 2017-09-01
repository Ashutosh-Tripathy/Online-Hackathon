class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
node = Node(1)
node.next = Node(2)
node.next.next = Node(3)
node.next.next.next = Node(4)
node.next.next.next.next = Node(5)
node.next.next.next.next.next = Node(6)
node.next.next.next.next.next.next = Node(7)
node.next.next.next.next.next.next.next = Node(8)

def print_list(node):
    while True:
        if node is None:
            break
        print(node.value)
        node = node.next
temp = node
print_list(temp)

def reverse_list_by_size(head, size):
    current = head
    next, prev = None, None
    count = 0
    while current is not None and count < size:
        next = current.next
        current.next = prev
        prev = current
        current = next
        count += 1
    if next is not None:
        head.next = reverse_list_by_size(next, size)
    return prev
    
    
    

def reverse_list(node):
    result = None
    while node:
        temp = node.next
        node.next = result
        result = node
        node = temp
    return result



# node = reverse_list(node)
node = reverse_list_by_size(node, 3)
print_list(node)