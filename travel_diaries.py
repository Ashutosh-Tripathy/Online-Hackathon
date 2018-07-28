# N, M = map(int, input().split())
# mat = []
# for i in range(N):
#     mat.append([int(x) for x in input().split()])

# ones, twos = [], set()

# for i in range(N):
#     for j in range(M):
#         if mat[i][j] == 1:
#             ones.append((i, j))
#         elif mat[i][j] == 2:
#             twos.add((i, j))
# count = 0
# while len(ones) > 0:
#     while i < len(ones):
#         x, y = ones[i]
#         if len(set([(x+1, y), (x, y+1), (x, y-1), (x-1, y)]).intersection(twos)) > 0:
#             twos.add(ones.pop(0))
#         else:
#             i += 1
#     count += 1

# print(count)


N = int(input())
arr = map(int, input().split())
numCount = {}
for item in arr:
    numCount[item] = numCount.get(item, 0) + 1
sortedNum = list(sorted(numCount.keys()))

t = int(input())

for i in range(t):
    index = sortedNum.index(i) + 1
    count = 0
    while index < len(sortedNum):
        count += numCount[sortedNum[index]]
    print(count)
