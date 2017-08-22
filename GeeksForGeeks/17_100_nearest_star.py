num = [5,2,6,8,10,16, 18,11,19]
from heapq import *
q = []

for item in num:
    heappush(q, item)

for i in range(5):
    print(heappop(num))