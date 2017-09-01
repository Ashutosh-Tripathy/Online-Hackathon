class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

root = Node(2)
root.right = Node(5)
root.left = Node(7)

root.left.right = Node(6)

root.left.right.left = Node(1)
root.left.right.right = Node(11)

root.right.right = Node(9)
root.right.right.left = Node(4)

def remove_half_node(root):
    while bool(root.left) ^ bool(root.right):
        root = root.left if bool(root.left) else root.right
    parent = root
    queue = [root]
    while len(queue) > 0:
        node = queue[0]
        if bool(node.left or node.right) == False:
            queue.pop(0)
            continue
        if bool(node.left.left) ^ bool(node.left.right):
            node.left = node.left.right if bool(node.left.right) else node.left.left
        if bool(node.right.left) ^ bool(node.right.right):
            node.right = node.right.right if bool(node.right.right) else node.right.left
        if not (bool(node.left.left) ^ bool(node.left.right)) and not(bool(node.right.left) ^ bool(node.right.right)):
            queue.pop(0)
            queue.append(node.left)
            queue.append(node.right)

remove_half_node(root)

print(root)


# square, rect, other = 0, 0, 0
# while True:
#     item = input()
#     try:
#         item = raw_input()
#     except (EOFError):
#         break #end of file reached
    
#     a, b, c, d = [int(x) for x in item.split()]
#     if min(a, b, c, d) <=0:
#         other += 1
#     elif max(a, b, c, d)  == min(a, b, c ,d):
#         square += 1
#     elif a == c and b == d:
#         rect += 1
#     else:
#         other += 1
# print("".join([str(x) for x in [square, rect, other]]))

# search = set(input().split())
# word_count = {}
# def generate_word_count(id, arr):
#     global word_count
#     if id not in word_count:
#         word_count[id] = {}
#     words = word_count[id]
#     for item in arr:
#         item = item.replace(",", "").replace(".","")
#         if item not in words:
#             words[item] = 1
#         else:
#             words[item] += 1


# M = int(input())
# for i in range(M):
#     hotel_id = int(input())
#     generate_word_count(hotel_id, input().split())

# hotel_review = []
# for hotel_id in word_count:
#     matches = 0
#     for item in search:
#         if item in word_count[hotel_id]:
#             matches += word_count[hotel_id][item]
#     hotel_review.append((matches, hotel_id))

# hotel_review.sort()
# hotel_ids = []
# for item in hotel_review:
#     hotel_ids.append(item[1])
# print(" ".join([str(x) for x in hotel_ids]))


# numbers = [int(x) for x in input().split()]
# for i in range(len(numbers) - 1, 0, -1):
#     numbers[i] -= numbers[i - 1]
# print(item.pop(0), end=" ")
# for item in numbers:
#     result = str(item) + " "
#     if abs(item) > 127:
#         result = "-128 " + result
#     print(result, end="")

# X = int(input())
# N = int(input())
# max_counter = 0

# timestamp = []
# for i in range(N):
#     start, end = [int(x) for x in input().split()]
#     timestamp.append((start, end))

# timestamp.sort()

# for i in range(len(timestamp)):
#     start, end = timestamp[i]
#     counter = 1
#     for j in range(i + 1, len(timestamp)):
#         start_j, end_j = timestamp[j]
#         if start_j <= end <= end_j:
#             counter += 1
#         else:
#             break
#     max_counter = max(counter, max_counter)    
# print(max(max_counter - X, 0))        

















